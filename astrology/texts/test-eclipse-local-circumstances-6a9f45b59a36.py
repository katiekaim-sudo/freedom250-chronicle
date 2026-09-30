#!/usr/bin/env python3
"""Invariant tests for the Washington-local 2024-2026 eclipse layer."""

from __future__ import annotations

import json
import unittest
from datetime import datetime
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = HERE / "eclipse_local_circumstances.json"


def parse(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


class EclipseLocalCircumstancesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(DATA.read_text(encoding="utf-8"))
        cls.events = {event["date"]: event for event in cls.payload["events"]}

    def test_complete_ordered_nine_event_sequence(self) -> None:
        self.assertEqual(
            [event["date"] for event in self.payload["events"]],
            [
                "2024-10-02",
                "2025-03-14",
                "2025-03-29",
                "2025-09-07",
                "2025-09-21",
                "2026-02-17",
                "2026-03-03",
                "2026-08-12",
                "2026-08-28",
            ],
        )

    def test_libra_seed_path_and_washington_visibility_stay_separate(self) -> None:
        seed = self.events["2024-10-02"]
        self.assertEqual(seed["global"]["type"], "annular")
        self.assertFalse(seed["washington"]["visible"])
        self.assertEqual(seed["washington"]["local_type"], "none")
        self.assertGreater(seed["washington"]["sun_true_altitude_at_syzygy_deg"], 30)

    def test_horizon_threshold_events_remain_distinct(self) -> None:
        aries_seed = self.events["2025-03-29"]["washington"]
        self.assertEqual(aries_seed["status"], "visible_at_sunrise")
        self.assertLess(aries_seed["sun_true_altitude_at_syzygy_deg"], 0)
        self.assertLess(aries_seed["observable_minutes"], 3)
        self.assertLess(aries_seed["obscuration_at_observable_maximum"], 0.02)

        virgo_reveal = self.events["2026-03-03"]
        self.assertEqual(virgo_reveal["washington"]["status"], "sets_during_eclipse")
        self.assertLess(virgo_reveal["washington"]["moon_true_altitude_at_syzygy_deg"], 0)
        moonset = parse(virgo_reveal["washington"]["moonset_during_eclipse"]["utc"])
        syzygy = parse(virgo_reveal["global"]["syzygy"]["utc"])
        self.assertLess(moonset, syzygy)
        self.assertGreater(virgo_reveal["washington"]["total_phase"]["minutes_above_horizon"], 30)

    def test_path_and_horizon_are_not_collapsed(self) -> None:
        september = self.events["2025-09-21"]["washington"]
        self.assertFalse(september["visible"])
        self.assertGreater(september["sun_true_altitude_at_global_max_deg"], 30)

        february = self.events["2026-02-17"]["washington"]
        self.assertFalse(february["visible"])
        self.assertLess(abs(february["sun_true_altitude_at_syzygy_deg"]), 0.1)

    def test_global_type_does_not_overwrite_local_type(self) -> None:
        august_solar = self.events["2026-08-12"]
        self.assertEqual(august_solar["global"]["type"], "total")
        self.assertEqual(august_solar["washington"]["local_type"], "partial")
        self.assertLess(august_solar["washington"]["obscuration_at_observable_maximum"], 0.05)
        self.assertGreater(august_solar["washington"]["observable_minutes"], 60)

        august_lunar = self.events["2026-08-28"]
        self.assertEqual(august_lunar["global"]["type"], "partial")
        self.assertGreater(august_lunar["washington"]["umbral_magnitude"], 0.9)
        self.assertGreater(august_lunar["washington"]["partial_phase"]["minutes_above_horizon"], 190)


if __name__ == "__main__":
    unittest.main()
