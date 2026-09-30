---
title: Ongoing Planetary World — Design Note
date: 2026-08-31
updated: 2026-09-24
status: first_instrument_built_context_audit_recorded_not_shipped
artifact_role: durable design note
project: Freedom 250 Observatory
authority_boundary: Workbench design record only; not live-vault doctrine, implementation authority, a storyline finding, evidence, or forecast permission.
---

# Ongoing Planetary World — Design Note

## Why this note exists

Katie wants planetary motion to become much more prominent in the Freedom 250 Observatory. The governing insight is that astrology is not a library of static charts. It is an **ongoing planetary world**: a complicated calendar of bodies and relationships that never returns to the exact same total configuration.

This note preserves the shared conceptual understanding before implementation begins. It authorizes no build or promotion by itself.

## Governing language

> Position tells us where the actor is. Relationship tells us whom it is speaking with. Motion tells us what the actor and relationship are doing now.

> A chart is one requested frame from continuous planetary and relationship histories.

> A return is a rhyme, not a replay.

The planets repeatedly form familiar relationships, but each encounter occurs inside a configuration that has continued to change. Returning to a degree does not return the world to the same moment. Chronological history never rewinds.

## Core model

```text
ONGOING PLANETARY WORLD
│
├── Individual planetary journeys
│   ├── solar phase and visibility cycle
│   ├── longitude direction and speed
│   ├── station, retrograde, and shadow arcs
│   └── declination journey
│
├── Continuous relationship histories
│   ├── synodic phase
│   ├── applying / perfection / separation
│   ├── retrograde reapplication
│   ├── pass identity
│   └── parallel / contraparallel history
│
├── Governing mundane frames
│   ├── ingress
│   ├── lunation
│   └── eclipse
│
└── Independent world record
    ├── political events
    ├── developing storylines
    └── prospective or retrospective comparison
```

An ingress does not create the planetary world. It opens a governing frame within a world already moving. A lunation can time or expose a development inside that frame. An eclipse can charge a longer development. None of them resets an existing planetary relationship.

## The three motion lanes

### 1. Individual longitudinal motion

Every planet has its own characteristic relationship to the Sun and its own native speed range. Motion must be evaluated relative to that body, never by comparing raw degrees per day across unlike planets.

Required factual states include:

- direct, stationing retrograde, retrograde, stationing direct;
- signed longitude speed;
- body-relative tempo such as unusually slow, typical, or unusually fast;
- accelerating or decelerating;
- exact station time and a body-specific functional station corridor;
- distance in time and longitude from the next reversal;
- sign ingress and egress;
- solar phase and visibility state where relevant.

Mercury and Venus especially require their complete solar cycles, including superior and inferior conjunctions, elongation/visibility phases, station arcs, and shadow periods.

### 2. Relationship motion

An aspect is not only a geometry at one moment. It is a developmental encounter with history.

Required factual states include:

- directed elongation from the slower body to the faster body;
- waxing or waning synodic direction;
- relative angular speed;
- applying, exact, separating, or reapplying;
- entry into and exit from the active aspect corridor;
- first, second, third, or later pass identity;
- station or retrograde reversal that reopens the relationship;
- the ordered events that occurred between encounters.

The phrase “Mercury square Saturn” is insufficient without knowing which pass it is, whether Mercury is slowing or stationing, whether the aspect will reopen, and what the earlier encounter already carried.

Motion may support a watch expectation that an astrological process remains open. It does not by itself prove that a political storyline is unfinished. The independent political record determines what actually returns, changes, resolves, or fails to recur.

### 3. Declination motion

Declination is a second continuous coordinate and relationship system, not a small modifier beside longitude.

Required factual states include:

- north or south declination;
- northbound or southbound motion;
- declination speed and acceleration;
- approach to and departure from a declination turn;
- celestial-equator crossing;
- out-of-bounds entry and return in bounds;
- parallel or contraparallel applying, exact, separating, and reapplying;
- pass identity for repeated declination contacts.

A longitudinal silence may still contain a tightening declination relationship. A longitude aspect may be separating while its declination relationship is still perfecting. Both channels must remain visible without being collapsed into one vote.

## Retrograde and shadow arcs

A retrograde period is a complete arc:

```text
shadow entry
    → first direct passage
    → deceleration
    → retrograde station
    → return passage
    → direct station
    → final passage
    → shadow exit
```

The exact retrograde dates alone omit the first and third chapters. Political or institutional subjects may first appear during the pre-shadow, be revised or reopened during the retrograde, and receive an operative resolution only after the final direct passage. This is an interpretive watch structure, not an automatic event forecast.

## Slow cycles and nested political stories

The Saturn–Neptune conjunction is the reference example supplied by Katie. The pair approached closely more than once but perfected only once. The exact conjunction is the seed-point; the prolonged approach is the seedbed in which that seed was prepared. Because the planets move slowly, the formation and development belong to a much larger generational timeframe than the exact date.

Faster cycles, ingresses, lunations, eclipses, and inner-planet passages unfold inside that outer-planet hue. They may describe smaller episodes through which the larger generational relationship becomes visible. Repeated symbolic participation does not create additional evidence votes, prove causality, or make a literal outcome certain.

## Interpretation and evidence boundary

Greater astronomical specificity should make real political correspondences easier to recognize without forcing them. Comparison can ask whether an event belongs to:

- preparation or approach;
- first emergence;
- exact perfection;
- reversal or reconsideration;
- repeated encounter;
- dissemination;
- separation or release;
- apparent closure followed by reapplication.

If chronology does not fit, leave the event unmatched. Motion refines the question and the watch window; it does not manufacture correspondence.

Preserve the existing fences:

- event capture remains independent of astrology;
- symbolic correspondence is not factual evidence;
- one relationship appearing through several techniques is not several votes;
- no automatic storyline ownership, causal claim, score, or forecast confidence;
- compute all motion facts, narrate only what earns narration;
- a literal event claim in a literal window remains a separate Forecast Ledger act.

## Orrery bridge

### Sentient Sun provenance

The former Sentient Sun Orrery is preserved at:

`[local-path-removed] Sun/_archive/product_history/2026-07-25-decision-164/orrery/`

Decision 164 retired the former implementation; the current Sentient Sun app shows Orrery only as a future room. Treat the archived implementation as inspectable design and engineering provenance, not as active Sentient Sun authority.

Structurally reusable features include:

- living heliocentric Space View;
- geocentric Earth View;
- animated two-seat morph between the two frames;
- exact engine anchor for a frozen chart moment;
- live sky, go-to-date, previous/next UTC-day, and press-and-hold stepping;
- separation of scenery/display ephemeris from chart-grade calculation authority;
- drag, zoom, label collision handling, and direct body-to-label connectors;
- self-contained assembler pipeline and fail-loud bind assertions;
- per-body profile/cast/dossier interaction patterns.

Freedom 250 must reuse only structure, interaction, and generic visual mechanics. No private chart identity, person-specific values, Sentient Sun interpretation, client material, or calibration content may cross into the Observatory.

### Existing Freedom 250 provenance

Freedom 250 already has an unwired review build at:

`Chronicle/99 - Templates/orrery-wip/`

Its existing architectural decision is also useful: heliocentric picture and geocentric meaning are separate engines, joined by an animated Sun/Earth perspective morph. Do not start from scratch. Before any build, compare the archived Sentient Sun structure with this Freedom 250 prototype and decide which owner supplies each generic capability.

The older `orrery-wip` instruction to formalize a new standalone tab predates the 2026-08-31 five-room Observatory floor plan. The current design preference is a governed planetary-motion instrument inside the existing **Transits & Cycles** room, with compact projections into other Sky and Chart surfaces. Any Orrery presentation must be reconciled with that current navigation authority rather than reviving the old tab plan automatically.

## Product direction

The visible feature may be called **Planetary Motion**. The underlying model is **Ongoing Planetary World**.

Preferred architecture:

1. One canonical, continuous motion producer.
2. One primary motion instrument inside Transits & Cycles.
3. A body-first view of longitude motion, body-relative speed, station/shadow arcs, solar phase, and declination travel.
4. Relationship overlays for synodic phase, applying/separating, pass history, and declination contacts.
5. Compact factual projections into Sky Calendar, Ingress Charts, Chart Readings, and Relationship Field/History.
6. Storyline surfaces may route to motion history but cannot derive ownership, evidence, or forecasts from it.

## Required pre-build decisions

- canonical ephemeris owner and exact-event root-finding policy;
- body-specific speed reference ranges and station-corridor definitions;
- shadow-period definitions for Mercury, Venus, Mars, and other retrograding bodies;
- inner-planet solar-phase and visibility vocabulary;
- declination-turn, OOB, parallel, and contraparallel semantics;
- equator-crossing rule and validator for near-zero declination;
- continuous sampling resolution versus exact event records;
- relationship pass identity and durable chronological history;
- which Sentient Sun Orrery structures are extracted, rewritten, or retired;
- visual distinction between physical heliocentric space, exact geocentric bearing, and presentation-only radial tracks;
- progressive disclosure that keeps motion intelligible without producing a wall of decimals.

## First implementation receipt — 2026-08-31

Katie authorized the first build slice: place the Orrery inside the Observatory, replace the former personal/natal profile direction with Freedom 250's mundane planet voice, and make planetary speed visible.

