from __future__ import annotations

import json
import unittest
from pathlib import Path

import build_whole_chart_packet_index as packets


ROOT = Path(__file__).resolve().parent.parent


class WholeChartPacketIndexTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = packets.build_payload()
        cls.history = json.loads((ROOT / packets.SOURCES["history"]).read_text(encoding="utf-8"))
        cls.bones = json.loads((ROOT / packets.SOURCES["bones_index"]).read_text(encoding="utf-8"))
        cls.history_by_id = {row["id"]: row for row in cls.history["charts"]}
        cls.bone_by_id = {row["id"]: row for row in cls.bones["charts"]}
        cls.packet_by_id = {row["chart_id"]: row for row in cls.payload["packets"]}

    def test_complete_registered_population_and_groups(self) -> None:
        self.assertEqual(self.payload["schema"], "freedom250.whole-chart-packet-index/v1")
        self.assertEqual(self.payload["counts"]["packet_count"], 30)
        self.assertEqual(self.payload["counts"]["ingress_packet_count"], 5)
        self.assertEqual(self.payload["counts"]["lunation_packet_count"], 25)
        self.assertEqual(
            {row["chart_id"] for row in self.payload["packets"]},
            set(self.bone_by_id),
        )
        self.assertEqual(
            [(row["group_id"], row["packet_count"]) for row in self.payload["groups"]],
            [("ingress_governors", 5), ("new_moon_seeds", 12), ("full_moon_culminations", 13)],
        )

    def test_identity_clocks_readings_and_bones_are_exact_routes(self) -> None:
        for chart_id, packet in self.packet_by_id.items():
            history = self.history_by_id[chart_id]
            self.assertEqual(packet["exact_clock"]["utc"], history["utc"])
            self.assertEqual(packet["exact_clock"]["local"], history["local"])
            self.assertEqual(packet["reading_ref"]["source"], history["reading_source"])
            self.assertEqual(
                packet["reading_ref"]["selection_message"],
                {"action": "selectReading", "chart_id": chart_id},
            )
            self.assertTrue((ROOT / packet["bones_ref"]["path"]).is_file())

    def test_reference_only_boundary_has_no_chart_payloads(self) -> None:
        forbidden_keys = {"positions", "houses", "aspects", "points", "placidus_cusps", "root_members"}

        def walk(value):
            if isinstance(value, dict):
                self.assertTrue(forbidden_keys.isdisjoint(value.keys()))
                for child in value.values():
                    walk(child)
            elif isinstance(value, list):
                for child in value:
                    walk(child)

        walk(self.payload["packets"])
        self.assertFalse(self.payload["authority_boundary"]["chart_payload_copied"])

    def test_ingress_governance_is_typed_without_false_self_inheritance(self) -> None:
        for chart_id, packet in self.packet_by_id.items():
            governor = packet["governing_ingress_ref"]
            if packet["chart_type"] == "ingress":
                self.assertEqual(governor["state"], "this_packet_establishes_governance")
                self.assertEqual(governor["chart_id"], chart_id)
            else:
                expected = self.history_by_id[chart_id]["governing_ingress_id"]
                self.assertEqual(governor["state"], "governed_lunation")
                self.assertEqual(governor["chart_id"], expected)

    def test_lineage_counts_and_aries_full_moon_routes(self) -> None:
        self.assertEqual(self.payload["counts"]["moon_family_link_count"], 13)
        self.assertEqual(self.payload["counts"]["eclipse_genealogy_link_count"], 4)
        aries = self.packet_by_id["lun-2026-09-26-fu"]
        self.assertEqual(aries["governing_ingress_ref"]["chart_id"], "ingress-2026-libra")
        self.assertEqual(
            {row["pattern_id"] for row in aries["applicable_pattern_refs"]},
            {
                "aries_full_moon_mars_pluto_sequence",
                "barbault_basket_ai_arc",
                "thirteen_moon_family_harvests",
                "distributed_field_recursive_command",
            },
        )
        self.assertEqual(
            aries["lunation_or_eclipse_lineage_refs"][0]["lineage_id"],
            "pessin:lun-2025-03-29-ne-solar",
        )

    def test_2026_physical_geometry_is_complete_and_inherited_2025_governor_is_explicit(self) -> None:
        for chart_id, packet in self.packet_by_id.items():
            for key in ("inner_planet_motion_ref", "outer_planet_geometry_ref"):
                state = packet["analysis_refs"][key]["state"]
                if chart_id == "ingress-2025-capricorn":
                    self.assertEqual(state, "not_in_control_population")
                else:
                    self.assertEqual(state, "available")

    def test_source_receipts_are_unique_and_current(self) -> None:
        receipts = self.payload["source_receipts"]
        paths = [row["path"] for row in receipts]
        self.assertEqual(paths, sorted(set(paths)))
        for row in receipts:
            if row["path"] == packets.SOURCES["synodic_stacks"]:
                self.assertEqual(row["charts_sha256"], packets.stacks_charts_sha256())
            else:
                self.assertEqual(row["sha256"], packets.sha256(row["path"]))

    def test_generated_artifact_matches_builder(self) -> None:
        stored = json.loads(packets.OUT.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.payload)


if __name__ == "__main__":
    unittest.main()
