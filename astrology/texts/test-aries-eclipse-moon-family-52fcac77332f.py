import json
import unittest

import build_aries_eclipse_moon_family as family


class AriesEclipseMoonFamilyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = family.build_payload()
        cls.members = {row["role"]: row for row in cls.payload["members"]}

    def test_registered_three_clock_sequence(self):
        self.assertEqual(list(self.members), ["seed", "first_quarter", "full"])
        self.assertEqual(
            self.members["first_quarter"]["phase_event_id"],
            "lunation-2025-12-27-fq",
        )
        self.assertAlmostEqual(
            self.members["first_quarter"]["elapsed_days_from_seed"], 273.341685, places=6
        )

    def test_first_quarter_staging_and_root(self):
        chart = self.members["first_quarter"]["chart"]
        self.assertEqual(chart["ascendant"]["sign"], "Taurus")
        self.assertEqual(chart["chart_ruler"], "Venus")
        self.assertEqual(chart["positions"]["Moon"]["house"], 12)
        self.assertEqual(chart["positions"]["Sun"]["house"], 9)
        self.assertEqual(chart["positions"]["Pluto"]["house"], 10)
        self.assertEqual(
            chart["all_terminal_circuits"], [["Jupiter", "Moon", "Mars", "Saturn"]]
        )

    def test_distribution_opens_across_the_family(self):
        gaps = [self.members[role]["distribution"]["largest_empty_arc_deg"] for role in self.members]
        self.assertGreater(gaps[0], gaps[1])
        self.assertGreater(gaps[1], gaps[2])

    def test_first_quarter_sun_pluto_parallel_is_tight(self):
        contacts = self.members["first_quarter"]["declination_contacts"]
        row = next(
            item
            for item in contacts
            if {item["first"], item["second"]} == {"Sun", "Pluto"}
        )
        self.assertEqual(row["relationship"], "parallel")
        self.assertLess(row["orb_deg"], 0.05)

    def test_eclipse_pluto_prefigures_mars_pluto_seed_degree(self):
        contacts = self.payload["cross_cycle_degree_relay"]["contacts"]
        eclipse_pluto = next(
            row
            for row in contacts
            if row["event_id"] == "lun-2025-03-29-ne-solar" and row["point"] == "Pluto"
        )
        first_quarter_pluto = next(
            row
            for row in contacts
            if row["event_id"] == "lunation-2025-12-27-fq" and row["point"] == "Pluto"
        )
        self.assertLess(eclipse_pluto["orb_deg"], 0.06)
        self.assertLess(first_quarter_pluto["orb_deg"], 1.0)
        self.assertTrue(eclipse_pluto["admitted_under_policy"])
        self.assertTrue(first_quarter_pluto["admitted_under_policy"])

    def test_full_moon_lights_strike_mars_pluto_seed(self):
        contacts = self.payload["cross_cycle_degree_relay"]["contacts"]
        light_contacts = [
            row
            for row in contacts
            if row["event_id"] == "lun-2026-09-26-fu" and row["point"] in {"Sun", "Moon"}
        ]
        self.assertEqual(len(light_contacts), 2)
        self.assertTrue(all(row["orb_deg"] < 0.053 for row in light_contacts))
        self.assertTrue(all(row["admitted_under_policy"] for row in light_contacts))

    def test_first_quarter_mc_is_disclosed_threshold_miss(self):
        contacts = self.payload["cross_cycle_degree_relay"]["contacts"]
        mc = next(
            row
            for row in contacts
            if row["event_id"] == "lunation-2025-12-27-fq" and row["point"] == "MC"
        )
        self.assertGreater(mc["orb_deg"], 1.0)
        self.assertLess(mc["orb_deg"], 1.1)
        self.assertFalse(mc["admitted_under_policy"])

    def test_eclipse_family_matures_away_from_shadow_geometry(self):
        control = self.payload["nodal_separation_control"]
        rows = {row["role"]: row for row in control["members"]}
        self.assertEqual(
            rows["seed"]["shadow_state"], "registered_partial_solar_eclipse"
        )
        self.assertEqual(
            rows["full"]["shadow_state"], "non_eclipse_moon_family_phase"
        )
        self.assertAlmostEqual(
            rows["seed"]["moon_nearest_node_separation_deg"],
            11.576028,  # DE441 mundane history (DR-080); was 11.576031 on DE406
            places=5,
        )
        self.assertAlmostEqual(
            rows["full"]["moon_nearest_node_separation_deg"],
            34.09451,
            places=5,
        )
        self.assertTrue(
            control["monotonic_checks"][
                "moon_nearest_node_separation_increases"
            ]
        )
        self.assertTrue(
            control["monotonic_checks"][
                "absolute_moon_ecliptic_latitude_increases"
            ]
        )
        self.assertLess(
            control["seed_to_full"]["true_north_node_motion_deg"], -27.8
        )
        self.assertGreater(
            control["seed_to_full"]["nearest_node_separation_increase_deg"],
            22.5,
        )
        self.assertIn(
            "not an eclipse-recurrence clock", control["interpretive_boundary"]
        )

    def test_generated_artifact_matches_builder(self):
        stored = json.loads(family.OUT.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.payload)


if __name__ == "__main__":
    unittest.main()
