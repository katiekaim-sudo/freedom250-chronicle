# Freedom 250 Mundane Organism — Design

## Design ruling

The mundane organism is a sibling specialization of the Sentient Sun organism,
not a renamed natal reader and not a greenfield astrology engine.

Its semantic delta is deliberately small:

| Layer | Disposition |
|---|---|
| Astronomy, zodiac coordinates, angles, Whole Sign frame | Reuse or adapt existing factual owners |
| Aspect geometry and operator meanings | Share |
| Planetary relationship identity, phase, relative motion, and exact-pass history | Reuse calculated facts; add a first-class continuous relationship-time owner |
| Traditional dignity and rulership facts | Share |
| Condition and dispositor mechanics | Share; rewrite civic Translation only |
| Projection, navigation, identities, gates, validation | Extract and adapt |
| Planet meanings | Author independent mundane collective-function owners |
| Sign meanings | Author twelve independent mundane expressions using Modality and Element as structural inputs |
| House meanings | Author twelve independent national, civic, and institutional arenas |
| Subject and chart intake | Replace with mundane target/event/locality/technique identity |
| Time container | Add a period-skin that references intact charts and bounded slices of continuous relationship histories |
| Judgment and Translation | Build as new mundane owners |
| Forecast | Route separately to the existing Forecast Ledger |

## Mundane Sign construction

Signs are close to universal, but mundane work gives their two structural axes
more interpretive weight:

```text
Modality supplies the movement.
Element shapes and carries the movement.
The unique Sign is the collective expression of both at once.
```

### Modality — movement supplied

- **Cardinal:** opens a phase, mobilizes available material, and establishes direction across a threshold.
- **Fixed:** consolidates what has formed and sustains its continuity, concentration, and development.
- **Mutable:** modifies, redistributes, or releases an established phase toward transition.

### Element — movement shaped

- **Fire:** ignition and animation.
- **Earth:** practical and material reality.
- **Air:** thought and exchange.
- **Water:** emotion and feeling.

These are candidate owner definitions for Katie's review. They are not a
four-by-three keyword generator. Aries, Cancer, Libra, and Capricorn all
initiate, but what they initiate differs because fire, water, air, and earth
shape the motion differently. The same irreducibility holds across every row
and column of the zodiac.

## Dignity as a separate condition owner

Dignity describes the **condition or fit of the Sign-supplied tools for
the Planet using them**:

- domicile or exaltation: fitting or especially capable tools for the actor's
  mundane function;
- detriment or fall: awkward, contrary, or costly tools; the actor's motivation
  remains intact;
- neutral: no special traditional dignity condition is asserted.

Dignity is not a strength score, importance score, or whole-chart verdict.
Angularity, dispositorship, tight relationships, and the final whole-chart job
own prominence separately. A Planet in fall may still run the chart.

## Two scopes, not one giant multichart

### Continuous relationship-time layer

Planets keep their archetypal motivations; they do not receive fixed plot
assignments. The pair is a stable relationship identity whose exact condition
changes through time.

```text
relationship_ref
+ seed_family_ref and exact pass_ref, where applicable
+ relationship_state_ref keyed by exact astronomical instant and calculation frame
+ ordered transition history
= one continuous relationship arc
```

Each `relationship_state_ref` records the computed phase or governed exception,
direct aspect and orb, and immediate relative motion for one pair at one exact
instant under one coordinate/ephemeris frame and engine version. Charts and
snapshots reference that state; co-temporal charts may share it while retaining
their own chart, snapshot, locality, and house-frame identities. Different
instants always receive different state identities. The history orders entries,
exits, perfections, separations, reapplications, phase boundary crossings, and
repeated exact passes. Retrograde motion may reverse the directed hand or reopen
a prior geometric condition, but it never reuses an earlier state or pass
identity and never reverses chronological history.

The shared astronomical state does not own chart-dependent narration. Each
chart observation adds a separate projection with three independent lanes:

1. **Direct geometry visibility** — the five-Aspect dialogue remains visible
   whether or not phase prose is admitted.
