#!/usr/bin/env python3
"""Validate the review-only 28-pair Planetary Relationship Clock package."""

from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
VAULT = Path("Chronicle/")
REGISTRY = HERE / "planetary_relationship_registry.json"
GRAPH = HERE / "planetary_relationship_clock_graph.json"
FAMILIES = HERE / "inside_planet_conjunction_families.json"
LONG_CLOCKS = VAULT / "99 - Templates" / "chart_synodic_stacks.json"
BUILDER = HERE / "build_planetary_relationship_clocks.py"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if not spec or not spec.loader:
        raise RuntimeError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def compare_long_clock_geometry(graph: dict[str, Any]) -> None:
    governed = load_json(LONG_CLOCKS)
    governed_charts = {row["chart_id"]: row for row in governed["charts"]}
    graph_charts = {row["chart_id"]: row for row in graph["charts"]}
    require(set(governed_charts) == set(graph_charts), "Chart IDs differ from Long Clocks")

    for chart_id, old_chart in governed_charts.items():
        old_cycles = {row["cycle_id"]: row for row in old_chart["cycles"]}
        new_cycles = {
            row["cycle_id"]: row
            for row in graph_charts[chart_id]["cycles"]
            if row["relationship_status"] == "active_long_clock"
        }
        require(set(old_cycles) == set(new_cycles), f"{chart_id}: ten-clock identity drift")
        for cycle_id, old in old_cycles.items():
            new = new_cycles[cycle_id]
            old_geometry = old["geometry"]
            new_geometry = new["geometry"]
            for key in (
                "elongation_deg",
                "phase_name",
                "phase_direction",
                "relative_speed_deg_per_day",
            ):
                require(
                    old_geometry[key] == new_geometry[key],
                    f"{chart_id}/{cycle_id}: geometry mismatch at {key}",
                )
            require(
                old_geometry["nearest_chapter_id"]
                == new_geometry["nearest_major_chapter_id"],
                f"{chart_id}/{cycle_id}: nearest chapter mismatch",
            )
            old_aspect = old.get("active_aspect")
            new_aspect = new.get("direct_aspect")
            require(bool(old_aspect) == bool(new_aspect), f"{chart_id}/{cycle_id}: active-aspect mismatch")
            if old_aspect and new_aspect:
                for key in (
                    "aspect_id",
                    "chapter_id",
                    "angle_deg",
                    "orb_deg",
                    "orb_limit_deg",
                    "applying",
                    "separating",
                    "motion_state",
                    "strength",
                    "flow_kind",
                ):
                    require(old_aspect[key] == new_aspect[key], f"{chart_id}/{cycle_id}: aspect mismatch at {key}")


