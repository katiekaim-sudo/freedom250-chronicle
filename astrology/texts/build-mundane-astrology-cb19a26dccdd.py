#!/usr/bin/env python3
"""Build the Mundane Astrology section (Katie, 2026-10-03; DR-095 through DR-100).

Where astrology crosses into political analysis. Astrology here is archetypal: the sky
offers images and themes for reading the story, not proof and not a grade (Katie: "astrology
is inherently archetypal and that's what we're focused on").

Every night (Grok's nightly runs this inside refresh_synthesis) it:
  1. computes the sky with mundane_sky_events.py (cached in mundane_sky_events.json);
  2. gathers research-side dates, facts only: official actions (Official Records, Executive
     Orders, dated records), deadlines on the clock (hub clocks, follow-up return dates),
     study timelines (dated rows in Workbench *TIMELINE* files) and X-save spikes;
  3. lines them up within a day of each other as crossover candidates, scored by how strong
     the sky event is and how weighty the research item is;
  4. reads filed crossovers, independent braid owners, the append-only overlap ledger,
     Living Story Room guides and fail-closed lunar review packets;
  5. projects the Grand Tour; three historical Story Room replays; factual,
     Research-knowledge, institutional, EO, entity-role, courts-braid provenance,
     express contest/remedy, attention, computed-sky, authored-overlap,
     unresolved-gate and later-review lanes; independent braid and comparison
     pages; crossover overview/timeline/filed/day pages; and scheduled hearings;
  6. writes 99 - Templates/mundane_crossovers.json and
     04 - Synthesis/Cross-cuts/Mundane Astrology.html.

The research lane stays astrology-free: nothing here is written into a research file.
The builder may sort governed objects and flag a hearing due; it never infers a
movement, authors an interpretation, chooses a review disposition or rewrites a
historical snapshot.

  python3 build_mundane_astrology.py                 build everything
  python3 build_mundane_astrology.py --candidates 5  print the strongest unfiled crossover days
                                                     near today, with the note template (Grok)
  python3 build_mundane_astrology.py --check         exit 1 if the outputs would change
"""
from __future__ import annotations

import glob
import html
import json
import os
import re
import sys
import tempfile
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
CC = os.path.join(VAULT, "04 - Synthesis", "Cross-cuts")
OUT_HTML = os.path.join(CC, "Mundane Astrology.html")
OUT_JSON = os.path.join(HERE, "mundane_crossovers.json")
SKY_CACHE = os.path.join(HERE, "mundane_sky_events.json")
TEMPLATE = os.path.join(HERE, "mundane_astrology_template.html")
MA = os.path.join(VAULT, "03 - Astrology", "Mundane Astrology")
FILED_DIR = os.path.join(MA, "Crossovers")
WINDOW = ("2024-01-01", "2028-12-31")
NEAR = 1  # days either side that still count as "on the date"


def classify_eo_movement(record_kind):
    """Keep institutional receipts distinct from research return machinery."""
    return classify_institutional_movement(record_kind, True)


def classify_institutional_movement(record_kind, has_eo_reference=False):
    prefix = "eo" if has_eo_reference else "institutional"
    if record_kind == "movement":
        return f"{prefix}_movement", 3, True
    if record_kind == "return_gate":
        return f"{prefix}_return_gate", 0, False
    return f"{prefix}_source_custody", 0, False


def workbench():
    for c in [os.path.expanduser("~/Documents/Freedom 250 Observatory")] + glob.glob("/sessions/*/mnt/Freedom 250 Observatory"):
        if os.path.isfile(os.path.join(c, "RESEARCH DESK CATALOG.json")):
            return c
    return None


def fm(text):
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    out = {}
    if not m:
        return out
    key = None
    for line in m.group(1).splitlines():
        if re.match(r"^\s+-\s", line) and key:
            out.setdefault(key, [])
            if isinstance(out[key], list):
                out[key].append(line.split("-", 1)[1].strip().strip('"'))
            continue
        k, sep, v = line.partition(":")
        if sep and not line.startswith(" "):
            key = k.strip()
            v = v.strip()
            if v.startswith("[") and v.endswith("]"):
                try:
                    out[key] = json.loads(v)
                except ValueError:
                    out[key] = [x.strip().strip('"').strip("'") for x in v[1:-1].split(",") if x.strip()]
            else:
                out[key] = v.strip('"').strip("'")
    return out


