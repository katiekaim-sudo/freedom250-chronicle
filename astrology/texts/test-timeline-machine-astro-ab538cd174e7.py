#!/usr/bin/env python3
"""Pure-provider and current-input parity tests for timeline_machine_astro."""
import hashlib
import json
import os
import unittest
from pathlib import Path

import build_castration_astro as castration
import build_fine_print_astro as fine_print
import timeline_machine_astro as subject

HERE = Path(__file__).resolve().parent
DATA_DIR = Path(os.environ.get("TIMELINE_ASTRO_FIXTURES", HERE))


class FakeSwe:
    SUN, MOON, MERCURY, VENUS, MARS = range(5)
    JUPITER, SATURN, URANUS, NEPTUNE, PLUTO = range(5, 10)
    TRUE_NODE, CHIRON = 10, 11
    FLG_MOSEPH, FLG_SPEED = 1, 2

    def __init__(self):
        self.julday_calls = []

    def julday(self, year, month, day, hour):
        self.julday_calls.append((year, month, day, hour))
        return year * 10000 + month * 100 + day + hour / 24

    def calc_ut(self, jd, code, flags=None):
        longitude = (code * 31.25 + jd % 1) % 360
        return ([longitude, 0, 0, -1 if code == self.MERCURY else 1],)

    def houses(self, jd, latitude, longitude, system):
        return ((), (123.456,))


class FakeWheel:
    @staticmethod
    def aspects_between(longitudes):
        return [{"t": "base", "o": 2.0}]

    @staticmethod
    def point_aspects(points, longitudes):
        name = next(iter(points))
        return [{"t": name, "o": {"Node": 1.5, "Chiron": 1.0, "America": 0.5}[name]}]


class FakeMinorPoints:
    def __init__(self, longitude=222.25, unavailable=False):
        self.longitude = longitude
        self.unavailable = unavailable

    def america_lon(self, jd):
        if self.unavailable:
            raise ValueError("outside grid")
        return self.longitude


class TimelineMachineAstroTests(unittest.TestCase):
    def test_time_convention_is_dst_aware_and_month_precision_is_chartless(self):
        fake = FakeSwe()
        subject.jd_for("2026-07-01", False, fake)
        subject.jd_for("2026-01-15", True, fake)
        self.assertEqual(fake.julday_calls, [(2026, 7, 1, 16.0), (2026, 1, 15, 5.0)])
        self.assertIsNone(subject.jd_for("2026-07", False, fake))

    def test_fake_provider_payload_preserves_schema_and_conventions(self):
        fake = FakeSwe()
        items = [
            {"date": "2026-07-01", "title": "release", "status": "Occurred"},
            {"date": "2026-01-15", "title": "deadline", "status": "Scheduled by rule"},
            {"date": "2026-07", "title": "month", "status": "Research"},
        ]
        payload, without_america = subject.build_payload(
            items, "comment", "generated", swe_module=fake, wheel_module=FakeWheel,
            minor_points_module=FakeMinorPoints(), dc=(1.0, 2.0))
        self.assertEqual(list(payload), ["_comment", "generated", "charts"])
        self.assertEqual(list(payload["charts"]),
                         ["2026-07-01|release", "2026-01-15|deadline"])
        self.assertEqual(payload["charts"]["2026-07-01|release"]["convention"], "noon D.C.")
        self.assertEqual(payload["charts"]["2026-01-15|deadline"]["convention"],
                         "midnight D.C. (day of)")
        positions = payload["charts"]["2026-07-01|release"]["pos"]
        by_name = {position[0]: position for position in positions}
        self.assertAlmostEqual((by_name["Node"][4] + 180) % 360, by_name["SNode"][4])
        self.assertIn("America", by_name)
        self.assertEqual(without_america, 0)

    def test_pre_grid_override_and_unavailable_grid_paths(self):
        fake = FakeSwe()
        key = "2023-01-01|event"
        overridden, missing = subject.build_payload(
            [{"date": "2023-01-01", "title": "event", "status": "Occurred"}], "c", "g",
            {key: 45.5}, fake, FakeWheel, FakeMinorPoints(unavailable=True), (1.0, 2.0))
        self.assertEqual(missing, 0)
        self.assertIn("America", [position[0] for position in overridden["charts"][key]["pos"]])
        no_override, missing = subject.build_payload(
            [{"date": "2023-01-01", "title": "event", "status": "Occurred"}], "c", "g",
            None, fake, FakeWheel, FakeMinorPoints(unavailable=True), (1.0, 2.0))
        self.assertEqual(missing, 1)
        self.assertNotIn("America", [position[0] for position in no_override["charts"][key]["pos"]])

    def assert_current_input_hash(self, family, comment, generated, expected_hash):
        seed = json.loads((DATA_DIR / f"{family}_seed.json").read_text(encoding="utf-8"))["items"]
        payload, _ = subject.build_payload(seed, comment, generated)
        actual_bytes = json.dumps(payload, ensure_ascii=False, indent=None).encode("utf-8")
        self.assertEqual(hashlib.sha256(actual_bytes).hexdigest(), expected_hash)

    def test_castration_current_input_is_byte_identical(self):
        self.assert_current_input_hash(
            "castration", castration.COMMENT, castration.GENERATED,
            "bc4de6066843ff2f65f26f78ed08211c7787480940c0cc8540fb1de5d1249194",
        )

    def test_fine_print_current_input_is_byte_identical(self):
        self.assert_current_input_hash(
            "fine_print", fine_print.COMMENT, fine_print.GENERATED,
            "7afe82a399c661d40c3f42c346419c631b5553ccef5ae9d7632241cfbe873e43",
        )


if __name__ == "__main__":
    unittest.main()
