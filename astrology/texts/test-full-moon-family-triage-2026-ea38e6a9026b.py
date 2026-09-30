#!/usr/bin/env python3
"""Focused invariants for the 2026 Full-Moon-family structural triage."""

import json
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "full_moon_family_triage_2026.json").read_text())


class FullMoonFamilyTriage2026Tests(unittest.TestCase):
    def setUp(self):
        self.rows = DATA["families"]
        self.by_sign = {row["full"]["moon_sign"]: row for row in self.rows}

    def test_complete_2026_roster_and_zero_credit(self):
        self.assertEqual(DATA["family_count"], 13)
        self.assertEqual(len(self.rows), 13)
        self.assertEqual(DATA["authority_boundary"]["ranking"].split(";")[0], "none")
        self.assertEqual(DATA["authority_boundary"]["evidence_credit"], "zero")

    def test_every_family_preserves_unreviewed_lineage_state(self):
        self.assertTrue(all(row["interpretation_status"] == "unreviewed" for row in self.rows))
        self.assertTrue(all(row["story_verdict"] is None for row in self.rows))

    def test_shadow_arrives_only_for_virgo_and_pisces(self):
        signs = {
            row["full"]["moon_sign"]
            for row in self.rows
            if row["shadow_transition"] == "shadow_arrives_at_harvest"
        }
        self.assertEqual(signs, {"Virgo", "Pisces"})

    def test_shadow_releases_only_for_libra_and_aries(self):
        signs = {
            row["full"]["moon_sign"]
            for row in self.rows
            if row["shadow_transition"] == "shadow_releases_before_harvest"
        }
        self.assertEqual(signs, {"Libra", "Aries"})

    def test_aquarius_and_virgo_are_quarter_degree_relays(self):
        tight = {
            row["full"]["moon_sign"]
            for row in self.rows
            if row["relays"]["first_quarter_to_full_moon_degree_gap_deg"] <= 0.25
        }
        self.assertEqual(tight, {"Virgo", "Aquarius"})

    def test_aquarius_remains_the_tightest_relay(self):
        order = DATA["quarter_to_full_degree_gap_order"]
        self.assertEqual(order[0]["moon_sign"], "Aquarius")
        self.assertLess(order[0]["gap_deg"], 0.002)
        self.assertEqual(order[1]["moon_sign"], "Virgo")

    def test_every_full_phase_has_locked_reading_and_shape(self):
        self.assertTrue(all(row["full"]["reading_id"] for row in self.rows))
        self.assertTrue(all(row["full"]["registered_shape"] for row in self.rows))

    def test_house_migrations_cover_ten_planets(self):
        for row in self.rows:
            migrations = row["relays"]["house_migrations"]
            self.assertEqual(set(migrations), {
                "Sun", "Moon", "Mercury", "Venus", "Mars",
                "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto",
            })
            self.assertTrue(all(len(path) == 3 for path in migrations.values()))


if __name__ == "__main__":
    unittest.main()
