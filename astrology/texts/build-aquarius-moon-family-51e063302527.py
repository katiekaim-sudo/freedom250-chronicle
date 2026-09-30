#!/usr/bin/env python3
"""Build the January 2025 Aquarius Moon-family comparison.

The output is calculation evidence for a contextual reread. It does not edit
the locked July 29, 2026 Full-Moon reading and grants astrology no factual,
causal, convergence, or Forecast Ledger credit.
"""

from __future__ import annotations

import datetime as dt
import json
import math
from pathlib import Path

import swisseph as swe


HERE = Path(__file__).resolve().parent
HISTORY = HERE / "mundane_history.json"
LINEAGES = HERE / "moon_lineages.json"
FULL_BONE = HERE / "chart_reading_bones" / "lun-2026-07-29-fu.json"
OUTPUT = HERE / "aquarius_moon_family_2025_2026.json"

PLANETS = (
    "Sun", "Moon", "Mercury", "Venus", "Mars",
    "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto",
)
SWE_PLANETS = {
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
SIGNS = (
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces",
)
RULERS = {
    "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury",
    "Cancer": "Moon", "Leo": "Sun", "Virgo": "Mercury",
    "Libra": "Venus", "Scorpio": "Mars", "Sagittarius": "Jupiter",
    "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter",
}
ASPECTS = (
    ("conjunction", 0.0), ("sextile", 60.0), ("square", 90.0),
    ("trine", 120.0), ("opposition", 180.0),
)
WASHINGTON = {"latitude": 38.9072, "longitude": -77.0369}


def parse_utc(value: str) -> dt.datetime:
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def jd_for(moment: dt.datetime) -> float:
    moment = moment.astimezone(dt.timezone.utc)
    hour = moment.hour + moment.minute / 60 + (moment.second + moment.microsecond / 1e6) / 3600
    return swe.julday(moment.year, moment.month, moment.day, hour)


def sign(lon: float) -> str:
    return SIGNS[int((lon % 360) // 30)]


def whole_sign_house(lon: float, asc: float) -> int:
    return ((int((lon % 360) // 30) - int((asc % 360) // 30)) % 12) + 1


def angular_distance(a: float, b: float) -> float:
    return abs((a - b + 180.0) % 360.0 - 180.0)


def sky_separation(a: dict, b: dict) -> float:
    ra1, dec1 = math.radians(a["right_ascension_deg"]), math.radians(a["declination_deg"])
    ra2, dec2 = math.radians(b["right_ascension_deg"]), math.radians(b["declination_deg"])
    cosine = math.sin(dec1) * math.sin(dec2) + math.cos(dec1) * math.cos(dec2) * math.cos(ra1 - ra2)
    return math.degrees(math.acos(max(-1.0, min(1.0, cosine))))


def aspects(positions: dict[str, float], max_orb: float = 3.0) -> list[dict]:
    rows: list[dict] = []
    for index, a in enumerate(PLANETS):
        for b in PLANETS[index + 1:]:
            separation = angular_distance(positions[a], positions[b])
            kind, angle = min(ASPECTS, key=lambda item: abs(separation - item[1]))
            orb = abs(separation - angle)
            if orb <= max_orb:
                rows.append({
                    "a": a,
                    "b": b,
                    "kind": kind,
                    "orb_deg": round(orb, 6),
                    "separation_deg": round(separation, 6),
                })
    return sorted(rows, key=lambda row: (row["orb_deg"], row["a"], row["b"]))


def declination_pairs(declinations: dict[str, float], max_orb: float = 1.0) -> list[dict]:
    rows: list[dict] = []
    for index, a in enumerate(PLANETS):
        for b in PLANETS[index + 1:]:
            orb = abs(abs(declinations[a]) - abs(declinations[b]))
            if orb <= max_orb:
                rows.append({
                    "a": a,
                    "b": b,
                    "kind": "parallel" if declinations[a] * declinations[b] >= 0 else "contra_parallel",
                    "orb_deg": round(orb, 6),
                    "declination_a_deg": round(declinations[a], 6),
                    "declination_b_deg": round(declinations[b], 6),
                })
    return sorted(rows, key=lambda row: (row["orb_deg"], row["a"], row["b"]))


def distribution(positions: dict[str, float]) -> dict:
    ordered = sorted((lon % 360, name) for name, lon in positions.items())
    gaps = []
    for index, (lon, name) in enumerate(ordered):
        next_lon, next_name = ordered[(index + 1) % len(ordered)]
        gap = (next_lon - lon) % 360
        gaps.append((gap, name, next_name))
    gap, from_body, to_body = max(gaps)
    return {
        "largest_empty_arc_deg": round(gap, 6),
        "occupied_span_deg": round(360.0 - gap, 6),
        "empty_arc_from_body": from_body,
        "empty_arc_to_body": to_body,
        "named_shape_policy": "withheld; raw ten-body distribution only",
    }


def dispositor_map(positions: dict[str, float]) -> dict:
    routes = {body: RULERS[sign(lon)] for body, lon in positions.items()}
    finals = sorted(body for body, ruler in routes.items() if body == ruler)
    cycles: set[tuple[str, ...]] = set()
    for start in PLANETS:
        path: list[str] = []
        current = start
        while current not in path:
            path.append(current)
            current = routes[current]
        cycle = path[path.index(current):]
        rotations = [tuple(cycle[i:] + cycle[:i]) for i in range(len(cycle))]
        cycles.add(min(rotations))
    return {
        "routes": routes,
        "final_dispositors": finals,
        "bounded_cycles": [list(cycle) for cycle in sorted(cycles)],
    }


def calculated_chart(moment: dt.datetime) -> dict:
    jd = jd_for(moment)
    flags = swe.FLG_SWIEPH | swe.FLG_SPEED
    _, ascmc = swe.houses_ex(jd, WASHINGTON["latitude"], WASHINGTON["longitude"], b"P")
    asc, mc = ascmc[0], ascmc[1]
    positions: dict[str, float] = {}
    bodies: dict[str, dict] = {}
    declinations: dict[str, float] = {}
    for body in PLANETS:
        vector, _ = swe.calc_ut(jd, SWE_PLANETS[body], flags)
        equatorial, _ = swe.calc_ut(jd, SWE_PLANETS[body], flags | swe.FLG_EQUATORIAL)
        _, true_altitude, apparent_altitude = swe.azalt(
            jd,
            swe.EQU2HOR,
            (WASHINGTON["longitude"], WASHINGTON["latitude"], 0.0),
            0.0,
            10.0,
            (equatorial[0], equatorial[1], equatorial[2]),
        )
        lon = vector[0] % 360
        positions[body] = lon
        declinations[body] = equatorial[1]
        bodies[body] = {
            "longitude_deg": round(lon, 9),
            "sign": sign(lon),
            "degree_in_sign": round(lon % 30, 9),
            "speed_deg_per_day": round(vector[3], 9),
            "retrograde": vector[3] < 0,
            "ecliptic_latitude_deg": round(vector[1], 9),
            "distance_au": round(vector[2], 9),
            "right_ascension_deg": round(equatorial[0], 9),
            "declination_deg": round(equatorial[1], 9),
            "true_altitude_deg": round(true_altitude, 9),
            "apparent_altitude_deg": round(apparent_altitude, 9),
            "whole_sign_house": whole_sign_house(lon, asc),
        }
    return {
        "exact_utc": moment.astimezone(dt.timezone.utc).isoformat().replace("+00:00", "Z"),
        "julian_day_ut": round(jd, 9),
        "ascendant_deg": round(asc, 9),
        "ascendant_sign": sign(asc),
        "mc_deg": round(mc, 9),
        "mc_sign": sign(mc),
        "bodies": bodies,
        "aspects_within_3_deg": aspects(positions),
        "declination_relationships_within_1_deg": declination_pairs(declinations),
        "distribution": distribution(positions),
        "dispositors": dispositor_map(positions),
    }


def apply_governed_positions(
    chart: dict,
    positions: dict[str, float],
    *,
    asc: float | None = None,
    mc: float | None = None,
    declinations: dict[str, float] | None = None,
) -> dict:
    """Replace fresh-call longitudes with the corpus-owned exact coordinates."""
    if asc is not None:
        chart["ascendant_deg"] = round(asc % 360, 9)
        chart["ascendant_sign"] = sign(asc)
    if mc is not None:
        chart["mc_deg"] = round(mc % 360, 9)
        chart["mc_sign"] = sign(mc)
    ascendant = chart["ascendant_deg"]
    for body, lon in positions.items():
        lon %= 360
        chart["bodies"][body]["longitude_deg"] = round(lon, 9)
        chart["bodies"][body]["sign"] = sign(lon)
        chart["bodies"][body]["degree_in_sign"] = round(lon % 30, 9)
        chart["bodies"][body]["whole_sign_house"] = whole_sign_house(lon, ascendant)
        if declinations and body in declinations:
            chart["bodies"][body]["declination_deg"] = round(declinations[body], 9)
    governed_positions = {body: chart["bodies"][body]["longitude_deg"] for body in PLANETS}
    governed_declinations = {body: chart["bodies"][body]["declination_deg"] for body in PLANETS}
    chart["aspects_within_3_deg"] = aspects(governed_positions)
    chart["declination_relationships_within_1_deg"] = declination_pairs(governed_declinations)
    chart["distribution"] = distribution(governed_positions)
    chart["dispositors"] = dispositor_map(governed_positions)
    return chart


def cross_chart_contacts(a: dict, b: dict, max_orb: float = 1.0) -> list[dict]:
    rows: list[dict] = []
    for body_a in PLANETS:
        lon_a = a["bodies"][body_a]["longitude_deg"]
        for body_b in PLANETS:
            lon_b = b["bodies"][body_b]["longitude_deg"]
            separation = angular_distance(lon_a, lon_b)
            kind, angle = min(ASPECTS, key=lambda item: abs(separation - item[1]))
            orb = abs(separation - angle)
            if orb <= max_orb:
                rows.append({
                    "from_body": body_a,
                    "to_body": body_b,
                    "kind": kind,
                    "orb_deg": round(orb, 6),
                })
    return sorted(rows, key=lambda row: (row["orb_deg"], row["from_body"], row["to_body"]))


def main() -> None:
    history = json.loads(HISTORY.read_text())
    lineages = json.loads(LINEAGES.read_text())
    seed_source = next(row for row in history["charts"] if row["id"] == "lun-2025-01-29-ne")
    lineage = next(row for row in lineages["lineages"] if row["lineage_id"] == "pessin:lun-2025-01-29-ne")
    phase_index = {row["phase_event_id"]: row for row in lineages["phase_events"]}
    quarter_source = phase_index["lunation-2025-10-29-fq"]
    full_source = phase_index["lun-2026-07-29-fu"]
    full_bone = json.loads(FULL_BONE.read_text())

    seed = calculated_chart(parse_utc(seed_source["utc"]))
    quarter = calculated_chart(parse_utc(quarter_source["exact_utc"]))
    full = calculated_chart(parse_utc(full_source["exact_utc"]))
    seed = apply_governed_positions(
        seed,
        {row["name"]: row["lon"] for row in seed_source["points"] if row["name"] in PLANETS},
        asc=seed_source["asc"],
        mc=seed_source["mc"],
    )
    quarter = apply_governed_positions(
        quarter,
        {"Sun": quarter_source["sun_lon_deg"], "Moon": quarter_source["moon_lon_deg"]},
    )
    full = apply_governed_positions(
        full,
        {body: full_bone["pos"][body]["lon"] for body in PLANETS},
        asc=full_bone["asc"],
        mc=full_bone["mc"],
        declinations={body: full_bone["pos"][body]["dec"] for body in PLANETS},
    )

    quarter_full_delta = angular_distance(
        quarter["bodies"]["Moon"]["longitude_deg"],
        full["bodies"]["Moon"]["longitude_deg"],
    )
    horizon_summary = {}
    for name, chart in (("seed", seed), ("first_quarter", quarter), ("full", full)):
        above = [body for body in PLANETS if chart["bodies"][body]["true_altitude_deg"] > 0]
        horizon_summary[name] = {
            "above_true_horizon": above,
            "below_or_on_true_horizon": [body for body in PLANETS if body not in above],
            "above_count": len(above),
            "below_or_on_count": len(PLANETS) - len(above),
        }
    full_geometry = {
        "sun_jupiter_true_sky_separation_deg": round(sky_separation(full["bodies"]["Sun"], full["bodies"]["Jupiter"]), 6),
        "moon_pluto_true_sky_separation_deg": round(sky_separation(full["bodies"]["Moon"], full["bodies"]["Pluto"]), 6),
        "sun_pluto_true_sky_separation_deg": round(sky_separation(full["bodies"]["Sun"], full["bodies"]["Pluto"]), 6),
        "moon_jupiter_true_sky_separation_deg": round(sky_separation(full["bodies"]["Moon"], full["bodies"]["Jupiter"]), 6),
        "jupiter_solar_elongation_deg": round(sky_separation(full["bodies"]["Sun"], full["bodies"]["Jupiter"]), 6),
        "pluto_solar_elongation_deg": round(sky_separation(full["bodies"]["Sun"], full["bodies"]["Pluto"]), 6),
        "scale_boundary": "geocentric angular geometry and local altitude supply physical context only; they do not prove astrological causation or assign interpretive weight",
    }
    result = {
        "schema": "freedom250.aquarius-moon-family/v1",
        "developed_through": "2026-09-25",
        "lineage_id": lineage["lineage_id"],
        "interpretation_status_before_reread": lineage["interpretation_status"],
        "story_verdict_before_reread": lineage["story_verdict"],
        "authority_boundary": {
            "calculation": "Registered longitudes and angles inherit governed mundane_history, moon_lineages and chart-bone coordinates; Swiss Ephemeris supplies the missing First-Quarter frame and secondary quantities",
            "verification": "Astro Gold remains pending where the source registry says pending",
            "interpretation": "contextual companion only; locked Pass 1 remains unchanged",
            "evidence_credit": "zero",
        },
        "family_members": lineage["members"],
        "charts": {
            "seed_2025_01_29": seed,
            "first_quarter_2025_10_29": quarter,
            "full_2026_07_29": full,
        },
        "degree_relays": {
            "seed_moon_degree_deg": round(seed["bodies"]["Moon"]["degree_in_sign"], 9),
            "first_quarter_moon_degree_deg": round(quarter["bodies"]["Moon"]["degree_in_sign"], 9),
            "full_moon_degree_deg": round(full["bodies"]["Moon"]["degree_in_sign"], 9),
            "first_quarter_to_full_moon_delta_deg": round(quarter_full_delta, 9),
            "first_quarter_to_full_moon_delta_arcsec": round(quarter_full_delta * 3600, 3),
            "meaning_boundary": "exact coordinate relay inside one Moon family; not an additional factual or causal vote",
        },
        "cross_chart_contacts_within_1_deg": {
            "seed_to_first_quarter": cross_chart_contacts(seed, quarter),
            "seed_to_full": cross_chart_contacts(seed, full),
            "first_quarter_to_full": cross_chart_contacts(quarter, full),
        },
        "house_migrations": {
            body: [
                seed["bodies"][body]["whole_sign_house"],
                quarter["bodies"][body]["whole_sign_house"],
                full["bodies"][body]["whole_sign_house"],
            ]
            for body in PLANETS
        },
        "astronomical_geometry": {
            "local_horizon": horizon_summary,
            "full_phase": full_geometry,
        },
        "factual_comparison": {
            "research_id": "january-2025-authority-operations-window",
            "path": "Research Packages/January 2025 Authority to Operations Window/README.md",
            "selection_method": "fixed action-date window; objects independently selected for materiality, traceability, and primary-source receipts",
            "shared_factual_grammar": "executive direction -> named administrative carrier -> operating rule or procedure -> review, litigation, or formalization",
            "non_finding": "the four objects are not one coordinated policy program and do not prove policy success",
        },
        "source_paths": [
            "99 - Templates/mundane_history.json",
            "99 - Templates/moon_lineages.json",
            "99 - Templates/chart_reading_bones/lun-2026-07-29-fu.json",
        ],
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {OUTPUT}")
    print(f"First-Quarter -> Full Moon coordinate delta: {quarter_full_delta * 3600:.3f} arcseconds")


if __name__ == "__main__":
    main()
