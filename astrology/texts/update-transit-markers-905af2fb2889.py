#!/usr/bin/env python3
"""Update the political day-markers on Transit Weather.

The POLITICAL array embedded in `04 - Synthesis/Cross-cuts/Transit Weather.html`
is the source of the clickable day-story markers. It was originally hand-built
and froze at 2026-05-29; this script keeps it alive.

Modes:
  --auto             scan event notes since the last marker; add a marker for any
                     high-volume news day (count >= 1.3x trailing-14-day median,
                     min 12 notes). Label = the day's loudest headline in its
                     dominant plotline. Marked "type":"news" + "auto":true so
                     they're easy to find and re-word editorially.
  --add DATE LABEL ARCKEY   add one curated marker (arckey: reckoning|war|money|
                     homeland|greatpower|infowar|fringe)
  --dry              print what would be added, write nothing

Context fields (active transits, prev/next lunation) are computed from the data
already embedded in Transit Weather / Lunar Weather. Run after the nightly sync
(refresh_synthesis calls --auto). Always edits the vault HTML — the Observatory
iframes it, so no rebuild needed; the desktop app needs a re-sync.
"""
import re, json, sys, glob, os, statistics
from collections import Counter
from datetime import date as Date, timedelta

HERE  = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(HERE)
TW    = os.path.join(VAULT, "04 - Synthesis", "Cross-cuts", "Transit Weather.html")
LW    = os.path.join(VAULT, "04 - Synthesis", "Cross-cuts", "Lunar Weather.html")
EVENTS= os.path.join(VAULT, "01 - Events")

ARC_KEYS = {
 "reckoning":"The Great Reckoning", "war":"War Footing — Iran & the Mideast",
 "money":"The Monetary Reset", "homeland":"Border & Homeland",
 "greatpower":"Great-Power Realignment", "infowar":"The Information War",
 "fringe":"Fringe, Disclosure & Health",
}
# plotline -> arc key (mirror of check_vault CLUSTERS)
CLUSTERS = {
 "reckoning":["Epstein","Clintons","Arrests & Legal","Government Fraud","Election Fraud","Scandals","Redistricting"],
 "war":["Iran","Israel/Jews","Military","Terror & Attacks"],
 "money":["Crypto","Economy","Energy"],
 "homeland":["Immigration","California","New York","Civil Unrest","Police/Crime"],
 "greatpower":["China","Russia/Ukraine","Other International","Europe","Canada","Mexico","Cuba","India","Foreign Policy"],
 "infowar":["Media Trust","Politics","Technology/AI","Supreme Court","Education","America","Right Wing Media"],
 "fringe":["Q","Disclosure","Theories","Electromagnetism","The Missing Scientists","Space","Health","Covid","Weather/Nature","History"],
}
PLOT2ARC = {p: k for k, pls in CLUSTERS.items() for p in pls}
AB = {"Sun":"Sun","Moon":"Moo","Mercury":"Mer","Venus":"Ven","Mars":"Mar","Jupiter":"Jup",
      "Saturn":"Sat","Uranus":"Ura","Neptune":"Nep","Pluto":"Plu"}

def load_political(html):
    m = re.search(r'const POLITICAL\s*=\s*(\[.*?\]);', html, re.S)
    return json.loads(m.group(1)), m.span(1)

def active_transits(html, d):
    """Names of outer/major synodic aspects in orb on date d, from the D lanes."""
    m = re.search(r'const D\s*=\s*(\{.*?\});\s*\n', html, re.S)
    data = json.loads(m.group(1))
    out = []
    for cat in data.get("cats", []):
        if cat.get("key") not in ("outer",):   # match original markers: outer cycles only
            continue
        for lane in cat.get("lanes", []):
            for a in lane.get("aspects", []):
                # ["b", n, start, end, exact, count, "Trine", "Uranus", "Pluto", "Sign1", "Sign2"]
                try: start, end, asp, p1, p2, s1, s2 = a[2], a[3], a[6], a[7], a[8], a[9], a[10]
                except Exception: continue
                if start <= d <= end:
                    out.append(f"{AB.get(p1,p1[:3])}–{AB.get(p2,p2[:3])} {asp} ({s1}/{s2})")
    return out

