#!/usr/bin/env python3
"""mm_astro.py — compute the astrology layer for The Money Machine.

For each filing in the corpus (seed + ingest, via build_money_machine.finalize):
  - cast a chart for the Federal Register PUBLICATION MOMENT: 12:00 ET in
    Washington D.C. on the publication date (Katie's choice 2026-06-17), Whole
    Sign houses, midnight-free (the moment is noon-ET). Positions via pyswisseph
    (Moshier flag — no ephe files in the sandbox).
  - build a `rec` in wheel_lib's format ({pos:[[name,sign,dms,retro,lon]], asc, asp})
    so the existing wheelSVG() renders it.
  - write a Greer-style mundane read (Moon = political class; 2nd = banks/Fed,
    10th = Treasury/Executive, 11th = Congress, 8th = international finance;
    combustion = swallowed by the executive; Sun-Neptune/Sun-Saturn = the danger
    aspects; Neptune = the solvent) in Katie's woven voice — no source labels.
  - map the filing to its Moon Family: the preceding New Moon's degree-band
    (Threshold 0-8 / Great Harvest 8-16 / Quiet Sowing 16-24 / Eclipse Storm 24-32).

Output: 99 - Templates/money_machine_astro.json  (keyed by filing url).
v1 is the base wheel file. mm_astro_v2.py reads this and writes
money_machine_astro_v2.json (Pessin / Greer / hearing bridge). Both are live.
Do not delete either.
Run in the sandbox (needs network? no — pure swe compute). Re-run any time.
"""
import os, sys, json, importlib.util
import swisseph as swe
from chart_conventions import (
    DC_LABEL, DC_LAT, DC_LON, clock_label, mundane_event_instant,
)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(HERE, "money_machine_astro.json")

# wheel_lib for aspects
spec = importlib.util.spec_from_file_location("wheel_lib", os.path.join(HERE, "wheel_lib.py"))
wl = importlib.util.module_from_spec(spec); spec.loader.exec_module(wl)
# builder for the corpus
bspec = importlib.util.spec_from_file_location("mm", os.path.join(HERE, "build_money_machine.py"))
mm = importlib.util.module_from_spec(bspec); bspec.loader.exec_module(mm)

SIGNS = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio",
         "Sagittarius","Capricorn","Aquarius","Pisces"]
RULERS = {"Aries":"Mars","Taurus":"Venus","Gemini":"Mercury","Cancer":"Moon",
          "Leo":"Sun","Virgo":"Mercury","Libra":"Venus","Scorpio":"Mars",
          "Sagittarius":"Jupiter","Capricorn":"Saturn","Aquarius":"Saturn","Pisces":"Jupiter"}
PLANETS = [("Sun",swe.SUN),("Moon",swe.MOON),("Mercury",swe.MERCURY),("Venus",swe.VENUS),
           ("Mars",swe.MARS),("Jupiter",swe.JUPITER),("Saturn",swe.SATURN),
           ("Uranus",swe.URANUS),("Neptune",swe.NEPTUNE),("Pluto",swe.PLUTO)]
FLAGS = swe.FLG_MOSEPH | swe.FLG_SPEED

# Greer mundane house significations (Katie's vocabulary)
HOUSE = {
 1:"the people", 2:"the economy, the banks, the Fed's own money", 3:"the press and the wires",
 4:"the opposition and the land", 5:"speculation and markets", 6:"the workers and the civil service",
 7:"foreign powers and treaties", 8:"international finance, debt, death-and-rebirth of the system",
 9:"the courts and the law", 10:"the government in power — the Executive and the Treasury",
 11:"the Congress and the legislature", 12:"what is hidden — secrets, prisons, undoing"}
TRACK_HOUSES = {"gate":[2,8,11], "rails":[3,9,2], "stablecoins":[2,8,11], "check":[10,1,6]}

def ordinal(n):
    return f"{n}{'th' if 11<=n%100<=13 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"
