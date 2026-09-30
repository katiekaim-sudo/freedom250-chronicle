# Freedom 250 Mundane Astrology Organism — Design Mold

**Status:** working design mold  
**Opened:** 2026-08-11  
**Authority:** none; the live Freedom 250 vault and Katie's current rulings win  
**Donor:** Sentient Sun architecture snapshot captured 2026-08-11  
**Authorization:** Katie authorized full editing of this new mundane mold while
the natal Sentient Sun organism remains untouched

## Purpose

This package turns the reusable Sentient Sun organism chassis into a separately
governed mundane-astrology mold for Freedom 250.

The design is intentionally conservative about what must change. Mundane and
natal astrology use the same sky, chart geometry, aspects, dignity facts,
condition mechanics, and dispositor grammar. The principal semantic adaptation is:

```text
Planet -> author an independent mundane collective function and civic actor
Sign   -> reuse modality/element structure; govern the unique mundane expression independently
House  -> author an independent national, civic, or institutional arena
```

Archetypal continuity may be source evidence, but no natal Planet or Sign owner
is inherited as mundane authority.

The 2026-08-30 relationship-time amendment adds a second invariant:

```text
Planet -> stable archetypal motivation; never one fixed plot assignment
Pair   -> stable relationship identity with a changing developmental arc
Chart  -> one exact state of that relationship
Period -> a bounded view into the already-moving relationship history
```

Aries always resets the mundane year. Cancer, Libra, and Capricorn take over
only when the incumbent ingress's rising-sign validity term permits succession.
Neither kind of boundary restarts a synodic relationship. Retrograde motion may
reverse the directed hand, reopen an aspect, or create repeated exact passes;
chronological history still moves forward and every later passage retains its
own identity.

Aspect operators remain shared. The interface changes from a living-person
birth-chart shell to a mundane target, chart-event, locality, chart type, and
period shell.

## Read in this order

1. [Build handoff](MUNDANE_ORGANISM_BUILD_HANDOFF.md) — the durable restart
   document: current rulings, Observatory placement, authority boundaries,
   staged plan, release gates and exact next action.
2. [Circular reading build plan](CIRCULAR_READING_BUILD_PLAN.md) — the approved
   whole → part → whole architecture, thin-pass sequence, extension contract,
   Sabian-first example and circular-reading acceptance tests.
3. [Ongoing Planetary World design note](ONGOING%20PLANETARY%20WORLD%20%E2%80%94%20DESIGN%20NOTE%202026-08-31.md) — the
   continuous-motion model, relationship and declination histories, Orrery
   provenance, evidence fences, first Planetary Motion implementation receipt,
   and the 2026-09-24 astronomy-context, Moon-family political-reservoir and
   whole-reading pattern audit. The audit now fixes quarter Moons as supporting
   chapters and astronomy as a normal consideration lane, including a required
   eclipse-geography and horizon hearing. The exact Aries Full Moon to
   Mars–Pluto choreography now has a separate generated clock, house, command-
   circuit and real-motion receipt in
   `99 - Templates/aries_mars_pluto_choreography.json`.
4. [2026 Pattern Atlas — Reorientation Map](2026%20PATTERN%20ATLAS%20%E2%80%94%20REORIENTATION%20MAP.md) — the
   governed turn from technique-by-technique discovery to question-driven
   whole-chart synthesis, with eleven coverage domains, five pattern records,
   two priority rereads, a two-item missing-evidence queue, a completed
   thirty-chart reference-only packet index projected into the Astrology Hub,
   and a frozen pre-outcome AI/superintelligence observation contract for the
   Barbault Basket.
5. [[The Eclipse Meets the Horizon — Washington Visibility 2025–2026]] — the
   eight-event global/local audit separating exact syzygy, greatest eclipse,
   shadow path, Washington visibility, horizon state and physical scale.
6. [[The Shadow Has More Than One Ancestor — Saros, Metonic and Moon-Family
   Time]] — the eight-event recurrence audit separating shadow series,
   date/degree echo, Pessin seed-phase lineage and the six 2024–2026
   Saros–Metonic braids; the control layer also tests Mars command, all-planet
   house persistence and raw ten-planet distribution without a shape-family
   label.
7. [The Field Scatters, the Command Tightens](THE%20FIELD%20SCATTERS%2C%20THE%20COMMAND%20TIGHTENS%20%E2%80%94%202026%20CHART%20SHAPE%20AND%20ROOT%20CONTINUITY.md) — the
   corrected thirty-chart 2026 distribution and dispositor-root continuity map,
   including the first-half phase pulse, July break, late-year low-gap corridor,
   and the distinction between distributed consequence and recursive command.
   Named Jones/Meyer family labels are explicitly withheld because the current
   live owner is unopened.
8. [The Second Sky Speaks](THE%20SECOND%20SKY%20SPEAKS%20%E2%80%94%202026%20DECLINATION%20CONTINUITY.md) — the
   normalized full-year declination audit, exact working relationship roots,
   second-axis continuity arcs and provisional equator-crossing rule.
