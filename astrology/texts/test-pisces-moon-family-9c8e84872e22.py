#!/usr/bin/env python3
from __future__ import annotations

import json
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "pisces_moon_family_2025_2026.json").read_text())


class PiscesMoonFamilyTests(unittest.TestCase):
    def test_family_identity(self):
        self.assertEqual(DATA["lineage_id"], "pessin:lun-2025-02-28-ne")
        self.assertEqual(len(DATA["family_members"]), 4)

    def test_shadow_arrives_at_full_phase(self):
        self.assertEqual(DATA["phase_eclipse_states"], {"seed": False, "first_quarter": False, "full": True})
        approach = DATA["node_approach"]
        self.assertGreater(approach["seed_nearest_axis_deg"], approach["full_nearest_axis_deg"])
        self.assertLess(approach["full_nearest_axis_deg"], 6.0)

    def test_seed_frame(self):
        seed = DATA["charts"]["seed_2025_02_28"]
        self.assertEqual(seed["ascendant_sign"], "Libra")
        self.assertEqual(seed["bodies"]["Moon"]["whole_sign_house"], 6)
        self.assertIn(["Jupiter", "Mercury"], seed["dispositors"]["bounded_cycles"])

    def test_first_quarter_frame(self):
        quarter = DATA["charts"]["first_quarter_2025_11_28"]
        self.assertEqual(quarter["bodies"]["Moon"]["sign"], "Pisces")
        self.assertAlmostEqual(quarter["bodies"]["Moon"]["degree_in_sign"], 6.295993639, places=6)

    def test_full_frame(self):
        full = DATA["charts"]["full_2026_08_28"]
        self.assertEqual(full["ascendant_sign"], "Gemini")
        self.assertEqual(full["bodies"]["Moon"]["whole_sign_house"], 10)
        self.assertEqual(full["bodies"]["Sun"]["whole_sign_house"], 4)
        self.assertEqual(full["dispositors"]["final_dispositors"], ["Mercury", "Venus"])

    def test_root_handoff(self):
        handoff = DATA["root_handoff"]
        self.assertIn(["Jupiter", "Mercury"], handoff["seed"]["terminal_structure"]["bounded_cycles"])
        self.assertIn(["Jupiter", "Moon"], handoff["first_quarter"]["terminal_structure"]["bounded_cycles"])
        self.assertEqual(handoff["full"]["terminal_structure"]["final_dispositors"], ["Mercury", "Venus"])
        self.assertGreater(handoff["seed"]["venus_station"]["hours_after_seed"], 47.0)
        self.assertLess(handoff["seed"]["venus_station"]["hours_after_seed"], 49.0)

    def test_full_mutable_t_square(self):
        full = DATA["charts"]["full_2026_08_28"]
        lookup = {(row["a"], row["b"], row["kind"]): row["orb_deg"] for row in full["aspects_within_3_deg"]}
        self.assertLess(lookup[("Mercury", "Uranus", "square")], 0.3)
        self.assertLess(lookup[("Sun", "Uranus", "square")], 0.8)
        self.assertLess(lookup[("Moon", "Uranus", "square")], 0.8)

    def test_declination_cross_cut(self):
        full = DATA["charts"]["full_2026_08_28"]
        lookup = {(row["a"], row["b"], row["kind"]): row["orb_deg"] for row in full["declination_relationships_within_1_deg"]}
        self.assertLess(lookup[("Mars", "Pluto", "contra_parallel")], 0.07)
        bridge = DATA["declination_bridge"]
        self.assertLess(bridge["exact_mars_pluto_contra_parallel"]["hours_before_full_phase"], 41.0)
        self.assertGreater(bridge["exact_mars_pluto_contra_parallel"]["hours_before_full_phase"], 39.0)

    def test_distribution_control(self):
        control = DATA["distribution_control"]
        self.assertEqual(control["first_splay_chart"]["chart_id"], "lun-2026-08-28-fu-lunar")
        self.assertEqual(control["immediately_prior_chart"]["chart_id"], "lun-2026-08-12-ne-solar")
        self.assertGreater(control["largest_gap_contraction_into_first_splay_deg"], 14.0)

    def test_washington_visibility(self):
        eclipse = DATA["astronomical_geometry"]["full_phase"]
        self.assertTrue(eclipse["washington_visible"])
        self.assertEqual(eclipse["washington_local_type"], "partial")
        self.assertGreater(eclipse["washington_moon_altitude_at_maximum_deg"], 39.0)
        self.assertGreater(eclipse["washington_partial_phase_minutes"], 198.0)

    def test_source_separation(self):
        factual = DATA["factual_comparison"]
        self.assertEqual(factual["research_id"], "fraud-payment-integrity")
        self.assertIn("selected independently", factual["selection_boundary"])
        self.assertEqual(DATA["authority_boundary"]["evidence_credit"], "zero")


if __name__ == "__main__":
    unittest.main()
