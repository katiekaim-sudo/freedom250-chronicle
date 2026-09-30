#!/usr/bin/env python3
"""Cast the 2025 retrospective shelf's chart-reading bones (DR-084).

    python3 build_chart_reading_bones_2025.py

Writes 99 - Templates/chart_reading_bones_2025/ (index.json + one bone per chart) for the
2024 Capricorn ingress through the December 19, 2025 New Moon.  Kept apart from
chart_reading_bones/ so the 2026 builders keep their own chart registry.

Cast ingresses and lunations for the chart-reading shelf.

Vault-native, Swiss/JPL (DE441) via swiss_ephemeris.FLAGS. D.C. Whole Sign.
Conventions copied from the 2026 chart_reading_bones (calibrated by diff):
workbook orbs, combust 8.5, cazimi 17', US natal hard hits <=1.2 (nameable <=1.0),
parallels <=1.0, Greer-to-ingress <=3.0 hard.
"""
import sys, json, math, datetime as dt
from pathlib import Path
from zoneinfo import ZoneInfo
T = Path(__file__).resolve().parent
sys.path.insert(0, str(T))
import swisseph as swe
from swiss_ephemeris import FLAGS, EPHEMERIS_LABEL, EPHE_DIR
swe.set_ephe_path(str(EPHE_DIR))
import mundane_engine as ME
from america import america_lon

DC_LAT, DC_LON = 38.9072, -77.0369
NY = ZoneInfo("America/New_York"); UTC = dt.timezone.utc
SIGNS = ME.SIGNS; RULER = ME.RULER; EXALT = ME.EXALT; FALL = ME.FALL
# mundane_engine.DETRI keeps only one detriment sign per planet (dict-comprehension collision);
# use the full traditional table (same as build_us_charts.py / build_world_charts.py).
DETRI_ALL = {"Sun":["Aquarius"],"Moon":["Capricorn"],"Mercury":["Sagittarius","Pisces"],"Venus":["Aries","Scorpio"],"Mars":["Taurus","Libra"],"Jupiter":["Gemini","Virgo"],"Saturn":["Cancer","Leo"]}
PL = ["Sun","Moon","Mercury","Venus","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto"]
PID = dict(zip(PL, range(10)))
ORB = {0:8.0, 60:5.0, 90:7.0, 120:7.0, 180:8.0}
ANAME = {0:"conjunction",60:"sextile",90:"square",120:"trine",180:"opposition"}
EXALT_DEG = {"Sun":19,"Moon":3,"Mercury":15,"Venus":27,"Mars":28,"Jupiter":15,"Saturn":21}
HOUSE = {1:"the nation / the body",2:"the treasury",3:"the press / communications / transport",4:"the land / opposition / foundations",
 5:"speculation / children / pleasure",6:"workers / health / armed services",7:"foreign powers / open enemies / treaties",
 8:"debt / death / other people's money",9:"courts / law / religion / long trade",10:"the government / executive / standing",
 11:"the legislature / allies",12:"the hidden / prisons / secret enemies"}
GREER_PAIRS = [("Sun","Moon"),("Venus","Mars"),("Jupiter","Saturn"),("Uranus","Neptune")]

