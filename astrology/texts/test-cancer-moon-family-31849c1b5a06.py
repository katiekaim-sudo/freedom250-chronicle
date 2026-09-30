from __future__ import annotations

import json
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "cancer_moon_family_2024_2026.json").read_text())


class CancerMoonFamilyTests(unittest.TestCase):
    def test_family_identity_and_future_boundary(self):
        self.assertEqual(DATA["lineage_id"], "pessin:lun-2024-07-05-ne")
        self.assertEqual(len(DATA["family_members"]), 4)
        self.assertEqual(
            DATA["phase_state_as_of_developed_through"]["last_quarter"],
            "future_not_interpreted_as_occurred",
        )

    def test_family_remains_ordinary_while_approaching_node(self):
        self.assertEqual(set(DATA["phase_eclipse_states"].values()), {False})
        node = DATA["node_approach"]
        values = [
            node["seed_nearest_axis_deg"],
            node["first_quarter_nearest_axis_deg"],
            node["full_nearest_axis_deg"],
            node["last_quarter_nearest_axis_deg"],
        ]
        self.assertTrue(all(a > b for a, b in zip(values, values[1:])))

    def test_four_phase_stage_alternation(self):
        repetition = DATA["four_phase_repetition"]
        self.assertEqual(repetition["ascendant_signs"], ["Sagittarius", "Scorpio", "Sagittarius", "Scorpio"])
        self.assertEqual(repetition["moon_houses"], [8, 9, 8, 9])
        self.assertEqual(repetition["sun_houses"], [8, 6, 2, 12])

    def test_moon_remains_final_across_all_phases(self):
        roots = DATA["root_repetition"]
        for phase in ("seed", "first_quarter", "full", "last_quarter"):
            self.assertIn("Moon", roots[phase]["final_dispositors"])
        self.assertEqual(roots["seed"]["final_dispositors"], ["Moon"])
        self.assertEqual(roots["full"]["final_dispositors"], ["Moon"])
        self.assertIn(["Jupiter", "Mercury"], roots["first_quarter"]["bounded_cycles"])
        self.assertTrue(
            any(set(cycle) == {"Sun", "Venus", "Mars"} for cycle in roots["last_quarter"]["bounded_cycles"])
        )

    def test_seed_returns_more_tightly_at_full_than_quarter_does(self):
        relay = DATA["degree_relays"]
        self.assertLess(relay["seed_to_full_delta_deg"], relay["first_quarter_to_full_delta_deg"])
        self.assertLess(relay["seed_to_full_delta_deg"], 1.356)
        self.assertGreater(relay["seed_to_last_quarter_delta_deg"], 4.03)

    def test_distribution_opens_into_last_quarter(self):
        distribution = DATA["distribution_development"]
        changes = distribution["occupied_span_changes_deg"]
        self.assertLess(changes["seed_to_first_quarter"], 0.0)
        self.assertGreater(changes["first_quarter_to_full"], 27.3)
        self.assertGreater(changes["full_to_last_quarter"], 75.0)
        boundaries = [
            (distribution[p]["empty_arc_from_body"], distribution[p]["empty_arc_to_body"])
            for p in ("seed", "first_quarter", "full", "last_quarter")
        ]
        self.assertEqual(len(set(boundaries)), 4)

    def test_full_declination_joins_value_and_force(self):
        rows = DATA["aspect_development"]["full_declinations_within_quarter_degree"]
        pair = next(row for row in rows if {row["a"], row["b"]} == {"Venus", "Mars"})
        self.assertEqual(pair["kind"], "parallel")
        self.assertLess(pair["orb_deg"], 0.081)

    def test_mars_pluto_interleave_is_exactly_bounded(self):
        interleave = DATA["mars_pluto_interleave"]
        self.assertGreater(interleave["days_full_to_conjunction"], 24.5)
        self.assertLess(interleave["days_full_to_conjunction"], 24.6)
        self.assertGreater(interleave["hours_opposition_to_last_quarter"], 2.76)
        self.assertLess(interleave["hours_opposition_to_last_quarter"], 2.78)

    def test_full_moon_is_visible_before_dawn(self):
        full = DATA["astronomical_geometry"]["full_phase"]
        self.assertGreater(full["moon_true_altitude_deg"], 0.0)
        self.assertLess(full["sun_true_altitude_deg"], 0.0)

    def test_factual_comparison_preserves_lifecycle_differences(self):
        factual = DATA["factual_comparison"]
        self.assertEqual(factual["research_id"], "july-2024-protection-financial-control-window")
        self.assertEqual(len(factual["objects"]), 5)
        self.assertIn("not one program", factual["negative_control"])

    def test_zero_evidence_credit(self):
        self.assertEqual(DATA["authority_boundary"]["evidence_credit"], "zero")


if __name__ == "__main__":
    unittest.main()
