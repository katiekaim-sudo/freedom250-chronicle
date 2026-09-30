#!/usr/bin/env python3
from __future__ import annotations

import json
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "capricorn_moon_family_2024_2026.json").read_text())


class CapricornMoonFamilyTests(unittest.TestCase):
    def test_family_identity(self):
        self.assertEqual(DATA["lineage_id"], "pessin:lun-2024-12-30-ne")
        self.assertEqual(len(DATA["family_members"]), 4)

    def test_ordinary_seed_and_harvest(self):
        self.assertEqual(
            DATA["phase_eclipse_states"],
            {"seed": False, "first_quarter": False, "full": False},
        )

    def test_degree_relay(self):
        relay = DATA["degree_relays"]
        self.assertLess(relay["first_quarter_to_full_moon_delta_deg"], 1.16)
        self.assertGreater(relay["first_quarter_to_full_moon_delta_arcminutes"], 69.0)

    def test_house_migration(self):
        houses = DATA["house_migrations"]
        self.assertEqual(houses["Moon"], [7, 9, 2])
        self.assertEqual(houses["Sun"], [7, 6, 8])
        self.assertEqual(houses["Mercury"], [6, 6, 8])

    def test_root_handoff(self):
        roots = DATA["root_handoff"]
        self.assertIn(["Jupiter", "Mercury"], roots["seed"]["bounded_cycles"])
        self.assertEqual(roots["first_quarter"]["final_dispositors"], ["Mars"])
        self.assertIn(
            ["Mars", "Mercury", "Moon", "Saturn"],
            roots["full"]["bounded_cycles"],
        )

    def test_distribution_opens_then_reconcentrates(self):
        distribution = DATA["distribution_development"]
        self.assertLess(distribution["seed_to_first_quarter_largest_gap_change_deg"], -74.0)
        self.assertGreater(distribution["first_quarter_to_full_largest_gap_change_deg"], 77.0)
        self.assertLess(abs(distribution["seed_to_full_largest_gap_change_deg"]), 3.0)
        self.assertEqual(distribution["seed"]["empty_arc_from_body"], "Mars")
        self.assertEqual(distribution["full"]["empty_arc_from_body"], "Venus")

    def test_full_declinations(self):
        rows = DATA["aspect_development"]["full_declinations_within_quarter_degree"]
        sun_pluto = next(row for row in rows if {row["a"], row["b"]} == {"Sun", "Pluto"})
        jupiter_uranus = next(row for row in rows if {row["a"], row["b"]} == {"Jupiter", "Uranus"})
        self.assertEqual(sun_pluto["kind"], "contra_parallel")
        self.assertLess(sun_pluto["orb_deg"], 0.047)
        self.assertEqual(jupiter_uranus["kind"], "parallel")
        self.assertLess(jupiter_uranus["orb_deg"], 0.141)

    def test_full_horizon(self):
        horizon = DATA["astronomical_geometry"]["local_horizon"]["full"]
        self.assertIn("Moon", horizon["below_or_on_true_horizon"])
        self.assertIn("Sun", horizon["above_true_horizon"])
        self.assertEqual(horizon["above_count"], 4)
        geometry = DATA["astronomical_geometry"]["full_phase"]
        self.assertGreater(geometry["sunset_after_exact_full_minutes"], 35.0)
        self.assertGreater(geometry["moonrise_after_exact_full_minutes"], 55.0)
        self.assertLess(geometry["moonrise_after_exact_full_minutes"], 65.0)

    def test_negative_control(self):
        factual = DATA["factual_comparison"]
        self.assertEqual(factual["research_id"], "treasury-irs")
        self.assertEqual(
            factual["fixed_window_control_research_id"],
            "december-2024-rule-perimeter-operating-identity-window",
        )
        self.assertIn("no force or effect", factual["pre_quarter_reversal"])
        self.assertIn("did not mature", factual["negative_control"])
        self.assertIn(
            "not extra astrology votes",
            factual["same_window_counter_control"]["interpretive_limit"],
        )
        self.assertEqual(DATA["authority_boundary"]["evidence_credit"], "zero")


if __name__ == "__main__":
    unittest.main()
