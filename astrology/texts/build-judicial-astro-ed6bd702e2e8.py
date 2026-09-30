#!/usr/bin/env python3
"""build_judicial_astro.py — charts for The Judicial Watch (judicial_astro.json).

THE JUDICIAL ANCHOR RULE (DR-047, Katie's ruling 2026-08-09):
  - verified clock time (HH:MM) preserves the exact courthouse instant
  - 'daytime' (released/heard during the day, no verified clock) -> NOON D.C.
  - 'date-only' (e-filings, signed orders, effective dates)      -> MIDNIGHT D.C.
  - every national wheel is cast once with Washington, D.C. angles
  - courthouse place remains factual metadata, never a second wheel
  - user-facing clocks are Washington local time (EST/EDT)

DST-aware per-place (zoneinfo). Whole Sign. Points: Sun..Pluto + True Node/SNode
+ Chiron (vendored ephe) + 916 America (cached Horizons grid 2024-27; the many
pre-2024 judicial events get no America — that is the grid bound, not an error).

Keyed by "date|title". Run after build_judicial_seed.py; then build_judicial_timeline.py.
"""
import os, json, importlib.util
from zoneinfo import ZoneInfo
import swisseph as swe
from chart_conventions import DC, DC_LABEL, clock_label, mundane_event_instant

HERE  = os.path.dirname(os.path.abspath(__file__))
SEED  = os.path.join(HERE, "judicial_seed.json")
OUT   = os.path.join(HERE, "judicial_astro.json")

