#!/usr/bin/env python3
"""Deterministic Sun–ASC daily frames for the Freedom 250 Daybreak Almanac.

This engine is deliberately factual.  It casts one Washington, D.C. chart at
the instant the geocentric solar centre crosses the Ascendant, then nests that
chart beneath registered ingress and lunation charts and the ten Long Clocks.
The daybreak frame never acquires governing standing and never ranks stories.

The geometric-rise seed uses Swiss Ephemeris with disc centre and refraction
disabled.  A short root solve then makes the actual chart definition exact:
Sun longitude == Ascendant longitude.  A frame runs from that crossing to the
next crossing.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import importlib.util
import json
import os
from functools import lru_cache
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import swisseph as swe


HERE = Path(__file__).resolve().parent
DEFAULT_VAULT_ROOT = Path(os.environ.get("F250_DAYBREAK_VAULT_ROOT", str(HERE.parent)))
SCHEMA = "f250.daybreak-frames/v1"
FRAME_METHOD_ID = "dc-sun-asc-geometric-centre/v1"

DC_LAT = 38.9072
DC_LON = -77.0369
DC_ALT_METRES = 0.0
DC_TZ_NAME = "America/New_York"
DC_TZ = ZoneInfo(DC_TZ_NAME)
UTC = dt.timezone.utc

SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces",
]
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
PLANET_ORDER = list(PLANET_CODES)
ASPECT_POINT_ORDER = PLANET_ORDER + ["America"]
RULER = {
    "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury",
    "Cancer": "Moon", "Leo": "Sun", "Virgo": "Mercury",
    "Libra": "Venus", "Scorpio": "Mars", "Sagittarius": "Jupiter",
    "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter",
}
HOUSE_MEANINGS = {
    1: "the people / national body",
    2: "treasury / revenue / material resources",
    3: "press / communications / transport",
    4: "land / opposition / foundations",
    5: "markets / children / national pleasure",
    6: "workers / health / armed services",
    7: "foreign powers / open opponents",
    8: "debt / mortality / shared finance",
    9: "courts / law / religion / long trade",
    10: "government / executive / national standing",
    11: "legislature / allies / public hopes",
    12: "hidden actors / confinement / undoing",
}
MAJOR_ASPECTS = [
    ("conjunction", 0.0, 8.0),
    ("sextile", 60.0, 5.0),
    ("square", 90.0, 7.0),
    ("trine", 120.0, 7.0),
    ("opposition", 180.0, 8.0),
]
CROSS_CONTACT_LIMIT_DEG = 3.0
import sys as _sys  # noqa: E402
if str(HERE) not in _sys.path:
    _sys.path.insert(0, str(HERE))
from swiss_ephemeris import FLAGS, EPHEMERIS_LABEL  # noqa: E402  2026-09-25: Swiss/JPL files, never silent Moshier
RISE_FLAGS = swe.CALC_RISE | swe.BIT_DISC_CENTER | swe.BIT_NO_REFRACTION


def _iso(moment: dt.datetime) -> str:
    return moment.isoformat(timespec="microseconds")


def _jd(moment: dt.datetime) -> float:
    if moment.tzinfo is None:
        raise ValueError("Daybreak moments must be timezone-aware")
    value = moment.astimezone(UTC)
    hour = value.hour + value.minute / 60 + value.second / 3600 + value.microsecond / 3_600_000_000
    return swe.julday(value.year, value.month, value.day, hour)


def _moment(jd_ut: float) -> dt.datetime:
    year, month, day, hour = swe.revjul(jd_ut, swe.GREG_CAL)
    return dt.datetime(year, month, day, tzinfo=UTC) + dt.timedelta(hours=hour)


def _signed_delta(angle: float, target: float) -> float:
    return ((angle - target + 180.0) % 360.0) - 180.0


def sign_of(longitude: float) -> str:
    return SIGNS[int((longitude % 360.0) // 30.0) % 12]


def degree_label(longitude: float) -> str:
    value = longitude % 360.0
    degree = value % 30.0
    whole = int(degree)
    minute = int(round((degree - whole) * 60))
    if minute == 60:
        whole = (whole + 1) % 30
        minute = 0
    return f"{whole}°{minute:02d}' {sign_of(value)}"


def strength(orb: float) -> str:
    if orb <= 0.25:
        return "exact"
    if orb <= 1.5:
        return "tight"
    return "active"


def _solar_asc_delta(jd_ut: float) -> float:
    sun = swe.calc_ut(jd_ut, swe.SUN, FLAGS)[0][0] % 360.0
    asc = swe.houses(jd_ut, DC_LAT, DC_LON, b"W")[1][0] % 360.0
    return _signed_delta(sun, asc)


@lru_cache(maxsize=1600)
def sun_asc_crossing(date_iso: str) -> dict[str, Any]:
    """Return the exact D.C. Sun–ASC crossing for one local calendar date."""
    day = dt.date.fromisoformat(date_iso)
    local_midnight = dt.datetime.combine(day, dt.time(0, 0), tzinfo=DC_TZ)
    jd_start = _jd(local_midnight)
    result, times = swe.rise_trans(
        jd_start,
        swe.SUN,
        RISE_FLAGS,
        (DC_LON, DC_LAT, DC_ALT_METRES),
    )
    if result < 0:
        raise RuntimeError(f"Swiss Ephemeris found no geometric sunrise for {date_iso}")
    guess = times[0]

    # The geometric-centre sunrise is already within seconds of Sun == ASC.
    # Bracket generously so a future Swiss Ephemeris revision still fails loud.
    lo, hi = guess - 0.025, guess + 0.025
    flo, fhi = _solar_asc_delta(lo), _solar_asc_delta(hi)
    for _ in range(5):
        if flo == 0 or fhi == 0 or flo * fhi < 0:
            break
        lo -= 0.025
        hi += 0.025
        flo, fhi = _solar_asc_delta(lo), _solar_asc_delta(hi)
    if flo * fhi > 0:
        raise RuntimeError(
            f"Could not bracket Sun–ASC crossing for {date_iso}: {flo:.6f}, {fhi:.6f}"
        )
    for _ in range(64):
        mid = (lo + hi) / 2.0
        fmid = _solar_asc_delta(mid)
        if flo * fmid <= 0:
            hi, fhi = mid, fmid
        else:
            lo, flo = mid, fmid
    jd_ut = (lo + hi) / 2.0
    moment_utc = _moment(jd_ut)
    local = moment_utc.astimezone(DC_TZ)
    if local.date() != day:
        raise RuntimeError(f"Sun–ASC crossing escaped requested D.C. date: {date_iso} -> {local}")
    sun = swe.calc_ut(jd_ut, swe.SUN, FLAGS)[0][0] % 360.0
    ascmc = swe.houses(jd_ut, DC_LAT, DC_LON, b"W")[1]
    asc, mc = ascmc[0] % 360.0, ascmc[1] % 360.0
    residual = _signed_delta(sun, asc) * 3600.0
    return {
        "date": date_iso,
        "jd_ut": jd_ut,
        "utc": _iso(moment_utc),
        "local": _iso(local),
        "clock": local.strftime("%-I:%M:%S %p %Z"),
        "asc": asc,
        "mc": mc,
        "sun": sun,
        "sun_asc_residual_arcsec": residual,
    }


def _planet_position(jd_ut: float, body: str) -> dict[str, Any]:
    ecl = swe.calc_ut(jd_ut, PLANET_CODES[body], FLAGS)[0]
    equ = swe.calc_ut(jd_ut, PLANET_CODES[body], FLAGS | swe.FLG_EQUATORIAL)[0]
    lon = ecl[0] % 360.0
    return {
        "lon": round(lon, 9),
        "lat": round(ecl[1], 9),
        "spd": round(ecl[3], 9),
        "dec": round(equ[1], 9),
        "retro": bool(ecl[3] < 0),
        "sign": sign_of(lon),
        "deg_in_sign": round(lon % 30.0, 6),
        "label": degree_label(lon),
    }


def _america_position(jd_ut: float, vault_root: Path) -> dict[str, Any]:
    moment = _moment(jd_ut)
    longitude, speed, key0, key1 = _canonical_america(moment, Path(vault_root))
    return {
        "lon": round(longitude, 9),
        "lat": None,
        "spd": round(speed, 9),
        "dec": None,
        "retro": bool(speed < 0),
        "sign": sign_of(longitude),
        "deg_in_sign": round(longitude % 30.0, 6),
        "label": degree_label(longitude),
        "authority": "america_ephemeris.json",
        "interpolation": "shortest_signed_arc_between_00_utc_daily_rows",
        "bracket_dates": [key0, key1],
    }



def _whole_sign_house(longitude: float, asc: float) -> int:
    return ((int(longitude // 30) - int(asc // 30)) % 12) + 1


def _dispositor_structure(positions: dict[str, dict[str, Any]], chart_ruler: str) -> dict[str, Any]:
    path: list[str] = []
    seen: dict[str, int] = {}
    current = chart_ruler
    while True:
        if current in seen:
            loop_members = path[seen[current]:]
            return {
                "path": path + [current],
                "loop": True,
                "root_members": sorted(set(loop_members), key=PLANET_ORDER.index),
            }
        seen[current] = len(path)
        path.append(current)
        current = RULER[positions[current]["sign"]]


def _aspect_candidate(longitude_a: float, longitude_b: float) -> tuple[str, float, float, float]:
    separation = abs(_signed_delta(longitude_b, longitude_a))
    aspect_id, angle, limit = min(MAJOR_ASPECTS, key=lambda row: abs(separation - row[1]))
    return aspect_id, angle, abs(separation - angle), limit


def _internal_aspects(jd_ut: float, positions: dict[str, dict[str, Any]], vault_root: Path) -> list[dict[str, Any]]:
    future = {body: swe.calc_ut(jd_ut + 1 / 24.0, code, FLAGS)[0][0] % 360.0 for body, code in PLANET_CODES.items()}
    future["America"] = _america_position(jd_ut + 1 / 24.0, vault_root)["lon"]
    rows: list[dict[str, Any]] = []
    for index, body_a in enumerate(ASPECT_POINT_ORDER):
        for body_b in ASPECT_POINT_ORDER[index + 1:]:
            aspect_id, angle, orb, limit = _aspect_candidate(positions[body_a]["lon"], positions[body_b]["lon"])
            if orb > limit:
                continue
            _, _, future_orb, _ = _aspect_candidate(future[body_a], future[body_b])
            separation = abs(_signed_delta(positions[body_b]["lon"], positions[body_a]["lon"]))
            rows.append({
                "a": body_a,
                "b": body_b,
                "aspect_id": aspect_id,
                "angle_deg": angle,
                "orb_deg": round(orb, 6),
                "orb_limit_deg": limit,
                "strength": strength(orb),
                "applying": future_orb < orb,
                "separating": future_orb >= orb,
                "separation_deg": round(separation, 6),
            })
    rows.sort(key=lambda row: (row["orb_deg"], ASPECT_POINT_ORDER.index(row["a"]), ASPECT_POINT_ORDER.index(row["b"])))
    return rows


def cast_daybreak(date_iso: str, *, vault_root: Path = DEFAULT_VAULT_ROOT) -> dict[str, Any]:
    vault_root = Path(vault_root)
    crossing = sun_asc_crossing(date_iso)
    next_day = (dt.date.fromisoformat(date_iso) + dt.timedelta(days=1)).isoformat()
    next_crossing = sun_asc_crossing(next_day)
    jd_ut = crossing["jd_ut"]
    asc, mc = crossing["asc"], crossing["mc"]
    positions = {body: _planet_position(jd_ut, body) for body in PLANET_ORDER}
    positions["America"] = _america_position(jd_ut, vault_root)
    for body in ASPECT_POINT_ORDER:
        house = _whole_sign_house(positions[body]["lon"], asc)
        positions[body]["house"] = house
        positions[body]["house_meaning"] = HOUSE_MEANINGS[house]
    asc_sign = sign_of(asc)
    chart_ruler = RULER[asc_sign]
    dispositors = _dispositor_structure(positions, chart_ruler)
    angular = [
        {"body": body, "house": positions[body]["house"], "label": positions[body]["label"]}
        for body in ASPECT_POINT_ORDER if positions[body]["house"] in {1, 4, 7, 10}
    ]
    focal = []
    for point in ["Sun", "Moon", "ASC", "MC", "America", chart_ruler, *dispositors["root_members"], *(item["body"] for item in angular)]:
        if point not in focal:
            focal.append(point)
    point_longitudes = {body: positions[body]["lon"] for body in ASPECT_POINT_ORDER}
    point_longitudes.update({"ASC": asc, "MC": mc})
    wheel_positions = [
        [body, positions[body]["sign"], degree_label(positions[body]["lon"]).split()[0], 1 if positions[body]["retro"] else 0, round(positions[body]["lon"], 6)]
        for body in ASPECT_POINT_ORDER
    ]
    chart = {
        "asc": round(asc, 9),
        "mc": round(mc, 9),
        "asc_sign": asc_sign,
        "mc_sign": sign_of(mc),
        "ruler": chart_ruler,
        "dispositors": dispositors,
        "root_members": dispositors["root_members"],
        "positions": positions,
        "point_longitudes": {key: round(value, 9) for key, value in point_longitudes.items()},
        "focal_points": focal,
        "angular_planets": angular,
        "aspects": _internal_aspects(jd_ut, positions, vault_root),
        "wheel": {
            "pos": wheel_positions,
            "asp": [],
            "asc": round(asc, 6),
            "cap1": f"Sun crossed the D.C. Ascendant · {crossing['clock']}",
            "cap2": "one exact instant · Whole Sign · subordinate daily frame",
        },
        "sunrise": {
            "method_id": FRAME_METHOD_ID,
            "utc": crossing["utc"],
            "local": crossing["local"],
            "clock": crossing["clock"],
            "jd_ut": round(jd_ut, 9),
            "sun_asc_residual_arcsec": round(crossing["sun_asc_residual_arcsec"], 9),
            "next_utc": next_crossing["utc"],
            "next_local": next_crossing["local"],
            "interval_basis": "this exact Sun–ASC crossing up to, but not including, the next",
        },
    }
    frame_id = f"daybreak-{date_iso}"
    for row in chart["aspects"]:
        row["geometry_id"] = (
            f"{frame_id}:internal:{row['a']}:{row['aspect_id']}:{row['b']}"
        )
    return chart



def _load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def _chart_registry(vault_root: Path) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    index = _load_json(vault_root / "99 - Templates" / "chart_reading_bones" / "index.json")
    charts = index.get("charts", [])
    return charts, {row["id"]: row for row in charts}


def _bone(vault_root: Path, chart_id: str) -> dict[str, Any]:
    return _load_json(vault_root / "99 - Templates" / "chart_reading_bones" / f"{chart_id}.json")


def _chart_label(meta: dict[str, Any], bone: dict[str, Any]) -> str:
    if meta["type"] == "ingress":
        return f"{meta['year']} {meta['sign']} Ingress"
    eclipse = bone.get("eclipse")
    kind = "New Moon" if meta.get("kind") == "new" else "Full Moon"
    if eclipse:
        kind = "Solar Eclipse" if str(eclipse).lower().startswith("solar") else "Lunar Eclipse"
    return f"{kind} · {meta.get('sign', '')} {meta.get('deg', '')}°"


def _chart_summary(vault_root: Path, meta: dict[str, Any]) -> dict[str, Any]:
    return _chart_summary_cached(str(Path(vault_root)), meta["id"], json.dumps(meta, sort_keys=True))



def resolve_context(
    date_iso: str,
    charts: list[dict[str, Any]],
    *,
    vault_root: Path = DEFAULT_VAULT_ROOT,
) -> dict[str, str | None]:
    """Compatibility wrapper: resolve the context at that date's Daybreak start."""
    crossing = sun_asc_crossing(date_iso)
    return resolve_context_at(
        _aware(crossing["utc"], field="Daybreak UTC"), charts, vault_root=Path(vault_root)
    )



