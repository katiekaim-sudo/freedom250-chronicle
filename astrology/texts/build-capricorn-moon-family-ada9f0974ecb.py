#!/usr/bin/env python3
"""Build the December 2024 Capricorn Moon-family comparison.

This output supports a contextual companion reread. It preserves the locked
June 29, 2026 Full-Moon reading and grants astrology no factual, causal,
convergence, or Forecast Ledger credit.
"""

from __future__ import annotations

import json
import datetime as dt
from pathlib import Path
from zoneinfo import ZoneInfo

import swisseph as swe

from build_aquarius_moon_family import (
    PLANETS,
    angular_distance,
    apply_governed_positions,
    calculated_chart,
    cross_chart_contacts,
    parse_utc,
    sky_separation,
)


HERE = Path(__file__).resolve().parent
HISTORY = HERE / "mundane_history.json"
LINEAGES = HERE / "moon_lineages.json"
FULL_BONE = HERE / "chart_reading_bones" / "lun-2026-06-29-fu.json"
TRIAGE = HERE / "full_moon_family_triage_2026.json"
OUTPUT = HERE / "capricorn_moon_family_2024_2026.json"
WASHINGTON = (-77.0369, 38.9072, 0.0)


def jd_instant(jd: float) -> dict:
    year, month, day, decimal_hour = swe.revjul(jd, swe.GREG_CAL)
    hour = int(decimal_hour)
    minute_float = (decimal_hour - hour) * 60.0
    minute = int(minute_float)
    second_float = (minute_float - minute) * 60.0
    second = int(second_float)
    microsecond = round((second_float - second) * 1_000_000)
    if microsecond == 1_000_000:
        second += 1
        microsecond = 0
    utc = dt.datetime(year, month, day, hour, minute, second, microsecond, tzinfo=dt.timezone.utc)
    local = utc.astimezone(ZoneInfo("America/New_York"))
    return {
        "julian_day_ut": round(jd, 9),
        "utc": utc.isoformat().replace("+00:00", "Z"),
        "washington_local": local.isoformat(),
    }


def next_horizon_event(jd: float, body: int, kind: str) -> dict:
    flag = swe.CALC_RISE if kind == "rise" else swe.CALC_SET
    result, times = swe.rise_trans(
        jd,
        body,
        flag | swe.BIT_DISC_CENTER,
        WASHINGTON,
        0.0,
        10.0,
        swe.FLG_SWIEPH | swe.FLG_SPEED,
    )
    if result != 0:
        raise RuntimeError(f"No {kind} event found")
    return {"kind": kind, "model": "Swiss Ephemeris apparent disc-center horizon event", **jd_instant(times[0])}


def node_state(chart: dict, governed_node_lon: float | None = None) -> dict:
    node = governed_node_lon
    if node is None:
        node = swe.calc_ut(
            chart["julian_day_ut"], swe.TRUE_NODE, swe.FLG_SWIEPH | swe.FLG_SPEED
        )[0][0] % 360.0
    south = (node + 180.0) % 360.0
    moon = chart["bodies"]["Moon"]["longitude_deg"]
    return {
        "true_north_node_longitude_deg": round(node, 9),
        "true_south_node_longitude_deg": round(south, 9),
        "moon_distance_to_nearest_node_axis_deg": round(
            min(angular_distance(moon, node), angular_distance(moon, south)), 9
        ),
        "moon_ecliptic_latitude_deg": chart["bodies"]["Moon"]["ecliptic_latitude_deg"],
    }


def horizon(chart: dict) -> dict:
    above = [body for body in PLANETS if chart["bodies"][body]["true_altitude_deg"] > 0]
    return {
        "above_true_horizon": above,
        "below_or_on_true_horizon": [body for body in PLANETS if body not in above],
        "above_count": len(above),
        "below_or_on_count": len(PLANETS) - len(above),
    }


def selected_aspects(chart: dict, maximum: float = 3.0) -> list[dict]:
    return [row for row in chart["aspects_within_3_deg"] if row["orb_deg"] <= maximum]


def selected_declinations(chart: dict, maximum: float = 0.25) -> list[dict]:
    return [
        row for row in chart["declination_relationships_within_1_deg"]
        if row["orb_deg"] <= maximum
    ]


