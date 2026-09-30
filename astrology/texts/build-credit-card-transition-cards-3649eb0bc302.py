#!/usr/bin/env python3
"""Build the Observatory-native credit-card transition astrology card plot."""

from __future__ import annotations

import hashlib
import html
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path


HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent
CARDS_PATH = HERE / "credit_card_transition_cards.json"
ASTRO_PATH = PACKAGE / "CREDIT_CARD_TRANSITION_ASTROLOGY_DATA_2026-07-28.json"
US_PATH = HERE / "vendor" / "us_rec.json"
WHEEL_PATH = HERE / "vendor" / "wheel_lib.py"
OUT_PATH = HERE / "outputs" / "Credit Card Transition — Money × Sky.html"
MANIFEST_PATH = HERE / "outputs" / "build_manifest.json"

_wlspec = importlib.util.spec_from_file_location("wheel_lib", WHEEL_PATH)
wheel_lib = importlib.util.module_from_spec(_wlspec)
assert _wlspec.loader
_wlspec.loader.exec_module(wheel_lib)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump_for_script(value) -> str:
    return json.dumps(value, ensure_ascii=False).replace("</", "<\\/")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def wheel_name(name: str) -> str:
    return "Node" if name == "True Node" else name


def pos_tuple(name: str, record: dict) -> list:
    longitude = float(record["longitude"])
    degree = int(longitude % 30)
    minute = int(round(((longitude % 30) - degree) * 60))
    if minute == 60:
        degree += 1
        minute = 0
    return [
        wheel_name(name),
        record["position"].split("° ", 1)[1],
        f"{degree}°{minute:02d}'",
        bool(record.get("retrograde")),
        longitude,
    ]


def event_wheel_record(event: dict, context_key: str = "contextual_container_clock") -> dict:
    context = event[context_key]
    lons = {
        wheel_name(name): float(value["longitude"])
        for name, value in context["positions"].items()
    }
    planet_lons = {
        name: longitude
        for name, longitude in lons.items()
        if name not in {"Chiron", "Node", "SNode", "America"}
    }
    aspects = wheel_lib.aspects_between(planet_lons)
    for point in ("Node", "Chiron", "America"):
        if point in lons:
            aspects += wheel_lib.point_aspects({point: lons[point]}, planet_lons)
    aspects.sort(key=lambda item: item["o"])
    return {
        "pos": [pos_tuple(name, value) for name, value in context["positions"].items()],
        "asp": aspects,
        "asc": float(context["ascendant"]["longitude"]),
        "__date": context.get("display", context["local"]),
        "cap1": context.get(
            "cap1",
            f"{event['label']} · {context['local']}",
        ),
        "cap2": context.get(
            "cap2",
            "Whole Sign · explicitly classified research clock",
        ),
        "mc": float(context["mc"]["longitude"]),
    }


def geometry_html(event: dict) -> str:
    parts = []
    for hit in event.get("outer_cycles", [])[:4]:
        parts.append(
            f"<li><b>{html.escape(hit['pair'])}</b> {html.escape(hit['aspect'])}"
            f" <span>{hit['orb']:.2f}°</span></li>"
        )
    for hit in event.get("us_money_axis_hits", [])[:5]:
        parts.append(
            f"<li><b>{html.escape(hit['transit'])}</b> {html.escape(hit['aspect'])} "
            f"U.S. {html.escape(hit['natal'])} <span>{hit['orb']:.2f}° · "
            f"{html.escape(hit['state'])}</span></li>"
        )
    for hit in event.get("us_money_midpoint_hits", [])[:4]:
        parts.append(
            f"<li><b>{html.escape(hit['transit'])}</b> {hit['harmonic_angle']}° "
            f"U.S. {html.escape(hit['midpoint'])} midpoint "
            f"<span>{hit['orb']:.2f}°</span></li>"
        )
    for hit in event.get("minor_point_aspects", [])[:4]:
        parts.append(
            f"<li><b>{html.escape(hit['point'])}</b> {html.escape(hit['aspect'])} "
            f"{html.escape(hit['planet'])} <span>{hit['orb']:.2f}°</span></li>"
        )
    if event.get("contextual_container_clock"):
        context = event["contextual_container_clock"]
        for hit in context["angle_contacts"]:
            parts.insert(
                0,
                f"<li><b>{html.escape(hit['planet'])}</b> "
                f"{html.escape(hit['aspect'])} {html.escape(hit['angle'])} "
                f"<span>{hit['orb']:.2f}°</span></li>",
            )
        for hit in context["aspects"][:5]:
            parts.insert(
                1,
                f"<li><b>{html.escape(hit['pair'])}</b> {html.escape(hit['aspect'])} "
                f"<span>{hit['orb']:.2f}° · {html.escape(hit['state'])}</span></li>",
            )
    if not parts:
        return (
            '<p class="withheld">No point geometry. This chronology band is intentionally '
            "not charted.</p>"
        )
    return "<ul class=\"geometry\">" + "".join(parts) + "</ul>"


