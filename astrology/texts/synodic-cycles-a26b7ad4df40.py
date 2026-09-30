#!/usr/bin/env python3
"""Freedom 250 Long Clocks calculation engine.

The engine keeps three facts independent:

1. ``geometry``: the exact slower-to-faster hand and DR-020 phase grammar;
2. ``active_aspect``: a direct chart aspect, or null outside Katie's orb;
3. ``nameability``: whether a reading may narrate the phase as a cycle story.

Seed-degree contacts are emitted separately as ``seed_echoes``.  No geometric
nearest chapter receives a prose verdict outside its applicable major orb.

All chart-moment work is registry-first.  The engine reads exact UTC moments and
positions from ``chart_reading_bones`` and refuses to guess a nearest lunation.
"""

from __future__ import annotations

import datetime as _dt
import hashlib
import importlib.util
import json
import os
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable, Iterable
from zoneinfo import ZoneInfo

import swisseph as swe


HERE = Path(__file__).resolve().parent
DEFAULT_VAULT_ROOT = Path(
    os.environ.get(
        "F250_LONG_CLOCKS_VAULT_ROOT",
        str(HERE.parent),
    )
)
DEFAULT_SEED_REGISTRY = HERE / "synodic_seed_families.json"

import sys as _sys  # noqa: E402
if str(HERE) not in _sys.path:
    _sys.path.insert(0, str(HERE))
