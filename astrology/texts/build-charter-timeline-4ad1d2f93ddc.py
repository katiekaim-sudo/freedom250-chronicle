#!/usr/bin/env python3
"""build_charter_timeline.py — The Charter Queue (sub-view of The Machines, obs-om).

Copied from build_castration_timeline.py per _Claude-Context/PATTERN — Timeline Machine Build.md.

The legal operating clock of the private monetary stack: who applied, who was approved,
who was let in — and who is still waiting at the Federal Reserve's door. Third room of the
One Machine, beside The Castration Timeline (the state binds its own bank) and The Judicial
Watch (the courts draw perimeters). One question in three rooms: who may act on the money?

Data from charter_seed.json + charter_astro.json (derived — run build_charter_seed.py then
build_charter_astro.py first). Canonical sources are the two Cross-cuts notes:
'The Charter Queue — Factual Timeline' + 'The Waiting Room'.

CSP-safe: event delegation only, no inline handlers. No toISOString().
Dark-native (Machines family); dark-mode/interp injectors deliberately omitted.
"""
import os, json, html, importlib.util

HERE  = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(HERE)
CC    = os.path.join(VAULT, "04 - Synthesis", "Cross-cuts")
SEED  = os.path.join(HERE, "charter_seed.json")
ASTRO = os.path.join(HERE, "charter_astro.json")
OUT   = os.path.join(CC, "The Charter Queue.html")

_wlspec = importlib.util.spec_from_file_location("wheel_lib", os.path.join(HERE, "wheel_lib.py"))
wl = importlib.util.module_from_spec(_wlspec); _wlspec.loader.exec_module(wl)

TRACKS = {
    "door":     ("The Door",     "#d4a017", "The OCC charter queue — applied, conditional, final, consummated. Five in one afternoon; the same agency that chartered the National Banks in 1863."),
    "gate":     ("The Gate",     "#e05252", "Federal Reserve account access. Kraken has a limited-purpose Tier 3 account; digital-asset national-trust Master Account access is a separate unresolved question."),
    "ledger":   ("The Ledger",   "#4a9eda", "Clearing and depository permission — PSSC's temporary registration, DTC's tokenization service, the Collateral AppChain."),
    "rulebook": ("The Rulebook", "#a06cd5", "The incumbents absorbing the new rails while keeping the constitution — Swift, Visa, Mastercard, the capital-treatment guidance."),
    "coin":     ("The Coin",     "#3dbd7d", "The issuers and their obligors. Who owes the holder money — and who can freeze it."),
    "interior": ("The Interior", "#e0883a", "The permissioned bank rails — Fnality, Partior, Canton, Kinexys, Broadridge. Where regulated balance sheets actually meet."),
    "stack":    ("The Stack",    "#c86d9e", "The acquisitions. Vertical integration is outrunning every protocol merger — buy the missing layer, do not build a coalition."),
}
TRACK_ORDER = ["door", "gate", "ledger", "rulebook", "coin", "interior", "stack"]

STATUS_KEYS = [("Occurred", "occurred"), ("Public", "position"), ("Proposed", "proposed"),
               ("Research", "research"), ("Scheduled", "scheduled")]

def status_key(s):
    for prefix, key in STATUS_KEYS:
        if s.startswith(prefix):
            return key
    return "occurred"

STRENGTHENS = [
    "Any cohort member gets a publicly confirmed Federal Reserve master account",
    "Anchorage's nine-month access request is granted",
    "Custodia wins, or the Court takes the case",
    "DTC's first tokenized entitlement settles against a NAMED cash leg",
    "A second, third and fourth conversion consummate and open for business",
    "Kraken's claimed limited-purpose account appears in a public regulator record",
]
WEAKENS = [
    "The Fed denies Anchorage outright and the queue keeps growing anyway",
    "The DTC service slips again, past the Dec 31 clearing mandate",
    "Circle's charter opens but never takes reserve management",
    "FIUSD never names an issuer or a redemption obligor",
    "The first insolvency shows the tokens were only ever a receipt",
    "Nothing was rebuilt: the incumbents absorb it all and no new body ever gets an account",
]

