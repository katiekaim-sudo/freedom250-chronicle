#!/usr/bin/env python3
"""Inject a 'Money Machine' sub-tab into Moon Families.html.

Adds the payment-rail filings to the Moon Families view, grouped by the lunar
family their preceding New Moon seeded (Pessin bands). Idempotent (markers).
The new tab plugs into the existing generic .mf-tab/.mf-sec switcher — no JS
change to the host file. Re-run after the corpus or astro data changes.

  python3 inject_mm_moonfamilies.py [--ingest-dir DIR]
"""
import os, sys, json, html, glob, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(HERE)
MF = os.path.join(VAULT, "04 - Synthesis", "Cross-cuts", "Moon Families.html")

mm = importlib.util.module_from_spec(importlib.util.spec_from_file_location("mm", os.path.join(HERE,"build_money_machine.py")))
importlib.util.spec_from_file_location("mm", os.path.join(HERE,"build_money_machine.py")).loader.exec_module(mm)
ASTRO = json.load(open(os.path.join(HERE,"money_machine_astro.json"),encoding="utf-8")) if os.path.exists(os.path.join(HERE,"money_machine_astro.json")) else {}

FAM_ORDER = ["The Threshold","The Great Harvest","The Quiet Sowing","The Eclipse Storm"]
FAM_GLOSS = {
 "The Threshold":"0–8° · a cycle barely opening",
 "The Great Harvest":"8–16° · the chronicle's bloom family — 2024 seeds coming due",
 "The Quiet Sowing":"16–24° · a quiet planting, results held back",
 "The Eclipse Storm":"24–32° · late-degree, eclipse-charged — seeds for a 2027 harvest"}
FAM_COL = {"The Threshold":"#4a9d7f","The Great Harvest":"#9a7d28",
           "The Quiet Sowing":"#4a72b0","The Eclipse Storm":"#5a4a8a"}
TLABEL = {"check":"The Check","rails":"The Rails","gate":"The Gate","stablecoins":"Stablecoins"}

def esc(s): return html.escape(str(s if s is not None else ""))

def build_items():
    items = mm.load_seed()
    idir = sys.argv[sys.argv.index("--ingest-dir")+1] if "--ingest-dir" in sys.argv else \
           "/sessions/amazing-lucid-brown/mnt/outputs/mm_ingest/clean"
    if os.path.isdir(idir):
        for jf in sorted(glob.glob(os.path.join(idir,"*.json"))):
            try: items += json.load(open(jf,encoding="utf-8"))
            except Exception: pass
    fin = mm.finalize(items)
    rows=[]
    for it in fin:
        url=(it.get("url") or "").split("?")[0]
        a=ASTRO.get(url)
        if not a: continue
        rows.append({"url":url,"title":it["title"],"us":mm.us_date(it["date"]),
                     "date":it["date"],"agency":it["agency"],"track":it["track"],
                     "family":a["family"],"seed":a.get("seed",{})})
    return rows