def sgn(l): return SIGNS[int(l//30)%12]
def dms(l):
    d=int(l%30); m=int(round((l%30-d)*60))
    if m==60: d+=1; m=0
    return f"{d}°{m:02d}'"
def sep(a,b): return abs((a-b+180)%360-180)
def whouse(lon, asc): return ((int(lon//30) - int(asc//30)) % 12) + 1

def jd_for(dateiso):
    return mundane_event_instant(dateiso)[0]

# ---- One-capital mundane ruling (DR-047, Katie 2026-08-09) ----
# exact stated time  -> preserve that real instant, cast with D.C. angles
# daytime, no time   -> noon Washington local
# no time info       -> midnight Washington local, "day of"
# source place       -> factual metadata only; never a second wheel

def instant_for(it):
    """(jd, D.C. caption, basis) for a seed item under DR-047."""
    stated = it.get("etime") or None
    date_only = not stated and it.get("timing") == "none"
    jd, dc_local, basis = mundane_event_instant(
        it["date"], stated_time=stated,
        source_tz=it.get("tz") or "America/New_York",
        date_only=date_only,
    )
    if stated:
        clock = clock_label(dc_local)
    elif date_only:
        clock = f"midnight {dc_local.tzname() or 'ET'}"
    else:
        clock = f"noon {dc_local.tzname() or 'ET'}"
    conv = f"{clock} · {DC_LABEL}"
    return jd, conv, basis

def chart(item):
    """item: dict with date (+ optional etime/timing/place/lat/lon/tz),
    or a bare date string (legacy noon-D.C. behavior)."""
    if isinstance(item, str): item = {"date": item}
    jd, conv, basis = instant_for(item)
    lons={}; pos=[]
    for nm,const in PLANETS:
        r = swe.calc_ut(jd, const, FLAGS)[0]
        l=r[0]%360; sp=r[3]
        lons[nm]=l
        pos.append([nm, sgn(l), dms(l), 1 if sp<0 else 0, round(l,2)])
    # true node
    nr = swe.calc_ut(jd, swe.TRUE_NODE, FLAGS)[0]; nl=nr[0]%360
    lons["Node"]=nl; pos.append(["Node", sgn(nl), dms(nl), 0, round(nl,2)])
    asc = swe.houses(jd, DC_LAT, DC_LON, b'W')[1][0] % 360
    _plc, _plm = wl.placidus_cusps(jd, DC_LAT, DC_LON)
    asp = wl.aspects_between({k:lons[k] for k in lons if k!="Node"})
    asp += wl.point_aspects({"Node":lons["Node"]}, {k:lons[k] for k in lons if k!="Node"})
    asp.sort(key=lambda a:a["o"])
    rec = {"pos":pos, "asc":round(asc,2), "asp":asp, "__date":item["date"],
           "cusps":_plc, "mc":_plm, "conv":conv, "cap2":conv, "basis":basis,
           "event_place":item.get("place") or None}
    return rec, lons, asc

def prev_new_moon(dateiso):
    """Walk back up to 31 days to find the preceding New Moon (min elongation)."""
    y,mo,d = map(int, dateiso.split("-"))
    base = swe.julday(y,mo,d,12.0)
    best=None
    j=base
    while j > base-31:
        s=swe.calc_ut(j, swe.SUN, FLAGS)[0][0]; m=swe.calc_ut(j, swe.MOON, FLAGS)[0][0]
        elong=abs((m-s+180)%360-180)
        if best is None or elong<best[0]: best=(elong, j, s)
        j-=0.25
    # refine ±0.5d
    _,jb,_=best
    for j in [jb+k*0.02 for k in range(-25,26)]:
        s=swe.calc_ut(j, swe.SUN, FLAGS)[0][0]; m=swe.calc_ut(j, swe.MOON, FLAGS)[0][0]
        elong=abs((m-s+180)%360-180)
        if elong<best[0]: best=(elong,j,s)
    _,jnm,slon=best
    yy,mm_,dd,_=swe.revjul(jnm)
    return {"date":f"{yy:04d}-{mm_:02d}-{dd:02d}", "lon":slon%360, "sign":sgn(slon%360), "deg":round(slon%30,1)}

def family_for(deg):
    if deg < 8:  return "The Threshold"
    if deg < 16: return "The Great Harvest"
    if deg < 24: return "The Quiet Sowing"
    return "The Eclipse Storm"

FAM_GLOSS = {
 "The Threshold":"a cycle just opening — 0–8°, the seed barely in the ground",
 "The Great Harvest":"8–16° — the chronicle's bloom family, the 2024 seeds coming due",
 "The Quiet Sowing":"16–24° — a quiet planting, results held back",
 "The Eclipse Storm":"24–32° — late-degree, eclipse-charged; seeds for a 2027 harvest"}

def read_for(item, lons, asc):
    tr=item["track"]
    asc_sign=sgn(asc); ruler=RULERS[asc_sign]
    moon_h=whouse(lons["Moon"], asc); moon_s=sgn(lons["Moon"])
    ruler_h=whouse(lons[ruler], asc) if ruler in lons else None
    nep_h=whouse(lons["Neptune"], asc)
    combust=[nm for nm in lons if nm not in ("Sun","Node") and sep(lons[nm],lons["Sun"])<=8.5]
    # danger aspects (hard orbs)
    def hard(a,b,orb=6):
        s=sep(lons[a],lons[b]);
        for ang in (0,90,180):
            if abs(s-ang)<=orb: return {0:"conjunct",90:"square",180:"opposite"}[ang]
        return None
    sn=hard("Sun","Neptune"); ss=hard("Sun","Saturn")
    parts=[]
    parts.append(f"The Moon — the political class — rides {moon_s} in the {ordinal(moon_h)} ({HOUSE[moon_h]}).")
    if ruler_h:
        parts.append(f"The chart's ruler, {ruler} in {sgn(lons[ruler])}, falls in the {ordinal(ruler_h)} ({HOUSE[ruler_h]}).")
    # track-weighted emphasis
    emph=TRACK_HOUSES.get(tr,[])
    tenants={}
    for nm in lons:
        h=whouse(lons[nm],asc)
        tenants.setdefault(h,[]).append(nm)
    for h in emph:
        if tenants.get(h):
            who=", ".join(p for p in tenants[h] if p!="Node")
            if who:
                parts.append(f"The {ordinal(h)} ({HOUSE[h]}) carries {who}.")
                break
    if combust:
        parts.append(f"{', '.join(combust)} {'is' if len(combust)==1 else 'are'} combust — swallowed by the Sun, the work of the executive done in its glare.")
    if sn:
        parts.append(f"Sun {sn} Neptune: the solvent on the state's own eyes — the most dangerous signature in this method.")
    elif nep_h in (2,8,10):
        parts.append(f"Neptune, the solvent, sits in the {ordinal(nep_h)} ({HOUSE[nep_h]}) — dissolving what should be solid.")
    if ss and not sn:
        parts.append(f"Sun {ss} Saturn: the weight of the old order pressing on the act.")
    return " ".join(parts)

def glance(item, fam, nm, convention=None):
    if convention is None:
        convention = instant_for(item)[1]
    return f"{item['us'] if item.get('us') else item['date']} · {convention} · seeded by the {nm['sign']} New Moon ({nm['deg']}°, {fam})."

def backfill_notes(astro):
    """Insert a '## Astrological signature' section into the Money Machine event
    notes (idempotent), keyed by source_url."""
    # DR-089 (Katie, 2026-10-02): official records belong in the research library, not the
    # X-feed Chronicle, and factual notes carry no astrology. Retired; kept for history.
    print("backfill_notes: retired 2026-10-02 (DR-089) — official records live in 02 - Research/Official Records; nothing written")
    return
    import glob, re
    EVENTS = os.path.join(os.path.dirname(HERE), "01 - Events")
    n=0
    for f in glob.glob(os.path.join(EVENTS, "2*.md")):
        try: t=open(f,encoding="utf-8").read()
        except Exception: continue
        m=re.search(r'^source_url:\s*"?([^"\n]+)', t, re.M)
        if not m: continue
        url=m.group(1).strip().split("?")[0]
        a=astro.get(url)
        if not a: continue
        if "## Astrological signature" in t: continue
        seed=a.get("seed",{})
        sig=(f"## Astrological signature\n\n{a['read']}\n\n"
             f"**Moon family:** {a['family']} — seeded by the {seed.get('sign','')} New Moon "
             f"({seed.get('deg','')}°) on {seed.get('date','')}.\n\n")
        if "## Why this matters" in t:
            t=t.replace("## Why this matters", sig+"## Why this matters", 1)
        else:
            t=t.rstrip()+"\n\n"+sig
        open(f,"w",encoding="utf-8").write(t); n+=1
    print(f"backfilled astro signature into {n} note(s)")

def main():
    if "--backfill-notes" in sys.argv:
        backfill_notes(json.load(open(OUT,encoding="utf-8")))
        return
    items = mm.load_seed()
    import glob as _g
    ing = os.path.join(HERE.replace("Freedom 250 Chronicle/99 - Templates","Freedom 250 Chronicle/99 - Templates"), )
    # ingest dir passed as arg, else default sandbox staging
    idir = sys.argv[sys.argv.index("--ingest-dir")+1] if "--ingest-dir" in sys.argv else \
           "/sessions/amazing-lucid-brown/mnt/outputs/mm_ingest/clean"
    if os.path.isdir(idir):
        for jf in sorted(_g.glob(os.path.join(idir,"*.json"))):
            try: items += json.load(open(jf,encoding="utf-8"))
            except Exception: pass
    fin = mm.finalize(items)
    out={}
    for it in fin:
        url=(it.get("url") or "").split("?")[0]
        date=it.get("date","")
        if not url or not date or len(date)!=10: continue
        try:
            rec, lons, asc = chart(it)
            nm = prev_new_moon(date)
            fam = family_for(nm["deg"])
            out[url] = {
                "rec": rec,
                "read": read_for(dict(it, us=mm.us_date(date)), lons, asc),
                "family": fam, "family_gloss": FAM_GLOSS[fam],
                "seed": nm,
                "glance": glance(dict(it, us=mm.us_date(date)), fam, nm, rec["conv"]),
            }
        except Exception as e:
            print("  ! chart failed", date, it.get("title","")[:40], e)
    json.dump(out, open(OUT,"w",encoding="utf-8"), ensure_ascii=False, separators=(",",":"))
    fams={}
    for v in out.values(): fams[v["family"]]=fams.get(v["family"],0)+1
    print(f"computed {len(out)} charts -> {OUT}")
    print("by family:", fams)

if __name__=="__main__":
    main()