def _cross_contacts(
    daily: dict[str, Any],
    parent: dict[str, Any] | None,
) -> list[dict[str, Any]]:
    if parent is None:
        return []
    rows: list[dict[str, Any]] = []
    source_points = daily["point_longitudes"]
    for source in daily["focal_points"]:
        source_lon = source_points[source]
        for target, target_lon in parent["targets"].items():
            aspect_id, angle, orb, _ = _aspect_candidate(source_lon, target_lon)
            if orb > CROSS_CONTACT_LIMIT_DEG:
                continue
            rows.append({
                "source": source,
                "source_lon_deg": round(source_lon, 6),
                "aspect_id": aspect_id,
                "angle_deg": angle,
                "target": target,
                "target_lon_deg": round(target_lon, 6),
                "orb_deg": round(orb, 6),
                "strength": strength(orb),
                "continuity": bool(source == target and source in {"Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"} and aspect_id == "conjunction"),
                "parent_chart_id": parent["chart_id"],
            })
    rows.sort(key=lambda row: (row["orb_deg"], daily["focal_points"].index(row["source"]), row["target"]))
    return rows


@lru_cache(maxsize=4)
def _load_synodic(vault_root_value: str):
    path = Path(vault_root_value) / "99 - Templates" / "synodic_cycles.py"
    spec = importlib.util.spec_from_file_location("f250_daybreak_synodic", path)
    if not spec or not spec.loader:
        raise RuntimeError(f"Cannot load Long Clocks engine: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _long_clock_delivery(date_iso: str, daily: dict[str, Any], vault_root: Path) -> dict[str, Any]:
    syn = _load_synodic(str(vault_root))
    registry = syn.load_seed_registry(vault_root / "99 - Templates" / "synodic_seed_families.json")
    by_id = syn.seed_registry_index(registry)
    moment = dt.datetime.fromisoformat(daily["sunrise"]["utc"])
    snapshot = syn.current_snapshot(moment, vault_root=vault_root, registry=registry)
    pseudo_bone = {
        "pos": {
            "Sun": {"lon": daily["positions"]["Sun"]["lon"]},
            "Moon": {"lon": daily["positions"]["Moon"]["lon"]},
        },
        "asc": daily["asc"],
        "mc": daily["mc"],
        "root_members": daily["root_members"],
        "ruler": daily["ruler"],
        "us_hits_sag": [],
    }
    cycles = []
    for state in snapshot["cycles"]:
        nameability = syn.phase_nameability(pseudo_bone, by_id[state["cycle_id"]])
        cycles.append({
            "cycle_id": state["cycle_id"],
            "tier_id": state["tier_id"],
            "pair": state["pair"],
            "geometry": {
                "elongation_deg": state["geometry"]["elongation_deg"],
                "phase_name": state["geometry"]["phase_name"],
                "phase_direction": state["geometry"]["phase_direction"],
                "nearest_chapter_id": state["geometry"]["nearest_chapter_id"],
                "nearest_chapter_orb_deg": state["geometry"]["nearest_chapter_orb_deg"],
            },
            "active_aspect": state["active_aspect"],
            "nameability": nameability,
        })
    frame_id = f"daybreak-{date_iso}"
    echoes = [
        {
            "cycle_id": row["cycle_id"],
            "seed_family_id": row["seed_family_id"],
            "matched_pass_id": row["matched_pass_id"],
            "point": row["point"],
            "point_group": row["point_group"],
            "point_lon_deg": row["point_lon_deg"],
            "aspect_id": row["aspect_id"],
            "orb_deg": row["orb_deg"],
            "strength": row["strength"],
            "seed_lon_deg": row["seed_lon_deg"],
        }
        for row in syn.seed_echoes(frame_id, pseudo_bone, registry)
    ]
    edges = []
    for state in cycles:
        if not state["active_aspect"]:
            continue
        edges.append({
            "cycle_id": state["cycle_id"],
            "pair": state["pair"],
            "tier_id": state["tier_id"],
            "phase_name": state["geometry"]["phase_name"],
            "phase_direction": state["geometry"]["phase_direction"],
            "nameability": state["nameability"],
            **state["active_aspect"],
        })
    edges.sort(key=lambda row: (row["orb_deg"], row["cycle_id"]))
    delivery = {
        "utc": snapshot["utc"],
        "cycles": cycles,
        "active_edges": edges,
        "seed_echoes": echoes,
        "active_cycle_ids": [row["cycle_id"] for row in edges],
    }
    frame_id = f"daybreak-{date_iso}"
    for row in delivery["cycles"]:
        row["geometry_id"] = f"{frame_id}:clock-cycle:{row['cycle_id']}"
    for row in delivery["active_edges"]:
        row["geometry_id"] = (
            f"{frame_id}:clock-edge:{row['cycle_id']}:{row['chapter_id']}"
        )
    for row in delivery["seed_echoes"]:
        row["geometry_id"] = (
            f"{frame_id}:seed-echo:{row['cycle_id']}:{row['matched_pass_id']}:"
            f"{row['point']}:{row['aspect_id']}"
        )
        row["reference_id"] = row["geometry_id"]
        row["structural_mirror"] = False
        row["mirror_family_id"] = None
        row["mirror_roles"] = []
        row["independent_occurrence"] = True
    echo_groups: dict[tuple[str, str, str, str], list[dict[str, Any]]] = {}
    for row in delivery["seed_echoes"]:
        if row["point"] in {"Sun", "ASC"}:
            key = (
                row["cycle_id"], row["matched_pass_id"], row["aspect_id"],
                f"{row['seed_lon_deg']:.9f}",
            )
            echo_groups.setdefault(key, []).append(row)
    for (cycle_id, pass_id, aspect_id, _seed_lon), candidates in echo_groups.items():
        roles = {row["point"] for row in candidates}
        if roles != {"Sun", "ASC"}:
            continue
        family_id = f"{frame_id}:seed-echo:{cycle_id}:{pass_id}:SunASC:{aspect_id}"
        for row in candidates:
            row["reference_id"] = family_id
            row["structural_mirror"] = True
            row["mirror_family_id"] = family_id
            row["mirror_roles"] = ["Sun", "ASC"]
            row["independent_occurrence"] = row["point"] == "Sun"
    return delivery



def _seed_charts(vault_root: Path) -> dict[str, dict[str, Any]]:
    syn = _load_synodic(str(vault_root))
    registry_path = vault_root / "99 - Templates" / "synodic_seed_families.json"
    registry = syn.load_seed_registry(registry_path)
    out: dict[str, dict[str, Any]] = {}
    for cycle in registry["cycles"]:
        chart = syn.seed_chart(cycle["cycle_id"], vault_root=vault_root, seed_registry_path=registry_path)
        wheel = {body: round(value["lon"], 9) for body, value in chart["positions"].items()}
        try:
            wheel["America"] = round(_america_position(chart["jd_ut"], vault_root)["lon"], 9)
            america_status = "computed_from_canonical_cache"
        except ValueError:
            # Historical seed epochs precede the 2024–2031 Horizons grid.  The
            # canonical America helper explicitly forbids extrapolation.
            america_status = "unresolved_outside_canonical_cache"
        wheel["ASC"] = round(chart["asc"], 9)
        out[cycle["cycle_id"]] = {
            "cycle_id": cycle["cycle_id"],
            "pair": cycle["pair"],
            "label": f"{cycle['pair'][0]}–{cycle['pair'][1]} seed",
            "seed_family_label": cycle["seed_family_label"],
            "pass_id": chart["pass_id"],
            "utc": chart["utc"],
            "asc": round(chart["asc"], 9),
            "mc": round(chart["mc"], 9),
            "america_status": america_status,
            "wheel": wheel,
        }
    return out


def _cohort(date_iso: str, experiment: dict[str, Any]) -> dict[str, Any]:
    for cohort in experiment.get("cohorts", []):
        if cohort["start"] <= date_iso <= cohort["end"]:
            return {
                "cohort_id": cohort["cohort_id"],
                "label": cohort["label"],
                "basis": cohort["basis"],
                "frozen_at": cohort.get("frozen_at"),
            }
    return {
        "cohort_id": "reference",
        "label": "Reference frame",
        "basis": "computed factual frame outside the scored experiment windows",
        "frozen_at": None,
    }


def baseline_core(frame: dict[str, Any]) -> dict[str, Any]:
    """Stable factual subset frozen for the prospective experiment."""
    core = {
        "frame_id": frame["frame_id"],
        "date": frame["date"],
        "sunrise_utc": frame["chart"]["sunrise"]["utc"],
        "asc": frame["chart"]["asc"],
        "mc": frame["chart"]["mc"],
        "ruler": frame["chart"]["ruler"],
        "root_members": frame["chart"]["root_members"],
        "hierarchy": frame["hierarchy"],
        "contacts": frame["contacts"],
        "active_edges": frame["long_clocks"]["active_edges"],
        "seed_echoes": frame["long_clocks"]["seed_echoes"],
    }
    core = json.loads(json.dumps(core))

    def strip_geometry_id(value: Any) -> None:
        if isinstance(value, dict):
            for key in (
                "geometry_id", "reference_id", "structural_mirror",
                "mirror_family_id", "mirror_roles", "independent_occurrence",
            ):
                value.pop(key, None)
            for item in value.values():
                strip_geometry_id(item)
        elif isinstance(value, list):
            for item in value:
                strip_geometry_id(item)

    strip_geometry_id(core)
    # The frozen v1 baseline predates the explicit America self-continuity
    # classification.  Keep that historical hash surface while the live
    # payload exposes the corrected non-trigger flag.
    for rows in core["contacts"].values():
        for row in rows:
            if (
                row["source"] == "America"
                and row["target"] == "America"
                and row["aspect_id"] == "conjunction"
            ):
                row["continuity"] = False
    return core



def canonical_sha256(value: Any) -> str:
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def build_payload(
    start: dt.date,
    end: dt.date,
    *,
    vault_root: Path = DEFAULT_VAULT_ROOT,
    experiment_path: Path | None = None,
    generated_at: dt.datetime | None = None,
) -> dict[str, Any]:
    vault_root = Path(vault_root)
    experiment_path = experiment_path or vault_root / "03 - Astrology" / "daybreak_experiment_registry.json"
    experiment = _load_json(experiment_path)
    charts, chart_index = _chart_registry(vault_root)
    if not charts:
        raise ValueError("Chart registry is empty; Daybreak cannot resolve governing parents")
    # Validate every registered exact time up front; never partially build.
    for meta in charts:
        _chart_timestamp(vault_root, meta)
    used_chart_ids: set[str] = set()
    frames: dict[str, Any] = {}
    previous_date = (start - dt.timedelta(days=1)).isoformat()
    previous_daily = cast_daybreak(previous_date, vault_root=vault_root)
    total = (end - start).days + 1
    for offset in range(total):
        day = start + dt.timedelta(days=offset)
        date_iso = day.isoformat()
        daily = cast_daybreak(date_iso, vault_root=vault_root)
        segments, transitions = _segments(
            daily, charts, chart_index, vault_root=vault_root, used=used_chart_ids
        )
        if not segments:
            raise RuntimeError(f"No exact hierarchy segment generated for {date_iso}")
        first = segments[0]
        frame = {
            "frame_id": f"daybreak-{date_iso}",
            "date": date_iso,
            "standing": "subordinate_experimental_daily_frame",
            "cohort": _cohort(date_iso, experiment),
            "hierarchy": first["hierarchy"],
            "chart": daily,
            "contacts": first["contacts"],
            "contact_classification": first["contact_classification"],
            "hierarchy_segments": segments,
            "parent_transitions": transitions,
            "daily_delta": _daily_delta(date_iso, previous_daily, daily, transitions),
            "long_clocks": _long_clock_delivery(date_iso, daily, vault_root),
        }
        frame["baseline_sha256"] = canonical_sha256(baseline_core(frame))
        frames[date_iso] = frame
        previous_daily = daily
    chart_catalog = {
        chart_id: _chart_summary(vault_root, chart_index[chart_id])
        for chart_id in sorted(used_chart_ids)
    }
    geometry_index = _geometry_index(frames)
    generated_at = generated_at or dt.datetime.now(UTC)
    return {
        "schema": SCHEMA,
        "generated_at": _iso(generated_at.astimezone(UTC)),
        "coverage": {"start": start.isoformat(), "end": end.isoformat(), "frame_count": len(frames)},
        "method": {
            "method_id": FRAME_METHOD_ID,
            "definition": "exact geocentric Sun-Ascendant conjunction in Washington, D.C.",
            "rise_seed": "solar disc centre; refraction disabled; refined to exact Sun-ASC longitude equality",
            "location": {
                "label": "Washington, D.C.", "latitude": DC_LAT,
                "longitude": DC_LON, "timezone": DC_TZ_NAME,
            },
            "houses": "Whole Sign",
            "mandatory_points": ["916 America"],
            "america_authority": "america_ephemeris.json; shortest signed-arc interpolation between 00:00 UTC daily rows",
            "america_max_daily_motion_deg": AMERICA_MAX_DAILY_MOTION_DEG,
            "parent_routing": "exact registered UTC timestamp inside each Sun-ASC interval",
            "seed_chart_america_policy": "include from canonical cache when covered; otherwise unresolved; never extrapolate",
            "cross_contact_limit_deg": CROSS_CONTACT_LIMIT_DEG,
            "cross_contact_strength": {"exact_max": 0.25, "tight_max": 1.5, "active_max": 3.0},
            "internal_major_orbs_deg": {name: limit for name, _angle, limit in MAJOR_ASPECTS},
            "standing": "The daybreak frame delivers registered governing charts; it never replaces or governs them.",
        },
        "experiment": experiment,
        "chart_catalog": chart_catalog,
        "seed_charts": _seed_charts(vault_root),
        "geometry_ref_contract": {
            "calculate_once": True,
            "reference_field": "geometry_refs",
            "canonical_row_reference_field": "reference_id",
            "identifier_fields": [
                "reference_id", "mirror_family_id", "geometry_id",
                "segment_id", "transition_id", "delta_id"
            ],
            "resolution": "geometry_index[ref] yields an RFC 6901 JSON Pointer into this payload",
            "missing_ref_policy": "fail_closed",
            "structural_mirror_policy": (
                "Daybreak Sun and ASC are definitionally co-located; paired hits use one "
                "SunASC mirror_family_id/reference_id and count as one occurrence"
            ),
        },
        "geometry_index": geometry_index,
        "frames": frames,
    }



def prospective_baseline(payload: dict[str, Any]) -> dict[str, Any]:
    cohort = next(row for row in payload["experiment"]["cohorts"] if row["cohort_id"] == "prospective-30d")
    frames = {
        date_iso: {
            "sha256": payload["frames"][date_iso]["baseline_sha256"],
            "core": baseline_core(payload["frames"][date_iso]),
        }
        for date_iso in sorted(payload["frames"])
        if cohort["start"] <= date_iso <= cohort["end"]
    }
    return {
        "schema": "f250.daybreak-prospective-baseline/v1",
        "status": "frozen",
        "frozen_at": cohort["frozen_at"],
        "cohort_id": cohort["cohort_id"],
        "start": cohort["start"],
        "end": cohort["end"],
        "frame_count": len(frames),
        "method_id": payload["method"]["method_id"],
        "frames": frames,
    }


def validate_prospective_baseline(payload: dict[str, Any], baseline: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for date_iso, frozen in baseline.get("frames", {}).items():
        current = payload.get("frames", {}).get(date_iso)
        if current is None:
            errors.append(f"frozen date missing from payload: {date_iso}")
            continue
        if current["baseline_sha256"] != frozen["sha256"]:
            errors.append(f"prospective baseline drift: {date_iso}")
    return errors

# Exact-routing / canonical-America support.
SLOW_BODIES = {"Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"}
DELTA_HOUSE_BODIES = {"Moon", "Mercury", "Venus", "Mars", "Jupiter", "America"}
AMERICA_MAX_DAILY_MOTION_DEG = 1.0

def _aware(value: str | dt.datetime, *, field: str) -> dt.datetime:
    moment = dt.datetime.fromisoformat(value) if isinstance(value, str) else value
    if moment.tzinfo is None:
        raise ValueError(f"{field} must be timezone-aware: {value!r}")
    return moment.astimezone(UTC)

@lru_cache(maxsize=8)
def _america_rows(cache_path: str) -> dict[str, float]:
    path = Path(cache_path)
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
        body = raw["916 America"]
        if not isinstance(body, dict) or not body:
            raise ValueError("916 America mapping is empty")
        rows = {str(key): float(value) % 360.0 for key, value in body.items()}
    except Exception as exc:
        raise RuntimeError(f"Canonical 916 America cache unavailable: {path}: {exc}") from exc
    return rows

def _canonical_america(moment: dt.datetime, vault_root: Path) -> tuple[float, float, str, str]:
    moment = _aware(moment, field="916 America moment")
    cache = Path(vault_root) / "99 - Templates" / "america_ephemeris.json"
    rows = _america_rows(str(cache))
    day0 = moment.date()
    key0 = day0.isoformat()
    key1 = (day0 + dt.timedelta(days=1)).isoformat()
    if key0 not in rows or key1 not in rows:
        missing = key0 if key0 not in rows else key1
        raise ValueError(
            f"916 America canonical interpolation requires bracketing 00:00 UTC rows; "
            f"missing {missing} in {cache}"
        )
    start = rows[key0]
    motion = _signed_delta(rows[key1], start)
    if abs(motion) > AMERICA_MAX_DAILY_MOTION_DEG:
        raise ValueError(
            f"916 America implausible motion {motion:.9f} deg/day at {key0}; refusing chart"
        )
    # Preserve the live whole-second interpolation precision so unaffected
    # frozen baseline bytes do not drift; only the signed-arc bug is repaired.
    seconds = moment.hour * 3600 + moment.minute * 60 + moment.second
    fraction = seconds / 86400.0
    return (start + motion * fraction) % 360.0, motion, key0, key1

def _chart_timestamp(vault_root: Path, meta: dict[str, Any]) -> dt.datetime:
    if not meta.get("id"):
        raise ValueError(f"Registered chart has no id: {meta!r}")
    bone = _bone(vault_root, meta["id"])
    if not bone.get("utc"):
        raise ValueError(f"Registered chart {meta['id']} has no exact UTC timestamp")
    return _aware(bone["utc"], field=f"{meta['id']}.utc")

@lru_cache(maxsize=256)
def _chart_summary_cached(vault_root_value: str, chart_id: str, meta_json: str) -> dict[str, Any]:
    vault_root = Path(vault_root_value)
    meta = json.loads(meta_json)
    bone = _bone(vault_root, chart_id)
    moment = _aware(bone.get("utc"), field=f"{chart_id}.utc")
    canonical_lon, speed, key0, key1 = _canonical_america(moment, vault_root)
    stored = bone.get("america", {}).get("lon")
    stored_delta = None if stored is None else abs(_signed_delta(float(stored), canonical_lon))
    positions = {body: round(bone["pos"][body]["lon"], 9) for body in PLANET_ORDER}
    positions["America"] = round(canonical_lon, 9)
    targets = dict(positions)
    targets.update({"ASC": round(bone["asc"], 9), "MC": round(bone["mc"], 9)})
    wheel = dict(positions)
    wheel["ASC"] = round(bone["asc"], 9)
    return {
        "chart_id": chart_id,
        "chart_type": meta["type"],
        "date": meta["date"],
        "utc": bone["utc"],
        "local": bone.get("edt"),
        "label": _chart_label(meta, bone),
        "sign": meta.get("sign"),
        "kind": meta.get("kind"),
        "eclipse": bone.get("eclipse"),
        "greer_quiet": bone.get("greer_quiet"),
        "asc": round(bone["asc"], 9),
        "mc": round(bone["mc"], 9),
        "ruler": bone.get("ruler"),
        "root_members": bone.get("root_members", []),
        "targets": targets,
        "wheel": wheel,
        "america": {
            "status": "computed_from_canonical_cache",
            "lon": round(canonical_lon, 9),
            "speed_deg_per_day": round(speed, 9),
            "authority": "america_ephemeris.json",
            "bracket_dates": [key0, key1],
            "stored_bone_lon_deg": None if stored is None else round(float(stored) % 360.0, 9),
            "stored_bone_delta_deg": None if stored_delta is None else round(stored_delta, 9),
            "stored_bone_matches_canonical": bool(stored_delta is not None and stored_delta <= 0.001),
        },
    }

def resolve_context_at(
    moment: dt.datetime,
    charts: list[dict[str, Any]],
    *,
    vault_root: Path = DEFAULT_VAULT_ROOT,
) -> dict[str, str | None]:
    moment_utc = _aware(moment, field="context moment")
    dated = [(row, _chart_timestamp(Path(vault_root), row)) for row in charts]
    available = [(row, stamp) for row, stamp in dated if stamp <= moment_utc]
    ingresses = [item for item in available if item[0]["type"] == "ingress"]
    new_moons = [
        item for item in available
        if item[0]["type"] == "lunation" and item[0].get("kind") == "new"
    ]
    lunations = [item for item in available if item[0]["type"] == "lunation"]
    ingress = max(ingresses, key=lambda item: item[1], default=None)
    chapter = max(new_moons, key=lambda item: item[1], default=None)
    phase = max(lunations, key=lambda item: item[1], default=None)
    if phase and chapter and phase[0]["id"] == chapter[0]["id"]:
        phase = None
    return {
        "ingress_id": ingress[0]["id"] if ingress else None,
        "chapter_id": chapter[0]["id"] if chapter else None,
        "phase_event_id": phase[0]["id"] if phase else None,
    }

def _contact_rows(
    daily: dict[str, Any],
    parent: dict[str, Any] | None,
    *,
    role: str,
    segment_key: str,
) -> list[dict[str, Any]]:
    rows = _cross_contacts(daily, parent)
    frame_id = f"daybreak-{daily['sunrise']['local'][:10]}"
    for row in rows:
        if (
            row["source"] == "America"
            and row["target"] == "America"
            and row["aspect_id"] == "conjunction"
        ):
            row["continuity"] = True
        row["geometry_id"] = (
            f"{frame_id}:{segment_key}:parent:{role}:{row['parent_chart_id']}:"
            f"{row['source']}:{row['aspect_id']}:{row['target']}"
        )
        row["reference_id"] = row["geometry_id"]
        row["structural_mirror"] = False
        row["mirror_family_id"] = None
        row["mirror_roles"] = []
        row["independent_occurrence"] = True
    by_mirror_key: dict[tuple[str, str, str], list[dict[str, Any]]] = {}
    for row in rows:
        if row["source"] in {"Sun", "ASC"}:
            key = (row["parent_chart_id"], row["aspect_id"], row["target"])
            by_mirror_key.setdefault(key, []).append(row)
    for (parent_id, aspect_id, target), candidates in by_mirror_key.items():
        roles = {row["source"] for row in candidates}
        if roles != {"Sun", "ASC"}:
            continue
        family_id = (
            f"{frame_id}:{segment_key}:parent:{role}:{parent_id}:"
            f"SunASC:{aspect_id}:{target}"
        )
        for row in candidates:
            row["reference_id"] = family_id
            row["structural_mirror"] = True
            row["mirror_family_id"] = family_id
            row["mirror_roles"] = ["Sun", "ASC"]
            row["independent_occurrence"] = row["source"] == "Sun"
    return rows

def _classify_contacts(contacts: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
    roles: dict[str, Any] = {}
    total_trigger = 0
    total_background = 0
    for role, rows in contacts.items():
        trigger_ids = []
        background_ids = []
        families: dict[str, list[dict[str, Any]]] = {}
        for row in rows:
            families.setdefault(row["reference_id"], []).append(row)
        for contact_id, family in families.items():
            eligible = any(
                not row["continuity"]
                and not (row["source"] in SLOW_BODIES and row["target"] in SLOW_BODIES)
                and row["independent_occurrence"]
                for row in family
            )
            target = trigger_ids if eligible else background_ids
            target.append(contact_id)
        total_trigger += len(trigger_ids)
        total_background += len(background_ids)
        roles[role] = {
            "trigger_contact_ids": trigger_ids,
            "background_contact_ids": background_ids,
            "no_trigger": not trigger_ids,
        }
    return {
        "roles": roles,
        "trigger_contact_count": total_trigger,
        "background_contact_count": total_background,
        "no_trigger": total_trigger == 0,
        "slow_filter_rule": (
            "same-body Jupiter-through-Pluto conjunction continuity and all slow-to-slow "
            "cross-chart contacts remain factual background, never daily triggers"
        ),
    }

def _parents_for(
    hierarchy: dict[str, str | None],
    *,
    vault_root: Path,
    chart_index: dict[str, dict[str, Any]],
    used: set[str],
) -> dict[str, dict[str, Any] | None]:
    parents: dict[str, dict[str, Any] | None] = {}
    for role, chart_id in hierarchy.items():
        if chart_id is None:
            parents[role] = None
            continue
        if chart_id not in chart_index:
            raise ValueError(f"Resolved parent {chart_id!r} is absent from chart registry")
        used.add(chart_id)
        parents[role] = _chart_summary(vault_root, chart_index[chart_id])
    return parents

def _contacts_for(
    daily: dict[str, Any],
    parents: dict[str, dict[str, Any] | None],
    *,
    segment_key: str,
) -> dict[str, Any]:
    return {
        "ingress": _contact_rows(daily, parents["ingress_id"], role="ingress", segment_key=segment_key),
        "chapter": _contact_rows(daily, parents["chapter_id"], role="chapter", segment_key=segment_key),
        "phase_event": _contact_rows(daily, parents["phase_event_id"], role="phase_event", segment_key=segment_key),
    }

def _geometry_index(frames: dict[str, Any]) -> dict[str, str]:
    """Stable calculate-once ref -> RFC 6901 pointer table."""
    out: dict[str, str] = {}

    def add(identifier: str, pointer: str) -> None:
        if identifier in out:
            raise ValueError(f"Duplicate geometry reference id: {identifier}")
        out[identifier] = pointer

    for date_iso, frame in frames.items():
        root = f"/frames/{date_iso}"
        for index, row in enumerate(frame["chart"]["aspects"]):
            add(row["geometry_id"], f"{root}/chart/aspects/{index}")
        for index, segment in enumerate(frame["hierarchy_segments"]):
            segment_root = f"{root}/hierarchy_segments/{index}"
            add(segment["segment_id"], segment_root)
            for role, rows in segment["contacts"].items():
                for row_index, row in enumerate(rows):
                    add(row["geometry_id"], f"{segment_root}/contacts/{role}/{row_index}")
                    if row["structural_mirror"] and row["independent_occurrence"]:
                        add(row["mirror_family_id"], f"{segment_root}/contacts/{role}/{row_index}")
        for index, row in enumerate(frame["parent_transitions"]):
            add(row["transition_id"], f"{root}/parent_transitions/{index}")
        for index, row in enumerate(frame["daily_delta"]["rows"]):
            add(row["delta_id"], f"{root}/daily_delta/rows/{index}")
        for lane in ("cycles", "active_edges", "seed_echoes"):
            for index, row in enumerate(frame["long_clocks"][lane]):
                add(row["geometry_id"], f"{root}/long_clocks/{lane}/{index}")
                if lane == "seed_echoes" and row["structural_mirror"] and row["independent_occurrence"]:
                    add(row["mirror_family_id"], f"{root}/long_clocks/{lane}/{index}")
    return dict(sorted(out.items()))

def _segments(
    daily: dict[str, Any],
    charts: list[dict[str, Any]],
    chart_index: dict[str, dict[str, Any]],
    *,
    vault_root: Path,
    used: set[str],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    start = _aware(daily["sunrise"]["utc"], field="frame start")
    end = _aware(daily["sunrise"]["next_utc"], field="frame end")
    events = sorted(
        [
            (stamp, row)
            for row in charts
            for stamp in [_chart_timestamp(vault_root, row)]
            if start < stamp < end and row["type"] in {"ingress", "lunation"}
        ],
        key=lambda item: (item[0], item[1]["id"]),
    )
    boundaries = [start] + sorted({stamp for stamp, _row in events}) + [end]
    segments: list[dict[str, Any]] = []
    transitions: list[dict[str, Any]] = []
    for index, (seg_start, seg_end) in enumerate(zip(boundaries, boundaries[1:]), start=1):
        hierarchy = resolve_context_at(seg_start, charts, vault_root=vault_root)
        parents = _parents_for(
            hierarchy, vault_root=vault_root, chart_index=chart_index, used=used
        )
        contacts = _contacts_for(daily, parents, segment_key=f"s{index:02d}")
        entering = [row for stamp, row in events if stamp == seg_start]
        segments.append({
            "segment_id": f"daybreak-{daily['sunrise']['local'][:10]}/s{index:02d}",
            "start_utc": _iso(seg_start),
            "start_local": _iso(seg_start.astimezone(DC_TZ)),
            "end_utc": _iso(seg_end),
            "end_local": _iso(seg_end.astimezone(DC_TZ)),
            "hierarchy": hierarchy,
            "contacts": contacts,
            "contact_classification": _classify_contacts(contacts),
            "transition_in": None if not entering else {
                "chart_ids": [row["id"] for row in entering],
                "at_utc": _iso(seg_start),
                "at_local": _iso(seg_start.astimezone(DC_TZ)),
            },
        })
    for stamp, row in events:
        before = resolve_context_at(stamp - dt.timedelta(microseconds=1), charts, vault_root=vault_root)
        after = resolve_context_at(stamp, charts, vault_root=vault_root)
        transitions.append({
            "transition_id": f"daybreak-{daily['sunrise']['local'][:10]}:{row['id']}",
            "chart_id": row["id"],
            "chart_type": row["type"],
            "kind": row.get("kind"),
            "at_utc": _iso(stamp),
            "at_local": _iso(stamp.astimezone(DC_TZ)),
            "hierarchy_before": before,
            "hierarchy_after": after,
        })
    return segments, transitions

def _aspect_key(row: dict[str, Any]) -> tuple[str, str, str]:
    return row["a"], row["b"], row["aspect_id"]

def _delta_row(delta_id: str, kind: str, summary: str, **extra: Any) -> dict[str, Any]:
    return {
        "delta_id": delta_id,
        "kind": kind,
        "precision": extra.pop("precision", "daybreak_snapshot_boundary"),
        "summary": summary,
        "continuity": bool(extra.pop("continuity", False)),
        **extra,
    }

def _daily_delta(
    date_iso: str,
    previous: dict[str, Any],
    current: dict[str, Any],
    transitions: list[dict[str, Any]],
) -> dict[str, Any]:
    prefix = f"daybreak-{date_iso}"
    rows: list[dict[str, Any]] = []
    if previous["ruler"] != current["ruler"]:
        rows.append(_delta_row(
            f"{prefix}:ruler", "ruler_change",
            f"Daybreak ruler changed {previous['ruler']} -> {current['ruler']}",
            **{"from": previous["ruler"], "to": current["ruler"]},
            daily_trigger_eligible=True,
        ))
    if previous["root_members"] != current["root_members"]:
        rows.append(_delta_row(
            f"{prefix}:root", "root_members_change",
            f"Dispositor root changed {previous['root_members']} -> {current['root_members']}",
            **{"from": previous["root_members"], "to": current["root_members"]},
            daily_trigger_eligible=True,
        ))
    for angle in ("ASC", "MC"):
        old_sign = previous["asc_sign" if angle == "ASC" else "mc_sign"]
        new_sign = current["asc_sign" if angle == "ASC" else "mc_sign"]
        if old_sign != new_sign:
            rows.append(_delta_row(
                f"{prefix}:angle-sign:{angle}", "angle_sign_change",
                f"{angle} changed sign {old_sign} -> {new_sign}",
                body=angle, **{"from": old_sign, "to": new_sign},
                daily_trigger_eligible=True,
            ))
    for body in ASPECT_POINT_ORDER:
        old = previous["positions"][body]
        new = current["positions"][body]
        if old["sign"] != new["sign"]:
            rows.append(_delta_row(
                f"{prefix}:body-sign:{body}", "body_sign_change",
                f"{body} changed sign {old['sign']} -> {new['sign']}",
                body=body, **{"from": old["sign"], "to": new["sign"]},
                daily_trigger_eligible=True,
            ))
        if body in DELTA_HOUSE_BODIES and old["house"] != new["house"]:
            rows.append(_delta_row(
                f"{prefix}:house:{body}", "whole_sign_house_change",
                f"{body} changed Whole Sign house {old['house']} -> {new['house']}",
                body=body, **{"from": old["house"], "to": new["house"]},
                daily_trigger_eligible=True,
            ))
    old_tight = {
        _aspect_key(row): row for row in previous["aspects"] if row["strength"] in {"exact", "tight"}
    }
    new_tight = {
        _aspect_key(row): row for row in current["aspects"] if row["strength"] in {"exact", "tight"}
    }
    for state, keys, source in (
        ("entered", sorted(set(new_tight) - set(old_tight)), new_tight),
        ("exited", sorted(set(old_tight) - set(new_tight)), old_tight),
    ):
        for key in keys:
            row = source[key]
            slow_slow = row["a"] in SLOW_BODIES and row["b"] in SLOW_BODIES
            rows.append(_delta_row(
                f"{prefix}:tight-aspect-{state}:{row['a']}:{row['aspect_id']}:{row['b']}",
                f"tight_internal_aspect_{state}",
                f"{row['a']} {row['aspect_id']} {row['b']} {state} the <=1.5 deg band",
                body=[row["a"], row["b"]],
                **{"from": None if state == "entered" else row["strength"],
                   "to": row["strength"] if state == "entered" else None},
                continuity=slow_slow,
                daily_trigger_eligible=not slow_slow,
                orb_deg=row["orb_deg"],
            ))
    for transition in transitions:
        rows.append(_delta_row(
            f"{prefix}:parent:{transition['chart_id']}", "parent_chart_transition",
            f"Registered {transition['chart_type']} parent changed at exact timestamp",
            at_utc=transition["at_utc"], at_local=transition["at_local"],
            **{"from": transition["hierarchy_before"], "to": transition["hierarchy_after"]},
            precision="exact_timestamp",
            daily_trigger_eligible=True,
            chart_id=transition["chart_id"],
        ))
    rows.sort(key=lambda row: (row["at_utc"] if row.get("at_utc") else current["sunrise"]["utc"], row["delta_id"]))
    eligible = [row for row in rows if row["daily_trigger_eligible"]]
    return {
        "none": not rows,
        "no_trigger": not eligible,
        "slow_only": bool(rows) and not eligible,
        "rows": rows,
        "comparison": {
            "from_utc": previous["sunrise"]["utc"],
            "to_utc": current["sunrise"]["utc"],
            "categorical_only": True,
            "tight_band_max_orb_deg": 1.5,
        },
    }

__all__ = [
    "SCHEMA", "FRAME_METHOD_ID", "sun_asc_crossing", "cast_daybreak",
    "resolve_context", "resolve_context_at", "build_payload", "baseline_core",
    "prospective_baseline", "validate_prospective_baseline", "canonical_sha256",
    "strength", "_chart_registry", "_canonical_america",
]
