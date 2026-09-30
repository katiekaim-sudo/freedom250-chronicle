#!/usr/bin/env python3
"""
build_deriv_houses.py — builds the Derivative Houses tab (the turned-chart calculator).

Pick a chart (the locked US Sagittarius chart, or any of the 8 governing/nuance
ingress charts) and an ACTOR (a mundane house). The view re-counts the wheel from
that actor's house, draws a turned-house numeral ring (colored by aspectual group),
and reads each turned house off the live chart's planets — with the mundane meaning
pulled from the Derivative Houses dictionary.

Reuses wheel_lib.WHEEL_JS (drawn-glyph Whole-Sign wheel). New interactions use
addEventListener under the compatibility/testability policy; the current wrapper
has `csp: null`. Reads readings from `deriv_dict.json` (parsed from the vault
dictionary note) so the view and the note never diverge.

Inputs (in 99 - Templates / outputs):
  - wheel_lib.py            (WHEEL_JS)
  - deriv_dict.json         (the 144 mundane readings, parsed from the dictionary note)
Output:
  - 04 - Synthesis/Cross-cuts/Derivative Houses.html
"""
import json, re, pathlib

HERE = pathlib.Path(__file__).resolve().parent
VAULT = HERE.parent
OUT = VAULT / "04 - Synthesis" / "Cross-cuts" / "Derivative Houses.html"

# ---- wheel engine ----
wl = (HERE / "wheel_lib.py").read_text()
WHEEL_JS = wl.split("WHEEL_JS = r'''")[1].split("'''")[0]

# ---- dictionary (parsed straight from the vault note, so view never diverges) ----
def parse_dict_from_note():
    md = (VAULT / "00 - Index" / "Derivative Houses — The Mundane Dictionary.md").read_text()
    parts = re.split(r'\n## (\d+) · ', md); d = {}
    for i in range(1, len(parts), 2):
        num = int(parts[i]); body = parts[i+1]; name = body.split('(')[0].strip()
        gm = re.search(r'\*\*Groups —\*\* (.+)', body); groups = gm.group(1).strip() if gm else ""
        rows = []
        for line in body.splitlines():
            m = re.match(r'\|\s*(\d+)\s+([^|]+?)\s*\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|', line)
            if m:
                rows.append({"n": int(m.group(1)), "label": m.group(2).strip(), "radical": int(m.group(3)),
                             "matter": m.group(4).strip(), "reading": m.group(5).strip()})
        if len(rows) == 12: d[str(num)] = {"name": name, "groups": groups, "rows": rows}
    return d
DICT = parse_dict_from_note()
assert len(DICT) == 12, f"dictionary parse got {len(DICT)} actors (expected 12)"

SGN = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio",
       "Sagittarius","Capricorn","Aquarius","Pisces"]

def dms(lon):
    d = int(lon % 30); m = int(round((lon % 1)*60))
    if m == 60: d += 1; m = 0
    return f"{d}°{m:02d}'"

