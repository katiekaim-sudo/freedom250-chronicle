#!/usr/bin/env python3
"""Build typed eclipse genealogies for the registered 2025-2026 sequence.

An eclipse can participate in three different time families that answer three
different questions:

* a Saros lineage repeats eclipse geometry after 223 synodic months;
* a Metonic echo returns the same lunar phase near the same calendar date and
  tropical-zodiac degree after 235 synodic months;
* a Pessin Moon Family follows one New-Moon seed through the roughly
  273/546/819-day First Quarter, Full and Last Quarter phases.

The producer keeps those identities separate.  It does not infer political
continuity or award evidence credit.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import swisseph as swe

from build_eclipse_local_circumstances import (
    EVENTS,
    GEOPOS,
    event_type,
    instant,
    syzygy_near,
)


HERE = Path(__file__).resolve().parent
LOCAL_DATA = HERE / "eclipse_local_circumstances.json"
MOON_FAMILY_DATA = HERE / "moon_lineages.json"
OUT = HERE / "eclipse_genealogies.json"

MEAN_SYNODIC_MONTH_DAYS = 29.530588853
SAROS_MONTHS = 223
METONIC_MONTHS = 235
SAROS_DAYS = SAROS_MONTHS * MEAN_SYNODIC_MONTH_DAYS
METONIC_DAYS = METONIC_MONTHS * MEAN_SYNODIC_MONTH_DAYS
TROPICAL_YEAR_DAYS = 365.24219
SIGNS = (
    "Aries",
    "Taurus",
    "Gemini",
    "Cancer",
    "Leo",
    "Virgo",
    "Libra",
    "Scorpio",
    "Sagittarius",
    "Capricorn",
    "Aquarius",
    "Pisces",
)
PLANETS = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mercury": swe.MERCURY,
    "Venus": swe.VENUS,
    "Mars": swe.MARS,
    "Jupiter": swe.JUPITER,
    "Saturn": swe.SATURN,
    "Uranus": swe.URANUS,
    "Neptune": swe.NEPTUNE,
    "Pluto": swe.PLUTO,
}
RULER = {
    "Aries": "Mars",
    "Taurus": "Venus",
    "Gemini": "Mercury",
    "Cancer": "Moon",
    "Leo": "Sun",
    "Virgo": "Mercury",
    "Libra": "Venus",
    "Scorpio": "Mars",
    "Sagittarius": "Jupiter",
    "Capricorn": "Saturn",
    "Aquarius": "Saturn",
    "Pisces": "Jupiter",
}
MAJOR_ASPECTS = (
    ("conjunction", 0.0),
    ("sextile", 60.0),
    ("square", 90.0),
    ("trine", 120.0),
    ("opposition", 180.0),
)
INSTITUTIONAL_SLOW_BODIES = ("Saturn", "Neptune", "Pluto")
TRADITIONAL_PLANETS = (
    "Sun",
    "Moon",
    "Mercury",
    "Venus",
    "Mars",
    "Jupiter",
    "Saturn",
)
CONTROL_ASPECT_ORB_DEG = 6.0
DECLINATION_ORB_DEG = 1.0


def rounded(value: float, places: int = 6) -> float:
    return round(float(value), places)


def signed_delta_deg(source: float, target: float) -> float:
    """Return target minus source on the shortest signed zodiac arc."""

    return (target - source + 180.0) % 360.0 - 180.0


def longitude_record(longitude: float) -> dict:
    longitude %= 360.0
    sign_index = int(longitude // 30.0)
    return {
        "longitude_deg": rounded(longitude, 9),
        "sign": SIGNS[sign_index],
        "degree_in_sign": rounded(longitude % 30.0, 6),
    }


def syzygy_positions(jd: float, kind: str) -> dict:
    sun = swe.calc_ut(jd, swe.SUN, swe.FLG_SWIEPH)[0][0]
    moon = swe.calc_ut(jd, swe.MOON, swe.FLG_SWIEPH)[0][0]
    reference = sun if kind == "solar" else moon
    return {
        "sun": longitude_record(sun),
        "moon": longitude_record(moon),
        "eclipse_degree_reference": "Sun-Moon conjunction" if kind == "solar" else "Moon",
        "eclipse_degree": longitude_record(reference),
    }


def sign_of(longitude: float) -> str:
    return SIGNS[int((longitude % 360.0) // 30.0)]


def whole_sign_house(longitude: float, ascendant: float) -> int:
    return (int((longitude % 360.0) // 30.0) - int((ascendant % 360.0) // 30.0)) % 12 + 1


def distribution_geometry(positions: dict[str, dict]) -> dict:
    """Return exact ten-planet circular geometry without a shape-family label.

    The live chart engine has no admitted Jones/Meyer family classifier.  This
    audit therefore carries only reproducible point, gap and occupied-span
    measurements; it cannot silently recreate a retired label.
    """

    points = sorted(
        (
            (positions[body]["longitude_deg"] % 360.0, body)
            for body in PLANETS
        ),
        key=lambda row: (row[0], row[1]),
    )
    gaps = []
    for index, (start, from_body) in enumerate(points):
        end, to_body = points[(index + 1) % len(points)]
        gaps.append(
            {
                "from_body": from_body,
                "to_body": to_body,
                "start_longitude_deg": rounded(start, 6),
                "end_longitude_deg": rounded(end, 6),
                "arc_deg": rounded((end - start) % 360.0, 6),
                "wraps_zero": end <= start,
            }
        )
    gap_sum = sum(gap["arc_deg"] for gap in gaps)
    if abs(gap_sum - 360.0) > 0.00002:
        raise RuntimeError(
            f"Ten-planet circular gaps do not sum to 360 degrees: {gap_sum}"
        )
    largest = max(gaps, key=lambda gap: gap["arc_deg"])
    return {
        "status": "measurement_only_named_family_owner_unopened",
        "point_set": "ten_planets_jones_meyer",
        "point_records": [
            {
                "body": body,
                "longitude_deg": rounded(longitude, 6),
            }
            for longitude, body in points
        ],
        "circular_gaps": gaps,
        "gap_sum_deg": rounded(gap_sum, 6),
        "largest_empty_arc": largest,
        "occupied_span_deg": rounded(360.0 - largest["arc_deg"], 6),
        "family_label": None,
        "automatic_evidence_credit": 0,
    }


def nearest_major_aspect(longitude_a: float, longitude_b: float) -> tuple[str, float, float]:
    separation = abs(signed_delta_deg(longitude_a, longitude_b))
    aspect, angle = min(MAJOR_ASPECTS, key=lambda row: abs(separation - row[1]))
    return aspect, angle, abs(separation - angle)


def dispositor_root(chart_ruler: str, positions: dict[str, dict]) -> tuple[list[str], list[str]]:
    path: list[str] = []
    seen: dict[str, int] = {}
    current = chart_ruler
    while current not in seen:
        seen[current] = len(path)
        path.append(current)
        current = RULER[positions[current]["sign"]]
    return path + [current], path[seen[current]:]


def mars_command_context(label: str, syzygy: dict) -> dict:
    """Return a transparent Mars/control comparison for one exact syzygy chart.

    This is deliberately not a chart score.  It exposes a fixed set of
    inspectable conditions so one lineage can be compared with the other seven
    without changing the criteria after seeing the Aries result.
    """

    jd = syzygy["jd_ut"]
    flags = swe.FLG_SWIEPH | swe.FLG_SPEED
    equatorial_flags = flags | swe.FLG_EQUATORIAL
    positions: dict[str, dict] = {}
    future_longitudes: dict[str, float] = {}
    for name, code in PLANETS.items():
        ecliptic = swe.calc_ut(jd, code, flags)[0]
        equatorial = swe.calc_ut(jd, code, equatorial_flags)[0]
        longitude = ecliptic[0] % 360.0
        positions[name] = {
            "longitude_deg": longitude,
            "speed_deg_per_day": ecliptic[3],
            "declination_deg": equatorial[1],
            "sign": sign_of(longitude),
        }
        future_longitudes[name] = swe.calc_ut(
            jd + 1.0 / 24.0, code, swe.FLG_SWIEPH
        )[0][0] % 360.0

    _cusps, ascmc = swe.houses(jd, GEOPOS[1], GEOPOS[0], b"W")
    ascendant, midheaven = ascmc[0] % 360.0, ascmc[1] % 360.0
    for position in positions.values():
        position["house"] = whole_sign_house(position["longitude_deg"], ascendant)

    chart_ruler = RULER[sign_of(ascendant)]
    chain, root_members = dispositor_root(chart_ruler, positions)
    true_obliquity = swe.calc_ut(jd, swe.ECL_NUT)[0][0]
    mars = positions["Mars"]

    applying_contacts = []
    declination_contacts = []
    for body in INSTITUTIONAL_SLOW_BODIES:
        aspect, angle, orb = nearest_major_aspect(
            mars["longitude_deg"], positions[body]["longitude_deg"]
        )
        if orb <= CONTROL_ASPECT_ORB_DEG:
            _future_aspect, _future_angle, future_orb = nearest_major_aspect(
                future_longitudes["Mars"], future_longitudes[body]
            )
            if future_orb < orb:
                applying_contacts.append(
                    {
                        "body": body,
                        "aspect": aspect,
                        "orb_deg": rounded(orb, 6),
                    }
                )

        parallel_orb = abs(mars["declination_deg"] - positions[body]["declination_deg"])
        contra_orb = abs(mars["declination_deg"] + positions[body]["declination_deg"])
        kind, declination_orb = min(
            (("parallel", parallel_orb), ("contra-parallel", contra_orb)),
            key=lambda row: row[1],
        )
        if declination_orb <= DECLINATION_ORB_DEG:
            declination_contacts.append(
                {
                    "body": body,
                    "kind": kind,
                    "orb_deg": rounded(declination_orb, 6),
                }
            )

    in_root = "Mars" in root_members
    rules_chart = chart_ruler == "Mars"
    return {
        "label": label,
        "syzygy": syzygy,
        "ascendant": longitude_record(ascendant),
        "midheaven": longitude_record(midheaven),
        "chart_ruler": chart_ruler,
        "dispositor_chain": chain,
        "root_members": root_members,
        "planet_houses": {
            body: positions[body]["house"] for body in PLANETS
        },
        "mars_in_command_structure": rules_chart or in_root,
        "mars_rules_chart": rules_chart,
        "mars_in_dispositor_root": in_root,
        "mars": {
            **longitude_record(mars["longitude_deg"]),
            "house": mars["house"],
            "angular": mars["house"] in (1, 4, 7, 10),
            "declination_deg": rounded(mars["declination_deg"], 6),
            "true_obliquity_deg": rounded(true_obliquity, 6),
            "out_of_bounds": abs(mars["declination_deg"]) > true_obliquity,
        },
        "distribution_geometry": distribution_geometry(positions),
        "applying_major_contacts_to_institutional_slow_bodies": applying_contacts,
        "declination_contacts_to_institutional_slow_bodies": declination_contacts,
    }


def mars_lineage_audit(
    current_syzygy: dict, previous_saros: dict, previous_metonic: dict
) -> dict:
    contexts = [
        mars_command_context("metonic_ancestor", previous_metonic["syzygy"]),
        mars_command_context("saros_ancestor", previous_saros["syzygy"]),
        mars_command_context("current_eclipse", current_syzygy),
    ]
    return {
        "contract": (
            "Diagnostic criteria fixed before running the eight-lineage comparison "
            "but prompted by the observed Aries pattern; no additive score, "
            "statistical-proof claim, or political or causal evidence credit"
        ),
        "criteria": {
            "command_structure": "Mars rules the Ascendant or belongs to the chart-ruler dispositor root",
            "angular": "Mars occupies a Whole Sign angle: houses 1, 4, 7 or 10",
            "out_of_bounds": "absolute Mars declination exceeds the true obliquity at the syzygy",
            "applying_contact": (
                "Mars applies within 6 degrees to a major longitude aspect with "
                "Saturn, Neptune or Pluto"
            ),
            "declination_contact": (
                "Mars is parallel or contra-parallel Saturn, Neptune or Pluto "
                "within 1 degree"
            ),
        },
        "contexts": contexts,
        "summary": {
            "command_structure_charts": sum(
                context["mars_in_command_structure"] for context in contexts
            ),
            "angular_mars_charts": sum(context["mars"]["angular"] for context in contexts),
            "out_of_bounds_mars_charts": sum(
                context["mars"]["out_of_bounds"] for context in contexts
            ),
            "applying_slow_body_contact_charts": sum(
                bool(context["applying_major_contacts_to_institutional_slow_bodies"])
                for context in contexts
            ),
            "declination_slow_body_contact_charts": sum(
                bool(context["declination_contacts_to_institutional_slow_bodies"])
                for context in contexts
            ),
            "all_three_in_command_structure": all(
                context["mars_in_command_structure"] for context in contexts
            ),
        },
    }


def mars_control_comparison(records: list[dict]) -> dict:
    fields = (
        "command_structure_charts",
        "angular_mars_charts",
        "out_of_bounds_mars_charts",
        "applying_slow_body_contact_charts",
        "declination_slow_body_contact_charts",
    )
    rows = [
        {
            "event_id": record["event_id"],
            "date": record["date"],
            "kind": record["kind"],
            **record["mars_command_control_audit"]["summary"],
        }
        for record in records
    ]
    maxima = {
        field: {
            "value": max(row[field] for row in rows),
            "event_ids": [
                row["event_id"]
                for row in rows
                if row[field] == max(item[field] for item in rows)
            ],
        }
        for field in fields
    }
    return {
        "status": "diagnostic_control_not_preregistered_statistical_test",
        "population": f"{len(records)} registered 2024-2026 eclipse lineages",
        "lineage_count": len(rows),
        "chart_context_count": len(rows) * 3,
        "rows": rows,
        "all_three_command_structure_event_ids": [
            row["event_id"] for row in rows if row["all_three_in_command_structure"]
        ],
        "maxima": maxima,
        "boundary": (
            "The comparison tests whether the observed Aries Mars structure is "
            "common inside this registered eclipse set. It is not an independent "
            "preregistration, significance test, political forecast or causal claim."
        ),
    }


def house_distribution_comparison(records: list[dict]) -> dict:
    """Compare house continuity and raw distribution across all lineages."""

    rows = []
    for record in records:
        contexts = record["mars_command_control_audit"]["contexts"]
        houses = [context["mars"]["house"] for context in contexts]
        empty_arcs = [
            context["distribution_geometry"]["largest_empty_arc"]["arc_deg"]
            for context in contexts
        ]
        rows.append(
            {
                "event_id": record["event_id"],
                "date": record["date"],
                "kind": record["kind"],
                "context_order": [context["label"] for context in contexts],
                "mars_house_sequence": houses,
                "same_mars_house_all_three": len(set(houses)) == 1,
                "largest_empty_arc_sequence_deg": empty_arcs,
                "occupied_span_sequence_deg": [
                    context["distribution_geometry"]["occupied_span_deg"]
                    for context in contexts
                ],
                "empty_arc_range_deg": rounded(max(empty_arcs) - min(empty_arcs), 6),
            }
        )
    return {
        "status": "descriptive_control_no_named_shape_family",
        "population": f"{len(records)} registered 2024-2026 eclipse lineages",
        "lineage_count": len(rows),
        "chart_context_count": len(rows) * 3,
        "context_order": [
            "metonic_ancestor",
            "saros_ancestor",
            "current_eclipse",
        ],
        "rows": rows,
        "same_mars_house_all_three_event_ids": [
            row["event_id"] for row in rows if row["same_mars_house_all_three"]
        ],
        "boundary": (
            "Whole Sign houses are Washington-time-and-place staging. Largest "
            "empty arc and occupied span are exact ten-planet geometry only. "
            "No Jones/Meyer family label, score, political forecast, causal claim "
            "or evidence credit is generated."
        ),
    }


def all_planet_house_persistence_comparison(records: list[dict]) -> dict:
    """Test the observed Mars house repetition against every planet-lineage pair."""

    rows = []
    persistent_records = []
    for record in records:
        contexts = record["mars_command_control_audit"]["contexts"]
        sequences = {
            planet: [context["planet_houses"][planet] for context in contexts]
            for planet in PLANETS
        }
        persistent = []
        for planet, houses in sequences.items():
            if len(set(houses)) != 1:
                continue
            command_all_three = planet in TRADITIONAL_PLANETS and all(
                planet == context["chart_ruler"]
                or planet in context["root_members"]
                for context in contexts
            )
            item = {
                "planet": planet,
                "house": houses[0],
                "house_sequence": houses,
                "traditional_planet": planet in TRADITIONAL_PLANETS,
                "angular_all_three": all(
                    house in (1, 4, 7, 10) for house in houses
                ),
                "traditional_command_structure_all_three": command_all_three,
            }
            persistent.append(item)
            persistent_records.append(
                {
                    "event_id": record["event_id"],
                    "date": record["date"],
                    "kind": record["kind"],
                    **item,
                }
            )
        rows.append(
            {
                "event_id": record["event_id"],
                "date": record["date"],
                "kind": record["kind"],
                "context_order": [context["label"] for context in contexts],
                "planet_house_sequences": sequences,
                "persistent_same_house_records": persistent,
            }
        )
    return {
        "status": "descriptive_post_observation_control_not_statistical_test",
        "population": f"ten planets across {len(records)} registered eclipse lineages",
        "planet_count": len(PLANETS),
        "lineage_count": len(rows),
        "planet_lineage_sequence_count": len(PLANETS) * len(rows),
        "chart_placement_count": len(PLANETS) * len(rows) * 3,
        "context_order": [
            "metonic_ancestor",
            "saros_ancestor",
            "current_eclipse",
        ],
        "rows": rows,
        "persistent_same_house_records": persistent_records,
        "classical_angular_command_persistence_records": [
            record
            for record in persistent_records
            if record["traditional_planet"]
            and record["angular_all_three"]
            and record["traditional_command_structure_all_three"]
        ],
        "boundary": (
            "The all-planet control was run after observing the Aries Mars "
            "pattern. It measures exact Washington Whole Sign house persistence "
            "only; it is not a preregistration, strength score, political forecast, "
            "causal claim or evidence vote."
        ),
    }


def global_eclipse_after(kind: str, start_jd: float) -> dict:
    if kind == "solar":
        flags, times = swe.sol_eclipse_when_glob(start_jd)
        maximum = times[0]
        _where_flags, _geopos, attr = swe.sol_eclipse_where(maximum)
        series = int(attr[9])
        member = int(attr[10])
    else:
        flags, times = swe.lun_eclipse_when(start_jd)
        maximum = times[0]
        _how_flags, attr = swe.lun_eclipse_how(maximum, GEOPOS)
        series = int(attr[9])
        member = int(attr[10])
    target = 0.0 if kind == "solar" else 180.0
    syzygy = syzygy_near(maximum, target)
    return {
        "kind": kind,
        "type": event_type(flags),
        "maximum": instant(maximum),
        "syzygy": instant(syzygy),
        "saros": series,
        "saros_member_engine_value": member,
        "positions_at_syzygy": syzygy_positions(syzygy, kind),
    }


def eclipse_near_syzygy(kind: str, syzygy_jd: float) -> dict | None:
    event = global_eclipse_after(kind, syzygy_jd - 1.0)
    if abs(event["syzygy"]["jd_ut"] - syzygy_jd) > 1.0:
        return None
    return event


def saros_neighbor(kind: str, maximum_jd: float, series: int, direction: int) -> dict:
    estimate = maximum_jd + direction * SAROS_DAYS
    event = global_eclipse_after(kind, estimate - 3.0)
    if abs(event["maximum"]["jd_ut"] - estimate) > 7.0:
        raise RuntimeError(f"No {kind} Saros neighbor near JD {estimate}")
    if event["saros"] != series:
        raise RuntimeError(
            f"Expected Saros {series} near JD {estimate}; found {event['saros']}"
        )
    event["interval_from_current_days"] = rounded(
        event["maximum"]["jd_ut"] - maximum_jd, 6
    )
    return event


def metonic_echo(kind: str, current_syzygy_jd: float, current_degree: float, direction: int) -> dict:
    target_angle = 0.0 if kind == "solar" else 180.0
    estimate = current_syzygy_jd + direction * METONIC_DAYS
    echo_syzygy = syzygy_near(estimate, target_angle)
    positions = syzygy_positions(echo_syzygy, kind)
    echo_degree = positions["eclipse_degree"]["longitude_deg"]
    eclipse = eclipse_near_syzygy(kind, echo_syzygy)
    interval_days = echo_syzygy - current_syzygy_jd
    return {
        "kind": kind,
        "phase": "New Moon" if kind == "solar" else "Full Moon",
        "syzygy": instant(echo_syzygy),
        "positions_at_syzygy": positions,
        "interval_from_current_days": rounded(interval_days, 6),
        "interval_from_current_tropical_years": rounded(
            interval_days / TROPICAL_YEAR_DAYS, 9
        ),
        "signed_degree_drift_from_current_deg": rounded(
            signed_delta_deg(current_degree, echo_degree), 6
        ),
        "absolute_degree_drift_from_current_deg": rounded(
            abs(signed_delta_deg(current_degree, echo_degree)), 6
        ),
        "is_eclipse": eclipse is not None,
        "eclipse": eclipse,
    }


def chart_id(date_iso: str, kind: str) -> str:
    suffix = "ne-solar" if kind == "solar" else "fu-lunar"
    return f"lun-{date_iso}-{suffix}"


def moon_family_for(date_iso: str, kind: str, moon_data: dict) -> dict:
    current_id = chart_id(date_iso, kind)
    matches = []
    for lineage in moon_data["lineages"]:
        for member in lineage["members"]:
            if member.get("phase_event_id") == current_id:
                matches.append((lineage, member))
    if not matches:
        return {
            "status": "no_complete_lineage_in_current_projection",
            "current_phase_event_id": current_id,
            "explanation": (
                "moon_lineages.json admits only seeds with a complete same-sign, "
                "within-6-degree 273/546/819-day chain inside its calculation horizon"
            ),
        }
    if len(matches) != 1:
        raise RuntimeError(f"Expected at most one Moon Family for {current_id}; found {len(matches)}")
    lineage, member = matches[0]
    return {
        "status": "complete_lineage_registered",
        "lineage_id": lineage["lineage_id"],
        "seed_chart_id": lineage["seed_chart_id"],
        "degree_band": lineage["degree_band"],
        "current_phase_event_id": member["phase_event_id"],
        "current_role": member["role"],
        "elapsed_days_from_seed": member["elapsed_days_from_seed"],
        "zodiac_distance_from_seed_deg": member["zodiac_distance_from_seed_deg"],
        "members": lineage["members"],
        "interpretation_status": lineage["interpretation_status"],
        "story_verdict": lineage["story_verdict"],
    }


def event_record(local: dict, moon_data: dict) -> dict:
    date_iso = local["date"]
    kind = local["kind"]
    current_max = local["global"]["maximum"]["jd_ut"]
    current_syzygy = local["global"]["syzygy"]["jd_ut"]
    current_positions = syzygy_positions(current_syzygy, kind)
    current_degree = current_positions["eclipse_degree"]["longitude_deg"]
    current_saros = local["global"]["saros"]

    previous_metonic = metonic_echo(kind, current_syzygy, current_degree, -1)
    next_metonic = metonic_echo(kind, current_syzygy, current_degree, 1)
    previous_saros = saros_neighbor(kind, current_max, current_saros, -1)
    next_saros = saros_neighbor(kind, current_max, current_saros, 1)
    for echo in (previous_metonic, next_metonic):
        if echo["eclipse"] is not None:
            echo["saros_delta_from_current"] = echo["eclipse"]["saros"] - current_saros
        else:
            echo["saros_delta_from_current"] = None

    braid = None
    if previous_metonic["eclipse"] is not None:
        anchor = previous_metonic["eclipse"]
        saros_branch = saros_neighbor(
            kind,
            anchor["maximum"]["jd_ut"],
            anchor["saros"],
            1,
        )
        braid = {
            "identity_rule": (
                "one ancestral eclipse branches to a same-Saros return after 223 "
                "lunations and a Metonic return after 235 lunations"
            ),
            "shared_ancestor": anchor,
            "saros_branch": saros_branch,
            "metonic_branch": {
                "event_id": chart_id(date_iso, kind),
                "maximum": local["global"]["maximum"],
                "syzygy": local["global"]["syzygy"],
                "type": local["global"]["type"],
                "saros": current_saros,
            },
            "branch_separation_days": rounded(
                current_syzygy - saros_branch["syzygy"]["jd_ut"], 6
            ),
            "branch_separation_synodic_months": rounded(
                (current_syzygy - saros_branch["syzygy"]["jd_ut"])
                / MEAN_SYNODIC_MONTH_DAYS,
                6,
            ),
            "series_step_between_branches": current_saros - anchor["saros"],
        }

    return {
        "event_id": chart_id(date_iso, kind),
        "date": date_iso,
        "kind": kind,
        "current_eclipse": {
            "type": local["global"]["type"],
            "maximum": local["global"]["maximum"],
            "syzygy": local["global"]["syzygy"],
            "saros": current_saros,
            "saros_member_engine_value": local["global"][
                "saros_member_engine_value"
            ],
            "positions_at_syzygy": current_positions,
        },
        "saros_family": {
            "identity_rule": "same eclipse series after 223 synodic months",
            "series": current_saros,
            "previous": previous_saros,
            "next": next_saros,
        },
        "metonic_echo": {
            "identity_rule": (
                "same lunar phase near the same calendar date and tropical-zodiac "
                "degree after 235 synodic months; not the same Saros"
            ),
            "previous": previous_metonic,
            "next": next_metonic,
        },
        "saros_metonic_braid": braid,
        "moon_family": moon_family_for(date_iso, kind, moon_data),
        "mars_command_control_audit": mars_lineage_audit(
            local["global"]["syzygy"], previous_saros, previous_metonic
        ),
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path, default=OUT)
    args = parser.parse_args(argv)
    swe.set_ephe_path(str(HERE / "ephe"))
    local_payload = json.loads(LOCAL_DATA.read_text(encoding="utf-8"))
    moon_data = json.loads(MOON_FAMILY_DATA.read_text(encoding="utf-8"))
    expected = list(EVENTS)
    actual = [(event["date"], event["kind"]) for event in local_payload["events"]]
    if actual != expected:
        raise RuntimeError("Local eclipse source does not match the registered sequence")

    records = [event_record(event, moon_data) for event in local_payload["events"]]
    payload = {
        "schema_version": 1,
        "title": "Three typed eclipse genealogies, 2025-2026",
        "authority": "computed_context_zero_astrological_or_political_evidence_credit",
        "engine": {
            "name": "Swiss Ephemeris",
            "version": swe.version,
            "ephemeris_path": "99 - Templates/ephe",
        },
        "constants": {
            "mean_synodic_month_days": MEAN_SYNODIC_MONTH_DAYS,
            "saros_synodic_months": SAROS_MONTHS,
            "saros_mean_days": rounded(SAROS_DAYS, 9),
            "metonic_synodic_months": METONIC_MONTHS,
            "metonic_mean_days": rounded(METONIC_DAYS, 9),
            "tropical_year_days": TROPICAL_YEAR_DAYS,
        },
        "family_contract": {
            "saros": {
                "answers": "Which eclipses belong to the same evolving shadow-geometry series?",
                "identity": "same Saros number",
                "must_not_be_used_as": "proof of the same calendar date, locality or political story",
            },
            "metonic": {
                "answers": "When does the same lunar phase return near the same calendar date and zodiac degree?",
                "identity": "235-synodic-month phase echo",
                "must_not_be_used_as": "the same shadow path or the same Saros series",
            },
            "moon_family": {
                "answers": "Which 273/546/819-day chapter belongs to one New-Moon seed?",
                "identity": "Pessin seed, First Quarter, Full and Last Quarter lineage",
                "must_not_be_used_as": "a Saros or Metonic recurrence or an independent evidence vote",
            },
            "saros_metonic_braid": {
                "answers": (
                    "When does one ancestral eclipse split into a same-Saros return "
                    "and, about one lunar year later, a different-Saros Metonic return?"
                ),
                "identity": "shared ancestral eclipse with 223- and 235-lunation branches",
                "must_not_be_used_as": "two independent evidence votes or proof of one political storyline",
            },
        },
        "method_notes": [
            "Greatest eclipse and exact Sun-Moon syzygy remain separate instants.",
            "Metonic echoes are solved from exact phase geometry, not inferred from matching civil dates.",
            "An echo is labeled an eclipse only when a global eclipse maximum belongs to that syzygy.",
            "The relevant eclipse degree is the Sun-Moon conjunction for solar eclipses and the Moon for lunar eclipses.",
            "Saros member is retained as an engine value because external catalogs can use a different member count.",
            "Moon-family facts are imported from moon_lineages.json without adding a continuity verdict.",
            "No family identity supplies political continuity, causal proof, forecast credit or an additional evidence vote.",
            "The Saros-Metonic branch gap is 12 synodic months because 235 minus 223 equals 12.",
            "The Mars command/control audit applies one fixed three-chart protocol to every lineage and reports conditions rather than an additive chart score.",
            "Mars command structure means chart rulership or membership in the chart-ruler dispositor root; it is not a strength rating.",
            "The house/distribution comparison uses Washington Whole Sign houses and exact ten-planet circular gaps; it does not calculate a named Jones/Meyer chart-shape family.",
            "The all-planet house-persistence control compares all eighty planet-lineage sequences after observing the Aries Mars pattern; it is descriptive rather than an independent statistical test.",
        ],
        "source_urls": [
            "https://eclipse.gsfc.nasa.gov/SEsaros/SEperiodicity.html",
            "https://eclipse.gsfc.nasa.gov/LEsaros/LEperiodicity.html",
            "https://eclipse.gsfc.nasa.gov/solar.html",
            "https://eclipse.gsfc.nasa.gov/lunar.html",
            "https://www.astro.com/swisseph/swephprg.htm",
        ],
        "source_files": [
            "99 - Templates/eclipse_local_circumstances.json",
            "99 - Templates/moon_lineages.json",
        ],
        "mars_command_control_comparison": mars_control_comparison(records),
        "house_distribution_comparison": house_distribution_comparison(records),
        "all_planet_house_persistence_comparison": (
            all_planet_house_persistence_comparison(records)
        ),
        "events": records,
    }
    content = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        clean = args.output.exists() and args.output.read_text(encoding="utf-8") == content
        print("ECLIPSE GENEALOGY CHECK: CLEAN" if clean else "ECLIPSE GENEALOGY CHECK: STALE")
        return 0 if clean else 1
    args.output.write_text(content, encoding="utf-8")
    print(f"Wrote {args.output}")
    for record in records:
        previous_saros = record["saros_family"]["previous"]
        previous_metonic = record["metonic_echo"]["previous"]
        metonic_eclipse = previous_metonic["eclipse"]
        print(
            record["date"],
            record["kind"],
            f"Saros {record['current_eclipse']['saros']} <- {previous_saros['maximum']['utc'][:10]}",
            f"Metonic <- {previous_metonic['syzygy']['utc'][:10]}",
            f"Saros {metonic_eclipse['saros'] if metonic_eclipse else 'none'}",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
