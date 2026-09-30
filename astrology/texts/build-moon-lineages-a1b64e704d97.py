#!/usr/bin/env python3
"""Compute true Pessin Moon Family lineages and inject them into Moon Families.

A lineage = a New Moon (seed) plus its First Quarter (~9 lunar months later),
Full Moon (~18) and Last Quarter (~27) at the SAME sign and degree (±6°).
The full 2¼-year story of one seed — Pessin's Lunar Gestation Cycle proper,
complementing the degree-band families already in the tab.

Each member carries the chronicle's ±3-day window: note count, top plotlines,
top subplots. Chains are auto-titled by the seed window's dominant subplot.

Injects JSON between the LINEAGES-DATA markers in
`04 - Synthesis/Cross-cuts/Moon Families.html`. Needs pyswisseph.
Re-run after big ingests to refresh the event overlays (safe to repeat).
"""
import re, json, glob, os
import swisseph as swe
from datetime import date as Date, timedelta
from collections import Counter

HERE  = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(HERE)
MF    = os.path.join(VAULT, "04 - Synthesis", "Cross-cuts", "Moon Families.html")
EVENTS= os.path.join(VAULT, "01 - Events")

START = Date(2023, 1, 1)
HORIZON_END = Date(2029, 1, 31)
# A seed inside the chart horizon needs its complete 819-day Pessin tail even
# though those later quarter/full phases are context, not added chart-shelf rows.
CALC_END = Date(2031, 4, 30)
SIGNS = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
BANDS = [(0,8,"The Threshold"),(8,16,"The Great Harvest"),(16,24,"The Quiet Sowing"),(24,30,"The Eclipse Storm")]
# Pessin spacing in days, verified empirically against the ephemeris:
# NM -> FQ at same degree = 273d (9 synodic months + ¼ phase), FM = 546d, LQ = 819d
SPACING = {"fq": 273.0, "fm": 546.0, "lq": 819.0}

def lon(jd, p): return swe.calc_ut(jd, p)[0][0]