2. **Phase narration admission** — admit or withhold prose under DR-020 and
   record the exact ground: chart root, chart ruler, outer-pair era exception,
   or exact governed U.S.-natal contact.
3. **Seed echoes** — retain separate chart-point-to-seed-family references that
   neither manufacture direct geometry nor grant phase narration.

Co-temporal charts may therefore reference the same `relationship_state_ref`
while receiving different phase-narration decisions.

The whole-chart Aspect web retains all six adopted operators, including
quincunx. The narrower relationship-clock direct-dialogue policy admits only
conjunction, sextile, square, trine, and opposition, with `null` when none is
active. This prevents a whole-chart quincunx from silently becoming a governed
relationship-clock direct dialogue.

This owner crosses chart and period boundaries without blending them. Aries
always resets the mundane year; non-Aries cardinal ingresses succeed only under
the incumbent governor's rising-modality validity rule. Every ingress observes
the relationship already in motion, and none resets the synodic history. Pair-to-story use is
many-to-many. No relationship owns a plot, supplies factual Evidence, or gains
Forecast authority merely because its arc is continuous.

A plotline braid is a chart/period interpretation projection, not shared
astronomical state and not a new Evidence object. It may reference several
`relationship_state_ref` values only with an explicit non-duplicative role
(`lead_mechanism`, `co_mechanism`, `supporting_context`, `outcompeted`, or
`unresolved`) and presence mode (`inherited_substrate`, `active_dialogue`, or
`seed_echo`). The projection must retain its factual cutoff, governing chart
checkpoint, win/lose test, continuity case, and counterevidence. Several
symbolic fits never add votes or forecast confidence. A long-cycle condition,
faster carrier, and lunation/eclipse visibility may form one useful tested
braid, but the organism must not hard-code that sequence as a universal
hierarchy.

### Single-chart skin

One chart-skin owns one chart produced by exact inputs:

```text
target
+ chart-producing event
+ clock authority
+ observer locality
+ technique
+ coordinate and house-frame policy
= immutable chart snapshot
```

Identity fields:

- `target_ref`: the nation, government, institution, entity, city, or event
  whose affairs are being read;
- `event_ref`: the ingress, lunation, eclipse, founding act, filing, deadline,
  return, progression epoch, or other chart-producing event;
- `clock_ref`: exact, noon-daytime proxy, or midnight-date-only authority;
- `locality_ref`: the observer/casting locality;
- `technique_ref`: the chart technique;
- `chart_ref`: stable chart identity;
- `snapshot_ref`: immutable facts for exact inputs and engine version;
- `house_frame_ref`: exactly one Whole Sign house owner for that snapshot.

A target is not a chart. A chart-producing event is not the target. A locality
is neither of them.

### Period-skin

A period-skin is a bounded historical-weather container:

```text
continuous planetary relationship arcs
-> bounded relationship-clock slice
-> era context
-> governing ingress
-> lunation sequence
-> eclipse and Moon-family context
-> national/entity/founding-chart contacts
-> institutional and factual clocks
-> observed events
```

It stores typed references and role relations, never copied chart payloads.
Every member chart remains independently identified and calculated.

Required period roles:

- `relationship_clock_slice`
- `era_driver`
- `governing_ingress`
- `trigger_lunation`
- `eclipse`
- `anchor_radix`
- `entity_chart`
- `return_or_progression`
- `institutional_clock`
- `observed_event`

This preserves the project's nested time method without creating a blended
pseudo-chart.

## Mundane chart-type registry

### Core weather charts

- cardinal solar ingress;
- exact New Moon;
- exact Full Moon;
- solar eclipse;
- lunar eclipse.

### Receiving bodies and anchors

- national radix;
- governmental, institutional, corporate, or other entity radix;
- city or jurisdiction founding chart;
- event or activation radix.

### Event-clock charts

- exact event;
- filing;
- legal or administrative deadline;
- live transit instrument.

### Adopted specialist techniques