def load(n):
    s = importlib.util.spec_from_file_location(n, os.path.join(HERE, n + ".py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
wl = load("wheel_lib"); mp = load("minor_points")   # mp import sets the ephe path

SIGNS = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio",
         "Sagittarius","Capricorn","Aquarius","Pisces"]
PLANETS = [("Sun",swe.SUN),("Moon",swe.MOON),("Mercury",swe.MERCURY),("Venus",swe.VENUS),
           ("Mars",swe.MARS),("Jupiter",swe.JUPITER),("Saturn",swe.SATURN),
           ("Uranus",swe.URANUS),("Neptune",swe.NEPTUNE),("Pluto",swe.PLUTO)]
FLAGS = swe.FLG_MOSEPH | swe.FLG_SPEED
UTC = ZoneInfo("UTC")

# lat, lon, tz — courthouse-city anchors from the Judicial Money Map §8
PLACES = {
    "Washington, DC":    (DC[0],    DC[1],    "America/New_York"),
    "New York, NY":      (40.7143,  -74.0060, "America/New_York"),
    "Trenton, NJ":       (40.2171,  -74.7429, "America/New_York"),
    "Philadelphia, PA":  (39.9526,  -75.1652, "America/New_York"),
    "Lexington, KY":     (38.0406,  -84.5037, "America/New_York"),
    "Chicago, IL":       (41.8781,  -87.6298, "America/Chicago"),
    "New Orleans, LA":   (29.9511,  -90.0715, "America/Chicago"),
    "Birmingham, AL":    (33.5207,  -86.8025, "America/Chicago"),
    "Fort Worth, TX":    (32.7555,  -97.3308, "America/Chicago"),
    "Dallas, TX":        (32.7767,  -96.7970, "America/Chicago"),
    "Austin, TX":        (30.2672,  -97.7431, "America/Chicago"),
    "Sherman, TX":       (33.6357,  -96.6089, "America/Chicago"),
    "Denver, CO":        (39.7392, -104.9903, "America/Denver"),
    "Casper, WY":        (42.8666, -106.3131, "America/Denver"),
    "San Francisco, CA": (37.7749, -122.4194, "America/Los_Angeles"),
    # v2 map additions (2026-07-11): transaction/resolution events
    "Albany, NY":         (42.6526,  -73.7562, "America/New_York"),
    "Phoenix, AZ":        (33.4484, -112.0740, "America/Phoenix"),
    "Salt Lake City, UT": (40.7608, -111.8910, "America/Denver"),
    "San Jose, CA":       (37.3382, -121.8863, "America/Los_Angeles"),
}
DC = PLACES["Washington, DC"]

AMERICA_PRE_GRID = {}   # flagship pre-2024 longitudes (JPL Horizons 00:00 UT) when Katie wants them

def sgn(l): return SIGNS[int(l//30)%12]
def dms(l):
    d=int(l%30); m=int(round((l%30-d)*60))
    if m==60: d+=1; m=0
    return f"{d}°{m:02d}'"

def jd_for(date_iso, timeclass, tzname):
    parts = [int(x) for x in date_iso.split("-")]
    if len(parts) < 3:
        return None   # month precision = no honest chart
    stated = None if timeclass in ("daytime", "date-only") else timeclass
    return mundane_event_instant(
        date_iso, stated_time=stated, source_tz=tzname,
        date_only=timeclass == "date-only",
    )

def cast(jd, key, latlon):
    lons={}; pos=[]
    for nm, c in PLANETS:
        r = swe.calc_ut(jd, c, FLAGS)[0]; l = r[0]%360; lons[nm]=l
        pos.append([nm, sgn(l), dms(l), 1 if r[3]<0 else 0, round(l,2)])
    node = swe.calc_ut(jd, swe.TRUE_NODE, FLAGS)[0][0]%360
    pos.append(["Node", sgn(node), dms(node), 0, round(node,2)])
    sn=(node+180)%360; pos.append(["SNode", sgn(sn), dms(sn), 0, round(sn,2)])
    chi = swe.calc_ut(jd, swe.CHIRON)[0][0]%360
    pos.append(["Chiron", sgn(chi), dms(chi), 0, round(chi,2)])
    am = None
    if key in AMERICA_PRE_GRID:
        am = AMERICA_PRE_GRID[key]%360
    else:
        try: am = mp.america_lon(jd)%360
        except ValueError: am = None
    if am is not None:
        pos.append(["America", sgn(am), dms(am), 0, round(am,2)])
    asc = swe.houses(jd, latlon[0], latlon[1], b'W')[1][0]%360
    asp = wl.aspects_between(lons)
    asp += wl.point_aspects({"Node":node}, lons)
    asp += wl.point_aspects({"Chiron":chi}, lons)
    if am is not None: asp += wl.point_aspects({"America":am}, lons)
    asp.sort(key=lambda a:a["o"])
    return pos, round(asc,2), asp, am

def main():
    items = json.load(open(SEED, encoding="utf-8"))["items"]
    charts = {}; noam = 0
    for it in items:
        key = it["date"] + "|" + it["title"]
        scheduled = it["status"].startswith("Scheduled")
        place = it["place"] or "Washington, DC"
        if scheduled:
            place, timeclass = "Washington, DC", "date-only"
        else:
            timeclass = it["timeclass"]
        lat, lon, tzname = PLACES[place]
        resolved = jd_for(it["date"], timeclass, tzname)
        if resolved is None:
            continue
        jd, dc_local, basis = resolved
        pos, asc, asp, am = cast(jd, key, DC)
        if am is None: noam += 1
        if timeclass == "daytime":
            conv_time = f"noon {dc_local.tzname() or 'ET'}"
        elif timeclass == "date-only":
            conv_time = f"midnight {dc_local.tzname() or 'ET'}"
        else:
            conv_time = clock_label(dc_local)
        event_place = it["place"] or "unlocated"
        rec = {
            "pos": pos, "asc": asc, "asp": asp,
            "place": DC_LABEL,
            "eventPlace": event_place,
            "basis": basis,
            "convention": f"{conv_time} · {DC_LABEL}",
            "moonSign": next(p[1] for p in pos if p[0]=="Moon"),
        }
        charts[key] = rec
    json.dump({"_comment": "Charts for The Judicial Watch. DR-047: exact event instant > noon D.C. (daytime) > midnight D.C. (date-only); every national wheel uses Washington, D.C. angles and Eastern display time. Event place is metadata. Whole Sign. 916 America absent pre-2024 (grid bound).",
               "generated": "2026-08-09", "charts": charts},
              open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=None)
    print(f"cast {len(charts)} Washington, D.C. charts ({noam} without America pre-grid) -> {OUT}")

if __name__ == "__main__":
    main()
