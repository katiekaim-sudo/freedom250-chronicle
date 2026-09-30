#!/usr/bin/env python3
"""THE MUNDANE ENGINE — ingress / lunation / eclipse, cast for D.C., Whole Sign.

Reads the chronicle the way mundane astrology actually works (the nested
hierarchy), NOT via daily charts. Spec: 00 - Index/Mundane Engine — Method Spec.md.
Config (editable, Katie owns it): mundane_significators.json.

Public API:
  cast_ingress(year, sign)          -> full ingress chart dict (positions, dignity,
                                       combust, houses, chart_ruler, dispositor loop,
                                       sun_neptune, named_aspects)
  arc_scores(chart)                 -> {arc: score}, with a reasoning trace
  governing_ingress(date)           -> the ingress chart governing that date (Greer rule)
  lunations(start, end)             -> New/Full Moons cast for D.C.
  triggers(lunation, ingress)       -> [(ingress_point, aspect, orb)] hard hits, or []
  signature(date)                   -> the full read for a date: governing ingress +
                                       its arc emphasis + active lunation trigger +
                                       predicted dominant arc + reasoning
Needs pyswisseph. CSP/JS-free (pure compute module; views consume its JSON).
"""
import os, re, glob, json
import swisseph as swe
from datetime import date as Date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(HERE)
EPHE = os.path.join(HERE, "ephe")
if os.path.isdir(EPHE): swe.set_ephe_path(EPHE)
CFG = json.load(open(os.path.join(HERE, "mundane_significators.json")))
DC = CFG["dc"]; W = CFG["weights"]; ORB = CFG["orbs"]
INTERP = os.path.join(VAULT, "03 - Astrology", "Interpretations")

SIGNS = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
MODALITY = {0:"cardinal",1:"fixed",2:"mutable"}  # by sign_idx % 3
PLANETS = {"Sun":0,"Moon":1,"Mercury":2,"Venus":3,"Mars":4,"Jupiter":5,"Saturn":6,"Uranus":7,"Neptune":8,"Pluto":9}
# traditional rulerships (for dispositor chains — guarantees the classical loops)
RULER = {"Aries":"Mars","Taurus":"Venus","Gemini":"Mercury","Cancer":"Moon","Leo":"Sun",
         "Virgo":"Mercury","Libra":"Venus","Scorpio":"Mars","Sagittarius":"Jupiter",
         "Capricorn":"Saturn","Aquarius":"Saturn","Pisces":"Jupiter"}
EXALT = {"Sun":"Aries","Moon":"Taurus","Mercury":"Virgo","Venus":"Pisces","Mars":"Capricorn","Jupiter":"Cancer","Saturn":"Libra"}
# Each planet has one detriment sign per domicile (Mercury, Venus, Mars, Jupiter and Saturn have two).
# 2026-09-25: the earlier dict comprehension kept only the LAST sign per planet, silently dropping
# Jupiter/Gemini, Mercury/Sagittarius, Mars/Libra, Venus/Scorpio and Saturn/Cancer.
DETRI = {p: [] for p in ("Sun","Moon","Mercury","Venus","Mars","Jupiter","Saturn")}
for _p, _s in [("Mars","Aries"),("Venus","Taurus"),("Mercury","Gemini"),("Moon","Cancer"),("Sun","Leo"),
               ("Mercury","Virgo"),("Venus","Libra"),("Mars","Scorpio"),("Jupiter","Sagittarius"),
               ("Saturn","Capricorn"),("Saturn","Aquarius"),("Jupiter","Pisces")]:
    DETRI[_p].append(SIGNS[(SIGNS.index(_s)+6)%12])
FALL = {p:SIGNS[(SIGNS.index(s)+6)%12] for p,s in EXALT.items()}
ASPECTS = {0:"conjunction",60:"sextile",90:"square",120:"trine",180:"opposition"}
HARD = {"conjunction","square","opposition"}

