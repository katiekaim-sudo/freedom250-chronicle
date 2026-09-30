#!/usr/bin/env python3
"""Build the deterministic 28-pair relationship geometry/history contract.

The canonical ten-hand ``chart_synodic_stacks.json`` remains untouched.  This
sibling contract copies its factual geometry for those ten relationships,
computes seventeen candidate phaseable inside-planet relationships plus the
limited-geometry Mercury-Venus relationship, and orders all 28 through the
same thirty governed chart moments.  It contains no story, plot, evidence,
forecast, nameability, or interpretive-result fields.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from datetime import datetime
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE / "planetary_relationship_history.json"
DEFAULT_INSIDE_SOURCE = HERE / "inside_relationship_seed_families.json"
DEFAULT_LONG_SEEDS = HERE / "synodic_seed_families.json"
DEFAULT_LONG_STACKS = HERE / "chart_synodic_stacks.json"

SCHEMA_ID = "freedom250.planetary-relationships.geometry-history/v1"
EXPECTED_LONG_IDS = {
    "neptune-pluto",
    "uranus-neptune",
    "uranus-pluto",
    "saturn-uranus",
    "saturn-neptune",
    "saturn-pluto",
    "jupiter-saturn",
    "jupiter-uranus",
    "jupiter-neptune",
    "jupiter-pluto",
}
TIER_ORDER = {
    "era_currents": 1,
    "state_architecture": 2,
    "political_delivery": 3,
    "operational_delivery": 4,
    "value_alliance_delivery": 5,
    "signal_transaction_delivery": 6,
}
INSIDE_TIER_MAP = {
    "delivery_mars": "operational_delivery",
    "delivery_venus": "value_alliance_delivery",
    "delivery_mercury": "signal_transaction_delivery",
}
TIER_LABELS = {
    "era_currents": "Era currents",
    "state_architecture": "State architecture",
    "political_delivery": "Political delivery",
    "operational_delivery": "Action and force",
    "value_alliance_delivery": "Value and alliance",
    "signal_transaction_delivery": "Signal and transaction",
}
FORBIDDEN_OUTPUT_KEYS = {
    "storyline",
    "storylines",
    "plotline",
    "plotlines",
    "finding",
    "findings",
    "ownership",
    "evidence",
    "forecast",
    "domains",
    "enduring_question",
    "nameability",
    "dr020_nameability",
}
FORBIDDEN_OUTPUT_KEY_FRAGMENTS = {
    "storyline",
    "plotline",
    "finding",
    "ownership",
    "evidence",
    "forecast",
    "nameability",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if not spec or not spec.loader:
        raise RuntimeError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_utc(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def pair_from_id(relationship_id: str) -> list[str]:
    return [part.capitalize() for part in relationship_id.split("-")]


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


def inside_source_index(source: dict[str, Any]):
    columns = source["cycle_columns"]
    rows = [dict(zip(columns, row, strict=True)) for row in source["cycles"]]
    family_columns = source["family_columns"]
    pass_columns = source["pass_columns"]
    families: dict[str, list[dict[str, Any]]] = {}
    for raw in source["families"]:
        family = dict(zip(family_columns, raw, strict=True))
        family["passes"] = [
            dict(zip(pass_columns, item, strict=True)) for item in family["passes"]
        ]
        families.setdefault(family["cycle_id"], []).append(family)
    return rows, families


def mercury_venus_events(source: dict[str, Any]) -> list[dict[str, Any]]:
    block = source["mercury_venus_exception"]
    columns = block["crossing_columns"]
    events = []
    for raw in block["crossings"]:
        row = dict(zip(columns, raw, strict=True))
        row["event_id"] = f"mercury-venus-{row['utc'][:10].replace('-', '')}-crossing"
        events.append(row)
    return events


def seed_context(
    moment: datetime,
    *,
    families: list[dict[str, Any]],
    events: list[dict[str, Any]],
    phaseable: bool,
) -> dict[str, Any]:
    ordered_events = sorted(events, key=lambda row: parse_utc(row["utc"]))
    previous = [row for row in ordered_events if parse_utc(row["utc"]) <= moment]
    following = [row for row in ordered_events if parse_utc(row["utc"]) > moment]
    active_family_id = None
    if phaseable:
        eligible = [
            family
            for family in families
            if parse_utc(family["passes"][0]["utc"]) <= moment
        ]
        if eligible:
            active_family_id = max(
                eligible, key=lambda row: parse_utc(row["passes"][0]["utc"])
            )["seed_family_id"]
    return {
        "active_seed_family_id": active_family_id,
        "previous_conjunction_event_id": previous[-1]["event_id"] if previous else None,
        "next_conjunction_event_id": following[0]["event_id"] if following else None,
    }


def direct_aspect(
    *, angle: float, relative_speed: float, synodic: Any
) -> tuple[dict[str, Any] | None, dict[str, Any]]:
    chapter, orb_deg, delta = synodic.nearest_chapter(angle)
    orb_limit = synodic.ORB_LIMITS[chapter["aspect_id"]]
    movement, applying, separating = motion_state(delta, relative_speed)
    active = orb_deg <= orb_limit
    aspect = None
    if active:
        aspect = {
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
    nearest = {
        "nearest_chapter_id": chapter["chapter_id"],
        "nearest_chapter_angle_deg": chapter["angle_deg"],
        "nearest_chapter_orb_deg": round(orb_deg, 6),
        "nearest_chapter_within_orb": active,
    }
    return aspect, nearest


def inside_state(
    *,
    chart_id: str,
    bone: dict[str, Any],
    catalog: dict[str, Any],
    families: list[dict[str, Any]],
    events: list[dict[str, Any]],
    phase_func: Any,
    synodic: Any,
) -> dict[str, Any]:
    slow, fast = synodic.slow_fast(catalog["pair"])
    slow_lon = bone["pos"][slow]["lon"]
    fast_lon = bone["pos"][fast]["lon"]
    slow_speed = bone["pos"][slow]["spd"]
    fast_speed = bone["pos"][fast]["spd"]
    angle = (fast_lon - slow_lon) % 360.0
    relative_speed = fast_speed - slow_speed
    phaseable = catalog["phase_contract"] == "eight_phase"
    phase_name, phase_direction = phase_func(angle) if phaseable else (None, None)
    aspect, nearest = direct_aspect(
        angle=angle, relative_speed=relative_speed, synodic=synodic
    )
    return {
        "state_id": f"{chart_id}::{catalog['relationship_id']}",
        "relationship_id": catalog["relationship_id"],
        "tier_id": catalog["tier_id"],
        "pair": catalog["pair"],
        "slow_body": slow,
        "fast_body": fast,
        "authority_status": catalog["authority_status"],
        "phase_contract": catalog["phase_contract"],
        "geometry": {
            "elongation_deg": round(angle, 6),
            "phase_name": phase_name,
            "phase_direction": phase_direction,
            "phase_contract_available": phaseable,
            "relative_speed_deg_per_day": round(relative_speed, 9),
            "positions_deg": {
                slow: round(slow_lon, 6),
                fast: round(fast_lon, 6),
            },
            **nearest,
        },
        "direct_aspect": aspect,
        "seed_context": seed_context(
            parse_utc(bone["utc"]),
            families=families,
            events=events,
            phaseable=phaseable,
        ),
    }


def long_state(
    *,
    chart_id: str,
    chart_utc: str,
    canonical_state: dict[str, Any],
    catalog: dict[str, Any],
    family: dict[str, Any],
) -> dict[str, Any]:
    events = [
        {**row, "event_id": row["pass_id"]} for row in family["passes"]
    ]
    geometry = {
        **canonical_state["geometry"],
        "phase_contract_available": True,
    }
    return {
        "state_id": f"{chart_id}::{catalog['relationship_id']}",
        "relationship_id": catalog["relationship_id"],
        "tier_id": catalog["tier_id"],
        "pair": catalog["pair"],
        "slow_body": canonical_state["slow_body"],
        "fast_body": canonical_state["fast_body"],
        "authority_status": catalog["authority_status"],
        "phase_contract": catalog["phase_contract"],
        "geometry": geometry,
        "direct_aspect": canonical_state["active_aspect"],
        "seed_context": seed_context(
            parse_utc(chart_utc),
            families=[
                {
                    "seed_family_id": family["seed_family_id"],
                    "passes": events,
                }
            ],
            events=events,
            phaseable=True,
        ),
    }


def transition_kind(before: dict[str, Any] | None, after: dict[str, Any] | None) -> str:
    if before is None and after is None:
        return "none"
    if before is None:
        return "entered"
    if after is None:
        return "exited"
    if before["chapter_id"] != after["chapter_id"]:
        return "changed_chapter"
    if before["motion_state"] != after["motion_state"]:
        return "changed_motion"
    return "continued"


def build_histories(charts: list[dict[str, Any]], catalog: list[dict[str, Any]]) -> list[dict[str, Any]]:
    ordered = sorted(charts, key=lambda row: parse_utc(row["utc"]))
    state_lookup = {
        (chart["chart_id"], state["relationship_id"]): state
        for chart in ordered
        for state in chart["cycles"]
    }
    histories = []
    for relationship in catalog:
        relationship_id = relationship["relationship_id"]
        states = [state_lookup[(chart["chart_id"], relationship_id)] for chart in ordered]
        deltas = []
        for before_chart, after_chart, before, after in zip(
            ordered[:-1], ordered[1:], states[:-1], states[1:], strict=True
        ):
            before_aspect = before["direct_aspect"]
            after_aspect = after["direct_aspect"]
            deltas.append(
                {
                    "delta_id": f"{relationship_id}::{before_chart['chart_id']}->{after_chart['chart_id']}",
                    "from_state_id": before["state_id"],
                    "to_state_id": after["state_id"],
                    "from_chart_id": before_chart["chart_id"],
                    "to_chart_id": after_chart["chart_id"],
                    "from_utc": before_chart["utc"],
                    "to_utc": after_chart["utc"],
                    "phase_changed": before["geometry"]["phase_name"] != after["geometry"]["phase_name"],
                    "phase_from": before["geometry"]["phase_name"],
                    "phase_to": after["geometry"]["phase_name"],
                    "direct_aspect_transition": transition_kind(before_aspect, after_aspect),
                    "direct_aspect_from": before_aspect["chapter_id"] if before_aspect else None,
                    "direct_aspect_to": after_aspect["chapter_id"] if after_aspect else None,
                    "seed_family_changed": before["seed_context"]["active_seed_family_id"]
                    != after["seed_context"]["active_seed_family_id"],
                    "seed_family_from": before["seed_context"]["active_seed_family_id"],
                    "seed_family_to": after["seed_context"]["active_seed_family_id"],
                }
            )
        histories.append(
            {
                "relationship_id": relationship_id,
                "tier_id": relationship["tier_id"],
                "pair": relationship["pair"],
                "authority_status": relationship["authority_status"],
                "phase_contract": relationship["phase_contract"],
                "ordered_state_ids": [state["state_id"] for state in states],
                "deltas": deltas,
            }
        )
    return histories


def forbidden_paths(value: Any, prefix: str = "") -> list[str]:
    found = []
    if isinstance(value, dict):
        for key, child in value.items():
            path = f"{prefix}.{key}" if prefix else key
            normalized = key.lower()
            if key in FORBIDDEN_OUTPUT_KEYS or any(
                fragment in normalized for fragment in FORBIDDEN_OUTPUT_KEY_FRAGMENTS
            ):
                found.append(path)
            found.extend(forbidden_paths(child, path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(forbidden_paths(child, f"{prefix}[{index}]"))
    return found


def validate_payload(payload: dict[str, Any], canonical: dict[str, Any]) -> None:
    errors = []
    if payload.get("schema") != SCHEMA_ID:
        errors.append(f"schema: expected {SCHEMA_ID}, got {payload.get('schema')}")
    coverage = payload["coverage"]
    expected = {
        "chart_count": 30,
        "relationship_count": 28,
        "relationship_state_count": 840,
        "canonical_long_clock_state_count": 300,
        "candidate_inside_state_count": 540,
        "phaseable_inside_state_count": 510,
        "limited_geometry_state_count": 30,
        "history_count": 28,
        "history_delta_count": 812,
    }
    for key, wanted in expected.items():
        if coverage.get(key) != wanted:
            errors.append(f"coverage.{key}: expected {wanted}, got {coverage.get(key)}")
    forbidden = forbidden_paths(payload)
    if forbidden:
        errors.append("forbidden semantic fields: " + ", ".join(forbidden[:10]))
    catalog = payload["cycle_catalog"]
    catalog_ids = [row["relationship_id"] for row in catalog]
    if len(catalog_ids) != 28 or len(set(catalog_ids)) != 28:
        errors.append("cycle_catalog must contain exactly 28 unique relationships")
    status_counts = {
        status: sum(row["authority_status"] == status for row in catalog)
        for status in {
            "canonical_long_clock",
            "candidate_phaseable",
            "candidate_limited_geometry",
        }
    }
    if status_counts != {
        "canonical_long_clock": 10,
        "candidate_phaseable": 17,
        "candidate_limited_geometry": 1,
    }:
        errors.append(f"authority-status distribution mismatch: {status_counts}")
    limited_ids = [
        row["relationship_id"]
        for row in catalog
        if row["phase_contract"] == "limited_geometry"
    ]
    if limited_ids != ["mercury-venus"]:
        errors.append(f"limited geometry must be Mercury-Venus only: {limited_ids}")

    ordered_charts = sorted(payload["charts"], key=lambda row: parse_utc(row["utc"]))
    chart_ids = [row["chart_id"] for row in ordered_charts]
    if len(chart_ids) != 30 or len(set(chart_ids)) != 30:
        errors.append("charts must contain exactly 30 unique chart IDs")
    state_lookup: dict[str, dict[str, Any]] = {}
    for chart in ordered_charts:
        states = chart["cycles"]
        relationship_ids = [row["relationship_id"] for row in states]
        if relationship_ids != catalog_ids:
            errors.append(f"catalog/state ordering mismatch: {chart['chart_id']}")
        active_ids = [
            row["relationship_id"] for row in states if row["direct_aspect"] is not None
        ]
        if chart["active_direct_relationship_ids"] != active_ids:
            errors.append(f"active-direct index mismatch: {chart['chart_id']}")
        for state in states:
            expected_state_id = f"{chart['chart_id']}::{state['relationship_id']}"
            if state["state_id"] != expected_state_id:
                errors.append(f"state identity mismatch: {state['state_id']}")
            if state["state_id"] in state_lookup:
                errors.append(f"duplicate state identity: {state['state_id']}")
            state_lookup[state["state_id"]] = state
            geometry = state["geometry"]
            if state["relationship_id"] == "mercury-venus":
                if geometry["phase_name"] is not None or geometry["phase_direction"] is not None:
                    errors.append(f"Mercury-Venus phase must be null: {state['state_id']}")
                if geometry["phase_contract_available"]:
                    errors.append(f"Mercury-Venus phase contract must be unavailable: {state['state_id']}")
            elif (
                geometry["phase_name"] is None
                or geometry["phase_direction"] is None
                or not geometry["phase_contract_available"]
            ):
                errors.append(f"phaseable relationship missing phase: {state['state_id']}")

    histories = payload["histories"]
    if [row["relationship_id"] for row in histories] != catalog_ids:
        errors.append("history/catalog ordering mismatch")
    for history in histories:
        relationship_id = history["relationship_id"]
        expected_state_ids = [
            f"{chart_id}::{relationship_id}" for chart_id in chart_ids
        ]
        if history["ordered_state_ids"] != expected_state_ids:
            errors.append(f"ordered state history mismatch: {relationship_id}")
        if len(history["deltas"]) != 29:
            errors.append(f"expected 29 deltas: {relationship_id}")
        for index, delta in enumerate(history["deltas"]):
            if (
                delta["from_state_id"] != expected_state_ids[index]
                or delta["to_state_id"] != expected_state_ids[index + 1]
                or delta["from_state_id"] not in state_lookup
                or delta["to_state_id"] not in state_lookup
                or parse_utc(delta["from_utc"]) >= parse_utc(delta["to_utc"])
            ):
                errors.append(f"history delta linkage mismatch: {delta['delta_id']}")

    canonical_by_chart = {row["chart_id"]: row for row in canonical["charts"]}
    checked = 0
    for chart in payload["charts"]:
        old_states = {
            row["cycle_id"]: row for row in canonical_by_chart[chart["chart_id"]]["cycles"]
        }
        for state in chart["cycles"]:
            if state["relationship_id"] not in EXPECTED_LONG_IDS:
                continue
            old = old_states[state["relationship_id"]]
            geometry = dict(state["geometry"])
            geometry.pop("phase_contract_available")
            if geometry != old["geometry"]:
                errors.append(f"geometry parity failed: {state['state_id']}")
            if state["direct_aspect"] != old["active_aspect"]:
                errors.append(f"direct-aspect parity failed: {state['state_id']}")
            checked += 1
    if checked != 300:
        errors.append(f"expected 300 canonical parity states, checked {checked}")
    if errors:
        raise ValueError("Relationship history validation failed:\n- " + "\n- ".join(errors))


def build(
    *,
    vault_root: Path,
    inside_source_path: Path,
    long_seed_path: Path,
    long_stack_path: Path,
) -> dict[str, Any]:
    canonical = load_json(long_stack_path)
    long_seeds = load_json(long_seed_path)
    inside_source = load_json(inside_source_path)
    synodic_path = vault_root / "99 - Templates" / "synodic_cycles.py"
    chart_index_path = vault_root / "99 - Templates" / "chart_reading_bones" / "index.json"
    synodic = load_module("f250_relationship_history_synodic", synodic_path)
    phase_func, _ = synodic.phase_grammar(str(vault_root))
    chart_index = load_json(chart_index_path)

    long_catalog = []
    long_family_index = {}
    for cycle in long_seeds["cycles"]:
        long_family_index[cycle["cycle_id"]] = cycle
        long_catalog.append(
            {
                "relationship_id": cycle["cycle_id"],
                "tier_id": cycle["tier_id"],
                "tier_order": TIER_ORDER[cycle["tier_id"]],
                "cycle_order": cycle["order"],
                "pair": cycle["pair"],
                "authority_status": "canonical_long_clock",
                "phase_contract": "eight_phase",
                "nominal_cycle_years": cycle["nominal_cycle_years"],
                "seed_family_ids": [cycle["seed_family_id"]],
                "exact_conjunction_event_ids": [row["pass_id"] for row in cycle["passes"]],
            }
        )

    inside_rows, inside_families = inside_source_index(inside_source)
    mercury_venus = mercury_venus_events(inside_source)
    tier_counts: dict[str, int] = {}
    inside_catalog = []
    for row in inside_rows:
        tier_id = INSIDE_TIER_MAP[row["tier_id"]]
        tier_counts[tier_id] = tier_counts.get(tier_id, 0) + 1
        relationship_id = row["cycle_id"]
        phaseable = row["phase_contract"] == "phaseable"
        families = inside_families.get(relationship_id, [])
        events = [item for family in families for item in family["passes"]]
        if relationship_id == "mercury-venus":
            events = mercury_venus
        inside_catalog.append(
            {
                "relationship_id": relationship_id,
                "tier_id": tier_id,
                "tier_order": TIER_ORDER[tier_id],
                "cycle_order": tier_counts[tier_id],
                "pair": pair_from_id(relationship_id),
                "authority_status": "candidate_phaseable" if phaseable else "candidate_limited_geometry",
                "phase_contract": "eight_phase" if phaseable else "limited_geometry",
                "nominal_cycle_years": row["nominal_cycle_years"],
                "seed_family_ids": [family["seed_family_id"] for family in families],
                "exact_conjunction_event_ids": [
                    item.get("pass_id") or item["event_id"] for item in events
                ],
            }
        )
    catalog = sorted(
        long_catalog + inside_catalog,
        key=lambda row: (row["tier_order"], row["cycle_order"]),
    )
    if len(catalog) != 28 or len({row["relationship_id"] for row in catalog}) != 28:
        raise ValueError("Expected exactly 28 unique relationship identities")

    canonical_chart_index = {row["chart_id"]: row for row in canonical["charts"]}
    charts = []
    for chart_meta in chart_index["charts"]:
        chart_id = chart_meta["id"]
        bone_path = vault_root / "99 - Templates" / "chart_reading_bones" / f"{chart_id}.json"
        bone = load_json(bone_path)
        canonical_chart = canonical_chart_index[chart_id]
        canonical_states = {row["cycle_id"]: row for row in canonical_chart["cycles"]}
        states = []
        for relationship in catalog:
            relationship_id = relationship["relationship_id"]
            if relationship_id in EXPECTED_LONG_IDS:
                state = long_state(
                    chart_id=chart_id,
                    chart_utc=bone["utc"],
                    canonical_state=canonical_states[relationship_id],
                    catalog=relationship,
                    family=long_family_index[relationship_id],
                )
            else:
                families = inside_families.get(relationship_id, [])
                events = [item for family in families for item in family["passes"]]
                for event in events:
                    event["event_id"] = event["pass_id"]
                if relationship_id == "mercury-venus":
                    events = mercury_venus
                state = inside_state(
                    chart_id=chart_id,
                    bone=bone,
                    catalog=relationship,
                    families=families,
                    events=events,
                    phase_func=phase_func,
                    synodic=synodic,
                )
            states.append(state)
        charts.append(
            {
                "chart_id": chart_id,
                "chart_type": chart_meta["type"],
                "date": chart_meta["date"],
                "utc": bone["utc"],
                "window_id": canonical_chart["window_id"],
                "active_direct_relationship_ids": [
                    row["relationship_id"] for row in states if row["direct_aspect"]
                ],
                "cycles": states,
            }
        )

    histories = build_histories(charts, catalog)
    clean_catalog = [
        {key: value for key, value in row.items() if not key.startswith("_")}
        for row in catalog
    ]
    payload = {
        "schema": SCHEMA_ID,
        "status": "generated",
        "deterministic": True,
        "scope": {
            "bodies": ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"],
            "sun_excluded": True,
            "moon_excluded": True,
            "relationship_count": 28,
            "canonical_long_clock_count": 10,
            "candidate_phaseable_count": 17,
            "limited_geometry_count": 1,
        },
        "authority": {
            "scope": "factual geometry and ordered chart-state history only",
            "canonical_boundary": "DR-065 exact-ten Long Clocks remains unchanged",
            "candidate_boundary": "inside relationships are candidate geometry and do not become Long Clocks",
            "exclusions": [
                "interpretive mappings",
                "plot assignments",
                "evidentiary claims",
                "forecast claims",
            ],
        },
        "source": {
            "canonical_long_stacks_path": "99 - Templates/chart_synodic_stacks.json",
            "canonical_long_stacks_sha256": sha256(long_stack_path),
            "canonical_long_seeds_path": "99 - Templates/synodic_seed_families.json",
            "canonical_long_seeds_sha256": sha256(long_seed_path),
            "inside_seed_source_path": "99 - Templates/inside_relationship_seed_families.json",
            "inside_seed_source_sha256": sha256(inside_source_path),
            "chart_registry_path": "99 - Templates/chart_reading_bones/index.json",
            "chart_registry_sha256": sha256(chart_index_path),
            "geometry_engine_path": "99 - Templates/synodic_cycles.py",
            "geometry_engine_sha256": sha256(synodic_path),
        },
        "method": {
            "phase_grammar": "DR-020 eight phases for phaseable pairs",
            "hand_direction": "slower body to faster body",
            "direct_aspects": ["conjunction", "sextile", "square", "trine", "opposition"],
            "major_orbs_deg": synodic.ORB_LIMITS,
            "mercury_venus": "directed geometry and direct aspects only; phase fields are null",
            "history_order": "exact UTC; every chart state has a unique identity",
        },
        "tiers": [
            {"tier_id": tier_id, "label": TIER_LABELS[tier_id], "order": order}
            for tier_id, order in TIER_ORDER.items()
        ],
        "cycle_catalog": clean_catalog,
        "coverage": {
            "chart_count": len(charts),
            "relationship_count": len(clean_catalog),
            "relationship_state_count": sum(len(row["cycles"]) for row in charts),
            "canonical_long_clock_state_count": 30 * 10,
            "candidate_inside_state_count": 30 * 18,
            "phaseable_inside_state_count": 30 * 17,
            "limited_geometry_state_count": 30,
            "history_count": len(histories),
            "history_delta_count": sum(len(row["deltas"]) for row in histories),
        },
        "charts": charts,
        "histories": histories,
        "parity": {
            "source_schema": canonical["schema"],
            "checked_relationship_ids": sorted(EXPECTED_LONG_IDS),
            "checked_chart_count": 30,
            "checked_state_count": 300,
            "fields": ["geometry", "direct_aspect"],
            "result": "exact",
        },
    }
    validate_payload(payload, canonical)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault-root", type=Path, default=HERE.parent)
    parser.add_argument("--inside-source", type=Path, default=DEFAULT_INSIDE_SOURCE)
    parser.add_argument("--long-seeds", type=Path, default=DEFAULT_LONG_SEEDS)
    parser.add_argument("--long-stacks", type=Path, default=DEFAULT_LONG_STACKS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true", help="Validate without writing")
    args = parser.parse_args()
    payload = build(
        vault_root=args.vault_root,
        inside_source_path=args.inside_source,
        long_seed_path=args.long_seeds,
        long_stack_path=args.long_stacks,
    )
    if not args.check:
        args.output.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print(
        "PLANETARY RELATIONSHIP HISTORY VALID: "
        f"{payload['coverage']['chart_count']} charts · "
        f"{payload['coverage']['relationship_count']} relationships · "
        f"{payload['coverage']['relationship_state_count']} states · "
        f"{payload['coverage']['history_delta_count']} ordered deltas · "
        "300 canonical Long Clock states exact-parity"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
