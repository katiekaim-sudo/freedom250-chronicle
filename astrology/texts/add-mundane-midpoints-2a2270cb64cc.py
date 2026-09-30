#!/usr/bin/env python3
"""Project the native wheels and mundane midpoint engine into Ingress Charts.

This is the sole owner of both feature blocks. It reads the target once,
validates every marker/anchor before mutation, refreshes both projections from
their canonical sources, and writes atomically only when bytes change.

What the injected JS block does (all at page runtime, from the chart data
ALREADY embedded in the page — no position data is duplicated here):

  1. For each ingress card (INGRESS_DATA): computes the 78 midpoints of
     10 planets + Node + ASC + MC. Planet longitudes are parsed from the
     `pos` strings exactly the way the page's own ingressRec() does
     (regex deg°min' + sign offset); ASC/MC come from the curated
     ascDeg/mcDeg fields (full ecliptic longitudes).
     NOTE: INGRESS_DATA's `deg` field is inconsistent (sometimes full
     longitude, sometimes deg-within-sign) — deliberately NOT used.
  2. Adds a "Midpoint Trees" section to every card: pick any of the 13
     points, see every pair whose midpoint sits on it within 1.0° mod-45,
     plus a fixed "Crisis axes" line (Munkasey's MA/SA MA/UR MA/PL SA/PL
     SA/NE UR/PL tested against Sun, Moon, ASC, MC, Node).
  3. Hooks the synastry overlay tool: wraps window.computeOverlay and
     appends "Midpoint strikes" — the selected lunation's Sun and Moon
     tested against the selected ingress chart's 78 midpoints at 1.0°
     mod-45. Lunation longitudes are read from CHARTS["__lunation__"],
     which computeOverlay itself publishes for the biwheel (LUN_DATA is
     closed inside the overlay IIFE and not reachable any other way).
  4. Every row click-toggles an indented quip (pair meaning from
     midpoint_meanings.json + interp_quips tech.mundanemidpoint).

Mod-45 hit test: d = ((x - m) mod 45); hit when min(d, 45-d) <= 1.0.
(The +/-180° midpoint ambiguity vanishes mod 45, so (a+b)/2 suffices.)
"""
import json
import os
import stat
import tempfile
from pathlib import Path

from wheel_lib import WHEEL_JS

HERE = Path(__file__).resolve().parent
VAULT = HERE.parent
TARGET = VAULT / "04 - Synthesis" / "Cross-cuts" / "Ingress Charts.html"

NATIVE_START = "<!-- NATIVE-WHEELS-START -->"
NATIVE_END = "<!-- NATIVE-WHEELS-END -->"

NATIVE_BLOCK = (NATIVE_START + """
<script>
""" + WHEEL_JS + """
function ingressRec(ch){
  const SO=["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"];
  const pos=ch.planets.map(p=>{
    const m=p.pos.match(/(\\d+)°(\\d+)'/); const d=(+m[1])+(+m[2])/60;
    const lon=SO.indexOf(p.sign)*30+d;
    return [p.name, p.sign, m[0], p.retro?1:0, Math.round(lon*100)/100];
  });
  const DEFS=[[0,"conjunct"],[30,"semisextile"],[60,"sextile"],[90,"square"],[120,"trine"],[150,"quincunx"],[180,"opposite"]];
  const PT=n=>n==="Chiron"||n==="Node"||n==="SNode"||n==="America";
  const asp=[];
  for(let i=0;i<pos.length;i++) for(let j=i+1;j<pos.length;j++){
    const isPt=PT(pos[i][0])||PT(pos[j][0]);
    if(PT(pos[i][0])&&PT(pos[j][0])) continue;
    const sep=Math.abs(((pos[i][4]-pos[j][4]+180)%360+360)%360-180);
    DEFS.forEach(d=>{
      if(isPt&&d[0]!==0&&d[0]!==90&&d[0]!==180) return;
      const cap=isPt?2:((pos[i][0]==="Moon"||pos[j][0]==="Moon"||d[0]===30)?2:3);
      const orb=Math.abs(sep-d[0]);
      if(orb<=cap) asp.push({t:pos[i][0]+" "+d[1]+" "+pos[j][0], o:Math.round(orb*100)/100, x:orb<=0.3?1:0, ap:0});
    });
  }
  asp.sort((a,b)=>a.o-b.o);
  return {pos:pos, asp:asp, asc:ch.ascDeg,
          __date: ch.title.replace(" Solar Ingress",""),
          cap1: ch.rising+" rising · Whole Sign · Washington D.C.",
          cap2: ch.date};
}
function paintIngressWheels(){
  if (typeof INGRESS_DATA==="undefined") return;
  INGRESS_DATA.forEach(function(ch){
    var el=document.querySelector('.native-wheel[data-chart="'+ch.id+'"]');
    if (el && !el.dataset.done){ el.innerHTML=wheelSVG(ingressRec(ch), null, false); el.dataset.done="1"; }
  });
}
paintIngressWheels(); window.addEventListener('load', paintIngressWheels);
</script>
""" + NATIVE_END).strip()

