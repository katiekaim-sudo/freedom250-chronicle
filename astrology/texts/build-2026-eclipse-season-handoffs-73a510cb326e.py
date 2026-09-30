#!/usr/bin/env python3
"""Build the paired solar-seed/lunar-disclosure audit for 2026.

The builder preserves each locked eclipse reading while testing what changes
between the solar eclipse that opens a monthly chapter and the lunar eclipse
that reveals it: command roots, final dispositors, raw distribution, exact
cross-chart relays, declination-only continuities, and Washington-local stage.

The full 2026 New-Moon-to-Full-Moon roster supplies a bounded control.  No
eclipse, visibility, or geometric pattern receives factual, causal, forecast,
or corroborative credit.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
HISTORY = HERE / "mundane_history.json"
BONES = HERE / "chart_reading_bones"
LOCAL = HERE / "eclipse_local_circumstances.json"
OUT = HERE / "eclipse_season_handoffs_2026.json"

BODY_NAMES = (
    "Sun", "Moon", "Mercury", "Venus", "Mars",
    "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto",
)
ASPECTS = (
    ("conjunction", 0.0),
    ("sextile", 60.0),
    ("square", 90.0),
    ("trine", 120.0),
    ("opposition", 180.0),
)
SEASONS = (
    {
        "label": "winter",
        "seed_id": "lun-2026-02-17-ne-solar",
        "full_id": "lun-2026-03-03-fu-lunar",
        "seed_date": "2026-02-17",
        "full_date": "2026-03-03",
        "knowledge_state": "retrospective",
    },
    {
        "label": "summer",
        "seed_id": "lun-2026-08-12-ne-solar",
        "full_id": "lun-2026-08-28-fu-lunar",
        "seed_date": "2026-08-12",
        "full_date": "2026-08-28",
        "knowledge_state": "retrospective_astronomy_and_chart_structure_at_cutoff",
    },
)


def rounded(value: float, places: int = 6) -> float:
    return round(float(value), places)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_bone(chart_id: str) -> dict:
    return json.loads((BONES / f"{chart_id}.json").read_text(encoding="utf-8"))


def angle_points(chart: dict) -> dict[str, float]:
    return {
        "ASC": chart["asc"] % 360.0,
        "DSC": (chart["asc"] + 180.0) % 360.0,
        "MC": chart["mc"] % 360.0,
        "IC": (chart["mc"] + 180.0) % 360.0,
    }


def body_points(chart: dict) -> dict[str, float]:
    return {name: chart["pos"][name]["lon"] % 360.0 for name in BODY_NAMES}


def angular_distance(first: float, second: float) -> float:
    return abs((second - first + 180.0) % 360.0 - 180.0)


def major_contact(first: float, second: float) -> tuple[str, float]:
    separation = angular_distance(first, second)
    name, angle = min(ASPECTS, key=lambda row: abs(separation - row[1]))
    return name, abs(separation - angle)


def contact(source_label: str, source_lon: float, target_label: str, target_lon: float) -> dict:
    aspect, orb = major_contact(source_lon, target_lon)
    return {
        "source": source_label,
        "target": target_label,
        "aspect": aspect,
        "orb_deg": rounded(orb),
        "source_longitude_deg": rounded(source_lon, 9),
        "target_longitude_deg": rounded(target_lon, 9),
    }


def root_transition(seed: dict, full: dict) -> dict:
    source = set(seed["root_members"])
    target = set(full["root_members"])
    return {
        "seed_root_members": sorted(source),
        "full_root_members": sorted(target),
        "shared_members": sorted(source & target),
        "added_members": sorted(target - source),
        "removed_members": sorted(source - target),
        "complete_replacement": not bool(source & target),
        "seed_final_dispositors": seed["finals"],
        "full_final_dispositors": full["finals"],
        "both_frames_without_final_dispositor": not seed["finals"] and not full["finals"],
    }


def persistent_declinations(seed: dict, full: dict) -> list[dict]:
    def key(row: dict) -> tuple:
        return (*sorted((row["a"], row["b"])), row["kind"])

    source = {key(row): row for row in seed["parallels"]}
    target = {key(row): row for row in full["parallels"]}
    rows = []
    for pair_key in sorted(source.keys() & target.keys()):
        before = source[pair_key]
        after = target[pair_key]
        rows.append({
            "pair": list(pair_key[:2]),
            "kind": pair_key[2],
            "seed_orb_deg": rounded(before["orb"]),
            "full_orb_deg": rounded(after["orb"]),
            "tightens": after["orb"] < before["orb"],
            "longitude_major_aspect_at_seed": any(
                {row["a"], row["b"]} == set(pair_key[:2]) for row in seed["aspects"]
            ),
            "longitude_major_aspect_at_full": any(
                {row["a"], row["b"]} == set(pair_key[:2]) for row in full["aspects"]
            ),
        })
    return rows


def local_stage(event: dict) -> dict:
    global_row = event["global"]
    local = event["washington"]
    return {
        "date": event["date"],
        "kind": event["kind"],
        "global_type": global_row["type"],
        "syzygy_utc": global_row["syzygy"]["utc"],
        "greatest_eclipse_utc": global_row["maximum"]["utc"],
        "syzygy_to_greatest_eclipse_signed_minutes": rounded(
            global_row["syzygy_minus_maximum_minutes"], 3
        ),
        "washington_status": local["status"],
        "washington_type": local["local_type"],
        "true_altitude_at_syzygy_deg": rounded(
            local.get(
                "sun_true_altitude_at_syzygy_deg",
                local.get("moon_true_altitude_at_syzygy_deg"),
            ),
            6,
        ),
        "true_altitude_at_greatest_eclipse_deg": rounded(
            local.get(
                "sun_true_altitude_at_global_max_deg",
                local.get("moon_true_altitude_at_global_max_deg"),
            ),
            6,
        ),
        "observable_solar_minutes": local.get("observable_minutes"),
        "visible_partial_lunar_minutes": (local.get("partial_phase") or {}).get(
            "minutes_above_horizon"
        ),
        "visible_total_lunar_minutes": (local.get("total_phase") or {}).get(
            "minutes_above_horizon"
        ),
        "umbral_magnitude": local.get("umbral_magnitude"),
    }


def full_root_receipts(seed: dict, full: dict) -> list[dict]:
    seed_bodies = body_points(seed)
    full_bodies = body_points(full)
    receipts = []
    for root in full["root_members"]:
        candidates = [
            contact(body, longitude, root, full_bodies[root])
            for body, longitude in seed_bodies.items()
        ]
        receipts.append(min(candidates, key=lambda row: (row["orb_deg"], row["source"])))
    return receipts


def minimum_seed_angle_to_full_light(seed: dict, full: dict) -> dict:
    candidates = [
        contact(angle, longitude, light, body_points(full)[light])
        for angle, longitude in angle_points(seed).items()
        for light in ("Sun", "Moon")
    ]
    return min(candidates, key=lambda row: (row["orb_deg"], row["source"], row["target"]))


def chapter_pairs_2026(history_rows: list[dict]) -> list[tuple[str, str]]:
    rows = sorted(
        [
            row for row in history_rows
            if row.get("utc", "").startswith("2026-")
            and row.get("chart_type") == "lunation"
            and (BONES / f"{row['id']}.json").exists()
        ],
        key=lambda row: row["jd_ut"],
    )
    pairs = []
    for index, seed in enumerate(rows):
        if "-ne" not in seed["id"]:
            continue
        full = next((row for row in rows[index + 1:] if "-fu" in row["id"]), None)
        close = next((row for row in rows[index + 1:] if "-ne" in row["id"]), None)
        if full and (close is None or full["jd_ut"] < close["jd_ut"]):
            pairs.append((seed["id"], full["id"]))
    return pairs


def build_control(history_rows: list[dict]) -> dict:
    rows = []
    for seed_id, full_id in chapter_pairs_2026(history_rows):
        seed = load_bone(seed_id)
        full = load_bone(full_id)
        transition = root_transition(seed, full)
        receipts = full_root_receipts(seed, full)
        angle_light = minimum_seed_angle_to_full_light(seed, full)
        rows.append({
            "seed_id": seed_id,
            "full_id": full_id,
            "complete_root_replacement_with_no_final_dispositor_in_either_frame": (
                transition["complete_replacement"]
                and transition["both_frames_without_final_dispositor"]
            ),
            "all_full_root_members_receive_seed_body_contact_within_0_25_deg": all(
                receipt["orb_deg"] <= 0.25 for receipt in receipts
            ),
            "full_root_receipts": receipts,
            "minimum_seed_angle_to_full_light": angle_light,
        })
    return {
        "scope": "twelve registered 2026 New-Moon-to-first-Full-Moon chapters with chart bones",
        "chapter_count": len(rows),
        "chapters": rows,
        "complete_root_replacement_no_final_dispositor_chapters": [
            row["seed_id"] for row in rows
            if row["complete_root_replacement_with_no_final_dispositor_in_either_frame"]
        ],
        "all_full_roots_exactly_reached_chapters": [
            row["seed_id"] for row in rows
            if row["all_full_root_members_receive_seed_body_contact_within_0_25_deg"]
        ],
        "seed_angle_to_full_light_within_1_deg_chapters": [
            row["seed_id"] for row in rows
            if row["minimum_seed_angle_to_full_light"]["orb_deg"] <= 1.0
        ],
        "boundary": (
            "These are bounded 2026 structural controls, not all-history rarity or event-frequency claims."
        ),
    }


def season_relays(label: str, seed: dict, full: dict) -> list[dict]:
    sb = body_points(seed)
    fb = body_points(full)
    sa = angle_points(seed)
    fa = angle_points(full)
    if label == "winter":
        return [
            contact("seed Mars", sb["Mars"], "Full MC", fa["MC"]),
            contact("seed Mars", sb["Mars"], "Full IC", fa["IC"]),
            contact("seed MC", sa["MC"], "Full Sun", fb["Sun"]),
            contact("seed MC", sa["MC"], "Full Moon", fb["Moon"]),
            contact("seed IC", sa["IC"], "Full Sun", fb["Sun"]),
            contact("seed IC", sa["IC"], "Full Moon", fb["Moon"]),
        ]
    return [
        contact("seed Sun", sb["Sun"], "Full Venus", fb["Venus"]),
        contact("seed Moon", sb["Moon"], "Full Venus", fb["Venus"]),
        contact("seed Uranus", sb["Uranus"], "Full Mercury", fb["Mercury"]),
        contact("seed Uranus", sb["Uranus"], "Full Sun", fb["Sun"]),
        contact("seed Uranus", sb["Uranus"], "Full Moon", fb["Moon"]),
        contact("seed Venus", sb["Venus"], "Full Uranus", fb["Uranus"]),
    ]


def build_payload() -> dict:
    history = json.loads(HISTORY.read_text(encoding="utf-8"))
    local = json.loads(LOCAL.read_text(encoding="utf-8"))
    local_by_date = {row["date"]: row for row in local["events"]}
    rows = []
    for spec in SEASONS:
        seed = load_bone(spec["seed_id"])
        full = load_bone(spec["full_id"])
        rows.append({
            "season": spec["label"],
            "knowledge_state_at_2026_09_25": spec["knowledge_state"],
            "solar_seed": {
                "chart_id": spec["seed_id"],
                "ascendant_sign": seed["asc_sign"],
                "chart_ruler": seed["ruler"],
                "root_members": seed["root_members"],
                "final_dispositors": seed["finals"],
                "occupied_span_deg": rounded(seed["occupied_deg"]),
                "largest_empty_arc_deg": rounded(seed["empty_deg"]),
                "local_stage": local_stage(local_by_date[spec["seed_date"]]),
            },
            "lunar_disclosure": {
                "chart_id": spec["full_id"],
                "ascendant_sign": full["asc_sign"],
                "chart_ruler": full["ruler"],
                "root_members": full["root_members"],
                "final_dispositors": full["finals"],
                "occupied_span_deg": rounded(full["occupied_deg"]),
                "largest_empty_arc_deg": rounded(full["empty_deg"]),
                "local_stage": local_stage(local_by_date[spec["full_date"]]),
            },
            "root_transition": root_transition(seed, full),
            "distribution_transition": {
                "occupied_span_change_deg": rounded(full["occupied_deg"] - seed["occupied_deg"]),
                "largest_empty_arc_change_deg": rounded(full["empty_deg"] - seed["empty_deg"]),
            },
            "persistent_declination_relationships": persistent_declinations(seed, full),
            "cross_chart_relays": season_relays(spec["label"], seed, full),
            "full_root_receipts": full_root_receipts(seed, full),
            "clock_boundary": (
                "The solar eclipse governs the monthly chapter; the lunar eclipse reveals it. "
                "Saros, Metonic, Pessin Moon-family, ingress and direct relationship clocks remain distinct."
            ),
        })

    return {
        "schema": "freedom250.eclipse-season-handoffs-2026/v1",
        "status": "retrospective_structural_companion",
        "developed_through": "2026-09-25",
        "authority_boundary": {
            "locked_readings_preserved": True,
            "factual_evidence_credit": "zero",
            "forecast_ledger_credit": "zero",
            "causal_claim": False,
            "future_claim": False,
        },
        "seasons": rows,
        "bounded_lunation_control": build_control(history["charts"]),
        "interpretive_synthesis": {
            "winter": (
                "The Aquarius identity seed and its Mars-Saturn command loop rotate into a Virgo-Pisces "
                "relationship disclosure with a wholly new Jupiter-Moon-Mercury root. The seed Mars lands "
                "on the Full chart's meridian within 0.071 degrees while the seed meridian squares the Full "
                "lights within 0.679 degrees: command and stage exchange jobs across the chapter."
            ),
            "summer": (
                "The Leo public-authority seed retains Venus while exchanging Sun for Mercury at the root. "
                "The seed lights sextile Full Venus within 0.0014 degrees and seed Uranus squares Full Mercury "
                "within 0.0245 degrees, so both Full final dispositors receive an exact-band seed relay."
            ),
            "whole": (
                "Both eclipse chapters open their occupied sky at Full phase, but winter changes the whole "
                "command circuit while summer preserves a Venus bridge. Literal visibility also grows from "
                "absent or partial solar staging toward a more embodied lunar disclosure without transferring "
                "governance or supplying evidence credit."
            ),
        },
        "provenance": {
            "builder": "99 - Templates/build_2026_eclipse_season_handoffs.py",
            "history": "99 - Templates/mundane_history.json",
            "history_sha256": sha256(HISTORY),
            "local_circumstances": "99 - Templates/eclipse_local_circumstances.json",
            "local_circumstances_sha256": sha256(LOCAL),
            "bones_index": "99 - Templates/chart_reading_bones/index.json",
            "bones_index_sha256": sha256(BONES / "index.json"),
        },
    }


def main() -> None:
    payload = build_payload()
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
