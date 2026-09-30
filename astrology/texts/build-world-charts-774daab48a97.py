#!/usr/bin/env python3
"""Build "The World Charts" — national natal charts for the main powers, as one
instrument, matching The American Charts system (Whole Sign, hand-drawn wheels).

Ten nations, each with a locked PRIMARY founding chart plus 1-2 kept ALTERNATES
(the Campion / Book-of-World-Horoscopes candidates). No rectification scoreboard
and no lineage growth — just solid, sourced natal charts to read mundanely and to
receive ingress / lunation / eclipse transits, the way we already do for the US.

All positions via Swiss Ephemeris — never hand-typed (vault data-integrity rule).
Reuses wheel_lib.WHEEL_JS / aspects_between / placidus_cusps. Whole Sign throughout,
each chart cast for its own capital (or the city of the founding act). Times flagged
PROVISIONAL where the historical clock is uncertain — treat those angles/Moon as soft.

Output: The World Charts.html  (addEventListener, no inline onclick).
"""
import swisseph as swe, json, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
def load_wheel():
    for p in [os.path.join(HERE, "wheel_lib.py"),
              os.path.join(HERE, "99 - Templates", "wheel_lib.py")]:
        if os.path.exists(p):
            import importlib.util
            spec = importlib.util.spec_from_file_location("wheel_lib", p)
            m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
            return m.WHEEL_JS, m.aspects_between, m.placidus_cusps
    raise SystemExit("wheel_lib.py not found")
WHEEL_JS, aspects_between, placidus_cusps = load_wheel()

SGN = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio",
       "Sagittarius","Capricorn","Aquarius","Pisces"]
RULER = {"Aries":"Mars","Taurus":"Venus","Gemini":"Mercury","Cancer":"Moon",
         "Leo":"Sun","Virgo":"Mercury","Libra":"Venus","Scorpio":"Mars",
         "Sagittarius":"Jupiter","Capricorn":"Saturn","Aquarius":"Saturn","Pisces":"Jupiter"}
DOM={"Sun":["Leo"],"Moon":["Cancer"],"Mercury":["Gemini","Virgo"],"Venus":["Taurus","Libra"],
     "Mars":["Aries","Scorpio"],"Jupiter":["Sagittarius","Pisces"],"Saturn":["Capricorn","Aquarius"]}
EXALT={"Sun":"Aries","Moon":"Taurus","Mercury":"Virgo","Venus":"Pisces","Mars":"Capricorn",
       "Jupiter":"Cancer","Saturn":"Libra"}
DETRI={"Sun":["Aquarius"],"Moon":["Capricorn"],"Mercury":["Sagittarius","Pisces"],
       "Venus":["Aries","Scorpio"],"Mars":["Taurus","Libra"],"Jupiter":["Gemini","Virgo"],
       "Saturn":["Cancer","Leo"]}
FALL={"Sun":"Libra","Moon":"Scorpio","Mercury":"Pisces","Venus":"Virgo","Mars":"Cancer",
      "Jupiter":"Capricorn","Saturn":"Aries"}
PLANETS=[("Sun",swe.SUN),("Moon",swe.MOON),("Mercury",swe.MERCURY),("Venus",swe.VENUS),
         ("Mars",swe.MARS),("Jupiter",swe.JUPITER),("Saturn",swe.SATURN),("Uranus",swe.URANUS),
         ("Neptune",swe.NEPTUNE),("Pluto",swe.PLUTO),("Node",swe.TRUE_NODE)]
AXIS={"Cancer":"the people & home vs the state & structure","Capricorn":"the state & structure vs the people & home",
      "Leo":"the leader vs the collective","Aquarius":"the collective vs the leader",
      "Aries":"sovereignty & self vs partnership","Libra":"partnership & treaties vs sovereignty",
      "Taurus":"national wealth vs shared/hidden power","Scorpio":"hidden power & crisis vs national wealth",
      "Gemini":"the press & word vs belief & law","Sagittarius":"belief, law & abroad vs the press & word",
      "Virgo":"labour & service vs ideals","Pisces":"ideals & dissolution vs labour"}

