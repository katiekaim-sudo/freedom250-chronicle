#!/usr/bin/env python3
"""Build the deterministic 30-chart Long Clocks data contract."""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import synodic_cycles as syn


HERE = Path(__file__).resolve().parent


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault-root", type=Path, default=syn.DEFAULT_VAULT_ROOT)
    parser.add_argument(
        "--seed-registry", type=Path, default=HERE / "synodic_seed_families.json"
    )
    parser.add_argument(
        "--output", type=Path, default=HERE / "chart_synodic_stacks.json"
    )
    parser.add_argument(
        "--as-of",
        default=None,
        help="Explicit timezone-aware snapshot instant; default is noon on today's D.C. date.",
    )
    parser.add_argument(
        "--skip-event-catalog",
        action="store_true",
        help="Fast diagnostic only; canonical output includes exact-event neighbors.",
    )
    args = parser.parse_args()

    started = time.perf_counter()
    payload = syn.build_chart_stacks_payload(
        vault_root=args.vault_root,
        seed_registry_path=args.seed_registry,
        as_of=args.as_of,
        include_event_catalog=not args.skip_event_catalog,
    )
    elapsed = time.perf_counter() - started
    payload["build_receipt"] = {
        "builder": Path(__file__).name,
        "elapsed_seconds": round(elapsed, 3),
        "offline": True,
        "event_catalog_included": not args.skip_event_catalog,
        "as_of_basis": payload["as_of_basis"],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"LONG CLOCKS STACKS: wrote {args.output} · "
        f"{payload['coverage']['generated_chart_count']} charts · "
        f"{payload['coverage']['relationship_state_count']} relationship states · "
        f"{elapsed:.3f}s"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
