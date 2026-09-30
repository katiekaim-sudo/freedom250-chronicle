#!/usr/bin/env python3
"""Build The Astrology Spine — a moving, score-free Sky & Charts map.

The view is a projection only.  It reuses canonical chart/readings routes and
does not cast, redraw, or reinterpret a wheel. Authored many-to-many Chronicle
links live in ``03 - Astrology/astrology_spine_overlaps.json``; orbital facts
come from Long Clocks, archetypal copy from the cycle-reading registry, and
exact awaited-release dates and source links from ``watch_calendar.json``.
"""

from __future__ import annotations

import datetime as dt
import importlib.util
import json
import re
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
VAULT = HERE.parent
ASTRO = VAULT / "03 - Astrology"
CROSS = VAULT / "04 - Synthesis" / "Cross-cuts"

OVERLAPS = ASTRO / "astrology_spine_overlaps.json"
PLOT_ROOMS = ASTRO / "astrology_spine_plot_rooms.json"
REGIME_WAVES = ASTRO / "institutional_regime_waves.json"
REGISTRY = ASTRO / "chart_reading_registry.json"
TRANSITIONS = ASTRO / "chart_transition_watches.json"
BONES = HERE / "chart_reading_bones" / "index.json"
WATCH_CALENDAR = HERE / "watch_calendar.json"
MOON_FAMILIES = CROSS / "Moon Families.html"
SUBPLOT_RULES = HERE / "subplot_rules.py"
SYNODIC_STACKS = HERE / "chart_synodic_stacks.json"
SYNODIC_READINGS = ASTRO / "synodic_cycle_readings.json"
SYNODIC_SEEDS = HERE / "synodic_seed_families.json"
RELATIONSHIP_HISTORY = HERE / "planetary_relationship_history.json"
AMERICA_EPHEMERIS = HERE / "america_ephemeris.json"
MUNDANE_HISTORY = HERE / "mundane_history.json"
RESEARCH_DESK = HERE / "research_desk_data.json"
ENTITY_MAPS = VAULT / "04 - Synthesis" / "Entity Theory" / "eo_entity_maps.json"
EO_DIR = VAULT / "03 - Executive Orders"
OUT = CROSS / "Astrology Spine.html"

SCHEMA = "f250.astrology-spine/v2"
PLOT_SCHEMA = "f250.astrology-spine-plots/v2"
RELATIONSHIP_HISTORY_SCHEMA = "freedom250.planetary-relationships.geometry-history/v1"
REGIME_SCHEMA = "f250.institutional-regime-waves/v2"
PLOT_WINDOWS = {"y2024", "aries2025", "winter", "aries2026", "cancer", "libra", "cap"}
PLOT_KINDS = {"watch", "hypothesis", "named_hole", "inherited_record", "record"}
LANES = {"political_record", "money_rules", "operating_proof"}
WAVE_CLOCKS = {"astrology", "legal_person", "decision_right", "money", "operating", "contest"}
WAVE_MATURITIES = {"proposed", "authorized", "effective", "operating", "contested", "reversed", "failed", "unchanged"}
PLOT_MATURITIES = WAVE_MATURITIES
STORYLINE_LIFECYCLES = {"pilot", "candidate", "reviewed", "retired"}
STORYLINE_MODES = {"retrospective_calibration", "prospective_watch", "mixed_boundary"}
STORYLINE_ROLES = {"lead mechanism", "co-mechanism", "supporting context", "outcompeted", "unresolved"}
PRESENCE_MODES = {"inherited substrate", "active dialogue", "seed echo"}
CHECKPOINT_ROLES = {"opening", "intermediate", "closing"}
CONVERGENCE_MODES = {"co_timing", "shared_note_co_membership"}
REVIEW_DISPOSITIONS = {"Lines up", "Partial", "Miss", "Unresolved"}
STORY_STATES = {
    "attention_doctrine_and_partial_operation",
    "authorized_not_effective",
    "contested",
    "doctrine_and_partial_implementation",
    "investigating_and_building_controls",
    "mixed_commitment_draw_build_and_operation",
    "mixed_operating_and_proposed",
    "mixed_plan_build_and_operation",
    "operating_and_expanding",
    "operating_and_rewriting",
    "operating_with_unresolved_risk",
    "partial_release_and_contested_record",
    "testing_and_transition",
}
TRADITIONAL_RULERS = {
    "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury", "Cancer": "Moon",
    "Leo": "Sun", "Virgo": "Mercury", "Libra": "Venus", "Scorpio": "Mars",
    "Sagittarius": "Jupiter", "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter",
}
HOUSE_MEANINGS = {
    1: "the nation / the body", 2: "the treasury", 3: "the press / records / neighbours",
    4: "the land / opposition / foundations", 5: "speculation / children / pleasure",
    6: "workers / health / armed services", 7: "foreign relations / open enemy / treaty",
    8: "debt / taxes / shared consequence", 9: "law / courts / foreign affairs",
    10: "the government / the office", 11: "the legislature / allies", 12: "the hidden / prisons / secret enemies",
}


def fail(message: str) -> None:
    raise SystemExit(f"Astrology Spine: {message}")


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read {path.relative_to(VAULT)}: {exc}")


def recursive_score_key(value: Any) -> str | None:
    if isinstance(value, dict):
        for key, child in value.items():
            if "score" in str(key).lower() and key != "scores_allowed":
                return str(key)
            hit = recursive_score_key(child)
            if hit:
                return hit
    elif isinstance(value, list):
        for child in value:
            hit = recursive_score_key(child)
            if hit:
                return hit
    return None


def parse_date(value: Any, label: str) -> dt.date:
    text = str(value or "")
    try:
        return dt.date.fromisoformat(text)
    except ValueError:
        fail(f"{label} must be an ISO date")


def parse_moment_date(value: Any, label: str) -> dt.date:
    text = str(value or "")
    try:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
            return dt.date.fromisoformat(text)
        return dt.datetime.fromisoformat(text.replace("Z", "+00:00")).date()
    except ValueError:
        fail(f"{label} must be an ISO date or date-time")


def require_vault_source(value: Any, label: str) -> str:
    source = str(value or "").strip()
    path = Path(source)
    if not source or path.is_absolute() or ".." in path.parts:
        fail(f"{label} must be a vault-relative source path")
    if not (VAULT / path).is_file():
        fail(f"{label} source missing: {source}")
    return source


def normalize_source_refs(value: Any, label: str) -> list[dict[str, str]]:
    if not isinstance(value, list):
        fail(f"{label} must be a source-reference list")
    rows: list[dict[str, str]] = []
    seen: set[str] = set()
    for raw in value:
        if not isinstance(raw, dict):
            fail(f"{label} entries must be objects")
        source = require_vault_source(raw.get("source"), label)
        if source in seen:
            fail(f"{label} repeats source {source!r}")
        seen.add(source)
        rows.append({"source": source, "note": str(raw.get("note") or "").strip()})
    return rows


