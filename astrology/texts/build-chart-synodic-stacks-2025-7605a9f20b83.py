#!/usr/bin/env python3
"""Build the Long Clocks chart stacks for the 2025 retrospective shelf (DR-084).

    python3 build_chart_synodic_stacks_2025.py

Same engine and schema as build_chart_synodic_stacks.py, pointed at
chart_reading_bones_2025/.  The snapshot instant is fixed at the end of the shelf
(the December 21, 2025 solstice), so re-runs are stable.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import synodic_cycles as syn

HERE = Path(__file__).resolve().parent
BONES = HERE / "chart_reading_bones_2025"
OUTPUT = HERE / "chart_synodic_stacks_2025.json"
AS_OF = "2025-12-21T15:03:00+00:00"


def _chart_registry(vault_root: Path):
    index = json.loads((BONES / "index.json").read_text(encoding="utf-8"))
    return index, {chart["id"]: chart for chart in index.get("charts", [])}


def _bone(vault_root: Path, chart_id: str):
    path = BONES / f"{chart_id}.json"
    if not path.exists():
        raise KeyError(f"Registered chart has no bones file: {chart_id}")
    return json.loads(path.read_text(encoding="utf-8"))


def _rel(path, root) -> str:
    try:
        return str(Path(path).relative_to(root))
    except (ValueError, OSError, TypeError):
        return str(path)


def main() -> int:
    started = time.perf_counter()
    syn._chart_registry = _chart_registry
    syn._bone = _bone
    vault_root = syn.DEFAULT_VAULT_ROOT
    registry = syn.load_seed_registry(HERE / "synodic_seed_families.json")
    phase_func, phase_source = syn.phase_grammar(str(vault_root))
    index, chart_index = _chart_registry(vault_root)
    moments = [syn.parse_moment(_bone(vault_root, cid)["utc"]) for cid in chart_index]
    catalog = syn.build_event_catalog(registry, min(moments), max(moments), phase_func=phase_func)
    all_ids = set(chart_index)
    charts = [
        syn.build_registered_chart_stack(meta, vault_root=vault_root, registry=registry,
                                         event_catalog=catalog, phase_func=phase_func,
                                         all_chart_ids=all_ids)
        for meta in index["charts"]
    ]
    payload = {
        "schema": "freedom250.long-clocks.chart-stacks/v1",
        "status": "generated",
        "decision_rule": "DR-084",
        "as_of": syn.iso_utc(syn.parse_moment(AS_OF)),
        "as_of_basis": "fixed: end of the 2025 retrospective shelf",
        "source": {
            "chart_registry_path": "99 - Templates/chart_reading_bones_2025/index.json",
            "chart_registry_generated": index.get("generated"),
            "chart_registry_sha256": syn._sha256(BONES / "index.json"),
            "seed_registry_path": "synodic_seed_families.json",
            "seed_registry_sha256": syn._sha256(HERE / "synodic_seed_families.json"),
            "phase_grammar_source": _rel(phase_source, vault_root),
        },
        "tiers": registry["tiers"],
        "cycle_catalog": registry["cycles"],
        "coverage": {
            "registered_chart_count": len(index["charts"]),
            "generated_chart_count": len(charts),
            "cycle_count": len(registry["cycles"]),
            "relationship_state_count": sum(len(c["cycles"]) for c in charts),
        },
        "charts": charts,
    }
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"LONG CLOCKS STACKS 2025: wrote {OUTPUT.name} · {len(charts)} charts · "
          f"{payload['coverage']['relationship_state_count']} relationship states · "
          f"{time.perf_counter() - started:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