OLD_IMG_TITLE = """    // Chart Wheel (Astro Gold screenshot)
    html += '<div class="section-title">Chart Wheel <span style="font-size:0.72rem;color:var(--faint);font-weight:400;font-style:italic">— Astro Gold · Whole Sign · Washington, D.C.</span></div>';"""

NATIVE_CARD_BLOCK = """    // Chart Wheel — native Observatory render (added 2026-06-09)
    html += '<div class="section-title">Chart Wheel <span style="font-size:0.72rem;color:var(--faint);font-weight:400;font-style:italic">— Observatory render · Whole Sign · Washington, D.C.</span></div>';
    html += '<div style="max-width:620px;margin:0.6rem auto 1.2rem"><div class="native-wheel" data-chart="'+chart.id+'"></div></div>';
    // Astro Gold reference screenshot
    html += '<div class="section-title">Astro Gold reference <span style="font-size:0.72rem;color:var(--faint);font-weight:400;font-style:italic">— click to expand</span></div>';"""

MARKER_START = "<!-- F250-MUNDANE-MIDPOINTS-START -->"
MARKER_END   = "<!-- F250-MUNDANE-MIDPOINTS-END -->"

# preferred anchor: just before the dark-mode block at the end of <body>;
# fallback: just before </body> itself.
ANCHOR_PRIMARY  = "<!-- F250-DARKMODE-START -->"
ANCHOR_FALLBACK = "</body>"


def load_lexicon():
    with (HERE / "midpoint_meanings.json").open(encoding="utf-8") as f:
        meanings = json.load(f)
    with (HERE / "interp_quips.json").open(encoding="utf-8") as f:
        quips = json.load(f)
    tech = quips.get("tech", {}).get(
        "mundanemidpoint",
        "event charts speak midpoints loudest (Munkasey) — in mundane work treat a lit axis literally")
    return meanings, tech


