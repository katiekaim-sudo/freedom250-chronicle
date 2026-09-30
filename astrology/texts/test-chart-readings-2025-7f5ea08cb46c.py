#!/usr/bin/env python3
"""Invariant tests for the 2025 retrospective shelf (DR-084) and the detriment table (DR-082)."""

from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
VAULT = HERE.parent
ASTRO = VAULT / "03 - Astrology"
REGISTRY = ASTRO / "chart_reading_registry_2025.json"
BONES = HERE / "chart_reading_bones_2025"
STACKS = HERE / "chart_synodic_stacks_2025.json"


class Retrospective2025ShelfTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        cls.index = json.loads((BONES / "index.json").read_text(encoding="utf-8"))

    def test_shelf_inventory(self) -> None:
        kinds = [row["kind"] for row in self.registry["readings"]]
        self.assertEqual(kinds.count("pass1"), 29)
        self.assertEqual(kinds.count("census"), 4)
        self.assertEqual(kinds.count("comparison"), 4)
        self.assertEqual(self.registry["comparison_contract"]["expected_shelf_count"], 37)
        self.assertEqual(len(self.index["charts"]), 29)

    def test_every_chart_reading_has_a_bone_and_a_stack(self) -> None:
        pass1 = {row["id"] for row in self.registry["readings"] if row["kind"] == "pass1"}
        bones = {row["id"] for row in self.index["charts"]}
        stacks = {row["chart_id"] for row in json.loads(STACKS.read_text(encoding="utf-8"))["charts"]}
        self.assertEqual(pass1, bones)
        self.assertEqual(bones, stacks)
        for chart_id in bones:
            self.assertTrue((BONES / f"{chart_id}.json").is_file(), chart_id)

    def test_seasons_and_eclipses(self) -> None:
        seasons = {}
        for row in self.index["charts"]:
            seasons.setdefault(row["season"], []).append(row["id"])
        self.assertEqual(sorted(seasons), ["2025-aries", "2025-cancer", "2025-libra", "2025-winter"])
        self.assertEqual({k: len(v) for k, v in seasons.items()},
                         {"2025-winter": 7, "2025-aries": 7, "2025-cancer": 8, "2025-libra": 7})
        eclipses = sorted(row["id"] for row in self.index["charts"] if row.get("eclipse"))
        self.assertEqual(eclipses, ["lun-2025-03-14-fu-lunar", "lun-2025-03-29-ne-solar",
                                    "lun-2025-09-07-fu-lunar", "lun-2025-09-21-ne-solar"])

    def test_frozen_baselines_hold(self) -> None:
        contract = self.registry["comparison_contract"]
        covered = []
        for baseline in contract["baselines"]:
            self.assertTrue(baseline["immutable"])
            self.assertEqual(baseline["mode"], "retrospective_calibration")
            rows = []
            for component in baseline["components"]:
                raw = (ASTRO / component["artifact"]).read_bytes()
                self.assertEqual(hashlib.sha256(raw).hexdigest(), component["sha256"])
                rows.append(f"{component['reading_id']}:{component['sha256']}\n")
                covered.append(component["reading_id"])
            aggregate = hashlib.sha256("".join(rows).encode("utf-8")).hexdigest()
            self.assertEqual(aggregate, baseline["aggregate_sha256"])
        self.assertEqual(sorted(covered), sorted(row["id"] for row in self.index["charts"]))

    def test_comparisons_are_closed_retrospective_and_unscored(self) -> None:
        for comparison in self.registry["comparison_contract"]["comparisons"]:
            self.assertEqual(comparison["mode"], "retrospective_calibration")
            self.assertEqual(comparison["state"], "closed")
            evidence = json.loads((ASTRO / comparison["evidence_map"]).read_text(encoding="utf-8"))
            self.assertFalse(evidence["boundary"]["forecast_credit_allowed"])
            self.assertFalse(evidence["method"]["scores_allowed"])
            for finding in evidence["findings"]:
                for item in finding["evidence"]:
                    self.assertIn(item["lane"], {"Attention", "Official", "Entity"})

    def test_known_chart_facts(self) -> None:
        aries = json.loads((BONES / "ingress-2025-aries.json").read_text(encoding="utf-8"))
        self.assertEqual(aries["asc_sign"], "Aquarius")
        self.assertEqual(aries["root_members"], ["Moon", "Mercury", "Mars", "Jupiter"])
        self.assertIn("detriment", aries["pos"]["Jupiter"]["cond"])  # DR-082
        cap = json.loads((BONES / "ingress-2024-capricorn.json").read_text(encoding="utf-8"))
        self.assertEqual(cap["asc_sign"], "Scorpio")
        self.assertEqual(cap["root_members"], ["Mercury", "Jupiter"])
        self.assertIn("detriment", cap["pos"]["Mercury"]["cond"])
        eclipse = json.loads((BONES / "lun-2025-09-21-ne-solar.json").read_text(encoding="utf-8"))
        self.assertEqual(eclipse["eclipse_detail"]["saros"], 154)


