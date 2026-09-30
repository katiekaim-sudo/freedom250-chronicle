#!/usr/bin/env python3
"""mm_astro_v2.py — the DEEPER astrology layer for The Money Machine.

Builds on mm_astro.py (v1: per-filing chart + Greer read + Moon family + seed).
v2 adds, per filing, the same three deep layers The Hearings tab carries:

  1. INGRESS LAYER — the governing cardinal ingress (the "year-king") for the
     filing's date (GOVERNANCE windows, matching build_almanac.py), the cross-chart
     synastry between the filing chart and that ingress, and the Greer
     "lunation-times-ingress" check: does the filing's Sun light up the year-king's
     own Sun / Neptune / Node? (When it does, the year's chart fires at the filing.)

  2. PESSIN LINEAGE — the filing's seed New Moon traced FORWARD +546d to its
     Full-Moon harvest (the Eclipse-Storm seeds reap in 2027) and BACK -546d to the
     parent New Moon (2024) it descends from; the XRP/crypto-rails lineage flag when
     the chain passes the Oct-2-2024 (10° Lib) or Dec-30-2024 (9° Cap) seeds the
     Hearings work already identified as the Ripple ecosystem's planting.

  3. GREER OVERLAYS — danger aspects (Sun-Neptune / Sun-Saturn the worst, then
     Mars-Saturn, Moon-Saturn) and combustion, read straight off the filing chart.

  + THE BRIDGE — which of the 9 HFSC hearings shares this filing's seed New Moon.
    A hearing and a filing born of the same lunation are one gestation: the
    legislative face and the administrative face of a single seed.

Reads the 71-filing corpus + per-filing rec/seed straight out of the built tab
(The Money Machine.html) so it needs no network and no ingest dir. Reads the 8
ingress charts (CHARTS) and the 9 hearing seeds (HLIN) out of The Hearings.html so
the two tabs can never diverge. Swiss Ephemeris (Moshier) only for the +/-546d
lineation.

Output: 99 - Templates/money_machine_astro_v2.json  (keyed by filing url).
"""
import os, re, json, datetime
import swisseph as swe

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(HERE)
XC = os.path.join(VAULT, "04 - Synthesis", "Cross-cuts")
MM_HTML = os.path.join(XC, "The Money Machine.html")
HR_HTML = os.path.join(XC, "The Hearings.html")
OUT = os.path.join(HERE, "money_machine_astro_v2.json")

SIGNS = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio",
         "Sagittarius","Capricorn","Aquarius","Pisces"]
SH = ["Ari","Tau","Gem","Can","Leo","Vir","Lib","Sco","Sag","Cap","Aqu","Pis"]
FLAGS = swe.FLG_MOSEPH | swe.FLG_SPEED

# Governing cardinal ingress per date — mirrors build_almanac.py GOVERNANCE.
GOVERNANCE = [
 ("2025-01-01","2025-03-19", None),
 ("2025-03-20","2026-03-19", "2025 Aries"),
 ("2026-03-20","2026-06-20", "2026 Aries"),
 ("2026-06-21","2026-09-22", "2026 Cancer"),
 ("2026-09-23","2026-12-31", "2026 Libra"),
]
def gov_for(d):
    for a,b,g in GOVERNANCE:
        if a <= d <= b: return g
    return None

