#!/usr/bin/env python3
"""Build the March 2025 Aries-eclipse Moon-family structural comparison.

The comparison keeps the registered seed, +273-day First Quarter, and
+546-day Full phase as three distinct clocks.  It computes Washington Whole
Sign staging, traditional dispositor circuits, ten-planet distribution,
standing wheel-policy aspects, and one-degree declination contacts.  The
output is astronomical/astrological context only: it assigns no causal,
forecast, political-continuity, or evidence credit.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import swisseph as swe

from build_aries_mars_pluto_choreography import (
    FLAGS,
    cast_chart,
    julian_day,
    parse_utc,
    rounded,
    signed_motion,
)
from wheel_lib import aspects_between


HERE = Path(__file__).resolve().parent
MOON_LINEAGES = HERE / "moon_lineages.json"
MARS_PLUTO_CHOREOGRAPHY = HERE / "aries_mars_pluto_choreography.json"
OUT = HERE / "aries_eclipse_moon_family.json"
LINEAGE_ID = "pessin:lun-2025-03-29-ne-solar"
ROLE_ORDER = ("seed", "first_quarter", "full")


def distribution(chart: dict) -> dict:
    ordered = sorted(
        (
            record["longitude_deg"],
            body,
        )
        for body, record in chart["positions"].items()
    )
    gaps = []
    for index, (longitude, body) in enumerate(ordered):
        next_longitude, next_body = ordered[(index + 1) % len(ordered)]
        gap = (next_longitude - longitude) % 360.0
        gaps.append((gap, body, next_body, longitude, next_longitude))
    gap, start_body, end_body, start_longitude, end_longitude = max(gaps)
    return {
        "largest_empty_arc_deg": rounded(gap, 6),
        "occupied_span_deg": rounded(360.0 - gap, 6),
        "empty_arc_from": {
            "body": start_body,
            "longitude_deg": rounded(start_longitude, 6),
        },
        "empty_arc_to": {
            "body": end_body,
            "longitude_deg": rounded(end_longitude, 6),
        },
        "boundary": (
            "Raw circular distribution only; no Jones/Meyer or other named "
            "shape family is assigned."
        ),
    }


def declination_contacts(chart: dict) -> list[dict]:
    rows = []
    positions = chart["positions"]
    for first, second in itertools.combinations(positions, 2):
        first_declination = positions[first]["declination_deg"]
        second_declination = positions[second]["declination_deg"]
        orb = abs(abs(first_declination) - abs(second_declination))
        if orb <= 1.0 + 1e-9:
            rows.append(
                {
                    "first": first,
                    "second": second,
                    "relationship": (
                        "parallel"
                        if first_declination * second_declination >= 0.0
                        else "contra_parallel"
                    ),
                    "orb_deg": rounded(orb, 6),
                    "first_declination_deg": first_declination,
                    "second_declination_deg": second_declination,
                }
            )
    return sorted(rows, key=lambda row: (row["orb_deg"], row["first"], row["second"]))


def chart_record(member: dict, phase_events: dict[str, dict]) -> dict:
    phase_event = phase_events[member["phase_event_id"]]
    chart = cast_chart(parse_utc(phase_event["exact_utc"]))
    longitudes = {
        body: record["longitude_deg"] for body, record in chart["positions"].items()
    }
    return {
        "role": member["role"],
        "phase_event_id": member["phase_event_id"],
        "chart_id": member["chart_id"],
        "exact_utc": phase_event["exact_utc"],
        "exact_local": phase_event["exact_local"],
        "elapsed_days_from_seed": member["elapsed_days_from_seed"],
        "zodiac_distance_from_seed_deg": member["zodiac_distance_from_seed_deg"],
        "governing_ingress_id": member["governing_ingress_id"],
        "chart": chart,
        "longitude_aspects": aspects_between(longitudes),
        "declination_contacts": declination_contacts(chart),
        "distribution": distribution(chart),
    }


def aspect_orb(longitude: float, reference: float, target_angle: float) -> float:
    separation = abs((longitude - reference + 180.0) % 360.0 - 180.0)
    return abs(separation - target_angle)


def nodal_separation_control(records: list[dict]) -> dict:
    rows = []
    for record in records:
        jd = julian_day(parse_utc(record["exact_utc"]))
        north_node = swe.calc_ut(jd, swe.TRUE_NODE, FLAGS)[0][0] % 360.0
        south_node = (north_node + 180.0) % 360.0
        moon = record["chart"]["positions"]["Moon"]
        sun = record["chart"]["positions"]["Sun"]
        moon_to_north = abs(signed_motion(north_node, moon["longitude_deg"]))
        moon_to_south = abs(signed_motion(south_node, moon["longitude_deg"]))
        sun_to_north = abs(signed_motion(north_node, sun["longitude_deg"]))
        sun_to_south = abs(signed_motion(south_node, sun["longitude_deg"]))
        rows.append(
            {
                "role": record["role"],
                "phase_event_id": record["phase_event_id"],
                "exact_utc": record["exact_utc"],
                "true_north_node_longitude_deg": rounded(north_node, 9),
                "true_south_node_longitude_deg": rounded(south_node, 9),
                "moon_longitude_deg": moon["longitude_deg"],
                "moon_ecliptic_latitude_deg": moon["latitude_deg"],
                "moon_nearest_node": (
                    "north" if moon_to_north <= moon_to_south else "south"
                ),
                "moon_nearest_node_separation_deg": rounded(
                    min(moon_to_north, moon_to_south), 6
                ),
                "sun_nearest_node": (
                    "north" if sun_to_north <= sun_to_south else "south"
                ),
                "sun_nearest_node_separation_deg": rounded(
                    min(sun_to_north, sun_to_south), 6
                ),
                "sun_moon_elongation_deg": rounded(
                    abs(signed_motion(sun["longitude_deg"], moon["longitude_deg"])),
                    6,
                ),
                "shadow_state": (
                    "registered_partial_solar_eclipse"
                    if record["role"] == "seed"
                    else "non_eclipse_moon_family_phase"
                ),
            }
        )

    seed, first_quarter, full = rows
    return {
        "status": "computed_astronomy_context_zero_forecast_or_evidence_credit",
        "members": rows,
        "monotonic_checks": {
            "moon_nearest_node_separation_increases": all(
                earlier["moon_nearest_node_separation_deg"]
                < later["moon_nearest_node_separation_deg"]
                for earlier, later in zip(rows, rows[1:])
            ),
            "absolute_moon_ecliptic_latitude_increases": all(
                abs(earlier["moon_ecliptic_latitude_deg"])
                < abs(later["moon_ecliptic_latitude_deg"])
                for earlier, later in zip(rows, rows[1:])
            ),
        },
        "seed_to_full": {
            "true_north_node_motion_deg": rounded(
                signed_motion(
                    seed["true_north_node_longitude_deg"],
                    full["true_north_node_longitude_deg"],
                ),
                6,
            ),
            "moon_family_longitude_motion_deg": rounded(
                signed_motion(seed["moon_longitude_deg"], full["moon_longitude_deg"]),
                6,
            ),
            "nearest_node_separation_increase_deg": rounded(
                full["moon_nearest_node_separation_deg"]
                - seed["moon_nearest_node_separation_deg"],
                6,
            ),
            "absolute_moon_latitude_increase_deg": rounded(
                abs(full["moon_ecliptic_latitude_deg"])
                - abs(seed["moon_ecliptic_latitude_deg"]),
                6,
            ),
        },
        "interpretive_boundary": (
            "The 273/546-day Moon-family phase clock is not an eclipse-recurrence "
            "clock. The registered partial-solar-eclipse seed matures through a "
            "non-eclipse First Quarter and Full Moon while the lights move farther "
            "from the lunar-node axis and the Moon's absolute ecliptic latitude "
            "increases. This supports the literal distinction between shadowed seed "
            "and unshadowed illumination; it does not add a vote, prove political "
            "continuity, or make the later phase stronger because it is farther from "
            "the node."
        ),
    }


def cross_cycle_relay(records: list[dict], choreography: dict) -> dict:
    members = {row["role"]: row for row in records}
    anchors = {row["event_id"]: row for row in choreography["anchors"]}
    conjunction = anchors["mars-pluto-conjunction-seed"]
    opposition = anchors["mars-opposite-pluto"]
    reference = conjunction["chart"]["positions"]["Pluto"]["longitude_deg"]

    rows = []

    def add(
        event_id: str,
        point: str,
        longitude: float,
        aspect: str,
        target_angle: float,
        policy_orb: float = 1.0,
        note: str | None = None,
    ) -> None:
        orb = aspect_orb(longitude, reference, target_angle)
        rows.append(
            {
                "event_id": event_id,
                "point": point,
                "longitude_deg": rounded(longitude, 9),
                "relationship_to_mars_pluto_seed": aspect,
                "orb_deg": rounded(orb, 6),
                "orb_arcmin": rounded(orb * 60.0, 3),
                "policy_orb_deg": policy_orb,
                "admitted_under_policy": orb <= policy_orb + 1e-9,
                "note": note,
            }
        )

    add(
        members["seed"]["phase_event_id"],
        "Pluto",
        members["seed"]["chart"]["positions"]["Pluto"]["longitude_deg"],
        "same_degree",
        0.0,
        note="The eclipse seed already places Pluto on the later conjunction coordinate.",
    )
    add(
        members["first_quarter"]["phase_event_id"],
        "Pluto",
        members["first_quarter"]["chart"]["positions"]["Pluto"]["longitude_deg"],
        "same_degree",
        0.0,
        note="Pluto remains inside the one-degree corridor at the contextual First Quarter.",
    )
    add(
        conjunction["event_id"],
        "Mars and Pluto",
        reference,
        "conjunction_seed",
        0.0,
        note="Reference coordinate for the 2026 Mars-Pluto family.",
    )
    add(
        members["full"]["phase_event_id"],
        "Pluto",
        members["full"]["chart"]["positions"]["Pluto"]["longitude_deg"],
        "same_degree",
        0.0,
    )
    add(
        members["full"]["phase_event_id"],
        "Moon",
        members["full"]["chart"]["positions"]["Moon"]["longitude_deg"],
        "sextile",
        60.0,
        policy_orb=0.5,
    )
    add(
        members["full"]["phase_event_id"],
        "Sun",
        members["full"]["chart"]["positions"]["Sun"]["longitude_deg"],
        "trine",
        120.0,
        policy_orb=0.5,
    )
    add(
        opposition["event_id"],
        "Pluto",
        opposition["chart"]["positions"]["Pluto"]["longitude_deg"],
        "same_degree",
        0.0,
    )
    add(
        members["first_quarter"]["phase_event_id"],
        "MC",
        members["first_quarter"]["chart"]["midheaven"]["longitude_deg"],
        "same_degree",
        0.0,
        note=(
            "The First-Quarter MC is a disclosed threshold miss: close to the corridor "
            "but outside the one-degree angle-to-seed policy."
        ),
    )
    return {
        "reference_event_id": conjunction["event_id"],
        "reference_longitude_deg": rounded(reference, 9),
        "reference_sign": "Aquarius",
        "reference_degree_in_sign": rounded(reference % 30.0, 6),
        "contacts": rows,
        "boundary": (
            "This is a direct geometry bridge between two independently owned clocks. "
            "It does not merge the Moon family with the Mars-Pluto family or supply "
            "another evidence or forecast vote."
        ),
    }


def build_payload() -> dict:
    source = json.loads(MOON_LINEAGES.read_text(encoding="utf-8"))
    choreography = json.loads(MARS_PLUTO_CHOREOGRAPHY.read_text(encoding="utf-8"))
    lineage = next(row for row in source["lineages"] if row["lineage_id"] == LINEAGE_ID)
    phase_events = {row["phase_event_id"]: row for row in source["phase_events"]}
    members = {row["role"]: row for row in lineage["members"]}
    records = [chart_record(members[role], phase_events) for role in ROLE_ORDER]
    return {
        "schema": "freedom250.aries-eclipse-moon-family.v2",
        "lineage_id": LINEAGE_ID,
        "degree_band": lineage["degree_band"],
        "interpretation_status": lineage["interpretation_status"],
        "source": "99 - Templates/moon_lineages.json",
        "method": {
            "location": "Washington, D.C.",
            "houses": "Whole Sign",
            "rulers": "traditional",
            "longitude_aspects": (
                "wheel_lib standing policy: three-degree major cap, two degrees "
                "for Moon contacts and semisextiles"
            ),
            "declination_contacts": "parallel or contra-parallel within one degree",
            "boundary": (
                "The registered phase clocks and computed charts provide context only. "
                "They do not establish political continuity, causation, forecast credit, "
                "or a separate event vote."
            ),
        },
        "members": records,
        "cross_cycle_degree_relay": cross_cycle_relay(records, choreography),
        "nodal_separation_control": nodal_separation_control(records),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    content = json.dumps(build_payload(), indent=2, ensure_ascii=False) + "\n"
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != content:
            raise SystemExit(f"stale generated artifact: {OUT}")
        print(f"OK: {OUT}")
        return
    OUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
