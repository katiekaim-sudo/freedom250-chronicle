#!/usr/bin/env python3
"""Build factual persona subsidiaries for all ten governed Long Clock anchors.

This builder is intentionally confined to its package.  It creates one shared
persona chart for each governed conjunction pair, keyed to the registry's
display anchor pass, and assigns the two conjunct bodies focal lenses inside
that one zero-vote subsidiary chart.
"""

from __future__ import annotations

import hashlib
import html
import importlib.util
import json
import math
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import swisseph as swe


HERE = Path(__file__).resolve().parent
DATA_DIR = HERE / "data"
CHARTS_DIR = HERE / "charts"
INDEX_PATH = DATA_DIR / "index.json"
HUB_PATH = CHARTS_DIR / "index.html"
MANIFEST_PATH = HERE / "manifest.json"

VAULT = Path("Chronicle/")
TEMPLATES = VAULT / "99 - Templates"
REGISTRY_PATH = TEMPLATES / "synodic_seed_families.json"
SYNODIC_PATH = TEMPLATES / "synodic_cycles.py"
CONVENTIONS_PATH = TEMPLATES / "chart_conventions.py"
WHEEL_PATH = TEMPLATES / "wheel_lib.py"
AMERICA_PATH = TEMPLATES / "america.py"
SENTIENT_SUN = Path("[local-path-removed] Sun")
TRADITIONAL_TABLES_PATH = SENTIENT_SUN / "canonical_traditional_tables.py"
BASE_BUILDER_PATH = HERE.parent / "Persona Pilots" / (
    "Deep Current Persona Charts Saturn-Neptune 2026-08-22/"
    "build_saturn_neptune_conjunction_persona.py"
)
PERSONA_METHOD_PATH = Path(
    "[local-path-removed] General/outputs/"
    "persona_charts_research_2026-07-22/"
    "PERSONA_CHARTS_CLEAN_METHOD_REFERENCE.md"
)