def h1(text):
    m = re.search(r"^# (.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def rel(p):
    return os.path.relpath(p, VAULT)


# ── sky ───────────────────────────────────────────────────────────────────────────
def sky_events(refresh=False):
    if not refresh and os.path.isfile(SKY_CACHE):
        d = json.load(open(SKY_CACHE, encoding="utf-8"))
        if d.get("window") == list(WINDOW) and d.get("version") == 1:
            return d["events"]
    import mundane_sky_events as mse
    events = mse.compute(*WINDOW)
    with open(SKY_CACHE, "w", encoding="utf-8") as f:
        json.dump({"schema": "f250.mundane-sky-events/v1", "version": 1, "window": list(WINDOW),
                   "about": "Computed sky events (Swiss Ephemeris). Regenerate with build_mundane_astrology.py --sky.", "events": events},
                  f, ensure_ascii=False, indent=0)
    return events


def readings_index():
    """Authored readings by date / ingress, so a sky event can point to the reading already written."""
    by_date, by_ingress = {}, {}
    for p in glob.glob(os.path.join(VAULT, "03 - Astrology", "**", "*.md"), recursive=True):
        n = os.path.basename(p)
        m = re.match(r"(\d{4}-\d\d-\d\d) .*(New Moon|Full Moon|Eclipse).*A Reading", n)
        if m:
            by_date.setdefault(m.group(1), rel(p))
        m = re.match(r"(\d{4}) (Aries|Cancer|Libra|Capricorn) Ingress — A Reading", n)
        if m:
            by_ingress[(m.group(1), m.group(2))] = rel(p)
    return by_date, by_ingress


# ── research side (facts only) ───────────────────────────────────────────────────
def research_items(wb, today):
    items = []
    lo, hi = WINDOW
    def add(d, kind, label, weight, detail="", **link):
        if d and lo <= d[:10] <= hi:
            items.append({"date": d[:10], "kind": kind, "label": label.strip(), "weight": weight, "detail": detail.strip()[:300], **link})
    # official actions
    for p in glob.glob(os.path.join(VAULT, "02 - Research", "Official Records", "**", "*.md"), recursive=True):
        if os.path.basename(p) == "README.md":
            continue
        t = open(p, encoding="utf-8", errors="ignore").read(4000)
        f = fm(t)
        folder = os.path.relpath(p, os.path.join(VAULT, "02 - Research", "Official Records")).split(os.sep)[0]
        add(str(f.get("date", "")), "official", h1(t) or os.path.basename(p)[:-3], 3 if folder == "Hearings" else 2,
            f"{folder} · {f.get('author', '')}", path=rel(p), plotline=f.get("primary_plotline", ""))
    for p in glob.glob(os.path.join(VAULT, "03 - Executive Orders", "*.md")):
        t = open(p, encoding="utf-8", errors="ignore").read(2500)
        f = fm(t)
        if f.get("type") != "executive_order":
            continue
        add(str(f.get("signing_date", "")), "official", f"EO {f.get('eo_number', '')}: {f.get('title', '')}", 3,
            f"Executive Order · {f.get('citation', '')}", path=rel(p), plotline=f.get("plotline", ""))
    # studies of one dated official action (the date sits in the research id, e.g. ...-2026-09-28)
    if wb:
        for pk in json.load(open(os.path.join(wb, "RESEARCH DESK CATALOG.json"), encoding="utf-8")).get("packages", []):
            m = re.search(r"(20\d\d-\d\d-\d\d)$", pk["research_id"])
            if m and pk.get("object_type") != "campaign" and (pk.get("object_type") == "source_event" or re.search(
                    r"\b(Order|Proposal|Registration|Roundtable|No-Action|Notices?|Statement|Hearing|Meeting|Address|Remarks|Release|Rule|Exemption|Decision)\b", pk["title"])):
                add(m.group(1), "official", pk["title"], 2, "Studied official action · " + (pk.get("bluf") or "")[:200], rids=[pk["research_id"]])
    rec_path = os.path.join(HERE, "library_records.json")
    if os.path.isfile(rec_path):
        for r in json.load(open(rec_path, encoding="utf-8")).get("records", []):
            for e in r.get("entries", []):
                add(str(e.get("date", "")), "official", e.get("title", ""), 2, f"Dated record: {r.get('title', '')}",
                    record=r.get("key"), rids=e.get("research_ids", [])[:3])
    # deadlines on the clock
    hubs = os.path.join(HERE, "library_hubs.json")
    if os.path.isfile(hubs):
        for hid, h in json.load(open(hubs, encoding="utf-8")).get("hubs", {}).items():
            for c in h.get("clock", []):
                if re.match(r"\d{4}-\d\d-\d\d$", c.get("when", "")):
                    add(c["when"], "deadline", c["what"], 3, f"On the clock · {hid} hub", rids=[c.get("proof")] if c.get("proof") else [])
    if wb:
        led = os.path.join(wb, "RESEARCH RETURN LEDGER.json")
        if os.path.isfile(led):
            for x in json.load(open(led, encoding="utf-8")).get("followups", []):
                if x.get("status") in ("open", "scheduled") and x.get("revisit_on"):
                    add(x["revisit_on"], "return_gate", x.get("question", ""), 0, "Follow-up return date",
                        rids=x.get("research_ids", [])[:3], crossover_eligible=False)
        movement_registry = os.path.join(
            wb,
            "Research Packages",
            "Federal Government Movement Atlas",
            "MOVEMENT_REGISTRY.json",
        )
        if os.path.isfile(movement_registry):
            movement_data = json.load(open(movement_registry, encoding="utf-8"))
            for movement in movement_data.get("movements", []):
                eo_refs = movement.get("executive_order_refs") or []
                kind, weight, crossover_eligible = classify_institutional_movement(
                    movement.get("record_kind", ""), bool(eo_refs)
                )
                before = movement.get("state_before", "")
                after = movement.get("state_after", "")
                add(
                    str(movement.get("event_date", "")),
                    kind,
                    movement.get("title", ""),
                    weight,
                    f"{movement.get('stage_reached', '').replace('_', ' ')} · {before} → {after}",
                    rids=[movement.get("research_id")] if movement.get("research_id") else [],
                    movement_id=movement.get("movement_id", ""),
                    eo_refs=eo_refs,
                    record_kind=movement.get("record_kind", ""),
                    entity_roles=movement.get("entity_roles") or [],
                    stage_reached=movement.get("stage_reached", ""),
                    unresolved_stages=movement.get("unresolved_stages") or [],
                    claim_limit=movement.get("claim_limit", ""),
                    next_receipt=movement.get("next_receipt", ""),
                    clocks=movement.get("clocks") or {},
                    crossover_eligible=crossover_eligible,
                )
        # study timelines
        reg_rids = {}
        regp = os.path.join(wb, "RESEARCH REGISTRY.md")
        if os.path.isfile(regp):
            for line in open(regp, encoding="utf-8"):
                m = re.match(r"\| `([^`]+)` \| `[^`]+` \| `[^`]+` \| `?([^`|]+)`? \|", line)
                if m:
                    reg_rids[m.group(1)] = [x.strip() for x in m.group(2).split(";")]
        for p in glob.glob(os.path.join(wb, "Research Packages", "**", "*TIMELINE*.md"), recursive=True):
            rp = os.path.relpath(p, wb)
            rids = reg_rids.get(rp, [])[:1]
            seen = set()
            for line in open(p, encoding="utf-8", errors="ignore"):
                if not line.startswith("|"):
                    continue
                cells = [c.strip().strip("*`") for c in line.strip().strip("|").split("|")]
                if len(cells) < 2:
                    continue
                m = re.match(r"(\d{4}-\d\d-\d\d)", cells[0])
                if not m:
                    continue
                clean = [re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", c) for c in cells[1:] if c and not c.startswith("http")]
                text = max(clean, key=len) if clean else ""
                key = (m.group(1), text[:80])
                if key in seen:
                    continue
                seen.add(key)
                add(m.group(1), "timeline", text[:220], 1, "Study timeline · " + os.path.basename(p)[:-3].replace("_", " ").title(), rids=rids, wb_path=rp)
    # X-save spikes
    per = defaultdict(Counter)
    titles = defaultdict(list)
    for p in glob.glob(os.path.join(VAULT, "01 - Events", "*.md")):
        n = os.path.basename(p)
        if not re.match(r"\d{4}-\d\d-\d\d", n):
            continue
        t = open(p, encoding="utf-8", errors="ignore").read(1500)
        pl = fm(t).get("primary_plotline", "")
        if not pl or pl == "Other":
            continue
        per[pl][n[:10]] += 1
        titles[(pl, n[:10])].append(re.sub(r"^\d{4}-\d\d-\d\d-\d{4} - ", "", n[:-3]))
    for pl, days in per.items():
        for d, n in days.items():
            base = date.fromisoformat(d)
            prior = [days.get((base - timedelta(days=k)).isoformat(), 0) for k in range(1, 31)]
            mean = sum(prior) / 30
            if n >= 4 and n >= 3 * max(mean, 0.5):
                add(d, "spike", f"{n} X saves on {pl}", 3 if n >= 8 else 2, "; ".join(titles[(pl, d)][:3]), plotline=pl, saves=n)
    return items


# ── matching ─────────────────────────────────────────────────────────────────────
def chapters(events):
    luns = [e for e in events if e["kind"] == "lunation"]
    seasons = [e for e in events if e["kind"] == "ingress" and e.get("season")]
    return luns, seasons


def last_before(seq, d):
    best = None
    for e in seq:
        if e["date"] <= d:
            best = e
        else:
            break
    return best


def match(events, items, readings):
    from mundane_sky_events import KEY_CHARTS
    by_date, by_ingress = readings
    sky_by_day = defaultdict(list)
    for e in events:
        r = by_date.get(e["date"]) if e["kind"] in ("lunation", "eclipse") else None
        if e["kind"] == "ingress" and e.get("season"):
            r = by_ingress.get((e["date"][:4], e["sign"]))
        if r:
            e = {**e, "reading": r}
        d0 = date.fromisoformat(e["date"])
        for k in range(-NEAR, NEAR + 1):
            sky_by_day[(d0 + timedelta(days=k)).isoformat()].append({**e, "offset": k})
    res_by_day = defaultdict(list)
    for it in items:
        res_by_day[it["date"]].append(it)
    luns, seasons = chapters(events)
    days = []
    for d, its in res_by_day.items():
        eligible = [it for it in its if it.get("crossover_eligible", True)]
        if not eligible:
            continue
        sky = sky_by_day.get(d, [])
        if not sky:
            continue
        text = " ".join(i["label"] + " " + i.get("detail", "") for i in eligible)
        scored = []
        for s in sky:
            w = s["weight"] + (1 if s["offset"] == 0 else 0)
            if s["kind"] == "transit":
                if re.search(KEY_CHARTS.get(s.get("chart"), "$^"), text):
                    w += 2
                    s = {**s, "resonates": True}
                elif s["chart"] != "United States":
                    w -= 1
            scored.append((w, s))
        scored.sort(key=lambda x: -x[0])
        top_sky = scored[0][0]
        uniq = {}
        for i in sorted(its, key=lambda i: -i["weight"]):
            uniq.setdefault(re.sub(r"\W+", " ", i["label"].lower()).strip()[:120], i)
        its = list(uniq.values())
        eligible_count = sum(it.get("crossover_eligible", True) for it in its)
        score = top_sky + max(it["weight"] for it in eligible) + min(2, eligible_count - 1) * 0.5 + min(2, len(scored) - 1) * 0.5
        ch = last_before(luns, d)
        se = last_before(seasons, d)
        days.append({"date": d, "score": round(score, 1),
                     "sky": [dict(s, strength=w) for w, s in scored[:6]],
                     "research": its[:8], "research_count": len(its),
                     "chapter": ch["label"] + " · " + ch["date"] if ch else "", "season": se["sign"] + " season · " + se["date"] if se else ""})
    days.sort(key=lambda x: x["date"])
    return days


# ── filed notes ───────────────────────────────────────────────────────────────────
def md_html(md):
    out, para, lst = [], [], []
    def inline(s):
        s = html.escape(s)
        s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
        s = re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)
        s = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", lambda m: "<span class='wl'>" + (m.group(2) or m.group(1)) + "</span>", s)
        s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', s)
        return s
    def flush():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>"); para.clear()
        if lst:
            out.append("<ul>" + "".join("<li>" + inline(x) + "</li>" for x in lst) + "</ul>"); lst.clear()
    for line in md.splitlines():
        if re.match(r"^#{1,6} ", line):
            flush(); lvl = min(4, len(line.split(" ")[0]) + 1); out.append(f"<h{lvl}>" + inline(line.split(" ", 1)[1]) + f"</h{lvl}>")
        elif re.match(r"^\s*[-*] ", line):
            if para: flush()
            lst.append(re.sub(r"^\s*[-*] ", "", line))
        elif line.startswith(">"):
            flush(); out.append("<blockquote>" + inline(line.lstrip("> ")) + "</blockquote>")
        elif not line.strip():
            flush()
        else:
            if lst: flush()
            para.append(line.strip())
    flush()
    return "\n".join(out)


def filed_notes():
    notes = []
    for p in sorted(glob.glob(os.path.join(FILED_DIR, "*.md"))):
        t = open(p, encoding="utf-8").read()
        f = fm(t)
        if f.get("type") != "mundane_crossover":
            continue
        body = re.sub(r"^---\n.*?\n---\n", "", t, flags=re.S)
        first = next((ln.strip() for ln in body.split("## The archetypal reading", 1)[-1].splitlines() if ln.strip() and not ln.startswith("#")), "")
        cid = os.path.basename(p)[:-3]
        notes.append({"id": cid, "title": f.get("title") or h1(body) or cid, "date": str(f.get("date", "")), "dates": f.get("dates") or [str(f.get("date", ""))],
                      "filed_by": f.get("filed_by", ""), "status": f.get("status", "filed"), "sky": f.get("sky") or [], "research": f.get("research") or [],
                      "plotlines": f.get("plotlines") or [], "research_ids": f.get("research_ids") or [], "braids": f.get("braids") or [], "summary": first[:400],
                      "path": rel(p), "html": md_html(body)})
    return notes


def overlap_files():
    """The overlap work that existed before this section (Katie: it moves in here). Files stay where they are."""
    out = []
    for folder, label in (("Mundane Story Overlaps", "Story overlap"), ("Money x Sky", "Money × Sky")):
        for p in sorted(glob.glob(os.path.join(VAULT, "03 - Astrology", "Astrology Files", folder, "**", "*.md"), recursive=True)):
            t = open(p, encoding="utf-8", errors="ignore").read()
            f = fm(t)
            n = os.path.basename(p)
            if n.upper().startswith(("README", "WAVE_")) or re.match(r"^[A-Z0-9_]+\.md$", n):
                continue
            body = re.sub(r"^---\n.*?\n---\n", "", t, flags=re.S)
            para = next((ln.strip() for ln in body.splitlines() if ln.strip() and not ln.startswith(("#", ">", "|", "-", "*"))), "")
            out.append({"title": f.get("title") or h1(body) or n[:-3], "kind": label, "path": rel(p), "summary": para[:300],
                        "dates": [x for x in [f.get("created"), f.get("initial_return_gate"), f.get("chapter_close"), f.get("extended_return_gate")] if x],
                        "gates": {k: f[k] for k in ("initial_return_gate", "chapter_close", "extended_return_gate") if f.get(k)}})
    return out


# ── story braids (Katie 2026-10-03: "follow a story through its astrological timeline") ──
BRAIDS_DIR = os.path.join(MA, "Braids")
STORY_ROOMS_DIR = os.path.join(MA, "Story Rooms")
REVIEW_HEARINGS_DIR = os.path.join(MA, "Review Hearings")
RELATIONSHIP_HISTORY = os.path.join(HERE, "planetary_relationship_history.json")
OVERLAP_LEDGER = os.path.join(MA, "Braid Overlap Ledger.jsonl")
STRAND_ROLES = {"lead_mechanism", "co_mechanism", "supporting_context", "outcompeted", "unresolved"}
STRAND_PRESENCE = {"inherited_substrate", "active_dialogue", "seed_echo"}


def load_braids():
    out = []
    for p in sorted(glob.glob(os.path.join(BRAIDS_DIR, "*.md"))):
        t = open(p, encoding="utf-8").read()
        f = fm(t)
        if f.get("type") != "story_braid":
            continue
        body = re.sub(r"^---\n.*?\n---\n", "", t, flags=re.S)
        body = re.sub(r"^\s*# [^\n]*\n+(\*[^\n]*\*\n+)?(## The braid so far\n+)?", "", body)
        out.append({"slug": os.path.basename(p)[:-3], "path": rel(p), "title": f.get("title", ""), "question": f.get("question", ""),
                    "subplots": f.get("subplots") or [], "plotlines": f.get("plotlines") or [], "keywords": f.get("keywords") or [],
                    "research_ids": f.get("research_ids") or [], "executive_orders": [str(x) for x in (f.get("executive_orders") or [])],
                    "movement_ids": f.get("movement_ids") or [],
                    "charts": f.get("charts") or [], "status": f.get("status", "active"),
                    "relationship_strands": f.get("relationship_strands") or [],
                    "relationship_frame": f.get("relationship_frame", ""),
                    "relationship_chapter": f.get("relationship_chapter", ""),
                    "relationship_authored_on": str(f.get("relationship_authored_on", "")),
                    "relationship_review_on": str(f.get("relationship_review_on", "")),
                    "html": md_html(body)})
    return out


def load_story_rooms():
    out = []
    for p in sorted(glob.glob(os.path.join(STORY_ROOMS_DIR, "*.md"))):
        t = open(p, encoding="utf-8").read()
        f = fm(t)
        if f.get("type") != "living_story_room":
            continue
        body = re.sub(r"^---\n.*?\n---\n", "", t, flags=re.S)
        body = re.sub(r"^\s*# [^\n]*\n+", "", body)
        out.append({
            "slug": f.get("slug") or os.path.basename(p)[:-3],
            "path": rel(p), "title": f.get("title", ""), "question": f.get("question", ""),
            "status": f.get("status", "guided"), "lead_braid": f.get("lead_braid", ""),
            "member_braids": f.get("member_braids") or [], "comparison": f.get("comparison", ""),
            "tour_order": int(f.get("tour_order") or 999), "html": md_html(body),
        })
    return out


def load_review_hearings():
    out = []
    for p in sorted(glob.glob(os.path.join(REVIEW_HEARINGS_DIR, "*.md"))):
        t = open(p, encoding="utf-8").read()
        f = fm(t)
        if f.get("type") != "braid_review_hearing":
            continue
        body = re.sub(r"^---\n.*?\n---\n", "", t, flags=re.S)
        body = re.sub(r"^\s*# [^\n]*\n+", "", body)
        out.append({
            "id": str(f.get("review_date", "")), "path": rel(p),
            "title": f.get("title", ""), "review_date": str(f.get("review_date", "")),
            "status": f.get("status", "scheduled"), "frame": f.get("frame", ""),
            "closing_chapter": f.get("closing_chapter", ""), "next_chapter": f.get("next_chapter", ""),
            "owners": f.get("owners") or [], "html": md_html(body),
        })
    return out


def build_review_hearings(specs, overlap_ledger, relationship_data, today):
    current = {row["owner_slug"]: row for row in overlap_ledger["records"] if row.get("status") == "current"}
    out = []
    seen = set()
    relationship_text = json.dumps(relationship_data, ensure_ascii=False)
    for spec in specs:
        if not re.match(r"^20\d\d-\d\d-\d\d$", spec["review_date"]):
            raise RuntimeError(f"review hearing {spec['title']} needs an exact review date")
        if spec["id"] in seen:
            raise RuntimeError(f"duplicate review hearing {spec['id']}")
        seen.add(spec["id"])
        if spec["status"] != "scheduled":
            raise RuntimeError(f"review hearing {spec['id']} may not pre-author a disposition")
        if len(spec["owners"]) != len(set(spec["owners"])) or set(spec["owners"]) != set(current):
            raise RuntimeError(f"review hearing {spec['id']} must name every current overlap owner exactly once")
        if spec["next_chapter"] not in relationship_text:
            raise RuntimeError(f"review hearing {spec['id']} next chapter is not in relationship history")
        snapshots = []
        for owner in spec["owners"]:
            row = current[owner]
            if row.get("frame") != spec["frame"] or row.get("chapter") != spec["closing_chapter"]:
                raise RuntimeError(f"review hearing {spec['id']} window differs from {owner}")
            if row.get("review_on") != spec["review_date"] or (row.get("review") or {}).get("status") != "pending":
                raise RuntimeError(f"review hearing {spec['id']} owner {owner} is not pending on its date")
            snapshots.append({
                "record_type": row["record_type"], "owner_slug": owner,
                "authored_on": row["authored_on"], "review_on": row["review_on"],
                "strand_count": len(row.get("strands") or []), "member_count": len(row.get("members") or []),
                "review_status": row["review"]["status"],
            })
        out.append({
            **spec, "display_status": "scheduled" if today.isoformat() < spec["review_date"] else "review_due",
            "snapshots": snapshots,
            "authority_boundary": "This packet prepares a human hearing. It may flag the date as due, but it cannot choose a disposition, move a strand, rewrite history or create a Forecast Ledger call.",
        })
    return out


def load_braid_comparisons():
    out = []
    for p in sorted(glob.glob(os.path.join(BRAIDS_DIR, "*.md"))):
        t = open(p, encoding="utf-8").read()
        f = fm(t)
        if f.get("type") != "braid_comparison":
            continue
        body = re.sub(r"^---\n.*?\n---\n", "", t, flags=re.S)
        body = re.sub(r"^\s*# [^\n]*\n+", "", body)
        out.append({
            "slug": f.get("slug") or os.path.basename(p)[:-3],
            "path": rel(p), "title": f.get("title", ""), "question": f.get("question", ""),
            "braids": f.get("braids") or [], "relationship_frame": f.get("relationship_frame", ""),
            "relationship_chapter": f.get("relationship_chapter", ""),
            "authored_on": str(f.get("authored_on", "")), "review_on": str(f.get("review_on", "")),
            "status": f.get("status", "active"), "html": md_html(body),
        })
    return out


def load_overlap_ledger():
    if not os.path.isfile(OVERLAP_LEDGER):
        raise RuntimeError("missing governed Braid Overlap Ledger")
    rows = [json.loads(line) for line in open(OVERLAP_LEDGER, encoding="utf-8") if line.strip()]
    if not rows or rows[0].get("record_type") != "meta" or rows[0].get("schema") != "f250.mundane-braid-overlap-history/v1":
        raise RuntimeError("unsupported Braid Overlap Ledger schema")
    return {"meta": rows[0], "records": rows[1:]}


def attach_overlap_history(braids, comparisons, ledger, today):
    braid_by_slug = {row["slug"]: row for row in braids}
    comparison_by_slug = {row["slug"]: row for row in comparisons}
    records_by_owner = defaultdict(list)
    current_keys = set()
    for record in ledger["records"]:
        record_type = record.get("record_type")
        owners = braid_by_slug if record_type == "braid" else comparison_by_slug if record_type == "comparison" else None
        owner_slug = record.get("owner_slug", "")
        if owners is None or owner_slug not in owners:
            raise RuntimeError(f"overlap ledger has unknown {record_type} owner {owner_slug!r}")
        key = (record_type, owner_slug, record.get("frame"), record.get("chapter"), record.get("authored_on"))
        if key in current_keys:
            raise RuntimeError(f"overlap ledger repeats window identity {key}")
        current_keys.add(key)
        if record.get("status") not in {"current", "historical"}:
            raise RuntimeError(f"overlap ledger {owner_slug} has invalid status")
        review = record.get("review") or {}
        if record.get("status") == "current" and review.get("status") != "pending":
            raise RuntimeError(f"current overlap ledger record {owner_slug} must remain pending")
        records_by_owner[(record_type, owner_slug)].append(record)

    for slug, braid in braid_by_slug.items():
        records = sorted(records_by_owner.get(("braid", slug), []), key=lambda row: (row["authored_on"], row["frame"], row["chapter"]))
        current = [row for row in records if row["status"] == "current"]
        strands = braid.get("relationship_strands") or []
        if strands:
            if len(current) != 1:
                raise RuntimeError(f"braid {slug} needs exactly one current overlap ledger record")
            record = current[0]
            expected = {
                "frame": braid["relationship_frame"], "chapter": braid["relationship_chapter"],
                "authored_on": braid["relationship_authored_on"], "review_on": braid["relationship_review_on"],
                "strands": strands,
            }
            if any(record.get(key) != value for key, value in expected.items()):
                raise RuntimeError(f"braid {slug} differs from its current overlap ledger snapshot")
        elif current:
            raise RuntimeError(f"unauthored braid {slug} cannot have a current overlap ledger record")
        braid["overlap_history"] = [{**row, "display_status": "review_due" if row["status"] == "current" and today.isoformat() >= row["review_on"] else row["status"]} for row in records]

    for slug, comparison in comparison_by_slug.items():
        records = sorted(records_by_owner.get(("comparison", slug), []), key=lambda row: (row["authored_on"], row["frame"], row["chapter"]))
        current = [row for row in records if row["status"] == "current"]
        if len(current) != 1:
            raise RuntimeError(f"braid comparison {slug} needs exactly one current overlap ledger record")
        record = current[0]
        expected = {"frame": comparison["relationship_frame"], "chapter": comparison["relationship_chapter"],
                    "authored_on": comparison["authored_on"], "review_on": comparison["review_on"],
                    "members": comparison["braids"]}
        if any(record.get(key) != value for key, value in expected.items()):
            raise RuntimeError(f"braid comparison {slug} differs from its overlap ledger snapshot")
        comparison["overlap_history"] = [{**row, "display_status": "review_due" if row["status"] == "current" and today.isoformat() >= row["review_on"] else row["status"]} for row in records]
    return {"schema": ledger["meta"]["schema"], "records": ledger["records"],
            "counts": {"records": len(ledger["records"]),
                       "current": sum(row.get("status") == "current" for row in ledger["records"]),
                       "historical": sum(row.get("status") == "historical" for row in ledger["records"]),
                       "review_due": sum(row.get("status") == "current" and today.isoformat() >= row.get("review_on", "") for row in ledger["records"])},
            "authority_boundary": ledger["meta"]["authority_boundary"]}


def build_braid_comparisons(comparisons, braids, today):
    by_slug = {row["slug"]: row for row in braids}
    out = []
    for comparison in comparisons:
        members = comparison.get("braids") or []
        if len(members) < 2 or len(set(members)) != len(members):
            raise RuntimeError(f"braid comparison {comparison['slug']} needs distinct members")
        missing = [slug for slug in members if slug not in by_slug]
        if missing:
            raise RuntimeError(f"braid comparison {comparison['slug']} has unknown members: {missing}")
        rows = [by_slug[slug] for slug in members]
        for row in rows:
            field = row.get("relationship_field") or {}
            if (field.get("frame") or {}).get("chart_id") != comparison.get("relationship_frame"):
                raise RuntimeError(f"braid comparison {comparison['slug']} frame differs from {row['slug']}")
            if (field.get("chapter") or {}).get("chart_id") != comparison.get("relationship_chapter"):
                raise RuntimeError(f"braid comparison {comparison['slug']} chapter differs from {row['slug']}")
        relationship_rows = defaultdict(list)
        pairs = {}
        for row in rows:
            for strand in (row.get("relationship_field") or {}).get("strands", []):
                relationship_id = strand["relationship_id"]
                pairs[relationship_id] = strand.get("pair") or []
                relationship_rows[relationship_id].append({
                    "braid": row["slug"], "title": row["title"], "role": strand["role"],
                    "presence": strand.get("presence") or [], "question": strand["question"],
                })
        shared = [{"relationship_id": rid, "pair": pairs[rid], "uses": uses}
                  for rid, uses in relationship_rows.items() if len(uses) > 1]
        shared.sort(key=lambda row: (-len(row["uses"]), row["relationship_id"]))
        out.append({**comparison,
                    "members": [{"slug": row["slug"], "title": row["title"], "question": row["question"],
                                 "readiness": row.get("readiness") or {}} for row in rows],
                    "shared_relationships": shared,
                    "comparison_status": "current_window" if today.isoformat() < comparison["review_on"] else "review_due",
                    "authority_boundary": "This comparison owns no factual claim or planetary strand. It displays separately authored roles and never creates a merged verdict, evidence vote or common-command claim."})
    return out


def _merge_room_objects(rows):
    """Deduplicate projections while preserving every contributing braid."""
    merged = {}
    for slug, row in rows:
        key = (row.get("date", ""), row.get("kind", ""), row.get("movement_id", ""), row.get("label", ""))
        if key not in merged:
            merged[key] = {**row, "source_braids": [slug]}
        elif slug not in merged[key]["source_braids"]:
            merged[key]["source_braids"].append(slug)
    return sorted(merged.values(), key=lambda row: (row.get("date", ""), row.get("kind", ""), row.get("label", "")))


def _chapter_date(chart_id):
    match = re.search(r"(20\d\d-\d\d-\d\d)", chart_id or "")
    return match.group(1) if match else ""


def build_story_rooms(room_specs, braids, comparisons, today):
    """Project independent braid owners into replayable lunar chapters.

    This function sorts and joins existing governed objects. It does not author
    a factual conclusion, movement, relationship role or review disposition.
    """
    by_slug = {row["slug"]: row for row in braids}
    comparison_by_slug = {row["slug"]: row for row in comparisons}
    out = []
    seen = set()
    for spec in room_specs:
        if spec["slug"] in seen:
            raise RuntimeError(f"duplicate Living Story Room {spec['slug']}")
        seen.add(spec["slug"])
        if spec["status"] not in {"flagship", "replay", "guided"}:
            raise RuntimeError(f"Living Story Room {spec['slug']} has invalid status")
        members = spec.get("member_braids") or []
        if len(members) < 2 or len(set(members)) != len(members):
            raise RuntimeError(f"Living Story Room {spec['slug']} needs distinct member braids")
        missing = [slug for slug in members if slug not in by_slug]
        if missing:
            raise RuntimeError(f"Living Story Room {spec['slug']} has unknown braids: {missing}")
        if spec.get("lead_braid") not in members:
            raise RuntimeError(f"Living Story Room {spec['slug']} lead braid is not a member")
        comparison = comparison_by_slug.get(spec.get("comparison")) if spec.get("comparison") else None
        if spec.get("comparison") and not comparison:
            raise RuntimeError(f"Living Story Room {spec['slug']} has unknown comparison")
        if comparison and set(row["slug"] for row in comparison["members"]) != set(members):
            raise RuntimeError(f"Living Story Room {spec['slug']} comparison membership differs")

        member_rows = [by_slug[slug] for slug in members]
        chapter_sources = defaultdict(list)
        for braid in member_rows:
            for chapter in braid.get("chapters", []):
                chapter_sources[chapter["date"]].append((braid["slug"], chapter))

        chapters = []
        for chapter_date, sources in sorted(chapter_sources.items()):
            exemplar = sources[0][1]
            cutoff = min(exemplar["end"], today.isoformat())
            beats = _merge_room_objects(
                [(slug, beat) for slug, chapter in sources for beat in chapter.get("beats", []) if beat.get("date", "") <= cutoff]
            )
            sky_map = {}
            sky_map[(chapter_date, "lunation", exemplar["label"])] = {
                "date": chapter_date, "kind": "lunation", "label": exemplar["label"]
            }
            for _slug, chapter in sources:
                for sky in chapter.get("sky", []):
                    if sky.get("date", "") <= cutoff:
                        sky_map[(sky.get("date"), sky.get("kind"), sky.get("label"))] = sky
            authored = []
            later_reviews = []
            for braid in member_rows:
                for window in braid.get("overlap_history", []):
                    if _chapter_date(window.get("chapter")) != chapter_date:
                        continue
                    authored.append({
                        "braid": braid["slug"], "title": braid["title"],
                        "authored_on": window["authored_on"], "review_on": window["review_on"],
                        "status": window["display_status"], "strands": window.get("strands") or [],
                    })
                    review = window.get("review") or {}
                    if review.get("status") != "pending":
                        later_reviews.append({"braid": braid["slug"], "title": braid["title"], **review})

            lanes = {
                "factual_record": [row for row in beats if row.get("kind") in {"official", "timeline"}],
                "research_knowledge": [row for row in beats if row.get("kind") == "study"],
                "institutional_movement": [row for row in beats if row.get("kind") == "institutional_movement"],
                "executive_order_lineage": [row for row in beats if row.get("kind") == "eo_movement"],
                "attention": [row for row in beats if row.get("kind") == "saves"],
                "unresolved_gates": [row for row in beats if row.get("kind") in {"deadline", "return_gate", "eo_return_gate", "institutional_return_gate"}],
                "computed_sky": sorted(sky_map.values(), key=lambda row: (row.get("date", ""), row.get("label", ""))),
                "authored_overlap": sorted(authored, key=lambda row: (row["authored_on"], row["braid"])),
                "later_review": sorted(later_reviews, key=lambda row: (row.get("reviewed_on", ""), row["braid"])),
            }
            entity_rows = []
            movement_like = (lanes["institutional_movement"] + lanes["executive_order_lineage"] + lanes["unresolved_gates"])
            for movement in movement_like:
                for role in movement.get("entity_roles") or []:
                    entity_rows.append(("|".join(movement.get("source_braids") or []), {
                        "date": movement.get("date", ""), "kind": "entity_role",
                        "label": role.get("entity_path", ""), "detail": role.get("role", "").replace("_", " "),
                        "movement_id": movement.get("movement_id", ""),
                        "source_braids": movement.get("source_braids") or [],
                    }))
            entity_merged = {}
            for _source_key, row in entity_rows:
                key = (row["date"], row["label"], row["detail"], row["movement_id"])
                if key not in entity_merged:
                    entity_merged[key] = row
                else:
                    entity_merged[key]["source_braids"] = sorted(set(entity_merged[key]["source_braids"] + row["source_braids"]))
            lanes["entity_path"] = sorted(entity_merged.values(), key=lambda row: (row["date"], row["label"], row["detail"]))
            lanes["court_braid_record"] = [
                row for row in lanes["factual_record"]
                if "courts-and-the-law" in (row.get("source_braids") or [])
            ]
            lanes["contest_and_remedy"] = [
                row for row in (lanes["institutional_movement"] + lanes["executive_order_lineage"])
                if any(ref.get("relation") == "contest_or_remedy" for ref in (row.get("eo_refs") or []))
            ]
            chapters.append({
                "date": chapter_date, "end": exemplar["end"], "cutoff": cutoff,
                "label": exemplar["label"], "sign": exemplar["sign"], "phase": exemplar["phase"],
                "season": exemplar["season"], "eclipse": exemplar.get("eclipse"), "lanes": lanes,
                "change": {
                    "since_chapter": chapters[-1]["date"] if chapters else "",
                    "factual_records": len(lanes["factual_record"]),
                    "research_updates": len(lanes["research_knowledge"]),
                    "institutional_movements": len(lanes["institutional_movement"]),
                    "executive_order_movements": len(lanes["executive_order_lineage"]),
                    "entity_roles": len(lanes["entity_path"]),
                    "court_braid_records": len(lanes["court_braid_record"]),
                    "contest_and_remedy_movements": len(lanes["contest_and_remedy"]),
                    "attention_items": len(lanes["attention"]),
                    "open_gates": len(lanes["unresolved_gates"]),
                    "authored_hearings": len(lanes["authored_overlap"]),
                    "boundary": "Categorical additions since the previous lunar cutoff; not a score, rank or claim of progress.",
                },
            })

        ahead = _merge_room_objects([
            (braid["slug"], row) for braid in member_rows for row in braid.get("ahead", [])
            if row.get("kind") in {"deadline", "return_gate", "eo_return_gate", "institutional_return_gate"}
        ])
        current_chapter = next((row for row in reversed(chapters) if row["date"] <= today.isoformat()), None)
        out.append({
            **spec,
            "members": [{"slug": row["slug"], "title": row["title"], "question": row["question"],
                         "readiness": row.get("readiness") or {}} for row in member_rows],
            "comparison_route": comparison["slug"] if comparison else "",
            "replay_enabled": spec["status"] in {"flagship", "replay"},
            "chapter_count": len(chapters),
            "current_chapter": current_chapter["date"] if current_chapter else "",
            "chapters": chapters if spec["status"] in {"flagship", "replay"} else [],
            "what_would_change": ahead[:16],
            "authority_boundary": "This room owns orientation and navigation only. Facts, institutional movements, attention, computed sky, authored overlaps and reviews remain independently owned and meet only on exact dates.",
        })
    return sorted(out, key=lambda row: (row["tour_order"], row["title"]))


def load_relationship_history():
    if not os.path.isfile(RELATIONSHIP_HISTORY):
        raise RuntimeError("missing governed planetary relationship history")
    data = json.load(open(RELATIONSHIP_HISTORY, encoding="utf-8"))
    if data.get("schema") != "freedom250.planetary-relationships.geometry-history/v1":
        raise RuntimeError("unsupported planetary relationship history schema")
    return data


def compact_relationship_state(state):
    if not state:
        return None
    geometry = state.get("geometry") or {}
    aspect = state.get("direct_aspect")
    return {
        "state_id": state.get("state_id", ""),
        "phase": geometry.get("phase_name"),
        "direction": geometry.get("phase_direction"),
        "aspect": aspect.get("aspect_id") if aspect else None,
        "orb": aspect.get("orb_deg") if aspect else None,
        "motion": aspect.get("motion_state") if aspect else None,
    }


def relationship_field_for_braid(braid, relationship_data, today):
    catalog = {row["relationship_id"]: row for row in relationship_data.get("cycle_catalog") or []}
    charts = {row["chart_id"]: row for row in relationship_data.get("charts") or []}
    strands = braid.get("relationship_strands") or []
    if not strands:
        return {
            "frame": None, "chapter": None, "strands": [], "status": "unauthored",
            "authored_on": "", "review_on": "",
            "authority_boundary": "No planetary relationship is assigned automatically. Plotlines remain narrative routes; astrology remains a separate interpretive rope.",
        }
    frame_id = braid.get("relationship_frame", "")
    chapter_id = braid.get("relationship_chapter", "")
    authored_on = braid.get("relationship_authored_on", "")
    review_on = braid.get("relationship_review_on", "")
    if frame_id not in charts or charts[frame_id].get("chart_type") != "ingress":
        raise RuntimeError(f"braid {braid['slug']} lacks a valid authored relationship ingress")
    if chapter_id not in charts or charts[chapter_id].get("chart_type") != "lunation":
        raise RuntimeError(f"braid {braid['slug']} lacks a valid authored relationship chapter")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", authored_on) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", review_on):
        raise RuntimeError(f"braid {braid['slug']} relationship window lacks valid dates")
    frame, chapter = charts[frame_id], charts[chapter_id]
    if frame["date"] > authored_on or chapter["date"] > authored_on or review_on <= chapter["date"]:
        raise RuntimeError(f"braid {braid['slug']} has an invalid authored relationship window")
    frame_states = {row["relationship_id"]: row for row in (frame or {}).get("cycles", [])}
    chapter_states = {row["relationship_id"]: row for row in (chapter or {}).get("cycles", [])}
    projected, seen = [], set()
    for strand in strands:
        if not isinstance(strand, dict):
            raise RuntimeError(f"braid {braid['slug']} has a non-object relationship strand")
        relationship_id = strand.get("relationship_id", "")
        role = strand.get("role", "")
        presence = strand.get("presence") or []
        if relationship_id not in catalog:
            raise RuntimeError(f"braid {braid['slug']} has unknown relationship {relationship_id!r}")
        if relationship_id in seen:
            raise RuntimeError(f"braid {braid['slug']} repeats relationship {relationship_id}")
        if role not in STRAND_ROLES:
            raise RuntimeError(f"braid {braid['slug']} has invalid relationship role {role!r}")
        if not isinstance(presence, list) or not presence or any(value not in STRAND_PRESENCE for value in presence):
            raise RuntimeError(f"braid {braid['slug']} has invalid presence for {relationship_id}")
        if not strand.get("question") or not strand.get("basis"):
            raise RuntimeError(f"braid {braid['slug']} relationship {relationship_id} lacks question or basis")
        seen.add(relationship_id)
        frame_state = compact_relationship_state(frame_states.get(relationship_id))
        chapter_state = compact_relationship_state(chapter_states.get(relationship_id))
        before = (frame_state or {}).get("aspect")
        after = (chapter_state or {}).get("aspect")
        if "active_dialogue" in presence and not (before or after):
            raise RuntimeError(f"braid {braid['slug']} calls {relationship_id} active without an authored-window aspect")
        if before and after == before:
            transition = "continued"
        elif not before and after:
            transition = "entered"
        elif before and not after:
            transition = "left"
        elif before != after:
            transition = "changed"
        else:
            transition = "no_direct_dialogue"
        projected.append({**strand, "pair": catalog[relationship_id].get("pair") or [],
                          "tier_id": catalog[relationship_id].get("tier_id", ""),
                          "frame_state": frame_state, "chapter_state": chapter_state,
                          "dialogue_transition": transition})
    return {
        "frame": {"chart_id": frame.get("chart_id"), "date": frame.get("date")} if frame else None,
        "chapter": {"chart_id": chapter.get("chart_id"), "date": chapter.get("date")} if chapter else None,
        "strands": projected, "authored_on": authored_on, "review_on": review_on,
        "status": "current_window" if today.isoformat() < review_on else "review_due",
        "authority_boundary": "This is a dated rope overlap, not DNA: plotline, factual record and planetary relationship remain independent. Roles are authored interpretations; geometry is computed; strand count is never a score, vote, confidence measure or factual claim.",
    }


