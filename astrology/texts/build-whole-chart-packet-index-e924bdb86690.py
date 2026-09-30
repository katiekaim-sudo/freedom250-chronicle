#!/usr/bin/env python3
"""Build the reference-only whole-chart packet index for the Astrology Hub.

This index is connective tissue, not a new chart owner. It keeps the identity
of each registered ingress or syzygy together and points outward to the exact
calculation, authored reading, governing period, lineage, relationship stack,
physical geometry and cross-chart studies. It never copies placements, houses,
aspects or judgments from those owners.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = HERE / "whole_chart_packet_index.json"
CUTOFF = "2026-09-25"
CUTOFF_INSTANT = datetime.fromisoformat("2026-09-26T03:59:59+00:00")

SOURCES = {
    "history": "99 - Templates/mundane_history.json",
    "bones_index": "99 - Templates/chart_reading_bones/index.json",
    "reading_registry": "03 - Astrology/chart_reading_registry.json",
    "synodic_stacks": "99 - Templates/chart_synodic_stacks.json",
    "moon_families": "99 - Templates/full_moon_family_triage_2026.json",
    "eclipse_genealogies": "99 - Templates/eclipse_genealogies.json",
    "eclipse_handoffs": "99 - Templates/eclipse_season_handoffs_2026.json",
    "ingress_seams": "99 - Templates/ingress_lunation_seams_2026.json",
    "long_clock_corridors": "99 - Templates/long_clock_seed_corridors_2026.json",
    "radix_inheritance": "99 - Templates/conjunction_radix_inheritance_2026.json",
    "sidereal_relays": "99 - Templates/sidereal_stage_relays_2026.json",
    "inner_motion": "99 - Templates/inner_planet_solar_motion_2026.json",
    "outer_geometry": "99 - Templates/outer_planet_physical_geometry_2026.json",
    "pattern_atlas": "99 - Templates/pattern_atlas_2026.json",
}


def load_json(relative_path: str) -> dict[str, Any]:
    return json.loads((ROOT / relative_path).read_text(encoding="utf-8"))


def sha256(relative_path: str) -> str:
    return hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()


def stacks_charts_sha256() -> str:
    """Hash only the stacks' chart rows: the file re-stamps generated_at, as_of and its daily
    snapshot every nightly, but the chart rows this index cites do not change with as_of."""
    rows = load_json(SOURCES["synodic_stacks"])["charts"]
    return hashlib.sha256(json.dumps(
        rows, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")).hexdigest()


def receipt(relative_path: str) -> dict[str, Any]:
    path = ROOT / relative_path
    if not path.is_file():
        raise FileNotFoundError(relative_path)
    if relative_path == SOURCES["synodic_stacks"]:
        return {"path": relative_path, "selector": "charts", "charts_sha256": stacks_charts_sha256()}
    return {"path": relative_path, "bytes": path.stat().st_size, "sha256": sha256(relative_path)}


def dataset_ref(source_key: str, selector: str, *, state: str = "available") -> dict[str, str]:
    return {"state": state, "dataset": SOURCES[source_key], "selector": selector}


def unavailable_ref(source_key: str, reason: str) -> dict[str, str]:
    return {"state": "not_in_control_population", "dataset": SOURCES[source_key], "reason": reason}


def rows_by_id(rows: list[dict[str, Any]], key: str) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for row in rows:
        value = str(row.get(key) or "")
        if not value or value in result:
            raise ValueError(f"duplicate or blank {key}: {value!r}")
        result[value] = row
    return result


def find_role_refs(payload: dict[str, Any], chart_id: str, *, list_key: str, label_key: str) -> list[dict[str, str]]:
    refs: list[dict[str, str]] = []
    for index, record in enumerate(payload.get(list_key, [])):
        label = str(record.get(label_key) or index)
        for role, value in record.items():
            if isinstance(value, dict) and value.get("chart_id") == chart_id:
                refs.append({"record": label, "role": role, "selector": f"{list_key}[{index}].{role}"})
    return refs


def display_kind(bone: dict[str, Any]) -> str:
    if bone["type"] == "ingress":
        return f"{bone['sign']} ingress"
    eclipse = str(bone.get("eclipse") or "").lower()
    if "solar" in eclipse:
        return "Solar eclipse"
    if "lunar" in eclipse:
        return "Lunar eclipse"
    return "New Moon" if bone.get("kind") == "new" else "Full Moon"


def packet_group(bone: dict[str, Any]) -> str:
    if bone["type"] == "ingress":
        return "ingress_governors"
    return "new_moon_seeds" if bone.get("kind") == "new" else "full_moon_culminations"


def applicable_patterns(
    chart_id: str,
    bone: dict[str, Any],
    pattern_records: list[dict[str, Any]],
) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    for pattern in pattern_records:
        pattern_id = pattern["pattern_id"]
        anchors = set(pattern.get("anchor_chart_refs") or [])
        reason = None
        if chart_id in anchors:
            reason = "explicit_anchor"
        elif pattern_id == "thirteen_moon_family_harvests" and bone.get("kind") == "full":
            reason = "member_of_complete_2026_full_moon_population"
        elif pattern_id == "distributed_field_recursive_command":
            reason = "member_of_complete_registered_packet_population"
        if reason:
            result.append({"pattern_id": pattern_id, "applicability": reason})
    return result


def build_payload() -> dict[str, Any]:
    data = {key: load_json(path) for key, path in SOURCES.items()}
    bones = data["bones_index"]["charts"]
    bone_by_id = rows_by_id(bones, "id")
    history_by_id = rows_by_id(data["history"]["charts"], "id")
    pass1 = [row for row in data["reading_registry"]["readings"] if row.get("kind") == "pass1"]
    reading_by_id = rows_by_id(pass1, "id")
    stack_by_id = rows_by_id(data["synodic_stacks"]["charts"], "chart_id")
    inner_ids = {row["chart_id"] for row in data["inner_motion"]["charts"]}
    outer_ids = {row["chart_id"] for row in data["outer_geometry"]["charts"]}
    long_clock_ids = {row["chart_id"] for row in data["long_clock_corridors"]["charts"]}
    radix_ids = {row["chart_id"] for row in data["radix_inheritance"]["charts"]}
    sidereal_ids = {row["chart_id"] for row in data["sidereal_relays"]["chart_fingerprints"]}
    eclipse_ids = {row["event_id"] for row in data["eclipse_genealogies"]["events"]}
    family_by_full_id = {
        row["full"]["chart_id"]: row
        for row in data["moon_families"]["families"]
    }
    patterns = data["pattern_atlas"]["pattern_records"]

    expected = set(bone_by_id)
    for name, population in (
        ("history", set(history_by_id)),
        ("pass-1 reading", set(reading_by_id)),
        ("synodic stack", set(stack_by_id)),
    ):
        if expected - population:
            raise ValueError(f"{name} coverage missing {sorted(expected - population)}")
    if len(expected) != 30:
        raise ValueError(f"expected 30 registered packets, found {len(expected)}")

    packets: list[dict[str, Any]] = []
    for bone in bones:
        chart_id = bone["id"]
        chart = history_by_id[chart_id]
        reading = reading_by_id[chart_id]
        bone_path = f"99 - Templates/chart_reading_bones/{chart_id}.json"
        if not (ROOT / bone_path).is_file():
            raise FileNotFoundError(bone_path)
        if chart.get("reading_source") != reading.get("source"):
            raise ValueError(f"reading route drift for {chart_id}")
        if stack_by_id[chart_id].get("utc") != chart.get("utc"):
            raise ValueError(f"synodic clock drift for {chart_id}")

        ingress_refs = find_role_refs(
            data["ingress_seams"], chart_id, list_key="seams", label_key="season"
        )
        handoff_refs = find_role_refs(
            data["eclipse_handoffs"], chart_id, list_key="seasons", label_key="season"
        )
        lineage: list[dict[str, str]] = []
        if chart_id in family_by_full_id:
            family = family_by_full_id[chart_id]
            lineage.append({
                "lineage_type": "moon_family",
                "lineage_id": family["lineage_id"],
                "dataset": SOURCES["moon_families"],
                "selector": f"families[lineage_id={family['lineage_id']}]",
            })
        if chart_id in eclipse_ids:
            lineage.append({
                "lineage_type": "eclipse_genealogy",
                "lineage_id": chart_id,
                "dataset": SOURCES["eclipse_genealogies"],
                "selector": f"events[event_id={chart_id}]",
            })
        for ref in handoff_refs:
            lineage.append({
                "lineage_type": "eclipse_season_handoff",
                "lineage_id": ref["record"],
                "role": ref["role"],
                "dataset": SOURCES["eclipse_handoffs"],
                "selector": ref["selector"],
            })

        governor_id = chart.get("governing_ingress_id")
        if bone["type"] == "ingress":
            governor = {
                "state": "this_packet_establishes_governance",
                "chart_id": chart_id,
                "relation": "governing_ingress_origin",
            }
        else:
            if not governor_id or governor_id not in history_by_id:
                raise ValueError(f"missing governing ingress for {chart_id}")
            governor = {
                "state": "governed_lunation",
                "chart_id": governor_id,
                "relation": "governing_ingress",
                "chart_ref": f"{SOURCES['history']}#charts[id={governor_id}]",
                "packet_state": "indexed" if governor_id in expected else "external_chart_reference",
            }

        direct_2026_reason = "The 2025 Capricorn ingress is the inherited annual governor but sits outside the 2026-only control population."
        analyses = {
            "synodic_stack_ref": dataset_ref("synodic_stacks", f"charts[chart_id={chart_id}]"),
            "long_clock_seed_corridor_ref": dataset_ref("long_clock_corridors", f"charts[chart_id={chart_id}]") if chart_id in long_clock_ids else unavailable_ref("long_clock_corridors", direct_2026_reason),
            "conjunction_radix_inheritance_ref": dataset_ref("radix_inheritance", f"charts[chart_id={chart_id}]") if chart_id in radix_ids else unavailable_ref("radix_inheritance", direct_2026_reason),
            "sidereal_stage_ref": dataset_ref("sidereal_relays", f"chart_fingerprints[chart_id={chart_id}]") if chart_id in sidereal_ids else unavailable_ref("sidereal_relays", direct_2026_reason),
            "inner_planet_motion_ref": dataset_ref("inner_motion", f"charts[chart_id={chart_id}]") if chart_id in inner_ids else unavailable_ref("inner_motion", direct_2026_reason),
            "outer_planet_geometry_ref": dataset_ref("outer_geometry", f"charts[chart_id={chart_id}]") if chart_id in outer_ids else unavailable_ref("outer_geometry", direct_2026_reason),
        }

        exact_utc = chart["utc"]
        packets.append({
            "chart_id": chart_id,
            "chart_type": bone["type"],
            "packet_group": packet_group(bone),
            "display_kind": display_kind(bone),
            "label": chart["label"],
            "knowledge_state_at_cutoff": "occurred" if datetime.fromisoformat(exact_utc) <= CUTOFF_INSTANT else "prospective",
            "chart_ref": f"{SOURCES['history']}#charts[id={chart_id}]",
            "snapshot_ref": dataset_ref("history", f"charts[id={chart_id}]"),
            "bones_ref": {"state": "available", "path": bone_path},
            "exact_clock": {"utc": exact_utc, "local": chart["local"], "source_ref": f"{SOURCES['history']}#charts[id={chart_id}]"},
            "locality_ref": {"label": data["history"]["location"]["label"], "source_ref": f"{SOURCES['history']}#location"},
            "house_frame_ref": {
                "interpretive": f"{bone_path}#pos.*.house",
                "comparison": f"{SOURCES['history']}#charts[id={chart_id}].placidus_cusps",
                "boundary": "Whole Sign is the interpretive frame; Placidus remains a separately displayed comparison frame.",
            },
            "positions_and_angles_ref": {"path": bone_path, "selectors": ["pos", "asc", "mc"], "computed_snapshot": f"{SOURCES['history']}#charts[id={chart_id}]"},
            "aspect_web_ref": {"path": bone_path, "selector": "aspects"},
            "dispositor_root_ref": {"path": bone_path, "selectors": ["chains", "finals", "loops", "root_members"]},
            "distribution_ref": {"path": bone_path, "selectors": ["shape", "occupied_deg", "empty_deg", "empty_from", "empty_to"]},
            "declination_ref": {"path": bone_path, "selectors": ["pos.*.declination", "parallels"]},
            "reading_ref": {"reading_id": chart_id, "kind": "pass1", "source": reading["source"], "selection_message": {"action": "selectReading", "chart_id": chart_id}},
            "governing_ingress_ref": governor,
            "lunation_or_eclipse_lineage_refs": lineage,
            "ingress_lunation_seam_refs": [
                {"season": ref["record"], "role": ref["role"], "dataset": SOURCES["ingress_seams"], "selector": ref["selector"]}
                for ref in ingress_refs
            ],
            "analysis_refs": analyses,
            "applicable_pattern_refs": applicable_patterns(chart_id, bone, patterns),
        })

    group_order = ["ingress_governors", "new_moon_seeds", "full_moon_culminations"]
    group_labels = {
        "ingress_governors": "Ingress governors",
        "new_moon_seeds": "New Moons and solar eclipses",
        "full_moon_culminations": "Full Moons and lunar eclipses",
    }
    groups = [
        {
            "group_id": group,
            "label": group_labels[group],
            "packet_count": sum(row["packet_group"] == group for row in packets),
        }
        for group in group_order
    ]

    return {
        "schema": "freedom250.whole-chart-packet-index/v1",
        "status": "reference_only_orientation_index",
        "developed_through": CUTOFF,
        "purpose": "Keep each registered chart whole while routing outward to canonical calculations, readings, governing periods, lineages, physical motion and cross-chart studies.",
        "reference_contract": {
            "owns": ["packet identity", "exact clock", "route availability", "applicability"],
            "does_not_own": ["planetary positions", "houses", "aspect lists", "semantic judgments", "political facts", "forecast calls"],
            "copy_rule": "Identity fields may be repeated for reliable routing. Chart payloads and judgments remain with their canonical owners.",
        },
        "counts": {
            "packet_count": len(packets),
            "ingress_packet_count": sum(row["chart_type"] == "ingress" for row in packets),
            "lunation_packet_count": sum(row["chart_type"] == "lunation" for row in packets),
            "moon_family_link_count": sum(any(ref["lineage_type"] == "moon_family" for ref in row["lunation_or_eclipse_lineage_refs"]) for row in packets),
            "eclipse_genealogy_link_count": sum(any(ref["lineage_type"] == "eclipse_genealogy" for ref in row["lunation_or_eclipse_lineage_refs"]) for row in packets),
        },
        "groups": groups,
        "packets": packets,
        "authority_boundary": {
            "locked_pass_1_readings_changed": False,
            "chart_payload_copied": False,
            "pattern_applicability_is_evidence": False,
            "political_fact_created": False,
            "causal_credit": "zero",
            "forecast_ledger_credit": "zero",
        },
        "source_receipts": [receipt(path) for path in sorted(set(SOURCES.values()))],
    }


def main() -> None:
    payload = build_payload()
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    counts = payload["counts"]
    print(
        f"Wrote {OUT.name}: {counts['packet_count']} packets, "
        f"{counts['moon_family_link_count']} Moon-family links, "
        f"{counts['eclipse_genealogy_link_count']} eclipse genealogies."
    )


if __name__ == "__main__":
    main()