def sgn(l): return SIGNS[int(l//30)%12]
def shrt(l): return SH[int(l//30)%12]
def dms(l):
    d=int(l%30); m=int(round((l%30-d)*60))
    if m==60: d+=1; m=0
    return f"{d}°{m:02d}'"
def sep(a,b): return abs((a-b+180)%360-180)

# ---- pull data straight from the built views (single source of truth) ----
def load_block(html, var):
    m = re.search(r'(?:const|var)\s+'+re.escape(var)+r'\s*=\s*(\[.*?\]|\{.*?\});', html, re.S)
    return json.loads(m.group(1)) if m else None

def load_all():
    mm_html = open(MM_HTML, encoding="utf-8").read()
    hr_html = open(HR_HTML, encoding="utf-8").read()
    mm = json.loads(re.search(r'<script[^>]*id="mm-data"[^>]*>(.*?)</script>', mm_html, re.S).group(1))
    CHARTS = load_block(hr_html, "CHARTS")
    HLIN = load_block(hr_html, "HLIN")
    HCH = load_block(hr_html, "HCHARTS")
    hdates = [c["__date"] for c in HCH]
    return mm, CHARTS, HLIN, hdates

# ---- synastry: filing chart vs governing ingress -------------------------
ASPECTS = [(0,"conjunct",3.0),(180,"opposite",3.0),(90,"square",3.0),
           (120,"trine",2.5),(60,"sextile",2.5)]
KEYISH = ["Sun","Moon","Mercury","Venus","Mars","Jupiter","Saturn","Neptune","Pluto","Node"]
def filing_lons(rec):
    return {p[0]: p[4] for p in rec["pos"]}

def synastry(flons, ing):
    """Top cross-aspects between filing planets (inner) and ingress planets (outer)."""
    out=[]
    ingpl = {k:v for k,v in ing.items() if k in KEYISH+["Chiron","America","ASC"]}
    for fp, fl in flons.items():
        for ip, il in ingpl.items():
            s = sep(fl, il)
            for ang,name,orb in ASPECTS:
                if abs(s-ang) <= orb:
                    out.append({"f":fp,"i":ip,"a":name,"o":round(abs(s-ang),2)})
                    break
    out.sort(key=lambda x:x["o"])
    return out

def king_fires(flons, ing):
    """Greer's lunation-times-ingress: does the filing's Sun (or Moon) sit on the
    year-king's Sun, Neptune or Node? Return the tightest hit <=2.5deg."""
    hits=[]
    for fp in ("Sun","Moon"):
        if fp not in flons: continue
        for ip in ("Sun","Neptune","Node"):
            if ip not in ing: continue
            s = sep(flons[fp], ing[ip])
            d = min(s, abs(s-180))   # conj or opp both "fire"
            asp = "conjunct" if s<=2.5 else ("opposite" if abs(s-180)<=2.5 else None)
            if asp:
                hits.append({"f":fp,"i":ip,"a":asp,"o":round(min(s,abs(s-180)),2)})
    hits.sort(key=lambda x:x["o"])
    return hits[:2]

# ---- Pessin lineage: +/-546d at the same degree --------------------------
def jd(dateiso, h=12.0):
    y,mo,d = map(int, dateiso.split("-"))
    return swe.julday(y,mo,d,h)
def _lunation_near(j0, want_full):
    """Nearest New (want_full=False) or Full (True) Moon to jd j0. Coarse scan over
    +/-18 days (> half a synodic month, so a real lunation is always inside the
    window) then refine to the minute."""
    def err(j):
        s=swe.calc_ut(j,swe.SUN,FLAGS)[0][0]; m=swe.calc_ut(j,swe.MOON,FLAGS)[0][0]
        e=abs((m-s+180)%360-180)            # 0 at New, 180 at Full
        return abs(e-180) if want_full else e
    best=None
    for k in range(-72,73):                 # +/-18 days at 0.25d steps
        j=j0+k*0.25; e=err(j)
        if best is None or e<best[0]: best=(e,j)
    _,jb=best
    for k in range(-25,26):                 # refine +/-0.5d at 0.02d steps
        j=jb+k*0.02; e=err(j)
        if e<best[0]: best=(e,j)
    j=best[1]
    body = swe.MOON if want_full else swe.SUN
    lon=swe.calc_ut(j,body,FLAGS)[0][0]%360
    y,mo,d,_=swe.revjul(j)
    return f"{y:04d}-{mo:02d}-{d:02d}", lon
def new_moon_near(j0):  return _lunation_near(j0, False)
def full_moon_near(j0): return _lunation_near(j0, True)

# The crypto-rails origin New Moons the Hearings work pinned to the Ripple
# ecosystem (HLIN parents): the Oct-2-2024 Libra solar eclipse (10 Lib) and the
# Dec-30-2024 Capricorn New Moon (9 Cap). A filing whose Great-Harvest bloom
# descends (same degree, -546d) from one of these is in the same lineage the
# keystone (#7) and structure (#9) hearings ride.
XRP_ORIGINS = [("2024-10-02",189.5,"the Oct-2-2024 Libra solar eclipse that planted the Ripple/XRP rails"),
               ("2024-12-30",279.5,"the Dec-30-2024 Capricorn New Moon that planted the Ripple/XRP rails")]
def lineage(seed):
    """Match the Hearings' Pessin method exactly:
       seed  (Eclipse-Storm New Moon, 24-32deg)  --+546d-->  HARVEST Full Moon (2027)
       seed  --~14.75d-->  BLOOM Full Moon (Great Harvest, the current revelation)
       BLOOM  --(-546d, same degree)-->  ORIGIN New Moon (2024 — the XRP-bearing link)."""
    sdate = seed["date"]
    js = jd(sdate)
    hd, hl = full_moon_near(js + 546)            # 2027 reap (same degree as seed)
    bd, bl = full_moon_near(js + 14.75)          # contemporaneous Great-Harvest bloom
    od, ol = new_moon_near(jd(bd) - 546)         # the bloom's 2024 origin (same degree)
    xrp=None
    for xd,xl,lab in XRP_ORIGINS:
        if sep(ol, xl) <= 8 and abs((datetime.date.fromisoformat(od)-datetime.date.fromisoformat(xd)).days) <= 20:
            xrp=lab; break
    return {
        "harvest": {"date":hd, "deg":f"{shrt(hl)} {hl%30:.0f}°"},   # 2027 reap
        "bloom":   {"date":bd, "deg":f"{shrt(bl)} {bl%30:.0f}°"},   # now: the revelation
        "origin":  {"date":od, "deg":f"{shrt(ol)} {ol%30:.0f}°"},   # 2024 planting of the bloom
        "xrp": xrp,
    }

# ---- Greer danger aspects off the filing chart ---------------------------
DANGER = {
 ("Sun","Neptune"): "Sun-Neptune — the single most dangerous signature: downfall, dissolution, the solvent on the state's own eyes",
 ("Sun","Saturn"): "Sun-Saturn — loss of power, the weight of the old order on the act",
 ("Mars","Saturn"): "Mars-Saturn — discontent, crimes against authority, the cut that draws blood",
 ("Moon","Saturn"): "Moon-Saturn — misfortune to the political class",
 ("Sun","Mars"): "Sun-Mars — conflict, belligerence at the top",
}
def greer(rec):
    lons = filing_lons(rec)
    out=[]
    for (a,b),txt in DANGER.items():
        if a in lons and b in lons:
            s=sep(lons[a],lons[b])
            for ang in (0,90,180):
                if abs(s-ang)<=6:
                    out.append({"pair":f"{a}-{b}","aspect":{0:"conjunct",90:"square",180:"opposite"}[ang],"o":round(abs(s-ang),2),"txt":txt})
                    break
    # combustion
    comb=[p for p in lons if p not in ("Sun","Node") and sep(lons[p],lons["Sun"])<=8.5]
    out.sort(key=lambda x:x["o"])
    return {"danger":out, "combust":comb}

# ---- the bridge: which hearing shares this filing's seed New Moon ---------
def hearing_for(seed, HLIN, hdates):
    sd = datetime.date.fromisoformat(seed["date"])
    for i,a in enumerate(HLIN):
        hs = a["seed"]                 # "2026-02-17 29° Aqu"
        m = re.match(r"(\d{4}-\d{2}-\d{2})", hs)
        if not m: continue
        hsd = datetime.date.fromisoformat(m.group(1))
        if abs((sd-hsd).days) <= 3:    # same lunation
            return {"idx":i+1, "date":hdates[i], "seed":hs}
    return None

# ---- keystone classifier (the structural filings) ------------------------
KEYWORDS = ["14247","genius","fednow","reg j","regulation j","master account",
            "payment system risk","reputation risk","tokeniz","fedwire","national settlement",
            "discount-window","discount window","reg d","regulation d","reg a","regulation a",
            "perpetual","stablecoin issuer","do not pay","disbursement","huione","clarity"]
def is_keystone(it):
    t=(it.get("title","")+" "+it.get("summary","")).lower()
    # SEC SRO listing notices are the flood, not structure
    if "self-regulatory organizations" in t and "stablecoin" not in t:
        return False
    return any(k in t for k in KEYWORDS)

# ---- woven-voice narrative (Greer mundane; NO source labels) -------------
INGRESS_VALIDITY = {  # rising modality of each governing ingress -> how long it rules
 "2025 Aries":"a fixed-sign year-king, valid the whole year",
 "2026 Aries":"a mutable-sign king, ruling the spring quarter",
 "2026 Cancer":"a mutable-sign king, ruling the summer quarter",
 "2026 Libra":"a cardinal-sign king, ruling the half-year",
}
ING_HOUSE_GLOSS = {  # the year-king's defining wound, in Katie's vocabulary
 "2025 Aries":"its own Sun exalted but fused to Neptune on the Aries Point — the executive dissolved into the throne",
 "2026 Aries":"its ruler Mercury wrecked — detriment, fall and retrograde — in the house of the state",
 "2026 Cancer":"Mercury and the Moon in mutual reception, the message and the masses trading places",
 "2026 Libra":"five planets on the angles and the Sun in fall — the hardest king of them all",
}
def _syn_phrase(s):
    """One cross-aspect, filing(inner) to year-king(outer), in mundane voice."""
    fp, ip, asp, o = s["f"], s["i"], s["a"], s["o"]
    king = "the year-king's "+("Ascendant" if ip=="ASC" else ip)
    verb = {"conjunct":"falls on","opposite":"opposes","square":"squares","trine":"trines","sextile":"sextiles"}[asp]
    colour = {
     ("Neptune","Sun"):" — the solvent on the throne",
     ("Neptune","Saturn"):" — the era's own Saturn–Neptune wound re-opened",
     ("Saturn","Sun"):" — the weight of the old order on the king",
     ("Node","Node"):" — the nodal axis returned to the king's own",
     ("Sun","Node"):" — the act timed to the king's fated axis",
     ("Pluto","Pluto"):" — raw power answering the king's power",
    }.get((fp,ip),"")
    return f"its {fp} {verb} {king} ({o}°){colour}"
def narrate(it, v):
    gov=v["gov"]; lin=v["lineage"]; gr=v["greer"]; hr=v["hearing"]; ks=v["keystone"]
    seed=it["astro"]["seed"]
    B=[]
    # --- ingress band ---
    if gov:
        ib=[f'<b>Signed under the {gov} ingress</b> — {INGRESS_VALIDITY.get(gov,"the governing chart of its season")}, '
            f'the year-king carrying {ING_HOUSE_GLOSS.get(gov,"its own signature")}.']
        if v["king_fires"]:
            k=v["king_fires"][0]
            ib.append(f'The king\'s chart fires at it: the filing\'s {k["f"]} {k["a"]} the ingress {k["i"]} to {k["o"]}°.')
        if ks and v["syn"]:
            picks=[p for p in v["syn"] if p["i"] in ("Sun","Saturn","Neptune","Node","ASC","Pluto")][:2] or v["syn"][:1]
            if picks:
                ib.append("Cross-chart, "+"; ".join(_syn_phrase(p) for p in picks)+".")
        B.append(('<div class="v2band v2ing"><div class="v2h">Under the year-king</div>'+ " ".join(ib) +'</div>'))
    # --- lineage band ---
    lb=[f'Its seed lies at <b>{seed["deg"]}° {seed["sign"]}</b> in <b>The Eclipse Storm</b> — the late, eclipse-charged band whose harvest comes in 2027. '
        f'This planting reaps at the <b>{lin["harvest"]["date"]}</b> Full Moon ({lin["harvest"]["deg"]}): the markup calendar.']
    if ks:
        lb.append(f'Right now it blooms under the {lin["bloom"]["date"]} {lin["bloom"]["deg"]} Full Moon, which descends from the {lin["origin"]["date"]} {lin["origin"]["deg"]} New Moon.')
    if lin["xrp"]:
        lb.append(f'And that origin is <b>{lin["xrp"]}</b> — the old dollar\'s death and the new rails\' birth are one lineage.')
    B.append('<div class="v2band v2lin"><div class="v2h">The lineage — planted for a 2027 harvest</div>'+ " ".join(lb) +'</div>')
    # --- greer band (keystone gets the narrative; others a flag line) ---
    if ks and (gr["danger"] or gr["combust"]):
        gb=[]
        if gr["danger"]:
            gb.append("The chart carries "+"; ".join(d["txt"] for d in gr["danger"][:2])+".")
        if gr["combust"]:
            who=", ".join(gr["combust"])
            gb.append(f'{who} {"burns" if len(gr["combust"])==1 else "burn"} combust in the Sun — the work done out of the public eye, swallowed by the executive.')
        B.append('<div class="v2band v2greer"><div class="v2h">The Greer signature</div>'+ " ".join(gb) +'</div>')
    # --- bridge band ---
    if hr:
        B.append(f'<div class="v2band v2bridge"><div class="v2h">⇄ The same New Moon as a hearing</div>'
                 f'Born of the very New Moon that seeded <b>Hearing #{hr["idx"]}</b> ({hr["date"]}) — the law written upstairs and the machine built downstairs, one gestation. '
                 f'<button class="xl v2hbtn" data-hearing="{hr["idx"]}">open Hearing #{hr["idx"]} &rarr;</button></div>')
    return "".join(B)

def main():
    mm, CHARTS, HLIN, hdates = load_all()
    out={}
    ksn=0
    for it in mm:
        url=(it.get("url") or "").split("?")[0]
        a=it.get("astro") or {}
        rec=a.get("rec"); seed=a.get("seed")
        if not url or not rec or not seed: continue
        flons=filing_lons(rec)
        gov=gov_for(it["date"])
        ing = CHARTS.get(gov) if gov else None
        syn = synastry(flons, ing) if ing else []
        kf  = king_fires(flons, ing) if ing else []
        lin = lineage(seed)
        gr  = greer(rec)
        hr  = hearing_for(seed, HLIN, hdates)
        ks  = is_keystone(it)
        if ks: ksn+=1
        v={
            "gov":gov, "syn":syn[:6], "king_fires":kf,
            "lineage":lin, "greer":gr, "hearing":hr, "keystone":ks,
        }
        v["html"]=narrate(it, v)
        out[url]=v
    json.dump(out, open(OUT,"w",encoding="utf-8"), ensure_ascii=False, separators=(",",":"))
    # report
    print(f"computed v2 for {len(out)} filings -> {OUT}")
    print(f"keystones: {ksn}")
    paired=sum(1 for v in out.values() if v["hearing"])
    print(f"share a seed lunation with a hearing: {paired}")
    xrp=sum(1 for v in out.values() if v["lineage"]["xrp"])
    print(f"descend from the XRP/Ripple parent seeds: {xrp}")
    fires=sum(1 for v in out.values() if v["king_fires"])
    print(f"the year-king's chart fires at them (Sun on king Sun/Nep/Node): {fires}")

if __name__=="__main__":
    main()
