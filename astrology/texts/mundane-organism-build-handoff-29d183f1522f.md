# Freedom 250 Mundane Astrology Organism — Build Handoff

**Handoff date:** 2026-08-11  
**Package state:** working design mold; implementation has not begun  
**Authority:** none; Katie's current rulings and the live Freedom 250 vault win  
**Target product:** a separately governed Mundane Living Chart instrument inside
Freedom 250 Observatory  
**Natal donor boundary:** Sentient Sun remains untouched and authoritative only
for its own natal organism

**Relationship-time amendment:** 2026-08-30 — Katie confirmed that Planets
retain archetypal motivations without receiving fixed plot assignments; their
relationships carry changing arcs through continuous time.

## Executive decision

Build the mundane organism into Freedom 250 Observatory.

It is not too large for the Observatory because it will be one deep,
lazy-loaded instrument rather than another top-level application or a flat set
of new tabs. Its proposed home is:

```text
Freedom 250 Observatory
└── Sky & Charts
    └── Workbench
        └── Mundane Living Chart
            ├── Lobby
            ├── Mundane Chart Room
            ├── Period Weather Room
            └── Organism / Method
```

At the time of this handoff, the live Sky & Charts registry contains fourteen
intact instruments; the older DR-043 decision text still describes its original
thirteen-instrument state. Mundane Living Chart would currently become the
fifteenth. It must be registered as a separate child instrument, loaded only
when selected, and remain directly addressable. It must not become a second
Observatory Home or a new source of astrological authority.

The existing Ingress Charts, American Charts, World Charts, Lunar Weather, Moon
Families, Transit Weather, Chart Comparison, Derivative Houses and other tools
remain intact. They should eventually offer governed **Open in Mundane Living
Chart** routes after each source child exposes a stable typed chart or period ID
and Sky & Charts gains a governed message action and resolver. Visible labels or
copied embedded payloads cannot serve as identity. The organism then reads the
selected object by canonical reference; it does not replace the source tool's
job or duplicate its calculations.

## Why this is the right fit

Freedom 250 already contains the mundane method, chart engines, time ladder,
national and entity charts, event clocks, timing instruments, worked readings,
and the Chronicle evidence system. The missing object is the deep-reading
environment that keeps all those parts visible as one governed astrological
organism.

Sky & Charts already solves the interface-size problem through job-based
progressive disclosure, search, remembered state and lazy loading. The organism
is therefore **deep rather than broad**: its internal complexity appears only
after Katie enters the instrument and opens the relevant room or cabinet.

## What has already been produced

This package currently contains:

1. `README.md` — package router and authority boundary.
2. `CIRCULAR_READING_BUILD_PLAN.md` — the approved whole → part → whole reading
   architecture, thin-pass build sequence, extension framework and acceptance
   tests.
3. `KNOWLEDGE_INVENTORY.md` — source map, doctrine inventory, semantic
   conflicts and runtime gaps.
4. `MUNDANE_ORGANISM_DESIGN.md` — architecture, identities, owner families,
   interfaces, gates and initial implementation sequence.
5. `mundane_method_atlas.json` — machine-readable v1 mold.
6. `validate_mundane_mold.py` — read-only structural validator.
7. This handoff — operational restart and implementation plan.

The atlas currently validates:

```text
10 Planets
12 Signs
12 Houses
3 Modalities
4 Elements
6 currently declared shared Aspect operators
17 chart types
18 owner families
```

This is structural coverage, not a claim that all semantics are ratified or
that a runnable application exists.

## Katie's rulings and provisional design consequences

The separation of mundane from natal astrology, the direction of the Planet,
Sign and House adaptation, the modality/element emphasis, dignity as Sign
condition, and the overall shared-Aspect boundary are Katie's rulings. Exact
field schemas and candidate semantic wording remain provisional until their
Phase 0 disposition.

### The mundane and natal organisms are separate

Mundane astrology and personal astrology use the same sky but ask different
questions. The new organism is a sibling specialization, not a mode switch
inside Sentient Sun and not a renamed natal reader.