Built in the live Chronicle vault:

- **Transits & Cycles → Planetary Motion** is the third lazy child; no new shell tab was created.
- The heliocentric model remains the spatial picture; the geocentric Time Machine remains the zodiacal position/aspect authority.
- A checked-in Swiss-Ephemeris-derived motion payload covers 1776–2055; the visible Orrery is clamped to the heliocentric model's supported 1800–2050 range.
- Sun through Pluto receive daily signed longitudinal-speed samples. Mercury through Pluto also receive exact station roots.
- The selected body shows direct/retrograde/stationing state, signed degrees per day, body- and direction-relative pace, slowing/gaining trend, and the next exact station.
- The animation control is labeled **Playback rate** so it cannot be mistaken for planetary speed.
- Mundane focus summaries are projected from the Observatory's authored interpretation owner. Earth is the observing seat, not a mundane actor.
- No Sentient Sun natal placements, private profile copy, or person-specific chart material crossed into Freedom 250.

This is only the first planetary-motion product layer. The September 24 method
audit now supplies authored shadow-arc, Mercury/Venus solar-phase and local
visibility, eclipse-path and local-horizon circumstances, declination-continuity
and pass-aware relationship-history hearings. Eclipse circumstances now have a
dedicated reproducible snapshot producer; a continuous motion producer and
in-chart UI remain future Ongoing Planetary World work.

## Astronomy-context and pattern audit — 2026-09-24

### Question and standing

Katie asked what the mundane practice may be calculating but not yet hearing, and
whether the physical solar-system arrangement can supply useful context for the
Earth-centred astrological view. This is a method audit and product recommendation,
not a new doctrine, storyline election, causal theory, Forecast Ledger call, or
permission to revise the locked Pass 1 readings.

The audit joins five already-governed factual owners without merging their votes:

1. `chart_reading_registry.json` and the thirty registered Pass 1 readings;
2. `chart_reading_bones/` for exact geometry, declination, chart shape, roots,
   planetary-node contacts and other computed facts;
3. `mundane_history.json` for the ordered ingress/lunation sequence;
4. `moon_lineages.json` for the established 273/546/819-day Pessin lineages;
5. the Orrery's heliocentric model plus Swiss Ephemeris for Earth distance and
   exact geocentric solar elongation.

### Three frames, three jobs

The governing distinction is:

```text
solar-system view     = broad physical configuration and relative nearness
Earth-centred chart   = exact tropical longitude, aspect, orb and direction
Washington chart      = local horizon, meridian, houses, angles and mundane stage
```

The Orrery is deliberately a compressed visual model. Slow outer planets can look
essentially unchanged across several days, so an estimated screenshot date is
adequate for recognizing a broad Sun–Earth–outer-planet arrangement. It is not an
ephemeris receipt. Exact aspect, applying/separating status, house, angle and
timing claims remain with the 2D chart engine.

The observer diagram Katie supplied is useful intuition for the third frame, with
one precision note: the MC is the ecliptic's intersection with the local meridian,
not ordinarily the literal zenith; the IC is its opposite ecliptic point, not
ordinarily the literal nadir. Whole Sign houses are zodiacal sign arenas counted
from the rising sign, not twelve equal wedges of the physical local sky.

The same boundary applies to planetary hemispheres. A planet in Whole Sign
houses 7–12 occupies the chart's symbolic upper hemisphere; it is not thereby
above the observer's physical horizon. Normal analysis now keeps three columns:

1. **Whole Sign hemisphere** for mundane arena and house-ruler staging;
2. **true altitude** for literal above/below-horizon geometry at the named
   location and clock; and
3. **optical visibility** for a separately modeled result that includes solar
   glare, twilight, magnitude and atmosphere.

This correction materially changes one earlier shorthand. The February 2024
Mars–Pluto conjunction was 2/8 by Whole Sign upper/lower hemisphere but 0/10 by
literal Washington altitude. The January 2026 conjunction was 10/0 by Whole Sign
hemisphere but 5/5 in the literal sky; Mars and Pluto themselves were about
12–13° below the horizon. At the September Full Moon the literal sky again split
5/5, with Sun and Mars above and Moon, Neptune and Pluto below. The Moon rose at
6:49:27 p.m. EDT, Neptune at 6:55:42 p.m. and the Sun set at 6:57:18 p.m., so the
Moon–Neptune presentation emerged at dusk rather than at the exact midday phase.
At the October opposition the sky remained 5/5, but Mars, Moon and Uranus were
above while Pluto, Venus, Mercury and Sun were below. This is a transfer of local
staging, not an added evidence vote or a claim that altitude causes events.

Root-solving the local thresholds reveals a still tighter sequence. Neptune's
modeled set falls 4m10s before the Mars–Pluto opposition; geometric civil dawn
begins 50 seconds after it; the Moon reaches upper transit 20m57s after the
aspect; sunrise follows at +28m47s and Saturn sets at +36m25s. Later that
morning, Mercury rises 15m51s before the Cancer Last Quarter and Venus rises
18m05s after it, while Pluto remains below the horizon until 4:03 p.m. The
sequence may be narrated as one local-sky handoff—image, confrontation, public
culmination, authority, boundary, record and value—but its components are
dependent timings inside one rotating sky and cannot be counted as independent
convergence.

The models must remain named. Civil dawn here is the geometric solar-center
−6° threshold. Rise and set times use the Swiss Ephemeris apparent disc-center
horizon calculation; meridian transit is a separate local-coordinate event.
None of those clocks alone proves naked-eye visibility.

### Saturn–Neptune: hidden seed to visible opposition

The February and September pictures are not merely “the same conjunction versus
opposition.” They are different astronomical relationships nested around the same
slow pair:

| Frame | Geocentric solar relationship | Saturn Earth distance | Neptune Earth distance |
|---|---:|---:|---:|
| Saturn–Neptune exact conjunction · 2026-02-20 16:52 UTC | both 28.69° from the Sun | 10.358 AU | 30.747 AU |
| Aries ingress · 2026-03-20 14:45 UTC | Saturn 4.13° and Neptune 1.77° from solar conjunction | 10.487 AU | 30.878 AU |
| Libra ingress · 2026-09-23 00:05 UTC | Saturn 12.20° and Neptune 3.08° from solar opposition | 8.455 AU | 28.876 AU |
| Orrery screenshot estimate · 2026-09-24 22:33 UTC | Saturn 10.15° and Neptune 1.14° from solar opposition | 8.448 AU | 28.876 AU |

The exact slow-pair conjunction occurred February 20; the Sun itself was not
conjunct the pair that day. Neptune's solar conjunction followed on March 22 and
Saturn's on March 25. Neptune reaches exact solar opposition on September 26 and
Saturn on October 4. The Aries ingress therefore frames the new Saturn–Neptune
seed near the far-side solar-glare phase, while the Libra ingress frames the same
pair near the near-side, all-night opposition phase. This is a real astronomical
mirror across the mundane year: **hidden/co-directional seed → visible/confronting
half-year revelation**.

NASA describes opposition as the Sun, Earth and outer planet aligning with Earth
in the middle; the planet is near its closest and fullest phase and is available
through the night. That observational context is worth displaying. It does not
establish that distance or visibility causes an astrological effect.

### Gravity: preserve the relative fact and the absolute scale

Katie's relative observation is correct: Saturn and Neptune pull more strongly on
Earth when Earth is on their near side than when it is on the far side. The Orrery
must nevertheless distinguish two different quantities:

- gravitational acceleration or force scales as `mass / distance²`;
- tidal differential across Earth scales as `mass / distance³`.

At the September 24 estimated frame versus the February 20 pair conjunction:

| Body | acceleration change | tidal-proxy change |
|---|---:|---:|
| Saturn | 1.503× · about 50.3% stronger | 1.843× · about 84.3% stronger |
| Neptune | 1.134× · about 13.4% stronger | 1.207× · about 20.7% stronger |

The absolute scale remains tiny. At the September frame Saturn's acceleration on
Earth is about `2.37e-8 m/s²` and Neptune's about `3.66e-10 m/s²`. Saturn's tidal
proxy is about `2.22e-7` of the Moon's at that instant; Neptune's is about
`1.00e-9` of the Moon's. The astronomy panel may show these values as context,
but it must not call a tidal value simply “pull,” combine `1/d²` and `1/d³`, or
offer gravity as proof of astrology.

### The largest reading gap: the Full Moons are already harvests

All **thirteen** registered 2026 Full Moons are established 546-day Full-phase
beats of earlier 2024–25 New Moon seeds in `moon_lineages.json`. The Pass 1 corpus
reads every Full Moon as a culmination inside its ingress, but no registered Pass
1 reading explicitly names its Pessin lineage. The calculation is present; the
continuity narration is missing.

The most immediate example is the September 26 Aries Full Moon:

- seed: March 29, 2025 Aries solar eclipse at about 9.0° Aries;
- Full-phase return: September 26, 2026 at about 3.6° Aries;
- elapsed time: 546.244 days;
- same-sign degree drift: 5.382°;
- interpretation and continuity verdict: still unreviewed.