def jd_of(y,mo,d,localhour,tz):
    """tz = hours East of UT (local = UT + tz)."""
    return swe.julday(y,mo,d,0.0) + (localhour - tz)/24.0

def fmt_dms(lon):
    deg=int(lon%30); mn=int(round((lon%1)*60))
    if mn==60: deg+=1; mn=0
    return f"{deg}°{mn:02d}'"
def signdeg(lon): return f"{SGN[int(lon//30)]} {fmt_dms(lon)}"
def ordn(n):
    n=int(n); s='th' if 10<=n%100<=20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th'); return f"{n}{s}"
def dignity(planet, sign):
    if planet in DOM and sign in DOM[planet]: return ("domicile","+")
    if EXALT.get(planet)==sign: return ("exalted","+")
    if planet in DETRI and sign in DETRI[planet]: return ("detriment","−")
    if FALL.get(planet)==sign: return ("fall","−")
    return ("","")

def compute_chart(jd, lat, lon):
    cusps, ascmc = swe.houses(jd, lat, lon, b'W')
    asc, mc = ascmc[0], ascmc[1]
    asc_idx = int(asc//30)
    pl_cusps, pl_mc = placidus_cusps(jd, lat, lon)
    pos=[]; lons={}
    for name,pid in PLANETS:
        res=swe.calc_ut(jd,pid); l=res[0][0]; spd=res[0][3]
        sign=SGN[int(l//30)]; house=((int(l//30)-asc_idx)%12)+1
        pos.append({"name":name,"sign":sign,"lon":l,"dms":fmt_dms(l),"retro":spd<0,"house":house})
        lons[name]=l
    return {"asc":asc,"mc":mc,"asc_idx":asc_idx,"pos":pos,"lons":lons,"cusps":pl_cusps,"pl_mc":pl_mc}

# ============================================================================
# The nations. tz = hours East of UT at the founding moment (standard zone / LMT).
# prov=True flags a provisional clock time (angles + Moon degree are soft).
# ============================================================================
NATIONS=[
 {"code":"de","name":"Germany","flag":"🇩🇪","charts":[
   {"key":"reun","label":"Reunification 1990","primary":True,"prov":False,
    "y":1990,"mo":10,"d":3,"h":0.0,"tz":1,"place":"Berlin","lat":52.5200,"lon":13.4050,
    "time":"3 Oct 1990 · 00:00 CET · Berlin",
    "src":"Unification Treaty in force at midnight — the current Federal Republic, whole. Campion's modern-Germany chart."},
   {"key":"frg","label":"Federal Republic 1949","primary":False,"prov":True,
    "y":1949,"mo":5,"d":24,"h":0.0,"tz":1,"place":"Bonn","lat":50.7374,"lon":7.0982,
    "time":"24 May 1949 · 00:00 CET · Bonn (time provisional)",
    "src":"Basic Law in force — West Germany, the Cold-War / Adenauer-era state (the MKUltra-years Germany)."},
   {"key":"reich","label":"Empire 1871","primary":False,"prov":True,
    "y":1871,"mo":1,"d":18,"h":12.0,"tz":0.894,"place":"Berlin (proclaimed Versailles)","lat":52.5200,"lon":13.4050,
    "time":"18 Jan 1871 · ~noon LMT · proclaimed at Versailles (time provisional)",
    "src":"Proclamation of the German Empire — the first unified nation-state."}]},
 {"code":"gb","name":"United Kingdom","flag":"🇬🇧","charts":[
   {"key":"uk1801","label":"United Kingdom 1801","primary":True,"prov":False,
    "y":1801,"mo":1,"d":1,"h":0.0,"tz":0.0,"place":"London","lat":51.5074,"lon":-0.1278,
    "time":"1 Jan 1801 · 00:00 LMT · London",
    "src":"Act of Union (GB + Ireland) in force at midnight — Campion's standard modern UK chart."},
   {"key":"gb1707","label":"Great Britain 1707","primary":False,"prov":True,
    "y":1707,"mo":5,"d":1,"h":0.0,"tz":0.0,"place":"London","lat":51.5074,"lon":-0.1278,
    "time":"1 May 1707 · 00:00 LMT · London (time provisional)",
    "src":"Union of England & Scotland — the birth of Great Britain."}]},
 {"code":"ru","name":"Russia","flag":"🇷🇺","charts":[
   {"key":"rf1991","label":"Russian Federation 1991","primary":True,"prov":True,
    "y":1991,"mo":12,"d":25,"h":19.5333,"tz":3,"place":"Moscow","lat":55.7558,"lon":37.6173,
    "time":"25 Dec 1991 · 19:32 MSK · Moscow",
    "src":"Soviet flag lowered over the Kremlin as Gorbachev resigns — the Russian Federation stands alone."},
   {"key":"sov1917","label":"Revolution 1917","primary":False,"prov":True,
    "y":1917,"mo":11,"d":7,"h":21.75,"tz":2,"place":"Petrograd","lat":59.9343,"lon":30.3351,
    "time":"7 Nov 1917 · ~21:45 · Petrograd (time provisional)",
    "src":"Bolshevik seizure of power / storming of the Winter Palace — the Soviet century's seed."},
   {"key":"rsfsr1990","label":"Sovereignty 1990","primary":False,"prov":True,
    "y":1990,"mo":6,"d":12,"h":0.0,"tz":3,"place":"Moscow","lat":55.7558,"lon":37.6173,
    "time":"12 Jun 1990 · 00:00 MSK · Moscow (time provisional)",
    "src":"Declaration of State Sovereignty of the RSFSR — 'Russia Day', the Federation's other candidate seed."}]},
 {"code":"cn","name":"China (PRC)","flag":"🇨🇳","charts":[
   {"key":"prc1949","label":"People's Republic 1949","primary":True,"prov":False,
    "y":1949,"mo":10,"d":1,"h":15.0,"tz":8,"place":"Beijing","lat":39.9042,"lon":116.4074,
    "time":"1 Oct 1949 · 15:00 · Beijing (Tiananmen)",
    "src":"Mao proclaims the People's Republic from the Gate of Heavenly Peace — the near-universal PRC chart."},
   {"key":"roc1912","label":"Republic of China 1912","primary":False,"prov":True,
    "y":1912,"mo":1,"d":1,"h":0.0,"tz":8,"place":"Nanjing","lat":32.0603,"lon":118.7969,
    "time":"1 Jan 1912 · 00:00 · Nanjing (time provisional)",
    "src":"Sun Yat-sen inaugurates the Republic — the end of the empire."}]},
 {"code":"fr","name":"France","flag":"🇫🇷","charts":[
   {"key":"v1958","label":"Fifth Republic 1958","primary":True,"prov":True,
    "y":1958,"mo":10,"d":4,"h":0.0,"tz":1,"place":"Paris","lat":48.8566,"lon":2.3522,
    "time":"4 Oct 1958 · 00:00 CET · Paris (time provisional)",
    "src":"Constitution of the Fifth Republic promulgated — de Gaulle's state, France today."},
   {"key":"r1792","label":"First Republic 1792","primary":False,"prov":True,
    "y":1792,"mo":9,"d":22,"h":0.0,"tz":0.157,"place":"Paris","lat":48.8566,"lon":2.3522,
    "time":"22 Sep 1792 · 00:00 LMT · Paris (time provisional)",
    "src":"Abolition of the monarchy / First Republic — also the autumnal equinox."}]},
 {"code":"jp","name":"Japan","flag":"🇯🇵","charts":[
   {"key":"jp1947","label":"Postwar State 1947","primary":True,"prov":False,
    "y":1947,"mo":5,"d":3,"h":0.0,"tz":9,"place":"Tokyo","lat":35.6762,"lon":139.6503,
    "time":"3 May 1947 · 00:00 JST · Tokyo",
    "src":"Postwar Constitution takes effect at midnight — modern democratic Japan."},
   {"key":"jp1889","label":"Meiji Empire 1889","primary":False,"prov":True,
    "y":1889,"mo":2,"d":11,"h":0.0,"tz":9,"place":"Tokyo","lat":35.6762,"lon":139.6503,
    "time":"11 Feb 1889 · 00:00 JST · Tokyo (time provisional)",
    "src":"Meiji Constitution promulgated — the modern imperial state."}]},
 {"code":"il","name":"Israel","flag":"🇮🇱","charts":[
   {"key":"il1948","label":"State of Israel 1948","primary":True,"prov":False,
    "y":1948,"mo":5,"d":14,"h":16.0,"tz":2,"place":"Tel Aviv","lat":32.0853,"lon":34.7818,
    "time":"14 May 1948 · 16:00 · Tel Aviv",
    "src":"Ben-Gurion reads the Declaration of Independence ~4 pm — the well-attested Israel chart."},
   {"key":"il_mandate","label":"Mandate ends 1948","primary":False,"prov":True,
    "y":1948,"mo":5,"d":15,"h":0.0,"tz":2,"place":"Tel Aviv","lat":32.0853,"lon":34.7818,
    "time":"15 May 1948 · 00:00 · Tel Aviv (time provisional)",
    "src":"British Mandate ends at midnight — the legal-sovereignty alternate."}]},
 {"code":"ir","name":"Iran","flag":"🇮🇷","charts":[
   {"key":"ir1979","label":"Islamic Republic 1979","primary":True,"prov":True,
    "y":1979,"mo":4,"d":1,"h":15.0,"tz":3.5,"place":"Tehran","lat":35.6892,"lon":51.3890,
    "time":"1 Apr 1979 · ~15:00 · Tehran (time provisional)",
    "src":"Khomeini proclaims the Islamic Republic after the referendum — the current state."},
   {"key":"ir_rev","label":"Revolution victory 1979","primary":False,"prov":True,
    "y":1979,"mo":2,"d":11,"h":14.0,"tz":3.5,"place":"Tehran","lat":35.6892,"lon":51.3890,
    "time":"11 Feb 1979 · ~14:00 · Tehran (time provisional)",
    "src":"Fall of the monarchy — the revolution's day of victory."}]},
 {"code":"ua","name":"Ukraine","flag":"🇺🇦","charts":[
   {"key":"ua1991","label":"Independence 1991","primary":True,"prov":True,
    "y":1991,"mo":8,"d":24,"h":18.0,"tz":3,"place":"Kyiv","lat":50.4501,"lon":30.5234,
    "time":"24 Aug 1991 · ~18:00 · Kyiv (time/zone provisional)",
    "src":"Verkhovna Rada adopts the Act of Independence — modern Ukraine."},
   {"key":"unr1918","label":"People's Republic 1918","primary":False,"prov":True,
    "y":1918,"mo":1,"d":22,"h":12.0,"tz":2,"place":"Kyiv","lat":50.4501,"lon":30.5234,
    "time":"22 Jan 1918 · ~noon · Kyiv (time provisional)",
    "src":"Ukrainian People's Republic declares full independence — the historical alternate."}]},
 {"code":"in","name":"India","flag":"🇮🇳","charts":[
   {"key":"in1947","label":"Independence 1947","primary":True,"prov":False,
    "y":1947,"mo":8,"d":15,"h":0.0,"tz":5.5,"place":"New Delhi","lat":28.6139,"lon":77.2090,
    "time":"15 Aug 1947 · 00:00 IST · New Delhi",
    "src":"Independence at the stroke of midnight — Nehru's 'tryst with destiny'."},
   {"key":"in1950","label":"Republic 1950","primary":False,"prov":True,
    "y":1950,"mo":1,"d":26,"h":10.25,"tz":5.5,"place":"New Delhi","lat":28.6139,"lon":77.2090,
    "time":"26 Jan 1950 · ~10:15 · New Delhi (time provisional)",
    "src":"Constitution in force — the Republic of India."}]},
]

def wheel_rec(chart,label,time):
    posJS=[[p["name"],p["sign"],p["dms"],p["retro"],round(p["lon"],4)] for p in chart["pos"]]
    main={p["name"]:p["lon"] for p in chart["pos"] if p["name"]!="Node"}
    asp=aspects_between(main)
    ruler=RULER[SGN[chart["asc_idx"]]]
    return {"pos":posJS,"asp":asp,"asc":round(chart["asc"],4),"cusps":chart["cusps"],
            "mc":chart["pl_mc"],"__date":label,"cap1":time,
            "cap2":f"{ruler} rules · Whole Sign"}

def placements_html(chart):
    rows=[]
    for p in chart["pos"]:
        glyph="☊ N.Node" if p["name"]=="Node" else p["name"]
        dig,mk=dignity(p["name"],p["sign"])
        cls="dig-pos" if mk=="+" else ("dig-neg" if mk=="−" else "")
        rows.append(f"<tr><td>{glyph}</td><td>{p['sign']} {p['dms']}{' ℞' if p['retro'] else ''}</td>"
                    f"<td class='hc'>{p['house']}</td><td class='{cls}'>{dig}</td></tr>")
    return ("<table class='pl'><thead><tr><th>Body</th><th>Position</th><th>Hse</th>"
            "<th>Dignity</th></tr></thead><tbody>"+"".join(rows)+"</tbody></table>")

def read_html(chart, ch):
    """Structural skeleton read from the data — for Katie to flesh out, not a verdict."""
    ai=chart["asc_idx"]; rising=SGN[ai]; ruler=RULER[rising]
    rlon=chart["lons"][ruler]; rsign=SGN[int(rlon//30)]; rhouse=((int(rlon//30)-ai)%12)+1
    rdig,rmk=dignity(ruler,rsign)
    digtxt=(f", <b>{rdig}</b>" if rdig else "")
    sun=chart["lons"]["Sun"]; sh=((int(sun//30)-ai)%12)+1
    moon=chart["lons"]["Moon"]; msign=SGN[int(moon//30)]; opp=SGN[(int(moon//30)+6)%12]
    mh=((int(moon//30)-ai)%12)+1
    # tightest body to an angle
    asc=chart["asc"]; mc=chart["mc"]; best=None
    for p in chart["pos"]:
        if p["name"]=="Node": continue
        for an,al in [("Ascendant",asc),("MC",mc),("Descendant",(asc+180)%360),("IC",(mc+180)%360)]:
            o=abs((p["lon"]-al+180)%360-180)
            if o<=3 and (best is None or o<best[2]): best=(p["name"],an,round(o,1))
    ang = (f"<b>{best[0]}</b> sits on the <b>{best[1]}</b> ({best[2]}°) — a signature to read first."
           if best else "No planet within 3° of an angle.")
    prov = "<div class='provwarn'>⚠ Time provisional — treat the Ascendant, MC, houses and the Moon's exact degree as soft; the planetary signs are solid.</div>" if ch["prov"] else ""
    return (prov+
      f"<p><b>{rising} rising</b>, so <b>{ruler}</b> is the nation's ruler — its animating drive — here in "
      f"<b>{rsign}</b>{digtxt}, in the <b>{ordn(rhouse)} house</b>. That placement is the root: take the reading "
      f"there first.</p>"
      f"<p><b>Sun</b> (the leadership / the sovereign function) falls in the <b>{ordn(sh)} house</b>; "
      f"<b>Moon</b> (the people, the mood, the body of the nation) is in <b>{msign}</b> — the "
      f"<b>{msign}/{opp}</b> family: {AXIS.get(msign,'')} — running through the <b>{ordn(mh)} house</b>.</p>"
      f"<p>{ang}</p>")

# build records + fragments
REC={}; META={}
for nat in NATIONS:
    REC[nat["code"]]={}; charts_meta={}
    order=[]
    for c in nat["charts"]:
        jd=jd_of(c["y"],c["mo"],c["d"],c["h"],c["tz"])
        chart=compute_chart(jd,c["lat"],c["lon"])
        REC[nat["code"]][c["key"]]=wheel_rec(chart,c["label"],c["time"])
        charts_meta[c["key"]]={"label":c["label"],"primary":c["primary"],"time":c["time"],
            "src":c["src"],"place":c["place"],"prov":c["prov"],
            "asc":signdeg(chart["asc"]),"mc":signdeg(chart["mc"]),
            "ruler":RULER[SGN[chart["asc_idx"]]],
            "pl":placements_html(chart),"read":read_html(chart,c)}
        order.append(c["key"])
    META[nat["code"]]={"name":nat["name"],"flag":nat["flag"],"order":order,"charts":charts_meta}

NAT_ORDER=[n["code"] for n in NATIONS]

def _readf(p):
    for c in [os.path.join(HERE,p), os.path.join(HERE,"99 - Templates",p)]:
        if os.path.exists(c): return open(c).read()
    return "{}"
COMP=_readf("composite_us_pairs.json")  # US × each nation progressed composite (swisseph-verified, Sabian)

HTML = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>The World Charts</title>
<style>
:root{--bg:#faf8f3;--ink:#23201a;--mut:#8a8377;--line:#e3d9c2;--gold:#a8821f;--red:#7a2e1d;--blue:#3a6ea5;--grn:#2e8b74;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"Iowan Old Style",Palatino,Georgia,serif;line-height:1.5}
.wrap{max-width:1080px;margin:0 auto;padding:26px 20px 80px}
h1{font-size:30px;margin:0 0 2px;letter-spacing:.3px}
.sub{color:var(--mut);font-style:italic;margin:0 0 18px}
.lead{font-size:15px;max-width:780px;margin:0 0 20px}
.nations{display:flex;gap:7px;flex-wrap:wrap;margin:0 0 14px}
.nat{cursor:pointer;border:1px solid var(--line);background:#fff;padding:7px 13px;border-radius:20px;font-family:inherit;font-size:14px;color:var(--ink)}
.nat.on{background:var(--ink);color:#fff;border-color:var(--ink)}
.tabs{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 18px;border-bottom:1px solid var(--line);padding-bottom:14px}
.tab{cursor:pointer;border:1px solid var(--line);background:#fff;padding:8px 14px;border-radius:8px;font-family:inherit;font-size:14px;color:var(--ink)}
.tab .tt{font-size:11px;color:var(--mut);display:block}
.tab.on{background:var(--gold);color:#fff;border-color:var(--gold)}
.tab.on .tt{color:#f3ead0}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:26px;align-items:start}
@media(max-width:820px){.grid{grid-template-columns:1fr}}
.card{border:1px solid var(--line);border-radius:12px;background:#fffdf8;padding:16px 18px;margin:0 0 20px}
.card h2{font-size:18px;margin:0 0 8px}.card h3{font-size:13px;text-transform:uppercase;letter-spacing:1px;color:var(--mut);margin:16px 0 6px;font-weight:normal}
#wheelbox svg{max-width:520px;margin:0 auto;display:block}
.idn{font-size:14.5px}.idn .src{color:var(--gold);font-style:italic}
.angles{font-size:13px;color:var(--mut);margin:6px 0 0}
table{border-collapse:collapse;width:100%;font-size:13px}
.pl td,.pl th{border-bottom:1px solid var(--line);padding:4px 6px;text-align:left}
.pl .hc{text-align:center;color:var(--mut)}
.dig-pos{color:var(--grn)}.dig-neg{color:var(--red)}
.provwarn{background:#fbeee0;border:1px solid #e6c48f;border-radius:8px;padding:8px 11px;font-size:12.5px;color:#7a4a1d;margin:0 0 10px}
.note{font-size:12.5px;color:var(--mut);max-width:800px;margin-top:16px}
.phpill{display:inline-block;background:var(--ink);color:#fff;border-radius:12px;padding:2px 10px;font-size:12.5px}
.card ul.ct{list-style:none;padding:0;margin:6px 0 0;font-size:12.5px}
.card ul.ct li{padding:3px 0;border-bottom:1px solid var(--line)}
b{font-weight:bold}
</style></head><body><div class="wrap">
<h1>The World Charts</h1>
<p class="sub">The main powers as natal charts — read the same way we read America.</p>
<p class="lead">Ten nations, each with a <b>locked primary</b> founding chart and its kept <b>alternates</b> (the standard mundane candidates). Cast from Swiss Ephemeris, Whole Sign houses, each chart set for its own capital or the city of the founding act. These are the bodies that receive the ingress, lunation and eclipse transits — the mundane counterparts to the US chart, without growing each nation's full lineage. Where the founding clock is uncertain, the chart is flagged <b>provisional</b> (angles &amp; Moon soft, planet signs solid).</p>
<div class="nations" id="nations">__NATIONS__</div>
<div class="tabs" id="tabs"></div>
<div id="panel"></div>
<p class="note">Built __DATE__ · positions from Swiss Ephemeris, never hand-entered · Whole Sign houses · each chart cast for its founding city · founding moments per the standard mundane sources (Campion, <i>The Book of World Horoscopes</i>), primaries chosen as the current-state chart. The skeleton reads are structural starting points — motivation-first, taken to the ruler — not finished interpretations. See the companion note for the full source list and the provisional-time flags.</p>
<script>
__WHEEL_JS__
var REC=__REC__, META=__META__, NAT_ORDER=__NATORDER__;
var COMP=__COMP__;
var PHINT={New:'a re-opening / reset',Crescent:'early momentum','1stQ':'a building crisis',Gibbous:'perfecting toward the peak',Full:'the defining confrontation',Disseminating:'sharing the harvest',LastQ:'a rupture / reckoning',Balsamic:'dark of the moon — dissolving toward reseed'};
function compositeCard(code){
  var cp=COMP[code]; if(!cp) return '';
  var n=cp.now, h='<div class="card"><h2>US × '+cp.name.replace(' (PRC)','')+' — progressed composite</h2>';
  if(cp.prov) h+='<div class="provwarn">Founding time provisional — the composite Moon &amp; exact phase are soft.</div>';
  h+='<p><span class="phpill">'+n.phase+'</span> <span style="color:#8a8377">'+n.elong+'° into the ~30-yr cycle — '+(PHINT[n.phase]||'')+'</span></p>';
  h+='<p><b>Composite now:</b> Sun '+n.sun+' · Moon '+n.moon+'<br><span style="font-style:italic;color:#5b5347">“'+n.sunsab+'”</span></p>';
  if(n.aspects&&n.aspects.length) h+='<p><b>Tightest ties:</b> '+n.aspects.slice(0,4).map(function(a){return a[1]+' <span style="color:#8a8377">'+a[0].toFixed(2)+'°</span>'+(a[2]?' ★':'');}).join(' · ')+'</p>';
  if(cp.timeline&&cp.timeline.length) h+='<h3>The relationship’s Moon phases</h3><ul class="ct">'+cp.timeline.map(function(t){return '<li><b>'+t.ym+'</b> '+t.phase+' · '+t.signdeg+' <span style="color:#8a8377">'+t.sabian+'</span></li>';}).join('')+'</ul>';
  h+='<p class="note">New = re-opening · Full = confrontation · Last Quarter = rupture (★ = in a cardinal sign). US chart × this nation’s primary, both secondary-progressed then composited (Blaschke). Full digest: “The Progressed Nation.”</p></div>';
  return h;
}
var curNat=NAT_ORDER[0], curKey=null;
function renderNations(){
  document.getElementById('nations').innerHTML=NAT_ORDER.map(function(code){
    return '<button class="nat'+(code===curNat?' on':'')+'" data-n="'+code+'">'+META[code].flag+' '+META[code].name+'</button>';
  }).join('');
}
function renderTabs(){
  var m=META[curNat];
  document.getElementById('tabs').innerHTML=m.order.map(function(k){
    var c=m.charts[k];
    return '<button class="tab'+(k===curKey?' on':'')+'" data-k="'+k+'"><span class="tl">'+(c.primary?'★ ':'')+c.label+'</span><span class="tt">'+c.place+(c.prov?' · time ~':'')+'</span></button>';
  }).join('');
}
function renderPanel(){
  var m=META[curNat], c=m.charts[curKey], r=REC[curNat][curKey];
  var html='<div class="grid">'
   +'<div><div id="wheelbox"></div></div>'
   +'<div><div class="card idn"><h2>'+m.flag+' '+m.name+' — '+c.label+'</h2>'
   +'<p class="src">'+c.src+'</p>'
   +'<p class="angles"><b>'+c.time+'</b><br>Ascendant '+c.asc+' · MC '+c.mc+' · ruler '+c.ruler+'</p>'
   +'<h3>The skeleton read</h3>'+c.read+'</div></div></div>'
   +'<div class="card"><h2>Placements</h2>'+c.pl+'</div>'
   +compositeCard(curNat);
  document.getElementById('panel').innerHTML=html;
  document.getElementById('wheelbox').innerHTML=wheelSVG(r,null,false);
}
function pickNation(code){curNat=code; curKey=META[code].order.find(function(k){return META[code].charts[k].primary;})||META[code].order[0]; renderNations(); renderTabs(); renderPanel();}
document.getElementById('nations').addEventListener('click',function(e){var b=e.target.closest('.nat'); if(b) pickNation(b.dataset.n);});
document.getElementById('tabs').addEventListener('click',function(e){var b=e.target.closest('.tab'); if(b){curKey=b.dataset.k; renderTabs(); renderPanel();}});
pickNation(NAT_ORDER[0]);
</script>
</div></body></html>"""

nations_html="".join(
  f'<button class="nat{" on" if i==0 else ""}" data-n="{n["code"]}">{n["flag"]} {n["name"]}</button>'
  for i,n in enumerate(NATIONS))

out=(HTML.replace("__NATIONS__",nations_html)
        .replace("__DATE__",datetime.date.today().isoformat())
        .replace("__WHEEL_JS__",WHEEL_JS)
        .replace("__REC__",json.dumps(REC))
        .replace("__META__",json.dumps(META))
        .replace("__NATORDER__",json.dumps(NAT_ORDER))
        .replace("__COMP__",COMP))

OUT=os.environ.get("OUT","The World Charts.html")
with open(OUT,"w") as fh: fh.write(out)
print("wrote",OUT,len(out),"bytes ·",len(NATIONS),"nations ·",
      sum(len(n["charts"]) for n in NATIONS),"charts")
# quick verification dump
for n in NATIONS:
    for c in n["charts"]:
        jd=jd_of(c["y"],c["mo"],c["d"],c["h"],c["tz"])
        ch=compute_chart(jd,c["lat"],c["lon"])
        print(f"  {n['name']:14s} {c['label']:26s} ASC {signdeg(ch['asc']):16s} "
              f"Sun {signdeg(ch['lons']['Sun']):16s} Moon {signdeg(ch['lons']['Moon'])}")