### Reuse the chassis; rewrite the mundane meaning

The Sentient Sun donor contributes architecture: identities, rooms, navigation,
owner separation, reversible focus, validation, source/generated boundaries
and build gates. Natal semantic content does not become mundane content merely
because the schema is reusable.

### Planets

Author each mundane Planet owner independently. Archetypal continuity may be
source evidence, but no natal Planet wording or owner is inherited. The adopted
owner must state the collective motivation, civic actor or function,
institutional expressions, gift, shadow and mundane translation. A Planet is
the actor or motivating function, not the arena.

### Signs

Modality and Element classifications are highly reusable astrological
structure, but every mundane Sign is an independently governed owner. Mundane
readings place more weight on its two structural inputs:

```text
Modality supplies the movement.
Element shapes and carries the movement.
The unique Sign is the irreducible collective expression of both.
```

Shared modality and element facts constrain and inform twelve distinct governed
Sign records or foundations under the Sign owner family; they do not generate
or authorize their semantics. The Signs are not produced by joining one
modality keyword to one element keyword. Natal prose is neither an input nor a
fallback for mundane Sign meaning.

### Houses

Each House is independently authored as a national, civic, institutional, and
collective arena.
Whole Sign Houses remain the governed frame. Exact ASC, DSC, MC and IC remain
points and do not silently redefine the complete Houses.

### Aspects

Aspect geometry and operator meanings remain shared. Mundane work changes the
actors at the endpoints and the civic translation of their relationship; it
does not create a second square, trine or opposition.

### Relationships through time

The organism must not confuse a Planet's enduring motivation with permanent
ownership of a story. A Planet may serve several plots at once, and each plot
may recruit several planetary relationships. Pair-to-story use is many-to-many.

One pair retains one stable `relationship_ref`. A `relationship_state_ref` is
keyed by that pair, the exact instant, coordinate/ephemeris frame, and engine
version—not by the observing chart. It contains the phase or governed
exception, current governed relationship-clock Aspect and orb, and immediate
relative motion. Charts and snapshots reference the state; co-temporal charts
may share it while retaining distinct chart, snapshot, locality, and house-frame
identities. Different instants always produce different states. Seed families
and every exact pass retain their own identities. The ordered history records
entry, perfection, separation, reapplication, phase-boundary crossings, and
later returns.

The chart observation keeps the Long Clocks' three lanes independent. Direct
five-Aspect geometry remains visible regardless of narration. Phase prose is
admitted or withheld per chart under DR-020, with the exact ground recorded as
chart root, chart ruler, outer-pair era exception, or exact governed U.S.-natal
contact. Seed echoes remain a third projection and cannot create a direct
Aspect or phase-narration permission. Two co-temporal charts may therefore share
one astronomical state while receiving different phase-narration decisions.

The whole-chart Aspect web keeps its six adopted operators, including quincunx.
The relationship-clock direct-dialogue roster is narrower: conjunction,
sextile, square, trine, and opposition, with `null` when none is active. A
quincunx may remain visible in the whole Aspect web; it does not silently become
a governed relationship-clock direct dialogue.

Retrograde motion may reverse the directed hand or reopen a geometric
condition, but historical time never runs backward. A later pass is a new
encounter carrying the history accumulated since the earlier one. Aries always
resets the mundane year; Cancer, Libra, and Capricorn succeed only when the
incumbent ingress's rising-sign validity term permits it. Neither kind of
boundary resets a synodic relationship. The Period Weather Room therefore
references bounded slices of continuous relationship histories rather than
beginning them at the ingress.

A plotline braid belongs in a chart/period interpretation projection, never in
the shared relationship state and never as Evidence. Each strand must name one
non-duplicative role (`lead_mechanism`, `co_mechanism`, `supporting_context`,
`outcompeted`, or `unresolved`) and one presence mode
(`inherited_substrate`, `active_dialogue`, or `seed_echo`). Retain the factual
cutoff, governing checkpoint, win/lose test, continuity case, and
counterevidence. Multiple symbolic matches never add convergence or forecast
confidence. Long-cycle condition → faster carrier → lunation/eclipse
visibility is an available hypothesis, not a hard-coded hierarchy.

