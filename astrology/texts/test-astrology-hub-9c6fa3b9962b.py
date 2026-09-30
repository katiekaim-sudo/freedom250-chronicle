#!/usr/bin/env python3
"""Regression tests for the native Astrology Hub orientation."""

from __future__ import annotations

import json
import html
from pathlib import Path
import unittest

import build_sky_charts as hub
import build_astrology_files as astrology_files


HERE = Path(__file__).resolve().parent
VAULT_ROOT = HERE.parent
SHELL = VAULT_ROOT / "04 - Synthesis" / "Cross-cuts" / "Freedom 250 Observatory.html"


class AstrologyHubTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.atlas = json.loads(hub.PATTERN_ATLAS_PATH.read_text(encoding="utf-8"))
        cls.packet_index = json.loads(hub.WHOLE_CHART_PACKET_INDEX_PATH.read_text(encoding="utf-8"))
        cls.rendered = hub.render()
        cls.shell = SHELL.read_text(encoding="utf-8")

    def test_hub_is_first_native_route(self) -> None:
        first = hub.SUBVIEWS[0]
        self.assertEqual(first["sub"], "astrology-hub")
        self.assertEqual(first["legacy_views"], ("obs-sky-home",))
        self.assertIsNone(first["filename"])
        self.assertEqual(sum(row["filename"] is not None for row in hub.SUBVIEWS), 13)

    def test_registry_keeps_native_home_distinct_from_instruments(self) -> None:
        registry = hub.shell_registry()
        self.assertEqual(registry[0]["sub"], "astrology-hub")
        self.assertIsNone(registry[0]["filename"])
        self.assertTrue(all(row["filename"] for row in registry[1:]))
        self.assertEqual(len({row["sub"] for row in registry}), len(registry))

    def test_orientation_names_three_scales_and_five_moves(self) -> None:
        for phrase in (
            "The present sky",
            "The whole chart",
            "The pattern through time",
            "Name the governor.",
            "Read the whole chart.",
            "Trace inheritance.",
            "Add real motion.",
            "Compare the world last.",
        ):
            self.assertIn(phrase, self.rendered)

    def test_corrected_pattern_routes_are_the_front_door(self) -> None:
        # Katie's ruling 2026-09-25: the corrected pattern routes lead the hub; the living sky follows.
        front = self.rendered.index('class="hub-front"')
        self.assertLess(front, self.rendered.index('class="hub-orrery"'))
        self.assertIn("The corrected pattern routes", self.rendered)
        self.assertIn(html.escape(hub.THESIS_DOCUMENT, quote=True), self.rendered)
        self.assertLess(front, self.rendered.index('What did the 2025–2026 ingress and lunation charts say'))

    def test_orrery_is_the_front_door_and_depth_remains_below_it(self) -> None:
        self.assertLess(self.rendered.index('class="hub-orrery"'), self.rendered.index('id="hubExplore"'))
        for phrase in (
            "The living sky",
            "What is moving?",
            "Live sky",
            "Storylines",
            "Explore",
            "Schematic scale and pace",
            "Turn the real sky",
        ):
            self.assertIn(phrase, self.rendered)
        self.assertIn('data-open-orrery', self.rendered)
        self.assertIn('message:{action:"goToSub",sub:"orrery"}', self.rendered)

    def test_home_packet_clock_is_data_driven(self) -> None:
        self.assertIn('id="f250-hub-packets"', self.rendered)
        self.assertIn('function updateHubMoment(value)', self.rendered)
        self.assertIn('timeZone:"America/New_York"', self.rendered)
        for packet in self.packet_index["packets"]:
            self.assertIn(f'"chartId":"{packet["chart_id"]}"', self.rendered)

    def test_priority_routes_come_from_pattern_atlas(self) -> None:
        routes = sorted(self.atlas["priority_synthesis_routes"], key=lambda row: row["priority"])
        self.assertGreaterEqual(len(routes), 2)
        for route in routes:
            self.assertIn(route["question"], self.rendered)
            for step in route["next_work"]:
                self.assertIn(step, self.rendered)

    def test_whole_chart_shelf_comes_from_reference_only_packet_index(self) -> None:
        self.assertEqual(self.packet_index["counts"]["packet_count"], 30)
        self.assertIn("Choose one intact chart", self.rendered)
        for group in self.packet_index["groups"]:
            self.assertIn(group["label"], self.rendered)
        for packet in self.packet_index["packets"]:
            self.assertIn(packet["label"], self.rendered)
            self.assertIn(f'data-open-reading="{packet["chart_id"]}"', self.rendered)
        self.assertIn('message:{action:"selectReading",chart_id:readingButton.dataset.openReading}', self.rendered)

    def test_hub_routes_to_existing_owners(self) -> None:
        for sub in (
            "sky-calendar",
            "lunar-weather",
            "transit-weather",
            "ingress-charts",
            "chart-readings",
            "chart-comparison",
            "astrology-spine",
            "astrology-reference-room",
        ):
            self.assertIn(f'data-open-sub="{sub}"', self.rendered)
        self.assertIn(html.escape(hub.PATTERN_ATLAS_DOCUMENT, quote=True), self.rendered)
        self.assertIn('action:"openAstrologyDocument"', self.rendered)

    def test_boundary_is_explicit(self) -> None:
        self.assertIn("Computed sky, authored interpretation, prospective calls, and political evidence remain separate", self.rendered)
        self.assertIn("creates no second chart or interpretation", self.rendered)

    def test_shell_has_one_distinguished_astrology_doorway(self) -> None:
        self.assertIn('>Astrology<span class="obs-caret">', self.shell)
        self.assertIn('data-view="obs-sky::astrology-hub"', self.shell)
        self.assertNotIn('>Sky<span class="obs-caret">', self.shell)
        self.assertNotIn('>Charts<span class="obs-caret">', self.shell)

    def test_native_home_does_not_break_child_validation(self) -> None:
        hub.validate_registry(hub.CROSS_CUTS_DIR)

    def test_astrology_reader_hides_metadata_and_renders_the_governing_quote(self) -> None:
        rendered = astrology_files.safe_markdown(
            "---\ntitle: Hidden metadata\n---\n# Visible title\n\n> First line\n> second line\n"
        )
        self.assertNotIn("Hidden metadata", rendered)
        self.assertIn("<h1>Visible title</h1>", rendered)
        self.assertIn("<blockquote><p>First line second line</p></blockquote>", rendered)


if __name__ == "__main__":
    unittest.main()