def section_html(rows):
    byf={f:[] for f in FAM_ORDER}
    for r in rows: byf.setdefault(r["family"],[]).append(r)
    n=len(rows); storm=len(byf.get("The Eclipse Storm",[]))
    parts=[]
    parts.append('<div class="mf-sec" id="sec-moneymachine">')
    parts.append('<style>'
      '#sec-moneymachine .mmf-intro{font-size:.95rem;line-height:1.6;color:#5a4e3a;max-width:760px;margin:0 0 16px}'
      '#sec-moneymachine .mmf-fam{margin:0 0 18px;border:1px solid #e3dccd;border-radius:10px;background:#fffdf7;overflow:hidden}'
      '#sec-moneymachine .mmf-fh{padding:9px 14px;border-left:4px solid #ccc;font-weight:700;color:#3a3020}'
      '#sec-moneymachine .mmf-fh small{font-weight:400;color:#938876;font-style:italic;margin-left:8px}'
      '#sec-moneymachine .mmf-row{display:flex;gap:10px;align-items:baseline;padding:6px 14px;border-top:1px solid #f0eadd;'
        'cursor:pointer;font-size:.9rem}'
      '#sec-moneymachine .mmf-row:hover{background:#f4eedd}'
      '#sec-moneymachine .mmf-d{color:#938876;font-family:system-ui,sans-serif;font-size:.78rem;white-space:nowrap;min-width:84px}'
      '#sec-moneymachine .mmf-t{color:#2b2620}'
      '#sec-moneymachine .mmf-ag{color:#938876;font-size:.78rem;font-style:italic}'
      '#sec-moneymachine .mmf-badge{font-family:system-ui,sans-serif;font-size:.7rem;border-radius:9px;padding:0 7px;'
        'border:1px solid #d4c9b0;color:#5a4e3a;white-space:nowrap}'
      '</style>')
    parts.append('<h2 style="font-size:1.25rem;color:#3a3020;margin:0 0 6px">The Money Machine — filings by lunar family</h2>')
    parts.append(f'<p class="mmf-intro">The payment-rail filings of the second Trump term, sorted into the Pessin families their '
      f'preceding New Moon seeded. The tell: <b>{storm} of {n}</b> land in <b>The Eclipse Storm</b> (24–32°) — the late-degree, '
      f'eclipse-charged band whose harvest comes in <b>2027</b>. The same lineage the Fed hearings followed: planted now, reaped at '
      f'the markup. Click any filing to open it in The Money Machine.</p>')
    for f in FAM_ORDER:
        rs=sorted(byf.get(f,[]), key=lambda r:r["date"], reverse=True)
        if not rs: continue
        col=FAM_COL[f]
        parts.append(f'<div class="mmf-fam"><div class="mmf-fh" style="border-left-color:{col}">{esc(f)} '
                     f'<small>{esc(FAM_GLOSS[f])} · {len(rs)} filing{"s" if len(rs)!=1 else ""}</small></div>')
        for r in rs:
            parts.append(f'<div class="mmf-row" data-mmurl="{esc(r["url"])}">'
                         f'<span class="mmf-d">{esc(r["us"])}</span>'
                         f'<span class="mmf-t">{esc(r["title"])} <span class="mmf-ag">— {esc(r["agency"])}</span></span>'
                         f'<span class="mmf-badge" style="margin-left:auto">{esc(TLABEL.get(r["track"],r["track"]))}</span></div>')
        parts.append('</div>')
    parts.append('<script>(function(){var s=document.getElementById("sec-moneymachine");if(!s)return;'
      's.addEventListener("click",function(e){var r=e.target.closest("[data-mmurl]");if(!r)return;'
      'try{if(window.parent&&window.parent.navigateTo)window.parent.navigateTo("obs-mm",{});'
      'else if(window.parent&&window.parent._switchTab)window.parent._switchTab("obs-mm");}catch(_){}});})();</script>')
    parts.append('</div>')
    return "\n".join(parts)

def upsert(text, start, end, block, anchor_before):
    blk = f"{start}\n{block}\n{end}"
    import re
    pat = re.compile(re.escape(start)+r"[\s\S]*?"+re.escape(end))
    if pat.search(text): return pat.sub(lambda m: blk, text, count=1)
    return text.replace(anchor_before, blk+"\n"+anchor_before, 1)

def main():
    import re
    rows = build_items()
    t = open(MF, encoding="utf-8").read()
    # 1) tab button — idempotent insert right after the Featured Storylines button
    btn = '<button class="mf-tab" data-sec="sec-moneymachine">The Money Machine</button>'
    if 'data-sec="sec-moneymachine"' not in t.split('<!-- Timeline -->')[0]:
        t = re.sub(r'<!--MM-MOONFAM-TAB-START-->[\s\S]*?<!--MM-MOONFAM-TAB-END-->', '', t)
        marker = '<button class="mf-tab" data-sec="sec-storylines">Featured Storylines</button>'
        t = t.replace(marker, marker + '\n  <!--MM-MOONFAM-TAB-START-->' + btn + '<!--MM-MOONFAM-TAB-END-->', 1)
    # 2) section — upsert before the Timeline section
    sec = section_html(rows)
    t = upsert(t, "<!--MM-MOONFAM-SEC-START-->", "<!--MM-MOONFAM-SEC-END-->", sec, '<!-- Timeline -->')
    open(MF, "w", encoding="utf-8").write(t)
    print(f"injected Money Machine sub-tab into Moon Families ({len(rows)} filings)")

if __name__ == "__main__":
    main()
