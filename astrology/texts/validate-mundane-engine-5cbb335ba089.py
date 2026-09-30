import json, sys
sys.path.insert(0, "99 - Templates")
import mundane_engine as ME

ev=json.load(open('/tmp/daily_events.json'))
ARCS=["reckoning","war","money","homeland","greatpower","infowar","fringe"]
def dom_arc(d0,d1):
    from collections import Counter
    c=Counter()
    for d,counts in ev.items():
        if d0<=d<d1:
            for a in ARCS: c[a]+=counts.get(a,0)
    return c.most_common(1)[0][0] if sum(c.values()) else None, dict(c)

# archive arc distribution (base rate)
from collections import Counter
glob_c=Counter()
for d,counts in ev.items():
    for a in ARCS: glob_c[a]+=counts.get(a,0)
tot=sum(glob_c.values()); base={a:glob_c[a]/tot for a in ARCS}
modal=max(base,key=base.get)
print(f"Archive base rates: "+", ".join(f"{a} {base[a]*100:.0f}%" for a,_ in glob_c.most_common()))
print(f"Naive baseline = always '{modal}' → would match the period-dominant arc when that's also {modal}\n")

# ingress periods: each cardinal -> next cardinal
ings=[]
for yr in (2025,2026):
    for sgn in ("Aries","Cancer","Libra","Capricorn"):
        ch=ME.cast_ingress(yr,sgn); ings.append((ch["date"],yr,sgn,ch))
ings.sort()
print(f"{'ingress':16s} {'period':23s} {'engine→':10s} {'actual':10s} {'norm→':10s} match")
print("-"*88)
hits=hits_norm=hits_modal=n=0
for i,(idate,yr,sgn,ch) in enumerate(ings):
    end = ings[i+1][0] if i+1<len(ings) else "2026-06-18"
    if idate<"2024-06-01" or idate>="2026-06-18": continue
    actual,counts = dom_arc(idate,end)
    if not actual: continue
    a=ME.arc_scores(ch)
    pred=a["top"]
    # base-rate-normalized prediction (distinctiveness vs archive)
    norm=sorted(((arc, a["scores"][arc]/base[arc]) for arc in ARCS), key=lambda kv:-kv[1])
    pred_norm=norm[0][0]
    n+=1; hit=pred==actual; hitn=pred_norm==actual; hitm=modal==actual
    hits+=hit; hits_norm+=hitn; hits_modal+=hitm
    print(f"{yr} {sgn:9s}  {idate}→{end[:10]}  {pred:10s} {actual:10s} {pred_norm:10s} {'✓' if hit else '·'}{'N' if hitn else ' '}")
print("-"*88)
print(f"Engine (raw)  : {hits}/{n} = {hits/n*100:.0f}%")
print(f"Engine (norm) : {hits_norm}/{n} = {hits_norm/n*100:.0f}%   <- base-rate-normalized (distinctiveness)")
print(f"Naive modal   : {hits_modal}/{n} = {hits_modal/n*100:.0f}%")
