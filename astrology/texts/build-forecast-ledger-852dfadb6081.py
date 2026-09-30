#!/usr/bin/env python3
"""Prediction Scorecard — named archetypes from the readings, scored by presence.

The predicted object is the motif named in a Pass 1 reading. Presence in
Attention (saved events), Official/Research (Research Desk packets, watches),
or Entity is a win. Seven-arc folder dominance is retired.

Literal DR-004 calls from forecast_curated.json remain a separate strip.
They are not mixed into the archetype presence rate.

Pessin harvests, mundane-engine one-arc triggers, and story-thread spike
tests are no longer generated here.
"""
from __future__ import annotations

import glob
import html
import json
import os
import re
from collections import Counter
from datetime import date as Date, datetime, timedelta
from pathlib import Path

from atomic_io import atomic_write_text

HERE = Path(__file__).resolve().parent
VAULT = HERE.parent
EVENTS = VAULT / "01 - Events"
OUTHTML = VAULT / "04 - Synthesis" / "Cross-cuts" / "Forecast Ledger.html"
LEDGER = HERE / "forecast_ledger.json"
WATCHLISTS = VAULT / "03 - Astrology" / "archetype_watch_lists.json"
CURATED = HERE / "forecast_curated.json"
WATCHCAL = HERE / "watch_calendar.json"
RESEARCH = HERE / "research_desk_data.json"

DISPOSITIONS = ("lines_up", "partial", "miss", "unresolved", "pending")
LABEL = {
    "lines_up": "Lines up",
    "partial": "Partial",
    "miss": "Miss",
    "unresolved": "Unresolved",
    "pending": "Pending",
}


def today_local() -> Date:
    return Date.today()


