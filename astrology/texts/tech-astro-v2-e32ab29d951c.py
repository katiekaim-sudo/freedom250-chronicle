#!/usr/bin/env python3
"""tech_astro_v2.py — the DEEPER astrology layer for The Tech Machine.

The same v2 layers The Hearings and The Money Machine carry, applied to the tech
filings. Builds on tech_astro.py (v1: per-filing chart + read + family + seed):

  1. PESSIN LINEAGE — the filing's seed New Moon traced FORWARD +546d to its 2027
     Full-Moon harvest, and its contemporaneous bloom traced BACK -546d to the
     2024 origin New Moon it descends from; the XRP/Ripple lineage flag when that
     origin is the Oct-2-2024 Libra solar eclipse (10° Lib) or the Dec-30-2024
     Capricorn New Moon (9° Cap) the Hearings work pinned as the Ripple planting.

  2. GREER OVERLAYS — danger aspects (Sun-Neptune / Sun-Saturn worst, then
     Mars-Saturn, Moon-Saturn, Sun-Mars) and combustion, off the filing chart.

  + THE BRIDGE — which of the 9 HFSC hearings shares this filing's seed New Moon.
    A hearing and a filing born of the same lunation are one gestation: the
    legislative face and the administrative face of a single seed.

Reads tech_machine_astro.json (per-filing rec + seed, from tech_astro.py) and the
9 hearing seeds (HLIN) out of The Hearings.html. Swiss Ephemeris (Moshier) for the
+/-546d lineation. Output: 99 - Templates/tech_machine_astro_v2.json (keyed by url).

  python3 tech_astro_v2.py
"""
import os, re, json, datetime
import swisseph as swe

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(HERE)
XC = os.path.join(VAULT, "04 - Synthesis", "Cross-cuts")
HR_HTML = os.path.join(XC, "The Hearings.html")
ASTRO = os.path.join(HERE, "tech_machine_astro.json")
OUT = os.path.join(HERE, "tech_machine_astro_v2.json")