def buildup_html(items: list[dict]) -> str:
    return "".join(
        '<div class="stage"><div class="sdate">'
        + html.escape(item["date"])
        + '</div><div class="slab"><div class="stag">'
        + html.escape(item["label"])
        + '</div><div class="snote">'
        + html.escape(item["note"])
        + "</div></div></div>"
        for item in items
    )


def render(cards: dict, astro: dict, us_rec: dict) -> str:
    events = {event["id"]: event for event in astro["events"]}
    tracks = cards["tracks"]
    overlays = {}
    chart_records = {}
    merged_cards = []
    for card in cards["cards"]:
        event = events[card["id"]]
        merged = {**card, "event": event}
        merged_cards.append(merged)
        if event.get("positions"):
            if event.get("contextual_container_clock"):
                context = event["contextual_container_clock"]
                chart_records[card["id"]] = {
                    "mode": "event",
                    "record": event_wheel_record(event),
                    "caption": context.get(
                        "caption",
                        "Event chart; use the visible clock boundary before reading angles or houses.",
                    ),
                }
                if event.get("dc_companion_clock"):
                    dc_context = event["dc_companion_clock"]
                    chart_records[f"{card['id']}__dc"] = {
                        "mode": "event",
                        "record": event_wheel_record(event, "dc_companion_clock"),
                        "caption": dc_context.get(
                            "caption",
                            "Washington, D.C. relocation companion at the same instant.",
                        ),
                    }
            else:
                overlays[card["id"]] = {
                    wheel_name(name): float(value["longitude"])
                    for name, value in event["positions"].items()
                }
                chart_records[card["id"]] = {"mode": "us-overlay"}

    track_css = "\n".join(
        f".t-{key} .card{{border-left-color:{meta['color']}}}"
        f" .t-{key} .tk{{background:{meta['color']}22;color:{meta['color']};"
        f"border:1px solid {meta['color']}55}}"
        f" .chip[data-track=\"{key}\"].on{{background:{meta['color']}33;"
        f"border-color:{meta['color']};color:#eee}}"
        for key, meta in tracks.items()
    )
    legend = "".join(
        '<div class="leg t-'
        + html.escape(key)
        + '"><span class="tk">'
        + html.escape(meta["label"])
        + "</span><p>"
        + html.escape(meta["description"])
        + "</p></div>"
        for key, meta in tracks.items()
    )
    track_chips = "".join(
        '<button class="chip on" data-track="'
        + html.escape(key)
        + '">'
        + html.escape(meta["label"])
        + "</button>"
        for key, meta in tracks.items()
    )

    entries = []
    last_year = None
    for card in merged_cards:
        event = card["event"]
        year = event["date"][:4]
        if year != last_year:
            entries.append(f'<div class="yr">{html.escape(year)}</div>')
            last_year = year
        chartable = card["id"] in chart_records
        quality = event.get(
            "chart_quality",
            "context chart"
            if event.get("contextual_container_clock")
            else "planetary proxy"
            if chartable
            else "chronology only",
        )
        chart_buttons = []
        if chartable:
            chart_buttons.append(
                f'<button class="cbtn" data-chart="{html.escape(card["id"])}" '
                f'data-slot="{html.escape(card["id"])}" data-label="local chart">'
                "local chart ▾</button>"
            )
            if event.get("dc_companion_clock"):
                chart_buttons.append(
                    f'<button class="cbtn" data-chart="{html.escape(card["id"])}__dc" '
                    f'data-slot="{html.escape(card["id"])}" data-label="D.C. companion">'
                    "D.C. companion ▾</button>"
                )
        chart_button = "".join(chart_buttons)
        source_links = [
            f'<a href="{html.escape(event["source"])}" target="_blank" '
            f'rel="noopener">primary / controlling source</a>'
        ]
        if event.get("source_secondary"):
            source_links.append(
                f'<a href="{html.escape(event["source_secondary"])}" target="_blank" '
                f'rel="noopener">supporting source</a>'
            )
        entries.append(
            f"""<article class="entry t-{html.escape(card['track'])}" data-track="{html.escape(card['track'])}">
  <div class="d">{html.escape(card['date_display'])}</div>
  <div class="card">
    <div class="meta">
      <span class="tk">{html.escape(tracks[card['track']]['label'])}</span>
      <span class="actor">{html.escape(card['actor'])}</span>
      <span class="st st-occurred">occurred</span>
      <span class="clock">clock {html.escape(event['clock_grade'])}</span>
      <span class="quality">{html.escape(quality)}</span>
      {chart_button}
    </div>
    <h3>{html.escape(card['title'])}</h3>
    <p class="fact">{html.escape(card['factual'])}</p>
    <div class="sources">{' · '.join(source_links)}</div>
    <details class="dd">
      <summary>open buildup + reading</summary>
      <div class="block">
        <div class="blabel">The buildup</div>
        <div class="story">{buildup_html(card['buildup'])}</div>
      </div>
      <div class="block qblock">
        <div class="blabel">The historical question</div>
        <p>{html.escape(card['question'])}</p>
      </div>
      <div class="block">
        <div class="blabel">Exact geometry shown</div>
        {geometry_html(event)}
      </div>
      <div class="block reading">
        <div class="blabel">Structural reading · symbolic, not causal</div>
        <p>{html.escape(card['reading'])}</p>
      </div>
      <div class="block caveat">
        <div class="blabel">Counterweight / provenance</div>
        <p>{html.escape(card['counterweight'])}</p>
        <p class="boundary">{html.escape(event['boundary'])}</p>
      </div>
    </details>
    <div class="astro-slot" data-slot="{html.escape(card['id'])}"></div>
  </div>
</article>"""
        )

    tests_plus = "".join(f"<li>{html.escape(item)}</li>" for item in cards["tests"]["strengthens"])
    tests_minus = "".join(f"<li>{html.escape(item)}</li>" for item in cards["tests"]["weakens"])
    findings = cards.get(
        "findings",
        [
            {"title": "1958 · credential", "text": "A bank promise becomes portable before it becomes electronic."},
            {"title": "1966–74 · control plane", "text": "Shared rules, authorization and settlement turn the card into a network."},
            {"title": "2014 · adapter", "text": "Apple Pay changes the presented credential while preserving card rails."},
            {"title": "2025 · deeper swap", "text": "Stablecoin can enter settlement behind an unchanged acceptance surface."},
        ],
    )
    findings_html = "".join(
        '<div class="finding"><div class="n">'
        + html.escape(item["title"])
        + "</div><p>"
        + html.escape(item["text"])
        + "</p></div>"
        for item in findings
    )
    method = cards.get("method")
    if method:
        method_paragraph = html.escape(method["paragraph"])
        method_items = "".join(f"<li>{html.escape(item)}</li>" for item in method["items"])
    else:
        method_paragraph = (
            "Geocentric tropical Swiss Ephemeris; locked U.S. Sagittarius-rising chart "
            "(2 July 1776, ~5:10 p.m. LMT, Philadelphia); Whole Sign houses on the locked chart. "
            "Day-only anchors use 12:00 UTC solely to place planets on the zodiac. Their event "
            "angles and houses are withheld. Apple Pay’s reported ~10:47 a.m. PDT reveal frame is "
            "the sole context chart; the 1986–87 securitization band is not charted."
        )
        method_items = "".join(
            f"<li>{html.escape(item)}</li>"
            for item in [
                "Outer-to-U.S. money-axis contacts: 3°; mod-45 money midpoints: 1.5°.",
                "Outer mutual aspects are descriptive background, not an event score.",
                "Cross-event repeats are not independent observations; several dates belong to one historical build.",
                "The project’s own daily backtest was null. No concrete causation, destiny or timing prediction is claimed.",
                "The 916 America point is unavailable for these historical dates and is not extrapolated.",
            ]
        )
    event_data = dump_for_script(
        [
            {
                "id": card["id"],
                "track": card["track"],
                "actor": card["actor"],
                "title": card["title"],
                "date": card["date_display"],
            }
            for card in merged_cards
        ]
    )
    records_data = dump_for_script(chart_records)
    overlay_data = dump_for_script(overlays)
    us_data = dump_for_script(us_rec["sag"])

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(cards['title'])}</title>
<style>
:root{{--bg:#0e1116;--panel:#161b24;--ink:#d6dae2;--dim:#8a93a3;--line:#2a3242;--accent:#c8a24a;--paper:#f6f2e8}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 -apple-system,'Segoe UI',Helvetica,Arial,sans-serif}}
.wrap{{max-width:1020px;margin:0 auto;padding:28px 20px 80px}}
header h1{{font-family:Georgia,serif;font-size:32px;margin:0 0 4px;color:#f0e9d8}}
header .thesis{{font-family:Georgia,serif;font-style:italic;color:var(--accent);font-size:17px;margin:2px 0 10px;max-width:82ch}}
header p.sub{{color:var(--dim);margin:0 0 18px;max-width:84ch}}
.finding-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:9px;margin:16px 0 22px}}
.finding{{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:11px 12px}}
.finding .n{{font-family:Georgia,serif;color:#f0e9d8;font-size:17px}}
.finding p{{color:var(--dim);font-size:12.5px;margin:4px 0 0}}
.legend{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:10px;margin:14px 0 22px}}
.leg{{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:10px 12px}}
.leg p{{margin:6px 0 0;color:var(--dim);font-size:13px}}
.tk{{display:inline-block;font-size:11px;letter-spacing:.06em;text-transform:uppercase;padding:2px 8px;border-radius:10px}}
.bar{{position:sticky;top:0;background:linear-gradient(var(--bg) 84%,transparent);padding:10px 0 14px;z-index:5}}
.chips{{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:6px}}
.chip{{background:#1a2130;border:1px solid var(--line);color:var(--dim);border-radius:14px;padding:3px 11px;font-size:12.5px;cursor:pointer}}
.chip.on{{color:#eee;border-color:#59657c;background:#232c3e}}
.count{{color:var(--dim);font-size:12.5px;margin-left:4px;align-self:center}}
.yr{{font-family:Georgia,serif;font-size:22px;color:#f0e9d8;border-bottom:1px solid var(--line);margin:30px 0 4px;padding-bottom:4px}}
.entry{{display:grid;grid-template-columns:130px 1fr;gap:14px;padding:10px 0}}
.entry .d{{color:var(--dim);font-size:12.5px;text-align:right;padding-top:14px;font-variant-numeric:tabular-nums}}
.card{{background:var(--panel);border:1px solid var(--line);border-left:3px solid #555;border-radius:8px;padding:12px 14px}}
.card h3{{margin:0 0 5px;font-size:16px;color:#e8ebf2;font-weight:600}}
.meta{{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin-bottom:7px}}
.actor,.clock,.quality{{font-size:11px;color:#c7cedb;background:#242e42;border-radius:10px;padding:2px 8px}}
.clock{{color:#d8c694;background:#2b281d}} .quality{{color:#9fb7d6;background:#1c2635}}
.st{{font-size:11px;border-radius:10px;padding:2px 8px;border:1px solid}}
.st-occurred{{color:#9fd6a9;border-color:#3d6b46}}
.fact{{margin:4px 0 6px;color:#aeb6c4;font-size:13.5px}}
.sources{{display:flex;flex-wrap:wrap;gap:4px;color:#667080;font-size:12px}}
.sources a{{color:#7fa8d9;text-decoration:none}} .sources a:hover{{text-decoration:underline}}
.dd{{margin-top:10px;border-top:1px solid #242d3d;padding-top:8px}}
.dd>summary{{cursor:pointer;color:#c8a24a;font-size:12px;letter-spacing:.02em;list-style:none}}
.dd>summary::-webkit-details-marker{{display:none}}
.dd>summary:before{{content:"＋ ";color:#7e8797}} .dd[open]>summary:before{{content:"− "}}
.block{{margin:11px 0 0;padding:10px 12px;background:#121720;border:1px solid #242d3d;border-radius:7px}}
.blabel{{font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:#8f9aac;margin-bottom:6px}}
.block p{{margin:0;color:#aeb6c4;font-size:13.2px}}
.qblock p{{font-family:Georgia,serif;font-style:italic;color:#d8dce5;font-size:14px}}
.reading{{border-color:#544729}} .caveat{{border-color:#493235}}
.boundary{{margin-top:7px!important;color:#7f8998!important;font-size:11.5px!important}}
.story{{display:grid;grid-template-columns:repeat(2,1fr);gap:8px}}
.stage{{display:grid;grid-template-columns:64px 1fr;gap:8px;align-items:start}}
.sdate{{font-family:Georgia,serif;color:#d4b65d;font-size:12px;padding-top:2px}}
.slab{{border-left:2px solid #3b465a;padding-left:9px}}
.stag{{color:#dbe0e9;font-size:12.5px;font-weight:600}} .snote{{color:#8f99aa;font-size:12px;margin-top:2px}}
.geometry{{margin:0;padding-left:18px;columns:2;column-gap:26px}}
.geometry li{{break-inside:avoid;color:#aeb6c4;font-size:12.5px;margin-bottom:4px}}
.geometry b{{color:#d9dee7;font-weight:600}} .geometry span{{color:#7f8999}}
.withheld{{font-style:italic;color:#8f99aa!important}}
.astro-slot{{margin-top:10px}}
.astro-wrap{{background:var(--paper);border-radius:8px;padding:8px}}
.astro-slot svg{{max-width:640px;width:100%;height:auto;margin:auto;background:var(--paper);border-radius:8px}}
.chart-cap{{color:#8f99aa;font-size:11.5px;margin:6px 3px 1px}}
.cbtn{{background:#1a2130;border:1px solid var(--line);color:#c8a24a;border-radius:12px;padding:2px 10px;font-size:11.5px;cursor:pointer;margin-left:auto}}
.tests{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:34px}}
.tests>div{{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:12px 16px}}
.tests h2{{font-family:Georgia,serif;font-size:17px;margin:0 0 8px}}
.tests .plus h2{{color:#9fd6a9}} .tests .minus h2{{color:#e0a48a}}
.tests li{{color:#aeb6c4;font-size:13px;margin-bottom:6px}}
.method{{margin-top:28px;background:#111720;border:1px solid var(--line);border-radius:8px;padding:13px 15px}}
.method h2{{font-family:Georgia,serif;font-size:17px;margin:0 0 6px;color:#ece5d3}}
.method p,.method li{{color:#929dac;font-size:12.5px}}
footer{{color:var(--dim);font-size:12px;margin-top:28px;border-top:1px solid var(--line);padding-top:10px}}
{track_css}
@media(max-width:760px){{.finding-grid{{grid-template-columns:1fr 1fr}}.entry{{grid-template-columns:1fr}}.entry .d{{text-align:left;padding-top:0}}.tests{{grid-template-columns:1fr}}}}
@media(max-width:520px){{.finding-grid,.story{{grid-template-columns:1fr}}.geometry{{columns:1}}}}
</style></head><body><div class="wrap">
<header>
  <h1>{html.escape(cards['title'])}</h1>
  <div class="thesis">{html.escape(cards['thesis'])}</div>
  <p class="sub">{html.escape(cards['method_note'])}</p>
</header>
<div class="finding-grid">
  {findings_html}
</div>
<div class="legend">{legend}</div>
<div class="bar"><div class="chips" id="trackChips">{track_chips}<span class="count" id="count"></span></div></div>
<main id="timeline">{''.join(entries)}</main>
<div class="tests">
  <div class="plus"><h2>{html.escape(cards["tests"].get("strengthens_title", "The adapter story gets stronger if…"))}</h2><ul>{tests_plus}</ul></div>
  <div class="minus"><h2>{html.escape(cards["tests"].get("weakens_title", "The adapter story weakens if…"))}</h2><ul>{tests_minus}</ul></div>
</div>
<section class="method">
  <h2>Clock and method discipline</h2>
  <p>{method_paragraph}</p>
  <ul>{method_items}</ul>
</section>
<footer>{html.escape(cards.get("footer", "Research-only Observatory card plot · factual chronology first · source and clock grade on every card"))} · generated {datetime.now(timezone.utc).strftime('%Y-%m-%d')}.</footer>
</div>
<script type="application/json" id="card-data">{event_data}</script>
<script type="application/json" id="chart-records">{records_data}</script>
<script type="application/json" id="chart-overlays">{overlay_data}</script>
<script type="application/json" id="us-record">{us_data}</script>
<script>{wheel_lib.WHEEL_JS}</script>
<script>
(function(){{
"use strict";
var DATA=JSON.parse(document.getElementById("card-data").textContent);
var RECORDS=JSON.parse(document.getElementById("chart-records").textContent);
var CHARTS_LOCAL=JSON.parse(document.getElementById("chart-overlays").textContent);
var US=JSON.parse(document.getElementById("us-record").textContent);
window.CHARTS=CHARTS_LOCAL;
var open={{}};
var active={{}};
document.querySelectorAll("[data-track]").forEach(function(node){{
  if(node.classList.contains("chip")) active[node.dataset.track]=true;
}});
function updateCount(){{
  var shown=0;
  document.querySelectorAll(".entry").forEach(function(entry){{
    var yes=!!active[entry.dataset.track];
    entry.hidden=!yes;
    if(yes) shown++;
  }});
  document.querySelectorAll(".yr").forEach(function(year){{
    var next=year.nextElementSibling, any=false;
    while(next && !next.classList.contains("yr")){{
      if(next.classList.contains("entry") && !next.hidden) any=true;
      next=next.nextElementSibling;
    }}
    year.hidden=!any;
  }});
  document.getElementById("count").textContent=shown+" of "+DATA.length+" shown";
}}
function paint(id,slotId){{
  var slot=document.querySelector('.astro-slot[data-slot="'+CSS.escape(slotId)+'"]');
  var info=RECORDS[id];
  if(!slot||!info)return;
  var svg;
  if(info.mode==="event"){{
    svg=wheelSVG(info.record,null,false);
    slot.innerHTML='<div class="astro-wrap">'+svg+'</div><p class="chart-cap">'+info.caption+'</p>';
  }} else {{
    svg=wheelSVG(US,id,true);
    slot.innerHTML='<div class="astro-wrap">'+svg+'</div><p class="chart-cap">Locked U.S. chart inside · event-day planetary proxy outside. The inner houses belong to the U.S. chart; no event angles or houses are implied.</p>';
  }}
}}
document.addEventListener("click",function(ev){{
  var chart=ev.target.closest?ev.target.closest(".cbtn"):null;
  if(chart){{
    var id=chart.dataset.chart;
    var slotId=chart.dataset.slot||id;
    open[slotId]=open[slotId]===id?null:id;
    document.querySelectorAll('.cbtn[data-slot="'+CSS.escape(slotId)+'"]').forEach(function(btn){{
      var label=btn.dataset.label||"chart";
      btn.textContent=label+(open[slotId]===btn.dataset.chart?" ▴":" ▾");
    }});
    if(open[slotId])paint(id,slotId);
    else{{
      var slot=document.querySelector('.astro-slot[data-slot="'+CSS.escape(slotId)+'"]');
      if(slot)slot.innerHTML="";
    }}
    return;
  }}
  var chip=ev.target.closest?ev.target.closest(".chip[data-track]"):null;
  if(!chip)return;
  active[chip.dataset.track]=!active[chip.dataset.track];
  chip.classList.toggle("on",active[chip.dataset.track]);
  updateCount();
}});
updateCount();
}})();
</script>
</body></html>"""


def main() -> None:
    cards = read_json(CARDS_PATH)
    astro = read_json(ASTRO_PATH)
    us_rec = read_json(US_PATH)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    output = render(cards, astro, us_rec)
    OUT_PATH.write_text(output, encoding="utf-8")
    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "artifact": OUT_PATH.name,
        "artifact_sha256": sha256(OUT_PATH),
        "cards": len(cards["cards"]),
        "chartable_cards": sum(
            1 for event in astro["events"] if event.get("positions")
        ),
        "wheel_records": sum(
            1 + int(bool(event.get("dc_companion_clock")))
            for event in astro["events"]
            if event.get("positions")
        ),
        "chronology_only_cards": sum(
            1 for event in astro["events"] if not event.get("positions")
        ),
        "source_hashes": {
            CARDS_PATH.name: sha256(CARDS_PATH),
            ASTRO_PATH.name: sha256(ASTRO_PATH),
            "vendor/wheel_lib.py": sha256(WHEEL_PATH),
            "vendor/us_rec.json": sha256(US_PATH),
        },
        "wheel_engine": {
            "source": "Freedom 250 Chronicle/99 - Templates/wheel_lib.py",
            "sha256": sha256(WHEEL_PATH),
        },
        "boundaries": cards.get(
            "boundaries",
            [
                "Date-only cards are planetary longitude proxies; event angles and houses are withheld.",
                "Apple Pay uses a contemporaneously reported reveal minute with a ±2-minute boundary.",
                "The 1986–1987 securitization band is chronology-only.",
                "No astrological strength or similarity score is computed.",
            ],
        ),
    }
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {OUT_PATH} ({len(output) // 1024} KB)")
    print(f"wrote {MANIFEST_PATH}")


if __name__ == "__main__":
    main()