def load_saves():
    saves = []
    for p in glob.glob(os.path.join(VAULT, "01 - Events", "*.md")):
        n = os.path.basename(p)
        if not re.match(r"\d{4}-\d\d-\d\d", n):
            continue
        t = open(p, encoding="utf-8", errors="ignore").read(1500)
        f = fm(t)
        saves.append((n[:10], re.sub(r"^\d{4}-\d\d-\d\d-\d{4} - ", "", n[:-3]), f.get("subplot", ""), f.get("primary_plotline", "")))
    return saves


def build_braids(braids, events, items, saves, notes, cat, rooms_research, today, relationship_data):
    luns = [e for e in events if e["kind"] == "lunation"]
    seasons = [e for e in events if e["kind"] == "ingress" and e.get("season")]
    t = today.isoformat()
    out, braided = [], set()
    for b in braids:
        rids = set(b["research_ids"])
        eo_keys = set(b.get("executive_orders") or [])
        movement_ids = set(b.get("movement_ids") or [])
        braided |= rids
        rx = re.compile("|".join(b["keywords"]), re.I) if b["keywords"] else None
        beats = []
        per_day = defaultdict(list)
        for d, title, sub, pl in saves:
            if sub in b["subplots"] or pl in b["plotlines"]:
                per_day[d].append(title)
        for d, ts in per_day.items():
            beats.append({"date": d, "kind": "saves", "n": len(ts), "label": f"{len(ts)} X save{'s' if len(ts) > 1 else ''}", "titles": ts[:4]})
        seen = set()
        for it in items:
            if it["kind"] == "spike":
                continue
            hit = (
                bool(set(it.get("rids") or []) & rids)
                or bool({str(ref.get("eo_key", "")) for ref in (it.get("eo_refs") or [])} & eo_keys)
                or bool(it.get("movement_id") and it.get("movement_id") in movement_ids)
                or (it["kind"] in {"official", "eo_movement", "institutional_movement"} and rx is not None and rx.search(it["label"]))
            )
            key = (it["date"], it["label"][:80])
            if hit and key not in seen:
                seen.add(key)
                beats.append({"date": it["date"], "kind": it["kind"], "label": it["label"], "detail": it.get("detail", ""),
                              "rids": it.get("rids") or [], "path": it.get("path") or it.get("wb_path") or "", "record": it.get("record"),
                              "movement_id": it.get("movement_id", ""), "eo_refs": it.get("eo_refs") or [],
                              "entity_roles": it.get("entity_roles") or [], "stage_reached": it.get("stage_reached", ""),
                              "unresolved_stages": it.get("unresolved_stages") or [], "claim_limit": it.get("claim_limit", ""),
                              "next_receipt": it.get("next_receipt", ""), "clocks": it.get("clocks") or {}})
        for rid in b["research_ids"]:
            p = cat.get(rid)
            if p and p.get("evidence_cutoff"):
                beats.append({"date": str(p["evidence_cutoff"])[:10], "kind": "study", "label": "Our research: " + (rooms_research.get(rid, {}).get("title") or p["title"]),
                              "rids": [rid], "detail": "evidence through this date"})
        beats = [x for x in beats if re.match(r"\d{4}-\d\d-\d\d$", x["date"]) and WINDOW[0] <= x["date"] <= WINDOW[1]]
        beats.sort(key=lambda x: (x["date"], x["kind"], x["label"]))
        # sky touching each beat (within a day), strong events only
        sky_day = defaultdict(list)
        for e in events:
            if e["weight"] >= 3 and (e["kind"] != "transit" or e.get("chart") in b["charts"]):
                d0 = date.fromisoformat(e["date"])
                for k in (-1, 0, 1):
                    sky_day[(d0 + timedelta(days=k)).isoformat()].append(e["label"])
        for x in beats:
            x["sky"] = sorted(set(sky_day.get(x["date"], [])))[:3]
        # chapters
        chapters = []
        for i, lu in enumerate(luns):
            if lu["date"] > t:
                break
            end = luns[i + 1]["date"] if i + 1 < len(luns) else "9999"
            bs = [x for x in beats if lu["date"] <= x["date"] < end and x["date"] <= t]
            if not bs:
                continue
            sky = [e for e in events if lu["date"] <= e["date"] < end and e["kind"] != "lunation" and
                   ((e["kind"] != "transit" and e["weight"] >= 4) or (e["kind"] == "transit" and e.get("chart") in b["charts"] and e["weight"] >= 3))]
            se = last_before(seasons, lu["date"])
            chapters.append({"label": lu["label"], "date": lu["date"], "end": end, "sign": lu.get("sign"), "phase": lu.get("phase"),
                             "eclipse": lu.get("eclipse"), "season": (se["sign"] + " season") if se else "",
                             "saves": sum(x.get("n", 0) for x in bs), "beats": bs,
                             "sky": [{"date": e["date"], "label": e["label"], "kind": e["kind"]} for e in sky][:8]})
        # rhythm: where the story gets loud
        by_sign = defaultdict(lambda: {"new": 0, "full": 0})
        by_season = Counter()
        for c in chapters:
            if c["sign"]:
                by_sign[c["sign"]][c["phase"] or "new"] += c["saves"]
            by_season[c["season"]] += c["saves"]
        loud = sorted(chapters, key=lambda c: -c["saves"])[:5]
        chart_hits = Counter(s["label"] for c in chapters for s in c["sky"] if s["kind"] == "transit")
        months = Counter(x["date"][:7] for x in beats if x["kind"] == "saves" for _ in range(x.get("n", 1)))
        ahead = [x for x in beats if x["date"] > t][:12]
        sky_ahead = [{"date": e["date"], "label": e["label"], "kind": e["kind"]} for e in events
                     if t < e["date"] <= (today + timedelta(days=200)).isoformat() and
                     ((e["kind"] in ("eclipse", "ingress") or (e["kind"] in ("aspect", "conjunction", "station") and e["weight"] >= 4)) or
                      (e["kind"] == "transit" and e.get("chart") in b["charts"]))][:16]
        filed = [n["id"] for n in notes if b["slug"] in (n.get("braids") or []) or
                 (set(n.get("plotlines") or []) & set(b["plotlines"])) or (set(n.get("research_ids") or []) & rids)]
        past = [x for x in beats if x["date"] <= t]
        relationship_field = relationship_field_for_braid(b, relationship_data, today)
        factual_beats = [x for x in past if x["kind"] not in {"saves", "return_gate", "eo_return_gate", "institutional_return_gate"}]
        institutional_receipts = [x for x in past if x["kind"] in {"official", "eo_movement", "institutional_movement"}]
        movement_records = [x for x in past if x.get("movement_id")]
        eo_lineage_records = [x for x in movement_records if x.get("eo_refs")]
        readiness = {
            "factual_timeline": "present" if factual_beats else "empty",
            "research_custody": "present" if b["research_ids"] else "empty",
            "institutional_receipts": "present" if institutional_receipts else "none_attached",
            "movement_lineage": "attached" if movement_records else "none_attached",
            "eo_lineage": (
                "attached" if eo_lineage_records else
                "awaiting_adjudicated_receipt" if b.get("executive_orders") else
                "not_declared"
            ),
            "authored_overlap": relationship_field["status"],
            "factual_beat_count": len(factual_beats),
            "institutional_receipt_count": len(institutional_receipts),
            "movement_lineage_record_count": len(movement_records),
            "eo_lineage_record_count": len(eo_lineage_records),
            "review_on": relationship_field.get("review_on", ""),
            "boundary": "These are categorical custody states, not a maturity score or comparative grade.",
        }
        out.append({**b, "beats_count": len(beats), "saves": sum(x.get("n", 0) for x in beats),
                    "relationship_field": relationship_field, "readiness": readiness,
                    "studies": [{"rid": r, "title": rooms_research.get(r, {}).get("title") or (cat.get(r) or {}).get("title", r),
                                 "cutoff": str((cat.get(r) or {}).get("evidence_cutoff") or "")[:10]} for r in b["research_ids"] if r in cat],
                    "first": past[0]["date"] if past else "", "last": past[-1]["date"] if past else "",
                    "chapters": chapters, "rhythm": {"by_sign": by_sign, "by_season": by_season.most_common(),
                    "loud": [{"label": c["label"], "date": c["date"], "saves": c["saves"], "eclipse": c["eclipse"]} for c in loud],
                    "chart_hits": chart_hits.most_common(6)},
                    "months": sorted(months.items()), "ahead": ahead, "sky_ahead": sky_ahead, "filed": filed})
    unbraided = sorted(r for r, e in rooms_research.items() if r not in braided and e.get("room") != "thesis")
    return out, unbraided


