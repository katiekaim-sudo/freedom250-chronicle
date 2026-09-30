#!/usr/bin/env python3
"""Parity and fail-closed tests for the one-owner Ingress projector."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import add_mundane_midpoints as projector


class IngressProjectorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.source = projector.read_exact(projector.TARGET)
        cls.meanings, cls.tech = projector.load_lexicon()

    def project(self, source: str | None = None) -> str:
        return projector.project(source or self.source, self.meanings, self.tech)

    def test_projection_is_idempotent_and_single_owner(self) -> None:
        projected = self.project()
        self.assertEqual(projector.project(projected, self.meanings, self.tech), projected)
        self.assertEqual(projected.count(projector.NATIVE_START), 1)
        self.assertEqual(projected.count(projector.NATIVE_END), 1)
        self.assertEqual(projected.count(projector.MARKER_START), 1)
        self.assertEqual(projected.count(projector.MARKER_END), 1)
        self.assertEqual(projected.count('class="native-wheel" data-chart='), 1)
        self.assertLess(
            projected.index(projector.NATIVE_START),
            projected.index(projector.MARKER_START),
        )

    def test_canonical_wheel_and_live_midpoint_lexicon_are_projected(self) -> None:
        projected = self.project()
        self.assertIn(projector.WHEEL_JS, projected)
        self.assertIn(projector.build_block(self.meanings, self.tech).rstrip("\n"), projected)
        self.assertIn("var MM_ORB  = 1.0", projected)
        self.assertIn("var MM_CRISIS=", projected)

    def test_chart_payloads_are_not_rewritten(self) -> None:
        projected = self.project()
        ingress_start = self.source.index("const INGRESS_DATA = [")
        ingress_end = self.source.index("\n];", ingress_start) + 3
        overlay_start = self.source.index("const ING_DATA = [")
        overlay_end = self.source.index(";", overlay_start) + 1
        self.assertEqual(
            projected[ingress_start:ingress_end],
            self.source[ingress_start:ingress_end],
        )
        self.assertIn(self.source[overlay_start:overlay_end], projected)

    def test_duplicate_or_unbalanced_markers_fail_closed(self) -> None:
        duplicate = self.source.replace(
            projector.NATIVE_START,
            projector.NATIVE_START + projector.NATIVE_START,
            1,
        )
        with self.assertRaises(SystemExit):
            self.project(duplicate)
        unbalanced = self.source.replace(projector.MARKER_END, "", 1)
        with self.assertRaises(SystemExit):
            self.project(unbalanced)
        reversed_markers = self.source.replace(
            projector.MARKER_START, "F250-MIDPOINT-TEMP", 1
        ).replace(
            projector.MARKER_END, projector.MARKER_START, 1
        ).replace(
            "F250-MIDPOINT-TEMP", projector.MARKER_END, 1
        )
        with self.assertRaises(SystemExit):
            self.project(reversed_markers)

    def test_missing_owned_blocks_are_reinserted_in_order(self) -> None:
        source = self.source
        for start, end in (
            (projector.NATIVE_START, projector.NATIVE_END),
            (projector.MARKER_START, projector.MARKER_END),
        ):
            begin = source.index(start)
            finish = source.index(end, begin) + len(end)
            source = source[:begin] + source[finish:]
        projected = self.project(source)
        self.assertEqual(projected.count(projector.NATIVE_START), 1)
        self.assertEqual(projected.count(projector.MARKER_START), 1)
        self.assertLess(
            projected.index(projector.NATIVE_START),
            projected.index(projector.MARKER_START),
        )

    def test_atomic_write_preserves_target_mode(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw) / "Ingress Charts.html"
            target.write_text("before", encoding="utf-8")
            target.chmod(0o644)
            projector.atomic_write(target, "after")
            self.assertEqual(target.read_text(encoding="utf-8"), "after")
            self.assertEqual(target.stat().st_mode & 0o777, 0o644)


if __name__ == "__main__":
    unittest.main()