def build_block(meanings, tech):
    mean_js = json.dumps(meanings, ensure_ascii=False)
    tech_js = json.dumps(tech, ensure_ascii=False)
    return MARKER_START + """
<style>
.mm-section{margin-top:0.4rem}
.mm-row{display:flex;justify-content:space-between;align-items:baseline;gap:8px;padding:4px 9px;margin-bottom:3px;background:var(--card-bg,#fffdf7);border:1px solid var(--border,#e2d8c2);border-left:3px solid var(--gold,#c9a227);border-radius:0 4px 4px 0;font-size:12.5px;cursor:pointer;font-family:'Iowan Old Style',Georgia,serif}
.mm-row:hover{background:var(--card-bg-alt,#f4f0e8)}
.mm-row.mm-crisis{border-left-color:var(--red,#b3402e)}
.mm-quip{display:none;margin:-1px 0 6px 20px;padding:4px 9px;font-size:11.5px;font-style:italic;color:var(--secondary,#5b554a);border-left:2px dotted var(--border-dark,#d4c9b0);font-family:'Iowan Old Style',Georgia,serif}
.mm-delta{font-size:10.5px;color:var(--faint,#8a7d68);white-space:nowrap;margin-left:8px}
.mm-select{font-size:12.5px;padding:5px 9px;border:1px solid var(--border-dark,#d4c9b0);border-radius:4px;background:var(--card-bg,#fffdf7);font-family:inherit;margin:0.3rem 0 0.5rem}
.mm-none{color:var(--faint,#8a7d68);font-size:12px;font-style:italic;margin:2px 0 6px}
</style>
<script>
(function(){
// === MUNDANE MIDPOINT ENGINE (Munkasey, mod-45) ===
var MM_MEAN = """ + mean_js + """;
var MM_TECH = """ + tech_js + """;
var MM_SO   = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"];
var MM_CODE = {Sun:"SU",Moon:"MO",Mercury:"ME",Venus:"VE",Mars:"MA",Jupiter:"JU",Saturn:"SA",Uranus:"UR",Neptune:"NE",Pluto:"PL",Node:"NN",ASC:"AS",MC:"MC"};
var MM_ORDER= ["SU","MO","ME","VE","MA","JU","SA","UR","NE","PL","NN","AS","MC"];
var MM_CRISIS={"MA/SA":1,"MA/UR":1,"MA/PL":1,"SA/PL":1,"SA/NE":1,"UR/PL":1};
var MM_ORB  = 1.0;

function mmNorm(x){return ((x%360)+360)%360;}
function mmD45(x,m){var d=mmNorm(x-m)%45;return Math.min(d,45-d);}
function mmFmtLon(l){l=mmNorm(l);var s=Math.floor(l/30),d=l-s*30,dd=Math.floor(d),mm=Math.round((d-dd)*60);if(mm===60){dd++;mm=0;}return dd+"\\u00b0"+(mm<10?"0":"")+mm+"' "+MM_SO[s];}

// 13 points: parse pos strings like the page's own ingressRec() — the deg
// field in INGRESS_DATA is unreliable (mixed full/within-sign longitudes).
function mmPoints(ch){
  var pts=[];
  ch.planets.forEach(function(p){
    var code=MM_CODE[p.name]; if(!code) return;            // skips Chiron, America
    var m=p.pos.match(/(\\d+)\\u00b0(\\d+)'/); if(!m) return;
    pts.push({name:p.name,code:code,lon:mmNorm(MM_SO.indexOf(p.sign)*30+(+m[1])+(+m[2])/60),label:p.pos});
  });
  pts.push({name:"ASC",code:"AS",lon:mmNorm(ch.ascDeg),label:ch.asc});
  pts.push({name:"MC", code:"MC",lon:mmNorm(ch.mcDeg), label:ch.mc});
  return pts;
}

// all 78 pairs, key earlier-code-first (midpoint_meanings.json convention)
function mmMidpoints(pts){
  var out=[];
  for(var i=0;i<pts.length;i++)for(var j=i+1;j<pts.length;j++){
    var a=pts[i],b=pts[j];
    if(MM_ORDER.indexOf(a.code)>MM_ORDER.indexOf(b.code)){var t=a;a=b;b=t;}
    out.push({key:a.code+"/"+b.code,names:a.name+"/"+b.name,lon:mmNorm((a.lon+b.lon)/2)});
  }
  return out;
}

function mmRows(list){
  return list.map(function(r){
    var mean=MM_MEAN[r.key]||"";
    return '<div class="mm-row'+(r.crisis?' mm-crisis':'')+'" title="click for the reading">'
      +'<span><b>'+r.key+'</b> <span style="color:var(--secondary,#5b554a)">'+r.names+'</span>'
      +(r.tag?' <span style="color:var(--faint,#8a7d68);font-size:10.5px">'+r.tag+'</span>':'')
      +' <i style="color:var(--faint,#8a7d68);font-size:11px">'+mean+'</i></span>'
      +'<span class="mm-delta">\\u0394 '+r.delta.toFixed(2)+'\\u00b0</span></div>'
      +'<div class="mm-quip">'+r.key+' \\u2014 '+mean+' \\u00b7 '+MM_TECH+'</div>';
  }).join('');
}

// quip toggle — one delegated listener for every mm-row on the page
document.addEventListener('click',function(e){
  var r=e.target&&e.target.closest?e.target.closest('.mm-row'):null; if(!r)return;
  var q=r.nextElementSibling;
  if(q&&q.classList.contains('mm-quip')) q.style.display=(q.style.display==='block')?'none':'block';
});

// --- per-card "Midpoint Trees" section -----------------------------------
function mmCardSection(ch){
  var body=document.getElementById('body-'+ch.id);
  if(!body||body.querySelector('.mm-section'))return;
  var pts=mmPoints(ch), mps=mmMidpoints(pts);

  var wrap=document.createElement('div'); wrap.className='mm-section';
  var html='<div class="section-title">Midpoint Trees <span style="font-size:0.72rem;color:var(--faint);font-weight:400;font-style:italic">\\u2014 mod-45 \\u00b7 \\u22641.0\\u00b0 \\u00b7 Munkasey</span></div>';

  // fixed crisis-axes line: MA/SA MA/UR MA/PL SA/PL SA/NE UR/PL on Su/Mo/ASC/MC/NN
  var anchors=pts.filter(function(p){return ["SU","MO","AS","MC","NN"].indexOf(p.code)>=0;});
  var hits=[];
  mps.forEach(function(mp){
    if(!MM_CRISIS[mp.key])return;
    anchors.forEach(function(a){
      var d=mmD45(a.lon,mp.lon);
      if(d<=MM_ORB)hits.push({key:mp.key,names:mp.names+" = "+a.name,tag:"mp "+mmFmtLon(mp.lon),delta:d,crisis:true});
    });
  });
  hits.sort(function(a,b){return a.delta-b.delta;});
  html+='<div style="font-size:0.78rem;color:var(--secondary);margin:0.2rem 0 0.3rem"><strong style="color:var(--red,#b3402e)">Crisis axes</strong> <span style="color:var(--faint)">(Munkasey pairs on Sun, Moon, ASC, MC, Node)</span>'
    +(hits.length?':':' \\u2014 <i>none within 1.0\\u00b0 \\u2014 quiet on the crisis axes.</i>')+'</div>';
  if(hits.length)html+=mmRows(hits);

  // the tree picker
  html+='<div style="font-size:0.78rem;color:var(--secondary);margin-top:0.4rem">Pairs sitting on '
    +'<select class="mm-select" id="mm-sel-'+ch.id+'">'
    +pts.map(function(p,i){return '<option value="'+i+'">'+p.name+' \\u2014 '+p.label+'</option>';}).join('')
    +'</select></div><div id="mm-tree-'+ch.id+'"></div>';

  wrap.innerHTML=html;
  body.appendChild(wrap);

  function paint(){
    var sel=document.getElementById('mm-sel-'+ch.id), out=document.getElementById('mm-tree-'+ch.id);
    var x=pts[+sel.value];
    var on=mps.filter(function(mp){return mmD45(x.lon,mp.lon)<=MM_ORB;})
              .map(function(mp){return {key:mp.key,names:mp.names+" = "+x.name,tag:"mp "+mmFmtLon(mp.lon),delta:mmD45(x.lon,mp.lon),crisis:!!MM_CRISIS[mp.key]};})
              .sort(function(a,b){return a.delta-b.delta;});
    out.innerHTML=on.length?mmRows(on):'<div class="mm-none">nothing on '+x.name+' within 1.0\\u00b0 (mod-45).</div>';
  }
  document.getElementById('mm-sel-'+ch.id).addEventListener('change',paint);
  paint();
}

function mmInitCards(){
  if(typeof INGRESS_DATA==="undefined")return;
  INGRESS_DATA.forEach(function(ch){try{mmCardSection(ch);}catch(e){}});
}
if(document.readyState==="loading")
  document.addEventListener('DOMContentLoaded',function(){setTimeout(mmInitCards,0);});
else setTimeout(mmInitCards,0);

// --- synastry overlay: "Midpoint strikes" --------------------------------
// LUN_DATA lives inside the overlay IIFE; computeOverlay publishes the
// selected lunation's full longitudes as CHARTS["__lunation__"] for the
// biwheel — we read them from there. Ingress is matched by option title.
function mmOverlay(){
  var res=document.getElementById('ov-results'); if(!res)return;
  var old=document.getElementById('mm-strikes'); if(old)old.remove();
  var sel=document.getElementById('ov-ingress');
  if(!sel||sel.selectedIndex<0||typeof INGRESS_DATA==="undefined")return;
  var title=sel.options[sel.selectedIndex].textContent.split(" \\u2014 ")[0];
  var ch=null;
  for(var i=0;i<INGRESS_DATA.length;i++)if(INGRESS_DATA[i].title===title){ch=INGRESS_DATA[i];break;}
  if(!ch)return;
  var lun=(window.CHARTS&&window.CHARTS["__lunation__"])||null;

  var div=document.createElement('div'); div.id='mm-strikes';
  div.style.cssText="margin-top:18px;font-family:'Iowan Old Style',Georgia,serif";
  var h='<h3 style="font-size:12px;color:#3d2b1f;border-bottom:1px solid #d4c9b0;padding-bottom:4px;margin:0 0 8px;text-transform:uppercase;letter-spacing:0.8px">Midpoint strikes <span style="color:#8a7d68;font-weight:400;text-transform:none;letter-spacing:0">(Munkasey \\u2014 event charts speak midpoints loudest)</span></h3>';
  h+='<p style="font-size:11px;color:#8a7d68;font-style:italic;margin:0 0 8px">Lunation \\u2192 ingress midpoints \\u00b7 the lunation\\u2019s Sun and Moon against the '+ch.title+'\\u2019s 78 midpoints \\u00b7 mod-45 \\u00b7 \\u22641.0\\u00b0</p>';

  if(!lun||typeof lun.Sun!=="number"||typeof lun.Moon!=="number"){
    h+='<div class="mm-none">lunation positions unavailable (wheel engine not loaded yet) \\u2014 reselect a lunation.</div>';
    div.innerHTML=h; res.appendChild(div); return;
  }
  var mps=mmMidpoints(mmPoints(ch)), rows=[];
  [["\\u2609 Lun Sun",lun.Sun],["\\u263d Lun Moon",lun.Moon]].forEach(function(L){
    mps.forEach(function(mp){
      var d=mmD45(L[1],mp.lon);
      if(d<=MM_ORB)rows.push({key:mp.key,names:L[0]+" "+mmFmtLon(L[1])+" = "+mp.names,tag:"mp "+mmFmtLon(mp.lon),delta:d,crisis:!!MM_CRISIS[mp.key]});
    });
  });
  rows.sort(function(a,b){return a.delta-b.delta;});
  h+=rows.length?mmRows(rows):'<div class="mm-none">no strikes \\u2014 this lunation slides past the ingress midpoint field.</div>';
  div.innerHTML=h; res.appendChild(div);
}

(function hook(){
  if(typeof window.computeOverlay!=="function"){setTimeout(hook,150);return;}
  var orig=window.computeOverlay;
  window.computeOverlay=function(){orig();try{mmOverlay();}catch(e){}};
  // the page's first auto-run (setTimeout(computeOverlay,120) inside the
  // overlay IIFE) captured the ORIGINAL function reference before this
  // wrapper existed — poll briefly so the initial render gets strikes too.
  var tries=0;
  (function first(){
    if(document.getElementById('mm-strikes'))return;
    var r=document.getElementById('ov-results');
    if(r&&r.innerHTML){try{mmOverlay();}catch(e){}return;}
    if(++tries<25)setTimeout(first,200);
  })();
})();
})();
</script>
""" + MARKER_END + "\n"