# ── now ────────────────────────────────────────────────────────────────────────────
def now_block(events, today, readings):
    by_date, by_ingress = readings
    t = today.isoformat()
    luns, seasons = chapters(events)
    se = last_before(seasons, t)
    ch = last_before(luns, t)
    nxt = next((e for e in luns if e["date"] > t), None)
    ecl_next = next((e for e in events if e["kind"] == "eclipse" and e["date"] > t), None)
    plot = Counter()
    if ch:
        for p in glob.glob(os.path.join(VAULT, "01 - Events", "*.md")):
            n = os.path.basename(p)
            if re.match(r"\d{4}-\d\d-\d\d", n) and ch["date"] <= n[:10] <= t:
                pl = fm(open(p, encoding="utf-8", errors="ignore").read(1200)).get("primary_plotline", "")
                if pl and pl != "Other":
                    plot[pl] += 1
    soon = [e for e in events if t <= e["date"] <= (today + timedelta(days=45)).isoformat() and e["weight"] >= 3 and e["kind"] != "transit"]
    return {"today": t,
            "season": {"label": se["sign"] + " ingress", "date": se["date"], "reading": by_ingress.get((se["date"][:4], se["sign"]))} if se else None,
            "chapter": {"label": ch["label"], "date": ch["date"], "reading": by_date.get(ch["date"]), "eclipse": ch.get("eclipse")} if ch else None,
            "next": {"label": nxt["label"], "date": nxt["date"], "reading": by_date.get(nxt["date"])} if nxt else None,
            "next_eclipse": {"label": ecl_next["label"], "date": ecl_next["date"]} if ecl_next else None,
            "plotlines": plot.most_common(8), "sky_soon": soon[:14]}


