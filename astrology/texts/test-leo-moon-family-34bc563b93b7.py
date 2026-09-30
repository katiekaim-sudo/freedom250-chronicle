from __future__ import annotations

import json
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "leo_moon_family_2024_2026.json").read_text())


class LeoMoonFamilyTests(unittest.TestCase):
    def test_family_identity_and_future_boundary(self):
        self.assertEqual(DATA["lineage_id"], "pessin:lun-2024-08-04-ne")
        self.assertEqual(len(DATA["family_members"]), 4)
        self.assertEqual(
            DATA["future_member_boundary"]["status_as_of_developed_through"],
            "future_not_interpreted_as_occurred",
        )

    def test_family_remains_ordinary_while_approaching_node(self):
        self.assertEqual(
            DATA["phase_eclipse_states"],
            {"seed": False, "first_quarter": False, "full": False},
        )
        node = DATA["node_approach"]
        self.assertGreater(node["seed_nearest_axis_deg"], node["first_quarter_nearest_axis_deg"])
        self.assertGreater(node["first_quarter_nearest_axis_deg"], node["full_nearest_axis_deg"])

    def test_seed_degree_returns_more_tightly_than_quarter_degree(self):
        relay = DATA["degree_relays"]
        self.assertLess(relay["seed_to_full_moon_delta_deg"], 0.5)
        self.assertGreater(relay["first_quarter_to_full_moon_delta_deg"], 1.28)
        self.assertLess(relay["seed_to_full_moon_delta_arcminutes"], 29.65)

    def test_leo_rises_at_seed_and_harvest(self):
        recurrence = DATA["angle_recurrence"]
        self.assertTrue(recurrence["same_ascendant_sign"])
        self.assertEqual(recurrence["seed_ascendant_sign"], "Leo")
        self.assertEqual(recurrence["full_ascendant_sign"], "Leo")

    def test_house_return_and_counterparty_concentration(self):
        houses = DATA["house_migrations"]
        self.assertEqual(houses["Moon"], [1, 2, 1])
        self.assertEqual(houses["Sun"], [1, 11, 7])
        self.assertEqual(houses["Mars"], [11, 2, 7])
        self.assertEqual(houses["Pluto"], [7, 8, 7])

    def test_root_never_reduces_to_one_final_after_seed(self):
        roots = DATA["root_handoff"]
        self.assertEqual(set(roots["seed"]["final_dispositors"]), {"Mercury", "Sun"})
        self.assertEqual(roots["first_quarter"]["final_dispositors"], [])
        self.assertEqual(roots["full"]["final_dispositors"], [])
        self.assertIn(["Mars", "Sun", "Venus"], roots["first_quarter"]["bounded_cycles"])
        self.assertIn(["Jupiter", "Moon", "Sun", "Saturn"], roots["full"]["bounded_cycles"])

    def test_quarter_installs_full_distribution_boundary(self):
        distribution = DATA["distribution_development"]
        self.assertTrue(distribution["same_quarter_full_empty_arc_boundary"])
        self.assertEqual(distribution["first_quarter"]["empty_arc_from_body"], "Moon")
        self.assertEqual(distribution["first_quarter"]["empty_arc_to_body"], "Pluto")
        self.assertLess(distribution["first_quarter_to_full_largest_gap_change_deg"], 1.2)

    def test_quarter_mars_flips_onto_full_mars(self):
        rows = DATA["aspect_development"]["quarter_to_full_contacts_within_1_25_deg"]
        mars = next(row for row in rows if row["from_body"] == row["to_body"] == "Mars")
        pluto = next(row for row in rows if row["from_body"] == row["to_body"] == "Pluto")
        self.assertEqual(mars["kind"], "opposition")
        self.assertLess(mars["orb_deg"], 0.197)
        self.assertEqual(pluto["kind"], "conjunction")
        self.assertLess(pluto["orb_deg"], 0.093)

    def test_declination_supplies_hidden_mars_uranus_axis(self):
        rows = DATA["aspect_development"]["full_declinations_within_quarter_degree"]
        mars_uranus = next(row for row in rows if {row["a"], row["b"]} == {"Mars", "Uranus"})
        self.assertEqual(mars_uranus["kind"], "contra_parallel")
        self.assertLess(mars_uranus["orb_deg"], 0.0093)
        geometry = DATA["astronomical_geometry"]["full_phase"]
        self.assertGreater(geometry["mars_uranus_longitude_separation_deg"], 110.0)

    def test_symbolic_first_house_moon_is_below_horizon_at_exactitude(self):
        geometry = DATA["astronomical_geometry"]["full_phase"]
        self.assertLess(geometry["moon_true_altitude_deg"], -1.8)
        self.assertGreater(geometry["sun_true_altitude_deg"], 2.8)
        self.assertGreater(geometry["minutes_until_moonrise"], 13.3)
        self.assertLess(geometry["minutes_until_moonrise"], 13.4)
        self.assertGreater(geometry["minutes_until_sunset"], 18.9)

    def test_factual_comparison_preserves_permission_operation_boundary(self):
        factual = DATA["factual_comparison"]
        self.assertEqual(factual["research_id"], "fed-clearing-treasury")
        self.assertIn("permission-without-operation", factual["negative_control"])
        self.assertEqual(DATA["authority_boundary"]["evidence_credit"], "zero")


if __name__ == "__main__":
    unittest.main()
