#!/usr/bin/env python3
"""Build the prospective late-2026 Moon-family control group.

Taurus, Gemini, and the December Cancer Full phases are future as of the
development cutoff. The output compares their already-registered charts and
past seed/First-Quarter frames without treating the Full phases as occurred,
selecting political maturations, or granting evidence or Forecast Ledger credit.
"""

from __future__ import annotations

import json
from pathlib import Path

from build_aquarius_moon_family import (
    PLANETS,
    angular_distance,
    apply_governed_positions,
    calculated_chart,
    cross_chart_contacts,
    parse_utc,
)
from build_scorpio_moon_family import horizon, horizon_event, node_state
import swisseph as swe


HERE = Path(__file__).resolve().parent
HISTORY = HERE / "mundane_history.json"
LINEAGES = HERE / "moon_lineages.json"
TRIAGE = HERE / "full_moon_family_triage_2026.json"
OUTPUT = HERE / "late_year_moon_family_controls_2026.json"

FAMILIES = (
    {
        "key": "taurus",
        "lineage_id": "pessin:lun-2025-04-27-ne",
        "seed_id": "lun-2025-04-27-ne",
        "quarter_id": "lunation-2026-01-26-fq",
        "full_id": "lun-2026-10-26-fu",
    },
    {
        "key": "gemini",
        "lineage_id": "pessin:lun-2025-05-27-ne",
        "seed_id": "lun-2025-05-27-ne",
        "quarter_id": "lunation-2026-02-24-fq",
        "full_id": "lun-2026-11-24-fu",
    },
    {
        "key": "cancer_december",
        "lineage_id": "pessin:lun-2025-06-25-ne",
        "seed_id": "lun-2025-06-25-ne",
        "quarter_id": "lunation-2026-03-25-fq",
        "full_id": "lun-2026-12-24-fu",
    },
)


def selected_declinations(chart: dict, maximum: float = 0.25) -> list[dict]:
    return [
        row for row in chart["declination_relationships_within_1_deg"]
        if row["orb_deg"] <= maximum
    ]


def build_family(config: dict, history: dict, lineages: dict, triage: dict) -> dict:
    seed_source = next(row for row in history["charts"] if row["id"] == config["seed_id"])
    lineage = next(row for row in lineages["lineages"] if row["lineage_id"] == config["lineage_id"])
    phases = {row["phase_event_id"]: row for row in lineages["phase_events"]}
    quarter_source = phases[config["quarter_id"]]
    full_source = phases[config["full_id"]]
    full_bone = json.loads((HERE / "chart_reading_bones" / f"{config['full_id']}.json").read_text())
    triage_row = next(row for row in triage["families"] if row["lineage_id"] == config["lineage_id"])

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

    full_jd = full["julian_day_ut"]
    previous_sunrise = horizon_event(full_jd, swe.SUN, "rise", "previous")
    next_sunset = horizon_event(full_jd, swe.SUN, "set", "next")
    previous_moonset = horizon_event(full_jd, swe.MOON, "set", "previous")
    next_moonrise = horizon_event(full_jd, swe.MOON, "rise", "next")

    return {
        "key": config["key"],
        "lineage_id": lineage["lineage_id"],
        "family_members": lineage["members"],
        "interpretation_status": lineage["interpretation_status"],
        "story_verdict": lineage["story_verdict"],
        "phase_state_as_of_2026_09_25": {
            "seed": "occurred",
            "first_quarter": "occurred",
            "full": "future_not_interpreted_as_occurred",
        },
        "phase_eclipse_states": {
            "seed": bool(phases[config["seed_id"]]["eclipse"]),
            "first_quarter": bool(quarter_source["eclipse"]),
            "full": bool(full_source["eclipse"]),
        },
        "charts": {"seed": seed, "first_quarter": quarter, "full": full},
        "degree_relays": {
            "seed_moon_degree_deg": seed["bodies"]["Moon"]["degree_in_sign"],
            "first_quarter_moon_degree_deg": quarter["bodies"]["Moon"]["degree_in_sign"],
            "full_moon_degree_deg": full["bodies"]["Moon"]["degree_in_sign"],
            "seed_to_first_quarter_deg": round(
                angular_distance(seed["bodies"]["Moon"]["longitude_deg"], quarter["bodies"]["Moon"]["longitude_deg"]), 9
            ),
            "seed_to_full_deg": round(
                angular_distance(seed["bodies"]["Moon"]["longitude_deg"], full["bodies"]["Moon"]["longitude_deg"]), 9
            ),
            "first_quarter_to_full_deg": round(
                angular_distance(quarter["bodies"]["Moon"]["longitude_deg"], full["bodies"]["Moon"]["longitude_deg"]), 9
            ),
            "meaning_boundary": "same-sign Pessin-family continuity does not require an exact coordinate return",
        },
        "node_path": [
            seed["node_geometry"]["moon_distance_to_nearest_node_axis_deg"],
            quarter["node_geometry"]["moon_distance_to_nearest_node_axis_deg"],
            full["node_geometry"]["moon_distance_to_nearest_node_axis_deg"],
        ],
        "house_migrations": triage_row["relays"]["house_migrations"],
        "root_handoff": {
            "seed": seed["dispositors"],
            "first_quarter": quarter["dispositors"],
            "full": full["dispositors"],
        },
        "distribution": {
            "seed": seed["distribution"],
            "first_quarter": quarter["distribution"],
            "full": full["distribution"],
            "quarter_to_full_largest_empty_arc_change_deg": round(
                full["distribution"]["largest_empty_arc_deg"] - quarter["distribution"]["largest_empty_arc_deg"], 6
            ),
            "quarter_to_full_occupied_span_change_deg": round(
                full["distribution"]["occupied_span_deg"] - quarter["distribution"]["occupied_span_deg"], 6
            ),
        },
        "quarter_to_full_contacts_within_1_25_deg": cross_chart_contacts(quarter, full, 1.25),
        "full_declinations_within_quarter_degree": selected_declinations(full),
        "full_phase_astronomy": {
            "registered_shape": triage_row["full"].get("registered_shape"),
            "sun_true_altitude_deg": full["bodies"]["Sun"]["true_altitude_deg"],
            "moon_true_altitude_deg": full["bodies"]["Moon"]["true_altitude_deg"],
            "horizon": full["horizon"],
            "previous_sunrise": previous_sunrise,
            "next_sunset": next_sunset,
            "previous_moonset": previous_moonset,
            "next_moonrise": next_moonrise,
        },
    }