- solar return;
- secondary, tertiary, or minor progression;
- profection;
- major conjunction/cycle seed;
- Zain declination Cycle.

Every chart type declares whether it may own Houses, which locality rule it
uses, what clock precision it requires, and which period roles it may fill.

## Owner map

The first mold needs fewer new owners than a wholesale fork would suggest.

### Shared/adapted factual owners

1. Target, event, clock, and locality identity
2. Coordinate frame and body positions
3. Whole Sign house frame
4. Exact ASC, DSC, MC, and IC points
5. Aspect relationships and whole Aspect web at one snapshot
6. Continuous planetary relationship identity, phase, motion, seed-family,
   pass, and ordered transition history
7. Traditional dignity and rulership
8. Condition facts
9. Dispositor edges and root classification
10. Optional specialist geometry: declination, midpoints, lunar nodes,
    planetary nodes, non-pair phase clocks, and 916 America

### Mundane semantic owners

11. Mundane Planet functions
12. Twelve independent mundane Sign expressions
13. Twelve independent mundane House arenas
14. Planet-Sign contribution
15. Chart-specific relationship observation: direct geometry, DR-020 phase
    narration admission, and separate seed echoes
16. Chart-specific Planet-in-House context
17. House governance and civic actor routing
18. Whole-chart structural synthesis

### Period owners

19. Era context
20. Ingress governance
21. Lunation trigger
22. Eclipse and Moon-family lineage
23. Radix/entity overlay contacts
24. Bounded relationship-clock slices and cross-frame arc continuity
25. Period membership and relations
26. Chronicle event bridge

### Reasoning and speech owners

27. Candidate claim formation
28. Evidence-family and counterevidence accounting
29. Whole-chart or whole-period Judgment
30. Symbolic reading
31. Civic Translation
32. Optional Forecast Ledger registration

The owner numbers are design addresses, not an execution sequence and not a
claim that every owner is already implemented.

## Interface mold

The mundane interface keeps the donor's whole-to-part-to-whole behavior and
changes what the shell selects.

### Lobby

The Lobby asks:

1. What target or period are we studying?
2. Which chart type or saved period do we want?
3. What chart-producing event and clock authority apply?
4. Which locality and house-frame rule apply?

There is no default "today" chart.

### Mundane Chart Room

Suggested cabinets:

- Identity, event, clock, and locality
- Wheel and exact frame
- Civic actors — Planets
- Operating fields — Signs
- National arenas — Houses
- Relationships — current Aspect web and relationship arcs through time
- Condition and dignity
- Rulership, governance, and root
- Specialist geometry
- Whole-chart structure
- Technical proof and coverage

### Period Weather Room

Suggested cabinets:

- Era tide
- Relationship arcs through time
- Governing ingress
- Lunation sequence
- Eclipse and Moon-family lineage
- National/entity contacts
- Institutional and factual clocks
- Observed events
- Candidate claims and Evidence
- Registered calls

Selecting a period member opens that member's intact Chart Room. It does not
load its facts into the period as a second house frame.

### Organism

The Organism view shows owner rooms, built/documented/unbuilt states,
dependencies, invalidation, and the permission boundary between fact,
semantics, Judgment, Translation, and Forecast.

## Navigation and identity invariants

- Changing focus never changes chart facts or relationship counts.
- One Aspect has one canonical identity everywhere it appears.
- One planetary pair has one stable relationship identity, while every
  time-indexed state and exact pass retains its own identity.
- One chart snapshot has exactly one Whole Sign house-frame owner.
- A comparison selects one displayed house frame; overlay angles are markers.
- A period references charts; it never silently merges them.
- A period references a bounded relationship-history slice; it never resets or
  copies the continuous arc.
- Doors carry navigation, not meaning, Evidence, or votes.
- Every traversal stack frame retains period, chart, snapshot, and selected
  subject identity.
- Missing mundane content returns `unresolved`; it never falls back to natal
  wording.

## Execution boundary

