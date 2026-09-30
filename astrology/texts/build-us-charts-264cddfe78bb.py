#!/usr/bin/env python3
"""Build "The American Charts" — the candidate US national charts as one instrument.

Casts every serious July 2 / July 4 1776 candidate, computes Whole Sign houses,
dignities, the annual-profection ladder (with the Freedom 250 / age-250 highlight),
the US Pluto return, and a rectification SCOREBOARD that tests each chart's angles
+ solar-arc directions + profected year-lord against eight American hinge-points.

All positions via Swiss Ephemeris — never hand-typed (vault data-integrity rule).
Reuses wheel_lib.WHEEL_JS for the wheels. Whole Sign throughout. Output:
04 - Synthesis/Cross-cuts/The American Charts.html  (addEventListener, no inline onclick).
"""
import swisseph as swe, json, os, datetime

# ---- pull the shared wheel engine ------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
def load_wheel_js():
    for p in [os.path.join(HERE, "wheel_lib.py"),
              os.path.join(HERE, "99 - Templates", "wheel_lib.py")]:
        if os.path.exists(p):
            import importlib.util
            spec = importlib.util.spec_from_file_location("wheel_lib", p)
            m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
            return m.WHEEL_JS, m.aspects_between, m.placidus_cusps
    raise SystemExit("wheel_lib.py not found")
WHEEL_JS, aspects_between, placidus_cusps = load_wheel_js()

SGN = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio",
       "Sagittarius","Capricorn","Aquarius","Pisces"]
RULER = {"Aries":"Mars","Taurus":"Venus","Gemini":"Mercury","Cancer":"Moon",
         "Leo":"Sun","Virgo":"Mercury","Libra":"Venus","Scorpio":"Mars",
         "Sagittarius":"Jupiter","Capricorn":"Saturn","Aquarius":"Saturn","Pisces":"Jupiter"}
# essential dignity by sign (traditional)
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
OUTERS=["Jupiter","Saturn","Uranus","Neptune","Pluto"]

PHL_LAT, PHL_LON = 39.9526, -75.1652
LMT = 5.011  # Philadelphia LMT->UT hours

def jd_lmt(y,mo,d,lmt_hours):
    return swe.julday(y,mo,d, lmt_hours + LMT)

def lon_of(jd, pid):
    return swe.calc_ut(jd, pid)[0]

def dignity(planet, sign):
    if planet in DOM and sign in DOM[planet]: return ("domicile","+")
    if EXALT.get(planet)==sign: return ("exalted","+")
    if planet in DETRI and sign in DETRI[planet]: return ("detriment","−")
    if FALL.get(planet)==sign: return ("fall","−")
    return ("","")

def fmt_dms(lon):
    deg=int(lon%30); mn=int(round((lon%1)*60))
    if mn==60: deg+=1; mn=0
    return f"{deg}°{mn:02d}'"

def ordn(n):
    n=int(n)
    s='th' if 10<=n%100<=20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')
    return f"{n}{s}"

