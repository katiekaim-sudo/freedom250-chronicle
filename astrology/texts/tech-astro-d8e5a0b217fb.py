#!/usr/bin/env python3
"""tech_astro.py — the astrology layer for The Tech Machine.

The exact method The Hearings and The Money Machine use, applied to the tech
filings. For each filing in the corpus (build_tech_machine.finalize):
  - cast a chart for the PUBLICATION MOMENT: 12:00 ET in Washington D.C. on the
    publication date, Whole Sign houses, positions via pyswisseph (Moshier flag —
    no ephe files). Same cast as mm_astro.py so the tabs can never diverge.
  - build a `rec` in wheel_lib's format so the shared wheelSVG() renders it.
  - write a Greer-style mundane read in Katie's woven voice (no source labels),
    with the house emphasis weighted to the filing's TECH track (defense = the
    war/treaty axis; energy = the land and the deep; space = the far horizon;
    biotech = the body and the lab; compute = the wires and hidden power; etc.).
  - map the filing to its Moon Family (preceding New Moon's degree-band).

Output: 99 - Templates/tech_machine_astro.json  (keyed by filing url).
  python3 tech_astro.py                  # compute charts -> json
  python3 tech_astro.py --backfill-notes # inject '## Astrological signature' into TM notes
Pure swe compute, no network. Re-run any time.
"""
import os, sys, json, datetime, importlib.util
import swisseph as swe
from chart_conventions import DC_LAT, DC_LON, DC_TZ

HERE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(HERE, "tech_machine_astro.json")

# wheel_lib for aspects + the canonical wheelSVG
spec = importlib.util.spec_from_file_location("wheel_lib", os.path.join(HERE, "wheel_lib.py"))
wl = importlib.util.module_from_spec(spec); spec.loader.exec_module(wl)
# the tech builder for the corpus (load_seed + finalize + us_date)
bspec = importlib.util.spec_from_file_location("techm", os.path.join(HERE, "build_tech_machine.py"))
techm = importlib.util.module_from_spec(bspec); bspec.loader.exec_module(techm)

SIGNS = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio",
         "Sagittarius","Capricorn","Aquarius","Pisces"]
RULERS = {"Aries":"Mars","Taurus":"Venus","Gemini":"Mercury","Cancer":"Moon",
          "Leo":"Sun","Virgo":"Mercury","Libra":"Venus","Scorpio":"Mars",
          "Sagittarius":"Jupiter","Capricorn":"Saturn","Aquarius":"Saturn","Pisces":"Jupiter"}
PLANETS = [("Sun",swe.SUN),("Moon",swe.MOON),("Mercury",swe.MERCURY),("Venus",swe.VENUS),
           ("Mars",swe.MARS),("Jupiter",swe.JUPITER),("Saturn",swe.SATURN),
           ("Uranus",swe.URANUS),("Neptune",swe.NEPTUNE),("Pluto",swe.PLUTO)]
FLAGS = swe.FLG_MOSEPH | swe.FLG_SPEED
ET = DC_TZ

# Mundane house significations — generalized from the Money/Hearings vocabulary
# so they read naturally for tech (3 = the roads & wires, 9 = the far horizon &
# aviation, 12 = the labs & the hidden, 8 = other powers' money & the deep).
HOUSE = {
 1:"the people", 2:"the economy and resources", 3:"the press, the wires, the roads",
 4:"the land and the opposition", 5:"markets and what is risked",
 6:"the workers and the civil service", 7:"foreign powers and treaties",
 8:"other powers' money, debt, death-and-rebirth", 9:"the courts, the law, the far horizon",
 10:"the government in power — the Executive", 11:"the Congress and the networks",
 12:"what is hidden — the labs, the secrets, the undoing"}

# Each tech track leans on the mundane houses that carry its story.
TRACK_HOUSES = {
 "defense-rd": [7, 10, 8],   # foreign powers / the state's command / weapons & the deep
 "autonomy":   [3, 6, 10],   # the roads / daily life / the state that licenses them
 "air-space":  [9, 3, 7],    # the far horizon & aviation / local air / foreign airspace
 "ai-compute": [3, 8, 11],   # the wires / data as power / the networks
 "space":      [9, 11, 12],  # the far horizon / the future & hopes / the vast unknown
 "energy":     [4, 2, 8],    # the land & the mines / resources / the deep power
 "biotech":    [6, 8, 12],   # the body & medicine / surgery & rebirth / the labs
}

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
    y,mo,d = map(int, dateiso.split("-"))
    local = datetime.datetime(y,mo,d,12,0,tzinfo=ET)
    u = local.astimezone(datetime.timezone.utc)
    return swe.julday(u.year,u.month,u.day, u.hour + u.minute/60 + u.second/3600)

def chart(dateiso):
    jd = jd_for(dateiso)
    lons={}; pos=[]
    for nm,const in PLANETS:
        r = swe.calc_ut(jd, const, FLAGS)[0]
        l=r[0]%360; sp=r[3]
        lons[nm]=l
        pos.append([nm, sgn(l), dms(l), 1 if sp<0 else 0, round(l,2)])
    nr = swe.calc_ut(jd, swe.TRUE_NODE, FLAGS)[0]; nl=nr[0]%360
    lons["Node"]=nl; pos.append(["Node", sgn(nl), dms(nl), 0, round(nl,2)])
    asc = swe.houses(jd, DC_LAT, DC_LON, b'W')[1][0] % 360
    _plc, _plm = wl.placidus_cusps(jd, DC_LAT, DC_LON)
    asp = wl.aspects_between({k:lons[k] for k in lons if k!="Node"})
    asp += wl.point_aspects({"Node":lons["Node"]}, {k:lons[k] for k in lons if k!="Node"})
    asp.sort(key=lambda a:a["o"])
    return {"pos":pos, "asc":round(asc,2), "asp":asp, "__date":dateiso,
            "cusps":_plc, "mc":_plm}, lons, asc