def load_module(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE = load_module(BASE_BUILDER_PATH, "f250_long_clock_persona_base")
SYNODIC = load_module(SYNODIC_PATH, "f250_long_clock_persona_synodic")
CONVENTIONS = load_module(CONVENTIONS_PATH, "f250_long_clock_persona_conventions")
TABLES = load_module(TRADITIONAL_TABLES_PATH, "f250_long_clock_persona_traditional_tables")

calculator = BASE.calculator
structure = BASE.structure
america = BASE.america
WHEEL = BASE.WHEEL
calculator.dignity_label = TABLES.dignity_classification
calculator.dignity_labels = TABLES.dignity_labels

PLACE = str(CONVENTIONS.DC_LABEL)
LATITUDE = float(CONVENTIONS.DC_LAT)
LONGITUDE = float(CONVENTIONS.DC_LON)
ZONE = CONVENTIONS.DC_TZ
SIGNS = tuple(calculator.SIGNS)
PLANET_CODES = dict(BASE.PLANET_CODES)
PLANET_ORDER = tuple(PLANET_CODES)
TRADITIONAL_BODIES = tuple(BASE.TRADITIONAL_BODIES)
TRACKED_CHANGE_BODIES = ("Mercury", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto")
SLOW_BODIES = ("Jupiter", "Saturn", "Uranus", "Neptune", "Pluto")
OUTER_BODIES = ("Uranus", "Neptune", "Pluto")
WHEEL_BODY_ORDER = (
    "Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn",
    "Uranus", "Neptune", "Pluto", "Chiron", "Node", "SNode", "America",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def flag_names(bits: int) -> list[str]:
    names = []
    for name, value in (
        ("FLG_JPLEPH", swe.FLG_JPLEPH),
        ("FLG_SWIEPH", swe.FLG_SWIEPH),
        ("FLG_MOSEPH", swe.FLG_MOSEPH),
        ("FLG_SPEED", swe.FLG_SPEED),
    ):
        if bits & value:
            names.append(name)
    return names


def calc_flag_receipt(jd_ut: float) -> dict[str, Any]:
    requested = swe.FLG_SWIEPH | swe.FLG_SPEED
    returned: dict[str, Any] = {}
    for body, code in PLANET_CODES.items():
        _position, actual = swe.calc_ut(jd_ut, code, requested)
        returned[body] = {
            "bits": int(actual),
            "names": flag_names(int(actual)),
            "fallback_from_requested_swieph": bool(
                (requested & swe.FLG_SWIEPH)
                and not (actual & swe.FLG_SWIEPH)
                and (actual & swe.FLG_MOSEPH)
            ),
        }
    ephe_path = Path(calculator.EPHE_PATH) if calculator.EPHE_PATH else None
    return {
        "requested": {"bits": requested, "names": flag_names(requested)},
        "returned_by_body": returned,
        "all_planets_returned_same_bits": len(
            {row["bits"] for row in returned.values()}
        )
        == 1,
        "fallback_observed": any(
            row["fallback_from_requested_swieph"] for row in returned.values()
        ),
        "ephemeris_path": None if ephe_path is None else str(ephe_path),
        "ephemeris_files": {
            "sepl_18.se1_planets": bool(ephe_path and (ephe_path / "sepl_18.se1").exists()),
            "seas_18.se1_asteroids": bool(ephe_path and (ephe_path / "seas_18.se1").exists()),
        },
        "receipt_boundary": (
            "Returned flags, not requested flags, name the planetary ephemeris. "
            "A Moshier fallback is reported explicitly and is not called an "
            "independent Swiss-file verification."
        ),
    }


def load_registry() -> tuple[dict[str, Any], dict[str, Any]]:
    registry = SYNODIC.load_seed_registry(REGISTRY_PATH)
    if registry.get("schema") != "freedom250.long-clocks.seed-families/v1":
        raise RuntimeError("Unsupported Long Clocks registry schema")
    if registry.get("status") != "active":
        raise RuntimeError("Long Clocks registry is not active")
    validation = SYNODIC.validate_seed_registry(registry)
    if not validation["ok"]:
        raise RuntimeError(f"Long Clocks registry invalid: {validation['errors']}")
    if len(registry["cycles"]) != 10 or validation["pass_count"] != 20:
        raise RuntimeError("Long Clocks registry must govern 10 cycles / 20 passes")
    return registry, validation


def anchor_for(cycle: dict[str, Any]) -> dict[str, Any]:
    matches = [
        row
        for row in cycle["passes"]
        if row["pass_id"] == cycle["display_anchor_pass_id"]
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Anchor identity is not unique for {cycle['cycle_id']}")
    return matches[0]


def verify_seed_root(cycle: dict[str, Any], anchor: dict[str, Any]) -> dict[str, Any]:
    seed_utc = datetime.fromisoformat(anchor["utc"]).astimezone(timezone.utc)
    seed_jd = BASE.jd_of(seed_utc)
    body_a, body_b = cycle["pair"]

    def delta(jd_ut: float) -> float:
        a = BASE.body_state(jd_ut, PLANET_CODES[body_a])[0]
        b = BASE.body_state(jd_ut, PLANET_CODES[body_b])[0]
        return BASE.signed_delta(a, b)

    independent_jd = BASE.bisection(delta, seed_jd - 1.0, seed_jd + 1.0)
    a_lon, a_speed = BASE.body_state(seed_jd, PLANET_CODES[body_a])
    b_lon, b_speed = BASE.body_state(seed_jd, PLANET_CODES[body_b])
    target = float(anchor["longitude_deg"])
    return {
        "seed_utc": seed_utc,
        "seed_jd": seed_jd,
        "target_longitude": target,
        "verification": {
            "independent_root_solver": "Moshier pair-difference bisection",
            "independent_root_utc": BASE.jd_to_utc(independent_jd).isoformat(
                timespec="microseconds"
            ),
            "registry_vs_independent_root_seconds": round(
                abs(independent_jd - seed_jd) * 86400.0, 9
            ),
            "pair_residual_arcseconds": round(
                BASE.angular_distance(a_lon, b_lon) * 3600.0, 12
            ),
            "target_minus_body_arcseconds": {
                body_a: round(BASE.signed_delta(target, a_lon) * 3600.0, 12),
                body_b: round(BASE.signed_delta(target, b_lon) * 3600.0, 12),
            },
            "body_speed_deg_day": {
                body_a: round(a_speed, 12),
                body_b: round(b_speed, 12),
            },
        },
    }


def find_persona_event(seed_jd: float, target: float) -> dict[str, Any]:
    requested = swe.FLG_SWIEPH
    primary_jd = float(swe.solcross_ut(target, seed_jd + 1e-7, requested))
    prior_jd = seed_jd + 1e-7
    prior_delta = BASE.signed_delta(
        BASE.sun_longitude(prior_jd, swe.FLG_MOSEPH), target
    )
    bracket: tuple[float, float] | None = None
    while prior_jd < seed_jd + 370.0:
        current_jd = prior_jd + 0.25
        current_delta = BASE.signed_delta(
            BASE.sun_longitude(current_jd, swe.FLG_MOSEPH), target
        )
        if prior_delta <= 0 <= current_delta and current_delta - prior_delta < 10:
            bracket = (prior_jd, current_jd)
            break
        prior_jd, prior_delta = current_jd, current_delta
    if bracket is None:
        raise RuntimeError("Could not bracket first later solar contact")
    independent_jd = BASE.bisection(
        lambda value: BASE.signed_delta(
            BASE.sun_longitude(value, swe.FLG_MOSEPH), target
        ),
        *bracket,
    )
    event_utc = BASE.jd_to_utc(primary_jd)
    _sun, returned = swe.calc_ut(
        primary_jd, swe.SUN, swe.FLG_SWIEPH | swe.FLG_SPEED
    )
    return {
        "jd_ut": primary_jd,
        "utc": event_utc,
        "local": event_utc.astimezone(ZONE),
        "verification": {
            "definition": "first later geocentric tropical Sun crossing of fixed anchor longitude",
            "primary_solver": "solcross_ut with FLG_SWIEPH requested",
            "primary_requested_flag_bits": int(swe.FLG_SWIEPH),
            "primary_requested_flag_names": ["FLG_SWIEPH"],
            "primary_observed_sun_flag_bits": int(returned),
            "primary_observed_sun_flag_names": flag_names(int(returned)),
            "primary_fallback_observed": bool(
                not (returned & swe.FLG_SWIEPH) and (returned & swe.FLG_MOSEPH)
            ),
            "independent_solver": "quarter-day bracket plus Moshier bisection",
            "independent_bisection_utc": BASE.jd_to_utc(independent_jd).isoformat(
                timespec="microseconds"
            ),
            "root_algorithm_delta_seconds": round(
                abs(primary_jd - independent_jd) * 86400.0, 9
            ),
            "sun_minus_target_arcseconds": round(
                BASE.signed_delta(
                    BASE.sun_longitude(primary_jd, swe.FLG_MOSEPH), target
                )
                * 3600.0,
                12,
            ),
            "independence_boundary": (
                "The two root algorithms are independent. When returned flags "
                "show Moshier fallback, they are not independent ephemerides."
            ),
        },
    }


def america_pair_coverage(seed_utc: datetime, persona_utc: datetime) -> dict[str, Any]:
    global_ok, receipt = america.available()
    checks: dict[str, Any] = {}
    for label, moment in (
        ("seed", seed_utc),
        ("seed_plus_one_hour", seed_utc + timedelta(hours=1)),
        ("persona", persona_utc),
        ("persona_plus_one_hour", persona_utc + timedelta(hours=1)),
    ):
        checks[label] = {
            "utc": moment.isoformat(timespec="microseconds"),
            "longitude_available": america.america_lon(moment) is not None,
            "speed_available": america.america_speed(moment) is not None,
        }
    include = global_ok and all(
        row["longitude_available"] and row["speed_available"]
        for row in checks.values()
    )
    return {
        "include_in_both_charts": include,
        "status": "included_both_endpoints" if include else "unavailable_no_extrapolation",
        "global_cache_receipt": receipt,
        "checks": checks,
        "policy": (
            "916 America is included only when the canonical cache covers both "
            "seed and persona plus the one-hour aspect-motion probes; otherwise "
            "it is unavailable in both charts and is never extrapolated."
        ),
    }


def minor_point_aspects(
    moment_utc: datetime, raw: dict[str, Any], include_america: bool
) -> list[dict[str, Any]]:
    future_utc = moment_utc + timedelta(hours=1)
    jd_ut = BASE.jd_of(moment_utc)
    future_jd = BASE.jd_of(future_utc)
    current_planets = {
        body: BASE.body_state(jd_ut, code)[0] for body, code in PLANET_CODES.items()
    }
    future_planets = {
        body: BASE.body_state(future_jd, code)[0]
        for body, code in PLANET_CODES.items()
    }
    local = future_utc.astimezone(ZONE)
    future_raw = calculator.compute(
        local.year,
        local.month,
        local.day,
        local.hour,
        local.minute,
        LATITUDE,
        LONGITUDE,
        local.utcoffset().total_seconds() / 3600.0,
        seconds=local.second + local.microsecond / 1_000_000.0,
    )
    current_points: dict[str, float] = {
        "Chiron": float(raw["pos"]["Chiron"]["lon"]),
        "Node": float(raw["pos"]["Node"]["lon"]),
    }
    future_points: dict[str, float] = {
        "Chiron": float(future_raw["pos"]["Chiron"]["lon"]),
        "Node": float(future_raw["pos"]["Node"]["lon"]),
    }
    if include_america:
        current_america = america.america_lon(moment_utc)
        future_america = america.america_lon(future_utc)
        if current_america is None or future_america is None:
            raise RuntimeError("Pair-level America coverage promise failed")
        current_points["America"] = current_america
        future_points["America"] = future_america
    rows: list[dict[str, Any]] = []
    for point, point_lon in current_points.items():
        for planet, planet_lon in current_planets.items():
            separation = BASE.angular_distance(point_lon, planet_lon)
            aspect, angle, limit = min(
                BASE.MINOR_POINT_HARD_ASPECTS,
                key=lambda row: abs(separation - row[1]),
            )
            orb = abs(separation - angle)
            if orb > limit:
                continue
            future_orb = abs(
                BASE.angular_distance(future_points[point], future_planets[planet])
                - angle
            )
            rows.append(
                {
                    "a": point,
                    "b": planet,
                    "aspect": aspect,
                    "angle_deg": angle,
                    "orb_deg": round(orb, 6),
                    "orb_limit_deg": limit,
                    "applying": future_orb < orb,
                    "separating": future_orb >= orb,
                    "separation_deg": round(separation, 6),
                    "nonacting_point": point,
                    "authority": "nonacting point-to-planet hard-aspect lane at 2 degrees or less",
                }
            )
    return sorted(rows, key=lambda row: row["orb_deg"])


def calculate_chart(
    moment_utc: datetime, include_america: bool, america_coverage: dict[str, Any]
) -> tuple[dict[str, Any], dict[str, Any]]:
    local = moment_utc.astimezone(ZONE)
    raw = calculator.compute(
        local.year,
        local.month,
        local.day,
        local.hour,
        local.minute,
        LATITUDE,
        LONGITUDE,
        local.utcoffset().total_seconds() / 3600.0,
        seconds=local.second + local.microsecond / 1_000_000.0,
    )
    positions = raw["pos"]
    huber = structure.huber_aspects(positions)
    configurations = structure.configurations(positions, huber)
    asc_index = int(raw["asc"] // 30)
    chart_ruler = structure.RULER[raw["asc_sign"]]
    tenth_sign = SIGNS[(asc_index + 9) % 12]
    tenth_ruler = structure.RULER[tenth_sign]
    mc_ruler = structure.RULER[raw["mc_sign"]]
    houses_ruled: dict[str, list[int]] = {body: [] for body in TRADITIONAL_BODIES}
    for house in range(1, 13):
        sign = SIGNS[(asc_index + house - 1) % 12]
        houses_ruled[structure.RULER[sign]].append(house)
    if include_america:
        america_lon = america.america_lon(moment_utc)
        america_speed = america.america_speed(moment_utc)
        if america_lon is None or america_speed is None:
            raise RuntimeError("America coverage disappeared during chart calculation")
        america_record: dict[str, Any] = {
            "status": "available_canonical_cache",
            "longitude": round(america_lon, 9),
            "sign": SIGNS[int(america_lon // 30) % 12],
            "degree_in_sign": round(america_lon % 30.0, 9),
            "whole_sign_house": BASE.sign_house(raw["asc"], america_lon),
            "retrograde": america_speed < 0,
            "speed_deg_day": round(america_speed, 9),
            "acting_status": "nonacting_minor_point",
            "source": "canonical JPL Horizons daily cache with shortest-arc interpolation",
        }
    else:
        america_record = {
            "status": "unavailable_no_extrapolation",
            "longitude": None,
            "sign": None,
            "degree_in_sign": None,
            "whole_sign_house": None,
            "retrograde": None,
            "speed_deg_day": None,
            "acting_status": "not_present",
            "source": "canonical cache cannot answer this historical epoch",
        }
    frame = {
        "asc": round(raw["asc"], 9),
        "asc_sign": raw["asc_sign"],
        "mc": round(raw["mc"], 9),
        "mc_sign": raw["mc_sign"],
        "mc_whole_sign_house": BASE.sign_house(raw["asc"], raw["mc"]),
        "chart_ruler": chart_ruler,
        "chart_ruler_house": int(positions[chart_ruler]["house"]),
        "chart_ruler_route": BASE.route_for(positions, chart_ruler),
        "whole_sign_tenth_sign": tenth_sign,
        "whole_sign_tenth_ruler": tenth_ruler,
        "whole_sign_tenth_ruler_house": int(positions[tenth_ruler]["house"]),
        "whole_sign_tenth_ruler_route": BASE.route_for(positions, tenth_ruler),
        "actual_mc_ruler": mc_ruler,
        "actual_mc_ruler_house": int(positions[mc_ruler]["house"]),
        "actual_mc_ruler_route": BASE.route_for(positions, mc_ruler),
        "houses_ruled_by": houses_ruled,
    }
    record = {
        "event": {
            "utc": moment_utc.isoformat(timespec="microseconds"),
            "local": local.isoformat(timespec="microseconds"),
            "zone_abbreviation": local.tzname(),
            "place": PLACE,
            "latitude": LATITUDE,
            "longitude": LONGITUDE,
        },
        "frame": frame,
        "positions": {
            body: BASE.compact_position(position)
            for body, position in positions.items()
        },
        "traditional_dignities": {
            body: {
                "classification": calculator.dignity_label(body, positions[body]["sign"]),
                "labels": calculator.dignity_labels(body, positions[body]["sign"]),
            }
            for body in TRADITIONAL_BODIES
        },
        "condition_scope": "base traditional dignity classification only; not full phase-aware Condition",
        "soli_lunar_phase": raw["soli_lunar_phase"],
        "governance_routes": {
            body: BASE.route_for(positions, body) for body in PLANET_ORDER
        },
        "mundane_major_aspects": BASE.mundane_major_aspects(moment_utc),
        "huber_aspects": huber,
        "minor_point_aspects": minor_point_aspects(
            moment_utc, raw, include_america
        ),
        "angle_aspects": BASE.angle_aspects(raw),
        "configurations": configurations,
        "huber_whole_pattern": structure.huber_whole_pattern(
            positions, huber, configurations
        ),
        "minor_points": {"america_916": america_record},
        "minor_point_policy": {
            "active_points": ["Chiron", "Node"]
            + (["America"] if include_america else []),
            "aspects": ["conjunction", "square", "opposition"],
            "orb_limit_deg": 2.0,
            "point_to_point": False,
            "america_pair_coverage": america_coverage,
        },
        "ephemeris_flags": calc_flag_receipt(BASE.jd_of(moment_utc)),
    }
    return record, raw


def endpoint_ledger(
    seed_rows: list[dict[str, Any]],
    persona_rows: list[dict[str, Any]],
    lane: str,
    *,
    derived_angle: bool = False,
) -> list[dict[str, Any]]:
    def key(row: dict[str, Any]) -> tuple[str, str]:
        if derived_angle:
            return row["point"], row["planet"]
        return tuple(sorted((row["a"], row["b"])))

    def endpoint(row: dict[str, Any]) -> dict[str, Any]:
        result = {
            "aspect": row.get("aspect", row.get("type")),
            "orb_deg": row.get("orb_deg", row.get("orb")),
        }
        for field in (
            "applying",
            "separating",
            "near_exact",
            "source_status",
            "mutual",
            "oneway",
            "nonacting_point",
        ):
            if field in row:
                result[field] = row[field]
        return result

    seed = {key(row): endpoint(row) for row in seed_rows}
    persona = {key(row): endpoint(row) for row in persona_rows}
    output: list[dict[str, Any]] = []
    for relationship in sorted(set(seed) | set(persona)):
        before = seed.get(relationship)
        after = persona.get(relationship)
        if before is None:
            change = "gained"
            classification = "materially_new_relationship_zero_vote"
        elif after is None:
            change = "lost"
            classification = "materially_vanished_relationship_zero_vote"
        elif before["aspect"] != after["aspect"]:
            change = "operator_changed"
            classification = "material_operator_change_zero_vote"
        else:
            change = "persisted_with_condition_change"
            classification = "persistent_relationship_not_independent_news"
        output.append(
            {
                "relationship": list(relationship),
                "change": change,
                "classification": classification,
                "seed": before,
                "persona": after,
                "lane": lane,
                "derived_angle_relationship": derived_angle,
            }
        )
    return output


def change_gate(
    seed_jd: float,
    persona_jd: float,
    radix: dict[str, Any],
    persona: dict[str, Any],
) -> dict[str, Any]:
    interval_days = persona_jd - seed_jd
    within_31_day_dependency_window = interval_days <= 31.0
    stations = BASE.station_events_between(
        seed_jd, persona_jd, TRACKED_CHANGE_BODIES
    )
    station_bodies = {row["body"] for row in stations}
    sign_changes = []
    direction_changes = []
    for body in TRACKED_CHANGE_BODIES:
        before = radix["positions"][body]
        after = persona["positions"][body]
        if before["sign"] != after["sign"]:
            sign_changes.append(
                {
                    "body": body,
                    "seed_sign": before["sign"],
                    "persona_sign": after["sign"],
                    "classification": "material_sign_change_zero_vote",
                }
            )
        if before["retrograde"] != after["retrograde"]:
            direction_changes.append(
                {
                    "body": body,
                    "seed_direction": "retrograde" if before["retrograde"] else "direct",
                    "persona_direction": "retrograde" if after["retrograde"] else "direct",
                    "classification": "material_direction_change_zero_vote",
                }
            )
    ledgers = {
        "mundane_major_ten_planet": endpoint_ledger(
            radix["mundane_major_aspects"],
            persona["mundane_major_aspects"],
            "Freedom 250 ten-planet mundane major-aspect lane",
        ),
        "huber_source_plus_chiron_overlay": endpoint_ledger(
            radix["huber_aspects"],
            persona["huber_aspects"],
            "source-Huber web plus visibly labeled Chiron overlay",
        ),
        "nonacting_minor_point": endpoint_ledger(
            radix["minor_point_aspects"],
            persona["minor_point_aspects"],
            "hard point-to-planet minor-point lane at 2 degrees or less",
        ),
        "derived_angle": endpoint_ledger(
            radix["angle_aspects"],
            persona["angle_aspects"],
            "ASC/MC derived-angle overlay using partner-planet Huber allowance",
            derived_angle=True,
        ),
    }
    material_relationship_changes = [
        {"lane": lane, **row}
        for lane, rows in ledgers.items()
        for row in rows
        if row["change"] in {"gained", "lost", "operator_changed"}
    ]
    slow_relationship_changes = [
        row
        for row in material_relationship_changes
        if any(body in SLOW_BODIES for body in row["relationship"])
    ]
    slow_body_carryover: dict[str, Any] = {}
    for body in SLOW_BODIES:
        before = radix["positions"][body]
        after = persona["positions"][body]
        delta = BASE.angular_distance(before["longitude"], after["longitude"])
        changed_sign = before["sign"] != after["sign"]
        changed_direction = before["retrograde"] != after["retrograde"]
        qualifying_relationships = [
            row for row in slow_relationship_changes if body in row["relationship"]
        ]
        slow_body_carryover[body] = {
            "seed_longitude": before["longitude"],
            "persona_longitude": after["longitude"],
            "absolute_longitude_delta_deg": round(delta, 9),
            "near_return_within_5_deg": delta <= 5.0,
            "near_return_threshold_note": (
                "Five degrees is a descriptive persistence flag, not evidence credit or an aspect orb."
            ),
            "stationed_between": body in station_bodies,
            "within_31_day_dependency_window": within_31_day_dependency_window,
            "changed_direction_at_endpoints": changed_direction,
            "changed_sign": changed_sign,
            "material_relationship_change_count": len(qualifying_relationships),
            "longitude_ruling": "positional_persistence_or_near_return_has_zero_independent_vote",
            "proximity_ruling": (
                "automatically_dependent_within_31_days"
                if within_31_day_dependency_window
                else "after_31_days_proximity_alone_still_never_additive"
            ),
            "condition_ruling": (
                "named_station_sign_or_relationship_change_may_be_considered_zero_vote"
                if body in station_bodies
                or changed_sign
                or changed_direction
                or qualifying_relationships
                else "carryover_only_not_news"
            ),
        }
    return {
        "rule": (
            "For Jupiter through Pluto, positional persistence or near-return "
            "within 31 days is automatically dependent carryover. After 31 days, "
            "proximity alone is still never additive. Only an exact station or "
            "direction change, sign change, or materially gained, lost, or changed "
            "relationship is admitted, and every admitted change remains "
            "conditional and zero-vote. Mercury is tracked separately for station "
            "and sign context but is not classified as a slow or outer body."
        ),
        "interval_days": round(interval_days, 9),
        "within_31_day_dependency_window": within_31_day_dependency_window,
        "tracked_bodies": list(TRACKED_CHANGE_BODIES),
        "slow_body_scope": list(SLOW_BODIES),
        "mercury_scope": "tracked_station_sign_relationship_context_not_slow_or_outer",
        "station_events_between": stations,
        "tracked_body_sign_changes": sign_changes,
        "tracked_body_direction_changes": direction_changes,
        "relationship_deltas": ledgers,
        "material_relationship_changes": material_relationship_changes,
        "slow_or_outer_material_relationship_changes": slow_relationship_changes,
        "persona_derived_angle_relationships": [
            {
                **row,
                "classification": "derived_angle_relationship_conditional_zero_vote",
                "novelty_owner": "persona_derived_angle",
            }
            for row in persona["angle_aspects"]
        ],
        "slow_body_carryover": slow_body_carryover,
    }


def cross_contacts(
    radix: dict[str, Any],
    persona: dict[str, Any],
    focal_bodies: tuple[str, str],
    include_america: bool,
    orb_limit: float = 2.0,
) -> list[dict[str, Any]]:
    seed_targets = {
        body: row["longitude"]
        for body, row in radix["positions"].items()
        if body != "SNode"
    }
    seed_targets.update({"ASC": radix["frame"]["asc"], "MC": radix["frame"]["mc"]})
    persona_sources = {
        body: row["longitude"]
        for body, row in persona["positions"].items()
        if body != "SNode"
    }
    persona_sources.update(
        {"ASC": persona["frame"]["asc"], "MC": persona["frame"]["mc"]}
    )
    if include_america:
        seed_targets["America"] = radix["minor_points"]["america_916"]["longitude"]
        persona_sources["America"] = persona["minor_points"]["america_916"]["longitude"]
    minor = {"Chiron", "Node", "America"}
    dependent = set(SLOW_BODIES) | minor
    rows: list[dict[str, Any]] = []
    for source, source_lon in persona_sources.items():
        for target, target_lon in seed_targets.items():
            if source in minor and target not in PLANET_CODES:
                continue
            if target in minor and source not in PLANET_CODES:
                continue
            separation = BASE.angular_distance(source_lon, target_lon)
            for aspect, angle in BASE.ASPECT_ANGLES:
                orb = abs(separation - angle)
                if orb > orb_limit:
                    continue
                if (source in minor or target in minor) and aspect not in {
                    "conjunction",
                    "square",
                    "opposition",
                }:
                    continue
                if source == "Sun":
                    dependency_class = "guaranteed_persona_sun_target_restatement"
                elif source == target and source in dependent:
                    dependency_class = "positional_near_return_carryover_zero_vote"
                elif (
                    source in focal_bodies
                    and target in focal_bodies
                    and aspect == "conjunction"
                ):
                    dependency_class = "fused_seed_slow_body_dependency_zero_vote"
                elif source == "America" or target == "America":
                    dependency_class = "nonacting_america_zero_vote"
                elif source in dependent and target in dependent:
                    dependency_class = "slow_or_minor_background_zero_vote"
                else:
                    dependency_class = "potentially_additive_conditional_zero_vote"
                rows.append(
                    {
                        "persona_factor": source,
                        "aspect": aspect,
                        "radix_factor": target,
                        "orb_deg": round(orb, 6),
                        "dependency_class": dependency_class,
                    }
                )
                break
    return sorted(rows, key=lambda row: row["orb_deg"])


def canonical_seed_comparison(
    cycle: dict[str, Any], anchor: dict[str, Any], radix: dict[str, Any]
) -> dict[str, Any]:
    canonical = SYNODIC.seed_chart(
        cycle["cycle_id"],
        anchor["pass_id"],
        vault_root=VAULT,
        seed_registry_path=REGISTRY_PATH,
    )
    comparison = {
        "utc_matches": canonical["utc"] == radix["event"]["utc"],
        "pass_id_matches": canonical["pass_id"] == anchor["pass_id"],
        "asc_delta_arcseconds": round(
            BASE.angular_distance(canonical["asc"], radix["frame"]["asc"])
            * 3600.0,
            12,
        ),
        "mc_delta_arcseconds": round(
            BASE.angular_distance(canonical["mc"], radix["frame"]["mc"])
            * 3600.0,
            12,
        ),
        "planet_delta_arcseconds": {
            body: round(
                BASE.angular_distance(
                    canonical["positions"][body]["lon"],
                    radix["positions"][body]["longitude"],
                )
                * 3600.0,
                12,
            )
            for body in PLANET_ORDER
        },
    }
    deltas = [
        comparison["asc_delta_arcseconds"],
        comparison["mc_delta_arcseconds"],
        *comparison["planet_delta_arcseconds"].values(),
    ]
    if not comparison["utc_matches"] or not comparison["pass_id_matches"]:
        raise RuntimeError(f"Canonical seed identity mismatch for {cycle['cycle_id']}")
    if max(deltas) > 0.01:
        raise RuntimeError(
            f"Current calculator differs from canonical seed for {cycle['cycle_id']}"
        )
    return comparison


def calculate_cycle(
    cycle: dict[str, Any], registry_validation: dict[str, Any]
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    anchor = anchor_for(cycle)
    governed = verify_seed_root(cycle, anchor)
    persona_event = find_persona_event(
        governed["seed_jd"], governed["target_longitude"]
    )
    coverage = america_pair_coverage(governed["seed_utc"], persona_event["utc"])
    include_america = bool(coverage["include_in_both_charts"])
    radix, radix_raw = calculate_chart(
        governed["seed_utc"], include_america, coverage
    )
    persona, persona_raw = calculate_chart(
        persona_event["utc"], include_america, coverage
    )
    comparison = canonical_seed_comparison(cycle, anchor, radix)
    gate = change_gate(
        governed["seed_jd"], persona_event["jd_ut"], radix, persona
    )
    focal: dict[str, Any] = {}
    focal_bodies = tuple(cycle["pair"])
    for body in focal_bodies:
        focal[body] = {
            "position": persona["positions"][body],
            "distance_from_persona_sun_deg": round(
                BASE.angular_distance(
                    persona["positions"][body]["longitude"],
                    persona["positions"]["Sun"]["longitude"],
                ),
                9,
            ),
            "governance_route": persona["governance_routes"][body],
            "huber_contacts": BASE.contacts_for(body, persona["huber_aspects"]),
            "mundane_major_contacts": BASE.contacts_for(
                body, persona["mundane_major_aspects"]
            ),
        }
    target = governed["target_longitude"]
    pass_roster = [dict(row) for row in cycle["passes"]]
    data = {
        "schema": "freedom250.long-clock-persona-subsidiary/v1",
        "status": "kept_conditional_subsidiary",
        "review_status": "reviewed",
        "review_disposition": "keep",
        "identity": {
            "cycle_id": cycle["cycle_id"],
            "tier_id": cycle["tier_id"],
            "pair": list(cycle["pair"]),
            "seed_family_id": cycle["seed_family_id"],
            "display_anchor_pass_id": anchor["pass_id"],
            "artifact_key": f"{cycle['cycle_id']}::{anchor['pass_id']}",
        },
        "evidence_boundary": {
            "family": "long_clock_persona_subsidiaries",
            "admission": "conditional_subordinate_zero_vote",
            "timing_authority": False,
            "event_proof": False,
            "independent_vote": False,
            "one_shared_chart": True,
            "focal_lenses": list(cycle["pair"]),
            "hearing_posture": "conditional_research_hearing_only",
        },
        "seed_family": {
            "cycle_id": cycle["cycle_id"],
            "seed_family_id": cycle["seed_family_id"],
            "seed_family_label": cycle["seed_family_label"],
            "nominal_cycle_years": cycle["nominal_cycle_years"],
            "anchor_basis": cycle["anchor_basis"],
            "display_anchor_pass_id": cycle["display_anchor_pass_id"],
            "pass_count": len(pass_roster),
            "complete_pass_roster": pass_roster,
            "multi_pass_handling": (
                "The display anchor owns the primary subsidiary. Other exact "
                "passes remain governed family members and may receive labeled "
                "pass variants, never additional votes."
                if len(pass_roster) > 1
                else "Single governed pass; display anchor and family pass are identical."
            ),
            "anchor_external_verification_status": anchor[
                "independent_verification_status"
            ],
            "registry_validation": {
                "ok": registry_validation["ok"],
                "cycle_count": registry_validation["cycle_count"],
                "pass_count": registry_validation["pass_count"],
                "error_count": len(registry_validation["errors"]),
                "unresolved_external_verification_count": len(
                    registry_validation["unresolved_verification"]
                ),
            },
        },
        "radix": {
            "pass_id": anchor["pass_id"],
            "target_longitude": target,
            "target_sign": anchor["sign"],
            "target_degree_in_sign": anchor["degree_in_sign"],
            "relative_motion": anchor["relative_motion"],
            "calculation_status": anchor["calculation_status"],
            "verification": {
                **governed["verification"],
                "canonical_seed_chart_comparison": comparison,
            },
            **radix,
        },
        "persona": {
            "definition": "first later geocentric tropical Sun crossing of the fixed display-anchor conjunction longitude",
            "target_longitude": target,
            "days_after_radix": round(
                persona_event["jd_ut"] - governed["seed_jd"], 12
            ),
            "verification": persona_event["verification"],
            **persona,
            "persona_sun": {
                "whole_sign_house": persona["positions"]["Sun"][
                    "whole_sign_house"
                ],
                "huber_contacts": BASE.contacts_for(
                    "Sun", persona["huber_aspects"]
                ),
                "mundane_major_contacts": BASE.contacts_for(
                    "Sun", persona["mundane_major_aspects"]
                ),
            },
            "focal_lenses": focal,
        },
        "radix_persona_overlay": {
            "orb_policy": "major cross contacts at 2 degrees; minor points hard-only and planet-facing; all zero-vote",
            "contacts": cross_contacts(
                radix, persona, focal_bodies, include_america
            ),
        },
        "seed_to_persona_change_gate": gate,
        "dependency_ledger": {
            "guaranteed": [
                f"Persona Sun repeats the fixed {target:.9f} degree anchor target.",
                "Persona-Sun radix contacts restate relationships already belonging to the seed target.",
            ],
            "dependent": [
                "The conjunction bodies share one target and one persona chart, not two charts or votes.",
                "For Jupiter through Pluto, proximity or near-return within 31 days is automatically dependent.",
                "After 31 days, slow or outer proximity alone is still never additive.",
                "Persistent slow-body geometry receives no independent vote.",
            ],
            "potentially_additive_but_zero_vote": [
                "derived Ascendant, houses, chart ruler, and dispositor routes",
                "actual MC and Whole Sign tenth-house governance",
                "internal aspect and configuration structure",
                "exact station/direction change, sign change, or materially gained/lost/changed relationship",
                "non-mechanical tight radix-persona contacts",
            ],
        },
        "america_916_coverage": coverage,
        "settings": {
            "zodiac": "tropical",
            "center": "geocentric",
            "houses": "Whole Sign",
            "angles": "houses_ex W frame at current governed Washington DC coordinates",
            "place": PLACE,
            "latitude": LATITUDE,
            "longitude": LONGITUDE,
            "timezone": str(CONVENTIONS.DC_TZ_NAME),
            "rulers": "traditional",
            "node": "true",
            "america_916": (
                "included as canonical nonacting minor point"
                if include_america
                else "unavailable_no_extrapolation"
            ),
        },
        "ephemeris_runtime_receipt": {
            "seed": radix["ephemeris_flags"],
            "persona": persona["ephemeris_flags"],
            "pyswisseph_version": swe.version,
            "chart_calculator_ephe_ok": bool(calculator.EPHE_OK),
            "interpretation": (
                "Requested SWIEPH flags fall back to Moshier for planets in the "
                "current runtime because a planetary Swiss file is absent. "
                "No independent-Swiss verification is claimed."
                if radix["ephemeris_flags"]["fallback_observed"]
                else "Returned flags report the actual available planetary ephemeris."
            ),
        },
        "provenance": {
            "seed_registry": str(REGISTRY_PATH),
            "synodic_engine": str(SYNODIC_PATH),
            "chart_conventions": str(CONVENTIONS_PATH),
            "chart_math": str(SENTIENT_SUN / "chart_calculator.py"),
            "structure_engine": str(SENTIENT_SUN / "reading_engine.py"),
            "wheel_engine": str(WHEEL_PATH),
            "america_reader": str(AMERICA_PATH),
            "america_cache": str(america.CACHE),
            "persona_method": str(PERSONA_METHOD_PATH),
            "generic_helper_source": str(BASE_BUILDER_PATH),
            "builder": str(Path(__file__).resolve()),
        },
        "_raw_chart_objects_excluded": {
            "radix_jd": round(float(radix_raw["jd"]), 12),
            "persona_jd": round(float(persona_raw["jd"]), 12),
        },
    }
    return data, radix_raw, persona_raw


def wheel_positions(chart: dict[str, Any]) -> list[list[Any]]:
    positions: list[list[Any]] = []
    for body in WHEEL_BODY_ORDER:
        if body == "America":
            position = chart["minor_points"]["america_916"]
            if position["status"] != "available_canonical_cache":
                continue
        else:
            position = chart["positions"][body]
        positions.append(
            [
                body,
                position["sign"],
                f"{math.floor(position['degree_in_sign'])}°",
                bool(position["retrograde"]),
                round(position["longitude"], 8),
            ]
        )
    return positions


def wheel_record(
    chart: dict[str, Any], title: str, caption_one: str, caption_two: str
) -> dict[str, Any]:
    operator = {
        "conjunction": "conjunct",
        "sextile": "sextile",
        "square": "square",
        "trine": "trine",
        "opposition": "opposite",
    }
    aspects = [
        {
            "t": f"{row['a']} {operator[row['aspect']]} {row['b']}",
            "o": round(row["orb_deg"], 2),
            "x": 1 if row["orb_deg"] <= 0.3 else 0,
            "ap": 1 if row["applying"] else 0,
            "pt": 0,
        }
        for row in chart["mundane_major_aspects"]
    ]
    aspects.extend(
        {
            "t": f"{row['a']} {operator[row['aspect']]} {row['b']}",
            "o": round(row["orb_deg"], 2),
            "x": 1 if row["orb_deg"] <= 0.3 else 0,
            "ap": 1 if row["applying"] else 0,
            "pt": 1,
        }
        for row in chart["minor_point_aspects"]
    )
    return {
        "asc": round(chart["frame"]["asc"], 8),
        "mc": round(chart["frame"]["mc"], 8),
        "pos": wheel_positions(chart),
        "asp": aspects,
        "__date": title,
        "cap1": caption_one,
        "cap2": caption_two,
    }


def render_cycle_charts(data: dict[str, Any]) -> tuple[Path, Path, str, str]:
    cycle_id = data["identity"]["cycle_id"]
    pair_label = "–".join(data["identity"]["pair"])
    persona_local = datetime.fromisoformat(data["persona"]["event"]["local"])
    event_label = persona_local.strftime("%d %b %Y · %H:%M:%S %Z")
    standalone_record = wheel_record(
        data["persona"],
        f"{pair_label.upper()} CONJUNCTION PERSONA",
        f"{event_label} · {PLACE}",
        "kept conditional subsidiary · zero independent vote",
    )
    radix_record = wheel_record(
        data["radix"],
        f"{pair_label.upper()} SEED + PERSONA",
        f"anchor {data['identity']['display_anchor_pass_id']} inside",
        f"persona outside · {event_label}",
    )
    outer_map = {row[0]: float(row[4]) for row in wheel_positions(data["persona"])}
    standalone_svg = BASE.render_svg(standalone_record)
    biwheel_svg = BASE.render_svg(
        radix_record,
        outer_name=f"{pair_label} Conjunction Persona",
        outer_map=outer_map,
    )
    standalone_path = CHARTS_DIR / f"{cycle_id}__persona-standalone.svg"
    biwheel_path = CHARTS_DIR / f"{cycle_id}__seed-persona-biwheel.svg"
    standalone_path.write_text(standalone_svg, encoding="utf-8")
    biwheel_path.write_text(biwheel_svg, encoding="utf-8")
    return standalone_path, biwheel_path, standalone_svg, biwheel_svg


def svg_data_uri(svg: str) -> str:
    import base64

    return "data:image/svg+xml;base64," + base64.b64encode(
        svg.encode("utf-8")
    ).decode("ascii")


def self_contained_hub(
    cycle_rows: list[dict[str, Any]], full_data: list[dict[str, Any]]
) -> str:
    cards = []
    for row in cycle_rows:
        data = row["data"]
        pair = "–".join(data["identity"]["pair"])
        seed = datetime.fromisoformat(data["radix"]["event"]["local"])
        persona = datetime.fromisoformat(data["persona"]["event"]["local"])
        target = BASE.degree_label(data["radix"]["target_longitude"])
        seed_zone = data["radix"]["event"]["zone_abbreviation"]
        persona_zone = data["persona"]["event"]["zone_abbreviation"]
        america_status = data["america_916_coverage"]["status"].replace("_", " ")
        cards.append(
            f"""<article id="{html.escape(data['identity']['cycle_id'])}">
<header><p class="eyebrow">{html.escape(data['identity']['tier_id'].replace('_', ' ').upper())}</p>
<h2>{html.escape(pair)}</h2><p><code>{html.escape(data['identity']['artifact_key'])}</code></p></header>
<div class="facts"><span><b>Seed</b> {html.escape(seed.strftime('%d %b %Y · %H:%M:%S'))} {html.escape(seed_zone)}</span>
<span><b>Target</b> {html.escape(target)}</span><span><b>Persona</b> {html.escape(persona.strftime('%d %b %Y · %H:%M:%S'))} {html.escape(persona_zone)}</span>
<span><b>America</b> {html.escape(america_status)}</span></div>
<div class="wheels"><section><h3>Persona</h3>{row['standalone_svg']}</section><section><h3>Seed + persona</h3>{row['biwheel_svg']}</section></div>
<div class="downloads"><a download="{html.escape(row['standalone_path'].name)}" href="{svg_data_uri(row['standalone_svg'])}">Download standalone SVG</a> · <a download="{html.escape(row['biwheel_path'].name)}" href="{svg_data_uri(row['biwheel_svg'])}">Download biwheel SVG</a></div>
<details><summary>Embedded factual receipt</summary><pre>{html.escape(json.dumps(data, indent=2, ensure_ascii=False))}</pre></details>
</article>"""
        )
    embedded = json.dumps(
        {
            "schema": "freedom250.long-clock-persona-self-contained-hub/v1",
            "cycles": full_data,
        },
        ensure_ascii=False,
        separators=(",", ":"),
    ).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Freedom 250 · Long Clock Persona Subsidiaries</title><style>
:root{{--paper:#f7f3e9;--card:#fffdf7;--ink:#2d2923;--muted:#746b5e;--line:#d9cdb8;--accent:#594b78}}*{{box-sizing:border-box}}body{{margin:0;background:var(--paper);color:var(--ink);font-family:"Iowan Old Style",Palatino,Georgia,serif}}main{{width:min(1500px,96vw);margin:auto;padding:40px 0 80px}}h1{{font-weight:400;font-size:clamp(2rem,5vw,4rem);margin:.1em 0}}.lead,.boundary{{color:var(--muted);line-height:1.55}}nav{{display:flex;flex-wrap:wrap;gap:8px;margin:24px 0}}nav a,.downloads a{{color:var(--accent)}}article{{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:20px;margin:22px 0}}h2{{font-size:2rem;font-weight:400;margin:.1em 0}}h3{{font-weight:400}}.eyebrow{{font-size:.7rem;letter-spacing:.13em;color:var(--accent);font-weight:700}}.facts{{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0}}.facts span{{background:#eee7da;padding:6px 9px;border-radius:8px;color:var(--muted)}}.wheels{{display:grid;grid-template-columns:1fr 1fr;gap:18px}}.wheels svg{{width:100%;height:auto;display:block}}details{{margin-top:14px}}pre{{white-space:pre-wrap;overflow-wrap:anywhere;font:11px/1.45 ui-monospace,SFMono-Regular,Menlo,monospace;background:#f2ede3;padding:12px;border-radius:10px;max-height:34rem;overflow:auto}}code{{color:var(--accent)}}@media(max-width:900px){{.wheels{{grid-template-columns:1fr}}}}
</style></head><body><main><header><p class="eyebrow">FREEDOM 250 · LONG CLOCKS</p><h1>Persona subsidiaries</h1><p class="lead">One governed display-anchor persona per conjunction family. Each chart is conditional, subordinate, and zero-vote; it cannot time an event or prove a present-day claim.</p><p class="boundary"><b>Dependency gate:</b> for Jupiter through Pluto, proximity within 31 days is automatically dependent. After 31 days, proximity alone is still never additive. This copied HTML contains every wheel and factual JSON receipt inline; it has no sidecar dependency.</p></header>
<nav>{''.join(f'<a href="#{html.escape(row["data"]["identity"]["cycle_id"])}">{html.escape("–".join(row["data"]["identity"]["pair"]))}</a>' for row in cycle_rows)}</nav>
{''.join(cards)}
<script type="application/json" id="long-clock-persona-data">{embedded}</script></main></body></html>"""


def source_hashes() -> dict[str, str]:
    sources = [
        REGISTRY_PATH,
        SYNODIC_PATH,
        CONVENTIONS_PATH,
        WHEEL_PATH,
        AMERICA_PATH,
        Path(america.CACHE),
        SENTIENT_SUN / "chart_calculator.py",
        SENTIENT_SUN / "reading_engine.py",
        BASE_BUILDER_PATH,
        PERSONA_METHOD_PATH,
    ]
    missing = [str(path) for path in sources if not path.exists()]
    if missing:
        raise RuntimeError(f"Missing source dependencies: {missing}")
    return {str(path): sha256(path) for path in sources}


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)
    registry, validation = load_registry()
    cycle_rows: list[dict[str, Any]] = []
    full_data: list[dict[str, Any]] = []
    for cycle in registry["cycles"]:
        data, _radix_raw, _persona_raw = calculate_cycle(cycle, validation)
        cycle_id = cycle["cycle_id"]
        data_path = DATA_DIR / f"{cycle_id}.json"
        data_path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        standalone_path, biwheel_path, standalone_svg, biwheel_svg = (
            render_cycle_charts(data)
        )
        full_data.append(data)
        cycle_rows.append(
            {
                "data": data,
                "data_path": data_path,
                "standalone_path": standalone_path,
                "biwheel_path": biwheel_path,
                "standalone_svg": standalone_svg,
                "biwheel_svg": biwheel_svg,
            }
        )
        print(
            f"BUILT {cycle_id} {data['identity']['display_anchor_pass_id']} "
            f"-> {data['persona']['event']['utc']}"
        )
    index = {
        "schema": "freedom250.long-clock-persona-index/v1",
        "status": "kept_conditional_subsidiary",
        "review_disposition": "keep",
        "admission": "conditional_subordinate_zero_vote",
        "cycle_count": len(cycle_rows),
        "pass_count_in_complete_rosters": sum(
            row["data"]["seed_family"]["pass_count"] for row in cycle_rows
        ),
        "cycles": [
            {
                "cycle_id": row["data"]["identity"]["cycle_id"],
                "pair": row["data"]["identity"]["pair"],
                "seed_family_id": row["data"]["identity"]["seed_family_id"],
                "display_anchor_pass_id": row["data"]["identity"][
                    "display_anchor_pass_id"
                ],
                "artifact_key": row["data"]["identity"]["artifact_key"],
                "seed_utc": row["data"]["radix"]["event"]["utc"],
                "target_longitude": row["data"]["radix"]["target_longitude"],
                "persona_utc": row["data"]["persona"]["event"]["utc"],
                "persona_local": row["data"]["persona"]["event"]["local"],
                "america_916_status": row["data"]["america_916_coverage"][
                    "status"
                ],
                "artifacts": {
                    "data": str(row["data_path"].relative_to(HERE)),
                    "standalone_svg": str(
                        row["standalone_path"].relative_to(HERE)
                    ),
                    "seed_persona_biwheel_svg": str(
                        row["biwheel_path"].relative_to(HERE)
                    ),
                },
                "sha256": {
                    "data": sha256(row["data_path"]),
                    "standalone_svg": sha256(row["standalone_path"]),
                    "seed_persona_biwheel_svg": sha256(row["biwheel_path"]),
                },
            }
            for row in cycle_rows
        ],
        "policy": {
            "primary_persona_per_family": 1,
            "multi_pass_variants": "retained_in_roster_not_additional_votes",
            "one_shared_chart_two_focal_lenses": True,
            "independent_vote": False,
        },
    }
    INDEX_PATH.write_text(
        json.dumps(index, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    HUB_PATH.write_text(
        self_contained_hub(cycle_rows, full_data), encoding="utf-8"
    )
    generated = sorted(
        [INDEX_PATH, HUB_PATH]
        + [row["data_path"] for row in cycle_rows]
        + [row["standalone_path"] for row in cycle_rows]
        + [row["biwheel_path"] for row in cycle_rows],
        key=lambda path: str(path.relative_to(HERE)),
    )
    validator_path = HERE / "validate_long_clock_personas.py"
    code_hashes = {str(Path(__file__).resolve()): sha256(Path(__file__).resolve())}
    if validator_path.exists():
        code_hashes[str(validator_path)] = sha256(validator_path)
    manifest = {
        "schema": "freedom250.long-clock-persona-manifest/v1",
        "status": "kept_conditional_subsidiary",
        "review_disposition": "keep",
        "admission": "conditional_subordinate_zero_vote",
        "cycle_count": 10,
        "governed_anchor_count": 10,
        "governed_family_pass_count": 20,
        "self_contained_hub": str(HUB_PATH.relative_to(HERE)),
        "outputs_sha256": {
            str(path.relative_to(HERE)): sha256(path) for path in generated
        },
        "package_code_sha256": code_hashes,
        "source_sha256": source_hashes(),
        "runtime": {
            "python": sys.version.split()[0],
            "pyswisseph": swe.version,
            "requested_planetary_flags": ["FLG_SWIEPH", "FLG_SPEED"],
            "actual_planetary_fallback_observed": any(
                row["data"]["ephemeris_runtime_receipt"]["seed"][
                    "fallback_observed"
                ]
                for row in cycle_rows
            ),
            "actual_planetary_returned_flag_names": sorted(
                {
                    name
                    for row in cycle_rows
                    for receipt in row["data"]["ephemeris_runtime_receipt"][
                        "seed"
                    ]["returned_by_body"].values()
                    for name in receipt["names"]
                }
            ),
            "ephemeris_boundary": "actual returned flags govern; no independent-Swiss claim",
            "persona_primary_solver": "solcross_ut with SWIEPH requested and actual fallback recorded",
            "persona_independent_solver": "quarter-day bracket plus Moshier bisection",
        },
    }
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        f"WROTE {len(cycle_rows)} cycles, {len(generated)} hashed outputs, "
        f"manifest={MANIFEST_PATH.name}"
    )


if __name__ == "__main__":
    main()
