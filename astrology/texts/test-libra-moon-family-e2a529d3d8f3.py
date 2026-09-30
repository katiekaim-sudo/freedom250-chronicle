from __future__ import annotations

import json
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "libra_moon_family_2024_2026.json").read_text())


class LibraMoonFamilyTests(unittest.TestCase):
    def test_family_identity_and_future_boundary(self):
        self.assertEqual(DATA["lineage_id"], "pessin:lun-2024-10-02-ne-solar")
        self.assertEqual(len(DATA["family_members"]), 4)
        self.assertEqual(
            DATA["future_member_boundary"]["status_as_of_developed_through"],
            "future_not_interpreted_as_occurred",
        )

    def test_shadow_releases_before_harvest(self):
        self.assertEqual(
            DATA["phase_eclipse_states"],
            {"seed": True, "first_quarter": False, "full": False},
        )
        shadow = DATA["shadow_release"]
        self.assertLess(shadow["seed_nearest_axis_deg"], 3.5)
        self.assertGreater(shadow["first_quarter_nearest_axis_deg"], 20.0)
        self.assertGreater(shadow["full_nearest_axis_deg"], 33.0)

    def test_global_eclipse_did_not_cross_washington(self):
        eclipse = DATA["astronomical_geometry"]["seed_eclipse"]
        self.assertEqual(eclipse["global"]["type"], "annular")
        self.assertFalse(eclipse["washington"]["visible"])
        self.assertGreater(eclipse["washington"]["sun_true_altitude_at_syzygy_deg"], 39.0)

    def test_degree_relay(self):
        relay = DATA["degree_relays"]
        self.assertLess(relay["seed_to_full_moon_delta_deg"], 2.3)
        self.assertLess(relay["first_quarter_to_full_moon_delta_deg"], 1.2)
        self.assertGreater(relay["first_quarter_to_full_moon_delta_arcminutes"], 71.0)

    def test_house_migrations(self):
        houses = DATA["house_migrations"]
        self.assertEqual(houses["Sun"], [10, 9, 6])
        self.assertEqual(houses["Moon"], [10, 12, 12])
        self.assertEqual(houses["Venus"], [11, 7, 7])
        self.assertEqual(houses["Pluto"], [1, 4, 4])

    def test_venus_final_installed_at_first_quarter(self):
        roots = DATA["root_handoff"]
        self.assertEqual(roots["seed"]["final_dispositors"], [])
        self.assertIn(["Mars", "Moon", "Venus"], roots["seed"]["bounded_cycles"])
        self.assertEqual(roots["first_quarter"]["final_dispositors"], ["Venus"])
        self.assertEqual(roots["full"]["final_dispositors"], ["Venus"])

    def test_quarter_installs_full_container(self):
        distribution = DATA["distribution_development"]
        self.assertTrue(distribution["same_quarter_full_empty_arc_boundary"])
        self.assertEqual(distribution["first_quarter"]["empty_arc_from_body"], "Moon")
        self.assertEqual(distribution["first_quarter"]["empty_arc_to_body"], "Pluto")
        self.assertLess(distribution["first_quarter_to_full_largest_gap_change_deg"], 0.95)

    def test_quarter_power_pressures_full_settlement(self):
        rows = DATA["aspect_development"]["quarter_to_full_contacts_within_1_25_deg"]
        pluto_venus = next(
            row for row in rows
            if row["from_body"] == "Pluto" and row["to_body"] == "Venus"
        )
        self.assertEqual(pluto_venus["kind"], "square")
        self.assertLess(pluto_venus["orb_deg"], 0.118)

    def test_full_declination_pressure(self):
        rows = DATA["aspect_development"]["full_declinations_within_quarter_degree"]
        saturn_neptune = next(row for row in rows if {row["a"], row["b"]} == {"Saturn", "Neptune"})
        self.assertEqual(saturn_neptune["kind"], "contra_parallel")
        self.assertLess(saturn_neptune["orb_deg"], 0.0052)
        self.assertLess(saturn_neptune["orb_deg"] * 3600.0, 18.6)
        geometry = DATA["astronomical_geometry"]["full_phase"]
        self.assertGreater(geometry["saturn_neptune_longitude_separation_deg"], 3.4)

    def test_full_moon_is_physically_visible_at_exact_phase(self):
        geometry = DATA["astronomical_geometry"]["full_phase"]
        self.assertGreater(geometry["moon_true_altitude_deg"], 28.0)
        self.assertLess(geometry["sun_true_altitude_deg"], -29.0)
        self.assertGreater(geometry["minutes_since_moonrise"], 165.0)
        self.assertGreater(geometry["minutes_until_moonset"], 516.0)

    def test_factual_comparison_keeps_gate_timing_honest(self):
        factual = DATA["factual_comparison"]
        self.assertEqual(factual["research_id"], "contested-logistics")
        self.assertIn("already ratified and signed", factual["negative_control"])
        self.assertEqual(DATA["authority_boundary"]["evidence_credit"], "zero")


if __name__ == "__main__":
    unittest.main()