SH = ["Ari","Tau","Gem","Can","Leo","Vir","Lib","Sco","Sag","Cap","Aqu","Pis"]
FLAGS = swe.FLG_MOSEPH | swe.FLG_SPEED
def sep(a,b): return abs((a-b+180)%360-180)
def shrt(l): return SH[int(l//30)%12]

# ---- Pessin lineage: +/-546d at the same degree ----------------------------
def jd(dateiso, h=12.0):
    y,mo,d = map(int, dateiso.split("-")); return swe.julday(y,mo,d,h)
def _lunation_near(j0, want_full):
    def err(j):
        s=swe.calc_ut(j,swe.SUN,FLAGS)[0][0]; m=swe.calc_ut(j,swe.MOON,FLAGS)[0][0]
        e=abs((m-s+180)%360-180)
        return abs(e-180) if want_full else e
    best=None
    for k in range(-72,73):
        j=j0+k*0.25; e=err(j)
        if best is None or e<best[0]: best=(e,j)
    jb=best[1]
    for k in range(-25,26):
        j=jb+k*0.02; e=err(j)
        if e<best[0]: best=(e,j)
    j=best[1]; body = swe.MOON if want_full else swe.SUN
    lon=swe.calc_ut(j,body,FLAGS)[0][0]%360
    y,mo,d,_=swe.revjul(j)
    return f"{y:04d}-{mo:02d}-{d:02d}", lon
def new_moon_near(j0):  return _lunation_near(j0, False)
def full_moon_near(j0): return _lunation_near(j0, True)

XRP_ORIGINS = [("2024-10-02",189.5,"the Oct-2-2024 Libra solar eclipse that planted the Ripple/XRP rails"),
               ("2024-12-30",279.5,"the Dec-30-2024 Capricorn New Moon that planted the Ripple/XRP rails")]
def lineage(seed):
    sdate = seed["date"]; js = jd(sdate)
    hd, hl = full_moon_near(js + 546)
    bd, bl = full_moon_near(js + 14.75)
    od, ol = new_moon_near(jd(bd) - 546)
    xrp=None
    for xd,xl,lab in XRP_ORIGINS:
        if sep(ol, xl) <= 8 and abs((datetime.date.fromisoformat(od)-datetime.date.fromisoformat(xd)).days) <= 20:
            xrp=lab; break
    return {
        "harvest": {"date":hd, "deg":f"{shrt(hl)} {hl%30:.0f}°"},
        "bloom":   {"date":bd, "deg":f"{shrt(bl)} {bl%30:.0f}°"},
        "origin":  {"date":od, "deg":f"{shrt(ol)} {ol%30:.0f}°"},
        "xrp": xrp,
    }

# ---- Greer danger aspects off the filing chart -----------------------------
DANGER = {
 ("Sun","Neptune"): "Sun–Neptune — the single most dangerous signature: dissolution, the solvent on the state's own eyes",
 ("Sun","Saturn"): "Sun–Saturn — loss of power, the weight of the old order on the act",
 ("Mars","Saturn"): "Mars–Saturn — the cut that draws blood, force against the structure",
 ("Moon","Saturn"): "Moon–Saturn — misfortune to the political class",
 ("Sun","Mars"): "Sun–Mars — belligerence at the top",
 ("Sun","Uranus"): "Sun–Uranus — the break, the new machine forced through (apt for invention, hard on order)",
}
def filing_lons(rec): return {p[0]: p[4] for p in rec["pos"]}
def greer(rec):
    lons = filing_lons(rec); out=[]
    for (a,b),txt in DANGER.items():
        if a in lons and b in lons:
            s=sep(lons[a],lons[b])
            for ang in (0,90,180):
                if abs(s-ang)<=6:
                    out.append({"pair":f"{a}–{b}","aspect":{0:"conjunct",90:"square",180:"opposite"}[ang],"o":round(abs(s-ang),2),"txt":txt})
                    break
    comb=[p for p in lons if p not in ("Sun","Node") and sep(lons[p],lons["Sun"])<=8.5]
    out.sort(key=lambda x:x["o"])
    return {"danger":out, "combust":comb}

# ---- the bridge: which hearing shares this filing's seed New Moon -----------
def load_hearings():
    if not os.path.exists(HR_HTML): return [], []
    h = open(HR_HTML, encoding="utf-8").read()
    m = re.search(r'const HLIN\s*=\s*(\[.*?\]);', h, re.S)
    HLIN = json.loads(m.group(1)) if m else []
    meta = re.search(r'const HEARINGS\s*=\s*\[(.*?)\];', h, re.S)
    dates=[]
    if meta:
        for o in re.findall(r'\{.*?\}', meta.group(1), re.S):
            mm=re.search(r'date\s*:\s*(["\'])((?:\\.|(?!\1).)*?)\1', o, re.S)
            dates.append(mm.group(2) if mm else "")
    return HLIN, dates
def hearing_for(seed, HLIN, hdates):
    sd = datetime.date.fromisoformat(seed["date"])
    for i,a in enumerate(HLIN):
        m = re.match(r"(\d{4}-\d{2}-\d{2})", a.get("seed",""))
        if not m: continue
        hsd = datetime.date.fromisoformat(m.group(1))
        if abs((sd-hsd).days) <= 3:
            return {"idx":i+1, "date":hdates[i] if i<len(hdates) else "", "seed":a["seed"]}
    return None

def main():
    A = json.load(open(ASTRO, encoding="utf-8"))
    HLIN, hdates = load_hearings()
    out={}
    nx=nbridge=0
    for url, a in A.items():
        seed = a.get("seed"); rec = a.get("rec")
        if not seed or not rec: continue
        lin = lineage(seed)
        g = greer(rec)
        hr = hearing_for(seed, HLIN, hdates)
        if lin["xrp"]: nx+=1
        if hr: nbridge+=1
        out[url] = {"lineage": lin, "danger": g["danger"], "combust": g["combust"], "hearing": hr}
    json.dump(out, open(OUT,"w",encoding="utf-8"), ensure_ascii=False, separators=(",",":"))
    print(f"computed v2 for {len(out)} filings -> {OUT}")
    print(f"  Ripple/XRP lineage: {nx}   shared-hearing bridge: {nbridge}")

if __name__ == "__main__":
    main()