That Full Moon also lands about one day after exact Neptune opposition and places
its MC at 0.798° Libra, only 0.045° from exact opposition to the 0.753° Aries
Saturn–Neptune conjunction seed. These are three distinct clocks—Moon lineage,
solar visibility geometry and an angle-to-seed contact. They may form one strong
hearing date, but they do not become three evidence votes.

The node audit now supplies a necessary fourth distinction. The eclipse seed's
lights were 11.576° from the true lunar-node axis; the First-Quarter Moon was
25.025° from its nearest node; and the Full-phase Moon is 34.093° away. Absolute
lunar ecliptic latitude rises from 1.063° to 2.152° to 2.912°. The 273/546-day
Moon-family clock is therefore not an eclipse-recurrence clock: the phase family
continues while the shadow geometry monotonically falls away. Normal analysis
may read this as shadowed seed becoming unshadowed illumination, but it must not
score the widening node distance as strength or create another vote.

### The quarter phases are the missing chapters

The established Moon-family method is not only New Moon seed and Full Moon
harvest. It also requires First Quarter at about +273 days and Last Quarter at
about +819 days. The factual engine contains lineage-qualified quarter phases,
yet the chart-reading registry admits no quarter-moon Pass 1 readings.

Within the registered Libra-to-Capricorn sequence alone, the omitted beats include:

| Date | Phase | Original seed |
|---|---|---|
| 2026-10-03 | Last Quarter | 2024-07-05 Cancer New Moon |
| 2026-10-18 | First Quarter | 2026-01-18 Capricorn New Moon |
| 2026-11-01 | Last Quarter | 2024-08-04 Leo New Moon |
| 2026-11-17 | First Quarter | 2026-02-17 Aquarius solar eclipse |
| 2026-12-01 | Last Quarter | 2024-09-03 Virgo New Moon |
| 2026-12-17 | First Quarter | 2026-03-19 Pisces New Moon |
| 2026-12-30 | Last Quarter | 2024-10-02 Libra solar eclipse |

Recommendation: do not create twenty-four more full Pass 1 essays. Add a compact
**Moon-family chapter strip** to each lunation/season view. It should name the
seed, current gestational role, elapsed days, same-sign degree drift and next
family beat. Only a quarter phase with an earned governing-chart, root, angle,
radix or developing-story contact should receive a fuller hearing.

### Quarter-phase triage result — late 2026

The Libra-to-Capricorn quarter phases were subsequently cast at their exact
Washington clocks and tested under that rule. The result validates selective
admission rather than universal narration:

| Date | Role | Earned context | Disposition |
|---|---|---|---|
| Oct 3 | Cancer Last Quarter | Mars–Pluto opposition 0.067°, double T-square, exact cross-cycle braid | expanded contextual chapter |
| Oct 18 | Capricorn First Quarter | retrograde Venus applying square Pluto; treasury/collective action test | compact strip |
| Nov 1 | Leo Last Quarter | Moon trine Saturn, but no materially new relationship or root hinge | restraint case |
| Nov 17 | Aquarius First Quarter | solar-eclipse lineage; Mars–Jupiter conjunction in government field; both inner values newly direct | expanded strip hearing |
| Dec 1 | Virgo Last Quarter | Uranus–Pluto trine 0.111° after exact pass; Mars applying square Uranus | expanded strip hearing |
| Dec 17 | Pisces First Quarter | exact declination braid across Sun/Mercury/Pluto and Moon/Saturn/Neptune | expanded strip hearing |
| Dec 30 | Libra Last Quarter | solar-eclipse lineage; Mercury square Saturn 0.320°; seed drift 0.975° | expanded strip hearing |

The current human-facing owner is [[Quarter Moons Re-enter the Story — Libra to
Capricorn 2026]]. October 3 has the separate fuller hearing [[Two Cycles Meet at
the Reckoning — October 3, 2026]]. None was promoted into the registered Pass 1
corpus, and none receives a Forecast or Evidence vote.

### Ten-planet distribution changes regime; automatic shape labels are withheld

The earlier draft reused provisional bowl, locomotive and splay labels stored in
the August chart bones. The current live structure engine has no admitted
Jones/Meyer family owner and now returns `shape: null`. The exact point set,
circular gaps, largest empty arc and occupied span remain available. The
continuity claim is therefore corrected to use only those measurements:

- January through June 15 shows a phase-linked pulse: New Moons leave
  183.22°–199.78° largest gaps while the intervening Full Moons leave
  112.33°–170.67° gaps;
- the July 14 New Moon breaks that pattern with a 149.40° largest gap, and the
  field continues opening through the August eclipses;
- August 28 is the first chart below a 104° largest gap, and every registered
  chart from September 11 through December 24 remains below 93°.

The Full-Moon-to-opposition audit finds a more precise transition inside that
late-year corridor. Venus and Pluto bound the largest empty arc at the August
28 eclipse (103.55°), September 11 New Moon (92.82°), Libra ingress (86.62°),
September 26 Full Moon (85.48°), October 3 opposition and Cancer Last Quarter
(84.62°). At the October 10 New Moon and October 26 Full Moon, Mercury and Pluto
become the endpoints instead. The aspect sequence and raw distribution therefore
agree on one non-additive handoff: value/consent turns, then the record becomes
the active boundary with power.

The opposition-to-quarter interval also supplies a clean rotation control. In
2h46m the Washington Ascendant advances 33.44° and the MC 39.66°, moving every
planet back one Whole Sign house. The Venus–Pluto largest gap changes only
0.00021°. Earth's daily spin rotates angles and local mundane stages; it does
not rotate the planets around the tropical zodiac. The Sun's annual geocentric
motion and the planets' other longitude changes arise from orbital motion,
including Earth's revolution.

This is not a one-chart decoration, but neither is a gap threshold a named shape
family. Recommendation: every Pass 1 should preserve exact distribution geometry
and compare it with the preceding governing chart. A bowl, locomotive, splay or
other family name may return only through a reviewed owner using the complete
criteria, never by silently converting one gap measurement into a label.

The corrected human-facing continuity ribbon is preserved in [[THE FIELD
SCATTERS, THE COMMAND TIGHTENS — 2026 CHART SHAPE AND ROOT CONTINUITY]]. It
covers all thirty registered 2026 ingress/lunation bones, verifies their gaps
against the current live engine, and joins the first-half phase pulse, July break
and late-year low-gap corridor to dispositor-root continuity. It remains a
contextual companion rather than a revision of any Pass 1 reading.

### The Libra root changes hands in an intelligible sequence

The dispositor roots across the Libra-to-Capricorn sequence do not merely vary;
they hand authority from one closed circuit to another:

```text
Libra ingress          Mars–Moon–Saturn
Sep 26 Full Moon       Mars–Moon
Oct 10 / Oct 26 / Nov 9
                       Mars–Sun–Venus
Nov 24 Full Moon       Jupiter–Sun–Venus
Dec 9 New Moon         Jupiter–Sun
Capricorn ingress      Jupiter–Mars–Mercury–Saturn–Sun
Dec 24 Full Moon       Jupiter–Mars–Mercury–Moon–Saturn–Sun
```

The sequence begins with protection, public feeling and institutional limit;
moves into force, executive purpose and value/relationship; then brings Jupiter's
law, scale, banks and legitimacy into the circuit; and finally closes the year in
a much larger multi-actor loop. This is a better continuity instrument than
treating each chart's root as a static isolated fact. Recommendation: add a
root-handoff timeline to seasonal comparisons.

That authored timeline now exists in [[THE FIELD SCATTERS, THE COMMAND TIGHTENS
— 2026 CHART SHAPE AND ROOT CONTINUITY]]. Its principal finding is that the
late-year field becomes more spatially distributed while dispositorship becomes
more recursive, culminating in a five-body institutional circuit plus an
independent domiciled Moon on December 24.

### Declination is telling a second Saturn–Neptune story

Longitude and declination reverse their relationship during the year:

- around the February conjunction through the Aries ingress, Saturn and Neptune
  are longitudinally conjoined and also closely parallel in declination;
- at the April 2 Full Moon, their contra-parallel is effectively exact at 0.005°
  even while their longitude relationship has begun to separate;
- by the October 26 Full Moon the pair is applying again in longitude while the
  contra-parallel tightens from 0.930° to 0.165° by December 9.

The Libra ingress adds a particularly strange double statement: its Sun opposes
Neptune in longitude by 3.08° applying while the Sun and Neptune are parallel in
declination by 0.077°. The chart simultaneously stages visible confrontation and
same-declination co-presence. This is exactly the kind of structure lost when
declination is treated as a footnote.

There is also an engine rule to settle. At the Aries ingress the Sun is almost
exactly on the celestial equator. The current bone records both parallel and
contra-parallel to Saturn and Neptune because the absolute-difference and
absolute-sum tests are simultaneously within orb. The future declination owner
must define an equator-crossing ambiguity rule and prevent this from silently
becoming two interpretive votes.

### Seed degrees form a relay across chart types

Long-clock conjunction seeds are not only background eras. Several become exact
geometrical hinges in the 2026 governing sequence:

- the Libra ingress Sun is 0.753° from opposition to the 2026 Saturn–Neptune
  seed and 0.081° from square to the 1988 Saturn–Uranus seed;
