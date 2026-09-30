#!/usr/bin/env python3
"""Fail-closed validation for the Saturn-Neptune 2026 persona pilot."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import swisseph as swe


HERE = Path(__file__).resolve().parent
CHARTS = HERE / "charts"
DATA_PATH = HERE / "SATURN_NEPTUNE_2026_CONJUNCTION_PERSONA.json"
MANIFEST_PATH = CHARTS / "conjunction_persona_manifest.json"
BUILDER_PATH = HERE / "build_saturn_neptune_conjunction_persona.py"
README_PATH = HERE / "README.md"
HEARING_PATH = HERE / "SATURN_NEPTUNE_2026_PERSONA_HEARING.md"
GALLERY_PATH = CHARTS / "Saturn–Neptune 2026 — Conjunction Persona Gallery.html"
STANDALONE_PATH = CHARTS / "Saturn–Neptune 2026 — Conjunction Persona — Standalone.svg"
BIWHEEL_PATH = CHARTS / "Saturn–Neptune 2026 — Conjunction Persona + Radix — Biwheel.svg"
VAULT = Path("Chronicle/")
SEED_REGISTRY = VAULT / "99 - Templates" / "synodic_seed_families.json"
SYNODIC_ENGINE = VAULT / "99 - Templates" / "synodic_cycles.py"
EXPECTED_TARGET = 0.752728085
EXPECTED_SEED = "2026-02-20T16:52:10.880812+00:00"
EXPECTED_PERSONA = "2026-03-21T08:56:41.280458+00:00"
PLANETS = {
    "Sun",
    "Moon",
    "Mercury",
    "Venus",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
    "Pluto",
}
PLANET_ORDER = (
    "Sun",
    "Moon",
    "Mercury",
    "Venus",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
    "Pluto",
)
BODY_CODES = {
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
    "Node": swe.TRUE_NODE,
}
MINOR_POINTS = {"Chiron", "Node", "America"}
HARD_ASPECTS = {"conjunction", "square", "opposition"}
MUNDANE_MAJOR_RULES = (
    ("conjunction", 0.0, 8.0),
    ("sextile", 60.0, 5.0),
    ("square", 90.0, 7.0),
    ("trine", 120.0, 7.0),
    ("opposition", 180.0, 8.0),
)
HUBER_ANGLE_RULES = (
    ("conjunction", 0.0),
    ("opposition", 180.0),
    ("trine", 120.0),
    ("square", 90.0),
    ("sextile", 60.0),
    ("quincunx", 150.0),
    ("semisextile", 30.0),
)
HUBER_CLASS = {
    "Sun": 0,
    "Moon": 0,
    "Mercury": 1,
    "Venus": 1,
    "Jupiter": 1,
    "Mars": 2,
    "Saturn": 2,
    "Uranus": 3,
    "Neptune": 3,
    "Pluto": 3,
    "Chiron": 3,
}
HUBER_ORB = {
    "conjunction": (9.0, 7.0, 6.0, 5.0),
    "opposition": (9.0, 7.0, 6.0, 5.0),
    "trine": (8.0, 6.0, 5.0, 4.0),
    "square": (6.0, 5.0, 4.0, 3.0),
    "sextile": (5.0, 4.0, 3.0, 2.0),
    "quincunx": (5.0, 4.0, 3.0, 2.0),
    "semisextile": (3.0, 2.0, 1.5, 1.0),
}
ANGLE_PARTNERS = PLANET_ORDER + ("Chiron",)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def signed_delta(a: float, b: float) -> float:
    return ((a - b + 540.0) % 360.0) - 180.0


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
    from datetime import timedelta

    return datetime(2000, 1, 1, 12, tzinfo=timezone.utc) + timedelta(
        days=jd_ut - 2451545.0
    )


def angular_distance(a: float, b: float) -> float:
    return abs(signed_delta(a, b))


def body_state(jd_ut: float, body: str) -> tuple[float, float]:
    result = swe.calc_ut(
        jd_ut,
        BODY_CODES[body],
        swe.FLG_MOSEPH | swe.FLG_SPEED,
    )[0]
    return result[0] % 360.0, result[3]


def speed_root(jd_lo: float, jd_hi: float, body: str) -> float:
    speed_lo = body_state(jd_lo, body)[1]
    speed_hi = body_state(jd_hi, body)[1]
    if speed_lo * speed_hi > 0.0:
        raise RuntimeError(f"speed root not bracketed for {body}")
    for _ in range(90):
        mid = (jd_lo + jd_hi) / 2.0
        speed_mid = body_state(mid, body)[1]
        if speed_lo * speed_mid <= 0.0:
            jd_hi = mid
            speed_hi = speed_mid
        else:
            jd_lo = mid
            speed_lo = speed_mid
    return (jd_lo + jd_hi) / 2.0


def independent_station_events(
    start_jd: float, end_jd: float, bodies: tuple[str, ...]
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for body in bodies:
        prior_jd = start_jd
        prior_speed = body_state(prior_jd, body)[1]
        while prior_jd < end_jd:
            current_jd = min(prior_jd + 0.125, end_jd)
            current_speed = body_state(current_jd, body)[1]
            if prior_speed * current_speed < 0.0:
                root_jd = speed_root(prior_jd, current_jd, body)
                before = body_state(root_jd - 1.0 / 1440.0, body)[1]
                after = body_state(root_jd + 1.0 / 1440.0, body)[1]
                longitude = body_state(root_jd, body)[0]
                rows.append(
                    {
                        "body": body,
                        "utc": jd_to_utc(root_jd),
                        "longitude": longitude,
                        "direction_before": "direct" if before > 0 else "retrograde",
                        "direction_after": "direct" if after > 0 else "retrograde",
                    }
                )
            prior_jd = current_jd
            prior_speed = current_speed
    return sorted(rows, key=lambda row: row["utc"])


def independent_major_aspects(
    positions: dict[str, float],
) -> dict[tuple[str, str], dict[str, Any]]:
    output: dict[tuple[str, str], dict[str, Any]] = {}
    for index, body_a in enumerate(PLANET_ORDER):
        for body_b in PLANET_ORDER[index + 1 :]:
            separation = angular_distance(positions[body_a], positions[body_b])
            aspect, angle, limit = min(
                MUNDANE_MAJOR_RULES,
                key=lambda row: abs(separation - row[1]),
            )
            orb = abs(separation - angle)
            if orb <= limit:
                output[tuple(sorted((body_a, body_b)))] = {
                    "aspect": aspect,
                    "orb_deg": orb,
                }
    return output


def load_module(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate_links(errors: list[str]) -> None:
    html = GALLERY_PATH.read_text(encoding="utf-8")
    local_refs = re.findall(r'(?:src|href)="([^"]+)"', html)
    for ref in local_refs:
        if ref.startswith(("http://", "https://", "#")):
            continue
        target = (GALLERY_PATH.parent / ref).resolve()
        check(target.exists(), f"gallery link is missing: {ref}", errors)


def validate_manifest(data: dict[str, Any], manifest: dict[str, Any], errors: list[str]) -> None:
    check(manifest.get("status") == data.get("status"), "manifest status drift", errors)
    check(
        manifest.get("review_status") == "awaiting_katie_review",
        "manifest review status is not awaiting Katie",
        errors,
    )
    check(
        manifest.get("review_disposition") is None,
        "manifest must not infer a Katie disposition",
        errors,
    )
    output_paths = {
        DATA_PATH.name: DATA_PATH,
        GALLERY_PATH.name: GALLERY_PATH,
        STANDALONE_PATH.name: STANDALONE_PATH,
        BIWHEEL_PATH.name: BIWHEEL_PATH,
        BUILDER_PATH.name: BUILDER_PATH,
    }
    for name, expected_hash in manifest.get("sha256", {}).items():
        path = output_paths.get(name)
        check(path is not None, f"manifest hashes unknown output: {name}", errors)
        if path is not None:
            check(path.exists(), f"manifest output is missing: {path}", errors)
            if path.exists():
                check(sha256(path) == expected_hash, f"output hash drift: {name}", errors)
    check(
        set(output_paths) == set(manifest.get("sha256", {})),
        "manifest output hash inventory is incomplete or excessive",
        errors,
    )
    for source, expected_hash in manifest.get("source_sha256", {}).items():
        path = Path(source)
        check(path.exists(), f"source dependency is missing: {path}", errors)
        if path.exists():
            check(sha256(path) == expected_hash, f"source hash drift: {path}", errors)
    source_names = {Path(path).name for path in manifest.get("source_sha256", {})}
    for required in {
        "synodic_seed_families.json",
        "synodic_cycles.py",
        "chart_conventions.py",
        "PERSONA_CHARTS_CLEAN_METHOD_REFERENCE.md",
        "Mundane Astrology — Master Reference.md",
        "chart_calculator.py",
        "reading_engine.py",
        "wheel_lib.py",
        "america.py",
        "america_ephemeris.json",
    }:
        check(required in source_names, f"source hash inventory omits {required}", errors)
    runtime = manifest.get("runtime", {})
    check(bool(runtime.get("pyswisseph")), "runtime lacks pyswisseph version", errors)
    check(
        runtime.get("persona_primary_solver") == "solcross_ut with FLG_SWIEPH",
        "primary persona solver provenance drift",
        errors,
    )


def validate_seed_authority(data: dict[str, Any], errors: list[str]) -> None:
    engine = load_module(SYNODIC_ENGINE, "f250_persona_validator_synodic")
    registry = engine.load_seed_registry(SEED_REGISTRY)
    validation = engine.validate_seed_registry(registry)
    check(validation["ok"], f"live seed registry fails: {validation['errors']}", errors)
    cycles = [row for row in registry["cycles"] if row["cycle_id"] == "saturn-neptune"]
    check(len(cycles) == 1, "live registry does not have one Saturn-Neptune cycle", errors)
    if len(cycles) != 1:
        return
    cycle = cycles[0]
    check(cycle["pair"] == ["Saturn", "Neptune"], "governed pair drift", errors)
    check(cycle["seed_family_id"] == "saturn-neptune-2026", "seed family drift", errors)
    check(
        cycle["display_anchor_pass_id"] == "saturn-neptune-20260220-p1",
        "display anchor drift",
        errors,
    )
    check(len(cycle["passes"]) == 1, "Saturn-Neptune pass count drift", errors)
    anchor = cycle["passes"][0]
    check(anchor["utc"] == EXPECTED_SEED, "governed seed UTC drift", errors)
    check(abs(anchor["longitude_deg"] - EXPECTED_TARGET) < 1e-12, "target drift", errors)
    canonical = engine.seed_chart(
        "saturn-neptune",
        "saturn-neptune-20260220-p1",
        vault_root=VAULT,
        seed_registry_path=SEED_REGISTRY,
    )
    comparison = data["radix"]["verification"]["canonical_seed_chart_comparison"]
    radix = data["radix"]
    check(canonical["utc"] == radix["event"]["utc"], "canonical seed UTC mismatch", errors)
    recomputed = {
        "asc": abs(signed_delta(canonical["asc"], radix["frame"]["asc"])) * 3600.0,
        "mc": abs(signed_delta(canonical["mc"], radix["frame"]["mc"])) * 3600.0,
        "planets": {
            body: abs(
                signed_delta(
                    canonical["positions"][body]["lon"],
                    radix["positions"][body]["longitude"],
                )
            )
            * 3600.0
            for body in PLANET_ORDER
        },
    }
    deltas = [recomputed["asc"], recomputed["mc"]]
    deltas.extend(recomputed["planets"].values())
    check(max(deltas) <= 0.01, "serialized radix disagrees with canonical seed by >0.01 arcsec", errors)
    check(
        abs(recomputed["asc"] - comparison["asc_delta_arcseconds"]) <= 0.00001,
        "stored ASC comparison receipt disagrees with recomputation",
        errors,
    )
    check(
        abs(recomputed["mc"] - comparison["mc_delta_arcseconds"]) <= 0.00001,
        "stored MC comparison receipt disagrees with recomputation",
        errors,
    )
    for body in PLANET_ORDER:
        check(
            abs(
                recomputed["planets"][body]
                - comparison["planet_delta_arcseconds"][body]
            )
            <= 0.00001,
            f"stored {body} comparison receipt disagrees with recomputation",
            errors,
        )


def validate_exactness(data: dict[str, Any], errors: list[str]) -> None:
    radix = data["radix"]
    persona = data["persona"]
    check(radix["event"]["utc"] == EXPECTED_SEED, "serialized seed UTC drift", errors)
    check(persona["event"]["utc"] == EXPECTED_PERSONA, "serialized persona UTC drift", errors)
    check(abs(radix["target_longitude"] - EXPECTED_TARGET) < 1e-12, "serialized target drift", errors)
    seed_moment = datetime.fromisoformat(radix["event"]["utc"])
    persona_moment = datetime.fromisoformat(persona["event"]["utc"])
    check(persona_moment > seed_moment, "persona is not later than seed", errors)
    check(0 < persona["days_after_radix"] < 370, "persona is not first-year later solar contact", errors)
    seed_jd = jd_of(seed_moment)
    saturn = swe.calc_ut(seed_jd, swe.SATURN, swe.FLG_MOSEPH | swe.FLG_SPEED)[0][0]
    neptune = swe.calc_ut(seed_jd, swe.NEPTUNE, swe.FLG_MOSEPH | swe.FLG_SPEED)[0][0]
    check(abs(signed_delta(saturn, neptune)) * 3600 < 0.01, "seed is not exact Saturn-Neptune conjunction", errors)
    persona_jd = jd_of(persona_moment)
    sun = swe.calc_ut(persona_jd, swe.SUN, swe.FLG_SWIEPH | swe.FLG_SPEED)[0][0]
    check(abs(signed_delta(sun, EXPECTED_TARGET)) * 3600 < 0.01, "persona Sun misses target", errors)
    check(
        abs(persona["verification"]["sun_minus_target_arcseconds"]) < 0.01,
        "stored persona residual exceeds 0.01 arcsec",
        errors,
    )
    check(
        persona["verification"]["swiss_solcross_vs_moshier_bisection_seconds"] < 0.1,
        "independent persona solvers differ by >=0.1 seconds",
        errors,
    )


def validate_boundaries(data: dict[str, Any], errors: list[str]) -> None:
    check(data.get("schema") == "freedom250.deep-current-conjunction-persona/v1", "data schema drift", errors)
    check(data.get("status") == "research_only_not_adopted", "data is not research-only", errors)
    check(data.get("review_status") == "awaiting_katie_review", "data review status drift", errors)
    check(data.get("review_disposition") is None, "data infers a Katie disposition", errors)
    boundary = data["evidence_boundary"]
    check(boundary["admission"] == "conditional_subordinate_zero_vote", "admission drift", errors)
    check(boundary["timing_authority"] is False, "persona gained timing authority", errors)
    check(boundary["event_proof"] is False, "persona gained event-proof status", errors)
    check(boundary["one_shared_chart"] is True, "one-chart rule drift", errors)
    check(boundary["focal_lenses"] == ["Saturn", "Neptune"], "focal lenses drift", errors)
    check(data["seed_family"]["pass_count"] == 1, "serialized seed pass count drift", errors)
    check(data["seed_family"]["independent_verification_status"] == "astro_gold_pending", "external verification status drift", errors)
    check(data["settings"]["houses"] == "Whole Sign", "house-system drift", errors)
    check(data["settings"]["rulers"] == "traditional", "ruler-policy drift", errors)
    check(data["settings"]["node"] == "true", "node-policy drift", errors)
    for chart_name in ("radix", "persona"):
        chart = data[chart_name]
        check("SNode" in chart["positions"], f"{chart_name} omits SNode", errors)
        check("america_916" in chart["minor_points"], f"{chart_name} omits 916 America", errors)
        policy = chart["minor_point_policy"]
        check(policy["point_to_point"] is False, f"{chart_name} permits point-to-point aspects", errors)
        for row in chart["mundane_major_aspects"]:
            check(row["a"] in PLANETS and row["b"] in PLANETS, f"{chart_name} major lane contains nonplanet", errors)
        for row in chart["minor_point_aspects"]:
            check(row["a"] in MINOR_POINTS, f"{chart_name} minor lane source is not a minor point", errors)
            check(row["b"] in PLANETS, f"{chart_name} minor lane target is not a planet", errors)
            check(row["aspect"] in HARD_ASPECTS, f"{chart_name} minor lane contains flowing aspect", errors)
            check(row["orb_deg"] <= 2.0, f"{chart_name} minor lane exceeds 2 degrees", errors)
    for row in data["radix_persona_overlay"]["contacts"]:
        check(row["orb_deg"] <= 2.0, "radix-persona overlay exceeds 2 degrees", errors)
        if row["persona_factor"] in MINOR_POINTS:
            check(
                row["radix_factor"] in PLANETS,
                f"persona {row['persona_factor']} overlays a nonplanet",
                errors,
            )
            check(
                row["aspect"] in HARD_ASPECTS,
                f"persona {row['persona_factor']} has a nonhard overlay",
                errors,
            )
        if row["radix_factor"] in MINOR_POINTS:
            check(
                row["persona_factor"] in PLANETS,
                f"radix {row['radix_factor']} overlays a nonplanet",
                errors,
            )
            check(
                row["aspect"] in HARD_ASPECTS,
                f"radix {row['radix_factor']} has a nonhard overlay",
                errors,
            )
    mc_uranus = [
        row
        for row in data["radix_persona_overlay"]["contacts"]
        if row["persona_factor"] == "MC" and row["radix_factor"] == "Uranus"
    ]
    check(len(mc_uranus) == 1, "expected one persona-MC/radix-Uranus overlay", errors)
    if len(mc_uranus) == 1:
        check(
            mc_uranus[0]["dependency_class"]
            == "dependent_correlated_overlay_zero_vote",
            "persona-MC/radix-Uranus is not dependency-labeled",
            errors,
        )


def validate_change_gate(data: dict[str, Any], errors: list[str]) -> None:
    gate = data.get("seed_to_persona_change_gate", {})
    check(
        "carryover, not a finding" in gate.get("rule", ""),
        "slow-body carryover rule is missing",
        errors,
    )
    check(
        gate.get("outer_planets") == ["Uranus", "Neptune", "Pluto"],
        "outer-planet taxonomy drift",
        errors,
    )
    seed_jd = jd_of(datetime.fromisoformat(data["radix"]["event"]["utc"]))
    persona_jd = jd_of(datetime.fromisoformat(data["persona"]["event"]["utc"]))
    tracked = ("Mercury", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto")
    independent_stations = independent_station_events(seed_jd, persona_jd, tracked)
    serialized_stations = sorted(
        gate.get("station_events_between", []),
        key=lambda row: row["utc"],
    )
    check(
        len(independent_stations) == len(serialized_stations) == 3,
        "station-event count disagrees with independent speed-root scan",
        errors,
    )
    for computed, stored in zip(independent_stations, serialized_stations):
        check(computed["body"] == stored["body"], "station body drift", errors)
        check(
            computed["direction_before"] == stored["direction_before"]
            and computed["direction_after"] == stored["direction_after"],
            f"{computed['body']} station direction drift",
            errors,
        )
        stored_utc = datetime.fromisoformat(stored["utc"])
        check(
            abs((computed["utc"] - stored_utc).total_seconds()) < 0.1,
            f"{computed['body']} station time differs from independent root",
            errors,
        )
        check(
            angular_distance(computed["longitude"], stored["longitude"]) * 3600.0
            < 0.01,
            f"{computed['body']} station longitude drift",
            errors,
        )
        independent_hours = (persona_jd - jd_of(computed["utc"])) * 24.0
        check(
            abs(independent_hours - stored["hours_before_persona"]) < 0.0001,
            f"{computed['body']} hours-before-persona drift",
            errors,
        )

    computed_station_bodies = {row["body"] for row in independent_stations}
    slow_bodies = ("Jupiter", "Saturn", "Uranus", "Neptune", "Pluto")
    check(
        gate.get("tracked_slow_bodies") == list(slow_bodies),
        "serialized tracked slow-body roster or order drift",
        errors,
    )
    check(
        gate.get("outer_planets") == ["Uranus", "Neptune", "Pluto"],
        "serialized outer-planet taxonomy drift",
        errors,
    )
    independent_sign_changes: list[str] = []
    for body in slow_bodies:
        signs: set[int] = set()
        probe = seed_jd
        while probe <= persona_jd:
            signs.add(int(body_state(probe, body)[0] // 30))
            probe += 0.125
        signs.add(int(body_state(persona_jd, body)[0] // 30))
        if len(signs) > 1:
            independent_sign_changes.append(body)
    check(independent_sign_changes == [], "independent scan found a slow-body sign change", errors)
    check(gate.get("slow_body_sign_changes") == [], "serialized slow-body sign changes drift", errors)
    carryover = gate.get("slow_body_carryover", {})
    for body in slow_bodies:
        row = carryover.get(body, {})
        check(
            row.get("stationed_between") == (body in computed_station_bodies),
            f"{body} serialized station flag disagrees with scan",
            errors,
        )
        check(row.get("changed_sign") is False, f"{body} serialized sign flag drift", errors)

    seed_positions = {
        body: body_state(seed_jd, body)[0]
        for body in PLANET_ORDER + ("Node",)
    }
    persona_positions = {
        body: body_state(persona_jd, body)[0]
        for body in PLANET_ORDER + ("Node",)
    }
    _cusps, ascmc = swe.houses_ex(
        persona_jd,
        float(data["persona"]["event"]["latitude"]),
        float(data["persona"]["event"]["longitude"]),
        b"W",
        swe.FLG_SWIEPH | swe.FLG_SPEED,
    )
    mc_uranus_orb = abs(
        angular_distance(float(ascmc[1]), persona_positions["Uranus"]) - 180.0
    )
    saturn_pluto_seed_orb = abs(
        angular_distance(seed_positions["Saturn"], seed_positions["Pluto"]) - 60.0
    )
    saturn_pluto_persona_orb = abs(
        angular_distance(persona_positions["Saturn"], persona_positions["Pluto"])
        - 60.0
    )
    saturn_uranus_seed_orb = abs(
        angular_distance(seed_positions["Saturn"], seed_positions["Uranus"]) - 60.0
    )
    saturn_uranus_persona_orb = abs(
        angular_distance(persona_positions["Saturn"], persona_positions["Uranus"])
        - 60.0
    )
    mars_jupiter_orb = abs(
        angular_distance(persona_positions["Mars"], persona_positions["Jupiter"])
        - 120.0
    )
    future_mars = body_state(persona_jd + 1.0 / 24.0, "Mars")[0]
    future_jupiter = body_state(persona_jd + 1.0 / 24.0, "Jupiter")[0]
    mars_jupiter_applying = (
        abs(angular_distance(future_mars, future_jupiter) - 120.0)
        < mars_jupiter_orb
    )
    mercury_node_orb = angular_distance(
        persona_positions["Mercury"], persona_positions["Node"]
    )
    venus_jupiter_seed_orb = abs(
        angular_distance(seed_positions["Venus"], seed_positions["Jupiter"])
        - 120.0
    )
    venus_jupiter_persona_orb = abs(
        angular_distance(persona_positions["Venus"], persona_positions["Jupiter"])
        - 90.0
    )

    changes = {
        row.get("factor"): row
        for row in gate.get("promoted_question_relevant_changes", [])
    }
    for factor in {
        "Jupiter",
        "Mercury",
        "persona MC and Uranus",
        "Saturn and Pluto",
        "Saturn and Uranus",
        "Venus and Jupiter",
    }:
        check(factor in changes, f"promoted change list omits {factor}", errors)
    if "persona MC and Uranus" in changes:
        row = changes["persona MC and Uranus"]
        check(abs(row["orb_deg"] - mc_uranus_orb) < 0.00001, "MC-Uranus orb is not independently reproduced", errors)
        check(
            row.get("novelty_owner") == "derived_persona_MC_not_uranus_near_return",
            "MC-Uranus novelty owner drift",
            errors,
        )
        check(
            row.get("classification")
            == "potentially_additive_derived_relation_zero_vote",
            "MC-Uranus classification drift",
            errors,
        )
    if "Saturn and Pluto" in changes:
        row = changes["Saturn and Pluto"]
        check(abs(row["seed_mundane_orb_deg"] - saturn_pluto_seed_orb) < 0.00001, "seed Saturn-Pluto orb drift", errors)
        check(abs(row["persona_huber_orb_deg"] - round(saturn_pluto_persona_orb, 2)) < 0.00001, "persona Saturn-Pluto Huber orb drift", errors)
        check(saturn_pluto_seed_orb > 3.0 and saturn_pluto_persona_orb < 2.0, "Saturn-Pluto Huber entry is not reproduced", errors)
        check(
            row.get("classification")
            == "tightness_change_not_a_new_outer_return_vote",
            "Saturn-Pluto classification drift",
            errors,
        )
    if "Saturn and Uranus" in changes:
        row = changes["Saturn and Uranus"]
        check(abs(row["seed_mundane_orb_deg"] - saturn_uranus_seed_orb) < 0.00001, "seed Saturn-Uranus orb drift", errors)
        check(abs(row["persona_sextile_orb_deg"] - saturn_uranus_persona_orb) < 0.00001, "persona Saturn-Uranus orb drift", errors)
        check(saturn_uranus_seed_orb <= 5.0 < saturn_uranus_persona_orb, "Saturn-Uranus lane exit is not reproduced", errors)
        check(
            row.get("classification") == "relationship_admission_change_zero_vote",
            "Saturn-Uranus classification drift",
            errors,
        )
    if "Jupiter" in changes:
        row = changes["Jupiter"]
        check(abs(row["related_persona_contact"]["orb_deg"] - mars_jupiter_orb) < 0.00001, "Mars-Jupiter orb drift", errors)
        check(
            row["related_persona_contact"].get("applying")
            == mars_jupiter_applying,
            "Mars-Jupiter applying status drift",
            errors,
        )
        check(
            row.get("classification")
            == "potentially_additive_condition_change_zero_vote",
            "Jupiter classification drift",
            errors,
        )
        check(
            row.get("station", {}).get("utc")
            in {item["utc"] for item in serialized_stations if item["body"] == "Jupiter"},
            "Jupiter promoted station is not the validated station event",
            errors,
        )
    if "Mercury" in changes:
        row = changes["Mercury"]
        check(abs(row["related_persona_contact"]["orb_deg"] - mercury_node_orb) < 0.00001, "Mercury-Node orb drift", errors)
        check(
            row["related_persona_contact"].get("point_status")
            == "nonacting_minor_point",
            "Mercury-Node point status drift",
            errors,
        )
        check(
            row.get("classification")
            == "potentially_additive_condition_change_zero_vote",
            "Mercury classification drift",
            errors,
        )
        check(
            row.get("station", {}).get("utc")
            in {
                item["utc"]
                for item in serialized_stations
                if item["body"] == "Mercury"
                and item["direction_after"] == "direct"
            },
            "Mercury promoted station is not the validated direct station",
            errors,
        )
    if "Venus and Jupiter" in changes:
        row = changes["Venus and Jupiter"]
        check(abs(row["seed_trine_orb_deg"] - venus_jupiter_seed_orb) < 0.00001, "seed Venus-Jupiter orb drift", errors)
        check(abs(row["persona_square_orb_deg"] - venus_jupiter_persona_orb) < 0.00001, "persona Venus-Jupiter orb drift", errors)
        check(
            row.get("classification")
            == "question_relevant_counterweight_fast_partner_driven_zero_vote",
            "Venus-Jupiter classification drift",
            errors,
        )

    ledger = gate.get("relationship_deltas", {})
    for key in (
        "mundane_major_ten_planet",
        "huber_source_plus_katie_chiron_overlay",
        "nonacting_minor_point",
        "persona_derived_angle_relationships",
    ):
        check(isinstance(ledger.get(key), list), f"relationship delta ledger omits {key}", errors)
    check(
        "selective, not exhaustive" in gate.get("promotion_rule", ""),
        "promotion selection is not explicitly bounded",
        errors,
    )
    serialized_angles = ledger.get("persona_derived_angle_relationships", [])
    check(
        serialized_angles == data["persona"].get("angle_aspects"),
        "derived-angle delta ledger is not identical to the persona angle lane",
        errors,
    )
    expected_angles: list[dict[str, Any]] = []
    point_longitudes = {"ASC": float(ascmc[0]), "MC": float(ascmc[1])}
    for point, point_longitude in point_longitudes.items():
        for body in ANGLE_PARTNERS:
            if body in persona_positions:
                body_longitude = persona_positions[body]
            else:
                body_longitude = float(
                    data["persona"]["positions"][body]["longitude"]
                )
            separation = angular_distance(point_longitude, body_longitude)
            for aspect, angle in HUBER_ANGLE_RULES:
                allowed = HUBER_ORB[aspect][HUBER_CLASS[body]]
                orb = abs(separation - angle)
                if orb <= allowed:
                    expected_angles.append(
                        {
                            "point": point,
                            "planet": body,
                            "aspect": aspect,
                            "orb_deg": round(orb, 6),
                            "orb_limit_deg": allowed,
                            "near_exact": orb <= 1.0,
                            "authority": (
                                "Katie angle overlay; partner planet Huber allowance"
                            ),
                        }
                    )
                    break
    expected_angles.sort(key=lambda row: row["orb_deg"])
    check(
        serialized_angles == expected_angles,
        "derived-angle delta ledger differs from independent angle reconstruction",
        errors,
    )
    independent_seed_major = independent_major_aspects(seed_positions)
    independent_persona_major = independent_major_aspects(persona_positions)
    stored_major = {
        tuple(row["pair"]): row
        for row in ledger.get("mundane_major_ten_planet", [])
    }
    expected_pairs = set(independent_seed_major) | set(independent_persona_major)
    check(
        set(stored_major) == expected_pairs,
        "mundane relationship-delta ledger is not the complete independent union",
        errors,
    )
    for pair in expected_pairs & set(stored_major):
        stored = stored_major[pair]
        seed_row = independent_seed_major.get(pair)
        persona_row = independent_persona_major.get(pair)
        if seed_row is None:
            expected_change = "gained"
        elif persona_row is None:
            expected_change = "lost"
        elif seed_row["aspect"] != persona_row["aspect"]:
            expected_change = "operator_changed"
        else:
            expected_change = "persisted_with_condition_change"
        check(stored["change"] == expected_change, f"{pair} delta classification drift", errors)
        for label, computed, serialized in (
            ("seed", seed_row, stored.get("seed")),
            ("persona", persona_row, stored.get("persona")),
        ):
            check((computed is None) == (serialized is None), f"{pair} {label} admission drift", errors)
            if computed is not None and serialized is not None:
                check(computed["aspect"] == serialized["aspect"], f"{pair} {label} operator drift", errors)
                check(abs(computed["orb_deg"] - serialized["orb_deg"]) < 0.00001, f"{pair} {label} orb drift", errors)

    def validate_serialized_lane(
        ledger_key: str,
        chart_key: str,
    ) -> None:
        def chart_index(chart_name: str) -> dict[tuple[str, str], dict[str, Any]]:
            return {
                tuple(sorted((row["a"], row["b"]))): {
                    "aspect": row.get("aspect", row.get("type")),
                    "orb_deg": row.get("orb_deg", row.get("orb")),
                }
                for row in data[chart_name][chart_key]
            }

        seed_lane = chart_index("radix")
        persona_lane = chart_index("persona")
        stored_lane = {
            tuple(row["pair"]): row
            for row in ledger.get(ledger_key, [])
        }
        union = set(seed_lane) | set(persona_lane)
        check(
            set(stored_lane) == union,
            f"{ledger_key} is not the complete admitted union",
            errors,
        )
        for pair in union & set(stored_lane):
            seed_row = seed_lane.get(pair)
            persona_row = persona_lane.get(pair)
            row = stored_lane[pair]
            if seed_row is None:
                expected_change = "gained"
            elif persona_row is None:
                expected_change = "lost"
            elif seed_row["aspect"] != persona_row["aspect"]:
                expected_change = "operator_changed"
            else:
                expected_change = "persisted_with_condition_change"
            check(
                row["change"] == expected_change,
                f"{ledger_key} {pair} delta classification drift",
                errors,
            )
            for label, computed, serialized in (
                ("seed", seed_row, row.get("seed")),
                ("persona", persona_row, row.get("persona")),
            ):
                check(
                    (computed is None) == (serialized is None),
                    f"{ledger_key} {pair} {label} admission drift",
                    errors,
                )
                if computed is not None and serialized is not None:
                    check(
                        computed["aspect"] == serialized["aspect"],
                        f"{ledger_key} {pair} {label} operator drift",
                        errors,
                    )
                    check(
                        abs(computed["orb_deg"] - serialized["orb_deg"])
                        < 0.00001,
                        f"{ledger_key} {pair} {label} orb drift",
                        errors,
                    )

    validate_serialized_lane(
        "huber_source_plus_katie_chiron_overlay",
        "huber_aspects",
    )
    validate_serialized_lane(
        "nonacting_minor_point",
        "minor_point_aspects",
    )


def generated_hashes() -> dict[str, str]:
    return {
        path.name: sha256(path)
        for path in (
            DATA_PATH,
            STANDALONE_PATH,
            BIWHEEL_PATH,
            GALLERY_PATH,
            MANIFEST_PATH,
        )
    }


def rebuild(errors: list[str]) -> None:
    runs: list[dict[str, str]] = []
    for run_number in (1, 2):
        result = subprocess.run(
            [sys.executable, "-B", str(BUILDER_PATH)],
            cwd=HERE.parent.parent,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        check(
            result.returncode == 0,
            f"determinism rebuild {run_number} failed: {result.stderr[:500]}",
            errors,
        )
        if result.returncode != 0:
            return
        runs.append(generated_hashes())
    check(runs[0] == runs[1], "two consecutive rebuild hash sets differ", errors)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--rebuild",
        action="store_true",
        help="Opt in to two persistent package rebuilds and compare their hashes.",
    )
    args = parser.parse_args()
    errors: list[str] = []
    required = [
        README_PATH,
        HEARING_PATH,
        DATA_PATH,
        MANIFEST_PATH,
        BUILDER_PATH,
        Path(__file__),
        GALLERY_PATH,
        STANDALONE_PATH,
        BIWHEEL_PATH,
    ]
    for path in required:
        check(path.exists(), f"required artifact is missing: {path}", errors)
    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return 1

    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    validate_seed_authority(data, errors)
    validate_exactness(data, errors)
    validate_boundaries(data, errors)
    validate_change_gate(data, errors)
    validate_manifest(data, manifest, errors)
    validate_links(errors)

    gallery_text = GALLERY_PATH.read_text(encoding="utf-8")
    check("EST" in gallery_text, "gallery seed label does not preserve EST", errors)
    check("EDT" in gallery_text, "gallery persona label does not preserve EDT", errors)
    check("UTC-05:00" not in gallery_text, "gallery exposes fixed-offset seed label", errors)
    check("UTC-04:00" not in gallery_text, "gallery exposes fixed-offset persona label", errors)

    for svg in (STANDALONE_PATH, BIWHEEL_PATH):
        text = svg.read_text(encoding="utf-8")
        check(text.startswith("<svg"), f"not an SVG: {svg.name}", errors)
        check(
            'color="#9a917f"' in text,
            f"render omits the wheel library's SNode glyph color: {svg.name}",
            errors,
        )
        check(
            'color="#1d3f8c"' in text,
            f"render omits the wheel library's 916 America glyph color: {svg.name}",
            errors,
        )
        check("EDT" in text, f"render does not preserve EDT: {svg.name}", errors)
        check("UTC-04:00" not in text, f"render exposes fixed offset: {svg.name}", errors)
    builder_text = BUILDER_PATH.read_text(encoding="utf-8")
    check("import make_reading" not in builder_text, "builder imports retired make_reading", errors)

    if args.rebuild and not errors:
        rebuild(errors)

    if errors:
        for error in errors:
            print(f"FAIL {error}")
        print(f"Validation failed with {len(errors)} error(s).")
        return 1
    print("PASS Saturn-Neptune 2026 conjunction persona package")
    print("PASS governed seed identity and live registry validation")
    print("PASS independent exactness checks and canonical seed agreement")
    print("PASS one-chart/two-lens, zero-vote, and minor-point boundaries")
    print("PASS slow-body carryover versus station/sign/relationship change gate")
    print("PASS output/source hashes, links, and wheel content")
    if args.rebuild:
        print("PASS two consecutive rebuilds are byte-identical across 5 generated outputs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
