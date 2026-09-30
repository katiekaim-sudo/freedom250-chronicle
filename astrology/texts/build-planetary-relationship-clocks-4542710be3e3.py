#!/usr/bin/env python3
"""Build the review-only 28-pair Planetary Relationship Clock graph.

This is a sibling projection of the universal DR-020 phase table.  It does not
change DR-065's governed ten-hand Long Clocks instrument, chart-reading bones,
Transit Weather, factual plot ownership, or the Forecast Ledger.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
DEFAULT_VAULT = Path("Chronicle/")
DEFAULT_REGISTRY = HERE / "planetary_relationship_registry.json"
DEFAULT_OUTPUT = HERE / "planetary_relationship_clock_graph.json"
LATE_YEAR_HANDOFF_CHART_IDS = [
    "lun-2026-12-09-ne",
    "ingress-2026-capricorn",
    "lun-2026-12-24-fu",
]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if not spec or not spec.loader:
        raise RuntimeError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def motion_state(delta: float, relative_speed: float) -> tuple[str, bool, bool]:
    if abs(delta) <= 1e-7:
        return "exact", False, False
    if abs(relative_speed) <= 1e-8:
        return "stationary", False, False
    applying = delta * relative_speed < 0.0
    return ("applying" if applying else "separating"), applying, not applying


def aspect_strength(orb_deg: float) -> str:
    if orb_deg <= 0.25:
        return "exact"
    if orb_deg <= 1.5:
        return "tight"
    return "active"


def relationship_field_metrics(states: list[dict[str, Any]]) -> dict[str, Any]:
    """Derive the direct/phase overlap without turning either lane into a score."""
    direct_ids = [state["cycle_id"] for state in states if state["direct_aspect"]]
    nameable_ids = [
        state["cycle_id"]
        for state in states
        if state["dr020_nameability"]["earned"]
    ]
    direct_set = set(direct_ids)
    nameable_set = set(nameable_ids)
    ordered_ids = [state["cycle_id"] for state in states]
    both_ids = [cycle_id for cycle_id in ordered_ids if cycle_id in direct_set and cycle_id in nameable_set]
    direct_only_ids = [cycle_id for cycle_id in ordered_ids if cycle_id in direct_set and cycle_id not in nameable_set]
    phase_only_ids = [cycle_id for cycle_id in ordered_ids if cycle_id in nameable_set and cycle_id not in direct_set]
    silent_ids = [cycle_id for cycle_id in ordered_ids if cycle_id not in direct_set and cycle_id not in nameable_set]
    return {
        "direct_count": len(direct_ids),
        "nameable_phase_count": len(nameable_ids),
        "both_count": len(both_ids),
        "direct_only_count": len(direct_only_ids),
        "phase_only_count": len(phase_only_ids),
        "silent_count": len(silent_ids),
        "both_cycle_ids": both_ids,
        "direct_only_cycle_ids": direct_only_ids,
        "phase_only_cycle_ids": phase_only_ids,
        "silent_cycle_ids": silent_ids,
    }


def corpus_field_control(chart_rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Expose corpus controls for a late-year field handoff found in review."""
    direct_exceeds = [
        chart["chart_id"]
        for chart in chart_rows
        if chart["field_metrics"]["direct_count"]
        > chart["field_metrics"]["nameable_phase_count"]
    ]
    max_direct_only = max(
        chart["field_metrics"]["direct_only_count"] for chart in chart_rows
    )
    max_direct_only_ids = [
        chart["chart_id"]
        for chart in chart_rows
        if chart["field_metrics"]["direct_only_count"] == max_direct_only
    ]
    by_id = {chart["chart_id"]: chart for chart in chart_rows}
    missing = [chart_id for chart_id in LATE_YEAR_HANDOFF_CHART_IDS if chart_id not in by_id]
    if missing:
        raise ValueError(f"Missing late-year handoff charts: {missing}")

    handoff_rows = []
    for chart_id in LATE_YEAR_HANDOFF_CHART_IDS:
        chart = by_id[chart_id]
        handoff_rows.append(
            {
                "chart_id": chart_id,
                "date": chart["date"],
                **{
                    key: chart["field_metrics"][key]
                    for key in (
                        "direct_count",
                        "nameable_phase_count",
                        "both_count",
                        "direct_only_count",
                        "phase_only_count",
                        "silent_count",
                    )
                },
            }
        )

    dec09 = by_id[LATE_YEAR_HANDOFF_CHART_IDS[0]]
    capricorn = by_id[LATE_YEAR_HANDOFF_CHART_IDS[1]]
    ordered_cycle_ids = [state["cycle_id"] for state in dec09["cycles"]]
    dec09_direct = set(dec09["active_direct_cycle_ids"])
    capricorn_direct = set(capricorn["active_direct_cycle_ids"])
    dec09_nameable = set(dec09["nameable_cycle_ids"])
    capricorn_nameable = set(capricorn["nameable_cycle_ids"])
    metric_keys = (
        "direct_count",
        "nameable_phase_count",
        "both_count",
        "direct_only_count",
        "phase_only_count",
        "silent_count",
    )
    chronological = sorted(chart_rows, key=lambda chart: chart["utc"])
    count_twins = []
    for earlier, later in zip(chronological, chronological[1:]):
        if any(
            earlier["field_metrics"][key] != later["field_metrics"][key]
            for key in metric_keys
        ):
            continue
        earlier_direct = set(earlier["active_direct_cycle_ids"])
        later_direct = set(later["active_direct_cycle_ids"])
        earlier_nameable = set(earlier["nameable_cycle_ids"])
        later_nameable = set(later["nameable_cycle_ids"])
        order = [state["cycle_id"] for state in later["cycles"]]
        count_twins.append(
            {
                "from_chart_id": earlier["chart_id"],
                "to_chart_id": later["chart_id"],
                "from_date": earlier["date"],
                "to_date": later["date"],
                "shared_counts": {
                    key: later["field_metrics"][key] for key in metric_keys
                },
                "direct_cycle_ids_left": [
                    cycle_id for cycle_id in order
                    if cycle_id in earlier_direct and cycle_id not in later_direct
                ],
                "direct_cycle_ids_entered": [
                    cycle_id for cycle_id in order
                    if cycle_id in later_direct and cycle_id not in earlier_direct
                ],
                "phase_nameability_ids_left": [
                    cycle_id for cycle_id in order
                    if cycle_id in earlier_nameable and cycle_id not in later_nameable
                ],
                "phase_nameability_ids_entered": [
                    cycle_id for cycle_id in order
                    if cycle_id in later_nameable and cycle_id not in earlier_nameable
                ],
            }
        )
    return {
        "boundary": {
            "direct_aspect_and_phase_nameability_are_independent": True,
            "counts_are_census_not_strength_score": True,
            "no_evidence_or_forecast_credit": True,
        },
        "direct_exceeds_nameable_phase": {
            "chart_count": len(direct_exceeds),
            "chart_ids": direct_exceeds,
        },
        "maximum_direct_only": {
            "count": max_direct_only,
            "chart_ids": max_direct_only_ids,
        },
        "consecutive_equal_count_identity_turnovers": count_twins,
        "late_year_handoff": {
            "chart_ids": LATE_YEAR_HANDOFF_CHART_IDS,
            "rows": handoff_rows,
            "december_09_to_capricorn_ingress": {
                "direct_count_delta": (
                    capricorn["field_metrics"]["direct_count"]
                    - dec09["field_metrics"]["direct_count"]
                ),
                "nameable_phase_count_delta": (
                    capricorn["field_metrics"]["nameable_phase_count"]
                    - dec09["field_metrics"]["nameable_phase_count"]
                ),
                "direct_cycle_ids_left": [
                    cycle_id
                    for cycle_id in ordered_cycle_ids
                    if cycle_id in dec09_direct and cycle_id not in capricorn_direct
                ],
                "direct_cycle_ids_entered": [
                    cycle_id
                    for cycle_id in ordered_cycle_ids
                    if cycle_id in capricorn_direct and cycle_id not in dec09_direct
                ],
                "phase_nameability_ids_gained": [
                    cycle_id
                    for cycle_id in ordered_cycle_ids
                    if cycle_id in capricorn_nameable and cycle_id not in dec09_nameable
                ],
                "phase_nameability_ids_lost": [
                    cycle_id
                    for cycle_id in ordered_cycle_ids
                    if cycle_id in dec09_nameable and cycle_id not in capricorn_nameable
                ],
            },
        },
    }