from swiss_ephemeris import FLAGS, EPHEMERIS_LABEL  # noqa: E402  2026-09-25: Swiss/JPL files, never silent Moshier
SIGNS = [
    "Aries",
    "Taurus",
    "Gemini",
    "Cancer",
    "Leo",
    "Virgo",
    "Libra",
    "Scorpio",
    "Sagittarius",
    "Capricorn",
    "Aquarius",
    "Pisces",
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

# DR-020's ordering: slowest -> fastest.  The hand is always measured from the
# slower body to the faster one, so 0 -> 180 is waxing and 180 -> 360 waning.
SLOWEST_FIRST = [
    "Pluto",
    "Neptune",
    "Uranus",
    "Saturn",
    "Jupiter",
    "Mars",
    "Sun",
    "Venus",
    "Mercury",
    "Moon",
]
SLOW_INDEX = {name: index for index, name in enumerate(SLOWEST_FIRST)}
OUTER = {"Uranus", "Neptune", "Pluto"}
TIER_ORDER = {
    "era_currents": 1,
    "state_architecture": 2,
    "political_delivery": 3,
}

# Exact method drawer orbs supplied by Katie's workbook.
ORB_LIMITS = {
    "conjunction": 8.0,
    "sextile": 5.0,
    "square": 7.0,
    "trine": 7.0,
    "opposition": 8.0,
}

# Aspect chapter is geometry, not a replacement for DR-020's universal phases.
CHAPTERS = [
    {
        "chapter_id": "conjunction",
        "aspect_id": "conjunction",
        "angle_deg": 0.0,
        "flow_kind": "seed",
    },
    {
        "chapter_id": "waxing_sextile",
        "aspect_id": "sextile",
        "angle_deg": 60.0,
        "flow_kind": "flowing",
    },
    {
        "chapter_id": "waxing_square",
        "aspect_id": "square",
        "angle_deg": 90.0,
        "flow_kind": "hard",
    },
    {
        "chapter_id": "waxing_trine",
        "aspect_id": "trine",
        "angle_deg": 120.0,
        "flow_kind": "flowing",
    },
    {
        "chapter_id": "opposition",
        "aspect_id": "opposition",
        "angle_deg": 180.0,
        "flow_kind": "hard",
    },
    {
        "chapter_id": "waning_trine",
        "aspect_id": "trine",
        "angle_deg": 240.0,
        "flow_kind": "flowing",
    },
    {
        "chapter_id": "waning_square",
        "aspect_id": "square",
        "angle_deg": 270.0,
        "flow_kind": "hard",
    },
    {
        "chapter_id": "waning_sextile",
        "aspect_id": "sextile",
        "angle_deg": 300.0,
        "flow_kind": "flowing",
    },
]

# Exact mirror of phases.py.  The live function is imported when available;
# tests assert this fallback stays identical at boundaries and interior samples.
DR020_PHASES = [
    (0.0, "New"),
    (45.0, "Crescent"),
    (90.0, "First Quarter"),
    (135.0, "Gibbous"),
    (180.0, "Full"),
    (225.0, "Disseminating"),
    (270.0, "Last Quarter"),
    (315.0, "Balsamic"),
]

SEED_ECHO_POLICY = {
    "policy_id": "seed-echo-hard-3.5/v1",
    "points": ["Sun", "Moon", "ASC", "MC"],
    "aspects": ["conjunction", "square", "opposition"],
    "orb_limit_deg": 3.5,
    "note": "Seed echoes are sensitive-degree contacts, separate from current pair aspects.",
}


def parse_moment(value: str | _dt.datetime) -> _dt.datetime:
    """Return a timezone-aware UTC datetime."""
    if isinstance(value, _dt.datetime):
        moment = value
    else:
        moment = _dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if moment.tzinfo is None:
        raise ValueError("Long Clocks moments must carry an explicit timezone")
    return moment.astimezone(_dt.timezone.utc)


def jd_of(value: str | _dt.datetime) -> float:
    moment = parse_moment(value)
    hour = (
        moment.hour
        + moment.minute / 60
        + moment.second / 3600
        + moment.microsecond / 3_600_000_000
    )
    return swe.julday(moment.year, moment.month, moment.day, hour)


def datetime_from_jd(jd_ut: float) -> _dt.datetime:
    year, month, day, hour = swe.revjul(jd_ut, swe.GREG_CAL)
    base = _dt.datetime(year, month, day, tzinfo=_dt.timezone.utc)
    return base + _dt.timedelta(hours=hour)


def iso_utc(value: str | _dt.datetime | float) -> str:
    if isinstance(value, float):
        moment = datetime_from_jd(value)
    else:
        moment = parse_moment(value)
    return moment.isoformat(timespec="microseconds")


def _position(jd_ut: float, body: str) -> tuple[float, float]:
    result = swe.calc_ut(jd_ut, PLANET_CODES[body], FLAGS)[0]
    return result[0] % 360.0, result[3]


def _signed_delta(angle: float, target: float) -> float:
    """Shortest signed distance from target to angle, in [-180, 180)."""
    return ((angle - target + 180.0) % 360.0) - 180.0


def _circular_distance(angle: float, target: float) -> float:
    return abs(_signed_delta(angle, target))


def _phase_of_mirror(angle: float) -> tuple[str, str]:
    value = angle % 360.0
    phase_name = DR020_PHASES[0][1]
    for lower, candidate in DR020_PHASES:
        if value >= lower:
            phase_name = candidate
    return phase_name, ("waxing" if value < 180.0 else "waning")


@lru_cache(maxsize=8)
def phase_grammar(vault_root_value: str) -> tuple[Callable[[float], tuple[str, str]], str]:
    """Load DR-020's canonical ``phase_of``; use its exact mirror if unavailable."""
    path = Path(vault_root_value) / "99 - Templates" / "phases.py"
    if path.exists():
        spec = importlib.util.spec_from_file_location("f250_live_phases", path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module.phase_of, str(path)
    return _phase_of_mirror, "mirrored DR-020 grammar (live phases.py unavailable)"


def load_seed_registry(path: Path | str = DEFAULT_SEED_REGISTRY) -> dict[str, Any]:
    with Path(path).open(encoding="utf-8") as handle:
        registry = json.load(handle)
    cycles = registry.get("cycles", [])
    ids = [cycle["cycle_id"] for cycle in cycles]
    if len(cycles) != 10 or len(set(ids)) != 10:
        raise ValueError("Long Clocks seed registry must contain ten unique cycles")
    for cycle in cycles:
        pass_ids = {item["pass_id"] for item in cycle["passes"]}
        if cycle["display_anchor_pass_id"] not in pass_ids:
            raise ValueError(f"Missing display anchor for {cycle['cycle_id']}")
    return registry


def seed_registry_index(registry: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {cycle["cycle_id"]: cycle for cycle in registry["cycles"]}


def slow_fast(pair: Iterable[str]) -> tuple[str, str]:
    first, second = tuple(pair)
    return (
        (first, second)
        if SLOW_INDEX[first] < SLOW_INDEX[second]
        else (second, first)
    )


def angle_at(jd_ut: float, cycle: dict[str, Any]) -> tuple[float, float, dict[str, float], dict[str, float]]:
    slow, fast = slow_fast(cycle["pair"])
    slow_lon, slow_speed = _position(jd_ut, slow)
    fast_lon, fast_speed = _position(jd_ut, fast)
    angle = (fast_lon - slow_lon) % 360.0
    return (
        angle,
        fast_speed - slow_speed,
        {slow: slow_lon, fast: fast_lon},
        {slow: slow_speed, fast: fast_speed},
    )


def _aspect_strength(orb_deg: float) -> str:
    if orb_deg <= 0.25:
        return "exact"
    if orb_deg <= 1.5:
        return "tight"
    return "active"


def _motion_state(delta: float, relative_speed: float) -> tuple[str, bool, bool]:
    if abs(delta) <= 1e-7:
        return "exact", False, False
    if abs(relative_speed) <= 1e-8:
        return "stationary", False, False
    applying = delta * relative_speed < 0.0
    return ("applying" if applying else "separating"), applying, not applying


def nearest_chapter(angle: float) -> tuple[dict[str, Any], float, float]:
    chapter = min(CHAPTERS, key=lambda item: _circular_distance(angle, item["angle_deg"]))
    delta = _signed_delta(angle, chapter["angle_deg"])
    return chapter, abs(delta), delta


def _event_id(cycle_id: str, chapter_id: str, moment: _dt.datetime) -> str:
    stamp = moment.strftime("%Y%m%dT%H%M%SZ")
    return f"{cycle_id}::{chapter_id}::{stamp}"


def _refine_aspect_root(
    cycle: dict[str, Any], target_deg: float, lo: float, hi: float
) -> float:
    flo = _signed_delta(angle_at(lo, cycle)[0], target_deg)
    for _ in range(60):
        mid = (lo + hi) / 2.0
        fmid = _signed_delta(angle_at(mid, cycle)[0], target_deg)
        if flo == 0.0:
            return lo
        if flo * fmid <= 0.0:
            hi = mid
        else:
            lo = mid
            flo = fmid
    return (lo + hi) / 2.0


def exact_aspect_events(
    cycle: dict[str, Any],
    start: _dt.datetime,
    stop: _dt.datetime,
    *,
    step_days: float = 1.0,
    phase_func: Callable[[float], tuple[str, str]] = _phase_of_mirror,
) -> list[dict[str, Any]]:
    """Find every exact oriented major-aspect pass in a bounded window."""
    start_jd, stop_jd = jd_of(start), jd_of(stop)
    cursor = start_jd
    prior_angle, _, _, _ = angle_at(cursor, cycle)
    prior = {
        chapter["chapter_id"]: _signed_delta(prior_angle, chapter["angle_deg"])
        for chapter in CHAPTERS
    }
    events: list[dict[str, Any]] = []
    while cursor < stop_jd:
        next_jd = min(cursor + step_days, stop_jd)
        next_angle, _, _, _ = angle_at(next_jd, cycle)
        for chapter in CHAPTERS:
            chapter_id = chapter["chapter_id"]
            current = _signed_delta(next_angle, chapter["angle_deg"])
            previous = prior[chapter_id]
            # The second condition rejects the +/-180 discontinuity opposite the target.
            if previous * current < 0.0 and abs(previous - current) < 30.0:
                root = _refine_aspect_root(cycle, chapter["angle_deg"], cursor, next_jd)
                moment = datetime_from_jd(root)
                exact_angle, relative_speed, positions, speeds = angle_at(root, cycle)
                phase_name, direction = phase_func(chapter["angle_deg"] % 360.0)
                event = {
                    "event_id": _event_id(cycle["cycle_id"], chapter_id, moment),
                    "cycle_id": cycle["cycle_id"],
                    "chapter_id": chapter_id,
                    "aspect_id": chapter["aspect_id"],
                    "angle_deg": chapter["angle_deg"],
                    "utc": iso_utc(moment),
                    "jd_ut": round(root, 9),
                    "phase_name": phase_name,
                    "phase_direction": direction,
                    "relative_motion": "forward" if relative_speed > 0 else "reverse",
                    "residual_arcsec": round(
                        _circular_distance(exact_angle, chapter["angle_deg"]) * 3600.0,
                        8,
                    ),
                    "positions_deg": {key: round(value, 9) for key, value in positions.items()},
                    "speeds_deg_per_day": {
                        key: round(value, 9) for key, value in speeds.items()
                    },
                }
                if not events or abs(root - events[-1]["jd_ut"]) > 1e-5:
                    events.append(event)
            prior[chapter_id] = current
        cursor = next_jd
    events.sort(key=lambda item: item["utc"])
    return events


def build_event_catalog(
    registry: dict[str, Any],
    coverage_start: _dt.datetime,
    coverage_stop: _dt.datetime,
    *,
    phase_func: Callable[[float], tuple[str, str]] = _phase_of_mirror,
) -> dict[str, list[dict[str, Any]]]:
    """Build enough exact events to bracket every 2025-26 chart for every clock."""
    catalog: dict[str, list[dict[str, Any]]] = {}
    for cycle in registry["cycles"]:
        padding = _dt.timedelta(days=(cycle["nominal_cycle_years"] / 2.0 + 2.0) * 365.2425)
        catalog[cycle["cycle_id"]] = exact_aspect_events(
            cycle,
            coverage_start - padding,
            coverage_stop + padding,
            phase_func=phase_func,
        )
    return catalog


def _compact_event(event: dict[str, Any] | None) -> dict[str, Any] | None:
    if event is None:
        return None
    return {
        key: event[key]
        for key in (
            "event_id",
            "chapter_id",
            "aspect_id",
            "utc",
            "phase_name",
            "phase_direction",
            "relative_motion",
        )
    }


def exact_event_neighbors(
    events: list[dict[str, Any]], moment: _dt.datetime, chapter_id: str
) -> dict[str, Any]:
    when = parse_moment(moment)
    prior_major = None
    next_major = None
    prior_chapter = None
    next_chapter = None
    for event in events:
        event_time = parse_moment(event["utc"])
        if event_time <= when:
            prior_major = event
            if event["chapter_id"] == chapter_id:
                prior_chapter = event
        elif next_major is None:
            next_major = event
        if event_time > when and event["chapter_id"] == chapter_id and next_chapter is None:
            next_chapter = event
        if next_major is not None and next_chapter is not None:
            break
    return {
        "previous_major_exact": _compact_event(prior_major),
        "next_major_exact": _compact_event(next_major),
        "previous_same_chapter_exact": _compact_event(prior_chapter),
        "next_same_chapter_exact": _compact_event(next_chapter),
    }


def cycle_state(
    cycle: dict[str, Any],
    *,
    moment: _dt.datetime,
    positions: dict[str, float],
    speeds: dict[str, float],
    phase_func: Callable[[float], tuple[str, str]],
    events: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    slow, fast = slow_fast(cycle["pair"])
    angle = (positions[fast] - positions[slow]) % 360.0
    relative_speed = speeds[fast] - speeds[slow]
    phase_name, phase_direction = phase_func(angle)
    chapter, orb_deg, delta = nearest_chapter(angle)
    orb_limit = ORB_LIMITS[chapter["aspect_id"]]
    motion_state, applying, separating = _motion_state(delta, relative_speed)
    active = orb_deg <= orb_limit
    active_aspect = None
    if active:
        active_aspect = {
            "aspect_id": chapter["aspect_id"],
            "chapter_id": chapter["chapter_id"],
            "angle_deg": chapter["angle_deg"],
            "orb_deg": round(orb_deg, 6),
            "orb_limit_deg": orb_limit,
            "applying": applying,
            "separating": separating,
            "motion_state": motion_state,
            "strength": _aspect_strength(orb_deg),
            "flow_kind": chapter["flow_kind"],
        }
    state = {
        "cycle_id": cycle["cycle_id"],
        "tier_id": cycle["tier_id"],
        "tier_order": TIER_ORDER[cycle["tier_id"]],
        "cycle_order": cycle["order"],
        "pair": list(cycle["pair"]),
        "slow_body": slow,
        "fast_body": fast,
        "nominal_cycle_years": cycle["nominal_cycle_years"],
        "seed_family_id": cycle["seed_family_id"],
        "seed_family_label": cycle["seed_family_label"],
        "display_anchor_pass_id": cycle["display_anchor_pass_id"],
        "geometry": {
            "elongation_deg": round(angle, 6),
            "phase_name": phase_name,
            "phase_direction": phase_direction,
            "relative_speed_deg_per_day": round(relative_speed, 9),
            "positions_deg": {
                slow: round(positions[slow], 6),
                fast: round(positions[fast], 6),
            },
            "nearest_chapter_id": chapter["chapter_id"],
            "nearest_chapter_angle_deg": chapter["angle_deg"],
            "nearest_chapter_orb_deg": round(orb_deg, 6),
            "nearest_chapter_within_orb": active,
        },
        "active_aspect": active_aspect,
        "interpretive_status": "active" if active else "between_chapters",
    }
    if events is not None:
        state["exact_event_neighbors"] = exact_event_neighbors(
            events, moment, chapter["chapter_id"]
        )
    return state


def _chart_registry(vault_root: Path) -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    path = vault_root / "99 - Templates" / "chart_reading_bones" / "index.json"
    with path.open(encoding="utf-8") as handle:
        index = json.load(handle)
    charts = index.get("charts", [])
    return index, {chart["id"]: chart for chart in charts}


def _bone(vault_root: Path, chart_id: str) -> dict[str, Any]:
    path = vault_root / "99 - Templates" / "chart_reading_bones" / f"{chart_id}.json"
    if not path.exists():
        raise KeyError(f"Registered chart has no bones file: {chart_id}")
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def _window_id(chart_meta: dict[str, Any], all_ids: set[str]) -> str:
    if chart_meta["type"] == "ingress":
        return chart_meta["id"]
    label = chart_meta.get("governing")
    if not label:
        raise ValueError(f"Lunation missing governing ingress: {chart_meta['id']}")
    year, sign = label.split(maxsplit=1)
    window_id = f"ingress-{year}-{sign.lower()}"
    if window_id not in all_ids:
        raise ValueError(
            f"Lunation {chart_meta['id']} points to unregistered window {window_id}"
        )
    return window_id


def phase_nameability(bone: dict[str, Any], cycle: dict[str, Any]) -> dict[str, Any]:
    """DR-020 fence for phase narrative only; direct aspects remain visible."""
    pair = set(cycle["pair"])
    roots = set(bone.get("root_members") or [])
    ruler = bone.get("ruler")
    reasons: list[str] = []
    evidence: list[dict[str, Any]] = []
    if pair <= OUTER:
        reasons.append("era")
    root_hits = sorted(pair & roots)
    if root_hits:
        reasons.append("root")
        evidence.append({"reason": "root", "bodies": root_hits})
    if ruler in pair:
        reasons.append("chart_ruler")
        evidence.append({"reason": "chart_ruler", "body": ruler})
    natal_hits = [
        hit
        for hit in bone.get("us_hits_sag", [])
        if hit.get("nameable") is True and hit.get("eclipse_point") in pair
    ]
    if natal_hits:
        reasons.append("exact_us_natal")
        evidence.extend(
            {
                "reason": "exact_us_natal",
                "transit_point": hit["eclipse_point"],
                "aspect_id": hit["aspect"],
                "natal_point": hit["us_point"],
                "orb_deg": hit["orb"],
                "radix": hit.get("radix", "sag"),
            }
            for hit in natal_hits
        )
    return {
        "earned": bool(reasons),
        "reasons": reasons,
        "evidence": evidence,
        "applies_to": "phase_narrative_only",
        "does_not_hide_direct_aspect": True,
    }


def _point_longitudes(bone: dict[str, Any]) -> dict[str, float]:
    return {
        "Sun": bone["pos"]["Sun"]["lon"],
        "Moon": bone["pos"]["Moon"]["lon"],
        "ASC": bone["asc"],
        "MC": bone["mc"],
    }


def seed_echoes(
    chart_id: str, bone: dict[str, Any], registry: dict[str, Any]
) -> list[dict[str, Any]]:
    """Closest active hard contact from lights/angles to each seed family."""
    points = _point_longitudes(bone)
    echo_aspects = [("conjunction", 0.0), ("square", 90.0), ("opposition", 180.0)]
    limit = SEED_ECHO_POLICY["orb_limit_deg"]
    echoes: list[dict[str, Any]] = []
    for cycle in registry["cycles"]:
        for point, point_lon in points.items():
            best: tuple[float, str, dict[str, Any], float] | None = None
            for seed_pass in cycle["passes"]:
                separation = abs(_signed_delta(point_lon, seed_pass["longitude_deg"]))
                for aspect_id, angle_deg in echo_aspects:
                    orb = abs(separation - angle_deg)
                    candidate = (orb, aspect_id, seed_pass, angle_deg)
                    if best is None or candidate[0] < best[0]:
                        best = candidate
            assert best is not None
            orb, aspect_id, matched_pass, angle_deg = best
            if orb <= limit:
                echoes.append(
                    {
                        "echo_id": f"{chart_id}::{cycle['cycle_id']}::{point.lower()}::{aspect_id}",
                        "active": True,
                        "policy_id": SEED_ECHO_POLICY["policy_id"],
                        "cycle_id": cycle["cycle_id"],
                        "tier_id": cycle["tier_id"],
                        "seed_family_id": cycle["seed_family_id"],
                        "matched_pass_id": matched_pass["pass_id"],
                        "family_pass_count": len(cycle["passes"]),
                        "point": point,
                        "point_group": "lights" if point in {"Sun", "Moon"} else "angles",
                        "point_lon_deg": round(point_lon, 6),
                        "aspect_id": aspect_id,
                        "angle_deg": angle_deg,
                        "orb_deg": round(orb, 6),
                        "orb_limit_deg": limit,
                        "strength": _aspect_strength(orb),
                        "seed_lon_deg": matched_pass["longitude_deg"],
                        "long_clocks_route": {
                            "view": "long-clocks",
                            "mode": "moment",
                            "chart_id": chart_id,
                            "cycle_id": cycle["cycle_id"],
                            "focus": "seed-echoes",
                        },
                    }
                )
    echoes.sort(key=lambda item: (item["orb_deg"], item["cycle_id"], item["point"]))
    return echoes


def build_registered_chart_stack(
    chart_meta: dict[str, Any],
    *,
    vault_root: Path,
    registry: dict[str, Any],
    event_catalog: dict[str, list[dict[str, Any]]] | None,
    phase_func: Callable[[float], tuple[str, str]],
    all_chart_ids: set[str],
) -> dict[str, Any]:
    chart_id = chart_meta["id"]
    bone = _bone(vault_root, chart_id)
    moment = parse_moment(bone["utc"])
    positions = {body: bone["pos"][body]["lon"] for body in PLANET_CODES}
    speeds = {body: bone["pos"][body]["spd"] for body in PLANET_CODES}
    cycles: list[dict[str, Any]] = []
    for cycle in registry["cycles"]:
        state = cycle_state(
            cycle,
            moment=moment,
            positions=positions,
            speeds=speeds,
            phase_func=phase_func,
            events=(event_catalog or {}).get(cycle["cycle_id"]),
        )
        state["nameability"] = phase_nameability(bone, cycle)
        state["long_clocks_route"] = {
            "view": "long-clocks",
            "mode": "cycle",
            "cycle_id": cycle["cycle_id"],
            "chart_id": chart_id,
        }
        cycles.append(state)
    active_cycle_ids = [state["cycle_id"] for state in cycles if state["active_aspect"]]
    nameable_cycle_ids = [
        state["cycle_id"] for state in cycles if state["nameability"]["earned"]
    ]
    active_edges = []
    for state in cycles:
        aspect = state["active_aspect"]
        if aspect is None:
            continue
        active_edges.append(
            {
                "edge_id": f"{chart_id}::{state['cycle_id']}",
                "cycle_id": state["cycle_id"],
                "tier_id": state["tier_id"],
                "pair": state["pair"],
                **aspect,
                "phase_narrative_earned": state["nameability"]["earned"],
                "long_clocks_route": state["long_clocks_route"],
            }
        )
    echoes = seed_echoes(chart_id, bone, registry)
    return {
        "chart_id": chart_id,
        "chart_type": chart_meta["type"],
        "date": chart_meta["date"],
        "utc": iso_utc(moment),
        "local": bone.get("edt"),
        "window_id": _window_id(chart_meta, all_chart_ids),
        "root_members": bone.get("root_members", []),
        "chart_ruler": bone.get("ruler"),
        "active_cycle_ids": active_cycle_ids,
        "nameable_cycle_ids": nameable_cycle_ids,
        "cycles": cycles,
        "active_edges": active_edges,
        "seed_echoes": echoes,
        "long_clocks_route": {
            "view": "long-clocks",
            "mode": "moment",
            "chart_id": chart_id,
        },
    }


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def build_chart_stacks_payload(
    *,
    vault_root: Path = DEFAULT_VAULT_ROOT,
    seed_registry_path: Path = DEFAULT_SEED_REGISTRY,
    as_of: str | None = None,
    include_event_catalog: bool = True,
) -> dict[str, Any]:
    vault_root = Path(vault_root)
    registry = load_seed_registry(seed_registry_path)
    phase_func, phase_source = phase_grammar(str(vault_root))
    try:
        phase_source_display = str(Path(phase_source).relative_to(vault_root))
    except (ValueError, OSError):
        phase_source_display = phase_source
    index, chart_index = _chart_registry(vault_root)
    chart_moments = [parse_moment(_bone(vault_root, chart_id)["utc"]) for chart_id in chart_index]
    event_catalog = None
    if include_event_catalog:
        event_catalog = build_event_catalog(
            registry, min(chart_moments), max(chart_moments), phase_func=phase_func
        )
    all_ids = set(chart_index)
    charts = [
        build_registered_chart_stack(
            chart_meta,
            vault_root=vault_root,
            registry=registry,
            event_catalog=event_catalog,
            phase_func=phase_func,
            all_chart_ids=all_ids,
        )
        for chart_meta in index["charts"]
    ]
    if len(charts) != 30:
        raise ValueError(f"Expected 30 canonical chart moments; got {len(charts)}")
    if as_of is None:
        now_dc = _dt.datetime.now(ZoneInfo("America/New_York"))
        snapshot_moment = _dt.datetime(
            now_dc.year,
            now_dc.month,
            now_dc.day,
            12,
            0,
            tzinfo=ZoneInfo("America/New_York"),
        ).astimezone(_dt.timezone.utc)
        as_of_basis = "current America/New_York calendar day at 12:00 local"
    else:
        snapshot_moment = parse_moment(as_of)
        as_of_basis = "explicit --as-of"
    snapshot = current_snapshot(
        snapshot_moment,
        vault_root=vault_root,
        registry=registry,
        event_catalog=event_catalog,
        phase_func=phase_func,
    )
    index_path = vault_root / "99 - Templates" / "chart_reading_bones" / "index.json"
    return {
        "schema": "freedom250.long-clocks.chart-stacks/v1",
        "status": "generated",
        "generated_at": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "as_of": iso_utc(snapshot_moment),
        "as_of_basis": as_of_basis,
        "source": {
            "chart_registry_path": "99 - Templates/chart_reading_bones/index.json",
            "chart_registry_generated": index.get("generated"),
            "chart_registry_sha256": _sha256(index_path),
            "seed_registry_path": Path(seed_registry_path).name,
            "seed_registry_sha256": _sha256(Path(seed_registry_path)),
            "phase_grammar_source": phase_source_display,
            "positions_policy": "registered chart bones for covered charts; pyswisseph Swiss/JPL files for free moments",
        },
        "method": {
            "phase_grammar": "DR-020 phases.py: New, Crescent, First Quarter, Gibbous, Full, Disseminating, Last Quarter, Balsamic",
            "hand_direction": "slower body to faster body; waxing 0-180, waning 180-360",
            "major_orbs_deg": ORB_LIMITS,
            "strength_bands_deg": {
                "exact": "<=0.25",
                "tight": ">0.25 and <=1.5",
                "active": ">1.5 and <= aspect orb",
                "between_chapters": "outside aspect orb; geometry only, no verdict",
            },
            "nameability": "DR-020; phase narrative only. Direct chart aspects remain visible.",
            "seed_echo_policy": SEED_ECHO_POLICY,
            "canonical_lunation_policy": "registered chart IDs only; no nearest-lunation scan",
        },
        "tiers": registry["tiers"],
        "cycle_catalog": registry["cycles"],
        "exact_event_catalog": event_catalog or {},
        "snapshot": snapshot,
        "coverage": {
            "registered_chart_count": len(index["charts"]),
            "generated_chart_count": len(charts),
            "cycle_count": len(registry["cycles"]),
            "relationship_state_count": sum(len(chart["cycles"]) for chart in charts),
        },
        "charts": charts,
    }


def current_snapshot(
    moment_value: str | _dt.datetime,
    *,
    vault_root: Path = DEFAULT_VAULT_ROOT,
    registry: dict[str, Any] | None = None,
    event_catalog: dict[str, list[dict[str, Any]]] | None = None,
    phase_func: Callable[[float], tuple[str, str]] | None = None,
) -> dict[str, Any]:
    moment = parse_moment(moment_value)
    registry = registry or load_seed_registry()
    if phase_func is None:
        phase_func, _ = phase_grammar(str(vault_root))
    jd_ut = jd_of(moment)
    positions: dict[str, float] = {}
    speeds: dict[str, float] = {}
    for body in {body for cycle in registry["cycles"] for body in cycle["pair"]}:
        positions[body], speeds[body] = _position(jd_ut, body)
    cycles = [
        cycle_state(
            cycle,
            moment=moment,
            positions=positions,
            speeds=speeds,
            phase_func=phase_func,
            events=(event_catalog or {}).get(cycle["cycle_id"]),
        )
        for cycle in registry["cycles"]
    ]
    for state in cycles:
        pair = set(state["pair"])
        state["nameability"] = {
            "earned": pair <= OUTER,
            "reasons": ["era"] if pair <= OUTER else [],
            "evidence": [],
            "applies_to": "phase_narrative_only",
            "does_not_hide_direct_aspect": True,
            "context_note": "No chart root/ruler supplied for free-moment snapshot.",
        }
        state["long_clocks_route"] = {
            "view": "long-clocks",
            "mode": "cycle",
            "cycle_id": state["cycle_id"],
        }
    return {
        "utc": iso_utc(moment),
        "cycles": cycles,
        "active_cycle_ids": [state["cycle_id"] for state in cycles if state["active_aspect"]],
        "long_clocks_route": {"view": "long-clocks", "mode": "clock-room"},
    }


def registered_stack_for_chart_id(
    chart_id: str,
    *,
    vault_root: Path = DEFAULT_VAULT_ROOT,
    seed_registry_path: Path = DEFAULT_SEED_REGISTRY,
) -> dict[str, Any]:
    registry = load_seed_registry(seed_registry_path)
    phase_func, _ = phase_grammar(str(vault_root))
    _, chart_index = _chart_registry(Path(vault_root))
    if chart_id not in chart_index:
        raise KeyError(f"Unregistered chart_id: {chart_id}")
    return build_registered_chart_stack(
        chart_index[chart_id],
        vault_root=Path(vault_root),
        registry=registry,
        event_catalog=None,
        phase_func=phase_func,
        all_chart_ids=set(chart_index),
    )


def registered_stack_for_date(
    date_iso: str,
    *,
    vault_root: Path = DEFAULT_VAULT_ROOT,
    seed_registry_path: Path = DEFAULT_SEED_REGISTRY,
) -> dict[str, Any]:
    """Strict date lookup.  It never guesses a preceding or nearest lunation."""
    _, chart_index = _chart_registry(Path(vault_root))
    matches = [chart_id for chart_id, meta in chart_index.items() if meta["date"] == date_iso]
    if len(matches) != 1:
        raise KeyError(
            f"{date_iso} resolves to {len(matches)} registered charts; supply canonical chart_id"
        )
    return registered_stack_for_chart_id(
        matches[0], vault_root=vault_root, seed_registry_path=seed_registry_path
    )


def _wheel_record_from_bone(bone: dict[str, Any], vault_root: Path) -> dict[str, Any]:
    """Build a wheel-lib record from canonical bone positions without recasting."""
    longitudes = {body: bone["pos"][body]["lon"] for body in PLANET_CODES}
    positions = [
        [
            body,
            bone["pos"][body]["sign"],
            _degree_label(bone["pos"][body]["lon"]).split()[0],
            1 if bone["pos"][body]["retro"] else 0,
            round(bone["pos"][body]["lon"], 2),
        ]
        for body in PLANET_CODES
    ]
    node_lon = bone["node"]["lon"]
    positions.append(
        [
            "Node",
            SIGNS[int(node_lon // 30) % 12],
            _degree_label(node_lon).split()[0],
            1,
            round(node_lon, 2),
        ]
    )
    wheel_path = vault_root / "99 - Templates" / "wheel_lib.py"
    spec = importlib.util.spec_from_file_location("f250_wheel_lib_registered", wheel_path)
    if not spec or not spec.loader:
        raise RuntimeError(f"Cannot load wheel library: {wheel_path}")
    wheel = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(wheel)
    return {
        "pos": positions,
        "asp": wheel.aspects_between(longitudes),
        "asc": round(bone["asc"], 2),
    }


def _lunation_type(bone: dict[str, Any]) -> str:
    eclipse = bone.get("eclipse")
    if eclipse:
        return "Solar Eclipse" if eclipse.lower().startswith("solar") else "Lunar Eclipse"
    return "New Moon" if bone.get("lunation_kind") == "new" else "Full Moon"


def _registered_context_panel(
    chart_meta: dict[str, Any],
    *,
    vault_root: Path,
    seed_registry_path: Path,
    current_rows: dict[str, dict[str, Any]],
    cycle_catalog: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    chart_id = chart_meta["id"]
    bone = _bone(vault_root, chart_id)
    chart_stack = registered_stack_for_chart_id(
        chart_id,
        vault_root=vault_root,
        seed_registry_path=seed_registry_path,
    )
    points = {body: bone["pos"][body]["lon"] for body in PLANET_CODES}
    points.update({"ASC": bone["asc"], "MC": bone["mc"]})
    triggers = []
    for echo in chart_stack["seed_echoes"]:
        current = current_rows[echo["cycle_id"]]
        active_aspect = current["active_aspect"]
        pair = cycle_catalog[echo["cycle_id"]]["pair"]
        triggers.append(
            {
                "trigger_id": echo["echo_id"],
                "current": f"{pair[0]}–{pair[1]}",
                "cycle_id": echo["cycle_id"],
                "pair": list(pair),
                "via": echo["point"],
                "target": "seed degree",
                "aspect": echo["aspect_id"],
                "orb": echo["orb_deg"],
                "flowing": bool(
                    active_aspect and active_aspect["flow_kind"] == "flowing"
                ),
                "phase": current["phase"],
                "strength": echo["strength"],
                "seed_family_id": echo["seed_family_id"],
                "matched_pass_id": echo["matched_pass_id"],
                "current_active": bool(active_aspect),
                "current_flow_kind": (
                    active_aspect["flow_kind"] if active_aspect else None
                ),
                "long_clocks_route": echo["long_clocks_route"],
            }
        )
    wheel_record = _wheel_record_from_bone(bone, vault_root)
    if chart_meta["type"] == "ingress":
        title = f"{chart_meta['year']} {chart_meta['sign']} Solar Ingress"
        context_type = "Solar Ingress"
    else:
        context_type = _lunation_type(bone)
        title = f"{context_type} · {chart_meta['date']}"
    return {
        "id": chart_id,
        "chart_id": chart_id,
        "title": title,
        "type": context_type,
        "date": chart_meta["date"],
        "utc": iso_utc(bone["utc"]),
        "rising": bone["asc_sign"],
        "points": points,
        "asc": bone["asc"],
        "sun": bone["pos"]["Sun"]["lon"],
        "moon": bone["pos"]["Moon"]["lon"],
        "rec": wheel_record,
        "triggers": triggers,
        "seed_echoes": chart_stack["seed_echoes"],
        "long_clocks_route": chart_stack["long_clocks_route"],
    }


def registered_context_for_date(
    date_iso: str,
    *,
    vault_root: Path = DEFAULT_VAULT_ROOT,
    seed_registry_path: Path = DEFAULT_SEED_REGISTRY,
) -> dict[str, Any]:
    """Resolve an arbitrary covered date from the canonical chart registry.

    Selection is purely registry-based: latest registered ingress and latest
    registered lunation on or before the requested calendar date. This retains
    the opening-lunation-before-ingress behavior at cardinal boundaries and
    never searches the ephemeris for a synthetic nearest phase.
    """
    requested = _dt.date.fromisoformat(date_iso)
    vault_root = Path(vault_root)
    seed_registry_path = Path(seed_registry_path)
    index, chart_index = _chart_registry(vault_root)
    lunations = sorted(
        (meta for meta in index["charts"] if meta["type"] == "lunation"),
        key=lambda meta: (meta["date"], meta["id"]),
    )
    ingresses = sorted(
        (meta for meta in index["charts"] if meta["type"] == "ingress"),
        key=lambda meta: (meta["date"], meta["id"]),
    )
    covered_years = {int(meta["date"][:4]) for meta in lunations}
    if requested.year not in covered_years:
        raise KeyError(
            f"{date_iso} is outside registered lunation years {sorted(covered_years)}"
        )
    eligible_lunations = [meta for meta in lunations if meta["date"] <= date_iso]
    eligible_ingresses = [meta for meta in ingresses if meta["date"] <= date_iso]
    if not eligible_lunations or not eligible_ingresses:
        raise KeyError(f"{date_iso} precedes the first complete registered context")
    lunation_meta = eligible_lunations[-1]
    ingress_meta = eligible_ingresses[-1]
    registry = load_seed_registry(seed_registry_path)
    catalog = seed_registry_index(registry)
    compatibility_rows = currents(
        date_iso, vault_root=vault_root, seed_registry_path=seed_registry_path
    )
    # ``currents`` keeps a few empty legacy keys for old direct callers.  The
    # registered-context payload is a new factual contract, so those prose-era
    # compatibility fields do not cross this boundary.
    current_list = []
    for compatibility_row in compatibility_rows:
        row = dict(compatibility_row)
        for legacy_key in ("verdict", "underlies", "underlies_keys"):
            row.pop(legacy_key, None)
        current_list.append(row)
    current_rows = {row["cycle_id"]: row for row in current_list}
    ingress_panel = _registered_context_panel(
        ingress_meta,
        vault_root=vault_root,
        seed_registry_path=seed_registry_path,
        current_rows=current_rows,
        cycle_catalog=catalog,
    )
    lunation_panel = _registered_context_panel(
        lunation_meta,
        vault_root=vault_root,
        seed_registry_path=seed_registry_path,
        current_rows=current_rows,
        cycle_catalog=catalog,
    )
    return {
        "schema": "freedom250.long-clocks.registered-context/v1",
        "requested_date": date_iso,
        "resolution": {
            "policy": "latest registered chart on or before requested date",
            "ephemeris_phase_scan": False,
            "ingress_chart_id": ingress_meta["id"],
            "ingress_date": ingress_meta["date"],
            "lunation_chart_id": lunation_meta["id"],
            "lunation_date": lunation_meta["date"],
            "lunation_registered_window_id": _window_id(
                lunation_meta, set(chart_index)
            ),
        },
        "currents": current_list,
        "ingress": ingress_panel,
        "lunation": lunation_panel,
    }


def seed_chart(
    cycle_id: str,
    pass_id: str | None = None,
    *,
    vault_root: Path = DEFAULT_VAULT_ROOT,
    seed_registry_path: Path = DEFAULT_SEED_REGISTRY,
) -> dict[str, Any]:
    """Exact D.C.-relocated seed chart input for the existing wheel builder."""
    registry = load_seed_registry(seed_registry_path)
    cycle = seed_registry_index(registry)[cycle_id]
    chosen_id = pass_id or cycle["display_anchor_pass_id"]
    chosen = next((item for item in cycle["passes"] if item["pass_id"] == chosen_id), None)
    if chosen is None:
        raise KeyError(f"Unknown seed pass {cycle_id}/{chosen_id}")
    moment = parse_moment(chosen["utc"])
    jd_ut = jd_of(moment)
    positions = {}
    for body in PLANET_CODES:
        longitude, speed = _position(jd_ut, body)
        positions[body] = {"lon": longitude, "spd": speed}
    conventions_path = Path(vault_root) / "99 - Templates" / "chart_conventions.py"
    spec = importlib.util.spec_from_file_location("f250_chart_conventions", conventions_path)
    if not spec or not spec.loader:
        raise RuntimeError(f"Cannot load chart conventions: {conventions_path}")
    conventions = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(conventions)
    ascmc = swe.houses(jd_ut, conventions.DC_LAT, conventions.DC_LON, b"W")[1]
    return {
        "cycle_id": cycle_id,
        "seed_family_id": cycle["seed_family_id"],
        "pass_id": chosen_id,
        "utc": iso_utc(moment),
        "jd_ut": jd_ut,
        "positions": positions,
        "asc": ascmc[0] % 360.0,
        "mc": ascmc[1] % 360.0,
        "cast_location": "Washington, D.C.",
    }


def _date_at_noon_dc(date_iso: str) -> _dt.datetime:
    year, month, day = (int(part) for part in date_iso.split("-"))
    return _dt.datetime(
        year, month, day, 12, 0, tzinfo=ZoneInfo("America/New_York")
    ).astimezone(_dt.timezone.utc)


def _degree_label(longitude: float) -> str:
    sign = SIGNS[int(longitude // 30) % 12]
    degree = longitude % 30
    whole = int(degree)
    minutes = int(round((degree - whole) * 60))
    if minutes == 60:
        whole += 1
        minutes = 0
    return f"{whole}°{minutes:02d}' {sign}"


def currents(
    date_iso: str,
    *,
    vault_root: Path = DEFAULT_VAULT_ROOT,
    seed_registry_path: Path = DEFAULT_SEED_REGISTRY,
) -> list[dict[str, Any]]:
    """Compatibility adapter for legacy callers of ``currents(dateiso)``.

    It keeps the old structural keys while carrying the new exact fields.  It
    never emits ``approaching`` or legacy verdict prose; outside-orb rows are
    explicitly ``between_chapters``.  New builders should consume the v1 JSON
    payload directly rather than this adapter.
    """
    registry = load_seed_registry(seed_registry_path)
    registry_by_id = seed_registry_index(registry)
    moment = _date_at_noon_dc(date_iso)
    snapshot = current_snapshot(
        moment, vault_root=Path(vault_root), registry=registry, event_catalog=None
    )
    rows = []
    for state in snapshot["cycles"]:
        cycle = registry_by_id[state["cycle_id"]]
        anchor = next(
            seed_pass
            for seed_pass in cycle["passes"]
            if seed_pass["pass_id"] == cycle["display_anchor_pass_id"]
        )
        aspect = state["active_aspect"]
        positions = state["geometry"]["positions_deg"]
        first, second = cycle["pair"]
        rows.append(
            {
                "cycle_id": cycle["cycle_id"],
                "tier_id": cycle["tier_id"],
                "pair": list(cycle["pair"]),
                "name": f"{first}–{second}",
                "gloss": "",
                "cycle_yrs": cycle["nominal_cycle_years"],
                "seed_date": anchor["utc"][:10],
                "seed_utc": anchor["utc"],
                "seed_display": anchor["utc"],
                "seed_basis": cycle["anchor_basis"],
                "seed_family_utc": [item["utc"] for item in cycle["passes"]],
                "seed_detail": (
                    f"{len(cycle['passes'])}-pass {cycle['seed_family_label']}"
                    if len(cycle["passes"]) > 1
                    else cycle["seed_family_label"]
                ),
                "seed_deg": _degree_label(anchor["longitude_deg"]).split()[0],
                "seed_sign": anchor["sign"],
                "seed_lon": anchor["longitude_deg"],
                "seed_lons": {first: anchor["longitude_deg"], second: anchor["longitude_deg"]},
                "now": {
                    first: _degree_label(positions[first]),
                    second: _degree_label(positions[second]),
                },
                "now_lons": {first: positions[first], second: positions[second]},
                "elongation": state["geometry"]["elongation_deg"],
                "phase": (
                    f"{state['geometry']['phase_direction']} "
                    f"{state['geometry']['phase_name']}"
                ),
                "aspect": aspect["aspect_id"] if aspect else "between chapters",
                "orb": (
                    aspect["orb_deg"]
                    if aspect
                    else state["geometry"]["nearest_chapter_orb_deg"]
                ),
                "strength": aspect["strength"] if aspect else "between_chapters",
                "flowing": bool(aspect and aspect["flow_kind"] == "flowing"),
                "verdict": "",
                "underlies": [],
                "underlies_keys": [],
                "geometry": state["geometry"],
                "active_aspect": aspect,
                "nameability": state["nameability"],
                "interpretive_status": state["interpretive_status"],
            }
        )
    return rows


def chart_rec(
    seed: str,
    *,
    vault_root: Path = DEFAULT_VAULT_ROOT,
) -> tuple[dict[str, Any], dict[str, float]]:
    """Compatibility seed-chart caster used by existing wheel builders."""
    moment = parse_moment(seed) if "T" in seed else _date_at_noon_dc(seed)
    jd_ut = jd_of(moment)
    positions = []
    longitudes: dict[str, float] = {}
    for body, code in PLANET_CODES.items():
        result = swe.calc_ut(jd_ut, code, FLAGS)[0]
        longitude = result[0] % 360.0
        longitudes[body] = longitude
        positions.append(
            [
                body,
                SIGNS[int(longitude // 30) % 12],
                _degree_label(longitude).split()[0],
                1 if result[3] < 0 else 0,
                round(longitude, 2),
            ]
        )
    node_result = swe.calc_ut(jd_ut, swe.TRUE_NODE, FLAGS)[0]
    node_lon = node_result[0] % 360.0
    positions.append(
        [
            "Node",
            SIGNS[int(node_lon // 30) % 12],
            _degree_label(node_lon).split()[0],
            1,
            round(node_lon, 2),
        ]
    )
    conventions_path = Path(vault_root) / "99 - Templates" / "chart_conventions.py"
    conventions_spec = importlib.util.spec_from_file_location(
        "f250_chart_conventions_compat", conventions_path
    )
    if not conventions_spec or not conventions_spec.loader:
        raise RuntimeError(f"Cannot load chart conventions: {conventions_path}")
    conventions = importlib.util.module_from_spec(conventions_spec)
    conventions_spec.loader.exec_module(conventions)
    asc = swe.houses(jd_ut, conventions.DC_LAT, conventions.DC_LON, b"W")[1][0] % 360.0
    wheel_path = Path(vault_root) / "99 - Templates" / "wheel_lib.py"
    wheel_spec = importlib.util.spec_from_file_location("f250_wheel_lib_compat", wheel_path)
    if not wheel_spec or not wheel_spec.loader:
        raise RuntimeError(f"Cannot load wheel library: {wheel_path}")
    wheel = importlib.util.module_from_spec(wheel_spec)
    wheel_spec.loader.exec_module(wheel)
    return {
        "pos": positions,
        "asp": wheel.aspects_between(longitudes),
        "asc": round(asc, 2),
    }, longitudes


def stack(
    date_iso: str,
    *,
    vault_root: Path = DEFAULT_VAULT_ROOT,
    seed_registry_path: Path = DEFAULT_SEED_REGISTRY,
) -> dict[str, Any]:
    """Compatibility name backed only by the canonical chart registry."""
    return registered_context_for_date(
        date_iso, vault_root=vault_root, seed_registry_path=seed_registry_path
    )


def governing_ingress_id(
    date_iso: str,
    *,
    vault_root: Path = DEFAULT_VAULT_ROOT,
) -> str:
    context = registered_context_for_date(date_iso, vault_root=vault_root)
    return context["resolution"]["ingress_chart_id"].removeprefix("ingress-")


def validate_seed_registry(
    registry: dict[str, Any] | None = None,
) -> dict[str, Any]:
    registry = registry or load_seed_registry()
    errors = []
    checked = []
    for cycle in registry["cycles"]:
        slow, fast = slow_fast(cycle["pair"])
        for seed_pass in cycle["passes"]:
            jd_ut = jd_of(seed_pass["utc"])
            slow_lon, _ = _position(jd_ut, slow)
            fast_lon, _ = _position(jd_ut, fast)
            residual_arcsec = abs(_signed_delta(fast_lon, slow_lon)) * 3600.0
            circular_mid = (slow_lon + _signed_delta(fast_lon, slow_lon) / 2.0) % 360.0
            stored_delta_arcsec = (
                _circular_distance(circular_mid, seed_pass["longitude_deg"]) * 3600.0
            )
            row = {
                "cycle_id": cycle["cycle_id"],
                "pass_id": seed_pass["pass_id"],
                "residual_arcsec": residual_arcsec,
                "stored_longitude_delta_arcsec": stored_delta_arcsec,
            }
            checked.append(row)
            if residual_arcsec > 0.01:
                errors.append({**row, "error": "conjunction residual exceeds 0.01 arcsec"})
            if stored_delta_arcsec > 0.01:
                errors.append({**row, "error": "stored longitude differs by >0.01 arcsec"})
    return {
        "ok": not errors,
        "cycle_count": len(registry["cycles"]),
        "pass_count": len(checked),
        "checked": checked,
        "errors": errors,
        "unresolved_verification": [
            {
                "cycle_id": cycle["cycle_id"],
                "pass_id": seed_pass["pass_id"],
                "status": seed_pass["independent_verification_status"],
            }
            for cycle in registry["cycles"]
            for seed_pass in cycle["passes"]
            if seed_pass["independent_verification_status"]
            not in {"astro_gold_verified"}
        ],
    }


__all__ = [
    "CHAPTERS",
    "ORB_LIMITS",
    "SEED_ECHO_POLICY",
    "build_chart_stacks_payload",
    "build_event_catalog",
    "chart_rec",
    "current_snapshot",
    "currents",
    "exact_aspect_events",
    "governing_ingress_id",
    "load_seed_registry",
    "registered_stack_for_chart_id",
    "registered_stack_for_date",
    "registered_context_for_date",
    "seed_chart",
    "seed_echoes",
    "stack",
    "validate_seed_registry",
]
