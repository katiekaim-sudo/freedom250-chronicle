#!/usr/bin/env python3
"""build_entity_charts.py — cast a natal chart for every dated federal entity.

Reads entity_founding_dates.json and casts a Whole Sign chart per entity via
Swiss Ephemeris (Moshier for Sun..Pluto+Node so it works 1775→now with no files):

  - TIME: documented official time where it exists (OVERRIDES — the US locked
    July-2-1776 Sag chart; the Fed's ~6:02 PM EST signing). Else a SUNRISE chart
    (Sun on the Ascendant) at the founding city — the vault's standard fallback.
  - PLACE: founding / HQ city (Reserve Banks in their cities, BIS in Basel, …);
    federal default Washington D.C.
  - POINTS: Sun–Pluto, the True Node + South Node, Chiron (swisseph ephe files,
    1800+), and asteroid 916 America — from the vault's cached grid for 2024–27
    dates, and from JPL-Horizons flagship values (AMERICA_OVERRIDE) for the key
    historical charts. America is the Chronicle's signature point.

Output: 04 - Synthesis/Entity Theory/entity_charts.json (keyed by name).
First-pass dates — verify exact day/time before load-bearing readings.
"""
import os, re, json, importlib.util, datetime
import swisseph as swe
from chart_conventions import DC

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(HERE)
SEED = os.path.join(VAULT, "04 - Synthesis", "Entity Theory", "entity_founding_dates.json")
OUT  = os.path.join(VAULT, "04 - Synthesis", "Entity Theory", "entity_charts.json")
FG   = os.path.join(VAULT, "04 - Synthesis", "Cross-cuts", "The Federal Group.html")

spec = importlib.util.spec_from_file_location("wheel_lib", os.path.join(HERE, "wheel_lib.py"))
wl = importlib.util.module_from_spec(spec); spec.loader.exec_module(wl)
# minor_points sets the ephe path (enables Chiron + cached America)
mpspec = importlib.util.spec_from_file_location("minor_points", os.path.join(HERE, "minor_points.py"))
mp = importlib.util.module_from_spec(mpspec); mpspec.loader.exec_module(mp)

SIGNS = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio",
         "Sagittarius","Capricorn","Aquarius","Pisces"]
PLANETS = [("Sun",swe.SUN),("Moon",swe.MOON),("Mercury",swe.MERCURY),("Venus",swe.VENUS),
           ("Mars",swe.MARS),("Jupiter",swe.JUPITER),("Saturn",swe.SATURN),
           ("Uranus",swe.URANUS),("Neptune",swe.NEPTUNE),("Pluto",swe.PLUTO)]
FLAGS = swe.FLG_MOSEPH | swe.FLG_SPEED

CITY = {
    "Washington": DC, "Philadelphia": (39.9526,-75.1652),
    "Boston": (42.3601,-71.0589), "New York": (40.7128,-74.0060),
    "Cleveland": (41.4993,-81.6944), "Richmond": (37.5407,-77.4360),
    "Atlanta": (33.7490,-84.3880), "Chicago": (41.8781,-87.6298),
    "St. Louis": (38.6270,-90.1994), "Minneapolis": (44.9778,-93.2650),
    "Kansas City": (39.0997,-94.5786), "Dallas": (32.7767,-96.7970),
    "San Francisco": (37.7749,-122.4194), "Basel": (47.5596,7.5886),
    "Geneva": (46.2044,6.1432), "Paris": (48.8566,2.3522), "Madrid": (40.4168,-3.7038),
    "Manila": (14.5995,120.9842), "Abidjan": (5.3600,-4.0083), "London": (51.5074,-0.1278),
    "Bretton Woods": (44.2581,-71.4406),
}
NAME_CITY = {
    "Bank for International Settlements":"Basel", "Basel Committee on Banking Supervision":"Basel",
    "Financial Stability Board":"Basel", "World Health Organization":"Geneva",
    "World Trade Organization":"Geneva", "ILO · FAO":"Geneva", "UNESCO":"Paris",
    "OECD":"Paris", "FATF":"Paris", "IOSCO":"Madrid", "Asian Development Bank":"Manila",
    "African Development Bank":"Abidjan", "EBRD":"London", "United Nations":"New York",
    "Bretton Woods institutions":"Bretton Woods",
}
def jd_ut(y,mo,d,h): return swe.julday(y,mo,d,h)
def jd_lmt(y,mo,d,h,lon): return swe.julday(y,mo,d, h - lon/15.0)
OVERRIDES = {
    "United States": {"jd": jd_lmt(1776,7,2,17+10/60,-75.1652), "loc": CITY["Philadelphia"],
                      "place":"Philadelphia", "src":"Katie's locked US chart (5:10 PM LMT)"},
    "The Federal Reserve System": {"jd": jd_ut(1913,12,23,23+2/60), "loc": DC,
                      "place":"Washington", "src":"documented signing (~6:02 PM EST)"},
}
# 916 America geocentric ecliptic longitude at 00:00 UT of the founding day,
# from JPL Horizons (flagship historical charts; the cached grid covers 2024–27).
AMERICA_OVERRIDE = {
    "United States":207.19, "Dept of the Treasury":143.03,
    "The Federal Reserve System":201.11, "Board of Governors":201.11,
    "≈2,000 member banks (statutory stock subscribers)":201.11, "The 12 Federal Reserve Banks":241.00,
    "Bank for International Settlements":17.64, "SEC":67.73,
    "Social Security Administration":163.53, "Fannie Mae":40.89,
    "IMF":152.83, "World Bank Group":152.83, "IBRD":152.83, "Freddie Mac":57.84,
}