def parse_day(value: str | None) -> Date | None:
    if not value:
        return None
    text = str(value).strip()[:10]
    try:
        return Date.fromisoformat(text)
    except ValueError:
        pass
    for fmt in ("%b %d, %Y", "%B %d, %Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(str(value).strip()[:40], fmt).date()
        except ValueError:
            continue
    return None


def load_events():
    idx = {}
    for path in glob.glob(str(EVENTS / "2*.md")):
        day = os.path.basename(path)[:10]
        try:
            Date.fromisoformat(day)
        except ValueError:
            continue
        raw = open(path, encoding="utf-8", errors="ignore").read(2500)
        title_m = re.search(r'^title:\s*"?([^"\n]+)"?', raw, re.M)
        plot_m = re.search(r'primary_plotline:\s*"?([^"\n]+)"?', raw)
        sub_m = re.search(r'^subplot:\s*"([^"\n]+)"', raw, re.M)
        idx.setdefault(day, []).append({
            "date": day,
            "title": title_m.group(1).strip() if title_m else os.path.basename(path),
            "plot": plot_m.group(1).strip() if plot_m else "",
            "sub": sub_m.group(1).strip() if sub_m else "",
            "stem": os.path.splitext(os.path.basename(path))[0],
        })
    return idx


def load_packages():
    if not RESEARCH.exists():
        return []
    try:
        data = json.loads(RESEARCH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    out = []
    for pkg in data.get("packages") or []:
        if not isinstance(pkg, dict):
            continue
        rid = pkg.get("research_id") or pkg.get("primary_research_id")
        if not rid:
            continue
        out.append({
            "research_id": rid,
            "title": pkg.get("title") or rid,
            "lane": pkg.get("lane") or "",
            "question": pkg.get("question") or "",
            "bluf": pkg.get("bluf") or "",
            "cutoff": str(pkg.get("evidence_cutoff") or "")[:10],
        })
    return out


def load_watch_calendar():
    if not WATCHCAL.exists():
        return []
    try:
        data = json.loads(WATCHCAL.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    return [w for w in (data.get("entries") or data.get("watches") or []) if isinstance(w, dict)]


def load_watchlists():
    data = json.loads(WATCHLISTS.read_text(encoding="utf-8"))
    if data.get("schema") != "f250.archetype-presence/v1":
        raise SystemExit("archetype_watch_lists.json schema drifted")
    charts = data.get("charts") or []
    if not charts:
        raise SystemExit("archetype_watch_lists.json has no charts")
    return data


def in_window(day: str, start: str, end: str) -> bool:
    return bool(day and start <= day <= end)


def event_blob(ev: dict) -> str:
    return " ".join([ev.get("title", ""), ev.get("plot", ""), ev.get("sub", "")]).lower()


def motif_needles(motif: dict) -> list[str]:
    needles = [n.lower() for n in (motif.get("needles") or []) if n]
    needles += [s.lower() for s in (motif.get("subplots") or []) if s]
    return needles


def match_text(text: str, needles: list[str]) -> bool:
    hay = (text or "").lower()
    return any(n and n in hay for n in needles)


def collect_attention(idx: dict, start: str, end: str, motif: dict, limit: int = 6) -> list[dict]:
    subs = {s.lower() for s in (motif.get("subplots") or []) if s}
    needles = motif_needles(motif)
    hits = []
    counts = Counter()
    d0 = Date.fromisoformat(start)
    d1 = Date.fromisoformat(end)
    day = d0
    while day <= d1:
        key = day.isoformat()
        for ev in idx.get(key, []):
            blob = event_blob(ev)
            sub = (ev.get("sub") or "").lower()
            if sub in subs or match_text(blob, needles):
                counts[ev.get("sub") or ev.get("plot") or "note"] += 1
                if len(hits) < limit:
                    hits.append({
                        "lane": "Attention",
                        "date": ev["date"],
                        "label": ev["title"][:140],
                        "sub": ev.get("sub") or "",
                        "route": {"tab": "obs-df", "date": ev["date"]},
                    })
        day += timedelta(days=1)
    return hits, dict(counts)


def collect_official(packages: list, watches: list, start: str, end: str, motif: dict) -> list[dict]:
    hits = []
    wanted = set(motif.get("research_ids") or [])
    watch_ids = set(motif.get("watch_ids") or [])
    needles = motif_needles(motif)
    for pkg in packages:
        rid = pkg["research_id"]
        cutoff = pkg.get("cutoff") or ""
        in_ids = rid in wanted
        in_time = bool(cutoff) and in_window(cutoff, start, end)
        if in_ids or (in_time and match_text(pkg["title"] + " " + pkg.get("question", ""), needles)):
            hits.append({
                "lane": "Official",
                "date": cutoff or start,
                "label": pkg["title"],
                "kind": "research-packet",
                "research_id": rid,
                "route": {"tab": "obs-rd", "researchId": rid},
            })
    for watch in watches:
        wid = watch.get("watch_id") or ""
        wdate = str(watch.get("date") or "")[:10]
        wend = str(watch.get("end") or wdate)[:10]
        overlaps = wdate and not (wend < start or wdate > end)
        if wid in watch_ids or (overlaps and match_text(
            (watch.get("label") or "") + " " + (watch.get("detail") or ""), needles
        )):
            if not overlaps and wid not in watch_ids:
                continue
            hits.append({
                "lane": "Official",
                "date": wdate or start,
                "label": watch.get("label") or wid,
                "kind": "watch",
                "watch_id": wid,
                "route": {"tab": "obs-sd", "date": wdate or start},
            })
    # de-dupe by label+date
    seen = set()
    uniq = []
    for hit in hits:
        key = (hit.get("research_id") or hit.get("watch_id") or hit["label"], hit["date"])
        if key in seen:
            continue
        seen.add(key)
        uniq.append(hit)
    return uniq[:12]


def chart_disposition(motifs: list[dict]) -> str:
    statuses = [m["status"] for m in motifs]
    if any(s == "lines_up" for s in statuses):
        return "lines_up"
    if any(s == "partial" for s in statuses):
        return "partial"
    if any(s == "unresolved" for s in statuses):
        return "unresolved"
    if any(s == "miss" for s in statuses):
        return "miss"
    return "pending"


def score_charts(watchlists: dict, idx: dict, packages: list, watches: list, data_end: str):
    scored_charts = []
    for chart in watchlists.get("charts") or []:
        start = chart["window_start"]
        end = chart["window_end"]
        closed = end <= data_end
        motifs_out = []
        for motif in chart.get("motifs") or []:
            attention, counts = collect_attention(idx, start, end, motif)
            official = collect_official(packages, watches, start, end, motif)
            authored = motif.get("disposition")
            if authored in DISPOSITIONS:
                status = authored
            elif not closed:
                status = "pending"
            elif official or attention:
                status = "lines_up"
            else:
                status = "miss"
            if not closed and status != "pending" and authored not in DISPOSITIONS:
                status = "pending"
            motifs_out.append({
                "id": motif["id"],
                "chart_id": chart["id"],
                "reading_id": chart.get("reading_id"),
                "name": motif["name"],
                "poles": motif.get("poles") or {},
                "status": status,
                "note": motif.get("disposition_note") or "",
                "credit": chart.get("credit") or "calibration",
                "attention": attention,
                "official": official,
                "attention_counts": counts,
                "research_ids": motif.get("research_ids") or [],
                "window_start": start,
                "window_end": end,
                "window_center": chart.get("date") or start,
            })
        scored_charts.append({
            "id": chart["id"],
            "reading_id": chart.get("reading_id"),
            "kind": chart.get("kind"),
            "season": chart.get("season"),
            "label": chart.get("label"),
            "date": chart.get("date"),
            "window_start": start,
            "window_end": end,
            "credit": chart.get("credit") or "calibration",
            "question": chart.get("question") or "",
            "status": chart_disposition(motifs_out),
            "motifs": motifs_out,
        })
    return scored_charts


def score_literals(idx: dict, packages: list, watches: list, data_end: str):
    if not CURATED.exists():
        return []
    try:
        calls = json.loads(CURATED.read_text(encoding="utf-8")).get("calls") or []
    except (OSError, json.JSONDecodeError):
        return []
    out = []
    for call in calls:
        center = call.get("window_center")
        if not center:
            continue
        span = int(call.get("span") or 3)
        start = (Date.fromisoformat(center) - timedelta(days=span)).isoformat()
        end = (Date.fromisoformat(center) + timedelta(days=span)).isoformat()
        closed = end <= data_end
        sub = call.get("predicted_sub") or ""
        stop = {"that", "this", "with", "from", "have", "been", "into", "over", "under"}
        needles = [sub.lower()] if sub else []
        needles += [w for w in re.findall(r"[a-z0-9-]{4,}", sub.lower()) if w not in stop]
        n = 0
        d0 = Date.fromisoformat(start)
        d1 = Date.fromisoformat(end)
        day = d0
        while day <= d1:
            for ev in idx.get(day.isoformat(), []):
                if sub and (ev.get("sub") or "") == sub:
                    n += 1
                elif needles and match_text(event_blob(ev), needles):
                    n += 1
            day += timedelta(days=1)
        official = []
        fake_motif = {"needles": needles, "subplots": [sub] if sub else [], "research_ids": [], "watch_ids": []}
        official = collect_official(packages, watches, start, end, fake_motif)
        if not closed:
            status = "pending"
        elif n or official:
            status = "lines_up"
        else:
            status = "unresolved" if not sub else "miss"
        row = dict(call)
        row.update({
            "status": status,
            "actual_sub_n": n,
            "official_n": len(official),
            "window_start": start,
            "window_end": end,
            "call_class": "literal",
            "score_mode": "archetype_presence",
        })
        out.append(row)
    return out


def tally(charts: list) -> dict:
    motifs = [m for c in charts for m in c["motifs"]]
    def count(status, rows):
        return sum(1 for r in rows if r["status"] == status)
    scored = [m for m in motifs if m["status"] in ("lines_up", "partial", "miss", "unresolved")]
    charts_scored = [c for c in charts if c["status"] in ("lines_up", "partial", "miss", "unresolved")]
    prospective = [m for m in motifs if m.get("credit") == "prospective"]
    calibration = [m for m in motifs if m.get("credit") != "prospective"]

    def rate(rows, key="lines_up"):
        closed = [r for r in rows if r["status"] in ("lines_up", "partial", "miss", "unresolved")]
        if not closed:
            return None
        return sum(1 for r in closed if r["status"] == key) / len(closed)

    presence = rate(motifs)
    present_or_partial = None
    closed = [m for m in motifs if m["status"] in ("lines_up", "partial", "miss", "unresolved")]
    if closed:
        present_or_partial = sum(1 for m in closed if m["status"] in ("lines_up", "partial")) / len(closed)
    sc = {
        "method": "archetype_presence",
        "n_total": len(motifs),
        "scored": len(scored),
        "lines_up": count("lines_up", motifs),
        "partials": count("partial", motifs),
        "miss": count("miss", motifs),
        "unresolved": count("unresolved", motifs),
        "pending": count("pending", motifs),
        "presence_rate": presence,
        "present_or_partial_rate": present_or_partial,
        "chart_total": len(charts),
        "chart_scored": len(charts_scored),
        "chart_lines_up": count("lines_up", charts),
        "chart_pending": count("pending", charts),
        "prospective_scored": len([m for m in prospective if m["status"] in ("lines_up", "partial", "miss", "unresolved")]),
        "prospective_lines_up": count("lines_up", prospective),
        "calibration_scored": len([m for m in calibration if m["status"] in ("lines_up", "partial", "miss", "unresolved")]),
        "calibration_lines_up": count("lines_up", calibration),
        # Compatibility aliases for older primer/badge readers during the cutover.
        "hits": count("lines_up", motifs),
        "hit_rate": presence,
        "chance": None,
    }
    return sc, motifs


def pct(value) -> str:
    if value is None:
        return "—"
    return f"{value * 100:.0f}%"


def esc(value) -> str:
    return html.escape(str(value or ""), quote=True)


def evidence_html(items: list) -> str:
    if not items:
        return '<p class="muted">None retrieved in this window.</p>'
    bits = []
    for item in items:
        label = esc(item.get("label"))
        date = esc(item.get("date"))
        lane = esc(item.get("lane"))
        route = item.get("route") or {}
        tab = route.get("tab") or ""
        attrs = f'data-tab="{esc(tab)}"'
        if route.get("date"):
            attrs += f' data-date="{esc(route["date"])}"'
        if route.get("researchId"):
            attrs += f' data-research="{esc(route["researchId"])}"'
        bits.append(
            f'<button type="button" class="ev" {attrs}>'
            f'<span class="ev-lane">{lane}</span> {date} · {label}</button>'
        )
    return '<div class="ev-list">' + "".join(bits) + "</div>"


def render(charts: list, literals: list, sc: dict, data_end: str) -> str:
    css = """
*{box-sizing:border-box}
body{margin:0;padding:22px 22px 48px;font-family:-apple-system,Segoe UI,Roboto,sans-serif;
  background:#faf8f3;color:#2b2620;line-height:1.5}
h1{font-size:26px;margin:0 0 4px}
.sub{color:#7a6f60;margin:0 0 18px;font-size:14px;max-width:70rem}
.card{background:#fff;border:1px solid #e7e0d4;border-radius:12px;padding:16px 18px;margin-bottom:16px}
.score{display:flex;gap:22px;flex-wrap:wrap;align-items:baseline}
.score .big{font-size:34px;font-weight:800}
.score .lbl,.lbl{font-size:11px;color:#7a6f60;text-transform:uppercase;letter-spacing:.04em}
.note{font-size:13px;color:#54493b;background:#f3eee3;border-radius:8px;padding:10px 12px;margin-top:10px}
.filters{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 16px}
.filters button{border:1px solid #e7e0d4;background:#fff;border-radius:999px;padding:6px 12px;
  font:600 12px/1 -apple-system,Segoe UI,Roboto,sans-serif;color:#54493b;cursor:pointer}
.filters button[aria-pressed="true"]{background:#2b2620;color:#faf8f3;border-color:#2b2620}
.chart{border:1px solid #e7e0d4;border-radius:12px;background:#fff;margin-bottom:14px;overflow:hidden}
.chart-h{padding:14px 16px 10px;border-bottom:1px solid #efe9dd}
.chart-h h2{font-size:18px;margin:0 0 4px}
.q{color:#54493b;font-size:13px;margin:6px 0 0}
.meta{font-size:12px;color:#7a6f60}
.motif{padding:12px 16px;border-top:1px solid #f3eee3}
.motif h3{font-size:15px;margin:0 0 6px}
.poles{font-size:12px;color:#54493b;margin:0 0 8px}
.badge{display:inline-block;font-size:11px;font-weight:800;letter-spacing:.04em;text-transform:uppercase;
  border-radius:6px;padding:2px 7px;margin-right:6px}
.badge.lines_up{background:#e4f3ea;color:#2f7d4f}
.badge.partial{background:#fff3d6;color:#8a6a12}
.badge.miss{background:#f8e1de;color:#b5453f}
.badge.unresolved{background:#ece8f4;color:#5b4d7a}
.badge.pending{background:#eeeae2;color:#7a6f60}
.badge.credit{background:#f3eee3;color:#7a6f60;font-weight:600}
.ev-list{display:flex;flex-direction:column;gap:6px}
.ev{text-align:left;border:1px solid #efe9dd;background:#fbf7ee;border-radius:8px;padding:7px 9px;
  font-size:12px;color:#2b2620;cursor:pointer}
.ev:hover,.ev:focus{outline:none;border-color:#b8860b;background:#fff8e8}
.ev-lane{font-weight:800;font-size:10px;letter-spacing:.04em;text-transform:uppercase;color:#7a6f60;margin-right:6px}
.muted{color:#9a8f7e;font-size:12px}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:12px}
@media(max-width:800px){.cols{grid-template-columns:1fr}}
table{width:100%;border-collapse:collapse;font-size:13px}
th,td{text-align:left;padding:7px 9px;vertical-align:top;border-bottom:1px solid #efe9dd}
th{font-size:11px;text-transform:uppercase;letter-spacing:.04em;color:#9a8f7e}
.literal-row{cursor:pointer}
.literal-row:hover{background:#fbf7ee}
"""
    chart_html = []
    for chart in charts:
        motifs = "".join(
            f"""<article class="motif" data-call-id="{esc(m['id'])}" data-status="{esc(m['status'])}">
  <h3><span class="badge {esc(m['status'])}">{esc(LABEL[m['status']])}</span> {esc(m['name'])}</h3>
  <p class="poles"><b>Constructive.</b> {esc((m.get('poles') or {}).get('constructive'))}
     <b>Shadow.</b> {esc((m.get('poles') or {}).get('shadow'))}</p>
  {"<p class='muted'>" + esc(m['note']) + "</p>" if m.get("note") else ""}
  <div class="cols">
    <div><div class="lbl">Attention</div>{evidence_html(m.get("attention") or [])}</div>
    <div><div class="lbl">Official / Research</div>{evidence_html(m.get("official") or [])}</div>
  </div>
</article>"""
            for m in chart["motifs"]
        )
        chart_html.append(
            f"""<section class="chart" data-season="{esc(chart.get('season'))}" data-kind="{esc(chart.get('kind'))}"
  data-credit="{esc(chart.get('credit'))}" data-status="{esc(chart['status'])}" data-date="{esc(chart.get('date'))}"
  data-call-id="{esc(chart['id'])}">
  <div class="chart-h">
    <div class="meta"><span class="badge {esc(chart['status'])}">{esc(LABEL[chart['status']])}</span>
      <span class="badge credit">{esc(chart.get('credit'))}</span>
      {esc(chart.get('window_start'))} → {esc(chart.get('window_end'))} · {esc(chart.get('kind'))}</div>
    <h2>{esc(chart['label'])}</h2>
    <p class="q">{esc(chart.get('question'))}</p>
    <p class="meta"><button type="button" class="ev" data-tab="obs-sky" data-chart="{esc(chart.get('reading_id') or chart['id'])}">Open Chart Reading</button></p>
  </div>
  {motifs}
</section>"""
        )
    lit_rows = []
    for call in sorted(literals, key=lambda c: c.get("window_center") or ""):
        lit_rows.append(
            f'<tr class="literal-row" data-date="{esc(call.get("window_center"))}" data-call-id="{esc(call.get("id"))}">'
            f'<td>{esc(call.get("window_center"))}</td>'
            f'<td><span class="badge {esc(call.get("status"))}">{esc(LABEL.get(call.get("status"), call.get("status")))}</span></td>'
            f'<td>{esc(call.get("framework"))}</td>'
            f'<td>{esc(call.get("predicted_sub") or call.get("id"))}</td>'
            f'<td class="muted">{esc(call.get("basis"))}</td></tr>'
        )
    presence = pct(sc.get("presence_rate"))
    both = pct(sc.get("present_or_partial_rate"))
    chart_rate = pct(
        (sc["chart_lines_up"] / sc["chart_scored"]) if sc.get("chart_scored") else None
    )
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Prediction Scorecard</title>
<style>{css}</style></head>
<body>
<h1>Prediction Scorecard</h1>
<p class="sub">Named archetypes from the ingress and lunation readings. Presence in Attention, Official/Research, or Entity is a win. Seven-arc folder races are retired. Generated {esc(today_local().isoformat())} · data through {esc(data_end)}.</p>
<div class="card">
  <div class="score">
    <div><div class="big">{esc(presence)}</div><div class="lbl">motif presence</div></div>
    <div><div class="big">{esc(both)}</div><div class="lbl">lines up or partial</div></div>
    <div><div class="big">{esc(chart_rate)}</div><div class="lbl">charts that lined up</div></div>
    <div><div class="big">{sc['lines_up']}/{sc['scored']}</div><div class="lbl">motifs scored</div></div>
    <div><div class="big">{sc['pending']}</div><div class="lbl">pending</div></div>
  </div>
  <div class="note">A win is the reading’s named room showing up, not the loudest X folder. Official/Research uses Research Desk packets and the watch calendar, not bookmark volume. Calibration charts were frozen after their windows and get no forecast credit. Prospective charts were frozen before. Exact-day literal misses still miss. The State Transition Watch remains a stricter separate instrument.</div>
  <div class="note">Calibration: {sc['calibration_lines_up']} lined up of {sc['calibration_scored']} scored.
    Prospective: {sc['prospective_lines_up']} lined up of {sc['prospective_scored']} scored.</div>
</div>
<div class="filters" role="toolbar" aria-label="Filter charts">
  <button type="button" data-filter="all" aria-pressed="true">All</button>
  <button type="button" data-filter="season:cancer">Cancer</button>
  <button type="button" data-filter="season:aries">Aries</button>
  <button type="button" data-filter="credit:prospective">Prospective</button>
  <button type="button" data-filter="credit:calibration">Calibration</button>
  <button type="button" data-filter="kind:ingress">Climate</button>
  <button type="button" data-filter="kind:lunation">Weather</button>
</div>
<div id="charts">{"".join(chart_html)}</div>
<div class="card">
  <h2>Literal calls (separate strip)</h2>
  <p class="muted">DR-004 calls from <code>forecast_curated.json</code>. Scored by presence of the named subplot, not by arc dominance. Not mixed into the motif rate.</p>
  <table><thead><tr><th>window</th><th>result</th><th>framework</th><th>named object</th><th>basis</th></tr></thead>
  <tbody>{"".join(lit_rows) or '<tr><td colspan="5" class="muted">None.</td></tr>'}</tbody></table>
</div>
<script>
(function(){{
  function post(msg){{ try{{ parent.postMessage(msg, '*'); }}catch(_){{}} }}
  function filter(key){{
    var charts = document.querySelectorAll('.chart');
    charts.forEach(function(ch){{
      var show = true;
      if(key === 'all') show = true;
      else if(key.indexOf('season:')===0) show = ch.dataset.season === key.slice(7);
      else if(key.indexOf('credit:')===0) show = ch.dataset.credit === key.slice(7);
      else if(key === 'kind:ingress') show = ch.dataset.kind === 'ingress';
      else if(key === 'kind:lunation') show = ch.dataset.kind !== 'ingress';
      ch.style.display = show ? '' : 'none';
    }});
  }}
  document.addEventListener('click', function(e){{
    var btn = e.target.closest('[data-filter]');
    if(btn){{
      document.querySelectorAll('[data-filter]').forEach(function(b){{ b.setAttribute('aria-pressed', b===btn ? 'true':'false'); }});
      filter(btn.getAttribute('data-filter'));
      return;
    }}
    var ev = e.target.closest('.ev');
    if(ev){{
      var tab = ev.getAttribute('data-tab');
      if(tab === 'obs-df' && ev.getAttribute('data-date')){{
        post({{action:'navigateTo', tab:'obs-df', date:ev.getAttribute('data-date')}});
      }} else if(tab === 'obs-rd' && ev.getAttribute('data-research')){{
        post({{action:'navigateTo', tab:'obs-rd', childAction:'openResearch', id:ev.getAttribute('data-research')}});
        post({{action:'openResearch', id:ev.getAttribute('data-research')}});
      }} else if(ev.getAttribute('data-chart')){{
        post({{action:'navigateTo', tab:'obs-cr', childAction:'selectReading', chart_id:ev.getAttribute('data-chart')}});
      }} else if(tab === 'obs-sd' && ev.getAttribute('data-date')){{
        post({{action:'navigateTo', tab:'obs-sd', date:ev.getAttribute('data-date')}});
      }}
      return;
    }}
    var row = e.target.closest('.literal-row[data-date]');
    if(row){{ post({{action:'navigateTo', tab:'obs-df', date:row.dataset.date}}); }}
  }});
  function focusId(id){{
    if(!id) return;
    var target = document.querySelector('[data-call-id="'+id+'"]');
    if(!target) return;
    target.scrollIntoView({{behavior:'smooth', block:'center'}});
  }}
  function focusDate(date){{
    if(!date) return;
    var all = Array.from(document.querySelectorAll('.chart[data-date], .literal-row[data-date]'));
    var target = all.find(function(el){{ return el.dataset.date === date; }});
    if(target) target.scrollIntoView({{behavior:'smooth', block:'center'}});
  }}
  window.addEventListener('message', function(e){{
    if(!e.data) return;
    if(e.data.action==='goToCall' && e.data.callId) focusId(e.data.callId);
    if((e.data.action==='goToDate'||e.data.action==='scrollToDate') && e.data.date) focusDate(e.data.date);
  }});
}})();
</script>
</body></html>
"""


def predictions_projection(charts: list, literals: list) -> list:
    rows = []
    for chart in charts:
        for motif in chart["motifs"]:
            rows.append({
                "id": motif["id"],
                "framework": "Archetype presence",
                "call_class": "archetype",
                "made_on": "2026-08-15" if motif.get("credit") == "calibration" else "2026-08-15",
                "window_center": motif["window_center"],
                "window_start": motif["window_start"],
                "window_end": motif["window_end"],
                "status": motif["status"],
                "basis": motif["name"],
                "credit": motif.get("credit"),
                "reading_id": motif.get("reading_id"),
                "chart_id": motif.get("chart_id"),
            })
    for call in literals:
        rows.append(call)
    return rows


def main():
    watchlists = load_watchlists()
    idx = load_events()
    data_end = max(idx) if idx else today_local().isoformat()
    packages = load_packages()
    watches = load_watch_calendar()
    charts = score_charts(watchlists, idx, packages, watches, data_end)
    literals = score_literals(idx, packages, watches, data_end)
    sc, motifs = tally(charts)
    payload = {
        "schema": "f250.archetype-presence/v1",
        "generated": datetime.now().isoformat(),
        "data_end": data_end,
        "method": watchlists.get("method"),
        "scorecard": sc,
        "charts": charts,
        "predictions": predictions_projection(charts, literals),
        "literals": [
            {"id": c.get("id"), "status": c.get("status"), "window_center": c.get("window_center"),
             "framework": c.get("framework"), "predicted_sub": c.get("predicted_sub")}
            for c in literals
        ],
    }
    LEDGER.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    atomic_write_text(OUTHTML, render(charts, literals, sc, data_end))
    print(
        f"✓ Prediction Scorecard: {sc['n_total']} motifs "
        f"({sc['scored']} scored: {sc['lines_up']} lines up / {sc['partials']} partial / "
        f"{sc['miss']} miss / {sc['unresolved']} unresolved; {sc['pending']} pending). "
        f"presence {pct(sc['presence_rate'])}."
    )
    print(f"  → {OUTHTML}")


if __name__ == "__main__":
    main()
