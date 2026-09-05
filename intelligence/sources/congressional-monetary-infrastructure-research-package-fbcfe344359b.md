# Congressional Monetary Infrastructure — Research Package

**Read first.**  
**Cutoff:** 2026-07-18  
**State:** `pending workspace research; no live-vault files changed`  
**Scope:** DTC/DTCC tokenization, House Financial Services hearings, cross-committee market-structure work, PACE, sovereign digital reserves, prudential regulation, consumer/AML controls and the existing Freedom 250 monetary corpus.

## Short answer

Yes: a large financial re-architecture is moving, but it is not one bill or one launch. It is a coordinated-looking convergence of separately authorized systems:

- DTC completed limited production transactions using tokenized securities while retaining the authoritative entitlement record; the participant-facing service launch remains scheduled for October;
- NSCC is already operating 24x5 and the Treasury-clearing build continues through FICC and competing infrastructures;
- Congress is constructing private payment-issuer and payment-provider lanes while resisting a direct retail CBDC model;
- the Fed, OCC, FDIC, NCUA, SEC, CFTC, CFPB, FinCEN and Treasury are each being assigned different pieces;
- Treasury digital-asset custody is moving from executive policy toward a proposed statutory structure;
- the congressional task force studying the Fed and Treasury market has been reauthorized, so the nine-hearing series is entering a second phase.

The vault already understood most of the machine. The newly exposed gap was the **congressional assembly layer** connecting these systems.

### July 18 audit delta

`Research Packages/Government-Wide Audit 2026-07-18/` closes the prior July
14–17 hearing-capture gap. It preserves official caption corpora for the House
and Senate Fed and CFPB hearings, the House CLARITY field hearing and HSGAC's
fraud hearing, with source records, hashes and a cross-agency rule/watchdog
delta. No hearing itself changed a statute, Fed operating framework, CFPB
structure or digital-asset bill state.

## 1. Strongest findings

### A. July 15 is an occurred DTC production milestone, with one important caveat

DTCC's July 15 press release says DTC-custodied assets were converted into tokens and used in real production trades involving more than 30 firms. It names collateral pledge, securities lending, Treasury/repo DVP, equity DVP, equity DVD, token transfer and CCP-margin workflows on Hyperledger Besu and Canton.

The correct state is:

`limited production trades occurred / October participant-service launch scheduled`

not:

`full commercial service launched`.

The release names the participating-firm roster and workflow classes but does not publish transaction-level CUSIPs, matched counterparties, values or on-chain identifiers. The October 2026 preliminary service launch remains a separate announced target.

### B. DTC tokenization centralizes the legal record while distributing the interface

DTC's model is not issuer-native stock appearing independently on a blockchain. It is a controlled token representation of a DTC participant's existing security entitlement.

The chain layer can become multi-network and continuously available, but DTC retains:

- the final entitlement record;
- wallet and network approval;
- mint/burn, freeze, pause, clawback and force-transfer controls;
- corporate-action and reconciliation authority;
- restrictions on eligible assets and participants.

That is best understood as **federated technical rails around a centralized legal record**.

### C. The March 25 tokenization hearing is the largest missing congressional bridge

HFSC's 2026-03-25 *Tokenization and the Future of Securities* hearing put DTCC, SIFMA, Nasdaq, the Blockchain Association and Plume into the same record and attached two discussion drafts.

It bridges:

- SEC staff's entity-specific no-action relief;
- DTC's controlled production service;
- exchange tokenized-trading proposals;
- wider statutory recognition of blockchain records;
- possible joint SEC/CFTC tokenization study and rules.

The infrastructure is already well mapped in the vault. The missing object is the complete hearing source packet and bill-to-rule comparison.

### D. PACE is a two-gate federal payments architecture

H.R. 8395 would allow a qualifying payment provider to seek OCC registration and then separately apply to the Federal Reserve Board for a payments reserve account supporting Fedwire, FedNow and FedACH.

