#!/usr/bin/env python3
"""Regression proof for the Daybreak factual repair and promoted bone recast."""

from __future__ import annotations

import datetime as dt
import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import america
import build_daybreak_frames as frame_builder
import daybreak_engine as engine


VAULT = Path(
    os.environ.get(
        "F250_DAYBREAK_VAULT_ROOT",
        "Chronicle/",
    )
)


class AmericaInterpolationTests(unittest.TestCase):
    def setUp(self):
        self.old_cache = america.CACHE

    def tearDown(self):
        america.CACHE = self.old_cache
        america.reset_cache_for_tests()

    def _fixture(self, rows: dict[str, float]) -> tempfile.TemporaryDirectory:
        folder = tempfile.TemporaryDirectory()
        path = Path(folder.name) / "america_ephemeris.json"
        path.write_text(json.dumps({"916 America": rows}), encoding="utf-8")
        america.CACHE = path
        america.reset_cache_for_tests()
        return folder

    def test_retrograde_uses_shortest_signed_arc(self):
        with self._fixture({"2026-03-20": 137.2, "2026-03-21": 137.0}):
            noon = dt.datetime(2026, 3, 20, 12, tzinfo=dt.timezone.utc)
            self.assertAlmostEqual(america.america_lon(noon), 137.1, places=9)
            self.assertAlmostEqual(america.america_speed(noon), -0.2, places=9)

    def test_true_wrap_uses_shortest_signed_arc(self):
        with self._fixture({"2026-01-01": 359.8, "2026-01-02": 0.2}):
            noon = dt.datetime(2026, 1, 1, 12, tzinfo=dt.timezone.utc)
            self.assertAlmostEqual(america.america_lon(noon), 0.0, places=9)
            self.assertAlmostEqual(america.america_speed(noon), 0.4, places=9)

    def test_human_position_rounds_across_sign_boundary(self):
        with self._fixture({"2026-01-01": 29.9999, "2026-01-02": 30.0}):
            start = dt.datetime(2026, 1, 1, tzinfo=dt.timezone.utc)
            self.assertEqual(america.america_pos(start), "0°00' Taurus")

    def test_missing_bracket_fails_closed(self):
        with self._fixture({"2026-01-01": 10.0}):
            # Compatibility contract: the shared reader returns None; the
            # chart engine converts an unresolved mandatory point into a hard
            # build failure.
            self.assertIsNone(
                america.america_lon(dt.datetime(2026, 1, 2, 12, tzinfo=dt.timezone.utc))
            )

    def test_implausible_motion_fails_closed(self):
        with self._fixture({"2026-01-01": 10.0, "2026-01-02": 20.0}):
            self.assertIsNone(
                america.america_lon(dt.datetime(2026, 1, 1, 12, tzinfo=dt.timezone.utc))
            )

    def test_unaffected_direct_motion_keeps_live_whole_second_precision(self):
        with self._fixture({"2026-01-01": 10.0, "2026-01-02": 10.4}):
            a = dt.datetime(2026, 1, 1, 12, 0, 0, 1, tzinfo=dt.timezone.utc)
            b = dt.datetime(2026, 1, 1, 12, 0, 0, 999999, tzinfo=dt.timezone.utc)
            self.assertEqual(america.america_lon(a), america.america_lon(b))

    def test_mandatory_engine_path_fails_closed_on_missing_bracket(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            cache = root / "99 - Templates" / "america_ephemeris.json"
            cache.parent.mkdir(parents=True)
            cache.write_text(
                json.dumps({"916 America": {"2026-01-01": 10.0}}), encoding="utf-8"
            )
            engine._america_rows.cache_clear()
            with self.assertRaisesRegex(ValueError, "bracketing"):
                engine._canonical_america(
                    dt.datetime(2026, 1, 1, 12, tzinfo=dt.timezone.utc), root
                )
            engine._america_rows.cache_clear()


class CanonicalAriesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.charts, cls.chart_index = engine._chart_registry(VAULT)

    def test_every_aries_day_has_plausible_canonical_america_motion(self):
        day = dt.date(2026, 3, 20)
        end = dt.date(2026, 6, 20)
        prior_lon = None
        while day <= end:
            chart = engine.cast_daybreak(day.isoformat(), vault_root=VAULT)
            america_row = chart["positions"]["America"]
            self.assertLessEqual(abs(america_row["spd"]), 1.0, day.isoformat())
            self.assertEqual(america_row["authority"], "america_ephemeris.json")
            if prior_lon is not None:
                motion = abs(((america_row["lon"] - prior_lon + 180) % 360) - 180)
                self.assertLessEqual(motion, 1.0, day.isoformat())
            prior_lon = america_row["lon"]
            day += dt.timedelta(days=1)

    def test_recast_parent_targets_match_canonical_america(self):
        expected = {
            "ingress-2026-aries": 137.2117822998993,
            "lun-2026-01-03-fu": 152.9232962791875,
            "lun-2026-01-18-ne": 150.80201948467246,
            "lun-2026-02-01-fu": 147.57621945307292,
            "lun-2026-02-17-ne-solar": 143.38725616922224,
            "lun-2026-03-03-fu-lunar": 139.97328652452083,
            "lun-2026-03-19-ne": 137.38179414624884,
            "lun-2026-04-02-fu": 136.45706075388657,
        }
        for chart_id, expected_lon in expected.items():
            summary = engine._chart_summary(VAULT, self.chart_index[chart_id])
            self.assertTrue(summary["america"]["stored_bone_matches_canonical"], chart_id)
            self.assertEqual(summary["targets"]["America"], summary["america"]["lon"])
            self.assertAlmostEqual(summary["america"]["lon"], expected_lon, places=9)
            self.assertLess(summary["america"]["stored_bone_delta_deg"], 0.001)

    def test_later_parent_target_remains_canonical(self):
        summary = engine._chart_summary(VAULT, self.chart_index["lun-2026-04-17-ne"])
        self.assertTrue(summary["america"]["stored_bone_matches_canonical"])
        self.assertLess(summary["america"]["stored_bone_delta_deg"], 0.001)


class ExactHierarchyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.charts, _ = engine._chart_registry(VAULT)

    def _context(self, value: str):
        return engine.resolve_context_at(dt.datetime.fromisoformat(value), self.charts, vault_root=VAULT)

    def test_aries_ingress_changes_only_at_exact_time(self):
        before = self._context("2026-03-20T14:45:57.733395+00:00")
        at = self._context("2026-03-20T14:45:57.733396+00:00")
        self.assertEqual(before["ingress_id"], "ingress-2025-capricorn")
        self.assertEqual(at["ingress_id"], "ingress-2026-aries")

    def test_june_new_moon_is_june_14_local_split(self):
        payload = engine.build_payload(
            dt.date(2026, 6, 14), dt.date(2026, 6, 14),
            vault_root=VAULT,
            generated_at=dt.datetime(2026, 8, 15, tzinfo=dt.timezone.utc),
        )
        frame = payload["frames"]["2026-06-14"]
        self.assertEqual(len(frame["hierarchy_segments"]), 2)
        transition = frame["parent_transitions"][0]
        self.assertEqual(transition["chart_id"], "lun-2026-06-15-ne")
        self.assertTrue(transition["at_local"].startswith("2026-06-14T22:54:10.466913-04:00"))
        self.assertEqual(
            frame["hierarchy_segments"][1]["hierarchy"]["chapter_id"],
            "lun-2026-06-15-ne",
        )

    def test_all_known_aries_split_frames(self):
        expected = {
            "2026-03-20": "ingress-2026-aries",
            "2026-04-17": "lun-2026-04-17-ne",
            "2026-05-01": "lun-2026-05-01-fu",
            "2026-05-16": "lun-2026-05-16-ne",
            "2026-06-14": "lun-2026-06-15-ne",
            "2026-06-20": "ingress-2026-cancer",
        }
        for date_iso, chart_id in expected.items():
            payload = engine.build_payload(
                dt.date.fromisoformat(date_iso), dt.date.fromisoformat(date_iso),
                vault_root=VAULT,
                generated_at=dt.datetime(2026, 8, 15, tzinfo=dt.timezone.utc),
            )
            frame = payload["frames"][date_iso]
            self.assertIn(chart_id, [row["chart_id"] for row in frame["parent_transitions"]])
            self.assertEqual(len(frame["hierarchy_segments"]), 2)

    def test_every_registered_event_in_coverage_is_routed_to_its_exact_frame(self):
        start = dt.date(2026, 3, 20)
        end = dt.date(2026, 6, 20)
        payload = engine.build_payload(
            start, end, vault_root=VAULT,
            generated_at=dt.datetime(2026, 8, 15, tzinfo=dt.timezone.utc),
        )
        actual = {
            row["chart_id"]: (date_iso, row["at_utc"], row["at_local"])
            for date_iso, frame in payload["frames"].items()
            for row in frame["parent_transitions"]
        }
        coverage_start = dt.datetime.fromisoformat(
            payload["frames"][start.isoformat()]["chart"]["sunrise"]["utc"]
        )
        coverage_end = dt.datetime.fromisoformat(
            payload["frames"][end.isoformat()]["chart"]["sunrise"]["next_utc"]
        )
        expected = {}
        for meta in self.charts:
            if meta["type"] not in {"ingress", "lunation"}:
                continue
            stamp = engine._chart_timestamp(VAULT, meta)
            if coverage_start < stamp < coverage_end:
                expected[meta["id"]] = stamp.isoformat(timespec="microseconds")
        self.assertEqual(set(actual), set(expected))
        for chart_id, stamp in expected.items():
            self.assertEqual(actual[chart_id][1], stamp)
        self.assertEqual(actual["lun-2026-04-02-fu"][0], "2026-04-01")
        self.assertEqual(actual["lun-2026-05-31-fu"][0], "2026-05-30")
        self.assertEqual(actual["lun-2026-06-15-ne"][0], "2026-06-14")


class PayloadContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = engine.build_payload(
            dt.date(2026, 3, 20), dt.date(2026, 6, 20),
            vault_root=VAULT,
            generated_at=dt.datetime(2026, 8, 15, tzinfo=dt.timezone.utc),
        )

    def test_stable_geometry_ids_and_delta_lane(self):
        for frame in self.payload["frames"].values():
            self.assertIn("daily_delta", frame)
            self.assertIn("none", frame["daily_delta"])
            self.assertIn("no_trigger", frame["daily_delta"])
            self.assertTrue(all("geometry_id" in row for row in frame["chart"]["aspects"]))
            self.assertTrue(all("segment_id" in row for row in frame["hierarchy_segments"]))
            self.assertTrue(all("geometry_id" in row for row in frame["long_clocks"]["active_edges"]))
            self.assertTrue(all("geometry_id" in row for row in frame["long_clocks"]["seed_echoes"]))
            for segment in frame["hierarchy_segments"]:
                for rows in segment["contacts"].values():
                    self.assertTrue(all("geometry_id" in row for row in rows))

    def test_slow_continuity_never_becomes_daily_trigger(self):
        for frame in self.payload["frames"].values():
            ids = set()
            for segment in frame["hierarchy_segments"]:
                classification = segment["contact_classification"]
                for role in classification["roles"].values():
                    ids.update(role["background_contact_ids"])
                for role, rows in segment["contacts"].items():
                    for row in rows:
                        if row["continuity"]:
                            self.assertIn(row["geometry_id"], ids, role)

    def test_same_body_slow_or_america_conjunction_never_enters_trigger_lane(self):
        protected = {"Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "America"}
        for frame in self.payload["frames"].values():
            for segment in frame["hierarchy_segments"]:
                trigger_ids = {
                    identifier
                    for role in segment["contact_classification"]["roles"].values()
                    for identifier in role["trigger_contact_ids"]
                }
                for rows in segment["contacts"].values():
                    for row in rows:
                        if (
                            row["source"] == row["target"]
                            and row["source"] in protected
                            and row["aspect_id"] == "conjunction"
                        ):
                            self.assertTrue(row["continuity"])
                            self.assertNotIn(row["reference_id"], trigger_ids)

    def test_sun_asc_parent_mirrors_are_one_reference_family(self):
        found = 0
        for frame in self.payload["frames"].values():
            for segment in frame["hierarchy_segments"]:
                trigger_ids = [
                    identifier
                    for role in segment["contact_classification"]["roles"].values()
                    for identifier in role["trigger_contact_ids"]
                ]
                mirrors = {}
                for rows in segment["contacts"].values():
                    for row in rows:
                        if row["structural_mirror"]:
                            mirrors.setdefault(row["mirror_family_id"], []).append(row)
                for family_id, rows in mirrors.items():
                    found += 1
                    self.assertEqual({row["source"] for row in rows}, {"Sun", "ASC"})
                    self.assertEqual(sum(row["independent_occurrence"] for row in rows), 1)
                    self.assertTrue(all(row["reference_id"] == family_id for row in rows))
                    self.assertLessEqual(trigger_ids.count(family_id), 1)
                    self.assertIn(family_id, self.payload["geometry_index"])
        self.assertGreater(found, 0)

    def test_contact_reference_families_are_classified_once(self):
        mirror_count = 0
        for frame in self.payload["frames"].values():
            for segment in frame["hierarchy_segments"]:
                for role, rows in segment["contacts"].items():
                    lanes = segment["contact_classification"]["roles"][role]
                    trigger = set(lanes["trigger_contact_ids"])
                    background = set(lanes["background_contact_ids"])
                    self.assertTrue(trigger.isdisjoint(background), (frame["date"], role))
                    expected = {row["reference_id"] for row in rows}
                    self.assertEqual(trigger | background, expected, (frame["date"], role))
                    for family_id in {
                        row["mirror_family_id"] for row in rows if row["structural_mirror"]
                    }:
                        mirror_count += 1
                        self.assertEqual(int(family_id in trigger) + int(family_id in background), 1)
        self.assertGreater(mirror_count, 0)

    def test_sun_asc_seed_echo_mirrors_are_one_reference_family(self):
        found = 0
        for frame in self.payload["frames"].values():
            mirrors = {}
            for row in frame["long_clocks"]["seed_echoes"]:
                if row["structural_mirror"]:
                    mirrors.setdefault(row["mirror_family_id"], []).append(row)
            for family_id, rows in mirrors.items():
                found += 1
                self.assertEqual({row["point"] for row in rows}, {"Sun", "ASC"})
                self.assertEqual(sum(row["independent_occurrence"] for row in rows), 1)
                self.assertTrue(all(row["reference_id"] == family_id for row in rows))
                self.assertIn(family_id, self.payload["geometry_index"])
        self.assertGreater(found, 0)

    def test_start_context_is_backward_compatible_segment_zero(self):
        for frame in self.payload["frames"].values():
            first = frame["hierarchy_segments"][0]
            self.assertEqual(frame["hierarchy"], first["hierarchy"])
            self.assertEqual(frame["contacts"], first["contacts"])

    def test_frozen_prospective_baseline_is_preserved_as_history(self):
        """The Aug 15 prospective freeze is an immutable historical record.

        2026-09-25 ephemeris correction (DR-080): the live engine moved from the
        Moshier fallback to the vendored JPL DE441 Swiss files and the Long Clock
        registry was reseated, so a fresh recomputation no longer reproduces the
        frozen per-frame hashes byte-for-byte. The freeze is therefore checked for
        its own integrity (file hash, cohort, dates) and for date coverage by the
        corrected engine; it is never rewritten. The pre-correction engine that
        reproduces it exactly is preserved in
        _Holding/ephemeris-fix-2026-09-25/pre-fix-snapshot.tar.gz.
        """
        import hashlib
        frozen_path = VAULT / "03 - Astrology" / "daybreak_prospective_baseline.json"
        self.assertEqual(
            hashlib.sha256(frozen_path.read_bytes()).hexdigest(),
            "2893a4b3dd0a5dcbfdc46e156842ef517d152c229475d2bd244029291a4301d9",
        )
        frozen = json.loads(frozen_path.read_text(encoding="utf-8"))
        self.assertEqual(frozen["status"], "frozen")
        self.assertEqual(len(frozen["frames"]), 30)
        current = engine.build_payload(
            dt.date(2026, 8, 16), dt.date(2026, 9, 14),
            vault_root=VAULT,
            generated_at=dt.datetime(2026, 8, 15, 16, tzinfo=dt.timezone.utc),
        )
        self.assertEqual(sorted(current["frames"]), sorted(frozen["frames"]))


class MaterializerReceiptTests(unittest.TestCase):
    def _run(self, output: Path, *, explicit: str | None = None) -> dt.datetime | None:
        captured: dict[str, dt.datetime | None] = {}

        def fake_build(start, end, **kwargs):
            captured["generated_at"] = kwargs.get("generated_at")
            stamp = kwargs.get("generated_at") or dt.datetime(2026, 8, 15, 23, tzinfo=dt.timezone.utc)
            return {
                "schema": frame_builder.SCHEMA,
                "generated_at": stamp.isoformat(),
                "coverage": {"start": start.isoformat(), "end": end.isoformat(), "frame_count": 1},
                "frames": {},
            }

        argv = ["build_daybreak_frames.py", "--start", "2026-01-01", "--end", "2026-01-01",
                "--output", str(output)]
        if explicit:
            argv.extend(["--generated-at", explicit])
        with mock.patch.object(sys, "argv", argv), \
                mock.patch.object(frame_builder.engine, "build_payload", side_effect=fake_build), \
                contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(frame_builder.main(), 0)
        return captured["generated_at"]

    def test_default_rebuild_preserves_existing_reviewed_receipt(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "daybreak_frames.json"
            preserved = "2026-08-16T00:00:00+00:00"
            frame_builder._write_atomic(output, {
                "schema": frame_builder.SCHEMA,
                "generated_at": preserved,
                "coverage": {"start": "2026-01-01", "end": "2026-01-01", "frame_count": 1},
                "frames": {},
            })
            before = output.read_bytes()
            self.assertIsNone(self._run(output))
            self.assertEqual(output.read_bytes(), before)

    def test_changed_fact_uses_new_candidate_receipt(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "daybreak_frames.json"
            frame_builder._write_atomic(output, {
                "schema": frame_builder.SCHEMA,
                "generated_at": "2026-08-16T00:00:00+00:00",
                "coverage": {"start": "2026-01-01", "end": "2026-01-01", "frame_count": 1},
                "frames": {"changed": True},
            })
            self.assertIsNone(self._run(output))
            rebuilt = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(rebuilt["generated_at"], "2026-08-15T23:00:00+00:00")
            self.assertEqual(rebuilt["frames"], {})

    def test_explicit_generated_at_overrides_existing_receipt(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "daybreak_frames.json"
            frame_builder._write_atomic(output, {
                "schema": frame_builder.SCHEMA,
                "generated_at": "2026-08-16T00:00:00+00:00",
                "coverage": {"start": "2026-01-01", "end": "2026-01-01", "frame_count": 1},
                "frames": {},
            })
            override = "2026-08-17T12:30:00+00:00"
            self.assertEqual(self._run(output, explicit=override), dt.datetime.fromisoformat(override))
            rebuilt = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(rebuilt["generated_at"], override)

    def test_first_build_without_output_delegates_now_to_engine(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "daybreak_frames.json"
            self.assertIsNone(self._run(output))


if __name__ == "__main__":
    unittest.main(verbosity=2)
