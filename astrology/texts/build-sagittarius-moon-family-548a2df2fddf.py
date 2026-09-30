#!/usr/bin/env python3
"""Build the December 2024 Sagittarius Moon-family comparison.

This output supports a retrospective contextual companion through the May 31,
2026 Full phase and a prospective boundary for the February 28, 2027 Last
Quarter. It preserves the locked Full-Moon reading and grants astrology no
factual, causal, corroborative, convergence, or Forecast Ledger credit.
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
from build_scorpio_moon_family import (
    horizon,
    horizon_event,
    node_state,
    selected_aspects,
    selected_declinations,
)


HERE = Path(__file__).resolve().parent
HISTORY = HERE / "mundane_history.json"
LINEAGES = HERE / "moon_lineages.json"
FULL_BONE = HERE / "chart_reading_bones" / "lun-2026-05-31-fu.json"
TRIAGE = HERE / "full_moon_family_triage_2026.json"
OUTPUT = HERE / "sagittarius_moon_family_2024_2027.json"


def phase_summary(chart: dict) -> dict:
    return {
        "exact_utc": chart["exact_utc"],
        "ascendant_sign": chart["ascendant_sign"],
        "mc_sign": chart["mc_sign"],
        "sun_house": chart["bodies"]["Sun"]["whole_sign_house"],
        "moon_house": chart["bodies"]["Moon"]["whole_sign_house"],
        "pluto_house": chart["bodies"]["Pluto"]["whole_sign_house"],
        "dispositors": chart["dispositors"],
        "distribution": chart["distribution"],
        "horizon": chart["horizon"],
    }


def main() -> None:
    history = json.loads(HISTORY.read_text())
    lineages = json.loads(LINEAGES.read_text())
    full_bone = json.loads(FULL_BONE.read_text())
    triage = json.loads(TRIAGE.read_text())

    seed_source = next(row for row in history["charts"] if row["id"] == "lun-2024-12-01-ne")
    lineage = next(
        row for row in lineages["lineages"]
        if row["lineage_id"] == "pessin:lun-2024-12-01-ne"
    )
    phases = {row["phase_event_id"]: row for row in lineages["phase_events"]}
    quarter_source = phases["lunation-2025-08-31-fq"]
    full_source = phases["lun-2026-05-31-fu"]
    last_quarter_source = phases["lunation-2027-02-28-lq"]
    triage_row = next(
        row for row in triage["families"] if row["lineage_id"] == lineage["lineage_id"]
    )

    seed = calculated_chart(parse_utc(seed_source["utc"]))
    first_quarter = calculated_chart(parse_utc(quarter_source["exact_utc"]))
    full = calculated_chart(parse_utc(full_source["exact_utc"]))
    last_quarter = calculated_chart(parse_utc(last_quarter_source["exact_utc"]))
    seed = apply_governed_positions(
        seed,
        {row["name"]: row["lon"] for row in seed_source["points"] if row["name"] in PLANETS},
        asc=seed_source["asc"],
        mc=seed_source["mc"],
    )
    first_quarter = apply_governed_positions(
        first_quarter,
        {"Sun": quarter_source["sun_lon_deg"], "Moon": quarter_source["moon_lon_deg"]},
    )
    full = apply_governed_positions(
        full,
        {body: full_bone["pos"][body]["lon"] for body in PLANETS},
        asc=full_bone["asc"],
        mc=full_bone["mc"],
        declinations={body: full_bone["pos"][body]["dec"] for body in PLANETS},
    )
    last_quarter = apply_governed_positions(
        last_quarter,
        {"Sun": last_quarter_source["sun_lon_deg"], "Moon": last_quarter_source["moon_lon_deg"]},
    )

    seed_node = next(row["lon"] for row in seed_source["points"] if row["name"] == "Node")
    seed["node_geometry"] = node_state(seed, seed_node)
    first_quarter["node_geometry"] = node_state(first_quarter)
    full["node_geometry"] = node_state(full, full_bone["node"]["lon"])
    last_quarter["node_geometry"] = node_state(last_quarter)
    for chart in (seed, first_quarter, full, last_quarter):
        chart["horizon"] = horizon(chart)

    seed_quarter_contacts = cross_chart_contacts(seed, first_quarter, 1.25)
    seed_full_contacts = cross_chart_contacts(seed, full, 1.25)
    quarter_full_contacts = cross_chart_contacts(first_quarter, full, 1.25)
    full_last_contacts = cross_chart_contacts(full, last_quarter, 1.25)
    full_jd = full["julian_day_ut"]

    result = {
        "schema": "freedom250.sagittarius-moon-family/v1",
        "developed_through": "2026-09-25",
        "lineage_id": lineage["lineage_id"],
        "interpretation_status_before_reread": lineage["interpretation_status"],
        "story_verdict_before_reread": lineage["story_verdict"],
        "authority_boundary": {
            "calculation": "registered seed and Full-phase coordinates with Swiss Ephemeris calculation of the missing quarter frames and secondary geometry",
            "verification": "Astro Gold remains pending wherever the source registry says pending",
            "interpretation": "retrospective companion through the May 31 Full phase; the February 28, 2027 Last Quarter remains prospective as of the cutoff; locked Pass 1 remains unchanged",
            "evidence_credit": "zero",
        },
        "family_members": lineage["members"],
        "phase_state_as_of_developed_through": {
            "seed": "occurred",
            "first_quarter": "occurred",
            "full": "occurred",
            "last_quarter": "future_not_interpreted_as_occurred",
        },
        "phase_eclipse_states": {
            "seed": bool(phases["lun-2024-12-01-ne"]["eclipse"]),
            "first_quarter": bool(quarter_source["eclipse"]),
            "full": bool(full_source["eclipse"]),
            "last_quarter": bool(last_quarter_source["eclipse"]),
        },
        "charts": {
            "seed_2024_12_01": seed,
            "first_quarter_2025_08_31": first_quarter,
            "full_2026_05_31": full,
            "last_quarter_2027_02_28_prospective": last_quarter,
        },
        "phase_summaries": {
            "seed": phase_summary(seed),
            "first_quarter": phase_summary(first_quarter),
            "full": phase_summary(full),
            "last_quarter": phase_summary(last_quarter),
        },
        "degree_relays": {
            "seed_moon_degree_deg": round(seed["bodies"]["Moon"]["degree_in_sign"], 9),
            "first_quarter_moon_degree_deg": round(first_quarter["bodies"]["Moon"]["degree_in_sign"], 9),
            "full_moon_degree_deg": round(full["bodies"]["Moon"]["degree_in_sign"], 9),
            "last_quarter_moon_degree_deg": round(last_quarter["bodies"]["Moon"]["degree_in_sign"], 9),
            "seed_to_first_quarter_delta_deg": round(
                angular_distance(seed["bodies"]["Moon"]["longitude_deg"], first_quarter["bodies"]["Moon"]["longitude_deg"]), 9
            ),
            "seed_to_full_delta_deg": triage_row["relays"]["seed_to_full_moon_degree_gap_deg"],
            "first_quarter_to_full_delta_deg": triage_row["relays"]["first_quarter_to_full_moon_degree_gap_deg"],
            "seed_to_last_quarter_delta_deg": round(
                angular_distance(seed["bodies"]["Moon"]["longitude_deg"], last_quarter["bodies"]["Moon"]["longitude_deg"]), 9
            ),
            "seed_to_first_quarter_contacts_within_1_25_deg": seed_quarter_contacts,
            "seed_to_full_contacts_within_1_25_deg": seed_full_contacts,
            "quarter_to_full_contacts_within_1_25_deg": quarter_full_contacts,
            "full_to_last_quarter_contacts_within_1_25_deg": full_last_contacts,
            "meaning_boundary": "same-sign Pessin family continuity; exact cross-chart contacts do not add factual or causal evidence",
        },
        "node_development": {
            "seed_nearest_axis_deg": seed["node_geometry"]["moon_distance_to_nearest_node_axis_deg"],
            "first_quarter_nearest_axis_deg": first_quarter["node_geometry"]["moon_distance_to_nearest_node_axis_deg"],
            "full_nearest_axis_deg": full["node_geometry"]["moon_distance_to_nearest_node_axis_deg"],
            "last_quarter_nearest_axis_deg": last_quarter["node_geometry"]["moon_distance_to_nearest_node_axis_deg"],
            "finding": "the ordinary family recedes from the nodal axis through Full phase before returning closer at the prospective Last Quarter",
        },
        "house_migrations_seed_quarter_full": triage_row["relays"]["house_migrations"],
        "stage_development": {
            "moon_houses": [
                seed["bodies"]["Moon"]["whole_sign_house"],
                first_quarter["bodies"]["Moon"]["whole_sign_house"],
                full["bodies"]["Moon"]["whole_sign_house"],
                last_quarter["bodies"]["Moon"]["whole_sign_house"],
            ],
            "pluto_houses": [
                seed["bodies"]["Pluto"]["whole_sign_house"],
                first_quarter["bodies"]["Pluto"]["whole_sign_house"],
                full["bodies"]["Pluto"]["whole_sign_house"],
                last_quarter["bodies"]["Pluto"]["whole_sign_house"],
            ],
            "ascendant_signs": [
                seed["ascendant_sign"],
                first_quarter["ascendant_sign"],
                full["ascendant_sign"],
                last_quarter["ascendant_sign"],
            ],
            "finding": "through harvest the Sagittarius Moon moves fourth to sixth to eighth while Pluto moves sixth to eighth to tenth, transferring the question from national foundation through administration and shared exposure into public authority",
        },
        "root_development": {
            "seed": seed["dispositors"],
            "first_quarter": first_quarter["dispositors"],
            "full": full["dispositors"],
            "last_quarter": last_quarter["dispositors"],
            "finding": "the seed Jupiter-Mercury circuit divides at First Quarter into Jupiter-Moon and Mercury-Sun circuits; at Full phase Mercury becomes the sole final dispositor while the Jupiter-Moon public-response circuit remains",
        },
        "distribution_development": {
            "seed": seed["distribution"],
            "first_quarter": first_quarter["distribution"],
            "full": full["distribution"],
            "last_quarter": last_quarter["distribution"],
            "occupied_span_changes_deg": {
                "seed_to_first_quarter": round(first_quarter["distribution"]["occupied_span_deg"] - seed["distribution"]["occupied_span_deg"], 6),
                "first_quarter_to_full": round(full["distribution"]["occupied_span_deg"] - first_quarter["distribution"]["occupied_span_deg"], 6),
                "full_to_last_quarter": round(last_quarter["distribution"]["occupied_span_deg"] - full["distribution"]["occupied_span_deg"], 6),
            },
            "finding": "the occupied field opens by more than sixty-three degrees at First Quarter and then contracts by more than seventy-five degrees at Full phase, moving from a distributed administrative mechanism into a concentrated harvest account",
        },
        "seed_harvest_power_relay": {
            "seed_mars_to_full_pluto_opposition_orb_deg": next(
                row["orb_deg"] for row in seed_full_contacts
                if row["from_body"] == "Mars" and row["to_body"] == "Pluto" and row["kind"] == "opposition"
            ),
            "seed_mercury_pluto_parallel_orb_deg": next(
                row["orb_deg"] for row in selected_declinations(seed)
                if {row["a"], row["b"]} == {"Mercury", "Pluto"} and row["kind"] == "parallel"
            ),
            "finding": "the seed binds record and concentrated power in declination, then seed Mars returns opposite Full-phase Pluto within well under one degree as Pluto reaches the tenth house",
        },
        "aspect_development": {
            "seed_within_3_deg": selected_aspects(seed),
            "seed_declinations_within_quarter_degree": selected_declinations(seed),
            "first_quarter_within_3_deg": selected_aspects(first_quarter),
            "first_quarter_declinations_within_quarter_degree": selected_declinations(first_quarter),
            "full_within_3_deg": selected_aspects(full),
            "full_declinations_within_quarter_degree": selected_declinations(full),
            "last_quarter_within_3_deg": selected_aspects(last_quarter),
            "last_quarter_declinations_within_quarter_degree": selected_declinations(last_quarter),
        },
        "astronomical_geometry": {
            "local_horizon": {
                "seed": seed["horizon"],
                "first_quarter": first_quarter["horizon"],
                "full": full["horizon"],
                "last_quarter": last_quarter["horizon"],
            },
            "full_phase": {
                "moon_true_altitude_deg": full["bodies"]["Moon"]["true_altitude_deg"],
                "sun_true_altitude_deg": full["bodies"]["Sun"]["true_altitude_deg"],
                "previous_moonrise": horizon_event(full_jd, swe.MOON, "rise", "previous"),
                "next_moonset": horizon_event(full_jd, swe.MOON, "set", "next"),
                "next_sunrise": horizon_event(full_jd, swe.SUN, "rise", "next"),
                "scale_boundary": "local altitude supplies physical context only; Whole Sign house and literal visibility remain separate coordinate systems",
            },
        },
        "factual_comparison": {
            "research_id": "december-2024-beneficial-ownership-reporting-perimeter",
            "read_first": "Research Packages/December 2024 Beneficial Ownership Reporting Perimeter/README.md",
            "selection_boundary": "one independently identified federal reporting-perimeter object beginning in the fixed December 1-7, 2024 seed week; litigation, enforcement policy, interim rule and final rule remain separate authority states",
            "objects": [
                {
                    "object": "Corporate Transparency Act beneficial-ownership reporting perimeter",
                    "seed_state": "December 3, 2024 nationwide preliminary injunction interrupted CTA enforcement and stayed reporting deadlines",
                    "first_quarter_state": "the March 26, 2025 interim final rule was operating, exempting domestic entities and retaining a narrower foreign-entity reporting perimeter",
                    "full_phase_state": "foreign-only interim perimeter remained operative; comments and final-rule disposition were still pending at the May 31 Full phase",
                    "state_by_cutoff": "August 14, 2026 final rule made the narrowed foreign-entity-focused perimeter final and added further U.S.-person exemptions",
                }
            ],
            "finding": "the factual maturation moves from judicial interruption of a broad reporting duty to executive enforcement relief and finally to a durable regulatory redefinition of who counts as a reporting company",
            "negative_control": "a preliminary injunction is not repeal; a stay is not a merits judgment; enforcement discretion is not rule text; the foreign reporting perimeter, State entity rules, customer due diligence, sanctions screening and observed database use remain separate objects",
        },
        "source_paths": [
            "99 - Templates/mundane_history.json",
            "99 - Templates/moon_lineages.json",
            "99 - Templates/chart_reading_bones/lun-2026-05-31-fu.json",
            "99 - Templates/full_moon_family_triage_2026.json",
        ],
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
