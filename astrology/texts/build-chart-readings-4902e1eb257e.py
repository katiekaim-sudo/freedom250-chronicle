#!/usr/bin/env python3
"""Build the Sky & Charts Chart Readings instrument.

Projects the vault-owned Aster reading shelf into a click-through Observatory
reader. Markdown remains the editable authority; the HTML is its generated
view.

    python3 build_chart_readings.py
    python3 build_chart_readings.py --check
    python3 build_chart_readings.py --capture-baseline BASELINE_ID
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

from atomic_io import atomic_write_text


HERE = Path(__file__).resolve().parent
DEFAULT_VAULT = HERE.parent
if not (DEFAULT_VAULT / "03 - Astrology").is_dir():
    DEFAULT_VAULT = Path(
        os.environ.get(
            "F250_CHRONICLE_VAULT",
            Path.home() / "Documents" / "Obsidian" / "Freedom 250 Chronicle",
        )
    ).expanduser().resolve()
WHEEL_HOME = HERE if (HERE / "wheel_lib.py").is_file() else DEFAULT_VAULT / "99 - Templates"
if str(WHEEL_HOME) not in sys.path:
    sys.path.insert(0, str(WHEEL_HOME))
from wheel_lib import WHEEL_JS, point_aspects

VAULT = DEFAULT_VAULT
CROSS = VAULT / "04 - Synthesis" / "Cross-cuts"
OUTPUT = CROSS / "Chart Readings.html"
ASTROLOGY = VAULT / "03 - Astrology"
REGISTRY = ASTROLOGY / "chart_reading_registry.json"
BONES = VAULT / "99 - Templates" / "chart_reading_bones"
SYNODIC_STACKS = VAULT / "99 - Templates" / "chart_synodic_stacks.json"
# DR-084: the 2025 retrospective shelf keeps its own registry, bones and stacks so the
# 2026 builders that read chart_reading_bones/ are untouched.
REGISTRY_2025 = ASTROLOGY / "chart_reading_registry_2025.json"
# DR-085: factual corrections to sealed readings live in one ledger, never inside the reading.
AMENDMENT_LEDGER = ASTROLOGY / "Chart Reading Amendments — Ledger.md"
AMENDMENT_RE = re.compile(
    r'<!-- amendment reading_id="([^"]+)" rule="(DR-\d{3})" date="(\d{4}-\d{2}-\d{2})" -->\n'
    r'## [^\n]*\n\n(.*?)(?=\n<!-- amendment |\Z)',
    re.S,
)


def load_amendments() -> dict[str, list[dict[str, str]]]:
    """reading_id -> dated amendments from the ledger (empty when the ledger is absent)."""
    if not AMENDMENT_LEDGER.is_file():
        return {}
    text = AMENDMENT_LEDGER.read_text(encoding="utf-8")
    found: dict[str, list[dict[str, str]]] = {}
    for rid, rule, date, body in AMENDMENT_RE.findall(text):
        body = " ".join(body.split())
        if not body:
            fail(f"empty amendment for {rid} in {AMENDMENT_LEDGER.name}")
        found.setdefault(rid, []).append({"rule": rule, "date": date, "body": body})
    if text.count("<!-- amendment ") != sum(len(v) for v in found.values()):
        fail(f"{AMENDMENT_LEDGER.name} has a malformed amendment block")
    return found


def with_amendments(text: str, amendments: list[dict[str, str]]) -> str:
    """Show ledger amendments under the sealed reading; the reading file itself is never edited."""
    for row in amendments:
        text += (
            f"\n\n## Amendment — {row['date']} ({row['rule']})\n\n> {row['body']}\n\n"
            "*From the Chart Reading Amendments ledger. The reading above is the sealed original.*\n"
        )
    return text
BONES_2025 = VAULT / "99 - Templates" / "chart_reading_bones_2025"
SYNODIC_STACKS_2025 = VAULT / "99 - Templates" / "chart_synodic_stacks_2025.json"
SHELF_HAS_WATCHES = True
SYNODIC_STACK_SCHEMA = "freedom250.long-clocks.chart-stacks/v1"
SYNODIC_CYCLE_IDS = {
    "jupiter-saturn",
    "jupiter-uranus",
    "jupiter-neptune",
    "jupiter-pluto",
    "saturn-uranus",
    "saturn-neptune",
    "saturn-pluto",
    "uranus-neptune",
    "uranus-pluto",
    "neptune-pluto",
}
SYNODIC_TIERS = {"era_currents", "state_architecture", "political_delivery"}
NAMEABILITY_REASONS = {"root", "chart_ruler", "era", "exact_us_natal"}

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
SIGNS = (
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
)
KIND_TO_WHEEL = {
    "conjunction": "conjunct",
    "opposition": "opposite",
    "conjunct": "conjunct",
    "opposite": "opposite",
    "sextile": "sextile",
    "square": "square",
    "trine": "trine",
    "semisextile": "semisextile",
    "quincunx": "quincunx",
}

SEASONS: tuple[dict[str, str], ...] = (
    {
        "id": "winter",
        "label": "Winter 2026",
        "ingress": "ingress-2025-capricorn",
        "ingress_sky": "2025-capricorn",
        "window": "Jan 3 – Mar 19",
        "blurb": "Capricorn 2025 climate, six lunations, record census, and retrospective comparison.",
    },
    {
        "id": "aries",
        "label": "Aries 2026",
        "ingress": "ingress-2026-aries",
        "ingress_sky": "2026-aries",
        "window": "Mar 20 – Jun 21",
        "blurb": "Aries climate, six lunations, record census, and retrospective comparison.",
    },
    {
        "id": "cancer",
        "label": "Cancer 2026",
        "ingress": "ingress-2026-cancer",
        "ingress_sky": "2026-cancer",
        "window": "Jun 21 – Sep 23",
        "blurb": "Cancer climate, six lunations, record census, and mixed-boundary watch.",
    },
    {
        "id": "libra",
        "label": "Libra 2026",
        "ingress": "ingress-2026-libra",
        "ingress_sky": "2026-libra",
        "window": "Sep 23 – Mar 2027",
        "blurb": "Six-month Libra climate, six lunations, and the first clean prospective comparison.",
    },
    {
        "id": "capricorn",
        "label": "Capricorn 2026",
        "ingress": "ingress-2026-capricorn",
        "ingress_sky": "2026-capricorn",
        "window": "Dec 21 →",
        "blurb": "Nested winter subframe, opening Cancer Full Moon, and clean prospective watch.",
    },
)

SEASONS_2025: tuple[dict[str, str], ...] = (
    {
        "id": "2025-winter",
        "label": "Winter 2025 · retrospective",
        "ingress": "ingress-2024-capricorn",
        "ingress_sky": "",
        "window": "Dec 21, 2024 – Mar 19, 2025",
        "blurb": "The inauguration winter: 2024 Capricorn climate, six lunations, record census, and retrospective comparison.",
    },
    {
        "id": "2025-aries",
        "label": "Aries 2025 · retrospective",
        "ingress": "ingress-2025-aries",
        "ingress_sky": "2025-aries",
        "window": "Mar 20 – Jun 20, 2025",
        "blurb": "The year chart's first quarter: Aries climate, six lunations, record census, and retrospective comparison.",
    },
    {
        "id": "2025-cancer",
        "label": "Cancer 2025 · retrospective",
        "ingress": "ingress-2025-cancer",
        "ingress_sky": "2025-cancer",
        "window": "Jun 21 – Sep 21, 2025",
        "blurb": "Nested Cancer frame beneath the Aries year: seven lunations with both September eclipses, record census, and retrospective comparison.",
    },
    {
        "id": "2025-libra",
        "label": "Libra 2025 · retrospective",
        "ingress": "ingress-2025-libra",
        "ingress_sky": "2025-libra",
        "window": "Sep 22 – Dec 20, 2025",
        "blurb": "Nested Libra frame beneath the Aries year: six lunations, record census, and retrospective comparison.",
    },
)

GOVERNING_TO_SEASON_2025 = {
    "2024 Capricorn": "2025-winter",
    "2025 Aries": "2025-aries",
    "2025 Cancer": "2025-cancer",
    "2025 Libra": "2025-libra",
}

GOVERNING_TO_SEASON = {
    "2025 Capricorn": "winter",
    "2026 Aries": "aries",
    "2026 Cancer": "cancer",
    "2026 Libra": "libra",
    "2026 Capricorn": "capricorn",
}

KIND_LABEL = {
    "pass1": "Reading",
    "census": "Record census",
    "weave": "Storyline comparison",
    "comparison": "Storyline comparison",
}
HEADING = re.compile(r"^(#{1,6})\s+(.+)$")
DARKMODE_BLOCK = re.compile(
    r"\s*<!-- F250-DARKMODE-START -->.*?<!-- F250-DARKMODE-END -->\s*",
    re.S,
)
SHA256 = re.compile(r"^[0-9a-f]{64}$")
COMPARISON_MODES = {"retrospective_calibration", "prospective_watch"}
COMPARISON_STATES = {"open", "closed"}
DISPOSITIONS = {"Lines up", "Partial", "Miss", "Unresolved"}
EVIDENCE_LANES = {"Attention", "Official", "Entity"}
STATE_TRANSITION_SCHEMA = "f250.chart-readings.state-transition/v1"
STATE_TRANSITION_BOUNDARIES = {
    "mid_window_forward_addendum",
    "before_window_addendum",
}
STATE_TRANSITION_MATURITY = {
    "proposed",
    "authorized",
    "effective",
    "operating",
    "contested",
    "reversed",
    "failed",
    "unchanged",
}
FREEDOM_250_ARCS = {
    "The Monetary Reset",
    "The Information War",
    "War Footing — Iran & the Mideast",
    "Border & Homeland",
    "The Great Reckoning",
    "Great-Power Realignment",
    "Fringe, Disclosure & Health",
}
EXACT_ROUTE_KEYS = {
    "eventKey",
    "hearing",
    "eo",
    "researchId",
    "entityId",
    "notePath",
    "targetId",
}


def fail(message: str) -> None:
    raise SystemExit(f"Chart Readings build FAILED: {message}")


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def aggregate_sha256(rows: list[tuple[str, str]]) -> str:
    payload = "".join(f"{reading_id}:{digest}\n" for reading_id, digest in rows)
    return sha256_bytes(payload.encode("utf-8"))


def canonical_object_sha256(value: dict[str, Any], omit: set[str] | None = None) -> str:
    omitted = omit or set()
    payload = {key: child for key, child in value.items() if key not in omitted}
    raw = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return sha256_bytes(raw)


def configure_paths(args: argparse.Namespace) -> None:
    global VAULT, CROSS, OUTPUT, ASTROLOGY, REGISTRY, BONES, SYNODIC_STACKS
    global REGISTRY_2025, BONES_2025, SYNODIC_STACKS_2025, AMENDMENT_LEDGER
    VAULT = args.vault.expanduser().resolve()
    CROSS = VAULT / "04 - Synthesis" / "Cross-cuts"
    ASTROLOGY = VAULT / "03 - Astrology"
    REGISTRY = (
        args.registry.expanduser().resolve()
        if args.registry
        else ASTROLOGY / "chart_reading_registry.json"
    )
    BONES = (
        args.bones.expanduser().resolve()
        if args.bones
        else VAULT / "99 - Templates" / "chart_reading_bones"
    )
    SYNODIC_STACKS = (
        args.synodic_stacks.expanduser().resolve()
        if args.synodic_stacks
        else VAULT / "99 - Templates" / "chart_synodic_stacks.json"
    )
    OUTPUT = (
        args.output.expanduser().resolve()
        if args.output
        else CROSS / "Chart Readings.html"
    )
    # The 2025 retrospective shelf rides along only with the default registry;
    # a fixture registry (--registry) is built alone.
    REGISTRY_2025 = (
        ASTROLOGY / "chart_reading_registry_2025.json"
        if not args.registry
        else ASTROLOGY / "__no_2025_shelf__.json"
    )
    BONES_2025 = VAULT / "99 - Templates" / "chart_reading_bones_2025"
    SYNODIC_STACKS_2025 = VAULT / "99 - Templates" / "chart_synodic_stacks_2025.json"
    AMENDMENT_LEDGER = (
        ASTROLOGY / "Chart Reading Amendments — Ledger.md"
        if not args.registry
        else ASTROLOGY / "__no_amendment_ledger__.md"
    )


def sign_of(lon: float) -> str:
    return SIGNS[int(((lon % 360) + 360) % 360 // 30)]


def short_dms(body: dict[str, Any], lon: float) -> str:
    raw = str(body.get("lon_dms") or "")
    match = re.match(r"(\d+)°(\d+)", raw)
    if match:
        return f"{match.group(1)}°{match.group(2)}'"
    deg = ((lon % 360) + 360) % 360 % 30
    return f"{int(deg)}°{int((deg % 1) * 60):02d}'"


def face_line(bone: dict[str, Any]) -> str:
    bits: list[str] = []
    if bone.get("asc_dms"):
        bits.append(f"{bone['asc_dms']} rising")
    elif bone.get("asc_sign"):
        bits.append(f"{bone['asc_sign']} rising")
    if bone.get("sect"):
        bits.append(str(bone["sect"]))
    edt = str(bone.get("edt") or "")
    if edt:
        bits.append(edt[:16].replace("T", " ") + " ET")
    return " · ".join(bits)


def bone_to_rec(bone: dict[str, Any], label: str) -> dict[str, Any]:
    pos: list[list[Any]] = []
    lons: dict[str, float] = {}
    bodies = bone.get("pos") or {}
    for name in PLANET_ORDER:
        body = bodies.get(name)
        if not isinstance(body, dict) or body.get("lon") is None:
            continue
        lon = float(body["lon"])
        pos.append(
            [
                name,
                body.get("sign") or sign_of(lon),
                short_dms(body, lon),
                1 if body.get("retro") else 0,
                round(lon, 2),
            ]
        )
        lons[name] = lon
    if len(pos) < 8:
        fail(f"bones for {label!r} are missing planetary positions")

    extras: dict[str, float] = {}
    node = bone.get("node") or {}
    if node.get("lon") is not None:
        lon = float(node["lon"])
        pos.append(["Node", sign_of(lon), short_dms(node, lon), 1, round(lon, 2)])
        extras["Node"] = lon
    america = bone.get("america") or {}
    if america.get("lon") is not None:
        lon = float(america["lon"])
        pos.append(
            [
                "America",
                america.get("sign") or sign_of(lon),
                short_dms(america, lon),
                0,
                round(lon, 2),
            ]
        )
        extras["America"] = lon

    asp: list[dict[str, Any]] = []
    for row in bone.get("aspects") or []:
        kind = KIND_TO_WHEEL.get(str(row.get("kind") or ""), "")
        a, b = row.get("a"), row.get("b")
        if not kind or not a or not b:
            continue
        orb = float(row.get("orb") or 0)
        asp.append(
            {
                "t": f"{a} {kind} {b}",
                "o": round(orb, 2),
                "x": 1 if orb <= 0.3 else 0,
                "ap": 1 if row.get("applying") else 0,
            }
        )
    if extras and lons:
        asp.extend(point_aspects(extras, lons, cap=2.0))
    asp.sort(key=lambda row: row["o"])

    edt = str(bone.get("edt") or "")
    cap2 = "Whole Sign · Washington, D.C."
    if edt:
        cap2 = edt[:16].replace("T", " ") + " ET · D.C."
    rising = bone.get("asc_sign") or ""
    return {
        "pos": pos,
        "asp": asp,
        "asc": round(float(bone["asc"]), 2),
        "mc": round(float(bone["mc"]), 2) if bone.get("mc") is not None else None,
        "__date": label,
        "cap1": f"{rising} rising · Whole Sign".strip(" ·")
        if rising
        else "Whole Sign · D.C.",
        "cap2": cap2,
    }


def load_bone(stem: str) -> dict[str, Any]:
    path = BONES / f"{stem}.json"
    if not path.is_file():
        fail(f"missing bones file {path.name}")
    return load_json(path)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"cannot read {path}: {exc}")


def _has_synodic_verdict(value: Any) -> bool:
    """The chart join is geometry and identity only, never a finding generator."""
    forbidden = {"interpretation", "finding", "claim", "score", "prediction", "verdict", "causal"}
    if isinstance(value, dict):
        if forbidden.intersection(str(key).lower() for key in value):
            return True
        return any(_has_synodic_verdict(child) for child in value.values())
    if isinstance(value, list):
        return any(_has_synodic_verdict(child) for child in value)
    return False


def prepare_synodic_stacks(bones_index: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Validate and narrow the Long Clocks join for the reading payload.

    Three lanes remain independent:
    - current chart geometry: every cycle inside a standard aspect orb;
    - DR-020 phase narration: only engine-earned root/ruler, era, or exact-US rows;
    - seed echoes: active chart-point contacts to a registered seed family.

    The all-ten clock inventory remains factual Technical Proof.  No lane creates
    a storyline comparison finding or implies causation.
    """
    if not SYNODIC_STACKS.is_file():
        fail(f"synodic chart-stack data missing: {SYNODIC_STACKS}")
    payload = load_json(SYNODIC_STACKS)
    if not isinstance(payload, dict) or payload.get("schema") != SYNODIC_STACK_SCHEMA:
        fail(f"synodic chart stacks must use {SYNODIC_STACK_SCHEMA}")
    if _has_synodic_verdict(payload):
        fail("synodic chart stacks contain a forbidden verdict/finding field")
    if "approaching" in json.dumps(payload, ensure_ascii=False).lower():
        fail("synodic chart stacks use the prohibited approaching phase label")

    raw_charts = payload.get("charts")
    if isinstance(raw_charts, dict):
        chart_rows = []
        for chart_id, row in raw_charts.items():
            if not isinstance(row, dict) or row.get("chart_id") != chart_id:
                fail(f"synodic chart-stack key/identity drifted: {chart_id!r}")
            chart_rows.append(row)
    elif isinstance(raw_charts, list):
        chart_rows = raw_charts
    else:
        fail("synodic chart stacks need a charts object or list")

    bone_rows = {
        str(row.get("id") or ""): row
        for row in bones_index.get("charts") or []
        if row.get("id")
    }
    expected_chart_ids = set(bone_rows)
    ingress_ids = {
        chart_id for chart_id, row in bone_rows.items() if row.get("type") == "ingress"
    }
    expected_window_by_chart: dict[str, str] = {}
    season_ingress = {season["id"]: season["ingress"] for season in SEASONS}
    for chart_id, bone in bone_rows.items():
        if bone.get("type") == "ingress":
            expected_window_by_chart[chart_id] = chart_id
            continue
        season_id = GOVERNING_TO_SEASON.get(str(bone.get("governing") or ""))
        if not season_id or season_id not in season_ingress:
            fail(f"cannot derive synodic window for chart {chart_id!r}")
        expected_window_by_chart[chart_id] = season_ingress[season_id]

    prepared: dict[str, dict[str, Any]] = {}
    for chart in chart_rows:
        if not isinstance(chart, dict):
            fail("synodic chart stack contains a non-object row")
        chart_id = str(chart.get("chart_id") or "")
        if not chart_id or chart_id in prepared:
            fail(f"duplicate or blank synodic chart_id: {chart_id!r}")
        bone = bone_rows.get(chart_id)
        if not bone:
            fail(f"synodic chart stack points outside chart bones: {chart_id!r}")
        if chart.get("date") != bone.get("date"):
            fail(f"synodic chart-stack date drifted for {chart_id!r}")
        if chart.get("chart_type") != bone.get("type"):
            fail(f"synodic chart-stack type drifted for {chart_id!r}")
        window_id = str(chart.get("window_id") or "")
        if window_id not in ingress_ids or window_id != expected_window_by_chart[chart_id]:
            fail(f"synodic window_id drifted for {chart_id!r}: {window_id!r}")
        if not chart.get("utc"):
            fail(f"synodic chart stack lacks exact chart instant for {chart_id!r}")

        route = chart.get("long_clocks_route") or {}
        if route.get("view") != "long-clocks" or route.get("mode") != "moment" or \
           route.get("chart_id") != chart_id:
            fail(f"synodic moment route drifted for {chart_id!r}")

        cycles = chart.get("cycles") or []
        if not isinstance(cycles, list) or len(cycles) != len(SYNODIC_CYCLE_IDS):
            fail(f"synodic chart {chart_id!r} must compute all ten clock hands")
        cycle_by_id: dict[str, dict[str, Any]] = {}
        active_geometry: list[dict[str, Any]] = []
        nameable_cycles: list[dict[str, Any]] = []
        for cycle in cycles:
            if not isinstance(cycle, dict):
                fail(f"synodic chart {chart_id!r} has a non-object cycle")
            cycle_id = str(cycle.get("cycle_id") or "")
            if cycle_id not in SYNODIC_CYCLE_IDS or cycle_id in cycle_by_id:
                fail(f"synodic chart {chart_id!r} has invalid cycle_id {cycle_id!r}")
            if cycle.get("tier_id") not in SYNODIC_TIERS or not cycle.get("pair"):
                fail(f"synodic cycle identity is incomplete: {chart_id!r}/{cycle_id!r}")
            geometry = cycle.get("geometry") or {}
            for field in (
                "elongation_deg",
                "phase_direction",
                "nearest_chapter_id",
                "nearest_chapter_angle_deg",
                "nearest_chapter_orb_deg",
            ):
                if geometry.get(field) is None:
                    fail(f"synodic geometry lacks {field}: {chart_id!r}/{cycle_id!r}")
            active_aspect = cycle.get("active_aspect")
            if active_aspect is not None:
                if not isinstance(active_aspect, dict) or not active_aspect.get("aspect_id"):
                    fail(f"active synodic aspect is malformed: {chart_id!r}/{cycle_id!r}")
                try:
                    orb = float(active_aspect["orb_deg"])
                    orb_limit = float(active_aspect["orb_limit_deg"])
                except (KeyError, TypeError, ValueError):
                    fail(f"active synodic aspect lacks numeric orb: {chart_id!r}/{cycle_id!r}")
                if orb < 0 or orb > orb_limit:
                    fail(f"active synodic aspect exceeds its orb: {chart_id!r}/{cycle_id!r}")
                expected_strength = "exact" if orb <= 0.25 else "tight" if orb <= 1.5 else "active"
                if active_aspect.get("strength") != expected_strength:
                    fail(f"active synodic aspect strength drifted: {chart_id!r}/{cycle_id!r}")
                if not isinstance(active_aspect.get("applying"), bool) or \
                   not isinstance(active_aspect.get("separating"), bool):
                    fail(f"active synodic aspect lacks motion state: {chart_id!r}/{cycle_id!r}")
                active_geometry.append(cycle)

            nameability = cycle.get("nameability") or {}
            earned = nameability.get("earned")
            reasons = set(nameability.get("reasons") or [])
            if not isinstance(earned, bool) or not reasons.issubset(NAMEABILITY_REASONS):
                fail(f"DR-020 nameability is malformed: {chart_id!r}/{cycle_id!r}")
            if earned != bool(reasons):
                fail(f"DR-020 earned/reasons disagree: {chart_id!r}/{cycle_id!r}")
            if nameability.get("applies_to") != "phase_narrative_only" or \
               nameability.get("does_not_hide_direct_aspect") is not True:
                fail(f"DR-020 lane boundary drifted: {chart_id!r}/{cycle_id!r}")
            if cycle.get("tier_id") == "era_currents" and (not earned or "era" not in reasons):
                fail(f"era cycle is not nameable under DR-020: {chart_id!r}/{cycle_id!r}")
            if earned:
                nameable_cycles.append(cycle)

            cycle_route = cycle.get("long_clocks_route") or {}
            if cycle_route.get("view") != "long-clocks" or \
               cycle_route.get("mode") != "cycle" or \
               cycle_route.get("cycle_id") != cycle_id or \
               cycle_route.get("chart_id") != chart_id:
                fail(f"synodic cycle route drifted: {chart_id!r}/{cycle_id!r}")
            cycle_by_id[cycle_id] = cycle

        if set(cycle_by_id) != SYNODIC_CYCLE_IDS:
            fail(f"synodic cycle coverage drifted for {chart_id!r}")
        active_ids = list(chart.get("active_cycle_ids") or [])
        expected_active_ids = [cycle["cycle_id"] for cycle in active_geometry]
        if active_ids != expected_active_ids:
            fail(f"active synodic cycle order/coverage drifted for {chart_id!r}")
        nameable_ids = list(chart.get("nameable_cycle_ids") or [])
        expected_nameable_ids = [cycle["cycle_id"] for cycle in nameable_cycles]
        if nameable_ids != expected_nameable_ids:
            fail(f"nameable synodic cycle order/coverage drifted for {chart_id!r}")

        # Consume the engine's canonical edge lane directly. It duplicates the
        # current-aspect subset intentionally so Chart Readings never has to infer
        # a direct edge from phase-nameability state.
        active_edges = chart.get("active_edges") or []
        if not isinstance(active_edges, list) or \
           [edge.get("cycle_id") for edge in active_edges if isinstance(edge, dict)] != active_ids:
            fail(f"active synodic edge order/coverage drifted for {chart_id!r}")
        aspect_fields = (
            "aspect_id", "chapter_id", "angle_deg", "orb_deg", "orb_limit_deg",
            "applying", "separating", "motion_state", "strength", "flow_kind",
        )
        for edge in active_edges:
            if not isinstance(edge, dict):
                fail(f"active synodic edge is not an object for {chart_id!r}")
            cycle_id = str(edge.get("cycle_id") or "")
            cycle = cycle_by_id.get(cycle_id)
            aspect = (cycle or {}).get("active_aspect") or {}
            edge_route = edge.get("long_clocks_route") or {}
            if edge.get("edge_id") != f"{chart_id}::{cycle_id}" or \
               edge.get("tier_id") != (cycle or {}).get("tier_id") or \
               edge.get("pair") != (cycle or {}).get("pair") or \
               any(edge.get(field) != aspect.get(field) for field in aspect_fields) or \
               edge_route.get("view") != "long-clocks" or \
               edge_route.get("mode") != "cycle" or \
               edge_route.get("cycle_id") != cycle_id or \
               edge_route.get("chart_id") != chart_id:
                fail(f"active synodic edge/cycle contract drifted: {chart_id!r}/{cycle_id!r}")

        seed_echoes = chart.get("seed_echoes") or []
        if not isinstance(seed_echoes, list):
            fail(f"seed echoes must be a list for {chart_id!r}")
        echo_ids: set[str] = set()
        active_seed_echoes: list[dict[str, Any]] = []
        for echo in seed_echoes:
            if not isinstance(echo, dict):
                fail(f"seed echo is not an object for {chart_id!r}")
            echo_id = str(echo.get("echo_id") or "")
            if not echo_id or echo_id in echo_ids or echo.get("active") is not True:
                fail(f"seed echo identity/activity drifted for {chart_id!r}")
            if echo.get("cycle_id") not in SYNODIC_CYCLE_IDS or not echo.get("seed_family_id"):
                fail(f"seed echo lacks cycle/family identity: {chart_id!r}/{echo_id!r}")
            for field in ("matched_pass_id", "point", "aspect_id", "orb_deg", "orb_limit_deg"):
                if echo.get(field) is None:
                    fail(f"seed echo lacks {field}: {chart_id!r}/{echo_id!r}")
            if float(echo["orb_deg"]) < 0 or float(echo["orb_deg"]) > float(echo["orb_limit_deg"]):
                fail(f"seed echo exceeds its orb: {chart_id!r}/{echo_id!r}")
            echo_route = echo.get("long_clocks_route") or {}
            if echo_route.get("view") != "long-clocks" or \
               echo_route.get("mode") != "moment" or \
               echo_route.get("chart_id") != chart_id or \
               echo_route.get("cycle_id") != echo.get("cycle_id") or \
               echo_route.get("focus") != "seed-echoes":
                fail(f"seed echo route drifted: {chart_id!r}/{echo_id!r}")
            echo_ids.add(echo_id)
            active_seed_echoes.append(echo)

        prepared[chart_id] = {
            "chart_id": chart_id,
            "chart_type": chart["chart_type"],
            "date": chart["date"],
            "utc": chart["utc"],
            "window_id": window_id,
            "active_geometry": active_edges,
            "nameable_cycles": nameable_cycles,
            "seed_echoes": active_seed_echoes,
            "technical_cycles": cycles,
        }

    if set(prepared) != expected_chart_ids:
        fail(
            "synodic chart-stack coverage drifted: "
            f"missing={sorted(expected_chart_ids - set(prepared))} "
            f"extra={sorted(set(prepared) - expected_chart_ids)}"
        )
    return prepared


