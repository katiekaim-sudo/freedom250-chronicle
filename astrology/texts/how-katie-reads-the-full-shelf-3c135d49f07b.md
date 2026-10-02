---
title: How Katie reads — the full shelf
type: method
created: 2026-08-13
updated: 2026-08-30
purpose: Grok boot for chart work. The Aries 2026 test showed the engine and old notes skip layers she already built. This file names the shelf. It does not replace Reading the Charts.
reads_with:
  - 00 - Index/Reading the Charts — START HERE.md
  - 00 - Index/Mundane Astrology Reference — Katie's Method.xlsx
  - _AI-Context/BOOT — Chart Reading.md
  - 99 - Templates/Chart reading authoring template.md
---

# How Katie reads — the full shelf

The on-ramp is still [[Reading the Charts — START HERE]]. The **atomic lookups** live in `00 - Index/Mundane Astrology Reference — Katie's Method.xlsx`. That workbook was built on purpose. A reading that only uses `mundane_dossier.py` output is a thin slice.

Pass 1 is the chart. Pass 2 is the record. Pass 3 is the rhyme. Do not mix them.

## The workbook is the method drawer

Open the xlsx. Every tab is a technique she saved. Use it or say why you didn't.

| Tab | What it is | Skip cost (Aries 2026 test) |
|---|---|---|
| **README — Doctrine** | Whole Sign, D.C., root, no scores | — |
| **Planets / Signs / Houses** | Actor, field, arena | — |
| **Derivative Houses** | 144 turns | Dossier only prints the 10th turn. Turning **the root** (2nd = 1st) was the better sentence. |
| **Aspects** | **The dialogue.** Orbs. Huber colour. **Silence = signal.** Parallels on every chart. | Engine used a flat 6°. Workbook orbs differ (conj 8, sextile 5, square 7, trine 7). Mercury–Jupiter at 6.74° is a talk. |
| **Aspect Figures** | Named Huber figures as one unit | Bowl/bundle must be named before the parts. |
| **Aspect Registers** | Waxing vs waning of the *same* aspect | Applying/separating is not enough; the cycle half matters. |
| **Apex Planets** | Who carries a T-square / yod | Only if a figure exists. |
| **Lunar Phases** | Pessin lifecycle of *one* story | — |
| **Moon Families** | Band **and** mood; 273d lineage | Dossier prints the band name. It does not print mood or neighbors. |
| **Eclipses** | Supercharge; Metonic; Zain path | No eclipse *inside* Aries 2026 validity. Winter eclipses can still be burning. |
| **Dignities** | Sign-condition lookup | Dossier says “exalted.” It does not say **0.23° from the exaltation degree**. Tab lists modern outer domiciles; **prose / `phases.py` refuse them** — classical only. |
| **Midpoint Pairs / Points** | Munkasey mundane | Dossier only prints pictures on Sun/Moon/ASC/MC ≤1°. |
| **Lots** | Fortune & Spirit chiefly | Unused until this pass. |
| **Profections** | National year-house (secondary) | Ingress ladder leads. Still compute the US year-house. **Flips on the birthday (2 July), not on the solstice.** Age 249 / 10th until 2 Jul 2026; then 250 / 11th. Workbook 2026 row is the 11th year. |
| **Planetary Nodes** | Jones; Saturn NN = wars begin | Dossier prints hits ≤2.5°. Empty is a finding. |
| **Planetary Cycles** | Synodic eras (20 / 36 / 127 yr…) | **The outer hue.** A 3-month chart does not invent a new Pluto. |
| **Transits & Progressions** | Nested ladder, not daily | — |
| **Chart Shapes** | Gestalt first | Aries 2026 is a **bowl** (~160°). |
| **Modifiers** | Sect, retro, angular, combust | — |
| **National Charts** | Locked US + Gemini-rising secondary | Domestic-money events may want the Gemini chart as a second overlay. Overlay clock = **July 2 1776 ~2:13 AM LMT**, not Zain’s July 4 2:13. |
| **Sabian 360** | Degree caption. `floor(deg)+1`. Jones images. | Behind the scenes, after structure. Both poles. Not on quarters (DR-023). |
| **Assembler** | Demo join for one ingress | Demo is Cancer, not a live Aries assembler. |

Sabian JSON is **not** to be invented. Look up the workbook `Sabian 360` tab. A fuller personal sheet is optional play, not a missing deliverable (DR-062).

## Three layers the old notes starved

### 1. Aspects = who is talking to whom

The plot is the dialogue. Name **speakers**, not just glyphs.

Planets keep their archetypal motivations, but they do not own fixed plots.
**Relationships carry arcs.** Read the direct Aspect as the present scene, the
synodic phase as that scene's location within the longer relationship arc, and immediate motion as its
delivery. A chart is one frame in that history. Retrograde motion may separate
and reapply, reopen a phase sector, or create repeated exact passes, but every
later encounter has a distinct time identity and inherits what happened before
it. Every ingress supplies a frame; only Aries or a lawfully succeeding
non-Aries ingress changes the governor. No ingress resets the relationship.

