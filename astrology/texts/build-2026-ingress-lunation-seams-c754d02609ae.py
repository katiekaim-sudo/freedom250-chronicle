#!/usr/bin/env python3
"""Build the 2026 ingress-lunation seam audit.

Every cardinal ingress occurs inside a lunar chapter that began before the
seasonal handoff.  This builder joins each 2026 ingress to its inherited New
Moon, first Full Moon, and chapter-closing New Moon; compares dispositor roots
and raw distribution; measures lunar age at the ingress; and tests seed-degree
contacts to the incoming seasonal frame.

The monthly chapter clock, Pessin Moon-family clock, and ingress-governance
clock remain distinct.  The result supplies no event, causal, forecast, or
factual-evidence credit and does not modify locked Pass 1 readings.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from phases import phase_of


HERE = Path(__file__).resolve().parent
HISTORY = HERE / "mundane_history.json"
BONES = HERE / "chart_reading_bones"
OUT = HERE / "ingress_lunation_seams_2026.json"

SEAMS = (
    {
        "season": "Aries",
        "seed_id": "lun-2026-03-19-ne",
        "ingress_id": "ingress-2026-aries",
        "full_id": "lun-2026-04-02-fu",
        "next_new_id": "lun-2026-04-17-ne",
        "knowledge_state": "retrospective",
    },
    {
        "season": "Cancer",
        "seed_id": "lun-2026-06-15-ne",
        "ingress_id": "ingress-2026-cancer",
        "full_id": "lun-2026-06-29-fu",
        "next_new_id": "lun-2026-07-14-ne",
        "knowledge_state": "retrospective",
    },
    {
        "season": "Libra",
        "seed_id": "lun-2026-09-11-ne",
        "ingress_id": "ingress-2026-libra",
        "full_id": "lun-2026-09-26-fu",
        "next_new_id": "lun-2026-10-10-ne",
        "knowledge_state": "ingress_occurred_full_and_close_future_at_cutoff",
    },
    {
        "season": "Capricorn",
        "seed_id": "lun-2026-12-09-ne",
        "ingress_id": "ingress-2026-capricorn",
        "full_id": "lun-2026-12-24-fu",
        "next_new_id": "lun-2027-01-07-ne",
        "knowledge_state": "prospective_at_cutoff",
    },
)

ASPECTS = (
    ("conjunction", 0.0),
    ("sextile", 60.0),
    ("square", 90.0),
    ("trine", 120.0),
    ("opposition", 180.0),
)
TRADITIONAL_BODIES = (
    "Sun", "Moon", "Mercury", "Venus", "Mars",
    "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto",
)


def rounded(value: float, places: int = 9) -> float:
    return round(float(value), places)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_bone(chart_id: str) -> dict:
    return json.loads((BONES / f"{chart_id}.json").read_text(encoding="utf-8"))


def optional_chart_summary(chart_id: str, history_row: dict) -> dict:
    """Return a governed chart summary without inventing an absent bone.

    The January 2027 chapter-closing New Moon has an exact registered clock in
    mundane_history.json but no chart-reading bone at this cutoff.  Its clock is
    sufficient to delimit the inherited lunar chapter; dispositors and shape
    must remain unavailable until the chart itself is registered.
    """
    bone_path = BONES / f"{chart_id}.json"
    if bone_path.exists():
        summary = chart_summary(chart_id, history_row, load_bone(chart_id))
        summary["chart_registration_state"] = "registered_chart_bone"
        return summary
    return {
        "chart_id": chart_id,
        "label": history_row["label"],
        "exact_utc": history_row["utc"],
        "exact_local": history_row["local"],
        "chart_registration_state": "exact_clock_only_chart_bone_absent_at_cutoff",
        "interpretive_fields": "withheld",
    }


def point_longitudes(chart: dict) -> dict[str, float]:
    points = {
        body: chart["pos"][body]["lon"] % 360.0
        for body in TRADITIONAL_BODIES
    }
    points.update({
        "ASC": chart["asc"] % 360.0,
        "DSC": (chart["asc"] + 180.0) % 360.0,
        "MC": chart["mc"] % 360.0,
        "IC": (chart["mc"] + 180.0) % 360.0,
    })
    return points


def angular_distance(first: float, second: float) -> float:
    return abs((second - first + 180.0) % 360.0 - 180.0)


def seed_degree_contacts(seed: dict, ingress: dict) -> list[dict]:
    seed_degree = seed["pos"]["Sun"]["lon"] % 360.0
    rows = []
    for point, longitude in point_longitudes(ingress).items():
        separation = angular_distance(seed_degree, longitude)
        aspect, angle = min(ASPECTS, key=lambda item: abs(separation - item[1]))
        orb = abs(separation - angle)
        if orb <= 3.5 + 1e-12:
            rows.append({
                "point": point,
                "point_longitude_deg": rounded(longitude),
                "aspect": aspect,
                "aspect_angle_deg": angle,
                "orb_deg": rounded(orb, 6),
                "strength_band": "exact_relay" if orb <= 1.0 + 1e-12 else "contextual_contact",
            })
    return sorted(rows, key=lambda row: (row["orb_deg"], row["point"]))


def chart_summary(chart_id: str, history_row: dict, bone: dict) -> dict:
    return {
        "chart_id": chart_id,
        "label": history_row["label"],
        "exact_utc": history_row["utc"],
        "exact_local": history_row["local"],
        "ascendant_sign": bone["asc_sign"],
        "chart_ruler": bone["ruler"],
        "final_dispositors": bone["finals"],
        "bounded_cycles": bone["loops"],
        "root_members": bone["root_members"],
        "occupied_span_deg": rounded(bone["occupied_deg"], 6),
        "largest_empty_arc_deg": rounded(bone["empty_deg"], 6),
        "named_shape_status": "legacy_stored_label_not_used_as_live_authority",
    }


def root_transition(source: dict, target: dict) -> dict:
    source_roots = set(source["root_members"])
    target_roots = set(target["root_members"])
    return {
        "shared_members": sorted(source_roots & target_roots),
        "added_members": sorted(target_roots - source_roots),
        "removed_members": sorted(source_roots - target_roots),
        "same_root_set": source_roots == target_roots,
        "source_root_is_subset": source_roots <= target_roots,
        "overlap_count": len(source_roots & target_roots),
        "union_count": len(source_roots | target_roots),
        "jaccard": rounded(len(source_roots & target_roots) / len(source_roots | target_roots), 6),
    }


def history_positions(row: dict) -> dict[str, float]:
    return {point["name"]: point["lon"] for point in row["points"]}


def build_control(history_rows: list[dict]) -> dict:
    complete_years = []
    all_waxing_years = []
    increasing_years = []
    for year in range(2017, 2029):
        rows = {
            row["sign"]: row
            for row in history_rows
            if row["chart_type"] == "ingress" and row["year"] == year
        }
        if set(rows) != {"Aries", "Cancer", "Libra", "Capricorn"}:
            continue
        elongations = []
        for sign in ("Aries", "Cancer", "Libra", "Capricorn"):
            positions = history_positions(rows[sign])
            elongations.append((positions["Moon"] - positions["Sun"]) % 360.0)
        complete_years.append({
            "year": year,
            "ingress_moon_sun_elongations_deg": [rounded(value, 6) for value in elongations],
            "all_waxing": all(value < 180.0 for value in elongations),
            "strictly_increasing_without_wrap": all(
                earlier < later for earlier, later in zip(elongations, elongations[1:])
            ),
        })
        if all(value < 180.0 for value in elongations):
            all_waxing_years.append(year)
        if all(earlier < later for earlier, later in zip(elongations, elongations[1:])):
            increasing_years.append(year)
    return {
        "coverage": "2017-2028 complete four-ingress years in mundane_history.json",
        "years": complete_years,
        "all_four_ingresses_waxing_years": all_waxing_years,
        "strictly_increasing_without_wrap_years": increasing_years,
        "boundary": (
            "The 2026 all-waxing progression is uncommon inside this bounded twelve-year control "
            "but not unique and not an all-history rarity claim."
        ),
    }


def build_payload() -> dict:
    history = json.loads(HISTORY.read_text(encoding="utf-8"))
    history_index = {row["id"]: row for row in history["charts"]}
    rows = []
    for spec in SEAMS:
        seed_history = history_index[spec["seed_id"]]
        ingress_history = history_index[spec["ingress_id"]]
        full_history = history_index[spec["full_id"]]
        next_new_history = history_index[spec["next_new_id"]]
        seed = load_bone(spec["seed_id"])
        ingress = load_bone(spec["ingress_id"])
        full = load_bone(spec["full_id"])
        ingress_positions = history_positions(ingress_history)
        elongation = (ingress_positions["Moon"] - ingress_positions["Sun"]) % 360.0
        phase_name, phase_direction = phase_of(elongation)
        chapter_days = next_new_history["jd_ut"] - seed_history["jd_ut"]
        age_days = ingress_history["jd_ut"] - seed_history["jd_ut"]
        to_full_days = full_history["jd_ut"] - ingress_history["jd_ut"]
        seed_summary = chart_summary(spec["seed_id"], seed_history, seed)
        ingress_summary = chart_summary(spec["ingress_id"], ingress_history, ingress)
        full_summary = chart_summary(spec["full_id"], full_history, full)
        next_new_summary = optional_chart_summary(spec["next_new_id"], next_new_history)
        rows.append({
            "season": spec["season"],
            "knowledge_state_at_2026_09_25": spec["knowledge_state"],
            "inherited_new_moon": seed_summary,
            "incoming_ingress": ingress_summary,
            "first_full_moon": full_summary,
            "chapter_closing_new_moon": next_new_summary,
            "lunar_phase_at_ingress": {
                "moon_from_sun_oriented_elongation_deg": rounded(elongation, 6),
                "phase_name": phase_name,
                "phase_direction": phase_direction,
                "chapter_age_days": rounded(age_days, 6),
                "chapter_duration_days": rounded(chapter_days, 6),
                "chapter_elapsed_percent": rounded(100.0 * age_days / chapter_days, 6),
                "days_from_ingress_to_first_full_moon": rounded(to_full_days, 6),
            },
            "seed_to_ingress_root_transition": root_transition(seed_summary, ingress_summary),
            "ingress_to_full_root_transition": root_transition(ingress_summary, full_summary),
            "seed_to_ingress_distribution": {
                "occupied_span_change_deg": rounded(
                    ingress_summary["occupied_span_deg"] - seed_summary["occupied_span_deg"], 6
                ),
                "largest_empty_arc_change_deg": rounded(
                    ingress_summary["largest_empty_arc_deg"] - seed_summary["largest_empty_arc_deg"], 6
                ),
            },
            "seed_degree_contacts_to_incoming_ingress": seed_degree_contacts(seed, ingress),
            "clock_boundary": (
                "The inherited New Moon governs the local monthly chapter until the next New Moon. "
                "The ingress changes seasonal authority at its exact clock. The first Full Moon also "
                "belongs to its separately registered Pessin Moon family; these clocks are not merged."
            ),
        })

    ages = [row["lunar_phase_at_ingress"]["chapter_age_days"] for row in rows]
    leads = [row["lunar_phase_at_ingress"]["days_from_ingress_to_first_full_moon"] for row in rows]
    return {
        "schema": "freedom250.ingress-lunation-seams-2026/v1",
        "status": "retrospective_to_current_with_prospective_late_year_structure",
        "developed_through": "2026-09-25",
        "authority_boundary": {
            "governance": "Ingress -> inherited/current lunation -> separately typed eclipse and Moon-family clocks",
            "locked_readings_preserved": True,
            "future_boundary": (
                "Libra's Full Moon and close and the complete Capricorn seam are prospective at the cutoff; "
                "their structure is not narrated as occurred political fact."
            ),
            "factual_evidence_credit": "zero",
            "forecast_ledger_credit": "zero",
            "causal_claim": False,
        },
        "seams": rows,
        "year_pattern": {
            "every_ingress_occurs_inside_a_new_moon_chapter_planted_under_predecessor_ingress": True,
            "every_seed_and_ingress_has_bounded_cycle_root_not_final_dispositor": all(
                not row["inherited_new_moon"]["final_dispositors"]
                and not row["incoming_ingress"]["final_dispositors"]
                and row["inherited_new_moon"]["bounded_cycles"]
                and row["incoming_ingress"]["bounded_cycles"]
                for row in rows
            ),
            "chapter_ages_strictly_increase": all(a < b for a, b in zip(ages, ages[1:])),
            "days_to_first_full_moon_strictly_decrease": all(a > b for a, b in zip(leads, leads[1:])),
            "chapter_ages_days": ages,
            "days_to_first_full_moon": leads,
            "finding": (
                "Across 2026 the seasonal handoff enters progressively later in its inherited lunar chapter, "
                "while the first Full Moon arrives progressively sooner after the ingress. Seasonal authority "
                "changes, but the local Moon story never restarts at the seam."
            ),
        },
        "bounded_year_control": build_control(history["charts"]),
        "interpretive_synthesis": {
            "aries": (
                "The Pisces seed's Jupiter-Moon circuit is expanded by Mars at the Aries ingress; "
                "a nearly unchanged concentrated sky acquires an action carrier."
            ),
            "cancer": (
                "The Gemini seed's Mercury-Moon circuit survives the Cancer ingress unchanged; "
                "the season changes while the message-public/foundation-material feedback loop does not."
            ),
            "libra": (
                "The Virgo seed's Mercury-Venus-Mars-Moon loop loses record and value at the seam, "
                "retains Mars-Moon, and gains Saturn; agreement becomes force, public need and boundary."
            ),
            "capricorn": (
                "The Sagittarius seed's Sun-Jupiter mission circuit is absorbed into the five-body winter "
                "operating chain, while the seed degree lands on the incoming Descendant within 0.027 degrees."
            ),
            "whole_year": (
                "The year does not move from four clean seasonal beginnings. It carries four inherited lunar "
                "questions across the threshold: action is added, dialogue is preserved, agreement is hardened "
                "into boundary, and mission is absorbed into an institutional operating circuit."
            ),
        },
        "provenance": {
            "builder": "99 - Templates/build_2026_ingress_lunation_seams.py",
            "history": "99 - Templates/mundane_history.json",
            "history_sha256": sha256(HISTORY),
            "bones_index": "99 - Templates/chart_reading_bones/index.json",
            "bones_index_sha256": sha256(BONES / "index.json"),
            "calculation_scope": "registered Washington, D.C. Whole Sign chart bones and exact mundane history clocks",
        },
    }


def main() -> None:
    payload = build_payload()
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
