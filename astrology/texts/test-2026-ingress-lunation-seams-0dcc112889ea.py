from __future__ import annotations

import json
import unittest

import build_2026_ingress_lunation_seams as seams


class IngressLunationSeamTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = seams.build_payload()
        cls.rows = {row["season"]: row for row in cls.payload["seams"]}

    def test_four_cardinal_seams_are_registered(self):
        self.assertEqual(list(self.rows), ["Aries", "Cancer", "Libra", "Capricorn"])
        self.assertTrue(
            self.payload["year_pattern"][
                "every_ingress_occurs_inside_a_new_moon_chapter_planted_under_predecessor_ingress"
            ]
        )

    def test_ingress_enters_progressively_older_lunar_chapter(self):
        ages = self.payload["year_pattern"]["chapter_ages_days"]
        self.assertTrue(all(a < b for a, b in zip(ages, ages[1:])))
        self.assertAlmostEqual(ages[0], 1.557276, places=6)
        self.assertAlmostEqual(ages[-1], 12.832211, places=6)

    def test_first_full_moon_arrives_progressively_sooner(self):
        leads = self.payload["year_pattern"]["days_to_first_full_moon"]
        self.assertTrue(all(a > b for a, b in zip(leads, leads[1:])))
        self.assertAlmostEqual(leads[0], 12.476396, places=6)
        self.assertAlmostEqual(leads[-1], 2.193055, places=6)

    def test_every_seed_and_ingress_is_circuit_rooted(self):
        self.assertTrue(
            self.payload["year_pattern"][
                "every_seed_and_ingress_has_bounded_cycle_root_not_final_dispositor"
            ]
        )

    def test_expected_root_handoffs(self):
        aries = self.rows["Aries"]["seed_to_ingress_root_transition"]
        self.assertTrue(aries["source_root_is_subset"])
        self.assertEqual(aries["added_members"], ["Mars"])
        cancer = self.rows["Cancer"]["seed_to_ingress_root_transition"]
        self.assertTrue(cancer["same_root_set"])
        libra = self.rows["Libra"]["seed_to_ingress_root_transition"]
        self.assertEqual(libra["shared_members"], ["Mars", "Moon"])
        self.assertEqual(libra["removed_members"], ["Mercury", "Venus"])
        self.assertEqual(libra["added_members"], ["Saturn"])
        capricorn = self.rows["Capricorn"]["seed_to_ingress_root_transition"]
        self.assertTrue(capricorn["source_root_is_subset"])
        self.assertEqual(capricorn["added_members"], ["Mars", "Mercury", "Saturn"])

    def test_sagittarius_seed_lands_on_capricorn_descendant(self):
        contacts = self.rows["Capricorn"]["seed_degree_contacts_to_incoming_ingress"]
        dsc = next(row for row in contacts if row["point"] == "DSC")
        self.assertEqual(dsc["aspect"], "conjunction")
        self.assertLess(dsc["orb_deg"], 0.027)
        self.assertEqual(dsc["strength_band"], "exact_relay")

    def test_libra_seam_is_explicit_contact_control(self):
        self.assertEqual(
            self.rows["Libra"]["seed_degree_contacts_to_incoming_ingress"], []
        )

    def test_bounded_year_control_prevents_uniqueness_claim(self):
        control = self.payload["bounded_year_control"]
        self.assertEqual(control["all_four_ingresses_waxing_years"], [2018, 2026])
        self.assertIn(2026, control["strictly_increasing_without_wrap_years"])
        self.assertIn("not unique", control["boundary"])

    def test_future_boundary_and_zero_credit(self):
        self.assertEqual(
            self.rows["Capricorn"]["knowledge_state_at_2026_09_25"],
            "prospective_at_cutoff",
        )
        boundary = self.payload["authority_boundary"]
        self.assertEqual(boundary["factual_evidence_credit"], "zero")
        self.assertEqual(boundary["forecast_ledger_credit"], "zero")
        self.assertFalse(boundary["causal_claim"])

    def test_absent_future_closing_chart_is_not_invented(self):
        closing = self.rows["Capricorn"]["chapter_closing_new_moon"]
        self.assertEqual(
            closing["chart_registration_state"],
            "exact_clock_only_chart_bone_absent_at_cutoff",
        )
        self.assertEqual(closing["interpretive_fields"], "withheld")

    def test_generated_artifact_matches_builder(self):
        stored = json.loads(seams.OUT.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.payload)


if __name__ == "__main__":
    unittest.main()