class DetrimentTableTests(unittest.TestCase):
    def test_engine_tags_both_detriments(self) -> None:
        import sys
        sys.path.insert(0, str(HERE))
        import mundane_engine as me
        pairs = {"Mercury": {"Sagittarius", "Pisces"}, "Venus": {"Scorpio", "Aries"},
                 "Mars": {"Libra", "Taurus"}, "Jupiter": {"Gemini", "Virgo"},
                 "Saturn": {"Cancer", "Leo"}, "Sun": {"Aquarius"}, "Moon": {"Capricorn"}}
        for planet, signs in pairs.items():
            self.assertEqual(set(me.DETRI[planet]), signs, planet)
            for sign in signs:
                self.assertIn("detriment", me.condition(planet, sign, False))

    def test_2026_bones_carry_the_correction(self) -> None:
        bone = json.loads((HERE / "chart_reading_bones" / "lun-2026-09-26-fu.json").read_text(encoding="utf-8"))
        self.assertIn("detriment", bone["pos"]["Venus"]["cond"])
        for path in (HERE / "chart_reading_bones").glob("*-*.json"):
            data = json.loads(path.read_text(encoding="utf-8"))
            for planet, body in data["pos"].items():
                if (planet, body["sign"]) in {("Venus", "Scorpio"), ("Mercury", "Sagittarius"),
                                              ("Jupiter", "Gemini"), ("Mars", "Libra"),
                                              ("Saturn", "Cancer")}:
                    self.assertIn("detriment", body["cond"], f"{path.name} {planet}")


class AmendmentLedgerTests(unittest.TestCase):
    """DR-085: corrections go in the ledger; sealed readings stay byte-identical to their watches."""

    def test_watched_readings_match_their_frozen_hash(self) -> None:
        registry = json.loads((ASTRO / "chart_reading_registry.json").read_text(encoding="utf-8"))
        source = {row["id"]: row["source"] for row in registry["readings"]}
        watches = json.loads((ASTRO / "chart_transition_watches.json").read_text(encoding="utf-8"))
        for watch in watches["watches"]:
            path = VAULT / source[watch["reading_id"]]
            live = hashlib.sha256(path.read_bytes()).hexdigest()
            self.assertEqual(live, watch["baseline_sha256"], watch["reading_id"])

    def test_no_amendment_inside_a_reading(self) -> None:
        for path in ASTRO.glob("*— A Reading.md"):
            self.assertNotIn("## Amendment —", path.read_text(encoding="utf-8"), path.name)

    def test_ledger_covers_every_dr082_chart(self) -> None:
        import re
        ledger = (ASTRO / "Chart Reading Amendments — Ledger.md").read_text(encoding="utf-8")
        ids = set(re.findall(r'<!-- amendment reading_id="([^"]+)" rule="DR-082"', ledger))
        # the signs the old one-per-planet table dropped and DR-082 restored
        added = {("Venus", "Scorpio"), ("Mercury", "Sagittarius"), ("Jupiter", "Gemini"),
                 ("Mars", "Libra"), ("Saturn", "Cancer")}
        registry = json.loads((ASTRO / "chart_reading_registry.json").read_text(encoding="utf-8"))
        expected = set()
        for row in registry["readings"]:
            if row["kind"] != "pass1":
                continue
            bone = json.loads((HERE / "chart_reading_bones" / f"{row['id']}.json").read_text(encoding="utf-8"))
            if any((pl, body["sign"]) in added for pl, body in bone["pos"].items()):
                expected.add(row["id"])
        self.assertEqual(ids, expected)


if __name__ == "__main__":
    unittest.main()