def state_for_chart(
    *,
    cycle: dict[str, Any],
    bone: dict[str, Any],
    phases: Any,
    synodic: Any,
    tier_order: dict[str, int],
) -> dict[str, Any]:
    slow, fast = synodic.slow_fast(cycle["pair"])
    positions = {slow: bone["pos"][slow]["lon"], fast: bone["pos"][fast]["lon"]}
    speeds = {slow: bone["pos"][slow]["spd"], fast: bone["pos"][fast]["spd"]}
    angle = (positions[fast] - positions[slow]) % 360.0
    relative_speed = speeds[fast] - speeds[slow]
    raw_phase_name, raw_phase_direction = phases.phase_of(angle)
    chapter, orb_deg, delta = synodic.nearest_chapter(angle)
    orb_limit = synodic.ORB_LIMITS[chapter["aspect_id"]]
    active = orb_deg <= orb_limit
    movement, applying, separating = motion_state(delta, relative_speed)
    direct_aspect = None
    if active:
        direct_aspect = {
            "aspect_id": chapter["aspect_id"],
            "chapter_id": chapter["chapter_id"],
            "angle_deg": chapter["angle_deg"],
            "orb_deg": round(orb_deg, 6),
            "orb_limit_deg": orb_limit,
            "applying": applying,
            "separating": separating,
            "motion_state": movement,
            "strength": aspect_strength(orb_deg),
            "flow_kind": chapter["flow_kind"],
        }

    limited_model = cycle["phase_model"] == "limited_geocentric_elongation"
    if limited_model:
        # Mercury-Venus never reaches a geocentric opposition and its directed
        # hand reverses.  The universal phase table can still identify the raw
        # angular sector, but that sector is not an admissible synodic phase.
        phase_name = None
        phase_direction = None
        nameability = {
            "earned": False,
            "reasons": ["phase_contract_unresolved"],
            "evidence": [],
            "applies_to": "phase_narrative_only",
            "does_not_hide_direct_aspect": True,
        }
    else:
        phase_name = raw_phase_name
        phase_direction = raw_phase_direction
        nameability = synodic.phase_nameability(bone, cycle)
    return {
        "cycle_id": cycle["cycle_id"],
        "tier_id": cycle["tier_id"],
        "tier_order": tier_order[cycle["tier_id"]],
        "cycle_order": cycle["order"],
        "pair": list(cycle["pair"]),
        "slow_body": slow,
        "fast_body": fast,
        "relationship_status": cycle["status"],
        "source_path": cycle["source_path"],
        "phase_model": cycle["phase_model"],
        "phase_model_limited": limited_model,
        "phase_model_note": cycle.get("phase_model_note"),
        "geometry": {
            "elongation_deg": round(angle, 6),
            "phase_name": phase_name,
            "phase_direction": phase_direction,
            "phase_contract_available": not limited_model,
            "raw_directed_sector_label": raw_phase_name if limited_model else None,
            "raw_directed_sector_direction": raw_phase_direction if limited_model else None,
            "relative_speed_deg_per_day": round(relative_speed, 9),
            "positions_deg": {
                slow: round(positions[slow], 6),
                fast: round(positions[fast], 6),
            },
            "nearest_major_chapter_id": chapter["chapter_id"],
            "nearest_major_chapter_angle_deg": chapter["angle_deg"],
            "nearest_major_chapter_orb_deg": round(orb_deg, 6),
            "nearest_major_chapter_within_orb": active,
        },
        "direct_aspect": direct_aspect,
        "dr020_nameability": nameability,
        "interpretive_status": "active_direct_aspect" if active else "between_major_aspects",
        "reading_boundary": {
            "direct_aspect_always_visible": True,
            "phase_prose_requires_dr020_nameability": True,
            "plotline_test_is_separate_review_lane": True,
            "evidence_credit": 0,
        },
    }