### Dignity and condition

Dignity describes the condition or fit of the Sign-supplied equipment for the
Planet using it:

- domicile indicates a native operating condition and exaltation an elevated
  or specialized operating condition;
- detriment and fall indicate awkward, contrary or costly tools;
- neutral records no special essential-dignity classification; it does not
  imply that the Planet's overall condition is neutral.

Dignity is not a strength score, importance score, prominence score or final
Judgment. A Planet in fall may still govern the chart. Angularity,
dispositorship, exact relationships and whole-chart structure may contribute
visibility or structural prominence; only Judgment assigns materiality,
hierarchy or final job.

### Judgment, Translation and Forecast

These remain separate permissions:

1. symbolic mundane reading;
2. concrete civic Translation;
3. optional falsifiable Forecast Ledger call.

Astrological structure does not automatically become prose, and prose does not
automatically become a forecast. Katie's disposition gate is
`keep / revise / reject / hold` after a complete candidate answer and its
deterministic validation receipt.

## Authority and product boundary

The durable ownership chain should be:

```text
Katie's ruling + Decision Log
→ governed method and semantic owners in the live vault
→ machine-readable mundane method atlas
→ existing factual calculation owners and mundane adapters
→ deterministic validation and assembly gate
→ generated canonical Mundane Living Chart child view
→ Sky & Charts lazy-loaded host
→ sync_observatory_app.sh staging
→ governed Tauri build and install
→ frozen Mac app projection
```

The boundaries are non-negotiable:

- The Research Workbench package is design evidence until selectively promoted.
- The live vault owns adopted method and semantics.
- Calculation modules own reproducible facts, not meaning by themselves.
- Generated JSON and HTML are products, never semantic owners.
- The Observatory is a projection and retrieval surface, never a second vault.
- The packaged app is a frozen governed projection of the vault build.
- Sentient Sun continues to own natal astrology only.

Before implementation starts, choose exact vault destinations for the adopted
mundane atlas, semantic owner documents and implementation code. Do not make
the Workbench package a hidden runtime dependency.

## Product topology

### Lobby

The Lobby establishes the exact object being studied:

- target nation, government, institution, entity, jurisdiction or event;
- chart-producing event;
- chart type or saved governing period;
- clock authority and precision;
- casting locality;
- technique and coordinate policy;
- one Whole Sign house frame where the technique permits Houses.

There is no default-today chart and no silent noon fallback where exact time is
required.

### Mundane chart-type registry

The intake must name the actual mundane technique rather than offer a generic
natal-shaped chart selector. The first registry contains:

- **Core weather:** cardinal ingress, exact New Moon, exact Full Moon, solar
  eclipse and lunar eclipse.
- **Receiving bodies and anchors:** national radix, entity radix and founding
  chart.
- **Event clocks:** event chart, filing chart, deadline chart and live-transit
  instrument.
- **Specialist techniques:** solar return, progression, profection, exact major
  conjunction/perfection chart and declination Cycle chart.

U.S. national mundane weather uses Washington, D.C. angles. National, entity
and founding radices retain the source-governed birthplace or foundation-place
rule. Every registry entry declares its clock precision, locality policy,
whether it may own Houses and which period roles it may fill.

A governing period is a reference container, not an eighteenth chart type. An
exact outer-planet conjunction/perfection may own a chart, but DR-003 requires
the cycle to be tested through its complete co-presence window. That window and
its repeated perfections belong to Period Weather; exactness alone is never the
cycle test.

### Mundane Chart Room

The Chart Room owns one immutable chart snapshot. Its proposed cabinets are:

