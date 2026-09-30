from __future__ import annotations

import json
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "scorpio_moon_family_2024_2026.json").read_text())


class ScorpioMoonFamilyTests(unittest.TestCase):
    def test_family_identity_and_future_boundary(self):
        self.assertEqual(DATA["lineage_id"], "pessin:lun-2024-11-01-ne")
        self.assertEqual(len(DATA["family_members"]), 4)
        self.assertEqual(
            DATA["future_member_boundary"]["status_as_of_developed_through"],
            "future_not_interpreted_as_occurred",
        )

    def test_family_is_ordinary_and_recedes_from_node(self):
        self.assertEqual(
            DATA["phase_eclipse_states"],
            {"seed": False, "first_quarter": False, "full": False},
        )
        node = DATA["node_recession"]
        self.assertLess(node["seed_nearest_axis_deg"], node["first_quarter_nearest_axis_deg"])
        self.assertLess(node["first_quarter_nearest_axis_deg"], node["full_nearest_axis_deg"])

    def test_seed_returns_at_quarter_more_exactly_than_at_harvest(self):
        relay = DATA["degree_relays"]
        self.assertLess(relay["seed_to_first_quarter_moon_delta_deg"], 0.062)
        self.assertLess(relay["seed_to_first_quarter_moon_delta_arcminutes"], 3.663)
        self.assertGreater(relay["seed_to_full_moon_delta_deg"], 1.75)
        self.assertGreater(relay["first_quarter_to_full_moon_delta_deg"], 1.81)

    def test_house_story_moves_information_into_foundation(self):
        houses = DATA["house_migrations"]
        self.assertEqual(houses["Moon"], [1, 3, 4])
        self.assertEqual(houses["Sun"], [1, 12, 10])
        self.assertEqual(houses["Mercury"], [1, 12, 9])
        self.assertEqual(houses["Pluto"], [3, 6, 7])

    def test_root_handoff_is_loop_to_sun_to_mars(self):
        roots = DATA["root_handoff"]
        self.assertEqual(roots["seed"]["final_dispositors"], [])
        self.assertIn(["Mars", "Moon"], roots["seed"]["bounded_cycles"])
        self.assertEqual(roots["first_quarter"]["final_dispositors"], ["Sun"])
        self.assertEqual(roots["full"]["final_dispositors"], ["Mars"])

    def test_quarter_is_widest_occupied_phase_then_recontracts(self):
        distribution = DATA["distribution_development"]
        self.assertGreater(distribution["seed_to_first_quarter_occupied_span_change_deg"], 17.62)
        self.assertLess(distribution["first_quarter_to_full_occupied_span_change_deg"], -29.43)
        self.assertEqual(distribution["first_quarter"]["empty_arc_from_body"], "Moon")
        self.assertEqual(distribution["full"]["empty_arc_from_body"], "Jupiter")

    def test_quarter_sun_prepares_full_venus_saturn_mechanism(self):
        contacts = DATA["quarter_prefiguration"]["registered_contacts"]
        saturn = next(row for row in contacts if row["to_body"] == "Saturn")
        venus = next(row for row in contacts if row["to_body"] == "Venus")
        self.assertEqual(saturn["kind"], "trine")
        self.assertLess(saturn["orb_deg"], 0.301)
        self.assertEqual(venus["kind"], "sextile")
        self.assertLess(venus["orb_deg"], 0.364)

    def test_declination_adds_venus_pluto_polarity(self):
        rows = DATA["aspect_development"]["full_declinations_within_quarter_degree"]
        venus_pluto = next(row for row in rows if {row["a"], row["b"]} == {"Venus", "Pluto"})
        self.assertEqual(venus_pluto["kind"], "contra_parallel")
        self.assertLess(venus_pluto["orb_deg"], 0.071)
        geometry = DATA["astronomical_geometry"]["full_phase"]
        self.assertGreater(geometry["venus_pluto_longitude_separation_deg"], 56.0)

    def test_seed_contains_applying_mars_pluto_opposition(self):
        context = DATA["seed_mars_pluto_context"]
        self.assertLess(context["seed_orb_deg"], 0.671)
        self.assertGreater(context["hours_seed_to_exact"], 46.8)
        self.assertLess(context["hours_seed_to_exact"], 46.9)
        self.assertEqual(
            context["next_exact_opposition"]["washington_local"][:19],
            "2024-11-03T06:36:34",
        )

    def test_full_moon_is_below_horizon_in_daylight(self):
        geometry = DATA["astronomical_geometry"]["full_phase"]
        self.assertLess(geometry["moon_true_altitude_deg"], 0.0)
        self.assertGreater(geometry["sun_true_altitude_deg"], 0.0)
        self.assertGreater(geometry["minutes_until_moonrise"], 0.0)
        self.assertGreater(geometry["minutes_until_sunset"], 0.0)

    def test_factual_comparison_preserves_every_gate(self):
        factual = DATA["factual_comparison"]
        self.assertEqual(factual["research_id"], "international-monetary-transition")
        self.assertIn("regime commencement was not a licence", factual["negative_control"])
        self.assertIn("licence was not a coin launch", factual["negative_control"])
        self.assertEqual(DATA["authority_boundary"]["evidence_credit"], "zero")


if __name__ == "__main__":
    unittest.main()
