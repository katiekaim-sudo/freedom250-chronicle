#!/usr/bin/env python3
from __future__ import annotations

import json
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "virgo_moon_family_2024_2026.json").read_text())


class VirgoMoonFamilyTests(unittest.TestCase):
    def test_family_identity(self):
        self.assertEqual(DATA["lineage_id"], "pessin:lun-2024-09-03-ne")
        self.assertEqual(len(DATA["family_members"]), 4)

    def test_shadow_arrives_at_harvest(self):
        self.assertEqual(DATA["phase_eclipse_states"], {"seed": False, "first_quarter": False, "full": True})
        node = DATA["node_approach"]
        self.assertGreater(node["seed_nearest_axis_deg"], node["first_quarter_nearest_axis_deg"])
        self.assertGreater(node["first_quarter_nearest_axis_deg"], node["full_nearest_axis_deg"])

    def test_degree_relay(self):
        relay = DATA["degree_relays"]
        self.assertLess(relay["first_quarter_to_full_moon_delta_deg"], 0.064)
        self.assertGreater(relay["first_quarter_to_full_moon_delta_arcminutes"], 3.7)
        self.assertLess(relay["first_quarter_to_full_moon_delta_arcminutes"], 3.9)

    def test_house_migration(self):
        houses = DATA["house_migrations"]
        self.assertEqual(houses["Moon"], [5, 8, 7])
        self.assertEqual(houses["Sun"], [5, 5, 1])
        self.assertEqual(houses["Mercury"], [4, 5, 1])

    def test_root_handoff(self):
        roots = DATA["root_handoff"]
        self.assertEqual(roots["seed"]["final_dispositors"], ["Venus"])
        self.assertIn(["Mercury", "Sun"], roots["seed"]["bounded_cycles"])
        self.assertEqual(roots["first_quarter"]["final_dispositors"], ["Mercury"])
        self.assertIn(["Jupiter", "Moon", "Mercury"], roots["full"]["bounded_cycles"])

    def test_distribution_continuity(self):
        distribution = DATA["distribution_continuity"]
        self.assertTrue(distribution["same_boundary_bodies_at_quarter_and_full"])
        self.assertLess(abs(distribution["first_quarter_to_full_largest_gap_change_deg"]), 1.0)

    def test_cross_chart_neptune_saturn_relay(self):
        relay = DATA["aspect_development"]["quarter_neptune_to_full_saturn"]
        self.assertEqual(relay["kind"], "conjunction")
        self.assertLess(relay["orb_deg"], 0.12)

    def test_full_declination(self):
        rows = DATA["aspect_development"]["full_declinations_within_quarter_degree"]
        match = next(row for row in rows if {row["a"], row["b"]} == {"Jupiter", "Pluto"})
        self.assertEqual(match["kind"], "contra_parallel")
        self.assertLess(match["orb_deg"], 0.055)

    def test_washington_horizon_exit(self):
        geometry = DATA["astronomical_geometry"]
        self.assertTrue(geometry["washington"]["visible"])
        self.assertEqual(geometry["washington"]["local_type"], "total")
        self.assertGreater(geometry["moonset_before_syzygy_seconds"], 50.0)
        self.assertLess(geometry["moonset_before_syzygy_seconds"], 52.0)

    def test_source_separation(self):
        factual = DATA["factual_comparison"]
        self.assertEqual(factual["research_id"], "sec-credit-rating-recordkeeping-orders-2024-2026")
        self.assertIn("selected independently", factual["selection_boundary"])
        self.assertEqual(DATA["authority_boundary"]["evidence_credit"], "zero")


if __name__ == "__main__":
    unittest.main()

