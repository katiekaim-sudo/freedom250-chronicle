#!/usr/bin/env python3
"""MOON vs. 1st-HOUSE RULER — Greer's "has the political class lost the plot?" gauge.

Greer's most distinctive mundane indicator (Astrology of Nations; Master Reference §2b):
  • The Moon = the POLITICAL CLASS (the ~20% with a political voice), NOT "the people".
  • The 1st house and its ruler = the GENERAL POPULATION — the people.
  • Moon in helpful aspect to the 1st-ruler (or Moon in the 1st)  -> the political class
    and the people are ALIGNED.
  • Moon in hostile aspect to the 1st-ruler                       -> the political class
    has lost track of the realities of governance; turmoil follows.
  • A PROLONGED SERIES of hostile lunations = "the political class has lost the plot."

This module computes the gauge for every cardinal ingress (the season) and every
New/Full Moon (the minute hand) cast for Washington D.C., Whole Sign — reusing the
shared mundane_engine so the math is identical to the rest of the vault. It emits
moon_vs_ruler.json (consumed by the Situation Deck tier and the reading note).
NEVER fabricates a degree — every position is computed; verify against Astro Gold.

Usage:
  python3 moon_vs_ruler.py                 # print the report + write moon_vs_ruler.json
  python3 moon_vs_ruler.py 2024-01-01 2027-12-31   # custom lunation span
"""
import os, sys, json
import swisseph as swe
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import mundane_engine as ME

# --- aspect classification (Greer) ---
# helpful = the political class & the people are aligned; hostile = lost track.
HARMONY  = {"sextile", "trine"}
HOSTILE  = {"square", "opposition"}
# conjunction is read separately (fusion, judged by condition); none-in-orb = disconnected.
MOON_RULER_ORB = 6.0   # same chart-level orb the dossier uses; the Moon is fast, 6° is fair.

VERDICT_LABEL = {
    "aligned":      "ALIGNED — political class & people in step",
    "hostile":      "HOSTILE — the political class has lost track",
    "fused":        "FUSED — one body (conjunction); read by condition",
    "fused_ruler":  "ONE RULER — the Moon itself rules the people (Cancer rising)",
    "disconnected": "OUT OF CONTACT — no major aspect; talking past each other",
}

def _closest_aspect(sep):
    """sep in [0,180]; return (aspect_name, orb) for the nearest Ptolemaic aspect within orb, else (None,None)."""
    best = (None, None)
    for ang, nm in ME.ASPECTS.items():
        orb = abs(sep - ang)
        if orb <= MOON_RULER_ORB and (best[1] is None or orb < best[1]):
            best = (nm, round(orb, 2))
    return best

def _applying(jd, moon_pid, ruler_pid, aspect_angle):
    """Is the Moon-ruler aspect applying (orb shrinking) at jd? Robust to a retrograde ruler."""
    def orb_at(t):
        m = ME.lon(t, moon_pid); r = ME.lon(t, ruler_pid)
        sep = abs((m - r + 180) % 360 - 180)
        return abs(sep - aspect_angle)
    return orb_at(jd + 0.04) < orb_at(jd - 0.04)   # ~1 hour step