def first_heading(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^#\s+(.+?)\s*$", text, re.M)
    if not match:
        fail(f"reading has no H1: {path.relative_to(VAULT)}")
    return match.group(1).strip()


def load_subplot_rules() -> dict[str, list[tuple[str, Any]]]:
    spec = importlib.util.spec_from_file_location("f250_subplot_rules", SUBPLOT_RULES)
    if spec is None or spec.loader is None:
        fail("cannot import canonical subplot rules")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.RULES


def extract_moon_data() -> tuple[dict[str, Any], dict[str, Any]]:
    text = MOON_FAMILIES.read_text(encoding="utf-8")
    families_match = re.search(r"const DATA = (\{.*?\});\n", text, re.S)
    lineages_match = re.search(
        r"/\* LINEAGES-DATA-START \*/const LINEAGES=(\{.*?\});"
        r"/\* LINEAGES-DATA-END \*/",
        text,
        re.S,
    )
    if not families_match or not lineages_match:
        fail("Moon Families.html no longer exposes governed DATA/LINEAGES blocks")
    return json.loads(families_match.group(1)), json.loads(lineages_match.group(1))


def moon_context(
    date: str,
    kind: str,
    families: dict[str, Any],
    lineages: dict[str, Any],
) -> dict[str, Any] | None:
    if kind not in {"new", "full"}:
        return None
    family_hits: list[dict[str, Any]] = []
    for family in families.get("families", {}).values():
        for phase in family.get("phases", []):
            for member in phase.get("members", []):
                if member.get("date") == date:
                    family_hits.append(
                        {
                            "band": family.get("name"),
                            "band_description": family.get("description"),
                            "band_range": family.get("degree_range"),
                            "band_phase": phase.get("type"),
                            "member_sign": member.get("sign"),
                            "member_degree": member.get("degree"),
                        }
                    )
    if len(family_hits) != 1:
        fail(f"expected one degree-band Moon-family match for {date}, got {len(family_hits)}")

    phase_code = "nm" if kind == "new" else "fm"
    lineage_hits: list[tuple[dict[str, Any], dict[str, Any]]] = []
    for chain in lineages.get("chains", []):
        for member in chain.get("members", []):
            if member.get("date") == date and member.get("ph") == phase_code:
                lineage_hits.append((chain, member))
    if not lineage_hits and kind == "new":
        family = family_hits[0]
        return {
            **family,
            "lineage_phase": "seed",
            "seed_date": date,
            "seed_sign": family.get("member_sign"),
            "seed_degree": family.get("member_degree"),
            "seed_eclipse": False,
            "planted_subplot": "",
        }
    if len(lineage_hits) != 1:
        fail(f"expected one Pessin lineage match for {date}, got {len(lineage_hits)}")
    chain, member = lineage_hits[0]
    return {
        **family_hits[0],
        "lineage_phase": "seed" if kind == "new" else "full_moon_harvest",
        "seed_date": chain.get("seed_date"),
        "seed_sign": chain.get("sign"),
        "seed_degree": chain.get("deg"),
        "seed_eclipse": bool(chain.get("eclipse")),
        "planted_subplot": chain.get("planted") or "",
        "member_degree": member.get("deg") or family_hits[0].get("member_degree"),
    }


def bone_detail(reading_id: str) -> dict[str, Any]:
    path = HERE / "chart_reading_bones" / f"{reading_id}.json"
    if not path.is_file():
        fail(f"missing exact chart bone for {reading_id!r}")
    return load_json(path)


def current_phase_context(
    families: dict[str, Any], lineages: dict[str, Any], as_of_utc: str
) -> dict[str, Any] | None:
    """Return the latest exact lunar phase at or before the Long Clocks snapshot.

    Moon Families owns this already-computed geometry. Event counts in that
    generated surface are deliberately ignored because they have a separate
    refresh clock.
    """
    candidates: list[dict[str, Any]] = []
    for family in families.get("families", {}).values():
        for phase in family.get("phases", []):
            for member in phase.get("members", []):
                date = str(member.get("date") or "")
                time_utc = str(member.get("time_utc") or "00:00")
                if not date:
                    continue
                exact = f"{date}T{time_utc}:00+00:00"
                if exact <= as_of_utc:
                    candidates.append(
                        {
                            "exact_utc": exact,
                            "date": date,
                            "phase": member.get("type") or phase.get("type"),
                            "sign": member.get("sign") or member.get("moon_sign"),
                            "degree": member.get("degree"),
                            "band": family.get("name"),
                            "eclipse": bool(member.get("eclipse")),
                        }
                    )
    if not candidates:
        return None
    current = max(candidates, key=lambda row: row["exact_utc"])
    phase_codes = {
        "New Moon": "nm",
        "First Quarter": "fq",
        "Full Moon": "fm",
        "Last Quarter": "lq",
    }
    code = phase_codes.get(str(current.get("phase")))
    hits: list[dict[str, Any]] = []
    if code:
        for chain in lineages.get("chains", []):
            for member in chain.get("members", []):
                if member.get("date") == current["date"] and member.get("ph") == code:
                    hits.append(chain)
    if len(hits) == 1:
        chain = hits[0]
        current["lineage"] = {
            "seed_date": chain.get("seed_date"),
            "seed_sign": chain.get("sign"),
            "seed_degree": chain.get("deg"),
            "planted_subplot": chain.get("planted") or "",
        }
    parsed = dt.datetime.fromisoformat(current["exact_utc"])
    current["exact_local"] = parsed.astimezone(ZoneInfo("America/New_York")).isoformat()
    return current


def current_chapter_context(
    as_of_utc: str,
    bones: dict[str, dict[str, Any]],
    readings: dict[str, dict[str, Any]],
) -> dict[str, Any] | None:
    rows: list[dict[str, Any]] = []
    for reading_id, bone in bones.items():
        if bone.get("type") != "lunation" or bone.get("kind") != "new":
            continue
        detail = bone_detail(reading_id)
        utc = str(detail.get("utc") or "")
        registry = readings.get(reading_id)
        if not utc or not registry:
            continue
        rows.append(
            {
                "reading_id": reading_id,
                "exact_utc": utc,
                "exact_local": detail.get("edt"),
                "title": first_heading(VAULT / str(registry.get("source"))),
                "source": registry.get("source"),
                "sign": bone.get("sign"),
                "degree": bone.get("deg"),
                "eclipse": bone.get("eclipse"),
                "root": detail.get("root_members") or [],
            }
        )
    rows.sort(key=lambda row: row["exact_utc"])
    past = [row for row in rows if row["exact_utc"] <= as_of_utc]
    if not past:
        return None
    current = dict(past[-1])
    future = [row for row in rows if row["exact_utc"] > current["exact_utc"]]
    if future:
        current["governs_until_utc"] = future[0]["exact_utc"]
        current["governs_until_local"] = future[0]["exact_local"]
    return current


def america_hand(as_of_utc: str) -> dict[str, Any]:
    data = load_json(AMERICA_EPHEMERIS)
    date = as_of_utc[:10]
    lon = (data.get("916 America") or {}).get(date)
    if lon is None:
        fail(f"916 America cache does not cover {date}")
    signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    idx = int(float(lon) // 30) % 12
    return {
        "date": date,
        "longitude": float(lon),
        "sign": signs[idx],
        "degree": float(lon) % 30,
        "source": "99 - Templates/america_ephemeris.json",
        "source_generated": data.get("_generated"),
        "reading": "04 - Synthesis/Cross-cuts/2026-08-20 - America Is the Covenant — Astrology-First Working Reading.md",
    }


def america_context(detail: dict[str, Any]) -> dict[str, Any]:
    america = detail.get("america") or {}
    radical = int(america.get("house") or 0)
    sign = str(america.get("sign") or "")
    if radical not in range(1, 13) or sign not in TRADITIONAL_RULERS:
        fail("exact chart bone has no usable 916 America seat")
    positions = detail.get("pos") or {}
    steward = TRADITIONAL_RULERS[sign]
    steward_pos = positions.get(steward) or {}
    topics = []
    for turned, label in ((1, "American claim"), (2, "resources / price"), (7, "counterpart / challenger"), (10, "public standing")):
        landed = ((radical + turned - 2) % 12) + 1
        occupants = [name for name, row in positions.items() if row.get("house") == landed]
        topics.append(
            {
                "turned_house": turned,
                "label": label,
                "radical_house": landed,
                "radical_meaning": HOUSE_MEANINGS[landed],
                "occupants": occupants,
            }
        )
    return {
        "longitude": america.get("lon"),
        "position": america.get("lon_dms"),
        "sign": sign,
        "degree": america.get("deg_in_sign"),
        "radical_house": radical,
        "steward": steward,
        "steward_sign": steward_pos.get("sign"),
        "steward_house": steward_pos.get("house"),
        "steward_condition": steward_pos.get("cond") or [],
        "topics": topics,
    }


def build_umbrellas(
    authored_rows: list[dict[str, Any]],
    anchors: list[dict[str, Any]],
    releases: list[dict[str, Any]],
    subplot_rules: dict[str, list[tuple[str, Any]]],
) -> list[dict[str, Any]]:
    stacks = load_json(SYNODIC_STACKS)
    snapshot = stacks.get("snapshot") or {}
    cycles = {row.get("cycle_id"): row for row in snapshot.get("cycles", [])}
    reading_rows = load_json(SYNODIC_READINGS).get("readings", [])
    readings = {row.get("cycle_id"): row for row in reading_rows}
    anchor_ids = {row["reading_id"] for row in anchors}
    release_ids = {row["key"] for row in releases}
    seen: set[str] = set()
    prepared: list[dict[str, Any]] = []
    for row in authored_rows:
        cycle_id = str(row.get("cycle_id") or "")
        if not cycle_id or cycle_id in seen:
            fail(f"duplicate or blank umbrella cycle_id {cycle_id!r}")
        seen.add(cycle_id)
        orbital = cycles.get(cycle_id)
        archetype = readings.get(cycle_id)
        if not orbital or not archetype:
            fail(f"umbrella {cycle_id!r} is missing orbital or archetypal authority")
        carriers = [str(value) for value in row.get("carrier_reading_ids") or []]
        watches = [str(value) for value in row.get("watch_ids") or []]
        if not carriers or any(value not in anchor_ids for value in carriers):
            fail(f"umbrella {cycle_id!r} has an unknown chart carrier")
        if any(value not in release_ids for value in watches):
            fail(f"umbrella {cycle_id!r} has an unresolved watch reference")
        manifestations: list[dict[str, Any]] = []
        for link in row.get("manifestations") or []:
            plotline = str(link.get("plotline") or "")
            subplot = str(link.get("subplot") or "")
            state = str(link.get("state") or "")
            function = str(link.get("function") or "").strip()
            allowed = {label for label, _ in subplot_rules.get(plotline, [])}
            if subplot not in allowed or state not in STORY_STATES or not function:
                fail(f"umbrella {cycle_id!r} has an invalid manifestation link")
            manifestations.append({"plotline": plotline, "subplot": subplot, "state": state, "function": function})
        if not manifestations:
            fail(f"umbrella {cycle_id!r} has no manifestations")
        prepared.append(
            {
                "cycle_id": cycle_id,
                "label": row.get("label"),
                "current_note": row.get("current_note"),
                "co_presence": row.get("co_presence"),
                "carrier_reading_ids": carriers,
                "watch_ids": watches,
                "manifestations": manifestations,
                "archetype": archetype,
                "orbital": orbital,
                "as_of": snapshot.get("utc"),
            }
        )
    return prepared


def build_conjunction_map(editorial: dict[str, Any]) -> dict[str, Any]:
    """Join authored era groupings to calculate-once seed and phase facts."""
    if not editorial:
        fail("conjunction_map is required")
    seed_data = load_json(SYNODIC_SEEDS)
    stacks = load_json(SYNODIC_STACKS)
    reading_rows = load_json(SYNODIC_READINGS).get("readings", [])
    seeds = {row.get("cycle_id"): row for row in seed_data.get("cycles", [])}
    snapshot = stacks.get("snapshot") or {}
    cycles = {row.get("cycle_id"): row for row in snapshot.get("cycles", [])}
    readings = {row.get("cycle_id"): row for row in reading_rows}
    if not seeds or set(seeds) != set(cycles) or set(seeds) != set(readings):
        fail("conjunction roots, orbital snapshot, and cycle readings no longer align")

    groups: list[dict[str, Any]] = []
    covered: list[str] = []
    group_ids: set[str] = set()
    for group in editorial.get("eras") or []:
        group_id = str(group.get("id") or "")
        cycle_ids = [str(value) for value in group.get("cycle_ids") or []]
        if not group_id or group_id in group_ids or not cycle_ids:
            fail("conjunction_map has a blank/duplicate era or an empty cycle list")
        group_ids.add(group_id)
        if any(value not in seeds for value in cycle_ids):
            fail(f"conjunction era {group_id!r} references an unknown cycle")
        covered.extend(cycle_ids)
        groups.append(
            {
                "id": group_id,
                "label": group.get("label"),
                "years": group.get("years"),
                "theme": group.get("theme"),
                "cycle_ids": cycle_ids,
            }
        )
    if len(covered) != len(set(covered)) or set(covered) != set(seeds):
        fail("conjunction eras must cover each canonical cycle exactly once")

    roots: list[dict[str, Any]] = []
    for cycle_id in covered:
        seed = seeds[cycle_id]
        passes = seed.get("passes") or []
        if not passes:
            fail(f"conjunction root {cycle_id!r} has no exact passes")
        verification = sorted({str(row.get("independent_verification_status") or "") for row in passes})
        roots.append(
            {
                "cycle_id": cycle_id,
                "pair": seed.get("pair") or [],
                "tier_id": seed.get("tier_id"),
                "nominal_cycle_years": seed.get("nominal_cycle_years"),
                "seed_family_label": seed.get("seed_family_label"),
                "display_anchor_pass_id": seed.get("display_anchor_pass_id"),
                "passes": passes,
                "independent_verification": verification,
                "orbital": cycles[cycle_id],
                "archetype": readings[cycle_id],
            }
        )

    window = editorial.get("exact_window") or {}
    start, end = str(window.get("start") or ""), str(window.get("end") or "")
    if not start or not end or start > end:
        fail("conjunction_map exact_window is invalid")
    exacts: list[dict[str, Any]] = []
    for cycle_id, events in (stacks.get("exact_event_catalog") or {}).items():
        if cycle_id not in seeds:
            continue
        for event in events:
            date = str(event.get("utc") or "")[:10]
            if start <= date <= end:
                exacts.append(
                    {
                        "cycle_id": cycle_id,
                        "pair": seeds[cycle_id].get("pair") or [],
                        "utc": event.get("utc"),
                        "chapter_id": event.get("chapter_id"),
                        "aspect_id": event.get("aspect_id"),
                        "phase_name": event.get("phase_name"),
                        "phase_direction": event.get("phase_direction"),
                        "positions_deg": event.get("positions_deg") or {},
                    }
                )
    exacts.sort(key=lambda row: str(row.get("utc") or ""))
    if not exacts:
        fail("conjunction_map exact_window resolved no exact contacts")
    return {
        "title": editorial.get("title"),
        "dek": editorial.get("dek"),
        "groups": groups,
        "roots": roots,
        "exact_window": {
            "start": start,
            "end": end,
            "title": window.get("title"),
            "note": window.get("note"),
            "events": exacts,
        },
        "as_of": snapshot.get("utc"),
        "calculation_method": seed_data.get("calculation_method") or {},
    }


def resolve_watch_refs(
    refs: list[dict[str, Any]], rows: list[dict[str, Any]], window: dict[str, str]
) -> list[dict[str, Any]]:
    by_id: dict[str, dict[str, Any]] = {}
    for row in rows:
        watch_id = str(row.get("watch_id") or "")
        if watch_id:
            if watch_id in by_id:
                fail(f"duplicate watch_calendar watch_id {watch_id!r}")
            by_id[watch_id] = row

    resolved: list[dict[str, Any]] = []
    used: set[str] = set()
    for ref in refs:
        lane = ref.get("lane")
        if lane not in LANES:
            fail(f"invalid watch lane {lane!r}")
        row: dict[str, Any] | None = None
        key = str(ref.get("watch_id") or "")
        if key:
            row = by_id.get(key)
            if row is None:
                fail(f"unknown watch ref {key!r}")
        else:
            selector = ref.get("selector") or {}
            date, label = selector.get("date"), selector.get("label")
            hits = [r for r in rows if r.get("date") == date and r.get("label") == label]
            if len(hits) != 1:
                fail(f"watch selector {date!r} / {label!r} resolved {len(hits)} rows")
            row = hits[0]
            slug = re.sub(r"[^a-z0-9]+", "-", str(label).lower()).strip("-")[:44]
            key = f"calendar-{date}-{slug}"
        if key in used:
            fail(f"watch ref repeated: {key!r}")
        used.add(key)
        date = str(row.get("date") or "")
        if not (window["start"] <= date <= window["end"]):
            fail(f"watch ref {key!r} falls outside the authored window")
        resolved.append(
            {
                "key": key,
                "date": date,
                "end": row.get("end"),
                "approx": bool(row.get("approx")),
                "label": row.get("label"),
                "detail": row.get("detail") or "",
                "source": row.get("source") or "",
                "research_ids": row.get("research_ids") or [],
                "lane": lane,
            }
        )
    return sorted(resolved, key=lambda row: (row["date"], row["label"]))


def load_eo_inventory() -> dict[int, dict[str, Any]]:
    """Resolve the local EO shelf without inventing signing-time precision."""
    rows: dict[int, dict[str, Any]] = {}
    pattern = re.compile(r"^(\d{4}-\d{2}-\d{2}) - EO (\d+) - (.+)\.md$")
    for path in EO_DIR.glob("*.md"):
        match = pattern.match(path.name)
        if not match:
            continue
        date, number_text, filename_title = match.groups()
        number = int(number_text)
        if number in rows:
            fail(f"duplicate EO number in local shelf: {number}")
        title = filename_title
        try:
            title = first_heading(path).removeprefix(f"EO {number} — ").removeprefix(f"EO {number} - ")
        except SystemExit:
            pass
        rows[number] = {
            "number": number,
            "date": date,
            "title": title,
            "path": str(path.relative_to(VAULT)),
            "time_precision": "date",
        }
    return rows


def prepare_regime_waves() -> dict[str, Any]:
    authored = load_json(REGIME_WAVES)
    if authored.get("schema") != REGIME_SCHEMA:
        fail(f"institutional wave source must use {REGIME_SCHEMA}")
    score_key = recursive_score_key(authored)
    if score_key:
        fail(f"score-like field is forbidden in institutional waves: {score_key!r}")
    method = authored.get("method") or {}
    for flag in (
        "record_first_retrospective", "rhyme_is_not_cause", "daily_prediction_forbidden",
        "unchanged_is_valid", "degree_band_is_not_lineage",
    ):
        if method.get(flag) is not True:
            fail(f"institutional-wave method must preserve {flag}")
    for flag in ("chart_first", "pass1_freeze", "storyline_comparison"):
        if method.get(flag) is not False:
            fail(f"institutional-wave method must explicitly keep {flag} false")
    if method.get("comparison_mode") != "retrospective_calibration":
        fail("institutional waves must remain retrospective calibration")
    if method.get("layer_role") != "eo_led_maturity_overlay":
        fail("institutional waves must identify as the EO-led maturity overlay")
    if method.get("scores_allowed") is not False:
        fail("institutional-wave method must explicitly forbid scores")
    authority_layers = authored.get("authority_layers") or []
    if [row.get("id") for row in authority_layers] != [
        "climate", "official_story", "eo_maturity", "reorganization", "entity_routes",
    ]:
        fail("institutional-wave authority stack is missing or out of order")
    coverage_gaps = [str(value).strip() for value in authored.get("coverage_gaps") or [] if str(value).strip()]
    if not str(authored.get("scope_statement") or "").strip() or not coverage_gaps:
        fail("institutional waves must expose their scope and coverage gaps")

    history = load_json(MUNDANE_HISTORY)
    charts = {str(row.get("id") or ""): row for row in history.get("charts", [])}
    eo_inventory = load_eo_inventory()
    entity_data = load_json(ENTITY_MAPS)
    entity_numbers = {int(key) for key in (entity_data.get("maps") or {}) if str(key).isdigit()}
    research_data = load_json(RESEARCH_DESK)
    research_ids = {str(row.get("research_id") or "") for row in research_data.get("packages", [])}
    reading_registry = load_json(REGISTRY)
    reading_ids = {str(row.get("id") or "") for row in reading_registry.get("readings", [])}

    def chart_ref(chart_id: str) -> dict[str, Any]:
        row = charts.get(chart_id)
        if not row:
            fail(f"institutional wave references unknown chart {chart_id!r}")
        has_reading = chart_id in reading_ids
        return {
            "chart_id": chart_id,
            "label": row.get("label"),
            "date": row.get("date"),
            "utc": row.get("utc"),
            "local": row.get("local"),
            "chart_type": row.get("chart_type"),
            "kind": row.get("kind"),
            "sign": row.get("sign"),
            "degree": row.get("degree"),
            "eclipse": row.get("eclipse"),
            "asc_sign": row.get("asc_sign"),
            "root_members": row.get("root_members") or [],
            "governing_ingress_id": row.get("governing_ingress_id"),
            "verification": row.get("verification") or {},
            "reading_state": "authored" if has_reading else "computed_only",
            "reading_id": chart_id if has_reading else None,
        }

    def endpoint(spec: dict[str, Any]) -> dict[str, Any]:
        kind = str(spec.get("kind") or "")
        if kind == "chart":
            chart = chart_ref(str(spec.get("chart_id") or ""))
            return {"kind": kind, "date": chart["date"], "utc": chart["utc"], "label": chart["label"], "chart": chart}
        if kind in {"event", "cutoff"}:
            date = str(spec.get("date") or "")
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
                fail(f"institutional wave has invalid {kind} date {date!r}")
            return {"kind": kind, "date": date, "utc": f"{date}T00:00:00-04:00", "label": spec.get("label") or date}
        fail(f"institutional wave has unknown endpoint kind {kind!r}")

    waves: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    partials = 0
    for expected_ordinal, source in enumerate(authored.get("waves") or [], 1):
        wave_id = str(source.get("id") or "")
        if not wave_id or wave_id in seen_ids:
            fail(f"duplicate or blank institutional wave id {wave_id!r}")
        seen_ids.add(wave_id)
        if source.get("ordinal") != expected_ordinal:
            fail(f"institutional wave ordinal drift at {wave_id!r}")
        status = str(source.get("status") or "")
        if status not in {"closed", "partial"}:
            fail(f"institutional wave {wave_id!r} has invalid status")
        partials += status == "partial"
        start = endpoint(source.get("start") or {})
        end = endpoint(source.get("end") or {})
        hierarchy = source.get("chart_hierarchy") or {}
        strict_governor = chart_ref(str(hierarchy.get("strict_governor_id") or ""))
        local_frame_id = hierarchy.get("local_frame_id")
        local_frame = chart_ref(str(local_frame_id)) if local_frame_id else None
        if local_frame and local_frame["chart_id"] == strict_governor["chart_id"]:
            fail(f"institutional wave {wave_id!r} collapses strict governor and local frame")

        scope = source.get("eo_scope") or {}
        first = int(scope.get("expected_first") or 0)
        last = int(scope.get("expected_last") or 0)
        expected_count = int(scope.get("expected_count") or 0)
        expected_numbers = list(range(first, last + 1))
        if not first or last < first or len(expected_numbers) != expected_count:
            fail(f"institutional wave {wave_id!r} has an incoherent EO range/count")
        available_numbers = [number for number in expected_numbers if number in eo_inventory]
        missing_numbers = [number for number in expected_numbers if number not in eo_inventory]
        available_rows = [eo_inventory[number] for number in available_numbers]
        entity_mapped = [number for number in available_numbers if number in entity_numbers]
        boundary_rows = [
            eo_inventory[number] if number in eo_inventory else {"number": number, "missing": True}
            for number in scope.get("boundary_cases") or []
        ]

        beats: list[dict[str, Any]] = []
        for beat in source.get("beats") or []:
            chart = chart_ref(str(beat.get("chart_id") or ""))
            beats.append({**beat, "chart": chart})
        if not beats:
            fail(f"institutional wave {wave_id!r} has no lunar beats")
        new_moon_indexes = [idx for idx, beat in enumerate(beats) if beat["chart"].get("kind") == "new"]
        for position, idx in enumerate(new_moon_indexes):
            beat = beats[idx]
            chapter_start = str(beat["chart"].get("date") or "")
            next_start = (
                str(beats[new_moon_indexes[position + 1]]["chart"].get("date") or "")
                if position + 1 < len(new_moon_indexes) else "9999-12-31"
            )
            scope_start = str(scope.get("signed_from") or "")
            scope_end = str(scope.get("signed_through") or "")
            in_chapter = [
                row for row in available_rows
                if max(chapter_start, scope_start) <= row["date"] < next_start and row["date"] <= scope_end
            ]
            beat["eo_count"] = len(in_chapter)
            beat["eo_numbers"] = [row["number"] for row in in_chapter]

        evidence: list[dict[str, Any]] = []
        for item in source.get("evidence") or []:
            if item.get("clock") not in WAVE_CLOCKS:
                fail(f"institutional wave evidence {item.get('id')!r} has unknown clock")
            if item.get("maturity") not in WAVE_MATURITIES:
                fail(f"institutional wave evidence {item.get('id')!r} has unknown maturity")
            missing_research = sorted(set(item.get("research_ids") or []) - research_ids)
            if missing_research:
                fail(f"institutional wave evidence {item.get('id')!r} has unknown research ids {missing_research}")
            item_numbers = [int(number) for number in item.get("eo_numbers") or []]
            evidence.append({
                **item,
                "eo_coverage": {
                    "available": [number for number in item_numbers if number in eo_inventory],
                    "missing": [number for number in item_numbers if number not in eo_inventory],
                },
            })

        summary = source.get("summary") or {}
        required_summary = {"factual_movement", "archetypal_movement", "working_synthesis", "governing_question", "constructive", "shadow", "continuity", "handoff"}
        if required_summary - set(summary):
            fail(f"institutional wave {wave_id!r} is missing summary fields")
        official_story = source.get("official_story")
        if official_story:
            official_reading_id = str(official_story.get("reading_id") or "")
            if official_reading_id not in reading_ids:
                fail(f"institutional wave {wave_id!r} references unknown official story {official_reading_id!r}")
        waves.append({
            "id": wave_id,
            "ordinal": source["ordinal"],
            "status": status,
            "title": source.get("title"),
            "research_path": source.get("research_path"),
            "start": start,
            "end": end,
            "chart_hierarchy": {
                **hierarchy,
                "strict_governor": strict_governor,
                "local_frame": local_frame,
            },
            "root_note": source.get("root_note"),
            "slow_movement": source.get("slow_movement"),
            "summary": summary,
            "official_story": official_story,
            "eo_scope": {
                **scope,
                "available_count": len(available_rows),
                "available_numbers": available_numbers,
                "missing_numbers": missing_numbers,
                "coverage_state": "complete" if not missing_numbers else "gapped",
                "entity_mapped_count": len(entity_mapped),
                "orders": available_rows,
                "boundary_rows": boundary_rows,
            },
            "beats": beats,
            "evidence": evidence,
        })

    if len(waves) != 7 or partials != 1 or waves[-1]["status"] != "partial":
        fail("institutional wave series must contain six closed waves and one final partial wave")
    for previous, current in zip(waves, waves[1:]):
        if previous["end"].get("kind") == "chart" and current["start"].get("kind") == "chart":
            previous_chart = previous["end"]["chart"]["chart_id"]
            current_chart = current["start"]["chart"]["chart_id"]
            if previous_chart != current_chart:
                fail(f"institutional wave boundary gap: {previous['id']} → {current['id']}")

    cross_wave = authored.get("cross_wave") or {}
    required_cross = {"title", "thesis", "institutional_image", "transaction_rule", "sequence", "research_path"}
    if required_cross - set(cross_wave):
        fail("institutional wave source is missing the cross-wave thesis")
    sequence = cross_wave.get("sequence") or []
    if [row.get("wave_id") for row in sequence] != [row["id"] for row in waves]:
        fail("cross-wave sequence must name every wave exactly once in ordinal order")
    if any(not str(row.get("stage") or "").strip() for row in sequence):
        fail("every cross-wave sequence row needs a stage label")
    if any(not str(row.get("research_path") or "").strip() for row in waves):
        fail("every institutional wave needs a Research Desk source path")

    return {
        "schema": authored.get("schema"),
        "updated": authored.get("updated"),
        "status": authored.get("status"),
        "title": authored.get("title"),
        "window": authored.get("window"),
        "method": method,
        "scope_statement": authored.get("scope_statement"),
        "authority_layers": authority_layers,
        "coverage_gaps": coverage_gaps,
        "cross_wave": cross_wave,
        "waves": waves,
    }


def prepare_storylines(
    authored: dict[str, Any],
    subplot_rules: dict[str, list[tuple[str, Any]]],
) -> list[dict[str, Any]]:
    relationship_data = load_json(RELATIONSHIP_HISTORY)
    if relationship_data.get("schema") != RELATIONSHIP_HISTORY_SCHEMA:
        fail(f"relationship history must use {RELATIONSHIP_HISTORY_SCHEMA}")
    if relationship_data.get("status") != "generated" or relationship_data.get("deterministic") is not True:
        fail("relationship history must remain generated and deterministic")

    relationship_ids: set[str] = set()
    for row in relationship_data.get("cycle_catalog") or []:
        relationship_id = str(row.get("relationship_id") or "")
        if not relationship_id or relationship_id in relationship_ids:
            fail(f"relationship history has a blank or duplicate relationship {relationship_id!r}")
        relationship_ids.add(relationship_id)

    chart_by_id: dict[str, dict[str, Any]] = {}
    state_by_id: dict[str, dict[str, Any]] = {}
    for chart in relationship_data.get("charts") or []:
        chart_id = str(chart.get("chart_id") or "")
        if not chart_id or chart_id in chart_by_id:
            fail(f"relationship history has a blank or duplicate chart {chart_id!r}")
        chart_by_id[chart_id] = chart
        for state in chart.get("cycles") or []:
            state_id = str(state.get("state_id") or "")
            if not state_id or state_id in state_by_id:
                fail(f"relationship history has a blank or duplicate state {state_id!r}")
            state_by_id[state_id] = {"chart_id": chart_id, "state": state}
    ordered_charts = sorted(
        chart_by_id.items(),
        key=lambda row: (str(row[1].get("utc") or ""), str(row[1].get("date") or ""), row[0]),
    )
    chart_order = {chart_id: ordinal for ordinal, (chart_id, _) in enumerate(ordered_charts)}

    delta_by_id: dict[str, dict[str, Any]] = {}
    for history in relationship_data.get("histories") or []:
        relationship_id = str(history.get("relationship_id") or "")
        if relationship_id not in relationship_ids:
            fail(f"relationship history references unknown relationship {relationship_id!r}")
        for delta in history.get("deltas") or []:
            delta_id = str(delta.get("delta_id") or "")
            if not delta_id or delta_id in delta_by_id:
                fail(f"relationship history has a blank or duplicate delta {delta_id!r}")
            delta_by_id[delta_id] = {"relationship_id": relationship_id, "delta": delta}

    raw_storylines = authored.get("storylines")
    if not isinstance(raw_storylines, list):
        fail("plot-room source must carry an open-ended storylines list")

    storylines: list[dict[str, Any]] = []
    seen_storylines: set[str] = set()
    for raw in raw_storylines:
        if not isinstance(raw, dict):
            fail("storyline entries must be objects")
        storyline_id = str(raw.get("storyline_id") or "")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", storyline_id) or storyline_id in seen_storylines:
            fail(f"blank, malformed, or duplicate storyline_id {storyline_id!r}")
        seen_storylines.add(storyline_id)
        title = str(raw.get("title") or "").strip()
        question = str(raw.get("question") or "").strip()
        continuity_case = str(raw.get("continuity_case") or "").strip()
        if not title or not question or not continuity_case:
            fail(f"storyline {storyline_id!r} needs title, question, and continuity case")

        lifecycle = raw.get("lifecycle") or {}
        lifecycle_status = str(lifecycle.get("status") or "")
        lifecycle_reason = str(lifecycle.get("reason") or "").strip()
        lifecycle_at = str(lifecycle.get("status_at") or "")
        if lifecycle_status not in STORYLINE_LIFECYCLES or not lifecycle_reason:
            fail(f"storyline {storyline_id!r} has an invalid lifecycle")
        parse_moment_date(lifecycle_at, f"storyline {storyline_id!r} lifecycle.status_at")

        plot_refs_raw = raw.get("plot_refs")
        if not isinstance(plot_refs_raw, list) or not plot_refs_raw:
            fail(f"storyline {storyline_id!r} needs at least one canonical plot reference")
        plot_refs: list[dict[str, str]] = []
        seen_plot_refs: set[tuple[str, str]] = set()
        for ref in plot_refs_raw:
            if not isinstance(ref, dict):
                fail(f"storyline {storyline_id!r} plot refs must be objects")
            plotline = str(ref.get("plotline") or "")
            subplot = str(ref.get("subplot") or "")
            if plotline not in subplot_rules:
                fail(f"storyline {storyline_id!r} references unknown plotline {plotline!r}")
            if subplot and subplot not in {label for label, _ in subplot_rules.get(plotline, [])}:
                fail(f"storyline {storyline_id!r} references unknown subplot {plotline!r} / {subplot!r}")
            key = (plotline, subplot)
            if key in seen_plot_refs:
                fail(f"storyline {storyline_id!r} repeats plot ref {plotline!r} / {subplot!r}")
            seen_plot_refs.add(key)
            normalized_ref = {"plotline": plotline}
            if subplot:
                normalized_ref["subplot"] = subplot
            plot_refs.append(normalized_ref)

        frame = raw.get("factual_frame") or {}
        comparison_mode = str(frame.get("comparison_mode") or "")
        if comparison_mode not in STORYLINE_MODES:
            fail(f"storyline {storyline_id!r} has an invalid comparison mode")
        window = frame.get("window") or {}
        window_start_text = str(window.get("start") or "")
        window_end_text = str(window.get("end") or "")
        cutoff_text = str(frame.get("cutoff") or "")
        window_start = parse_date(window_start_text, f"storyline {storyline_id!r} window.start")
        window_end = parse_date(window_end_text, f"storyline {storyline_id!r} window.end")
        cutoff_date = parse_moment_date(cutoff_text, f"storyline {storyline_id!r} cutoff")
        if window_start > window_end:
            fail(f"storyline {storyline_id!r} window runs backward")
        if comparison_mode == "retrospective_calibration" and cutoff_date < window_end:
            fail(f"retrospective storyline {storyline_id!r} cutoff precedes its window end")
        if comparison_mode == "prospective_watch" and cutoff_date > window_start:
            fail(f"prospective storyline {storyline_id!r} was not frozen by its window start")
        if comparison_mode == "mixed_boundary" and not window_start <= cutoff_date <= window_end:
            fail(f"mixed-boundary storyline {storyline_id!r} cutoff must fall inside its window")

        attention_refs = normalize_source_refs(frame.get("attention_refs"), f"storyline {storyline_id!r} Attention")
        official_refs = normalize_source_refs(frame.get("official_refs"), f"storyline {storyline_id!r} Official")
        entity_refs = normalize_source_refs(frame.get("entity_refs"), f"storyline {storyline_id!r} Entity")
        if not attention_refs and not official_refs and not entity_refs:
            fail(f"storyline {storyline_id!r} has no factual source in any evidence lane")

        convergence_raw = frame.get("factual_convergence_refs", [])
        if not isinstance(convergence_raw, list):
            fail(f"storyline {storyline_id!r} factual_convergence_refs must be a list")
        convergence_refs: list[dict[str, Any]] = []
        seen_convergence: set[tuple[str, str, str]] = set()
        for ref in convergence_raw:
            if not isinstance(ref, dict):
                fail(f"storyline {storyline_id!r} convergence refs must be objects")
            mode = str(ref.get("mode") or "")
            if mode not in CONVERGENCE_MODES or ref.get("historical") is not True:
                fail(f"storyline {storyline_id!r} has an invalid or non-historical convergence ref")
            source = require_vault_source(ref.get("source"), f"storyline {storyline_id!r} convergence")
            historical_cutoff = str(ref.get("cutoff") or "")
            if parse_moment_date(historical_cutoff, f"storyline {storyline_id!r} convergence cutoff") > cutoff_date:
                fail(f"storyline {storyline_id!r} convergence source is newer than its factual cutoff")
            key = (mode, source, historical_cutoff)
            if key in seen_convergence:
                fail(f"storyline {storyline_id!r} repeats a convergence reference")
            seen_convergence.add(key)
            convergence_refs.append({
                "mode": mode,
                "historical": True,
                "source": source,
                "cutoff": historical_cutoff,
                "note": str(ref.get("note") or "").strip(),
            })

        transition = raw.get("candidate_transition") or {}
        transition_out = {
            "from": str(transition.get("from") or "").strip(),
            "toward": str(transition.get("toward") or "").strip(),
            "mechanism": str(transition.get("mechanism") or "").strip(),
        }
        if not all(transition_out.values()):
            fail(f"storyline {storyline_id!r} needs a complete candidate transition")

        checkpoint_raw = raw.get("checkpoint_refs")
        if not isinstance(checkpoint_raw, list) or len(checkpoint_raw) < 2:
            fail(f"storyline {storyline_id!r} needs at least opening and closing checkpoints")
        checkpoint_refs: list[dict[str, str]] = []
        checkpoint_ids: list[str] = []
        for ref in checkpoint_raw:
            if not isinstance(ref, dict):
                fail(f"storyline {storyline_id!r} checkpoint refs must be objects")
            chart_id = str(ref.get("chart_id") or "")
            role = str(ref.get("role") or "")
            if chart_id not in chart_by_id or chart_id in checkpoint_ids or role not in CHECKPOINT_ROLES:
                fail(f"storyline {storyline_id!r} has an invalid or duplicate checkpoint {chart_id!r}")
            chart_date = parse_date(chart_by_id[chart_id].get("date"), f"relationship chart {chart_id!r} date")
            if not window_start <= chart_date <= window_end:
                fail(f"storyline {storyline_id!r} checkpoint {chart_id!r} falls outside its factual window")
            checkpoint_ids.append(chart_id)
            checkpoint_refs.append({"chart_id": chart_id, "role": role})
        if checkpoint_refs[0]["role"] != "opening" or checkpoint_refs[-1]["role"] != "closing":
            fail(f"storyline {storyline_id!r} must begin with opening and end with closing")
        if any(ref["role"] != "intermediate" for ref in checkpoint_refs[1:-1]):
            fail(f"storyline {storyline_id!r} interior checkpoints must be intermediate")
        orders = [chart_order[chart_id] for chart_id in checkpoint_ids]
        if orders != sorted(orders) or len(orders) != len(set(orders)):
            fail(f"storyline {storyline_id!r} checkpoints are not in governed chronological order")
        checkpoint_set = set(checkpoint_ids)

        strands_raw = raw.get("strands")
        if not isinstance(strands_raw, list) or not strands_raw:
            fail(f"storyline {storyline_id!r} needs at least one relationship strand")
        strands: list[dict[str, Any]] = []
        seen_relationships: set[str] = set()
        for strand in strands_raw:
            if not isinstance(strand, dict):
                fail(f"storyline {storyline_id!r} strands must be objects")
            relationship_id = str(strand.get("relationship_id") or "")
            role = str(strand.get("role") or "")
            if relationship_id not in relationship_ids or relationship_id in seen_relationships:
                fail(f"storyline {storyline_id!r} has an unknown or duplicate relationship {relationship_id!r}")
            if role not in STORYLINE_ROLES:
                fail(f"storyline {storyline_id!r} / {relationship_id!r} has an invalid role")
            seen_relationships.add(relationship_id)
            presence_modes = strand.get("presence_modes")
            if not isinstance(presence_modes, list) or not presence_modes or len(presence_modes) != len(set(presence_modes)):
                fail(f"storyline {storyline_id!r} / {relationship_id!r} needs unique presence modes")
            if any(mode not in PRESENCE_MODES for mode in presence_modes):
                fail(f"storyline {storyline_id!r} / {relationship_id!r} has an invalid presence mode")
            if "seed echo" in presence_modes:
                fail(
                    f"storyline {storyline_id!r} / {relationship_id!r} claims a seed echo "
                    "without a governed v2 echo-reference field"
                )
            win_if = str(strand.get("win_if") or "").strip()
            lose_if = str(strand.get("lose_if") or "").strip()
            if not win_if or not lose_if:
                fail(f"storyline {storyline_id!r} / {relationship_id!r} needs win and lose tests")

            state_ids_raw = strand.get("state_ids")
            if not isinstance(state_ids_raw, list) or len(state_ids_raw) != len(checkpoint_ids) or len(state_ids_raw) != len(set(state_ids_raw)):
                fail(f"storyline {storyline_id!r} / {relationship_id!r} needs one unique state per checkpoint")
            state_rows: list[tuple[int, str, dict[str, Any]]] = []
            for state_id_raw in state_ids_raw:
                state_id = str(state_id_raw or "")
                resolved = state_by_id.get(state_id)
                if not resolved or resolved["state"].get("relationship_id") != relationship_id:
                    fail(f"storyline {storyline_id!r} / {relationship_id!r} has an invalid state {state_id!r}")
                state_rows.append((chart_order[resolved["chart_id"]], state_id, resolved))
            if {row[2]["chart_id"] for row in state_rows} != checkpoint_set:
                fail(f"storyline {storyline_id!r} / {relationship_id!r} states do not cover its checkpoints exactly")
            state_rows.sort(key=lambda row: row[0])
            if "active dialogue" in presence_modes and not any(row[2]["state"].get("direct_aspect") for row in state_rows):
                fail(f"storyline {storyline_id!r} / {relationship_id!r} claims active dialogue without a direct Aspect")

            delta_ids_raw = strand.get("delta_ids")
            if not isinstance(delta_ids_raw, list) or not delta_ids_raw or len(delta_ids_raw) != len(set(delta_ids_raw)):
                fail(f"storyline {storyline_id!r} / {relationship_id!r} needs unique relationship deltas")
            delta_rows: list[tuple[int, str]] = []
            for delta_id_raw in delta_ids_raw:
                delta_id = str(delta_id_raw or "")
                resolved = delta_by_id.get(delta_id)
                if not resolved or resolved["relationship_id"] != relationship_id:
                    fail(f"storyline {storyline_id!r} / {relationship_id!r} has an invalid delta {delta_id!r}")
                delta = resolved["delta"]
                from_chart = str(delta.get("from_chart_id") or "")
                to_chart = str(delta.get("to_chart_id") or "")
                if from_chart not in chart_order or to_chart not in chart_order:
                    fail(f"storyline {storyline_id!r} / {relationship_id!r} delta has unknown endpoints")
                if not orders[0] <= chart_order[from_chart] < chart_order[to_chart] <= orders[-1]:
                    fail(f"storyline {storyline_id!r} / {relationship_id!r} delta falls outside its checkpoints")
                delta_rows.append((chart_order[from_chart], delta_id))
            delta_rows.sort(key=lambda row: row[0])
            strands.append({
                "relationship_id": relationship_id,
                "role": role,
                "presence_modes": list(presence_modes),
                "state_ids": [row[1] for row in state_rows],
                "delta_ids": [row[1] for row in delta_rows],
                "win_if": win_if,
                "lose_if": lose_if,
            })

        counterevidence_refs = normalize_source_refs(
            raw.get("counterevidence_refs"), f"storyline {storyline_id!r} counterevidence"
        )
        review = raw.get("review") or {}
        disposition = review.get("disposition")
        closed_at = review.get("closed_at")
        reviewed_by = str(review.get("reviewed_by") or "").strip() or None
        populated_review = disposition is not None or closed_at is not None or reviewed_by is not None
        complete_review = disposition in REVIEW_DISPOSITIONS and closed_at is not None and reviewed_by is not None
        if lifecycle_status in {"pilot", "candidate"} and populated_review:
            fail(f"open storyline {storyline_id!r} cannot carry a closed review")
        if lifecycle_status == "reviewed" and not complete_review:
            fail(f"reviewed storyline {storyline_id!r} needs disposition, close time, and reviewer")
        if lifecycle_status == "retired" and populated_review and not complete_review:
            fail(f"retired storyline {storyline_id!r} has an incomplete historical review")
        if complete_review:
            if parse_moment_date(closed_at, f"storyline {storyline_id!r} review.closed_at") < cutoff_date:
                fail(f"storyline {storyline_id!r} review closed before its factual cutoff")
            if not counterevidence_refs:
                fail(f"closed storyline {storyline_id!r} must retain sourced counterevidence")

        storylines.append({
            "storyline_id": storyline_id,
            "title": title,
            "lifecycle": {"status": lifecycle_status, "status_at": lifecycle_at, "reason": lifecycle_reason},
            "plot_refs": plot_refs,
            "factual_frame": {
                "comparison_mode": comparison_mode,
                "window": {"start": window_start_text, "end": window_end_text},
                "cutoff": cutoff_text,
                "attention_refs": attention_refs,
                "official_refs": official_refs,
                "entity_refs": entity_refs,
                "factual_convergence_refs": convergence_refs,
            },
            "question": question,
            "candidate_transition": transition_out,
            "continuity_case": continuity_case,
            "checkpoint_refs": checkpoint_refs,
            "strands": strands,
            "counterevidence_refs": counterevidence_refs,
            "review": {
                "disposition": disposition if complete_review else None,
                "closed_at": str(closed_at) if complete_review else None,
                "reviewed_by": reviewed_by if complete_review else None,
            },
        })
    return storylines


def prepare_plot_rooms(
    subplot_rules: dict[str, list[tuple[str, Any]]],
    anchors: list[dict[str, Any]],
    umbrellas: list[dict[str, Any]],
    releases: list[dict[str, Any]],
) -> dict[str, Any]:
    authored = load_json(PLOT_ROOMS)
    if authored.get("schema") != PLOT_SCHEMA:
        fail(f"plot-room source must use {PLOT_SCHEMA}")
    score_key = recursive_score_key(authored)
    if score_key:
        fail(f"plot-room score-like field is forbidden: {score_key!r}")
    method = authored.get("method") or {}
    for flag in ("chart_first", "rhyme_is_not_cause", "unchanged_is_valid"):
        if method.get(flag) is not True:
            fail(f"plot-room method must preserve {flag}")
    for flag in ("scores_allowed", "automatic_story_assignment", "automatic_strand_promotion", "forecast_permission"):
        if method.get(flag) is not False:
            fail(f"plot-room method must explicitly keep {flag} false")
    if method.get("astrology_evidence_credit") != "none":
        fail("plot-room method must give astrology no factual-evidence credit")

    calendar_by_id: dict[str, dict[str, Any]] = {}
    for row in load_json(WATCH_CALENDAR).get("entries", []):
        watch_id = str(row.get("watch_id") or "")
        if watch_id:
            calendar_by_id[watch_id] = row
    release_by_watch = {row["key"]: row for row in releases}

    required_pairs: set[tuple[str, str]] = set()
    for umbrella in umbrellas:
        for link in umbrella.get("manifestations") or []:
            required_pairs.add((link["plotline"], link["subplot"]))
    for anchor in anchors:
        for overlap in anchor.get("overlaps") or []:
            required_pairs.add((overlap["plotline"], overlap["subplot"]))

    rooms_out: list[dict[str, Any]] = []
    seen_plotlines: set[str] = set()
    seen_clocks: set[str] = set()
    covered_pairs: set[tuple[str, str]] = set()
    DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

    for room in authored.get("rooms") or []:
        plotline = str(room.get("plotline") or "")
        if not plotline or plotline in seen_plotlines:
            fail(f"blank or duplicate plot-room plotline {plotline!r}")
        if plotline not in subplot_rules:
            fail(f"plot-room uses unknown plotline {plotline!r}")
        seen_plotlines.add(plotline)
        poles = room.get("poles") or {}
        if not str(room.get("dek") or "").strip() or not str(room.get("locked_question") or "").strip():
            fail(f"plot-room {plotline!r} needs a dek and locked question")
        if not str(poles.get("light") or "").strip() or not str(poles.get("shadow") or "").strip():
            fail(f"plot-room {plotline!r} needs both poles")
        allowed = {label for label, _ in subplot_rules.get(plotline, [])}
        subplots_out: list[dict[str, Any]] = []
        seen_subplots: set[str] = set()
        for sub in room.get("subplots") or []:
            subplot = str(sub.get("subplot") or "")
            state = str(sub.get("state") or "")
            function = str(sub.get("function") or "").strip()
            if subplot in seen_subplots or subplot not in allowed or state not in STORY_STATES or not function:
                fail(f"plot-room {plotline!r} has an invalid subplot {subplot!r}")
            seen_subplots.add(subplot)
            covered_pairs.add((plotline, subplot))
            clocks_out: list[dict[str, Any]] = []
            for clock in sub.get("clocks") or []:
                clock_id = str(clock.get("id") or "")
                if not clock_id or clock_id in seen_clocks:
                    fail(f"blank or duplicate plot-room clock {clock_id!r}")
                seen_clocks.add(clock_id)
                kind = str(clock.get("kind") or "")
                window = str(clock.get("window") or "")
                maturity = str(clock.get("maturity") or "")
                label = str(clock.get("label") or "").strip()
                why = str(clock.get("why") or "").strip()
                date = str(clock.get("date") or "")
                if kind not in PLOT_KINDS or window not in PLOT_WINDOWS or maturity not in PLOT_MATURITIES:
                    fail(f"clock {clock_id!r} has an invalid kind, window, or maturity")
                if not label or not why or not DATE.match(date):
                    fail(f"clock {clock_id!r} needs a date, label, and why")
                watch_id = str(clock.get("watch_id") or "") or None
                reading_id = str(clock.get("reading_id") or "") or None
                source = str(clock.get("source") or "") or None
                if kind == "watch":
                    if not watch_id or watch_id not in calendar_by_id:
                        fail(f"clock {clock_id!r} is a watch without a calendar id")
                    calendar_date = str(calendar_by_id[watch_id].get("date") or "")
                    if date != calendar_date:
                        fail(f"clock {clock_id!r} date {date} != watch_calendar {calendar_date}")
                elif kind in {"hypothesis", "named_hole", "record"}:
                    if not source:
                        fail(f"clock {clock_id!r} needs a vault source path")
                elif kind == "inherited_record":
                    if not reading_id and not source:
                        fail(f"clock {clock_id!r} inherited record needs a reading or source")
                if source:
                    source_path = VAULT / source
                    if not source_path.is_file():
                        fail(f"clock {clock_id!r} source missing: {source}")
                if reading_id and reading_id not in {row["reading_id"] for row in anchors}:
                    fail(f"clock {clock_id!r} references unknown reading {reading_id!r}")
                clocks_out.append(
                    {
                        "id": clock_id,
                        "date": date,
                        "label": label,
                        "maturity": maturity,
                        "window": window,
                        "kind": kind,
                        "inherited": bool(clock.get("inherited")),
                        "why": why,
                        "open_clock": str(clock.get("open_clock") or "").strip(),
                        "watch_id": watch_id,
                        "reading_id": reading_id,
                        "source": source,
                        "release": release_by_watch.get(watch_id) if watch_id else None,
                    }
                )
            clocks_out.sort(key=lambda row: row["date"])
            if not clocks_out:
                fail(f"plot-room {plotline!r} / {subplot!r} has no clocks")
            subplots_out.append(
                {
                    "subplot": subplot,
                    "state": state,
                    "function": function,
                    "clocks": clocks_out,
                }
            )
        if not subplots_out:
            fail(f"plot-room {plotline!r} has no subplots")
        rooms_out.append(
            {
                "plotline": plotline,
                "dek": str(room.get("dek") or "").strip(),
                "locked_question": str(room.get("locked_question") or "").strip(),
                "poles": {"light": str(poles.get("light") or "").strip(), "shadow": str(poles.get("shadow") or "").strip()},
                "subplots": subplots_out,
                "clock_count": sum(len(row["clocks"]) for row in subplots_out),
            }
        )

    missing = sorted(required_pairs - covered_pairs)
    if missing:
        fail("plot rooms missing required spine pairs: " + "; ".join(f"{a} / {b}" for a, b in missing))
    storylines = prepare_storylines(authored, subplot_rules)
    return {
        "schema": PLOT_SCHEMA,
        "updated": authored.get("updated"),
        "status": authored.get("status"),
        "title": authored.get("title"),
        "dek": authored.get("dek"),
        "method": method,
        "rooms": rooms_out,
        "storylines": storylines,
    }


def climate_for(date: str) -> dict[str, Any]:
    # Strict Greer validity: Cancer takes over only after mutable Aries expires;
    # fixed-rising Libra then governs six months. Capricorn is a nested winter
    # frame and does not replace Libra.
    if date < "2026-09-23":
        return {"governing": "2026 Cancer", "governing_reading_id": "ingress-2026-cancer"}
    row: dict[str, Any] = {
        "governing": "2026 Libra",
        "governing_reading_id": "ingress-2026-libra",
    }
    if date >= "2026-12-21":
        row.update({"nested": "2026 Capricorn", "nested_reading_id": "ingress-2026-capricorn"})
    return row


def build_payload() -> dict[str, Any]:
    authored = load_json(OVERLAPS)
    if authored.get("schema") != SCHEMA:
        fail(f"overlap source must use {SCHEMA}")
    score_key = recursive_score_key(authored)
    if score_key:
        fail(f"score-like field is forbidden: {score_key!r}")
    method = authored.get("method") or {}
    for flag in ("chart_first", "rhyme_is_not_cause", "unchanged_is_valid", "degree_band_is_not_lineage"):
        if method.get(flag) is not True:
            fail(f"method must preserve {flag}")
    if method.get("scores_allowed") is not False:
        fail("method must explicitly forbid scores")

    registry = load_json(REGISTRY)
    readings = {row["id"]: row for row in registry.get("readings", [])}
    transition_data = load_json(TRANSITIONS)
    transitions = {row["reading_id"]: row for row in transition_data.get("watches", [])}
    bones_data = load_json(BONES)
    bones = {row["id"]: row for row in bones_data.get("charts", [])}
    expected = set(transitions)
    actual = {str(row.get("reading_id") or "") for row in authored.get("anchors", [])}
    if actual != expected:
        fail(f"anchor coverage drifted: missing={sorted(expected-actual)} extra={sorted(actual-expected)}")

    subplot_rules = load_subplot_rules()
    families, lineages = extract_moon_data()
    anchors: list[dict[str, Any]] = []
    seen: set[str] = set()
    for authored_anchor in authored.get("anchors", []):
        reading_id = str(authored_anchor.get("reading_id") or "")
        if reading_id in seen:
            fail(f"duplicate anchor {reading_id!r}")
        seen.add(reading_id)
        registry_row = readings.get(reading_id)
        transition = transitions.get(reading_id)
        bone = bones.get(reading_id)
        if not registry_row or not transition or not bone:
            fail(f"anchor {reading_id!r} is missing registry, transition, or bone authority")

        source_rel = str(registry_row.get("source") or "")
        source_path = VAULT / source_rel
        if not source_path.is_file():
            fail(f"anchor source missing: {source_rel}")
        source_text = source_path.read_text(encoding="utf-8")
        if not re.search(rf"^reading_id:\s*{re.escape(reading_id)}\s*$", source_text, re.M):
            fail(f"reading identity drifted in {source_rel}")

        overlaps = authored_anchor.get("overlaps") or []
        if not 1 <= len(overlaps) <= 4:
            fail(f"anchor {reading_id!r} needs one to four natural overlaps")
        prepared_overlaps: list[dict[str, Any]] = []
        for overlap in overlaps:
            plotline = str(overlap.get("plotline") or "")
            subplot = str(overlap.get("subplot") or "")
            why = str(overlap.get("why") or "").strip()
            if not why:
                fail(f"anchor {reading_id!r} has an incomplete overlap hypothesis")
            allowed = {label for label, _ in subplot_rules.get(plotline, [])}
            if subplot not in allowed:
                fail(f"noncanonical overlap pair: {plotline!r} / {subplot!r}")
            prepared_overlaps.append({"plotline": plotline, "subplot": subplot, "why": why})

        date = str(bone.get("date") or "")
        chart_kind = str(bone.get("kind") or bone.get("type") or "")
        moon = moon_context(date, chart_kind, families, lineages)
        detail_bone = bone_detail(reading_id)
        exact_utc = str(detail_bone.get("utc") or "")
        exact_local = str(detail_bone.get("edt") or "")
        anchors.append(
            {
                "key": f"anchor-{reading_id}",
                "reading_id": reading_id,
                "date": date,
                "display_date": exact_local[:10] if exact_local else date,
                "exact_utc": exact_utc,
                "exact_local": exact_local,
                "title": first_heading(source_path),
                "source": source_rel,
                "chart_type": bone.get("type"),
                "chart_kind": chart_kind,
                "chart_role": transition.get("chart_role"),
                "sign": bone.get("sign"),
                "degree": bone.get("deg"),
                "eclipse": bone.get("eclipse"),
                "greer_quiet": bone.get("greer_quiet"),
                "climate": climate_for(date),
                "ingress_key": reading_id.removeprefix("ingress-") if bone.get("type") == "ingress" else None,
                "authority_question": transition.get("authority_question"),
                "decision_right": transition.get("decision_right"),
                "current_holder": transition.get("current_holder"),
                "claimant_or_constraint": transition.get("claimant_or_constraint"),
                "transition": transition.get("transition"),
                "mechanisms": transition.get("mechanisms") or [],
                "poles": transition.get("poles") or {},
                "arcs": (transition.get("synchronization") or {}).get("arcs") or [],
                "watch_for": (transition.get("synchronization") or {}).get("watch_for"),
                "evidence_test": transition.get("evidence_test") or {},
                "moon": moon,
                "root": detail_bone.get("root_members") or [],
                "america": america_context(detail_bone),
                "overlaps": prepared_overlaps,
            }
        )

    anchors.sort(key=lambda row: row["exact_utc"] or row["date"])
    releases = resolve_watch_refs(
        authored.get("watch_refs") or [],
        load_json(WATCH_CALENDAR).get("entries", []),
        authored["window"],
    )
    umbrellas = build_umbrellas(authored.get("umbrellas") or [], anchors, releases, subplot_rules)
    conjunction_map = build_conjunction_map(authored.get("conjunction_map") or {})
    regime_waves = prepare_regime_waves()
    plot_rooms = prepare_plot_rooms(subplot_rules, anchors, umbrellas, releases)
    for anchor in anchors:
        anchor["umbrella_ids"] = [
            row["cycle_id"] for row in umbrellas if anchor["reading_id"] in row["carrier_reading_ids"]
        ]
    for release in releases:
        release["umbrella_ids"] = [
            row["cycle_id"] for row in umbrellas if release["key"] in row["watch_ids"]
        ]
    as_of = str((umbrellas[0].get("as_of") if umbrellas else "") or "")
    return {
        "schema": SCHEMA,
        "built": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "updated": authored.get("updated"),
        "title": authored.get("title"),
        "status": authored.get("status"),
        "window": authored.get("window"),
        "method": method,
        "as_of": as_of,
        "current_chapter": current_chapter_context(as_of, bones, readings),
        "current_phase": current_phase_context(families, lineages, as_of),
        "america_hand": america_hand(as_of),
        "conjunction_map": conjunction_map,
        "regime_waves": regime_waves,
        "plot_rooms": plot_rooms,
        "umbrellas": umbrellas,
        "anchors": anchors,
        "releases": releases,
        "climates": [
            {"label": "Cancer climate", "start": "2026-06-21", "end": "2026-09-22", "reading_id": "ingress-2026-cancer", "note": "Mutable Aries expired; Cancer governs the quarter."},
            {"label": "Libra climate", "start": "2026-09-23", "end": "2027-03-19", "reading_id": "ingress-2026-libra", "note": "Aries rising makes this a six-month governing frame."},
            {"label": "Capricorn nested frame", "start": "2026-12-21", "end": "2027-03-19", "reading_id": "ingress-2026-capricorn", "nested": True, "note": "A winter subframe inside still-governing Libra."},
        ],
        "pattern_notes": [
            "One story can live beneath several planetary umbrellas, and one umbrella can move through many stories. These links are lenses, not ownership tags.",
            "A direct aspect, a cycle phase, and sign co-presence are different clocks. The view names them separately instead of holding the sky forever at exactitude.",
            "The governing ingress sets the room; the New Moon opens the chapter; Moon-family phases distribute and harvest the slower field through lived time.",
            "By plot is a third internal mode, not a second climate. Clocks live under canonical stories so a lunation card does not have to carry the whole reservoir.",
        ],
    }


TEMPLATE = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Astrology Spine — Freedom 250 Observatory</title>
<style>
:root{--paper:#f7f1e4;--paper2:#fffdf7;--ink:#2b261e;--muted:#766d60;--line:#d9cdb8;--navy:#173b55;--navy2:#285f78;--gold:#ad8240;--rust:#a75238;--sage:#617a68;--violet:#6f5b82;--shadow:0 12px 36px rgba(58,43,22,.10)}
html[data-theme="dark"]{--paper:#17191b;--paper2:#202326;--ink:#f1eadc;--muted:#b8ad9d;--line:#45413b;--navy:#86bfd5;--navy2:#5e9cb8;--gold:#d4ae6c;--rust:#db846a;--sage:#91b89a;--violet:#b6a3ca;--shadow:0 14px 38px rgba(0,0,0,.3)}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font-family:Georgia,'Times New Roman',serif;min-height:100vh}.shell{max-width:1460px;margin:auto;padding:24px 28px 52px}.hero{border:1px solid var(--line);border-radius:18px;padding:26px 30px;background:radial-gradient(circle at 88% 10%,rgba(173,130,64,.15),transparent 34%),var(--paper2);box-shadow:var(--shadow)}.eyebrow,.meta,.chip,.filter,.action,.date,.lane,.rank,.mini-label,.empty{font-family:system-ui,-apple-system,sans-serif}.eyebrow{font-size:11px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--gold)}h1{font-size:clamp(34px,5vw,68px);line-height:.96;margin:10px 0 14px;color:var(--navy);font-weight:500;letter-spacing:-.035em}.hero p{font-size:18px;line-height:1.55;max-width:900px;margin:0;color:var(--muted)}.hero-actions,.actions,.chips,.filters{display:flex;flex-wrap:wrap;gap:8px}.hero-actions{margin-top:20px}.action,.filter{appearance:none;border:1px solid var(--line);background:var(--paper2);color:var(--ink);border-radius:999px;padding:8px 13px;font-size:12px;font-weight:750;cursor:pointer;text-decoration:none}.action:hover,.filter:hover,.filter.active{border-color:var(--gold);color:var(--navy);background:color-mix(in srgb,var(--gold) 12%,var(--paper2))}.action.primary{background:var(--navy);color:var(--paper2);border-color:var(--navy)}.method-strip{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:16px 0}.pattern{padding:15px 16px;border:1px solid var(--line);border-radius:12px;background:var(--paper2);font-size:14px;line-height:1.45;color:var(--muted)}.pattern::before{content:'✦';color:var(--gold);margin-right:7px}.climate{margin:18px 0 10px;border:1px solid var(--line);border-radius:14px;background:var(--paper2);padding:14px 16px}.climate-head{display:flex;justify-content:space-between;gap:14px;align-items:baseline;margin-bottom:10px}.climate-head h2{font-size:16px;margin:0;color:var(--navy)}.meta{font-size:11px;color:var(--muted)}.climate-track{display:grid;grid-template-columns:34fr 57fr 9fr;height:12px;border-radius:999px;overflow:hidden;background:var(--line)}.climate-track button{border:0;cursor:pointer}.climate-track .cancer{background:var(--navy2)}.climate-track .libra{background:var(--gold)}.climate-track .capricorn{background:var(--rust)}.climate-labels{display:grid;grid-template-columns:34fr 57fr 9fr;gap:8px;margin-top:8px;font-family:system-ui,sans-serif;font-size:11px;color:var(--muted)}.controls{position:sticky;top:0;z-index:8;display:flex;justify-content:space-between;gap:14px;align-items:center;margin:18px 0 12px;padding:10px;border:1px solid var(--line);border-radius:14px;background:color-mix(in srgb,var(--paper) 90%,transparent);backdrop-filter:blur(12px)}.filters{min-width:0}.search{width:min(320px,35vw);border:1px solid var(--line);border-radius:999px;padding:9px 14px;background:var(--paper2);color:var(--ink);font:13px system-ui,sans-serif}.workspace{display:grid;grid-template-columns:minmax(340px, .82fr) minmax(480px,1.6fr);gap:16px;align-items:start}.timeline{border:1px solid var(--line);border-radius:16px;background:var(--paper2);padding:10px;max-height:calc(100vh - 110px);overflow:auto}.timeline-row{position:relative;display:grid;grid-template-columns:80px 18px 1fr;gap:10px;width:100%;border:0;background:transparent;color:var(--ink);text-align:left;padding:9px 8px;cursor:pointer;border-radius:10px}.timeline-row:hover,.timeline-row.active{background:color-mix(in srgb,var(--gold) 11%,transparent)}.timeline-row .date{font-size:11px;color:var(--muted);padding-top:3px}.node{position:relative;width:14px;height:14px;border-radius:50%;margin-top:3px;border:3px solid var(--paper2);box-shadow:0 0 0 1px var(--line);background:var(--navy)}.timeline-row:not(:last-child) .node::after{content:'';position:absolute;width:1px;height:42px;background:var(--line);top:14px;left:6px}.timeline-row.release .node{width:9px;height:9px;margin:5px 0 0 3px;border:0;box-shadow:none;background:var(--violet)}.timeline-row.release.money_rules .node{background:var(--gold)}.timeline-row.release.operating_proof .node{background:var(--sage)}.row-title{font-size:14px;line-height:1.28}.timeline-row.anchor .row-title{font-size:16px;color:var(--navy);font-weight:700}.row-sub{font:11px/1.35 system-ui,sans-serif;color:var(--muted);margin-top:3px}.detail{border:1px solid var(--line);border-radius:16px;background:var(--paper2);box-shadow:var(--shadow);min-height:620px}.detail-inner{padding:26px 28px 34px}.detail h2{font-size:clamp(26px,3.3vw,43px);line-height:1.05;margin:8px 0 12px;color:var(--navy);font-weight:500}.detail h3{font-size:17px;color:var(--navy);margin:25px 0 10px}.lead{font-size:19px;line-height:1.48;margin:0 0 17px}.chip{display:inline-flex;align-items:center;border:1px solid var(--line);border-radius:999px;padding:5px 9px;font-size:11px;color:var(--muted);background:var(--paper)}.chip.eclipse{border-color:var(--rust);color:var(--rust)}.chip.arc{cursor:pointer}.chip.arc:hover{border-color:var(--gold);color:var(--navy)}.transition{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:18px 0}.transition>div,.family-box,.proof-box,.release-box{border:1px solid var(--line);border-radius:12px;padding:14px 15px;background:var(--paper)}.mini-label{font-size:10px;text-transform:uppercase;letter-spacing:.11em;font-weight:850;color:var(--gold);margin-bottom:5px}.transition p,.family-box p,.proof-box p,.release-box p{margin:0;font-size:14px;line-height:1.45;color:var(--muted)}.family-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}.overlaps{display:grid;gap:10px}.overlap{border:1px solid var(--line);border-left:4px solid var(--gold);border-radius:12px;padding:13px 15px;background:var(--paper)}.overlap.also_watch{border-left-color:var(--navy2)}.overlap-top{display:flex;justify-content:space-between;gap:10px;align-items:flex-start}.overlap h4{font-size:17px;margin:0;color:var(--navy)}.overlap h4 button{font:inherit;color:inherit;border:0;background:transparent;padding:0;cursor:pointer;text-align:left}.overlap h4 button:hover{text-decoration:underline}.rank{font-size:10px;text-transform:uppercase;letter-spacing:.08em;font-weight:850;color:var(--gold);white-space:nowrap}.overlap p{font-size:14px;line-height:1.48;margin:7px 0 0;color:var(--muted)}.subplot-link{font:12px system-ui,sans-serif;color:var(--rust);border:0;background:transparent;padding:0;margin-top:4px;cursor:pointer}.subplot-link:hover{text-decoration:underline}.nearby{display:grid;gap:8px}.nearby button{width:100%;display:grid;grid-template-columns:82px 1fr;gap:10px;text-align:left;border:1px solid var(--line);border-radius:10px;padding:10px;background:var(--paper);color:var(--ink);cursor:pointer}.nearby button:hover{border-color:var(--gold)}.nearby .nd{font:11px system-ui,sans-serif;color:var(--muted)}.nearby .nt{font-size:13px}.release-detail .lane{display:inline-block;font-size:10px;text-transform:uppercase;letter-spacing:.1em;font-weight:850;color:var(--violet)}.source-link{color:var(--navy);word-break:break-word}.empty{padding:30px;text-align:center;color:var(--muted)}.ethics{margin-top:22px;border-top:1px solid var(--line);padding-top:16px;font:12px/1.5 system-ui,sans-serif;color:var(--muted)}
.now-stack{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:16px 0}.now-card{border:1px solid var(--line);border-radius:14px;background:var(--paper2);padding:15px}.now-card h2{font-size:16px;color:var(--navy);margin:5px 0 7px}.now-card p{font-size:12px;line-height:1.45;color:var(--muted);margin:0}.umbrella-shell{border:1px solid var(--line);border-radius:16px;background:var(--paper2);padding:16px;margin:16px 0}.umbrella-head{display:flex;justify-content:space-between;gap:16px;align-items:flex-end}.umbrella-head h2{margin:0;color:var(--navy);font-size:20px}.umbrella-head p{margin:0;max-width:660px;color:var(--muted);font-size:13px;line-height:1.4}.umbrella-rail{display:grid;grid-template-columns:repeat(6,minmax(145px,1fr));gap:8px;margin-top:13px;overflow:auto}.umbrella-card{border:1px solid var(--line);border-radius:12px;background:var(--paper);color:var(--ink);padding:12px;text-align:left;cursor:pointer;min-height:115px}.umbrella-card:hover,.umbrella-card.active{border-color:var(--gold);background:color-mix(in srgb,var(--gold) 10%,var(--paper))}.umbrella-card b{display:block;color:var(--navy);font-size:14px;line-height:1.2}.umbrella-card span{display:block;font:11px/1.35 system-ui,sans-serif;color:var(--muted);margin-top:7px}.manifestations{display:grid;gap:10px}.manifestation{border:1px solid var(--line);border-radius:12px;padding:14px 15px;background:var(--paper)}.manifestation h4{font-size:17px;margin:0;color:var(--navy)}.manifestation p{margin:7px 0 0;font-size:14px;line-height:1.45;color:var(--muted)}button.chip{cursor:pointer}.orbit-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}.rank{display:none}
.mode-switch{display:flex;gap:8px;margin:14px 0 0;padding:5px;border:1px solid var(--line);border-radius:999px;background:var(--paper2);width:max-content;max-width:100%}.mode-button{appearance:none;border:0;border-radius:999px;background:transparent;color:var(--muted);padding:9px 14px;cursor:pointer;font:800 12px system-ui,sans-serif;white-space:nowrap}.mode-button.active{background:var(--navy);color:var(--paper2)}[hidden]{display:none!important}.wave-mode{margin-top:16px}.wave-intro{border:1px solid var(--line);border-radius:16px;background:linear-gradient(135deg,color-mix(in srgb,var(--gold) 10%,var(--paper2)),var(--paper2) 52%);padding:18px 20px}.wave-intro h2{color:var(--navy);font-weight:500;font-size:28px;margin:5px 0 8px}.wave-intro p{font-size:14px;line-height:1.5;color:var(--muted);margin:0;max-width:1050px}.wave-thesis-line{font-size:18px!important;color:var(--ink)!important;margin-top:10px!important}.wave-arc{display:grid;grid-template-columns:repeat(7,minmax(120px,1fr));gap:6px;overflow:auto;margin:14px 0 0}.wave-arc button{position:relative;border:0;border-top:3px solid var(--gold);background:color-mix(in srgb,var(--gold) 8%,var(--paper));color:var(--navy);padding:10px 8px;text-align:left;cursor:pointer;font:800 11px/1.25 system-ui,sans-serif}.wave-arc button:not(:last-child)::after{content:'→';position:absolute;right:-7px;top:8px;color:var(--gold);z-index:2}.wave-arc small{display:block;color:var(--muted);font-weight:600;margin-top:3px}.wave-rail{display:grid;grid-template-columns:repeat(7,minmax(150px,1fr));gap:8px;overflow:auto;margin:12px 0}.wave-tab{border:1px solid var(--line);border-radius:13px;background:var(--paper2);color:var(--ink);padding:12px;text-align:left;cursor:pointer;min-height:98px}.wave-tab:hover,.wave-tab.active{border-color:var(--gold);background:color-mix(in srgb,var(--gold) 10%,var(--paper2))}.wave-tab b{display:block;color:var(--navy);font-size:13px;line-height:1.25}.wave-tab span{display:block;font:10px/1.4 system-ui,sans-serif;color:var(--muted);margin-top:6px}.wave-layout{display:grid;grid-template-columns:minmax(290px,.72fr) minmax(520px,1.6fr);gap:14px;align-items:start}.wave-sidebar,.wave-detail{border:1px solid var(--line);border-radius:16px;background:var(--paper2)}.wave-sidebar{padding:16px;position:sticky;top:12px}.wave-sidebar h3{font-size:18px;color:var(--navy);margin:5px 0 10px}.wave-sidebar p{font-size:13px;line-height:1.45;color:var(--muted);margin:7px 0}.wave-detail{padding:24px 26px}.wave-detail h2{font-size:clamp(28px,3.2vw,44px);font-weight:500;line-height:1.04;color:var(--navy);margin:6px 0 12px}.wave-detail h3{font-size:18px;color:var(--navy);margin:24px 0 10px}.wave-kicker{font:800 11px/1.4 system-ui,sans-serif;text-transform:uppercase;letter-spacing:.1em;color:var(--gold)}.wave-thesis{font-size:20px;line-height:1.45;margin:0 0 16px}.wave-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}.wave-panel{border:1px solid var(--line);border-radius:12px;background:var(--paper);padding:14px 15px}.wave-panel p{font-size:14px;line-height:1.47;color:var(--muted);margin:0}.wave-panel b{color:var(--ink)}.beat-list,.evidence-list{display:grid;gap:9px}.beat-card,.evidence-card{border:1px solid var(--line);border-radius:12px;background:var(--paper);padding:13px 14px}.beat-head,.evidence-head{display:flex;gap:10px;align-items:flex-start;justify-content:space-between}.beat-card h4,.evidence-card h4{font-size:16px;color:var(--navy);margin:0}.beat-card p,.evidence-card p{font-size:13px;line-height:1.45;color:var(--muted);margin:7px 0 0}.beat-meta,.coverage{font:800 10px/1.35 system-ui,sans-serif;text-transform:uppercase;letter-spacing:.07em;color:var(--gold);white-space:nowrap}.coverage.gapped{color:var(--rust)}.coverage.boundary-note{white-space:normal;text-transform:none;letter-spacing:0}.eo-strip{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}.eo-link{border:1px solid var(--line);border-radius:999px;background:var(--paper2);color:var(--navy);padding:5px 8px;cursor:pointer;font:750 10px system-ui,sans-serif}.eo-link:hover{border-color:var(--gold)}.hard-boundary{border-left:3px solid var(--rust);padding-left:10px}.wave-actions{display:flex;flex-wrap:wrap;gap:8px;margin-top:13px}.wave-actions button{border:1px solid var(--line);border-radius:999px;background:var(--paper2);color:var(--ink);padding:7px 10px;cursor:pointer;font:750 11px system-ui,sans-serif}.wave-actions button:hover{border-color:var(--gold);color:var(--navy)}
.wave-layout,.wave-sidebar,.wave-detail,.wave-grid,.wave-panel,.beat-list,.evidence-list,.beat-card,.evidence-card{min-width:0}.wave-sidebar p,.wave-detail p,.wave-detail h4,.wave-actions button{overflow-wrap:anywhere}
.root-shell{border:1px solid var(--line);border-radius:18px;background:linear-gradient(135deg,color-mix(in srgb,var(--navy) 8%,var(--paper2)),var(--paper2) 46%);padding:20px;margin:16px 0}.root-head{display:flex;align-items:flex-end;justify-content:space-between;gap:20px}.root-head h2{font-size:25px;font-weight:500;color:var(--navy);margin:4px 0 0}.root-head p{font-size:14px;line-height:1.48;color:var(--muted);max-width:730px;margin:0}.era-tabs{display:flex;gap:8px;overflow:auto;margin:16px 0 12px;padding-bottom:2px}.era-tab{border:1px solid var(--line);border-radius:999px;background:var(--paper);color:var(--ink);padding:8px 12px;white-space:nowrap;cursor:pointer;font:700 11px system-ui,sans-serif}.era-tab.active,.era-tab:hover{border-color:var(--gold);color:var(--navy);background:color-mix(in srgb,var(--gold) 11%,var(--paper))}.era-theme{border-left:3px solid var(--gold);padding:2px 0 2px 12px;font-size:14px;line-height:1.46;color:var(--muted);margin:0 0 13px}.root-workspace{display:grid;grid-template-columns:minmax(280px,.85fr) minmax(430px,1.5fr);gap:12px}.root-list{display:grid;gap:8px}.root-card{border:1px solid var(--line);border-radius:12px;background:var(--paper);color:var(--ink);padding:12px 13px;text-align:left;cursor:pointer}.root-card:hover,.root-card.active{border-color:var(--gold);background:color-mix(in srgb,var(--gold) 9%,var(--paper))}.root-card b{display:block;font-size:15px;color:var(--navy)}.root-card span{display:block;font:11px/1.4 system-ui,sans-serif;color:var(--muted);margin-top:4px}.root-detail{border:1px solid var(--line);border-radius:14px;background:var(--paper2);padding:18px 20px;min-height:240px}.root-detail h3{font-size:24px;font-weight:500;color:var(--navy);margin:5px 0 9px}.root-detail .lead{font-size:16px;margin-bottom:13px}.seed-passes{display:flex;flex-wrap:wrap;gap:7px;margin:10px 0}.seed-pass{border:1px solid var(--line);border-radius:9px;background:var(--paper);padding:8px 9px;font:11px/1.35 system-ui,sans-serif;color:var(--muted)}.seed-pass b{color:var(--ink)}.clock-now{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:12px 0}.clock-now>div{border:1px solid var(--line);border-radius:10px;background:var(--paper);padding:11px 12px}.clock-now p{font-size:12px;line-height:1.42;color:var(--muted);margin:4px 0 0}.exact-shell{margin-top:19px;border-top:1px solid var(--line);padding-top:17px}.exact-head{display:flex;align-items:flex-end;justify-content:space-between;gap:16px}.exact-head h3{font-size:18px;color:var(--navy);margin:3px 0 0}.exact-head p{font:11px/1.4 system-ui,sans-serif;color:var(--muted);max-width:690px;margin:0}.exact-rail{display:flex;gap:8px;overflow:auto;padding:11px 1px 4px}.exact-event{min-width:185px;border:1px solid var(--line);border-radius:11px;background:var(--paper);color:var(--ink);padding:10px 11px;text-align:left;cursor:pointer}.exact-event:hover{border-color:var(--gold)}.exact-event time{display:block;font:800 10px system-ui,sans-serif;color:var(--gold);text-transform:uppercase;letter-spacing:.07em}.exact-event b{display:block;color:var(--navy);font-size:14px;margin:4px 0}.exact-event span{display:block;font:11px/1.36 system-ui,sans-serif;color:var(--muted)}
.authority-stack{display:grid;grid-template-columns:repeat(5,minmax(150px,1fr));gap:7px;overflow:auto;margin-top:14px}.authority-layer{border:1px solid var(--line);border-radius:10px;background:var(--paper);padding:10px}.authority-layer b{display:block;font:800 11px/1.3 system-ui,sans-serif;color:var(--navy)}.authority-layer span{display:block;font:10px/1.4 system-ui,sans-serif;color:var(--muted);margin-top:4px}.scope-warning{margin-top:12px!important;border-left:3px solid var(--rust);padding-left:11px}.official-story{border-color:var(--gold);background:color-mix(in srgb,var(--gold) 8%,var(--paper))}
.plot-intro{border:1px solid var(--line);border-radius:16px;background:linear-gradient(135deg,color-mix(in srgb,var(--navy) 8%,var(--paper2)),var(--paper2) 52%);padding:16px 20px}.plot-intro h2{color:var(--navy);font-weight:500;font-size:28px;margin:4px 0 6px}.plot-intro p{font-size:14px;line-height:1.45;color:var(--muted);margin:0;max-width:980px}.plot-board{display:block;margin-top:4px}.plot-stage{border:1px solid var(--line);border-radius:16px;background:var(--paper2);padding:16px 18px 12px;overflow-x:auto}.plot-stage-head{margin-bottom:10px}.plot-stage-head h3{margin:3px 0 6px;color:var(--navy);font-size:26px;font-weight:500}.plot-stage-head p{margin:0;max-width:860px;color:var(--muted);font-size:15px;line-height:1.4}.plot-legend{display:flex;flex-wrap:wrap;gap:8px 14px;margin:8px 0 0;font:700 10px/1.2 system-ui,sans-serif;color:var(--muted);text-transform:uppercase;letter-spacing:.06em}.plot-legend i{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:5px;vertical-align:-1px;border:2px solid}.plot-legend .watch i{border-color:var(--violet);background:var(--violet)}.plot-legend .hypothesis i{border-color:var(--gold);background:transparent}.plot-legend .named_hole i{border-color:var(--rust);background:var(--rust)}.plot-legend .inherited_record i{border-color:var(--navy);background:var(--navy)}.plot-legend .record i{border-color:var(--sage);background:var(--sage)}.plot-key,#plotRoomDek{margin:6px 0 0;font:13px/1.4 system-ui,sans-serif;color:var(--muted);max-width:860px}.plot-axis{position:relative;height:44px;margin:0 8px 0 210px}.plot-ticks{position:absolute;inset:0 0 22px}.plot-tick{position:absolute;top:0;transform:translateX(-50%);font:700 10px system-ui,sans-serif;color:var(--muted);white-space:nowrap}.plot-tick.first{transform:none}.plot-tick.last{transform:translateX(-100%)}.plot-bands{position:absolute;left:0;right:0;top:18px;height:10px;border-radius:7px;overflow:hidden}.plot-band{position:absolute;top:0;bottom:0}.plot-band.y2024{background:color-mix(in srgb,var(--muted) 16%,var(--paper))}.plot-band.y2025{background:color-mix(in srgb,var(--muted) 28%,var(--paper))}.plot-band.aries{background:color-mix(in srgb,var(--sage) 55%,var(--paper))}.plot-band.cancer{background:var(--navy2)}.plot-band.libra{background:var(--gold)}.plot-band.cap{background:var(--rust)}.plot-band-labels{position:absolute;left:0;right:0;top:30px;height:14px}.plot-band-labels span{position:absolute;transform:translateX(-50%);font:800 9px system-ui,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}.plot-lanes{position:relative;min-width:760px}.plot-today-rail{position:absolute;left:210px;right:0;top:0;bottom:0;pointer-events:none;z-index:3}.plot-today{position:absolute;top:0;bottom:0;width:0;border-left:1px dashed var(--rust);z-index:3;pointer-events:none}.plot-today span{position:absolute;top:-16px;transform:translateX(-50%);font:800 9px system-ui,sans-serif;color:var(--rust);letter-spacing:.08em;text-transform:uppercase;background:var(--paper2);padding:0 4px}.plot-lane{display:grid;grid-template-columns:210px minmax(0,1fr);min-height:72px;border-top:1px solid var(--line)}.plot-lane-label{padding:12px 12px 8px 2px}.plot-lane-label b{display:block;font:700 12px/1.25 system-ui,sans-serif;color:var(--navy)}.plot-lane-label span{display:block;font:10px/1.3 system-ui,sans-serif;color:var(--muted);margin-top:3px}.plot-track{position:relative;min-height:72px}.plot-track-bg{position:absolute;inset:14px 0;border-radius:8px;overflow:hidden;opacity:.18}.plot-node{position:absolute;top:50%;width:32px;height:32px;margin-left:-16px;border:0;background:transparent;transform:translateY(-50%);cursor:pointer;z-index:4;padding:0}.plot-dot{position:absolute;left:50%;top:50%;width:16px;height:16px;margin:-8px 0 0 -8px;border-radius:50%;border:2px solid currentColor;background:transparent;pointer-events:none}.plot-node.watch{color:var(--violet)}.plot-node.hypothesis{color:var(--gold)}.plot-node.named_hole{color:var(--rust)}.plot-node.inherited_record{color:var(--navy)}.plot-node.record{color:var(--sage)}.plot-node.filled .plot-dot{background:currentColor}.plot-node:hover,.plot-node.active{z-index:7}.plot-node.active .plot-dot{box-shadow:0 0 0 4px color-mix(in srgb,currentColor 30%,transparent);transform:scale(1.12)}.plot-tip{position:absolute;left:50%;bottom:calc(100% + 4px);transform:translateX(-50%);white-space:nowrap;font:700 10px/1.2 system-ui,sans-serif;color:var(--ink);background:var(--paper2);border:1px solid var(--line);border-radius:8px;padding:4px 7px;box-shadow:var(--shadow);pointer-events:none;max-width:220px;overflow:hidden;text-overflow:ellipsis}.plot-tip{display:none;z-index:8}.plot-node:hover .plot-tip{display:block}.plot-inspector{border:1px solid var(--line);border-radius:16px;background:var(--paper2);box-shadow:var(--shadow);padding:20px 22px 24px;margin-top:14px}.plot-inspector h3{font-size:26px;font-weight:500;color:var(--navy);margin:6px 0 8px;line-height:1.15}.plot-inspector p{font-size:15px;line-height:1.5;color:var(--muted);margin:0 0 10px}.plot-poles{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:10px 0 12px}.plot-poles div{border:1px solid var(--line);border-radius:10px;padding:10px 11px;background:var(--paper)}.plot-poles p{margin:0;font-size:13px}.plot-empty{color:var(--muted);font-size:15px}
@media(max-width:1100px){.now-stack{grid-template-columns:1fr 1fr}.umbrella-rail{grid-template-columns:repeat(3,minmax(180px,1fr))}}
@media(max-width:980px){.method-strip{grid-template-columns:1fr}.workspace,.root-workspace,.wave-layout{grid-template-columns:1fr}.wave-sidebar{position:static}.timeline{max-height:390px}.detail{min-height:0}.controls{position:static;align-items:stretch;flex-direction:column}.search{width:100%;max-width:none}.family-grid{grid-template-columns:1fr}.umbrella-head,.root-head,.exact-head{display:block}.umbrella-head p,.root-head p,.exact-head p{margin-top:8px}.plot-poles{grid-template-columns:1fr}.plot-axis{margin-left:0}.plot-today-rail{left:0}}
@media(max-width:600px){.shell{padding:14px 12px 36px}.hero{padding:21px 18px}.hero p{font-size:16px}.mode-switch{width:100%;overflow:auto}.now-stack,.wave-grid{grid-template-columns:1fr}.wave-rail{grid-template-columns:repeat(7,190px)}.wave-detail{padding:20px 17px}.beat-head,.evidence-head{flex-wrap:wrap}.beat-meta,.coverage{white-space:normal}.umbrella-rail{grid-template-columns:repeat(6,210px)}.root-shell{padding:16px}.clock-now{grid-template-columns:1fr}.climate-labels{font-size:9px}.timeline-row{grid-template-columns:70px 14px 1fr}.detail-inner{padding:21px 18px 28px}.transition,.orbit-grid{grid-template-columns:1fr}}
</style>
</head>
<body>
<div class="shell">
  <header class="hero">
    <div class="eyebrow">Sky &amp; Charts · moving orbital map</div>
    <h1>The Astrology Spine</h1>
    <p>Real planetary cycles move through governing climates, lunar chapters, Chronicle manifestations, and awaited political gates. Umbrellas overlap freely: they organize the weather without owning a plotline or forcing an event.</p>
    <div class="hero-actions">
      <button class="action primary" type="button" data-focus-now>Focus the next chart</button>
      <button class="action" type="button" data-open-sub="chart-readings">Open Chart Readings</button>
      <button class="action" type="button" data-open-sub="moon-families">Open Moon Families</button>
      <button class="action" type="button" data-open-clocks>Open Long Clocks</button>
      <button class="action" type="button" data-open-comparison>Compare charts</button>
    </div>
  </header>
  <nav class="mode-switch" aria-label="Astrology Spine modes">
    <button class="mode-button active" type="button" data-mode="current">Now &amp; forward</button>
    <button class="mode-button" type="button" data-mode="plots">By plot</button>
    <button class="mode-button" type="button" data-mode="waves">Institutional waves · 2025→now</button>
  </nav>
  <section class="wave-mode" id="plotMode" hidden>
    <div class="plot-intro">
      <div class="eyebrow">Event timeline · same spine, no second climate</div>
      <h2 id="plotTitle"></h2>
      <p id="plotDek"></p>
    </div>
    <div class="era-tabs" id="plotRail" role="tablist" aria-label="Plotline rooms"></div>
    <div class="plot-board">
      <div class="plot-stage">
        <div class="plot-stage-head">
          <div class="eyebrow" id="plotKicker">Select a plot</div>
          <h3 id="plotRoomTitle"></h3>
          <p id="plotRoomDek"></p>
          <p id="plotQuestion"></p>
          <div class="plot-legend" aria-label="Event kinds">
            <span class="record"><i></i>Dated event</span>
            <span class="inherited_record"><i></i>On the chronicle</span>
            <span class="watch"><i></i>Still open</span>
            <span class="hypothesis"><i></i>Hypothesis</span>
            <span class="named_hole"><i></i>Named hole</span>
          </div>
          <p class="plot-key">Filled dots already happened. Open rings are unresolved. A watch is an event that has not closed yet.</p>
        </div>
        <div class="plot-axis" id="plotAxis"></div>
        <div class="plot-lanes" id="plotLanes"></div>
      </div>
      <aside class="plot-inspector" id="plotInspector" aria-live="polite"></aside>
    </div>
  </section>
  <section class="wave-mode" id="institutionalWaveMode" hidden>
    <div class="wave-intro">
      <div class="eyebrow">Record-first retrospective calibration · EO maturity layer</div>
      <h2>How the EO-led institutional layer matured inside the climate</h2>
      <p class="wave-thesis-line" id="waveCrossThesis"></p>
      <p id="waveMethod"></p>
      <div class="authority-stack" id="waveAuthority" aria-label="Interpretive authority stack"></div>
      <p class="scope-warning" id="waveScope"></p>
      <div class="wave-arc" id="waveArc" aria-label="Cross-wave institutional sequence"></div>
      <div class="wave-actions"><button type="button" data-wave-doc="cross">Read the full cross-wave synthesis</button></div>
    </div>
    <div class="wave-rail" id="waveRail" role="tablist" aria-label="Institutional regime waves"></div>
    <div class="wave-layout">
      <aside class="wave-sidebar" id="waveSidebar"></aside>
      <article class="wave-detail" id="waveDetail" aria-live="polite"></article>
    </div>
  </section>
  <div id="currentSpineMode">
  <section class="now-stack" id="nowStack" aria-label="The sky stack now"></section>
  <section class="root-shell" id="conjunctionRoots" aria-label="Long-cycle conjunction roots">
    <div class="root-head"><div><div class="eyebrow">Seed → phase → lived time</div><h2 id="rootTitle"></h2></div><p id="rootDek"></p></div>
    <div class="era-tabs" id="eraTabs" role="tablist" aria-label="Conjunction eras"></div>
    <p class="era-theme" id="eraTheme"></p>
    <div class="root-workspace">
      <div class="root-list" id="rootList" aria-label="Cycle roots"></div>
      <article class="root-detail" id="rootDetail" aria-live="polite"></article>
    </div>
    <div class="exact-shell">
      <div class="exact-head"><div><div class="eyebrow">Exact orbital handoffs</div><h3 id="exactTitle"></h3></div><p id="exactNote"></p></div>
      <div class="exact-rail" id="exactRail" aria-label="Exact 2026 long-cycle contacts"></div>
    </div>
  </section>
  <section class="umbrella-shell">
    <div class="umbrella-head"><div><div class="eyebrow">Planetary umbrellas</div><h2>One sky, many co-mingling stories</h2></div><p>Select an umbrella to hear its orbital phase, both archetypal poles, current manifestations, chart carriers, and factual release gates. Selection filters the timeline; it does not score support.</p></div>
    <div class="umbrella-rail" id="umbrellaRail"></div>
  </section>
  <section class="method-strip" id="patternNotes" aria-label="Patterns in the current sequence"></section>
  <section class="climate">
    <div class="climate-head"><h2>The governing frame</h2><span class="meta">Strict ingress validity · Capricorn stays nested under Libra</span></div>
    <div class="climate-track" aria-label="Cancer, Libra and nested Capricorn frames">
      <button class="cancer" type="button" data-reading="ingress-2026-cancer" title="Cancer climate"></button>
      <button class="libra" type="button" data-reading="ingress-2026-libra" title="Libra climate"></button>
      <button class="capricorn" type="button" data-reading="ingress-2026-capricorn" title="Capricorn nested frame"></button>
    </div>
    <div class="climate-labels"><span>Cancer · to Sep 22, 8:05 PM EDT</span><span>Libra · Sep 22 to Mar 19</span><span>Capricorn nested · Dec 21</span></div>
  </section>
  <section class="controls" aria-label="Timeline controls">
    <div class="filters" id="filters">
      <button class="filter active" type="button" data-filter="all">Everything</button>
      <button class="filter" type="button" data-filter="astrology">Charts</button>
      <button class="filter" type="button" data-filter="releases">Awaited releases</button>
      <button class="filter" type="button" data-filter="political_record">Political record</button>
      <button class="filter" type="button" data-filter="money_rules">Money &amp; rules</button>
      <button class="filter" type="button" data-filter="operating_proof">Operating proof</button>
    </div>
    <input class="search" id="search" type="search" placeholder="Find a plotline, subplot, chart, or release…" autocomplete="off">
  </section>
  <main class="workspace">
    <section class="timeline" id="timeline" aria-label="Astrology and release timeline"></section>
    <aside class="detail" id="detail" aria-live="polite"></aside>
  </main>
  </div>
</div>
<script id="astrology-spine-data" type="application/json">__DATA__</script>
<script>
(function(){
  "use strict";
  var DATA=JSON.parse(document.getElementById("astrology-spine-data").textContent);
  var timeline=document.getElementById("timeline"), detail=document.getElementById("detail"), search=document.getElementById("search"), umbrellaRail=document.getElementById("umbrellaRail");
  var conjunction=DATA.conjunction_map||{}, waveData=DATA.regime_waves||{}, plotData=DATA.plot_rooms||{}, filter="all", activeKey="", activeUmbrella="", activeEra="2020-braid", activeRoot="", activeWave=(DATA.regime_waves&&DATA.regime_waves.waves[0]?DATA.regime_waves.waves[0].id:""), activePlot=(plotData.rooms&&plotData.rooms[0]?plotData.rooms[0].plotline:""), activeClock="";
  var PLOT_DEFAULT_T0="2025-01-20", PLOT_DEFAULT_T1="2027-01-18";
  var PLOT_T0=PLOT_DEFAULT_T0, PLOT_T1=PLOT_DEFAULT_T1;
  var laneLabel={political_record:"Political record",money_rules:"Money & rules",operating_proof:"Operating proof"};
  var month=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
  function esc(v){return String(v==null?"":v).replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]})}
  function fmt(d){if(!d)return "";var p=d.split("-");return month[+p[1]-1]+" "+(+p[2])+", "+p[0]}
  function exactLocal(d){if(!d)return "";try{return new Intl.DateTimeFormat("en-US",{timeZone:"America/New_York",month:"short",day:"numeric",year:"numeric",hour:"numeric",minute:"2-digit",timeZoneName:"short"}).format(new Date(d))}catch(_){return d}}
  function exactUTC(d){if(!d)return "";try{return new Intl.DateTimeFormat("en-US",{timeZone:"UTC",month:"short",day:"numeric",year:"numeric",hour:"numeric",minute:"2-digit",hourCycle:"h23",timeZoneName:"short"}).format(new Date(d))}catch(_){return d}}
  function deg(v){return v==null?"":Number(v).toFixed(2)+"°"}
  function ord(v){var n=Number(v),m=n%100;if(m>=11&&m<=13)return n+"th";return n+({1:"st",2:"nd",3:"rd"}[n%10]||"th")}
  function dayDiff(a,b){return Math.round((new Date(a+"T12:00:00Z")-new Date(b+"T12:00:00Z"))/86400000)}
  function post(msg){try{window.parent.postMessage(msg,"*")}catch(_){}}
  function openReading(id,date){post({action:"navigateTo",tab:"obs-cr",date:date,childAction:"openReading",id:id})}
  function waveById(id){return (waveData.waves||[]).find(function(x){return x.id===id})}
  function chartAction(chart,label){if(!chart)return "";return '<button type="button" data-wave-chart="'+esc(chart.chart_id)+'">'+esc(label||chart.label)+'</button>'}
  function chartAuthorityAction(chart,label){if(!chart)return "";var state=chart.reading_state==="authored"?'authored reading available':'computed chart · no authored reading';return chartAction(chart,(label||chart.label)+' · '+state)}
  function eoButtons(numbers,limit){var rows=(numbers||[]),shown=rows.slice(0,limit||10),more=rows.length-shown.length;return shown.map(function(n){return '<button class="eo-link" type="button" data-eo="'+esc(n)+'">EO '+esc(n)+'</button>'}).join("")+(more>0?'<button class="eo-link" type="button" data-wave-eos>+'+more+' more in Executive Office</button>':"")}
  function setMode(mode){
    document.getElementById("institutionalWaveMode").hidden=mode!=="waves";
    document.getElementById("currentSpineMode").hidden=mode!=="current";
    document.getElementById("plotMode").hidden=mode!=="plots";
    document.querySelectorAll("[data-mode]").forEach(function(button){button.classList.toggle("active",button.dataset.mode===mode)});
    if(mode==="waves"){renderWaveRail();renderWave(activeWave)}
    if(mode==="plots"){renderPlotRail();renderPlot(activePlot)}
  }
  function plotRoom(id){return (plotData.rooms||[]).find(function(x){return x.plotline===id})}
  function windowLabel(w){return {y2024:"2024 rails",aries2025:"2025 Aries year",winter:"Winter nested",aries2026:"2026 Aries",cancer:"2026 Cancer · open",libra:"2026 Libra · watch",cap:"2026 Cap nested · watch"}[w]||w}
  function kindLabelPlot(k){return {watch:"Still open",hypothesis:"Hypothesis",named_hole:"Named hole · join existing map",inherited_record:"On the chronicle",record:"Dated event"}[k]||k}
  function plotDay(d){return Math.round((new Date(d+"T12:00:00Z")-new Date(PLOT_T0+"T12:00:00Z"))/86400000)}
  function plotPct(d){var span=plotDay(PLOT_T1);if(span<=0)return 0;var x=plotDay(d);return Math.max(0,Math.min(100,(x/span)*100))}
  function todayISO(){var n=new Date(),pad=function(x){return String(x).padStart(2,"0")};return n.getFullYear()+"-"+pad(n.getMonth()+1)+"-"+pad(n.getDate())}
  function earlierDate(a,b){return a<b?a:b}
  function laterDate(a,b){return a>b?a:b}
  function plotClocks(r){var rows=[];(r.subplots||[]).forEach(function(sub){(sub.clocks||[]).forEach(function(c){rows.push(Object.assign({subplot:sub.subplot,state:sub.state,subplot_function:sub.function},c))})});return rows}
  function findPlotClock(r,id){return plotClocks(r).find(function(c){return c.id===id})}
  function pickPlotClock(r){if(activeClock&&findPlotClock(r,activeClock))return activeClock;return ""}
  function setPlotSpan(r){
    PLOT_T0=PLOT_DEFAULT_T0;PLOT_T1=PLOT_DEFAULT_T1;
    var dates=plotClocks(r).map(function(c){return c.date}).sort();
    if(!dates.length)return;
    if(dates[0]<PLOT_T0) PLOT_T0=dates[0].slice(0,8)+"01";
    if(dates[dates.length-1]>PLOT_T1) PLOT_T1=dates[dates.length-1];
  }
  function plotBand(cls,start,end){
    if(!start||!end||end<=start)return "";
    return '<div class="plot-band '+cls+'" style="left:'+plotPct(start)+'%;width:'+(plotPct(end)-plotPct(start))+'%"></div>';
  }
  function plotClimateBands(){
    return plotBand("y2024",PLOT_T0,earlierDate(PLOT_T1,"2025-01-20"))
      +plotBand("y2025",laterDate(PLOT_T0,"2025-01-20"),earlierDate(PLOT_T1,"2026-03-20"))
      +plotBand("aries",laterDate(PLOT_T0,"2026-03-20"),earlierDate(PLOT_T1,"2026-06-21"))
      +plotBand("cancer",laterDate(PLOT_T0,"2026-06-21"),earlierDate(PLOT_T1,"2026-09-23"))
      +plotBand("libra",laterDate(PLOT_T0,"2026-09-23"),earlierDate(PLOT_T1,"2026-12-21"))
      +plotBand("cap",laterDate(PLOT_T0,"2026-12-21"),PLOT_T1);
  }
  function plotTickRows(){
    var rows=[[PLOT_T0,month[+PLOT_T0.slice(5,7)-1]+" "+PLOT_T0.slice(0,4),"first"]];
    var y=+PLOT_T0.slice(0,4), endY=+PLOT_T1.slice(0,4);
    for(var yy=y;yy<=endY;yy++){
      ["01-01","07-01"].forEach(function(md){
        var d=yy+"-"+md;
        if(d>PLOT_T0&&d<PLOT_T1) rows.push([d,month[+md.slice(0,2)-1]+" "+yy,""]);
      });
    }
    rows.push([PLOT_T1,month[+PLOT_T1.slice(5,7)-1]+" "+PLOT_T1.slice(0,4),"last"]);
    return rows;
  }
  function renderPlotAxis(){
    var tickHtml=plotTickRows().map(function(row){return '<span class="plot-tick '+row[2]+'" style="left:'+plotPct(row[0])+'%">'+esc(row[1])+'</span>'}).join("");
    var labels=[];
    if(PLOT_T0<"2025-01-20") labels.push([PLOT_T0,earlierDate(PLOT_T1,"2025-01-20"),"2024"]);
    [["2026-03-20","2026-06-21","Aries"],["2026-06-21","2026-09-23","Cancer"],["2026-09-23","2026-12-21","Libra"],["2026-12-21","2027-01-18","Cap"]].forEach(function(row){
      if(row[1]>PLOT_T0&&row[0]<PLOT_T1) labels.push([laterDate(row[0],PLOT_T0),earlierDate(row[1],PLOT_T1),row[2]]);
    });
    var labelHtml=labels.map(function(row){return '<span style="left:'+((plotPct(row[0])+plotPct(row[1]))/2)+'%">'+esc(row[2])+'</span>'}).join("");
    document.getElementById("plotAxis").innerHTML='<div class="plot-ticks">'+tickHtml+'</div><div class="plot-bands">'+plotClimateBands()+'</div><div class="plot-band-labels">'+labelHtml+'</div>';
  }
  function plotNodeHtml(c, stacked, stackIndex){
    var filled=["operating","effective","failed"].indexOf(c.maturity)>=0?" filled":"";
    var top=stacked?' top:calc(50% + '+(stackIndex*18-8)+'px);':'';
    var tip=fmt(c.date)+" · "+c.label;
    return '<button class="plot-node '+esc(c.kind)+filled+(c.id===activeClock?" active":"")+'" type="button" data-plot-clock="'+esc(c.id)+'" aria-label="'+esc(tip)+'" style="left:'+plotPct(c.date)+'%'+top+'"><span class="plot-dot"></span><span class="plot-tip">'+esc(tip)+'</span></button>';
  }
  function renderPlotInspector(r){
    var c=findPlotClock(r,activeClock);
    var el=document.getElementById("plotInspector");
    if(!c){el.innerHTML='<div class="eyebrow">Read an event</div><p class="plot-empty">This is a timeline. Hover a node for the name. Click to read what happened, or what is still open. The label hides when you move away.</p>';return}
    var actions='<button type="button" data-plotline-map="'+esc(r.plotline)+'">Open Subplot Map</button>';
    if(c.reading_id) actions+='<button type="button" data-reading="'+esc(c.reading_id)+'">Open chart reading</button>';
    if(c.watch_id||c.date) actions+='<button type="button" data-day="'+esc(c.date)+'">Open that day</button>';
    if(c.release&&c.release.source&&/^https?:/.test(c.release.source)) actions+='<a class="action" href="'+esc(c.release.source)+'" target="_blank" rel="noopener">Official source ↗</a>';
    el.innerHTML='<div class="eyebrow">Selected event · click another node to change</div><div class="eyebrow" style="margin-top:6px">'+esc(fmt(c.date))+' · '+esc(kindLabelPlot(c.kind))+'</div><h3>'+esc(c.label)+'</h3><div class="chips" style="margin:0 0 10px"><span class="chip">'+esc(c.subplot)+'</span><span class="chip">'+esc(windowLabel(c.window))+'</span><span class="chip">'+esc(c.maturity.replaceAll("_"," "))+(c.inherited?" · inherited":"")+'</span></div><p>'+esc(c.why)+'</p>'+(c.open_clock?'<p class="hard-boundary"><b>Still open:</b> '+esc(c.open_clock)+'</p>':'')+'<div class="plot-poles"><div><div class="mini-label">Light</div><p>'+esc(r.poles.light)+'</p></div><div><div class="mini-label">Shadow</div><p>'+esc(r.poles.shadow)+'</p></div></div><div class="wave-actions">'+actions+'</div><div class="ethics">This is a timeline of events. A watch is one kind of event, still unresolved. A node is not a ranking.</div>';
  }
  function selectPlotClock(id){
    var r=plotRoom(activePlot);if(!r||!findPlotClock(r,id))return;
    activeClock=id;
    document.querySelectorAll(".plot-node").forEach(function(node){node.classList.toggle("active",node.getAttribute("data-plot-clock")===id)});
    renderPlotInspector(r);
    var panel=document.getElementById("plotInspector");
    if(panel) panel.scrollIntoView({behavior:"smooth",block:"nearest"});
  }
  function renderPlotRail(){
    document.getElementById("plotTitle").textContent=plotData.title||"By plot";
    document.getElementById("plotDek").textContent=plotData.dek||"";
    document.getElementById("plotRail").innerHTML=(plotData.rooms||[]).map(function(r){return '<button class="era-tab'+(r.plotline===activePlot?' active':'')+'" type="button" role="tab" aria-selected="'+(r.plotline===activePlot?'true':'false')+'" data-open-plot="'+esc(r.plotline)+'">'+esc(r.plotline)+'</button>'}).join("");
  }
  function renderPlot(id){
    var r=plotRoom(id)||(plotData.rooms||[])[0];if(!r)return;activePlot=r.plotline;setPlotSpan(r);activeClock=pickPlotClock(r);renderPlotRail();
    document.getElementById("plotKicker").textContent=r.clock_count+" events · "+r.subplots.length+" lanes · click any node";
    document.getElementById("plotRoomTitle").textContent=r.plotline;
    document.getElementById("plotRoomDek").textContent=r.dek||"";
    document.getElementById("plotQuestion").textContent=r.locked_question;
    renderPlotAxis();
    var today=todayISO();
    var todayHtml=(today>=PLOT_T0&&today<=PLOT_T1)?'<div class="plot-today-rail"><div class="plot-today" style="left:'+plotPct(today)+'%"><span>today</span></div></div>':"";
    document.getElementById("plotLanes").innerHTML=todayHtml+r.subplots.map(function(sub){
      var byDate={};
      (sub.clocks||[]).forEach(function(c){var k=c.date;(byDate[k]||(byDate[k]=[])).push(c)});
      var nodes=Object.keys(byDate).sort().map(function(date){
        var stack=byDate[date];
        return stack.map(function(c,i){return plotNodeHtml(c,stack.length>1,i)}).join("");
      }).join("");
      return '<div class="plot-lane"><div class="plot-lane-label"><b>'+esc(sub.subplot)+'</b><span>'+esc(sub.state.replaceAll("_"," "))+'</span></div><div class="plot-track"><div class="plot-track-bg">'+plotClimateBands()+'</div>'+nodes+'</div></div>';
    }).join("");
    renderPlotInspector(r);
  }
  function renderWaveRail(){
    document.getElementById("waveRail").innerHTML=(waveData.waves||[]).map(function(w){var scope=w.eo_scope||{},state=scope.coverage_state==="complete"?scope.available_count+" EOs":scope.available_count+" of "+scope.expected_count+" EOs in vault";return '<button class="wave-tab'+(w.id===activeWave?' active':'')+'" type="button" role="tab" aria-selected="'+(w.id===activeWave?'true':'false')+'" data-wave="'+esc(w.id)+'"><b>Wave '+esc(w.ordinal)+' · '+esc(w.title)+'</b><span>EO tranche · '+esc(fmt(scope.signed_from))+' → '+esc(fmt(scope.signed_through))+'<br>'+esc(state)+(w.status==="partial"?' · interim through '+esc(fmt(w.end.date)):'')+'</span></button>'}).join("");
  }
  function renderWaveArc(){
    var cross=waveData.cross_wave||{};
    document.getElementById("waveCrossThesis").textContent=cross.thesis||"";
    document.getElementById("waveAuthority").innerHTML=(waveData.authority_layers||[]).map(function(row){return '<div class="authority-layer"><b>'+esc(row.label)+'</b><span>'+esc(row.role)+'</span></div>'}).join("");
    document.getElementById("waveScope").innerHTML='<b>Coverage boundary:</b> '+esc(waveData.scope_statement||'')+' Open gaps: '+esc((waveData.coverage_gaps||[]).join(', '))+'.';
    document.getElementById("waveArc").innerHTML=(cross.sequence||[]).map(function(row,index){return '<button type="button" data-wave="'+esc(row.wave_id)+'"><b>'+esc(row.stage)+'</b><small>Wave '+esc(index+1)+'</small></button>'}).join("");
  }
  function renderWaveSidebar(w){
    var h=w.chart_hierarchy||{},scope=w.eo_scope||{},local=h.local_frame,missing=scope.missing_numbers||[],boundaries=scope.boundary_rows||[],coverage=scope.coverage_state==="complete"?'Complete local EO shelf':'Local EO gaps: '+missing.map(function(n){return 'EO '+n}).join(', '),boundaryNote=boundaries.length?'<p class="coverage gapped boundary-note"><b>Boundary object'+(boundaries.length===1?'':'s')+':</b> '+boundaries.map(function(row){var state=row.state||(row.missing?'missing locally':'date-only; exact side unresolved');return 'EO '+esc(row.number)+' · '+esc(state.replaceAll('_',' '))}).join('; ')+'</p>':'';
    document.getElementById("waveSidebar").innerHTML='<div class="wave-kicker">Wave '+esc(w.ordinal)+' · '+esc(w.status)+'</div><h3>EO tranche · '+esc(fmt(scope.signed_from))+' → '+esc(fmt(scope.signed_through))+'</h3><p><b>Astrology hearing:</b> '+esc(fmt(w.start.date))+' → '+esc(fmt(w.end.date))+(w.status==="partial"?' evidence cutoff':'')+'.</p><p><b>Roster:</b> EO '+esc(scope.expected_first)+'–'+esc(scope.expected_last)+' · '+esc(scope.expected_count)+' expected · '+esc(scope.available_count)+' available.</p><p><b>Count basis:</b> '+esc(scope.count_basis||'authored roster')+'.</p><p class="coverage '+(scope.coverage_state==="complete"?'':'gapped')+'">'+esc(coverage)+'</p>'+boundaryNote+'<div class="wave-actions">'+chartAuthorityAction(h.strict_governor,'Strict governor · '+h.strict_governor.label)+(local?chartAuthorityAction(local,'Local frame · '+local.label):'')+'<button type="button" data-wave-eos>Open EO tranche</button><button type="button" data-wave-doc="wave">Read full wave research</button></div><h3>Root</h3><p>'+esc(w.root_note)+'</p><h3>Slow movement</h3><p>'+esc(w.slow_movement)+'</p><div class="ethics"><b>Boundary rule:</b> '+esc(scope.scope_basis)+'. The EO/research tranche and the exact astrological hearing are shown separately; date-only orders are never promoted to an exact signing-time claim.</div>';
  }
  function renderWave(waveId){
    var w=waveById(waveId)||waveData.waves[0];if(!w)return;activeWave=w.id;renderWaveRail();renderWaveSidebar(w);
    var summary=w.summary||{},scope=w.eo_scope||{};
    var beats=(w.beats||[]).map(function(beat){var c=beat.chart||{},eclipse=c.eclipse?' · '+(c.eclipse.type||'eclipse')+' '+c.eclipse.family+' eclipse':'',count=c.kind==="new"?'<span class="beat-meta">'+esc(beat.eo_count||0)+' EO'+(beat.eo_count===1?'':'s')+' in chapter</span>':'<span class="beat-meta">'+esc(beat.role)+'</span>';return '<article class="beat-card"><div class="beat-head"><div><h4><button class="subplot-link" type="button" data-wave-chart="'+esc(c.chart_id)+'">'+esc(c.label)+'</button></h4><div class="meta">'+esc(c.sign)+' '+esc(deg(c.degree))+eclipse+' · '+esc(beat.role)+'</div></div>'+count+'</div><p>'+esc(beat.endorsement)+'</p>'+(beat.eo_numbers&&beat.eo_numbers.length?'<div class="eo-strip">'+eoButtons(beat.eo_numbers,8)+'</div>':'')+'</article>'}).join("");
    var evidence=(w.evidence||[]).map(function(item){var research=(item.research_ids||[]).map(function(id){return '<button type="button" data-research="'+esc(id)+'">Research · '+esc(id)+'</button>'}).join(""),missing=(item.eo_coverage&&item.eo_coverage.missing||[]);return '<article class="evidence-card"><div class="evidence-head"><h4>'+esc(item.claim)+'</h4><span class="beat-meta">'+esc(item.clock.replaceAll('_',' '))+' · '+esc(item.maturity)+'</span></div><p class="hard-boundary"><b>Hard boundary:</b> '+esc(item.hard_boundary)+'</p><div class="eo-strip">'+eoButtons(item.eo_numbers,8)+(missing.length?'<span class="coverage gapped">Missing locally: '+esc(missing.join(', '))+'</span>':'')+'</div><div class="wave-actions">'+research+'</div></article>'}).join("");
    var missingNote=scope.missing_numbers.length?'<div class="wave-panel"><div class="mini-label">Coverage gap is visible</div><p>The official working range expects '+esc(scope.expected_count)+' orders; '+esc(scope.available_count)+' are present in the local vault. Missing: '+esc(scope.missing_numbers.map(function(n){return 'EO '+n}).join(', '))+'. No missing order is silently treated as mapped evidence.</p></div>':'';
    var official=w.official_story?'<div class="wave-panel official-story"><div class="mini-label">Official seasonal weave remains above this layer</div><p><b>'+esc(w.official_story.label)+'</b><br>'+esc(w.official_story.role)+'</p><div class="wave-actions"><button type="button" data-reading="'+esc(w.official_story.reading_id)+'">Open official storyline weave</button></div></div>':'<div class="wave-panel"><div class="mini-label">Authority boundary</div><p>This is the EO maturity layer. It does not elect the season’s official story or replace the locked climate reading.</p></div>';
    document.getElementById("waveDetail").innerHTML='<div class="wave-kicker">EO maturity overlay · Wave '+esc(w.ordinal)+' · '+esc(w.status)+(w.status==="partial"?' through '+fmt(w.end.date):'')+'</div><h2>'+esc(w.title)+'</h2>'+official+'<p class="wave-thesis">'+esc(summary.working_synthesis)+'</p><div class="wave-grid"><div class="wave-panel"><div class="mini-label">Factual institutional movement</div><p>'+esc(summary.factual_movement)+'</p></div><div class="wave-panel"><div class="mini-label">Archetypal movement</div><p>'+esc(summary.archetypal_movement)+'</p></div></div><h3>The governing question</h3><div class="wave-panel"><p><b>'+esc(summary.governing_question)+'</b></p></div><div class="wave-grid" style="margin-top:10px"><div class="wave-panel"><div class="mini-label">Constructive pole</div><p>'+esc(summary.constructive)+'</p></div><div class="wave-panel"><div class="mini-label">Shadow pole</div><p>'+esc(summary.shadow)+'</p></div><div class="wave-panel"><div class="mini-label">Continuity is a result</div><p>'+esc(summary.continuity)+'</p></div>'+missingNote+'</div><h3>Lunar chapters and reveals</h3><div class="beat-list">'+beats+'</div><h3>What changed state by the evidence cutoff</h3><div class="evidence-list">'+evidence+'</div><h3>Handoff</h3><div class="wave-panel"><p>'+esc(summary.handoff)+'</p></div><div class="ethics"><b>Observation rule:</b> the ingress is climate, the New Moon opens a chapter, and a Full Moon reveals or harvests. These natural overlaps are unscored and non-causal. EO instruction, legal effect, operation, transaction, contest, reversal, and unchanged state remain separate clocks. This record-first retrospective layer cannot overwrite a Pass 1 or official storyline.</div>';
  }
  function cycleRoot(id){return (conjunction.roots||[]).find(function(x){return x.cycle_id===id})}
  function cycleGroup(id){return (conjunction.groups||[]).find(function(g){return (g.cycle_ids||[]).indexOf(id)>=0})}
  function pairLabel(row){return (row.pair||[]).join("–")}
  function renderEraTabs(){
    document.getElementById("eraTabs").innerHTML=(conjunction.groups||[]).map(function(g){return '<button class="era-tab'+(g.id===activeEra?' active':'')+'" type="button" role="tab" aria-selected="'+(g.id===activeEra?'true':'false')+'" data-era="'+esc(g.id)+'">'+esc(g.label)+' · '+esc(g.years)+'</button>'}).join("");
  }
  function renderRootDetail(root){
    if(!root)return;
    var o=root.orbital||{},g=o.geometry||{},a=o.active_aspect,n=o.exact_event_neighbors||{},prev=n.previous_major_exact||{},next=n.next_major_exact||{};
    var relation=a?'<b>'+esc(a.aspect_id)+' · '+esc(deg(a.orb_deg))+' '+esc(a.motion_state)+'</b>':'<b>No direct major aspect inside the project orb</b>';
    var passes=(root.passes||[]).map(function(p){return '<div class="seed-pass"><b>'+esc(exactUTC(p.utc))+'</b><br>'+esc(deg(p.degree_in_sign))+' '+esc(p.sign)+' · '+esc(p.relative_motion)+'<br>'+esc(p.independent_verification_status.replaceAll("_"," "))+'</div>'}).join("");
    document.getElementById("rootDetail").innerHTML='<div class="eyebrow">'+esc(root.seed_family_label)+' · ~'+esc(root.nominal_cycle_years)+' years</div><h3>'+esc(pairLabel(root))+'</h3><p class="lead">'+esc(root.archetype.summary)+'</p><div class="mini-label">The conjunction seed</div><div class="seed-passes">'+passes+'</div><div class="clock-now"><div><div class="mini-label">Where the seed has reached by '+esc((conjunction.as_of||"").slice(0,4))+'</div><p>'+esc(g.phase_name)+' / '+esc(g.phase_direction)+' · elongation '+esc(deg(g.elongation_deg))+'. '+relation+'</p></div><div><div class="mini-label">Exact chapter boundary</div><p>'+(prev.utc?'Previous '+esc(prev.aspect_id)+' '+esc(exactLocal(prev.utc))+'. ':'')+(next.utc?'Next '+esc(next.aspect_id)+' '+esc(exactLocal(next.utc))+'.':'No next exact boundary is present in the current catalog.')+'</p></div></div><div class="transition"><div><div class="mini-label">Constructive pole</div><p>'+esc(root.archetype.constructive)+'</p></div><div><div class="mini-label">Shadow pole</div><p>'+esc(root.archetype.shadow)+'</p></div></div><div class="proof-box"><div class="mini-label">The authority question carried through time</div><p>'+esc(root.archetype.authority_question)+'</p></div><div class="actions" style="margin-top:13px"><button class="action primary" type="button" data-open-clocks data-cycle="'+esc(root.cycle_id)+'">Open this Long Clock</button></div>';
  }
  function renderEra(){
    var group=(conjunction.groups||[]).find(function(g){return g.id===activeEra})||conjunction.groups[0];if(!group)return;
    activeEra=group.id;if((group.cycle_ids||[]).indexOf(activeRoot)<0)activeRoot=group.cycle_ids[0];
    document.getElementById("eraTheme").textContent=group.theme||"";
    document.getElementById("rootList").innerHTML=(group.cycle_ids||[]).map(function(id){var r=cycleRoot(id),g=(r.orbital||{}).geometry||{};return '<button class="root-card'+(id===activeRoot?' active':'')+'" type="button" data-cycle-root="'+esc(id)+'"><b>'+esc(pairLabel(r))+'</b><span>'+esc(r.seed_family_label)+'<br>Now: '+esc(g.phase_name)+' / '+esc(g.phase_direction)+'</span></button>'}).join("");
    renderRootDetail(cycleRoot(activeRoot));
  }
  function selectRoot(id){var group=cycleGroup(id);if(!group)return;activeRoot=id;activeEra=group.id;renderEraTabs();renderEra();document.getElementById("conjunctionRoots").scrollIntoView({behavior:"smooth",block:"start"})}
  function renderConjunctionMap(){
    if(!(conjunction.groups||[]).length)return;
    if(!conjunction.groups.some(function(g){return g.id===activeEra}))activeEra=conjunction.groups[0].id;
    document.getElementById("rootTitle").textContent=conjunction.title||"The conjunction roots";
    document.getElementById("rootDek").textContent=conjunction.dek||"";
    var window=conjunction.exact_window||{};document.getElementById("exactTitle").textContent=window.title||"Exact contacts";document.getElementById("exactNote").textContent=window.note||"";
    document.getElementById("exactRail").innerHTML=(window.events||[]).map(function(e){return '<button class="exact-event" type="button" data-cycle-root="'+esc(e.cycle_id)+'"><time>'+esc(fmt((e.utc||"").slice(0,10)))+'</time><b>'+esc(pairLabel(e))+'</b><span>'+esc((e.chapter_id||e.aspect_id||"").replaceAll("_"," "))+' · '+esc(e.phase_name)+' / '+esc(e.phase_direction)+'</span></button>'}).join("");
    renderEraTabs();renderEra();
  }
  function openSub(sub){post({action:"navigateTo",tab:sub})}
  function umbrella(id){return DATA.umbrellas.find(function(x){return x.cycle_id===id})}
  function umbrellaChips(ids){return (ids||[]).map(function(id){var u=umbrella(id);return u?'<button class="chip" type="button" data-umbrella="'+esc(id)+'">'+esc(u.label)+'</button>':''}).join("")}
  function textOf(row){
    var umbrellaText=(row.umbrella_ids||[]).map(function(id){var u=umbrella(id);return u?[u.label,u.current_note].join(" "):""});
    if(row.itemType==="anchor") return [row.title,row.authority_question,row.watch_for].concat(row.arcs||[],umbrellaText,(row.overlaps||[]).flatMap(function(x){return [x.plotline,x.subplot,x.why]})).join(" ").toLowerCase();
    return [row.label,row.detail,laneLabel[row.lane]].concat(umbrellaText).join(" ").toLowerCase();
  }
  function combined(){
    var rows=[];
    DATA.anchors.forEach(function(x){rows.push(Object.assign({itemType:"anchor"},x))});
    DATA.releases.forEach(function(x){rows.push(Object.assign({itemType:"release"},x))});
    rows.sort(function(a,b){return a.date.localeCompare(b.date)||(a.itemType==="anchor"?-1:1)});
    return rows;
  }
  function matches(row){
    var q=search.value.trim().toLowerCase();
    var f=filter==="all"||(filter==="astrology"&&row.itemType==="anchor")||(filter==="releases"&&row.itemType==="release")||(row.lane===filter);
    var u=!activeUmbrella||(row.umbrella_ids||[]).indexOf(activeUmbrella)>=0;
    return f&&u&&(!q||textOf(row).indexOf(q)>=0);
  }
  function kindLabel(a){
    if(a.chart_type==="ingress")return "Ingress · governing gate";
    var phase=a.chart_kind==="new"?"New Moon":"Full Moon";
    return phase+(a.eclipse?" · "+a.eclipse:"")+(a.degree!=null?" · "+a.degree+"° "+a.sign:"");
  }
  function renderNow(){
    var chapter=DATA.current_chapter||{}, phase=DATA.current_phase||{}, lin=phase.lineage||{}, america=DATA.america_hand||{};
    var cards=[
      ["Governing room","Cancer ingress","Mutable Aries expired; Cancer governs until the Libra ingress at "+exactLocal("2026-09-23T00:05:00Z")+"."],
      ["Lunar chapter",(chapter.eclipse?chapter.eclipse+" · ":"")+(chapter.degree!=null?chapter.degree+"° ":"")+(chapter.sign||""),"Opened "+exactLocal(chapter.exact_utc)+" · root "+(chapter.root||[]).join(" + ")+" · carries until "+exactLocal(chapter.governs_until_utc)+"."],
      ["Current phase strike",(phase.phase||"")+" · "+(phase.degree!=null?phase.degree+"° ":"")+(phase.sign||""),"Exact "+exactLocal(phase.exact_utc)+(lin.seed_date?" · harvesting the "+fmt(lin.seed_date)+" "+lin.seed_sign+" seed.":".")],
      ["916 America · daily hand",deg(america.degree)+" "+(america.sign||""),"The canonical daily JPL cache for "+fmt(america.date)+"; a moving America hand, not a dignity-bearing planet. The exact event charts own their individual seats and derivative turns."]
    ];
    document.getElementById("nowStack").innerHTML=cards.map(function(c,i){return '<article class="now-card"><div class="mini-label">'+esc(c[0])+'</div><h2>'+esc(c[1])+'</h2><p>'+esc(c[2])+'</p>'+(i===1?'<button class="subplot-link" type="button" data-reading="'+esc(chapter.reading_id)+'">Open chapter →</button>':i===3?'<button class="subplot-link" type="button" data-america-reading>Open Aug 20 context →</button>':'')+'</article>'}).join("");
  }
  function renderUmbrellaRail(){
    umbrellaRail.innerHTML='<button type="button" class="umbrella-card'+(!activeUmbrella?' active':'')+'" data-clear-umbrella><b>All umbrellas</b><span>Let every orbital field co-mingle across the full spine.</span></button>'+DATA.umbrellas.map(function(u){var g=u.orbital.geometry||{}, a=u.orbital.active_aspect;var clock=a?(a.aspect_id+" · "+deg(a.orb_deg)+" "+a.motion_state):(g.phase_name+" · no direct major aspect");return '<button type="button" class="umbrella-card'+(activeUmbrella===u.cycle_id?' active':'')+'" data-umbrella="'+esc(u.cycle_id)+'"><b>'+esc(u.label)+'</b><span>'+esc(u.cycle_id.replace("-","–"))+'<br>'+esc(clock)+'</span></button>'}).join("");
  }
  function renderUmbrella(u){
    var o=u.orbital,g=o.geometry||{},a=o.active_aspect,n=o.exact_event_neighbors||{}, prev=n.previous_same_chapter_exact||n.previous_major_exact||{}, next=n.next_same_chapter_exact||n.next_major_exact||{};
    var aspect=a?'<b>'+esc(a.aspect_id)+' · '+esc(deg(a.orb_deg))+' '+esc(a.motion_state)+'</b>':'<b>No direct major aspect inside the project orb</b>';
    var manifestations=u.manifestations.map(function(m){return '<article class="manifestation"><div class="mini-label">'+esc(m.state.replaceAll("_"," "))+'</div><h4><button type="button" data-plotline="'+esc(m.plotline)+'">'+esc(m.plotline)+'</button></h4><button class="subplot-link" type="button" data-subplot="'+esc(m.subplot)+'">'+esc(m.subplot)+' →</button><p>'+esc(m.function)+'</p></article>'}).join("");
    var carriers=u.carrier_reading_ids.map(function(id){var x=DATA.anchors.find(function(r){return r.reading_id===id});return x?'<button class="chip" type="button" data-open="'+esc(x.key)+'">'+esc(fmt(x.display_date))+' · '+esc(x.title.replace(" — A Reading",""))+'</button>':''}).join("");
    var watches=u.watch_ids.map(function(id){var x=DATA.releases.find(function(r){return r.key===id});return x?'<button class="chip" type="button" data-open="'+esc(x.key)+'">'+esc(fmt(x.date))+' · '+esc(x.label)+'</button>':''}).join("");
    detail.innerHTML='<div class="detail-inner"><div class="eyebrow">Planetary umbrella · orbital snapshot '+esc(exactLocal(u.as_of))+'</div><h2>'+esc(u.label)+'</h2><p class="lead">'+esc(u.archetype.summary)+'</p><div class="orbit-grid"><div class="proof-box"><div class="mini-label">Where the bodies are in the cycle</div><p>'+esc(u.cycle_id.replace("-","–"))+' · '+esc(g.phase_name)+' / '+esc(g.phase_direction)+'. '+aspect+(prev.utc?' Previous exact '+esc(exactLocal(prev.utc))+'.':'')+(next.utc?' Next exact '+esc(exactLocal(next.utc))+'.':'')+'</p></div><div class="proof-box"><div class="mini-label">Current distinction</div><p>'+esc(u.current_note)+(u.co_presence?' '+esc(u.co_presence)+'.':'')+'</p></div></div><h3>The archetypal question</h3><div class="proof-box"><p>'+esc(u.archetype.authority_question)+'</p></div><div class="transition"><div><div class="mini-label">Constructive pole</div><p>'+esc(u.archetype.constructive)+'</p></div><div><div class="mini-label">Shadow pole</div><p>'+esc(u.archetype.shadow)+'</p></div></div><div class="proof-box"><div class="mini-label">Continuity is also a result</div><p>'+esc(u.archetype.continuity)+'</p></div><h3>Current Chronicle manifestations</h3><div class="manifestations">'+manifestations+'</div><h3>Charts carrying this field</h3><div class="chips">'+carriers+'</div>'+(watches?'<h3>Awaited factual gates</h3><div class="chips">'+watches+'</div>':'')+'<div class="actions" style="margin-top:18px"><button class="action primary" type="button" data-open-clocks data-cycle="'+esc(u.cycle_id)+'">Open this Long Clock</button><button class="action" type="button" data-open-comparison>Compare carrier charts</button></div><div class="ethics"><b>Observation rule:</b> recurrence is continuity, not independent confirmation. These manifestations share an archetypal umbrella; they are not ranked, owned by the planet, or required to produce a literal event.</div></div>';
  }
  function renderTimeline(){
    var rows=combined().filter(matches), h="";
    rows.forEach(function(row){
      var on=row.key===activeKey?" active":"";
      if(row.itemType==="anchor"){
        h+='<button type="button" class="timeline-row anchor'+on+'" data-open="'+esc(row.key)+'"><span class="date">'+esc(fmt(row.display_date||row.date))+'</span><span class="node"></span><span><span class="row-title">'+esc(row.title.replace(" — A Reading",""))+'</span><span class="row-sub">'+esc(kindLabel(row))+'</span></span></button>';
      }else{
        h+='<button type="button" class="timeline-row release '+esc(row.lane)+on+'" data-open="'+esc(row.key)+'"><span class="date">'+esc(fmt(row.date))+'</span><span class="node"></span><span><span class="row-title">'+esc(row.label)+'</span><span class="row-sub">'+esc(laneLabel[row.lane])+'</span></span></button>';
      }
    });
    timeline.innerHTML=h||'<div class="empty">Nothing matches this filter.</div>';
  }
  function climateChips(c){
    var h='<button class="chip" type="button" data-reading="'+esc(c.governing_reading_id)+'">Governing: '+esc(c.governing)+'</button>';
    if(c.nested)h+='<button class="chip" type="button" data-reading="'+esc(c.nested_reading_id)+'">Nested: '+esc(c.nested)+'</button>';
    return h;
  }
  function familyHtml(m){
    if(!m)return "";
    var lineage=m.lineage_phase==="seed"?'A new Pessin seed begins here.':'Pessin Full-Moon harvest of the '+fmt(m.seed_date)+' '+m.seed_sign+' seed.';
    if(m.planted_subplot) lineage+=' The seed window was registered to “'+m.planted_subplot+'.”';
    return '<h3>Moon family context</h3><div class="family-grid"><div class="family-box"><div class="mini-label">Degree-band mood</div><p><b>'+esc(m.band)+'</b> · '+esc(m.band_range)+'. '+esc(m.band_description)+'</p></div><div class="family-box"><div class="mini-label">Pessin lineage</div><p>'+esc(lineage)+'</p></div></div>';
  }
  function nearbyReleases(a){
    var rows=DATA.releases.filter(function(r){return Math.abs(dayDiff(r.date,a.date))<=10});
    if(!rows.length)return "";
    return '<h3>Awaited releases and gates nearby</h3><div class="nearby">'+rows.map(function(r){return '<button type="button" data-open="'+esc(r.key)+'"><span class="nd">'+esc(fmt(r.date))+'<br>'+esc(laneLabel[r.lane])+'</span><span class="nt">'+esc(r.label)+'</span></button>'}).join("")+'</div>';
  }
  function americaHtml(a){
    var am=a.america;if(!am)return "";
    var topics=(am.topics||[]).map(function(t){return '<div class="family-box"><div class="mini-label">America’s turned '+ord(t.turned_house)+' · '+esc(t.label)+'</div><p><b>Radical '+ord(t.radical_house)+'</b> · '+esc(t.radical_meaning)+'. '+(t.occupants.length?'Occupied by '+esc(t.occupants.join(" + "))+'.':'No classical planet physically occupies the landed house; judge its ruler in the full reading.')+'</p></div>'}).join("");
    var condition=(am.steward_condition||[]).join(", ")||"no listed essential condition";
    return '<h3>916 America · one derivative turn</h3><div class="proof-box"><div class="mini-label">America’s seat and steward</div><p><b>'+esc(am.position)+' · radical '+ord(am.radical_house)+'.</b> Treat that occupied radical house as America’s turned 1st. '+esc(am.steward)+' stewards the whole American claim from '+esc(am.steward_sign)+' in the radical '+ord(am.steward_house)+' ('+esc(condition)+'). Capacity is not goodness; strain is not an automatic bad outcome.</p></div><div class="family-grid" style="margin-top:10px">'+topics+'</div>';
  }
  function renderAnchor(a){
    var eclipse=a.eclipse?'<span class="chip eclipse">'+esc(a.eclipse)+'</span>':"";
    var overlaps=(a.overlaps||[]).map(function(o){return '<article class="overlap"><h4><button type="button" data-plotline="'+esc(o.plotline)+'">'+esc(o.plotline)+'</button></h4><button class="subplot-link" type="button" data-subplot="'+esc(o.subplot)+'">'+esc(o.subplot)+' →</button><p>'+esc(o.why)+'</p></article>'}).join("");
    var arcs=(a.arcs||[]).map(function(x){return '<button class="chip arc" type="button" data-arc="'+esc(x)+'">'+esc(x)+'</button>'}).join("");
    var ingressAction=a.chart_type==="ingress"?'<button class="action" type="button" data-ingress="'+esc(a.ingress_key)+'">Open existing wheel</button>':'<button class="action" type="button" data-lunar="'+esc(a.date)+'">Open in Lunar Weather</button>';
    detail.innerHTML='<div class="detail-inner"><div class="eyebrow">'+esc(fmt(a.display_date||a.date))+' · '+esc(kindLabel(a))+'</div><h2>'+esc(a.title.replace(" — A Reading",""))+'</h2><div class="chips">'+climateChips(a.climate)+eclipse+umbrellaChips(a.umbrella_ids)+'</div><p class="lead">'+esc(a.authority_question)+'</p><p class="meta">Exact '+esc(exactLocal(a.exact_utc))+(a.root&&a.root.length?' · root '+esc(a.root.join(" + ")):'')+'</p><div class="actions"><button class="action primary" type="button" data-reading="'+esc(a.reading_id)+'">Open full reading</button>'+ingressAction+'<button class="action" type="button" data-day="'+esc(a.display_date||a.date)+'">That day</button></div><div class="transition"><div><div class="mini-label">From</div><p>'+esc(a.transition.from)+'</p></div><div><div class="mini-label">Toward</div><p>'+esc(a.transition.toward)+'</p></div></div><div class="proof-box"><div class="mini-label">What would synchronize</div><p>'+esc(a.watch_for)+'</p><div class="chips" style="margin-top:9px">'+arcs+'</div></div>'+americaHtml(a)+familyHtml(a.moon)+'<h3>Natural Chronicle manifestations</h3><div class="overlaps">'+overlaps+'</div>'+nearbyReleases(a)+'<div class="ethics"><b>Observation rule:</b> these are unranked archetypal hypotheses, not assigned outcomes. Shared timing or vocabulary is not cause; unchanged, failed, reversed, and unresolved remain valid. The full reading and existing wheel retain authority over the chart.</div></div>';
  }
  function renderRelease(r){
    var research=(r.research_ids||[]).map(function(id){return '<button class="action" type="button" data-research="'+esc(id)+'">Research Desk · '+esc(id)+'</button>'}).join("");
    var source=/^https?:/.test(r.source)?'<a class="action" href="'+esc(r.source)+'" target="_blank" rel="noopener">Official source ↗</a>':"";
    detail.innerHTML='<div class="detail-inner release-detail"><span class="lane">'+esc(laneLabel[r.lane])+'</span><div class="eyebrow" style="margin-top:8px">'+esc(fmt(r.date))+(r.approx?' · approximate':'')+'</div><h2>'+esc(r.label)+'</h2><div class="chips" style="margin-bottom:14px">'+umbrellaChips(r.umbrella_ids)+'</div><div class="release-box"><div class="mini-label">Canonical watch detail</div><p>'+esc(r.detail||"No additional detail is recorded in the current watch calendar.")+'</p></div><div class="actions" style="margin-top:16px">'+source+'<button class="action primary" type="button" data-day="'+esc(r.date)+'">Open that day</button>'+research+'</div><div class="ethics">Date, wording, and source are resolved directly from <b>watch_calendar.json</b>. The planetary umbrellas supply interpretive context but do not alter the factual release state.</div></div>';
  }
  function find(key){return combined().find(function(x){return x.key===key})}
  function open(key,scroll){
    var row=find(key);if(!row)return;activeKey=key;renderTimeline();
    if(row.itemType==="anchor")renderAnchor(row);else renderRelease(row);
    if(scroll){var el=timeline.querySelector('[data-open="'+key+'"]');if(el)el.scrollIntoView({behavior:"smooth",block:"center"})}
  }
  function focusNow(){var n=new Date(),pad=function(x){return String(x).padStart(2,"0")},today=n.getFullYear()+"-"+pad(n.getMonth()+1)+"-"+pad(n.getDate());var a=DATA.anchors.find(function(x){return x.date>=today})||DATA.anchors[DATA.anchors.length-1];if(a)open(a.key,true)}
  document.getElementById("patternNotes").innerHTML=DATA.pattern_notes.map(function(x){return '<div class="pattern">'+esc(x)+'</div>'}).join("");
  document.getElementById("waveMethod").textContent=(waveData.method||{}).reading_rule||"";
  renderWaveArc();
  document.addEventListener("click",function(event){
    var el=event.target.closest("[data-mode]");if(el){setMode(el.dataset.mode);return}
    el=event.target.closest("[data-open-plot]");if(el){activeClock="";setMode("plots");renderPlot(el.dataset.openPlot);return}
    el=event.target.closest("[data-plot-clock]");if(el){selectPlotClock(el.dataset.plotClock);return}
    el=event.target.closest("[data-plotline-map]");if(el){post({action:"navigateTo",tab:"obs-sm",plotline:el.dataset.plotlineMap});return}
    el=event.target.closest("[data-wave]");if(el){renderWave(el.dataset.wave);return}
    el=event.target.closest("[data-wave-chart]");if(el){post({action:"navigateTo",tab:"obs-cc",childAction:"openComparison",chartIds:[el.dataset.waveChart]});return}
    el=event.target.closest("[data-eo]");if(el){post({action:"navigateTo",tab:"obs-eo",eo:"EO "+el.dataset.eo});return}
    el=event.target.closest("[data-wave-eos]");if(el){var w=waveById(activeWave),first=w&&w.eo_scope?w.eo_scope.expected_first:"";post({action:"navigateTo",tab:"obs-eo",eo:first?"EO "+first:""});return}
    el=event.target.closest("[data-wave-doc]");if(el){var w=waveById(activeWave),path=el.dataset.waveDoc==="cross"?(waveData.cross_wave||{}).research_path:(w||{}).research_path;if(path){if(path.indexOf("03 - Astrology/Astrology Files/")===0)post({action:"navigateTo",tab:"astrology-reference-room",childAction:"openAstrologyDocument",path:path});else post({action:"goToResearchDocument",path:path});}return}
    el=event.target.closest("[data-open]");if(el){open(el.dataset.open,false);return}
    el=event.target.closest("[data-era]");if(el){activeEra=el.dataset.era;activeRoot="";renderEraTabs();renderEra();return}
    el=event.target.closest("[data-cycle-root]");if(el){selectRoot(el.dataset.cycleRoot);return}
    el=event.target.closest("[data-focus-now]");if(el){setMode("current");focusNow();return}
    el=event.target.closest("[data-clear-umbrella]");if(el){activeUmbrella="";renderUmbrellaRail();renderTimeline();focusNow();return}
    el=event.target.closest("[data-umbrella]");if(el){activeUmbrella=el.dataset.umbrella;renderUmbrellaRail();renderTimeline();renderUmbrella(umbrella(activeUmbrella));return}
    el=event.target.closest("[data-open-clocks]");if(el){post({action:"navigateTo",tab:"obs-dc",childAction:"openClock",cycle_id:el.dataset.cycle||activeUmbrella||DATA.umbrellas[0].cycle_id});return}
    el=event.target.closest("[data-open-comparison]");if(el){var ids=activeUmbrella?(umbrella(activeUmbrella).carrier_reading_ids||[]):[];post({action:"navigateTo",tab:"obs-cc",childAction:"openComparison",chartIds:ids.slice(0,4)});return}
    el=event.target.closest("[data-america-reading]");if(el){post({action:"navigateTo",tab:"obs-df",date:DATA.america_hand.date});return}
    el=event.target.closest("[data-filter]");if(el){filter=el.dataset.filter;document.querySelectorAll("[data-filter]").forEach(function(x){x.classList.toggle("active",x===el)});renderTimeline();return}
    el=event.target.closest("[data-reading]");if(el){var a=DATA.anchors.find(function(x){return x.reading_id===el.dataset.reading});openReading(el.dataset.reading,a?a.date:"");return}
    el=event.target.closest("[data-lunar]");if(el){post({action:"navigateTo",tab:"obs-lw",date:el.dataset.lunar});return}
    el=event.target.closest("[data-ingress]");if(el){post({action:"navigateTo",tab:"obs-ic",childAction:"selectIngress",id:el.dataset.ingress});return}
    el=event.target.closest("[data-open-sub]");if(el){openSub(el.dataset.openSub);return}
    el=event.target.closest("[data-day]");if(el){post({action:"navigateTo",tab:"obs-df",date:el.dataset.day});return}
    el=event.target.closest("[data-plotline]");if(el){if(plotRoom(el.dataset.plotline)){setMode("plots");renderPlot(el.dataset.plotline);return}post({action:"navigateTo",tab:"obs-sm",plotline:el.dataset.plotline});return}
    el=event.target.closest("[data-subplot]");if(el){post({action:"navigateTo",tab:"obs-sm",subplot:el.dataset.subplot});return}
    el=event.target.closest("[data-arc]");if(el){post({action:"navigateTo",tab:"obs-cm",arc:el.dataset.arc});return}
    el=event.target.closest("[data-research]");if(el){post({action:"goToResearch",id:el.dataset.research});return}
  });
  search.addEventListener("input",renderTimeline);
  window.addEventListener("message",function(event){var m=event.data||{};if(m.action==="setTheme"){document.documentElement.setAttribute("data-theme",m.theme==="dark"?"dark":"light")}else if(m.action==="openWave"&&m.id){setMode("waves");renderWave(m.id)}else if(m.action==="openPlot"&&(m.plotline||m.id)){setMode("plots");renderPlot(m.plotline||m.id)}else if((m.action==="goToDate"||m.action==="scrollToDate")&&m.date){var a=DATA.anchors.find(function(x){return x.date>=m.date})||DATA.anchors[DATA.anchors.length-1];if(a){setMode("current");open(a.key,true)}}});
  try{document.documentElement.setAttribute("data-theme",localStorage.getItem("f250-theme")||"light")}catch(_){}
  renderNow();renderConjunctionMap();renderUmbrellaRail();renderTimeline();renderWaveArc();renderWaveRail();renderWave(activeWave);focusNow();
})();
</script>
</body>
</html>
'''


def main() -> None:
    payload = build_payload()
    encoded = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    encoded = encoded.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    rendered = TEMPLATE.replace("__DATA__", encoded)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(rendered, encoding="utf-8")
    print(
        f"✓ Astrology Spine: {len(payload['anchors'])} chart anchors, "
        f"{len(payload['releases'])} awaited releases, "
        f"{len(payload['plot_rooms']['rooms'])} plot rooms → {OUT.relative_to(VAULT)}"
    )


if __name__ == "__main__":
    main()