- identity, event, clock and locality;
- wheel and exact frame;
- civic actors — Planets;
- operating fields — Signs;
- national arenas — Houses;
- relationships — current Aspect dialogue and continuous relationship history;
- condition and dignity;
- rulership, governance and root;
- specialist geometry;
- whole-chart structure;
- technical proof and coverage.

Focus changes what is visible, never what is true. One Aspect has one canonical
identity everywhere it appears. One chart snapshot has exactly one Whole Sign
house-frame owner.

### Period Weather Room

A period is not a giant multichart. It is a bounded reference container:

```text
continuous planetary relationship arcs
→ bounded relationship-clock slices
→ era context
→ governing ingress
→ lunation sequence
→ eclipse and Moon-family context
→ national/entity/founding-chart contacts
→ institutional and factual clocks
→ observed Chronicle events
```

Each member chart remains independently identified and calculated. Selecting a
member opens its intact Chart Room. The period stores typed references and
relations rather than copied chart payloads or blended house frames.

The required first period container is intentionally small:

- `period_ref`, target, locality and bounded interval;
- one governing-ingress reference;
- ordered member-chart references;
- bounded relationship-history references and each member chart's exact
  relationship-state references;
- typed `governs` and `triggers` relations.

Era drivers, eclipse and Moon-family lineage, national/entity overlays,
institutional clocks, the Chronicle event bridge and a saved-period library are
optional later adapters. The first useful period does not wait for all of them.

### Organism / Method

The technical organism exposes:

- semantic and factual owners;
- built, documented, unresolved and unbuilt states;
- dependencies and invalidation;
- navigation and relationship identities;
- fact, semantic, Judgment, Translation and Forecast permissions;
- source provenance and validation receipts.

The human-facing answer should lead. Machine state and proof belong beneath
progressive disclosure rather than dominating the reading experience.

## Reuse and rewrite map

### Reuse or adapt

- astronomical coordinates and chart mathematics;
- tropical zodiac and Whole Sign frame;
- exact angles and point identities;
- Aspect geometry, operator identities, applying/separating facts and whole-web
  mechanics;
- stable planetary-pair identity, phase geometry, relative motion, conjunction
  families, exact passes, and ordered relationship-transition history;
- traditional rulership and essential-dignity facts;
- condition, retrogradation, stations and solar proximity mechanics;
- dispositor-chain structure;
- projection, room, focus, traversal and whole-return mechanics;
- source snapshots, validators, atomic builds and release gates;
- existing Freedom 250 ingress, lunation, eclipse, national/entity and timing
  calculators.

### Rewrite or newly govern

- mundane Planet functions and civic actors;
- collective Sign presentation and its modality/element emphasis;
- all twelve national and institutional House domains;
- mundane Planet–Sign and Planet–House contributions;
- civic House governance and actor routing;
- mundane whole-chart Judgment and Translation;
- target, event, clock, locality and chart-type intake;
- the reference-only governing-period skin;
- Chronicle association and Evidence boundaries.

### Do not transplant

- natal Planet, House or developmental wording;
- natal intake and saved-birth-chart assumptions;
- the monolithic Sentient Sun live-data compiler;
- named generated payloads, readings or fixtures as runtime dependencies;
- named voice/client payloads as generic mundane runtime inputs;
- natal Moon-state, ASC or DSC semantics without independent mundane adoption;
- Freedom 250 arc weights as universal mundane doctrine;
- runtime interpretation shortcuts that outrun documented authority.

Shared Aspect mechanics do not authorize every mundane use. Endpoint actors,
pair-specific civic Judgment, salience/admission and any Forecast use remain
mundane adapter or later-reasoning responsibilities. A Sun–Neptune risk ruling,
for example, is a mundane pair judgment—not a new square, conjunction or
opposition operator.

The current mold declares six shared operators. Sentient Sun's active shared
foundation also documents the 30° semisextile. Its mundane adoption is
`unresolved`, not silently excluded or already authorized; Phase 0 must either
add it to the shared roster or record why it remains documented-only.

## Recommended implementation plan

### Phase 0 — Governance and ratification

**Goal:** establish the authoritative mundane owner set before building against
provisional language.

