#!/usr/bin/env python3
"""build_charter_seed.py — parse The Charter Queue corpus into charter_seed.json.

Copied from build_castration_seed.py per _Claude-Context/PATTERN — Timeline Machine Build.md.

Reads '04 - Synthesis/Cross-cuts/The Charter Queue — Factual Timeline.md'
(entry format: '### DATE — title' / **Status:** / [**Time:**] / **Entities:** / **Track:** / body / **Source:**)

Seven tracks (the legal operating clock of the private monetary stack):
  door     — the OCC charter queue (application -> conditional -> final -> consummated)
  gate     — Federal Reserve account access. The door nobody has walked through.
  ledger   — clearing & depository permission (PSSC, DTC tokenization, Collateral AppChain)
  rulebook — the incumbents absorbing the new rails while keeping the constitution
  coin     — the issuers and their obligors: who owes the holder money, who can freeze it
  interior — the permissioned bank rails (Fnality, Partior, Canton, Kinexys, Broadridge)
  stack    — the acquisitions; vertical integration outrunning any protocol merger

NEW vs the castration seed: an optional '**Time:**' field (HH:MM, local D.C.).
Per feedback_event_chart_time_convention, an ACTUAL STATED TIME beats noon —
Paxos's charter conversion was effective 5:00 p.m., 2025-12-12.

Re-run after editing the timeline note; the seed is derived, the note is canonical.
"""
import os, re, json

HERE  = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(HERE)
SRC   = os.path.join(VAULT, "04 - Synthesis", "Cross-cuts",
                     "The Charter Queue — Factual Timeline.md")
OUT   = os.path.join(HERE, "charter_seed.json")

TRACK_MAP = [
    (r"the door",     "door"),
    (r"the gate",     "gate"),
    (r"the ledger",   "ledger"),
    (r"the rulebook", "rulebook"),
    (r"the coin",     "coin"),
    (r"the interior", "interior"),
    (r"the stack",    "stack"),
]
# order matters — specific before generic
ACTOR_MAP = [
    (r"\bocc\b",                              "OCC"),
    (r"federal reserve|kansas city",          "Federal Reserve"),
    (r"supreme court|custodia",               "Courts"),
    (r"\bsec\b",                              "SEC"),
    (r"nydfs",                                "NYDFS"),
    (r"bank of england|hm treasury",          "Bank of England"),
    (r"dtcc|dtc\b|cede",                      "DTCC"),
    (r"swift",                                "Swift"),
    (r"visa",                                 "Visa"),
    (r"mastercard",                           "Mastercard"),
    (r"j\.p\. morgan|kinexys|jpm",            "J.P. Morgan"),
    (r"circle",                               "Circle"),
    (r"ripple|standard custody",              "Ripple"),
    (r"paxos|pssc",                           "Paxos"),
    (r"coinbase",                             "Coinbase"),
    (r"kraken|payward",                       "Kraken"),
    (r"anchorage|anchor labs",                "Anchorage"),
    (r"bitgo",                                "BitGo"),
    (r"stripe|bridge",                        "Stripe / Bridge"),
    (r"zerohash",                             "zerohash"),
    (r"sofi",                                 "SoFi"),
    (r"fiserv",                               "Fiserv"),
    (r"moneygram",                            "MoneyGram"),
    (r"fnality",                              "Fnality"),
    (r"partior|dbs|deutsche bank",            "Partior"),
    (r"canton|digital asset|chainlink",       "Canton / Digital Asset"),
    (r"broadridge|hqlax",                     "Broadridge"),
]

def classify(track_line):
    t = track_line.lower()
    for pat, tr in TRACK_MAP:
        if re.search(pat, t):
            return tr
    return "door"

def actor(entities):
    e = entities.lower()
    for pat, a in ACTOR_MAP:
        if re.search(pat, e):
            return a
    return "Other"

def parse_timeline(md):
    items = []
    for m in re.finditer(r"^### (.+?) — (.+?)\n(.*?)(?=^### |^## |\Z)", md, re.M | re.S):
        rawdate, title, block = m.group(1).strip(), m.group(2).strip(), m.group(3)
        def field(name):
            fm = re.search(r"\*\*" + name + r":\*\*\s*(.+)", block)
            return fm.group(1).strip() if fm else ""
        status = field("Status").rstrip("\\").strip()
        ents   = field("Entities").rstrip("\\").strip()
        track  = field("Track")
        tm     = field("Time")
        paras = [p.strip() for p in block.split("\n\n")
                 if p.strip() and not p.strip().startswith(("**", "#", "-", "---"))]
        summary = paras[0].replace("\n", " ") if paras else ""
        src = re.search(r"\*\*Sources?:\*\*\s*\[(.+?)\]\((.+?)\)", block)
        d = re.match(r"(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?", rawdate)
        date = "-".join(x for x in d.groups() if x) if d else rawdate
        it = {
            "date": date, "date_display": rawdate, "title": title,
            "status": status, "actor": actor(ents), "entities": ents,
            "track": classify(track), "track_source": track,
            "summary": summary,
            "source_label": src.group(1) if src else "",
            "url": src.group(2) if src else "",
            "origin": "timeline",
        }
        if re.match(r"^\d{1,2}:\d{2}$", tm):
            it["time"] = tm          # stated time beats noon (Katie's convention)
        items.append(it)
    return items

def main():
    md = open(SRC, encoding="utf-8").read()
    items = parse_timeline(md)
    items.sort(key=lambda x: x["date"])
    json.dump({"_comment": "Derived seed — canonical source is 'The Charter Queue — Factual Timeline' (Cross-cuts). "
                           "Re-run build_charter_seed.py after editing it. Never hand-edit this file.",
               "items": items},
              open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    from collections import Counter
    print(len(items), "items ->", OUT)
    print("tracks:", dict(Counter(i["track"] for i in items)))
    print("actors:", dict(Counter(i["actor"] for i in items)))
    print("status:", dict(Counter(i["status"].split(" ")[0] for i in items)))
    print("timed :", [i["title"] for i in items if "time" in i])
    print("chartless (month-precision):", sum(1 for i in items if len(i["date"].split("-")) < 3))

if __name__ == "__main__":
    main()