def lon(jd,p): return swe.calc_ut(jd,p)[0][0]
def sign_of(l): return SIGNS[int(((l%360)+1e-6)//30)%12]   # epsilon-robust at sign boundaries
def deg_in_sign(l): return round(((l%360)+1e-6)%30, 2)

# ---------- ingress moment ----------
def ingress_jd(year, sign):
    """jd (UT) when the Sun enters 0° of a cardinal sign."""
    target = SIGNS.index(sign)*30  # 0/90/180/270
    guess = {"Aries":(3,20),"Cancer":(6,21),"Libra":(9,22),"Capricorn":(12,21)}[sign]
    lo = swe.julday(year, guess[0], guess[1]-4, 0.0)
    hi = swe.julday(year, guess[0], guess[1]+4, 0.0)
    def f(jd):
        d = (lon(jd,0) - target + 180) % 360 - 180
        return d
    for _ in range(60):
        mid=(lo+hi)/2
        if f(lo)*f(mid)<=0: hi=mid
        else: lo=mid
    return (lo+hi)/2

# ---------- chart ----------
def condition(planet, sgn, combust):
    tags=[]
    if RULER.get(sgn)==planet: tags.append("domicile")
    if EXALT.get(planet)==sgn: tags.append("exalted")
    if sgn in DETRI.get(planet, ()): tags.append("detriment")
    if FALL.get(planet)==sgn: tags.append("fall")
    if combust: tags.append("combust")
    return tags

def cast_ingress(year, sign):
    jd = ingress_jd(year, sign)
    cusps, ascmc = swe.houses(jd, DC["lat"], DC["lon"], b'W')
    asc = ascmc[0]; asc_sign = sign_of(asc); asc_idx = int(asc//30)
    mc = ascmc[1]
    sun_lon = float(SIGNS.index(sign)*30)  # the Sun is at 0° of the ingress sign BY DEFINITION
    pos={}
    for nm,pid in PLANETS.items():
        l = sun_lon if nm=="Sun" else lon(jd,pid)
        sgn=sign_of(l)
        house = ((int(((l%360)+1e-6)//30)-asc_idx)%12)+1
        combust = (nm!="Sun" and abs((l-sun_lon+180)%360-180) <= ORB["combust"])
        spd = swe.calc_ut(jd,pid)[0][3]
        pos[nm]={"lon":l,"sign":sgn,"deg":deg_in_sign(l),"house":house,
                 "retro":spd<0,"combust":combust,"cond":condition(nm,sgn,combust)}
    # chart ruler + dispositor chain (traditional)
    chart_ruler = RULER[asc_sign]
    chain=[]; seen=set(); cur=chart_ruler; loop=False
    while cur and cur not in seen:
        seen.add(cur); chain.append(cur); nxt=RULER[pos[cur]["sign"]]
        if nxt in seen: chain.append(nxt); loop=True; break
        cur=nxt
    # Sun-Neptune tracker
    sn_orb = abs((pos["Sun"]["lon"]-pos["Neptune"]["lon"]+180)%360-180)
    sn_asp=None
    for ang,nm in ASPECTS.items():
        if abs(sn_orb-ang)<=ORB["named_aspect"]: sn_asp=(nm,round(min(abs(sn_orb-ang),abs(sn_orb-(360-ang))),2)); break
    # named aspects present
    named=[]
    for kind in ("dangerous","fortunate"):
        for a,b in CFG["named_aspects"][kind]:
            sep=abs((pos[a]["lon"]-pos[b]["lon"]+180)%360-180)
            for ang,nm in ASPECTS.items():
                if abs(sep-ang)<=ORB["named_aspect"]:
                    hostile = nm in HARD
                    named.append({"pair":[a,b],"aspect":nm,"orb":round(abs(sep-ang),2),
                                  "kind":kind,"active":(hostile if kind=="dangerous" else nm in ("conjunction","trine","sextile"))})
                    break
    y,mo,dd,h = swe.revjul(jd)
    return {"year":year,"sign":sign,"jd":jd,"date":f"{y:04d}-{mo:02d}-{dd:02d}",
            "asc":asc,"asc_sign":asc_sign,"asc_modality":MODALITY[SIGNS.index(asc_sign)%3],
            "mc":mc,"mc_sign":sign_of(mc),"pos":pos,"chart_ruler":chart_ruler,
            "dispositor_chain":chain,"dispositor_loop":loop,
            "sun_neptune":{"aspect":sn_asp[0] if sn_asp else None,"orb":sn_asp[1] if sn_asp else None},
            "named_aspects":named}

def validity_months(asc_modality):
    return {"fixed":12,"cardinal":6,"mutable":3}[asc_modality]

# ---------- pair -> arc (parsed live from interpretation notes) ----------
_PAIR_ARC=None
def pair_arc_map():
    global _PAIR_ARC
    if _PAIR_ARC is not None: return _PAIR_ARC
    m={}; n2k=CFG["arc_name_to_key"]
    for f in glob.glob(os.path.join(INTERP,"*.md")):
        base=os.path.basename(f)[:-3]
        parts=re.split(r"[–-]", base)
        if len(parts)<2: continue
        pair=tuple(p.strip() for p in parts[:2])
        txt=open(f,encoding="utf-8",errors="ignore").read()
        seg=txt.split("Chronicle arcs")[-1] if "Chronicle arcs" in txt else ""
        arcs=set()
        for name,key in n2k.items():
            if name in seg: arcs.add(key)
        trigger = "trigger" in seg.lower() and "activates" in seg.lower()
        if arcs: m[frozenset(pair)]={"arcs":sorted(arcs),"trigger":trigger}
    _PAIR_ARC=m
    return m

def _arc_for_pair(a,b):
    return pair_arc_map().get(frozenset((a,b)))

# ---------- arc scoring for an ingress ----------
def arc_scores(chart):
    sc={k:0.0 for k in CFG["arc_names"]}
    trace=[]
    def add(arcmap, amount, why):
        for arc,wt in arcmap.items():
            sc[arc]+=amount*wt
        trace.append((round(amount,2),why))
    # era background
    for name,drv in CFG["era_drivers"].items():
        add(drv["arcs"], W["era_background"]*drv["weight"], f"era: {name}")
    # planets by house + by planet, weighted by condition/angularity/ruler
    for nm,pl in chart["pos"].items():
        mult=1.0; cond=pl["cond"]
        if pl["house"] in (1,4,7,10): mult*=W["angular_mult"]
        if nm==chart["chart_ruler"]: mult*=W["chart_ruler_mult"]
        dig = ("domicile" in cond or "exalted" in cond)
        deb = ("detriment" in cond or "fall" in cond)
        bonus = (W["dignified_bonus"] if dig else 0)+(W["debilitated_penalty"] if deb else 0)+(W["combust_penalty"] if pl["combust"] else 0)
        base = max(0.1, W["planet_base"]*mult + bonus)
        # house domain arc
        ha=CFG["house_arc"].get(str(pl["house"]),{})
        if ha: add(ha, W["house_base"]*mult, f"{nm} in {pl['house']}H {'/'.join(cond) or 'peregrine'}")
        # planet actor arc
        pa=CFG["planet_arc"].get(nm,{})
        if pa: add(pa, base, f"{nm} actor")
    # named aspects (active ones) -> their pair's arc
    for na in chart["named_aspects"]:
        if not na["active"]: continue
        pa=_arc_for_pair(*na["pair"])
        arcs = {a:1.0 for a in pa["arcs"]} if pa else {}
        if arcs:
            amt=W["named_aspect"]*(1.0 if na["kind"]=="dangerous" else 0.6)
            add(arcs, amt, f"{na['pair'][0]}–{na['pair'][1]} {na['aspect']} ({na['kind']})")
    # Sun-Neptune tracker (always weighted — the recurring signature)
    if chart["sun_neptune"]["aspect"]:
        pa=_arc_for_pair("Sun","Neptune")
        if pa: add({a:1.0 for a in pa["arcs"]}, W["named_aspect"], f"Sun–Neptune {chart['sun_neptune']['aspect']} (the tracker)")
    ranked=sorted(sc.items(), key=lambda kv:-kv[1])
    return {"scores":sc,"ranked":ranked,"top":ranked[0][0],"trace":trace}

# ---------- governing ingress for a date ----------
def governing_ingress(d):
    d=Date.fromisoformat(d) if isinstance(d,str) else d
    # candidate cardinal ingresses in the ~15 months before d
    cands=[]
    for yr in (d.year-1, d.year):
        for sgn in ("Aries","Cancer","Libra","Capricorn"):
            ch=cast_ingress(yr,sgn)
            idate=Date.fromisoformat(ch["date"])
            if idate<=d: cands.append((idate,ch))
    cands.sort()
    # walk forward: each chart governs validity_months unless superseded by the next cardinal it doesn't outlast
    gov=None
    for idate,ch in cands:
        end=idate+timedelta(days=int(validity_months(ch["asc_modality"])*30.4))
        if idate<=d<=end: gov=ch  # latest one still in force
    if gov is None and cands: gov=cands[-1][1]
    return gov

# ---------- lunations ----------
def _lunation_eclipse(jd, code):
    """Tag a New/Full Moon if Swiss Eph finds a solar/lunar eclipse within 0.8d.
    `kind` stays new/full so callers do not break. Type is Total/Annular/Hybrid/Partial/Penumbral."""
    if code == "new":
        rf, tret = swe.sol_eclipse_when_glob(jd - 0.8, swe.FLG_SWIEPH, 0)
        t = tret[0]
        if abs(t - jd) < 0.8:
            typ = ("Total" if rf & swe.ECL_TOTAL else "Annular" if rf & swe.ECL_ANNULAR
                   else "Hybrid" if rf & swe.ECL_HYBRID else "Partial")
            return f"solar {typ}"
    else:
        rf, tret = swe.lun_eclipse_when(jd - 0.8, swe.FLG_SWIEPH, 0)
        t = tret[0]
        if abs(t - jd) < 0.8:
            typ = ("Total" if rf & swe.ECL_TOTAL else "Partial" if rf & swe.ECL_PARTIAL
                   else "Penumbral")
            return f"lunar {typ}"
    return None

def lunations(start, end):
    start=Date.fromisoformat(start) if isinstance(start,str) else start
    end=Date.fromisoformat(end) if isinstance(end,str) else end
    out=[]; prev=None; d=start
    while d<=end:
        jd=swe.julday(d.year,d.month,d.day,0.0)
        ph=(lon(jd,1)-lon(jd,0))%360
        for ang,code in ((0,"new"),(180,"full")):
            if prev is not None:
                a=(prev[1]-ang+180)%360-180; b=(ph-ang+180)%360-180
                if a*b<=0 and abs(a-b)<90:
                    loo,hi=prev[0],jd; f=lambda x,ang=ang:((lon(x,1)-lon(x,0))%360-ang+180)%360-180; flo=f(loo)
                    for _ in range(40):
                        mid=(loo+hi)/2
                        if flo*f(mid)<=0: hi=mid
                        else: loo,flo=mid,f(mid)
                    x=(loo+hi)/2; y,mo,dd,_=swe.revjul(x)
                    out.append({"date":f"{y:04d}-{mo:02d}-{dd:02d}","kind":code,"jd":x,
                                "sun":lon(x,0),"moon":lon(x,1),"sign":sign_of(lon(x,1) if code=="full" else lon(x,0)),
                                "deg":round((lon(x,0) if code=="new" else lon(x,1))%30,1),
                                "eclipse":_lunation_eclipse(x, code)})
        prev=(jd,ph); d+=timedelta(days=1)
    return out

def triggers(lunation, ingress):
    """Does the lunation's Sun/Moon hit an ingress position by conj/opp/square (≤orb)?"""
    hits=[]
    lpts={"lunSun":lunation["sun"],"lunMoon":lunation["moon"]}
    for lname,ll in lpts.items():
        for pname,pl in ingress["pos"].items():
            sep=abs((ll-pl["lon"]+180)%360-180)
            for ang,nm in ASPECTS.items():
                if nm in HARD and abs(sep-ang)<=ORB["lunation_to_ingress"]:
                    hits.append({"lun_point":lname,"ingress_planet":pname,"ingress_house":pl["house"],
                                 "aspect":nm,"orb":round(abs(sep-ang),2)})
    return sorted(hits,key=lambda h:h["orb"])

# ---------- top-level signature for a date ----------
def signature(d):
    gov=governing_ingress(d)
    asc=arc_scores(gov)
    # active lunation: the most recent new/full at or before d, within 31 days
    dd=Date.fromisoformat(d) if isinstance(d,str) else d
    luns=lunations((dd-timedelta(days=32)).isoformat(), dd.isoformat())
    active=luns[-1] if luns else None
    lun_hits=triggers(active,gov) if active else []
    # boost the arc carried by the tightest hit's house/planet
    boost=dict(asc["scores"])
    fired=None
    if lun_hits:
        h=lun_hits[0]; ha=CFG["house_arc"].get(str(h["ingress_house"]),{})
        for arc,wt in ha.items(): boost[arc]+=W["lunation_trigger_boost"]*wt
        fired=h
    ranked=sorted(boost.items(),key=lambda kv:-kv[1])
    return {"date":(d if isinstance(d,str) else d.isoformat()),
            "governing_ingress":f"{gov['year']} {gov['sign']}","asc_sign":gov["asc_sign"],
            "validity_months":validity_months(gov["asc_modality"]),
            "ingress_top_arc":asc["top"],"ingress_ranked":asc["ranked"],
            "lunation":(active["date"]+" "+active["kind"]+" Moon "+active["sign"] if active else None),
            "lunation_triggers":bool(lun_hits),"fired":fired,
            "predicted_arc":ranked[0][0],"ranked":ranked,
            "reasoning":asc["trace"]}

if __name__=="__main__":
    import sys
    # quick self-test: cast the 8 ingresses and print their top arc + key features
    print("MUNDANE ENGINE — ingress self-test\n"+"="*60)
    for yr in (2025,2026):
        for sgn in ("Aries","Cancer","Libra","Capricorn"):
            ch=cast_ingress(yr,sgn); a=arc_scores(ch)
            sn=ch["sun_neptune"]
            print(f"{yr} {sgn:9s} | ASC {ch['asc_sign']:11s}({ch['asc_modality'][:4]} {validity_months(ch['asc_modality'])}mo) "
                  f"| ruler {ch['chart_ruler']:7s} {'LOOP' if ch['dispositor_loop'] else '   '} "
                  f"| Sun-Nep {str(sn['aspect'] or '-'):11s}{sn['orb'] if sn['orb'] is not None else '':<5} "
                  f"| TOP: {a['top']} ({a['ranked'][0][1]:.1f})")
    if len(sys.argv)>1:
        print("\nSIGNATURE for",sys.argv[1])
        s=signature(sys.argv[1])
        print(json.dumps({k:v for k,v in s.items() if k!="reasoning"},indent=1,default=str))