def lunations():
    lw = open(LW, encoding="utf-8").read()
    luns = []
    for m in re.finditer(r'\{"type":"(New Moon|First Quarter|Full Moon|Last Quarter)","date":"(\d{4}-\d{2}-\d{2})"[^{]*?"(?:moon_)?sign":"([A-Za-z]+)"', lw):
        luns.append((m.group(2), m.group(1), m.group(3)))
    return sorted(set(luns))

def lun_context(luns, d):
    dd = Date.fromisoformat(d)
    prev = nxt = None
    for ld, typ, sign in luns:
        l = Date.fromisoformat(ld)
        if l <= dd: prev = (ld, typ, sign, (dd - l).days)
        elif nxt is None: nxt = (ld, typ, sign, (l - dd).days)
    p = f"{prev[1]} in {prev[2]} — {prev[0]} ({prev[3]}d before)" if prev else None
    n = f"{nxt[1]} in {nxt[2]} — {nxt[0]} ({nxt[3]}d after)" if nxt else None
    return p, n

def day_notes(d):
    out = []
    for f in sorted(glob.glob(os.path.join(EVENTS, f"{d}*.md"))):
        t = open(f, encoding="utf-8").read()
        pm = re.search(r'primary_plotline:\s*"?([^"\n]+)"?', t)
        title = re.sub(r'^\d{4}-\d{2}-\d{2}-\d{4} - ', '', os.path.basename(f))[:-3]
        out.append((pm.group(1).strip() if pm else "?", title))
    return out

def make_marker(html, luns, d, label, arckey, typ="news", auto=False):
    p, n = lun_context(luns, d)
    mk = {"date": d, "label": label, "arc": arckey, "arc_name": ARC_KEYS[arckey],
          "type": typ, "transits": active_transits(html, d),
          "prev_lun": p, "next_lun": n, "eclipses": []}
    if auto: mk["auto"] = True
    return mk

def save(html, pol, span):
    body = json.dumps(pol, ensure_ascii=False, separators=(",", ":"))
    new = html[:span[0]] + body + html[span[1]:]
    open(TW, "w", encoding="utf-8").write(new)

def auto_candidates(pol):
    last = max(p["date"] for p in pol)
    have = {p["date"] for p in pol}
    counts = Counter(os.path.basename(f)[:10] for f in glob.glob(os.path.join(EVENTS, "2*.md")))
    days = sorted(dd for dd in counts if dd > last and dd <= Date.today().isoformat())
    adds = []
    for dd in days:
        if dd in have: continue
        d0 = Date.fromisoformat(dd)
        trail = [counts.get((d0 - timedelta(days=i)).isoformat(), 0) for i in range(1, 15)]
        med = statistics.median(trail) if trail else 0
        if counts[dd] < max(12, 1.3 * med): continue
        notes = day_notes(dd)
        dom = Counter(p for p, _ in notes).most_common(1)[0][0]
        in_dom = [t for p, t in notes if p == dom]
        loud = [t for t in in_dom if re.match(r'(JUST IN|BREAKING)', t)] or in_dom
        label = re.sub(r'^(JUST IN|BREAKING)\s*', '', loud[0]).strip()
        adds.append((dd, label, PLOT2ARC.get(dom, "infowar")))
    return adds

def main():
    html = open(TW, encoding="utf-8").read()
    pol, span = load_political(html)
    luns = lunations()
    dry = "--dry" in sys.argv
    added = []
    if "--add" in sys.argv:
        i = sys.argv.index("--add")
        d, label, arckey = sys.argv[i+1], sys.argv[i+2], sys.argv[i+3]
        assert arckey in ARC_KEYS, f"arc key must be one of {list(ARC_KEYS)}"
        added.append(make_marker(html, luns, d, label, arckey))
    if "--auto" in sys.argv:
        for d, label, arckey in auto_candidates(pol):
            added.append(make_marker(html, luns, d, label, arckey, auto=True))
    for mk in added:
        print(f"  + {mk['date']}  [{mk['arc']}] {mk['label']}  (transits: {len(mk['transits'])})")
    if not added:
        print("MARKERS: nothing to add"); return
    if dry:
        print("(dry run — not written)"); return
    pol = sorted(pol + added, key=lambda p: p["date"])
    save(html, pol, span)
    print(f"MARKERS: {len(added)} added, {len(pol)} total -> Transit Weather.html")

if __name__ == "__main__":
    main()