def sd(a,b): return (a-b+180)%360-180
def sign(l): return SIGNS[int(((l%360)+1e-9)//30)%12]
def dms(l):
    l%=360; d=l%30; D=int(d); m=(d-D)*60; M=int(m); s=round((m-M)*60,1)
    if s>=60: s-=60; M+=1
    if M>=60: M-=60; D+=1
    return f"{D}°{M:02d}′{s:04.1f}″ {sign(l)}"
def whole_house(l, asc): return ((int((l%360)//30)-int((asc%360)//30))%12)+1
def moment(jd):
    y,m,d,h = swe.revjul(jd); return dt.datetime(y,m,d,tzinfo=UTC)+dt.timedelta(hours=h)
def calc(jd, pid):
    x = swe.calc_ut(jd, pid, FLAGS)[0]; e = swe.calc_ut(jd, pid, FLAGS|swe.FLG_EQUATORIAL)[0]
    return x[0]%360, x[1], x[3], e[1]

def cond(p, sg, combust, cazimi):
    t=[]
    if RULER.get(sg)==p: t.append("domicile")
    if EXALT.get(p)==sg: t.append("exalted")
    if sg in DETRI_ALL.get(p,[]): t.append("detriment")
    if FALL.get(p)==sg: t.append("fall")
    if combust: t.append("combust")
    if cazimi: t.append("cazimi")
    return t or ["peregrine"]

def us_radix():
    r=json.load(open(T/"us_rec.json")); out={}
    for key in ("sag","gem"):
        pts={row[0]:row[4] for row in r[key]["pos"]}
        for ang in ("asc","mc"):
            v=r[key].get(ang)
            if v is not None: pts[ang.upper()]=v
        out[key]=pts
    return out
US = us_radix()

def aspect_of(sep_abs):
    for ang in (0,60,90,120,180):
        if abs(sep_abs-ang)<=ORB[ang]: return ang
    return None

def dispositors(pos):
    chains={}; loops=[]; finals=[]
    for p in PL:
        path=[p]; cur=p
        while True:
            nxt=RULER[pos[cur]["sign"]]
            if nxt==cur:
                chains[p]={"path":path,"loop":False}
                if cur not in finals: finals.append(cur)
                break
            if nxt in path:
                path.append(nxt); chains[p]={"path":path,"loop":True}
                i=path.index(nxt); loop=path[i:]
                key=sorted(set(loop))
                if key not in [sorted(set(l)) for l in loops]: loops.append(loop)
                break
            path.append(nxt); cur=nxt
    root=sorted(set(finals)|{m for l in loops for m in l}, key=PL.index)
    return chains, finals, loops, root

def cast(jd, meta, sun_override=None):
    cusps, ascmc = swe.houses(jd, DC_LAT, DC_LON, b"W")
    asc, mc = ascmc[0]%360, ascmc[1]%360
    raw = {p:calc(jd,PID[p]) for p in PL}
    if sun_override is not None:
        l,la,sp,de = raw['Sun']; raw['Sun']=(sun_override,la,sp,de)
    fut = {p:calc(jd+1/24,PID[p])[0] for p in PL}
    sun = raw["Sun"][0]
    night = (sun-asc)%360 < 180
    pos={}
    for p in PL:
        l,la,sp,de = raw[p]; sg=sign(l)
        el = abs(sd(l,sun))
        combust = p!="Sun" and el<=8.5; cazimi = p!="Sun" and el<=17/60
        ex = EXALT.get(p)==sg
        pos[p]={"lon":l,"lon_dms":dms(l),"lat":la,"spd":sp,"dec":de,"sign":sg,"deg_in_sign":l%30,
                "house":whole_house(l,asc),"house_meaning":HOUSE[whole_house(l,asc)],"retro":sp<0,
                "cond":cond(p,sg,combust,cazimi),"combust":combust,"cazimi":cazimi,
                "exalt_degree":EXALT_DEG[p] if ex else None,"exalt_orb":round(abs(l%30-EXALT_DEG[p]),3) if ex else None}
    node = swe.calc_ut(jd, swe.TRUE_NODE, FLAGS)[0][0]%360
    m = moment(jd)
    try:
        am = america_lon(m)
        if am is None: raise ValueError("outside america_ephemeris.json")
        america={"lon":am,"lon_dms":dms(am),"sign":sign(am),"deg_in_sign":am%30,"house":whole_house(am,asc)}
    except Exception as e:
        america={"unavailable":str(e)}
    moon=raw["Moon"][0]
    fort = (asc+moon-sun)%360 if not night else (asc+sun-moon)%360
    spir = (asc+sun-moon)%360 if not night else (asc+moon-sun)%360
    asps=[]
    for i,a in enumerate(PL):
        for b in PL[i+1:]:
            s=abs(sd(pos[b]["lon"],pos[a]["lon"])); ang=aspect_of(s)
            if ang is None: continue
            orb=abs(s-ang); s2=abs(sd(fut[b],fut[a])); orb2=abs(s2-ang)
            fa,fs = (a,b) if abs(pos[a]["spd"])>abs(pos[b]["spd"]) else (b,a)
            waxing = sd(pos[fa]["lon"],pos[fs]["lon"])>0
            asps.append({"a":a,"b":b,"kind":ANAME[ang],"ang":ang,"orb":round(orb,3),"applying":orb2<orb,"waxing":waxing,"sep":round(s,3)})
    asps.sort(key=lambda r:r["orb"])
    greer={}
    for a,b in GREER_PAIRS:
        hit=next((r for r in asps if {r["a"],r["b"]}=={a,b}),None)
        greer[f"{a}/{b}"]=hit if hit else {"silent":True}
    par=[]
    for i,a in enumerate(PL):
        for b in PL[i+1:]:
            da,db=pos[a]["dec"],pos[b]["dec"]
            po,co=abs(da-db),abs(da+db)
            for kind,orb in (("parallel",po),("contra-parallel",co)):
                if orb<=1.0: par.append({"a":a,"b":b,"kind":kind,"orb":round(orb,3),"dec_a":round(da,3),"dec_b":round(db,3)})
    par.sort(key=lambda r:r["orb"])
    chains,finals,loops,root = dispositors(pos)
    pts={p:pos[p]["lon"] for p in PL}; pts.update({"Node":node,"SN":(node+180)%360,"ASC":asc,"MC":mc})
    if "lon" in america: pts["America"]=america["lon"]
    hits={}
    for key,radix in US.items():
        rows=[]
        for pn,pl in pts.items():
            for un,ul in radix.items():
                s=abs(sd(pl,ul))
                for ang,nm in ((0,"conjunction"),(90,"square"),(180,"opposition")):
                    if abs(s-ang)<=1.2:
                        rows.append({"eclipse_point":pn,"aspect":nm,"us_point":un,"orb":round(abs(s-ang),3),"nameable":abs(s-ang)<=1.0,"radix":key})
        hits[key]=sorted(rows,key=lambda r:r["orb"])
    local=m.astimezone(NY)
    bone={"schema":"f250.chart-bones-lite/v1","ephemeris":EPHEMERIS_LABEL,"jd":jd,"utc":m.isoformat(),"edt":local.isoformat(),
          "asc":asc,"asc_dms":dms(asc),"asc_sign":sign(asc),"asc_modality":ME.MODALITY[SIGNS.index(sign(asc))%3],
          "mc":mc,"mc_dms":dms(mc),"mc_house":whole_house(mc,asc),"night":night,"sect":"night" if night else "day",
          "ruler":RULER[sign(asc)],"pos":pos,
          "node":{"lon":node,"lon_dms":dms(node),"house":whole_house(node,asc),"sn_lon":(node+180)%360,"sn_dms":dms(node+180),"sn_house":whole_house(node+180,asc)},
          "america":america,"fortune":{"lon":fort,"lon_dms":dms(fort),"house":whole_house(fort,asc)},
          "spirit":{"lon":spir,"lon_dms":dms(spir),"house":whole_house(spir,asc)},
          "chains":chains,"finals":finals,"loops":loops,"root_members":root,"aspects":asps,"greer":greer,"parallels":par,
          "us_hits_sag":hits["sag"],"us_hits_gem":hits["gem"]}
    bone.update(meta)
    return bone

def ingress_jd(year, sg):
    target=SIGNS.index(sg)*30
    lo=ME.ingress_jd(year,sg)-0.05; hi=lo+0.1
    f=lambda x: sd(swe.calc_ut(x,0,FLAGS)[0][0],target)
    for _ in range(80):
        mid=(lo+hi)/2
        if f(lo)*f(mid)<=0: hi=mid
        else: lo=mid
    return (lo+hi)/2

def syzygies(start, end):
    out=[]; jd=swe.julday(*start,0.0); jend=swe.julday(*end,0.0)
    el=lambda x: (swe.calc_ut(x,1,FLAGS)[0][0]-swe.calc_ut(x,0,FLAGS)[0][0])%360
    prev=el(jd); step=0.25
    while jd<jend:
        nxt=jd+step; e=el(nxt)
        for ang,kind in ((0,"new"),(180,"full")):
            a=sd(prev,ang); b=sd(e,ang)
            if a<0<=b:
                lo,hi=jd,nxt
                for _ in range(60):
                    mid=(lo+hi)/2
                    if sd(el(mid),ang)<0: lo=mid
                    else: hi=mid
                out.append(((lo+hi)/2,kind))
        jd,prev=nxt,e
    return out

def eclipse_info(jd, kind):
    if kind=="new":
        rf,t=swe.sol_eclipse_when_glob(jd-2,FLAGS,0)
        if abs(t[0]-jd)>1: return None
        typ="Total" if rf&swe.ECL_TOTAL else "Annular" if rf&swe.ECL_ANNULAR else "Hybrid" if rf&swe.ECL_HYBRID else "Partial"
        geo=swe.sol_eclipse_where(t[0],FLAGS)
        attr=geo[2] if len(geo)>2 else geo[1]
        how=swe.sol_eclipse_how(t[0],(DC_LON,DC_LAT,0),FLAGS)
        return {"type":f"solar {typ}","greatest_utc":moment(t[0]).isoformat(),"magnitude_global":round(attr[0],4),
                "saros":int(round(attr[9])),"saros_member":int(round(attr[10])),
                "dc_visible":bool(how[0]), "dc_magnitude":round(how[1][0],4) if how[0] else 0.0}
    rf,t=swe.lun_eclipse_when(jd-2,FLAGS,0)
    if abs(t[0]-jd)>1: return None
    typ="Total" if rf&swe.ECL_TOTAL else "Partial" if rf&swe.ECL_PARTIAL else "Penumbral"
    how=swe.lun_eclipse_how(t[0],(DC_LON,DC_LAT,0),FLAGS)
    attr=how[1]
    dur_total = (t[5]-t[4])*24*60 if t[4] and t[5] else 0
    dur_partial = (t[3]-t[2])*24*60 if t[2] and t[3] else 0
    alt=swe.azalt(t[0],swe.ECL2HOR,(DC_LON,DC_LAT,0),0,0,swe.calc_ut(t[0],1,FLAGS)[0][:3])[1]
    return {"type":f"lunar {typ}","greatest_utc":moment(t[0]).isoformat(),"umbral_magnitude":round(attr[0],4),"dc_moon_altitude_deg":round(alt,1),
            "saros":int(round(attr[9])),"saros_member":int(round(attr[10])),"totality_min":round(dur_total,1),"partial_min":round(dur_partial,1)}

SEASON_OF={"ingress-2024-capricorn":"2025-winter","ingress-2025-aries":"2025-aries","ingress-2025-cancer":"2025-cancer","ingress-2025-libra":"2025-libra"}
LABEL={"ingress-2024-capricorn":"2024 Capricorn","ingress-2025-aries":"2025 Aries","ingress-2025-cancer":"2025 Cancer","ingress-2025-libra":"2025 Libra"}
GENERATED="2026-09-25"  # cast date; fixed so re-runs are byte-stable

def dump(obj, path):
    Path(path).write_text(json.dumps(obj, indent=1, default=str) + "\n", encoding="utf-8")

if __name__=="__main__":
    out=T/"chart_reading_bones_2025"
    out.mkdir(parents=True,exist_ok=True)
    ingresses=[(2024,"Capricorn"),(2025,"Aries"),(2025,"Cancer"),(2025,"Libra")]
    ing={}; idx=[]
    for y,sg in ingresses:
        jd=ingress_jd(y,sg); cid=f"ingress-{y}-{sg.lower()}"
        b=cast(jd,{"kind":"ingress","type":"ingress","ingress":sg,"year":y,"sign":sg},sun_override=SIGNS.index(sg)*30.0)
        b["validity_months"]={"fixed":12,"cardinal":6,"mutable":3}[b["asc_modality"]]
        b["date"]=moment(jd).astimezone(NY).date().isoformat(); b["season"]=SEASON_OF[cid]
        ing[cid]=b; dump(b,out/f"{cid}.json")
        idx.append({"id":cid,"type":"ingress","year":y,"sign":sg,"date":b["date"],"asc":b["asc_sign"],
                    "validity_months":b["validity_months"],"season":SEASON_OF[cid],"root":b["root_members"]})
    def frames(jd):
        if jd < ing["ingress-2025-aries"]["jd"]: return "ingress-2024-capricorn","ingress-2024-capricorn"
        if jd < ing["ingress-2025-cancer"]["jd"]: return "ingress-2025-aries","ingress-2025-aries"
        if jd < ing["ingress-2025-libra"]["jd"]: return "ingress-2025-aries","ingress-2025-cancer"
        return "ingress-2025-aries","ingress-2025-libra"
    def trig(g,sun,moon):
        rows=[]
        for ln,ll in (("lunSun",sun),("lunMoon",moon)):
            for pn,pv in g["pos"].items():
                s_=abs(sd(ll,pv["lon"]))
                for ang,nm in ((0,"conjunction"),(90,"square"),(180,"opposition")):
                    if abs(s_-ang)<=3.0: rows.append({"lun_point":ln,"aspect":nm,"ingress_planet":pn,"ingress_house":pv["house"],"orb":round(abs(s_-ang),3),"ingress_dms":pv["lon_dms"]})
            for an,av in (("ASC",g["asc"]),("MC",g["mc"])):
                s_=abs(sd(ll,av))
                for ang,nm in ((0,"conjunction"),(90,"square"),(180,"opposition")):
                    if abs(s_-ang)<=3.0: rows.append({"lun_point":ln,"aspect":nm,"ingress_planet":an,"ingress_house":None,"orb":round(abs(s_-ang),3),"ingress_dms":dms(av)})
        return sorted(rows,key=lambda r:r["orb"])
    for jd,kind in syzygies((2024,12,21),(2025,12,21)):
        m=moment(jd); loc=m.astimezone(NY)
        sun=swe.calc_ut(jd,0,FLAGS)[0][0]; moon=swe.calc_ut(jd,1,FLAGS)[0][0]
        lp = sun if kind=="new" else moon
        ecl=eclipse_info(jd,kind); gov,frame=frames(jd)
        suffix={"new":"ne","full":"fu"}[kind]+(("-solar" if kind=="new" else "-lunar") if ecl else "")
        cid=f"lun-{loc.date().isoformat()}-{suffix}"
        meta={"kind":"lunation","type":"lunation","lunation_kind":kind,"sign":sign(lp),"deg":round(lp%30,2),
              "date":loc.date().isoformat(),
              "eclipse":(ecl["type"].split()[0]+" "+ecl["type"].split()[1]) if ecl else None,"eclipse_detail":ecl,
              "governing":LABEL[frame],"governing_ingress_id":frame,"year_governor":LABEL[gov],"year_governor_id":gov,
              "season":SEASON_OF[frame]}
        b=cast(jd,meta)
        b["greer_to_ingress"]=trig(ing[gov],sun,moon)
        b["greer_quiet"]=not any(r["ingress_planet"] in PL for r in b["greer_to_ingress"])
        b["greer_to_frame"]=trig(ing[frame],sun,moon) if frame!=gov else []
        dump(b,out/f"{cid}.json")
        idx.append({"id":cid,"type":"lunation","date":b["date"],"kind":kind,"sign":b["sign"],"deg":b["deg"],
                    "eclipse":b["eclipse"],"governing":b["governing"],"year_governor":b["year_governor"],
                    "season":b["season"],"greer_quiet":b["greer_quiet"],"root":b["root_members"]})
    dump({"generated":GENERATED,"schema":"f250.chart-bones-lite/v1","decision_rule":"DR-084","ephemeris":EPHEMERIS_LABEL,
          "note":"2025 retrospective shelf. For lunations, `governing` names the seasonal frame used to place the chart (the nested Cancer/Libra ingress); `year_governor` names the fixed-rising 2025 Aries chart that governs the year.",
          "charts":idx}, out/"index.json")
    print(f"CHART BONES 2025: {len(idx)} charts -> {out}")