Work:

1. Select the exact live-vault home for the adopted atlas and owner documents.
2. Review the ten Planet, twelve Sign and twelve House seeds with Katie.
3. Resolve named doctrine conflicts rather than blending them silently.
4. Ratify the shared Aspect boundary and dignity-as-condition wording.
5. Ratify the continuous relationship-time contract while keeping the governed
   pair roster and inside-planet clock promotion as separate decisions.
6. Lock the chart-type registry schema, the initially supported chart types,
   clock rules, locality rules and one-house-frame contract. Other documented
   types remain `documented_only` or `future`.
7. Record adopted rulings in the Decision Log or the method owner it names.

Planet checkpoint as of 2026-08-11: the complete ten-Planet candidate roster,
human review surface and closed owner lifecycle shell now exist. All ten remain
pending Katie disposition; none has an active semantic revision. The review
surface also corrects the workbook shorthand that equates gift with dignity and
shadow with affliction: both poles are intrinsic, while dignity describes the
quality of Sign-supplied tools.

Sign and House checkpoint as of 2026-08-11: twelve complete independent Sign
candidates and twelve complete independent House arena candidates now exist in
closed lifecycle shells. Sign content begins with Modality movement and Element
shaping but requires an independently reviewed unique expression. House content
is arena-only. Natural-sign/natural-ruler analogies, Planet assignments, exact
angles and derivative routes are absent from the radical House owners. The
fifth/eleventh chamber allocation remains explicitly unresolved.

The registry schema must keep `method_status`, `runtime_status` and
`permitted_use` separate. During review, also decide whether filing and deadline
are event kinds under the event-chart technique, and whether live transit is a
runtime/view mode rather than an independent chart technique.

Exit gate:

- every core semantic atom is `ratified`, `provisional` or `unresolved`;
- no provisional atom can execute as adopted meaning;
- every owner has provenance and a versioned identity.

### Phase 1 — Semantic-closed mundane identity chassis

**Goal:** create a new namespace without copying the natal organism wholesale.

Work:

1. Start from the donor's small generic candidates: `chart_projection.py`,
   `build_support.py`, Navigation Spine schema/test patterns and validator
   orchestration patterns.
2. Rename and rebind every route, output, adapter and template.
3. Build Lobby, Chart Room, Period Weather Room and Organism shells.
4. Implement immutable chart and period identity records.
5. Keep all semantic execution closed.

Treat `living_chart_app.py`, the HTML template, assembler and construction-state
generators as adaptation references until every named fixture path, route,
output and natal payload assumption has been removed.

Exit gate:

- no Sentient Sun name, route, output or fixture is required at runtime;
- navigation round-trips without changing facts;
- missing owners visibly fail closed.

### Phase 2 — One factual chart end to end

**Goal:** connect the new shell to existing Freedom 250 calculations without
calculating the same fact twice.

Work:

1. Build the mundane chart adapter.
2. Materialize target, event, clock, locality, technique and snapshot identity.
3. Emit coordinates, angles, one Whole Sign frame, occupancy, Aspects,
   traditional dignity, condition, rulership and dispositor facts.
4. Add a mandatory technical-inspection receipt.
5. Render one complete calibration chart with no automated Judgment.

Exit gate:

- each fact is calculated once and referenced everywhere else;
- exact inputs reproduce the same snapshot;
- changing focus cannot change counts, facts or authority;
- Houses and exact angles are semantically available only when the clock
  authority produces a defensible local frame. Noon or midnight proxies may
  produce explicitly synthetic display coordinates, but cannot silently own
  event-House or event-angle meaning;
- unsupported layers say `unresolved` rather than borrowing natal prose.

### Phase 3 — Core mundane semantics

**Goal:** make one chart intelligible through governed mundane owners.

Work:

1. Connect ratified Planet functions.
2. Connect modality, element and unique-Sign owners.
3. Connect the twelve mundane House domains.
4. Add Planet–Sign and Planet–House contribution packets.
5. Add Aspect-web, condition, governance and root structure.
6. Add references to exact shared relationship states, chart-specific DR-020
   narration projections, separate seed echoes, and one continuous relationship
   history without assigning either Planet or pair a plot.
7. Build a whole-chart structural return before prose.

Exit gate:

- every semantic statement maps to an exact owner and exact chart facts;
- address labels and adjacency cannot masquerade as interpretation;
- dignity modifies condition only;
- the whole-chart return preserves all meaningful tensions and both poles.

### Phase 4 — One governing period end to end

**Goal:** make the nested mundane time ladder inspectable without blending
charts.

Work:

1. Build the minimal period adapter with identity, bounded interval,
   governing-ingress reference, ordered chart references and typed
   `governs`/`triggers` relations.
2. Reference bounded slices of continuous planetary relationship histories;
   preserve distinct state and exact-pass identities through retrograde returns
   and across ingress boundaries.
3. Preserve separate chart snapshots and Evidence identities.
4. Add era context only when an adopted cycle owner earns it.
5. Add eclipse/Moon-family lineage and national/entity contacts as separately
   gated adapters.
6. Add institutional clocks and the read-only Chronicle event bridge after
   their identity and Evidence contracts are ratified.

Exit gate:

- the period contains references, never duplicate chart payloads;
- the period neither starts nor resets a relationship history;
- every trigger retains its typed `governs`/`triggers` relation plus the exact
  governing chart or contact reference;
- Chronicle capture remains independent of astrology;
- temporal co-occurrence alone grants no Evidence.

This phase plus Phase 3 is the first genuinely useful release: **one complete
mundane chart and one inspectable governing period**. Automated prose is not
required for success.

### Evidence-family boundary

Before Judgment opens, the organism must keep these record families distinct:

- **computed chart facts** — reproducible coordinates, frames, relationships,
  conditions and typed period membership;
- **adopted semantic authority** — versioned meanings and connector rules;
- **Chronicle factual evidence** — independently captured real-world records;
- **observed outcomes** — what occurred inside or after a registered window;
- **counterevidence** — facts or outcomes that weaken a candidate claim;
- **forecast scoring** — evaluation of a separately registered literal call.

Repeated display and cross-family counts do not create independent support.
Chronicle co-occurrence cannot upgrade interpretive confidence merely because
an event happened near an astrological contact.

### Phase 5 — Judgment, speech and review

**Goal:** open reasoning only after facts, owners and whole structure are stable.

Work:

1. Implement candidate-claim formation.
2. Implement Evidence-family and counterevidence accounting.
3. Add deterministic validation before human review.
4. Open Katie's `keep / revise / reject / hold` disposition gate.
5. Produce symbolic reading and civic Translation as separate outputs.
6. Keep Forecast Ledger registration optional and separately permissioned.

Exit gate:

- no prose is released without its fact and semantic lineage;
- revisions never silently alter the underlying facts;
- a forecast has a literal claim, literal window and separate registry state.

### Phase 6 — Observatory integration

**Goal:** make the stable instrument available without making the Observatory
larger at startup or changing existing tools' jobs.

Work:

1. Produce a standalone generated `Mundane Living Chart.html` child view.
2. Add its builder and validator to governed build/check coverage.
3. Generate the child under `04 - Synthesis/Cross-cuts/` and register its
   builder in `99 - Templates/build_manifest.json` and refresh ordering.
4. Register the child under Sky & Charts → Workbench by editing
   `99 - Templates/build_sky_charts.py` → `SUBVIEWS`; never hand-edit generated
   `Sky & Charts.html`.
5. Give it a stable `data-sky-id`, filename, aliases, direct/legacy route and
   date-action policy.
6. Add it to recursive wrapper validation and declare its theme classification
   and injector behavior. If the child embeds data, update stale-scan exemptions
   in both `check_vault.py` and `refresh_synthesis.py`.