def main() -> None:
    history = json.loads(HISTORY.read_text())
    lineages = json.loads(LINEAGES.read_text())
    triage = json.loads(TRIAGE.read_text())
    families = [build_family(config, history, lineages, triage) for config in FAMILIES]

    full_degrees = [row["degree_relays"]["full_moon_degree_deg"] for row in families]
    empty_arc_changes = [row["distribution"]["quarter_to_full_largest_empty_arc_change_deg"] for row in families]
    occupied_changes = [row["distribution"]["quarter_to_full_occupied_span_change_deg"] for row in families]
    result = {
        "schema": "freedom250.late-year-moon-family-controls/v1",
        "developed_through": "2026-09-25",
        "authority_boundary": {
            "calculation": "registered seed and Full-phase coordinates with Swiss Ephemeris calculation of missing First-Quarter frames and secondary geometry",
            "temporal": "all three Full phases are future as of the cutoff and are not described as occurred",
            "interpretation": "prospective structural control only; locked chart readings remain unchanged",
            "political_maturation": "withheld until each Full phase has occurred and an independently researched official-source record can be tested without hindsight substitution",
            "evidence_credit": "zero",
        },
        "families": families,
        "group_findings": {
            "all_full_phases_registered_splay": all(
                row["full_phase_astronomy"]["registered_shape"] == "splay" for row in families
            ),
            "full_moon_degree_min_deg": round(min(full_degrees), 9),
            "full_moon_degree_max_deg": round(max(full_degrees), 9),
            "full_moon_degree_range_deg": round(max(full_degrees) - min(full_degrees), 9),
            "quarter_to_full_largest_empty_arc_changes_deg": empty_arc_changes,
            "quarter_to_full_occupied_span_changes_deg": occupied_changes,
            "finding": "wide degree drift coexists with a shared late-year splay transition: each family sharply contracts its largest empty arc and expands its occupied field from First Quarter to Full phase",
            "control_value": "family continuity can be carried by phase identity, house migration, root change, distribution and astronomy even when the Moon does not return to a tight earlier degree",
        },
        "source_paths": [
            "99 - Templates/mundane_history.json",
            "99 - Templates/moon_lineages.json",
            "99 - Templates/full_moon_family_triage_2026.json",
            "99 - Templates/chart_reading_bones/lun-2026-10-26-fu.json",
            "99 - Templates/chart_reading_bones/lun-2026-11-24-fu.json",
            "99 - Templates/chart_reading_bones/lun-2026-12-24-fu.json",
        ],
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