def build(vault_root: Path, registry_path: Path) -> dict[str, Any]:
    registry = load_json(registry_path)
    cycles = registry["cycles"]
    tiers = registry["tiers"]
    tier_order = {row["tier_id"]: row["order"] for row in tiers}
    if len(cycles) != 28 or len({row["cycle_id"] for row in cycles}) != 28:
        raise ValueError("Relationship registry must contain exactly 28 unique cycles")

    phases_path = vault_root / "99 - Templates" / "phases.py"
    synodic_path = vault_root / "99 - Templates" / "synodic_cycles.py"
    chart_index_path = vault_root / "99 - Templates" / "chart_reading_bones" / "index.json"
    phases = load_module("f250_relationship_phases", phases_path)
    synodic = load_module("f250_relationship_synodic", synodic_path)
    chart_index = load_json(chart_index_path)
    charts = chart_index.get("charts", [])
    if len(charts) != 30:
        raise ValueError(f"Expected 30 governed chart bones, found {len(charts)}")

    cycle_catalog = []
    for cycle in cycles:
        source = vault_root / cycle["source_path"]
        if not source.exists():
            raise FileNotFoundError(source)
        cycle_catalog.append(
            {
                **cycle,
                "source_sha256": sha256(source),
            }
        )

    chart_rows = []
    for chart_meta in charts:
        bone_path = (
            vault_root
            / "99 - Templates"
            / "chart_reading_bones"
            / f"{chart_meta['id']}.json"
        )
        bone = load_json(bone_path)
        states = [
            state_for_chart(
                cycle=cycle,
                bone=bone,
                phases=phases,
                synodic=synodic,
                tier_order=tier_order,
            )
            for cycle in cycles
        ]
        states.sort(key=lambda row: (row["tier_order"], row["cycle_order"]))
        metrics = relationship_field_metrics(states)
        chart_rows.append(
            {
                "chart_id": chart_meta["id"],
                "chart_type": chart_meta["type"],
                "date": chart_meta["date"],
                "utc": bone["utc"],
                "governing": chart_meta.get("governing"),
                "rising_sign": bone["asc_sign"],
                "chart_ruler": bone.get("ruler"),
                "root_members": bone.get("root_members") or [],
                "nameable_cycle_ids": [
                    state["cycle_id"]
                    for state in states
                    if state["dr020_nameability"]["earned"]
                ],
                "active_direct_cycle_ids": [
                    state["cycle_id"] for state in states if state["direct_aspect"]
                ],
                "field_metrics": metrics,
                "cycles": states,
                "source_bone_path": str(bone_path.relative_to(vault_root)),
                "source_bone_sha256": sha256(bone_path),
            }
        )

    inside_ids = [row["cycle_id"] for row in cycles if row["status"] == "candidate_relationship_clock"]
    long_ids = [row["cycle_id"] for row in cycles if row["status"] == "active_long_clock"]
    return {
        "schema": "freedom250.planetary-relationship-clock-graph/v0.2",
        "status": "proposal_for_review",
        "deterministic": True,
        "scope": {
            "bodies": ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"],
            "sun_excluded": True,
            "moon_excluded": True,
            "relationship_count": 28,
            "inside_relationship_count": 18,
            "inside_phaseable_relationship_count": 17,
            "limited_geometry_relationship_count": 1,
            "existing_long_clock_count": 10,
        },
        "governance": registry["authority_boundary"],
        "method": {
            "phase_authority": "DR-020 via 99 - Templates/phases.py",
            "direct_aspect_orbs": "Katie's workbook orbs via 99 - Templates/synodic_cycles.py",
            "long_clocks_boundary": "DR-065 remains exactly ten governed hands",
            "phase_and_direct_aspect_independent": True,
            "plotline_join_authority": "review_only_many_to_many",
            "mercury_venus_exception": "limited geocentric elongation; do not imply a physically unavailable opposition/full-phase arc",
        },
        "source": {
            "registry_path": str(registry_path),
            "registry_sha256": sha256(registry_path),
            "phase_engine_path": str(phases_path.relative_to(vault_root)),
            "phase_engine_sha256": sha256(phases_path),
            "direct_aspect_engine_path": str(synodic_path.relative_to(vault_root)),
            "direct_aspect_engine_sha256": sha256(synodic_path),
            "chart_index_path": str(chart_index_path.relative_to(vault_root)),
            "chart_index_sha256": sha256(chart_index_path),
        },
        "tiers": tiers,
        "cycle_catalog": cycle_catalog,
        "coverage": {
            "chart_count": len(chart_rows),
            "relationship_count": len(cycles),
            "relationship_state_count": len(chart_rows) * len(cycles),
            "inside_relationship_state_count": len(chart_rows) * len(inside_ids),
            "inside_phaseable_state_count": len(chart_rows) * 17,
            "limited_geometry_state_count": len(chart_rows),
            "existing_long_clock_state_count": len(chart_rows) * len(long_ids),
        },
        "corpus_field_control": corpus_field_control(chart_rows),
        "charts": chart_rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault-root", type=Path, default=DEFAULT_VAULT)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    payload = build(args.vault_root, args.registry)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        "RELATIONSHIP CLOCKS: wrote "
        f"{args.output} · {payload['coverage']['chart_count']} charts · "
        f"{payload['coverage']['relationship_state_count']} states"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
