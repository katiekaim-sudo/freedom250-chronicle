#!/usr/bin/env python3
"""Build the registry-driven Freedom 250 Astrology Hub host.

The compatibility file remains ``Sky & Charts.html``. The registry below is the
sole governed inventory for the hub UI, child iframes, legacy routes, date
behavior, and shell-discovery payload. Keep those concerns together: a tool
cannot silently appear in one surface and disappear from another.

Examples:
    python3 build_sky_charts.py
    python3 build_sky_charts.py --output "/private/tmp/Sky & Charts.html"
    python3 build_sky_charts.py --source-dir "/path/to/Cross-cuts"
    python3 build_sky_charts.py --check --output "/path/to/Sky & Charts.html"
    python3 build_sky_charts.py --print-registry
"""

from __future__ import annotations

import argparse
import html
import json
import os
from pathlib import Path
import re
import sys
from typing import Any

from atomic_io import atomic_write_text


HOST_ID = "obs-sky"
OUTPUT_NAME = "Sky & Charts.html"
LAST_SUBVIEW_KEY = "f250-sky-last-subview"
THEME_KEY = "f250-theme"
HERE = Path(__file__).resolve().parent
VAULT_ROOT = HERE.parent
CROSS_CUTS_DIR = VAULT_ROOT / "04 - Synthesis" / "Cross-cuts"
PATTERN_ATLAS_PATH = HERE / "pattern_atlas_2026.json"
WHOLE_CHART_PACKET_INDEX_PATH = HERE / "whole_chart_packet_index.json"
PATTERN_ATLAS_DOCUMENT = (
    "03 - Astrology/Astrology Files/"
    "Working Papers — Sept 2026/"
    "2026 PATTERN ATLAS — REORIENTATION MAP.md"
)

THESIS_DOCUMENT = (
    "03 - Astrology/Astrology Files/The Sky We're Living Through/"
    "THE SKY WE'RE LIVING THROUGH — 2020s Thesis.md"
)

CORRECTION_LABELS = {
    "holds": "Holds",
    "holds_as_rhythm": "Holds · rhythm",
    "holds_with_corrected_clocks": "Holds · clocks corrected",
    "strengthened": "Strengthened",
    "mostly_ordinary": "Mostly ordinary",
    "new": "New · 2020s thesis",
}

SECTIONS: tuple[dict[str, str], ...] = (
    {
        "id": "orientation",
        "label": "Start Here",
        "description": "Orient the present sky, the intact chart, and the pattern through time.",
    },
    {
        "id": "sky",
        "label": "Present Sky",
        "description": "The living sky — calendar, moon, slow-planet weather, and the watchlist.",
    },
    {
        "id": "chart-library",
        "label": "Chart Library",
        "description": "Canonical mundane, national, world, and personal charts.",
    },
    {
        "id": "workbench",
        "label": "Workbench",
        "description": "Compute, compare, locate, and turn a chart.",
    },
    {
        "id": "readings-files",
        "label": "Readings & Files",
        "description": "Authored readings and forecasts, plus the astrology reference files.",
    },
)

# SINGLE GOVERNED SUBVIEW REGISTRY.
# `legacy_views` preserves old shell routes. The first entry is canonical for
# favorites/recents and hostSubChanged. `date_action` is the message understood
# by that child when the shell's global date changes.
SUBVIEWS: tuple[dict[str, Any], ...] = (
    {
        "sub": "astrology-hub",
        "label": "Astrology Hub",
        "section": "orientation",
        "filename": None,
        "legacy_views": ("obs-sky-home",),
        "aliases": (
            "astrology", "astrology home", "astrology hub home", "start here",
            "orientation", "whole chart", "pattern atlas",
        ),
        "date_action": None,
        "description": "Begin with the present sky, one intact chart, and the pattern through time.",
    },
    {
        "sub": "sky-calendar",
        "label": "Sky Calendar",
        "section": "sky",
        # Wrapper hosting Calendar.html + Almanac.html (absorbs `almanac`).
        "filename": "Sky Calendar.html",
        "legacy_views": ("obs-cal", "obs-al"),
        "aliases": (
            "calendar", "month", "monthly sky", "the sky calendar",
            "almanac", "daybreak almanac", "day", "daily sky", "ephemeris",
            "daybreak", "sun asc", "sunrise",
            "Calendar.html", "Almanac.html",
        ),
        "date_action": "goToDate",
        "description": "Month grid ↔ any day's full sky",
    },
    {
        "sub": "lunar-weather",
        "label": "Moon & Eclipses",
        "section": "sky",
        # Wrapper hosting Lunar Weather.html + Moon Families.html
        # (absorbs `moon-families`).
        "filename": "Moon & Eclipses.html",
        "legacy_views": ("obs-lw", "obs-mf"),
        "aliases": (
            "lunations", "moon weather", "new moon", "full moon", "lunar weather",
            "moon-families", "moon families", "lunar families", "gestation", "pessin",
            "Lunar Weather.html", "Moon Families.html",
        ),
        "date_action": "scrollToDate",
        "description": "Every lunation and eclipse, plus the families timeline",
    },
    {
        "sub": "transit-weather",
        "label": "Transits & Cycles",
        "section": "sky",
        # Wrapper hosting Transit Weather.html + Deep Currents.html + Live Orrery.html
        # (absorbs `deep-currents`; the Orrery remains a child, not a new host row).
        "filename": "Transits & Cycles.html",
        "legacy_views": ("obs-tw", "obs-dc"),
        "aliases": (
            "transits", "weather", "planetary weather", "transit weather",
            "deep-currents", "deep currents", "outer planets", "slow sky",
            "era weather", "synodic cycles", "long clocks", "the long clocks",
            "orrery", "live orrery", "planetary motion", "ongoing planetary world",
            "Transit Weather.html", "Deep Currents.html", "Live Orrery.html",
        ),
        "date_action": "scrollToDate",
        "description": "Planetary weather, long clocks, and the moving solar system",
    },
    {
        "sub": "astrology-spine",
        "label": "Sky Watchlist",
        "section": "sky",
        "filename": "Astrology Spine.html",
        "legacy_views": ("obs-as",),
        "aliases": (
            "astrology spine", "forecast spine", "astrology timeline",
            "prospective timeline", "overlap map", "institutional waves",
            "regime waves", "executive order astrology", "eo spine",
        ),
        "date_action": "goToDate",
        "description": "What's coming and what hasn't resolved yet",
    },
    {
        "sub": "ingress-charts",
        "label": "Ingress Charts",
        "section": "chart-library",
        "filename": "Ingress Charts.html",
        "legacy_views": ("obs-ic",),
        "aliases": ("ingresses", "mundane ingresses", "aries ingress"),
        "date_action": None,
        "description": "Seasonal mundane charts and their overlays.",
    },
    {
        "sub": "american-charts",
        "label": "The US Chart",
        "section": "chart-library",
        # Wrapper hosting The American Charts.html + US Time Machine.html
        # (absorbs `us-time-machine`).
        "filename": "The US Chart.html",
        "legacy_views": ("obs-ac", "obs-tm"),
        "aliases": (
            "america charts", "us charts", "united states charts", "american charts",
            "us-time-machine", "us time machine", "time machine", "us history",
            "generational clock",
            "The American Charts.html", "US Time Machine.html",
        ),
        "date_action": None,
        "description": "The canonical national-chart library, plus the U.S. chart at any historical date.",
    },
    {
        "sub": "world-charts",
        "label": "World Charts",
        "section": "chart-library",
        "filename": "The World Charts.html",
        "legacy_views": ("obs-wc",),
        "aliases": ("country charts", "mundane charts", "global charts"),
        "date_action": None,
        "description": "Country and world-entity chart library.",
    },
    {
        "sub": "katies-sky",
        "label": "My Chart",
        "section": "chart-library",
        "filename": "Katies Sky.html",
        "legacy_views": ("obs-kk", "obs-ks"),
        "aliases": ("katie", "personal sky", "natal", "my sky", "katie's sky", "katies sky"),
        "date_action": "goToDate",
        "description": "Katie's personal astrology, kept visibly distinct.",
    },
    {
        "sub": "chart-comparison",
        "label": "Chart Comparison",
        "section": "workbench",
        "filename": "Chart Comparison.html",
        "legacy_views": ("obs-cc",),
        "aliases": ("comparison", "synastry", "multi-ring", "chart overlays"),
        "date_action": "goToDate",
        "description": "Compare four charts under one explicit house frame.",
    },
    {
        "sub": "astro-map",
        "label": "Astro Map",
        "section": "workbench",
        "filename": "Astro Map.html",
        "legacy_views": ("obs-am",),
        "aliases": ("map", "astrocartography", "chart map"),
        "date_action": None,
        "description": "Explore calculated AC/DC/MC/IC chart lines, overlays, and eclipse geography on a rotatable full Earth.",
    },
    {
        "sub": "derivative-houses",
        "label": "Derivative Houses",
        "section": "workbench",
        "filename": "Derivative Houses.html",
        "legacy_views": ("obs-dh",),
        "aliases": ("turned houses", "mundane dictionary", "houses"),
        "date_action": None,
        "description": "Turn the chart from an actor or institutional house.",
    },
    {
        "sub": "chart-readings",
        "label": "Chart Readings",
        "section": "readings-files",
        # Wrapper hosting Chart Readings.html + Readings & Predictions.html
        # (absorbs `readings-predictions`).
        "filename": "Readings.html",
        "legacy_views": ("obs-cr", "obs-rp"),
        "aliases": (
            "readings", "pass 1", "weaves", "interpretations", "chart interpretations",
            "readings-predictions", "readings & predictions", "predictions",
            "forecasts", "dated readings", "forecast synthesis", "saved readings",
            "outcome review",
            "Chart Readings.html", "Readings & Predictions.html",
        ),
        "date_action": "goToDate",
        "description": (
            "Aster readings, record censuses, and storyline comparisons, plus dated "
            "authored synthesis, conditional forecasts, and exact scored calls."
        ),
    },
    {
        "sub": "astrology-reference-room",
        "label": "Astrology Files",
        "section": "readings-files",
        "filename": "Astrology Reference Room.html",
        "legacy_views": ("obs-arr",),
        "aliases": (
            "astrology files", "astrology reference", "astrology reference room", "astrology methods",
            "astrology experiments", "persona hearings", "mundane astrology organism",
        ),
        "date_action": None,
        "description": (
            "The Chronicle-owned home for astrology methods, chart experiments, "
            "persona work and interpretive overlays. It is its own astrology collection, "
            "not government Research or a research reference shelf."
        ),
    },
)

# Every route retired by a merge preserves both the surviving host row and the
# requested inner wrapper subview. Without `inner_sub`, legacy routes collapse
# to the wrapper's first tab and silently open the wrong instrument.
ABSORBED_ROUTES: dict[str, dict[str, str]] = {
    "almanac": {"survivor": "sky-calendar", "inner_sub": "almanac"},
    "obs-al": {"survivor": "sky-calendar", "inner_sub": "almanac"},
    "obs-cal": {"survivor": "sky-calendar", "inner_sub": "calendar"},
    "moon-families": {"survivor": "lunar-weather", "inner_sub": "moon-families"},
    "obs-mf": {"survivor": "lunar-weather", "inner_sub": "moon-families"},
    "obs-lw": {"survivor": "lunar-weather", "inner_sub": "lunar-weather"},
    "deep-currents": {"survivor": "transit-weather", "inner_sub": "deep-currents"},
    "obs-dc": {"survivor": "transit-weather", "inner_sub": "deep-currents"},
    "obs-tw": {"survivor": "transit-weather", "inner_sub": "transit-weather"},
    "us-time-machine": {"survivor": "american-charts", "inner_sub": "us-time-machine"},
    "obs-tm": {"survivor": "american-charts", "inner_sub": "us-time-machine"},
    "obs-ac": {"survivor": "american-charts", "inner_sub": "american-charts"},
    "readings-predictions": {"survivor": "chart-readings", "inner_sub": "readings-predictions"},
    "obs-rp": {"survivor": "chart-readings", "inner_sub": "readings-predictions"},
    "obs-cr": {"survivor": "chart-readings", "inner_sub": "chart-readings"},
}


def fail(message: str) -> None:
    raise SystemExit(f"Astrology Hub build FAILED: {message}")