# ---- CHARTS: US Sag (locked) + 8 ingresses ----
def chart_from_pos(cid, title, sub, asc, pos_list):
    asc_idx = int(asc // 30)
    pos = []
    for name, sign, lon, retro in pos_list:
        pos.append([name, sign, dms(lon), bool(retro), round(lon, 4)])
    return {"id": cid, "title": title, "sub": sub, "asc": round(asc, 4),
            "asc_idx": asc_idx, "pos": pos}

CHARTS = []

# US Sagittarius chart (Master Reference §5b) — exact positions
us_sag = [
    ("Sun","Cancer",101.4167,False),("Moon","Capricorn",298.3333,False),
    ("Mercury","Cancer",114.9833,True),("Venus","Cancer",90.65,False),
    ("Jupiter","Cancer",95.4833,False),("Mars","Gemini",80.0167,False),
    ("Saturn","Libra",194.75,False),("Uranus","Gemini",68.8167,False),
    ("Neptune","Virgo",172.3833,False),("Pluto","Capricorn",297.6,False),
    ("Node","Leo",126.5833,False),
]
CHARTS.append(chart_from_pos("us-sag", "The United States — Sagittarius rising",
    "July 2, 1776 · ~5:10 PM LMT · Philadelphia · the locked chart", 250.7333, us_sag))

# 8 ingress charts (from Ingress Charts.html ING_DATA)
# pull ingress charts straight from the Ingress Charts view (no json dependency)
_ic = (VAULT / "04 - Synthesis" / "Cross-cuts" / "Ingress Charts.html").read_text()
ING = json.loads(re.search(r'const ING_DATA = (\[.*?\]);', _ic, re.S).group(1))
GOV = {"2025-aries","2026-aries","2026-cancer","2026-libra","2027-aries","2028-aries"}
for c in ING:
    pos_list = []
    for name, (lon, sign, house) in c["p"].items():
        pos_list.append((name, sign, lon, False))
    sub = ("governing chart · " if c["id"] in GOV else "nuance chart · ") + c["date"] + " · " + c["rising"] + " rising"
    CHARTS.append(chart_from_pos(c["id"], c["title"], sub, c["asc_deg"], pos_list))

DATA = {"CHARTS": CHARTS, "DICT": DICT}

HTML = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Derivative Houses — the turned chart</title>
<style>
:root{ --bg:#faf8f3; --ink:#2b2620; --mut:#8a8377; --line:#e2d8c4; --card:#fffdf8;
 --gold:#c9a227; --blue:#3a6ea5; --green:#4a7d5f; --red:#b3402e; --amber:#a8821f; --grey:#8a8377; }
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"Iowan Old Style",Palatino,Georgia,serif;line-height:1.5}
.wrap{max-width:1180px;margin:0 auto;padding:18px 20px 60px}
h1{font-size:24px;margin:0 0 2px}
.sub{color:var(--mut);font-style:italic;font-size:14px;margin-bottom:14px}
.controls{display:flex;flex-wrap:wrap;gap:14px;align-items:flex-end;margin-bottom:14px;padding:12px 14px;background:var(--card);border:1px solid var(--line);border-radius:10px}
.ctl label{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:var(--mut);margin-bottom:3px}
select{font-family:inherit;font-size:14px;padding:6px 9px;border:1px solid var(--line);border-radius:7px;background:#fff;color:var(--ink);min-width:230px}
.layout{display:flex;gap:22px;flex-wrap:wrap;align-items:flex-start}
.wheelcol{flex:1 1 420px;max-width:560px}
.readcol{flex:1 1 460px;min-width:340px}
#wheel{width:100%}
.legend{display:flex;flex-wrap:wrap;gap:5px 12px;margin:8px 2px 2px;font-size:12px;color:var(--mut)}
.legend b{font-weight:normal}
.dot{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:4px;vertical-align:-1px}
.actorhead{margin:2px 0 8px;font-size:15px}
.actorhead .nm{font-weight:bold;font-size:18px}
.grpline{font-size:12.5px;color:var(--mut);margin:2px 0 12px;line-height:1.6}
.row{border:1px solid var(--line);border-left-width:5px;border-radius:8px;background:var(--card);padding:9px 12px;margin-bottom:8px}
.row .top{display:flex;justify-content:space-between;align-items:baseline;gap:8px}
.row .nh{font-size:12px;color:var(--mut)}
.row .nh b{color:var(--ink)}
.row .matter{font-weight:bold;font-size:14.5px}
.row .reading{font-size:13.5px;margin:3px 0 0}
.row .planets{font-size:12.5px;color:#5b554a;margin-top:5px}
.row .planets .pl{display:inline-block;margin-right:9px;white-space:nowrap}
.row .planets .dig{font-style:italic;color:var(--mut)}
.row.empty .planets{color:#b5a98c;font-style:italic}
.grp-self{border-left-color:var(--gold)} .grp-trine{border-left-color:var(--blue)}
.grp-sextile{border-left-color:var(--green)} .grp-cross{border-left-color:var(--red)}
.grp-inconj{border-left-color:var(--amber)} .grp-semis{border-left-color:var(--grey)}
.tag{font-size:10px;text-transform:uppercase;letter-spacing:.04em;padding:1px 6px;border-radius:4px;color:#fff}
.tag-self{background:var(--gold)} .tag-trine{background:var(--blue)} .tag-sextile{background:var(--green)}
.tag-cross{background:var(--red)} .tag-inconj{background:var(--amber)} .tag-semis{background:var(--grey)}
.note{font-size:12px;color:var(--mut);margin-top:14px;font-style:italic;line-height:1.6}
</style></head>
<body><div class="wrap">
<h1>Derivative Houses <span style="font-weight:normal;color:var(--mut);font-size:18px">— the turned chart</span></h1>
<div class="sub">Turn any mundane chart from any actor's chair. The wheel re-counts; each turned house reads off the live planets.</div>
<div class="controls">
  <div class="ctl"><label for="chartSel">Chart</label><select id="chartSel"></select></div>
  <div class="ctl"><label for="actorSel">Turn from — the actor on the 1st</label><select id="actorSel"></select></div>
</div>
<div class="layout">
  <div class="wheelcol"><div id="wheel"></div>
    <div class="legend">
      <span><span class="dot" style="background:var(--gold)"></span><b>the actor (1st)</b></span>
      <span><span class="dot" style="background:var(--blue)"></span><b>support · trine</b></span>
      <span><span class="dot" style="background:var(--green)"></span><b>opportunity · sextile</b></span>
      <span><span class="dot" style="background:var(--red)"></span><b>crisis · cross</b></span>
      <span><span class="dot" style="background:var(--amber)"></span><b>nagging · inconjunct</b></span>
      <span><span class="dot" style="background:var(--grey)"></span><b>adjacent · semisextile</b></span>
    </div>
    <div class="note">The numerals on the inner ring are the <b>radical</b> houses; the colored ring is the chart <b>turned</b> from your chosen actor (its house = 1). A turned house locates the topic on real planets &mdash; the verdict is the planets' condition, read in the whole chart. A D.C. chart shows how the <i>nation experiences</i> an actor, not that actor's own reality.</div>
  </div>
  <div class="readcol">
    <div class="actorhead">From the chair of <span class="nm" id="actorName"></span></div>
    <div class="grpline" id="grpline"></div>
    <div id="readings"></div>
  </div>
</div>
</div>
<script>
%%WHEEL_JS%%
</script>
<script>
var DATA = %%DATA%%;
var CHARTS_DH = DATA.CHARTS, DICT = DATA.DICT;
var SGN=["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"];
var ACTOR_NAMES={1:"The People",2:"The Economy",3:"The Press",4:"The Opposition / the Land",5:"The Markets",6:"Workers & the Military",7:"A Foreign Power",8:"International Finance",9:"The Courts & Law",10:"The Government",11:"The Legislature",12:"The Hidden"};
function derived(H,N){return ((H-1)+(N-1))%12+1;}
// group of a turned-house number N (1..12), by aspect offset to the actor
function grpOf(N){var o=(N-1)%12; if(o===0)return"self";
  if(o===4||o===8)return"trine"; if(o===2||o===10)return"sextile";
  if(o===3||o===9||o===6)return"cross"; if(o===5||o===7)return"inconj"; return"semis";}
var GRPCOL={self:"#c9a227",trine:"#3a6ea5",sextile:"#4a7d5f",cross:"#b3402e",inconj:"#a8821f",semis:"#8a8377"};
var GRPLAB={self:"the actor",trine:"support",sextile:"opportunity",cross:"crisis",inconj:"nagging",semis:"adjacent"};
// classical dignity (7 visibles) for flavor
var RUL={Sun:["Leo"],Moon:["Cancer"],Mercury:["Gemini","Virgo"],Venus:["Taurus","Libra"],Mars:["Aries","Scorpio"],Jupiter:["Sagittarius","Pisces"],Saturn:["Capricorn","Aquarius"]};
var EXA={Sun:"Aries",Moon:"Taurus",Mercury:"Virgo",Venus:"Pisces",Mars:"Capricorn",Jupiter:"Cancer",Saturn:"Libra"};
var DET={Sun:["Aquarius"],Moon:["Capricorn"],Mercury:["Sagittarius","Pisces"],Venus:["Aries","Scorpio"],Mars:["Taurus","Libra"],Jupiter:["Gemini","Virgo"],Saturn:["Cancer","Leo"]};
var FAL={Sun:"Libra",Moon:"Scorpio",Mercury:"Pisces",Venus:"Virgo",Mars:"Cancer",Jupiter:"Capricorn",Saturn:"Aries"};
function dignity(p,sign){ if(EXA[p]===sign)return"exalted"; if(FAL[p]===sign)return"fall";
  if(RUL[p]&&RUL[p].indexOf(sign)>=0)return"ruler"; if(DET[p]&&DET[p].indexOf(sign)>=0)return"detriment"; return"";}
var PGLY={Sun:"☉",Moon:"☽",Mercury:"☿",Venus:"♀",Mars:"♂",Jupiter:"♃",Saturn:"♄",Uranus:"♅",Neptune:"♆",Pluto:"♇",Node:"☊"};

function chartById(id){for(var i=0;i<CHARTS_DH.length;i++)if(CHARTS_DH[i].id===id)return CHARTS_DH[i];return CHARTS_DH[0];}
function planetsByHouse(ch){ // radical house -> [ {name,sign,retro,lon} ]
  var by={}; for(var h=1;h<=12;h++)by[h]=[];
  ch.pos.forEach(function(p){var lon=p[4]; var house=((Math.floor(lon/30)-ch.asc_idx+12)%12)+1; by[house].push({name:p[0],sign:p[1],retro:p[3],lon:lon});});
  return by;
}

function render(){
  var ch=chartById(document.getElementById("chartSel").value);
  var actor=parseInt(document.getElementById("actorSel").value,10);
  // base wheel
  var rec={pos:ch.pos, asp:[], asc:ch.asc, __date:ch.title, cap1:ch.sub, cap2:"Whole Sign · turned from "+ACTOR_NAMES[actor]};
  var svg=wheelSVG(rec);
  // turned-house numeral ring, injected before </svg>
  var cx=330,cy=330, cusp=Math.floor(ch.asc/30)*30;
  function pt(r,L){var a=(180+(L-cusp))*Math.PI/180; return [cx+r*Math.cos(a), cy-r*Math.sin(a)];}
  var ring=['<g font-family="Iowan Old Style,Palatino,Georgia,serif">'];
  for(var i=0;i<12;i++){
    var R=i+1;                             // radical house number of this sector (i = sectors from the Ascendant)
    var N=((R-actor+12)%12)+1;             // its turned-house number from the actor
    var g=grpOf(N), col=GRPCOL[g];
    var L=((ch.asc_idx+i)%12)*30 + 15;     // sector midpoint degree (sign of this sector)
    var p=pt(196,L);
    var rad=(N===1)?13:11;
    ring.push('<circle cx="'+p[0].toFixed(1)+'" cy="'+p[1].toFixed(1)+'" r="'+rad+'" fill="'+col+'" fill-opacity="'+(N===1?0.95:0.82)+'" stroke="#fffdf8" stroke-width="1"/>');
    ring.push('<text x="'+p[0].toFixed(1)+'" y="'+p[1].toFixed(1)+'" text-anchor="middle" dominant-baseline="central" font-size="'+(N===1?13:11)+'" font-weight="bold" fill="#fff">'+N+'</text>');
  }
  ring.push('</g>');
  svg=svg.replace("</svg>", ring.join("")+"</svg>");
  document.getElementById("wheel").innerHTML=svg;

  // readings
  document.getElementById("actorName").textContent=ACTOR_NAMES[actor];
  var rows=DICT[actor].rows, byH=planetsByHouse(ch);
  // group summary line
  var summ={trine:[],sextile:[],cross:[],inconj:[],semis:[]};
  rows.forEach(function(r){var g=grpOf(r.n); if(summ[g])summ[g].push(r.matter);});
  var gl=[];
  [["cross","crisis"],["trine","support"],["sextile","opportunity"],["inconj","nagging"],["semis","adjacent"]].forEach(function(pair){
    var k=pair[0]; gl.push('<span style="color:'+GRPCOL[k]+'">●</span> <b style="color:var(--ink)">'+pair[1]+':</b> '+summ[k].join(", "));
  });
  document.getElementById("grpline").innerHTML=gl.join(" &nbsp;·&nbsp; ");

  var out=[];
  rows.forEach(function(r){
    var g=grpOf(r.n), radical=r.radical;
    var pls=byH[radical]||[];
    var plhtml;
    if(pls.length){ plhtml=pls.map(function(o){var dg=dignity(o.name,o.sign); var gl=PGLY[o.name]||o.name;
        return '<span class="pl">'+gl+' '+o.name+(o.retro?' ℞':'')+' <span class="dig">'+o.sign+(dg?' · '+dg:'')+'</span></span>';}).join("");
    } else { plhtml='— no planets in this house'; }
    out.push('<div class="row grp-'+g+(pls.length?'':' empty')+'">'
      +'<div class="top"><div class="matter">'+r.matter+'</div>'
      +'<span class="tag tag-'+g+'">'+GRPLAB[g]+'</span></div>'
      +'<div class="nh">the actor’s <b>'+ordn(r.n)+' house</b> → radical <b>'+radical+'</b> ('+r.label+')</div>'
      +'<div class="reading">'+r.reading+'</div>'
      +'<div class="planets">'+plhtml+'</div></div>');
  });
  document.getElementById("readings").innerHTML=out.join("");
}
function ordn(n){var s=["th","st","nd","rd"],v=n%100;return n+(s[(v-20)%10]||s[v]||s[0]);}

// populate controls
(function(){
  var cs=document.getElementById("chartSel");
  CHARTS_DH.forEach(function(c){var o=document.createElement("option");o.value=c.id;o.textContent=c.title;cs.appendChild(o);});
  var as=document.getElementById("actorSel");
  [10,1,7,2,4,11,9,8,5,6,3,12].forEach(function(h){var o=document.createElement("option");o.value=h;o.textContent=h+" — "+ACTOR_NAMES[h];as.appendChild(o);});
  cs.value="us-sag"; as.value="10";
  cs.addEventListener("change",render);
  as.addEventListener("change",render);
  render();
})();
</script>
</body></html>
"""

HTML = HTML.replace("%%WHEEL_JS%%", WHEEL_JS).replace("%%DATA%%", json.dumps(DATA))
OUT.write_text(HTML)
print("wrote", OUT, f"({len(HTML)} bytes)")
print("charts:", [c['id'] for c in CHARTS])
