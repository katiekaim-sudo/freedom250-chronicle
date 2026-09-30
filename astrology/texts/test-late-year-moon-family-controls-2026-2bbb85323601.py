from __future__ import annotations

import json
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "late_year_moon_family_controls_2026.json").read_text())
FAMILIES = {row["key"]: row for row in DATA["families"]}


class LateYearMoonFamilyControlTests(unittest.TestCase):
    def test_three_future_full_phases_are_not_described_as_occurred(self):
        self.assertEqual(set(FAMILIES), {"taurus", "gemini", "cancer_december"})
        for row in FAMILIES.values():
            self.assertEqual(
                row["phase_state_as_of_2026_09_25"]["full"],
                "future_not_interpreted_as_occurred",
            )
        self.assertEqual(DATA["authority_boundary"]["political_maturation"][:8], "withheld")

    def test_all_three_families_remain_ordinary(self):
        for row in FAMILIES.values():
            self.assertEqual(
                row["phase_eclipse_states"],
                {"seed": False, "first_quarter": False, "full": False},
            )

    def test_degree_drift_is_intentionally_wide(self):
        self.assertGreater(FAMILIES["taurus"]["degree_relays"]["first_quarter_to_full_deg"], 3.47)
        self.assertGreater(FAMILIES["gemini"]["degree_relays"]["first_quarter_to_full_deg"], 3.56)
        self.assertGreater(FAMILIES["cancer_december"]["degree_relays"]["first_quarter_to_full_deg"], 2.91)
        self.assertLess(DATA["group_findings"]["full_moon_degree_range_deg"], 0.53)

    def test_all_three_full_phases_are_splay(self):
        self.assertTrue(DATA["group_findings"]["all_full_phases_registered_splay"])
        for row in FAMILIES.values():
            self.assertEqual(row["full_phase_astronomy"]["registered_shape"], "splay")

    def test_largest_empty_arcs_collapse_as_occupied_fields_expand(self):
        for row in FAMILIES.values():
            self.assertLess(row["distribution"]["quarter_to_full_largest_empty_arc_change_deg"], -116.0)
            self.assertGreater(row["distribution"]["quarter_to_full_occupied_span_change_deg"], 116.0)

    def test_node_paths_diverge(self):
        taurus = FAMILIES["taurus"]["node_path"]
        gemini = FAMILIES["gemini"]["node_path"]
        cancer = FAMILIES["cancer_december"]["node_path"]
        self.assertLess(taurus[0], taurus[1])
        self.assertLess(taurus[1], taurus[2])
        self.assertLess(gemini[0], gemini[1])
        self.assertGreater(gemini[1], gemini[2])
        self.assertGreater(cancer[0], cancer[1])
        self.assertGreater(cancer[1], cancer[2])

    def test_house_paths_remain_family_specific(self):
        self.assertEqual(FAMILIES["taurus"]["house_migrations"]["Moon"], [9, 8, 10])
        self.assertEqual(FAMILIES["gemini"]["house_migrations"]["Moon"], [6, 4, 6])
        self.assertEqual(FAMILIES["cancer_december"]["house_migrations"]["Moon"], [1, 12, 12])

    def test_taurus_retains_exact_quarter_mars_to_full_neptune_relay(self):
        contacts = FAMILIES["taurus"]["quarter_to_full_contacts_within_1_25_deg"]
        relay = next(row for row in contacts if row["from_body"] == "Mars" and row["to_body"] == "Neptune")
        self.assertEqual(relay["kind"], "sextile")
        self.assertLess(relay["orb_deg"], 0.018)

    def test_gemini_and_cancer_declination_controls_differ(self):
        self.assertEqual(FAMILIES["taurus"]["full_declinations_within_quarter_degree"], [])
        self.assertEqual(len(FAMILIES["gemini"]["full_declinations_within_quarter_degree"]), 3)
        self.assertEqual(len(FAMILIES["cancer_december"]["full_declinations_within_quarter_degree"]), 2)

    def test_visibility_staging_differs_across_splay_group(self):
        taurus = FAMILIES["taurus"]["full_phase_astronomy"]
        gemini = FAMILIES["gemini"]["full_phase_astronomy"]
        cancer = FAMILIES["cancer_december"]["full_phase_astronomy"]
        self.assertGreater(taurus["moon_true_altitude_deg"], 0.0)
        self.assertLess(taurus["sun_true_altitude_deg"], 0.0)
        self.assertLess(gemini["moon_true_altitude_deg"], 0.0)
        self.assertGreater(gemini["sun_true_altitude_deg"], 0.0)
        self.assertGreater(cancer["moon_true_altitude_deg"], 0.0)
        self.assertLess(cancer["sun_true_altitude_deg"], 0.0)

    def test_zero_evidence_credit(self):
        self.assertEqual(DATA["authority_boundary"]["evidence_credit"], "zero")


if __name__ == "__main__":
    unittest.main()