def validate_registry(source_dir: Path | None = None) -> None:
    expected_sections = [row["id"] for row in SECTIONS]
    section_ids = set(expected_sections)
    if len(section_ids) != len(expected_sections):
        fail("duplicate section id")

    seen_subs: set[str] = set()
    seen_legacy: set[str] = set()
    seen_files: set[str] = set()
    for index, tool in enumerate(SUBVIEWS):
        required = {
            "sub",
            "label",
            "section",
            "filename",
            "legacy_views",
            "aliases",
            "date_action",
            "description",
        }
        missing = required.difference(tool)
        if missing:
            fail(f"registry row {index} lacks {', '.join(sorted(missing))}")

        sub = tool["sub"]
        if not isinstance(sub, str) or not sub or sub != sub.lower():
            fail(f"invalid stable sub id: {sub!r}")
        if sub in seen_subs:
            fail(f"duplicate sub id: {sub}")
        seen_subs.add(sub)

        if tool["section"] not in section_ids:
            fail(f"{sub} names unknown section {tool['section']!r}")
        filename = tool["filename"]
        if filename is None:
            if sub != "astrology-hub":
                fail(f"only astrology-hub may use the native host view")
        else:
            if not str(filename).endswith(".html"):
                fail(f"{sub} filename is not HTML")
            if filename in seen_files:
                fail(f"duplicate iframe target: {filename}")
            seen_files.add(filename)

        legacy_views = tool["legacy_views"]
        if not legacy_views or not all(
            isinstance(item, str) and item.startswith("obs-")
            for item in legacy_views
        ):
            fail(f"{sub} must have at least one obs-* legacy route")
        for legacy in legacy_views:
            if legacy in seen_legacy:
                fail(f"duplicate legacy route: {legacy}")
            seen_legacy.add(legacy)

        if tool["date_action"] not in {None, "goToDate", "scrollToDate"}:
            fail(f"{sub} has unsupported date action {tool['date_action']!r}")

        if source_dir is not None and filename is not None and not (source_dir / filename).is_file():
            fail(f"missing child view: {source_dir / filename}")

    used_sections = {tool["section"] for tool in SUBVIEWS}
    if used_sections != section_ids:
        fail(
            "empty or unused sections: "
            + ", ".join(sorted(section_ids.symmetric_difference(used_sections)))
        )

    by_sub = {tool["sub"]: tool for tool in SUBVIEWS}
    for route, spec in ABSORBED_ROUTES.items():
        if set(spec) != {"survivor", "inner_sub"}:
            fail(f"absorbed route {route!r} must name survivor and inner_sub")
        survivor_sub = spec["survivor"]
        inner_sub = spec["inner_sub"]
        survivor = by_sub.get(survivor_sub)
        if survivor is None:
            fail(f"absorbed route {route!r} names missing survivor {survivor_sub!r}")
        if route.startswith("obs-"):
            if route not in survivor["legacy_views"]:
                fail(f"legacy route {route!r} must survive on {survivor_sub}.legacy_views")
        elif route != survivor_sub and route not in survivor["aliases"]:
            fail(f"retired sub id {route!r} must survive on {survivor_sub}.aliases")
        if inner_sub != survivor_sub and inner_sub not in survivor["aliases"]:
            fail(f"absorbed route {route!r} has undeclared inner_sub {inner_sub!r}")


def shell_registry() -> list[dict[str, Any]]:
    """Return the public, serializable registry consumed by the shell."""
    section_labels = {row["id"]: row["label"] for row in SECTIONS}
    tools: list[dict[str, Any]] = []
    for tool in SUBVIEWS:
        tools.append(
            {
                "id": tool["legacy_views"][0],
                "host": HOST_ID,
                "sub": tool["sub"],
                "legacyView": tool["legacy_views"][0],
                "legacyViews": list(tool["legacy_views"]),
                "label": tool["label"],
                "section": section_labels[tool["section"]],
                "sectionId": tool["section"],
                "filename": tool["filename"],
                "aliases": list(tool["aliases"]),
                "absorbedRoutes": {
                    route: spec["inner_sub"]
                    for route, spec in ABSORBED_ROUTES.items()
                    if spec["survivor"] == tool["sub"]
                },
                "dateAction": tool["date_action"],
                "description": tool["description"],
            }
        )
    return tools