def resolve_vault_source(source_rel: str) -> Path:
    source = (VAULT / source_rel).resolve()
    try:
        source.relative_to(VAULT.resolve())
    except ValueError:
        fail(f"reading source escapes vault: {source_rel}")
    return source


def resolve_registry_artifact(artifact_rel: str) -> Path:
    root = REGISTRY.parent.resolve()
    artifact = (root / artifact_rel).resolve()
    try:
        artifact.relative_to(root)
    except ValueError:
        fail(f"comparison artifact escapes registry folder: {artifact_rel}")
    return artifact


def has_score_field(value: Any) -> bool:
    if isinstance(value, dict):
        for key, child in value.items():
            if "score" in str(key).lower() or has_score_field(child):
                return True
    elif isinstance(value, list):
        return any(has_score_field(child) for child in value)
    return False


def validate_exact_route(route: Any, evidence_id: str) -> None:
    if not isinstance(route, dict):
        fail(f"comparison evidence {evidence_id!r} has no exact route object")
    if not route.get("view") or not route.get("action"):
        fail(f"comparison evidence {evidence_id!r} route needs view and action")
    params = route.get("params")
    if not isinstance(params, dict) or not any(key in params for key in EXACT_ROUTE_KEYS):
        fail(
            f"comparison evidence {evidence_id!r} route needs one exact target key: "
            f"{sorted(EXACT_ROUTE_KEYS)}"
        )


def capture_baseline(registry: dict[str, Any], baseline_id: str) -> None:
    contract = registry.get("comparison_contract") or {}
    baselines = contract.get("baselines") or []
    baseline = next(
        (row for row in baselines if row.get("baseline_id") == baseline_id),
        None,
    )
    if not isinstance(baseline, dict):
        fail(f"unknown comparison baseline {baseline_id!r}")
    if (
        baseline.get("immutable")
        or baseline.get("captured_at")
        or baseline.get("aggregate_sha256")
    ):
        fail(f"baseline {baseline_id!r} is already pinned; overwrite is forbidden")

    reading_configs = {
        str(row.get("id") or ""): row
        for row in registry.get("readings") or []
        if row.get("kind") == "pass1"
    }
    artifact_dir = str(baseline.get("artifact_dir") or "")
    if not artifact_dir:
        fail(f"baseline {baseline_id!r} needs artifact_dir before capture")
    components = baseline.get("components") or []
    if not components:
        fail(f"baseline {baseline_id!r} has no component reading IDs")

    planned: list[tuple[dict[str, Any], str, Path, bytes, str]] = []
    for component in components:
        reading_id = str(component.get("reading_id") or "")
        config = reading_configs.get(reading_id)
        if not config:
            fail(f"baseline {baseline_id!r} references unknown chart reading {reading_id!r}")
        if component.get("artifact") or component.get("sha256"):
            fail(
                f"baseline {baseline_id!r} component {reading_id!r} is partially pinned; "
                "capture refuses mixed state"
            )
        source_rel = str(config.get("source") or "")
        source = resolve_vault_source(source_rel)
        if not source.is_file():
            fail(f"cannot capture missing live reading: {source_rel}")
        artifact_rel = str(Path(artifact_dir) / source.name)
        artifact = resolve_registry_artifact(artifact_rel)
        if artifact.exists():
            fail(f"baseline capture refuses to overwrite {artifact}")
        raw = source.read_bytes()
        planned.append((component, artifact_rel, artifact, raw, sha256_bytes(raw)))

    created: list[Path] = []
    try:
        for component, artifact_rel, artifact, raw, digest in planned:
            artifact.parent.mkdir(parents=True, exist_ok=True)
            descriptor = os.open(
                artifact,
                os.O_WRONLY | os.O_CREAT | os.O_EXCL,
                0o644,
            )
            with os.fdopen(descriptor, "wb") as handle:
                handle.write(raw)
            created.append(artifact)
            component["artifact"] = artifact_rel
            component["sha256"] = digest
        baseline["captured_at"] = dt.datetime.now().astimezone().isoformat(
            timespec="seconds"
        )
        baseline["immutable"] = True
        baseline["aggregate_sha256"] = aggregate_sha256(
            [
                (str(component["reading_id"]), str(component["sha256"]))
                for component in components
            ]
        )
        registry["version"] = max(2, int(registry.get("version") or 1))
        registry["updated"] = dt.date.today().isoformat()
        atomic_write_text(
            REGISTRY,
            json.dumps(registry, ensure_ascii=False, indent=2) + "\n",
        )
    except BaseException:
        for artifact in created:
            artifact.unlink(missing_ok=True)
        raise
    print(
        f"Captured immutable baseline {baseline_id} · {len(components)} readings · "
        f"{baseline['aggregate_sha256']}"
    )


def strip_frontmatter(raw: str) -> str:
    lines = raw.splitlines()
    if not lines or lines[0].strip() != "---":
        return raw
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return "\n".join(lines[index + 1 :]).lstrip("\n")
    fail("reading has an unclosed YAML frontmatter block")