9. [Knowledge inventory](KNOWLEDGE_INVENTORY.md) — what Freedom 250 already
   knows, where it lives, and what is missing.
10. [Complete Planet review](MUNDANE_PLANET_OWNER_REVIEW.md) — all ten mundane
   Planet candidates, scope conditions, source divergences, and the exact
   Katie dispositions still required.
11. [Planet candidate registry](MUNDANE_PLANET_OWNER_CANDIDATES.json) — the
   machine-readable review packets; complete but deliberately non-authoritative.
12. [Planet owner mold](mundane_planet_function_owner.json) — the ten-record
   lifecycle and permission shell; every active revision remains closed.
13. [Sign and House review](MUNDANE_SIGN_AND_HOUSE_OWNER_REVIEW.md) — all twelve
   Sign and twelve House candidates, their structural inputs, source tensions,
   and Katie decisions.
14. `MUNDANE_SIGN_OWNER_CANDIDATES.json` and
   `MUNDANE_HOUSE_OWNER_CANDIDATES.json` — machine-readable review packets.
15. `mundane_sign_owner_registry.json` and
   `mundane_house_owner_registry.json` — closed twelve-record lifecycle shells.
16. [Organism design](MUNDANE_ORGANISM_DESIGN.md) — the shared-versus-mundane
   boundary, identities, interface, owners, and build sequence.
17. [Machine-readable mold](mundane_method_atlas.json) — the first authored
   mundane atlas: ten Planet references, twelve Signs, twelve Houses, shared
   Aspects, chart types, scopes, owner families, gates, and interface workspaces.
18. `validate_mundane_mold.py` — read-only structural validator for the mold and
   all three complete candidate/owner boundaries.

## Authority and source boundary

The live source spine is:

1. `00 - Index/DECISION LOG.md` for binding rulings.
2. `00 - Index/Reading the Charts — START HERE.md` for method and Judgment.
3. `00 - Index/Mundane Astrology Reference — Katie's Method.xlsx` for atomic
   lookup facts.
4. `00 - Index/Mundane Astrology — Master Reference.md` for the living source
   synthesis and dictionary.
5. Calculation code and generated dossiers for reproducible facts and runtime
   coverage, never semantic authority by themselves.
6. Worked readings and study notes as examples and provenance.

This package does not replace any of those sources. It makes their ownership
and interfaces explicit enough to build against.

## What is already built rather than being reinvented

- exact chart calculation through the existing Freedom 250 engines;
- tropical geocentric coordinates and Whole Sign Houses;
- aspect geometry and canonical relationship identity;
- dignity, condition, angularity, retrogradation, combustion, and stations;
- traditional rulership and dispositor-chain mechanics;
- ingress, lunation, eclipse, radix, event, return, progression, midpoint,
  declination, planetary-node, derivative-house, and 916 America machinery in
  varying states of integration;
- the Sentient Sun projection, navigation, owner, fail-closed, and validation
  patterns.

## What this design adds

- a mundane target and chart-event identity contract;
- an explicit registry of the chart types Freedom 250 actually uses;
- a period-skin that relates intact charts without blending them;
- independent mundane Planet owners, twelve independent Sign owners, and twelve
  independent House owners;
- shared Aspect ownership rather than duplicate mundane geometry;
- explicit boundaries between facts, semantic contribution, whole-chart
  Judgment, civic Translation, and optional Forecast Ledger calls;
- a first-class planetary relationship-time owner separating stable pair
  identity, instantaneous state, ordered pass history, and bounded period
  projections without granting any pair fixed plot ownership;
- a full-year human-facing continuity map that reads chart-shape regimes and
  dispositor circuit handoffs together without turning either into automatic
  Judgment;
- a normalized full-year declination continuity audit that keeps its proposed
  equator-crossing rule outside generated facts until Katie reviews it;
- an authored eclipse-geography companion plus reproducible local-circumstance
  producer that keeps syzygy, greatest eclipse, global path, Washington horizon
  and chart interpretation distinct;
- a machine-readable mold with structural validation.

## Current boundary

This is a design and semantic mold, not yet a runnable app fork. The separate
live method now owns the 2026-08-30 relationship-time doctrine; this package
now also owns authored full-year shape/root and declination continuity
companions and the 2025–2026 eclipse-geography hearing. The declination equator
rule remains a proposal. The eclipse local-circumstance dataset is a factual
projection, not a semantic owner. The package activates no live semantic owner,
Sentient Sun owner, generated chart, app instrument, pair roster, or forecast.
The ten Planet, twelve Sign, and twelve House candidates are ready for Katie's
**keep / revise / reject / hold** review. No meaning can load at runtime until a
kept candidate receives a validated immutable revision and promotion receipt.
App extraction follows semantic ratification rather than preceding it.
