#!/usr/bin/env python3
"""Invariant tests for the typed 2025-2026 eclipse genealogies."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = HERE / "eclipse_genealogies.json"


class EclipseGenealogyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads(DATA.read_text(encoding="utf-8"))
        cls.events = {event["date"]: event for event in cls.payload["events"]}

    def test_complete_ordered_sequence(self) -> None:
        self.assertEqual(
            [event["date"] for event in self.payload["events"]],
            [
                "2024-10-02",
                "2025-03-14",
                "2025-03-29",
                "2025-09-07",
                "2025-09-21",
                "2026-02-17",
                "2026-03-03",
                "2026-08-12",
                "2026-08-28",
            ],
        )

    def test_saros_family_preserves_series_not_calendar_date(self) -> None:
        for event in self.payload["events"]:
            current = event["current_eclipse"]
            family = event["saros_family"]
            self.assertEqual(family["series"], current["saros"])
            self.assertEqual(family["previous"]["saros"], current["saros"])
            self.assertEqual(family["next"]["saros"], current["saros"])
            self.assertAlmostEqual(
                abs(family["previous"]["interval_from_current_days"]),
                self.payload["constants"]["saros_mean_days"],
                delta=0.05,
            )

        self.assertEqual(
            self.events["2025-03-29"]["saros_family"]["previous"]["maximum"]["utc"][:10],
            "2007-03-19",
        )
        self.assertEqual(
            self.events["2026-03-03"]["saros_family"]["previous"]["maximum"]["utc"][:10],
            "2008-02-21",
        )

    def test_metonic_echo_is_close_in_degree_but_not_same_saros(self) -> None:
        for event in self.payload["events"]:
            previous = event["metonic_echo"]["previous"]
            self.assertLess(previous["absolute_degree_drift_from_current_deg"], 0.5)
            self.assertAlmostEqual(
                abs(previous["interval_from_current_days"]),
                self.payload["constants"]["metonic_mean_days"],
                delta=0.75,
            )
            if previous["is_eclipse"]:
                self.assertEqual(previous["saros_delta_from_current"], -10)
                self.assertNotEqual(
                    previous["eclipse"]["saros"], event["current_eclipse"]["saros"]
                )

    def test_high_value_metonic_examples_remain_typed(self) -> None:
        aries = self.events["2025-03-29"]["metonic_echo"]["previous"]
        self.assertEqual(aries["syzygy"]["utc"][:10], "2006-03-29")
        self.assertEqual(aries["eclipse"]["type"], "total")
        self.assertEqual(aries["eclipse"]["saros"], 139)
        self.assertEqual(self.events["2025-03-29"]["current_eclipse"]["saros"], 149)

        virgo = self.events["2026-03-03"]["metonic_echo"]["previous"]
        self.assertEqual(virgo["syzygy"]["utc"][:10], "2007-03-03")
        self.assertEqual(virgo["eclipse"]["saros"], 123)
        self.assertEqual(self.events["2026-03-03"]["current_eclipse"]["saros"], 133)

        pisces = self.events["2026-08-28"]["metonic_echo"]["previous"]
        self.assertEqual(pisces["syzygy"]["utc"][:10], "2007-08-28")
        self.assertEqual(pisces["eclipse"]["type"], "total")
        self.assertEqual(pisces["eclipse"]["saros"], 128)
        self.assertEqual(self.events["2026-08-28"]["current_eclipse"]["saros"], 138)

    def test_metonic_phase_return_need_not_be_an_eclipse(self) -> None:
        self.assertFalse(
            self.events["2026-02-17"]["metonic_echo"]["previous"]["is_eclipse"]
        )
        self.assertFalse(
            self.events["2026-08-12"]["metonic_echo"]["previous"]["is_eclipse"]
        )

    def test_saros_metonic_braid_is_one_anchor_with_two_branches(self) -> None:
        braided_dates = {
            "2024-10-02",
            "2025-03-14",
            "2025-03-29",
            "2025-09-07",
            "2025-09-21",
            "2026-03-03",
            "2026-08-28",
        }
        for date, event in self.events.items():
            braid = event["saros_metonic_braid"]
            if date not in braided_dates:
                self.assertIsNone(braid)
                continue
            self.assertIsNotNone(braid)
            self.assertEqual(braid["series_step_between_branches"], 10)
            self.assertAlmostEqual(
                braid["branch_separation_synodic_months"], 12.0, delta=0.03
            )
            self.assertGreater(braid["branch_separation_days"], 353.5)
            self.assertLess(braid["branch_separation_days"], 355.2)
            self.assertEqual(
                braid["shared_ancestor"]["saros"], braid["saros_branch"]["saros"]
            )

        self.assertEqual(
            self.events["2025-03-29"]["saros_metonic_braid"]["saros_branch"]
            ["maximum"]["utc"][:10],
            "2024-04-08",
        )
        self.assertEqual(
            self.events["2026-03-03"]["saros_metonic_braid"]["saros_branch"]
            ["maximum"]["utc"][:10],
            "2025-03-14",
        )

    def test_moon_family_is_a_third_identity_with_an_honest_null(self) -> None:
        for date, event in self.events.items():
            family = event["moon_family"]
            if date == "2025-09-21":
                self.assertEqual(
                    family["status"], "no_complete_lineage_in_current_projection"
                )
            else:
                self.assertEqual(family["status"], "complete_lineage_registered")
                self.assertTrue(family["lineage_id"].startswith("pessin:"))
                self.assertNotIn("saros", family)

    def test_mars_control_audit_uses_the_same_three_contexts_without_a_score(self) -> None:
        for event in self.payload["events"]:
            audit = event["mars_command_control_audit"]
            self.assertEqual(
                [context["label"] for context in audit["contexts"]],
                ["metonic_ancestor", "saros_ancestor", "current_eclipse"],
            )
            self.assertNotIn("score", audit)
            self.assertIn("no additive score", audit["contract"])
            for context in audit["contexts"]:
                self.assertIn("mars_in_command_structure", context)
                self.assertIn("root_members", context)
                self.assertEqual(len(context["planet_houses"]), 10)
                self.assertEqual(set(context["planet_houses"].values()).issubset(
                    set(range(1, 13))
                ), True)
                self.assertIn("out_of_bounds", context["mars"])
                geometry = context["distribution_geometry"]
                self.assertEqual(
                    geometry["status"],
                    "measurement_only_named_family_owner_unopened",
                )
                self.assertIsNone(geometry["family_label"])
                self.assertEqual(len(geometry["point_records"]), 10)
                self.assertEqual(len(geometry["circular_gaps"]), 10)
                self.assertAlmostEqual(geometry["gap_sum_deg"], 360.0, places=5)
                self.assertIn(
                    "applying_major_contacts_to_institutional_slow_bodies", context
                )

    def test_aries_lineage_has_three_distinct_mars_command_mechanisms(self) -> None:
        contexts = {
            context["label"]: context
            for context in self.events["2025-03-29"]["mars_command_control_audit"][
                "contexts"
            ]
        }
        metonic = contexts["metonic_ancestor"]
        saros = contexts["saros_ancestor"]
        current = contexts["current_eclipse"]

        self.assertTrue(metonic["mars_in_dispositor_root"])
        self.assertTrue(metonic["mars"]["out_of_bounds"])
        self.assertIn(
            ("Pluto", "opposition"),
            {
                (row["body"], row["aspect"])
                for row in metonic[
                    "applying_major_contacts_to_institutional_slow_bodies"
                ]
            },
        )

        self.assertTrue(saros["mars_rules_chart"])
        self.assertIn(
            ("Saturn", "opposition"),
            {
                (row["body"], row["aspect"])
                for row in saros[
                    "applying_major_contacts_to_institutional_slow_bodies"
                ]
            },
        )
        self.assertIn(
            ("Neptune", "conjunction"),
            {
                (row["body"], row["aspect"])
                for row in saros[
                    "applying_major_contacts_to_institutional_slow_bodies"
                ]
            },
        )

        self.assertTrue(current["mars_rules_chart"])
        self.assertTrue(current["mars_in_dispositor_root"])
        self.assertTrue(current["mars"]["out_of_bounds"])
        self.assertTrue(
            self.events["2025-03-29"]["mars_command_control_audit"]["summary"]
            ["all_three_in_command_structure"]
        )

    def test_aries_lineage_is_unique_inside_the_registered_control_set(self) -> None:
        comparison = self.payload["mars_command_control_comparison"]
        self.assertEqual(comparison["lineage_count"], 9)
        self.assertEqual(comparison["chart_context_count"], 27)
        self.assertEqual(
            comparison["all_three_command_structure_event_ids"],
            ["lun-2025-03-29-ne-solar"],
        )
        for field in (
            "command_structure_charts",
            "angular_mars_charts",
            "applying_slow_body_contact_charts",
        ):
            self.assertEqual(comparison["maxima"][field]["value"], 3)
            self.assertEqual(
                comparison["maxima"][field]["event_ids"],
                ["lun-2025-03-29-ne-solar"],
            )

    def test_aries_lineage_uniquely_keeps_mars_in_one_house(self) -> None:
        comparison = self.payload["house_distribution_comparison"]
        self.assertEqual(comparison["lineage_count"], 9)
        self.assertEqual(comparison["chart_context_count"], 27)
        self.assertEqual(
            comparison["same_mars_house_all_three_event_ids"],
            ["lun-2025-03-29-ne-solar"],
        )
        aries = next(
            row
            for row in comparison["rows"]
            if row["event_id"] == "lun-2025-03-29-ne-solar"
        )
        self.assertEqual(aries["mars_house_sequence"], [4, 4, 4])
        self.assertEqual(
            aries["context_order"],
            ["metonic_ancestor", "saros_ancestor", "current_eclipse"],
        )
        self.assertAlmostEqual(
            aries["largest_empty_arc_sequence_deg"][0], 103.507, places=3
        )
        self.assertAlmostEqual(
            aries["largest_empty_arc_sequence_deg"][1], 120.245, places=3
        )
        self.assertAlmostEqual(
            aries["largest_empty_arc_sequence_deg"][2], 190.723, places=3
        )

    def test_all_planet_control_limits_same_house_persistence_to_two_cases(self) -> None:
        comparison = self.payload["all_planet_house_persistence_comparison"]
        self.assertEqual(comparison["planet_count"], 10)
        self.assertEqual(comparison["lineage_count"], 9)
        self.assertEqual(comparison["planet_lineage_sequence_count"], 90)
        self.assertEqual(comparison["chart_placement_count"], 270)
        records = comparison["persistent_same_house_records"]
        self.assertEqual(
            [
                (record["event_id"], record["planet"], record["house"])
                for record in records
            ],
            [
                ("lun-2025-03-29-ne-solar", "Mars", 4),
                ("lun-2025-09-21-ne-solar", "Uranus", 6),
            ],
        )
        self.assertEqual(
            [
                (record["event_id"], record["planet"], record["house"])
                for record in comparison[
                    "classical_angular_command_persistence_records"
                ]
            ],
            [("lun-2025-03-29-ne-solar", "Mars", 4)],
        )


if __name__ == "__main__":
    unittest.main()