def strip_comparison_evidence_targets(raw: str) -> str:
    """Keep source audit lists durable while the app renders them structurally."""
    return re.sub(
        r"\n\*\*Evidence targets\*\*\s*\n(?:\s*-\s+[^\n]+\n?)+",
        "\n",
        raw,
        flags=re.I,
    )


def first_heading(text: str) -> str:
    for line in strip_frontmatter(text).splitlines():
        match = HEADING.match(line.strip())
        if match:
            return match.group(2).strip()
    return path_title_fallback(text)


def path_title_fallback(text: str) -> str:
    for line in text.splitlines():
        if line.strip():
            return line.strip("# ").strip()
    return "Untitled reading"


def inline_md(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"(?<!_)_([^_\n]+)_(?!_)", r"<em>\1</em>", text)
    text = re.sub(
        r'\[([^\]]+)\]\((https?://[^)]+)\)',
        r'<a href="\2" target="_blank" rel="noopener">\1</a>',
        text,
    )
    text = re.sub(
        r'\[([^\]]+)\]\(([^)]+)\)',
        r'<span class="md-ref">\1</span>',
        text,
    )
    return text


def render_table(rows: list[str]) -> str:
    body: list[list[str]] = []
    for row in rows:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if cells and re.match(r"^:?-+:?$", cells[0].replace(" ", "")):
            continue
        body.append(cells)
    if not body:
        return ""
    head, rest = body[0], body[1:]
    out = ["<table><thead><tr>"]
    out.extend(f"<th>{inline_md(cell)}</th>" for cell in head)
    out.append("</tr></thead><tbody>")
    for row in rest:
        out.append("<tr>")
        out.extend(f"<td>{inline_md(cell)}</td>" for cell in row)
        out.append("</tr>")
    out.append("</tbody></table>")
    return "".join(out)


def markdown_to_html(raw: str) -> str:
    raw = strip_frontmatter(raw)
    proof: str | None = None
    proof_match = re.search(r"^##\s+Technical proof\s*$", raw, flags=re.I | re.M)
    if proof_match:
        proof = raw[proof_match.end() :].strip()
        raw = raw[: proof_match.start()].rstrip()
    lines = raw.splitlines()
    out: list[str] = []
    paragraph: list[str] = []
    in_code = False
    list_tag: str | None = None
    table_rows: list[str] = []

    def close_list() -> None:
        nonlocal list_tag
        if list_tag:
            out.append(f"</{list_tag}>")
            list_tag = None

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            out.append("<p>" + inline_md(" ".join(x.strip() for x in paragraph)) + "</p>")
            paragraph = []

    def flush_table() -> None:
        nonlocal table_rows
        if table_rows:
            out.append(render_table(table_rows))
            table_rows = []

    for line in lines:
        if line.strip().startswith("```"):
            flush_paragraph()
            flush_table()
            close_list()
            if in_code:
                out.append("</code></pre>")
            else:
                out.append("<pre><code>")
            in_code = not in_code
            continue
        if in_code:
            out.append(html.escape(line) + "\n")
            continue
        if line.lstrip().startswith("|"):
            flush_paragraph()
            close_list()
            table_rows.append(line)
            continue
        flush_table()
        heading = HEADING.match(line)
        numbered = re.match(r"^\s*\d+\.\s+(.+)$", line)
        bullet = re.match(r"^\s*[-*]\s+(.+)$", line)
        quote = re.match(r"^\s*>\s?(.*)$", line)
        if heading:
            flush_paragraph()
            close_list()
            level = min(4, len(heading.group(1)))
            out.append(f"<h{level}>{inline_md(heading.group(2))}</h{level}>")
        elif numbered:
            flush_paragraph()
            if list_tag != "ol":
                close_list()
                out.append("<ol>")
                list_tag = "ol"
            out.append("<li>" + inline_md(numbered.group(1)) + "</li>")
        elif bullet:
            flush_paragraph()
            if list_tag != "ul":
                close_list()
                out.append("<ul>")
                list_tag = "ul"
            out.append("<li>" + inline_md(bullet.group(1)) + "</li>")
        elif quote:
            flush_paragraph()
            close_list()
            out.append("<blockquote>" + inline_md(quote.group(1)) + "</blockquote>")
        elif re.match(r"^\s*---+\s*$", line):
            flush_paragraph()
            close_list()
            out.append("<hr>")
        elif not line.strip():
            flush_paragraph()
            close_list()
        else:
            if list_tag:
                close_list()
            paragraph.append(line)
    flush_paragraph()
    flush_table()
    close_list()
    if in_code:
        out.append("</code></pre>")
    rendered = "".join(out)
    if proof is not None:
        rendered += (
            '<details class="technical-proof"><summary>Technical proof</summary>'
            + markdown_to_html(proof)
            + "</details>"
        )
    return rendered


def first_paragraph(text: str) -> str:
    text = strip_frontmatter(text)
    chunks: list[str] = []
    for line in text.splitlines():
        if HEADING.match(line) or line.startswith("---") or line.startswith("```"):
            if chunks:
                break
            continue
        if not line.strip():
            if chunks:
                break
            continue
        chunks.append(line.strip())
        if len(" ".join(chunks)) > 280:
            break
    summary = " ".join(chunks)
    return re.sub(r"\s+", " ", summary)[:360]


def kind_label_for(kind: str, date: str | None) -> str:
    del date
    return KIND_LABEL[kind]


def auto_links(item: dict[str, Any]) -> list[dict[str, str]]:
    links: list[dict[str, str]] = []
    date = item.get("date")
    ingress_sky = item.get("ingress_sky")
    if item.get("chart_kind") == "ingress" and ingress_sky:
        links.append({"label": "Open the wheel", "kind": "wheel", "ingress": ingress_sky})
    elif item.get("chart_kind") == "lunation" and date:
        if ingress_sky:
            links.append({
                "label": "Overlay on climate",
                "kind": "overlay",
                "ingress": ingress_sky,
                "date": date,
            })
        links.append({"label": "Lunar Weather", "kind": "lunar", "date": date})
    if date:
        links.append({"label": "That day", "kind": "day", "date": date})
        links.append({"label": "Almanac", "kind": "almanac", "date": date})
    return links


def comparison_badge(mode: str) -> str:
    return (
        "Retrospective calibration"
        if mode == "retrospective_calibration"
        else "Prospective watch"
    )