- the September 26 Full Moon MC is 0.045° from opposition to the
  Saturn–Neptune seed;
- the Libra ingress Ascendant is 1.489° from square to the 2020 Jupiter–Pluto
  seed.

Recommendation: give seed-degree contacts their own factual lane, labeled by
point, aspect, orb and seed owner. Do not mix them into ordinary transiting-planet
aspects or count several contacts to one seed as several independent proofs.

### Lexical coverage is not calculation coverage

A plain-text audit of the thirty authored Pass 1 Markdown readings found roots or
dispositors in 23, declination in 7, chart shape in 5, midpoints in 2, planetary
nodes in 2, profections in 5, and no explicit references to derivative houses,
Lots, Moon-family lineage, Sabians or synodic phase. Motion language appears much
more often. This is only a lexical audit: most omitted facts exist in the chart
bones, and absence of a keyword does not prove absence of thought.

The practical conclusion is not “put every technique in every reading.” It is to
build a governed admission checklist so a technique is visibly considered and
then either narrated because it materially changes Judgment or withheld with no
penalty.

### Recommended product contract

Add an **Astronomical Context** layer to Planetary Motion with progressive
disclosure:

1. **Space view — configuration:** heliocentric placement, true current Earth
   distance, light-time and a visible warning that display radii are compressed.
2. **Earth view — exact projection:** solar elongation, conjunction/opposition
   state, visibility phase, geocentric longitude and a projection thread from the
   physical body through Earth to the zodiac ring.
3. **Washington view — local stage:** horizon, meridian, Ascendant/Descendant,
   MC/IC and Whole Sign houses supplied only by the chart-grade owner.
4. **Physical context drawer:** separate gravitational acceleration (`1/d²`) and
   tidal proxy (`1/d³`), with absolute units and Moon/Sun comparison. No combined
   “gravitational/tidal pull” label.
5. **Continuity drawer:** relationship phase/pass, declination relationship,
   Moon-family chapter, chart-shape regime, root handoff and exact seed-degree
   contacts. Each item keeps its source owner and never creates evidence credit.

The Orrery remains the picture and teaching instrument. The chart remains the
measuring and delineating instrument. The local Washington frame remains the
mundane stage. Keeping those jobs distinct is what lets the astronomy deepen the
astrology without replacing it.

### Eclipse geography is a separate local-stage axis

The 2025–2026 eclipse audit exposes another category that the chart corpus was
mostly naming without hearing: the difference among exact syzygy, greatest
eclipse, global eclipse class, shadow path and Washington-local visibility.

The complete audit is preserved in [[The Eclipse Meets the Horizon — Washington
Visibility 2025–2026]]. Its strongest corrections are:

- the March 29, 2025 Aries solar-eclipse seed perfects below the Washington
  horizon, becomes visible only at sunrise and ends less than two and a half
  minutes later;
- the February 17, 2026 annular eclipse is not visible as an eclipse in
  Washington even though the exact New Moon sits almost exactly on the sunrise
  horizon and on the chart Ascendant;
- the March 3 total lunar eclipse reaches maximum only 0.29° above the western
  horizon, sets while still total and reaches exact Full Moon about 51 seconds
  after moonset;
- the August 12 total solar eclipse is only a 3.68%-obscured partial in
  Washington, while the August 28 deep partial lunar eclipse is fully visible
  for its entire 198-minute umbral phase.

The local stage therefore modifies entrance, exit and witness. It does not
change chart ownership, transfer the lunar chapter, or create evidence. A
globally total eclipse can be locally partial or absent; a luminary can be above
the horizon while the shadow path misses Washington; a locally invisible
eclipse chart can still be angular because the syzygy and the path are different
geometries.

The normal eclipse hearing must now preserve:

1. exact conjunction/opposition used for the chart;
2. greatest-eclipse clock and its offset from syzygy;
3. global type and path;
4. Washington-local type, magnitude and solar obscuration where applicable;
5. true/apparent altitude, rise/set condition and observable phase duration;
6. a source/model label for every horizon-sensitive number.

The factual producer is `99 - Templates/build_eclipse_local_circumstances.py`;
its current output is `99 - Templates/eclipse_local_circumstances.json`.

### Eclipse genealogy is three clocks, not one family label

The recurrence audit in [[The Shadow Has More Than One Ancestor — Saros,
Metonic and Moon-Family Time]] adds a second eclipse invariant. Every historical
comparison must declare which identity it is using:

1. **Saros:** 223 synodic months; the same evolving eclipse series and similar
   shadow geometry;
2. **Metonic:** 235 synodic months; the same lunar phase near the same calendar
   date and tropical-zodiac degree, which may be a different Saros or not an
   eclipse at all;
3. **Pessin Moon Family:** one New-Moon seed and its 273/546/819-day phase
   chapters.

The difference between Saros and Metonic intervals is twelve lunations. One
ancestral eclipse can therefore branch into a same-Saros return and, about one
lunar year later, a different-Saros Metonic echo. Six such braids appear in the
2024–2026 corridor. They are one shared astronomical ancestry with two later
branches, not two independent evidence votes.

The strongest operational examples are:

- the March 29, 2006 total solar eclipse branches to the April 8, 2024
  same-Saros eclipse and the March 29, 2025 same-degree Metonic eclipse;
- the March 3, 2007 total lunar eclipse branches to the March 14, 2025
  same-Saros eclipse and the March 3, 2026 same-degree Metonic eclipse;
- the August 28, 2007 total lunar eclipse branches to the September 7, 2025
  same-Saros eclipse and the August 28, 2026 same-degree Metonic eclipse.

The February 17 and August 12, 2007 same-phase echoes were not eclipses. Their
2026 solar counterparts may not be narrated as returns of a 2007 eclipse. The
September 21, 2025 eclipse has no complete Pessin lineage admitted by the
current Moon-motion projection; that null remains visible.

The factual producer is `99 - Templates/build_eclipse_genealogies.py`; its
output is `99 - Templates/eclipse_genealogies.json`, checked by
`99 - Templates/test_eclipse_genealogies.py`.

### Source and calculation receipts

