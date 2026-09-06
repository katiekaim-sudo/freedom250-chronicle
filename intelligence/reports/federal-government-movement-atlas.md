# Government-Wide Research Hub

This maintained package is the one human-facing hub for Freedom 250 government
research. The compatibility identity `federal-government-movement-atlas`, the
package directory and the generated HTML filename remain stable. The hub keeps
the Research Desk Catalog as the package-library authority, the live Federal
Group as the topology authority, and each research system as the owner of its
own records. It presents six coordinated views without merging their meaning:

1. every exact Catalog package card plus the complete Registry shelf for that
   research identity;
2. the Federal Group's canonical entity notes;
3. exact entity joins from the federal-budget and Money/Tech Machine indexes;
4. exact congressional-body joins from the committee control plane; and
5. already adjudicated before/after movements from the authored movement
   registry; and
6. typed gaps and exact next-check conditions projected from their existing
   owners without turning them into one generic watch list.

The entity chart covers all 642 Federal Group nodes. Research paths currently
highlight 167 exact note-bearing or research-bearing entities; Whole family
restores the surrounding structural nodes without treating sparse coverage as a
finding of no activity.

## Read order

1. **Past research** in the interactive hub — the government-wide dated series
   or every saved Catalog package, with its curated Catalog routes, complete
   Registry shelf and handoff to the Research Desk package reader.
2. `ATLAS_CONTRACT.md` — package-library, authority, state, entity-role and
   generation rules.
3. `ATTACHMENT_POLICY.json` — governed source and join rules for entity notes,
   budget records, machine filings, committee artifacts and held Catalog labels.
4. `COVERAGE_GAP_POLICY.json` — owners, selection rules, review order and
   not-a-gap boundaries for the gap board.
5. `MOVEMENT_REGISTRY.json` — the small authored registry of adjudicated
   movements and exact future evidence gates.
6. `generated/ENTITY_TOPOLOGY.json` — generated projection of the live Federal
   Group hierarchy. Do not hand-edit.
7. `generated/ENTITY_ATTACHMENTS.json` — exact generated note/research joins.
8. `generated/CATALOG_ENTITY_MATCH_REVIEW.json` — review-only Catalog label
   candidates; no row here is an attachment.
9. `generated/COVERAGE_GAP_AUDIT.json` — generated typed gap inventory. Its
   items remain owned by the Return Ledger, Source Monitor, committee control
   plane, campaign package, Catalog or Registry named in each source.
10. `generated/ATLAS_DATA.json` — exact Catalog cards and assignments plus the
   complete Registry shelf and resolved topology, attachment, movement, gap
   and search projections.
11. `outputs/Federal Government Movement Atlas.html` — interactive Government-
   Wide Research Hub. The filename is retained for compatibility.
12. `GAP_AUDIT_2026-09-22.md` — the first gap classification and fill-wave
    receipt.
13. `GAP_BOARD_ACCEPTANCE_2026-09-22.md` — complete Registry shelf, focused
    validation and browser visual-QA receipt.
14. `UNIFIED_HUB_ACCEPTANCE_2026-09-22.md` — consolidation validation and visual-
    QA receipt. The pilot and expansion receipts remain historical records.
15. `PACKAGE_EXPLORER_ACCEPTANCE_2026-09-22.md` — wide package reading-room,
    package entity-map, complete-file and browser-QA acceptance receipt.

The default **Past research** view opens on the dated Government-Wide Research
Series and can expand to all Catalog research. Each package card is an exact
Catalog copy: compact display is a presentation choice, not a rewritten record.
**Explore package** opens a wide package reading room with three coordinated
views: overview and curated routes, a package-scoped entity map, and the complete
Registry shelf. The Catalog's declared `registry_refs` remain visible as curated
membership routes. Complete Registry membership is generated separately so
routers, answers, ledgers, source objects, methods and projections are not hidden
merely because they are not curated card routes.

The package entity map distinguishes exact governed joins from uniquely located
Catalog mentions. Exact joins come only from an artifact owner or adjudicated
movement. Review-only mentions may locate and open the matching Federal Group
family for inspection, but they do not become attachments, chart coverage or
institutional relationships.

Each entity branch opens on the familiar layered chart. **Research paths** shows
matching nodes plus the canonical structure needed to locate them; **Whole
family** restores every node in that branch. Selecting a node reveals its
Federal Group context, budget notes, machine filings, committee research and
direct adjudicated movements in separate labeled panels.

The September 22 Joint Warfighter Evaluation appears as an adjudicated
Department of Defense personnel-governance movement. Its official announcement
clock falls inside the dated campaign cutoff, while its later recovery clock
remains visible in the controlling package. The hub does not convert the
announcement into service implementation or a promotion outcome.

**Gaps & next checks** keeps six kinds of incompleteness separate:

- already-researched objects awaiting movement-representation review;
- dated or source-triggered Return Ledger questions;
- held source families and exact body/diff recovery;
- high-signal committee backfill;
- artifact-specific entity-join review; and
- package/Registry custody.

A structural blank, archive shelf state, unmatched private or foreign actor,
or committee that has not been selected for a plotline-led scan is not silently
promoted into a research assignment.

## Authority boundary

- The Chronicle's live Federal Group view owns institutional topology.
- `RESEARCH DESK CATALOG.json` owns package identity, package fields, Research
  Library assignments, series membership and curated Registry references.
- `RESEARCH REGISTRY.md` owns complete artifact membership, file role, file
  state, precedence, controlling path and Chronicle landing.
- Each movement's controlling research package owns facts, sources, clocks,
  disposition and evidence cutoff.
- `ATTACHMENT_POLICY.json` owns the declared research sources and exact join
  rules. Generated attachments remain projections of their named owners.
- `MOVEMENT_REGISTRY.json` owns only the cross-package entity/role join and the
  concise before/after transition representation.
- `COVERAGE_GAP_POLICY.json` owns only gap-projection rules. The records it
  projects keep their original owners and do not become a second queue.
- Generated JSON and HTML are projections. Rebuild them; never hand-edit them.
- A source-monitor change is not admitted here until supervised research has
  adjudicated its actor, source, clocks, state change, claim limit and owner.

This package does not replace or split dated sweep packages. It provides one
governed destination from which they can all be read.

## Commands

Build all projections:

```bash
python3 "Research Packages/Federal Government Movement Atlas/build_movement_atlas.py"
```

Validate authored and generated state without writing:

```bash
python3 "Research Packages/Federal Government Movement Atlas/validate_movement_atlas.py"
```

The builder requires local Node.js only to evaluate the data-only `DATA`
expression embedded in the canonical Federal Group HTML. It hashes and records
that exact source file in the generated topology receipt.

## Extension rule

Add an attachment source only when it has a stable exact entity key and a named
owner. Package-level Catalog entity lists remain review candidates because a
package can contain many artifacts concerning different actors. Add a movement
only after its controlling research owner has reached a final disposition. Use
one record with multiple typed entity roles; never copy the same movement into
separate entity files. Rebuild and validate after any owner or policy change.

For gaps, reconcile representation and custody before commissioning new web
research. A new stage type requires method review; do not force court,
legislative, oversight or organizational objects into an ill-fitting movement
stage merely to increase coverage.