- Conjunction: they become one motive.
- Square: friction that forces action (the braid tightens).
- Opposition: two truths across a table.
- Trine: open channel; can be lazy.
- Sextile: an opening that must be taken.
- **No aspect:** they do not confer directly in this frame. That is political.
  Their synodic relationship continues as background or between chapters;
  `unaspected` means separate immediate tracks, not that the longer relationship
  ceased to exist.

**Plots are relationship braids (DR-069).** Several pairs may be correct at
once because they are performing different jobs, not because symbolic matches
stack into proof. Assign every proposed strand a role — `lead mechanism`,
`co-mechanism`, `supporting context`, `outcompeted`, or `unresolved` — and a
presence mode — `inherited substrate`, `active dialogue`, or `seed echo`.
Compare the braid from one governed checkpoint to the next: what continued,
what changed phase or direct Aspect, what separated/reapplied, and what the new
chart foregrounded. A useful hypothesis is outer condition → faster carrier →
lunation/eclipse visibility, but test it; never force it into a fixed hierarchy.

Use **workbook orbs**, not a single engine number. Note applying vs separating, and the waxing/waning register.

**Greer binaries** (the usual political braid): Sun/Moon · Venus/Mars · Jupiter/Saturn · Uranus/Neptune. If a binary is silent, say so. The braid may be coming from another talk (e.g. Venus–Jupiter instead of Jupiter–Saturn).

**Declination** is on the Aspects tab: parallel ≈ conjunction; contra-parallel ≈ opposition. Read it on every chart. A longitude silence can still be a declination talk (Aries 2026: Jupiter contra-parallel Pluto 0.12°).

### 2. Sabians = the degree’s picture

Fifth layer. Not motivation, tools, stage, or dignity. A frozen scene.

- Lookup: **symbol number = floor(degrees-in-sign) + 1**. 0°00′–0°59′ Aries = Aries 1.
- After the structure. Caption, not cause. Both poles. Drop it if it only repeats the architecture.
- NM / FM / eclipse / ingress points. **No Sabian on quarter moons** (DR-023).
- Source: workbook `Sabian 360`. Jones line.

### 3. Outers = hue, not weather

Uranus ~7 years/sign, Neptune ~14, Pluto ~20, Saturn–Neptune ~36, Uranus–Pluto ~127. They are the **standing character** of a decade. A cardinal ingress does not recast them. You watch them *progress* — stations, sign ingresses, exact talks with each other.

In a 3-month chart:

- The outers are the room’s color. The inners walk through it.
- Test outer conjunctions by **co-presence window**, not one exact day (DR-003).
- The rare exception: an outer **changes sign** inside the validity (Aries 2026: Uranus leaves Taurus for Gemini on April 25). That is a character change mid-season. Name it.

Saturn is social, not outer, but his cycles with Neptune/Pluto belong on this shelf.

## Moon Families (built; often half-used)

Two layers, both already in the vault:

1. **Band / mood** (workbook + `build_threads.py`): Threshold 0–8, Great Harvest 8–16, Quiet Sowing 16–24, Eclipse Storm 24–30.
2. **True lineage** (`build_moon_lineages.py`): same degree at ~273 / 546 / 819 days. A lunation is one beat of a longer story.

“Quiet” means no Greer hit on the *ingress*. It does not mean empty. Always also check the locked US natal (≤1° to name).

## State-transition pass (DR-064)

This pass comes **after** the chart has been heard as a whole. It does not
replace the root, dialogue, mundane translation, or both-poles reading. It asks
the Freedom 250 question in a comparison-safe form: **which legitimate decision
right may be moving, from whose hands toward whose, through what mechanism, and
how mature is that change?**

The thesis is a lens, not the answer. Preserve **proposed / authorized /
effective / operating / contested / reversed / failed / unchanged** as distinct
states. Name the constructive pole, shadow pole, and continuity case. Then name
what synchronization across the seven arcs and what Attention / Official /
Entity evidence would make the watch line up, miss, or remain unresolved.

For prospective work, freeze the State Transition Watch as a separate hashed
addendum. Never revise an earlier baseline to make it look as though the lens
was present before it was. The governed output shape is
`99 - Templates/Chart reading authoring template.md`.

## Minimum compute for one ingress (future Grok)

1. Bones: positions, dignity **and exaltation degree**, houses, ruler, **root**, America, sect.
2. Gestalt: chart shape, then the figure (if any).
3. Dialogue: full web at workbook orbs, silences, Greer binaries, declination, applying/separating.
4. Overlay: US natal (Philly, Sag 10°44′) hard hits ≤1° to *name*; Gemini-rising only if the story is domestic money (**July 2 ~2:13 AM LMT**, not Zain July 4).
5. Lots Fortune & Spirit. Profection year-house (secondary) — **birthday-strict** (US flips 2 July).
6. Derivative from the **root**, not only from the 10th.
7. Outer hue + any sign-change inside the window.
8. Opening New Moon (may sit *before* the ingress). Then each NM/FM: own ASC/chain, Greer hits, US-natal hits, family **mood + 273d neighbors**.
9. Sun-contacts as a clock hand, **not** a topic filter.
10. Sabians last, on points that earned a caption.

Never write a degree from memory. Never score a chart. Never start with today’s transits.
