from __future__ import annotations

import json
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "sagittarius_moon_family_2024_2027.json").read_text())


class SagittariusMoonFamilyTests(unittest.TestCase):
    def test_family_identity_and_future_boundary(self):
        self.assertEqual(DATA["lineage_id"], "pessin:lun-2024-12-01-ne")
        self.assertEqual(len(DATA["family_members"]), 4)
        self.assertEqual(
            DATA["phase_state_as_of_developed_through"]["last_quarter"],
            "future_not_interpreted_as_occurred",
        )

    def test_family_remains_ordinary(self):
        self.assertEqual(set(DATA["phase_eclipse_states"].values()), {False})

    def test_moon_and_pluto_climb_through_harvest(self):
        stage = DATA["stage_development"]
        self.assertEqual(stage["moon_houses"][:3], [4, 6, 8])
        self.assertEqual(stage["pluto_houses"][:3], [6, 8, 10])
        self.assertEqual(stage["ascendant_signs"], ["Virgo", "Cancer", "Taurus", "Scorpio"])

    def test_seed_degree_returns_at_full_and_last_quarter(self):
        relay = DATA["degree_relays"]
        self.assertLess(relay["seed_to_full_delta_deg"], 0.381)
        self.assertLess(relay["seed_to_last_quarter_delta_deg"], 0.167)
        self.assertLess(relay["seed_to_last_quarter_delta_deg"], relay["seed_to_full_delta_deg"])

    def test_root_resolves_to_mercury_at_full(self):
        roots = DATA["root_development"]
        self.assertIn(["Jupiter", "Mercury"], roots["seed"]["bounded_cycles"])
        self.assertIn(["Jupiter", "Moon"], roots["first_quarter"]["bounded_cycles"])
        self.assertIn(["Mercury", "Sun"], roots["first_quarter"]["bounded_cycles"])
        self.assertEqual(roots["full"]["final_dispositors"], ["Mercury"])
        self.assertIn(["Jupiter", "Moon"], roots["full"]["bounded_cycles"])

    def test_quarter_opens_then_full_reconcentrates(self):
        changes = DATA["distribution_development"]["occupied_span_changes_deg"]
        self.assertGreater(changes["seed_to_first_quarter"], 63.5)
        self.assertLess(changes["first_quarter_to_full"], -75.9)

    def test_record_power_and_force_power_relays_are_exact(self):
        power = DATA["seed_harvest_power_relay"]
        self.assertLess(power["seed_mercury_pluto_parallel_orb_deg"], 0.021)
        self.assertLess(power["seed_mars_to_full_pluto_opposition_orb_deg"], 0.585)

    def test_full_phase_is_visible_before_sunrise(self):
        full = DATA["astronomical_geometry"]["full_phase"]
        self.assertGreater(full["moon_true_altitude_deg"], 0.0)
        self.assertLess(full["sun_true_altitude_deg"], 0.0)
        self.assertLess(full["next_moonset"]["julian_day_ut"], full["next_sunrise"]["julian_day_ut"])

    def test_factual_comparison_preserves_authority_states(self):
        factual = DATA["factual_comparison"]
        self.assertEqual(
            factual["research_id"],
            "december-2024-beneficial-ownership-reporting-perimeter",
        )
        self.assertEqual(len(factual["objects"]), 1)
        self.assertIn("preliminary injunction is not repeal", factual["negative_control"])
        self.assertIn("final rule", factual["objects"][0]["state_by_cutoff"])

    def test_zero_evidence_credit(self):
        self.assertEqual(DATA["authority_boundary"]["evidence_credit"], "zero")


if __name__ == "__main__":
    unittest.main()
