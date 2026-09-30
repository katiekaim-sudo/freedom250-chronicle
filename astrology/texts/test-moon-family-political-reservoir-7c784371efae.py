from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

import build_moon_family_political_reservoir as reservoir


ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "03 - Astrology" / "Astrology Files" / "ASTROLOGY FILES CATALOG.json"
REGISTRY = ROOT / "03 - Astrology" / "Astrology Files" / "ASTROLOGY FILES REGISTRY.json"


class MoonFamilyPoliticalReservoirTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = reservoir.build_payload()

    def test_population_and_clock_states(self):
        self.assertEqual(self.payload["counts"], {
            "families": 13,
            "retrospective_comparisons_complete": 9,
            "pre_full_comparisons_prepared": 1,
            "prospective_maturations_withheld": 3,
        })
        states = {row["comparison_state"] for row in self.payload["records"]}
        self.assertEqual(states, {
            "retrospective_comparison_complete",
            "pre_full_comparison_prepared",
            "prospective_maturation_withheld",
        })

    def test_retrospective_routes_and_future_withholding(self):
        for row in self.payload["records"]:
            if row["full_phase"]["clock_state_at_cutoff"] == "occurred":
                self.assertEqual(row["comparison_state"], "retrospective_comparison_complete")
                self.assertTrue(row["research_routes"])
            elif row["comparison_state"] == "pre_full_comparison_prepared":
                self.assertEqual(row["seed"]["chart_id"], "lun-2025-03-29-ne-solar")
                self.assertTrue(row["research_routes"])
            else:
                self.assertEqual(row["comparison_state"], "prospective_maturation_withheld")
                self.assertEqual(row["research_routes"], [])

    def test_capricorn_has_backbone_and_same_window_control(self):
        capricorn = next(
            row for row in self.payload["records"]
            if row["seed"]["chart_id"] == "lun-2024-12-30-ne"
        )
        ids = {route["research_id"] for route in capricorn["research_routes"]}
        self.assertEqual(ids, {
            "treasury-irs",
            "december-2024-rule-perimeter-operating-identity-window",
        })
        control = next(
            route for route in capricorn["research_routes"]
            if route["research_id"] == "december-2024-rule-perimeter-operating-identity-window"
        )
        self.assertIn("not an additional astrology vote", control["role"])

    def test_authority_boundary(self):
        boundary = self.payload["authority_boundary"]
        for key in (
            "workbench_content_imported",
            "astrology_selected_evidence",
            "same_window_objects_are_extra_votes",
            "thematic_similarity_is_maturation",
            "locked_readings_changed",
        ):
            self.assertFalse(boundary[key])
        self.assertEqual(boundary["evidence_credit"], "zero")
        self.assertEqual(boundary["forecast_ledger_credit"], "zero")

    def test_source_receipts_are_current(self):
        for receipt in self.payload["source_receipts"]:
            path = ROOT / receipt["path"]
            self.assertTrue(path.is_file(), receipt["path"])
            self.assertEqual(receipt["bytes"], path.stat().st_size)
            self.assertEqual(receipt["sha256"], hashlib.sha256(path.read_bytes()).hexdigest())

    def test_catalog_and_registry_route_the_companion(self):
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
        package = next(
            row for row in catalog["packages"]
            if row["astrology_id"] == "full-moon-family-triage-2026"
        )
        self.assertIn(reservoir.RESERVOIR_NOTE, package["artifact_refs"])
        registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        registered = [
            row for row in registry["artifacts"]
            if row["path"] == reservoir.RESERVOIR_NOTE
        ]
        self.assertEqual(len(registered), 1)
        self.assertIn("full-moon-family-triage-2026", registered[0]["astrology_ids"])

    def test_generated_artifact_matches_builder(self):
        stored = json.loads(reservoir.OUT.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.payload)


if __name__ == "__main__":
    unittest.main()