7. Lazy-load only the selected child and selected chart or period payload.
8. Preserve direct routing, search aliases, favorites and recents. Sky & Charts
   owns its remembered last-selected instrument; the child separately owns any
   remembered internal room or focus preference.
9. Add governed **Open in Mundane Living Chart** links from relevant chart
   libraries and timing tools.
10. Stage the Mac app only through the existing vault sync/build chain.

Exit gate:

- unopened organism code and data do not load at Observatory startup;
- every local child route resolves in vault, staging and packaged projections;
- responsive layout, fit-to-viewport, zoom/pan and collision-aware chart labels
  pass visual QA;
- app behavior creates no new astrological authority.

### Phase 7 — Self-sustaining operation

**Goal:** make ordinary semantic, calculation and interface changes safe and
traceable without reconstructing the architecture each time.

Work:

1. Generate construction status and remaining-owner projections from the atlas.
2. Maintain source-only, focused and release validation lanes.
3. Add contract tests for owner identity, permissions, chart/period references,
   one-house-frame policy and navigation round trips.
4. Add source/generated drift checks and deterministic rebuild checks.
5. Document one maintenance route and one release route.
6. Keep generated artifacts out of semantic review and versioned owners out of
   generated output files.

Exit gate:

- an owner change invalidates only its true downstream dependents;
- a UI change invalidates no astrology;
- a calculation change cannot silently alter meaning owners;
- a semantic change cannot silently alter astronomy;
- a clean release can be rebuilt from governed sources and verified
  deterministically.

## What “self-sustaining” means here

The organism will be self-sustaining when its structure carries its own
maintenance instructions and failure boundaries:

- one versioned machine atlas inventories owners, states, dependencies and
  permissions;
- every fact and semantic contribution has a canonical identity;
- generated status tells the next builder what is built, unresolved or blocked;
- validators reject missing provenance, duplicate calculations, natal fallback,
  stale outputs and permission leaks;
- the build graph knows which products must regenerate after each kind of
  change;
- Katie reviews complete candidate meaning or prose rather than repairing
  machine fragments;
- new chart types enter through the typed registry and cannot bypass clock,
  locality, frame or Evidence rules;
- the Observatory can expose more depth without loading or displaying all of it
  at once.

Self-sustaining does not mean self-authorizing. New doctrine, Judgment and
Forecast permissions always remain governed.

## Critical fail-closed rules

- No natal semantic fallback.
- No default-today chart.
- No silent precision upgrade or noon proxy where exact time is required.
- No Houses or angles without a verified frame.
- No second house frame silently projected onto a comparison.
- No blended multichart payload presented as one chart.
- No period governance without a versioned ingress-validity rule.
- No ingress boundary, including Aries, represented as the beginning or reset
  of a synodic relationship.
- No retrograde return or repeated perfection represented as the same state or
  pass occurring twice.
- No Planet or pair assigned permanent ownership of a plot.
- No trigger claim without a typed `governs`/`triggers` relation and exact
  governing chart or contact reference.
- No event-to-astrology causal claim from temporal proximity.
- No Judgment from counts, centrality, angularity or dignity alone.
- No generated HTML or JSON as semantic authority.
- No Freedom 250 arc score in symbolic or level-one reading prose.
- No Forecast without a separately registered, falsifiable call.

## Known doctrine and runtime review items

These are review lanes, not permission to choose silently:

1. Moon as political class/public mood versus broader masses/general public.
2. Neptune risk weighting versus the required multivalent two-pole reading.
3. Pluto's importance in mundane work across divergent sources.
4. Venus's actor boundary across diplomacy, women, arts, currency and value.
5. Fifth-house Senate language versus the eleventh-house legislature owner.
6. Traditional rulership as formal governance versus modern co-rulers embedded
   in some lower machine material.
7. Explicit separation of lunar nodes from planetary orbital nodes.
8. Shared-fact adapter coverage missing from the current core dossier,
   including applying/separating and dissociate Aspect texture, DC/IC,
   declination admission, eclipse path/duration, true Moon-family lineage and
   the two-way Full Moon reading.