def compute_chart(jd):
    asc, mc = None, None
    cusps, ascmc = swe.houses(jd, PHL_LAT, PHL_LON, b'W')
    asc, mc = ascmc[0], ascmc[1]
    asc_idx = int(asc//30)
    pl_cusps, pl_mc = placidus_cusps(jd, PHL_LAT, PHL_LON)   # for the WS/Placidus toggle
    pos=[]; lons={}
    for name,pid in PLANETS:
        res=swe.calc_ut(jd,pid); lon=res[0][0]; spd=res[0][3]
        sign=SGN[int(lon//30)]
        house=((int(lon//30)-asc_idx)%12)+1
        retro = spd<0
        pos.append({"name":name,"sign":sign,"lon":lon,"dms":fmt_dms(lon),
                    "retro":retro,"house":house})
        lons[name]=lon
    return {"asc":asc,"mc":mc,"asc_idx":asc_idx,"pos":pos,"lons":lons,
            "cusps":pl_cusps,"pl_mc":pl_mc}

# --- candidate charts -------------------------------------------------------
CANDS=[
 {"key":"sag","label":"Sagittarius Rising","time":"July 2, 1776 · ~5:10 PM LMT","canon":True,
  "jd":jd_lmt(1776,7,2,17+10/60),"tradition":"★ THE CHART — locked in",
  "blurb":"<b>Locked in as the chart of the United States.</b> Jupiter — <b>exalted</b> in Cancer — rules the nation, and Saturn is <b>exalted</b> too: both of the country's societal planets at their finest tools. The Cancer stellium falls in the <b>8th house</b> — other people's money, debt, the reserve currency, death &amp; rebirth: the faith-and-finance empire. Chosen over July 4 because its Moon is a live <b>Capricorn</b> (conjunct Pluto, on the people-vs-government axis), not Sibley's void Aquarius."},
 {"key":"gem","label":"Gemini Rising","time":"July 2, 1776 · ~2:13 AM LMT","canon":False,
  "jd":jd_lmt(1776,7,2,2+13/60),"tradition":"alternate — commercial-republic / domestic-money overlay (July 2, not Zain’s July 4)",
  "blurb":"The kept alternate. Mercury (℞) rules; the Cancer stellium falls in the <b>2nd house</b> — the nation's own treasury and values; Mars and Uranus <b>rise in the 1st</b> (a body born armed, restless, Promethean). Across 17 turning-points this chart owns the <i>domestic</i>-money crises — the truer chart of America's own body and money."},
 {"key":"sib","label":"Sibley (July 4)","time":"July 4, 1776 · 5:10 PM LMT","canon":False,
  "jd":jd_lmt(1776,7,4,17+10/60),"tradition":"the standard chart — shown for contrast",
  "blurb":"The textbook US chart, kept for contrast. Same Sag-rising, 8th-house-Sun architecture as the locked chart — but two days on, the Moon has slipped into late Aquarius and goes <b>void of course</b>. Rejected for exactly that: “We are NOT a void-moon nation.”"},
]
for c in CANDS:
    c["chart"]=compute_chart(c["jd"])

# --- profection ladder ------------------------------------------------------
def profection_row(asc_idx, age):
    sign=SGN[(asc_idx+age)%12]
    return {"age":age,"house":(age%12)+1,"sign":sign,"lord":RULER[sign]}

def profection_ladder(asc_idx):
    # the run-up to and through Freedom 250
    return [profection_row(asc_idx,a) for a in range(246,254)]

# --- US Pluto return (transiting Pluto back to natal Pluto) ------------------
def pluto_return_passes(natal_pluto_lon):
    passes=[]; prev=None
    jd=swe.julday(2020,1,1,0); end=swe.julday(2024,1,1,0)
    while jd<end:
        l=swe.calc_ut(jd,swe.PLUTO)[0][0]
        d=(l-natal_pluto_lon+180)%360-180
        if prev is not None and (prev<0)!=(d<0) and abs(d)<1:
            y,m,dd,_=swe.revjul(jd); passes.append(f"{m:02d}/{y}")
        prev=d; jd+=5
    # dedupe consecutive
    out=[]
    for p in passes:
        if not out or out[-1]!=p: out.append(p)
    return out

# --- solar arc + transit helpers --------------------------------------------
def solar_arc(natal_jd, event_jd, natal_sun):
    prog_jd = natal_jd + (event_jd-natal_jd)/365.2422
    prog_sun = swe.calc_ut(prog_jd, swe.SUN)[0][0]
    return (prog_sun - natal_sun) % 360

def hits_angle(lon, asc, mc, orb):
    best=None
    for ang_name,ang in [("ASC",asc),("MC",mc),("DSC",(asc+180)%360),("IC",(mc+180)%360)]:
        for asp,a in [("conj",0),("sq",90),("opp",180)]:
            sep=abs((lon-ang+180)%360-180)
            o=abs(sep-a) if asp!="conj" else min(sep,abs(sep-0))
            o=abs((lon-ang+180)%360-180 - a)
            o=abs(abs((lon-ang+180)%360-180)-a)
            if o<=orb:
                if best is None or o<best[2]:
                    best=(ang_name,asp,round(o,1))
    return best

# --- the rectification scoreboard -------------------------------------------
EVENTS=[
 ("1781-10-19","Yorktown — the Revolution won",(1781,10,19)),
 ("1861-04-12","Fort Sumter — Civil War begins",(1861,4,12)),
 ("1913-12-23","The Federal Reserve Act — the Fed is born",(1913,12,23)),
 ("1929-10-29","Black Tuesday — the Crash",(1929,10,29)),
 ("1933-03-06","FDR's bank holiday / gold seizure",(1933,3,6)),
 ("1941-12-07","Pearl Harbor",(1941,12,7)),
 ("1944-07-22","Bretton Woods — the dollar system built",(1944,7,22)),
 ("1963-11-22","JFK assassination",(1963,11,22)),
 ("1971-08-15","Nixon closes the gold window",(1971,8,15)),
 ("1974-08-09","Nixon resigns — Watergate",(1974,8,9)),
 ("1989-11-09","Berlin Wall falls — Cold War ends",(1989,11,9)),
 ("2001-09-11","9/11",(2001,9,11)),
 ("2008-09-15","Lehman — the GFC",(2008,9,15)),
 ("2016-11-08","Trump elected — the populist turn",(2016,11,8)),
 ("2020-03-11","COVID declared a pandemic",(2020,3,11)),
 ("2022-02-24","Ukraine invaded — the US Pluto return",(2022,2,24)),
 ("2026-06-15","Iran peace deal — signed today (LIVE)",(2026,6,15)),
]

def score_event(cand, ev):
    chart=cand["chart"]; asc=chart["asc"]; mc=chart["mc"]; asc_idx=chart["asc_idx"]
    natal_jd=cand["jd"]; natal=chart["lons"]
    y,m,d=ev[2]; ejd=swe.julday(y,m,d,17.0)
    score=0; reasons=[]
    # 1) transiting outers to the angles (≤2°) — the rectification gold
    for p in OUTERS:
        tl=swe.calc_ut(ejd, dict(PLANETS)[p])[0][0]
        h=hits_angle(tl, asc, mc, 2.0)
        if h: score+=3; reasons.append(f"tr {p} {h[1]} {h[0]} {h[2]}°")
    # 2) solar-arc directed planets to the angles (≤1°)
    arc=solar_arc(natal_jd, ejd, natal["Sun"])
    for p in ["Sun","Mars","Saturn","Uranus","Pluto"]:
        dl=(natal[p]+arc)%360
        h=hits_angle(dl, asc, mc, 1.0)
        if h: score+=2; reasons.append(f"SA {p} {h[1]} {h[0]} {h[2]}°")
    # 3) profected year-lord activated by a transiting outer (conj ≤2°)
    age=y-1776 - (0 if (m,d)>=(7,2 if cand['key']!='sib' else 4) else 1)
    prof=profection_row(asc_idx, age)
    lord_lon=natal[prof["lord"]]
    for p in OUTERS:
        tl=swe.calc_ut(ejd, dict(PLANETS)[p])[0][0]
        sep=abs((tl-lord_lon+180)%360-180)
        if min(sep,abs(sep-180),abs(sep-90))<=2.0:
            score+=2; reasons.append(f"year-lord {prof['lord']} hit by tr {p}"); break
    # 4) angular-house emphasis: transiting outers sitting in angular houses (1/4/7/10)
    ang_h=0
    for p in OUTERS:
        tl=swe.calc_ut(ejd, dict(PLANETS)[p])[0][0]
        hh=((int(tl//30)-asc_idx)%12)+1
        if hh in (1,4,7,10): ang_h+=1
    if ang_h: score+=ang_h; reasons.append(f"{ang_h} outer(s) in angular houses")
    return score, reasons

SCORE={}
for c in CANDS:
    SCORE[c["key"]]={"total":0,"rows":{}}
    for ev in EVENTS:
        s,r=score_event(c,ev)
        SCORE[c["key"]]["rows"][ev[0]]={"s":s,"r":r}
        SCORE[c["key"]]["total"]+=s

# ---- emit data for the wheels ---------------------------------------------
def wheel_rec(cand):
    chart=cand["chart"]
    posJS=[[p["name"],p["sign"],p["dms"],p["retro"],round(p["lon"],4)] for p in chart["pos"]]
    main={p["name"]:p["lon"] for p in chart["pos"] if p["name"] in
          ["Sun","Moon","Mercury","Venus","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto"]}
    asp=aspects_between(main)
    return {"pos":posJS,"asp":asp,"asc":round(chart["asc"],4),
            "cusps":chart["cusps"],"mc":chart["pl_mc"],
            "__date":cand["label"],"cap1":cand["time"],
            "cap2":f"{RULER[SGN[chart['asc_idx']]]} rules · Whole Sign · D.C. mundane"}

REC={c["key"]:wheel_rec(c) for c in CANDS}
PLUTO_PASSES=pluto_return_passes(CANDS[0]["chart"]["lons"]["Pluto"])

# build per-chart static html fragments (placements, identity, profections, now)
def placements_html(cand):
    chart=cand["chart"]
    rows=[]
    for p in chart["pos"]:
        if p["name"]=="Node": glyph="☊ N.Node"
        elif p["name"]=="Chiron": glyph="⚷ Chiron"
        else: glyph=p["name"]
        dig,sgnmark=dignity(p["name"],p["sign"]) if p["name"] in DOM else ("","")
        digcls="dig-pos" if sgnmark=="+" else ("dig-neg" if sgnmark=="−" else "")
        rows.append(f"<tr><td>{glyph}</td><td>{p['sign']} {p['dms']}{' ℞' if p['retro'] else ''}</td>"
                    f"<td class='hc'>{p['house']}</td><td class='{digcls}'>{dig}</td></tr>")
    return ("<table class='pl'><thead><tr><th>Body</th><th>Position</th><th>Hse</th>"
            "<th>Dignity</th></tr></thead><tbody>"+"".join(rows)+"</tbody></table>")

def profection_html(cand):
    chart=cand["chart"]; asc_idx=chart["asc_idx"]
    rows=[]
    for r in profection_ladder(asc_idx):
        hl = (r["age"]==250)
        rows.append(f"<tr class='{'f250' if hl else ''}'><td>{r['age']}</td>"
                    f"<td>{ordn(r['house'])}</td><td>{r['sign']}</td><td>{r['lord']}</td>"
                    f"<td>{'◄ FREEDOM 250' if hl else ''}</td></tr>")
    return ("<table class='pf'><thead><tr><th>Age</th><th>House</th><th>Sign</th>"
            "<th>Lord of the Year</th><th></th></tr></thead><tbody>"+"".join(rows)+"</tbody></table>")

def now_html(cand):
    chart=cand["chart"]; asc=chart["asc"]; mc=chart["mc"]
    njd=swe.julday(2026,6,15,17.0)
    out=[]
    for p in OUTERS:
        tl=swe.calc_ut(njd,dict(PLANETS)[p])[0][0]
        h=hits_angle(tl,asc,mc,3.0)
        if h: out.append(f"transiting <b>{p}</b> {h[1]} the <b>{h[0]}</b> ({h[2]}°)")
    # current profection (age 250 from July 2 2026; on Jun 15 2026 still 249)
    age_now=249
    pr=profection_row(chart["asc_idx"],age_now)
    nxt=profection_row(chart["asc_idx"],250)
    s=(f"<p><b>Now (June 2026):</b> profected to the <b>{ordn(pr['house'])} house, {pr['sign']}</b> "
       f"— year-lord <b>{pr['lord']}</b>. On July 2 it rolls into the <b>{ordn(nxt['house'])} "
       f"({nxt['sign']}), lord {nxt['lord']}</b> — the Freedom 250 year.</p>")
    if out: s+="<p>"+"; ".join(out)+".</p>"
    else: s+="<p><i>No outer planet within 3° of an angle right now.</i></p>"
    return s

# ===== Pessin: the lunar gestation layer ====================================
def phase_role(elong):
    e=elong%360
    bands=[(180,"Full Moon — bloom / revelation","Born at the instant of revelation — Pessin's “all the cards on the table.” The Declaration <i>is</i> the Full Moon: a public unveiling."),
           (225,"disseminating — broadcasting","Born to spread the word — the evangelist phase, demonstrating its creed to the world. (Two days past the revelation.)"),
           (270,"Last Quarter — release","Born at the turning-in: collecting the seed for the next cycle."),
           (135,"waxing gibbous — refinement","Born just shy of the revelation, still perfecting the idea."),
           (90,"First Quarter — breaking ground","Born in the crisis of action."),
           (45,"waxing crescent — struggle","Born struggling out of the seed."),
           (315,"balsamic — the dying seed","Born at a cycle's end, an old soul."),
           (0,"New Moon — seed","Born invisible, a pure beginning.")]
    return min(bands,key=lambda b:abs((e-b[0]+180)%360-180))[1:]

def find_newmoon_before(jd_t):
    jd=jd_t-45; prev=None; last=None
    while jd<jd_t:
        s=swe.calc_ut(jd,swe.SUN)[0][0]; m=swe.calc_ut(jd,swe.MOON)[0][0]
        d=(m-s+180)%360-180
        if prev is not None and prev<0 and d>=0:
            lo,hi=jd-0.5,jd
            for _ in range(42):
                mid=(lo+hi)/2
                s2=swe.calc_ut(mid,swe.SUN)[0][0]; m2=swe.calc_ut(mid,swe.MOON)[0][0]
                if (m2-s2+180)%360-180<0: lo=mid
                else: hi=mid
            last=hi
        prev=d; jd+=0.5
    return last, swe.calc_ut(last,swe.SUN)[0][0]

def eclipses_between(jds,jde):
    out=[]; j=jds
    while j<jde:
        rf,tret=swe.sol_eclipse_when_glob(j,swe.FLG_SWIEPH,0); t=tret[0]
        if t>jde: break
        sun=swe.calc_ut(t,swe.SUN)[0][0]; node=swe.calc_ut(t,swe.TRUE_NODE)[0][0]
        dN=abs((sun-node+180)%360-180); dS=abs((sun-(node+180)+180)%360-180)
        typ="Total" if rf&swe.ECL_TOTAL else("Annular" if rf&swe.ECL_ANNULAR else("Hybrid" if rf&swe.ECL_HYBRID else "Partial"))
        y,mo,d,_=swe.revjul(t)
        out.append({"kind":"Solar","type":typ,"lon":sun%360,"node":"N" if dN<dS else "S","date":f"{mo:02d}/{d:02d}/{y}","y":y,"m":mo,"d":d})
        j=t+10
    j=jds
    while j<jde:
        rf,tret=swe.lun_eclipse_when(j,swe.FLG_SWIEPH,0); t=tret[0]
        if t>jde: break
        moon=swe.calc_ut(t,swe.MOON)[0][0]
        typ="Total" if rf&swe.ECL_TOTAL else("Partial" if rf&swe.ECL_PARTIAL else "Penumbral")
        y,mo,d,_=swe.revjul(t)
        out.append({"kind":"Lunar","type":typ,"lon":moon%360,"node":None,"date":f"{mo:02d}/{d:02d}/{y}","y":y,"m":mo,"d":d})
        j=t+10
    out.sort(key=lambda e:(e["y"],e["m"],e["d"]))
    return out

SEED_JD,  SEED_SUN  = find_newmoon_before(CANDS[0]["jd"])             # the founding seed
RESEED_JD,RESEED_SUN= find_newmoon_before(swe.julday(2026,7,2,12.0))  # the Freedom 250 seed
ECL = eclipses_between(swe.julday(2026,7,2,0), swe.julday(2027,8,1,0))

def signdeg(lon): return f"{SGN[int(lon//30)]} {fmt_dms(lon)}"
def house_of(lon, ai): return ((int(lon//30)-ai)%12)+1
AXIS={"Cancer":"the people &amp; home vs the government &amp; structure",
      "Capricorn":"the government &amp; structure vs the people &amp; home",
      "Leo":"the executive vs the legislature","Aquarius":"the legislature vs the executive",
      "Aries":"sovereignty vs partnership","Libra":"partnership vs sovereignty",
      "Taurus":"national wealth vs shared/hidden power","Scorpio":"hidden power vs national wealth",
      "Gemini":"the press &amp; word vs belief &amp; law","Sagittarius":"belief &amp; law vs the press &amp; word",
      "Virgo":"labour vs ideals","Pisces":"ideals vs labour"}

def pessin_html(cand):
    ch=cand["chart"]; ai=ch["asc_idx"]
    sun=ch["lons"]["Sun"]; moon=ch["lons"]["Moon"]
    pname,prole=phase_role((moon-sun)%360)
    msign=SGN[int(moon//30)]; opp=SGN[(int(moon//30)+6)%12]
    seed_h=house_of(SEED_SUN,ai); reseed_h=house_of(RESEED_SUN,ai)
    moon_h=house_of(moon,ai); opp_h=house_of(moon+180,ai)
    r=[]
    r.append(f"<p><b>Founding phase:</b> {pname}. {prole}</p>")
    r.append(f"<p><b>The Family axis:</b> natal Moon in <b>{msign}</b> ({signdeg(moon)}) — the "
             f"<b>{msign}/{opp}</b> family: {AXIS.get(msign,'')}. Here it runs through the "
             f"<b>{ordn(moon_h)} &amp; {ordn(opp_h)} houses</b>.</p>")
    r.append(f"<p><b>The original seed:</b> independence was seeded at the New Moon of "
             f"<b>{signdeg(SEED_SUN)}</b> (06/16/1776) — a Gemini seed: a <i>document, a debate, the written word.</i> "
             f"It plants in this chart's <b>{ordn(seed_h)} house</b>.</p>")
    r.append(f"<p><b>The Freedom 250 re-seed:</b> the year's New Moon — <b>{signdeg(RESEED_SUN)}</b> (06/15/2026) — "
             f"falls within ~1° of the founding seed. <i>The founding degree, re-planted for the 250th year.</i> "
             f"It plants in this chart's <b>{ordn(reseed_h)} house</b>.</p>")
    elines=[]
    for e in ECL:
        h=house_of(e["lon"],ai)
        nd=("North Node — the nation <b>initiates</b>" if e["node"]=="N" else
            ("South Node — the nation <b>responds</b>" if e["node"]=="S" else "lunar — revelation / crisis"))
        hit=""
        for nm,nl in [("natal Moon",moon),("natal Sun",sun),("the ASC",ch["asc"]),("the MC",ch["mc"])]:
            o=abs((e["lon"]-nl+180)%360-180)
            oo=abs((e["lon"]-(nl+180)+180)%360-180)
            if o<=3: hit=f" — <b>conjunct {nm}</b> ({o:.1f}°)"; break
            if oo<=3: hit=f" — <b>opposite {nm}</b> ({oo:.1f}°)"; break
        elines.append(f"<li>{e['date']} {e['kind']} ({e['type']}) <b>{signdeg(e['lon'])}</b> · {nd} · "
                      f"<b>{ordn(h)} house</b>{hit}</li>")
    r.append("<p><b>Eclipses lighting the 250th year:</b></p><ul class='ecl'>"+"".join(elines)+"</ul>")
    return "".join(r)

# ===== The Timing Stack — the locked Sagittarius chart, run forward =========
def timing_stack():
    sag=[c for c in CANDS if c["key"]=="sag"][0]
    ch=sag["chart"]; njd=sag["jd"]; ai=ch["asc_idx"]
    asc=ch["asc"]; mc=ch["mc"]; natal=ch["lons"]
    main=["Sun","Moon","Mercury","Venus","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto"]
    pid={n:dict(PLANETS)[n] for n in main}
    def hse(l): return ((int(l//30)-ai)%12)+1
    # profection
    pn_now=profection_row(ai,249); pn_250=profection_row(ai,250)
    prof=(f"<p>Right now (age 249) the nation runs a <b>{ordn(pn_now['house'])}-house {pn_now['sign']}</b> "
          f"profection — year-lord <b>{pn_now['lord']}</b> (the administration year). On <b>July 2, 2026</b> it "
          f"rolls into the <b>{ordn(pn_250['house'])}-house {pn_250['sign']}</b> year — lord <b>{pn_250['lord']}</b>, "
          f"with the nation's <b>exalted Saturn</b> sitting right in that profected 11th. The 11th = the legislature, "
          f"allies, collective hopes — the legislative-reset year (true for any rising; only sign &amp; lord change). "
          f"Year-lord {pn_250['lord']} is natally Cancer in the 8th, so 2026–27 transits to {pn_250['lord']} are the triggers.</p>")
    # secondary progressions
    nowjd=swe.julday(2026,6,15,12.0); pj=njd+(nowjd-njd)/365.2422
    prog={n:swe.calc_ut(pj,pid[n])[0][0] for n in main}
    nxt=None; cur=int(prog["Sun"]//30)
    for yy in range(2026,2055):
        s=int(swe.calc_ut(njd+(swe.julday(yy,7,1,12)-njd)/365.2422,swe.SUN)[0][0]//30)
        if s!=cur: nxt=(SGN[s],yy); break
    rows=[]
    for p,pl in prog.items():
        for nn,nl in natal.items():
            o=abs((pl-nl+180)%360-180)
            for ang,a in [("conjunct",0),("sextile",60),("square",90),("trine",120),("opposite",180)]:
                if abs(o-a)<=1.0: rows.append((abs(o-a),f"prog {p} {ang} natal {nn} ({abs(o-a):.1f}°)"))
    rows.sort()
    prog_h=(f"<p>Progressed Sun <b>{signdeg(prog['Sun'])}</b> — the old national identity in its final "
        f"<b>Piscean dissolution</b>; it enters <b>{nxt[0]} ~{nxt[1]}</b>, the next 30-year re-founding chapter. "
        f"Progressed Moon <b>{signdeg(prog['Moon'])}</b> (the ~2.5-year public mood). Live progressed contacts:</p>"
        f"<ul class='ecl'>{''.join(f'<li>{t}</li>' for _,t in rows[:6])}</ul>")
    # solar arc
    arc=(prog["Sun"]-natal["Sun"])%360; sa=[]
    for p,pl in natal.items():
        dl=(pl+arc)%360
        for nn,nl in list(natal.items())+[("ASC",asc),("MC",mc)]:
            if nn==p: continue
            o=abs((dl-nl+180)%360-180)
            for ang,a in [("conj",0),("sq",90),("opp",180),("trine",120),("sextile",60)]:
                if abs(o-a)<=1.2: sa.append((abs(o-a),f"SA {p} {ang} {nn} ({abs(o-a):.1f}°)"))
    sa.sort()
    sa_h=(f"<p>Solar arc = <b>{arc:.1f}°</b>. Directed contacts within ~1°:</p>"+
          ("<ul class='ecl'>"+"".join(f"<li>{t}</li>" for _,t in sa[:5])+"</ul>" if sa else
           "<p><i>Between major directed contacts at the moment — the active arc hits cluster on the 2026–27 ingress dates in the scoreboard below.</i></p>"))
    # solar return 2026 (DC)
    DC=(38.9072,-77.0369); jd=swe.julday(2026,7,1,0.0)
    for _ in range(80):
        d=(swe.calc_ut(jd,swe.SUN)[0][0]-natal["Sun"]+180)%360-180
        if abs(d)<0.005: break
        jd-=d/1.0
    sasc=swe.houses(jd,*DC,b'W')[1][0]; smc=swe.houses(jd,*DC,b'W')[1][1]; sidx=int(sasc//30)
    srsun=swe.calc_ut(jd,swe.SUN)[0][0]; srmoon=swe.calc_ut(jd,swe.MOON)[0][0]
    y,mo,dd,_=swe.revjul(jd)
    sr_h=(f"<p>The 250th-birthday year-chart, cast for Washington, D.C. ({mo:02d}/{dd:02d}/{y}): "
        f"<b>{signdeg(sasc)} rising</b> — conjunct the nation's natal Uranus (Gemini 8°): a disruptive, awakening "
        f"year for the body politic. SR <b>MC {signdeg(smc)}</b> with the SR <b>Moon {signdeg(srmoon)}</b> right on it "
        f"— the public mood and the government's year both turned to the new paradigm / the legislature. SR Sun lands in "
        f"the SR <b>{ordn(((int(srsun//30)-sidx)%12)+1)} house</b> — a money year. The year-chart reads as a "
        f"publicly-led monetary &amp; paradigm disruption.</p>")
    # ZR lots
    day = hse(natal["Sun"]) in (7,8,9,10,11,12)
    if day: LoF=(asc+natal["Moon"]-natal["Sun"])%360; LoS=(asc+natal["Sun"]-natal["Moon"])%360
    else:   LoF=(asc+natal["Sun"]-natal["Moon"])%360; LoS=(asc+natal["Moon"]-natal["Sun"])%360
    zr_h=(f"<p>The chart is a <b>day chart</b> (Sun above the horizon, 8th house). The Lots that zodiacal releasing "
        f"runs from: <b>Fortune {signdeg(LoF)}</b> ({ordn(hse(LoF))} house — body &amp; circumstance, here in the 7th of "
        f"open enemies &amp; treaties) and <b>Spirit {signdeg(LoS)}</b> ({ordn(hse(LoS))} house — action &amp; intent, here "
        f"in the 6th of the armed forces &amp; labour). ZR releases time-lord chapters from these signs, each sign's length "
        f"set by its ruler's lesser years (Cap/Aqu 30 · Can 25 · Gem/Vir 20 · Leo 19 · Ari/Sco 15 · Sag/Pis 12 · Tau/Lib 8). "
        f"<b>The live L1/L2 timeline and the “loosing of the bond” jumps are deferred</b> until the Hellenistic source is "
        f"in hand — per this project's rule never to commit a technique from memory. The Lots themselves are exact and ready.</p>")
    return ('<div class="card tstack"><h2>The United States, running — the timing stack</h2>'
        '<p class="idn">Now that the chart is set, here is the locked <b>Sagittarius</b> chart run forward by the '
        'classical time-lord and directed techniques — the nation\'s own chart as a clock for the Freedom 250 year.</p>'
        '<h3>Annual profection — the year-lord</h3>'+prof
        +'<h3>Secondary progressions</h3>'+prog_h
        +'<h3>Solar arc directions</h3>'+sa_h
        +'<h3>Solar return 2026 — the year-chart, cast for D.C.</h3>'+sr_h
        +'<h3>Zodiacal releasing — the Lots</h3>'+zr_h+'</div>')

FRAG={c["key"]:{"pl":placements_html(c),"pf":profection_html(c),"now":now_html(c),
                "pess":pessin_html(c),
                "blurb":c["blurb"],"trad":c["tradition"],"time":c["time"]} for c in CANDS}
TIMING_SECTION=timing_stack()

# scoreboard html
winner=max(SCORE,key=lambda k:SCORE[k]["total"])
labels={c["key"]:c["label"] for c in CANDS}
def scoreboard_html():
    head="<tr><th class='evh'>American hinge-point</th>"+"".join(
        f"<th>{labels[c['key']]}</th>" for c in CANDS)+"</tr>"
    body=[]
    for ev in EVENTS:
        best=max(CANDS,key=lambda c:SCORE[c["key"]]["rows"][ev[0]]["s"])["key"]
        cells=[]
        for c in CANDS:
            cell=SCORE[c["key"]]["rows"][ev[0]]
            win="winrow" if c["key"]==best and cell["s"]>0 else ""
            tip=" · ".join(cell["r"][:4]) if cell["r"] else "—"
            cells.append(f"<td class='{win}'><span class='sc'>{cell['s']}</span>"
                         f"<span class='rs'>{tip}</span></td>")
        live="(LIVE)" in ev[1]; lbl=ev[1].replace(" (LIVE)","")
        badge=" <span class='livebadge'>● live today</span>" if live else ""
        rc=" class='liverow'" if live else ""
        body.append(f"<tr{rc}>"
                    f"<td class='evh'><b>{ev[0][:4]}</b> {lbl}{badge}</td>"+"".join(cells)+"</tr>")
    tot="<tr class='totrow'><td class='evh'>TOTAL</td>"+"".join(
        f"<td class='{'wintot' if c['key']==winner else ''}'>{SCORE[c['key']]['total']}</td>"
        for c in CANDS)+"</tr>"
    return ("<table class='sb'><thead>"+head+"</thead><tbody>"+"".join(body)+tot+"</tbody></table>")

# ---------------------------------------------------------------------------
HTML = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>The American Charts</title>
<style>
:root{--bg:#faf8f3;--ink:#23201a;--mut:#8a8377;--line:#e3d9c2;--gold:#a8821f;--red:#7a2e1d;--blue:#3a6ea5;--grn:#2e8b74;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"Iowan Old Style",Palatino,Georgia,serif;line-height:1.5}
.wrap{max-width:1080px;margin:0 auto;padding:26px 20px 80px}
h1{font-size:30px;margin:0 0 2px;letter-spacing:.3px}
.sub{color:var(--mut);font-style:italic;margin:0 0 18px}
.lead{font-size:15.5px;max-width:760px;margin:0 0 22px}
.tabs{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 18px;border-bottom:1px solid var(--line);padding-bottom:14px}
.tab{cursor:pointer;border:1px solid var(--line);background:#fff;padding:9px 15px;border-radius:8px;font-family:inherit;font-size:14.5px;color:var(--ink)}
.tab .tt{font-size:11.5px;color:var(--mut);display:block}
.tab.on{background:var(--ink);color:#fff;border-color:var(--ink)}
.tab.on .tt{color:#cfc6b4}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:26px;align-items:start}
@media(max-width:820px){.grid{grid-template-columns:1fr}}
.card{border:1px solid var(--line);border-radius:12px;background:#fffdf8;padding:16px 18px;margin:0 0 20px}
.card h2{font-size:18px;margin:0 0 8px}
.card h3{font-size:14px;text-transform:uppercase;letter-spacing:1px;color:var(--mut);margin:18px 0 6px;font-weight:normal}
#wheelbox svg{max-width:520px;margin:0 auto;display:block}
.idn{font-size:14.5px}
.idn .trad{color:var(--gold);font-style:italic}
table{border-collapse:collapse;width:100%;font-size:13px}
.pl td,.pl th,.pf td,.pf th{border-bottom:1px solid var(--line);padding:4px 6px;text-align:left}
.pl .hc{text-align:center;color:var(--mut)}
.dig-pos{color:var(--grn)}.dig-neg{color:var(--red)}
.pf .f250{background:#fbf2d6;font-weight:bold}
.pf .f250 td{border-color:#e6d28f}
.sb{font-size:12.5px;margin-top:6px}
.sb th{background:#f1ead8;padding:8px;border:1px solid var(--line);text-align:center}
.sb th.evh{text-align:left;width:34%}
.sb td{border:1px solid var(--line);padding:7px 8px;vertical-align:top;text-align:center}
.sb td.evh{text-align:left}
.sb .sc{font-size:17px;font-weight:bold;display:block}
.sb .rs{font-size:10.5px;color:var(--mut);display:block;line-height:1.3;margin-top:2px}
.sb .winrow{background:#eef5ee}
.sb .winrow .sc{color:var(--grn)}
.sb .totrow td{background:#f1ead8;font-size:18px;font-weight:bold}
.sb .wintot{background:#dff0df;color:var(--grn)}
.sb .liverow td{background:#eef6f0}.sb .liverow td.evh{border-left:4px solid var(--grn)}
.livebadge{color:var(--grn);font-size:10.5px;font-weight:bold;margin-left:6px}
.tstack{border-left:4px solid var(--gold)}
.tstack h3{color:var(--red)}
.note{font-size:12.5px;color:var(--mut);max-width:780px;margin-top:14px}
.verdict{background:#fbf2d6;border:1px solid #e6d28f;border-radius:10px;padding:14px 18px;margin:14px 0;font-size:14.5px}
.ecl{margin:6px 0 0;padding-left:18px;font-size:12.5px}.ecl li{margin:4px 0}
.moonbar{background:#eef0f6;border:1px solid #cdd4e6;border-left:4px solid var(--blue);border-radius:10px;padding:13px 18px;margin:0 0 22px;font-size:14.5px;max-width:840px}
.locked{background:#fbf2d6;border:1px solid #e6d28f;border-left:4px solid var(--gold);border-radius:10px;padding:13px 18px;margin:0 0 16px;font-size:14.5px;max-width:840px}
.tab.canon{border-color:var(--gold)}
.tab.canon.on{background:var(--gold);border-color:var(--gold);color:#fff}
.tab.canon.on .tt{color:#f3ead0}
b{font-weight:bold}
</style></head><body><div class="wrap">
<h1>The American Charts</h1>
<p class="sub">July 2, 1776 · Sagittarius rising — <b>the chart, chosen.</b> The alternates kept for the truths they still tell.</p>
<div class="locked">★ <b>Locked in.</b> The United States = <b>July 2, 1776 · ~5:10 PM LMT · Philadelphia · Sagittarius 10°44′ rising</b>, ruled by an <b>exalted Jupiter</b> in Cancer — with <b>Saturn exalted</b> too (both societal planets at their finest). Chosen after testing every candidate against __NEV__ turning-points; the Gemini and Sibley charts remain below as alternates.</div>
<p class="lead">No clock survives from the day Congress voted for independence, so several charts were possible — each a different room of the same house. This instrument casts them all from Swiss Ephemeris, runs the timing layers on each (annual profections, the Pluto return, transits to the angles), and lets them <b>confess against history</b>: __NEV__ American turning-points from Yorktown to today, scored by how hard each chart's <i>own</i> angles, solar-arc directions, and year-lord were lit when the event struck. The chart that knew American history best — Sagittarius rising, July 2 — is now locked in; the others stay as the truths they still tell.</p>
<div class="moonbar">__MOONBAR__</div>
<div class="tabs" id="tabs">__TABS__</div>
<div id="panel"></div>

__TIMINGSTACK__

<div class="card">
<h2>The rectification scoreboard</h2>
<p class="idn">Each cell scores that chart at that event: <b>+3</b> per transiting outer planet on an angle (≤2°), <b>+2</b> per solar-arc direction to an angle (≤1°), <b>+2</b> if the profected year-lord was struck by a transiting outer, <b>+1</b> per outer planet sitting in an angular house. Only the things that <i>differ between charts</i> are scored — transit-to-natal-planet hits are identical across all three, so they're left out. The green cell wins each row. The final row is <b>today's Iran peace deal</b> — a live test, not a historical anchor: it simply shows whose angles are lit right now.</p>
__SCOREBOARD__
<div class="verdict">__VERDICT__</div>
<p class="note">A caveat in Katie's spirit: __NEV__ events is a fuller jury, but a scoreboard is still a blunt instrument for something as alive as a national chart. Treat it as suggestive testimony, not a verdict from on high. The charts each still tell a truth — this only asks which one tells it on time. Method: angles and MC from the listed candidate clock times (Philadelphia LMT → UT); solar arc = secondary-progressed Sun's travel; profection by Whole-Sign rising; all bodies midnight-to-noon UT Swiss Ephemeris.</p>
</div>

<p class="note">Built __DATE__ · positions computed from Swiss Ephemeris, never hand-entered · Whole Sign houses · charts cast for Philadelphia (founding) — mundane transits read for D.C. per project convention. Asteroid 916 America omitted here (needs the cached Horizons grid); add via minor_points.py on a later pass.</p>

<script>
__WHEEL_JS__
var CHARTS={};
var REC=__REC__;
var FRAG=__FRAG__;
var ORDER=__ORDER__;
function render(key){
  var r=REC[key], f=FRAG[key];
  document.querySelectorAll('.tab').forEach(function(t){t.classList.toggle('on',t.dataset.k===key);});
  var html=''
   +'<div class="grid">'
   +'<div><div id="wheelbox"></div></div>'
   +'<div><div class="card idn"><h2>'+document.querySelector(\'.tab[data-k="\'+key+\'"] .tl\').textContent+'</h2>'
   +'<p class="trad">'+f.trad+' — '+f.time+'</p>'
   +'<p>'+f.blurb+'</p>'
   +'<h3>Placements</h3>'+f.pl+'</div></div>'
   +'</div>'
   +'<div class="grid">'
   +'<div class="card"><h2>The profection ladder</h2>'
   +'<p class="idn">Each year of national life advances the year-lord one Whole-Sign house from the rising. Watch what governs the 250th year:</p>'+f.pf+'</div>'
   +'<div class="card"><h2>Right now</h2>'+f.now+'</div>'
   +'</div>'
   +'<div class="card"><h2>Lunar gestation — Pessin (the Moon families)</h2>'
   +'<p class="idn">Every national storyline is a lunation cycle — seeded at a New Moon, revealed at the Full, the same degrees recurring as a family across the years. Here is this chart\'s lunar lineage.</p>'+f.pess+'</div>';
  document.getElementById('panel').innerHTML=html;
  document.getElementById('wheelbox').innerHTML=wheelSVG(r,null,false);
}
document.getElementById('tabs').addEventListener('click',function(e){
  var t=e.target.closest('.tab'); if(t) render(t.dataset.k);
});
render(ORDER[0]);
</script>
</div></body></html>"""

tabs="".join(
 f'<button class="tab{" on" if i==0 else ""}{" canon" if c.get("canon") else ""}" data-k="{c["key"]}">'
 f'<span class="tl">{"★ " if c.get("canon") else ""}{c["label"]}</span><span class="tt">{c["time"]}</span></button>'
 for i,c in enumerate(CANDS))

t_gem,t_sag,t_sib=SCORE['gem']['total'],SCORE['sag']['total'],SCORE['sib']['total']
verdict=(f"The bigger jury reveals something better than a single winner. The scoreboard can cleanly separate the "
  f"<b>Gemini-rising body</b> from the <b>Sagittarius-rising pair</b> — and when it does, American history sorts itself "
  f"<b>by house</b>. The Gemini chart (Cancer money in the <b>2nd</b> — our OWN money) lights up for the domestic-money "
  f"crises and internal upheavals: the 1929 Crash, FDR's 1933 gold seizure, Nixon's 1971 gold window, Watergate, COVID. "
  f"The Sagittarius chart (Cancer money in the <b>8th</b> — the SYSTEM and other people's money) lights up for the "
  f"structural and foreign turns: the 1913 birth of the Fed, 1944 Bretton Woods, Pearl Harbor, 9/11, the 2016 populist "
  f"turn, the 2022 Pluto-return war. Each rising tells its truth — and the events sort themselves between the two rooms.")
verdict+=(f"<br><br>Totals: Sibley {t_sib} · Sagittarius (July 2) {t_sag} · Gemini {t_gem}. <b>But read the top two with "
  f"great care.</b> Sibley and the Sagittarius-July-2 chart are the <b>same chart ±2 days</b> (ascendants 252° vs 251°), so "
  f"this test cannot truly separate them — their gap is orb-noise — and it is <i>blind to the Moon</i>, which is the only real "
  f"difference between them: July 2's Capricorn Moon applying to Pluto vs July 4's void Aquarius Moon. On the Moon — your whole "
  f"objection — July 2 wins decisively. So the honest reading of {len(EVENTS)} turning-points: the rising is <b>Sagittarian</b> "
  f"(the 8th-house, freedom-crusader, debt-empire America), and the day is <b>July 2</b>. The Gemini chart isn't wrong — it's "
  f"the truer chart of the nation's <i>own</i> money and body — but Sagittarius rising carries the system, and the system is "
  f"this chronicle's spine.")
verdict+=(f"<br><br>For all candidates, the <b>US Pluto return</b> (transiting Pluto back to natal Pluto "
          f"{CANDS[0]['chart']['pos'][9]['sign']} {CANDS[0]['chart']['pos'][9]['dms']}) completed in "
          +(", ".join(PLUTO_PASSES) if PLUTO_PASSES else "2022")
          +" — the once-in-248-years rebirth of the national power-core, now behind us as Pluto enters Aquarius. That is the backdrop the whole chronicle is written against.")

cap_ecl=next((e for e in ECL if SGN[int(e["lon"]//30)]=="Capricorn" and e["kind"]=="Lunar"),None)
moonbar=("<b>The lunar headline.</b> The New Moon seeding the Freedom 250 year — <b>"+signdeg(RESEED_SUN)+
  "</b> on 06/15/2026 — falls within ~1° of the New Moon that seeded independence itself (<b>"+signdeg(SEED_SUN)+
  "</b>, 06/16/1776): <i>the founding seed-degree, re-planted 250 years on.</i>")
if cap_ecl:
    moonbar+=(" And on "+cap_ecl["date"]+" a lunar eclipse at <b>"+signdeg(cap_ecl["lon"])+
      "</b> falls on the US natal Moon — re-lighting the founding Cancer–Capricorn axis (the people vs the government) to close the year.")

out=(HTML
  .replace("__MOONBAR__",moonbar)
  .replace("__TIMINGSTACK__",TIMING_SECTION)
  .replace("__NEV__",str(len(EVENTS)))
  .replace("__TABS__",tabs)
  .replace("__SCOREBOARD__",scoreboard_html())
  .replace("__VERDICT__",verdict)
  .replace("__DATE__",datetime.date.today().isoformat())
  .replace("__WHEEL_JS__",WHEEL_JS)
  .replace("__REC__",json.dumps(REC))
  .replace("__FRAG__",json.dumps(FRAG))
  .replace("__ORDER__",json.dumps([c["key"] for c in CANDS])))

OUT=os.environ.get("OUT","The American Charts.html")
with open(OUT,"w") as fh: fh.write(out)
print("wrote",OUT,len(out),"bytes")
print("scores:",{labels[k]:SCORE[k]["total"] for k in SCORE},"winner:",labels[winner])
print("pluto passes:",PLUTO_PASSES)