def validate() -> dict[str, int]:
    registry = load_json(REGISTRY)
    graph = load_json(GRAPH)
    families = load_json(FAMILIES)
    cycles = registry["cycles"]
    cycle_ids = {row["cycle_id"] for row in cycles}
    unordered_pairs = {frozenset(row["pair"]) for row in cycles}
    bodies = set(graph["scope"]["bodies"])
    expected_bodies = {"Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"}

    require(
        graph["schema"] == "freedom250.planetary-relationship-clock-graph/v0.2",
        "Relationship graph schema drift",
    )
    require(graph["status"] == "proposal_for_review", "Graph must remain review-only")
    require(graph["deterministic"] is True, "Graph must declare deterministic output")
    require(bodies == expected_bodies, "Non-luminary body set drift")
    require("Sun" not in bodies and "Moon" not in bodies, "Luminary leaked into relationship graph")
    require(len(cycles) == len(cycle_ids) == len(unordered_pairs) == 28, "Expected 28 unique non-luminary pairs")

    long_ids = {row["cycle_id"] for row in cycles if row["status"] == "active_long_clock"}
    inside_ids = {row["cycle_id"] for row in cycles if row["status"] == "candidate_relationship_clock"}
    require(len(long_ids) == 10, "DR-065 Long Clocks must remain exactly ten")
    require(len(inside_ids) == 18, "Expected the exact 18-pair inside-planet complement")
    require(not long_ids & inside_ids and long_ids | inside_ids == cycle_ids, "Relationship status partition is invalid")

    chart_rows = graph["charts"]
    require(len(chart_rows) == 30, "Expected exactly 30 governed chart bones")
    require(graph["coverage"]["relationship_state_count"] == 840, "Expected 840 relationship states")
    require(graph["coverage"]["inside_relationship_state_count"] == 540, "Expected 540 inside-pair states")
    require(graph["coverage"]["inside_phaseable_state_count"] == 510, "Expected 510 phaseable inside-pair states")
    require(graph["coverage"]["limited_geometry_state_count"] == 30, "Expected 30 limited Mercury-Venus states")
    require(graph["coverage"]["existing_long_clock_state_count"] == 300, "Expected 300 existing Long Clock states")

    mercury_venus_seen = 0
    forbidden_keys = {"seed_family_id", "seed_family_label", "display_anchor_pass_id", "long_clocks_route", "plotline_id", "verdict", "causal_claim"}
    for chart in chart_rows:
        states = chart["cycles"]
        require(len(states) == 28, f"{chart['chart_id']}: expected 28 states")
        require({row["cycle_id"] for row in states} == cycle_ids, f"{chart['chart_id']}: cycle set drift")
        require(
            chart["active_direct_cycle_ids"] == [row["cycle_id"] for row in states if row["direct_aspect"]],
            f"{chart['chart_id']}: active direct ID list drift",
        )
        require(
            chart["nameable_cycle_ids"] == [row["cycle_id"] for row in states if row["dr020_nameability"]["earned"]],
            f"{chart['chart_id']}: nameable ID list drift",
        )
        builder = load_module("f250_relationship_builder_metrics", BUILDER)
        require(
            chart["field_metrics"] == builder.relationship_field_metrics(states),
            f"{chart['chart_id']}: relationship field metrics drift",
        )
        metrics = chart["field_metrics"]
        require(
            metrics["both_count"]
            + metrics["direct_only_count"]
            + metrics["phase_only_count"]
            + metrics["silent_count"]
            == 28,
            f"{chart['chart_id']}: relationship field partition drift",
        )
        for state in states:
            require(state["reading_boundary"]["evidence_credit"] == 0, "Astrology state acquired evidence credit")
            require(not (forbidden_keys & set(state)), f"{chart['chart_id']}/{state['cycle_id']}: authority leakage")
            if state["cycle_id"] == "mercury-venus":
                mercury_venus_seen += 1
                require(state["phase_model_limited"] is True, "Mercury-Venus exception flag missing")
                require(state["phase_model"] == "limited_geocentric_elongation", "Mercury-Venus model drift")
                require(state["geometry"]["phase_contract_available"] is False, "Mercury-Venus phase contract leaked")
                require(state["geometry"]["phase_name"] is None, "Mercury-Venus received an inadmissible phase name")
                require(state["geometry"]["phase_direction"] is None, "Mercury-Venus received an inadmissible phase direction")
                require(state["dr020_nameability"]["earned"] is False, "Mercury-Venus phase prose became nameable")
            elif state["relationship_status"] == "candidate_relationship_clock":
                require(state["phase_model_limited"] is False, f"Unexpected limited phase model: {state['cycle_id']}")
                require(state["geometry"]["phase_contract_available"] is True, f"Phase contract missing: {state['cycle_id']}")
    require(mercury_venus_seen == 30, "Mercury-Venus exception must appear once per chart")

    field_control = graph["corpus_field_control"]
    require(
        field_control["direct_exceeds_nameable_phase"]
        == {"chart_count": 1, "chart_ids": ["lun-2026-12-09-ne"]},
        "December 9 direct/nameable corpus control drift",
    )
    require(
        field_control["maximum_direct_only"]
        == {"count": 9, "chart_ids": ["lun-2026-12-09-ne"]},
        "Maximum direct-only corpus control drift",
    )
    count_twins = field_control["consecutive_equal_count_identity_turnovers"]
    require(
        [(row["from_chart_id"], row["to_chart_id"]) for row in count_twins]
        == [
            ("lun-2026-03-19-ne", "ingress-2026-aries"),
            ("lun-2026-09-11-ne", "ingress-2026-libra"),
        ],
        "Equal-count identity-turnover roster drift",
    )
    require(
        not count_twins[0]["direct_cycle_ids_left"]
        and not count_twins[0]["direct_cycle_ids_entered"],
        "Aries ingress should preserve the direct relationship cast",
    )
    require(
        count_twins[0]["phase_nameability_ids_left"]
        == ["venus-saturn", "venus-uranus", "venus-neptune", "venus-pluto"],
        "Aries ingress Venus-led phase handoff drift",
    )
    require(
        count_twins[0]["phase_nameability_ids_entered"]
        == ["mars-saturn", "mars-uranus", "mars-neptune", "mars-pluto"],
        "Aries ingress Mars-led phase handoff drift",
    )
    require(
        len(count_twins[1]["direct_cycle_ids_left"])
        == len(count_twins[1]["direct_cycle_ids_entered"])
        == len(count_twins[1]["phase_nameability_ids_left"])
        == len(count_twins[1]["phase_nameability_ids_entered"])
        == 4,
        "Libra ingress equal-count cast turnover drift",
    )
    expected_handoff_rows = [
        {
            "chart_id": "lun-2026-12-09-ne",
            "date": "2026-12-09",
            "direct_count": 16,
            "nameable_phase_count": 14,
            "both_count": 7,
            "direct_only_count": 9,
            "phase_only_count": 7,
            "silent_count": 5,
        },
        {
            "chart_id": "ingress-2026-capricorn",
            "date": "2026-12-21",
            "direct_count": 8,
            "nameable_phase_count": 25,
            "both_count": 8,
            "direct_only_count": 0,
            "phase_only_count": 17,
            "silent_count": 3,
        },
        {
            "chart_id": "lun-2026-12-24-fu",
            "date": "2026-12-24",
            "direct_count": 9,
            "nameable_phase_count": 25,
            "both_count": 9,
            "direct_only_count": 0,
            "phase_only_count": 16,
            "silent_count": 3,
        },
    ]
    require(
        field_control["late_year_handoff"]["rows"] == expected_handoff_rows,
        "December relationship-field handoff drift",
    )
    handoff_delta = field_control["late_year_handoff"]["december_09_to_capricorn_ingress"]
    require(handoff_delta["direct_count_delta"] == -8, "December direct-count delta drift")
    require(handoff_delta["nameable_phase_count_delta"] == 11, "December phase-nameability delta drift")
    require(len(handoff_delta["direct_cycle_ids_left"]) == 9, "Expected nine direct relationships to leave")
    require(len(handoff_delta["direct_cycle_ids_entered"]) == 1, "Expected one direct relationship to enter")
    require(len(handoff_delta["phase_nameability_ids_gained"]) == 11, "Expected eleven phase admissions")
    require(not handoff_delta["phase_nameability_ids_lost"], "Unexpected phase admission loss")

    family_rows = families["families"]
    family_ids = [row[1] for row in family_rows]
    pass_rows = [event for family in family_rows for event in family[4]]
    pass_ids = [row[0] for row in pass_rows]
    family_cycle_ids = {row[0] for row in family_rows}
    phaseable_inside_ids = inside_ids - {"mercury-venus"}
    require(families["status"] == "proposal_only_not_vault_authority", "Family ledger authority drift")
    require(families["coverage"]["phaseable_pair_count"] == 17, "Family ledger phaseable-pair count drift")
    require(families["coverage"]["phaseable_seed_family_count"] == 55, "Family ledger family count drift")
    require(families["coverage"]["phaseable_exact_pass_count"] == 73, "Family ledger exact-pass count drift")
    require(len(family_rows) == len(set(family_ids)) == 55, "Expected 55 unique conjunction families")
    require(len(pass_rows) == len(set(pass_ids)) == 73, "Expected 73 unique exact conjunction passes")
    require(family_cycle_ids == phaseable_inside_ids, "Family ledger does not cover the exact 17 phaseable inside pairs")
    require(families["mercury_venus_exception"]["status"] == "unresolved_not_admitted", "Mercury-Venus exception became admitted")
    require(len(families["mercury_venus_exception"]["crossings"]) == 6, "Expected six unresolved Mercury-Venus crossings")

    compare_long_clock_geometry(graph)

    builder = load_module("f250_relationship_builder_validation", BUILDER)
    rebuilt = builder.build(VAULT, REGISTRY)
    require(rebuilt == graph, "Checked-in graph is not a byte-meaningful deterministic rebuild")

    phases = load_module("f250_phases_validation", VAULT / "99 - Templates" / "phases.py")
    boundary_expectations = {
        0.0: ("New", "waxing"),
        45.0: ("Crescent", "waxing"),
        90.0: ("First Quarter", "waxing"),
        135.0: ("Gibbous", "waxing"),
        180.0: ("Full", "waning"),
        225.0: ("Disseminating", "waning"),
        270.0: ("Last Quarter", "waning"),
        315.0: ("Balsamic", "waning"),
    }
    for angle, expected in boundary_expectations.items():
        require(phases.phase_of(angle) == expected, f"Phase boundary drift at {angle} degrees")

    return {
        "charts": len(chart_rows),
        "relationships": len(cycles),
        "states": sum(len(row["cycles"]) for row in chart_rows),
        "long_clock_parity_states": len(chart_rows) * len(long_ids),
        "inside_states": len(chart_rows) * len(inside_ids),
        "seed_families": len(family_rows),
        "exact_seed_passes": len(pass_rows),
    }


def main() -> int:
    counts = validate()
    print(
        "RELATIONSHIP CLOCKS VALID: "
        f"{counts['charts']} charts · {counts['relationships']} relationships · "
        f"{counts['states']} states · {counts['long_clock_parity_states']} Long Clock parity states · "
        f"{counts['inside_states']} inside-pair states · {counts['seed_families']} seed families · "
        f"{counts['exact_seed_passes']} exact seed passes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
