# Freedom 250 — Treasury / IRS Research Package

Completed: 2026-07-14  
Status: first full source-first sweep; pending review and selective promotion into the live vault  
Cutoff: 2026-07-14

## Short answer

The United States is **not replacing internal taxation with foreign taxation**. It is doing something narrower and structurally important:

1. adding larger border and cross-border revenue objects;
2. routing more reporting, intake and collection work through private intermediaries;
3. moving receipts and refunds onto Treasury-controlled electronic rails that depend on banks and processors;
4. extending use of federal tax information into other agencies;
5. centralizing day-to-day IRS management under a new CEO while the statutory Commissioner office is vacant.

The legal core has not moved. Congress creates the tax. Treasury supervises Internal Revenue Code administration. IRS assesses and maintains the taxpayer account. Sovereign enforcement powers remain public. What is moving outward is the **interface layer**: border collection, reporting nodes, filing software, paper scanning, debt-contact work, money transmission, payment execution and some data use.

## The decisive factual test

Treasury's June 2026 Monthly Treasury Statement shows that customs duties were still less than 4% of fiscal-year-to-date receipts. Individual income, corporate income and employment/general-retirement receipts supplied about 92%. Customs receipts were elevated, but the February 2026 Supreme Court ruling against the IEEPA tariff authority started a refund clock and made the earlier $418 billion FY2026 customs projection stale.

The safe formulation is therefore:

> The revenue perimeter is becoming more border-facing and intermediary-heavy, while the tax base remains predominantly internal and the legal assessment/enforcement core remains Treasury/IRS.

## Package map

| File | Function |
|---|---|
| `TREASURY_IRS_ENTITY_AUTHORITY_MAP.md` | legal entities, statutory offices, delegated operators, public/private seams and flow maps |
| `TREASURY_IRS_EXTERNALIZED_TAXATION_DEEP_DIVE.md` | evidence for and against the externalization thesis, with cross-story integration |
| `TREASURY_IRS_TRANSITION_TIMELINE.md` | meaningful 2024–2026 legal, organization, capacity, data and rail state changes |
| `TREASURY_IRS_CLAIM_AUDIT.md` | correction ledger for the highest-load claims in the live corpus |
| `TREASURY_IRS_SOURCE_WATCHBOARD.md` | source paths, clocks and exact promotion tests |
| `TREASURY_IRS_EXISTING_CORPUS_AUDIT.md` | existing vault coverage, contradictions, gaps and recommended integration points |

## Headline findings

### 1. The External Revenue Service is still a proposal

The January 20, 2025 trade memorandum ordered a feasibility and design investigation. The April 2025 report summary described ERS as an opportunity for Treasury–Commerce–DHS collaboration. S.175 was introduced and referred to committee. None of those acts created an agency, appropriated operating funds, hired staff or transferred CBP's collection authority.

**Current status:** `proposed / not established`.

### 2. Customs revenue is external by object, not usually by payer

CBP, inside DHS, collects customs duties from the importer of record and deposits federal receipts through Treasury systems. The taxable object crosses the border, but the legal payer is normally the importer. CBO estimates U.S. businesses and consumers bear most tariff costs. The source may be external; the incidence is largely domestic.

### 3. The clearest new externalized tax is the remittance-transfer excise tax

Effective January 1, 2026, a private remittance provider has a statutory duty to collect a 1% tax on specified cash-like U.S.-to-foreign transfers, deposit it semimonthly and report it on Form 720. If the provider fails to collect, the provider can become liable. The implementing regulations remain proposed, and the first scheduled January 29 deposit deadline is not evidence that a particular deposit or federal receipt occurred. This is a real private collection chokepoint—but the taxpayer is the domestic sender, not the foreign recipient.

### 4. IRS governance changed without changing the statute

