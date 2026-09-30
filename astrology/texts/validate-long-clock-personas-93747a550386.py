#!/usr/bin/env python3
"""Fail-closed validation for all governed Long Clock persona subsidiaries."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import swisseph as swe


HERE = Path(__file__).resolve().parent
BUILDER_PATH = HERE / "build_long_clock_personas.py"
DATA_DIR = HERE / "data"
CHARTS_DIR = HERE / "charts"
INDEX_PATH = DATA_DIR / "index.json"
HUB_PATH = CHARTS_DIR / "index.html"
MANIFEST_PATH = HERE / "manifest.json"
VAULT = Path("Chronicle/")
REGISTRY_PATH = VAULT / "99 - Templates" / "synodic_seed_families.json"
SYNODIC_PATH = VAULT / "99 - Templates" / "synodic_cycles.py"
PLANET_CODES = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mercury": swe.MERCURY,
    "Venus": swe.VENUS,
    "Mars": swe.MARS,
    "Jupiter": swe.JUPITER,
    "Saturn": swe.SATURN,
    "Uranus": swe.URANUS,
    "Neptune": swe.NEPTUNE,
    "Pluto": swe.PLUTO,
}
PLANET_ORDER = tuple(PLANET_CODES)
TRACKED = ("Mercury", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto")
SLOW = ("Jupiter", "Saturn", "Uranus", "Neptune", "Pluto")
MUNDANE_RULES = (
    ("conjunction", 0.0, 8.0),
    ("sextile", 60.0, 5.0),
    ("square", 90.0, 7.0),
    ("trine", 120.0, 7.0),
    ("opposition", 180.0, 8.0),
)


def load_module(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BUILD = load_module(BUILDER_PATH, "f250_long_clock_persona_validator_builder")
SYNODIC = load_module(SYNODIC_PATH, "f250_long_clock_persona_validator_synodic")


def check(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def signed_delta(a: float, b: float) -> float:
    return ((a - b + 540.0) % 360.0) - 180.0


def angular_distance(a: float, b: float) -> float:
    return abs(signed_delta(a, b))


def jd_of(moment: datetime) -> float:
    utc = moment.astimezone(timezone.utc)
    hour = (
        utc.hour
        + utc.minute / 60.0
        + utc.second / 3600.0
        + utc.microsecond / 3_600_000_000.0
    )
    return swe.julday(utc.year, utc.month, utc.day, hour)


def jd_to_utc(jd_ut: float) -> datetime:
    return datetime(2000, 1, 1, 12, tzinfo=timezone.utc) + timedelta(
        days=jd_ut - 2451545.0
    )


def body_state(jd_ut: float, body: str) -> tuple[float, float, int]:
    result, returned = swe.calc_ut(
        jd_ut, PLANET_CODES[body], swe.FLG_MOSEPH | swe.FLG_SPEED
    )
    return result[0] % 360.0, result[3], int(returned)


def bisection(function, lo: float, hi: float, iterations: int = 100) -> float:
    flo, fhi = function(lo), function(hi)
    if flo == 0:
        return lo
    if fhi == 0:
        return hi
    if flo * fhi > 0:
        raise RuntimeError(f"Root not bracketed: {flo=} {fhi=}")
    for _ in range(iterations):
        mid = (lo + hi) / 2.0
        fm = function(mid)
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2.0


def independent_seed_root(cycle: dict[str, Any], anchor: dict[str, Any]) -> float:
    seed_jd = jd_of(datetime.fromisoformat(anchor["utc"]))
    a, b = cycle["pair"]
    return bisection(
        lambda value: signed_delta(
            body_state(value, a)[0], body_state(value, b)[0]
        ),
        seed_jd - 1.0,
        seed_jd + 1.0,
    )


def independent_persona_root(seed_jd: float, target: float) -> float:
    def delta(value: float) -> float:
        sun = body_state(value, "Sun")[0]
        return signed_delta(sun, target)

    prior_jd = seed_jd + 1e-7
    prior_delta = delta(prior_jd)
    while prior_jd < seed_jd + 370.0:
        current_jd = prior_jd + 0.25
        current_delta = delta(current_jd)
        if prior_delta <= 0 <= current_delta and current_delta - prior_delta < 10:
            return bisection(delta, prior_jd, current_jd)
        prior_jd, prior_delta = current_jd, current_delta
    raise RuntimeError("Independent persona root was not found")


def independent_stations(
    start_jd: float, end_jd: float
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for body in TRACKED:
        prior_jd = start_jd
        prior_speed = body_state(prior_jd, body)[1]
        last_root: float | None = None
        while prior_jd < end_jd:
            current_jd = min(prior_jd + 0.125, end_jd)
            current_speed = body_state(current_jd, body)[1]
            if prior_speed == 0.0 or prior_speed * current_speed < 0.0:
                root = bisection(
                    lambda value: body_state(value, body)[1], prior_jd, current_jd
                )
                if last_root is None or abs(root - last_root) > 1e-5:
                    before = body_state(root - 1.0 / 1440.0, body)[1]
                    after = body_state(root + 1.0 / 1440.0, body)[1]
                    rows.append(
                        {
                            "body": body,
                            "jd": root,
                            "direction_before": "direct" if before > 0 else "retrograde",
                            "direction_after": "direct" if after > 0 else "retrograde",
                        }
                    )
                    last_root = root
            prior_jd, prior_speed = current_jd, current_speed
    return sorted(rows, key=lambda row: row["jd"])


def aspect_key(row: dict[str, Any], *, angle: bool = False) -> tuple[str, str]:
    if angle:
        return row["point"], row["planet"]
    return tuple(sorted((row["a"], row["b"])))


def independent_mundane(
    positions: dict[str, dict[str, Any]]
) -> dict[tuple[str, str], tuple[str, float]]:
    output: dict[tuple[str, str], tuple[str, float]] = {}
    for index, a in enumerate(PLANET_ORDER):
        for b in PLANET_ORDER[index + 1 :]:
            separation = angular_distance(
                positions[a]["longitude"], positions[b]["longitude"]
            )
            aspect, angle, limit = min(
                MUNDANE_RULES, key=lambda row: abs(separation - row[1])
            )
            orb = abs(separation - angle)
            if orb <= limit:
                output[tuple(sorted((a, b)))] = (aspect, orb)
    return output


def validate_endpoint_ledger(
    data: dict[str, Any], cycle_id: str, errors: list[str]
) -> None:
    gate = data["seed_to_persona_change_gate"]
    ledgers = gate.get("relationship_deltas", {})
    specs = {
        "mundane_major_ten_planet": (
            "mundane_major_aspects",
            False,
        ),
        "huber_source_plus_chiron_overlay": ("huber_aspects", False),
        "nonacting_minor_point": ("minor_point_aspects", False),
        "derived_angle": ("angle_aspects", True),
    }
    for lane, (field, angle) in specs.items():
        rows = ledgers.get(lane)
        check(isinstance(rows, list), f"{cycle_id}: missing ledger {lane}", errors)
        if not isinstance(rows, list):
            continue
        seed_rows = data["radix"][field]
        persona_rows = data["persona"][field]
        expected = {
            aspect_key(row, angle=angle) for row in seed_rows + persona_rows
        }
        actual = {tuple(row["relationship"]) for row in rows}
        check(actual == expected, f"{cycle_id}: incomplete endpoint union in {lane}", errors)
        for row in rows:
            key = tuple(row["relationship"])
            before = next(
                (item for item in seed_rows if aspect_key(item, angle=angle) == key),
                None,
            )
            after = next(
                (
                    item
                    for item in persona_rows
                    if aspect_key(item, angle=angle) == key
                ),
                None,
            )
            check(
                (row["seed"] is None) == (before is None),
                f"{cycle_id}: seed endpoint mismatch {lane}/{key}",
                errors,
            )
            check(
                (row["persona"] is None) == (after is None),
                f"{cycle_id}: persona endpoint mismatch {lane}/{key}",
                errors,
            )
            expected_change = (
                "gained"
                if before is None
                else "lost"
                if after is None
                else "operator_changed"
                if before.get("aspect", before.get("type"))
                != after.get("aspect", after.get("type"))
                else "persisted_with_condition_change"
            )
            check(
                row["change"] == expected_change,
                f"{cycle_id}: change classification mismatch {lane}/{key}",
                errors,
            )
            check(bool(row.get("classification")), f"{cycle_id}: unclassified ledger row", errors)


def validate_chart_lanes(
    data: dict[str, Any], cycle_id: str, errors: list[str]
) -> None:
    for endpoint in ("radix", "persona"):
        chart = data[endpoint]
        for field in (
            "frame",
            "positions",
            "mundane_major_aspects",
            "huber_aspects",
            "minor_point_aspects",
            "angle_aspects",
            "huber_whole_pattern",
            "governance_routes",
        ):
            check(field in chart, f"{cycle_id}: {endpoint} omits {field}", errors)
        independent = independent_mundane(chart["positions"])
        serialized = {
            aspect_key(row): (row["aspect"], row["orb_deg"])
            for row in chart["mundane_major_aspects"]
        }
        check(
            set(independent) == set(serialized),
            f"{cycle_id}: {endpoint} mundane aspect inventory incomplete",
            errors,
        )
        for key, (aspect, orb) in independent.items():
            if key not in serialized:
                continue
            check(
                serialized[key][0] == aspect,
                f"{cycle_id}: {endpoint} mundane operator mismatch {key}",
                errors,
            )
            check(
                abs(serialized[key][1] - orb) <= 0.000001,
                f"{cycle_id}: {endpoint} mundane orb mismatch {key}",
                errors,
            )
        for row in chart["minor_point_aspects"]:
            check(
                row["a"] in {"Chiron", "Node", "America"}
                and row["b"] in PLANET_CODES,
                f"{cycle_id}: invalid minor-point direction",
                errors,
            )
            check(
                row["aspect"] in {"conjunction", "square", "opposition"}
                and row["orb_deg"] <= 2.0,
                f"{cycle_id}: invalid minor-point aspect",
                errors,
            )
        for row in chart["angle_aspects"]:
            check(
                row["point"] in {"ASC", "MC"} and bool(row["planet"]),
                f"{cycle_id}: invalid derived-angle relationship",
                errors,
            )


def validate_america(
    data: dict[str, Any], cycle_id: str, errors: list[str]
) -> None:
    seed = datetime.fromisoformat(data["radix"]["event"]["utc"])
    persona = datetime.fromisoformat(data["persona"]["event"]["utc"])
    expected = all(
        BUILD.america.america_lon(moment) is not None
        and BUILD.america.america_speed(moment) is not None
        for moment in (seed, seed + timedelta(hours=1), persona, persona + timedelta(hours=1))
    )
    coverage = data["america_916_coverage"]
    check(
        coverage["include_in_both_charts"] == expected,
        f"{cycle_id}: America pair coverage mismatch",
        errors,
    )
    for endpoint in ("radix", "persona"):
        point = data[endpoint]["minor_points"]["america_916"]
        rows = data[endpoint]["minor_point_aspects"]
        if expected:
            check(
                point["status"] == "available_canonical_cache"
                and point["longitude"] is not None,
                f"{cycle_id}: covered America missing at {endpoint}",
                errors,
            )
        else:
            check(
                point["status"] == "unavailable_no_extrapolation"
                and point["longitude"] is None,
                f"{cycle_id}: historical America not fail-closed at {endpoint}",
                errors,
            )
            check(
                all("America" not in {row["a"], row["b"]} for row in rows),
                f"{cycle_id}: unavailable America leaked into aspects",
                errors,
            )


def validate_change_gate(
    data: dict[str, Any], cycle_id: str, errors: list[str]
) -> None:
    seed_jd = jd_of(datetime.fromisoformat(data["radix"]["event"]["utc"]))
    persona_jd = jd_of(datetime.fromisoformat(data["persona"]["event"]["utc"]))
    gate = data["seed_to_persona_change_gate"]
    interval = persona_jd - seed_jd
    check(
        abs(gate["interval_days"] - interval) <= 1e-9,
        f"{cycle_id}: change-gate interval drift",
        errors,
    )
    check(
        gate["within_31_day_dependency_window"] == (interval <= 31.0),
        f"{cycle_id}: 31-day gate mismatch",
        errors,
    )
    rule = gate["rule"]
    check(
        "within 31 days" in rule
        and "After 31 days" in rule
        and "Mercury" in rule,
        f"{cycle_id}: explicit 31-day/Mercury clause missing",
        errors,
    )
    check(
        gate["slow_body_scope"] == list(SLOW)
        and "Mercury" not in gate["slow_body_scope"],
        f"{cycle_id}: Mercury incorrectly classified slow/outer",
        errors,
    )
    expected_signs = {
        body
        for body in TRACKED
        if data["radix"]["positions"][body]["sign"]
        != data["persona"]["positions"][body]["sign"]
    }
    stored_signs = {row["body"] for row in gate["tracked_body_sign_changes"]}
    check(expected_signs == stored_signs, f"{cycle_id}: sign gate incomplete", errors)
    expected_directions = {
        body
        for body in TRACKED
        if data["radix"]["positions"][body]["retrograde"]
        != data["persona"]["positions"][body]["retrograde"]
    }
    stored_directions = {
        row["body"] for row in gate["tracked_body_direction_changes"]
    }
    check(
        expected_directions == stored_directions,
        f"{cycle_id}: direction gate incomplete",
        errors,
    )
    independent = independent_stations(seed_jd, persona_jd)
    stored = gate["station_events_between"]
    check(
        len(independent) == len(stored),
        f"{cycle_id}: station count mismatch {len(stored)} != {len(independent)}",
        errors,
    )
    for expected, actual in zip(independent, stored):
        check(expected["body"] == actual["body"], f"{cycle_id}: station body/order mismatch", errors)
        actual_jd = jd_of(datetime.fromisoformat(actual["utc"]))
        check(
            abs(expected["jd"] - actual_jd) * 86400.0 <= 0.001,
            f"{cycle_id}: station time mismatch for {actual['body']}",
            errors,
        )
        check(
            expected["direction_before"] == actual["direction_before"]
            and expected["direction_after"] == actual["direction_after"],
            f"{cycle_id}: station direction mismatch for {actual['body']}",
            errors,
        )
    validate_endpoint_ledger(data, cycle_id, errors)


def validate_cycle(
    cycle: dict[str, Any], index_row: dict[str, Any], errors: list[str]
) -> None:
    cycle_id = cycle["cycle_id"]
    data_path = HERE / index_row["artifacts"]["data"]
    check(data_path.exists(), f"{cycle_id}: data file missing", errors)
    if not data_path.exists():
        return
    data = json.loads(data_path.read_text(encoding="utf-8"))
    anchor = next(
        row
        for row in cycle["passes"]
        if row["pass_id"] == cycle["display_anchor_pass_id"]
    )
    check(
        data.get("schema") == "freedom250.long-clock-persona-subsidiary/v1",
        f"{cycle_id}: schema mismatch",
        errors,
    )
    check(
        data.get("status") == "kept_conditional_subsidiary"
        and data.get("review_disposition") == "keep",
        f"{cycle_id}: keep disposition/status mismatch",
        errors,
    )
    boundary = data["evidence_boundary"]
    check(
        boundary["admission"] == "conditional_subordinate_zero_vote"
        and boundary["independent_vote"] is False
        and boundary["one_shared_chart"] is True
        and boundary["focal_lenses"] == cycle["pair"],
        f"{cycle_id}: evidence boundary drift",
        errors,
    )
    identity = data["identity"]
    check(identity["cycle_id"] == cycle_id, f"{cycle_id}: cycle identity mismatch", errors)
    check(
        identity["display_anchor_pass_id"] == anchor["pass_id"],
        f"{cycle_id}: anchor identity mismatch",
        errors,
    )
    check(
        identity["artifact_key"] == f"{cycle_id}::{anchor['pass_id']}",
        f"{cycle_id}: artifact key mismatch",
        errors,
    )
    check(
        data["seed_family"]["complete_pass_roster"] == cycle["passes"],
        f"{cycle_id}: complete family pass roster drift",
        errors,
    )
    radix = data["radix"]
    persona = data["persona"]
    check(radix["event"]["utc"] == anchor["utc"], f"{cycle_id}: seed UTC mismatch", errors)
    check(
        abs(radix["target_longitude"] - anchor["longitude_deg"]) < 1e-12,
        f"{cycle_id}: target mismatch",
        errors,
    )
    seed_jd = jd_of(datetime.fromisoformat(anchor["utc"]))
    independent_seed = independent_seed_root(cycle, anchor)
    check(
        abs(independent_seed - seed_jd) * 86400.0 <= 0.01,
        f"{cycle_id}: independent seed root mismatch",
        errors,
    )
    independent_persona = independent_persona_root(
        seed_jd, anchor["longitude_deg"]
    )
    stored_persona = jd_of(datetime.fromisoformat(persona["event"]["utc"]))
    check(
        abs(independent_persona - stored_persona) * 86400.0 <= 0.001,
        f"{cycle_id}: independent persona root mismatch",
        errors,
    )
    sun = body_state(stored_persona, "Sun")[0]
    check(
        angular_distance(sun, anchor["longitude_deg"]) * 3600.0 <= 0.01,
        f"{cycle_id}: persona Sun target residual exceeds 0.01 arcsec",
        errors,
    )
    canonical = SYNODIC.seed_chart(
        cycle_id,
        anchor["pass_id"],
        vault_root=VAULT,
        seed_registry_path=REGISTRY_PATH,
    )
    deltas = [
        angular_distance(canonical["asc"], radix["frame"]["asc"]) * 3600.0,
        angular_distance(canonical["mc"], radix["frame"]["mc"]) * 3600.0,
    ]
    deltas.extend(
        angular_distance(
            canonical["positions"][body]["lon"],
            radix["positions"][body]["longitude"],
        )
        * 3600.0
        for body in PLANET_ORDER
    )
    check(max(deltas) <= 0.01, f"{cycle_id}: canonical seed chart mismatch", errors)
    for body in cycle["pair"]:
        check(body in persona["focal_lenses"], f"{cycle_id}: missing focal lens {body}", errors)
    check(
        len(persona["focal_lenses"]) == 2,
        f"{cycle_id}: conjunction must have exactly two focal lenses",
        errors,
    )
    validate_chart_lanes(data, cycle_id, errors)
    validate_america(data, cycle_id, errors)
    validate_change_gate(data, cycle_id, errors)
    runtime = data["ephemeris_runtime_receipt"]
    for endpoint, moment in (
        ("seed", seed_jd),
        ("persona", stored_persona),
    ):
        _pos, actual = swe.calc_ut(
            moment, swe.SUN, swe.FLG_SWIEPH | swe.FLG_SPEED
        )
        stored = runtime[endpoint]["returned_by_body"]["Sun"]
        check(stored["bits"] == int(actual), f"{cycle_id}: actual flag receipt drift", errors)
        fallback = not (actual & swe.FLG_SWIEPH) and bool(actual & swe.FLG_MOSEPH)
        check(
            stored["fallback_from_requested_swieph"] == fallback,
            f"{cycle_id}: fallback receipt mismatch",
            errors,
        )
    serialized = json.dumps(data, ensure_ascii=False).lower()
    check(
        "swiss_solcross_vs_moshier" not in serialized,
        f"{cycle_id}: independent-Swiss overclaim found",
        errors,
    )
    check(
        "no independent-swiss verification is claimed" in serialized
        and "returned flags" in serialized,
        f"{cycle_id}: explicit actual-flag/no-independent-Swiss boundary missing",
        errors,
    )


def validate_hub(index: dict[str, Any], errors: list[str]) -> None:
    html_text = HUB_PATH.read_text(encoding="utf-8")
    check(html_text.count("<svg") == 20, "self-contained hub does not inline 20 SVGs", errors)
    check('src="' not in html_text, "self-contained hub has external src dependency", errors)
    relative_hrefs = re.findall(r'href="(?!data:|#)([^"]+)"', html_text)
    check(not relative_hrefs, f"self-contained hub has sidecar hrefs: {relative_hrefs}", errors)
    match = re.search(
        r'<script type="application/json" id="long-clock-persona-data">(.*?)</script>',
        html_text,
        re.S,
    )
    check(match is not None, "self-contained hub lacks embedded data", errors)
    if match:
        embedded = json.loads(match.group(1))
        check(len(embedded.get("cycles", [])) == 10, "embedded hub data count mismatch", errors)
        check(
            {row["identity"]["cycle_id"] for row in embedded["cycles"]}
            == {row["cycle_id"] for row in index["cycles"]},
            "embedded hub identities drift",
            errors,
        )


def validate_manifest(manifest: dict[str, Any], errors: list[str]) -> None:
    check(
        manifest.get("schema") == "freedom250.long-clock-persona-manifest/v1",
        "manifest schema mismatch",
        errors,
    )
    check(manifest.get("cycle_count") == 10, "manifest cycle count mismatch", errors)
    check(
        manifest.get("governed_family_pass_count") == 20,
        "manifest pass count mismatch",
        errors,
    )
    for relative, expected in manifest.get("outputs_sha256", {}).items():
        path = HERE / relative
        check(path.exists(), f"manifest output missing: {relative}", errors)
        if path.exists():
            check(sha256(path) == expected, f"manifest output hash drift: {relative}", errors)
    expected_outputs = {
        str(path.relative_to(HERE))
        for path in [INDEX_PATH, HUB_PATH]
        + sorted(DATA_DIR.glob("*.json"))
        + sorted(CHARTS_DIR.glob("*.svg"))
    }
    check(
        set(manifest.get("outputs_sha256", {})) == expected_outputs,
        "manifest generated-output inventory incomplete or excessive",
        errors,
    )
    for source, expected in manifest.get("source_sha256", {}).items():
        path = Path(source)
        check(path.exists(), f"manifest source missing: {source}", errors)
        if path.exists():
            check(sha256(path) == expected, f"manifest source hash drift: {source}", errors)
    required_sources = {
        "synodic_seed_families.json",
        "synodic_cycles.py",
        "chart_conventions.py",
        "wheel_lib.py",
        "america.py",
        "america_ephemeris.json",
        "chart_calculator.py",
        "reading_engine.py",
        "build_saturn_neptune_conjunction_persona.py",
        "PERSONA_CHARTS_CLEAN_METHOD_REFERENCE.md",
    }
    check(
        required_sources
        <= {Path(path).name for path in manifest.get("source_sha256", {})},
        "manifest source inventory incomplete",
        errors,
    )
    code_hashes = manifest.get("package_code_sha256", {})
    for path in (BUILDER_PATH, Path(__file__).resolve()):
        check(str(path) in code_hashes, f"manifest code hash omits {path.name}", errors)
        if str(path) in code_hashes:
            check(code_hashes[str(path)] == sha256(path), f"package code hash drift: {path.name}", errors)
    runtime = manifest.get("runtime", {})
    check(
        runtime.get("ephemeris_boundary")
        == "actual returned flags govern; no independent-Swiss claim",
        "manifest ephemeris boundary missing",
        errors,
    )


def validate_package() -> list[str]:
    errors: list[str] = []
    for path in (INDEX_PATH, HUB_PATH, MANIFEST_PATH, BUILDER_PATH):
        check(path.exists(), f"required package file missing: {path}", errors)
    if errors:
        return errors
    registry = SYNODIC.load_seed_registry(REGISTRY_PATH)
    registry_validation = SYNODIC.validate_seed_registry(registry)
    check(registry_validation["ok"], f"live registry fails: {registry_validation['errors']}", errors)
    check(len(registry["cycles"]) == 10, "live registry cycle count drift", errors)
    check(registry_validation["pass_count"] == 20, "live registry pass count drift", errors)
    index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    check(
        index.get("schema") == "freedom250.long-clock-persona-index/v1",
        "index schema mismatch",
        errors,
    )
    check(index.get("cycle_count") == 10, "index cycle count mismatch", errors)
    check(
        index.get("pass_count_in_complete_rosters") == 20,
        "index roster pass count mismatch",
        errors,
    )
    indexed = {row["cycle_id"]: row for row in index.get("cycles", [])}
    expected = {row["cycle_id"] for row in registry["cycles"]}
    check(set(indexed) == expected, "index/live cycle identities differ", errors)
    for cycle in registry["cycles"]:
        if cycle["cycle_id"] in indexed:
            validate_cycle(cycle, indexed[cycle["cycle_id"]], errors)
    for row in index.get("cycles", []):
        for kind, relative in row["artifacts"].items():
            path = HERE / relative
            check(path.exists(), f"index artifact link missing: {relative}", errors)
            if path.exists():
                check(
                    sha256(path) == row["sha256"][kind],
                    f"index artifact hash drift: {relative}",
                    errors,
                )
                if path.suffix == ".svg":
                    text = path.read_text(encoding="utf-8")
                    check(text.startswith("<svg") and text.rstrip().endswith("</svg>"), f"invalid SVG: {relative}", errors)
    validate_hub(index, errors)
    validate_manifest(manifest, errors)
    return errors


def generated_hashes() -> dict[str, str]:
    paths = [MANIFEST_PATH, INDEX_PATH, HUB_PATH]
    paths.extend(sorted(DATA_DIR.glob("*.json")))
    paths.extend(sorted(CHARTS_DIR.glob("*.svg")))
    return {str(path.relative_to(HERE)): sha256(path) for path in paths}


def rebuild(errors: list[str]) -> None:
    snapshots = []
    for run in range(2):
        result = subprocess.run(
            [sys.executable, "-B", str(BUILDER_PATH)],
            cwd=HERE,
            capture_output=True,
            text=True,
            timeout=180,
            check=False,
        )
        check(
            result.returncode == 0,
            f"determinism build {run + 1} failed: {result.stderr[-2000:]}",
            errors,
        )
        if result.returncode != 0:
            return
        snapshots.append(generated_hashes())
    check(
        snapshots[0] == snapshots[1],
        "two consecutive builds produced different generated hashes",
        errors,
    )
    if snapshots[0] != snapshots[1]:
        all_names = sorted(set(snapshots[0]) | set(snapshots[1]))
        for name in all_names:
            if snapshots[0].get(name) != snapshots[1].get(name):
                errors.append(f"nondeterministic output: {name}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--rebuild",
        action="store_true",
        help="Opt in to two persistent package rebuilds and compare their hashes.",
    )
    args = parser.parse_args()
    errors = validate_package()
    if not errors and args.rebuild:
        rebuild(errors)
        if not errors:
            errors.extend(validate_package())
    if errors:
        print(f"FAIL long-clock-personas: {len(errors)} error(s)")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    print(
        "PASS long-clock-personas: "
        f"{index['cycle_count']} anchors / "
        f"{index['pass_count_in_complete_rosters']} governed family passes / "
        f"{len(manifest['outputs_sha256'])} hashed outputs / "
        "0 errors"
        + (" / deterministic x2" if args.rebuild else "")
    )


if __name__ == "__main__":
    main()