def lunations():
    names = {0:"nm", 90:"fq", 180:"fm", 270:"lq"}
    days = [(START + timedelta(days=i)) for i in range((CALC_END - START).days + 1)]
    out = []
    prev = None
    for d in days:
        j = swe.julday(d.year, d.month, d.day, 0.0)
        ph = (lon(j,1) - lon(j,0)) % 360
        if prev is not None:
            for ang, code in names.items():
                a = (prev[1] - ang + 180) % 360 - 180
                b = (ph - ang + 180) % 360 - 180
                if a * b <= 0 and abs(a - b) < 90:
                    lo, hi = prev[0], j
                    f = lambda x, ang=ang: ((lon(x,1)-lon(x,0)) % 360 - ang + 180) % 360 - 180
                    flo = f(lo)
                    for _ in range(40):
                        mid = (lo + hi) / 2
                        if flo * f(mid) <= 0: hi = mid
                        else: lo, flo = mid, f(mid)
                    x = (lo + hi) / 2
                    y, mo, dd, _ = swe.revjul(x)
                    ml = lon(x, 1)
                    node = lon(x, swe.TRUE_NODE)
                    sun = lon(x, 0)
                    ndist = min(abs((sun - node + 180) % 360 - 180), abs((sun - node) % 360 - 180) % 180)
                    ecl = (code in ("nm","fm")) and is_real_eclipse(x, code)
                    out.append({"date": f"{y:04d}-{mo:02d}-{dd:02d}", "ph": code, "jd": x,
                                "sign": SIGNS[int(ml//30)], "deg": round(ml % 30, 1),
                                "fdeg": ml, "ec": bool(ecl)})
        prev = (j, ph)
    return out

_ECL_CACHE={"nm":set(),"fm":set()}
def _scan_real_eclipses(jd0, jd1):
    """Exact eclipse dates via swisseph (replaces the old <17-deg node heuristic,
    which produced false eclipses; verified 2026-06-10)."""
    for kind,fn in (("nm",swe.sol_eclipse_when_glob),("fm",swe.lun_eclipse_when)):
        jd=jd0
        while jd<jd1:
            rf,tret=fn(jd,swe.FLG_SWIEPH,0)
            mx=tret[0]
            if mx>=jd1: break
            _ECL_CACHE[kind].add(round(mx))
            jd=mx+5
def is_real_eclipse(jd, code):
    if not _ECL_CACHE["nm"] and not _ECL_CACHE["fm"]:
        _scan_real_eclipses(jd-3000, jd+3000)
    return any(abs(round(jd)-e)<=1 for e in _ECL_CACHE[code])

def day_events():
    idx = {}
    for f in glob.glob(os.path.join(EVENTS, "2*.md")):
        d = os.path.basename(f)[:10]
        t = open(f, encoding="utf-8").read()
        pm = re.search(r'primary_plotline:\s*"?([^"\n]+)"?', t)
        sm = re.search(r'^subplot:\s*"([^"\n]+)"', t, re.M)
        idx.setdefault(d, []).append((pm.group(1).strip() if pm else "?", sm.group(1).strip() if sm else None))
    return idx

def window_stats(idx, dstr, span=3):
    d0 = Date.fromisoformat(dstr)
    plots, subs = Counter(), Counter()
    n = 0
    for i in range(-span, span+1):
        for p, s in idx.get((d0 + timedelta(days=i)).isoformat(), []):
            n += 1; plots[p] += 1
            if s: subs[s] += 1
    return n, plots.most_common(3), subs.most_common(3)

def band(deg):
    for a, b, name in BANDS:
        if a <= deg < b: return name
    return "The Eclipse Storm"

def degree_distance(a, b):
    """Shortest zodiacal distance; preserves families that straddle 0° Aries."""
    return abs((a - b + 180) % 360 - 180)

def main():
    luns = lunations()
    idx = day_events()
    nms = [l for l in luns if l["ph"] == "nm" and "2023-06-01" <= l["date"] <= HORIZON_END.isoformat()]
    chains = []
    for nm in nms:
        members = [nm]
        ok = True
        for code in ("fq", "fm", "lq"):
            target = nm["jd"] + SPACING[code]
            cands = [l for l in luns if l["ph"] == code and abs(l["jd"] - target) <= 18
                     and degree_distance(l["fdeg"], nm["fdeg"]) <= 6]
            if not cands: ok = False; break
            members.append(min(cands, key=lambda l: abs(l["deg"] - nm["deg"])))
        if not ok: continue
        # keep chains touching the chronicle's interesting window
        if not any("2024-09-01" <= m["date"] <= HORIZON_END.isoformat() for m in members): continue
        mem_out = []
        for m in members:
            n, plots, subs = window_stats(idx, m["date"])
            mem_out.append({"ph": m["ph"], "date": m["date"], "sign": m["sign"], "deg": m["deg"],
                            "ec": m["ec"], "n": n, "plots": [list(x) for x in plots],
                            "subs": [list(x) for x in subs]})
        planted = mem_out[0]["subs"][0][0] if mem_out[0]["subs"] else (
                  mem_out[0]["plots"][0][0] if mem_out[0]["plots"] else "")
        chains.append({"seed_date": nm["date"], "sign": nm["sign"], "deg": nm["deg"],
                       "band": band(nm["deg"]), "eclipse": any(m["ec"] for m in mem_out),
                       "planted": planted, "members": mem_out})
    blob = json.dumps({"coverage":{"seed_through":HORIZON_END.isoformat(),
                                    "complete_tail_through":CALC_END.isoformat()},
                       "chains": chains}, ensure_ascii=False, separators=(",", ":"))
    html = open(MF, encoding="utf-8").read()
    new = re.sub(r"(/\* LINEAGES-DATA-START \*/).*?(/\* LINEAGES-DATA-END \*/)",
                 lambda m: m.group(1) + "const LINEAGES=" + blob + ";" + m.group(2),
                 html, flags=re.S)
    if new == html:
        print("⚠ LINEAGES markers not found"); return
    open(MF, "w", encoding="utf-8").write(new)
    hot = sum(1 for c in chains for m in c["members"] if "2026-06-01" <= m["date"] <= "2026-12-31")
    print(f"✓ {len(chains)} lineage chains injected ({hot} phases land Jun–Dec 2026)")

if __name__ == "__main__":
    main()