def render(items, astro):
    data = json.dumps(items, ensure_ascii=False).replace("</", "<\\/")
    astro_data = json.dumps(astro, ensure_ascii=False).replace("</", "<\\/")
    track_css = "\n".join(
        f".t-{k} .card{{border-left-color:{c}}} .t-{k} .tk{{background:{c}22;color:{c};border:1px solid {c}55}}"
        f" .chip[data-track=\"{k}\"].on{{background:{c}33;border-color:{c};color:#eee}}"
        for k, (_, c, _) in TRACKS.items())
    track_chips = "".join(
        f'<button class="chip on" data-track="{k}" title="{html.escape(b)}">{html.escape(lbl)}</button>'
        for k, (lbl, c, b) in ((k, TRACKS[k]) for k in TRACK_ORDER))
    legend = "".join(
        f'<div class="leg t-{k}"><span class="tk">{html.escape(lbl)}</span><p>{html.escape(b)}</p></div>'
        for k, (lbl, c, b) in ((k, TRACKS[k]) for k in TRACK_ORDER))
    tests = ("".join(f"<li>{html.escape(t)}</li>" for t in STRENGTHENS),
             "".join(f"<li>{html.escape(t)}</li>" for t in WEAKENS))

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Charter Queue</title>
<style>
:root{{--bg:#0e1116;--panel:#161b24;--ink:#d6dae2;--dim:#8a93a3;--line:#2a3242;--accent:#c8a24a}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 -apple-system,'Segoe UI',Helvetica,Arial,sans-serif}}
.wrap{{max-width:980px;margin:0 auto;padding:28px 20px 80px}}
header h1{{font-family:Georgia,serif;font-size:30px;margin:0 0 4px;color:#f0e9d8}}
header .thesis{{font-family:Georgia,serif;font-style:italic;color:var(--accent);font-size:17px;margin:2px 0 10px}}
header p.sub{{color:var(--dim);margin:0 0 18px;max-width:70ch}}
.gatebox{{background:#1d1418;border:1px solid #5c2b2b;border-left:3px solid #e05252;border-radius:8px;padding:11px 14px;margin:0 0 18px}}
.gatebox b{{color:#e8a0a0}}
.gatebox p{{margin:4px 0 0;color:#b9a3a3;font-size:13.5px}}
.legend{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:10px;margin:14px 0 22px}}
.leg{{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:10px 12px}}
.leg p{{margin:6px 0 0;color:var(--dim);font-size:13px}}
.tk{{display:inline-block;font-size:11px;letter-spacing:.06em;text-transform:uppercase;padding:2px 8px;border-radius:10px}}
.bar{{position:sticky;top:0;background:linear-gradient(var(--bg) 82%,transparent);padding:10px 0 14px;z-index:5}}
.chips{{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:6px}}
.chip{{background:#1a2130;border:1px solid var(--line);color:var(--dim);border-radius:14px;padding:3px 11px;font-size:12.5px;cursor:pointer}}
.chip.on{{color:#eee;border-color:#59657c;background:#232c3e}}
.count{{color:var(--dim);font-size:12.5px;margin-left:4px}}
.yr{{font-family:Georgia,serif;font-size:22px;color:#f0e9d8;border-bottom:1px solid var(--line);margin:30px 0 4px;padding-bottom:4px}}
.entry{{display:grid;grid-template-columns:120px 1fr;gap:14px;padding:10px 0}}
.entry .d{{color:var(--dim);font-size:12.5px;text-align:right;padding-top:14px;font-variant-numeric:tabular-nums}}
.card{{background:var(--panel);border:1px solid var(--line);border-left:3px solid #555;border-radius:8px;padding:11px 14px}}
.card h3{{margin:0 0 5px;font-size:15.5px;color:#e8ebf2;font-weight:600}}
.meta{{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin-bottom:6px}}
.actor{{font-size:11px;color:#c7cedb;background:#242e42;border-radius:10px;padding:2px 8px}}
.st{{font-size:11px;border-radius:10px;padding:2px 8px;border:1px solid}}
.st-occurred{{color:#9fd6a9;border-color:#3d6b46}}
.st-position{{color:#c9b7e8;border-color:#5d4a80;font-style:italic}}
.st-proposed{{color:#e8d28a;border-color:#8a7433;border-style:dashed}}
.st-research{{color:#9fc4d6;border-color:#3d5d6b;border-style:dotted}}
.st-scheduled{{color:#e0a48a;border-color:#8a5433;background:#2a1e16}}
.card p{{margin:4px 0 6px;color:#aeb6c4;font-size:13.5px}}
.card a{{color:#7fa8d9;font-size:12.5px;text-decoration:none}}
.card a:hover{{text-decoration:underline}}
.astro-slot{{margin-top:8px}}
.astro-slot svg{{max-width:560px;width:100%;height:auto;background:#f6f2e8;border-radius:8px}}
.cbtn{{background:#1a2130;border:1px solid var(--line);color:#c8a24a;border-radius:12px;padding:2px 10px;font-size:11.5px;cursor:pointer;margin-left:auto}}
.moon{{font-size:11px;color:#9aa7bd;background:#1c2434;border-radius:10px;padding:2px 8px}}
.nochart{{font-size:10.5px;color:#5a6478;margin-left:auto;font-style:italic}}
.conv{{font-size:10.5px;color:#66708f;margin-left:6px}}
.future .yr{{color:var(--accent)}}
.tests{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:34px}}
.tests>div{{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:12px 16px}}
.tests h2{{font-family:Georgia,serif;font-size:17px;margin:0 0 8px}}
.tests .plus h2{{color:#9fd6a9}} .tests .minus h2{{color:#e0a48a}}
.tests li{{color:#aeb6c4;font-size:13px;margin-bottom:6px}}
footer{{color:var(--dim);font-size:12px;margin-top:34px;border-top:1px solid var(--line);padding-top:10px}}
{track_css}
@media(max-width:640px){{.entry{{grid-template-columns:1fr}}.entry .d{{text-align:left;padding-top:0}}.tests{{grid-template-columns:1fr}}}}
</style></head><body><div class="wrap">
<header>
  <h1>The Charter Queue</h1>
  <div class="thesis">The OCC hands out charters like candy. The Federal Reserve hands out nothing.</div>
  <p class="sub">The <em>legal operating clock</em> of the private monetary stack &mdash; application, conditional approval,
  final approval, consummation, and account access. Not the company build clock: a press release moves that one;
  only a regulator moves this one. Third room of the One Machine, beside <em>The Castration Timeline</em> (the state
  binds its own bank) and <em>The Judicial Watch</em> (the courts draw perimeters). One question in three rooms:
  <strong>who may act on the money?</strong></p>
</header>
<div class="gatebox">
  <b>The finding, in one line.</b>
  <p>Not one member of this cohort has a publicly confirmed Federal Reserve master account. Circle has a final charter and no account.
  Paxos and BitGo are consummated and numbered &mdash; no account. Anchorage has been a chartered national bank for five years and its
  access request, filed 2025-08-28, is <em>still pending</em>. The charter queue is a waiting room outside a door that has not opened
  &mdash; which makes <strong>Custodia the load-bearing case of the entire private stack.</strong></p>
</div>
<div class="legend">{legend}</div>
<div class="bar">
  <div class="chips" id="trackChips">{track_chips}</div>
  <div class="chips" id="statusChips">
    <button class="chip on" data-status="occurred">Occurred</button>
    <button class="chip on" data-status="position">Public position</button>
    <button class="chip on" data-status="proposed">Proposed</button>
    <button class="chip on" data-status="research">Research</button>
    <button class="chip on" data-status="scheduled">Scheduled</button>
    <span class="count" id="count"></span>
  </div>
  <div class="chips" id="actorChips"></div>
</div>
<div id="tl"></div>
<div class="tests">
  <div class="plus"><h2>The story gets stronger if&hellip;</h2><ul>{tests[0]}</ul></div>
  <div class="minus"><h2>The story weakens if&hellip;</h2><ul>{tests[1]}</ul></div>
</div>
<footer>Derived view &mdash; edit the two Cross-cuts notes (<em>The Charter Queue &mdash; Factual Timeline</em> &middot; <em>The Waiting Room</em>),
then re-run build_charter_seed.py &rarr; build_charter_astro.py &rarr; build_charter_timeline.py.
Charts: a stated time beats noon D.C.; scheduled dates cast midnight &ldquo;day of&rdquo;; Whole Sign; month-precision dates get no chart.
Company metrics are self-reported and are never promoted to fact. Sub-view of The Machines (obs-om).</footer>
</div>
<script type="application/json" id="cq-data">{data}</script>
<script type="application/json" id="cq-astro">{astro_data}</script>
<script>{wl.WHEEL_JS}</script>
<script>
(function(){{
"use strict";
var DATA = JSON.parse(document.getElementById('cq-data').textContent);
var ASTRO = JSON.parse(document.getElementById('cq-astro').textContent).charts || {{}};
var openCharts = {{}};
var state = {{track:{{}}, status:{{}}, actor:null}};
document.querySelectorAll('#trackChips .chip').forEach(function(c){{state.track[c.dataset.track]=true;}});
document.querySelectorAll('#statusChips .chip').forEach(function(c){{state.status[c.dataset.status]=true;}});

var ACTORS = [];
DATA.forEach(function(d){{ if(ACTORS.indexOf(d.actor)<0) ACTORS.push(d.actor); }});
ACTORS.sort();
var ac = document.getElementById('actorChips');
ac.innerHTML = '<button class="chip on" data-actor="__all">All actors</button>' +
  ACTORS.map(function(a){{return '<button class="chip" data-actor="'+a+'">'+a+'</button>';}}).join('');

function esc(s){{var d=document.createElement('div');d.textContent=s||'';return d.innerHTML;}}
function stLabel(k){{return {{occurred:'occurred',position:'public position',proposed:'proposed',research:'research',scheduled:'scheduled'}}[k];}}

function render(){{
  var tl=document.getElementById('tl'), out=[], lastYear=null, shown=0;
  var futureOpen=false;
  DATA.forEach(function(d){{
    if(!state.track[d.track]) return;
    if(!state.status[d.statusKey]) return;
    if(state.actor && d.actor!==state.actor) return;
    shown++;
    var yr=d.date.slice(0,4);
    if(d.statusKey==='scheduled' && !futureOpen){{
      out.push('<div class="future"><div class="yr">The fuse ahead &mdash; formally scheduled</div></div>');
      futureOpen=true; lastYear=null;
    }}
    if(yr!==lastYear && !futureOpen){{ out.push('<div class="yr">'+yr+'</div>'); lastYear=yr; }}
    var akey = d.date+'|'+d.title, ch = ASTRO[akey];
    out.push('<div class="entry t-'+d.track+'">'
      +'<div class="d">'+esc(d.date_display)+'</div>'
      +'<div class="card"><div class="meta">'
      +'<span class="tk">'+esc(d.trackLabel)+'</span>'
      +'<span class="actor">'+esc(d.actor)+'</span>'
      +'<span class="st st-'+d.statusKey+'">'+stLabel(d.statusKey)+'</span>'
      +(ch?'<span class="moon">Moon '+esc(ch.moonSign)+'</span>':'')
      +(ch?'<button class="cbtn" data-akey="'+esc(akey)+'">'+(openCharts[akey]?'chart \\u25B4':'chart \\u25BE')+'</button>'
          :'<span class="nochart">month precision &mdash; no chart</span>')
      +'</div><h3>'+esc(d.title)+'</h3>'
      +'<p>'+esc(d.summary)+'</p>'
      +(d.url?'<a href="'+esc(d.url)+'" target="_blank" rel="noopener">'+esc(d.source_label||'source')+'</a>'
             :'<span style="color:#66708033;font-size:12px">'+esc(d.source_label)+'</span>')
      +(ch?'<span class="conv">'+esc(ch.convention)+' \\u00B7 Whole Sign</span>':'')
      +'<div class="astro-slot" data-slot="'+esc(akey)+'"></div>'
      +'</div></div>');
  }});
  tl.innerHTML=out.join('');
  document.getElementById('count').textContent = shown+' of '+DATA.length+' shown';
  Object.keys(openCharts).forEach(function(k){{ if(openCharts[k]) paint(k); }});
}}

function paint(akey){{
  var slot=document.querySelector('.astro-slot[data-slot="'+CSS.escape(akey)+'"]');
  var ch=ASTRO[akey];
  if(!slot||!ch) return;
  if(!ch.__svg){{
    var d=DATA.filter(function(x){{return x.date+'|'+x.title===akey;}})[0]||{{}};
    ch.__svg=wheelSVG({{pos:ch.pos,asp:ch.asp,asc:ch.asc,__date:d.date_display||'',
      cap1:d.title||'', cap2:ch.convention+' \\u00B7 Whole Sign \\u00B7 '+(d.trackLabel||'')}},null,false);
  }}
  slot.innerHTML=ch.__svg;
}}

document.addEventListener('click', function(ev){{
  var cb = ev.target.closest ? ev.target.closest('.cbtn') : null;
  if(cb){{
    var k=cb.dataset.akey;
    openCharts[k]=!openCharts[k];
    cb.textContent=openCharts[k]?'chart \\u25B4':'chart \\u25BE';
    if(openCharts[k]) paint(k);
    else {{ var s=document.querySelector('.astro-slot[data-slot="'+CSS.escape(k)+'"]'); if(s) s.innerHTML=''; }}
    return;
  }}
  var c = ev.target.closest ? ev.target.closest('.chip') : null;
  if(!c) return;
  if(c.dataset.track){{ state.track[c.dataset.track]=!state.track[c.dataset.track]; c.classList.toggle('on'); }}
  else if(c.dataset.status){{ state.status[c.dataset.status]=!state.status[c.dataset.status]; c.classList.toggle('on'); }}
  else if(c.dataset.actor){{
    var all = c.dataset.actor==='__all';
    state.actor = all ? null : c.dataset.actor;
    document.querySelectorAll('#actorChips .chip').forEach(function(x){{x.classList.toggle('on', x===c);}});
  }}
  render();
}});

window.addEventListener('message', function(ev){{
  var m = ev.data||{{}};
  if(m.action==='filterTrack' && m.track && state.track.hasOwnProperty(m.track)){{
    Object.keys(state.track).forEach(function(k){{state.track[k]=(k===m.track);}});
    document.querySelectorAll('#trackChips .chip').forEach(function(x){{x.classList.toggle('on', x.dataset.track===m.track);}});
    render();
  }}
}});
render();
}})();
</script>
</body></html>"""

def main():
    seed = json.load(open(SEED, encoding="utf-8"))["items"]
    astro = json.load(open(ASTRO, encoding="utf-8")) if os.path.exists(ASTRO) else {"charts": {}}
    for d in seed:
        d["statusKey"] = status_key(d["status"])
        d["trackLabel"] = TRACKS[d["track"]][0]
    seed.sort(key=lambda x: (x["statusKey"] == "scheduled", x["date"]))
    out = render(seed, astro)
    open(OUT, "w", encoding="utf-8").write(out)
    print("wrote", OUT, f"({len(out)//1024} KB, {len(seed)} entries)")

if __name__ == "__main__":
    main()
