#!/usr/bin/env python3
"""Materialize deterministic Daybreak geometry before Almanac projection."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import tempfile
from pathlib import Path

import daybreak_engine as engine

SCHEMA = "f250.daybreak-frames/v1"


def _date(value: str) -> dt.date:
    return dt.date.fromisoformat(value)


def _write_atomic(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=False, separators=(",", ":")) + "\n"
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=path.parent, prefix=f".{path.name}.", delete=False
    ) as handle:
        handle.write(raw)
        temporary = Path(handle.name)
    os.replace(temporary, path)


def _prior_payload(path: Path) -> dict | None:
    if not path.exists():
        return None
    try:
        prior = json.loads(path.read_text(encoding="utf-8"))
        if prior.get("schema") != SCHEMA:
            return None
        value = dt.datetime.fromisoformat(prior["generated_at"])
        return prior if value.tzinfo is not None else None
    except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError):
        return None


def _same_facts(left: dict, right: dict) -> bool:
    left_facts = dict(left)
    right_facts = dict(right)
    left_facts.pop("generated_at", None)
    right_facts.pop("generated_at", None)
    return left_facts == right_facts


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=_date, default=dt.date(2026, 1, 1))
    parser.add_argument("--end", type=_date, default=dt.date(2026, 12, 31))
    parser.add_argument("--vault-root", type=Path, default=engine.DEFAULT_VAULT_ROOT)
    parser.add_argument("--experiment", type=Path)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent / "daybreak_frames.json",
    )
    parser.add_argument("--generated-at", help="timezone-aware ISO timestamp for deterministic receipts")
    args = parser.parse_args()
    if args.end < args.start:
        parser.error("--end must be on or after --start")
    generated_at = None
    if args.generated_at:
        generated_at = dt.datetime.fromisoformat(args.generated_at)
        if generated_at.tzinfo is None:
            parser.error("--generated-at must be timezone-aware")
    payload = engine.build_payload(
        args.start,
        args.end,
        vault_root=args.vault_root,
        experiment_path=args.experiment,
        generated_at=generated_at,
    )
    if not args.generated_at:
        prior = _prior_payload(args.output)
        if prior is not None and _same_facts(prior, payload):
            payload["generated_at"] = prior["generated_at"]
    _write_atomic(args.output, payload)
    print(
        json.dumps(
            {
                "status": "ok",
                "output": str(args.output),
                "schema": payload["schema"],
                "coverage": payload["coverage"],
                "sha256": engine.canonical_sha256(payload),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