def js_safe_json(value: Any, *, indent: int | None = None) -> str:
    # Prevent a future registry label from terminating its JSON script element.
    return (
        json.dumps(value, ensure_ascii=False, indent=indent, separators=None if indent else (",", ":"))
        .replace("&", "\\u0026")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


def build_sections() -> str:
    blocks: list[str] = []
    for section in SECTIONS:
        buttons: list[str] = []
        for tool in (row for row in SUBVIEWS if row["section"] == section["id"]):
            haystack = " ".join(
                (
                    tool["label"],
                    tool["description"],
                    *tool["aliases"],
                    *tool["legacy_views"],
                )
            ).lower()
            buttons.append(
                f"""          <button class="sky-tool" type="button"
            data-sky-id="{html.escape(tool['sub'], quote=True)}"
            data-search="{html.escape(haystack, quote=True)}"
            aria-controls="sky-view-{html.escape(tool['sub'], quote=True)}">
            <span class="sky-tool-name">{html.escape(tool['label'])}</span>
            <span class="sky-tool-desc">{html.escape(tool['description'])}</span>
          </button>"""
            )
        blocks.append(
            f"""        <section class="sky-section" data-section="{html.escape(section['id'], quote=True)}">
          <h2>{html.escape(section['label'])}</h2>
          <p>{html.escape(section['description'])}</p>
          <div class="sky-tool-list">
{os.linesep.join(buttons)}
          </div>
        </section>"""
        )
    return os.linesep.join(blocks)


def load_pattern_atlas() -> dict[str, Any]:
    if not PATTERN_ATLAS_PATH.is_file():
        fail(f"missing Pattern Atlas projection: {PATTERN_ATLAS_PATH}")
    try:
        atlas = json.loads(PATTERN_ATLAS_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read Pattern Atlas projection: {exc}")
    if atlas.get("schema") != "freedom250.pattern-atlas-2026/v1":
        fail("unsupported Pattern Atlas schema")
    routes = atlas.get("priority_synthesis_routes")
    patterns = atlas.get("pattern_records")
    if not isinstance(routes, list) or not routes:
        fail("Pattern Atlas has no priority synthesis routes")
    if not isinstance(patterns, list) or not patterns:
        fail("Pattern Atlas has no pattern records")
    return atlas


def load_whole_chart_packet_index() -> dict[str, Any]:
    if not WHOLE_CHART_PACKET_INDEX_PATH.is_file():
        fail(f"missing whole-chart packet index: {WHOLE_CHART_PACKET_INDEX_PATH}")
    try:
        packet_index = json.loads(WHOLE_CHART_PACKET_INDEX_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read whole-chart packet index: {exc}")
    if packet_index.get("schema") != "freedom250.whole-chart-packet-index/v1":
        fail("unsupported whole-chart packet index schema")
    packets = packet_index.get("packets")
    if not isinstance(packets, list) or len(packets) != 30:
        fail("whole-chart packet index must expose exactly 30 registered packets")
    return packet_index


def build_priority_routes(atlas: dict[str, Any]) -> str:
    patterns = {
        row.get("pattern_id"): row
        for row in atlas["pattern_records"]
        if isinstance(row, dict) and row.get("pattern_id")
    }
    cards: list[str] = []
    for route in sorted(atlas["priority_synthesis_routes"], key=lambda row: row["priority"]):
        pattern_refs = route.get("pattern_refs") or []
        primary = patterns.get(pattern_refs[0]) if pattern_refs else None
        documents = primary.get("companion_refs") if primary else None
        document = route.get("document_ref") or (documents[0] if documents else PATTERN_ATLAS_DOCUMENT)
        steps = "".join(
            f"<li>{html.escape(str(step))}</li>"
            for step in (route.get("next_work") or [])
        )
        cards.append(
            f"""          <article class="hub-route">
            <div class="hub-route-kicker">Priority {int(route['priority'])}</div>
            <h3>{html.escape(route['question'])}</h3>
            <ol>{steps}</ol>
            <button class="hub-link" type="button" data-open-document="{html.escape(document, quote=True)}">Open the route packet</button>
          </article>"""
        )
    return os.linesep.join(cards)


def build_pattern_strip(atlas: dict[str, Any]) -> str:
    cards: list[str] = []
    for record in atlas["pattern_records"]:
        correction = record.get("correction_2026_09_25") or {}
        status = str(correction.get("status", ""))
        label = CORRECTION_LABELS.get(status, status.replace("_", " ").capitalize())
        refs = record.get("companion_refs") or []
        document = refs[0] if refs else PATTERN_ATLAS_DOCUMENT
        cards.append(
            f"""          <button class="hub-pattern" type="button" data-open-document="{html.escape(document, quote=True)}">
            <em data-status="{html.escape(status, quote=True)}">{html.escape(label)}</em>
            <strong>{html.escape(record['title'])}</strong>
            <span>{html.escape(str(correction.get('note', record.get('next_question', ''))))}</span>
          </button>"""
        )
    return os.linesep.join(cards)


def build_packet_shelf(packet_index: dict[str, Any]) -> str:
    packets_by_group: dict[str, list[dict[str, Any]]] = {}
    for packet in packet_index["packets"]:
        packets_by_group.setdefault(packet["packet_group"], []).append(packet)
    groups: list[str] = []
    for position, group in enumerate(packet_index["groups"]):
        packet_rows = packets_by_group.get(group["group_id"], [])
        buttons: list[str] = []
        for packet in packet_rows:
            state = packet["knowledge_state_at_cutoff"]
            state_label = "Prospective at cutoff" if state == "prospective" else "Occurred by cutoff"
            buttons.append(
                f"""              <button class="hub-packet" type="button"
                data-open-reading="{html.escape(packet['chart_id'], quote=True)}">
                <strong>{html.escape(packet['label'])}</strong>
                <span>{html.escape(packet['display_kind'])} · {html.escape(packet['exact_clock']['local'][:10])}</span>
                <em data-state="{html.escape(state, quote=True)}">{state_label}</em>
              </button>"""
            )
        open_attr = " open" if position == 0 else ""
        groups.append(
            f"""          <details class="hub-packet-group"{open_attr}>
            <summary><span>{html.escape(group['label'])}</span><strong>{int(group['packet_count'])}</strong></summary>
            <div class="hub-packet-grid">
{os.linesep.join(buttons)}
            </div>
          </details>"""
        )
    return os.linesep.join(groups)


def build_hub_home(atlas: dict[str, Any], packet_index: dict[str, Any]) -> str:
    summary = atlas["coverage_summary"]
    developed_through = html.escape(str(atlas.get("developed_through", "unknown")))
    orientation_document = html.escape(PATTERN_ATLAS_DOCUMENT, quote=True)
    thesis_document = html.escape(THESIS_DOCUMENT, quote=True)
    hub_packets = [
        {
            "chartId": packet["chart_id"],
            "label": packet["label"],
            "kind": packet["display_kind"],
            "group": packet["packet_group"],
            "utc": packet["exact_clock"]["utc"],
            "local": packet["exact_clock"]["local"],
        }
        for packet in packet_index["packets"]
    ]
    hub_packets_json = js_safe_json(hub_packets)
    return f"""      <section class="sky-view hub-view" id="sky-view-astrology-hub"
        data-sky-id="astrology-hub" role="region" aria-label="Astrology Hub" hidden>
        <div class="hub-scroll">
          <section class="hub-front" aria-labelledby="hub-front-title">
            <div class="hub-kicker">The corrected pattern routes · {developed_through}</div>
            <h1 id="hub-front-title">Where the sky's story stands</h1>
            <p class="hub-front-deck">Start with what already happened, then what is live, then what is building. Every clock here was recomputed on the JPL DE441 ephemeris (DR-080); patterns that did not survive were retired, and patterns that are merely built into the geometry are marked ordinary.</p>
            <div class="hub-link-row hub-front-links">
              <button class="hub-primary" type="button" data-open-document="{thesis_document}">Read the 2020s thesis</button>
              <button class="hub-link" type="button" data-open-document="{orientation_document}">Codex's Pattern Atlas (working paper)</button>
            </div>
            <div class="hub-route-grid hub-front-routes">
{build_priority_routes(atlas)}
            </div>
            <div class="hub-pattern-strip" aria-label="Pattern records and their correction status">
{build_pattern_strip(atlas)}
            </div>
          </section>
          <header class="hub-orrery" data-hub-mode="sky" aria-labelledby="hub-live-title">
            <div class="hub-stars" aria-hidden="true"></div>
            <div class="hub-live-top">
              <div class="hub-live-brand"><span aria-hidden="true"></span><strong>The living sky</strong></div>
              <div class="hub-mode-nav" role="group" aria-label="Astrology Hub view">
                <button type="button" data-hub-mode-button="sky" aria-pressed="true">Live sky</button>
                <button type="button" data-hub-mode-button="story" aria-pressed="false">Storylines</button>
                <button type="button" data-hub-mode-button="explore" aria-pressed="false">Explore</button>
              </div>
              <div class="hub-live-clock"><strong id="hub-live-date">Today</strong><span>Washington, D.C.</span></div>
            </div>
            <div class="hub-live-intro">
              <div class="hub-live-eyebrow" id="hub-live-eyebrow">The sky right now</div>
              <h1 id="hub-live-title">What is moving?</h1>
              <p id="hub-live-deck">Begin with the whole sky. Touch a planet in the living solar system, follow a relationship, then open the exact Earth-centered chart when you want the particulars.</p>
            </div>
            <div class="hub-system-wrap">
              <div class="hub-solar-system" role="img" aria-label="Slow schematic solar system; open Planetary Motion for exact date-driven positions">
                <span class="hub-orbit o1" aria-hidden="true"></span>
                <span class="hub-orbit o2" aria-hidden="true"></span>
                <span class="hub-orbit o3" aria-hidden="true"></span>
                <span class="hub-orbit o4" aria-hidden="true"></span>
                <span class="hub-orbit o5" aria-hidden="true"></span>
                <span class="hub-orbit o6" aria-hidden="true"></span>
                <span class="hub-orbit o7" aria-hidden="true"></span>
                <span class="hub-orbit o8" aria-hidden="true"></span>
                <button class="hub-sun" type="button" data-hub-body="Sun" aria-label="Sun"><span>Sun</span></button>
                <span class="hub-carrier c-mercury" style="--angle:202deg;--neg-angle:-202deg;--dur:380s"><button class="hub-body" type="button" data-hub-body="Mercury" aria-label="Mercury"><span class="hub-planet mercury"></span><span class="hub-planet-label">Mercury</span></button></span>
                <span class="hub-carrier c-venus" style="--angle:325deg;--neg-angle:-325deg;--dur:500s"><button class="hub-body" type="button" data-hub-body="Venus" aria-label="Venus"><span class="hub-planet venus"></span><span class="hub-planet-label">Venus</span></button></span>
                <span class="hub-carrier c-earth" style="--angle:301deg;--neg-angle:-301deg;--dur:640s"><button class="hub-body is-selected" type="button" data-hub-body="Earth" aria-label="Earth and Moon"><span class="hub-planet earth"><i aria-hidden="true"></i></span><span class="hub-planet-label">Earth + Moon</span></button></span>
                <span class="hub-carrier c-mars" style="--angle:163deg;--neg-angle:-163deg;--dur:780s"><button class="hub-body" type="button" data-hub-body="Mars" aria-label="Mars"><span class="hub-planet mars"></span><span class="hub-planet-label">Mars</span></button></span>
                <span class="hub-carrier c-jupiter" style="--angle:201deg;--neg-angle:-201deg;--dur:1100s"><button class="hub-body" type="button" data-hub-body="Jupiter" aria-label="Jupiter"><span class="hub-planet jupiter"></span><span class="hub-planet-label">Jupiter</span></button></span>
                <span class="hub-carrier c-saturn" style="--angle:312deg;--neg-angle:-312deg;--dur:1400s"><button class="hub-body" type="button" data-hub-body="Saturn" aria-label="Saturn"><span class="hub-planet saturn"></span><span class="hub-planet-label">Saturn</span></button></span>
                <span class="hub-carrier c-uranus" style="--angle:224deg;--neg-angle:-224deg;--dur:1680s"><button class="hub-body" type="button" data-hub-body="Uranus" aria-label="Uranus"><span class="hub-planet uranus"></span><span class="hub-planet-label">Uranus</span></button></span>
                <span class="hub-carrier c-neptune" style="--angle:326deg;--neg-angle:-326deg;--dur:1960s"><button class="hub-body" type="button" data-hub-body="Neptune" aria-label="Neptune"><span class="hub-planet neptune"></span><span class="hub-planet-label">Neptune</span></button></span>
                <span class="hub-carrier c-pluto" style="--angle:15deg;--neg-angle:-15deg;--dur:2320s"><button class="hub-body" type="button" data-hub-body="Pluto" aria-label="Pluto"><span class="hub-planet pluto"></span><span class="hub-planet-label">Pluto</span></button></span>
                <span class="hub-relation hub-relation-one" aria-hidden="true"></span>
                <span class="hub-relation hub-relation-two" aria-hidden="true"></span>
              </div>
            </div>
            <aside class="hub-story-panel" aria-live="polite">
              <div class="hub-story-kicker" id="hub-story-kicker">Approaching chapter</div>
              <h2 id="hub-story-title">The next registered chart</h2>
              <p id="hub-story-text">The exact chart clock will appear here.</p>
              <div class="hub-story-meta"><span aria-hidden="true"></span><em id="hub-story-meta">One sky · several scales</em></div>
              <button class="hub-story-link" type="button" data-open-orrery>Open exact planetary motion</button>
            </aside>
            <div class="hub-entry-dock" aria-label="Primary Astrology Hub entries">
              <button class="hub-entry primary" type="button" data-hub-next-reading><strong>Enter this chart</strong><span>governor + exact whole-chart packet</span></button>
              <button class="hub-entry" type="button" data-open-orrery><strong>Turn the real sky</strong><span>date-driven Planetary Motion</span></button>
              <button class="hub-entry" type="button" data-scroll-explore><strong>Explore the library</strong><span>all charts, patterns and files</span></button>
            </div>
            <div class="hub-scale-note">Schematic scale and pace · exact positions live in Planetary Motion</div>
          </header>
          <script id="f250-hub-packets" type="application/json">{hub_packets_json}</script>

          <div class="hub-depth" id="hubExplore">

          <section class="hub-section" aria-labelledby="hub-three-scales">
            <div class="hub-section-head">
              <div>
                <div class="hub-kicker">The orientation</div>
                <h2 id="hub-three-scales">Three scales, one reading</h2>
              </div>
              <p>Do not stack isolated techniques. Move outward from the governed moment while keeping the chart whole.</p>
            </div>
            <div class="hub-scale-grid">
              <article class="hub-scale">
                <div class="hub-number">01</div>
                <h3>The present sky</h3>
                <p>Establish the governing ingress, lunation or eclipse chapter, exact relationships, stations, handoffs, and physical geometry.</p>
                <div class="hub-link-row">
                  <button class="hub-link" type="button" data-open-sub="sky-calendar">Sky Calendar</button>
                  <button class="hub-link" type="button" data-open-sub="lunar-weather">Moon &amp; Eclipses</button>
                  <button class="hub-link" type="button" data-open-sub="transit-weather">Transits &amp; Cycles</button>
                </div>
              </article>
              <article class="hub-scale">
                <div class="hub-number">02</div>
                <h3>The whole chart</h3>
                <p>Hold its exact clock, locality, house frame, angles, aspect web, distribution, dispositor root, declination, and reading together.</p>
                <div class="hub-link-row">
                  <button class="hub-link" type="button" data-open-sub="ingress-charts">Ingress Charts</button>
                  <button class="hub-link" type="button" data-open-sub="chart-readings">Chart Readings</button>
                  <button class="hub-link" type="button" data-open-sub="chart-comparison">Chart Comparison</button>
                </div>
              </article>
              <article class="hub-scale">
                <div class="hub-number">03</div>
                <h3>The pattern through time</h3>
                <p>Trace Moon families, synodic chapters, inherited conjunction radices, seed-degree relays, and astronomical motion without giving any one pattern an extra vote.</p>
                <div class="hub-link-row">
                  <button class="hub-link" type="button" data-open-document="{thesis_document}">2020s Thesis</button>
                  <button class="hub-link" type="button" data-open-document="{orientation_document}">Pattern Atlas</button>
                  <button class="hub-link" type="button" data-open-sub="astrology-spine">Sky Watchlist</button>
                  <button class="hub-link" type="button" data-open-sub="astrology-reference-room">Astrology Files</button>
                </div>
              </article>
            </div>
          </section>

          <section class="hub-section hub-reading-order" aria-labelledby="hub-reading-order">
            <div class="hub-section-head">
              <div>
                <div class="hub-kicker">Reading order</div>
                <h2 id="hub-reading-order">Five moves before judgment</h2>
              </div>
              <p>The hub is an orientation layer. It routes to the owners beneath it and creates no second chart or interpretation.</p>
            </div>
            <ol class="hub-steps">
              <li><strong>Name the governor.</strong><span>Ingress, lunar chapter, and the exact clock.</span></li>
              <li><strong>Read the whole chart.</strong><span>Angles, houses, relationships, root, shape, and declination in one frame.</span></li>
              <li><strong>Trace inheritance.</strong><span>Moon family, conjunction radix, seed degrees, and earlier chapter handoffs.</span></li>
              <li><strong>Add real motion.</strong><span>Stations, solar phase, heliocentric geometry, distance, and visibility as context.</span></li>
              <li><strong>Compare the world last.</strong><span>Join independently sourced political records only in an explicit comparison layer.</span></li>
            </ol>
          </section>

          <section class="hub-section" aria-labelledby="hub-whole-chart-packets">
            <div class="hub-section-head">
              <div>
                <div class="hub-kicker">Whole-chart entry</div>
                <h2 id="hub-whole-chart-packets">Choose one intact chart</h2>
              </div>
              <p>Each of the {int(packet_index['counts']['packet_count'])} packets preserves one exact chart and routes to its governor, lineage, synodic stack, physical motion, pattern studies, and authored reading.</p>
            </div>
            <div class="hub-packet-shelf">
{build_packet_shelf(packet_index)}
            </div>
          </section>

          <section class="hub-section hub-coverage" aria-labelledby="hub-coverage">
            <div class="hub-section-head">
              <div>
                <div class="hub-kicker">Coverage already in hand</div>
                <h2 id="hub-coverage">The system remembers the deep work</h2>
              </div>
              <p>Counts are read from the generated Pattern Atlas, never typed into the hub.</p>
            </div>
            <div class="hub-stat-grid">
              <div><strong>{int(summary['registered_2026_ingress_and_syzygy_charts'])}</strong><span>registered 2026 ingress and syzygy charts</span></div>
              <div><strong>{int(summary['full_moon_families'])}</strong><span>Full-Moon families</span></div>
              <div><strong>{int(summary['inner_planet_snapshots'])}</strong><span>inner-planet motion snapshots</span></div>
              <div><strong>{int(summary['outer_planet_snapshots'])}</strong><span>outer-planet geometry snapshots</span></div>
              <div><strong>{int(summary['coverage_domain_count'])}</strong><span>mapped analysis domains</span></div>
              <div><strong>{int(summary['pattern_record_count'])}</strong><span>cross-chart pattern records</span></div>
            </div>
          </section>

          <aside class="hub-boundary">
            <strong>Keep the lanes honest.</strong>
            <span>Computed sky, authored interpretation, prospective calls, and political evidence remain separate at the source. Their meeting belongs in a named comparison—not in an automatic score.</span>
          </aside>
          </div>
        </div>
      </section>"""


def build_views() -> str:
    atlas = load_pattern_atlas()
    packet_index = load_whole_chart_packet_index()
    blocks: list[str] = []
    for tool in SUBVIEWS:
        safe_sub = html.escape(tool["sub"], quote=True)
        if tool["filename"] is None:
            blocks.append(build_hub_home(atlas, packet_index))
            continue
        blocks.append(
            f"""      <section class="sky-view" id="sky-view-{safe_sub}"
        data-sky-id="{safe_sub}" role="region"
        aria-label="{html.escape(tool['label'], quote=True)}" hidden>
        <iframe data-sky-id="{safe_sub}"
          data-src="{html.escape(tool['filename'], quote=True)}"
          title="{html.escape(tool['label'], quote=True)}" loading="lazy"></iframe>
      </section>"""
        )
    return os.linesep.join(blocks)


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="color-scheme" content="light dark">
<title>Astrology Hub — Freedom 250 Observatory</title>
<style>
:root{
  --sky-bg:#f4f0e6;--sky-panel:#fbf8f1;--sky-card:#fffdf8;
  --sky-ink:#28251f;--sky-muted:#736b5d;--sky-faint:#9b9282;
  --sky-line:#d8d0c1;--sky-accent:#8a542f;--sky-accent-soft:#efe1d2;
  --sky-focus:#2f6d8a;--sky-shadow:rgba(43,35,24,.16);
  color-scheme:light;
}
html[data-theme="dark"]{
  --sky-bg:#16140f;--sky-panel:#1d1a13;--sky-card:#242017;
  --sky-ink:#e6dfd0;--sky-muted:#b9b09c;--sky-faint:#857d6c;
  --sky-line:#3a3426;--sky-accent:#d99570;--sky-accent-soft:#35271d;
  --sky-focus:#70b7d4;--sky-shadow:rgba(0,0,0,.4);
  color-scheme:dark;
}
*{box-sizing:border-box}
html,body{width:100%;height:100%;margin:0;overflow:hidden;background:var(--sky-bg);color:var(--sky-ink)}
body{font-family:Inter,ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
button,input{font:inherit}
button:focus-visible,input:focus-visible{outline:3px solid color-mix(in srgb,var(--sky-focus) 48%,transparent);outline-offset:2px}
.sky-shell{display:grid;grid-template-columns:272px minmax(0,1fr);height:100%}
.sky-rail{
  min-width:0;overflow-y:auto;overscroll-behavior:contain;padding:18px 14px 36px;
  background:var(--sky-panel);border-right:1px solid var(--sky-line)
}
.sky-brand{display:flex;align-items:start;justify-content:space-between;gap:12px;padding:1px 6px 13px}
.sky-brand h1{font:700 22px/1.12 Georgia,"Times New Roman",serif;margin:0;color:var(--sky-ink)}
.sky-brand span{display:block;margin-top:4px;color:var(--sky-muted);font-size:11px;line-height:1.35}
.sky-close{display:none;border:1px solid var(--sky-line);border-radius:999px;width:34px;height:34px;background:var(--sky-card);color:var(--sky-ink);cursor:pointer}
.sky-search{position:relative;margin:0 4px 17px}
.sky-search label{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.sky-search input{
  width:100%;border:1px solid var(--sky-line);border-radius:9px;background:var(--sky-card);
  color:var(--sky-ink);padding:9px 10px 9px 31px;font-size:12px
}
.sky-search::before{content:"⌕";position:absolute;left:10px;top:6px;color:var(--sky-faint);font-size:18px;z-index:1}
.sky-section{margin:0 0 20px}
.sky-section[hidden]{display:none}
.sky-section h2{margin:0 6px 3px;color:var(--sky-accent);font-size:10px;line-height:1.2;letter-spacing:.15em;text-transform:uppercase}
.sky-section>p{margin:0 6px 7px;color:var(--sky-faint);font:italic 11px/1.35 Georgia,serif}
.sky-tool-list{display:grid;gap:3px}
.sky-tool{
  display:block;width:100%;border:1px solid transparent;border-radius:8px;background:transparent;
  color:var(--sky-ink);text-align:left;padding:8px 9px;cursor:pointer
}
.sky-tool:hover{background:var(--sky-card);border-color:var(--sky-line)}
.sky-tool.active{background:var(--sky-accent-soft);border-color:color-mix(in srgb,var(--sky-accent) 38%,var(--sky-line));box-shadow:inset 3px 0 0 var(--sky-accent)}
.sky-tool[hidden]{display:none}
.sky-tool-name{display:block;font-size:13px;font-weight:700;line-height:1.25}
.sky-tool-desc{display:block;margin-top:2px;color:var(--sky-muted);font-size:10px;line-height:1.28}
.sky-main{min-width:0;display:grid;grid-template-rows:42px minmax(0,1fr);height:100%;background:var(--sky-bg)}
.sky-topbar{
  display:flex;align-items:center;gap:9px;min-width:0;padding:0 15px;
  background:var(--sky-panel);border-bottom:1px solid var(--sky-line)
}
.sky-menu{
  display:none;border:1px solid var(--sky-line);border-radius:7px;background:var(--sky-card);
  color:var(--sky-ink);padding:6px 9px;cursor:pointer
}
.sky-breadcrumb{display:flex;align-items:center;gap:7px;min-width:0;font-size:12px;color:var(--sky-muted);white-space:nowrap}
.sky-breadcrumb .host{color:var(--sky-faint)}
.sky-breadcrumb .sep{color:var(--sky-line)}
.sky-breadcrumb .section{color:var(--sky-muted)}
.sky-breadcrumb .tool{overflow:hidden;text-overflow:ellipsis;color:var(--sky-ink);font-weight:700}
.sky-shortcut{margin-left:auto;color:var(--sky-faint);font-size:10px;white-space:nowrap}
.sky-stage{position:relative;min-width:0;min-height:0}
.sky-view{position:absolute;inset:0;background:var(--sky-bg)}
.sky-view[hidden]{display:none}
.sky-view iframe{display:block;width:100%;height:100%;border:0;background:var(--sky-bg)}
.hub-view{overflow:hidden}
.hub-scroll{height:100%;overflow:auto;overscroll-behavior:contain;padding:0;scrollbar-gutter:stable;background:var(--sky-bg)}
.hub-depth{width:min(1180px,calc(100% - clamp(32px,8vw,116px)));margin:0 auto;padding:6px 0 clamp(36px,5vw,70px)}
.hub-orrery{
  --hub-ink:#eef8ff;--hub-muted:#9bb5c8;--hub-cyan:#66dcff;--hub-gold:#ffcc69;
  --hub-red:#ff715f;--hub-blue:#6f9dff;--hub-violet:#b292ff;--hub-line:rgba(126,211,255,.19);
  position:relative;width:100%;min-height:max(690px,calc(100vh - 42px));overflow:hidden;
  color:var(--hub-ink);background:
    radial-gradient(circle at 58% 47%,rgba(255,190,70,.12),transparent 17%),
    radial-gradient(circle at 14% 10%,rgba(53,143,219,.16),transparent 31%),
    linear-gradient(145deg,#030911,#071624)
}
.hub-stars,.hub-stars::before,.hub-stars::after{
  position:absolute;inset:0;content:"";pointer-events:none;background-image:
    radial-gradient(circle,rgba(213,241,255,.82) 0 1px,transparent 1.4px),
    radial-gradient(circle,rgba(100,211,255,.46) 0 1px,transparent 1.5px);
  background-size:83px 83px,137px 137px;background-position:7px 19px,43px 61px;opacity:.34
}
.hub-stars::before{transform:translate(31px,22px);opacity:.28}.hub-stars::after{transform:translate(-19px,41px);opacity:.18}
.hub-live-top{position:relative;z-index:14;display:flex;align-items:center;justify-content:space-between;gap:18px;padding:19px 26px;border-bottom:1px solid rgba(130,214,255,.13);background:linear-gradient(180deg,rgba(3,9,17,.88),rgba(3,9,17,.22))}
.hub-live-brand{display:flex;align-items:center;gap:10px;min-width:0;color:var(--hub-muted);font-size:11px;letter-spacing:.14em;text-transform:uppercase}
.hub-live-brand>span{width:27px;height:27px;flex:0 0 auto;border-radius:50%;background:radial-gradient(circle at 38% 34%,#fff5b4 0 8%,#ffc95b 30%,#f1842b 68%,#9e2f17 100%);box-shadow:0 0 22px rgba(255,190,86,.58)}
.hub-live-brand strong{color:var(--hub-ink);font-weight:700;white-space:nowrap}
.hub-mode-nav{display:flex;gap:5px;padding:4px;border:1px solid rgba(131,210,255,.14);border-radius:999px;background:rgba(3,11,19,.66)}
.hub-mode-nav button{border:0;border-radius:999px;background:transparent;color:var(--hub-muted);padding:8px 13px;min-height:34px;font-size:11px;font-weight:700;cursor:pointer}
.hub-mode-nav button[aria-pressed="true"]{background:rgba(91,208,255,.15);color:var(--hub-ink);box-shadow:inset 0 0 0 1px rgba(102,220,255,.28)}
.hub-live-clock{text-align:right;color:var(--hub-muted);font-size:11px;line-height:1.4;white-space:nowrap}.hub-live-clock strong,.hub-live-clock span{display:block}.hub-live-clock strong{color:var(--hub-ink);font-weight:700}
.hub-live-intro{position:absolute;z-index:10;left:clamp(25px,4.3vw,68px);top:clamp(100px,16vh,150px);width:min(390px,39%)}
.hub-live-eyebrow,.hub-story-kicker{color:var(--hub-cyan);font-size:10px;font-weight:800;letter-spacing:.15em;text-transform:uppercase}
.hub-live-intro h1{margin:10px 0 14px;font:700 clamp(40px,6vw,76px)/.94 Georgia,"Times New Roman",serif;letter-spacing:-.04em}
.hub-live-intro p{max-width:355px;margin:0;color:var(--hub-muted);font:16px/1.55 Georgia,"Times New Roman",serif}
.hub-system-wrap{position:absolute;inset:62px 0 0;overflow:hidden}
.hub-solar-system{position:absolute;left:61%;top:49%;width:min(680px,66vw);aspect-ratio:1;transform:translate(-50%,-50%)}
.hub-orbit{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);border:1px solid var(--hub-line);border-radius:50%;pointer-events:none;box-shadow:inset 0 0 12px rgba(56,178,229,.035)}
.hub-orbit.o1{width:16%;height:16%}.hub-orbit.o2{width:25%;height:25%}.hub-orbit.o3{width:35%;height:35%}.hub-orbit.o4{width:46%;height:46%}.hub-orbit.o5{width:58%;height:58%}.hub-orbit.o6{width:70%;height:70%}.hub-orbit.o7{width:83%;height:83%}.hub-orbit.o8{width:96%;height:96%}
.hub-sun{position:absolute;z-index:7;left:50%;top:50%;width:60px;height:60px;transform:translate(-50%,-50%);display:grid;place-items:center;border:0;border-radius:50%;background:radial-gradient(circle at 36% 32%,#fff6b5 0 5%,#ffd15d 23%,#ff8b32 63%,#d44018 100%);box-shadow:0 0 38px rgba(255,172,67,.78),0 0 94px rgba(255,142,53,.23);color:#2d1705;cursor:pointer}
.hub-sun span{font-size:9px;font-weight:900;letter-spacing:.09em;text-transform:uppercase}
.hub-carrier{position:absolute;left:50%;top:50%;transform:rotate(var(--angle));transform-origin:0 0;pointer-events:none}
.hub-carrier.c-mercury{width:8%}.hub-carrier.c-venus{width:12.5%}.hub-carrier.c-earth{width:17.5%}.hub-carrier.c-mars{width:23%}.hub-carrier.c-jupiter{width:29%}.hub-carrier.c-saturn{width:35%}.hub-carrier.c-uranus{width:41.5%}.hub-carrier.c-neptune{width:48%}.hub-carrier.c-pluto{width:48%}
.hub-body{position:absolute;left:100%;top:0;transform:translate(-50%,-50%) rotate(var(--neg-angle));pointer-events:auto;border:0;background:transparent;color:var(--hub-ink);padding:0;min-width:46px;min-height:46px;display:grid;place-items:center;cursor:pointer}
.hub-planet{display:block;position:relative;width:var(--planet-size);height:var(--planet-size);border-radius:50%;background:var(--planet-fill);box-shadow:0 0 14px var(--planet-halo);transition:transform .2s ease,box-shadow .2s ease}
.hub-body:hover .hub-planet,.hub-body:focus-visible .hub-planet,.hub-body.is-selected .hub-planet{transform:scale(1.28);box-shadow:0 0 26px var(--planet-halo),0 0 0 6px rgba(102,220,255,.08)}
.hub-planet-label{position:absolute;top:calc(50% + 15px);left:50%;transform:translateX(-50%);font-size:9px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--hub-muted);white-space:nowrap}.hub-body.is-selected .hub-planet-label{color:var(--hub-ink)}
.hub-planet.mercury{--planet-size:8px;--planet-fill:#aaa9a4;--planet-halo:rgba(210,210,205,.65)}
.hub-planet.venus{--planet-size:11px;--planet-fill:#f1c77d;--planet-halo:rgba(241,199,125,.7)}
.hub-planet.earth{--planet-size:14px;--planet-fill:linear-gradient(135deg,#63d1e6,#245bbb);--planet-halo:rgba(82,192,231,.84)}
.hub-planet.earth i{position:absolute;width:5px;height:5px;border-radius:50%;background:#d9ecff;right:-9px;top:-3px;box-shadow:0 0 8px #d9ecff}
.hub-planet.mars{--planet-size:10px;--planet-fill:#d65c3e;--planet-halo:rgba(255,103,71,.78)}
.hub-planet.jupiter{--planet-size:22px;--planet-fill:linear-gradient(#d9b389 0 24%,#f0d5a9 25% 42%,#a87855 43% 55%,#e4c79d 56%);--planet-halo:rgba(230,195,147,.72)}
.hub-planet.saturn{--planet-size:18px;--planet-fill:#ddc487;--planet-halo:rgba(221,196,135,.75)}
.hub-planet.saturn::after{content:"";position:absolute;left:50%;top:50%;width:30px;height:8px;transform:translate(-50%,-50%) rotate(-16deg);border:1px solid rgba(235,211,149,.82);border-radius:50%}
.hub-planet.uranus{--planet-size:14px;--planet-fill:#8fd5d6;--planet-halo:rgba(143,213,214,.75)}
.hub-planet.neptune{--planet-size:14px;--planet-fill:#426ecb;--planet-halo:rgba(85,130,241,.86)}
.hub-planet.pluto{--planet-size:7px;--planet-fill:#c7b6a2;--planet-halo:rgba(205,184,163,.68)}
.hub-relation{position:absolute;z-index:4;height:1px;background:linear-gradient(90deg,transparent,var(--hub-cyan),transparent);transform-origin:left center;opacity:0;transition:opacity .25s ease;box-shadow:0 0 8px rgba(102,220,255,.5);pointer-events:none}
.hub-relation-one{left:29%;top:62%;width:50%;transform:rotate(-13deg)}.hub-relation-two{left:47%;top:28%;width:35%;transform:rotate(11deg)}
.hub-orrery[data-hub-mode="story"] .hub-relation{opacity:.8}
.hub-story-panel{position:absolute;z-index:12;right:clamp(24px,4vw,58px);bottom:82px;width:min(345px,36%);padding:18px 19px;border:1px solid rgba(119,209,250,.18);border-radius:16px;background:rgba(6,20,33,.84);backdrop-filter:blur(16px);box-shadow:0 20px 55px rgba(0,0,0,.3)}
.hub-story-panel h2{margin:7px 0 8px;font:700 24px/1.08 Georgia,"Times New Roman",serif}.hub-story-panel p{margin:0;color:var(--hub-muted);font-size:12px;line-height:1.5}
.hub-story-meta{display:flex;gap:8px;align-items:center;margin-top:12px;padding-top:12px;border-top:1px solid rgba(133,214,251,.14);color:var(--hub-muted);font-size:10px}.hub-story-meta span{width:7px;height:7px;border-radius:50%;background:var(--hub-cyan);box-shadow:0 0 12px var(--hub-cyan);flex:0 0 auto}.hub-story-meta em{font-style:normal}
.hub-story-link{margin-top:12px;border:0;background:transparent;color:var(--hub-cyan);padding:0;font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.08em;cursor:pointer}
.hub-entry-dock{position:absolute;z-index:13;left:clamp(24px,4vw,58px);bottom:28px;display:flex;gap:9px;align-items:center;max-width:58%}
.hub-entry{min-height:48px;padding:10px 13px;border:1px solid rgba(117,208,248,.18);border-radius:12px;background:rgba(3,13,22,.76);color:var(--hub-ink);text-align:left;backdrop-filter:blur(12px);cursor:pointer}.hub-entry strong,.hub-entry span{display:block}.hub-entry strong{font-size:11px}.hub-entry span{margin-top:2px;color:var(--hub-muted);font-size:9px}.hub-entry.primary{border-color:transparent;background:var(--hub-cyan);color:#03111a}.hub-entry.primary span{color:rgba(3,17,26,.67)}
.hub-scale-note{position:absolute;z-index:9;right:clamp(24px,4vw,58px);bottom:25px;color:rgba(155,181,200,.62);font-size:8px;letter-spacing:.07em;text-transform:uppercase}
@media(prefers-reduced-motion:no-preference){
  .hub-carrier{animation:hub-orbit var(--dur) linear infinite}.hub-body{animation:hub-counter var(--dur) linear infinite}
  @keyframes hub-orbit{to{transform:rotate(calc(var(--angle) + 360deg))}}
  @keyframes hub-counter{to{transform:translate(-50%,-50%) rotate(calc(var(--neg-angle) - 360deg))}}
}
.hub-hero{
  position:relative;overflow:hidden;padding:clamp(30px,5vw,66px);border:1px solid var(--sky-line);
  border-radius:24px;background:
    radial-gradient(circle at 82% 15%,color-mix(in srgb,var(--sky-accent) 20%,transparent),transparent 36%),
    linear-gradient(135deg,var(--sky-card),var(--sky-panel));box-shadow:0 18px 46px var(--sky-shadow)
}
.hub-hero::after{content:"";position:absolute;right:-90px;bottom:-150px;width:330px;height:330px;border:1px solid color-mix(in srgb,var(--sky-accent) 32%,transparent);border-radius:50%;box-shadow:0 0 0 34px color-mix(in srgb,var(--sky-accent) 7%,transparent),0 0 0 78px color-mix(in srgb,var(--sky-accent) 5%,transparent);pointer-events:none}
.hub-eyebrow,.hub-kicker,.hub-route-kicker{color:var(--sky-accent);font-size:10px;font-weight:800;letter-spacing:.17em;text-transform:uppercase}
.hub-hero h1{position:relative;z-index:1;max-width:760px;margin:10px 0 13px;font:700 clamp(38px,6vw,74px)/.98 Georgia,"Times New Roman",serif;letter-spacing:-.035em}
.hub-deck{position:relative;z-index:1;max-width:760px;margin:0;color:var(--sky-muted);font:18px/1.55 Georgia,"Times New Roman",serif}
.hub-actions{position:relative;z-index:1;display:flex;flex-wrap:wrap;gap:9px;margin-top:28px}
.hub-primary,.hub-secondary,.hub-link{border:1px solid var(--sky-line);border-radius:999px;background:var(--sky-card);color:var(--sky-ink);padding:9px 13px;font-size:12px;font-weight:750;cursor:pointer}
.hub-primary{border-color:var(--sky-accent);background:var(--sky-accent);color:var(--sky-bg);padding:10px 16px}
.hub-primary:hover,.hub-secondary:hover,.hub-link:hover{transform:translateY(-1px);box-shadow:0 7px 18px var(--sky-shadow)}
.hub-section{margin-top:clamp(38px,5vw,64px)}
.hub-section-head{display:flex;align-items:end;justify-content:space-between;gap:26px;margin-bottom:18px;padding:0 3px}
.hub-section-head h2{margin:5px 0 0;font:700 clamp(25px,3vw,38px)/1.05 Georgia,"Times New Roman",serif;letter-spacing:-.02em}
.hub-section-head>p{max-width:470px;margin:0;color:var(--sky-muted);font-size:13px;line-height:1.55}
.hub-scale-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:13px}
.hub-scale,.hub-route{border:1px solid var(--sky-line);border-radius:16px;background:var(--sky-card);padding:23px}
.hub-scale{display:flex;flex-direction:column;min-height:290px}
.hub-number{color:var(--sky-faint);font:700 12px/1 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.12em}
.hub-scale h3,.hub-route h3{margin:12px 0 8px;font:700 22px/1.12 Georgia,"Times New Roman",serif}
.hub-scale p{margin:0;color:var(--sky-muted);font-size:13px;line-height:1.55}
.hub-link-row{display:flex;flex-wrap:wrap;gap:7px;margin-top:auto;padding-top:22px}
.hub-link{padding:7px 10px;color:var(--sky-accent);font-size:11px}
.hub-reading-order{border-top:1px solid var(--sky-line);border-bottom:1px solid var(--sky-line);padding:30px 0}
.hub-steps{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:0;margin:0;padding:0;list-style:none;counter-reset:hub-step}
.hub-steps li{counter-increment:hub-step;min-width:0;padding:16px;border-left:1px solid var(--sky-line)}
.hub-steps li:first-child{border-left:0}
.hub-steps li::before{content:"0" counter(hub-step);display:block;margin-bottom:14px;color:var(--sky-accent);font:700 10px/1 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.12em}
.hub-steps strong,.hub-steps span{display:block}
.hub-steps strong{font:700 16px/1.2 Georgia,"Times New Roman",serif}
.hub-steps span{margin-top:7px;color:var(--sky-muted);font-size:11px;line-height:1.45}
.hub-route-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:13px}
.hub-front{padding:clamp(26px,4vw,52px) clamp(16px,4vw,48px) clamp(20px,3vw,34px);border-bottom:1px solid var(--sky-line)}
.hub-front h1{margin:8px 0 10px;font:700 clamp(30px,4vw,48px)/1.04 Georgia,"Times New Roman",serif;letter-spacing:-.02em}
.hub-front-deck{max-width:760px;margin:0;color:var(--sky-muted);font-size:14px;line-height:1.6}
.hub-front-links{margin:18px 0 22px;padding-top:0}
.hub-front-routes{grid-template-columns:repeat(3,minmax(0,1fr))}
.hub-pattern-strip{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:10px;margin-top:16px}
.hub-pattern{display:flex;flex-direction:column;gap:6px;text-align:left;border:1px solid var(--sky-line);border-radius:12px;background:var(--sky-card);color:var(--sky-ink);padding:13px 14px;cursor:pointer;font:inherit}
.hub-pattern strong{font:700 15px/1.25 Georgia,"Times New Roman",serif}
.hub-pattern span{color:var(--sky-muted);font-size:11.5px;line-height:1.45}
.hub-pattern em{align-self:flex-start;font-style:normal;font-size:10px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--sky-accent);background:var(--sky-accent-soft);border-radius:999px;padding:3px 8px}
.hub-pattern em[data-status="mostly_ordinary"]{color:var(--sky-muted);background:transparent;border:1px solid var(--sky-line)}
.hub-route h3{font-size:21px;line-height:1.25}
.hub-route ol{margin:15px 0 19px;padding-left:20px;color:var(--sky-muted);font-size:12px;line-height:1.48}
.hub-route li+li{margin-top:6px}
.hub-packet-shelf{display:grid;gap:9px}
.hub-packet-group{border:1px solid var(--sky-line);border-radius:14px;background:var(--sky-card);overflow:hidden}
.hub-packet-group summary{display:flex;align-items:center;justify-content:space-between;gap:18px;padding:16px 18px;cursor:pointer;font:700 17px/1.2 Georgia,"Times New Roman",serif;list-style:none}
.hub-packet-group summary::-webkit-details-marker{display:none}
.hub-packet-group summary::before{content:"+";order:2;color:var(--sky-accent);font:700 17px/1 ui-monospace,SFMono-Regular,Menlo,monospace}
.hub-packet-group[open] summary::before{content:"−"}
.hub-packet-group summary>strong{order:1;margin-left:auto;color:var(--sky-faint);font:700 11px/1 ui-monospace,SFMono-Regular,Menlo,monospace}
.hub-packet-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1px;border-top:1px solid var(--sky-line);background:var(--sky-line)}
.hub-packet{display:flex;min-width:0;min-height:112px;flex-direction:column;align-items:flex-start;border:0;background:var(--sky-card);color:var(--sky-ink);padding:16px;text-align:left;cursor:pointer}
.hub-packet:hover{background:var(--sky-accent-soft)}
.hub-packet strong{font:700 15px/1.3 Georgia,"Times New Roman",serif}
.hub-packet span{margin-top:6px;color:var(--sky-muted);font-size:10px;line-height:1.35}
.hub-packet em{margin-top:auto;padding-top:12px;color:var(--sky-faint);font-size:9px;font-style:normal;letter-spacing:.08em;text-transform:uppercase}
.hub-packet em[data-state="prospective"]{color:var(--sky-accent)}
.hub-stat-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));border:1px solid var(--sky-line);border-radius:16px;background:var(--sky-card);overflow:hidden}
.hub-stat-grid>div{padding:21px;border-left:1px solid var(--sky-line);border-top:1px solid var(--sky-line)}
.hub-stat-grid>div:nth-child(-n+3){border-top:0}
.hub-stat-grid>div:nth-child(3n+1){border-left:0}
.hub-stat-grid strong,.hub-stat-grid span{display:block}
.hub-stat-grid strong{color:var(--sky-accent);font:700 32px/1 Georgia,"Times New Roman",serif}
.hub-stat-grid span{margin-top:7px;color:var(--sky-muted);font-size:11px;line-height:1.35}
.hub-boundary{display:flex;gap:18px;align-items:baseline;margin-top:42px;margin-bottom:20px;padding:18px 20px;border-left:4px solid var(--sky-accent);background:var(--sky-accent-soft);color:var(--sky-muted);font-size:12px;line-height:1.5}
.hub-boundary strong{flex:0 0 auto;color:var(--sky-ink);font:700 16px/1.2 Georgia,"Times New Roman",serif}
.sky-empty{
  display:none;margin:24px;border:1px dashed var(--sky-line);border-radius:10px;
  color:var(--sky-muted);padding:26px;text-align:center;font-size:13px
}
.sky-empty.visible{display:block}
.sky-backdrop{display:none}
@media(max-width:900px){
  .sky-shell{display:block}
  .sky-rail{
    position:fixed;z-index:30;inset:0 auto 0 0;width:min(340px,88vw);
    box-shadow:12px 0 34px var(--sky-shadow);transform:translateX(-105%);
    transition:transform .18s ease
  }
  body.sky-drawer-open .sky-rail{transform:translateX(0)}
  .sky-close,.sky-menu{display:inline-grid;place-items:center}
  .sky-backdrop{
    display:block;position:fixed;z-index:20;inset:0;border:0;background:rgba(20,16,11,.48);
    opacity:0;visibility:hidden;transition:opacity .18s ease,visibility .18s ease;cursor:default
  }
  body.sky-drawer-open .sky-backdrop{opacity:1;visibility:visible}
  .sky-main{height:100%}
  .sky-topbar{padding:0 10px}
  .sky-shortcut{display:none}
  .hub-orrery{min-height:790px}
  .hub-live-top{padding:15px 18px;align-items:flex-start;flex-wrap:wrap}
  .hub-mode-nav{order:3;width:100%;justify-content:center}
  .hub-live-intro{left:20px;right:20px;top:116px;width:auto;text-align:center}
  .hub-live-intro p{margin-left:auto;margin-right:auto}
  .hub-solar-system{left:50%;top:51%;width:min(560px,86vw)}
  .hub-story-panel{left:20px;right:20px;bottom:82px;width:auto}
  .hub-entry-dock{left:20px;right:20px;bottom:19px;max-width:none;justify-content:center}
  .hub-scale-note{display:none}
  .hub-depth{width:min(100% - 36px,1180px)}
  .hub-scale-grid{grid-template-columns:1fr}
  .hub-packet-grid{grid-template-columns:1fr 1fr}
  .hub-scale{min-height:0}
  .hub-steps{grid-template-columns:1fr 1fr}
  .hub-steps li:nth-child(odd){border-left:0}
  .hub-steps li:nth-child(n+3){border-top:1px solid var(--sky-line)}
}
@media(max-width:520px){
  .sky-breadcrumb .host,.sky-breadcrumb .section,.sky-breadcrumb .sep:first-of-type{display:none}
  .hub-orrery{min-height:850px}
  .hub-live-brand strong{font-size:10px}.hub-live-clock span{display:none}
  .hub-mode-nav button{padding:7px 10px}
  .hub-live-intro{top:115px}.hub-live-intro h1{font-size:46px}
  .hub-live-intro p{font-size:14px}
  .hub-solar-system{top:49%;width:410px}
  .hub-planet-label{display:none}
  .hub-story-panel{bottom:88px}
  .hub-entry:nth-child(3){display:none}
  .hub-entry{padding:9px 10px}
  .hub-hero{padding:27px 22px;border-radius:17px}
  .hub-hero h1{font-size:42px}
  .hub-section-head{display:block}
  .hub-section-head>p{margin-top:9px}
  .hub-route-grid,.hub-stat-grid,.hub-steps,.hub-front-routes{grid-template-columns:1fr}
  .hub-packet-grid{grid-template-columns:1fr}
  .hub-stat-grid>div,.hub-stat-grid>div:nth-child(-n+3){border-left:0;border-top:1px solid var(--sky-line)}
  .hub-stat-grid>div:first-child{border-top:0}
  .hub-steps li,.hub-steps li:nth-child(odd){border-left:0;border-top:1px solid var(--sky-line)}
  .hub-steps li:first-child{border-top:0}
  .hub-boundary{display:block}
  .hub-boundary span{display:block;margin-top:7px}
}
@media(prefers-reduced-motion:reduce){
  .sky-rail,.sky-backdrop{transition:none}
}
/* Embedded under the Observatory shell: the Astrology menu owns navigation,
   so the rail becomes an on-demand drawer at every width. */
html.sky-embedded .sky-shell{display:block}
html.sky-embedded .sky-rail{
  position:fixed;z-index:30;inset:0 auto 0 0;width:min(340px,88vw);
  box-shadow:12px 0 34px var(--sky-shadow);transform:translateX(-105%);
  transition:transform .18s ease
}
html.sky-embedded body.sky-drawer-open .sky-rail{transform:translateX(0)}
html.sky-embedded .sky-close,html.sky-embedded .sky-menu{display:inline-grid;place-items:center}
html.sky-embedded .sky-backdrop{
  display:block;position:fixed;z-index:20;inset:0;border:0;background:rgba(20,16,11,.48);
  opacity:0;visibility:hidden;transition:opacity .18s ease,visibility .18s ease;cursor:default
}
html.sky-embedded body.sky-drawer-open .sky-backdrop{opacity:1;visibility:visible}
html.sky-embedded .sky-main{height:100%}
@media(prefers-reduced-motion:reduce){
  html.sky-embedded .sky-rail,html.sky-embedded .sky-backdrop{transition:none}
}
</style>
</head>
<body>
<script>try{if(window.self!==window.top)document.documentElement.classList.add("sky-embedded")}catch(_){document.documentElement.classList.add("sky-embedded")}</script>
<div class="sky-shell">
  <aside class="sky-rail" id="skyRail" aria-label="Astrology Hub instruments">
    <div class="sky-brand">
      <div><h1>Astrology Hub</h1><span>One orientation. __INSTRUMENT_COUNT__ instruments. No lost depth.</span></div>
      <button class="sky-close" id="skyClose" type="button" aria-label="Close instruments">×</button>
    </div>
    <div class="sky-search">
      <label for="skySearch">Filter instruments</label>
      <input id="skySearch" type="search" placeholder="Find an instrument…" autocomplete="off">
    </div>
    <nav id="skyNav" aria-label="Astrology Hub">
__SECTIONS__
    </nav>
    <div class="sky-empty" id="skyEmpty">No instrument matches that search.</div>
  </aside>
  <button class="sky-backdrop" id="skyBackdrop" type="button" tabindex="-1" aria-label="Close instruments"></button>
  <main class="sky-main">
    <header class="sky-topbar">
      <button class="sky-menu" id="skyMenu" type="button" aria-controls="skyRail" aria-expanded="false" aria-label="Open instruments">☰</button>
      <div class="sky-breadcrumb" id="skyBreadcrumb" aria-live="polite">
        <span class="host">Astrology Hub</span><span class="sep">/</span>
        <span class="section"></span><span class="sep">/</span><span class="tool"></span>
      </div>
      <span class="sky-shortcut">/ find · ⌥↑/↓ switch</span>
    </header>
    <div class="sky-stage" id="skyStage">
__VIEWS__
    </div>
  </main>
</div>
<script id="f250-sky-tool-registry" type="application/json">__REGISTRY__</script>
<script>
(function(){
  "use strict";
  var HOST_ID=__HOST_ID__;
  var LAST_KEY=__LAST_KEY__;
  var THEME_KEY=__THEME_KEY__;
  var registry=JSON.parse(document.getElementById("f250-sky-tool-registry").textContent);
  var hubPacketNode=document.getElementById("f250-hub-packets");
  var hubPackets=hubPacketNode ? JSON.parse(hubPacketNode.textContent) : [];
  window.F250_SKY_TOOL_REGISTRY=registry;

  var bySub=Object.create(null);
  var aliases=Object.create(null);
  var routeTargets=Object.create(null);
  registry.forEach(function(tool){
    bySub[tool.sub]=tool;
    [tool.sub,tool.id,tool.legacyView,tool.filename,tool.label]
      .concat(tool.legacyViews||[],tool.aliases||[])
      .forEach(function(value){
        if(value) aliases[String(value).trim().toLowerCase()]=tool.sub;
      });
    Object.keys(tool.absorbedRoutes||{}).forEach(function(route){
      routeTargets[String(route).trim().toLowerCase()]={sub:tool.sub,innerSub:tool.absorbedRoutes[route]};
    });
  });

  var rail=document.getElementById("skyRail");
  var menu=document.getElementById("skyMenu");
  var closeButton=document.getElementById("skyClose");
  var backdrop=document.getElementById("skyBackdrop");
  var nav=document.getElementById("skyNav");
  var search=document.getElementById("skySearch");
  var empty=document.getElementById("skyEmpty");
  var stage=document.getElementById("skyStage");
  var crumbSection=document.querySelector("#skyBreadcrumb .section");
  var crumbTool=document.querySelector("#skyBreadcrumb .tool");
  var activeSub=null;
  var currentDate=null;
  var currentTheme="light";
  var lastDrawerFocus=null;
  var pendingBySub=Object.create(null);

  var hubBodies={
    Sun:{k:"The light",t:"Opposition puts Earth in the middle",p:"The Earth-centered chart names the relationship we experience. The physical view shows the arrangement; the exact chart shows where the light lands in Washington.",m:"Astronomy supplies context, not a second vote"},
    Moon:{k:"The chapter keeper",t:"The Moon carries the immediate plot",p:"New Moons seed, Full Moons illuminate, eclipses deepen the chapter, and quarter Moons show the turn. Open the exact lunar chart for its houses, roots and lineage.",m:"Moon families continue beyond one lunation"},
    Mercury:{k:"Terms and transmission",t:"Mercury carries the record",p:"Mercury moves language, evidence, negotiation and technical terms through the wider field. Its station, solar phase and chart role decide how loudly it speaks.",m:"Fast motion translates the long clocks"},
    Venus:{k:"Value and accord",t:"Venus sets the terms of worth",p:"Venus can carry agreement, resources, legitimacy and judgment. Its actual condition matters more than an isolated keyword.",m:"Open the whole chart before judging"},
    Mars:{k:"Action in the field",t:"Mars makes the pressure visible",p:"Mars brings movement, enforcement, rupture and courage into the present chapter. Its relationship history shows what confrontation is reaching a new phase.",m:"Follow the pair, not one dramatic headline"},
    Jupiter:{k:"Scale and judgment",t:"Jupiter enlarges what it touches",p:"Jupiter can widen law, belief, jurisdiction and opportunity. The intact chart tells us whether expansion is support, excess or both.",m:"Scale is a condition, not a conclusion"},
    Saturn:{k:"The institutional edge",t:"Saturn gives the chapter a boundary",p:"Saturn marks rule, duration, duty, legitimacy and material constraint. Its slow relationship clocks outlast any single lunation.",m:"The long clock remains in motion"},
    Uranus:{k:"The break in continuity",t:"Uranus changes the operating pattern",p:"Uranus can expose the unstable hinge between an inherited system and a new one. Exact aspects and house placement show where the break is active.",m:"Disruption does not name the outcome"},
    Neptune:{k:"Image and permeability",t:"Neptune changes what can be seen",p:"Neptune carries image, atmosphere, faith, diffusion and uncertainty. Declination and solar geometry add physical context to its longitude story.",m:"Keep symbol, visibility and evidence separate"},
    Pluto:{k:"Long-cycle pressure",t:"Pluto holds the far end of the field",p:"Pluto marks concentrated power, exposure, compulsion and remaking across long spans. A later opposition belongs to the history seeded at conjunction.",m:"A phase is a development, not a replay"}
  };
  var hubModeCopy={
    sky:{e:"The sky right now",t:"What is moving?",d:"Begin with the whole sky. Touch a planet in the living solar system, follow a relationship, then open the exact Earth-centered chart when you want the particulars."},
    story:{e:"The story in motion",t:"What is coming due?",d:"See the governing lunar chapter, the next exact confrontation and the longer clocks as one moving sequence—then enter the intact chart."},
    explore:{e:"The deeper rooms",t:"Choose your doorway.",d:"The charts, methods and pattern studies are still here. They wait beneath the experience, organized by the question you want to ask."}
  };
  function hubMomentMs(value){
    if(!value) return Date.now();
    var text=String(value);
    if(/^\d{4}-\d{2}-\d{2}$/.test(text)) text+="T12:00:00Z";
    var parsed=Date.parse(text);
    return Number.isFinite(parsed) ? parsed : Date.now();
  }
  function hubDateText(ms,includeTime){
    var options={timeZone:"America/New_York",month:"long",day:"numeric",year:"numeric"};
    if(includeTime) Object.assign(options,{hour:"numeric",minute:"2-digit",timeZoneName:"short"});
    return new Date(ms).toLocaleString("en-US",options);
  }
  function hubCleanLabel(label){return String(label||"").replace(/^\d{4}-\d{2}-\d{2}\s+/,"");}
  function updateHubMoment(value){
    var dateEl=document.getElementById("hub-live-date");
    var nextButton=document.querySelector("[data-hub-next-reading]");
    if(!dateEl || !nextButton || !hubPackets.length) return;
    var ms=hubMomentMs(value),day=86400000;
    dateEl.textContent=hubDateText(ms,false);
    var ordered=hubPackets.slice().sort(function(a,b){return Date.parse(a.utc)-Date.parse(b.utc);});
    var lunar=ordered.filter(function(packet){return packet.group!=="ingress_governors";});
    var next=ordered.find(function(packet){return Date.parse(packet.utc)>=ms;})||null;
    var previousLunar=null;
    lunar.forEach(function(packet){if(Date.parse(packet.utc)<=ms) previousLunar=packet;});
    var nearNext=next && Date.parse(next.utc)>=ms && Date.parse(next.utc)-ms<=3*day;
    var feature=nearNext ? next : (previousLunar||next||lunar[lunar.length-1]);
    if(!feature) return;
    nextButton.dataset.chartId=feature.chartId;
    nextButton.querySelector("strong").textContent=nearNext ? "Enter the approaching chart" : "Enter the governing chart";
    var selected=document.querySelector("[data-hub-body].is-selected");
    if(selected && selected.dataset.hubBody!=="Earth") return;
    document.getElementById("hub-story-kicker").textContent=nearNext ? "Approaching chapter" : (next ? "Governing lunar chapter" : "Latest registered lunar chapter");
    document.getElementById("hub-story-title").textContent=hubCleanLabel(feature.label);
    document.getElementById("hub-story-text").textContent=feature.kind+" · "+hubDateText(Date.parse(feature.utc),true)+". Open the intact chart for houses, angles, roots, lineage and the complete relationship field.";
    document.getElementById("hub-story-meta").textContent=next && feature!==next ? "Next threshold: "+hubCleanLabel(next.label) : "Exact whole-chart packet ready";
  }
  function setHubBody(name){
    document.querySelectorAll("[data-hub-body]").forEach(function(button){button.classList.toggle("is-selected",button.dataset.hubBody===name);});
    if(name==="Earth"){updateHubMoment(currentDate);return;}
    var body=hubBodies[name];
    if(!body) return;
    document.getElementById("hub-story-kicker").textContent=body.k;
    document.getElementById("hub-story-title").textContent=body.t;
    document.getElementById("hub-story-text").textContent=body.p;
    document.getElementById("hub-story-meta").textContent=body.m;
  }
  function setHubMode(mode){
    var root=document.querySelector(".hub-orrery"),copy=hubModeCopy[mode]||hubModeCopy.sky;
    if(!root) return;
    root.dataset.hubMode=mode;
    document.querySelectorAll("[data-hub-mode-button]").forEach(function(button){button.setAttribute("aria-pressed",button.dataset.hubModeButton===mode?"true":"false");});
    document.getElementById("hub-live-eyebrow").textContent=copy.e;
    document.getElementById("hub-live-title").textContent=copy.t;
    document.getElementById("hub-live-deck").textContent=copy.d;
    if(mode==="story") setHubBody("Mars");
    else if(mode==="sky") setHubBody("Earth");
    else{setHubBody("Earth");document.getElementById("hubExplore").scrollIntoView({behavior:"smooth",block:"start"});}
  }

  function resolveSub(value){
    if(value==null) return null;
    var key=String(value).trim().toLowerCase();
    return bySub[key] ? key : (aliases[key]||null);
  }
  function frameFor(sub){
    var view=document.querySelector('.sky-view[data-sky-id="'+sub+'"]');
    return view ? view.querySelector('iframe[data-sky-id="'+sub+'"]') : null;
  }
  function sourceSub(source){
    for(var i=0;i<registry.length;i+=1){
      var frame=frameFor(registry[i].sub);
      if(frame && frame.contentWindow===source) return registry[i].sub;
    }
    return null;
  }
  function parentPost(message){
    if(window.parent===window) return;
    try{window.parent.postMessage(message,"*");}catch(_){}
  }
  function sendFrame(frame,message){
    if(!frame || !frame.contentWindow) return;
    try{frame.contentWindow.postMessage(message,"*");}catch(_){}
  }
  function postToSub(sub,message){
    var frame=frameFor(sub);
    if(!frame) return;
    if(!frame.getAttribute("src")){
      (pendingBySub[sub]||(pendingBySub[sub]=[])).push(message);
      loadFrame(sub);
      return;
    }
    sendFrame(frame,message);
  }
  function translatedDate(tool,date){
    return tool.dateAction && date ? {action:tool.dateAction,date:date} : null;
  }
  function hydrateFrame(sub){
    var tool=bySub[sub],frame=frameFor(sub);
    if(!tool || !frame) return;
    sendFrame(frame,{action:"setTheme",theme:currentTheme});
    var dateMessage=translatedDate(tool,currentDate);
    if(dateMessage) sendFrame(frame,dateMessage);
    (pendingBySub[sub]||[]).splice(0).forEach(function(message){sendFrame(frame,message);});
    sendFrame(frame,{action:"redraw"});
  }
  function loadFrame(sub){
    var frame=frameFor(sub);
    if(!frame || frame.getAttribute("src")) return frame;
    frame.addEventListener("load",function(){hydrateFrame(sub);},{once:true});
    frame.setAttribute("src",frame.dataset.src);
    return frame;
  }
  function announce(tool){
    parentPost({
      action:"hostSubChanged",host:HOST_ID,sub:tool.sub,
      legacyView:tool.legacyView,label:tool.label
    });
  }
  function setDrawer(open){
    document.body.classList.toggle("sky-drawer-open",!!open);
    menu.setAttribute("aria-expanded",open ? "true" : "false");
    if(open){
      lastDrawerFocus=document.activeElement;
      setTimeout(function(){
        var active=nav.querySelector(".sky-tool.active");
        (active||search).focus();
      },0);
    }else if(lastDrawerFocus && document.contains(lastDrawerFocus)){
      lastDrawerFocus.focus();
      lastDrawerFocus=null;
    }
  }
  function activate(value,options){
    options=options||{};
    var requestedKey=value==null ? "" : String(value).trim().toLowerCase();
    var requestedTarget=routeTargets[requestedKey];
    if(requestedTarget && !options.innerSub) options.innerSub=requestedTarget.innerSub;
    var sub=resolveSub(value);
    if(!sub) return false;
    var tool=bySub[sub];
    var changed=activeSub!==sub;
    activeSub=sub;

    document.querySelectorAll(".sky-tool[data-sky-id]").forEach(function(button){
      var on=button.dataset.skyId===sub;
      button.classList.toggle("active",on);
      if(on) button.setAttribute("aria-current","page");
      else button.removeAttribute("aria-current");
    });
    document.querySelectorAll(".sky-view[data-sky-id]").forEach(function(view){
      view.hidden=view.dataset.skyId!==sub;
    });
    crumbSection.textContent=tool.section;
    crumbTool.textContent=tool.label;
    document.title=tool.label+" — Astrology Hub";
    try{localStorage.setItem(LAST_KEY,sub);}catch(_){}

    if(options.date){
      currentDate=options.date;
      updateHubMoment(currentDate);
    }
    var frame=frameFor(sub),wasUnloaded=!!(frame && !frame.getAttribute("src"));
    if(wasUnloaded && options.message){
      (pendingBySub[sub]||(pendingBySub[sub]=[])).push(options.message);
    }
    loadFrame(sub);
    if(!wasUnloaded){
      if(options.date){
        var dateMessage=translatedDate(tool,currentDate);
        if(dateMessage) postToSub(sub,dateMessage);
      }
      if(options.message) postToSub(sub,options.message);
    }
    setTimeout(function(){postToSub(sub,{action:"redraw"});},changed ? 40 : 0);
    if(options.closeDrawer!==false && window.matchMedia("(max-width:900px)").matches) setDrawer(false);
    if(changed || options.announce!==false) announce(tool);
    return true;
  }
  function applyTheme(theme){
    currentTheme=theme==="dark" ? "dark" : "light";
    document.documentElement.setAttribute("data-theme",currentTheme);
    try{localStorage.setItem(THEME_KEY,currentTheme);}catch(_){}
    registry.forEach(function(tool){
      var frame=frameFor(tool.sub);
      if(frame && frame.getAttribute("src")) sendFrame(frame,{action:"setTheme",theme:currentTheme});
    });
  }
  function applyDate(date,excludeSub){
    if(!date) return;
    currentDate=date;
    updateHubMoment(currentDate);
    registry.forEach(function(tool){
      if(tool.sub===excludeSub || !tool.dateAction) return;
      var frame=frameFor(tool.sub);
      if(frame && frame.getAttribute("src")) sendFrame(frame,{action:tool.dateAction,date:date});
    });
    var active=bySub[activeSub];
    if(active && active.sub!==excludeSub && active.dateAction){
      var activeFrame=frameFor(active.sub);
      if(activeFrame && !activeFrame.getAttribute("src")) postToSub(active.sub,{action:active.dateAction,date:date});
    }
  }
  function publicRegistry(){
    return registry.map(function(tool){
      return {
        id:tool.id,host:tool.host,sub:tool.sub,legacyView:tool.legacyView,
        legacyViews:(tool.legacyViews||[]).slice(),label:tool.label,
        section:tool.section,sectionId:tool.sectionId,filename:tool.filename,
        aliases:(tool.aliases||[]).slice(),absorbedRoutes:Object.assign({},tool.absorbedRoutes||{}),dateAction:tool.dateAction,
        description:tool.description
      };
    });
  }
  function announceRegistry(action,requestId){
    var message={action:action,host:HOST_ID,tools:publicRegistry()};
    if(requestId!==undefined) message.requestId=requestId;
    parentPost(message);
  }
  function routeOptions(message){
    var forwarded={};
    Object.keys(message).forEach(function(key){
      if(key!=="action" && key!=="sub" && key!=="tab" && key!=="host" && key!=="innerSub") forwarded[key]=message[key];
    });
    return forwarded;
  }
  function childRouteMessage(message){
    var childMessage=routeOptions(message);
    delete childMessage.date; // activate() translates the governed date once.
    if(message.innerSub){
      var nested={action:"goToSub",sub:message.innerSub};
      if(message.date) nested.date=message.date;
      if(Object.keys(childMessage).length) nested.childMessage=childMessage;
      return nested;
    }
    if(childMessage.childAction){
      childMessage.action=childMessage.childAction;
      delete childMessage.childAction;
    }
    return Object.keys(childMessage).length ? childMessage : null;
  }
  function isDateMessage(message){
    return !!(message && message.date &&
      ["setDate","dateChanged","goToDate","scrollToDate"].indexOf(message.action)>=0);
  }
  function handleParentMessage(message){
    if(!message || typeof message!=="object") return;
    if(message.action==="getToolRegistry"){
      announceRegistry("toolRegistry",message.requestId);
      return;
    }
    if(message.action==="goToSub"){
      activate(message.sub,{date:message.date,innerSub:message.innerSub,message:childRouteMessage(message)});
      return;
    }
    if(message.action==="setTheme"){
      applyTheme(message.theme);
      return;
    }
    if(message.action==="redraw"){
      postToSub(activeSub,message);
      return;
    }
    if(message.action==="escape"){
      if(document.body.classList.contains("sky-drawer-open")) setDrawer(false);
      else postToSub(activeSub,message);
      return;
    }
    if(isDateMessage(message)){
      applyDate(message.date,null);
      return;
    }
    // Route legacy sky tabs sent as ordinary shell navigation.
    if(message.action==="navigateTo" && resolveSub(message.tab)){
      activate(message.tab,{date:message.date,message:childRouteMessage(message)});
      return;
    }
    // All non-host controls, including {type:"astromap",chart}, reach the
    // active child unchanged.
    postToSub(activeSub,message);
  }
  function handleChildMessage(message,childSub){
    if(!message || typeof message!=="object") return;
    if(message.action==="navigateTo" && resolveSub(message.tab)){
      activate(message.tab,{date:message.date,message:childRouteMessage(message)});
      return;
    }
    if(message.action==="goToMap" && message.chart){
      activate("astro-map",{message:{type:"astromap",chart:message.chart}});
      return;
    }
    if(message.type==="goToArc" && message.arc){
      parentPost({action:"navigateTo",tab:"obs-cm",arc:message.arc});
      return;
    }
    if(message.action==="dateChanged" && message.date){
      currentDate=message.date;
      parentPost(message);
      return;
    }
    parentPost(message);
  }
  function filterTools(query){
    var needle=String(query||"").trim().toLowerCase();
    var visible=0;
    document.querySelectorAll(".sky-section").forEach(function(section){
      var sectionVisible=0;
      section.querySelectorAll(".sky-tool").forEach(function(button){
        var match=!needle || button.dataset.search.indexOf(needle)>=0;
        button.hidden=!match;
        if(match){sectionVisible+=1;visible+=1;}
      });
      section.hidden=sectionVisible===0;
    });
    empty.classList.toggle("visible",visible===0);
  }
  function visibleButtons(){
    return Array.prototype.slice.call(nav.querySelectorAll(".sky-tool:not([hidden])"))
      .filter(function(button){return !button.closest(".sky-section").hidden;});
  }
  function moveButtonFocus(current,delta){
    var buttons=visibleButtons();
    if(!buttons.length) return;
    var index=buttons.indexOf(current);
    index=index<0 ? 0 : (index+delta+buttons.length)%buttons.length;
    buttons[index].focus();
  }

  nav.addEventListener("click",function(event){
    var button=event.target.closest(".sky-tool[data-sky-id]");
    if(button) activate(button.dataset.skyId);
  });
  stage.addEventListener("click",function(event){
    var modeButton=event.target.closest("[data-hub-mode-button]");
    if(modeButton){setHubMode(modeButton.dataset.hubModeButton);return;}
    var bodyButton=event.target.closest("[data-hub-body]");
    if(bodyButton){setHubBody(bodyButton.dataset.hubBody);return;}
    var orreryButton=event.target.closest("[data-open-orrery]");
    if(orreryButton){
      activate("transit-weather",{message:{action:"goToSub",sub:"orrery"}});
      return;
    }
    var exploreButton=event.target.closest("[data-scroll-explore]");
    if(exploreButton){setHubMode("explore");return;}
    var nextReadingButton=event.target.closest("[data-hub-next-reading]");
    if(nextReadingButton && nextReadingButton.dataset.chartId){
      activate("chart-readings",{
        message:{action:"selectReading",chart_id:nextReadingButton.dataset.chartId}
      });
      return;
    }
    var readingButton=event.target.closest("[data-open-reading]");
    if(readingButton){
      activate("chart-readings",{
        message:{action:"selectReading",chart_id:readingButton.dataset.openReading}
      });
      return;
    }
    var subButton=event.target.closest("[data-open-sub]");
    if(subButton){activate(subButton.dataset.openSub);return;}
    var documentButton=event.target.closest("[data-open-document]");
    if(documentButton){
      activate("astrology-reference-room",{
        message:{action:"openAstrologyDocument",path:documentButton.dataset.openDocument}
      });
    }
  });
  nav.addEventListener("keydown",function(event){
    var button=event.target.closest(".sky-tool[data-sky-id]");
    if(!button) return;
    if(event.key==="ArrowDown"){event.preventDefault();moveButtonFocus(button,1);}
    else if(event.key==="ArrowUp"){event.preventDefault();moveButtonFocus(button,-1);}
    else if(event.key==="Home"){event.preventDefault();var buttons=visibleButtons();if(buttons[0])buttons[0].focus();}
    else if(event.key==="End"){event.preventDefault();var buttons=visibleButtons();if(buttons.length)buttons[buttons.length-1].focus();}
  });
  search.addEventListener("input",function(){filterTools(search.value);});
  menu.addEventListener("click",function(){setDrawer(true);});
  closeButton.addEventListener("click",function(){setDrawer(false);});
  backdrop.addEventListener("click",function(){setDrawer(false);});
  document.addEventListener("keydown",function(event){
    if(event.key==="/" && !event.metaKey && !event.ctrlKey && !event.altKey &&
       !/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)){
      event.preventDefault();
      if(window.matchMedia("(max-width:900px)").matches) setDrawer(true);
      search.focus();
      return;
    }
    if(event.key==="Escape"){
      if(document.body.classList.contains("sky-drawer-open")){setDrawer(false);return;}
      if(document.activeElement===search && search.value){search.value="";filterTools("");return;}
      postToSub(activeSub,{action:"escape"});
      return;
    }
    if(event.altKey && (event.key==="ArrowDown" || event.key==="ArrowUp")){
      event.preventDefault();
      var buttons=visibleButtons();
      var index=registry.findIndex(function(tool){return tool.sub===activeSub;});
      var next=index+(event.key==="ArrowDown" ? 1 : -1);
      next=(next+registry.length)%registry.length;
      activate(registry[next].sub);
    }
  });
  window.addEventListener("message",function(event){
    var childSub=sourceSub(event.source);
    if(childSub){handleChildMessage(event.data,childSub);return;}
    if(window.parent!==window && event.source===window.parent) handleParentMessage(event.data);
  });
  window.addEventListener("resize",function(){
    if(!window.matchMedia("(max-width:900px)").matches) setDrawer(false);
    postToSub(activeSub,{action:"redraw"});
  });

  window.F250SkyCharts={
    host:HOST_ID,
    open:function(sub,options){return activate(sub,options||{});},
    active:function(){return activeSub;},
    getRegistry:publicRegistry
  };

  // Same-origin children historically call shell functions directly through
  // `window.parent`. Preserve that API boundary while this wrapper is nested.
  // Sky destinations stay inside the host; all other destinations bubble to
  // the real shell as the same postMessage routes it already understands.
  window.navigateTo=function(tab,options){
    options=options||{};
    if(resolveSub(tab)){
      var forwarded=Object.assign({},options);
      var date=forwarded.date;
      delete forwarded.date;
      if(resolveSub(tab)==="astro-map" && forwarded.chart && !forwarded.type){
        forwarded.type="astromap";
      }
      if(forwarded.childAction){
        forwarded.action=forwarded.childAction;
        delete forwarded.childAction;
      }
      activate(tab,{
        date:date,
        message:Object.keys(forwarded).length ? forwarded : null
      });
      return;
    }
    parentPost(Object.assign({action:"navigateTo",tab:tab},options));
  };
  window._switchTab=function(tab){window.navigateTo(tab,{});};
  window.goToArc=function(arc){parentPost({action:"navigateTo",tab:"obs-cm",arc:arc});};
  window.goToSubplot=function(subplot){parentPost({action:"navigateTo",tab:"obs-sm",subplot:subplot});};
  window.goToPlotline=function(plotline){parentPost({action:"navigateTo",tab:"obs-sm",plotline:plotline});};
  window.goToMonth=function(month){parentPost({action:"navigateTo",tab:"obs-mt",scrollToMonth:month});};
  window.goToDay=function(date){parentPost({action:"navigateTo",tab:"obs-df",date:date});};
  window.goToSky=function(date){activate("sky-calendar",{date:date});};
  window.goToMap=function(chart){activate("astro-map",{message:{type:"astromap",chart:chart}});};
  window.goToMoneyMachine=function(seed){parentPost({action:"goToMoneyMachine",date:seed});};
  window.goToHearing=function(index){parentPost({action:"navigateTo",tab:"obs-hr",hearing:index});};
  window.goToThread=function(id){parentPost({action:"navigateTo",tab:"obs-th",thread:id});};
  window.goToThreeMachines=function(){parentPost({action:"navigateTo",tab:"obs-3m"});};
  window.goToResearch=function(id){parentPost({action:"goToResearch",id:id});};
  window.goToFederalGroup=function(entity){
    parentPost(entity?{action:"goToFederalGroup",entity:entity}:{action:"goToFederalGroup"});
  };

  try{currentTheme=localStorage.getItem(THEME_KEY)||"light";}catch(_){}
  applyTheme(currentTheme);
  updateHubMoment(null);
  setHubBody("Earth");
  var saved=registry[0].sub;
  try{saved=resolveSub(localStorage.getItem(LAST_KEY))||saved;}catch(_){}
  activate(saved,{closeDrawer:false});
  announceRegistry("registerTools");
  setTimeout(function(){announceRegistry("registerTools");},250);
})();
</script>
</body>
</html>
"""


def render() -> str:
    registry_json = js_safe_json(shell_registry(), indent=2)
    result = HTML_TEMPLATE
    replacements = {
        "__INSTRUMENT_COUNT__": str(sum(1 for tool in SUBVIEWS if tool["filename"] is not None)),
        "__SECTIONS__": build_sections(),
        "__VIEWS__": build_views(),
        "__REGISTRY__": registry_json,
        "__HOST_ID__": js_safe_json(HOST_ID),
        "__LAST_KEY__": js_safe_json(LAST_SUBVIEW_KEY),
        "__THEME_KEY__": js_safe_json(THEME_KEY),
    }
    for marker, value in replacements.items():
        if marker not in result:
            fail(f"template marker absent: {marker}")
        result = result.replace(marker, value)
    if "__" in result:
        unresolved = sorted(
            {part.split("__", 1)[0] for part in result.split("__")[1::2] if part}
        )
        fail(f"unresolved template marker near {unresolved[:3]}")
    return result


def strip_shared_projection_blocks(content: str) -> str:
    """Compare the owned host while tolerating downstream shared injectors."""
    for start, end in (
        ("<!-- F250-DARKMODE-START -->", "<!-- F250-DARKMODE-END -->"),
        ("<!--F250-INTERP-START-->", "<!--F250-INTERP-END-->"),
    ):
        content = re.sub(re.escape(start) + r".*?" + re.escape(end), "", content, flags=re.S)
    return re.sub(r"\n{2,}(?=</body>)", "\n", content)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=CROSS_CUTS_DIR / OUTPUT_NAME,
        help=f"generated host path (default: vault Cross-cuts/{OUTPUT_NAME})",
    )
    parser.add_argument(
        "--source-dir",
        type=Path,
        default=CROSS_CUTS_DIR,
        help="Cross-cuts directory used to validate every child iframe target",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit nonzero if --output differs from a fresh render; do not write",
    )
    parser.add_argument(
        "--print-registry",
        action="store_true",
        help="print the shell-discovery registry as JSON and exit",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    source_dir = args.source_dir.resolve() if args.source_dir else None
    validate_registry(source_dir)

    if args.print_registry:
        print(json.dumps(shell_registry(), ensure_ascii=False, indent=2))
        return 0

    content = render()
    output = args.output.resolve()
    if args.check:
        if not output.is_file():
            print(f"Astrology Hub check FAILED: missing {output}", file=sys.stderr)
            return 1
        current = strip_shared_projection_blocks(output.read_text(encoding="utf-8"))
        if current.strip() != content.strip():
            print(f"Astrology Hub check FAILED: stale {output}", file=sys.stderr)
            return 1
        print(f"Astrology Hub check OK: 1 orientation + {len(SUBVIEWS) - 1} instruments · {output}")
        return 0

    atomic_write_text(output, content)
    print(
        f"Built {output} · 1 orientation + {len(SUBVIEWS) - 1} instruments · {len(SECTIONS)} sections"
        + (f" · sources validated in {source_dir}" if source_dir else "")
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