PACE is not automatic Fed access, a bank charter, FDIC insurance, discount-window access or an entitlement to credit. Its importance is that it creates a possible national nonbank payment-provider lane with:

- a 40-state-license or qualifying state-charter entry test;
- 1:1 reserve assets and segregation;
- OCC supervision of the provider and critical vendors;
- a special resolution regime outside ordinary Chapters 7 and 11;
- statutory agency clocks and deemed approvals;
- a second Board account gate followed by Reserve Bank onboarding.

The two approval gates can move faster than ordinary open-ended account processes, but only if Congress enacts the bill and agency/technical implementation follows.

### E. ARMA is the largest newly exposed sovereign-asset bill

H.R. 8957, the American Reserve Modernization Act, would convert the executive-order Strategic Bitcoin Reserve and Digital Asset Stockpile into Treasury statutory structures if enacted.

It combines:

- federal digital-asset inventory and transfer;
- a 20-year Bitcoin holding floor;
- quarterly cryptographic proof-of-reserve;
- independent audit and GAO oversight;
- segregated Treasury custody for state-owned Bitcoin with state title retained;
- management of non-Bitcoin federal assets;
- ESF Bitcoin reporting;
- a Treasury-Commerce study of budget-neutral acquisition routes including forfeitures, taxes/tariffs, gifts, Reserve Bank remittances and gold-certificate revaluation.

The last item is a **study mandate**, not present authority to revalue gold, compel Fed remittances, accept Bitcoin taxes or purchase Bitcoin.

### F. The story requires four congressional committees

The legal assembly line is:

```text
House Financial Services + House Agriculture
                    |
             House product
                    |
Senate Banking + Senate Agriculture
                    |
       reconciled Senate product
                    |
    identical House/Senate text
```

GENIUS completed this process and became law. CLARITY has not. The House passed H.R. 3633 on 2025-07-17; Senate Agriculture and Senate Banking later advanced different committee products that still require reconciliation.

### G. The monetary-policy hearing series is continuing

HFSC agreed on 2026-06-30 to reauthorize the Task Force on Monetary Policy, Treasury Market Resilience, and Economic Prosperity. The resolution takes effect July 23, 2026 and authorizes more hearings, investigations, reports and recommended legislation.

The vault's nine-hearing sequence should therefore be preserved as **Act I**, with post-reauthorization work captured as **Act II**.

### H. The June 30 markup is the control-plane prequel to programmable finance

The complete June 30 “Various Measures” record joins regulatory process, product
classification, identity, fraud friction, data flow, liability and federal
preemption in one committee action. H.R. 9329 would constrain SEC rulemaking and
restructure the agency; H.R. 9330 would place qualifying earned-wage access
outside federal credit and lending classifications; H.R. 9331 would authorize
temporary availability holds on suspect checks and wires; and H.R. 1483 would
remove direct identity fields from CAT reports while preserving transaction
telemetry.

The rejected amendments are part of the finding. The committee declined to
hard-code crypto, stablecoin, digital-asset and AI/algorithm risks into H.R.
9329's cost-benefit framework; declined a federal EWA fee/tip ceiling and
stronger preservation of state law; and declined consumer opt-in for expanded
rent, utility and telecom reporting. It adopted a narrower bipartisan
protection requiring that an EWA advance not exceed wages actually earned.

This is not a crypto bill package and it is not enacted law. It is the legal
workmanship around the private stack: define the category, decide who sees
identity, choose where delay is lawful, shape the regulator, allocate remedy
and decide whether states may differ. Read first:
HFSC Various Measures Markup 2026-06-30/README.md.

## 2. What the existing vault already does exceptionally well

No baseline rebuild is needed for:

- Federal Reserve Board versus FOMC versus twelve Reserve Banks;
- Treasury debt, cash, gold-certificate and ESF mechanics;
- DTC versus DTCC parent versus NSCC and FICC;
- Treasury clearing, dealer balance sheets, repo, margin and collateral;
- GENIUS issuer/reserve/insolvency/regulator structure;
- bank, fintech, stablecoin and crypto company legal entities;
- judicial account-access, agency-authority, forfeiture and property boundaries;
- the private monetary adapter stack.

The vault's central method—legal person first, then authority, status and clock—is exactly the right method for the current wave.

## 3. Genuine gaps, not duplicate research

| Priority | Gap | Why it matters |
|---:|---|---|
| P0 | March 25 tokenization hearing packet | direct DTC-to-legislation bridge |
| P0 | June 4 prudential-regulator testimony | current Fed/OCC/FDIC/NCUA positions in one record |
| P0 | May 20 bank-fintech hearing and H.R. 6552 | defines sponsor-bank partnership model that may compete with PACE |
| closed Jul 18 | July 14 House and July 15 Senate Warsh records | captured in the government-wide audit package; current Fed commitments remain review/communications clocks |
| closed Jul 18 | July 15/16 CFPB records | captured in the government-wide audit package; consumer-redress, fraud and payment-rights counterweight preserved |
| closed Jul 18 | July 17 CLARITY/ARMA field-hearing packet | captured in the government-wide audit package; H.R. 8957 remained introduced and unadvanced |
| P0 | July 21 FinCEN and FHLBank hearings | AML/control perimeter and a thinly mapped liquidity system |
| P1 | equity order-execution stack | exchanges, wholesalers, retail brokers, best execution, CAT and market data |
| P1 | FinCEN/BSA modernization | new providers and tokens expand the surveillance/compliance perimeter |
| P1 | PACE applicant census | must be built at the exact subsidiary/license/charter level |
| P1 | tokenized-reserve opinion tree | DTC Treasury entitlement is not automatically an accepted GENIUS/PACE reserve asset |
| P1 | CFTC authority-versus-capacity map | expanded spot jurisdiction and agency staffing/appropriation are separate clocks |

## 4. Corrections to carry into the vault

1. **CLARITY House passage:** 2025-07-17, not 2025-07-15.
2. **CLARITY state:** passed House, later processed separately by Senate Agriculture and Senate Banking; not enacted and the jurisdictional assembly is not over.
3. **Warsh July 15:** Senate semiannual monetary-policy testimony, not a nomination hearing.
4. **H.R. 6552:** ordered reported amended by HFSC; not passed House.
5. **Price Stability:** the hearing discussion draft became H.R. 5396; preserve draft and introduced dates separately.
6. **March tokenization texts:** still discussion drafts; do not assign them numbered-bill or enacted status.
7. **June 24/25 hearings:** marked aired but still mechanically stored as `UPCOMING` in `The Hearings.html`.
8. **Machine Spine:** its frozen hearing/filing totals are stale and internally inconsistent.
9. **Watch calendar:** add the July 17 HFSC field hearing and separate July 21 FinCEN, FHLBank and House Agriculture events.

No live-vault corrections were made in this research pass.

## 5. How fast could the chain move?

Faster than a normal single-bill reading suggests, because many prerequisites are already moving in parallel:

- DTC has conditional SEC staff relief and is testing before the broader service launch;
- exchanges are filing their own tokenized-trading rules;
- stablecoin law is already in implementation;
- nonbank Fed-access rules and PACE legislation can move on separate administrative and statutory tracks;
- NSCC 24x5 and Treasury central clearing are operational/in-progress independent of tokenization;
- Congress can combine committee products or insert provisions into a larger financial package;
- reauthorization keeps the Fed/Treasury task-force record open for additional bills.

The limiting sequence is still legal and operational:

```text
authority -> rule/relief -> entity approval -> onboarding -> production -> collateral/settlement use
```

The system can compress the calendar by running adjacent steps in parallel. It cannot safely skip the controlling legal person, asset-title, cash-leg, failure/finality and operational-readiness questions.

## 6. The leading indicators that matter most

Watch these instead of headline volume:

1. DTC's first named production transaction and written launch notice to SEC staff;
2. DTC's approved-network list, participant terms, fees and wallet standards;
3. whether tokenized entitlements receive collateral or settlement value;
4. whether a regulated stablecoin or tokenized deposit supplies the cash/distribution leg;
5. PACE markup, Senate companion and exact OCC/Fed account language;
6. first PACE-qualified legal entity, if enacted—not the parent brand;
7. GENIUS final rules, exact effective trigger and first issuer approval;
8. CLARITY reconciliation between Senate Banking and Senate Agriculture;
9. ARMA amendment/markup and any independent Treasury operational-reserve publication;
10. Fed Payment Account final rule and first approval;
11. FICC/NSCC/DTC/OCC/CME/ICE notices that accept tokenized assets into margin, repo, lending or clearing;
12. CFPB, FinCEN, OFAC and prudential rules defining fraud, privacy, sanctions, BSA and customer-redress duties;
13. the first post-July-23 monetary-policy task-force hearing or report;
14. failure events: lost key, clawback, chain outage, participant default, cash-leg failure, insolvency or litigation.

## 7. Package reading order

1. `CONGRESSIONAL_MONETARY_EXISTING_CORPUS_AUDIT.md` — what is already deep, partial, thin or absent.
2. `HFSC Various Measures Markup 2026-06-30/README.md` — Event 119430 control-plane analysis and rejected-protection record.
3. `DTC_TOKENIZATION_SOFT_LAUNCH_STATUS_2026-07-15.md` — today's event and the refreshed public operating model.
4. `HFSC_MONETARY_INFRASTRUCTURE_HEARING_REGISTRY.md` — the expanded House Financial Services record.
5. `CONGRESSIONAL_MONETARY_CROSS_COMMITTEE_MAP.md` — the four-committee assembly line.
6. `MONETARY_HEARING_ENTITY_BILL_CROSSWALK.md` — exact legal entities and bill states.
7. `PACE_ACT_LEGAL_MAP.md` — the payment-provider/Fed-account architecture.
8. `AMERICAN_RESERVE_MODERNIZATION_ACT_LEGAL_MAP.md` — sovereign reserve-asset proposal.
9. `CONGRESSIONAL_MONETARY_SOURCE_WATCHBOARD.md` — where each next state change will appear.

## 8. Primary official anchors

- DTCC July/October tokenization timeline: https://www.dtcc.com/news/2026/may/04/dtcc-advances-development-of-new-tokenization-service
- DTCC July 15 soft-launch statement: https://www.dtcc.com/dtcc-connection/articles/2026/may/19/tokenization-moves-from-theory-to-reality
- SEC staff/DTC no-action record: https://www.sec.gov/files/tm/no-action/dtc-nal-121125.pdf
- HFSC tokenization hearing: https://financialservices.house.gov/calendar/eventsingle.aspx?EventID=411038
- HFSC Future of Payments/PACE hearing: https://financialservices.house.gov/calendar/eventsingle.aspx?EventID=411134
- PACE introduced text: https://www.govinfo.gov/app/details/BILLS-119hr8395ih
- HFSC task-force reauthorization: https://financialservices.house.gov/calendar/eventsingle.aspx?EventID=411136
- Task-force resolution: https://docs.house.gov/meetings/BA/BA00/20260630/119430/BILLS-119pih-ReauthorizetheTaskForce.pdf
- July 17 field hearing: https://financialservices.house.gov/calendar/eventsingle.aspx?EventID=411176
- H.R. 8957 introduced text: https://docs.house.gov/meetings/BA/BA21/20260717/119461/BILLS-119HR8957ih.pdf
- House Agriculture CLARITY passage record: https://agriculture.house.gov/news/documentsingle.aspx?documentid=7973
- Senate Banking hearings: https://www.banking.senate.gov/hearings
- Senate Agriculture hearings: https://www.agriculture.senate.gov/hearings