9. Mandatory 916 America integration gaps in some core mundane modules.
10. Chart-confidence behavior when national or entity birth time is uncertain.
11. Dignity phase measured from a Planet's exaltation as a separate mundane
    timing owner; it may reuse the traditional exaltation fact but must not be
    folded into essential-dignity classification.
12. Continuous planetary relationship time is now a required structural owner:
    stable pair identity, exact chart state, seed-family and pass identity, and
    ordered transition history. The governed pair roster and live runtime
    coverage remain separate decisions; the 2026-08-30 Workbench relationship
    clocks do not promote themselves into the organism.

## Decisions that can wait until their gate

Do not block early factual work on these, but do not silently decide them:

- final user-facing instrument name;
- the first calibration chart and governing period;
- which specialist layers enter the first useful release;
- whether a saved-period library is part of the first interface pass;
- exact visual styling after the donor chassis is separated from natal content;
- whether compact summaries later appear in a currently governed
  timing/discovery surface, if one exists when that gate opens.

Any compact cross-view summary remains a link or bounded projection. It must not
embed the whole organism or create a second interpretation owner.

## Cold restart route

A future builder should resume in this order:

1. Read the live vault router:
   `Freedom 250 Chronicle/_Claude-Context/README.md`.
2. Refresh the vault Primer if current operational state matters.
3. Read `00 - Index/DECISION LOG.md`.
4. Read `00 - Index/Reading the Charts — START HERE.md`.
5. Read `00 - Index/Mundane Astrology — Master Reference.md`, the governed
   mundane method/atlas owner and the semantic owner set.
6. Read this handoff.
7. Read `KNOWLEDGE_INVENTORY.md`.
8. Read `MUNDANE_ORGANISM_DESIGN.md`.
9. Inspect `mundane_method_atlas.json` and run
   `validate_mundane_mold.py`.
10. Before app work, read `_Claude-Context/BOOT — Build a View.md`,
    `_Claude-Context/VIEWS REGISTRY.md` and
    `00 - Index/Observatory — Unified Experience Architecture.md`.
11. Inspect the live code and git state; do not infer it from this dated
    handoff.

## Exact next action when work resumes

Start with **Phase 0: governance and ratification**, not an app fork.

Begin Katie's Planet review with **Sun / Moon**, then proceed through Mercury,
Venus / Mars, Jupiter / Saturn, and Uranus / Neptune / Pluto. The complete
surface is `MUNDANE_PLANET_OWNER_REVIEW.md`; machine candidates are in
`MUNDANE_PLANET_OWNER_CANDIDATES.json`; the deliberately closed ten-record
owner shell is `mundane_planet_function_owner.json`.

The equivalent Sign and House surface is now
`MUNDANE_SIGN_AND_HOUSE_OWNER_REVIEW.md`. Review Signs after ratifying the three
Modality and four Element inputs; review Houses by axis. Each atom shows:

- current proposed wording;
- modality and element structural inputs where relevant;
- source provenance;
- known divergences;
- dependent connectors;
- Katie disposition;
- resulting atlas state.

Once those atoms and the chart identity contract are sufficiently ratified,
extract the smallest semantic-closed mundane identity chassis and prove one
factual chart end to end. Do not begin by copying the complete Sentient Sun
repository or by wiring an unfinished organism into the Observatory shell.

## Current verification receipt

At handoff creation:

- the mundane mold validator passes its declared structural scope;
- no Sentient Sun files were edited;
- no live Freedom 250 vault method, view or app source was edited by this
  package;
- no generated Observatory view exists yet;
- no automated Judgment, Translation or Forecast permission is open.

2026-08-30 amendment verification:

- relationship-time is now explicit in the design, circular-reading plan,
  handoff, knowledge inventory, machine atlas, and mold validator;
- the amendment changes the design contract only—no app fork, generated view,
  semantic owner activation, pair-roster promotion, or forecast was opened.

This receipt is dated evidence only. Re-run the package validator and inspect
live vault/app status before relying on it in a later session.
