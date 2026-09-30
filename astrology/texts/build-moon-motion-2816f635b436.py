#!/usr/bin/env python3
"""Build factual Moon-motion geometry for governed downstream adapters.

This builder keeps Pessin's 273/546/819-day lineage distinct from an
approximate half-year New-to-Full candidate geometry. It imports only the
calculation helpers from the legacy Moon Families injector; it never parses the
generated Moon Families or Lunar Weather HTML and carries no event/story data.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import swisseph as swe

from atomic_io import atomic_write_text
import build_moon_lineages as calculation

HERE = Path(__file__).resolve().parent
VAULT = HERE.parent
OUTPUT = HERE / "moon_lineages.json"
MUNDANE = HERE / "mundane_history.json"
READINGS = VAULT / "03 - Astrology" / "chart_reading_registry.json"
METHOD = VAULT / "00 - Index" / "Pessin — Lunar Shadows III Study Notes.md"
METHOD_ROUTER = VAULT / "00 - Index" / "Reading the Charts — START HERE.md"
LEGACY_CALCULATOR = HERE / "build_moon_lineages.py"
NY = ZoneInfo("America/New_York")
PHASE_LABEL = {"nm": "new_moon", "fq": "first_quarter", "fm": "full_moon", "lq": "last_quarter"}
PHASE_ROLE = {"nm": "seed", "fq": "first_quarter", "fm": "full", "lq": "last_quarter"}
CANONICAL_JD_TOLERANCE_DAYS = 0.0001
ECHO_KEYS = {
    "echo_id", "echo_kind", "method_status", "seed_chart_id", "seed_phase_event_id",
    "return_chart_id", "return_phase_event_id", "elapsed_days", "zodiac_distance_deg",
    "interpretation_status", "continuity_verdict",
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def iso_utc(jd: float) -> str:
    year, month, day, hour = swe.revjul(jd)
    value = datetime(year, month, day, tzinfo=timezone.utc) + timedelta(hours=hour)
    return value.isoformat(timespec="microseconds").replace("+00:00", "Z")


def iso_local(jd: float) -> str:
    return datetime.fromisoformat(iso_utc(jd).replace("Z", "+00:00")).astimezone(NY).isoformat(timespec="microseconds")


def _canonicalize(lunations: list[dict]) -> tuple[set[str], list[dict]]:
    mundane = load(MUNDANE)
    reading_ids = {row["id"] for row in load(READINGS)["readings"]}
    charts = mundane["charts"]
    catalog_lunations = [row for row in charts if row.get("chart_type") == "lunation"]
    ingresses = sorted(
        (row for row in charts if row.get("chart_type") == "ingress" and row.get("standing") == "governing"),
        key=lambda row: row["jd_ut"],
    )
    by_phase_date = {}
    for row in catalog_lunations:
        code = "nm" if row.get("kind") == "new" else "fm"
        by_phase_date.setdefault((code, row["utc_date"]), []).append(row)
    for event in lunations:
        event["exact_utc"] = iso_utc(event["jd"])
        event["exact_local"] = iso_local(event["jd"])
        event["sun_lon"] = calculation.lon(event["jd"], swe.SUN)
        event["moon_lon"] = calculation.lon(event["jd"], swe.MOON)
        matches = by_phase_date.get((event["ph"], event["date"]), [])
        event["canonical"] = min(matches, key=lambda row: abs(row["jd_ut"] - event["jd"])) if matches else None
        if event["canonical"] and abs(event["canonical"]["jd_ut"] - event["jd"]) > CANONICAL_JD_TOLERANCE_DAYS:
            raise ValueError(f"Moon-motion calculation drift for {event['canonical']['id']}")
        governors = [row for row in ingresses if row["jd_ut"] <= event["jd"]]
        event["governing_ingress_id"] = governors[-1]["id"] if governors else None
        if event["canonical"] and event["canonical"].get("governing_ingress_id") != event["governing_ingress_id"]:
            raise ValueError(f"Moon-motion ingress drift for {event['canonical']['id']}")
    return reading_ids, ingresses


def phase_event(event: dict, reading_ids: set[str]) -> dict:
    canonical = event["canonical"]
    chart_id = canonical["id"] if canonical else None
    phase_event_id = chart_id or f"lunation-{event['date']}-{event['ph']}"
    moon_lon = event["moon_lon"]
    sun_lon = event["sun_lon"]
    if canonical:
        moon_lon = next(row["lon"] for row in canonical["points"] if row["name"] == "Moon")
        sun_lon = next(row["lon"] for row in canonical["points"] if row["name"] == "Sun")
    return {
        "phase_event_id": phase_event_id,
        "chart_id": chart_id,
        "phase": PHASE_LABEL[event["ph"]],
        "exact_utc": canonical["utc"].replace("+00:00", "Z") if canonical else event["exact_utc"],
        "exact_local": canonical["local"] if canonical else event["exact_local"],
        "place_id": "washington-dc",
        "sun_lon_deg": round(sun_lon, 9),
        "moon_lon_deg": round(moon_lon, 9),
        "moon_sign": calculation.SIGNS[int(moon_lon // 30)],
        "moon_degree": round(moon_lon % 30, 1),
        "eclipse": None if event["ph"] not in {"nm", "fm"} else bool(canonical.get("eclipse") if canonical else event["ec"]),
        "governing_ingress_id": event["governing_ingress_id"],
        "reading_id": chart_id if chart_id in reading_ids else None,
        "route": {"tab": "obs-lw", "date": event["date"]},
    }


def validate_payload(payload: dict) -> None:
    events = {row["phase_event_id"]: row for row in payload["phase_events"]}
    for lineage in payload["lineages"]:
        members = lineage["members"]
        if [row["role"] for row in members] != ["seed", "first_quarter", "full", "last_quarter"]:
            raise ValueError(f"Pessin lineage phase order drift: {lineage['lineage_id']}")
        seed_sign = events[members[0]["phase_event_id"]]["moon_sign"]
        if any(events[row["phase_event_id"]]["moon_sign"] != seed_sign for row in members):
            raise ValueError(f"Pessin lineage crosses signs: {lineage['lineage_id']}")
    for echo in payload["echo_candidates"]:
        if set(echo) != ECHO_KEYS:
            raise ValueError(f"Half-year echo schema drift: {echo.get('echo_id', 'unknown')}")
        if (
            echo["echo_kind"] != "approx_half_year_degree_echo"
            or echo["method_status"] != "candidate_projection"
            or echo["interpretation_status"] != "unreviewed"
            or echo["continuity_verdict"] is not None
            or not 165 <= echo["elapsed_days"] <= 201
            or not 0 <= echo["zodiac_distance_deg"] <= 6
        ):
            raise ValueError(f"Half-year echo authority drift: {echo['echo_id']}")


def build_payload() -> dict:
    lunations = calculation.lunations()
    reading_ids, _ = _canonicalize(lunations)
    by_key = {(row["ph"], row["date"]): row for row in lunations}
    new_moons = [row for row in lunations if row["ph"] == "nm"
                 and "2023-06-01" <= row["date"] <= calculation.HORIZON_END.isoformat()]
    used_keys = set()
    lineages = []
    for seed in new_moons:
        members = [seed]
        for code in ("fq", "fm", "lq"):
            target = seed["jd"] + calculation.SPACING[code]
            candidates = [row for row in lunations if row["ph"] == code
                          and abs(row["jd"] - target) <= 18
                          and row["sign"] == seed["sign"]
                          and calculation.degree_distance(row["fdeg"], seed["fdeg"]) <= 6]
            if not candidates:
                members = []
                break
            members.append(min(candidates, key=lambda row: (
                calculation.degree_distance(row["fdeg"], seed["fdeg"]), abs(row["jd"] - target))))
        if not members or not any("2024-09-01" <= row["date"] <= calculation.HORIZON_END.isoformat() for row in members):
            continue
        seed_ref = phase_event(seed, reading_ids)
        member_rows = []
        for member in members:
            used_keys.add((member["ph"], member["date"]))
            ref = phase_event(member, reading_ids)
            member_rows.append({
                "role": PHASE_ROLE[member["ph"]],
                "phase_event_id": ref["phase_event_id"],
                "chart_id": ref["chart_id"],
                "governing_ingress_id": ref["governing_ingress_id"],
                "elapsed_days_from_seed": round(member["jd"] - seed["jd"], 6),
                "zodiac_distance_from_seed_deg": round(calculation.degree_distance(member["fdeg"], seed["fdeg"]), 6),
            })
        lineages.append({
            "lineage_id": f"pessin:{seed_ref['chart_id'] or seed_ref['phase_event_id']}",
            "seed_chart_id": seed_ref["chart_id"],
            "seed_phase_event_id": seed_ref["phase_event_id"],
            "degree_band": calculation.band(seed["deg"]),
            "members": member_rows,
            "interpretation_status": "unreviewed",
            "story_verdict": None,
        })

    echoes = []
    for seed in new_moons:
        seed_ref = phase_event(seed, reading_ids)
        matches = [row for row in lunations if row["ph"] == "fm"
                   and abs((row["jd"] - seed["jd"]) - 183.0) <= 18
                   and calculation.degree_distance(row["fdeg"], seed["fdeg"]) <= 6]
        for returned in sorted(matches, key=lambda row: row["jd"]):
            return_ref = phase_event(returned, reading_ids)
            used_keys.add((returned["ph"], returned["date"]))
            echoes.append({
                "echo_id": f"half-year:{seed_ref['chart_id'] or seed_ref['phase_event_id']}:{return_ref['chart_id'] or return_ref['phase_event_id']}",
                "echo_kind": "approx_half_year_degree_echo",
                "method_status": "candidate_projection",
                "seed_chart_id": seed_ref["chart_id"],
                "seed_phase_event_id": seed_ref["phase_event_id"],
                "return_chart_id": return_ref["chart_id"],
                "return_phase_event_id": return_ref["phase_event_id"],
                "elapsed_days": round(returned["jd"] - seed["jd"], 6),
                "zodiac_distance_deg": round(calculation.degree_distance(returned["fdeg"], seed["fdeg"]), 6),
                "interpretation_status": "unreviewed",
                "continuity_verdict": None,
            })
    phase_events = [phase_event(by_key[key], reading_ids)
                    for key in sorted(used_keys, key=lambda item: by_key[item]["jd"])]
    ids = [row["phase_event_id"] for row in phase_events]
    if len(ids) != len(set(ids)):
        raise ValueError("Moon-motion phase event IDs must be unique")
    payload = {
        "schema": "f250.moon-motion/v1",
        "status": "generated_factual_projection",
        "coverage": {
            "calculation_from": calculation.START.isoformat(),
            "seed_from": "2023-06-01",
            "seed_through": calculation.HORIZON_END.isoformat(),
            "complete_tail_through": calculation.CALC_END.isoformat(),
        },
        "method": {
            "owner_path": str(METHOD.relative_to(VAULT)),
            "lineage_rule": "same_sign_and_degree_near_273_546_819_days",
            "target_days": {"first_quarter": 273, "full": 546, "last_quarter": 819},
            "date_tolerance_days": 18,
            "degree_tolerance_deg": 6,
            "canonical_chart_time_tolerance_seconds": CANONICAL_JD_TOLERANCE_DAYS * 86400,
            "half_year_echo": {
                "status": "candidate_projection_not_adopted_pessin_phase",
                "target_days": 183,
                "date_tolerance_days": 18,
                "degree_tolerance_deg": 6
            },
            "source_tension": "The current Pessin digest says First Quarter is roughly three months and also says nine months between same-degree phases. The factual engine follows the established 273/546/819-day implementation; Studio does not silently resolve the prose conflict."
        },
        "phase_events": phase_events,
        "lineages": lineages,
        "echo_candidates": echoes,
        "source_receipts": {
            str(MUNDANE.relative_to(VAULT)): {"sha256": sha256(MUNDANE)},
            str(READINGS.relative_to(VAULT)): {"sha256": sha256(READINGS)},
            str(METHOD.relative_to(VAULT)): {"sha256": sha256(METHOD)},
            str(METHOD_ROUTER.relative_to(VAULT)): {"sha256": sha256(METHOD_ROUTER)},
            str(LEGACY_CALCULATOR.relative_to(VAULT)): {"sha256": sha256(LEGACY_CALCULATOR)}
        },
        "boundaries": {
            "story_assignment": False,
            "continuity_verdict": False,
            "prediction": False,
            "forecast_credit": False,
            "factual_evidence_credit": False,
            "ranking": False,
            "attention_proximity_in_factual_adapter": False,
            "half_year_echo_is_adopted_pessin_phase": False
        }
    }
    validate_payload(payload)
    return payload


def render(payload: dict) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args(argv)
    content = render(build_payload())
    if args.check:
        clean = args.output.exists() and args.output.read_text(encoding="utf-8") == content
        print("MOON MOTION CHECK: CLEAN" if clean else "MOON MOTION CHECK: STALE")
        return 0 if clean else 1
    atomic_write_text(args.output, content)
    payload = json.loads(content)
    print(f"MOON MOTION BUILT: {len(payload['lineages'])} Pessin lineages · {len(payload['echo_candidates'])} half-year candidates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
