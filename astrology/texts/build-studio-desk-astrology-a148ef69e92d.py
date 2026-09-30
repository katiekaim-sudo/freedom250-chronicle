#!/usr/bin/env python3
"""Build the compact, plot-free astrology layer for Studio Desk.

This projection reads governed astrology owners. It does not calculate a second
sky, assign stories, create evidence, or write interpretation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path

from atomic_io import atomic_write_text

HERE = Path(__file__).resolve().parent
VAULT = HERE.parent
OUTPUT = HERE / "studio_desk_astrology.json"
MUNDANE = HERE / "mundane_history.json"
STACKS = HERE / "chart_synodic_stacks.json"
RELATIONSHIPS = HERE / "planetary_relationship_history.json"
READINGS = VAULT / "03 - Astrology" / "chart_reading_registry.json"
WATCHES = VAULT / "03 - Astrology" / "chart_transition_watches.json"
BRAIDS = VAULT / "03 - Astrology" / "astrology_spine_plot_rooms.json"
ASTRO_MAP_BUILDER = HERE / "build_astro_map.py"
MOON_MOTION = HERE / "moon_lineages.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def instant(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def map_chart_id(chart_id: str) -> str:
    """Return the explicit existing Astro Map compatibility ID.

    Studio emits this ID so the UI never guesses across the two historical ID
    contracts. Wave 2.5 will replace compatibility mapping with a shared
    machine-readable geometry catalog.
    """
    if chart_id.startswith("ingress-"):
        return chart_id.removeprefix("ingress-")
    match = re.fullmatch(r"(lun-\d{4}-\d{2}-\d{2})-(?:ne|fu)(?:-.+)?", chart_id)
    if match:
        return match.group(1)
    raise ValueError(f"no explicit Astro Map compatibility ID for {chart_id}")


def compact_chart(chart: dict) -> dict:
    wanted = {"Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter",
              "Saturn", "Uranus", "Neptune", "Pluto"}
    return {
        "chart_id": chart["id"],
        "map_chart_id": map_chart_id(chart["id"]),
        "label": chart["label"],
        "chart_type": chart["chart_type"],
        "exact_utc": chart["utc"],
        "exact_local": chart["local"],
        "asc_sign": chart.get("asc_sign"),
        "reading_source": chart.get("reading_source"),
        "verification": chart.get("verification", {}),
        "actors": [
            {
                "body": point["name"],
                "sign": point["sign"],
                "dms": point["dms"],
                "speed_deg_per_day": point["speed"],
                "retrograde": point["retro"],
            }
            for point in chart.get("points", [])
            if point.get("name") in wanted
        ],
    }


def build_payload() -> dict:
    mundane = load(MUNDANE)
    stacks = load(STACKS)
    relationships = load(RELATIONSHIPS)
    readings = load(READINGS)
    watches = load(WATCHES)
    braids = load(BRAIDS)
    moon_motion = load(MOON_MOTION)
    if moon_motion.get("schema") != "f250.moon-motion/v1":
        raise ValueError("Studio astrology requires the governed Moon-motion projection")

    as_of = instant(stacks["as_of"])
    by_id = {row["id"]: row for row in mundane["charts"]}
    checkpoints = [
        row for row in relationships["charts"]
        if instant(row["utc"]) <= as_of
        and (by_id.get(row.get("chart_id"), {}).get("chart_type") == "lunation")
        and "-ne" in (row.get("chart_id") or "")
    ]
    if not checkpoints:
        raise ValueError("relationship history has no New Moon chapter at or before Long Clocks as_of")
    checkpoint = max(checkpoints, key=lambda row: instant(row["utc"]))
    if len(checkpoint.get("cycles", [])) != 28:
        raise ValueError(f"expected 28 relationship states, found {len(checkpoint.get('cycles', []))}")

    chapter = by_id.get(checkpoint["chart_id"])
    if not chapter or chapter.get("chart_type") != "lunation" or "-ne" not in chapter["id"]:
        raise ValueError(f"checkpoint is not a New Moon chapter: {checkpoint['chart_id']}")
    chapter_start = instant(chapter["utc"])
    next_new = min(
        (
            row for row in mundane["charts"]
            if row.get("chart_type") == "lunation"
            and "-ne" in row.get("id", "")
            and instant(row["utc"]) > chapter_start
        ),
        key=lambda row: instant(row["utc"]),
    )
    chapter_end = instant(next_new["utc"])

    governing = by_id.get(checkpoint["window_id"])
    if not governing or governing.get("chart_type") != "ingress":
        raise ValueError(f"missing governing ingress {checkpoint['window_id']}")
    later_ingresses = sorted(
        (
            row for row in mundane["charts"]
            if row.get("chart_type") == "ingress"
            and chapter_start < instant(row["utc"]) < chapter_end
        ),
        key=lambda row: instant(row["utc"]),
    )
    ingress_chain = [governing] + later_ingresses
    segments = []
    for index, ingress in enumerate(ingress_chain):
        start = chapter["utc"] if index == 0 else ingress["utc"]
        end = ingress_chain[index + 1]["utc"] if index + 1 < len(ingress_chain) else next_new["utc"]
        segments.append({
            "ingress_id": ingress["id"],
            "label": ingress["label"],
            "from_utc": start,
            "until_utc": end,
            "handoff_local": ingress["local"] if index else None,
        })

    phase_strikes = [
        compact_chart(row)
        for row in sorted(mundane["charts"], key=lambda item: instant(item["utc"]))
        if row.get("chart_type") == "lunation"
        and "-fu" in row.get("id", "")
        and chapter_start < instant(row["utc"]) < chapter_end
    ]

    reading_row = next(row for row in readings["readings"] if row["id"] == chapter["id"])
    reading_path = VAULT / reading_row["source"]
    live_hash = sha256(reading_path)
    baseline = component = None
    for candidate in readings["comparison_contract"]["baselines"]:
        match = next((item for item in candidate["components"] if item["reading_id"] == chapter["id"]), None)
        if match:
            baseline, component = candidate, match
            break
    if not baseline or not component:
        raise ValueError(f"no frozen baseline for {chapter['id']}")
    transition_watch = next(
        (row for row in watches["watches"] if row["reading_id"] == chapter["id"]),
        None,
    )
    if not transition_watch:
        raise ValueError(f"no State Transition Watch for {chapter['id']}")

    states = []
    for row in checkpoint["cycles"]:
        direct = row.get("direct_aspect")
        geometry = row["geometry"]
        states.append({
            "state_id": row["state_id"],
            "relationship_id": row["relationship_id"],
            "tier_id": row["tier_id"],
            "pair": row["pair"],
            "authority_status": row["authority_status"],
            "phase_name": geometry.get("phase_name"),
            "phase_direction": geometry.get("phase_direction"),
            "phase_contract_available": geometry.get("phase_contract_available"),
            "direct_aspect": None if not direct else {
                "aspect_id": direct["aspect_id"],
                "orb_deg": direct["orb_deg"],
                "motion_state": direct["motion_state"],
                "strength": direct["strength"],
            },
            "seed_family_id": row.get("seed_context", {}).get("active_seed_family_id"),
        })

    storyline_braids = []
    for row in braids.get("storylines", []):
        storyline_braids.append({
            "storyline_id": row.get("storyline_id") or row.get("id"),
            "title": row.get("title"),
            "lifecycle": row.get("lifecycle"),
            "factual_cutoff": row.get("factual_frame", {}).get("cutoff"),
            "review": row.get("review"),
            "checkpoint_refs": row.get("checkpoint_refs", []),
            "strand_count": len(row.get("strands", [])),
        })

    motion_events = {row["phase_event_id"]: row for row in moon_motion["phase_events"]}
    current_lineage = next(
        (row for row in moon_motion["lineages"] if row["seed_chart_id"] == chapter["id"]),
        None,
    )
    if not current_lineage:
        raise ValueError(f"no governed Pessin lineage for current lunar chapter {chapter['id']}")

    def expand_lineage(lineage: dict) -> dict:
        return {
            "lineage_id": lineage["lineage_id"],
            "seed_chart_id": lineage["seed_chart_id"],
            "degree_band": lineage["degree_band"],
            "interpretation_status": lineage["interpretation_status"],
            "story_verdict": lineage["story_verdict"],
            "members": [{**member, "phase_event": motion_events[member["phase_event_id"]]}
                        for member in lineage["members"]],
        }

    chapter_phase_events = sorted(
        (
            row for row in moon_motion["phase_events"]
            if chapter_start < instant(row["exact_utc"]) < chapter_end
        ),
        key=lambda row: instant(row["exact_utc"]),
    )
    strike_motion = []
    for strike in chapter_phase_events:
        pessin = [expand_lineage(row) for row in moon_motion["lineages"]
                  if any(member["phase_event_id"] == strike["phase_event_id"] for member in row["members"])]
        echoes = [row for row in moon_motion["echo_candidates"]
                  if row["seed_phase_event_id"] == strike["phase_event_id"]
                  or row["return_phase_event_id"] == strike["phase_event_id"]]
        strike_motion.append({
            "phase_event_id": strike["phase_event_id"],
            "chart_id": strike["chart_id"],
            "phase": strike["phase"],
            "exact_utc": strike["exact_utc"],
            "governing_ingress_id": strike["governing_ingress_id"],
            "pessin_lineages": pessin,
            "half_year_echo_candidates": echoes,
            "relation_count": len(pessin) + len(echoes),
            "story_assignment": None,
            "continuity_verdict": None,
        })
    current_echoes = [row for row in moon_motion["echo_candidates"] if row["seed_chart_id"] == chapter["id"]]

    payload = {
        "schema": "f250.studio-desk.astrology/v1",
        "status": "generated_projection",
        "projection_generated_from": stacks["generated_at"],
        "cutoff": {
            "as_of_utc": stacks["as_of"],
            "basis": stacks["as_of_basis"],
            "display_timezone": "America/New_York",
            "relationship_checkpoint_utc": checkpoint["utc"],
            "relationship_checkpoint_rule": "latest registered New Moon chapter at or before Long Clocks as_of; not continuous sky now",
        },
        "governing_ingress": compact_chart(governing),
        "lunar_chapter": {
            **compact_chart(chapter),
            "ends_utc": next_new["utc"],
            "ends_local": next_new["local"],
            "ingress_segments": segments,
        },
        "phase_strikes": phase_strikes,
        "whole_chart_reading": {
            "reading_id": chapter["id"],
            "source": reading_row["source"],
            "live_sha256": live_hash,
            "baseline_id": baseline["baseline_id"],
            "baseline_sha256": component["sha256"],
            "drift": "unchanged" if live_hash == component["sha256"] else "changed",
            "transition_watch_id": transition_watch["watch_id"],
            "authority_question": transition_watch["authority_question"],
            "candidate_transition": transition_watch["transition"],
            "evidence_lanes": transition_watch["evidence_test"]["lanes"],
        },
        "relationship_field": {
            "checkpoint_chart_id": checkpoint["chart_id"],
            "checkpoint_utc": checkpoint["utc"],
            "window_id": checkpoint["window_id"],
            "relationship_count": len(states),
            "active_direct_count": len(checkpoint["active_direct_relationship_ids"]),
            "active_direct_relationship_ids": checkpoint["active_direct_relationship_ids"],
            "states": states,
        },
        "lunar_motion": {
            "method": {
                "pessin_lineage_rule": moon_motion["method"]["lineage_rule"],
                "pessin_target_days": moon_motion["method"]["target_days"],
                "half_year_echo": moon_motion["method"]["half_year_echo"],
                "source_tension": moon_motion["method"]["source_tension"],
            },
            "current_chapter_lineage": expand_lineage(current_lineage),
            "current_chapter_half_year_echo_candidates": current_echoes,
            "current_chapter_half_year_result": "candidate_geometry_present" if current_echoes else "no_candidate_under_current_rule",
            "phase_strike_relations": strike_motion,
            "multiplicity_rule": "One phase event may carry a chapter role, its own Pessin-lineage role, an approximate half-year candidate, a governing ingress, and several authored manifestation candidates at once. None elects the one real story.",
            "boundaries": moon_motion["boundaries"],
            "route": {"tab": "obs-mf", "date": chapter["date"]},
        },
        "storyline_braids": storyline_braids,
        "deferred": {
            "storyline_currentness": "five authored pilots retain their own factual cutoffs and open review states",
            "locality_context": "Wave 2.5 will harden machine-readable Astro Map geometry and sourced place identity; current bridge is route-only",
        },
        "routes": {
            "reading": {"tab": "obs-cr", "chart_id": chapter["id"]},
            "long_clocks": {"tab": "obs-dc", "chart_id": chapter["id"]},
            "sky_watchlist": {"tab": "obs-as"},
            "moon_families": {"tab": "obs-mf", "date": chapter["date"]},
            "astro_map": {"tab": "obs-am", "type": "astromap", "status": "route_only_until_wave_2_5"},
        },
        "source_receipts": {
            str(path.relative_to(VAULT)): sha256(path)
            for path in (MUNDANE, STACKS, RELATIONSHIPS, READINGS, WATCHES, BRAIDS, ASTRO_MAP_BUILDER, MOON_MOTION)
        },
        "authority_notice": "Geometry, chronology, and geographic proximity do not own stories. Astrology and locality add no factual evidence, ranking credit, causal claim, location prediction, or automatic review.",
    }
    forbidden = {"evidence_score", "confidence_score", "causation", "story_rank"}
    found = set()

    def walk(value):
        if isinstance(value, dict):
            found.update(forbidden.intersection(value))
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(payload)
    if found:
        raise ValueError(f"forbidden Studio astrology fields: {sorted(found)}")
    return payload


def render(payload: dict) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args(argv)
    content = render(build_payload())
    if args.check:
        if not args.output.exists() or args.output.read_text(encoding="utf-8") != content:
            print("STUDIO ASTROLOGY CHECK: STALE")
            return 1
        print("STUDIO ASTROLOGY CHECK: CLEAN")
        return 0
    atomic_write_text(args.output, content)
    print(f"STUDIO ASTROLOGY BUILT: {args.output.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
