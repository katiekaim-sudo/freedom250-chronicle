#!/usr/bin/env python3
"""Build a structural triage of every 2026 Full-Moon family.

The audit compares the registered seed, the usually unheard First Quarter and
the registered Full phase.  It identifies structural review flags without
ranking political importance, assigning a story, altering locked readings or
granting astrology factual, causal, convergence or Forecast Ledger credit.
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
BONES = HERE / "chart_reading_bones"
BONES_INDEX = BONES / "index.json"
OUTPUT = HERE / "full_moon_family_triage_2026.json"


def node_distance(chart: dict, governed_node_lon: float | None = None) -> float:
    node = governed_node_lon
    if node is None:
        node = swe.calc_ut(
            chart["julian_day_ut"], swe.TRUE_NODE, swe.FLG_SWIEPH | swe.FLG_SPEED
        )[0][0] % 360.0
    south = (node + 180.0) % 360.0
    moon = chart["bodies"]["Moon"]["longitude_deg"]
    return round(min(angular_distance(moon, node), angular_distance(moon, south)), 9)


def eclipse_transition(seed: bool, full: bool) -> str:
    if not seed and full:
        return "shadow_arrives_at_harvest"
    if seed and not full:
        return "shadow_releases_before_harvest"
    if seed and full:
        return "shadow_present_at_seed_and_harvest"
    return "ordinary_seed_and_harvest"


def root_signature(chart: dict) -> dict:
    root = chart["dispositors"]
    return {
        "final_dispositors": root["final_dispositors"],
        "bounded_cycles": root["bounded_cycles"],
    }


def horizon_counts(chart: dict) -> dict:
    above = [name for name in PLANETS if chart["bodies"][name]["true_altitude_deg"] > 0]
    return {
        "above": above,
        "below_or_on": [name for name in PLANETS if name not in above],
        "above_count": len(above),
        "below_or_on_count": len(PLANETS) - len(above),
    }


def main() -> None:
    history = json.loads(HISTORY.read_text())
    lineages = json.loads(LINEAGES.read_text())
    bone_index = json.loads(BONES_INDEX.read_text())

    history_by_id = {row["id"]: row for row in history["charts"]}
    phases = {row["phase_event_id"]: row for row in lineages["phase_events"]}
    bone_ids = {row["id"] for row in bone_index["charts"]}
    rows: list[dict] = []

    for lineage in lineages["lineages"]:
        members = {row["role"]: row for row in lineage["members"]}
        full_phase = phases[members["full"]["phase_event_id"]]
        if not full_phase["exact_utc"].startswith("2026-"):
            continue

        seed_phase = phases[members["seed"]["phase_event_id"]]
        quarter_phase = phases[members["first_quarter"]["phase_event_id"]]
        seed_source = history_by_id[members["seed"]["chart_id"]]
        full_id = members["full"]["chart_id"]
        if full_id not in bone_ids:
            raise RuntimeError(f"registered Full phase lacks chart bone: {full_id}")
        full_bone = json.loads((BONES / f"{full_id}.json").read_text())

        seed = calculated_chart(parse_utc(seed_phase["exact_utc"]))
        quarter = calculated_chart(parse_utc(quarter_phase["exact_utc"]))
        full = calculated_chart(parse_utc(full_phase["exact_utc"]))
        seed = apply_governed_positions(
            seed,
            {row["name"]: row["lon"] for row in seed_source["points"] if row["name"] in PLANETS},
            asc=seed_source["asc"],
            mc=seed_source["mc"],
        )
        quarter = apply_governed_positions(
            quarter,
            {"Sun": quarter_phase["sun_lon_deg"], "Moon": quarter_phase["moon_lon_deg"]},
        )
        full = apply_governed_positions(
            full,
            {body: full_bone["pos"][body]["lon"] for body in PLANETS},
            asc=full_bone["asc"],
            mc=full_bone["mc"],
            declinations={body: full_bone["pos"][body]["dec"] for body in PLANETS},
        )

        seed_node = next(row["lon"] for row in seed_source["points"] if row["name"] == "Node")
        seed_eclipse = bool(seed_phase["eclipse"])
        quarter_eclipse = bool(quarter_phase["eclipse"])
        full_eclipse = bool(full_phase["eclipse"])
        qf_contacts = cross_chart_contacts(quarter, full, 1.0)
        light_to_nonlight = [
            row for row in qf_contacts
            if row["from_body"] in {"Sun", "Moon"}
            and row["to_body"] not in {"Sun", "Moon"}
        ]
        exact_qf_contacts = [row for row in qf_contacts if row["orb_deg"] <= 0.25]
        full_declination = [
            row for row in full["declination_relationships_within_1_deg"]
            if row["orb_deg"] <= 0.25
        ]
        qf_degree_gap = angular_distance(
            quarter["bodies"]["Moon"]["longitude_deg"],
            full["bodies"]["Moon"]["longitude_deg"],
        )

        flags: list[str] = []
        transition = eclipse_transition(seed_eclipse, full_eclipse)
        if transition != "ordinary_seed_and_harvest":
            flags.append(transition)
        if qf_degree_gap <= 0.25:
            flags.append("quarter_and_full_moon_within_quarter_degree")
        if light_to_nonlight:
            flags.append("quarter_lights_configure_full_nonlight_planet_within_one_degree")
        if exact_qf_contacts:
            flags.append("quarter_to_full_contact_within_quarter_degree")
        if root_signature(seed) != root_signature(full):
            flags.append("seed_to_full_terminal_structure_changes")
        if full_declination:
            flags.append("full_phase_declination_relationship_within_quarter_degree")

        rows.append({
            "lineage_id": lineage["lineage_id"],
            "interpretation_status": lineage["interpretation_status"],
            "story_verdict": lineage["story_verdict"],
            "seed": {
                "phase_event_id": seed_phase["phase_event_id"],
                "chart_id": seed_phase["chart_id"],
                "exact_local": seed_phase["exact_local"],
                "moon_sign": seed_phase["moon_sign"],
                "moon_degree": seed_phase["moon_degree"],
                "eclipse": seed_eclipse,
                "node_axis_distance_deg": node_distance(seed, seed_node),
                "ascendant_sign": seed["ascendant_sign"],
                "root": root_signature(seed),
                "distribution": seed["distribution"],
                "horizon": horizon_counts(seed),
            },
            "first_quarter": {
                "phase_event_id": quarter_phase["phase_event_id"],
                "exact_local": quarter_phase["exact_local"],
                "moon_sign": quarter_phase["moon_sign"],
                "moon_degree": quarter_phase["moon_degree"],
                "eclipse": quarter_eclipse,
                "node_axis_distance_deg": node_distance(quarter),
                "ascendant_sign": quarter["ascendant_sign"],
                "root": root_signature(quarter),
                "distribution": quarter["distribution"],
                "horizon": horizon_counts(quarter),
            },
            "full": {
                "phase_event_id": full_phase["phase_event_id"],
                "chart_id": full_id,
                "reading_id": full_phase["reading_id"],
                "exact_local": full_phase["exact_local"],
                "moon_sign": full_phase["moon_sign"],
                "moon_degree": full_phase["moon_degree"],
                "eclipse": full_eclipse,
                "node_axis_distance_deg": node_distance(full, full_bone["node"]["lon"]),
                "ascendant_sign": full["ascendant_sign"],
                "root": root_signature(full),
                "distribution": full["distribution"],
                "registered_shape": full_bone["shape"],
                "horizon": horizon_counts(full),
                "declination_relationships_within_quarter_degree": full_declination,
            },
            "relays": {
                "seed_to_full_moon_degree_gap_deg": round(
                    angular_distance(
                        seed["bodies"]["Moon"]["longitude_deg"],
                        full["bodies"]["Moon"]["longitude_deg"],
                    ),
                    9,
                ),
                "first_quarter_to_full_moon_degree_gap_deg": round(qf_degree_gap, 9),
                "quarter_light_to_full_nonlight_contacts_within_one_degree": light_to_nonlight,
                "quarter_to_full_all_contacts_within_quarter_degree": exact_qf_contacts,
                "house_migrations": {
                    body: [
                        seed["bodies"][body]["whole_sign_house"],
                        quarter["bodies"][body]["whole_sign_house"],
                        full["bodies"][body]["whole_sign_house"],
                    ]
                    for body in PLANETS
                },
            },
            "shadow_transition": transition,
            "structural_review_flags": flags,
        })

    rows.sort(key=lambda row: row["full"]["exact_local"])
    qf_order = sorted(
        (
            {
                "lineage_id": row["lineage_id"],
                "full_phase_event_id": row["full"]["phase_event_id"],
                "moon_sign": row["full"]["moon_sign"],
                "gap_deg": row["relays"]["first_quarter_to_full_moon_degree_gap_deg"],
            }
            for row in rows
        ),
        key=lambda row: (row["gap_deg"], row["full_phase_event_id"]),
    )
    shadow_groups: dict[str, list[str]] = {}
    for row in rows:
        shadow_groups.setdefault(row["shadow_transition"], []).append(row["lineage_id"])

    result = {
        "schema": "freedom250.full-moon-family-triage-2026/v1",
        "developed_through": "2026-09-25",
        "authority_boundary": {
            "scope": "all thirteen registered 2026 Full Moons and their Pessin seed and First-Quarter charts",
            "calculation": "registered seed and Full-phase coordinates with Swiss Ephemeris calculation of missing First-Quarter frames and secondary geometry",
            "ranking": "none; structural flags route human review and do not rank political importance",
            "interpretation": "none; locked readings remain unchanged and companion rereads require separate human semantic disposition",
            "evidence_credit": "zero",
        },
        "family_count": len(rows),
        "shadow_transition_groups": shadow_groups,
        "quarter_to_full_degree_gap_order": qf_order,
        "families": rows,
        "source_paths": [
            "99 - Templates/mundane_history.json",
            "99 - Templates/moon_lineages.json",
            "99 - Templates/chart_reading_bones/index.json",
            "99 - Templates/chart_reading_bones/*.json",
        ],
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {OUTPUT}")
    print(f"2026 Full-Moon families: {len(rows)}")
    print("Tightest quarter-to-Full relays:")
    for row in qf_order[:5]:
        print(f"  {row['moon_sign']}: {row['gap_deg']:.6f}°")
    print("Shadow transitions:")
    for key, values in shadow_groups.items():
        print(f"  {key}: {len(values)}")


if __name__ == "__main__":
    main()
