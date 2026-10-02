#!/usr/bin/env python3
"""build_charter_astro.py — charts for The Charter Queue (charter_astro.json).

Copied from build_castration_astro.py per _AI-Context/PATTERN — Timeline Machine Build.md.

Time convention (Katie's ruling, feedback_event_chart_time_convention, refined 2026-07-11):
  1. an ACTUAL STATED TIME wins            -> that hour, D.C. local   (seed "time" field)
  2. releases/actions (occurred/position/proposed/research) -> NOON D.C.
  3. day-of facts (scheduled deadlines, effective dates)    -> MIDNIGHT D.C. ("day of")
DST-aware (zoneinfo America/New_York). Whole Sign, D.C. coordinates.

Month-precision dates get NO chart — a month is not a moment and we do not fake one.

Points: Sun..Pluto + True Node/SNode + Chiron (vendored ephe) + 916 America
(cached Horizons grid 2024–27; pre-2024 entries get no America).

Keyed by "date|title". Run after build_charter_seed.py, then build_charter_timeline.py.
"""
import os, json, importlib.util
from datetime import datetime
from zoneinfo import ZoneInfo
import swisseph as swe
from chart_conventions import DC, DC_TZ

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = os.path.join(HERE, "charter_seed.json")
OUT  = os.path.join(HERE, "charter_astro.json")

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
TZ = DC_TZ; UTC = ZoneInfo("UTC")
AMERICA_PRE_GRID = {}   # none load-bearing yet (grid starts 2024-01-01)

def sgn(l): return SIGNS[int(l//30)%12]
def dms(l):
    d=int(l%30); m=int(round((l%30-d)*60))
    if m==60: d+=1; m=0
    return f"{d}°{m:02d}'"

def status_key(s):
    for prefix, key in [("Occurred","occurred"),("Public","position"),("Proposed","proposed"),
                        ("Research","research"),("Scheduled","scheduled")]:
        if s.startswith(prefix): return key
    return "occurred"

def jd_for(date_iso, midnight, stated=None):
    parts = [int(x) for x in date_iso.split("-")]
    if len(parts) < 3:
        return None, None          # month precision — chartless by design
    y, mo, d = parts
    if stated:
        hh, mm = (int(x) for x in stated.split(":"))
        conv = f"{stated} D.C. (stated)"
    elif midnight:
        hh, mm, conv = 0, 0, "midnight D.C. (day of)"
    else:
        hh, mm, conv = 12, 0, "noon D.C."
    local = datetime(y, mo, d, hh, mm, tzinfo=TZ)
    ut = local.astimezone(UTC)
    return swe.julday(ut.year, ut.month, ut.day, ut.hour + ut.minute/60.0), conv

def cast(jd, key):
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
    asc = swe.houses(jd, *DC, b'W')[1][0]%360
    asp = wl.aspects_between(lons)
    asp += wl.point_aspects({"Node":node}, lons)
    asp += wl.point_aspects({"Chiron":chi}, lons)
    if am is not None: asp += wl.point_aspects({"America":am}, lons)
    asp.sort(key=lambda a:a["o"])
    return pos, round(asc,2), asp, am

def main():
    items = json.load(open(SEED, encoding="utf-8"))["items"]
    charts = {}; noam = 0; skipped = 0
    for it in items:
        midnight = status_key(it["status"]) == "scheduled"
        key = it["date"] + "|" + it["title"]
        jd, conv = jd_for(it["date"], midnight, it.get("time"))
        if jd is None:
            skipped += 1
            continue
        pos, asc, asp, am = cast(jd, key)
        if am is None: noam += 1
        charts[key] = {"pos": pos, "asc": asc, "asp": asp, "convention": conv,
                       "moonSign": next(p[1] for p in pos if p[0]=="Moon")}
    json.dump({"_comment": "Charts for The Charter Queue. Stated time > noon D.C. (releases) > midnight D.C. (scheduled). "
                           "Whole Sign. Month-precision dates chartless by design. 916 America absent pre-2024 (grid bound).",
               "generated": "2026-07-12", "charts": charts},
              open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=None)
    print(f"cast {len(charts)} charts ({skipped} chartless month-precision, {noam} without America) -> {OUT}")

if __name__ == "__main__":
    main()