def main() -> None:
    history = json.loads(HISTORY.read_text())
    lineages = json.loads(LINEAGES.read_text())
    full_bone = json.loads(FULL_BONE.read_text())
    triage = json.loads(TRIAGE.read_text())

    seed_source = next(row for row in history["charts"] if row["id"] == "lun-2024-12-30-ne")
    lineage = next(
        row for row in lineages["lineages"]
        if row["lineage_id"] == "pessin:lun-2024-12-30-ne"
    )
    phases = {row["phase_event_id"]: row for row in lineages["phase_events"]}
    quarter_source = phases["lunation-2025-09-29-fq"]
    full_source = phases["lun-2026-06-29-fu"]
    triage_row = next(
        row for row in triage["families"] if row["lineage_id"] == lineage["lineage_id"]
    )

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

    seed_node = next(row["lon"] for row in seed_source["points"] if row["name"] == "Node")
    seed["node_geometry"] = node_state(seed, seed_node)
    quarter["node_geometry"] = node_state(quarter)
    full["node_geometry"] = node_state(full, full_bone["node"]["lon"])
    for chart in (seed, quarter, full):
        chart["horizon"] = horizon(chart)

    qf_contacts = cross_chart_contacts(quarter, full, 1.25)
    full_jd = full["julian_day_ut"]
    sunset = next_horizon_event(full_jd, swe.SUN, "set")
    moonrise = next_horizon_event(full_jd, swe.MOON, "rise")
    result = {
        "schema": "freedom250.capricorn-moon-family/v1",
        "developed_through": "2026-09-25",
        "lineage_id": lineage["lineage_id"],
        "interpretation_status_before_reread": lineage["interpretation_status"],
        "story_verdict_before_reread": lineage["story_verdict"],
        "authority_boundary": {
            "calculation": "registered seed and Full-phase coordinates with Swiss Ephemeris calculation of the missing First-Quarter frame and secondary geometry",
            "verification": "Astro Gold remains pending wherever the source registry says pending",
            "interpretation": "contextual companion only; locked June 29, 2026 Pass 1 remains unchanged",
            "evidence_credit": "zero",
        },
        "family_members": lineage["members"],
        "phase_eclipse_states": {
            "seed": bool(phases["lun-2024-12-30-ne"]["eclipse"]),
            "first_quarter": bool(quarter_source["eclipse"]),
            "full": bool(full_source["eclipse"]),
        },
        "charts": {
            "seed_2024_12_30": seed,
            "first_quarter_2025_09_29": quarter,
            "full_2026_06_29": full,
        },
        "degree_relays": {
            "seed_moon_degree_deg": round(seed["bodies"]["Moon"]["degree_in_sign"], 9),
            "first_quarter_moon_degree_deg": round(quarter["bodies"]["Moon"]["degree_in_sign"], 9),
            "full_moon_degree_deg": round(full["bodies"]["Moon"]["degree_in_sign"], 9),
            "seed_to_full_moon_delta_deg": triage_row["relays"]["seed_to_full_moon_degree_gap_deg"],
            "first_quarter_to_full_moon_delta_deg": triage_row["relays"]["first_quarter_to_full_moon_degree_gap_deg"],
            "first_quarter_to_full_moon_delta_arcminutes": round(
                triage_row["relays"]["first_quarter_to_full_moon_degree_gap_deg"] * 60.0, 6
            ),
            "quarter_to_full_contacts_within_1_25_deg": qf_contacts,
            "meaning_boundary": "same-sign Pessin family continuity; degree proximity is one structural relay, not an extra factual or causal vote",
        },
        "node_approach": {
            "seed_nearest_axis_deg": seed["node_geometry"]["moon_distance_to_nearest_node_axis_deg"],
            "first_quarter_nearest_axis_deg": quarter["node_geometry"]["moon_distance_to_nearest_node_axis_deg"],
            "full_nearest_axis_deg": full["node_geometry"]["moon_distance_to_nearest_node_axis_deg"],
            "finding": "the Moon approaches the nodal axis at every phase, but both seed and harvest remain ordinary rather than eclipsed",
        },
        "house_migrations": triage_row["relays"]["house_migrations"],
        "root_handoff": {
            "seed": seed["dispositors"],
            "first_quarter": quarter["dispositors"],
            "full": full["dispositors"],
            "finding": "a Jupiter-Mercury seed circuit opens into a Mars final plus two bounded circuits at First Quarter, then reconverges as a Mars-Mercury-Moon-Saturn circuit at Full phase",
        },
        "distribution_development": {
            "seed": seed["distribution"],
            "first_quarter": quarter["distribution"],
            "full": full["distribution"],
            "seed_to_first_quarter_largest_gap_change_deg": round(
                quarter["distribution"]["largest_empty_arc_deg"]
                - seed["distribution"]["largest_empty_arc_deg"], 6
            ),
            "first_quarter_to_full_largest_gap_change_deg": round(
                full["distribution"]["largest_empty_arc_deg"]
                - quarter["distribution"]["largest_empty_arc_deg"], 6
            ),
            "seed_to_full_largest_gap_change_deg": round(
                full["distribution"]["largest_empty_arc_deg"]
                - seed["distribution"]["largest_empty_arc_deg"], 6
            ),
            "finding": "the chart opens widely at First Quarter, then reconcentrates near the seed's occupied span while changing the empty-arc boundary",
        },
        "aspect_development": {
            "seed_within_3_deg": selected_aspects(seed),
            "seed_declinations_within_quarter_degree": selected_declinations(seed),
            "first_quarter_within_3_deg": selected_aspects(quarter),
            "first_quarter_declinations_within_quarter_degree": selected_declinations(quarter),
            "full_within_3_deg": selected_aspects(full),
            "full_declinations_within_quarter_degree": selected_declinations(full),
        },
        "astronomical_geometry": {
            "local_horizon": {
                "seed": seed["horizon"],
                "first_quarter": quarter["horizon"],
                "full": full["horizon"],
            },
            "full_phase": {
                "moon_true_altitude_deg": full["bodies"]["Moon"]["true_altitude_deg"],
                "sun_true_altitude_deg": full["bodies"]["Sun"]["true_altitude_deg"],
                "sunset_after_exact_full": sunset,
                "sunset_after_exact_full_minutes": round((sunset["julian_day_ut"] - full_jd) * 1440.0, 3),
                "moonrise_after_exact_full": moonrise,
                "moonrise_after_exact_full_minutes": round((moonrise["julian_day_ut"] - full_jd) * 1440.0, 3),
                "mars_uranus_true_sky_separation_deg": round(
                    sky_separation(full["bodies"]["Mars"], full["bodies"]["Uranus"]), 6
                ),
                "sun_pluto_true_sky_separation_deg": round(
                    sky_separation(full["bodies"]["Sun"], full["bodies"]["Pluto"]), 6
                ),
                "scale_boundary": "geocentric angular geometry and local altitude supply physical context only; they do not prove astrological causation or assign interpretive weight",
            },
        },
        "factual_comparison": {
            "research_id": "treasury-irs",
            "read_first": "Research Packages/Treasury and IRS/TREASURY_IRS_TRANSITION_TIMELINE.md",
            "fixed_window_control_research_id": "december-2024-rule-perimeter-operating-identity-window",
            "fixed_window_control_read_first": "Research Packages/December 2024 Rule Perimeter and Operating Identity Window/README.md",
            "seed_date_object": "Treasury and IRS published the final noncustodial digital-asset broker rule on December 30, 2024",
            "pre_quarter_reversal": "Public Law 119-5 disapproved that exact rule on April 10, 2025, declaring that it shall have no force or effect",
            "surviving_adjacent_rail": "separate custodial-broker reporting rules continued: 2025 gross-proceeds transactions were reported on Form 1099-DA in 2026, while basis reporting began for certain post-2025 acquisitions and sales",
            "same_window_counter_control": {
                "denominator": "673 Federal Register documents published December 27, 2024 through January 2, 2025; three material final rules selected for traceable later receipts, not an exhaustive review",
                "cfpb_overdraft_rule": "Public Law 119-10 disapproved the December 30 final rule before its scheduled October 1, 2025 effective date",
                "sec_edgar_next": "the December 27 final rule reached mandatory credentialed operation in September 2025 through individual identities, typed roles, delegation, multifactor authentication and optional APIs",
                "interpretive_limit": "the two additional objects are same-window controls, not extra astrology votes and not substitutes for the exact DeFi rule lifecycle",
            },
            "selection_boundary": "selected independently from official Treasury, IRS, Federal Register and enrolled-law objects; astrology supplied no evidence credit and does not prove causation, coordination or outcome",
            "negative_control": "the seed-date DeFi rule itself did not mature at harvest; it was legally extinguished before First Quarter, while a distinct custodial reporting perimeter became operational",
        },
        "source_paths": [
            "99 - Templates/mundane_history.json",
            "99 - Templates/moon_lineages.json",
            "99 - Templates/chart_reading_bones/lun-2026-06-29-fu.json",
            "99 - Templates/full_moon_family_triage_2026.json",
        ],
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