def prepare_comparison_items(
    registry: dict[str, Any], readings: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    contract = registry.get("comparison_contract")
    if contract is None:
        return []
    if not isinstance(contract, dict) or contract.get("schema") != (
        "f250.chart-readings.comparison/v2"
    ):
        fail("comparison_contract must use f250.chart-readings.comparison/v2")
    policy = contract.get("policy") or {}
    if set(policy.get("modes") or []) != COMPARISON_MODES:
        fail("comparison policy mode vocabulary drifted")
    if set(policy.get("states") or []) != COMPARISON_STATES:
        fail("comparison policy state vocabulary drifted")
    if set(policy.get("dispositions") or []) != DISPOSITIONS:
        fail("comparison policy disposition vocabulary drifted")
    if set(policy.get("evidence_lanes") or []) != EVIDENCE_LANES:
        fail("comparison policy evidence-lane vocabulary drifted")
    if policy.get("scores_allowed") is not False:
        fail("comparison policy must explicitly forbid scores")
    if not str(policy.get("causation_notice") or "").strip():
        fail("comparison policy must preserve the rhyme-is-not-cause boundary")

    row_by_id = {row["id"]: row for row in readings}
    pass1_ids = {row["id"] for row in readings if row["kind"] == "pass1"}
    coverage: dict[str, int] = {reading_id: 0 for reading_id in pass1_ids}
    baseline_by_id: dict[str, dict[str, Any]] = {}
    for baseline in contract.get("baselines") or []:
        baseline_id = str(baseline.get("baseline_id") or "")
        if not baseline_id or baseline_id in baseline_by_id:
            fail(f"duplicate or blank comparison baseline id: {baseline_id!r}")
        mode = str(baseline.get("mode") or "")
        if mode not in COMPARISON_MODES:
            fail(f"baseline {baseline_id!r} has invalid mode {mode!r}")
        if baseline.get("immutable") is not True or not baseline.get("captured_at"):
            fail(f"baseline {baseline_id!r} is not immutably captured")
        aggregate = str(baseline.get("aggregate_sha256") or "")
        if not SHA256.fullmatch(aggregate):
            fail(f"baseline {baseline_id!r} has invalid aggregate SHA-256")
        component_payloads: list[dict[str, Any]] = []
        aggregate_rows: list[tuple[str, str]] = []
        seen_here: set[str] = set()
        for component in baseline.get("components") or []:
            reading_id = str(component.get("reading_id") or "")
            if reading_id not in pass1_ids:
                fail(
                    f"baseline {baseline_id!r} references unknown chart reading "
                    f"{reading_id!r}"
                )
            if reading_id in seen_here:
                fail(f"baseline {baseline_id!r} repeats {reading_id!r}")
            seen_here.add(reading_id)
            coverage[reading_id] += 1
            digest = str(component.get("sha256") or "")
            if not SHA256.fullmatch(digest):
                fail(
                    f"baseline {baseline_id!r} component {reading_id!r} has invalid SHA-256"
                )
            artifact_rel = str(component.get("artifact") or "")
            artifact = resolve_registry_artifact(artifact_rel)
            if not artifact.is_file():
                fail(f"baseline artifact missing: {artifact_rel}")
            artifact_raw = artifact.read_bytes()
            actual_digest = sha256_bytes(artifact_raw)
            if actual_digest != digest:
                fail(
                    f"baseline artifact hash mismatch for {reading_id!r}: "
                    f"registry={digest} actual={actual_digest}"
                )
            live_row = row_by_id[reading_id]
            live_source = resolve_vault_source(str(live_row["source_name"]))
            live_raw = live_source.read_bytes()
            current_digest = sha256_bytes(live_raw)
            try:
                artifact_text = artifact_raw.decode("utf-8")
                live_text = live_raw.decode("utf-8")
            except UnicodeDecodeError as exc:
                fail(f"baseline text for {reading_id!r} is not UTF-8: {exc}")
            aggregate_rows.append((reading_id, digest))
            component_payloads.append(
                {
                    "reading_id": reading_id,
                    "title": live_row["title"],
                    "artifact": artifact_rel,
                    "baseline_sha256": digest,
                    "current_sha256": current_digest,
                    "drift": "unchanged" if digest == current_digest else "drifted",
                    "baseline_html": markdown_to_html(artifact_text),
                    "current_html": markdown_to_html(live_text),
                }
            )
        if aggregate_sha256(aggregate_rows) != aggregate:
            fail(f"baseline {baseline_id!r} aggregate SHA-256 does not match components")
        prepared = dict(baseline)
        prepared["components"] = component_payloads
        prepared["drift_count"] = sum(
            component["drift"] == "drifted" for component in component_payloads
        )
        baseline_by_id[baseline_id] = prepared
        prospective_ids = set(baseline.get("prospective_reading_ids") or [])
        for component in component_payloads:
            row_by_id[component["reading_id"]]["baseline_context"] = {
                "baseline_id": baseline_id,
                "mode": mode,
                "captured_at": baseline["captured_at"],
                "capture_boundary": baseline.get("capture_boundary") or "",
                "clean_prospective": baseline.get("clean_prospective") is True,
                "prospective_eligible": component["reading_id"] in prospective_ids,
                "baseline_sha256": component["baseline_sha256"],
                "current_sha256": component["current_sha256"],
                "drift": component["drift"],
                "baseline_html": component["baseline_html"],
            }

    missing = sorted(reading_id for reading_id, count in coverage.items() if count == 0)
    repeated = sorted(reading_id for reading_id, count in coverage.items() if count > 1)
    if missing or repeated:
        fail(
            "comparison baselines must cover every chart-only reading exactly once: "
            f"missing={missing} repeated={repeated}"
        )

    virtual_items: list[dict[str, Any]] = []
    comparison_ids: set[str] = set()
    shelf_ids: set[str] = set()
    baseline_use: dict[str, int] = {baseline_id: 0 for baseline_id in baseline_by_id}
    extra_links = registry.get("links") or {}
    for comparison in contract.get("comparisons") or []:
        if has_score_field(comparison):
            fail("comparison records may not contain score fields")
        comparison_id = str(comparison.get("comparison_id") or "")
        shelf_id = str(comparison.get("shelf_id") or "")
        if not comparison_id or comparison_id in comparison_ids:
            fail(f"duplicate or blank comparison id: {comparison_id!r}")
        if not shelf_id or shelf_id in shelf_ids:
            fail(f"duplicate or blank comparison shelf id: {shelf_id!r}")
        comparison_ids.add(comparison_id)
        shelf_ids.add(shelf_id)
        baseline_id = str(comparison.get("baseline_id") or "")
        baseline = baseline_by_id.get(baseline_id)
        if not baseline:
            fail(f"comparison {comparison_id!r} references unknown baseline {baseline_id!r}")
        baseline_use[baseline_id] += 1
        mode = str(comparison.get("mode") or "")
        state = str(comparison.get("state") or "")
        if mode != baseline.get("mode") or mode not in COMPARISON_MODES:
            fail(f"comparison {comparison_id!r} mode does not match its baseline")
        if state not in COMPARISON_STATES:
            fail(f"comparison {comparison_id!r} has invalid state {state!r}")
        if state == "closed" and not comparison.get("closed_at"):
            fail(f"closed comparison {comparison_id!r} needs closed_at")
        if state == "open" and comparison.get("closed_at"):
            fail(f"open comparison {comparison_id!r} cannot have closed_at")

        evidence_rel = str(comparison.get("evidence_map") or "")
        if not evidence_rel:
            fail(f"comparison {comparison_id!r} needs an evidence_map")
        evidence_path = resolve_registry_artifact(evidence_rel)
        if not evidence_path.is_file():
            fail(f"comparison evidence map missing: {evidence_rel}")
        evidence_map = load_json(evidence_path)
        if evidence_map.get("schema") != "f250.chart-readings.evidence/v1":
            fail(f"comparison {comparison_id!r} evidence schema drifted")
        if evidence_map.get("comparison_id") != comparison_id:
            fail(f"comparison {comparison_id!r} evidence identity drifted")
        if evidence_map.get("mode") != mode or evidence_map.get("state") != state:
            fail(f"comparison {comparison_id!r} evidence state/mode drifted")
        method = evidence_map.get("method") or {}
        if method.get("rhyme_is_not_cause") is not True:
            fail(f"comparison {comparison_id!r} must preserve rhyme-is-not-cause")
        if method.get("scores_allowed") is not False:
            fail(f"comparison {comparison_id!r} evidence map must forbid scores")
        if set(method.get("evidence_lanes") or []) != EVIDENCE_LANES:
            fail(f"comparison {comparison_id!r} evidence-lane contract drifted")
        if set(method.get("dispositions") or []) != DISPOSITIONS:
            fail(f"comparison {comparison_id!r} disposition contract drifted")
        if mode == "prospective_watch":
            if method.get("finding_unit") != "state_transition":
                fail(f"comparison {comparison_id!r} must test state transitions")
            if method.get("state_transition_schema") != STATE_TRANSITION_SCHEMA:
                fail(f"comparison {comparison_id!r} transition schema drifted")
            transition_watch_ids = list(method.get("state_transition_watch_ids") or [])
            if not transition_watch_ids or len(transition_watch_ids) != len(
                set(transition_watch_ids)
            ):
                fail(f"comparison {comparison_id!r} needs unique transition watch ids")
        else:
            transition_watch_ids = []
        comparison = dict(comparison)
        comparison["state_transition_watch_ids"] = transition_watch_ids
        comparison["findings"] = list(evidence_map.get("findings") or [])
        comparison["boundary"] = evidence_map.get("boundary") or {}
        comparison["review_gates"] = evidence_map.get("review_gates") or []
        comparison["evidence_map_sha256"] = sha256_bytes(evidence_path.read_bytes())

        finding_ids: set[str] = set()
        findings = comparison.get("findings") or []
        if has_score_field(findings):
            fail(f"comparison {comparison_id!r} findings may not contain score fields")
        if state == "closed" and not findings:
            fail(f"closed comparison {comparison_id!r} needs findings")
        if state == "open" and findings:
            fail(f"open comparison {comparison_id!r} cannot preload findings")
        baseline_component_ids = {
            component["reading_id"] for component in baseline["components"]
        }
        for finding in findings:
            finding_id = str(finding.get("finding_id") or "")
            if not finding_id or finding_id in finding_ids:
                fail(f"comparison {comparison_id!r} has duplicate finding {finding_id!r}")
            finding_ids.add(finding_id)
            if finding.get("disposition") not in DISPOSITIONS:
                fail(f"finding {finding_id!r} has invalid disposition")
            for reference in finding.get("baseline_refs") or []:
                if reference.get("reading_id") not in baseline_component_ids:
                    fail(f"finding {finding_id!r} points outside its frozen baseline")
            evidence_ids: set[str] = set()
            for evidence in finding.get("evidence") or []:
                evidence_id = str(evidence.get("evidence_id") or "")
                if not evidence_id or evidence_id in evidence_ids:
                    fail(f"finding {finding_id!r} has duplicate evidence {evidence_id!r}")
                evidence_ids.add(evidence_id)
                if evidence.get("lane") not in EVIDENCE_LANES:
                    fail(f"evidence {evidence_id!r} has invalid lane")
                source_rel = str(evidence.get("source_path") or "")
                source_path = resolve_vault_source(source_rel) if source_rel else None
                if source_path is None or not source_path.is_file():
                    fail(f"evidence {evidence_id!r} source note is missing")
                recorded_sha = str(evidence.get("source_sha256") or "")
                if recorded_sha:
                    if not SHA256.fullmatch(recorded_sha):
                        fail(f"evidence {evidence_id!r} has invalid source SHA-256")
                    evidence["source_drift"] = (
                        "unchanged"
                        if sha256_bytes(source_path.read_bytes()) == recorded_sha
                        else "drifted"
                    )
                validate_exact_route(evidence.get("route"), evidence_id)

        payload = dict(comparison)
        payload["baseline"] = baseline
        payload["policy"] = {
            "causation_notice": policy["causation_notice"],
            "scores_allowed": False,
            "dispositions": list(policy["dispositions"]),
            "evidence_lanes": list(policy["evidence_lanes"]),
        }
        source_reading_id = str(comparison.get("source_reading_id") or "")
        if source_reading_id:
            source_row = row_by_id.get(source_reading_id)
            if not source_row or shelf_id != source_reading_id:
                fail(
                    f"comparison {comparison_id!r} source_reading_id must match an "
                    "existing shelf id"
                )
            source_row["comparison"] = payload
            continue
        if shelf_id in row_by_id:
            fail(f"virtual comparison shelf id collides with a reading: {shelf_id!r}")
        season = str(comparison.get("season") or "")
        season_row = next((row for row in SEASONS if row["id"] == season), None)
        if not season_row:
            fail(f"comparison {comparison_id!r} has invalid season {season!r}")
        climate = load_bone(season_row["ingress"])
        title = str(comparison.get("title") or comparison_id)
        summary = str(comparison.get("summary") or "")
        virtual_items.append(
            {
                "id": shelf_id,
                "kind": "comparison",
                "season": season,
                "title": title,
                "date": str(comparison.get("date") or ""),
                "chart_kind": "season",
                "ingress_sky": season_row["ingress_sky"],
                "sign": "",
                "eclipse": None,
                "source_name": "Structured comparison registry; no separate Markdown narrative",
                "authority_label": "Registry comparison state",
                "html": markdown_to_html(f"# {title}\n\n{summary}"),
                "summary": summary,
                "face": face_line(climate),
                "wheel": bone_to_rec(climate, f"{season.title()} climate"),
                "wheel_note": "Season climate wheel. The comparison baseline preserves the original reading text separately.",
                "badge": comparison_badge(mode),
                "links": list(extra_links.get(shelf_id, [])),
                "author": str(registry.get("author") or "Aster"),
                "status": str(registry.get("status") or "live_working"),
                "comparison": payload,
            }
        )

    unused = sorted(baseline_id for baseline_id, count in baseline_use.items() if count != 1)
    if unused:
        fail(f"every comparison baseline must be used exactly once: {unused}")
    expected_comparisons = int(contract.get("expected_comparison_count") or 0)
    if expected_comparisons and len(comparison_ids) != expected_comparisons:
        fail(
            f"comparison inventory drifted: expected {expected_comparisons}, "
            f"got {len(comparison_ids)}"
        )
    comparison_seasons = {
        str(row.get("season") or "") for row in contract.get("comparisons") or []
    }
    expected_seasons = {row["id"] for row in SEASONS}
    if comparison_seasons != expected_seasons:
        fail(
            "comparison seasons drifted: "
            f"missing={sorted(expected_seasons - comparison_seasons)} "
            f"extra={sorted(comparison_seasons - expected_seasons)}"
        )
    return virtual_items


def prepare_transition_watches(
    registry: dict[str, Any], readings: list[dict[str, Any]]
) -> None:
    """Validate and join immutable State Transition Watch addenda.

    The chart reading remains the primary hearing.  These records are a
    separately frozen, comparison-safe lens attached only to readings that the
    comparison registry explicitly identifies as prospective.
    """

    contract = registry.get("state_transition_contract")
    if not isinstance(contract, dict):
        fail("state_transition_contract is required")
    if contract.get("schema") != STATE_TRANSITION_SCHEMA:
        fail(f"state_transition_contract must use {STATE_TRANSITION_SCHEMA}")
    if contract.get("decision_rule") != "DR-064":
        fail("state_transition_contract must bind DR-064")
    if contract.get("required_for") != "prospective_reading_ids":
        fail("state-transition watches must be required for prospective_reading_ids")
    if contract.get("immutable_addenda") is not True:
        fail("state-transition watches must be immutable addenda")

    source_rel = str(contract.get("source") or "")
    source_digest = str(contract.get("source_sha256") or "")
    if not source_rel or not SHA256.fullmatch(source_digest):
        fail("state-transition source and SHA-256 are required")
    source_path = resolve_registry_artifact(source_rel)
    if not source_path.is_file():
        fail(f"state-transition source is missing: {source_rel}")
    actual_source_digest = sha256_bytes(source_path.read_bytes())
    if actual_source_digest != source_digest:
        fail(
            "state-transition source hash mismatch: "
            f"registry={source_digest} actual={actual_source_digest}"
        )

    watch_data = load_json(source_path)
    if watch_data.get("schema") != STATE_TRANSITION_SCHEMA:
        fail("state-transition source schema drifted")
    if watch_data.get("decision_rule") != contract.get("decision_rule"):
        fail("state-transition source decision rule drifted")

    thesis = watch_data.get("thesis") or {}
    thesis_rel = str(contract.get("thesis_source") or "")
    thesis_digest = str(contract.get("thesis_sha256") or "")
    if thesis.get("source") != thesis_rel or thesis.get("sha256") != thesis_digest:
        fail("state-transition thesis identity drifted between registry and source")
    if not thesis_rel or not SHA256.fullmatch(thesis_digest):
        fail("state-transition thesis source and SHA-256 are required")
    thesis_path = resolve_vault_source(thesis_rel)
    if not thesis_path.is_file():
        fail(f"state-transition thesis source is missing: {thesis_rel}")
    if sha256_bytes(thesis_path.read_bytes()) != thesis_digest:
        fail("state-transition thesis source hash drifted")
    if not str(thesis.get("governing_question") or "").strip():
        fail("state-transition thesis needs its governing authority question")

    policy = watch_data.get("policy") or {}
    for flag in ("chart_first", "lens_not_conclusion", "rhyme_is_not_cause"):
        if policy.get(flag) is not True:
            fail(f"state-transition policy must preserve {flag}")
    if policy.get("scores_allowed") is not False:
        fail("state-transition policy must explicitly forbid scores")
    if set(policy.get("evidence_lanes") or []) != EVIDENCE_LANES:
        fail("state-transition evidence-lane vocabulary drifted")
    if set(policy.get("maturity_states") or []) != STATE_TRANSITION_MATURITY:
        fail("state-transition maturity vocabulary drifted")
    if set(policy.get("boundaries") or []) != STATE_TRANSITION_BOUNDARIES:
        fail("state-transition boundary vocabulary drifted")
    if set(policy.get("arcs") or []) != FREEDOM_250_ARCS:
        fail("state-transition synchronization arcs drifted")

    comparison_contract = registry.get("comparison_contract") or {}
    baselines = comparison_contract.get("baselines") or []
    expected_ids: set[str] = set()
    baseline_by_reading: dict[str, dict[str, Any]] = {}
    for baseline in baselines:
        prospective_ids = list(baseline.get("prospective_reading_ids") or [])
        component_by_id = {
            str(component.get("reading_id") or ""): component
            for component in baseline.get("components") or []
        }
        for reading_id in prospective_ids:
            if reading_id in expected_ids:
                fail(f"prospective reading is repeated across baselines: {reading_id!r}")
            component = component_by_id.get(reading_id)
            if not component:
                fail(
                    f"prospective reading {reading_id!r} is not in baseline "
                    f"{baseline.get('baseline_id')!r}"
                )
            expected_ids.add(reading_id)
            baseline_by_reading[reading_id] = {
                "baseline_id": str(baseline.get("baseline_id") or ""),
                "baseline_sha256": str(component.get("sha256") or ""),
            }

    watches = watch_data.get("watches") or []
    expected_count = int(contract.get("expected_watch_count") or 0)
    if expected_count != len(expected_ids) or len(watches) != expected_count:
        fail(
            "state-transition inventory drifted: "
            f"expected={expected_count} prospective={len(expected_ids)} "
            f"watches={len(watches)}"
        )

    row_by_id = {row["id"]: row for row in readings}
    watch_ids: set[str] = set()
    watched_reading_ids: set[str] = set()
    watch_by_reading: dict[str, dict[str, Any]] = {}

    def required_text(watch: dict[str, Any], field: str) -> str:
        value = str(watch.get(field) or "").strip()
        if not value:
            fail(f"state-transition watch {watch.get('watch_id')!r} needs {field}")
        return value

    for watch in watches:
        if not isinstance(watch, dict) or has_score_field(watch):
            fail("state-transition watches must be score-free objects")
        watch_id = required_text(watch, "watch_id")
        reading_id = required_text(watch, "reading_id")
        if watch_id in watch_ids:
            fail(f"duplicate state-transition watch id: {watch_id!r}")
        if reading_id in watched_reading_ids:
            fail(f"duplicate state-transition reading id: {reading_id!r}")
        watch_ids.add(watch_id)
        watched_reading_ids.add(reading_id)
        if reading_id not in expected_ids:
            fail(f"watch {watch_id!r} points outside prospective_reading_ids")

        row = row_by_id.get(reading_id)
        if not row or row.get("kind") != "pass1":
            fail(f"watch {watch_id!r} requires a chart-only reading")
        if watch.get("season") != row.get("season"):
            fail(f"watch {watch_id!r} season does not match its chart reading")
        if not str(watch.get("chart_role") or "").strip():
            fail(f"watch {watch_id!r} needs a chart_role")
        if watch.get("immutable") is not True:
            fail(f"watch {watch_id!r} is not immutable")
        if watch.get("boundary") not in STATE_TRANSITION_BOUNDARIES:
            fail(f"watch {watch_id!r} has an invalid capture boundary")

        baseline_identity = baseline_by_reading[reading_id]
        context = row.get("baseline_context") or {}
        if context.get("prospective_eligible") is not True:
            fail(f"watch {watch_id!r} is not marked prospective in its live row")
        for key in ("baseline_id", "baseline_sha256"):
            if watch.get(key) != baseline_identity[key] or context.get(key) != watch.get(key):
                fail(f"watch {watch_id!r} {key} identity drifted")

        recorded_watch_digest = str(watch.get("watch_sha256") or "")
        if not SHA256.fullmatch(recorded_watch_digest):
            fail(f"watch {watch_id!r} has an invalid SHA-256")
        actual_watch_digest = canonical_object_sha256(watch, {"watch_sha256"})
        if actual_watch_digest != recorded_watch_digest:
            fail(
                f"watch {watch_id!r} hash mismatch: "
                f"recorded={recorded_watch_digest} actual={actual_watch_digest}"
            )

        frozen_at = required_text(watch, "frozen_at")
        try:
            frozen_date = dt.datetime.fromisoformat(frozen_at).date()
            reading_date = dt.date.fromisoformat(str(row.get("date") or ""))
        except ValueError as exc:
            fail(f"watch {watch_id!r} has an invalid date boundary: {exc}")
        if frozen_date > reading_date:
            fail(f"watch {watch_id!r} was frozen after its chart date")

        for field in (
            "authority_question",
            "decision_right",
            "current_holder",
            "claimant_or_constraint",
        ):
            required_text(watch, field)
        transition = watch.get("transition") or {}
        if not str(transition.get("from") or "").strip() or not str(
            transition.get("toward") or ""
        ).strip():
            fail(f"watch {watch_id!r} needs a from-to transition")
        mechanisms = watch.get("mechanisms") or []
        if not mechanisms or any(not str(value).strip() for value in mechanisms):
            fail(f"watch {watch_id!r} needs named transition mechanisms")
        states = set(watch.get("states_to_distinguish") or [])
        if not states or not states.issubset(STATE_TRANSITION_MATURITY):
            fail(f"watch {watch_id!r} uses invalid maturity states")
        if "unchanged" not in states:
            fail(f"watch {watch_id!r} must preserve unchanged as a valid outcome")

        poles = watch.get("poles") or {}
        if set(poles) != {"constructive", "shadow", "continuity"} or any(
            not str(poles.get(key) or "").strip()
            for key in ("constructive", "shadow", "continuity")
        ):
            fail(f"watch {watch_id!r} must hold both poles and continuity")
        synchronization = watch.get("synchronization") or {}
        arcs = set(synchronization.get("arcs") or [])
        if not arcs or not arcs.issubset(FREEDOM_250_ARCS):
            fail(f"watch {watch_id!r} uses invalid synchronization arcs")
        if not str(synchronization.get("watch_for") or "").strip():
            fail(f"watch {watch_id!r} needs a synchronization test")
        evidence_test = watch.get("evidence_test") or {}
        if set(evidence_test.get("lanes") or []) != EVIDENCE_LANES:
            fail(f"watch {watch_id!r} evidence lanes drifted")
        for field in ("lines_up_if", "miss_if", "unresolved_if"):
            if not str(evidence_test.get(field) or "").strip():
                fail(f"watch {watch_id!r} needs evidence test {field}")

        prepared = dict(watch)
        prepared["thesis_question"] = thesis["governing_question"]
        row["transition_watch"] = prepared
        watch_by_reading[reading_id] = prepared

    if watched_reading_ids != expected_ids:
        fail(
            "state-transition coverage drifted: "
            f"missing={sorted(expected_ids - watched_reading_ids)} "
            f"extra={sorted(watched_reading_ids - expected_ids)}"
        )

    comparisons_by_baseline = {
        str(row.get("comparison", {}).get("baseline_id") or ""): row
        for row in readings
        if row.get("comparison")
    }
    for baseline in baselines:
        baseline_id = str(baseline.get("baseline_id") or "")
        prospective_ids = set(baseline.get("prospective_reading_ids") or [])
        comparison_row = comparisons_by_baseline.get(baseline_id)
        if prospective_ids and not comparison_row:
            fail(f"prospective baseline {baseline_id!r} has no comparison shelf row")
        if not comparison_row:
            continue
        ordered_ids = [
            str(component.get("reading_id") or "")
            for component in baseline.get("components") or []
            if component.get("reading_id") in prospective_ids
        ]
        comparison_row["comparison"]["transition_watches"] = [
            watch_by_reading[reading_id] for reading_id in ordered_ids
        ]
        expected_watch_ids = [
            watch_by_reading[reading_id]["watch_id"] for reading_id in ordered_ids
        ]
        recorded_watch_ids = comparison_row["comparison"].get(
            "state_transition_watch_ids"
        ) or []
        if recorded_watch_ids != expected_watch_ids:
            fail(
                f"comparison watch map drifted for {baseline_id!r}: "
                f"recorded={recorded_watch_ids} expected={expected_watch_ids}"
            )


def collect_readings() -> tuple[list[dict[str, Any]], dict[str, Any], dict[str, Any]]:
    if not REGISTRY.is_file():
        fail(f"reading registry missing: {REGISTRY}")
    if not BONES.is_dir():
        fail(f"chart reading bones folder missing: {BONES}")
    registry = load_json(REGISTRY)
    bones_index = load_json(BONES / "index.json")
    bones = {row["id"]: row for row in bones_index.get("charts", [])}
    synodic_stacks = prepare_synodic_stacks(bones_index)
    extra_links = registry.get("links") or {}
    amendments = load_amendments()

    season_by_ingress = {row["ingress"]: row["id"] for row in SEASONS}
    sky_by_season = {row["id"]: row["ingress_sky"] for row in SEASONS}
    readings: list[dict[str, Any]] = []
    seen: set[str] = set()
    for config in registry.get("readings") or []:
        stem = str(config.get("id") or "")
        kind = str(config.get("kind") or "")
        source_rel = str(config.get("source") or "")
        if not stem or kind not in KIND_LABEL or not source_rel:
            fail(f"invalid reading registry row: {config!r}")
        if stem in seen:
            fail(f"duplicate reading registry id: {stem}")
        seen.add(stem)
        source = resolve_vault_source(source_rel)
        if not source.is_file():
            fail(f"missing registered reading: {source_rel}")
        text = source.read_text(encoding="utf-8")
        render_text = (
            strip_comparison_evidence_targets(text)
            if kind == "comparison"
            else text
        )
        if kind == "pass1" and stem in amendments:
            render_text = with_amendments(render_text, amendments[stem])

        if kind == "pass1":
            bone = bones.get(stem)
            if not bone:
                fail(f"registered chart reading has no bones index row: {stem}")
            if stem.startswith("ingress-"):
                season = season_by_ingress.get(stem)
                chart_kind = "ingress"
            else:
                season = GOVERNING_TO_SEASON.get(str(bone.get("governing") or ""))
                chart_kind = "lunation"
            if not season:
                fail(f"{stem} could not be placed in a season")
            date = bone.get("date")
            sign = bone.get("sign") or ""
            full_bone = load_bone(stem)
            item = {
                "id": stem,
                "kind": kind,
                "season": season,
                "title": first_heading(render_text),
                "date": date,
                "chart_kind": chart_kind,
                "ingress_sky": sky_by_season[season],
                "sign": sign,
                "eclipse": bone.get("eclipse"),
                "source_name": source_rel,
                "html": markdown_to_html(render_text),
                "summary": first_paragraph(render_text),
                "face": face_line(full_bone),
                "wheel": bone_to_rec(full_bone, first_heading(text)),
                "wheel_note": "Washington, D.C. · Whole Sign · computed from the registered chart facts.",
                "synodic_stack": synodic_stacks[stem],
            }
        else:
            season = str(config.get("season") or "")
            date = str(config.get("date") or "")
            if season not in sky_by_season or not date:
                fail(f"registered {kind} needs a valid season and date: {stem}")
            climate_id = next(row["ingress"] for row in SEASONS if row["id"] == season)
            climate = load_bone(climate_id)
            item = {
                "id": stem,
                "kind": kind,
                "season": season,
                "title": first_heading(render_text),
                "date": date,
                "chart_kind": "season",
                "ingress_sky": sky_by_season[season],
                "sign": "",
                "eclipse": None,
                "source_name": source_rel,
                "html": markdown_to_html(render_text),
                "summary": first_paragraph(render_text),
                "face": face_line(climate),
                "wheel": bone_to_rec(climate, f"{season.title()} climate"),
                "wheel_note": "Season climate wheel. Individual chart readings carry their own weather wheels.",
            }
        item["badge"] = kind_label_for(kind, date)
        item["links"] = auto_links(item) + list(extra_links.get(stem, []))
        item["author"] = str(config.get("author") or registry.get("author") or "Aster")
        item["status"] = str(config.get("status") or registry.get("status") or "live_working")
        readings.append(item)

    expected_pass1 = {row["id"] for row in bones_index.get("charts", [])}
    got_pass1 = {row["id"] for row in readings if row["kind"] == "pass1"}
    if got_pass1 != expected_pass1:
        fail(
            "Pass 1 coverage drifted: "
            f"missing={sorted(expected_pass1 - got_pass1)} "
            f"extra={sorted(got_pass1 - expected_pass1)}"
        )
    virtual_comparisons = prepare_comparison_items(registry, readings)
    readings.extend(virtual_comparisons)
    if SHELF_HAS_WATCHES:
        prepare_transition_watches(registry, readings)
    contract = registry.get("comparison_contract") or {}
    expected_shelf = int(contract.get("expected_shelf_count") or 34)
    if len(readings) != expected_shelf:
        fail(f"reading shelf coverage drifted: expected {expected_shelf}, got {len(readings)}")
    return readings, bones_index, registry


def collect_all_shelves() -> tuple[list[dict[str, Any]], dict[str, Any], dict[str, Any]]:
    """The 2026 shelf, then the 2025 retrospective shelf (DR-084), each validated alone."""
    global REGISTRY, BONES, SYNODIC_STACKS, SEASONS, GOVERNING_TO_SEASON, SHELF_HAS_WATCHES
    readings, bones_index, registry = collect_readings()
    if not REGISTRY_2025.is_file():
        return readings, bones_index, registry
    saved = (REGISTRY, BONES, SYNODIC_STACKS, SEASONS, GOVERNING_TO_SEASON, SHELF_HAS_WATCHES)
    REGISTRY, BONES, SYNODIC_STACKS = REGISTRY_2025, BONES_2025, SYNODIC_STACKS_2025
    SEASONS, GOVERNING_TO_SEASON, SHELF_HAS_WATCHES = SEASONS_2025, GOVERNING_TO_SEASON_2025, False
    try:
        shelf_2025, _bones_2025, _registry_2025 = collect_readings()
    finally:
        (REGISTRY, BONES, SYNODIC_STACKS, SEASONS, GOVERNING_TO_SEASON, SHELF_HAS_WATCHES) = saved
    clash = {row["id"] for row in readings} & {row["id"] for row in shelf_2025}
    if clash:
        fail(f"2025 shelf ids collide with the 2026 shelf: {sorted(clash)}")
    for row in shelf_2025:
        row["shelf"] = "2025-retrospective"
    pass1_ids = {row["id"] for row in readings + shelf_2025 if row["kind"] == "pass1"}
    stray = set(load_amendments()) - pass1_ids
    if stray:
        fail(f"amendment ledger names readings that are not on any shelf: {sorted(stray)}")
    return readings + shelf_2025, bones_index, registry


def js_safe_json(value: Any) -> str:
    return (
        json.dumps(value, ensure_ascii=False, indent=2)
        .replace("&", "\\u0026")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="color-scheme" content="light dark">
<title>Chart Readings — Freedom 250 Observatory</title>
<style>
:root{
  --rd-bg:#f4f0e6;--rd-panel:#fbf8f1;--rd-card:#fffdf8;
  --rd-ink:#28251f;--rd-muted:#736b5d;--rd-faint:#9b9282;
  --rd-line:#d8d0c1;--rd-accent:#8a542f;--rd-accent-soft:#efe1d2;
  --rd-focus:#2f6d8a;--rd-shadow:rgba(43,35,24,.16);
  --rd-weave:#6b3a6a;--rd-census:#2f6d5a;--rd-transition:#315f68;
  --rd-good:#356b4d;--rd-warn:#916c22;--rd-bad:#9b433c;--rd-open:#315f7b;
  color-scheme:light;
}
html[data-theme="dark"]{
  --rd-bg:#16140f;--rd-panel:#1d1a13;--rd-card:#242017;
  --rd-ink:#e6dfd0;--rd-muted:#b9b09c;--rd-faint:#857d6c;
  --rd-line:#3a3426;--rd-accent:#d99570;--rd-accent-soft:#35271d;
  --rd-focus:#70b7d4;--rd-shadow:rgba(0,0,0,.4);
  --rd-weave:#d4a3d0;--rd-census:#7dbea8;--rd-transition:#91c5ca;
  --rd-good:#82c79d;--rd-warn:#e0bd70;--rd-bad:#e28c82;--rd-open:#78b9d4;
  color-scheme:dark;
}
*{box-sizing:border-box}
html,body{width:100%;height:100%;margin:0;overflow:hidden;background:var(--rd-bg);color:var(--rd-ink)}
body{font-family:Georgia,"Iowan Old Style","Times New Roman",serif}
button,input{font:inherit}
button:focus-visible,input:focus-visible{outline:3px solid color-mix(in srgb,var(--rd-focus) 48%,transparent);outline-offset:2px}
.shell{
  display:grid;grid-template-columns:280px minmax(0,1fr);grid-template-rows:minmax(0,1fr);
  height:100%;min-height:0
}
.rail{
  min-width:0;min-height:0;overflow-y:auto;overscroll-behavior:contain;padding:16px 12px 32px;
  background:var(--rd-panel);border-right:1px solid var(--rd-line)
}
.brand{padding:2px 6px 12px}
.brand h1{font:700 22px/1.12 Georgia,serif;margin:0}
.brand span{display:block;margin-top:5px;color:var(--rd-muted);font:italic 11px/1.4 Georgia,serif}
.search{position:relative;margin:0 4px 14px}
.search label{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.search input{
  width:100%;border:1px solid var(--rd-line);border-radius:9px;background:var(--rd-card);
  color:var(--rd-ink);padding:8px 10px 8px 30px;font:12px/1.3 Inter,ui-sans-serif,sans-serif
}
.search::before{content:"⌕";position:absolute;left:9px;top:5px;color:var(--rd-faint);font-size:17px}
.season{margin:0 0 14px}
.season h2{
  margin:0 6px 2px;color:var(--rd-accent);font:700 10px/1.2 Inter,ui-sans-serif,sans-serif;
  letter-spacing:.15em;text-transform:uppercase
}
.season .win{margin:0 6px 6px;color:var(--rd-faint);font:italic 11px/1.35 Georgia,serif}
.item{
  display:block;width:100%;border:1px solid transparent;border-radius:8px;background:transparent;
  color:var(--rd-ink);text-align:left;padding:7px 8px;cursor:pointer;margin:0 0 3px
}
.item:hover{background:var(--rd-card);border-color:var(--rd-line)}
.item.active{background:var(--rd-accent-soft);border-color:color-mix(in srgb,var(--rd-accent) 38%,var(--rd-line));box-shadow:inset 3px 0 0 var(--rd-accent)}
.item[hidden]{display:none}
.item .name{display:block;font:700 12.5px/1.3 Inter,ui-sans-serif,sans-serif}
.item .meta{display:block;margin-top:2px;color:var(--rd-muted);font:11px/1.3 Inter,ui-sans-serif,sans-serif}
.main{min-width:0;min-height:0;display:flex;flex-direction:column;height:100%;overflow:hidden}
.top{
  flex:0 0 auto;display:flex;flex-wrap:wrap;align-items:flex-start;gap:10px 14px;padding:10px 22px 10px;
  background:var(--rd-panel);border-bottom:1px solid var(--rd-line)
}
.titles{min-width:0;flex:1}
.kicker{color:var(--rd-accent);font:700 10px/1.2 Inter,ui-sans-serif,sans-serif;letter-spacing:.14em;text-transform:uppercase}
.titles h2{margin:3px 0 0;font:700 20px/1.2 Georgia,serif}
.note{margin:4px 0 0;color:var(--rd-muted);font:italic 12px/1.35 Georgia,serif}
.actions{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.chip{
  border:1px solid var(--rd-line);border-radius:999px;background:var(--rd-card);color:var(--rd-ink);
  padding:5px 10px;font:600 11px/1.2 Inter,ui-sans-serif,sans-serif;cursor:pointer
}
.chip:hover{border-color:var(--rd-accent);color:var(--rd-accent)}
.chip.weave{border-color:color-mix(in srgb,var(--rd-weave) 45%,var(--rd-line));color:var(--rd-weave)}
.stage{
  flex:1 1 auto;min-width:0;min-height:0;overflow-y:scroll;overscroll-behavior:contain;
  padding:8px 0 56px;-webkit-overflow-scrolling:touch
}
.wheel-wrap{
  max-width:46rem;margin:8px auto 0;padding:0 18px 6px
}
.wheel-wrap[hidden]{display:none}
.wheel-card{
  border:1px solid var(--rd-line);border-radius:12px;background:var(--rd-card);padding:8px 10px 12px
}
.wheel-card .wlabel{
  margin:0 0 4px;text-align:center;color:var(--rd-muted);font:italic 12px/1.35 Georgia,serif
}
#wheelbox{max-width:520px;margin:0 auto}
#wheelbox svg{width:100%;height:auto;display:block}
.article{
  max-width:46rem;margin:0 auto;padding:10px 26px 8px;font-size:16.5px;line-height:1.62
}
.article h1{font-size:1.55rem;line-height:1.2;margin:0 0 12px}
.article h2{font-size:1.18rem;margin:1.6em 0 .45em;color:var(--rd-accent)}
.article h3{font-size:1.02rem;margin:1.35em 0 .35em}
.article h4{font-size:.95rem;margin:1.2em 0 .3em;letter-spacing:.02em}
.article p{margin:0 0 .9em}
.article ul,.article ol{margin:.2em 0 1em;padding-left:1.3em}
.article li{margin:.18em 0}
.article blockquote{
  margin:0 0 1em;padding:.15em 0 .15em 1em;border-left:3px solid var(--rd-accent);
  color:var(--rd-muted);font-style:italic
}
.article hr{border:0;border-top:1px solid var(--rd-line);margin:1.4em 0}
.article table{width:100%;border-collapse:collapse;margin:0 0 1.1em;font-size:.92em}
.article th,.article td{border:1px solid var(--rd-line);padding:5px 8px;text-align:left;vertical-align:top}
.article th{background:var(--rd-accent-soft);font:700 12px/1.3 Inter,ui-sans-serif,sans-serif}
.article code{font:12.5px/1.4 ui-monospace,Menlo,monospace}
.article pre{
  overflow:auto;padding:10px 12px;border:1px solid var(--rd-line);border-radius:8px;
  background:var(--rd-card);font-size:12.5px
}
.article a,.md-ref{color:var(--rd-accent)}
.technical-proof{
  margin:1.45em 0 .8em;border:1px solid var(--rd-line);border-radius:10px;background:var(--rd-card)
}
.technical-proof summary{
  cursor:pointer;padding:10px 12px;color:var(--rd-accent);
  font:700 12px/1.35 Inter,ui-sans-serif,sans-serif;letter-spacing:.02em
}
.technical-proof[open] summary{border-bottom:1px solid var(--rd-line)}
.technical-proof > :not(summary){margin-left:14px;margin-right:14px}
.technical-proof > :last-child{margin-bottom:14px}
.pager{display:flex;justify-content:space-between;gap:12px;max-width:46rem;margin:18px auto 0;padding:0 26px}
.pager button{
  border:1px solid var(--rd-line);border-radius:8px;background:var(--rd-card);color:var(--rd-ink);
  padding:8px 12px;cursor:pointer;font:12px/1.3 Inter,ui-sans-serif,sans-serif
}
.pager button[disabled]{opacity:.4;cursor:default}
.empty{margin:40px 26px;color:var(--rd-muted);text-align:center}
.authority{
  max-width:46rem;margin:0 auto;padding:0 26px 8px;color:var(--rd-faint);
  font:italic 12px/1.45 Georgia,serif
}
.synodic-stack{
  max-width:52rem;margin:10px auto 22px;padding:0 18px;font-family:Inter,ui-sans-serif,sans-serif
}
.synodic-stack[hidden]{display:none}
.synodic-card{
  overflow:hidden;border:1px solid color-mix(in srgb,var(--rd-accent) 34%,var(--rd-line));
  border-radius:12px;background:var(--rd-card)
}
.synodic-card>summary{
  display:flex;align-items:center;gap:9px;cursor:pointer;padding:11px 13px;
  color:var(--rd-accent);font:750 12px/1.35 Inter,sans-serif
}
.synodic-card[open]>summary{border-bottom:1px solid var(--rd-line)}
.synodic-summary-meta{margin-left:auto;color:var(--rd-muted);font-weight:600;font-size:10.5px}
.synodic-body{padding:13px}
.synodic-notice{
  margin:0 0 12px;padding:8px 10px;border-left:3px solid var(--rd-accent);
  background:var(--rd-accent-soft);color:var(--rd-muted);font:italic 12px/1.45 Georgia,serif
}
.synodic-lane{margin:0 0 14px}
.synodic-lane h4{
  margin:0 0 6px;color:var(--rd-accent);font:800 9.5px/1.2 Inter,sans-serif;
  letter-spacing:.11em;text-transform:uppercase
}
.synodic-lane-note{margin:0 0 7px;color:var(--rd-faint);font:11px/1.4 Georgia,serif}
.synodic-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:7px}
.synodic-item{
  min-width:0;padding:9px 10px;border:1px solid var(--rd-line);border-radius:8px;
  background:var(--rd-panel)
}
button.synodic-item{color:var(--rd-ink);text-align:left;cursor:pointer}
button.synodic-item:hover{border-color:var(--rd-accent)}
.synodic-item strong{display:block;font:700 11.5px/1.3 Inter,sans-serif}
.synodic-item span{display:block;margin-top:3px;color:var(--rd-muted);font:11px/1.35 Georgia,serif}
.synodic-reasons{display:flex!important;flex-wrap:wrap;gap:4px;margin-top:6px!important}
.synodic-reasons em{
  border:1px solid var(--rd-line);border-radius:999px;padding:2px 6px;color:var(--rd-accent);
  font:650 9px/1.2 Inter,sans-serif;font-style:normal
}
.synodic-empty{margin:0;color:var(--rd-faint);font:italic 11.5px/1.4 Georgia,serif}
.synodic-open{
  border:1px solid var(--rd-line);border-radius:999px;background:var(--rd-card);color:var(--rd-accent);
  padding:6px 10px;cursor:pointer;font:700 10.5px/1.2 Inter,sans-serif
}
.synodic-proof{margin-top:12px;border:1px solid var(--rd-line);border-radius:9px;background:var(--rd-panel)}
.synodic-proof>summary{cursor:pointer;padding:9px 10px;color:var(--rd-muted);font:700 10.5px/1.3 Inter,sans-serif}
.synodic-proof[open]>summary{border-bottom:1px solid var(--rd-line)}
.synodic-table-wrap{overflow-x:auto;padding:9px}
.synodic-table{width:100%;border-collapse:collapse;font:10.5px/1.35 Inter,sans-serif}
.synodic-table th,.synodic-table td{padding:5px 6px;border-bottom:1px solid var(--rd-line);text-align:left;white-space:nowrap}
.synodic-table th{color:var(--rd-faint);font-size:9px;letter-spacing:.08em;text-transform:uppercase}
.synodic-table tr:last-child td{border-bottom:0}
.transition-watch{
  max-width:52rem;margin:14px auto 22px;padding:0 18px;font-family:Inter,ui-sans-serif,sans-serif
}
.transition-watch[hidden]{display:none}
.transition-card{
  overflow:hidden;border:1px solid color-mix(in srgb,var(--rd-transition) 42%,var(--rd-line));
  border-radius:14px;background:linear-gradient(145deg,color-mix(in srgb,var(--rd-card) 95%,var(--rd-transition)),var(--rd-card));
  box-shadow:0 9px 26px color-mix(in srgb,var(--rd-shadow) 45%,transparent)
}
.transition-head{padding:16px 18px 14px;border-bottom:1px solid var(--rd-line)}
.transition-eyebrow{
  margin:0;color:var(--rd-transition);font:800 10px/1.25 Inter,sans-serif;
  letter-spacing:.14em;text-transform:uppercase
}
.transition-boundary{margin:5px 0 0;color:var(--rd-faint);font:italic 11px/1.4 Georgia,serif}
.transition-question{margin:12px 0 0;color:var(--rd-ink);font:700 20px/1.33 Georgia,serif}
.transition-body{padding:15px 18px 17px}
.transition-label{
  display:block;margin:0 0 4px;color:var(--rd-transition);font:800 9.5px/1.2 Inter,sans-serif;
  letter-spacing:.11em;text-transform:uppercase
}
.transition-body p{margin:0;color:var(--rd-muted);font:13px/1.5 Georgia,serif}
.transition-authority{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-bottom:12px}
.transition-block{min-width:0;padding:10px 11px;border:1px solid var(--rd-line);border-radius:9px;background:var(--rd-panel)}
.transition-flow{display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr);gap:10px;align-items:stretch;margin:12px 0}
.transition-state{padding:11px;border:1px solid var(--rd-line);border-radius:10px;background:var(--rd-card)}
.transition-state p{color:var(--rd-ink)}
.transition-arrow{align-self:center;color:var(--rd-transition);font:700 22px/1 Inter,sans-serif}
.transition-chipset{margin:12px 0 0}
.transition-chip-row{display:flex;flex-wrap:wrap;gap:6px}
.transition-chip{
  display:inline-flex;border:1px solid color-mix(in srgb,var(--rd-transition) 28%,var(--rd-line));
  border-radius:999px;padding:4px 8px;background:var(--rd-card);color:var(--rd-muted);
  font:650 10.5px/1.25 Inter,sans-serif
}
.transition-chip.state{border-style:dashed;color:var(--rd-transition)}
.transition-poles{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin-top:14px}
.transition-pole{padding:10px 11px;border:1px solid var(--rd-line);border-radius:9px;background:var(--rd-panel)}
.transition-pole.constructive{border-top:3px solid var(--rd-good)}
.transition-pole.shadow{border-top:3px solid var(--rd-bad)}
.transition-pole.continuity{border-top:3px solid var(--rd-faint)}
.transition-sync{margin-top:13px;padding:11px 12px;border-left:3px solid var(--rd-transition);background:color-mix(in srgb,var(--rd-transition) 7%,transparent)}
.transition-sync .transition-chip-row{margin:7px 0}
.transition-evidence{margin-top:13px;border:1px solid var(--rd-line);border-radius:9px;background:var(--rd-card)}
.transition-evidence>summary{cursor:pointer;padding:10px 12px;color:var(--rd-transition);font:750 11.5px/1.35 Inter,sans-serif}
.transition-evidence[open]>summary{border-bottom:1px solid var(--rd-line)}
.transition-test{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;padding:11px}
.transition-test>div{padding:9px;border:1px solid var(--rd-line);border-radius:8px;background:var(--rd-panel)}
.transition-meta{margin-top:11px!important;color:var(--rd-faint)!important;font:10px/1.4 ui-monospace,Menlo,monospace!important;overflow-wrap:anywhere}
.comparison{
  max-width:58rem;margin:8px auto 16px;padding:0 18px;font-family:Inter,ui-sans-serif,sans-serif
}
.comparison[hidden]{display:none}
.comparison-card{
  border:1px solid color-mix(in srgb,var(--rd-weave) 35%,var(--rd-line));border-radius:14px;
  background:linear-gradient(145deg,color-mix(in srgb,var(--rd-card) 94%,var(--rd-weave)),var(--rd-card));
  box-shadow:0 10px 30px color-mix(in srgb,var(--rd-shadow) 55%,transparent);overflow:hidden
}
.comparison-head{padding:16px 18px 13px;border-bottom:1px solid var(--rd-line)}
.comparison-badges{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:9px}
.status-pill{
  display:inline-flex;align-items:center;border:1px solid var(--rd-line);border-radius:999px;
  padding:4px 8px;background:var(--rd-panel);color:var(--rd-muted);font:700 10px/1.2 Inter,sans-serif;
  letter-spacing:.04em;text-transform:uppercase
}
.status-pill.open{border-color:color-mix(in srgb,var(--rd-open) 55%,var(--rd-line));color:var(--rd-open)}
.status-pill.closed{border-color:color-mix(in srgb,var(--rd-good) 55%,var(--rd-line));color:var(--rd-good)}
.comparison-head h3{margin:0;color:var(--rd-ink);font:700 18px/1.25 Georgia,serif}
.comparison-summary{margin:6px 0 0;color:var(--rd-muted);font:13px/1.48 Georgia,serif}
.causation{
  margin:12px 0 0;padding:8px 10px;border-left:3px solid var(--rd-weave);
  background:color-mix(in srgb,var(--rd-weave) 7%,transparent);color:var(--rd-ink);font:italic 12px/1.45 Georgia,serif
}
.transition-map{margin:13px 0 0;border:1px solid color-mix(in srgb,var(--rd-transition) 36%,var(--rd-line));border-radius:9px;background:var(--rd-card)}
.transition-map[hidden]{display:none}
.transition-map>summary{cursor:pointer;padding:9px 10px;color:var(--rd-transition);font:750 11.5px/1.35 Inter,sans-serif}
.transition-map[open]>summary{border-bottom:1px solid var(--rd-line)}
.transition-map-list{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:7px;padding:10px}
.transition-map-item{min-width:0;padding:9px 10px;border:1px solid var(--rd-line);border-radius:8px;background:var(--rd-panel);color:var(--rd-ink);text-align:left;cursor:pointer}
.transition-map-item:hover{border-color:var(--rd-transition)}
.transition-map-item strong{display:block;font:700 11px/1.3 Inter,sans-serif}
.transition-map-item span{display:block;margin-top:4px;color:var(--rd-muted);font:11px/1.35 Georgia,serif}
.comparison-proof>summary{
  cursor:pointer;padding:12px 18px;color:var(--rd-weave);background:var(--rd-panel);
  font:700 12px/1.35 Inter,ui-sans-serif,sans-serif;letter-spacing:.02em
}
.comparison-proof[open]>summary{border-bottom:1px solid var(--rd-line)}
.baseline-grid{display:grid;grid-template-columns:minmax(190px, .65fr) minmax(0,1.7fr);min-height:330px}
.baseline-list{padding:14px;border-right:1px solid var(--rd-line);background:color-mix(in srgb,var(--rd-panel) 78%,transparent)}
.baseline-list h4,.findings h4{margin:0 0 9px;color:var(--rd-muted);font:700 10px/1.2 Inter,sans-serif;letter-spacing:.12em;text-transform:uppercase}
.baseline-item{
  display:block;width:100%;margin:0 0 6px;padding:8px 9px;border:1px solid var(--rd-line);border-radius:8px;
  background:var(--rd-card);color:var(--rd-ink);text-align:left;cursor:pointer
}
.baseline-item.active{border-color:var(--rd-weave);box-shadow:inset 3px 0 0 var(--rd-weave)}
.baseline-item .btitle{display:block;font:700 11.5px/1.3 Inter,sans-serif}
.baseline-item .bmeta{display:block;margin-top:3px;color:var(--rd-muted);font:10px/1.25 ui-monospace,Menlo,monospace}
.drift{color:var(--rd-good)}.drift.drifted{color:var(--rd-warn)}
.snapshot{min-width:0;padding:14px 16px 16px}
.snapshot-tools{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:8px;margin-bottom:10px}
.segmented{display:inline-flex;border:1px solid var(--rd-line);border-radius:9px;overflow:hidden}
.segmented button{border:0;border-right:1px solid var(--rd-line);padding:6px 9px;background:var(--rd-panel);color:var(--rd-muted);cursor:pointer;font:700 10.5px/1.2 Inter,sans-serif}
.segmented button:last-child{border-right:0}.segmented button.active{background:var(--rd-weave);color:#fff}
.snapshot-meta{color:var(--rd-faint);font:10px/1.35 ui-monospace,Menlo,monospace;overflow-wrap:anywhere}
.snapshot-article{max-height:390px;overflow:auto;padding:2px 8px 0 0;font:14px/1.55 Georgia,serif}
.snapshot-article h1{font-size:1.25rem}.snapshot-article h2{font-size:1.05rem;color:var(--rd-accent)}
.snapshot-article .technical-proof{font-size:13px}
.findings{padding:14px 18px 18px;border-top:1px solid var(--rd-line)}
.finding{padding:11px 12px;margin:0 0 9px;border:1px solid var(--rd-line);border-left:4px solid var(--rd-faint);border-radius:9px;background:var(--rd-panel)}
.finding[data-disposition="Lines up"]{border-left-color:var(--rd-good)}
.finding[data-disposition="Partial"]{border-left-color:var(--rd-warn)}
.finding[data-disposition="Miss"]{border-left-color:var(--rd-bad)}
.finding[data-disposition="Unresolved"]{border-left-color:var(--rd-open)}
.finding-top{display:flex;gap:8px;align-items:flex-start;justify-content:space-between}.finding h5{margin:0;font:700 13px/1.35 Inter,sans-serif}
.finding p{margin:6px 0 0;color:var(--rd-muted);font:12.5px/1.45 Georgia,serif}
.evidence{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:7px;margin-top:10px}
.evidence-lane{min-width:0;padding:8px;border:1px solid var(--rd-line);border-radius:8px;background:var(--rd-card)}
.evidence-lane h6{margin:0 0 6px;color:var(--rd-muted);font:700 9.5px/1.2 Inter,sans-serif;letter-spacing:.1em;text-transform:uppercase}
.evidence-lane .chip{display:block;width:100%;margin:0 0 5px;text-align:left;white-space:normal;font-size:10px}
.evidence-lane .chip.drifted{border-color:var(--rd-warn);color:var(--rd-warn)}
.evidence-empty{margin:0;color:var(--rd-faint);font:italic 10.5px/1.35 Georgia,serif}
.chip.active{border-color:var(--rd-weave);background:color-mix(in srgb,var(--rd-weave) 10%,var(--rd-card));color:var(--rd-weave)}
.comparison-empty{margin:0;padding:10px;border:1px dashed var(--rd-line);border-radius:8px;color:var(--rd-muted);font:italic 12px/1.45 Georgia,serif}
.menu{display:none;border:1px solid var(--rd-line);border-radius:7px;background:var(--rd-card);padding:6px 9px;cursor:pointer}
@media(max-width:820px){
  .shell{grid-template-columns:1fr}
  .top{gap:8px 10px;padding:8px 12px 9px}
  .titles{flex:1 1 calc(100% - 54px);min-width:0}
  .actions{
    flex:1 0 100%;width:100%;flex-wrap:nowrap;overflow-x:auto;overscroll-behavior-x:contain;
    padding:1px 0 2px;-webkit-overflow-scrolling:touch
  }
  .chip{flex:0 0 auto;white-space:nowrap}
  .rail{display:none}
  body.rail-open .rail{
    display:block;position:fixed;inset:0 auto 0 0;width:min(340px,90vw);z-index:20;
    box-shadow:12px 0 34px var(--rd-shadow)
  }
  .menu{display:inline-grid}
  .comparison{padding:0 10px}.baseline-grid{grid-template-columns:1fr}.baseline-list{border-right:0;border-bottom:1px solid var(--rd-line)}
  .baseline-list h4{margin-bottom:6px}.baseline-item{display:inline-block;width:auto;max-width:100%;margin-right:4px;vertical-align:top}
  .evidence{grid-template-columns:1fr}
  .transition-watch{padding:0 10px}.transition-authority,.transition-poles,.transition-test,.transition-map-list{grid-template-columns:1fr}
  .synodic-stack{padding:0 10px}.synodic-grid{grid-template-columns:1fr}
  .transition-flow{grid-template-columns:1fr}.transition-arrow{justify-self:center;transform:rotate(90deg)}
}
</style>
</head>
<body>
<div class="shell">
  <aside class="rail" id="rail" aria-label="Readings">
    <div class="brand">
      <h1>Chart Readings</h1>
      <span>Aster-authored readings, record censuses, and storyline comparisons. Live working shelf — edit as we go.</span>
    </div>
    <div class="search">
      <label for="q">Filter readings</label>
      <input id="q" type="search" placeholder="Find a chart or season…" autocomplete="off">
    </div>
    <nav id="nav"></nav>
  </aside>
  <main class="main">
    <header class="top">
      <button class="menu" id="menu" type="button" data-action="toggle-menu" aria-label="Open readings" aria-controls="rail" aria-expanded="false">☰</button>
      <div class="titles">
        <div class="kicker" id="kicker">Sky &amp; Charts / Chart Library</div>
        <h2 id="title">Chart Readings</h2>
        <p class="note" id="note">Pick a climate, a lunation, a record census, or a storyline comparison.</p>
      </div>
      <div class="actions" id="actions"></div>
    </header>
    <div class="stage" id="stage">
      <div class="wheel-wrap" id="wheelwrap" hidden>
        <div class="wheel-card">
          <p class="wlabel" id="wheellabel"></p>
          <div id="wheelbox"></div>
        </div>
      </div>
      <p class="authority" id="authority"></p>
      <article class="article" id="article"></article>
      <section class="synodic-stack" id="synodicStack" aria-label="Synodic Stack" hidden></section>
      <section class="transition-watch" id="transitionWatch" aria-label="State Transition Watch" hidden></section>
      <section class="comparison" id="comparison" aria-label="Comparison workspace" hidden>
        <div class="comparison-card">
          <div class="comparison-head">
            <div class="comparison-badges" id="comparisonBadges"></div>
            <h3 id="comparisonTitle"></h3>
            <p class="comparison-summary" id="comparisonSummary"></p>
            <p class="causation" id="causation"></p>
            <details class="transition-map" id="transitionMap" hidden>
              <summary id="transitionMapSummary">State Transition Watch map</summary>
              <div class="transition-map-list" id="transitionMapList"></div>
            </details>
          </div>
          <details class="comparison-proof">
            <summary>Evidence joins &amp; frozen baseline</summary>
            <div class="baseline-grid">
              <div class="baseline-list">
                <h4>Frozen season baseline</h4>
                <div id="baselineList"></div>
              </div>
              <div class="snapshot">
                <div class="snapshot-tools">
                  <div class="segmented" aria-label="Reading version">
                    <button type="button" data-action="snapshot-mode" data-mode="baseline">Frozen baseline</button>
                    <button type="button" data-action="snapshot-mode" data-mode="current">Current live reading</button>
                  </div>
                  <span class="snapshot-meta" id="snapshotMeta"></span>
                </div>
                <div class="snapshot-article" id="snapshotArticle"></div>
              </div>
            </div>
            <div class="findings">
              <h4>Evidence-backed findings</h4>
              <div id="findings"></div>
            </div>
          </details>
        </div>
      </section>
      <div class="pager">
        <button type="button" id="prev" data-action="step" data-delta="-1">← Previous</button>
        <button type="button" id="next" data-action="step" data-delta="1">Next →</button>
      </div>
    </div>
  </main>
</div>
<script id="f250-chart-readings" type="application/json">__DATA__</script>
<script>
__WHEEL__
</script>
<script>
(function(){
  "use strict";
  var DATA=JSON.parse(document.getElementById("f250-chart-readings").textContent);
  var readings=DATA.readings;
  var seasons=DATA.seasons;
  var byId=Object.create(null);
  readings.forEach(function(row){ byId[row.id]=row; });
  var active=null;
  var LAST="f250-readings-last";
  var comparisonView={componentId:null,mode:"baseline"};
  var readingMode="current";
  var routeIndex=Object.create(null);
  var routeSequence=0;

  function postParent(msg){
    if(window.parent===window) return;
    try{window.parent.postMessage(msg,"*");}catch(_){}
  }
  function openRoute(tab, payload){
    payload=payload||{};
    if(window.parent && typeof window.parent.navigateTo==="function"){
      window.parent.navigateTo(tab, payload);
      return;
    }
    postParent(Object.assign({action:"navigateTo", tab:tab}, payload));
  }
  function routeKey(route){
    routeSequence+=1;
    var key="route-"+routeSequence;
    routeIndex[key]=route;
    return key;
  }
  function followExact(route){
    if(!route || !route.view || !route.action) return;
    var params=route.params||{};
    if(route.view==="obs-cr" && params.targetId){ openReading(params.targetId); return; }
    if(route.view==="obsidian" && params.notePath){
      window.location.href="[vault-route]"+encodeURIComponent("Freedom 250 Chronicle")+"&file="+encodeURIComponent(params.notePath);
      return;
    }
    openRoute(route.view, Object.assign({action:route.action}, params));
  }
  function node(tag, className, textValue){
    var item=document.createElement(tag);
    if(className) item.className=className;
    if(textValue!==undefined && textValue!==null) item.textContent=String(textValue);
    return item;
  }
  function setRail(open){
    var button=document.getElementById("menu");
    document.body.classList.toggle("rail-open", !!open);
    button.setAttribute("aria-expanded", open?"true":"false");
    button.setAttribute("aria-label", open?"Close readings":"Open readings");
  }
  function follow(link){
    if(!link) return;
    var kind=link.kind;
    if(kind==="wheel") openRoute("obs-ic", {action:"selectIngress", id:link.ingress});
    else if(kind==="overlay") openRoute("obs-ic", {action:"showOverlay", ingress:link.ingress, lunationDate:link.date, date:link.date});
    else if(kind==="lunar") openRoute("obs-lw", {date:link.date});
    else if(kind==="almanac") openRoute("obs-al", {date:link.date});
    else if(kind==="day") openRoute("obs-df", {date:link.date});
    else if(kind==="eo"){
      postParent({action:"goToEO", date:link.date});
      openRoute("obs-eo", {eo:link.query||"", date:link.date, query:link.query||""});
    }
    else if(kind==="hearings") openRoute("obs-hr", {date:link.date});
    else if(kind==="research") openRoute("obs-rd", {researchQuery:link.query||""});
    else if(kind==="machines") openRoute("obs-om", {});
    else if(kind==="feed") openRoute("obs-df", {date:link.date});
    else if(kind==="reading" && link.id) openReading(link.id);
  }
  function railTitle(row){
    if(row.kind==="comparison") return row.comparison && row.comparison.state==="open" ? "Open comparison watch" : "Storyline comparison";
    if(row.kind==="weave") return "Storyline comparison";
    if(row.kind==="census") return "Record census";
    if(row.chart_kind==="ingress") return "Climate · "+(row.sign||"ingress")+" ingress";
    var eclipse=row.eclipse ? " · eclipse" : "";
    var phase=/(-fu|full)/i.test(row.id) ? "Full Moon" : "New Moon";
    return (row.date||"")+" · "+phase+(row.sign?" · "+row.sign:"")+eclipse;
  }
  function seasonOf(id){
    for(var i=0;i<seasons.length;i+=1) if(seasons[i].id===id) return seasons[i];
    return null;
  }
  function visibleReadings(){
    var needle=String(document.getElementById("q").value||"").trim().toLowerCase();
    return readings.filter(function(row){
      if(!needle) return true;
      var watch=row.transition_watch||{};
      var mapped=((row.comparison||{}).transition_watches||[]).map(function(item){
        return [item.authority_question,item.decision_right,item.current_holder,item.claimant_or_constraint].join(" ");
      }).join(" ");
      return (row.title+" "+row.badge+" "+row.season+" "+(row.date||"")+" "+(row.summary||"")+" "+
        (watch.authority_question||"")+" "+(watch.decision_right||"")+" "+(watch.current_holder||"")+" "+
        (watch.claimant_or_constraint||"")+" "+mapped).toLowerCase().indexOf(needle)>=0;
    });
  }
  function buildNav(){
    var nav=document.getElementById("nav");
    nav.innerHTML="";
    var visible=new Set(visibleReadings().map(function(row){return row.id;}));
    seasons.forEach(function(season){
      var rows=readings.filter(function(row){return row.season===season.id && visible.has(row.id);});
      if(!rows.length) return;
      var section=document.createElement("section");
      section.className="season";
      section.innerHTML="<h2>"+season.label+"</h2><p class=\"win\">"+season.window+" · "+season.blurb+"</p>";
      rows.forEach(function(row){
        var button=document.createElement("button");
        button.type="button";
        button.className="item"+(row.id===active?" active":"");
        button.dataset.id=row.id;
        button.dataset.action="open-reading";
        button.innerHTML="<span class=\"name\">"+railTitle(row)+"</span><span class=\"meta\">"+row.badge+(row.date?" · "+row.date:"")+"</span>";
        section.appendChild(button);
      });
      nav.appendChild(section);
    });
    if(!nav.children.length){
      nav.innerHTML="<p class=\"empty\">No reading matches that search.</p>";
    }
  }
  function paintWheel(row){
    var wrap=document.getElementById("wheelwrap");
    var box=document.getElementById("wheelbox");
    var label=document.getElementById("wheellabel");
    if(!row.wheel || typeof wheelSVG!=="function"){
      wrap.hidden=true;
      box.innerHTML="";
      return;
    }
    wrap.hidden=false;
    label.textContent=row.wheel_note||"Washington, D.C. · Whole Sign";
    box.innerHTML=wheelSVG(row.wheel,null,false);
  }
  function prettySynodicId(value){
    return String(value||"").split(/[-_]/).filter(Boolean).map(function(part){
      return part.charAt(0).toUpperCase()+part.slice(1);
    }).join(" ");
  }
  function cycleLabel(cycle){
    var pair=cycle.pair;
    if(Array.isArray(pair)) return pair.map(prettySynodicId).join("–");
    if(pair && typeof pair==="object"){
      if(pair.label) return String(pair.label);
      var bodies=[pair.slower||pair.first||pair.a,pair.faster||pair.second||pair.b].filter(Boolean);
      if(bodies.length===2) return bodies.map(prettySynodicId).join("–");
    }
    if(typeof pair==="string" && pair) return pair;
    return prettySynodicId(cycle.cycle_id);
  }
  function degree(value){
    var number=Number(value);
    return Number.isFinite(number)?number.toFixed(2)+"°":"—";
  }
  function motionLabel(aspect){
    if(aspect.applying) return "applying";
    if(aspect.separating) return "separating";
    return "exact";
  }
  function aspectLine(cycle){
    var aspect=cycle.active_aspect||cycle;
    if(!aspect) return "Between standard major-aspect chapters";
    return prettySynodicId(aspect.strength)+" "+prettySynodicId(aspect.aspect_id)+
      " · orb "+degree(aspect.orb_deg)+" · "+motionLabel(aspect);
  }
  function phaseLine(cycle){
    var geometry=cycle.geometry||{};
    var state=cycle.active_aspect
      ?prettySynodicId(cycle.active_aspect.strength)+" "+prettySynodicId(cycle.active_aspect.aspect_id)+" chapter"
      :"between chapters";
    return prettySynodicId(geometry.phase_direction)+" · "+state+" · nearest "+
      prettySynodicId(geometry.nearest_chapter_id)+" chapter · "+
      degree(geometry.nearest_chapter_orb_deg)+" from exact";
  }
  function reasonLabels(reasons){
    var labels={root:"root",chart_ruler:"chart ruler",era:"era",exact_us_natal:"exact US natal"};
    return (reasons||[]).map(function(reason){return labels[reason]||prettySynodicId(reason);});
  }
  function synodicCycleButton(cycle,line){
    var button=node("button","synodic-item");
    button.type="button";
    button.dataset.action="open-synodic-clock";
    button.dataset.cycleId=cycle.cycle_id;
    button.appendChild(node("strong","",cycleLabel(cycle)));
    button.appendChild(node("span","",line));
    return button;
  }
  function synodicLane(title,noteText){
    var lane=node("section","synodic-lane");
    lane.appendChild(node("h4","",title));
    if(noteText) lane.appendChild(node("p","synodic-lane-note",noteText));
    return lane;
  }
  function renderSynodicStack(row){
    var host=document.getElementById("synodicStack");
    var stack=row.synodic_stack;
    host.innerHTML="";
    host.hidden=!stack;
    if(!stack) return;

    var details=node("details","synodic-card");
    var summary=node("summary","");
    summary.appendChild(node("strong","","Synodic Stack"));
    summary.appendChild(node(
      "span",
      "synodic-summary-meta",
      stack.active_geometry.length+" direct · "+stack.nameable_cycles.length+
        " nameable · "+stack.seed_echoes.length+" seed echoes"
    ));
    details.appendChild(summary);
    var body=node("div","synodic-body");
    body.appendChild(node(
      "p",
      "synodic-notice",
      "Three independent lanes: current aspect geometry, DR-020 phase nameability, and seed echoes. Timing context only; no score, storyline finding, political join, or causal claim is created here."
    ));

    var geometryLane=synodicLane(
      "Active moment geometry",
      "Direct aspects inside Katie's standard major-aspect orbs. These facts do not by themselves earn phase narration."
    );
    if(stack.active_geometry.length){
      var geometryGrid=node("div","synodic-grid");
      stack.active_geometry.forEach(function(cycle){
        geometryGrid.appendChild(synodicCycleButton(cycle,aspectLine(cycle)));
      });
      geometryLane.appendChild(geometryGrid);
    }else{
      geometryLane.appendChild(node("p","synodic-empty","No clock is inside a standard major-aspect orb at this chart moment."));
    }
    body.appendChild(geometryLane);

    var namedLane=synodicLane(
      "Nameable cycle chapters · DR-020",
      "Only root/chart-ruler, era, or exact-US-natal grounds may bring a universal phase into the reading."
    );
    if(stack.nameable_cycles.length){
      var namedGrid=node("div","synodic-grid");
      stack.nameable_cycles.forEach(function(cycle){
        var button=synodicCycleButton(cycle,phaseLine(cycle));
        var reasons=node("span","synodic-reasons");
        reasonLabels((cycle.nameability||{}).reasons).forEach(function(reason){
          reasons.appendChild(node("em","",reason));
        });
        button.appendChild(reasons);
        namedGrid.appendChild(button);
      });
      namedLane.appendChild(namedGrid);
    }else{
      namedLane.appendChild(node("p","synodic-empty","No phase narrative is earned under DR-020 at this chart."));
    }
    body.appendChild(namedLane);

    var echoLane=synodicLane(
      "Active seed echoes",
      "Chart points contacting registered conjunction-family degrees. This is separate from the planets' current aspect geometry."
    );
    if(stack.seed_echoes.length){
      var echoGrid=node("div","synodic-grid");
      stack.seed_echoes.forEach(function(echo){
        var cycle=(stack.technical_cycles||[]).find(function(item){return item.cycle_id===echo.cycle_id;})||{cycle_id:echo.cycle_id};
        var button=synodicCycleButton(
          cycle,
          prettySynodicId(echo.point)+" "+prettySynodicId(echo.aspect_id)+" "+
            prettySynodicId(echo.seed_family_id)+" · orb "+degree(echo.orb_deg)
        );
        button.appendChild(node("span","",String(echo.matched_pass_id)));
        echoGrid.appendChild(button);
      });
      echoLane.appendChild(echoGrid);
    }else{
      echoLane.appendChild(node("p","synodic-empty","No registered seed-family degree is active at this chart moment."));
    }
    body.appendChild(echoLane);

    var openButton=node("button","synodic-open","Open this moment in The Long Clocks");
    openButton.type="button";
    openButton.dataset.action="open-synodic-stack";
    body.appendChild(openButton);

    var proof=node("details","synodic-proof");
    proof.appendChild(node("summary","","Technical Proof · all ten factual clock hands"));
    var tableWrap=node("div","synodic-table-wrap");
    var table=node("table","synodic-table");
    var thead=node("thead","");
    var header=node("tr","");
    ["Cycle","Tier","Elongation","Direction","Nearest chapter","Active aspect"].forEach(function(label){
      header.appendChild(node("th","",label));
    });
    thead.appendChild(header);table.appendChild(thead);
    var tbody=node("tbody","");
    stack.technical_cycles.forEach(function(cycle){
      var geometry=cycle.geometry||{};
      var tr=node("tr","");
      var cycleCell=node("td","");
      var clockButton=node("button","synodic-open",cycleLabel(cycle));
      clockButton.type="button";
      clockButton.dataset.action="open-synodic-clock";
      clockButton.dataset.cycleId=cycle.cycle_id;
      cycleCell.appendChild(clockButton);
      tr.appendChild(cycleCell);
      tr.appendChild(node("td","",prettySynodicId(cycle.tier_id)));
      tr.appendChild(node("td","",degree(geometry.elongation_deg)));
      tr.appendChild(node("td","",prettySynodicId(geometry.phase_direction)));
      tr.appendChild(node("td","",prettySynodicId(geometry.nearest_chapter_id)+" · "+degree(geometry.nearest_chapter_orb_deg)));
      tr.appendChild(node("td","",cycle.active_aspect?aspectLine(cycle):"between chapters"));
      tbody.appendChild(tr);
    });
    table.appendChild(tbody);tableWrap.appendChild(table);proof.appendChild(tableWrap);body.appendChild(proof);
    details.appendChild(body);host.appendChild(details);
  }
  function openSynodicRoute(action,cycleId){
    var row=byId[active];
    var stack=row&&row.synodic_stack;
    if(!stack) return;
    var payload={
      childAction:action,
      chart_id:stack.chart_id,
      window_id:stack.window_id,
      date:stack.date
    };
    if(cycleId) payload.cycle_id=cycleId;
    openRoute("obs-dc",payload);
  }
  function chip(link){
    var button=document.createElement("button");
    button.type="button";
    button.className="chip"+(link.kind==="eo"||link.kind==="research"||link.kind==="machines"?" weave":"");
    button.textContent=link.label;
    button.dataset.action="follow-link";
    button.dataset.routeKey=routeKey(link);
    return button;
  }
  function labeledBlock(label,value,className){
    var block=node("div",className||"transition-block");
    block.appendChild(node("span","transition-label",label));
    block.appendChild(node("p","",value));
    return block;
  }
  function transitionChips(values,className){
    var row=node("div","transition-chip-row");
    (values||[]).forEach(function(value){
      row.appendChild(node("span","transition-chip"+(className?" "+className:""),value));
    });
    return row;
  }
  function renderTransitionWatch(row){
    var panel=document.getElementById("transitionWatch");
    var watch=row.transition_watch;
    panel.innerHTML="";
    panel.hidden=!watch;
    if(!watch) return;

    var card=node("div","transition-card");
    var head=node("div","transition-head");
    head.appendChild(node("p","transition-eyebrow","State Transition Watch · frozen addendum"));
    head.appendChild(node(
      "p",
      "transition-boundary",
      "Separate from the chart hearing. Lens, not conclusion; no score; a rhyme is not a cause. " +
        "It does not alter the frozen baseline · "+
        String(watch.boundary||"").replace(/_/g," ")
    ));
    head.appendChild(node("p","transition-question",watch.authority_question));
    card.appendChild(head);

    var body=node("div","transition-body");
    var authority=node("div","transition-authority");
    authority.appendChild(labeledBlock("Decision right in motion",watch.decision_right));
    authority.appendChild(labeledBlock("Current holder",watch.current_holder));
    authority.appendChild(labeledBlock("Claimant or constraint",watch.claimant_or_constraint));
    authority.appendChild(labeledBlock("Freedom 250 question",watch.thesis_question));
    body.appendChild(authority);

    var flow=node("div","transition-flow");
    flow.appendChild(labeledBlock("From",watch.transition.from,"transition-state"));
    flow.appendChild(node("div","transition-arrow","→"));
    flow.appendChild(labeledBlock("Toward",watch.transition.toward,"transition-state"));
    body.appendChild(flow);

    var mechanisms=node("div","transition-chipset");
    mechanisms.appendChild(node("span","transition-label","Candidate mechanisms"));
    mechanisms.appendChild(transitionChips(watch.mechanisms));
    body.appendChild(mechanisms);
    var states=node("div","transition-chipset");
    states.appendChild(node("span","transition-label","States to distinguish — no leapfrogging"));
    states.appendChild(transitionChips(watch.states_to_distinguish,"state"));
    body.appendChild(states);

    var poles=node("div","transition-poles");
    [
      ["Constructive pole","constructive"],
      ["Shadow pole","shadow"],
      ["Continuity / unchanged","continuity"]
    ].forEach(function(spec){
      poles.appendChild(labeledBlock(spec[0],watch.poles[spec[1]],"transition-pole "+spec[1]));
    });
    body.appendChild(poles);

    var sync=node("section","transition-sync");
    sync.appendChild(node("span","transition-label","Synchronization test"));
    sync.appendChild(transitionChips(watch.synchronization.arcs));
    sync.appendChild(node("p","",watch.synchronization.watch_for));
    body.appendChild(sync);

    var evidence=node("details","transition-evidence");
    evidence.appendChild(node("summary","","Evidence test · Attention / Official / Entity"));
    var tests=node("div","transition-test");
    tests.appendChild(labeledBlock("Lines up if",watch.evidence_test.lines_up_if));
    tests.appendChild(labeledBlock("Miss if",watch.evidence_test.miss_if));
    tests.appendChild(labeledBlock("Unresolved if",watch.evidence_test.unresolved_if));
    evidence.appendChild(tests);
    body.appendChild(evidence);
    body.appendChild(node(
      "p",
      "transition-meta",
      watch.watch_id+" · frozen "+watch.frozen_at+" · watch "+watch.watch_sha256.slice(0,12)+
        "… · baseline "+watch.baseline_sha256.slice(0,12)+"…"
    ));
    card.appendChild(body);
    panel.appendChild(card);
  }
  function renderSnapshot(comparison){
    var components=comparison.baseline.components||[];
    var component=components.find(function(item){return item.reading_id===comparisonView.componentId;})||components[0];
    if(!component) return;
    comparisonView.componentId=component.reading_id;
    document.querySelectorAll(".baseline-item").forEach(function(button){
      button.classList.toggle("active",button.dataset.readingId===component.reading_id);
    });
    document.querySelectorAll("[data-action='snapshot-mode']").forEach(function(button){
      button.classList.toggle("active",button.dataset.mode===comparisonView.mode);
      button.setAttribute("aria-pressed",button.dataset.mode===comparisonView.mode?"true":"false");
    });
    var baseline=comparisonView.mode==="baseline";
    document.getElementById("snapshotArticle").innerHTML=baseline?component.baseline_html:component.current_html;
    var digest=baseline?component.baseline_sha256:component.current_sha256;
    document.getElementById("snapshotMeta").textContent=
      (baseline?"frozen ":"live ")+digest.slice(0,12)+"… · "+component.drift;
  }
  function renderComparison(row){
    var panel=document.getElementById("comparison");
    var comparison=row.comparison;
    panel.hidden=!comparison;
    if(!comparison) return;
    var baseline=comparison.baseline;
    var badges=document.getElementById("comparisonBadges");
    badges.innerHTML="";
    var state=node("span","status-pill "+comparison.state,comparison.state);
    badges.appendChild(state);
    badges.appendChild(node("span","status-pill",comparison.mode==="retrospective_calibration"?"retrospective calibration":"prospective watch"));
    if(comparison.boundary && comparison.boundary.kind){
      badges.appendChild(node("span","status-pill",String(comparison.boundary.kind).replace(/_/g," ")));
    }
    badges.appendChild(node("span","status-pill",baseline.drift_count?baseline.drift_count+" live drift":"baseline unchanged"));
    var transitionWatches=comparison.transition_watches||[];
    if(transitionWatches.length){
      badges.appendChild(node("span","status-pill",transitionWatches.length+" transition watches"));
    }
    document.getElementById("comparisonTitle").textContent=comparison.title||row.title;
    document.getElementById("comparisonSummary").textContent=comparison.summary||"";
    document.getElementById("causation").textContent=comparison.policy.causation_notice;

    var transitionMap=document.getElementById("transitionMap");
    var transitionMapList=document.getElementById("transitionMapList");
    transitionMap.hidden=!transitionWatches.length;
    transitionMap.removeAttribute("open");
    transitionMapList.innerHTML="";
    document.getElementById("transitionMapSummary").textContent=
      "State Transition Watch map · "+transitionWatches.length+" frozen addenda";
    transitionWatches.forEach(function(watch){
      var linked=byId[watch.reading_id]||{};
      var button=node("button","transition-map-item");
      button.type="button";
      button.dataset.action="open-reading";
      button.dataset.id=watch.reading_id;
      button.appendChild(node("strong","",linked.title||watch.reading_id));
      button.appendChild(node("span","",watch.authority_question));
      button.appendChild(node("span","","From "+watch.transition.from+" → "+watch.transition.toward));
      transitionMapList.appendChild(button);
    });

    var list=document.getElementById("baselineList");
    list.innerHTML="";
    (baseline.components||[]).forEach(function(component){
      var button=node("button","baseline-item");
      button.type="button";
      button.dataset.action="select-baseline-component";
      button.dataset.readingId=component.reading_id;
      button.appendChild(node("span","btitle",component.title));
      var meta=node("span","bmeta "+(component.drift==="drifted"?"drift drifted":"drift"),component.drift+" · "+component.baseline_sha256.slice(0,8));
      button.appendChild(meta);
      list.appendChild(button);
    });

    var findings=document.getElementById("findings");
    findings.innerHTML="";
    if(!(comparison.findings||[]).length){
      findings.appendChild(node(
        "p",
        "comparison-empty",
        comparison.state==="open"
          ?(transitionWatches.length
            ?"No findings recorded yet. The frozen baseline and State Transition Watches are ready for evidence as the watch unfolds."
            :"No findings recorded yet. The frozen baseline is ready for evidence as the watch unfolds.")
          :"No findings were recorded before this comparison closed."
      ));
    }else{
      comparison.findings.forEach(function(finding){
        var card=node("section","finding");
        card.dataset.disposition=finding.disposition;
        var top=node("div","finding-top");
        top.appendChild(node("h5","",finding.claim));
        top.appendChild(node("span","status-pill",finding.disposition));
        card.appendChild(top);
        card.appendChild(node("p","",finding.rationale||""));
        var refs=(finding.baseline_refs||[]).map(function(ref){return ref.reading_id+(ref.heading?" · "+ref.heading:"");});
        if(refs.length) card.appendChild(node("p","snapshot-meta","Baseline: "+refs.join("; ")));
        var evidence=node("div","evidence");
        ["Attention","Official","Entity"].forEach(function(lane){
          var laneBox=node("section","evidence-lane");
          laneBox.appendChild(node("h6","",lane));
          var laneItems=(finding.evidence||[]).filter(function(item){return item.lane===lane;});
          if(!laneItems.length){
            laneBox.appendChild(node("p","evidence-empty","No joined evidence in this lane."));
          }else{
            laneItems.forEach(function(item){
              var label=(item.date?item.date+" · ":"")+item.label;
              var button=node("button","chip"+(item.source_drift==="drifted"?" drifted":""),label);
              button.type="button";
              button.dataset.action="open-evidence";
              button.dataset.routeKey=routeKey(item.route);
              button.title=item.source_path+(item.note?" — "+item.note:"");
              laneBox.appendChild(button);
            });
          }
          evidence.appendChild(laneBox);
        });
        card.appendChild(evidence);
        findings.appendChild(card);
      });
    }
    renderSnapshot(comparison);
  }
  function paintMainArticle(row){
    var context=row.baseline_context;
    var frozen=readingMode==="baseline" && context;
    var html=frozen?context.baseline_html:(row.html||"");
    html=html.replace(/^<h1>[\s\S]*?<\/h1>/,"");
    document.getElementById("article").innerHTML=html;
    document.querySelectorAll("[data-action='reading-mode']").forEach(function(button){
      button.classList.toggle("active",button.dataset.mode===readingMode);
      button.setAttribute("aria-pressed",button.dataset.mode===readingMode?"true":"false");
    });
    if(frozen){
      document.getElementById("authority").textContent=
        "Frozen baseline: "+context.baseline_id+" · captured "+context.captured_at+" · "+context.baseline_sha256.slice(0,12)+"…";
    }else{
      var suffix=context?" · baseline "+context.drift:"";
      document.getElementById("authority").textContent=
        (row.authority_label||"Vault source")+": "+row.source_name+" · "+(row.author||"Aster")+" · "+(row.status||"live_working").replace(/_/g," ")+suffix+" · edit as we go";
    }
  }
  function readingModeChip(mode,label){
    var button=node("button","chip",label);
    button.type="button";
    button.dataset.action="reading-mode";
    button.dataset.mode=mode;
    return button;
  }
  function openReading(id){
    var row=byId[id];
    if(!row) return;
    if(active!==id){
      comparisonView={componentId:null,mode:"baseline"};
      readingMode="current";
    }
    active=id;
    var season=seasonOf(row.season)||{};
    document.getElementById("kicker").textContent=(season.label||"Readings")+" · "+row.badge;
    document.getElementById("title").textContent=row.title;
    document.getElementById("note").textContent=row.face||"";
    paintWheel(row);
    renderComparison(row);
    var actions=document.getElementById("actions");
    actions.innerHTML="";
    if(row.baseline_context){
      actions.appendChild(readingModeChip("current","Live working"));
      actions.appendChild(readingModeChip("baseline","Frozen "+String(row.baseline_context.captured_at).slice(0,10)));
    }
    (row.links||[]).forEach(function(link){ actions.appendChild(chip(link)); });
    paintMainArticle(row);
    renderSynodicStack(row);
    renderTransitionWatch(row);
    var vis=visibleReadings();
    var index=vis.findIndex(function(item){return item.id===id;});
    document.getElementById("prev").disabled=index<=0;
    document.getElementById("next").disabled=index<0 || index>=vis.length-1;
    document.querySelectorAll(".item").forEach(function(button){
      button.classList.toggle("active", button.dataset.id===id);
    });
    document.getElementById("stage").scrollTop=0;
    try{ localStorage.setItem(LAST, id); }catch(_){}
    if(location.hash!=="#"+id){
      try{ history.replaceState(null, "", "#"+id); }catch(_){}
    }
    document.title=row.title+" — Chart Readings";
    if(window.matchMedia("(max-width:820px)").matches){
      setRail(false);
    }
  }
  function step(delta){
    var vis=visibleReadings();
    var index=vis.findIndex(function(item){return item.id===active;});
    var next=vis[index+delta];
    if(next) openReading(next.id);
  }
  document.addEventListener("input", function(event){
    if(event.target.id!=="q") return;
    buildNav();
    if(active && !visibleReadings().some(function(row){return row.id===active;})){
      var first=visibleReadings()[0];
      var choosingOnMobile=window.matchMedia("(max-width:820px)").matches &&
        document.body.classList.contains("rail-open");
      if(first && !choosingOnMobile) openReading(first.id);
    }
  });
  document.addEventListener("click", function(event){
    var button=event.target.closest("button[data-action]");
    if(!button) return;
    var action=button.dataset.action;
    if(action==="open-reading") openReading(button.dataset.id);
    else if(action==="follow-link") follow(routeIndex[button.dataset.routeKey]);
    else if(action==="open-evidence") followExact(routeIndex[button.dataset.routeKey]);
    else if(action==="step") step(Number(button.dataset.delta||0));
    else if(action==="toggle-menu") setRail(!document.body.classList.contains("rail-open"));
    else if(action==="open-synodic-stack") openSynodicRoute("openStack",null);
    else if(action==="open-synodic-clock") openSynodicRoute("openClock",button.dataset.cycleId);
    else if(action==="select-baseline-component"){
      comparisonView.componentId=button.dataset.readingId;
      var selected=byId[active];
      if(selected && selected.comparison) renderSnapshot(selected.comparison);
    }
    else if(action==="snapshot-mode"){
      comparisonView.mode=button.dataset.mode==="current"?"current":"baseline";
      var current=byId[active];
      if(current && current.comparison) renderSnapshot(current.comparison);
    }
    else if(action==="reading-mode"){
      readingMode=button.dataset.mode==="baseline"?"baseline":"current";
      var reading=byId[active];
      if(reading) paintMainArticle(reading);
    }
  });
  document.addEventListener("keydown", function(event){
    if(/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)) return;
    if(event.key==="/" ){ event.preventDefault(); document.getElementById("q").focus(); }
    if(event.key==="j"){ event.preventDefault(); step(1); }
    if(event.key==="k"){ event.preventDefault(); step(-1); }
    if(event.key==="Escape" && document.body.classList.contains("rail-open")){ setRail(false); }
  });
  window.addEventListener("message", function(event){
    var msg=event.data||{};
    if(msg.action==="setTheme"){
      document.documentElement.setAttribute("data-theme", msg.theme==="dark"?"dark":"light");
      return;
    }
    if(msg.action==="openReading" && msg.id){ openReading(msg.id); return; }
    if(msg.action==="selectReading" && msg.chart_id){ openReading(msg.chart_id); return; }
    if((msg.action==="goToDate" || msg.action==="scrollToDate") && msg.date){
      var hit=readings.find(function(row){ return row.date===msg.date; });
      if(hit) openReading(hit.id);
    }
  });
  buildNav();
  var start=null;
  if(location.hash) start=location.hash.replace(/^#/, "");
  if(!start){ try{ start=localStorage.getItem(LAST); }catch(_){ } }
  if(!byId[start]) start=readings[0] && readings[0].id;
  if(start) openReading(start);
})();
</script>
</body>
</html>
"""


def render(
    readings: list[dict[str, Any]],
    bones_index: dict[str, Any],
    generated_at: str | None = None,
) -> str:
    try:
        authority_source = str(REGISTRY.relative_to(VAULT))
    except ValueError:
        authority_source = str(REGISTRY)
    payload = {
        "generated_at": generated_at
        or dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "authority": {
            "source": authority_source,
            "additional_sources": (
                [str(REGISTRY_2025.relative_to(VAULT))] if REGISTRY_2025.is_file() else []
            ) + (
                [str(AMENDMENT_LEDGER.relative_to(VAULT))] if AMENDMENT_LEDGER.is_file() else []
            ),
            "author": "Aster",
            "lifecycle": "vault-owned live working readings; edit as we go",
            "not_canon": False,
        },
        "bones_generated": bones_index.get("generated"),
        "seasons": (list(SEASONS_2025) if REGISTRY_2025.is_file() else []) + list(SEASONS),
        "readings": readings,
        "count": len(readings),
    }
    html_out = HTML_TEMPLATE.replace("__DATA__", js_safe_json(payload)).replace(
        "__WHEEL__", WHEEL_JS
    )
    if "__DATA__" in html_out or "__WHEEL__" in html_out:
        fail("unresolved template marker in Chart Readings.html")
    return html_out


def generated_at_from(content: str) -> str | None:
    match = re.search(r'"generated_at"\s*:\s*"([^"]+)"', content)
    return match.group(1) if match else None


def normalize_generated(content: str) -> str:
    """Ignore the governed post-build theme block in freshness comparisons."""
    return DARKMODE_BLOCK.sub("\n", content).rstrip() + "\n"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", type=Path, default=DEFAULT_VAULT)
    parser.add_argument("--registry", type=Path)
    parser.add_argument("--bones", type=Path)
    parser.add_argument("--synodic-stacks", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--capture-baseline",
        metavar="BASELINE_ID",
        help="capture and pin one baseline, or `all`; refuses every overwrite",
    )
    parser.add_argument("--check", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    configure_paths(args)
    if args.capture_baseline:
        if args.check:
            fail("--capture-baseline and --check are mutually exclusive")
        registry = load_json(REGISTRY)
        if args.capture_baseline == "all":
            baseline_ids = [
                str(row.get("baseline_id") or "")
                for row in (registry.get("comparison_contract") or {}).get("baselines") or []
            ]
            if not baseline_ids:
                fail("registry contains no baselines to capture")
            for baseline_id in baseline_ids:
                capture_baseline(registry, baseline_id)
        else:
            capture_baseline(registry, args.capture_baseline)
        return 0
    readings, bones_index, _registry = collect_all_shelves()
    output = OUTPUT
    if args.check:
        if not output.is_file():
            print(f"Chart Readings check FAILED: missing {output}", file=sys.stderr)
            return 1
        existing = output.read_text(encoding="utf-8")
        stamp = generated_at_from(existing)
        if not stamp:
            print(
                f"Chart Readings check FAILED: generated timestamp missing in {output}",
                file=sys.stderr,
            )
            return 1
        content = render(readings, bones_index, generated_at=stamp)
        if normalize_generated(existing) != normalize_generated(content):
            print(f"Chart Readings check FAILED: stale {output}", file=sys.stderr)
            return 1
        print(f"Chart Readings check OK: {len(readings)} readings · {output}")
        return 0
    content = render(readings, bones_index)
    atomic_write_text(output, content)
    print(f"Built {output} · {len(readings)} readings · registry {REGISTRY}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