def build(today=None, refresh_sky=False):
    today = today or date.today()
    wb = workbench()
    events = sky_events(refresh_sky)
    readings = readings_index()
    items = research_items(wb, today)
    days = match(events, items, readings)
    notes = filed_notes()
    filed_dates = defaultdict(list)
    for n in notes:
        for d in n["dates"]:
            filed_dates[d].append(n["id"])
    for d in days:
        d["filed"] = filed_dates.get(d["date"], [])
    cat = {}
    rooms_research = {}
    if wb:
        cat = {p["research_id"]: p for p in json.load(open(os.path.join(wb, "RESEARCH DESK CATALOG.json"), encoding="utf-8"))["packages"]}
        rooms_research = json.load(open(os.path.join(wb, "RESEARCH ROOMS.json"), encoding="utf-8")).get("research", {})
        bf = os.path.join(wb, "RESEARCH BRIEFS.json")
        if os.path.isfile(bf):
            for rid, b in json.load(open(bf, encoding="utf-8")).get("briefs", {}).items():
                if rid in rooms_research and b.get("plain_title"):
                    rooms_research[rid] = {**rooms_research[rid], "title": b["plain_title"]}
    relationship_data = load_relationship_history()
    braids, unbraided = build_braids(load_braids(), events, items, load_saves(), notes, cat, rooms_research, today, relationship_data)
    braid_comparisons = build_braid_comparisons(load_braid_comparisons(), braids, today)
    overlap_ledger = attach_overlap_history(braids, braid_comparisons, load_overlap_ledger(), today)
    story_rooms = build_story_rooms(load_story_rooms(), braids, braid_comparisons, today)
    review_hearings = build_review_hearings(load_review_hearings(), overlap_ledger, relationship_data, today)
    data = {"schema": "f250.mundane-crossovers/v1", "built": today.isoformat(), "window": list(WINDOW),
            "about": "Where astrology crosses into political analysis. The sky is read archetypally; the research side is facts only.",
            "now": now_block(events, today, readings), "days": days, "filed": notes, "overlaps": overlap_files(),
            "braids": braids, "braid_comparisons": braid_comparisons, "story_rooms": story_rooms,
            "review_hearings": review_hearings, "overlap_ledger": overlap_ledger, "unbraided": unbraided,
            "counts": {"sky_events": len(events), "research_dates": len(items), "crossover_days": len(days),
                       "strong_days": sum(1 for d in days if d["score"] >= 8), "filed": len(notes),
                       "braids": len(braids), "braid_comparisons": len(braid_comparisons),
                       "story_rooms": len(story_rooms), "review_hearings": len(review_hearings),
                       "unbraided": len(unbraided)}}
    return data


