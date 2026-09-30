#!/usr/bin/env python3
"""Build the research-only Saturn-Neptune 2026 conjunction persona package.

The governed seed is the single exact 2026 Saturn-Neptune conjunction in the
Freedom 250 seed-family registry.  Its exact shared longitude becomes one
fused persona target.  The first later solar conjunction to that fixed degree
produces one shared derived chart, with Saturn and Neptune retained as two
focal lenses inside it.

This builder writes only to its own workbench package.  It does not amend the
live Chronicle vault or adopt the persona technique into Katie's method.
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
from zoneinfo import ZoneInfo

import swisseph as swe


HERE = Path(__file__).resolve().parent
CHARTS = HERE / "charts"
DATA_PATH = HERE / "SATURN_NEPTUNE_2026_CONJUNCTION_PERSONA.json"
MANIFEST_PATH = CHARTS / "conjunction_persona_manifest.json"
GALLERY_PATH = CHARTS / "Saturn–Neptune 2026 — Conjunction Persona Gallery.html"

VAULT = Path("Chronicle/")
SEED_REGISTRY = VAULT / "99 - Templates" / "synodic_seed_families.json"
SYNODIC_ENGINE = VAULT / "99 - Templates" / "synodic_cycles.py"
WHEEL_LIB_PATH = VAULT / "99 - Templates" / "wheel_lib.py"
AMERICA_PATH = VAULT / "99 - Templates" / "america.py"
CHART_CONVENTIONS_PATH = VAULT / "99 - Templates" / "chart_conventions.py"
SENTIENT_SUN = Path("[local-path-removed] Sun")
TRADITIONAL_TABLES_PATH = SENTIENT_SUN / "canonical_traditional_tables.py"
PERSONA_METHOD = Path(
    "[local-path-removed] General/outputs/"
    "persona_charts_research_2026-07-22/"
    "PERSONA_CHARTS_CLEAN_METHOD_REFERENCE.md"
)
MUNDANE_REFERENCE = (
    VAULT / "00 - Index" / "Mundane Astrology — Master Reference.md"
)

sys.path.insert(0, str(SENTIENT_SUN))
sys.path.insert(0, str(VAULT / "99 - Templates"))
import america  # noqa: E402
import chart_calculator as calculator  # noqa: E402
import reading_engine as structure  # noqa: E402

AMERICA_CACHE = Path(america.CACHE)


def _load_module(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


WHEEL = _load_module(WHEEL_LIB_PATH, "f250_persona_wheel")
CONVENTIONS = _load_module(CHART_CONVENTIONS_PATH, "f250_persona_conventions")
SYNODIC = _load_module(SYNODIC_ENGINE, "f250_persona_synodic")
TABLES = _load_module(TRADITIONAL_TABLES_PATH, "f250_persona_traditional_tables")
calculator.dignity_label = TABLES.dignity_classification
calculator.dignity_labels = TABLES.dignity_labels

LATITUDE = float(CONVENTIONS.DC_LAT)
LONGITUDE = float(CONVENTIONS.DC_LON)
PLACE = str(CONVENTIONS.DC_LABEL)
ZONE_NAME = str(CONVENTIONS.DC_TZ_NAME)
ZONE = CONVENTIONS.DC_TZ
FLAGS = swe.FLG_MOSEPH | swe.FLG_SPEED
SIGNS = tuple(calculator.SIGNS)
BODY_ORDER = (
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
    "Chiron",
    "Node",
    "SNode",
    "America",
)
TRADITIONAL_BODIES = (
    "Sun",
    "Moon",
    "Mercury",
    "Venus",
    "Mars",
    "Jupiter",
    "Saturn",
)
ASPECT_ANGLES = (
    ("conjunction", 0.0),
    ("sextile", 60.0),
    ("square", 90.0),
    ("trine", 120.0),
    ("opposition", 180.0),
)
MUNDANE_MAJOR_ASPECTS = (
    ("conjunction", 0.0, 8.0),
    ("sextile", 60.0, 5.0),
    ("square", 90.0, 7.0),
    ("trine", 120.0, 7.0),
    ("opposition", 180.0, 8.0),
)
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
MUNDANE_ASPECT_POINT_ORDER = tuple(PLANET_CODES)
MINOR_POINT_HARD_ASPECTS = (
    ("conjunction", 0.0, 2.0),
    ("square", 90.0, 2.0),
    ("opposition", 180.0, 2.0),
)
SLOW_CHANGE_BODIES = ("Jupiter", "Saturn", "Uranus", "Neptune", "Pluto")
OUTER_PLANETS = ("Uranus", "Neptune", "Pluto")
STATION_CONTEXT_BODIES = ("Mercury",) + SLOW_CHANGE_BODIES


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


def signed_delta(a: float, b: float) -> float:
    return ((a - b + 540.0) % 360.0) - 180.0


def angular_distance(a: float, b: float) -> float:
    return abs(signed_delta(a, b))


def body_state(jd_ut: float, body_code: int, flags: int = FLAGS) -> tuple[float, float]:
    result = swe.calc_ut(jd_ut, body_code, flags)[0]
    return result[0] % 360.0, result[3]


def bisection(function, lo: float, hi: float, iterations: int = 100) -> float:
    flo = function(lo)
    fhi = function(hi)
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
            hi = mid
            fhi = fm
        else:
            lo = mid
            flo = fm
    return (lo + hi) / 2.0


def station_events_between(
    start_jd: float,
    end_jd: float,
    bodies: tuple[str, ...] = STATION_CONTEXT_BODIES,
) -> list[dict[str, Any]]:
    """Find geocentric longitude-speed reversals between two chart moments."""
    rows: list[dict[str, Any]] = []
    step_days = 0.125
    for body in bodies:
        code = PLANET_CODES[body]
        previous_jd = start_jd
        previous_speed = body_state(previous_jd, code)[1]
        last_root: float | None = None
        while previous_jd < end_jd:
            current_jd = min(previous_jd + step_days, end_jd)
            current_speed = body_state(current_jd, code)[1]
            if previous_speed == 0.0 or previous_speed * current_speed < 0.0:
                root_jd = bisection(
                    lambda value: body_state(value, code)[1],
                    previous_jd,
                    current_jd,
                )
                if last_root is None or abs(root_jd - last_root) > 1e-5:
                    before_speed = body_state(root_jd - 1.0 / 1440.0, code)[1]
                    after_speed = body_state(root_jd + 1.0 / 1440.0, code)[1]
                    longitude = body_state(root_jd, code)[0]
                    moment_utc = jd_to_utc(root_jd)
                    rows.append(
                        {
                            "body": body,
                            "utc": moment_utc.isoformat(timespec="microseconds"),
                            "local": moment_utc.astimezone(ZONE).isoformat(
                                timespec="microseconds"
                            ),
                            "longitude": round(longitude, 9),
                            "sign": SIGNS[int(longitude // 30) % 12],
                            "direction_before": (
                                "direct" if before_speed > 0 else "retrograde"
                            ),
                            "direction_after": (
                                "direct" if after_speed > 0 else "retrograde"
                            ),
                            "hours_before_persona": round(
                                (end_jd - root_jd) * 24.0, 6
                            ),
                            "solver": "three-hour scan plus Moshier speed-root bisection",
                        }
                    )
                    last_root = root_jd
            previous_jd = current_jd
            previous_speed = current_speed
    return sorted(rows, key=lambda row: row["utc"])


def load_governed_seed() -> dict[str, Any]:
    registry = SYNODIC.load_seed_registry(SEED_REGISTRY)
    if registry.get("schema") != "freedom250.long-clocks.seed-families/v1":
        raise RuntimeError("Unsupported Long Clocks seed registry schema")
    if registry.get("status") != "active":
        raise RuntimeError("Long Clocks seed registry is not active")
    validation = SYNODIC.validate_seed_registry(registry)
    if not validation["ok"]:
        raise RuntimeError(
            "Long Clocks seed registry failed validation: "
            + json.dumps(validation["errors"], ensure_ascii=False)
        )
    cycle = next(
        item for item in registry["cycles"] if item["cycle_id"] == "saturn-neptune"
    )
    if cycle["pair"] != ["Saturn", "Neptune"]:
        raise RuntimeError("Saturn-Neptune governed pair identity mismatch")
    if cycle["seed_family_id"] != "saturn-neptune-2026":
        raise RuntimeError("Saturn-Neptune governed seed-family identity mismatch")
    if cycle["display_anchor_pass_id"] != "saturn-neptune-20260220-p1":
        raise RuntimeError("Saturn-Neptune governed display-anchor identity mismatch")
    if len(cycle["passes"]) != 1:
        raise RuntimeError("Saturn-Neptune 2026 pilot requires one governed pass")
    anchor = next(
        item
        for item in cycle["passes"]
        if item["pass_id"] == cycle["display_anchor_pass_id"]
    )
    if anchor["pass_id"] != "saturn-neptune-20260220-p1":
        raise RuntimeError("Saturn-Neptune governed pass identity mismatch")
    moment = datetime.fromisoformat(anchor["utc"]).astimezone(timezone.utc)
    registry_jd = jd_of(moment)

    def conjunction_delta(jd_ut: float) -> float:
        saturn, _ = body_state(jd_ut, swe.SATURN)
        neptune, _ = body_state(jd_ut, swe.NEPTUNE)
        return signed_delta(saturn, neptune)

    independent_jd = bisection(
        conjunction_delta, registry_jd - 1.0, registry_jd + 1.0
    )
    independent_utc = jd_to_utc(independent_jd)
    saturn, saturn_speed = body_state(registry_jd, swe.SATURN)
    neptune, neptune_speed = body_state(registry_jd, swe.NEPTUNE)
    canonical_seed_chart = SYNODIC.seed_chart(
        cycle["cycle_id"],
        anchor["pass_id"],
        vault_root=VAULT,
        seed_registry_path=SEED_REGISTRY,
    )
    return {
        "cycle": cycle,
        "anchor": anchor,
        "utc": moment,
        "jd_ut": registry_jd,
        "target_longitude": float(anchor["longitude_deg"]),
        "registry_validation": {
            "ok": validation["ok"],
            "cycle_count": validation["cycle_count"],
            "pass_count": validation["pass_count"],
            "error_count": len(validation["errors"]),
            "unresolved_external_verification_count": len(
                validation["unresolved_verification"]
            ),
        },
        "canonical_seed_chart": canonical_seed_chart,
        "verification": {
            "registry_vs_independent_root_seconds": round(
                abs(independent_jd - registry_jd) * 86400.0, 6
            ),
            "independent_root_utc": independent_utc.isoformat(timespec="microseconds"),
            "saturn_neptune_residual_arcseconds": round(
                angular_distance(saturn, neptune) * 3600.0, 9
            ),
            "registry_target_minus_saturn_arcseconds": round(
                signed_delta(float(anchor["longitude_deg"]), saturn) * 3600.0,
                9,
            ),
            "registry_target_minus_neptune_arcseconds": round(
                signed_delta(float(anchor["longitude_deg"]), neptune) * 3600.0,
                9,
            ),
            "saturn_speed_deg_day": round(saturn_speed, 9),
            "neptune_speed_deg_day": round(neptune_speed, 9),
        },
    }


def sun_longitude(jd_ut: float, flags: int) -> float:
    return swe.calc_ut(jd_ut, swe.SUN, flags | swe.FLG_SPEED)[0][0] % 360.0


def find_persona_event(seed_jd: float, target: float) -> dict[str, Any]:
    primary_jd = float(
        swe.solcross_ut(target, seed_jd + 1e-7, swe.FLG_SWIEPH)
    )
    step = 0.25
    previous_jd = seed_jd + 1e-7
    previous_delta = signed_delta(
        sun_longitude(previous_jd, swe.FLG_MOSEPH), target
    )
    bracket: tuple[float, float] | None = None
    while previous_jd < seed_jd + 370.0:
        current_jd = previous_jd + step
        current_delta = signed_delta(
            sun_longitude(current_jd, swe.FLG_MOSEPH), target
        )
        if previous_delta <= 0 <= current_delta:
            bracket = (previous_jd, current_jd)
            break
        previous_jd = current_jd
        previous_delta = current_delta
    if bracket is None:
        raise RuntimeError("Could not bracket first later solar contact")
    independent_jd = bisection(
        lambda value: signed_delta(
            sun_longitude(value, swe.FLG_MOSEPH), target
        ),
        *bracket,
    )
    event_utc = jd_to_utc(primary_jd)
    return {
        "jd_ut": primary_jd,
        "utc": event_utc,
        "local": event_utc.astimezone(ZONE),
        "verification": {
            "swiss_solcross_vs_moshier_bisection_seconds": round(
                abs(primary_jd - independent_jd) * 86400.0, 6
            ),
            "independent_bisection_utc": jd_to_utc(independent_jd).isoformat(
                timespec="microseconds"
            ),
            "sun_minus_target_arcseconds": round(
                signed_delta(
                    sun_longitude(primary_jd, swe.FLG_SWIEPH), target
                )
                * 3600.0,
                9,
            ),
        },
    }


def route_for(positions: dict[str, dict[str, Any]], body: str) -> dict[str, Any]:
    chain, terminal, kind = structure.dispositor_chain(positions, body)
    return {"chain": chain, "terminal": terminal, "kind": kind}


def sign_house(asc: float, longitude: float) -> int:
    return ((int(longitude // 30) - int(asc // 30)) % 12) + 1


def compact_position(position: dict[str, Any]) -> dict[str, Any]:
    speed = position.get("speed")
    declination = position.get("decl")
    return {
        "longitude": round(position["lon"], 9),
        "sign": position["sign"],
        "degree_in_sign": round(position["lon"] % 30.0, 9),
        "whole_sign_house": int(position["house"]),
        "retrograde": bool(position["retro"]),
        "speed_deg_day": None if speed is None else round(float(speed), 8),
        "declination": None
        if declination is None
        else round(float(declination), 6),
    }


def mundane_major_aspects(
    moment_utc: datetime,
) -> list[dict[str, Any]]:
    jd_ut = jd_of(moment_utc)
    future_jd = jd_ut + 1.0 / 24.0
    current = {
        body: body_state(jd_ut, code)[0]
        for body, code in PLANET_CODES.items()
    }
    future = {
        body: body_state(future_jd, code)[0]
        for body, code in PLANET_CODES.items()
    }
    rows: list[dict[str, Any]] = []
    for index, body_a in enumerate(MUNDANE_ASPECT_POINT_ORDER):
        for body_b in MUNDANE_ASPECT_POINT_ORDER[index + 1 :]:
            separation = angular_distance(current[body_a], current[body_b])
            aspect, angle, limit = min(
                MUNDANE_MAJOR_ASPECTS,
                key=lambda row: abs(separation - row[1]),
            )
            orb = abs(separation - angle)
            if orb > limit:
                continue
            future_separation = angular_distance(future[body_a], future[body_b])
            future_orb = abs(future_separation - angle)
            rows.append(
                {
                    "a": body_a,
                    "b": body_b,
                    "aspect": aspect,
                    "angle_deg": angle,
                    "orb_deg": round(orb, 6),
                    "orb_limit_deg": limit,
                    "applying": future_orb < orb,
                    "separating": future_orb >= orb,
                    "separation_deg": round(separation, 6),
                    "authority": "Freedom 250 ten-planet mundane major-aspect lane",
                }
            )
    return sorted(rows, key=lambda row: row["orb_deg"])


def minor_point_aspects(
    moment_utc: datetime, raw: dict[str, Any]
) -> list[dict[str, Any]]:
    """Hard aspects from a minor point to an actual planet, never point-to-point."""
    future_utc = moment_utc + timedelta(hours=1)
    jd_ut = jd_of(moment_utc)
    future_jd = jd_of(future_utc)
    current_planets = {
        body: body_state(jd_ut, code)[0]
        for body, code in PLANET_CODES.items()
    }
    future_planets = {
        body: body_state(future_jd, code)[0]
        for body, code in PLANET_CODES.items()
    }
    current_points = {
        "Chiron": float(raw["pos"]["Chiron"]["lon"]),
        "Node": float(raw["pos"]["Node"]["lon"]),
        "America": america.america_lon(moment_utc),
    }
    future_local = future_utc.astimezone(ZONE)
    future_seconds = future_local.second + future_local.microsecond / 1_000_000.0
    future_offset = future_local.utcoffset().total_seconds() / 3600.0
    future_raw = calculator.compute(
        future_local.year,
        future_local.month,
        future_local.day,
        future_local.hour,
        future_local.minute,
        LATITUDE,
        LONGITUDE,
        future_offset,
        seconds=future_seconds,
    )
    future_points = {
        "Chiron": float(future_raw["pos"]["Chiron"]["lon"]),
        "Node": float(future_raw["pos"]["Node"]["lon"]),
        "America": america.america_lon(future_utc),
    }
    if current_points["America"] is None or future_points["America"] is None:
        raise RuntimeError("916 America cache does not cover minor-point aspect window")

    rows: list[dict[str, Any]] = []
    for point, point_lon in current_points.items():
        for planet, planet_lon in current_planets.items():
            separation = angular_distance(float(point_lon), planet_lon)
            aspect, angle, limit = min(
                MINOR_POINT_HARD_ASPECTS,
                key=lambda row: abs(separation - row[1]),
            )
            orb = abs(separation - angle)
            if orb > limit:
                continue
            future_separation = angular_distance(
                float(future_points[point]), future_planets[planet]
            )
            future_orb = abs(future_separation - angle)
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
                    "authority": (
                        "Freedom 250 minor-point lane: point-to-planet hard "
                        "aspect at 2 degrees or less; no point-to-point aspects"
                    ),
                }
            )
    return sorted(rows, key=lambda row: row["orb_deg"])


def angle_aspects(raw: dict[str, Any]) -> list[dict[str, Any]]:
    """Katie angle overlay: the partner planet supplies its Huber allowance."""
    rows: list[dict[str, Any]] = []
    for point, point_lon in (("ASC", raw["asc"]), ("MC", raw["mc"])):
        for body in (
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
            "Chiron",
        ):
            position = raw["pos"][body]
            if position.get("missing"):
                continue
            separation = angular_distance(point_lon, position["lon"])
            for aspect, angle in structure.HUBER_ANGLE.items():
                orb = abs(separation - angle)
                allowed = structure._huber_allowance(aspect, body)
                if allowed is not None and orb <= allowed:
                    rows.append(
                        {
                            "point": point,
                            "planet": body,
                            "aspect": aspect,
                            "orb_deg": round(orb, 6),
                            "orb_limit_deg": allowed,
                            "near_exact": orb <= 1.0,
                            "authority": "Katie angle overlay; partner planet Huber allowance",
                        }
                    )
                    break
    return sorted(rows, key=lambda row: row["orb_deg"])


def calculate_chart(moment_utc: datetime) -> tuple[dict[str, Any], dict[str, Any]]:
    america_ok, america_message = america.available()
    if not america_ok:
        raise RuntimeError(f"916 America cache unavailable: {america_message}")
    local = moment_utc.astimezone(ZONE)
    seconds = local.second + local.microsecond / 1_000_000.0
    offset = local.utcoffset().total_seconds() / 3600.0
    raw = calculator.compute(
        local.year,
        local.month,
        local.day,
        local.hour,
        local.minute,
        LATITUDE,
        LONGITUDE,
        offset,
        seconds=seconds,
    )
    positions = raw["pos"]
    aspects = structure.huber_aspects(positions)
    configurations = structure.configurations(positions, aspects)
    asc_index = int(raw["asc"] // 30)
    chart_ruler = structure.RULER[raw["asc_sign"]]
    mc_house = sign_house(raw["asc"], raw["mc"])
    whole_sign_tenth_sign = SIGNS[(asc_index + 9) % 12]
    whole_sign_tenth_ruler = structure.RULER[whole_sign_tenth_sign]
    actual_mc_ruler = structure.RULER[raw["mc_sign"]]
    houses_ruled: dict[str, list[int]] = {body: [] for body in TRADITIONAL_BODIES}
    for house in range(1, 13):
        sign = SIGNS[(asc_index + house - 1) % 12]
        houses_ruled[structure.RULER[sign]].append(house)

    america_lon = america.america_lon(moment_utc)
    america_speed = america.america_speed(moment_utc)
    if america_lon is None or america_speed is None:
        raise RuntimeError("916 America cache does not cover chart moment")
    america_position = {
        "longitude": round(america_lon, 9),
        "sign": SIGNS[int(america_lon // 30) % 12],
        "degree_in_sign": round(america_lon % 30.0, 9),
        "whole_sign_house": sign_house(raw["asc"], america_lon),
        "retrograde": america_speed < 0,
        "speed_deg_day": round(america_speed, 9),
        "source": "canonical JPL Horizons daily cache with shortest-arc interpolation",
        "acting_status": "nonacting_minor_point",
    }
    traditional_dignities = {
        body: {
            "classification": calculator.dignity_label(
                body, positions[body]["sign"]
            ),
            "labels": calculator.dignity_labels(
                body, positions[body]["sign"]
            ),
        }
        for body in TRADITIONAL_BODIES
    }
    frame = {
        "asc": round(raw["asc"], 9),
        "asc_sign": raw["asc_sign"],
        "mc": round(raw["mc"], 9),
        "mc_sign": raw["mc_sign"],
        "mc_whole_sign_house": mc_house,
        "chart_ruler": chart_ruler,
        "chart_ruler_house": positions[chart_ruler]["house"],
        "chart_ruler_route": route_for(positions, chart_ruler),
        "whole_sign_tenth_sign": whole_sign_tenth_sign,
        "whole_sign_tenth_ruler": whole_sign_tenth_ruler,
        "whole_sign_tenth_ruler_house": positions[whole_sign_tenth_ruler]["house"],
        "whole_sign_tenth_ruler_route": route_for(
            positions, whole_sign_tenth_ruler
        ),
        "actual_mc_ruler": actual_mc_ruler,
        "actual_mc_ruler_house": positions[actual_mc_ruler]["house"],
        "actual_mc_ruler_route": route_for(positions, actual_mc_ruler),
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
            body: compact_position(position)
            for body, position in positions.items()
        },
        "traditional_dignities": traditional_dignities,
        "condition_scope": (
            "base traditional dignity classification only; not the complete "
            "phase-aware Condition owner; classification describes tools, "
            "never role size or weakness"
        ),
        "soli_lunar_phase": raw["soli_lunar_phase"],
        "governance_routes": {
            body: route_for(positions, body)
            for body in ("Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Neptune")
        },
        "huber_aspects": aspects,
        "mundane_major_aspects": mundane_major_aspects(moment_utc),
        "minor_point_aspects": minor_point_aspects(moment_utc, raw),
        "angle_aspects": angle_aspects(raw),
        "configurations": configurations,
        "huber_whole_pattern": structure.huber_whole_pattern(
            positions, aspects, configurations
        ),
        "minor_points": {
            "america_916": america_position,
        },
        "minor_point_policy": {
            "rule": "point-to-planet hard aspects only at 2 degrees or less",
            "points": ["Chiron", "Node", "America"],
            "planets": list(PLANET_CODES),
            "aspects": ["conjunction", "square", "opposition"],
            "point_to_point": False,
            "america_cache_receipt": america_message,
        },
    }
    return record, raw


def contacts_for(body: str, aspects: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        aspect
        for aspect in aspects
        if aspect["a"] == body or aspect["b"] == body
    ]


def find_aspect(
    aspects: list[dict[str, Any]],
    body_a: str,
    body_b: str,
    aspect: str,
) -> dict[str, Any]:
    for row in aspects:
        pair = {row["a"], row["b"]}
        operator = row.get("aspect", row.get("type"))
        if pair == {body_a, body_b} and operator == aspect:
            return row
    raise RuntimeError(f"Required aspect missing: {body_a} {aspect} {body_b}")


def relationship_delta_rows(
    seed_aspects: list[dict[str, Any]],
    persona_aspects: list[dict[str, Any]],
    lane: str,
) -> list[dict[str, Any]]:
    """Complete endpoint ledger for every relationship admitted in either chart."""

    def endpoint(row: dict[str, Any]) -> dict[str, Any]:
        result = {
            "aspect": row.get("aspect", row.get("type")),
            "orb_deg": row.get("orb_deg", row.get("orb")),
        }
        for key in (
            "applying",
            "separating",
            "source_status",
            "mutual",
            "oneway",
        ):
            if key in row:
                result[key] = row[key]
        return result

    def index(rows: list[dict[str, Any]]) -> dict[tuple[str, str], dict[str, Any]]:
        return {
            tuple(sorted((row["a"], row["b"]))): endpoint(row)
            for row in rows
        }

    seed = index(seed_aspects)
    persona = index(persona_aspects)
    output: list[dict[str, Any]] = []
    for pair in sorted(set(seed) | set(persona)):
        seed_row = seed.get(pair)
        persona_row = persona.get(pair)
        if seed_row is None:
            change = "gained"
        elif persona_row is None:
            change = "lost"
        elif seed_row["aspect"] != persona_row["aspect"]:
            change = "operator_changed"
        else:
            change = "persisted_with_condition_change"
        output.append(
            {
                "pair": list(pair),
                "change": change,
                "seed": seed_row,
                "persona": persona_row,
                "lane": lane,
            }
        )
    return output


def seed_to_persona_change_gate(
    governed: dict[str, Any],
    persona_event: dict[str, Any],
    radix: dict[str, Any],
    persona: dict[str, Any],
) -> dict[str, Any]:
    stations = station_events_between(
        governed["jd_ut"], persona_event["jd_ut"]
    )
    station_bodies = {row["body"] for row in stations}
    sign_changes = [
        {
            "body": body,
            "radix_sign": radix["positions"][body]["sign"],
            "persona_sign": persona["positions"][body]["sign"],
        }
        for body in SLOW_CHANGE_BODIES
        if radix["positions"][body]["sign"]
        != persona["positions"][body]["sign"]
    ]
    jupiter_station = next(
        row
        for row in stations
        if row["body"] == "Jupiter" and row["direction_after"] == "direct"
    )
    mercury_direct_station = next(
        row
        for row in stations
        if row["body"] == "Mercury" and row["direction_after"] == "direct"
    )
    mc_uranus = next(
        row
        for row in persona["angle_aspects"]
        if row["point"] == "MC"
        and row["planet"] == "Uranus"
        and row["aspect"] == "opposition"
    )
    seed_saturn_pluto = find_aspect(
        radix["mundane_major_aspects"], "Saturn", "Pluto", "sextile"
    )
    seed_saturn_uranus = find_aspect(
        radix["mundane_major_aspects"], "Saturn", "Uranus", "sextile"
    )
    persona_saturn_uranus_orb = abs(
        angular_distance(
            persona["positions"]["Saturn"]["longitude"],
            persona["positions"]["Uranus"]["longitude"],
        )
        - 60.0
    )
    persona_saturn_pluto = find_aspect(
        persona["huber_aspects"], "Saturn", "Pluto", "sextile"
    )
    mars_jupiter = find_aspect(
        persona["mundane_major_aspects"], "Mars", "Jupiter", "trine"
    )
    seed_venus_jupiter = find_aspect(
        radix["mundane_major_aspects"], "Venus", "Jupiter", "trine"
    )
    persona_venus_jupiter = find_aspect(
        persona["mundane_major_aspects"], "Venus", "Jupiter", "square"
    )
    mercury_node = find_aspect(
        persona["minor_point_aspects"], "Mercury", "Node", "conjunction"
    )
    relationship_deltas = {
        "scope": (
            "complete union of every relationship admitted at either endpoint "
            "inside each named lane; derived angle relationships remain separate"
        ),
        "mundane_major_ten_planet": relationship_delta_rows(
            radix["mundane_major_aspects"],
            persona["mundane_major_aspects"],
            "Freedom 250 ten-planet mundane major-aspect lane",
        ),
        "huber_source_plus_katie_chiron_overlay": relationship_delta_rows(
            radix["huber_aspects"],
            persona["huber_aspects"],
            "source-Huber web plus visibly labeled Katie Chiron overlay",
        ),
        "nonacting_minor_point": relationship_delta_rows(
            radix["minor_point_aspects"],
            persona["minor_point_aspects"],
            "hard point-to-planet minor-point lane at 2 degrees or less",
        ),
        "persona_derived_angle_relationships": persona["angle_aspects"],
    }
    return {
        "rule": (
            "A slow-body near-return within the short seed-to-persona interval "
            "is carryover, not a finding. Promote only a station or direction "
            "change, sign change, or genuinely new aspect/derived-angle relation; "
            "the novelty belongs to the changed condition or relationship, not "
            "to the near-return itself."
        ),
        "tracked_slow_bodies": list(SLOW_CHANGE_BODIES),
        "outer_planets": list(OUTER_PLANETS),
        "station_events_between": stations,
        "slow_body_sign_changes": sign_changes,
        "slow_body_carryover": {
            body: {
                "stationed_between": body in station_bodies,
                "changed_sign": any(row["body"] == body for row in sign_changes),
                "longitude_ruling": "near_return_carryover_not_news",
                "separate_change_gate": (
                    "station_or_relationship_change_may_qualify"
                    if body in station_bodies
                    else "relationship_change_may_qualify"
                ),
            }
            for body in SLOW_CHANGE_BODIES
        },
        "relationship_deltas": relationship_deltas,
        "promotion_rule": (
            "The promoted list is selective, not exhaustive: retain only changes "
            "that materially answer how this conjunction seed organizes itself. "
            "The complete admitted-relationship delta ledger remains above."
        ),
        "promoted_question_relevant_changes": [
            {
                "factor": "Jupiter",
                "change": "retrograde_at_seed_to_direct_at_persona",
                "station": jupiter_station,
                "related_persona_contact": {
                    "aspect": "Mars trine Jupiter",
                    "orb_deg": mars_jupiter["orb_deg"],
                    "applying": mars_jupiter["applying"],
                },
                "classification": "potentially_additive_condition_change_zero_vote",
            },
            {
                "factor": "Mercury",
                "change": "stationed_direct_shortly_before_persona",
                "station": mercury_direct_station,
                "persona_speed_deg_day": persona["positions"]["Mercury"][
                    "speed_deg_day"
                ],
                "related_persona_contact": {
                    "aspect": "Mercury conjunct true Node",
                    "orb_deg": mercury_node["orb_deg"],
                    "point_status": "nonacting_minor_point",
                },
                "classification": "potentially_additive_condition_change_zero_vote",
            },
            {
                "factor": "persona MC and Uranus",
                "change": "new_derived_angle_relationship",
                "aspect": "opposition",
                "orb_deg": mc_uranus["orb_deg"],
                "novelty_owner": "derived_persona_MC_not_uranus_near_return",
                "classification": "potentially_additive_derived_relation_zero_vote",
            },
            {
                "factor": "Saturn and Pluto",
                "change": "broader_seed_sextile_enters_tight_huber_web",
                "seed_mundane_orb_deg": seed_saturn_pluto["orb_deg"],
                "persona_huber_orb_deg": persona_saturn_pluto["orb"],
                "classification": (
                    "tightness_change_not_a_new_outer_return_vote"
                ),
            },
            {
                "factor": "Saturn and Uranus",
                "change": "seed_sextile_leaves_five_degree_mundane_lane",
                "seed_mundane_orb_deg": seed_saturn_uranus["orb_deg"],
                "persona_sextile_orb_deg": round(
                    persona_saturn_uranus_orb, 6
                ),
                "classification": "relationship_admission_change_zero_vote",
            },
            {
                "factor": "Venus and Jupiter",
                "change": "seed_trine_to_persona_square",
                "seed_trine_orb_deg": seed_venus_jupiter["orb_deg"],
                "persona_square_orb_deg": persona_venus_jupiter["orb_deg"],
                "persona_separating": persona_venus_jupiter["separating"],
                "classification": (
                    "question_relevant_counterweight_fast_partner_driven_zero_vote"
                ),
            },
        ],
        "excluded_as_news": [
            "persona Uranus conjunct radix Uranus",
            "persona Pluto conjunct radix Pluto",
            "persona Saturn and Neptune remaining near the fixed target",
            "slow-body geometry that merely persists from the seed",
        ],
    }


def cross_contacts(
    radix: dict[str, Any], persona: dict[str, Any], orb_limit: float = 2.0
) -> list[dict[str, Any]]:
    radix_targets = {
        **{
            body: position["longitude"]
            for body, position in radix["positions"].items()
            if body != "SNode"
        },
        "ASC": radix["frame"]["asc"],
        "MC": radix["frame"]["mc"],
        "America": radix["minor_points"]["america_916"]["longitude"],
    }
    persona_sources = {
        **{
            body: position["longitude"]
            for body, position in persona["positions"].items()
            if body != "SNode"
        },
        "ASC": persona["frame"]["asc"],
        "MC": persona["frame"]["mc"],
        "America": persona["minor_points"]["america_916"]["longitude"],
    }
    result: list[dict[str, Any]] = []
    minor_points = {"Chiron", "Node", "America"}
    slow_or_dependent = {
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
        "Pluto",
        "Chiron",
        "Node",
        "America",
    }
    for source, source_lon in persona_sources.items():
        for target, target_lon in radix_targets.items():
            if source in minor_points and target not in PLANET_CODES:
                continue
            if target in minor_points and source not in PLANET_CODES:
                continue
            separation = angular_distance(source_lon, target_lon)
            for aspect, angle in ASPECT_ANGLES:
                orb = abs(separation - angle)
                if orb <= orb_limit:
                    if (
                        source in minor_points or target in minor_points
                    ) and aspect not in {"conjunction", "square", "opposition"}:
                        continue
                    if source == "Sun":
                        dependency = "guaranteed_radix_target_restatement"
                    elif (
                        source in {"Saturn", "Neptune"}
                        and target in {"Saturn", "Neptune"}
                        and aspect == "conjunction"
                    ):
                        dependency = "fused_seed_slow_body_dependent"
                    elif source == target and source in slow_or_dependent:
                        dependency = "slow_body_dependent"
                    elif source == "America" or target == "America":
                        dependency = "nonacting_minor_point_zero_vote"
                    elif (
                        source in {"ASC", "MC"}
                        and target in slow_or_dependent
                        and target in persona["positions"]
                        and angular_distance(
                            persona["positions"][target]["longitude"],
                            target_lon,
                        )
                        <= orb_limit
                    ):
                        dependency = "dependent_correlated_overlay_zero_vote"
                    elif source in slow_or_dependent and target in slow_or_dependent:
                        dependency = "slow_to_slow_background_zero_vote"
                    else:
                        dependency = "potentially_additive_zero_vote"
                    result.append(
                        {
                            "persona_factor": source,
                            "aspect": aspect,
                            "radix_factor": target,
                            "orb_deg": round(orb, 6),
                            "dependency_class": dependency,
                        }
                    )
                    break
    return sorted(result, key=lambda item: item["orb_deg"])


def calculate() -> dict[str, Any]:
    governed = load_governed_seed()
    target = governed["target_longitude"]
    persona_event = find_persona_event(governed["jd_ut"], target)
    radix, radix_raw = calculate_chart(governed["utc"])
    persona, persona_raw = calculate_chart(persona_event["utc"])
    persona_aspects = persona["huber_aspects"]
    change_gate = seed_to_persona_change_gate(
        governed, persona_event, radix, persona
    )
    canonical_seed = governed["canonical_seed_chart"]
    seed_chart_comparison = {
        "utc_matches": canonical_seed["utc"] == radix["event"]["utc"],
        "pass_id_matches": canonical_seed["pass_id"]
        == governed["anchor"]["pass_id"],
        "asc_delta_arcseconds": round(
            angular_distance(canonical_seed["asc"], radix["frame"]["asc"])
            * 3600.0,
            9,
        ),
        "mc_delta_arcseconds": round(
            angular_distance(canonical_seed["mc"], radix["frame"]["mc"])
            * 3600.0,
            9,
        ),
        "planet_delta_arcseconds": {
            body: round(
                angular_distance(
                    canonical_seed["positions"][body]["lon"],
                    radix["positions"][body]["longitude"],
                )
                * 3600.0,
                9,
            )
            for body in PLANET_CODES
        },
    }
    if not seed_chart_comparison["utc_matches"] or not seed_chart_comparison[
        "pass_id_matches"
    ]:
        raise RuntimeError("Canonical seed-chart identity mismatch")
    if max(
        seed_chart_comparison["asc_delta_arcseconds"],
        seed_chart_comparison["mc_delta_arcseconds"],
        *seed_chart_comparison["planet_delta_arcseconds"].values(),
    ) > 0.01:
        raise RuntimeError("Current calculator disagrees with canonical seed chart")

    focal: dict[str, Any] = {}
    for body in ("Saturn", "Neptune"):
        focal[body] = {
            "position": persona["positions"][body],
            "distance_from_persona_sun_deg": round(
                angular_distance(
                    persona["positions"][body]["longitude"],
                    persona["positions"]["Sun"]["longitude"],
                ),
                9,
            ),
            "governance_route": persona["governance_routes"][body],
            "aspect_contacts": contacts_for(body, persona_aspects),
        }

    return {
        "schema": "freedom250.deep-current-conjunction-persona/v1",
        "status": "research_only_not_adopted",
        "review_status": "awaiting_katie_review",
        "review_disposition": None,
        "subject": "2026 Saturn-Neptune conjunction persona",
        "question": "How does the 2026 law-meets-the-ideal seed organize itself?",
        "evidence_boundary": {
            "family": "deep_current_persona_charts",
            "admission": "conditional_subordinate_zero_vote",
            "timing_authority": False,
            "event_proof": False,
            "one_shared_chart": True,
            "focal_lenses": ["Saturn", "Neptune"],
        },
        "seed_family": {
            "cycle_id": governed["cycle"]["cycle_id"],
            "seed_family_id": governed["cycle"]["seed_family_id"],
            "seed_family_label": governed["cycle"]["seed_family_label"],
            "anchor_basis": governed["cycle"]["anchor_basis"],
            "display_anchor_pass_id": governed["cycle"]["display_anchor_pass_id"],
            "pass_count": len(governed["cycle"]["passes"]),
            "independent_verification_status": governed["anchor"][
                "independent_verification_status"
            ],
            "registry_validation": governed["registry_validation"],
        },
        "radix": {
            "pass": "single exact geocentric conjunction",
            "target_longitude": target,
            "target_sign": governed["anchor"]["sign"],
            "target_degree_in_sign": governed["anchor"]["degree_in_sign"],
            "calculation_status": governed["anchor"]["calculation_status"],
            "verification": {
                **governed["verification"],
                "canonical_seed_chart_comparison": seed_chart_comparison,
            },
            **radix,
        },
        "persona": {
            "definition": "first later solar conjunction to the fixed shared Saturn-Neptune seed longitude",
            "target_longitude": target,
            "days_after_radix": round(
                persona_event["jd_ut"] - governed["jd_ut"], 9
            ),
            "verification": persona_event["verification"],
            **persona,
            "persona_sun": {
                "whole_sign_house": persona["positions"]["Sun"][
                    "whole_sign_house"
                ],
                "contacts": contacts_for("Sun", persona_aspects),
            },
            "focal_targets_inside_persona": focal,
        },
        "radix_persona_overlay": {
            "orb_policy": (
                "major cross aspects within 2 degrees; Chiron and Node use the "
                "hard-aspect minor-point lane; 916 America only aspects an actual "
                "planet; no independent evidence vote"
            ),
            "contacts": cross_contacts(radix, persona),
        },
        "seed_to_persona_change_gate": change_gate,
        "dependency_ledger": {
            "guaranteed": [
                "Persona Sun repeats the exact 0.752728085 Aries seed longitude.",
                "Persona-Sun contacts to the radix restate contacts already belonging to the seed target.",
            ],
            "dependent": [
                "Saturn and Neptune remain near the Persona Sun because the derived event occurs 28.67 days after the seed.",
                "Slow-planet persistence and near-returns receive no independent interpretive vote.",
                "A derived angle contact to a slow planet's radix near-return is a dependency-labeled echo of the internal persona contact, not corroboration.",
            ],
            "potentially_additive": [
                "derived Ascendant, chart ruler and ruler route",
                "derived houses and Persona-Sun house",
                "actual MC and Whole Sign 10th governance",
                "internal aspect and dispositor architecture",
                "station or direction change, sign change, or a genuinely new aspect/derived-angle relationship inside the short interval",
                "non-mechanical tight radix-persona contacts",
            ],
        },
        "settings": {
            "zodiac": "tropical",
            "center": "geocentric",
            "houses": "Whole Sign",
            "angles": "Swiss Ephemeris houses_ex W frame for Washington DC",
            "rulers": "traditional",
            "node": "true",
            "america_916": "canonical JPL Horizons daily cache; nonacting minor point",
            "minor_point_aspects": (
                "Chiron, true Node, and 916 America to actual planets only; "
                "conjunction, square, or opposition at 2 degrees or less; "
                "no point-to-point aspects"
            ),
            "reference_place_policy": "radix place retained for the persona event",
        },
        "provenance": {
            "seed_registry": str(SEED_REGISTRY),
            "synodic_engine": str(SYNODIC_ENGINE),
            "persona_method": str(PERSONA_METHOD),
            "mundane_house_meanings": str(MUNDANE_REFERENCE),
            "chart_math": str(SENTIENT_SUN / "chart_calculator.py"),
            "structure_engine": str(SENTIENT_SUN / "reading_engine.py"),
            "wheel_engine": str(WHEEL_LIB_PATH),
            "america_916": str(AMERICA_PATH),
            "america_916_cache": str(AMERICA_CACHE),
            "chart_conventions": str(CHART_CONVENTIONS_PATH),
            "builder": str(Path(__file__).resolve()),
            "runtime": {
                "python": sys.version.split()[0],
                "pyswisseph": swe.version,
                "chart_calculator_requested_flags": ["FLG_SWIEPH", "FLG_SPEED"],
                "seed_independent_check_flags": ["FLG_MOSEPH", "FLG_SPEED"],
                "persona_primary_solver": "solcross_ut with FLG_SWIEPH",
                "persona_independent_solver": "bisection with FLG_MOSEPH",
            },
        },
        "_raw_chart_objects_excluded": {
            "radix_jd": round(float(radix_raw["jd"]), 12),
            "persona_jd": round(float(persona_raw["jd"]), 12),
        },
    }


def degree_label(longitude: float, seconds: bool = True) -> str:
    sign = SIGNS[int(longitude // 30) % 12]
    value = longitude % 30.0
    degree = int(value)
    minute_value = (value - degree) * 60.0
    minute = int(minute_value)
    second = (minute_value - minute) * 60.0
    if seconds:
        return f"{degree}°{minute:02d}′{second:05.2f}″ {sign}"
    return f"{degree}°{minute:02d}′ {sign}"


def wheel_positions(chart: dict[str, Any]) -> list[list[Any]]:
    positions: list[list[Any]] = []
    for body in BODY_ORDER:
        if body == "America":
            position = chart["minor_points"]["america_916"]
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


def wheel_record(chart: dict[str, Any], title: str, cap1: str, cap2: str) -> dict[str, Any]:
    positions = wheel_positions(chart)
    operator = {
        "conjunction": "conjunct",
        "sextile": "sextile",
        "square": "square",
        "trine": "trine",
        "opposition": "opposite",
    }
    major_aspects = [
        {
            "t": f"{row['a']} {operator[row['aspect']]} {row['b']}",
            "o": round(row["orb_deg"], 2),
            "x": 1 if row["orb_deg"] <= 0.3 else 0,
            "ap": 1 if row["applying"] else 0,
            "pt": 0,
        }
        for row in chart["mundane_major_aspects"]
    ]
    point_aspects = [
        {
            "t": f"{row['a']} {operator[row['aspect']]} {row['b']}",
            "o": round(row["orb_deg"], 2),
            "x": 1 if row["orb_deg"] <= 0.3 else 0,
            "ap": 1 if row["applying"] else 0,
            "pt": 1,
        }
        for row in chart["minor_point_aspects"]
    ]
    aspects = major_aspects + point_aspects
    return {
        "asc": round(chart["frame"]["asc"], 8),
        "mc": round(chart["frame"]["mc"], 8),
        "pos": positions,
        "asp": aspects,
        "__date": title,
        "cap1": cap1,
        "cap2": cap2,
    }


def render_svg(
    record: dict[str, Any], outer_name: str | None = None, outer_map: dict[str, float] | None = None
) -> str:
    runner = [WHEEL.WHEEL_JS]
    if outer_name and outer_map:
        runner.append(f"\nconst CHARTS={json.dumps({outer_name: outer_map})};")
        runner.append(f"\nconst REC={json.dumps(record, ensure_ascii=False)};")
        runner.append(
            f"\nprocess.stdout.write(wheelSVG(REC,{json.dumps(outer_name)},true));"
        )
    else:
        runner.append("\nconst CHARTS={};")
        runner.append(f"\nconst REC={json.dumps(record, ensure_ascii=False)};")
        runner.append("\nprocess.stdout.write(wheelSVG(REC,null,false));")
    with tempfile.NamedTemporaryFile(
        "w", suffix=".mjs", delete=False, encoding="utf-8"
    ) as handle:
        handle.write("".join(runner))
        script = Path(handle.name)
    try:
        result = subprocess.run(
            ["node", str(script)],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
    finally:
        script.unlink(missing_ok=True)
    if result.returncode != 0 or not result.stdout.startswith("<svg"):
        raise RuntimeError(
            f"Wheel engine failed ({result.returncode}): {result.stderr[:1000]}"
        )
    svg = result.stdout
    if outer_name and outer_map:
        svg = svg.replace(
            'viewBox="0 0 660 660"',
            'viewBox="-60 -60 780 780"',
            1,
        )
    return svg


def gallery_html(data: dict[str, Any], standalone: str, biwheel: str) -> str:
    radix = data["radix"]
    persona = data["persona"]
    frame = persona["frame"]
    route = " → ".join(frame["chart_ruler_route"]["chain"])
    seed_local = datetime.fromisoformat(radix["event"]["local"]).astimezone(ZONE)
    persona_local = datetime.fromisoformat(persona["event"]["local"]).astimezone(ZONE)
    seed_label = seed_local.strftime("%d %b %Y · %H:%M:%S %Z")
    persona_label = persona_local.strftime("%d %b %Y · %H:%M:%S %Z")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>2026 Saturn–Neptune · Conjunction Persona</title>
<style>
  :root {{ --paper:#f8f5ed; --card:#fffdf8; --ink:#302b23; --muted:#786f61; --line:#d8ccb5; --accent:#574878; --wash:#eee8dc; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--paper); color:var(--ink); font-family:"Iowan Old Style",Palatino,Georgia,serif; }}
  main {{ width:min(1460px,96vw); margin:0 auto; padding:42px 0 72px; }}
  h1,h2,p {{ margin-top:0; }}
  h1 {{ font-size:clamp(2rem,4vw,3.7rem); font-weight:400; margin-bottom:10px; }}
  h2 {{ font-size:1.65rem; font-weight:400; }}
  p {{ color:var(--muted); line-height:1.55; }}
  .eyebrow {{ color:var(--accent); font-size:.72rem; font-weight:700; letter-spacing:.13em; }}
  .notice {{ margin:20px 0; padding:15px 18px; border:1px solid var(--line); border-left:4px solid var(--accent); border-radius:12px; background:var(--card); color:var(--ink); }}
  .facts {{ display:flex; flex-wrap:wrap; gap:8px; margin:16px 0 26px; }}
  .facts span {{ padding:6px 10px; border-radius:8px; background:var(--wash); color:var(--muted); }}
  .pair {{ display:grid; grid-template-columns:1fr 1fr; gap:24px; }}
  article {{ background:var(--card); border:1px solid var(--line); border-radius:16px; padding:20px; box-shadow:0 8px 30px rgba(50,42,28,.05); }}
  .wheel img {{ width:100%; height:auto; display:block; }}
  .boundary {{ margin-top:28px; }}
  code {{ color:var(--accent); }}
  a {{ color:var(--accent); text-underline-offset:3px; }}
  footer {{ margin-top:34px; color:var(--muted); line-height:1.5; }}
  @media(max-width:900px) {{ .pair {{ grid-template-columns:1fr; }} }}
</style>
</head>
<body>
<main>
  <header>
    <p class="eyebrow">FREEDOM 250 · LONG CLOCKS · RESEARCH-ONLY PERSONA PILOT</p>
    <h1>2026 Saturn–Neptune Conjunction Persona</h1>
    <p>One shared derived chart for the cycle seed called “law meets the ideal.” Saturn and Neptune remain two focal functions inside one chart, not two personas or two votes.</p>
    <div class="notice"><b>Research boundary.</b> Conditional, subordinate, and zero-vote. This chart asks how the seed organizes itself; it does not time events, validate present-day claims, or amend the live mundane method.</div>
    <div class="facts">
      <span><b>Seed</b> {html.escape(seed_label)}</span>
      <span><b>Shared degree</b> {degree_label(radix['target_longitude'])}</span>
      <span><b>Persona event</b> {html.escape(persona_label)}</span>
      <span><b>Persona ASC</b> {degree_label(frame['asc'])}</span>
      <span><b>Persona MC</b> {degree_label(frame['mc'])}</span>
      <span><b>Persona Sun</b> H{persona['persona_sun']['whole_sign_house']}</span>
      <span><b>Chart-ruler route</b> {html.escape(route)}</span>
    </div>
  </header>
  <section class="pair">
    <article>
      <h2>Conjunction persona alone</h2>
      <p>The derived event’s own Aquarius Ascendant, Whole Sign houses, planetary web, and nonacting 916 America point.</p>
      <div class="wheel"><img src="{html.escape(standalone, quote=True)}" alt="Saturn Neptune conjunction persona chart"></div>
      <a href="{html.escape(standalone, quote=True)}">Open standalone SVG</a>
    </article>
    <article>
      <h2>Persona around the exact seed radix</h2>
      <p>The single exact February conjunction inside; the first later solar contact on the outer ring.</p>
      <div class="wheel"><img src="{html.escape(biwheel, quote=True)}" alt="Saturn Neptune seed and persona biwheel"></div>
      <a href="{html.escape(biwheel, quote=True)}">Open biwheel SVG</a>
    </article>
  </section>
  <article class="boundary">
    <h2>What can and cannot add information</h2>
    <p><b>Guaranteed:</b> the Persona Sun repeats 0°45′ Aries. <b>Dependent:</b> Saturn and Neptune remain nearby only 28.67 days after the seed. A slow-body near-return is carryover, not news, unless a station/direction change, sign change, or genuinely new relationship qualifies. <b>Potentially additive:</b> Aquarius rising, the third-house derived arena, ruler and dispositor circuitry, MC governance, internal aspect structure, and non-mechanical tight overlays.</p>
    <p>Read the complete comparative hearing in <a href="../SATURN_NEPTUNE_2026_PERSONA_HEARING.md">SATURN_NEPTUNE_2026_PERSONA_HEARING.md</a>.</p>
  </article>
  <footer>Tropical · geocentric · Washington, D.C. · Whole Sign · traditional rulers · true node. Seed identity comes from the canonical Long Clocks registry. Chart facts use the current Sentient Sun calculator and structure engine. 916 America comes from the canonical JPL Horizons daily cache and remains a nonacting minor point. External Astro Gold verification of the seed is pending.</footer>
</main>
</body>
</html>
"""


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    CHARTS.mkdir(parents=True, exist_ok=True)
    data = calculate()
    DATA_PATH.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    radix = data["radix"]
    persona = data["persona"]
    persona_event = datetime.fromisoformat(persona["event"]["local"]).astimezone(ZONE)
    event_label = persona_event.strftime("%d %b %Y · %H:%M:%S %Z")
    standalone_record = wheel_record(
        persona,
        "SATURN–NEPTUNE CONJUNCTION PERSONA",
        f"{event_label} · {PLACE}",
        "research-only derived chart · Whole Sign",
    )
    radix_record = wheel_record(
        radix,
        "SEED RADIX + CONJUNCTION PERSONA",
        "20 Feb 2026 exact conjunction inside · persona outside",
        f"outer ring: shared conjunction persona · {event_label}",
    )
    outer_map = {
        row[0]: float(row[4]) for row in wheel_positions(persona)
    }
    standalone_svg = render_svg(standalone_record)
    biwheel_svg = render_svg(
        radix_record,
        outer_name="Saturn-Neptune Conjunction Persona",
        outer_map=outer_map,
    )
    standalone_name = "Saturn–Neptune 2026 — Conjunction Persona — Standalone.svg"
    biwheel_name = "Saturn–Neptune 2026 — Conjunction Persona + Radix — Biwheel.svg"
    standalone_path = CHARTS / standalone_name
    biwheel_path = CHARTS / biwheel_name
    standalone_path.write_text(standalone_svg, encoding="utf-8")
    biwheel_path.write_text(biwheel_svg, encoding="utf-8")
    GALLERY_PATH.write_text(
        gallery_html(data, standalone_name, biwheel_name),
        encoding="utf-8",
    )
    manifest = {
        "schema": "freedom250.deep-current-conjunction-persona-manifest/v1",
        "status": data["status"],
        "review_status": data["review_status"],
        "review_disposition": data["review_disposition"],
        "seed": {
            "cycle_id": data["seed_family"]["cycle_id"],
            "pass_id": data["seed_family"]["display_anchor_pass_id"],
            "utc": radix["event"]["utc"],
            "target_longitude": radix["target_longitude"],
            "external_verification": data["seed_family"][
                "independent_verification_status"
            ],
        },
        "persona": {
            "utc": persona["event"]["utc"],
            "local": persona["event"]["local"],
            "sun_residual_arcseconds": persona["verification"][
                "sun_minus_target_arcseconds"
            ],
        },
        "outputs": {
            "data": DATA_PATH.name,
            "gallery": GALLERY_PATH.name,
            "standalone_svg": standalone_name,
            "biwheel_svg": biwheel_name,
        },
        "sha256": {
            DATA_PATH.name: sha256(DATA_PATH),
            GALLERY_PATH.name: sha256(GALLERY_PATH),
            standalone_name: sha256(standalone_path),
            biwheel_name: sha256(biwheel_path),
            Path(__file__).name: sha256(Path(__file__)),
        },
        "source_sha256": {
            str(path): sha256(path)
            for path in (
                SEED_REGISTRY,
                SYNODIC_ENGINE,
                CHART_CONVENTIONS_PATH,
                PERSONA_METHOD,
                MUNDANE_REFERENCE,
                SENTIENT_SUN / "chart_calculator.py",
                SENTIENT_SUN / "reading_engine.py",
                WHEEL_LIB_PATH,
                AMERICA_PATH,
                AMERICA_CACHE,
            )
        },
        "provenance": data["provenance"],
        "runtime": data["provenance"]["runtime"],
    }
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(GALLERY_PATH)
    print(DATA_PATH)
    print(MANIFEST_PATH)
    print("Rendered one shared persona wheel and one exact-seed biwheel")


if __name__ == "__main__":
    main()
