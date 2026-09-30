#!/usr/bin/env python3
"""Audit (and fix) the 8 ingress charts against the Swiss Ephemeris.

Found 2026-06-09: the four NUANCE chart notes (2025 Cancer/Libra/Capricorn,
2026 Capricorn) carried fabricated positions from an earlier session — e.g.
2026 Capricorn Venus written as 10° Aquarius vs the true 13°47' Scorpio.
The four governing charts were clean.

  python3 audit_ingress_charts.py          # report discrepancies only
  python3 audit_ingress_charts.py --fix    # rewrite bad note tables and repair the
                                            ing_data.json / HTML overlay frames

After --fix: re-run build_almanac.py and build_lunation_wheels.py (they read
the notes' positions), and sync to observatory-app/public/. Interpretive PROSE
in the notes is NOT touched — wrong-sign mentions are listed for Katie.
"""
import re, os, sys, glob, json
import swisseph as swe

HERE  = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(HERE)
ASTRO = os.path.join(VAULT, "03 - Astrology")
IC    = os.path.join(VAULT, "04 - Synthesis", "Cross-cuts", "Ingress Charts.html")
ING_JSON = os.path.join(HERE, "ing_data.json")

SIGNS=["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
PL={0:"Sun",1:"Moon",2:"Mercury",3:"Venus",4:"Mars",5:"Jupiter",6:"Saturn",7:"Uranus",8:"Neptune",9:"Pluto"}
GLYPH={"Sun":"☉","Moon":"☽","Mercury":"☿","Venus":"♀","Mars":"♂","Jupiter":"♃","Saturn":"♄","Uranus":"♅","Neptune":"♆","Pluto":"♇"}
ABBR={"Sun":"Su","Moon":"Mo","Mercury":"Me","Venus":"Ve","Mars":"Ma","Jupiter":"Ju","Saturn":"Sa","Uranus":"Ur","Neptune":"Ne","Pluto":"Pl"}
DOM={"Sun":["Leo"],"Moon":["Cancer"],"Mercury":["Gemini","Virgo"],"Venus":["Taurus","Libra"],
     "Mars":["Aries","Scorpio"],"Jupiter":["Sagittarius","Pisces"],"Saturn":["Capricorn","Aquarius"]}
EXALT={"Sun":"Aries","Moon":"Taurus","Mercury":"Virgo","Venus":"Pisces","Mars":"Capricorn","Jupiter":"Cancer","Saturn":"Libra"}
INGRESSES=[(2025,3,0,"2025 Aries"),(2025,6,90,"2025 Cancer"),(2025,9,180,"2025 Libra"),(2025,12,270,"2025 Capricorn"),
           (2026,3,0,"2026 Aries"),(2026,6,90,"2026 Cancer"),(2026,9,180,"2026 Libra"),(2026,12,270,"2026 Capricorn")]

def zodiac_index(lon): return int((((lon % 360) + 1e-7) % 360) // 30)

def sign_of(lon): return SIGNS[zodiac_index(lon)]

def fmt(l): return f"{int(l%30)}°{int((l%1)*60):02d}' {sign_of(l)}"

def opp(sign): return SIGNS[(SIGNS.index(sign)+6)%12]

def find_ingress(year,mg,target):
    f=lambda j: ((swe.calc_ut(j,0)[0][0]-target+180)%360)-180
    lo=hi=swe.julday(year,mg,15,0.0); hi+=20
    while f(lo)>0: lo-=5
    while f(hi)<0: hi+=5
    for _ in range(50):
        mid=(lo+hi)/2
        if f(mid)<0: lo=mid
        else: hi=mid
    return (lo+hi)/2

def conditions(name,sign,lon,sun_lon,retro):
    out=[]
    if sign in DOM.get(name,[]): out.append("DOMICILE")
    if EXALT.get(name)==sign: out.append("EXALTED")
    if sign in [opp(s) for s in DOM.get(name,[])]: out.append("DETRIMENT")
    if EXALT.get(name) and opp(EXALT[name])==sign: out.append("FALL")
    if name!="Sun":
        d=abs((lon-sun_lon+180)%360-180)
        if d<8.5: out.append(f"COMBUST ({d:.1f}°)")
    if retro: out.append("RETROGRADE")
    return out or ["Peregrine"]

def truth_for(name):
    y,mg,t=[ (a,b,c) for a,b,c,n in INGRESSES if n==name ][0]
    j=find_ingress(y,mg,t)
    asc,mc=swe.houses(j,38.9072,-77.0369,b'W')[1][0:2]
    rows={}
    sun=swe.calc_ut(j,0)[0][0]
    for p in sorted(PL):
        r=swe.calc_ut(j,p)[0]
        eq=swe.calc_ut(j,p,swe.FLG_SWIEPH|swe.FLG_EQUATORIAL)[0]
        rows[PL[p]]={"lon":r[0],"speed":r[3],"retro":r[3]<0,"decl":eq[1]}
    node=swe.calc_ut(j,swe.TRUE_NODE)[0][0]
    return {"jd":j,"asc":asc,"mc":mc,"rows":rows,"node":node,"sun":sun}

def ord_(n):
    suf="th" if 10<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10,"th")
    return f"{n}{suf}"

def house_of(lon,asc):
    return (zodiac_index(lon)-zodiac_index(asc))%12+1

def decl_str(d):
    hemi="N" if d>=0 else "S"; d=abs(d)
    return f"{int(d):02d}°{hemi}{int((d%1)*60):02d}'"

def audit(fix=False):
    notes={}
    for f in glob.glob(os.path.join(ASTRO,"20*Solar Ingress.md")):
        t=open(f,encoding="utf-8").read()
        nm=re.search(r'year:\s*(\d{4})',t).group(1)+" "+re.search(r'ingress:\s*(\w+)',t).group(1)
        notes[nm]=f
    bad_charts=[]
    prose_flags=[]
    for nm,f in sorted(notes.items()):
        t=open(f,encoding="utf-8").read()
        T=truth_for(nm)
        diffs=[]
        for m in re.finditer(r'^\| (Sun|Moon|Mercury|Venus|Mars|Jupiter|Saturn|Uranus|Neptune|Pluto) \| (\d+)°(\d+)\' (\w+)',t,re.M):
            p,d,mn,s=m.group(1),int(m.group(2)),int(m.group(3)),m.group(4)
            if s not in SIGNS: continue
            note=SIGNS.index(s)*30+d+mn/60
            dd=abs((note-T["rows"][p]["lon"]+180)%360-180)
            if dd>0.2: diffs.append((p,s,dd))
        status="⚠" if diffs else "✓"
        print(f"{status} {nm}: {len(diffs)} bad positions" + ("" if not diffs else " — "+", ".join(f"{p} (Δ{d:.1f}°)" for p,_,d in diffs)))
        if not diffs: continue
        bad_charts.append(nm)
        if not fix: continue
        # ---- rewrite the planet table in the note ----
        asc=T["asc"]
        hdr="| Planet | Position | Sign | House | Speed | Condition |\n|--------|----------|------|-------|-------|-----------|"
        lines=[hdr]
        for p in [PL[i] for i in sorted(PL)]:
            R=T["rows"][p]; l=R["lon"]; s=sign_of(l)
            cond=", ".join(conditions(p,s,l,T["sun"],R["retro"]))
            cond_md=cond if cond=="Peregrine" else f"**{cond}**"
            lines.append(f"| {p} | {fmt(l)} | {s} | {ord_(house_of(l,asc))} | {R['speed']:+.2f}°/d | {cond_md} |")
        lines.append(f"| N. Node | {fmt(T['node'])} | {sign_of(T['node'])} | {ord_(house_of(T['node'],asc))} | — | — |")
        new_table="\n".join(lines)
        t2=re.sub(r'\| Planet \|[^\n]*\n\|[-| ]+\n(\| [^\n]+\n)+', new_table+"\n", t, count=1)
        # fix the Date/Time line + frontmatter time if off
        y,mo,d_,h=swe.revjul(T["jd"])
        tstr=f"{int(h):02d}:{int(h%1*60):02d}:{int(((h%1*60)%1)*60):02d}"
        t2=re.sub(r'(time_utc:\s*")[^"]*(")', rf'\g<1>{tstr}\g<2>', t2)
        # flag prose mentioning now-wrong signs
        for p,old_sign,_ in diffs:
            new_sign=sign_of(T["rows"][p]["lon"])
            if old_sign!=new_sign and re.search(rf'{p} in {old_sign}', t2):
                prose_flags.append(f"{nm}: prose says '{p} in {old_sign}' — true sign is {new_sign}")
        if t2!=t: open(f,"w",encoding="utf-8").write(t2)
        print(f"   fixed table + time in note")

    # ---- audit the compact overlay frame registry ----
    ing_rows=json.load(open(ING_JSON,encoding="utf-8"))
    by_id={row["id"]:row for row in ing_rows}
    frame_bad=[]
    for _,_,_,nm in INGRESSES:
        cid=nm.lower().replace(" ","-")
        row=by_id.get(cid)
        if not row:
            raise RuntimeError(f"{cid} missing from ing_data.json")
        T=truth_for(nm)
        rising=sign_of(T["asc"])
        asc_delta=abs((float(row.get("asc_deg",0))-T["asc"]+180)%360-180)
        p_bad=[]
        for p in [PL[i] for i in sorted(PL)]:
            got=(row.get("p") or {}).get(p)
            true_lon=T["rows"][p]["lon"]
            if (not isinstance(got,list) or len(got)<3 or
                abs((float(got[0])-true_lon+180)%360-180)>0.2 or
                got[1]!=sign_of(true_lon) or int(got[2])!=house_of(true_lon,T["asc"])):
                p_bad.append(p)
        if asc_delta>0.2 or row.get("rising")!=rising or p_bad:
            frame_bad.append(nm)
            detail=[]
            if asc_delta>0.2 or row.get("rising")!=rising:
                detail.append(f"ASC {row.get('rising')} {row.get('asc_deg')} → {rising} {T['asc']:.2f}")
            if p_bad: detail.append("p-map "+", ".join(p_bad))
            print(f"⚠ {nm}: overlay frame drift — {'; '.join(detail)}")
            if fix:
                row["rising"]=rising
                row["asc_deg"]=round(T["asc"],2)
                row["p"]={
                    p:[round(T["rows"][p]["lon"],2),sign_of(T["rows"][p]["lon"]),house_of(T["rows"][p]["lon"],T["asc"])]
                    for p in [PL[i] for i in sorted(PL)]
                }
        else:
            print(f"✓ {nm}: overlay frame")

    if fix and frame_bad:
        with open(ING_JSON,"w",encoding="utf-8") as handle:
            json.dump(ing_rows,handle,ensure_ascii=False,separators=(",",":"))
            handle.write("\n")
        print(f"\n✓ ing_data.json overlay frames fixed for: {', '.join(frame_bad)}")

    # ---- fix the HTML data stores ----
    if fix and bad_charts:
        html=open(IC,encoding="utf-8").read()
        for nm in bad_charts:
            cid=nm.lower().replace(" ","-")
            T=truth_for(nm); asc=T["asc"]
            # INGRESS_DATA planets array
            pl_js=",\n      ".join(
                "{name:\"%s\", glyph:\"%s\", abbr:\"%s\", pos:\"%s\", sign:\"%s\", deg:%.2f, house:%d, speed:\"%+.2f\", conditions:%s, retro:%s}" % (
                 p, GLYPH[p], ABBR[p], fmt(T["rows"][p]["lon"]), sign_of(T["rows"][p]["lon"]),
                 T["rows"][p]["lon"]%30, house_of(T["rows"][p]["lon"],asc), T["rows"][p]["speed"],
                 json.dumps(conditions(p,sign_of(T["rows"][p]["lon"]),T["rows"][p]["lon"],T["sun"],T["rows"][p]["retro"]) if conditions(p,sign_of(T["rows"][p]["lon"]),T["rows"][p]["lon"],T["sun"],T["rows"][p]["retro"])!=["Peregrine"] else []),
                 "true" if T["rows"][p]["retro"] else "false")
                for p in [PL[i] for i in sorted(PL)])
            html=re.sub(r'(id: "'+cid+r'",[\s\S]*?planets: \[)[\s\S]*?(\n    \])',
                        lambda m: m.group(1)+"\n      "+pl_js+m.group(2), html, count=1)
            # ING_DATA p-map
            pmap={p:[round(T["rows"][p]["lon"],2),sign_of(T["rows"][p]["lon"]),house_of(T["rows"][p]["lon"],asc)] for p in [PL[i] for i in sorted(PL)]}
            html=re.sub(r'("id":"'+cid+r'"[^{]*?"p":)\{[^}]*\}\}',
                        lambda m: m.group(1)+json.dumps(pmap,ensure_ascii=False,separators=(",",":"))+"}", html, count=1)
            # DECL_DATA
            dmap=",".join(f'\n    "{p}":"{decl_str(T["rows"][p]["decl"])}"' for p in [PL[i] for i in sorted(PL)])
            html=re.sub(r'("'+cid+r'": \{)[^}]*(\})', lambda m: m.group(1)+dmap+"\n  "+m.group(2), html, count=1)
        open(IC,"w",encoding="utf-8").write(html)
        print(f"\n✓ Ingress Charts.html data stores fixed for: {', '.join(bad_charts)}")
    if fix and frame_bad:
        html=open(IC,encoding="utf-8").read()
        compact=json.dumps(ing_rows,ensure_ascii=False,separators=(",",":"))
        html,n=re.subn(r'const ING_DATA = \[.*?\];', 'const ING_DATA = '+compact+';', html, count=1, flags=re.S)
        if n!=1: raise RuntimeError("could not replace const ING_DATA in Ingress Charts.html")
        open(IC,"w",encoding="utf-8").write(html)
        print("✓ Ingress Charts.html overlay registry synchronized")
    if prose_flags:
        print("\n⚠ PROSE REVIEW NEEDED (interpretation text mentions the old wrong positions):")
        for x in prose_flags: print("   -", x)
    return bad_charts, frame_bad

if __name__=="__main__":
    audit(fix="--fix" in sys.argv)