def render(data):
    tpl = open(TEMPLATE, encoding="utf-8").read()
    lite = dict(data)
    return tpl.replace("__DATA__", json.dumps(lite, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/"))


NOTE_TEMPLATE = """---
type: mundane_crossover
title: "{title}"
date: {date}
dates: [{date}]
filed_by: {who}
status: filed
sky: [{sky}]
research: [{research}]
plotlines: [{plotlines}]
research_ids: [{rids}]
season: "{season}"
chapter: "{chapter}"
---

# {title}

## The story (research side — facts only)

{story}

## The sky

{skytext}

## The archetypal reading

(What the sky's images say about this story: the archetypes in play, the mood of the chapter,
what the pairing suggests. Interpretive and playful — this is a reading, not a proof.)

## Threads to follow

- (storylines, dates or charts worth watching next)

## Looking back

(Optional, added later: how the story and the image kept talking to each other.)
"""


def candidates(data, n, today):
    lo = (today - timedelta(days=14)).isoformat()
    hi = (today + timedelta(days=14)).isoformat()
    pool = [d for d in data["days"] if lo <= d["date"] <= hi and not d["filed"]]
    pool.sort(key=lambda d: (-d["score"], d["date"]))
    print(f"MUNDANE CROSSOVER CANDIDATES · {today} · window {lo} → {hi} · {len(pool)} unfiled days")
    print("File the meaningful ones as notes in 03 - Astrology/Mundane Astrology/Crossovers/ (see README there).")
    for d in pool[:n]:
        print("\n" + "=" * 78)
        print(f"{d['date']}  score {d['score']}   {d['chapter']}   {d['season']}")
        print("SKY:")
        for s in d["sky"][:4]:
            print(f"   - {s['label']}  ({s['kind']}, {s['date']}{', reading: ' + s['reading'] if s.get('reading') else ''}{', resonates' if s.get('resonates') else ''})")
        print("RESEARCH (facts):")
        for r in d["research"][:5]:
            where = r.get("path") or r.get("wb_path") or ("rids: " + ", ".join(r.get("rids", [])) if r.get("rids") else "")
            print(f"   - [{r['kind']}] {r['label']}  · {r['detail'][:120]}  · {where}")
        slug = re.sub(r"[^a-z0-9]+", "-", (d["sky"][0]["label"] + " " + d["research"][0]["label"]).lower()).strip("-")[:70]
        print(f"NOTE PATH: 03 - Astrology/Mundane Astrology/Crossovers/{d['date']} — {slug}.md")


def main():
    args = sys.argv[1:]
    today = date.today()
    data = build(today, refresh_sky="--sky" in args)
    if "--candidates" in args:
        i = args.index("--candidates")
        n = int(args[i + 1]) if i + 1 < len(args) and args[i + 1].isdigit() else 5
        candidates(data, n, today)
        return 0
    js = json.dumps(data, ensure_ascii=False, indent=0) + "\n"
    page = render(data)
    check = "--check" in args
    changed = []
    for path, content in ((OUT_JSON, js), (OUT_HTML, page)):
        cur = open(path, encoding="utf-8").read() if os.path.isfile(path) else None
        def strip(t):
            value = re.sub(r"\s*<!-- F250-DARKMODE-START -->.*?<!-- F250-DARKMODE-END -->\s*", "\n", t or "", flags=re.S)
            return re.sub(r"\s*<!--F250-INTERP-START-->.*?<!--F250-INTERP-END-->\s*", "\n", value, flags=re.S)
        if strip(cur) != strip(content):
            changed.append(os.path.basename(path))
            if not check:
                fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), prefix=".mundane-", suffix=".tmp")
                with os.fdopen(fd, "w", encoding="utf-8") as f:
                    f.write(content)
                os.replace(tmp, path)
    c = data["counts"]
    msg = f"{c['crossover_days']} crossover days ({c['strong_days']} strong) · {c['filed']} filed · {c['story_rooms']} story rooms · {c['review_hearings']} review hearing · {c['braids']} braids ({c['unbraided']} studies on no braid) · {c['sky_events']} sky events · {c['research_dates']} research dates"
    if check:
        print(f"Mundane Astrology: {'would change' if changed else 'current'} ({msg})")
        return 1 if changed else 0
    print(f"✓ Mundane Astrology.html ({msg})" if changed else f"Mundane Astrology.html: unchanged ({msg})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