The statutory Commissioner remains a presidentially appointed, Senate-confirmed office under 26 U.S.C. §7803. That office is vacant. A new CEO now runs day-to-day operations and reports directly to the Treasury Secretary. Frank J. Bisignano is separately Senate-confirmed as Social Security Commissioner, but was not appointed to the §7803 IRS Commissioner office. The CEO is an operational/delegated layer, not a statutory replacement for the Commissioner.

### 5. Capacity contracted while selected interfaces moved outward

TIGTA found a net 28% staffing decline between January 2025 and January 2026, including about one-third of revenue agents and tax examiners. At the same time:

- Direct File was suspended in favor of Free File/public-private filing partnerships;
- four Zero Paper contractors received contracts totaling about $2.3 billion through possible extensions to 2030;
- private debt collection remained active but legally bounded;
- other contracts were canceled, so the direction is selective rather than blanket outsourcing.

### 6. Tax information is becoming a cross-agency asset

The 2025 IRS–DHS/ICE agreement produced one large address-data transfer. Litigation, matching defects and safeguarding concerns followed. TIGTA reported IRS's representation that the recipient would not use the transferred data pending litigation and no further sharing through TIGTA's review; those are time-bounded attributed representations, not independent proof of current recipient behavior. Separately, TIGTA found 1,124 known federal-tax-information sharing agreements and no complete authoritative centralized inventory. This externalizes use of the data asset; it does not externalize tax assessment.

### 7. The rail is increasingly Treasury-wide and electronic

EO 14247 directed the phaseout of routine paper federal receipts and disbursements. IRS determines the taxpayer account and authorizes refunds; the Bureau of the Fiscal Service executes governmentwide collection and disbursement services; banks, ACH/Fedwire nodes, card processors, wallets and software providers form the adapter layer.

## Cross-story placement

| Observatory layer | Treasury / IRS connection |
|---|---|
| Money Machine | add a receipts/collections chain and a separate refund chain |
| Entity Theory | distinguish statutory Commissioner, nonstatutory CEO, Treasury Secretary and proposed ERS |
| Border / trade | importer → CBP/DHS → Treasury; ERS remains dashed |
| Private monetary stack | tax software, custodial brokers, remittance providers, card processors and banks are adapters, not sovereign tax authorities |
| Judicial Money | IEEPA tariff authority/refunds and §6103 data-disclosure litigation move the perimeter |
| Data / compute | contractor scanning, identity matching, FTI-sharing inventory and modernization control the tax-data layer |
| Crypto | separate taxable asset, broker reporting, withholding, payment method, realization and forfeiture |
| Forfeiture / reserve | preserve investigator, seizing agency, title proceeding, custodian, fund and disposition as separate legal objects |

## Recommended promotion path

1. Review this workspace package as a factual set.
2. Repair the proposed-ERS status contradiction in Entity Theory before drawing a new entity chart.
3. Add an IRS charter shelf covering 26 U.S.C. §§7801–7804, §6103, the 1952–53 reorganization and current delegation instruments.
4. Add the IRS–ICE cases and the tariff refund clock to Judicial Money.
5. Promote primary-source event notes for the CEO structure, workforce contraction, Direct File suspension, Zero Paper contracts, remittance tax and Form 1099-DA.
6. Correct the loud event claims through the existing Claim Corrections register; retain original bookmarks.
7. Fold approved facts into the incorporated Treasury–Fed timeline in the live vault. Do not edit the incorporated workspace copy as if it were authoritative.

## Immediate document hunt

- operative Treasury/IRS delegations identifying the CEO's current authority;
- full, nonpublic or later-released ERS feasibility/design report and any implementation records;
- post-July 24, 2026 legal state of the temporary Trade Act §122 surcharge;
- monthly customs refunds and net receipts after the IEEPA decision;
- final remittance-transfer regulations;
- first complete centralized IRS inventory of FTI-sharing agreements;
- Zero Paper contractor performance and confidentiality/safeguards records;
- filing-season performance after Direct File suspension;
- current Commissioner and Chief Counsel nominations, if any.