def fail(message):
    raise SystemExit("INGRESS PROJECTOR FAILED: " + message)


def upsert_owned_block(source, start, end, block, anchors, label):
    start_count = source.count(start)
    end_count = source.count(end)
    if start_count != end_count or start_count > 1:
        fail(
            f"{label} marker ownership is ambiguous "
            f"({start_count} start, {end_count} end)"
        )
    if start_count == 1:
        begin = source.index(start)
        end_at = source.find(end, begin)
        if end_at < 0:
            fail(f"{label} end marker precedes its start marker")
        finish = end_at + len(end)
        return source[:begin] + block + source[finish:]
    for anchor in anchors:
        count = source.count(anchor)
        if count > 1:
            fail(f"{label} insertion anchor is ambiguous: {anchor}")
        if count == 1:
            return source.replace(anchor, block + "\n" + anchor, 1)
    fail(f"{label} has no governed insertion anchor")


def project(source, meanings, tech):
    native_cards = source.count('class="native-wheel" data-chart=')
    old_cards = source.count(OLD_IMG_TITLE)
    if (native_cards, old_cards) not in ((1, 0), (0, 1)):
        fail(
            "native card ownership must be exactly one projected fragment or "
            f"one legacy anchor; found {native_cards} projected, {old_cards} legacy"
        )

    # Every operation below is in memory. A failed later gate cannot partially
    # rewrite the generated target on disk.
    projected = source
    if native_cards == 0:
        projected = projected.replace(OLD_IMG_TITLE, NATIVE_CARD_BLOCK, 1)
    projected = upsert_owned_block(
        projected,
        NATIVE_START,
        NATIVE_END,
        NATIVE_BLOCK,
        (MARKER_START, ANCHOR_PRIMARY, ANCHOR_FALLBACK),
        "native wheel",
    )
    midpoint_block = build_block(meanings, tech).rstrip("\n")
    projected = upsert_owned_block(
        projected,
        MARKER_START,
        MARKER_END,
        midpoint_block,
        (ANCHOR_PRIMARY, ANCHOR_FALLBACK),
        "mundane midpoint",
    )

    if projected.count('class="native-wheel" data-chart=') != 1:
        fail("native card projection did not settle to one owner")
    for start, end, label in (
        (NATIVE_START, NATIVE_END, "native wheel"),
        (MARKER_START, MARKER_END, "mundane midpoint"),
    ):
        if projected.count(start) != 1 or projected.count(end) != 1:
            fail(f"{label} projection did not settle to one marker pair")
    if projected.index(NATIVE_START) > projected.index(MARKER_START):
        fail("native wheel block must precede the midpoint block")
    return projected


def read_exact(path):
    with path.open("r", encoding="utf-8", newline="") as handle:
        return handle.read()


def atomic_write(path, content):
    temporary = None
    mode = stat.S_IMODE(path.stat().st_mode)
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="",
            dir=path.parent,
            delete=False,
        ) as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
            os.fchmod(handle.fileno(), mode)
            temporary = handle.name
        os.replace(temporary, path)
        temporary = None
    finally:
        if temporary and os.path.exists(temporary):
            os.unlink(temporary)


def main():
    source = read_exact(TARGET)
    meanings, tech = load_lexicon()
    projected = project(source, meanings, tech)
    if projected == source:
        print("= Ingress Charts.html: native wheels + midpoint engine already current")
        return
    atomic_write(TARGET, projected)
    print("✓ Ingress Charts.html: native wheels + midpoint engine projected")
    print("  · 78 meanings embedded from midpoint_meanings.json")
    print("  · tech quip: " + tech[:60] + "…")
    print("  · 8 canonical wheels + card trees + crisis axes + midpoint strikes")


if __name__ == "__main__":
    main()
