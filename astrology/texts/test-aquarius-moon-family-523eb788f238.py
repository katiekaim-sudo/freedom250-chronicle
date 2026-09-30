#!/usr/bin/env python3
from __future__ import annotations

import json
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "aquarius_moon_family_2025_2026.json").read_text())


class AquariusMoonFamilyTests(unittest.TestCase):
    def test_family_identity(self):
        self.assertEqual(DATA["lineage_id"], "pessin:lun-2025-01-29-ne")
        self.assertEqual(len(DATA["family_members"]), 4)

    def test_quarter_full_degree_relay(self):
        relay = DATA["degree_relays"]
        self.assertLess(relay["first_quarter_to_full_moon_delta_deg"], 0.002)
        self.assertAlmostEqual(relay["first_quarter_to_full_moon_delta_arcsec"], 5.97, places=2)

    def test_seed_frame(self):
        seed = DATA["charts"]["seed_2025_01_29"]
        self.assertEqual(seed["ascendant_sign"], "Aquarius")
        self.assertEqual(seed["bodies"]["Sun"]["whole_sign_house"], 1)
        self.assertEqual(seed["bodies"]["Mars"]["whole_sign_house"], 6)
        self.assertEqual(seed["dispositors"]["bounded_cycles"], [["Jupiter", "Mercury", "Saturn"]])

    def test_first_quarter_frame(self):
        quarter = DATA["charts"]["first_quarter_2025_10_29"]
        self.assertEqual(quarter["ascendant_sign"], "Capricorn")
        self.assertEqual(quarter["bodies"]["Moon"]["whole_sign_house"], 2)
        self.assertEqual(quarter["dispositors"]["final_dispositors"], ["Mars", "Venus"])
        self.assertIn(["Jupiter", "Moon", "Saturn"], quarter["dispositors"]["bounded_cycles"])

    def test_full_frame(self):
        full = DATA["charts"]["full_2026_07_29"]
        self.assertEqual(full["ascendant_sign"], "Virgo")
        self.assertEqual(full["bodies"]["Moon"]["whole_sign_house"], 6)
        self.assertEqual(full["bodies"]["Sun"]["whole_sign_house"], 12)
        self.assertEqual(full["dispositors"]["final_dispositors"], ["Sun"])
        self.assertIn(["Mars", "Mercury", "Moon", "Saturn"], full["dispositors"]["bounded_cycles"])

    def test_full_tight_aspects(self):
        full = DATA["charts"]["full_2026_07_29"]
        lookup = {(row["a"], row["b"], row["kind"]): row["orb_deg"] for row in full["aspects_within_3_deg"]}
        self.assertLess(lookup[("Sun", "Jupiter", "conjunction")], 0.08)
        self.assertLess(lookup[("Venus", "Mars", "square")], 0.12)

    def test_full_declination(self):
        full = DATA["charts"]["full_2026_07_29"]
        lookup = {(row["a"], row["b"], row["kind"]): row["orb_deg"] for row in full["declination_relationships_within_1_deg"]}
        self.assertLess(lookup[("Venus", "Saturn", "parallel")], 0.03)
        self.assertLess(lookup[("Mars", "Pluto", "contra_parallel")], 0.13)

    def test_house_migration(self):
        self.assertEqual(DATA["house_migrations"]["Moon"], [1, 2, 6])
        self.assertEqual(DATA["house_migrations"]["Pluto"], [1, 2, 6])

    def test_astronomical_geometry(self):
        geometry = DATA["astronomical_geometry"]["full_phase"]
        self.assertLess(geometry["sun_jupiter_true_sky_separation_deg"], 0.6)
        self.assertLess(geometry["moon_pluto_true_sky_separation_deg"], 4.0)
        self.assertGreater(geometry["sun_pluto_true_sky_separation_deg"], 175.0)
        horizon = DATA["astronomical_geometry"]["local_horizon"]["full"]
        self.assertEqual(horizon["above_count"] + horizon["below_or_on_count"], 10)

    def test_zero_evidence_credit(self):
        self.assertEqual(DATA["authority_boundary"]["evidence_credit"], "zero")


if __name__ == "__main__":
    unittest.main()
