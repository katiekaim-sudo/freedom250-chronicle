> Source created: 2026-08-15 · Source evidence cutoff: 2026-08-15 ET

# Executive Order Entity Maps — Wave 1 Monetary Control Plane

## Outcome

The Executive Orders tab now carries a separate, source-routed entity map for
each of the 35 Wave 1 orders most directly connected to monetary control. The
maps sit above the astrological chart and show the operative sequence as typed
nodes: presidential instrument, federal actor, legal or administrative record,
controlled object, private intermediary, and conditional result.

This is a curated first wave, not a claim that all 491 orders have been mapped.
The route card reports `35 / 491`; the remaining 456 stay visibly unmapped until
their legal paths are researched and validated.

## Wave 1 cohort

| Research lane | Count | Executive orders |
|---|---:|---|
| Sanctions and investment controls | 6 | 13818, 13886, 13959, 14203, 14373, 14404 |
| Tariff and customs controls | 10 | 14257, 14323, 14324, 14326, 14346, 14360, 14361, 14388, 14389, 14411 |
| Digital assets, reserves, payments, fraud, grants, and regulator control | 11 | 14178, 14196, 14215, 14222, 14233, 14243, 14247, 14249, 14332, 14390, 14395 |
| Banking, markets, credit, retirement, fintech, and personnel | 8 | 14330, 14331, 14366, 14393, 14403, 14405, 14406, 14410 |

## Government-tree additions

The pass added only governmental bodies with a supportable organizational
identity. Annex rows, private companies, securities, accounts, HTS lines,
position descriptions, proposed organizations, and future deliverables remain
typed objects or gates rather than government entities.

| Tree node | Parent shown in the Federal Group | Registry result |
|---|---|---|
| National Economic Council | Executive Office of the President | Added |
| Presidential Working Group on Digital Asset Markets | National Economic Council | Already registered; now visible in tree |
| Task Force to Eliminate Fraud | Executive Office of the President | Added |
| Stablecoin Certification Review Committee | Department of the Treasury | Already registered; now visible in tree |
| Office of Information and Regulatory Affairs | Office of Management and Budget | Added |
| Domestic Policy Council | Executive Office of the President | Added |
| Office of the National Cyber Director | Executive Office of the President | Added |
| Cybersecurity and Infrastructure Security Agency | Department of Homeland Security | Added |

Six new founding records bring the governed registry to 387 entities. All
entity chart, progression, filing-index, forward-watch, and tree-badge layers
were rebuilt from that registry. Exact-date records remain subject to the
registry's existing evidentiary and natal-chart guardrails.

## Navigation and validation

- `Mapped orders only` filters the EO universe to the curated Wave 1 set.
- Search indexes map titles, scope, path labels, nodes, boundaries, and sources.
- Every exact federal join appears as a clickable entity node or chip. It opens
  the Federal Group tab, reveals the node's ancestry, fits it into view, opens
  its drawer, and applies a temporary focus treatment.
- Parallel actors remain parallel chips; the interface does not manufacture a
  parent-child relationship merely because two agencies share an EO step.
- The builder rejects duplicate EO maps, unknown EO numbers, path/edge mismatch,
  malformed fragment paths, and any join absent from either the governed entity
  registry or the actual Federal Group tree.

The canonical data is split into one registry and two Wave 1 fragments so each
map is maintained once and merged deterministically by
`99 - Templates/build_executive_orders.py`.

## Corrections and hard boundaries carried into the maps

1. **EO 13886 inherits an annex.** It replaces section 1 of EO 13224; its phrase
   “Annex to this order” continues to point to EO 13224's annex as amended by EO
   13268. It is not a zero-target order with an omitted new annex.
2. **Blocking is not taking title.** A sanctions edge can freeze and require
   reporting of covered property. It does not establish seizure, forfeiture,
   vesting, government custody, settlement, or transfer to a reserve or fund.
3. **The postal de minimis implementation chain belongs to EO 14324/14388.** The
   2026 CBP rule is not an EO 14411 descendant; EO 14411 has its own customs
   control path.
4. **A digital wallet is not automatically a blockchain edge.** No reviewed EO
   supplies a legal join that converts references to wallets or electronic
   payment into stablecoin, tokenization, or blockchain infrastructure.
5. **Proposals and due deliverables stay gates.** A requested plan, rule review,
   study, recommendation, future website, or proposed entity is not rendered as
   an operational institution, transaction, or completed money flow.

## Canonical surfaces

- Entity-map registry: eo_entity_maps.json
- Direct-controls fragment: eo_entity_maps_wave1_direct_controls.json
- 2026-finance fragment: eo_entity_maps_wave1_finance_2026.json
- Government entity registry: entity_founding_dates.json
- Federal Group view: `04 - Synthesis/Cross-cuts/The Federal Group.html`
- Executive Orders view: `04 - Synthesis/Cross-cuts/Executive Orders.html`
- Source-adjudicated research package: `EXECUTIVE_ORDER_ANNEX_MONETARY_AND_ENTITY_FLOW_CROSSWALK_2026-08-15.md`

## Selected primary authorities

- [EO 14178 — Strengthening American Leadership in Digital Financial Technology](https://www.federalregister.gov/documents/2025/01/31/2025-02123/strengthening-american-leadership-in-digital-financial-technology)
- [EO 14395 — Establishing the Task Force to Eliminate Fraud](https://www.federalregister.gov/documents/2026/03/19/2026-05497/establishing-the-task-force-to-eliminate-fraud)
- [EO 14410 — Implementing Schedule Policy/Career](https://www.federalregister.gov/documents/2026/06/10/2026-11594/implementing-schedule-policycareer-in-the-excepted-service)
- [OFAC's 2022 rule explaining EO 13886's inherited annex](https://ofac.treasury.gov/system/files/126/fr87_39337.pdf)
- [CBP postal de minimis rule implementing EO 14324/14388](https://www.federalregister.gov/documents/2026/06/24/2026-12669/indefinite-suspension-of-the-de-minimis-exemption-for-mail-shipments-and-new-postal-informal-entry)

## Validation receipt

- The governed EO builder completed with 491 orders, 491 charts, and 35 entity
  maps; all registry fragments and entity joins passed its fail-closed checks.
- `Mapped orders only` returned exactly 35 cards in the rebuilt app.
- Browser smoke tests opened representative digital-asset (14178), sanctions
  Annex (13818), protected-proceeds custody (14373), and personnel-Appendix
  (14410) maps. Each map appeared before its astrology chart.
- A single entity node and a parallel-agency chip both navigated to the exact
  Federal Group node, opened its details, and applied one focus state.
- At a 390-pixel viewport, the EO body and expanded map had no horizontal
  overflow.
- The canonical vault view, staged app view, and compiled app view have the
  same SHA-256. The installed macOS bundle passes strict signature validation.
- The build manifest is clean and the whole-site research package validator is
  healthy. The vault doctors separately report ten pre-existing stale Primer /
  Gateway count references (8,704 versus the current 8,725 events); the EO map
  pass did not run the independently authorized synthesis refresh needed to
  reconcile those live-count surfaces.

## Later waves

The next wave should be chosen by legal adjacency rather than chronology alone:
first the remaining monetary-policy and financial-enforcement orders; then the
procurement, technology, emergency, and infrastructure orders that activate or
constrain the same agencies. Each later wave must pass the same exact-join and
evidence-state gates before its count changes.
