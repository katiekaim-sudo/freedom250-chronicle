#!/usr/bin/env python3
"""MUNDANE DOSSIER — assemble every simultaneous truth about an ingress chart.

NOT a score. This surfaces all the layers an astrologer holds at once — placements,
aspects, midpoint pictures, planetary-node contacts, derivative-house turns, and the
lunations/moon-families the ingress feeds — accurately computed (never fabricated),
so a synthesis READING can be woven from real data. The weaving is done by hand,
in Katie's voice; this just lays the true material on the table.

Usage:  python3 mundane_dossier.py 2026 Aries
"""
import os, sys, json
import swisseph as swe
from datetime import date as Date, timedelta, datetime, timezone
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import mundane_engine as ME
from america import america_lon

# Workbook Aspects tab (not a flat 6°). Ledger named_aspect orb stays separate.
WORKBOOK_ORB = {0: 8.0, 60: 5.0, 90: 7.0, 120: 7.0, 180: 8.0}
EXALT_DEG = {"Sun": 19, "Moon": 3, "Mercury": 15, "Venus": 27,
             "Mars": 28, "Jupiter": 15, "Saturn": 21}

MIDMEAN=json.load(open(os.path.join(HERE,"midpoint_meanings.json")))
ABBR={"Sun":"SU","Moon":"MO","Mercury":"ME","Venus":"VE","Mars":"MA","Jupiter":"JU",
      "Saturn":"SA","Uranus":"UR","Neptune":"NE","Pluto":"PL","Node":"NN","ASC":"AS","MC":"MC"}
NODE_PLANETS={"Jupiter":5,"Saturn":6,"Uranus":7,"Neptune":8,"Pluto":9}
HOUSE_DOMAIN={1:"the people",2:"the economy",3:"the press",4:"the land/opposition",5:"markets/speculation",
 6:"workers & the armed forces",7:"foreign powers / open war",8:"international finance / death",
 9:"courts, law & religion",10:"the government in power",11:"the legislature & allies",12:"the hidden — intel, prisons, secret enemies"}

def dist45(a,b):
    d=abs((a-b))%45.0; return min(d,45-d)
def midpoint(a,b):
    m=((a+b)/2)%360
    if abs(((m-a+180)%360-180))>90: m=(m+180)%360
    return m

def mid_meaning(p1,p2):
    k1=f"{ABBR[p1]}/{ABBR[p2]}"; k2=f"{ABBR[p2]}/{ABBR[p1]}"
    return MIDMEAN.get(k1) or MIDMEAN.get(k2) or ""

