> Source created: 2026-08-15

# Annex entity addition audit — 2026-08-15

The monetary Annex pass exposed two real gaps in the Federal Group projection:

1. Treasury's sanctions and illicit-finance operating chain existed in the Entity Theory registry but was not visible in the structural tree.
2. The U.S. International Trade Commission was absent even though tariff Annexes repeatedly route technical Harmonized Tariff Schedule work through it.

The governing admission rule remains unchanged: a node is a legal or accounting entity with a verifiable organizational position. A person, foreign target, sanctions-list entry, security, HTS line, position description, private intermediary, or transaction is an object or overlay—not a new federal entity. Consultation, coordination, publication, and payment handoffs do not become parentage.

## Structural changes applied

### Treasury → TFI

The complete current Treasury subtree is now visible:

```text
Department of the Treasury
└─ Office of Terrorism & Financial Intelligence (TFI)
   ├─ Office of Foreign Assets Control (OFAC)
   ├─ Office of Intelligence & Analysis (OIA)
   ├─ Office of Terrorist Financing and Financial Crimes (TFFC)
   ├─ Treasury Executive Office for Asset Forfeiture (TEOAF)
   │  └─ Treasury Forfeiture Fund
   └─ FinCEN
```

Treasury describes TFI as its national-security arm and identifies exactly one bureau and four offices as its five components. Treasury Order 105-17 also places OFAC, OIA, the terrorist-financing office, TEOAF, and FinCEN under TFI's leadership. FinCEN therefore moved from a direct Treasury child to its current TFI position; it was not duplicated.

The subtree deliberately preserves three different legal states:

- **OFAC blocking:** covered property is frozen and reported; title does not transfer merely because it is blocked.
- **FinCEN/BSA controls:** reporting, analysis, rulemaking, and advisories are not sanctions designations or criminal adjudications.
- **TEOAF/Treasury Forfeiture Fund:** the special-fund path begins only through the separate seizure/forfeiture process and deposit authorities. It is not a downstream consequence of every OFAC block.

### Independent agencies → USITC

`United States International Trade Commission (USITC)` is now an independent-agency node in the existing regulator cluster. It is not nested under Commerce, USTR, DHS, or Treasury.

USITC describes itself as an independent, nonpartisan, quasi-judicial federal agency. Its functions include adjudication, trade research and analysis, and maintenance of the Harmonized Tariff Schedule. Its Tariff Affairs office compiles and publishes the HTS, keeps it under review, recommends changes to the President, and supplies technical work to USTR. CBP remains the customs assessment and collection entity.

## Money-flow edge applied

The money overlay now includes:

```text
CBP ⇄ Department of the Treasury
customs receipts / approved refunds
```

The forward direction represents CBP assessment, collection, and liquidation reaching government-wide customs-revenue accounting. The reverse direction represents the approved-refund instruction/accounting handoff: after CBP review, Treasury issues the claimant's refund. It does not mean Treasury pays CBP, and it does not claim a specific electronic route into the Treasury General Account.

The proposed External Revenue Service remains separately labeled proposed; it does not stand in for the existing CBP–Treasury chain.

## Founding-clock and accounting fields

| Entity | Legal form / parent | Clock encoded | Clock note | SFFAS field |
|---|---|---|---|---|
| TFI | Treasury office / Treasury | 2004-12-17 | Existing chart convention uses statutory establishment; Treasury Order 105-17 stood it up 2004-04-28. | consolidation |
| OFAC | TFI office | 1950-12 | OFAC's official history supports December 1950, not an exact day. The former `1950-12-01` precision was removed. | consolidation |
| OIA | TFI office and IC component | 2004-12-17 | Existing statutory clock retained; the April 2004 organizational-order clock remains a documented alternative. | consolidation |
| TFFC | TFI office | 2004 | Current-office lineage is verified to 2004; no exact day is encoded. | consolidation |
| TEOAF | TFI office | 1992 | Treasury's official page identifies the year only. The former unsupported `1992-10-28` precision was removed. | consolidation |
| Treasury Forfeiture Fund | statutory special fund / administered by TEOAF | 1992-10-06 | Treasury Forfeiture Fund Act of 1992 enactment clock. | consolidation |
| USITC | independent agency | 1916-09-08 | Revenue Act created the U.S. Tariff Commission; later name change preserves entity lineage. | consolidation |

USITC's consolidation field is independently corroborated by the FY 2025 Financial Report's Appendix A, which lists the International Trade Commission among additional consolidation entities.

## Objects deliberately not added as structural nodes

- foreign persons and companies named in sanctions Annexes;
- SDN, NS-CMIC, and other list entries;
- securities, derivatives, index products, HTS headings, product exceptions, and country-rate rows;
- importers, brokers, banks, exchanges, custodians, and other private intermediaries;
- EO 14410 position descriptions and personnel designations;
- a direct OFAC → DOJ/Treasury Fund → Strategic Bitcoin Reserve path without case-specific seizure, forfeiture, title, disposition, and deposit evidence.

Those belong in typed transaction, authority, personnel, or object overlays. Treating them as subsidiaries would erase the legal distinctions the tree is meant to show.

## Primary sources

- [Treasury Order 105-17 — Establishment of TFI](https://home.treasury.gov/about/general-information/orders-and-directives/treasury-order-105-17)
- [Treasury — TFI organization and five components](https://home.treasury.gov/about/offices/terrorism-and-financial-intelligence)
- [OFAC — official history](https://ofac.treasury.gov/about-ofac)
- [Treasury — TEOAF and Treasury Forfeiture Fund](https://home.treasury.gov/policy-issues/terrorism-and-illicit-finance/treasury-executive-office-for-asset-forfeiture-teoaf)
- [31 U.S.C. § 9705 — Department of the Treasury Forfeiture Fund](https://uscode.house.gov/view.xhtml?req=%28title%3A31%20section%3A9705%20edition%3Aprelim%29)
- [USITC — agency form, mission, and 1916 founding](https://www.usitc.gov/press_room/about_usitc.htm)
- [USITC Tariff Affairs — HTS functions](https://www.usitc.gov/offices/tata)
- [FY 2025 Financial Report, Appendix A — reporting entities](https://fiscal.treasury.gov/system/files/2026-03/appendix-a-2025.pdf)
- [CBP — CAPE review and Treasury ACH refund states](https://content.govdelivery.com/accounts/USDHSCBP/bulletins/415c8e9)
- [Fiscal Service — customs duties in government-wide revenue](https://fiscal.treasury.gov/accounting/us-financial-report/statements-operations-changes-in-net-position)

## Files changed

- `04 - Synthesis/Cross-cuts/The Federal Group.html`
- `04 - Synthesis/Entity Theory/entity_founding_dates.json`
- generated `entity_charts.json` and `entity_progressions.json`

Validation and app-install receipts are recorded in the implementation session; the structural names in the tree and registry remain exact join keys.
