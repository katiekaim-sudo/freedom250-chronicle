#!/usr/bin/env python3
"""Build the July 2024 Cancer Moon-family comparison.

This output supports a retrospective contextual companion through the January
3, 2026 Full phase and a prospective boundary for the October 3 Last Quarter.
It preserves the locked Full-Moon reading and grants astrology no factual,
causal, corroborative, convergence, or Forecast Ledger credit.
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
FULL_BONE = HERE / "chart_reading_bones" / "lun-2026-01-03-fu.json"
TRIAGE = HERE / "full_moon_family_triage_2026.json"
MARS_PLUTO = HERE / "aries_mars_pluto_choreography.json"
RELATIONSHIPS = HERE / "inside_relationship_seed_families.json"
OUTPUT = HERE / "cancer_moon_family_2024_2026.json"


def governed_family_pass(relationships: dict, family_id: str) -> dict:
    family = next(row for row in relationships["families"] if row[1] == family_id)
    pass_row = family[4][0]
    return {
        "pass_id": pass_row[0],
        "exact_utc": pass_row[1],
        "longitude_deg": pass_row[2],
        "sign": pass_row[3],
        "degree_in_sign": pass_row[4],
        "relative_motion": pass_row[5],
    }


def main() -> None:
    history = json.loads(HISTORY.read_text())
    lineages = json.loads(LINEAGES.read_text())
    full_bone = json.loads(FULL_BONE.read_text())
    triage = json.loads(TRIAGE.read_text())
    mars_pluto = json.loads(MARS_PLUTO.read_text())
    relationships = json.loads(RELATIONSHIPS.read_text())

    seed_source = next(row for row in history["charts"] if row["id"] == "lun-2024-07-05-ne")
    lineage = next(
        row for row in lineages["lineages"]
        if row["lineage_id"] == "pessin:lun-2024-07-05-ne"
    )
    phases = {row["phase_event_id"]: row for row in lineages["phase_events"]}
    quarter_source = phases["lunation-2025-04-05-fq"]
    full_source = phases["lun-2026-01-03-fu"]
    last_quarter_source = phases["lunation-2026-10-03-lq"]
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

    conjunction = governed_family_pass(relationships, "mars-pluto-2026")
    opposition = next(row for row in mars_pluto["events"] if row["event_id"] == "mars-opposite-pluto")
    cancer_last_quarter = next(
        row for row in mars_pluto["events"] if row["event_id"] == "cancer-last-quarter"
    )
    conjunction_jd = swe.julday(2026, 1, 27, 23 + 1 / 60 + 8.038711 / 3600, swe.GREG_CAL)

    full_jd = full["julian_day_ut"]
    result = {
        "schema": "freedom250.cancer-moon-family/v1",
        "developed_through": "2026-09-25",
        "lineage_id": lineage["lineage_id"],
        "interpretation_status_before_reread": lineage["interpretation_status"],
        "story_verdict_before_reread": lineage["story_verdict"],
        "authority_boundary": {
            "calculation": "registered seed and Full-phase coordinates with Swiss Ephemeris calculation of the missing quarter frames and secondary geometry",
            "verification": "Astro Gold remains pending wherever the source registry says pending",
            "interpretation": "retrospective companion through the January 3 Full phase; the October 3 Last Quarter remains prospective as of the cutoff; locked Pass 1 remains unchanged",
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
            "seed": bool(phases["lun-2024-07-05-ne"]["eclipse"]),
            "first_quarter": bool(quarter_source["eclipse"]),
            "full": bool(full_source["eclipse"]),
            "last_quarter": bool(last_quarter_source["eclipse"]),
        },
        "charts": {
            "seed_2024_07_05": seed,
            "first_quarter_2025_04_04": first_quarter,
            "full_2026_01_03": full,
            "last_quarter_2026_10_03_prospective": last_quarter,
        },
        "four_phase_repetition": {
            "ascendant_signs": [
                seed["ascendant_sign"],
                first_quarter["ascendant_sign"],
                full["ascendant_sign"],
                last_quarter["ascendant_sign"],
            ],
            "moon_houses": [
                seed["bodies"]["Moon"]["whole_sign_house"],
                first_quarter["bodies"]["Moon"]["whole_sign_house"],
                full["bodies"]["Moon"]["whole_sign_house"],
                last_quarter["bodies"]["Moon"]["whole_sign_house"],
            ],
            "sun_houses": [
                seed["bodies"]["Sun"]["whole_sign_house"],
                first_quarter["bodies"]["Sun"]["whole_sign_house"],
                full["bodies"]["Sun"]["whole_sign_house"],
                last_quarter["bodies"]["Sun"]["whole_sign_house"],
            ],
            "finding": "seed and Full repeat Sagittarius rising with the Cancer Moon in the eighth and the Moon as sole final authority; both quarter phases repeat Scorpio rising with the Cancer Moon in the ninth and add a second bounded circuit beside the Moon final",
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
        "node_approach": {
            "seed_nearest_axis_deg": seed["node_geometry"]["moon_distance_to_nearest_node_axis_deg"],
            "first_quarter_nearest_axis_deg": first_quarter["node_geometry"]["moon_distance_to_nearest_node_axis_deg"],
            "full_nearest_axis_deg": full["node_geometry"]["moon_distance_to_nearest_node_axis_deg"],
            "last_quarter_nearest_axis_deg": last_quarter["node_geometry"]["moon_distance_to_nearest_node_axis_deg"],
            "finding": "the Moon approaches the nodal axis at every phase but the family remains ordinary through its prospective Last Quarter",
        },
        "house_migrations_seed_quarter_full": triage_row["relays"]["house_migrations"],
        "root_repetition": {
            "seed": seed["dispositors"],
            "first_quarter": first_quarter["dispositors"],
            "full": full["dispositors"],
            "last_quarter": last_quarter["dispositors"],
            "finding": "the Moon is final in all four phases; seed and Full reduce to the Moon alone, while First Quarter adds a Jupiter-Mercury circuit and Last Quarter adds a Sun-Venus-Mars circuit",
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
            "finding": "the family contracts slightly at First Quarter, opens at Full phase and opens much more widely by Last Quarter; its empty-arc boundary changes at every phase",
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
        "mars_pluto_interleave": {
            "full_phase_exact_utc": full_source["exact_utc"],
            "mars_pluto_conjunction": conjunction,
            "days_full_to_conjunction": round(conjunction_jd - full_jd, 6),
            "mars_pluto_opposition_exact_local": opposition["exact_local"],
            "last_quarter_exact_local": cancer_last_quarter["exact_local"],
            "hours_opposition_to_last_quarter": round(
                (cancer_last_quarter["julian_day_ut"] - opposition["julian_day_ut"]) * 24.0, 6
            ),
            "finding": "the Cancer Full phase precedes the Mars-Pluto conjunction by roughly twenty-four days, while the same family's Last Quarter follows the Mars-Pluto opposition by less than three hours",
            "clock_boundary": "interleaving independent clocks does not merge their identities or create an evidence vote",
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
            "research_id": "july-2024-protection-financial-control-window",
            "read_first": "Research Packages/July 2024 Protection and Financial Control Window/README.md",
            "selection_boundary": "five federal objects were independently selected from the fixed July 2-8, 2024 Federal Register window for materiality and lifecycle traceability before astrology was allowed to hear them",
            "objects": [
                {"object": "CFPB nonbank orders registry", "seed_state": "final rule", "state_by_cutoff": "effective architecture later rescinded October 29, 2025"},
                {"object": "OCC recovery-planning guidelines", "seed_state": "proposal", "state_by_cutoff": "finalized and effective, then formal guidelines rescinded May 1, 2026 while adjacent funding expectations remained"},
                {"object": "Treasury outbound-investment controls", "seed_state": "proposal", "state_by_cutoff": "31 CFR part 850 operating since January 2, 2025 with statutory successor rulemaking pending"},
                {"object": "FinCEN Al-Huda Bank special measure", "seed_state": "final rule", "state_by_cutoff": "effective correspondent-account prohibition still listed without rescission"},
                {"object": "FEMA Public Assistance update", "seed_state": "proposal", "state_by_cutoff": "comment period reopened; no final rule located by cutoff"},
            ],
            "finding": "the factual maturation is a sorting among contingent-burden containers: two removed, one hardened and handed toward statute, one retained and one unfinished",
            "negative_control": "the five objects are not one program; rescission does not erase adjacent authority, proposal does not equal operation, and a listed rule does not prove every transaction or enforcement outcome",
        },
        "source_paths": [
            "99 - Templates/mundane_history.json",
            "99 - Templates/moon_lineages.json",
            "99 - Templates/chart_reading_bones/lun-2026-01-03-fu.json",
            "99 - Templates/full_moon_family_triage_2026.json",
            "99 - Templates/aries_mars_pluto_choreography.json",
            "99 - Templates/inside_relationship_seed_families.json",
        ],
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