def prev_new_moon(dateiso):
    y,mo,d = map(int, dateiso.split("-"))
    base = swe.julday(y,mo,d,12.0)
    best=None; j=base
    while j > base-31:
        s=swe.calc_ut(j, swe.SUN, FLAGS)[0][0]; m=swe.calc_ut(j, swe.MOON, FLAGS)[0][0]
        elong=abs((m-s+180)%360-180)
        if best is None or elong<best[0]: best=(elong, j, s)
        j-=0.25
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

# A short track register, so each card opens in its own key without a source label.
TRACK_LENS = {
 "defense-rd": "Read as a war chart — the state's reach and its weapons.",
 "autonomy":   "Read as a chart of the roads — who moves, and who is let move.",
 "air-space":  "Read as a chart of the air — the near sky and the far one.",
 "ai-compute": "Read as a chart of the wires — information as power.",
 "space":      "Read as a chart of the far horizon — the reach past the world.",
 "energy":     "Read as a chart of the ground — the land, the mines, the deep power.",
 "biotech":    "Read as a chart of the body — medicine, the lab, rebirth.",
}

def read_for(item, lons, asc):
    tr=item["track"]
    asc_sign=sgn(asc); ruler=RULERS[asc_sign]
    moon_h=whouse(lons["Moon"], asc); moon_s=sgn(lons["Moon"])
    ruler_h=whouse(lons[ruler], asc) if ruler in lons else None
    nep_h=whouse(lons["Neptune"], asc)
    combust=[nm for nm in lons if nm not in ("Sun","Node") and sep(lons[nm],lons["Sun"])<=8.5]
    def hard(a,b,orb=6):
        s=sep(lons[a],lons[b])
        for ang in (0,90,180):
            if abs(s-ang)<=orb: return {0:"conjunct",90:"square",180:"opposite"}[ang]
        return None
    sn=hard("Sun","Neptune"); ss=hard("Sun","Saturn"); su=hard("Sun","Uranus")
    parts=[]
    lens=TRACK_LENS.get(tr)
    if lens: parts.append(lens)
    parts.append(f"The Moon — the political class — rides {moon_s} in the {ordinal(moon_h)} ({HOUSE[moon_h]}).")
    if ruler_h:
        parts.append(f"The chart's ruler, {ruler} in {sgn(lons[ruler])}, falls in the {ordinal(ruler_h)} ({HOUSE[ruler_h]}).")
    # track-weighted emphasis: name the tenant of the first leaning house that's occupied
    emph=TRACK_HOUSES.get(tr,[])
    tenants={}
    for nm in lons:
        h=whouse(lons[nm],asc)
        tenants.setdefault(h,[]).append(nm)
    for h in emph:
        who=", ".join(p for p in tenants.get(h,[]) if p!="Node")
        if who:
            parts.append(f"The {ordinal(h)} ({HOUSE[h]}) carries {who}.")
            break
    if su:
        parts.append(f"Sun {su} Uranus: the break, the new machine forced into the world — apt for a chart of invention.")
    if combust:
        parts.append(f"{', '.join(combust)} {'is' if len(combust)==1 else 'are'} combust — swallowed by the Sun, the work done in the executive's glare.")
    if sn:
        parts.append("Sun conjunct/hard Neptune: the solvent on the state's own eyes — the most dangerous signature in this method." if sn else "")
    elif nep_h in (3,8,9,12):
        parts.append(f"Neptune, the solvent, sits in the {ordinal(nep_h)} ({HOUSE[nep_h]}) — dissolving what should be solid, or hiding it.")
    if ss and not sn:
        parts.append(f"Sun {ss} Saturn: the weight of the old order pressing on the act.")
    return " ".join(p for p in parts if p)

def glance(item, fam, nm):
    return f"{item['us'] if item.get('us') else item['date']} · cast for noon in Washington · seeded by the {nm['sign']} New Moon ({nm['deg']}°, {fam})."

def backfill_notes(astro):
    """Insert a '## Astrological signature' section into the Tech Machine event
    notes (idempotent), keyed by source_url."""
    import glob, re
    EVENTS = os.path.join(os.path.dirname(HERE), "01 - Events")
    n=0
    for f in glob.glob(os.path.join(EVENTS, "2*- TM *.md")):
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
    print(f"backfilled astro signature into {n} TM note(s)")

def main():
    if "--backfill-notes" in sys.argv:
        backfill_notes(json.load(open(OUT,encoding="utf-8")))
        return
    fin = techm.finalize(techm.load_seed())
    out={}
    for it in fin:
        url=(it.get("url") or "").split("?")[0]
        date=it.get("date","")
        if not url or not date or len(date)!=10: continue
        try:
            rec, lons, asc = chart(date)
            nm = prev_new_moon(date)
            fam = family_for(nm["deg"])
            out[url] = {
                "rec": rec,
                "read": read_for(dict(it, us=techm.us_date(date)), lons, asc),
                "family": fam, "family_gloss": FAM_GLOSS[fam],
                "seed": nm,
                "glance": glance(dict(it, us=techm.us_date(date)), fam, nm),
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
