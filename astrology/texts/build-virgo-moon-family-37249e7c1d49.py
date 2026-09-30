#!/usr/bin/env python3
"""Build the September 2024 Virgo Moon-family comparison.

This output supports a contextual companion reread. It preserves the locked
March 3, 2026 eclipse reading and grants astrology no factual, causal,
convergence, or Forecast Ledger credit.
"""

from __future__ import annotations

import json
from pathlib import Path

import swisseph as swe

from build_aquarius_moon_family import (
    PLANETS,
    angular_distance,
    apply_governed_positions,
    calculated_chart,
    cross_chart_contacts,
    parse_utc,
)


HERE = Path(__file__).resolve().parent
HISTORY = HERE / "mundane_history.json"
LINEAGES = HERE / "moon_lineages.json"
FULL_BONE = HERE / "chart_reading_bones" / "lun-2026-03-03-fu-lunar.json"
ECLIPSE_LOCAL = HERE / "eclipse_local_circumstances.json"
TRIAGE = HERE / "full_moon_family_triage_2026.json"
OUTPUT = HERE / "virgo_moon_family_2024_2026.json"


def node_state(chart: dict, governed_node_lon: float | None = None) -> dict:
    node = governed_node_lon
    if node is None:
        node = swe.calc_ut(
            chart["julian_day_ut"], swe.TRUE_NODE, swe.FLG_SWIEPH | swe.FLG_SPEED
        )[0][0] % 360.0
    south = (node + 180.0) % 360.0
    moon = chart["bodies"]["Moon"]["longitude_deg"]
    nearest = min(angular_distance(moon, node), angular_distance(moon, south))
    return {
        "true_north_node_longitude_deg": round(node, 9),
        "true_south_node_longitude_deg": round(south, 9),
        "moon_distance_to_nearest_node_axis_deg": round(nearest, 9),
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
    eclipse_local = json.loads(ECLIPSE_LOCAL.read_text())
    triage = json.loads(TRIAGE.read_text())

    seed_source = next(row for row in history["charts"] if row["id"] == "lun-2024-09-03-ne")
    lineage = next(row for row in lineages["lineages"] if row["lineage_id"] == "pessin:lun-2024-09-03-ne")
    phases = {row["phase_event_id"]: row for row in lineages["phase_events"]}
    quarter_source = phases["lunation-2025-06-03-fq"]
    full_source = phases["lun-2026-03-03-fu-lunar"]
    triage_row = next(row for row in triage["families"] if row["lineage_id"] == lineage["lineage_id"])

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

    qf_contacts = cross_chart_contacts(quarter, full, 0.25)
    full_eclipse = next(row for row in eclipse_local["events"] if row["date"] == "2026-03-03")
    moonset_jd = full_eclipse["washington"]["moonset_during_eclipse"]["jd_ut"]
    syzygy_jd = full_eclipse["global"]["syzygy"]["jd_ut"]

    result = {
        "schema": "freedom250.virgo-moon-family/v1",
        "developed_through": "2026-09-25",
        "lineage_id": lineage["lineage_id"],
        "interpretation_status_before_reread": lineage["interpretation_status"],
        "story_verdict_before_reread": lineage["story_verdict"],
        "authority_boundary": {
            "calculation": "registered seed and Full-phase coordinates with Swiss Ephemeris calculation of the missing First-Quarter frame and secondary geometry",
            "verification": "Astro Gold remains pending wherever the source registry says pending",
            "interpretation": "contextual companion only; locked March 3, 2026 Pass 1 remains unchanged",
            "evidence_credit": "zero",
        },
        "family_members": lineage["members"],
        "phase_eclipse_states": {
            "seed": bool(phases["lun-2024-09-03-ne"]["eclipse"]),
            "first_quarter": bool(quarter_source["eclipse"]),
            "full": bool(full_source["eclipse"]),
        },
        "charts": {
            "seed_2024_09_03": seed,
            "first_quarter_2025_06_03": quarter,
            "full_2026_03_03": full,
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
            "quarter_to_full_contacts_within_quarter_degree": qf_contacts,
            "meaning_boundary": "same-sign Pessin family continuity; degree proximity is one structural relay, not an extra factual or causal vote",
        },
        "node_approach": {
            "seed_nearest_axis_deg": seed["node_geometry"]["moon_distance_to_nearest_node_axis_deg"],
            "first_quarter_nearest_axis_deg": quarter["node_geometry"]["moon_distance_to_nearest_node_axis_deg"],
            "full_nearest_axis_deg": full["node_geometry"]["moon_distance_to_nearest_node_axis_deg"],
            "finding": "an ordinary seed reaches Full phase as a total lunar eclipse; shadow arrives at the harvest",
        },
        "house_migrations": triage_row["relays"]["house_migrations"],
        "root_handoff": {
            "seed": seed["dispositors"],
            "first_quarter": quarter["dispositors"],
            "full": full["dispositors"],
            "finding": "Venus plus a Mercury-Sun circuit becomes a Mercury final at First Quarter, then a Jupiter-Moon-Mercury circuit at Full phase",
        },
        "distribution_continuity": {
            "seed": seed["distribution"],
            "first_quarter": quarter["distribution"],
            "full": full["distribution"],
            "first_quarter_to_full_largest_gap_change_deg": round(
                full["distribution"]["largest_empty_arc_deg"]
                - quarter["distribution"]["largest_empty_arc_deg"], 6
            ),
            "same_boundary_bodies_at_quarter_and_full": (
                quarter["distribution"]["empty_arc_from_body"] == full["distribution"]["empty_arc_from_body"]
                and quarter["distribution"]["empty_arc_to_body"] == full["distribution"]["empty_arc_to_body"]
            ),
            "finding": "the First-Quarter and Full-phase raw distributions retain the Moon-to-Pluto empty-arc boundary and differ by less than one degree",
        },
        "aspect_development": {
            "seed_within_3_deg": selected_aspects(seed),
            "seed_declinations_within_quarter_degree": selected_declinations(seed),
            "first_quarter_within_3_deg": selected_aspects(quarter),
            "full_within_3_deg": selected_aspects(full),
            "full_declinations_within_quarter_degree": selected_declinations(full),
            "quarter_neptune_to_full_saturn": next(
                row for row in qf_contacts
                if row["from_body"] == "Neptune" and row["to_body"] == "Saturn"
            ),
        },
        "astronomical_geometry": {
            "global": full_eclipse["global"],
            "washington": full_eclipse["washington"],
            "moonset_before_syzygy_seconds": round((syzygy_jd - moonset_jd) * 86400.0, 3),
            "finding": "Washington sees maximum totality at the western horizon; the Moon sets before exact syzygy",
        },
        "factual_comparison": {
            "research_id": "sec-credit-rating-recordkeeping-orders-2024-2026",
            "read_first": "Research Packages/SEC Credit Rating Recordkeeping Orders 2024-2026/SEC_CREDIT_RATING_RECORDKEEPING_ORDERS_MATURATION_2024_2026.md",
            "seed_date_object": "six final SEC NRSRO recordkeeping orders entered September 3, 2024; all six firms admitted the orders' facts and violations",
            "maturation_state_at_full_phase": "four orders created a multi-stage independent-consultant process whose key reports were intended to remain nonpublic; the public objects prove required remediation, not successful completion",
            "selection_boundary": "selected independently from official SEC objects; astrology supplied no evidence credit and does not prove causation, coordination or outcome",
            "negative_control": "elapsed time and a mandated review do not establish that the public received the consultant findings or a completion receipt",
        },
        "source_paths": [
            "99 - Templates/mundane_history.json",
            "99 - Templates/moon_lineages.json",
            "99 - Templates/chart_reading_bones/lun-2026-03-03-fu-lunar.json",
            "99 - Templates/eclipse_local_circumstances.json",
            "99 - Templates/full_moon_family_triage_2026.json",
        ],
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()