def classify(moon_lon, ruler_name, ruler_lon, moon_house, jd, ruler_pid, ruler_cond):
    """Return a verdict dict for a single chart's Moon-vs-1st-ruler relationship."""
    # Cancer rising: the Moon rules the 1st — the people's ruler IS the political class.
    if ruler_name == "Moon":
        return {"verdict": "fused_ruler", "aspect": None, "orb": None, "applying": None,
                "phase_coupled": True,
                "note": "The people are ruled by the Moon — the very body that is the political class. "
                        "No gap to read: the two are one. Judge the Moon's own condition."}
    sep = abs((moon_lon - ruler_lon + 180) % 360 - 180)
    aspect, orb = _closest_aspect(sep)
    applying = None
    if aspect:
        applying = _applying(jd, ME.PLANETS["Moon"], ruler_pid, [a for a, n in ME.ASPECTS.items() if n == aspect][0])
    # Moon physically in the 1st house = aligned regardless (Greer: "Moon in the 1st OR helpful aspect").
    if moon_house == 1 and aspect not in HOSTILE:
        verdict = "aligned"
    elif aspect in HARMONY:
        verdict = "aligned"
    elif aspect in HOSTILE:
        verdict = "hostile"
    elif aspect == "conjunction":
        verdict = "fused"
    else:
        verdict = "disconnected"
    # When the 1st-ruler is a luminary, the Moon-ruler aspect is partly fixed by the lunation
    # phase itself (a Leo-rising Full Moon is necessarily Sun-opposite-Moon; Cancer rising is
    # always the Moon). Flag it as weaker evidence than an independent (non-luminary) ruler.
    phase_coupled = ruler_name in ("Sun", "Moon")
    return {"verdict": verdict, "aspect": aspect, "orb": orb, "applying": applying,
            "phase_coupled": phase_coupled, "ruler_condition": ruler_cond}

def analyze_ingress(year, sign):
    ch = ME.cast_ingress(year, sign)
    ruler = ch["chart_ruler"]
    rp = ch["pos"][ruler]; mp = ch["pos"]["Moon"]
    c = classify(mp["lon"], ruler, rp["lon"], mp["house"], ch["jd"], ME.PLANETS[ruler], rp["cond"])
    return {
        "kind": "ingress", "label": f"{year} {sign} ingress", "date": ch["date"],
        "asc_sign": ch["asc_sign"], "asc_modality": ch["asc_modality"],
        "validity_months": ME.validity_months(ch["asc_modality"]),
        "ruler": ruler, "ruler_sign": rp["sign"], "ruler_deg": rp["deg"], "ruler_house": rp["house"],
        "ruler_cond": rp["cond"], "ruler_retro": rp["retro"],
        "moon_sign": mp["sign"], "moon_deg": mp["deg"], "moon_house": mp["house"], "moon_cond": mp["cond"],
        **c,
    }