- NASA, [Basics of Space Flight — Chapter 1](https://science.nasa.gov/learn/basics-of-space-flight/chapter1-2/) — conjunction/opposition geometry and outer-planet nearness/full phase.
- NASA, [Skywatching FAQ](https://science.nasa.gov/skywatching/faq/) — opposition visibility through the night.
- NASA/NSSDC, [Planetary Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/) — body masses used for scale checks.
- `99 - Templates/chart_reading_bones/*.json` — exact chart facts.
- `99 - Templates/moon_lineages.json` — Pessin phase identities and lineage joins.
- `99 - Templates/mundane_history.json` — ordered chart sequence.
- `99 - Templates/eclipse_local_circumstances.json` — global/local eclipse type,
  syzygy versus maximum, horizon state, magnitude, obscuration and duration.
- `99 - Templates/eclipse_genealogies.json` — separately typed Saros, Metonic,
  Moon-family and Saros–Metonic braid identities.
- `99 - Templates/orrery-wip/helio_ephemeris.js` and Swiss Ephemeris — distance and exact geocentric solar-elongation checks.

The gravity calculations use Newtonian scale comparisons only. Values are rounded
for interpretation-facing display; exact reproducible production fields still
need a governed machine-readable producer and regression tests before any UI
implementation.

## Political-reservoir hearing — Moon-family seeds, 2026-09-24

### The test was frozen before the outcome search

The thirteen 2026 Full Moons were first joined to their established New Moon
seeds. Each seed then received a fixed `±3 civil days` reservoir query before its
Full-Moon window was inspected. This prevents a later headline from choosing its
own convenient seed. The lanes remain separate:

```text
seed chart -> official seed objects -> intervening maturity chain
          -> Full-Moon hearing -> later outcome/disposition
```

An event in the Full-Moon window is not automatically the seed's fruit. The
same legal person, authority, money route, operating object, or clearly preserved
institutional question must survive the interval. A thematic rhyme is retained
as context, not promoted into an object-level maturation.

The political reservoir is genuinely sparse around the first five 2024 seeds.
That is a coverage finding, not evidence that nothing happened. The 2025 seeds
are substantially richer:

| 2026 Full Moon | New Moon seed | Official material in the fixed seed window | Present disposition |
|---|---|---|---|
| Jan 3 | Jul 5, 2024 Cancer | none stored | untested; archive gap |
| Feb 1 | Aug 4, 2024 Leo | none stored | untested; archive gap |
| Mar 3 | Sep 3, 2024 Virgo | none stored | untested; archive gap |
| Apr 2 | Oct 2, 2024 Libra solar eclipse | none stored | untested; one nonofficial crypto item is not enough |
| May 1 | Nov 1, 2024 Scorpio | none stored | untested; archive gap |
| May 31 | Dec 1, 2024 Sagittarius | House Covid Select Subcommittee final-report business meeting, Dec 4 | direct Covid maturation not found in the Full-Moon window; unresolved |
| Jun 29 | Dec 30, 2024 Capricorn | no source-closed official object stored | untested |
| Jul 29 | Jan 29, 2025 Aquarius | reconstructed OMB-freeze, DOGE/USAID, Guantanamo and confirmation-hearing cluster; CBN FX Code is source-closed | rich attention record, but no clean same-object Full-Moon-window return yet |
| Aug 28 lunar eclipse | Feb 28, 2025 Pisces | GAO High Risk List; foreign-aid hearing; SEC Treasury-clearing extension | strong control/audit rhyme; only partial object continuity |
| Sep 26 | Mar 29, 2025 Aries solar eclipse | public-media hearing; JFK hearing; AI/power hearing; third-country-removal TRO; Nigeria digital-asset transition | strongest multi-branch seed; harvest still prospective at this cutoff |
| Oct 26 | Apr 27, 2025 Taurus | automated vehicles; secure software; BoE core ledger; DOD audit and drone hearings; UK crypto perimeter | seed established; harvest future |
| Nov 24 | May 27, 2025 Gemini | FCA stablecoin consultation; Treasury payment-modernization RFI | seed established; harvest future |
| Dec 24 | Jun 25, 2025 Cancer | Basel stablecoin statement; DOGE-cuts hearing; Hong Kong tokenization/gold objects; IMF conditionality | seed established; harvest future |

This table is a research map, not a declaration that every item belongs to the
Moon family. The sparse rows need retrospective primary-source reconstruction
before interpretation.

### March 29, 2025 eclipse seed: five institutional branches

The Aries eclipse window did not seed one political topic. It held several
independent objects that later acquired different bodies. The September 26,
2026 Full Moon can test all five without pretending they are one convergence
vote.

| Branch | Seed-window object | Maturation by cutoff | Exact boundary |
|---|---|---|---|
| Public media | Mar 26 House hearing converted media-trust claims into a funding question | May 1 executive order; Public Law 119-28 rescinded CPB FY2026/27 funds; CPB directors voted Dec 10 to dissolve; the federal case was dismissed as moot Jan 14, 2026 | hearing was not defunding; statute was not dissolution; board vote was not every D.C./IRS wind-down filing or repeal of 47 U.S.C. 396 |
| Declassification | Mar 26 NARA tranche and Apr 1 JFK task-force hearing | May 20 obstruction hearing; NARA says another 11,022 pages were posted Jan 30, 2026; later MLK and MKULTRA hearings widened the congressional records lane | most of the initial 80,000-plus-page release preceded the eclipse; the eclipse window institutionalized review rather than originating all release activity |
| Third-country removals | Mar 28 TRO in *D.V.D.* | the district court entered final APA relief; on Sep 18, 2026 the First Circuit vacated two sequencing declarations but otherwise affirmed the judgment; on Sep 24 the government announced an emergency Supreme Court return | the judgment set aside the challenged guidance rather than abolishing statutory third-country-removal authority; the Sep 23 docket event, Sep 24 application, stay disposition, replacement procedure and operating consequences remained open at cutoff |
| AI and power | Apr 1 hearing put data-center load, generation, water and rate allocation on the congressional record | EO 14318 created an operative acceleration route; DOE/Army/BLM later returned site, solicitation, selection, lease-negotiation, permit-framework and project-stage objects | direction, selection, lease negotiation, permit, construction and operation remain distinct; most projects were not operating at cutoff |
| Nigeria crypto perimeter | ISA 2025 brought virtual/digital assets into the securities perimeter | July 2026 coordination order, SEC proposed rules and participant additions, plus a CBN stablecoin/virtual-asset sandbox track | wider perimeter is not one regulator, one licence, a final stablecoin regime, a production cross-border route, or proof of customer settlement/finality |

Public media remains the most mature completed chain: a question placed in the
hearing record became an enacted rescission and then an organizational
dissolution decision. **Third-country removal is now the cleanest live-window
same-object return.** The identical case and guidance moved from a March 2025
provisional restraint into a September 2026 appellate judgment and a renewed
emergency Supreme Court contest. The AI/power and Nigeria branches show
substantial but still transitional maturation. Declassification shows continuing
publication and institutional review. None should be called the final September
26 outcome before the Full Moon's evidence window closes.

The *D.V.D.* return also proves why the comparison layer must preserve record
precision. The government's public statement described a broad block on
third-country removals. The retrieved appellate opinion is narrower: DHS retains
statutory removal authority, two sequencing declarations were vacated, and the
challenged guidance's notice-and-hearing procedure was set aside. The factual
chain now lives in Workbench `Research Packages/DVD Third-Country Removal
Authority 2025-2026/README.md`; the astrology file observes timing only after
that independent legal record is fixed.

### Two reservoirs can share a week without becoming one story

The September Full Moon and October opposition join two established astrological
clocks, so their political reservoirs require a cross-family identity test. Six
March 2025 Aries-eclipse authority objects were compared with six January 2026
Mars–Pluto force objects under a strict same-object rule: continuity of the
case, instrument, named authority, asset, parties or operating route. The
result is **zero cross-reservoir identity matches**.

The two clean near-window returns are real but separate. *D.V.D.* belongs to the
March eclipse's authority–procedure–remedy chain; the September 22 Greenland
agreement belongs to the January conjunction's security-demand-to-covenant
chain. Cross-border custody, economic coercion, national-security personnel and
investment governance produce several functional echoes across the reservoirs,
but theme and institutional function do not create object continuity.

This adds a required control to political-reservoir work:

1. establish same-object continuity inside each seed family;
2. test cross-family identity by case, instrument, legal person, asset,
   decision right and operating route;
3. retain structural rhymes as explicitly non-identical context; and
4. never let an astrological degree relay merge factual objects that their
   authorities keep separate.

The reproducible comparison is `99 -
Templates/aries_mars_pluto_reservoir_separation.json`.

### The Pisces seed and August 28 eclipse: rhyme versus continuity

The February 25–26 seed window grouped GAO's High Risk List, foreign-aid
oversight and the SEC's Treasury central-clearing extension. Around the August
28 lunar eclipse, official records included GSA's suspected-procurement-fraud
announcement, GAO review of DOE contractor-assurance systems, an OIG report on
CFPB workforce/contract actions and CMS prevention of laboratory payments.

That is a strong **audit, fraud-control and administrative-capacity rhyme**.
It is not yet one same-object harvest. The Treasury-clearing seed's cash and
repo implementation clocks still ran to December 31, 2026 and June 30, 2027.
The Full Moon therefore illuminated the control problem before that particular
market-infrastructure object reached its scheduled gate.

### Political source receipts

- House Oversight, [Anti-American Airwaves](https://oversight.house.gov/hearing/anti-american-airwaves-holding-the-heads-of-npr-and-pbs-accountable/),
  [The JFK Files](https://oversight.house.gov/hearing/task-force-on-the-declassification-of-federal-secrets-the-jfk-files/),
  and [America's AI Moonshot](https://oversight.house.gov/hearing/americas-ai-moonshot-the-economics-of-ai-data-centers-and-power-consumption/)
  supply the three congressional seed-window objects.
- [Public Law 119-28](https://www.govinfo.gov/content/pkg/PLAW-119publ28/html/PLAW-119publ28.htm)
  supplies the enacted CPB rescission. The CPB dissolution boundary is retained
  from `Research Packages/Federal Government Entity Library Harvest
  2026-08-22/waves/WAVE_N_CANDIDATES.md`, including D.D.C. case
  `1:25-cv-01305`, ECF 46.
- NARA's [2025 JFK release ledger](https://www.archives.gov/research/jfk/release-2025)
  separates each publication tranche and includes the January 30, 2026 return.
- The Supreme Court's June 23, 2025 [order in *DHS v. D.V.D.*](https://www.supremecourt.gov/opinions/24pdf/24a1153_l5gm.pdf)
  supplies the emergency-stay state; it is not treated as a final merits opinion.
- The official implementation states for AI/power are preserved in Workbench
  `Research Packages/Data Center Federal Legal Spine 2025-2026/`; the Nigerian
  authority, licence, sandbox, settlement and route boundaries are preserved in
  `Research Packages/International Monetary Transition/13 - International
  Crypto Map 2026/country_research/NG_PRIMARY_SOURCE_BASELINE_2026-09-15.md`.
- House Oversight's [GAO High Risk hearing](https://oversight.house.gov/hearing/the-government-accountability-offices-2025-high-risk-list/)
  and the SEC's [Treasury-clearing implementation page](https://www.sec.gov/featured-topics/treasury-clearing-implementation)
  supply the Pisces seed objects. Their later audit/fraud neighbours remain
  thematic context until exact same-object continuity is proved.

### The Aries family's missing middle is now recovered

The March 29, 2025 eclipse family had a computed but unheard First Quarter on
December 27, 2025. Its compact contextual hearing materially changes the
seed-to-harvest description without promoting the quarter into a protagonist.

At the eclipse seed, every traditional dispositor route terminates in the
Mars–Moon mutual reception. At the Taurus-rising First Quarter, Venus routes
through Saturn, Jupiter, Moon and Mars, and all ten planets terminate in one
four-body circuit: `Saturn → Jupiter → Moon → Mars → Saturn`. At the September
2026 Full phase, the circuit contracts again to Mars–Moon. Raw distribution
moves in the same developmental direction: the largest empty arc falls from
190.72° at seed to 150.40° at First Quarter and 85.48° at Full phase. Named
shape families remain withheld.

The December checkpoint is also source-legible. By then the independently
selected March authority objects had begun meeting administration, courts,
appropriations, record production and organizational survival: automobile
duties were operative and amended; the *D.V.D.* guidance was operating under a
Supreme Court stay while merits litigation continued; labor exclusions had
entered implementation and funding contest; the D.C. task-force container had
acquired an expanded enforcement posture; the Smithsonian review had produced
a renewed missing-record demand; and the public-media branch had reached
enacted rescission plus a CPB board dissolution vote. These are different
states, not one hit.

The methodological gain is precise: the quarter chart can reveal the
**mechanism between command and consequence**. It asks which institution, law,
record, appropriation or counterparty had begun carrying the seed before Full
phase made the consequences public. The generated comparison is `99 -
Templates/aries_eclipse_moon_family.json`; the authored hearing remains inside
[[The Image Becomes an Order — 2026 Aries Full Moon Reread]].

The same comparison exposes a second method gain. Pluto at the March eclipse
seed lies only 0.055° from the January 2026 Mars–Pluto conjunction coordinate;
First-Quarter Pluto remains within one degree; Full-phase Pluto and the October
opposition return to the corridor; and the Full-Moon lights aspect the
conjunction point within 0.052°. This is an admissible **cross-cycle
seed-degree relay** because the geometry is direct and computed. It does not
merge the Moon family with the synodic family, multiply votes or establish
causation. The First-Quarter MC, 1.047° from the conjunction coordinate, is
retained as a policy miss rather than rounded into the pattern.

The strict midpoint layer adds a different admissible relay. Under the existing
one-degree mod-45 crisis-axis policy, the conjunction seed's collapsed
Mars/Uranus–Uranus/Pluto axis contacts the later Full-Moon MC within 0.273°;
the Full-Moon Uranus/Pluto midpoint moves into the lights within 0.754° and then
lands on the opposition MC within 0.00375°; the opposition MC itself remains on
the collapsed Mars/Uranus–Uranus/Pluto axis within 0.075°. The exact
conjunction, opposition and Full-Moon symmetry create duplicate mathematical
representations, so paired hits are deduplicated as one axis rather than counted
as separate votes. The Cancer Last Quarter supplies useful restraint: it has no
current-chart crisis-pair hit to Sun, Moon, ASC, MC or true Node inside one
degree. The computed owner is `99 -
Templates/aries_mars_pluto_choreography.json`; the interpretation is preserved
in [[The Image Becomes an Order — 2026 Aries Full Moon Reread]].

A thirteen-Full-Moon control changes the significance claim without erasing the
relay. Eight 2026 Full Moons have at least one strict crisis-pair hit; three put
one on the lights. The Aries Uranus/Pluto light contact is therefore not unique.
Its sequence-specific importance comes from carrying into the already selected
October 3 Mars–Pluto opposition MC within 0.00375°, not from midpoint presence
alone. The control is descriptive and post-observation; it is not a frequency
model, statistical significance test or added score.

### Quarter Moons are supporting chapters, not automatic protagonists

Katie's disposition is now explicit: First- and Last-Quarter family beats are
context charts by default. They belong in the continuity strip because they
show how a seed is being tested or distributed, but they do not receive a full
Pass 1 hearing merely for existing.

- **First Quarter:** an implementation, decision or resistance chapter around
  `+273 days`; ask what the seed now has to do.
- **Full Moon:** the ordinary culmination/visibility hearing around `+546 days`.
- **Last Quarter:** a consequence, revision, distribution or release chapter
  around `+819 days`; ask what the matured fruit now requires the system to
  relinquish or reform.

A quarter chart earns promotion only through a material governing-ingress,
root, angle, long-clock seed, radix, or independently developing same-object
story contact. Otherwise one compact factual row is enough.

## Structural deepening of the 2026 sequence

### Why the August shape change is astronomically intelligible

The Sun's roughly one-degree-per-day zodiacal progress comes from Earth's
**yearly revolution** around the Sun. Earth's daily **rotation** moves the local
horizon and meridian and therefore the Washington angles. Mercury and Venus
remain visually tied to the solar side of the chart because their orbits lie
inside Earth's. A New or Full Moon adds another hard geometric constraint.
The slow outer planets supply the long-lived background distribution.

The August 12 solar eclipse is locomotive because the ten traditional chart
bodies leave a 118.01-degree empty arc from Venus at 5°53 Libra to Pluto at
3°54 Aquarius. By the August 28 lunar eclipse:

- Venus has advanced to 20°02 Libra, shrinking that gap to 103.55 degrees;
- the Full Moon has moved to 4°54 Pisces, filling the Pluto-to-Neptune side of
  the wheel rather than doubling the Sun in Leo; and
- Mars, Jupiter, Sun and Mercury form separated Cancer–Leo–Virgo centres.

The result crosses the chart engine's structural boundary into splay. The
September 11 New Moon remains splay even after the Moon returns to the solar
cluster because Venus has moved into Scorpio and the occupied centres remain
distributed. This is not arbitrary labeling and not solely an outer-planet
story: **inner-planet elongation, lunation geometry and the slow frame jointly
determine which chart shapes are astronomically available.**

### Libra-to-Capricorn root handoff: the actual circuits

The root list sometimes contains more than one independent terminus. The
precise circuit matters:

| Chart | Dispositor authority | What changes structurally |
|---|---|---|
| Libra ingress | `Mars -> Moon -> Saturn -> Mars` | every planet drains into one three-body loop; Mars and Saturn are both in fall, so the circuit is commanding but poorly tooled |
| Sep 26 Full Moon | `Mars <-> Moon` | the system contracts to direct feedback between action/force and voiced need; Saturn no longer sits inside the root |
| Sep 27 Mars enters Leo | `Sun -> Venus -> Mars -> Sun` | the Mars–Moon mutual reception ends and every planet briefly drains into one authority/value/force loop; Mars leaves fall but answers through a fallen Sun and detriment Venus |
| Oct 2 Moon enters Cancer / Oct 3 opposition and quarter | same three-body loop **plus** Moon final | the domiciled Moon becomes an independent root 48.5 minutes before Mercury squares Pluto; public need/protection stands beside, rather than inside, the terms-force-authority machine |
| Oct 10 New Moon | `Sun -> Venus -> Mars -> Sun` | executive purpose, value/agreement and force become one closed circuit |
| Oct 26 Full / Nov 9 New | `Sun <-> Mars` **plus** Venus final | two authority centres: executive-force feedback and Venus independently at home in Libra |
| Nov 24 Full | `Sun <-> Jupiter` **plus** Venus final | law, legitimacy, banks or scale enter the executive circuit while value/agreement remains autonomous |
| Dec 9 New | `Sun <-> Jupiter` | Venus has left her autonomous final seat; all roads now drain into executive-legitimacy feedback |
| Capricorn ingress | `Sun -> Saturn -> Mars -> Mercury -> Jupiter -> Sun` | one five-body institutional circuit joins executive, bureaucracy, force, record/trade and law/scale |
| Dec 24 Full | same five-body circuit **plus** Moon final in Cancer | the institutional machine and a self-governing public/need body coexist; this is not one six-body loop |

The October root split also supplies a controlled relationship-phase example.
The Moon conjoins Neptune before the September 26 Full Moon, becomes a domiciled
Cancer root on October 2, squares Neptune 152.95 hours after the conjunction and
trines Mercury 57.27 minutes later. The square is 10.00 hours before the
Mars–Pluto opposition. Because a Moon–Neptune conjunction-to-square develops
every lunar cycle, it receives no rarity or convergence credit. It is retained
only because it shows the selected Full Moon's Neptune material moving through
the newly independent Moon into the record inside the already admitted
opposition clock.

The house stages sharpen the relay. At the Libra ingress, Mars is in the 4th,
Moon in the 11th and Saturn in the 1st: land/opposition, legislature/allies and
the national body are locked together. At the September Full Moon the
Mars–Moon loop occupies the 8th and 5th: debt/other people's money and
speculation/children. By the Capricorn ingress the five actors span the 8th,
11th, 4th, 7th and 3rd houses before returning to the Sun. This is a change in
the architecture of authority, not merely a change in the cast list.

### Declination becomes a normal relationship lane

The Saturn–Neptune longitude/declination counterpoint is admitted as a standing
continuity fact, not an exotic extra. Every governing comparison should check:

1. longitude relationship and immediate motion;
2. declination parallel/contra-parallel and whether it is tightening;
3. whether one dimension repeats, contradicts or cross-cuts the other; and
4. whether an equator crossing makes parallel and contra-parallel tests
   simultaneously true.

The equator case receives one labeled ambiguity state, never two interpretive
votes. The Libra ingress Sun opposing Neptune while paralleling it by 0.077
degrees is the model example: confrontation in zodiacal longitude and
co-presence in celestial latitude-equivalent declination.

The full-year human-facing audit is now preserved in [[THE SECOND SKY SPEAKS —
2026 DECLINATION CONTINUITY]]. It normalizes the thirty registered bones to 138
unique within-orb contacts, identifies the Mars–Pluto, Saturn–Neptune,
Jupiter–Pluto and solstice Sun–Pluto continuity arcs, and proposes a
hemisphere-first equator-crossing rule. That producer rule remains pending
Katie's disposition and has not been written into the generated chart bones.

### The zero-Libra seed-degree relay is a three-chart sequence

The September 26 MC contact is part of a repeating hinge, not an isolated hit:

| Chart point | Saturn–Neptune 2026 seed, 0°45 Aries | Jupiter–Saturn 2020 seed, 0°29 Aquarius | Saturn–Uranus 1988 first pass, 29°55 Sagittarius |
|---|---:|---:|---:|
| Libra ingress Sun, 0°00 Libra | opposition 0.753° | trine 0.486° | square 0.081° |
| Sep 26 Full Moon MC, 0°48 Libra | opposition 0.045° | trine 0.312° | square 0.879° |
| Oct 10 New Moon MC, 29°44 Virgo | opposition 1.023° | trine 0.757° | square 0.190° |

The seasonal zero-Libra degree is therefore carried from **the ingress Sun** to
**the Full-Moon MC** and then remains on **the next New-Moon MC**. It joins the
new Saturn–Neptune institutional/ideal seed to the Jupiter–Saturn
law/order/banking seed and the older Saturn–Uranus structure-versus-breakthrough
family. These are three historical clocks meeting one hinge; they are not three
independent confirmations of an outcome.

The Libra-ingress Ascendant contact also needs exact labeling. Its 1.489-degree
square is to the **first April 2020 Jupiter–Pluto pass** at 24°53 Capricorn, not
to that family's governed November display anchor at 22°52 Capricorn. A pass
variant may be meaningful, but it must never masquerade as the primary family
anchor or receive an extra vote.

### Planetary-node labels require a hypothesis fence

The September Full Moon exposed another calculated-but-unnarrated lane: Mars is
0.488 degrees from Saturn's geocentric osculating ascending node and perfects
that conjunction 21h24m after the Full Moon, before entering Leo and opposing
Pluto. An exact root audit widens the sequence:

`Jupiter NN Sep 11 → Pluto NN Sep 14 → Full Moon Sep 26 → Saturn NN Sep 27 →
Mars enters Leo → Mars–Pluto opposition → Neptune NN Oct 22`

This is one node corridor. Jupiter, Pluto and Saturn's north nodes are clustered
within 9.35 degrees of Cancer, so a Mars transit through Cancer necessarily
encounters them in order. They may describe a handoff among planetary functions;
they may not be counted as three independent confirmations. The thirty-chart
control contains thirty planetary-node hits and five Mars-node snapshots.

The older generated bones retain `flag: escalation` for Saturn/Pluto nodes and
`flag: resolution` for Neptune nodes. Those are inherited Jones hypotheses, not
observed event states. The Chronicle backtest found the Saturn/Pluto escalation
test null and the Neptune reduction result suggestive but small-n. Normal
analysis must therefore:

1. report the exact planet, node body, ascending/descending side, orb and epoch;
2. root-solve the exact crossing when timing materially matters;
3. deduplicate a cluster of node degrees into one corridor;
4. distinguish the orbital coordinate from a physical meeting; and
5. never translate the legacy flag into an event prediction or evidence vote.

The reproducible owner is `99 - Templates/mars_planetary_node_corridor.json`.

### Derivative turns describe actor-relative topology, not extra evidence

The Aries Full Moon sequence demonstrates the useful and dangerous sides of
derivative houses. Turning each chart from Mars preserves a remarkably stable
functional map from the Virgo New Moon through the Libra ingress and Full Moon:
Mercury 4H, Venus 5H, Jupiter 2H, Saturn–Neptune 10H, Uranus 12H and Pluto 8H.
At the Mars–Pluto opposition that map genuinely reroutes: Pluto 8H → 7H,
Jupiter 2H → 1H, Saturn–Neptune 10H → 9H, Uranus 12H → 11H, Venus 5H → 4H,
Moon 10H → 12H, while Mercury remains 4H.

The meaning is specific: leverage becomes a direct counterparty; resources are
identified with the force actor; office moves into law or doctrine; hidden
disruption emerges through networks; and the record remains foundational. But
the calculation is still a relabeling of existing Whole Sign placements. It
does not add bodies, aspects or independent votes.

The opposition and Last Quarter provide the necessary control. They are 2h46m
apart, all radical houses rotate together by one sign, and every Mars-derived
house remains identical. Apparent repetition created by uniform rotation must
therefore be deduplicated as one relative topology. The reproducible owner is
`99 - Templates/aries_mars_pluto_derivative_topology.json`.

### A missing configuration leg may be occupied earlier in the governing clock

The October 3 fixed T-square supplies the first admitted example. At its exact
clock, Mars in Leo opposes Pluto in Aquarius, Mercury in Scorpio squares both,
and 3°06′ Taurus in the 8th house is empty. But the governing Full-Moon Moon
crossed that future Taurus coordinate on September 28 and squared Pluto three
minutes later at 3°08′. Mercury squared Pluto at 3°07′ Scorpio on October 2;
Mars opposed Pluto at 3°06′ Leo on October 3. Pluto moved only 0.0319° while
the Taurus, Scorpio and Leo arms arrived.

Normal analysis may therefore test whether a later configuration's unoccupied
leg was traversed by a governing light or ruler earlier inside the same admitted
clock. The result must remain typed as a **temporal configuration relay**:

1. preserve each exact event time and its own chart frame;
2. state that the full figure is not simultaneous;
3. measure the common degree corridor and the anchor planet's real motion;
4. explain any geometrical dependence on an already admitted aspect; and
5. deduplicate the relay rather than awarding one vote per occupied arm.

In this case the Moon–Pluto square follows from the established Full-Moon
degree relay, so it adds chronology rather than convergence. It shows that the
future Taurus 8H outlet—shared resources, debt, dependency, mortality and the
other party's means—received the Moon before Mercury supplied the Scorpio
account and Mars supplied the Leo confrontation. The reproducible owner is
`99 - Templates/aries_mars_pluto_choreography.json` under
`temporal_fixed_cross_relay`.

The method must also preserve negative controls. Applying it symmetrically to
the Sun–Saturn–Moon cardinal figure finds a Capricorn passage inside the same
Virgo lunar month, but the exact Moon–Saturn square misses the later 11°23′
Capricorn missing-leg coordinate by 1.0166°. The full cardinal corridor is
1.1013°, more than 34 times wider than the fixed relay, and Moon–Saturn hard
contacts recur every lunar orbit. The admissible result is therefore only a
sign-level chronology—foundation, boundary, public/government consequence,
authority. A traversed sign without a strict degree pass may enrich sequence,
but it does not become an exact temporal configuration relay or receive an
additional convergence vote. The control is stored under
`temporal_cardinal_cross_control`.

### Exact configurations also have temporal chambers

An exact aspect chart is one instant inside an applying-and-separating
relationship. When several hard aspects form one configuration, normal analysis
may calculate the interval during which every required arm remains inside the
same strict orb. The chamber must use one declared orb policy, preserve each
directed arm and remain one relationship history rather than a count of
successive confirmations.

The October fixed T-square supplies the worked example. Mars–Pluto remains
within the strict one-degree opposition orb for 82.22 hours; Mercury remains
within one degree of square to Mars for 67.23 hours and to Pluto for 37.20
hours. The intersection runs from **October 1 at 10:14 p.m. through October 3
at 11:26 a.m. EDT**, a 37.20-hour chamber containing the Moon's maximum north
declination, Mercury's exact squares, the Moon's Cancer root change, Venus's
station, the Mars–Pluto opposition, the Cancer Last Quarter and the Moon–Saturn
closure.

The same producer tests the immediately prior Mars–Pluto cycle's three
opposition passes. None has a third planet simultaneously square both poles
within one degree at the exact clock; only the 2026 opposition has Mercury,
within 0.745° of both squares. The admissible statement is limited to that
four-chart control. It is not a universal rarity claim.

The method contract is:

1. choose the configuration and orb from an existing policy before inspecting
   the interval;
2. root-solve entry, perfection and exit for every required arm;
3. intersect those windows rather than adding their durations;
4. narrate root changes, stations or lunar phases inside the chamber only when
   they materially alter who carries the configuration; and
5. count the entire chamber as one configuration history with zero factual,
   causal or forecast credit.

The reproducible owner is `99 - Templates/aries_mars_pluto_choreography.json`
under `fixed_t_square_corridor`.

### First and last lunar dialogues may clarify the carrier

The Aries Full Moon audit found another useful calculated-but-unheard layer:
the Moon's complete sequence of exact major Aspects inside each sign. The
reproducible producer now computes conjunction, sextile, square, trine and
opposition from the workbook's Aspects tab between successive lunar ingresses.
This is a chronology lane, not a new scoring or rarity system.

The September 26–October 4 passage produces four distinct chapters:

- Aries opens with Moon–Neptune and closes with Moon–Mercury: image becomes
  record around the Full-Moon exposure;
- Taurus opens with Moon–Mars and moves through Pluto, Venus and Jupiter:
  material consequence encounters force, power, terms and law or finance;
- Gemini opens seven mostly flowing dialogues across the active system while
  the Moon is out of bounds: transmission has broad channels without becoming
  proof of ease or a favorable outcome; and
- Cancer opens with Neptune, proceeds through Mercury and Venus, perfects the
  Last Quarter with the Sun and closes with Saturn. It contains no exact major
  Moon–Mars or Moon–Pluto Aspect.

That Cancer silence changes the reading materially. Once domiciled, the Moon is
an independent public or protective root, but it is not another combatant in
the Mars–Pluto opposition. It carries image, record and terms into authority
and boundary while Mars and Pluto conduct their confrontation on a separate
track. The absence of direct lunar dialogue is as meaningful as a present
Aspect when the whole chart and exact chronology support it.

Normal analysis may therefore inspect a governing light's first and last exact
major Aspect inside a sign when the sign passage contains an admitted chart or
relationship clock. It must:

1. use the workbook's Aspect families rather than a flat generic orb set;
2. preserve exact ingress and perfection times and the independent clock owner;
3. compute the complete sequence before selecting an opening or closing contact;
4. narrate silence only in relation to the whole chart, never as a free-standing
   event forecast;
5. avoid calling the post-contact interval void of course unless a governed
   definition has first been chosen; and
6. deduplicate recurring lunar contacts as one carrier chronology with zero
   additive evidence or convergence credit.

The exact owner is `99 - Templates/aries_mars_pluto_choreography.json` under
`lunar_sign_chapters`. Registered Full Moon and quarter clocks override small
working-engine root differences; those differences remain disclosed rather
than becoming duplicate events.

The first corpus control now covers all **25** registered 2026 New and Full
Moons. It finds:

- Neptune is the first exact major lunar partner in eight sign chapters;
- Jupiter is the last partner in seven;
- the lunation itself is the first exact major dialogue three times, the last
  six times and an interior event sixteen times;
- exact major-dialogue counts range from three to eight, with seven charts
  matching the Aries Full Moon's count of seven;
- the Neptune-first/Mercury-last bracket occurs twice, at the June 29 Capricorn
  Full Moon and September 26 Aries Full Moon;
- the median last-contact-to-next-ingress gap is 9.18 hours, compared with 4.83
  hours for the Aries Full Moon; and
- fourteen lunation Moons make no exact major Aspect to the traditional ruler
  of their sign inside that sign passage.

These controls establish that neither a first/last partner, dialogue count,
closing gap nor sign-ruler silence is exceptional by itself. Rulership topology
must therefore never be paraphrased as direct Aspect dialogue. A planet can
rule or receive the Moon without perfecting a major lunar Aspect in that sign.

The Aries sequence supplies the worked boundary case. The Pisces Moon trines
Cancer Mars 1h51m before entering Aries. Mars and the Moon then form the Full
Moon's terminal mutual reception without another exact major Moon–Mars Aspect
inside Aries. Mars enters Leo and breaks the reception; the Moon enters Taurus
and squares Mars 31 minutes later. A governed reading may inspect such an
ingress-boundary handoff when a ruler contact occurs immediately before or
after the admitted sign chapter, but it must preserve the distinction:

`direct dialogue → sign/dispositor architecture → changed direct dialogue`

The transition is one relationship history, not three confirmations. Its
meaning comes from the changed reception, Aspect and chronology together. The
25-chart counts remain controls and supply no rarity, strength, political or
forecast credit. The reproducible owner is the same payload under
`lunation_sign_chapter_control` and `lunar_sign_chapters.aries_ruler_handoff`.

The same audit rejects two attractive overreads:

- Fortune and Spirit coincide in all **25** exact 2026 New/Full Moon bones—12
  New Moons and 13 Full Moons. At a syzygy the two formulas collapse to the
  same longitude modulo 360, so their equality at this Full Moon is algebraic,
  not an Aries-specific convergence.
- Degree symbols are available for every point. Selecting a resonant symbol
  after reading the sequence creates a large post-hoc fit surface. No Sabian or
  other degree symbol should enter Judgment without a preregistered target
  point and comparison rule.

## Normal-analysis contract adopted from this audit

Astronomy is now a required **consideration lane** for mundane readings. It is
not mandatory prose and it cannot overrule the whole chart. The author checks,
in order:

1. chart-grade geocentric positions, aspects, houses and angles;
2. broad heliocentric configuration and which body lies between which;
3. Washington true altitude kept separate from Whole Sign hemisphere and from
   naked-eye visibility;
4. Earth distance, light-time and solar elongation when visibility/nearness
   materially changes the hearing; for Mercury and Venus, preserve signed solar
   side, illuminated fraction, local twilight altitude and model assumptions
   rather than inferring visibility from longitude separation alone;
5. signed motion, station history and the next exact turn;
6. declination relationship; for the Moon, test bounded out-of-bounds entry,
   maximum and exit as one chronology rather than treating each enclosed event
   as a separate vote;
7. admitted planetary-node contacts with exact epoch, clustering and hypothesis
   fences;
8. derivative-house turns only when they materially clarify actor-relative
   function, with uniform-rotation repetitions explicitly deduplicated;
9. Lots with the syzygy identity controlled before interpreting equality, and
   degree symbols only under a preregistered selection rule;
10. inner-planet and lunation geometry relevant to chart shape; for a material
    lunar physical claim, keep distance/perigee, apparent diameter, isolated
    acceleration or tidal-gradient proxy, and Sun–Moon spring/neap phase
    geometry distinct; and
11. only when genuinely useful, gravitational acceleration and tidal
   differential as separately labeled physical quantities with absolute
   Moon/Sun scale and an explicit no-causation statement.

Moon-family lineage, quarter chapter, chart-shape regime, dispositor handoff and
long-clock seed contacts sit beside this lane as continuity instruments. They
may deepen Judgment. They never manufacture political evidence or convergence
credit. When the lineage begins with an eclipse, the family phase and the
eclipse condition must be audited separately by recording the true-node
distance and lunar ecliptic latitude at each admitted phase.

### The inner-planet solar-motion lane now has a full-year control

The first normalized implementation is preserved in [[The Inner Rulers Turn at
the Gates — 2026 Mercury and Venus Solar Motion]]. Its producer compares
Mercury and Venus across all twenty-nine registered 2026 ingress and New/Full
Moon charts without flattening longitude, solar phase, speed, shadow history or
Washington twilight geometry into one score.

The control finds only two registered charts within twenty-four hours of an
exact inner-planet station. The Aries ingress occurs 4.782 hours before its
Mercury chart ruler stations direct; the Cancer season's first Full Moon occurs
6.345 hours after root-member Mercury stations retrograde. Four snapshots meet
the Orrery's body-relative station corridor, and five lie within the declared
seventy-two-hour solar-conjunction hearing band. Those counts describe the fixed
chart sample rather than a random-calendar rarity model. Twilight altitude is
kept separate from modeled visibility, and superior/inferior conjunction is not
silently converted into a traditional combustion doctrine.

### The outer-planet physical lane now has a full-year control

The corresponding Mars-through-Pluto implementation is preserved in [[The
Basket Walks Through the Full Moons — 2026 Outer-Planet Physical Geometry]]. It
normalizes 174 outer-planet snapshots across the same twenty-nine registered
charts while keeping geocentric apparent position, heliocentric placement,
three-dimensional line geometry, Earth distance, isolated acceleration and
tidal-gradient proxy in separate fields.

The first whole-year finding is a Basket-scale light relay. The July 29 Full
Moon places Jupiter with the Sun only 2.297 hours after Jupiter's solar
conjunction while Moon–Pluto occupy the other side 55.681 hours after Pluto's
solar opposition. Then three alternating Full Moons traverse the slow vertices
in order: Pluto on July 29, Neptune on September 26 and Uranus on November 24.
The sixty-day cadence follows the approximately sixty-degree Basket spacing and
must remain one structured geometry rather than three independent votes. A
thirteen-Full-Moon control finds five strict five-degree solar-axis body hits
across four charts, including a January Mars control and both Jupiter and Pluto
in July.

The same dataset formalizes the spring-to-autumn Saturn–Neptune flip. At the
Aries ingress both bodies occupy the solar-conjunction side and their farthest
registered-chart distances. At the Aries Full Moon both occupy the opposition
side; Neptune is nearest in the sample and Saturn second-nearest. Their isolated
acceleration and tidal proxies increase by different amounts, but every record
retains Moon-relative absolute scale and the explicit rule that physical
magnitude is not astrological strength or causal evidence.

## Current boundary

The live vault sources and generated Orrery view are built and validated. The
human-facing quarter-Moon strip, late-year relationship history, full-year
shape/root continuity map, full-year declination audit, first inner-planet
solar-phase/visibility hearing, normalized full-year Mercury/Venus solar-motion
control, normalized full-year outer-planet physical-geometry control,
eclipse-geography audit and typed eclipse-
genealogy audit are now saved and discoverable in Astrology Files. The
visibility hearing distinguishes exact elongation and phase from a Washington-
specific naked-eye model, and it does not install a traditional combustion
doctrine. The genealogy audit distinguishes shadow series, date/degree echo and
seed-phase lineage without creating extra votes. The declination audit's
equator normalization remains proposed rather than adopted. Machine-readable
continuity ribbons, continuous visibility records and dedicated in-chart UI
remain future implementation. The desktop application has **not** been rebuilt,
signed, or installed; that remains a separately authorized governed ship step.
Motion or continuity facts do not create storyline ownership, evidence,
causation, forecast confidence, or a Forecast Ledger call.
