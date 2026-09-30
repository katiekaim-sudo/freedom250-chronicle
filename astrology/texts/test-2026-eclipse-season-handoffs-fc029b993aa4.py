from __future__ import annotations

import json
import unittest

import build_2026_eclipse_season_handoffs as handoffs


class EclipseSeasonHandoffTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = handoffs.build_payload()
        cls.rows = {row["season"]: row for row in cls.payload["seasons"]}

    def test_two_2026_eclipse_seasons_are_joined(self):
        self.assertEqual(list(self.rows), ["winter", "summer"])

    def test_winter_replaces_one_closed_loop_with_another(self):
        transition = self.rows["winter"]["root_transition"]
        self.assertTrue(transition["complete_replacement"])
        self.assertTrue(transition["both_frames_without_final_dispositor"])
        self.assertEqual(transition["seed_root_members"], ["Mars", "Saturn"])
        self.assertEqual(transition["full_root_members"], ["Jupiter", "Mercury", "Moon"])

    def test_winter_stage_and_command_exchange_axes(self):
        rows = self.rows["winter"]["cross_chart_relays"]
        mars_mc = next(row for row in rows if row["source"] == "seed Mars" and row["target"] == "Full MC")
        self.assertEqual(mars_mc["aspect"], "sextile")
        self.assertLess(mars_mc["orb_deg"], 0.071)
        mc_sun = next(row for row in rows if row["source"] == "seed MC" and row["target"] == "Full Sun")
        self.assertEqual(mc_sun["aspect"], "square")
        self.assertLess(mc_sun["orb_deg"], 0.679)

    def test_winter_declination_corridors_tighten(self):
        rows = self.rows["winter"]["persistent_declination_relationships"]
        pairs = {tuple(row["pair"]): row for row in rows}
        self.assertTrue(pairs[("Jupiter", "Pluto")]["tightens"])
        self.assertTrue(pairs[("Neptune", "Saturn")]["tightens"])

    def test_summer_preserves_venus_and_changes_sun_to_mercury(self):
        transition = self.rows["summer"]["root_transition"]
        self.assertEqual(transition["shared_members"], ["Venus"])
        self.assertEqual(transition["removed_members"], ["Sun"])
        self.assertEqual(transition["added_members"], ["Mercury"])
        self.assertEqual(transition["seed_final_dispositors"], ["Sun", "Venus"])
        self.assertEqual(transition["full_final_dispositors"], ["Mercury", "Venus"])

    def test_summer_both_full_roots_receive_exact_seed_relays(self):
        receipts = {row["target"]: row for row in self.rows["summer"]["full_root_receipts"]}
        self.assertLess(receipts["Venus"]["orb_deg"], 0.0014)
        self.assertEqual(receipts["Venus"]["source"], "Moon")
        self.assertLess(receipts["Mercury"]["orb_deg"], 0.0245)
        self.assertEqual(receipts["Mercury"]["source"], "Uranus")

    def test_summer_mars_pluto_contra_parallel_tightens(self):
        rows = self.rows["summer"]["persistent_declination_relationships"]
        mars_pluto = next(row for row in rows if row["pair"] == ["Mars", "Pluto"])
        self.assertTrue(mars_pluto["tightens"])
        self.assertFalse(mars_pluto["longitude_major_aspect_at_seed"])
        self.assertFalse(mars_pluto["longitude_major_aspect_at_full"])

    def test_both_eclipse_chapters_expand_the_occupied_field(self):
        self.assertAlmostEqual(
            self.rows["winter"]["distribution_transition"]["occupied_span_change_deg"],
            56.66,
            places=2,
        )
        self.assertAlmostEqual(
            self.rows["summer"]["distribution_transition"]["occupied_span_change_deg"],
            14.46,
            places=2,
        )

    def test_local_visibility_never_changes_governance(self):
        self.assertEqual(
            self.rows["winter"]["solar_seed"]["local_stage"]["washington_status"],
            "not_visible",
        )
        self.assertEqual(
            self.rows["winter"]["lunar_disclosure"]["local_stage"]["washington_status"],
            "sets_during_eclipse",
        )
        self.assertEqual(
            self.rows["summer"]["solar_seed"]["local_stage"]["washington_type"],
            "partial",
        )
        self.assertAlmostEqual(
            self.rows["summer"]["lunar_disclosure"]["local_stage"]["visible_partial_lunar_minutes"],
            198.167,
            places=3,
        )

    def test_twelve_chapter_control_prevents_overclaim(self):
        control = self.payload["bounded_lunation_control"]
        self.assertEqual(control["chapter_count"], 12)
        self.assertEqual(
            control["complete_root_replacement_no_final_dispositor_chapters"],
            ["lun-2026-02-17-ne-solar"],
        )
        self.assertEqual(
            control["all_full_roots_exactly_reached_chapters"],
            ["lun-2026-08-12-ne-solar"],
        )
        self.assertEqual(
            control["seed_angle_to_full_light_within_1_deg_chapters"],
            ["lun-2026-02-17-ne-solar"],
        )

    def test_zero_credit_boundary(self):
        boundary = self.payload["authority_boundary"]
        self.assertEqual(boundary["factual_evidence_credit"], "zero")
        self.assertEqual(boundary["forecast_ledger_credit"], "zero")
        self.assertFalse(boundary["causal_claim"])

    def test_generated_artifact_matches_builder(self):
        stored = json.loads(handoffs.OUT.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.payload)


if __name__ == "__main__":
    unittest.main()