def dossier(year, sign):
    ch=ME.cast_ingress(year,sign)
    pos=ch["pos"]; asc=ch["asc"]; mc=ch["mc"]
    pts={**{n:pos[n]["lon"] for n in pos}, "ASC":asc, "MC":mc}
    # --- aspects among planets+angles (workbook orbs) ---
    asplist=[]
    names=list(pts)
    for i,a in enumerate(names):
        for b in names[i+1:]:
            sep=abs((pts[a]-pts[b]+180)%360-180)
            for ang,nm in ME.ASPECTS.items():
                lim = WORKBOOK_ORB.get(ang)
                if lim is None:
                    continue
                if abs(sep-ang)<=lim:
                    asplist.append((round(abs(sep-ang),2),a,nm,b)); break
    asplist.sort()
    # --- midpoint pictures striking a PRIORITY point (Sun/Moon/ASC/MC) within 1° ---
    prio=["Sun","Moon","ASC","MC"]
    strikes=[]
    for C in prio:
        for i,a in enumerate(names):
            for b in names[i+1:]:
                if C in (a,b): continue
                m=midpoint(pts[a],pts[b])
                if dist45(pts[C],m)<=1.0:
                    strikes.append((round(dist45(pts[C],m),2),C,a,b,mid_meaning(a,b)))
    strikes.sort()
    # --- planetary node contacts (Jones; OSCU geocentric), ingress planet on a node deg ≤2.5° ---
    jd=ch["jd"]; nodes={}
    for nm,pid in NODE_PLANETS.items():
        r=swe.nod_aps_ut(jd,pid,swe.NODBIT_OSCU)
        nodes[nm]=(r[0][0],r[1][0])  # asc(NN), desc(SN)
    node_hits=[]
    for pnm,pl in pos.items():
        for onm,(nn,sn) in nodes.items():
            for lbl,nd in (("NN",nn),("SN",sn)):
                s=abs((pl["lon"]-nd+180)%360-180)
                if s<=2.5:
                    node_hits.append((round(s,2),pnm,onm,lbl,ME.sign_of(nd),round(nd%30,1)))
    node_hits.sort()
    # --- derivative turns from key actors: where do the afflicted/angular planets land ---
    asc_idx=int(asc//30)
    def turn(actor_house):
        rows=[]
        for pnm,pl in pos.items():
            radical=pl["house"]
            derived=((radical-actor_house)%12)+1
            rows.append((pnm,radical,derived,HOUSE_DOMAIN[derived],pl["cond"]))
        return rows
    # --- lunations: last NM on/before ingress (may sit days before) through validity end ---
    vm=ME.validity_months(ch["asc_modality"])
    idate=Date.fromisoformat(ch["date"]); end=idate+timedelta(days=int(vm*30.4))
    lookback=(idate-timedelta(days=40)).isoformat()
    raw=ME.lunations(lookback, end.isoformat())
    opening=None
    for l in raw:
        if l["kind"]=="new" and Date.fromisoformat(l["date"])<=idate:
            opening=l
    if opening:
        od=Date.fromisoformat(opening["date"])
        luns=[l for l in raw if Date.fromisoformat(l["date"])>=od]
    else:
        luns=[l for l in raw if Date.fromisoformat(l["date"])>=idate]
    BANDS=[(0,8,"The Threshold"),(8,16,"The Great Harvest"),(16,24,"The Quiet Sowing"),(24,32,"The Eclipse Storm")]
    def band(deg):
        for a,b,n in BANDS:
            if a<=deg<b: return n
        return "The Eclipse Storm"
    lun_rows=[]
    for l in luns:
        hits=ME.triggers(l,ch)
        is_open=bool(opening and l["date"]==opening["date"] and l["kind"]=="new")
        lun_rows.append((l["date"],l["kind"],l["sign"],l["deg"],band(l["deg"]),hits[:2],
                         l.get("eclipse"),is_open))
    moves=window_moves(idate, end)
    return {"chart":ch,"aspects":asplist,"strikes":strikes,"nodes":nodes,"node_hits":node_hits,
            "turns":{"the people (1st)":turn(1),"the government (10th)":turn(10)},
            "lunations":lun_rows,"validity_months":vm,"moves":moves}

# Mercury–Pluto; skip Sun (no station) and Moon (too fast to list).
_MOVE_BODIES=(("Mercury",2),("Venus",3),("Mars",4),("Jupiter",5),
              ("Saturn",6),("Uranus",7),("Neptune",8),("Pluto",9))

def window_moves(start, end):
    """Stations and sign-changes inside the ingress validity (noon samples; day-level)."""
    events=[]; prev={}
    d=start
    while d<=end:
        jd=swe.julday(d.year,d.month,d.day,12.0)
        for nm,pid in _MOVE_BODIES:
            xx=swe.calc_ut(jd,pid)[0]
            lon,spd=xx[0],xx[3]
            if nm in prev:
                plon,pspd=prev[nm]
                if pspd*spd<=0 and (abs(pspd)+abs(spd))>1e-8:
                    events.append((d.isoformat(),nm,
                                   "stations retrograde" if spd<0 else "stations direct",
                                   ME.sign_of(lon),ME.deg_in_sign(lon)))
                if ME.sign_of(lon)!=ME.sign_of(plon):
                    events.append((d.isoformat(),nm,
                                   f"{ME.sign_of(plon)} → {ME.sign_of(lon)}",
                                   ME.sign_of(lon),ME.deg_in_sign(lon)))
            prev[nm]=(lon,spd)
        d+=timedelta(days=1)
    return events

def show(year,sign):
    d=dossier(year,sign); ch=d["chart"]; sn=ch["sun_neptune"]
    print("="*74); print(f"  {year} {sign} INGRESS — cast for Washington D.C., Whole Sign"); print("="*74)
    print(f"  {ch['date']}  ·  {ch['asc_sign']} rising ({ch['asc_modality']}, governs {d['validity_months']} months)  ·  MC {ch['mc_sign']}")
    loop = "  (LOOP — circle of service, not a vacancy)" if ch['dispositor_loop'] else ""
    print(f"  Chart ruler: {ch['chart_ruler']}   Dispositor: {' → '.join(ch['dispositor_chain'])}{loop}")
    print(f"  Sun–Neptune: {sn['aspect']} (orb {sn['orb']}°)  — the recurring signature")
    y, mo, dd, h = swe.revjul(ch["jd"])
    hour = int(h); minute = int((h - hour) * 60)
    am_dt = datetime(y, mo, dd, hour, minute, tzinfo=timezone.utc)
    am = america_lon(am_dt)
    if am is None:
        print("  916 America: unavailable")
    else:
        am_h = ((int(((am % 360) + 1e-6) // 30) - int(ch["asc"] // 30)) % 12) + 1
        print(f"  916 America: {ME.deg_in_sign(am):5.1f}° {ME.sign_of(am):11s} {am_h:>2d}H")
    print("\n  PLACEMENTS")
    for nm,pl in ch["pos"].items():
        extra = ""
        if "exalted" in pl["cond"] and nm in EXALT_DEG:
            extra = f"  exalt-deg {EXALT_DEG[nm]}° (orb {abs(pl['deg']-EXALT_DEG[nm]):.2f}°)"
        print(f"    {nm:8s} {pl['deg']:5.1f}° {pl['sign']:11s} {pl['house']:>2d}H  {'/'.join(pl['cond']) or 'peregrine'}{'  RETRO' if pl['retro'] else ''}{extra}")
    print("\n  TIGHTEST ASPECTS")
    for orb,a,nm,b in d["aspects"][:10]:
        print(f"    {a} {nm} {b}  ({orb}°)")
    print("\n  MIDPOINT PICTURES on the lights & angles (≤1°)")
    for orb,C,a,b,mean in d["strikes"][:10]:
        print(f"    {C} = {a}/{b}  ({orb}°)  — {mean}")
    if not d["strikes"]: print("    (none within 1°)")
    print("\n  PLANETARY-NODE CONTACTS (Jones, ≤2.5°)")
    for orb,p,o,lbl,sg,dg in d["node_hits"][:10]:
        flag = "  ⚔ war-rule: escalation" if (o in ("Saturn","Pluto") ) else ("  ☮ war-rule: resolution" if o=="Neptune" else "")
        print(f"    {p} on {o} {lbl} ({sg} {dg}°)  ({orb}°){flag}")
    if not d["node_hits"]: print("    (none within 2.5°)")
    print("\n  DERIVATIVE TURN — from THE GOVERNMENT (10th on the 1st): where the players land")
    for pnm,rad,der,dom,cond in d["turns"]["the government (10th)"]:
        if pnm in ("Sun","Moon","Mars","Saturn","Pluto") or ("detriment" in cond or "fall" in cond or "exalted" in cond):
            print(f"    {pnm:8s} (radical {rad}H) → government's {der}H = {dom}")
    print("\n  LUNATIONS (opening NM may sit before the ingress · eclipses named)")
    for date,kind,sg,dg,bd,hits,ecl,is_open in d["lunations"]:
        t = f"TRIGGERS: {hits[0]['lun_point']} {hits[0]['aspect']} {hits[0]['ingress_planet']} {hits[0]['ingress_house']}H ({hits[0]['orb']}°)" if hits else "Greer-quiet (check US natal before calling empty)"
        flags=[]
        if is_open: flags.append("OPENING")
        if ecl:
            parts=ecl.split(" ",1)
            extra=parts[1] if len(parts)==2 else ecl
            if ecl.startswith("solar"):
                flags.append(f"SOLAR ECLIPSE ({extra})")
            elif ecl.startswith("lunar"):
                flags.append(f"LUNAR ECLIPSE ({extra})")
            else:
                flags.append(ecl.upper())
        flag=("  "+", ".join(flags)) if flags else ""
        print(f"    {date}  {kind:4s} {sg:11s}{dg:4.1f}°  [{bd:17s}]{flag}  {t}")
    print("\n  IN-WINDOW STATIONS & SIGN CHANGES")
    if d["moves"]:
        for date,nm,what,sg,dg in d["moves"]:
            print(f"    {date}  {nm:8s}  {what}  ({dg:.1f}° {sg})")
    else:
        print("    (none)")

if __name__=="__main__":
    yr=int(sys.argv[1]) if len(sys.argv)>1 else 2026
    sg=sys.argv[2] if len(sys.argv)>2 else "Aries"
    show(yr,sg)
