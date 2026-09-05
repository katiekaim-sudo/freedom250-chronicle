> Source created: 2026-08-16

# Annex entity addition audit — 2026-08-16

The 15 August annex capture and monetary crosswalk put TFI / OFAC / USITC on the tree and mapped 35 monetary orders. This pass asks a narrower question: which **legal persons** named by the captured annexes were still missing from the Federal Group?

The governing admission rule is unchanged: a node is a legal or accounting entity with a verifiable organizational position. A person, foreign target, sanctions-list entry, security, HTS line, country-rate row, position description, private intermediary, or transaction is an object or overlay — not a new federal entity.

## What was checked

- All **55** EO 14410 parent agencies (4,862 appendix rows).
- The high-count listing units that already have siblings on the tree (CBP, USCIS, FDA, OCC, FinCEN, and the rest).
- The tariff and sanctions annexes for additional *US governmental* actors.

## Already on the chart

53 of 55 14410 parents were already registered. Name aliases that matter:

| Annex parent | Tree / registry name |
|---|---|
| Department of War | `Dept of Defense` (Army / Navy / Air Force already sit under it) |
| Office of Management and Budget | `Office of Management & Budget` |
| Export-Import Bank of the United States | was collapsed into `Export-Import Bank · DFC` |
| U.S. International Development Finance Corporation | same collapsed node |
| Corporation for National and Community Service | `AmeriCorps (CNCS)` |
| National Archives and Records Administration | `National Archives (NARA)` |

Tariff annexes still route through USITC, CBP, USTR, and Treasury — already visible. Sanctions annexes still route through TFI / OFAC. Names on those lists stay objects.

## Structural changes applied

| Entity | Parent / form | Clock | Why the annex makes it relevant |
|---|---|---|---|
| US Coast Guard | DHS / military service | 1915-01-28 | 108 Policy/Career chairs — largest missing 14410 unit. 14 USC 101 dates the named Coast Guard to this day. |
| Federal Student Aid | Education / bureau (PBO) | 1998-10-07 | Education had no child. FSA is the loan-book operator; 9 chairs. P.L. 105-244. |
| Armed Forces Retirement Home | independent establishment | 1990-11-05 | 14410 parent agency. P.L. 101-510 §1511. |
| Court Services and Offender Supervision Agency | independent establishment | 1997-08-05 | 14410 parent agency. P.L. 105-33. |
| Export-Import Bank | government corporation (split) | 1934-02-02 | 47 chairs. Kept the existing Ex-Im clock (EO 6581). |
| US International Development Finance Corporation | government corporation (split) | 2018-10-05 | 16 chairs. BUILD Act (P.L. 115-254 Div. F). Operations 20 Dec 2019 are a second clock, not the charter. |
| US Mint | Treasury / bureau (renamed) | 1792-04-02 | Was `US Mint / Bureau of Engraving`. 14410 lists 2 chairs. Coinage Act bureau. |
| Bureau of Engraving & Printing (BEP) | Treasury / bureau (surfaced) | 1862-08-29 | Already in the registry; hidden inside the combined tree node. 14410 lists 2 chairs. |

Net: registry **387 → 392** (remove one combined Ex-Im/DFC node, add six legal persons). Mint/BEP is a rename + surface, not a seventh new record. Charts rebuilt: **345** dated / **47** deferred.

Coast Guard note kept on the node: service lineage is the 4 Aug 1790 Revenue Cutter Service; the 1915 act is the named legal person; the DHS transfer is 1 Mar 2003. AFRH note refuses 1851 / 1811 — those are predecessor homes.

## Deliberately not added

- Every 14410 listing unit (266 of them). Internal offices, assistant-secretary portfolios, and DoDEA-class activities are not new legal persons.
- Office of Domestic Finance (30 chairs). An Assistant Secretary portfolio, not a chartered bureau.
- EOIR, ACF, IHS, PHMSA, BOEM / BSEE. Real bureaus; not required to close the annex parent-agency hole. Later census if Katie wants the next layer of departmental children.
- Karim Khan, Magnitsky names, CMIC companies, HTS lines, country rates, PD numbers.
- ICC, UN Secretary-General, foreign banks, brokers, custodians.
- The never-printed EO 13886 annex (inherited 13224 list — an object problem, not a missing US entity).

## Computed clocks on the new nodes

Sunrise charts, Washington, no official time. Not a reading.

- **Federal Student Aid** is at a progressed Full Moon (0.0° from exact as of the July 2026 progression epoch the builder uses). Recorded as computed data only.
- Ex-Im keeps the 1934 chart the combined node already had. DFC is a new 2018 sunrise chart.

## Files changed

- `04 - Synthesis/Cross-cuts/The Federal Group.html`
- `04 - Synthesis/Entity Theory/entity_founding_dates.json`
- generated `entity_charts.json` and `entity_progressions.json`
- `99 - Templates/entity_index.py` (join aliases)
- regenerated `99 - Templates/entity_index.json`

Vault HTML is live. The installed Mac app is frozen at its last build — not rebuilt on this pass.

## Primary sources

- [14 U.S.C. § 101 — Establishment of Coast Guard](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title14-section101)
- [NARA — Records of the United States Coast Guard](https://www.archives.gov/research/guide-fed-records/groups/026.html) (act of 28 Jan 1915, 38 Stat. 800)
- [24 U.S.C. ch. 10 — Armed Forces Retirement Home](https://uscode.house.gov/view.xhtml?path=/prelim@title24/chapter10&edition=prelim) (P.L. 101-510, 5 Nov 1990)
- [CRS IF11626 — The Armed Forces Retirement Home](https://www.congress.gov/crs-product/IF11626)
- [CSOSA — Our History](https://www.csosa.gov/our-history/) (P.L. 105-33, 5 Aug 1997)
- [D.C. Code § 24–133](https://code.dccouncil.gov/us/dc/council/code/sections/24-133)
- [CRS R47006 — U.S. International Development Finance Corporation](https://www.congress.gov/crs-product/R47006) (BUILD Act 5 Oct 2018; operations Dec 2019)
- Higher Education Amendments of 1998, P.L. 105-244 (7 Oct 1998) — Federal Student Aid as a performance-based organization