def sgn(l): return SIGNS[int(l//30)%12]
def dms(l):
    d=int(l%30); m=int(round((l%30-d)*60))
    if m==60: d+=1; m=0
    return f"{d}°{m:02d}'"
def sunrise_jd(y,mo,d,lat,lon):
    jd0 = swe.julday(y,mo,d,0.0)
    return swe.rise_trans(jd0, swe.SUN, swe.CALC_RISE|swe.BIT_DISC_CENTER, (lon,lat,0),0,0,FLAGS)[1][0]

def cast(jd, lat, lon, name):
    lons={}; pos=[]
    for nm,const in PLANETS:
        r = swe.calc_ut(jd, const, FLAGS)[0]
        l=r[0]%360; lons[nm]=l
        pos.append([nm, sgn(l), dms(l), 1 if r[3]<0 else 0, round(l,2)])
    node = swe.calc_ut(jd, swe.TRUE_NODE, FLAGS)[0][0]%360
    lons["Node"]=node; pos.append(["Node", sgn(node), dms(node), 0, round(node,2)])
    snode=(node+180)%360; pos.append(["SNode", sgn(snode), dms(snode), 0, round(snode,2)])
    # Chiron (swiss ephe; 1800+ only)
    chi=None
    try:
        chi = swe.calc_ut(jd, swe.CHIRON)[0][0]%360
        pos.append(["Chiron", sgn(chi), dms(chi), 0, round(chi,2)])
    except Exception:
        pass
    # 916 America — override (flagship) or cached grid (2024–27)
    am=None
    if name in AMERICA_OVERRIDE:
        am=AMERICA_OVERRIDE[name]%360
    else:
        try: am=mp.america_lon(jd)%360
        except Exception: am=None
    if am is not None:
        pos.append(["America", sgn(am), dms(am), 0, round(am,2)])
    asc = swe.houses(jd, lat, lon, b'W')[1][0] % 360
    planetdict={k:lons[k] for k in lons if k!="Node"}
    asp = wl.aspects_between(planetdict)
    asp += wl.point_aspects({"Node":lons["Node"]}, planetdict)
    if chi is not None: asp += wl.point_aspects({"Chiron":chi}, planetdict)
    if am  is not None: asp += wl.point_aspects({"America":am}, planetdict)
    asp.sort(key=lambda a:a["o"])
    return pos, round(asc,2), asp, am

def city_for(name):
    if name in NAME_CITY: return NAME_CITY[name]
    m = re.match(r'^\d+ · (.+)$', name)
    if m and m.group(1) in CITY: return m.group(1)
    return "Washington"

def america_hit(am, asc, pos):
    """Nearest tight (≤3°) contact of America to the ASC or a planet, for the drawer."""
    if am is None: return None
    def sep(a,b): return abs((a-b+180)%360-180)
    best=None
    for nm,_s,_d,_r,l in pos:
        if nm in ("America","SNode"): continue
        o=sep(am,l)
        if o<=3 and (best is None or o<best[1]): best=(nm,o)
    a_asc=sep(am,asc)
    if a_asc<=3 and (best is None or a_asc<best[1]): best=("Ascendant",a_asc)
    if best: return f"America conjunct {best[0]} ({best[1]:.1f}°)"
    return None

def inject_into_view(payload):
    """Replace the generated entity-chart payload in the canonical Federal Group view."""
    if not os.path.exists(FG):
        print("  WARN: The Federal Group.html not found — skipping chart injection")
        return
    with open(FG, encoding="utf-8") as f:
        html = f.read()
    compact = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    block = "<script>\nwindow.ENTITY_CHARTS=(" + compact + ").charts;\n</script>"
    html, count = re.subn(
        r'<script>\s*window\.ENTITY_CHARTS=\(.*?\)\.charts;\s*</script>',
        lambda _m: block,
        html,
        count=1,
        flags=re.S,
    )
    if count != 1:
        raise RuntimeError("expected exactly one ENTITY_CHARTS block in The Federal Group.html")
    with open(FG, "w", encoding="utf-8") as f:
        f.write(html)
    print("  injected entity charts into The Federal Group.html")

def main():
    seed=json.load(open(SEED))["entities"]
    charts={}; done=0; skip=0; amcount=0
    for e in seed:
        name=e["name"]; f=e.get("founded") or ""
        full=re.match(r'^(\d{4})-(\d{2})-(\d{2})$', f)
        if name in OVERRIDES:
            ov=OVERRIDES[name]; lat,lon=ov["loc"]
            pos,asc,asp,am=cast(ov["jd"],lat,lon,name); src=ov["src"]; place=ov["place"]
        elif full:
            y,mo,d=map(int,full.groups()); place=city_for(name); lat,lon=CITY[place]
            pos,asc,asp,am=cast(sunrise_jd(y,mo,d,lat,lon),lat,lon,name); src="sunrise (no official time)"
        else:
            if re.match(r'^\d{4}-\d{2}$', f): precision="month"
            elif re.match(r'^\d{4}$', f): precision="year"
            else: precision="approx"
            charts[name]={"charted":False,"date":f,"precision":precision}; skip+=1; continue
        sun=next(p for p in pos if p[0]=="Sun"); moon=next(p for p in pos if p[0]=="Moon")
        rec={"charted":True,"date":f,"place":place,"timeSource":src,"cat":e.get("cat"),"status":e.get("status"),
             "sunSign":sun[1],"moonSign":moon[1],"ascSign":sgn(asc),
             "rec":{"pos":pos,"asc":asc,"asp":asp}}
        if am is not None:
            rec["americaSign"]=sgn(am); rec["americaDeg"]=dms(am); rec["americaHit"]=america_hit(am,asc,pos); amcount+=1
        charts[name]=rec; done+=1
    payload={"generated":datetime.date.today().isoformat(),"note":"Institutional natal charts (Entity Theory). Whole Sign; sunrise where no official time; founding-city place. Sun-Pluto+Nodes+Chiron; 916 America from JPL Horizons (flagships) + cached grid (2024-27). Month/year-only clocks are deliberately deferred; verify exact day before load-bearing readings.","charts":charts}
    with open(OUT,"w",encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, separators=(",",":"))
    inject_into_view(payload)
    print(f"charted {done}, deferred {skip}, America on {amcount}. -> {OUT}")
    for p in ["United States","The Federal Reserve System","The 12 Federal Reserve Banks","IMF","Bank for International Settlements","Strategic Bitcoin Reserve","US Sovereign Wealth Fund"]:
        c=charts.get(p)
        if c and c.get("charted"):
            a=(" · America "+c.get("americaDeg","")+" "+c.get("americaSign","")) if c.get("americaSign") else ""
            hit=(" ["+c["americaHit"]+"]") if c.get("americaHit") else ""
            print(f"  {p:32s} {c['ascSign']:11s} rising{a}{hit}")

if __name__=="__main__":
    main()
