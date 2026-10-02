---
title: Mundane Astrology — how crossovers work
type: method
status: live
updated: 2026-10-03
design_lens: "[[Braid Constitution — Rope, Not DNA]]"
---

# Mundane Astrology — where the sky meets the story

Design lens: [[Braid Constitution — Rope, Not DNA]].

This is the section where astrology crosses into political analysis (Katie, 2026-10-03; DR-095). In the app it is its own menu group: **Overview**, **Story Braids**, **Crossover Timeline** and **Filed Crossovers**, plus Threads, the Prediction Scorecard and the Sky Watchlist.

**The spirit.** Astrology here is *archetypal*. The sky offers images and themes for reading what is happening: who is playing which part, what the mood of the chapter is, what a pairing suggests. It is a fun, private think-tank, not a courtroom. Crossover notes are readings, not proofs, and nobody grades them. They can be bold, playful and speculative. (Katie: "astrology is inherently archetypal and that's what we're focused on… this is a fun private research think-tank.")

**The one rule that stays.** The research side is facts only and stays astrology-free. A crossover note quotes or summarizes the research, citing the file path, but nothing astrological is ever written into a research file, a Workbench study or the Research Library. The two lanes meet here, on dates.

## How a crossover is found

`99 - Templates/build_mundane_astrology.py` runs every night inside the vault refresh (Grok's nightly). It lines up:

- **Sky events** (computed with the Swiss Ephemeris): lunations and eclipses; the Sun's season ingresses and outer planets changing sign; stations; exact aspects between Mars and the outer planets; conjunctions of any two planets (the conjunction charts); and Jupiter through Pluto hitting the key charts (the U.S. chart and the entity charts for Congress, the Supreme Court, the White House, Treasury, the Fed, the SEC, the CFTC, the OCC, the FDIC, DOJ, the FBI, DHS and Defense).
- **Research dates**, facts only: official actions (Official Records, Executive Orders, dated records, studies of one dated official action); deadlines on the clock (hub dates, follow-up return dates); dated rows in study timelines; and spikes in Katie's X saves on a storyline.

Anything within a day of each other becomes a **crossover day**. A day scores higher when the sky event is bigger (eclipse, season ingress, outer-planet aspect, a key chart hit) and the research is weightier. A key-chart hit glows **gold** when the story itself names that institution. The strongest days are marked ✦✦ or ✦✦✦.

## Filing a crossover

Grok files them itself every night (Katie's choice). Any chat, or Katie, can file one too. Every day page in the app shows the template, and so does `python3 "99 - Templates/build_mundane_astrology.py" --candidates 5`.

- **Where:** `03 - Astrology/Mundane Astrology/Crossovers/`
- **Name:** `YYYY-MM-DD — <short title>.md`
- **Frontmatter:** `type: mundane_crossover`, `title`, `date`, `braids` (optional, the braid slugs it belongs to), `dates` (all dates the crossover spans), `filed_by` (grok, claude, codex or katie), `status` (`filed`, or `looking back` once a reflection is added), `sky`, `research`, `plotlines`, `research_ids`, `season`, `chapter`.
- **Sections:**
  1. **The story (research side — facts only):** what happened, with file paths.
  2. **The sky:** the events, with exact times or degrees where useful.
  3. **The archetypal reading:** the heart of the note. Use Katie's own language and readings where they exist (the season and lunation readings, `Saturn-Neptune conjunction in Aries.md`, the 2020s Thesis).
  4. **Threads to follow:** what to watch next.
  5. **Looking back** (optional, later): how the story and the image kept talking to each other.
- **One note per crossover.** If a later date belongs to the same story, add it to `dates` and extend the note.
- **Up to three a night for Grok,** strongest first, favoring days that touch tonight's saves. Skip days where the research side is only a follow-up reminder.

## Story braids — follow a story through its astrological timeline

A braid is one storyline followed through time, such as stablecoin law, Iran and Hormuz, or the courts and the law (Katie, 2026-10-03, DR-096). Each braid is a file in `Braids/`:

- **Frontmatter:** `type: story_braid`, `title`, `question`, `subplots` (the X-feed subplots it follows), `plotlines` (optional whole plotlines), `keywords` (regular expressions that pull in official actions), `research_ids` (its studies), `executive_orders` (optional exact EO keys whose governed lineage records belong to the story), `movement_ids` (optional exact adjudicated institutional records that belong to the story without claiming EO descent), `charts` (the key charts to watch, by their Entity Theory names), and `status`. An interpreted rope overlap also names `relationship_frame`, `relationship_chapter`, `relationship_authored_on`, `relationship_review_on` and optional `relationship_strands`.
- **Body:** `## The braid so far`, the story in a few sentences and then the archetypal reading of its rhythm.

Each night the builder assembles every braid into a page with these parts:

- **Beats:** your saves on its subplots, the official actions, deadlines and timeline rows tied to its studies, and the dates its studies were written.
- **Chapters:** the beats grouped by lunar chapter and season, with the strong sky in each chapter.
- **Relationship braid:** authored relationship roles joined to the computed governing-ingress and current-lunation states. Roles are `lead_mechanism`, `co_mechanism`, `supporting_context`, `outcompeted` or `unresolved`; presence is `inherited_substrate`, `active_dialogue` or `seed_echo`. Several strands may be correct because they do different jobs. Strand count is never a score or vote.
- **Attention rhythm:** which lunar chapters and seasons contain more of Katie's saved posts. This is an inventory of attention, not evidence, event intensity or institutional change.
- **Charts lit up:** the transits to its key charts during its chapters.
- **Ahead:** its coming deadlines, plus the sky still to come.

**Keeping braids growing.** Every new study goes on its braid(s) when it is filed (step 7 in the Workbench `RESEARCH ROOMS — Filing Guide.md`). The Story Braids page lists any study on no braid. A crossover note can name its braids with `braids: [slug]`. Grok refreshes one braid's "The braid so far" each night: the braid with the newest beats, or the one whose summary is oldest.

An EO key adds no beat by itself. The Workbench Movement Registry must first
attach a completed, primary-source-adjudicated movement to one exact Chronicle
EO directive path. The braid then receives that dated movement, its reached
state and before→after transition. Executive direction, publication,
implementation, operation and effect remain separate facts.

A planetary relationship is never assigned by keyword or resemblance. An
authored strand must name its distinct job in the factual story and its mode of
presence. The builder supplies factual geometry and ordered state change from
`planetary_relationship_history.json`; it does not decide which relationship
owns a storyline. A braid with no authored strands says so explicitly while
retaining its factual timeline.

**The braid is rope, not DNA.** The factual plotline, social-attention route and
planetary relationship remain independent objects. An authored overlap belongs
to one exact ingress and lunar chapter and carries a review date. When that
window turns, the reading remains historical and becomes review-due; the same
relationships are never silently attached to the new chart. User-facing roles
are lead strand, companion strand, background strand, outcompeted strand or
unresolved strand. These describe one reading, not permanent plot ownership or
causal machinery.

`Braid Overlap Ledger.jsonl` preserves each authored braid window and rope
comparison as an append-only snapshot. A current record must match its authored
file exactly. At the lunar review hearing it becomes historical with explicit
retained, revised, released, outcompeted or unresolved dispositions; a new
window is authored separately. The ledger creates no factual claim, planetary
ownership, evidence credit or Forecast Ledger call.

## Living Story Rooms — watch a story become real

Living Story Rooms are guided routes through several independently owned
braids. They live inside the Mundane Astrology view at `#/rooms`; they are not a
new research store, shell tab or super-braid. `Living Story Room Contract.md`
owns the replay rules and `Story Rooms/*.md` owns each tour's question,
membership and authored guide.

The flagship **Money's New Pipes**, **Rebuilding the Federal Machine** and
**Capacity or Spectacle** rooms each replay one lunar chapter at a time. At each
historical cutoff they display separate factual-record, Research-knowledge,
institutional-movement, Executive Order, attention, computed-sky,
authored-overlap, unresolved-gate and later-review lanes. Its “what changed”
counts are categorical additions in that chapter, never a score or proof of
progress. The Federal room also projects exact typed entity roles and
court/remedy records without inferring either from keywords. Capacity keeps
plan, funding, delivery, acceptance and operation separate.

The internal `#/tour` route gives a three-minute explanation of the three rooms
without creating a new shell tab. Review packets in `Review Hearings/` are
fail-closed. Before their date they remain scheduled with pending snapshots; on
the date the builder may mark them review-due but cannot choose a disposition or
author the next overlap.

## What lives here and what doesn't

- New crossover notes live here.
- The earlier overlap work stays where it is: `Astrology Files/Mundane Story Overlaps/` and `Astrology Files/Money x Sky/`. It is shown on the Filed Crossovers page.
- Computed data: `99 - Templates/mundane_sky_events.json` (the sky; rebuild with `--sky`) and `99 - Templates/mundane_crossovers.json` (the matches). The view is `04 - Synthesis/Cross-cuts/Mundane Astrology.html`.