def analyze_lunation(lun):
    """lun is a row from ME.lunations(): has jd, sun, moon, kind, sign, deg, date."""
    jd = lun["jd"]
    cusps, ascmc = swe.houses(jd, ME.DC["lat"], ME.DC["lon"], b'W')
    asc = ascmc[0]; asc_sign = ME.sign_of(asc); asc_idx = int(asc // 30)
    ruler = ME.RULER[asc_sign]
    rpid = ME.PLANETS[ruler]
    ruler_lon = lun["moon"] if ruler == "Moon" else ME.lon(jd, rpid)
    ruler_sign = ME.sign_of(ruler_lon)
    ruler_house = ((int(((ruler_lon % 360) + 1e-6) // 30) - asc_idx) % 12) + 1
    ruler_retro = (ruler != "Moon" and swe.calc_ut(jd, rpid)[0][3] < 0)
    ruler_cond = ME.condition(ruler, ruler_sign, False)
    moon_lon = lun["moon"]
    moon_house = ((int(((moon_lon % 360) + 1e-6) // 30) - asc_idx) % 12) + 1
    c = classify(moon_lon, ruler, ruler_lon, moon_house, jd, rpid, ruler_cond)
    return {
        "kind": "lunation", "label": f"{lun['date']} {lun['kind']} Moon", "date": lun["date"],
        "lunation_kind": lun["kind"], "asc_sign": asc_sign,
        "ruler": ruler, "ruler_sign": ruler_sign, "ruler_deg": round(ruler_lon % 30, 1),
        "ruler_house": ruler_house, "ruler_cond": ruler_cond, "ruler_retro": ruler_retro,
        "moon_sign": ME.sign_of(moon_lon), "moon_deg": round(moon_lon % 30, 1), "moon_house": moon_house,
        **c,
    }

def streaks(records):
    """Greer's 'prolonged series': longest runs of consecutive HOSTILE lunations, plus current state."""
    luns = [r for r in records if r["kind"] == "lunation"]
    luns.sort(key=lambda r: r["date"])
    runs = []; cur = []
    for r in luns:
        if r["verdict"] == "hostile":
            cur.append(r["date"])
        else:
            if len(cur) >= 2: runs.append((cur[0], cur[-1], len(cur)))
            cur = []
    if len(cur) >= 2: runs.append((cur[0], cur[-1], len(cur)))
    runs.sort(key=lambda x: -x[2])
    # tally (all) + independent tally (excluding phase-coupled luminary-ruled charts)
    tally = {}; indep = {}
    for r in luns:
        tally[r["verdict"]] = tally.get(r["verdict"], 0) + 1
        if not r.get("phase_coupled"):
            indep[r["verdict"]] = indep.get(r["verdict"], 0) + 1
    # independent hostile runs (the strong-evidence version of Greer's "series")
    iruns = []; cur = []
    for r in luns:
        if r["verdict"] == "hostile" and not r.get("phase_coupled"):
            cur.append(r["date"])
        else:
            if len(cur) >= 2: iruns.append((cur[0], cur[-1], len(cur)))
            cur = []
    if len(cur) >= 2: iruns.append((cur[0], cur[-1], len(cur)))
    return {"hostile_runs": runs, "independent_hostile_runs": iruns,
            "tally": tally, "independent_tally": indep,
            "n_lunations": len(luns), "n_independent": sum(indep.values()),
            "current": luns[-1] if luns else None}

def build(span_start="2024-01-01", span_end="2027-12-31"):
    records = []
    for yr in (2025, 2026):
        for sgn in ("Aries", "Cancer", "Libra", "Capricorn"):
            records.append(analyze_ingress(yr, sgn))
    for lun in ME.lunations(span_start, span_end):
        records.append(analyze_lunation(lun))
    return {"records": records, "summary": streaks(records),
            "orb": MOON_RULER_ORB, "span": [span_start, span_end]}

def _fmt(r):
    asp = f"{r['aspect']} {r['orb']}°" + ("→" if r.get("applying") else ("←" if r.get("applying") is False else "")) if r["aspect"] else "—"
    return (f"  {r['date']}  {r['label']:26s} | {r['asc_sign']:11s} rising → ruler {r['ruler']:7s} "
            f"{r['ruler_deg']:4.1f}° {r['ruler_sign']:11s} {r['ruler_house']:>2d}H | Moon {r['moon_deg']:4.1f}° "
            f"{r['moon_sign']:11s} {r['moon_house']:>2d}H | {asp:18s} | {r['verdict'].upper()}")

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        data = build(sys.argv[1], sys.argv[2])
    else:
        data = build()
    print("=" * 100)
    print("  MOON vs. 1st-HOUSE RULER — has the political class lost the plot? (D.C., Whole Sign)")
    print("=" * 100)
    print("\n  THE EIGHT INGRESSES (the season's standing relationship)")
    for r in data["records"]:
        if r["kind"] == "ingress": print(_fmt(r))
    print("\n  THE LUNATIONS (the minute hand) —", data["summary"]["n_lunations"], "New/Full Moons")
    for r in data["records"]:
        if r["kind"] == "lunation": print(_fmt(r))
    s = data["summary"]
    print("\n  TALLY:", s["tally"])
    print("  LONGEST HOSTILE RUNS (Greer's 'lost the plot' series):")
    for a, b, n in s["hostile_runs"][:8]:
        print(f"    {n} in a row: {a} → {b}")
    if s["current"]:
        print(f"  CURRENT (latest lunation {s['current']['date']}): {VERDICT_LABEL[s['current']['verdict']]}")
    out = os.path.join(HERE, "moon_vs_ruler.json")
    json.dump(data, open(out, "w"), indent=1, default=str)
    print("\n  wrote", out)