```text
verified inputs
-> immutable calculated chart facts
-> mundane Planet/Sign/House owners
-> shared Aspect and condition relationships
-> continuous relationship state and ordered history
-> chart-specific contribution packets
-> whole-chart structural packet
-> period relations where applicable
-> candidate claims
-> Evidence and counterevidence accounting
-> Katie keep / revise / reject / hold
-> symbolic reading and civic Translation
-> optional separate Forecast Ledger call
```

The Chronicle event record remains independent. Astrology never decides what
deserves factual capture, and temporal co-occurrence alone grants no Evidence.

## Dependency and invalidation rules

- A corrected clock, locality, target, technique, or house-frame rule
  invalidates the affected chart snapshot and its downstream products.
- A changed Planet, Sign, or House meaning invalidates dependent semantic
  packets and Judgment, not astronomy.
- A changed Aspect presentation invalidates no Aspect fact.
- A corrected seed-family, phase, relative-motion, or pass fact invalidates the
  affected relationship history and its period projections, not Planet owners
  or unrelated chart snapshots.
- A changed ingress-validity rule invalidates period governance and membership,
  not the member chart snapshots.
- A corrected event record invalidates its associations and Evidence uses, not
  the sky calculation.
- A changed Freedom 250 arc map invalidates the arc adapter only.
- A UI or navigation change invalidates no astrology.

## First implementation sequence

1. Ratify the ten Planet, twelve Sign, and twelve House atoms already seeded in
   the machine atlas.
2. Extract the donor's semantic-closed identity, projection, navigation, room,
   node, door, and validation primitives into a mundane namespace.
3. Connect a single-chart shell to existing Freedom 250 calculation owners.
4. Implement the chart-type registry and one-house-frame rule.
5. Connect one continuous relationship history to its exact chart-state
   projections without assigning it a plot.
6. Build the Period Weather Room as a reference-only container with a bounded
   relationship-clock slice.
7. Add Planet-Sign and chart-specific Planet-in-House context packets with fail-closed
   semantics.
8. Add whole-chart structure before opening Judgment or prose.
9. Open the three speech levels separately; keep Forecast Ledger registration
   optional and falsifiable.

The first useful release is one complete mundane chart plus one inspectable
governing period. It need not automate a reading to be a successful organism.

## Concrete donor-to-mundane file map

The next implementation should create a new namespace and adapt these existing
pieces rather than starting from blank files:

| Mundane target | Existing donor or owner | Action |
|---|---|---|
| `mundane_method_atlas.json` | Sentient Sun atlas schema + this design mold | Preserve schema discipline; replace natal semantic content |
| `mundane_chart_projection.py` | Sentient Sun `chart_projection.py` | Extract canonical identity, registry, transition, focus, and whole-return mechanics |
| `mundane_chart_adapter.py` | Freedom `mundane_engine.py`, `mundane_dossier.py`, and chart conventions | Normalize existing calculations into typed chart records; do not recalculate astronomy |
| `mundane_period_adapter.py` | Freedom ingress/lunation/eclipse/lineage builders plus governed planetary relationship clocks | Assemble reference-only period membership, relations, and bounded relationship-history slices without copying or resetting the source arcs |
| `mundane_live_data.py` | Typed donor packet patterns | Compile mundane identity-bound facts and coverage states; do not fork `wheel_live_data.py` wholesale |
| `mundane_assemble.py` | Sentient Sun assembler/build-gate pattern | Validate schema, source/generated boundaries, and output names |
| `App/Freedom 250 — Mundane Living Chart (TEMPLATE).html` | Generic Living Chart template | Retain Lobby/Chart Room/Organism projection behavior; replace natal intake and add Period Weather Room |
| `mundane_chart_app.py` | Sentient Sun no-save `/living-chart` shell | Rebind route, payload, template, names, and adapters |
| `validate_mundane_project.py` | Donor validation-lane pattern + Freedom doctors | Add source-only, focused, and release gates without mutating the vault by default |

The donor's generated payloads, named fixtures, private renderers, natal adapter,
and monolithic natal compiler are not implementation shortcuts. The reusable
assets are the stable contracts and small generic primitives beneath them.
