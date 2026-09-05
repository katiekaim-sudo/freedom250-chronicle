> Source evidence cutoff: 2026-08-09

# Energy Infrastructure Continuous Finance — Source Document

## Controlling finding

**Energy project finance is already a state machine.** Construction advances, term conversion, reserves, cash waterfalls, borrowing bases, distributions and defaults already depend on defined project states and authorized evidence.

The existing chain is document-heavy:

```text
physical work or asset state
  -> contractor, operator or servicer report
  -> officer or independent-engineer certificate
  -> lender or agent review
  -> borrowing-base, cost-to-complete or covenant calculation
  -> controlled-account instruction
  -> bank settlement
  -> accounting and later assurance
```

AI and distributed ledgers can compress the handoffs:

```text
signed asset event + contract state + account state
  -> AI evidence and covenant preflight
  -> authorized approval or exception gate
  -> programmable account instruction
  -> settlement
  -> synchronized project, lender and accounting views
```

The financing constitution therefore does not need to be invented. It needs to become **machine-readable, continuously evidenced and safely executable**. DLT is useful when it supplies a shared, time-versioned record of evidence and authority. The payment token is secondary to whether the lender, engineer, account bank, insurer and governing contract recognize the same state transition.

## Current state versus future architecture

| Capability | Public evidence state at cutoff | Ruling |
|---|---|---|
| Certified construction draws and controlled accounts | Deployed through executed project agreements | Existing project-finance control, not DLT-dependent |
| Operating cash waterfalls and reserves | Deployed through executed loan and depositary agreements | Analog programmable finance already exists |
| Granular asset-pool borrowing bases | Deployed in solar finance | Asset and contract state already changes credit availability |
| GAAP statements plus recurring operating reports | Deployed through filed power-project agreements | Financial and physical evidence answer different questions and coexist |
| Electronic trade documents and interoperable e-bills of lading | Legally recognized or used in completed transactions in specified jurisdictions | Logistics, title and bank-finance chains can be joined when law and participants align |
| DLT product-event records and regulated tokenized collateral | Deployed or completed in non-energy-specific workflows; provider claims must be bounded | Evidence and collateral layers are technically active |
| AI-assembled draw packets and continuous covenants for turbine projects | Technically near; no complete named public deployment located | Structurally supported architecture, not current production fact |
| Asset event directly releasing project debt or stablecoin | Not established in the public primary record | Requires contract authority, correction, loss allocation and an actual transaction |
| Public-chain data replacing annual project GAAP audit | Not established | Current evidence supports layering, not substitution |

## The clocks that must remain separate

| Clock | State transition | Why it cannot be inferred from another clock |
|---|---|---|
| Physical clock | component produced, shipped, installed, tested, operating or impaired | physical occurrence does not establish contractual acceptance or title |
| Contract clock | milestone, completion, warranty, outage, covenant or default condition is satisfied | raw sensor data is not automatically the contractually governed result |
| Authority clock | engineer, buyer, operator, lender, agent or regulator signs or determines the state | technical evidence does not silently inherit an actor’s legal authority |
| Title and control clock | ownership, possession or electronic control changes | a logistics timestamp or generic token does not itself transfer title |
| Collateral clock | lien attaches, is perfected, has priority and becomes borrowing-base eligible | title, eligibility, valuation and lender priority are distinct questions |
| Funding clock | commitment, condition precedent, borrowing request and advance occur | a financing announcement or commitment is not borrower cash |
| Settlement clock | bank deposit, tokenized deposit or stablecoin becomes usable by the intended recipient | technical transfer is not necessarily redemption, legal discharge or unrestricted cash |
| Accounting clock | cost, revenue, asset, liability, reserve or impairment is recognized | settlement time and GAAP recognition can differ |
| Correction clock | meter resettlement, invoice dispute, engineering correction or ledger restatement is resolved | immutable history does not decide which corrected state controls |
| Remedy clock | draw stop, cash trap, cure, acceleration, liquidation or court remedy becomes effective | only authorized parties and governing law can impose or adjudicate remedies |

Atomic settlement does not make these clocks identical. It can make their relationships explicit and reduce the delay between authorized transitions.

## The analog system already has programmable logic

### Construction advances

The filed Long Ridge 2019 credit agreement required a construction requisition, contractor-payment documentation and a monthly progress report before an advance. The independent engineer tested whether available funds remained sufficient to reach completion. Term conversion depended on completion certificates, and the lender and engineer could observe performance tests.

Rio Grande LNG Train 5’s filed 2025 agreement requires independent-engineer advance certificates, EPC payment requests, lien waivers and monthly construction reports. Its operating package includes production and maintenance forecasts, operating statements and debt-service-coverage calculations.

CP2 LNG’s July 2025 facility routes term-loan proceeds through a controlled construction account and conditions formal disbursement requests on stated prerequisites. GAAP remains the accounting framework.

These agreements already implement a permissioned workflow. Today the authoritative objects are certificates, reports and account instructions rather than signed machine-readable events.

### Operating cash waterfalls

A filed FuelCell Energy/NRG project loan requires project revenue to enter a controlled operating account and applies a priority sequence covering operating costs, fees, debt service, reserves and permitted distributions. Trigger events stop borrower-directed withdrawals, while unbudgeted major maintenance can be paid from a controlled reserve with lender execution.

This is an analog smart contract: the logic is programmable, but authority remains with contractually named parties and the account bank.

### Asset-pool credit

Spruce’s June 2024 solar facility calculates availability from a borrowing base tied to eligible solar assets. Defaulted, defective or terminated assets receive zero value; electronic custody files include customer, performance, interconnection, net-metering, permission-to-operate and warranty documents. Payment performance, debt-service coverage and borrowing-base deficiencies can cause early amortization or mandatory repayment. Annual audited GAAP statements and accountant reports remain required.

Sunnova’s earlier facility similarly used monthly servicer reports and asset eligibility tied to interconnection, operating state, payment performance, contract enforceability, perfected collateral and authoritative electronic records.

Solar finance therefore supplies the closest deployed prototype: the financed object is a changing pool of identified assets, contracts and cash flows, while enterprise reporting and assurance remain alongside it.

## Buildout states that can become finance events

| Buildout state | Existing evidence | Existing consequence | Continuous-finance extension | Non-negotiable boundary |
|---|---|---|---|---|
| OEM slot reservation | reservation agreement, deposit, window and conditions | sponsor or development capital is committed before full certainty | segregated reservation capital and live milestone tracking | reservation is not a firm order, FID, financing commitment or operating capacity |
| Firm equipment order | supply contract, progress schedule and guarantees | manufacturing payments enter the construction budget | signed production milestones can assemble a draw packet | OEM progress is not title, lien release, delivery or acceptance |
| Permit and interconnection | regulator and ISO/RTO records | conditions precedent and projected completion change | shared authority record can refresh eligibility | queue position is not an executable interconnection right |
| Construction | invoice, lien waiver, progress report and engineer certificate | controlled-account advance is released | AI can reconcile asset, schedule, invoice, change order and cost-to-complete | independent engineer and lien state remain distinct |
| Commissioning | governed performance test and completion certificate | term conversion, holdback or damages can occur | approved test packet can drive a bounded state transition | raw SCADA output is not the contractual test result |
| Operation | meter, market statement, invoice, outage and O&M records | waterfall, DSCR, reserve and distribution states change | near-continuous covenant and liquidity view | measurements can be corrected and markets resettled |
| Major maintenance | fired hours, starts, condition evidence, scope and work completion | reserve is accrued or released | event-based reserve calculations and approved-work payment | AI diagnosis is not causation, warranty coverage or safe return to service |
| Stress or default | covenant failure, nonpayment, prolonged outage or trigger notice | cash is trapped, draws stop and remedies begin | immediate policy-bound hold and early warning | only authorized parties can declare, waive or cure default |

## Logistics finance is a stack, not one coin

The useful object is a governed bundle:

```text
physical component or shipment
  -> signed identity and event record
  -> legally recognized title or control record
  -> eligible collateral, receivable or loan interest
  -> funding and repayment asset
  -> accounting, correction and remedy record
```

| Layer | Object | What it can prove or execute | What it cannot do alone |
|---|---|---|---|
| Logistics evidence | product, manufacturing, inspection, shipment or receipt event | source, sequence and time under stated controls | transfer title, prove conformity or create a lender claim |
| Title or control | electronic bill of lading, warehouse receipt or controlled electronic record | legally effective possession or control where governing law and system requirements allow | prove value, insurance, acceptance or freedom from competing claims |
| Credit asset | receivable, inventory interest, loan or participation | represent the obligation and support servicing or distribution | create repayment capacity, perfection, priority or recourse without legal documents |
| Cash asset | bank deposit, tokenized deposit or permitted payment stablecoin | fund and repay an approved obligation | prove the draw was earned, lawful or finally discharged |
| Network resource | native token used for fees or security | operate the chosen ledger | become the turbine, bill of lading, dollar claim or loan absent a separate legal mapping |

The legal hinge is **reliable control**, not immutability by itself. UNCITRAL’s Model Law on Electronic Transferable Records supplies a technology-neutral framework for authoritative electronic records, integrity and exclusive control. The United Kingdom’s Electronic Trade Documents Act 2023 gives qualifying electronic trade documents the same legal effect as paper equivalents when control and integrity requirements are met. In the United States, the operative analysis may involve UCC Article 7, Article 12 and other state-law classifications; a generic token does not automatically carry title or a perfected lien.

DCSA reports continuing carrier and platform movement toward interoperable electronic bills of lading, with 100% adoption targeted by 2030. Singapore’s TradeTrust provides a completed comparator in which businesses, banks and carriers used an interoperable electronic bill of lading in a live paperless shipment and letter-of-credit transaction.

## Named networks: different roles, not one winner

The public evidence supports a **federated recognition stack**, not a single
“logistics coin.” Hedera, Hyperliquid and Ripple currently demonstrate different
parts of the architecture. Their native tokens are not the financed turbine,
the project loan or the legal settlement asset unless a separate governing
instrument makes them so.

### Hedera — provenance and bounded private credit

Avery Dennison and Hedera reported that the atma.io connected-product platform
integrated Hedera services for item-level lifecycle and carbon-accounting
events. This is evidence that large physical-event systems can anchor ordered,
attributed records to a public DLT. It does not show that the record transferred
title, made inventory eligible collateral or caused a lender advance.

Hedera’s May 2026 Kea Credit case study reports $5.5 million of disbursed loans,
with invoices, inventory and trade instruments placed into short-duration
tokenized vaults and native USDC used as the cash leg. A separate cSigma case
shows the continuing underwriting constitution: substantial asset coverage,
first-loss capital, creditor-rights jurisdiction and other support remain
important. These are ecosystem and platform claims, not an audited loan tape or
filed energy facility.

A completed Aberdeen, Lloyds and Archax transaction used tokenized fund units
and UK gilts issued, transferred and held by an FCA-regulated custodian on
Hedera as FX collateral. The regulated issuer, custodian, trading agreement and
law made the collateral usable; the network alone did not.

### Hyperliquid — continuous price and margin state

Hyperliquid’s HIP-3 framework permits builder-deployed perpetual markets with
defined oracles, leverage and open-interest controls. The dated workbench
snapshot found live oil, gas and industrial markets. This can provide public
price, funding, open-interest and liquidation signals for treasury and risk
models.

The contracts are perpetual financial exposures without physical delivery.
They do not by themselves provide a rated hedge counterparty, ISDA/EEI/NAESB
documentation, lender collateral priority or a hedge admitted under a project
credit agreement. A regulated intermediary would have to wrap or guarantee the
exposure before it could become a lender-recognized project hedge.

### Ripple — institutional treasury, cash and prospective credit execution

Ripple’s current stack separates the XRP Ledger, XRP, RLUSD, Ripple Mint,
Ripple Treasury, Ripple Prime and the proposed XRPL Lending Protocol. Ripple’s
June 2026 protocol description expressly leaves creditworthiness, legal terms,
compliance and risk allocation offchain while standardizing execution after
approval. That is structurally compatible with a supplier or receivables
facility, but the amendments remained subject to validator approval and no
energy deployment was established.

Ripple Prime’s own $200 million debt facility is the useful funding clue:
conventional lender capital funds a regulated intermediary that can then offer
digital and traditional client financing. RLUSD, Mint and Treasury could make
project cash more programmable and continuously visible, while redemption,
credit approval, lender dominion, accounting and legal discharge remain under
their existing authorities.

### Network ruling

The three roles are complementary:

```text
Hedera-like provenance and title evidence
  + Hyperliquid-like price and margin telemetry
  + Ripple-like regulated treasury, custody and credit execution
  + bank / stablecoin cash and lender balance sheet
  + project contracts, accounting and courts
```

No primary source located joins these networks into one production energy
facility. The architecture becomes load-bearing only when the OEM, carrier,
inspector, insurer, lender, account bank and governing contract recognize a
controlled mapping among their records.

## Federated recognition stack

One energy project will continue to use several authoritative systems:

| Layer | Authoritative object | Candidate institution or technology class | Residual gate |
|---|---|---|---|
| Physical and scientific state | sensor, meter, inspection, performance test and model result | OEM, operator, utility, DOE laboratory or Genesis testbed | attribution, calibration, safety and contract effect |
| Provenance and oracle | signer, source, timestamp, configuration and model version | governed event fabric, accredited inspector or oracle service | whether the contract makes the event operative |
| Document and title | bill of lading, warehouse receipt, acceptance certificate and component identity | MLETR/UCC-compatible system, carrier, registry and custodian | governing-law recognition and fraud controls |
| Claim and collateral | receivable, inventory interest, equipment lien or tokenized security | lender, collateral platform, vault or institutional ledger | perfection, priority, valuation and bankruptcy treatment |
| Cash and treasury | bank deposit, tokenized deposit, payment stablecoin and reserve claim | bank, stablecoin issuer, treasury system and custodian | redemption, sanctions, account access and legal discharge |
| Credit and balance sheet | commitment, advance, first-loss capital, guarantee and margin financing | bank, private-credit fund, prime broker and insurer | underwriting, capital, concentration and loss-bearing |
| Price and risk transfer | commodity, power, equipment, basis and margin exposure | traditional exchange or bilateral hedge and onchain market | basis fit, liquidity and lender-approved counterparty/documentation |
| Accounting and adjudication | recognition, correction, default, priority, damages and discharge | ERP, accountant, agent, trustee, regulator and court | cannot be silently outsourced to protocol consensus |

The load-bearing requirement is not that every party runs the same chain. It is that the OEM, operator, carrier, inspector, insurer, lender, account bank and governing contract recognize a controlled mapping among their records.

## Genesis and the upstream evidence layer

Executive Order 14363 directs DOE to create an integrated platform combining high-performance computing, AI agents and models, federal and proprietary data, and autonomous or AI-augmented experimentation and manufacturing tools. The order also requires work on metadata, provenance, partnerships, data/model sharing, intellectual property and commercialization. DOE’s grid challenge calls for integrated data and AI in planning, interconnection, operations and security.

This is highly relevant upstream: Genesis can improve the models, test data, digital twins, standards and supply-chain evidence used in infrastructure decisions. It is not a bank, payment system or disclosed federal blockchain. No located source establishes that Genesis uses Hyperliquid, Ripple, Hedera or any other named public network.

The joined thesis is:

`Genesis improves what is knowable -> DLT improves what is shareable and executable -> regulated institutions decide what is fundable and legally operative`

Each arrow remains a separate implementation and authority gate.

## Stablecoin and GENIUS boundary

The GENIUS Act becomes effective on the earlier of January 18, 2027 or 120 days after final implementing regulations are issued. It creates the federal framework for payment-stablecoin issuers and preserves specified lawful DLT, tokenized-deposit and custody activities by banking institutions. It does not create project-finance underwriting criteria or make a stablecoin transfer proof of a completed project milestone.

For an energy facility, stablecoin or tokenized-deposit settlement could shorten supplier payment, margin, reserve and cross-border cash cycles. The governing agreement must still determine:

- which account or token is eligible;
- when a draw is earned and authorized;
- whether proceeds are unrestricted and legally discharged;
- who can pause, freeze, reverse or redeem;
- how sanctions, export controls and KYC apply; and
- how the payment is recognized and corrected in the books.

## What changes in underwriting and assurance

The basic credit questions remain: who owes the money, what repays it, which collateral and contracts exist, whether rights are perfected and enforceable, whether the project can be completed and operated, and who absorbs loss.

The new underwriting category is **observability and governability**:

1. stable identity for each financed asset, component, contract, account and signer;
2. durable data rights after an OEM, operator, servicer or oracle failure;
3. calibrated, versioned and reproducible measurements and models;
4. exact mapping from event logic to the executed project documents;
5. independently reproducible borrowing-base, covenant and cost-to-complete calculations;
6. cyber-segregation between operational technology and finance systems;
7. explicit correction, dispute, late-resettlement and business-continuity procedures; and
8. named pause, override, cure, approval and loss-bearing authority.

Better evidence can change advance rates, reserves, monitoring cost, covenant headroom and pricing. It does not do so merely because the record uses DLT.

The likely assurance transition is layered:

| Evidence or assurance object | Durable role |
|---|---|
| Live asset, market and account feed | current monitoring, eligibility, forecasting and exception detection |
| Quarterly statements | entity-wide reconciliation of operations, financing, estimates, tax and legal obligations |
| Annual GAAP audit | completeness, classification, valuation, consolidation, control and off-ledger liabilities |
| Agreed-upon procedures or control attestation | data lineage, event transformation, eligibility formulas, smart-contract logic and exceptions |
| Independent engineer | technical completion, cost-to-complete and governed performance evidence |
| Agent or depositary | policy execution, account control and exception governance |

The center of gravity can move from periodic document reconstruction toward continuous controls and exception testing without eliminating GAAP or independent assurance.

## Highest-value near-term applications

1. **Supplier and milestone working capital:** finance a verified purchase order, segregated inventory pool, accepted component, shipment or receivable rather than relying only on the supplier’s enterprise balance sheet.
2. **Construction-draw preflight:** reconcile invoice, asset identity, schedule, lien waiver, change order, engineer certificate and cost-to-complete before the authorized release.
3. **Continuous borrowing bases:** update eligibility, concentration, payment, default, title and collateral states more frequently.
4. **Maintenance reserves:** accrue from governed usage or condition evidence and release against approved work completion.
5. **Operating cash control:** connect meter, market, PPA, outage, reserve and debt-service states to a current liquidity and covenant view.
6. **Refinancing diligence:** preserve years of asset, contract, payment, maintenance and correction history in a reusable evidence package.

The first gains are most likely in working capital, receivables, inventory, construction draws, margin, reserves and monitoring—not anonymous public-chain loans that bypass project agreements.

## Exact negatives and return gates

No located primary evidence establishes:

- turbine SCADA, APM or digital-twin output directly releasing loan proceeds or tokenized deposits in production;
- an automated asset event becoming conclusive for a project draw, covenant cure or default;
- a named energy SPV receiving a stablecoin loan with the complete lender-to-borrower, collateral, finality and accounting chain disclosed;
- a project lender accepting a public-chain energy perpetual as a permitted project hedge without a regulated and documented wrapper;
- a named Genesis project integrating operating DLT settlement into its grid or asset workflow; or
- removal of annual GAAP audit requirements because a DLT asset ledger is accepted as sufficient evidence.

Promote the architecture to production fact only when a named transaction supplies:

1. the executed financing clause recognizing the event or ledger state;
2. the asset, meter, engineer, title or work-event schema;
3. identity, signature, calibration and correction controls;
4. lender or agent reliance and liability allocation;
5. the restricted-account, tokenized-deposit or stablecoin instruction path;
6. evidence of an actual draw, reserve, borrowing-base, price or covenant action;
7. accounting, audit and tax treatment; and
8. pause, reversal, default, dispute, cyber-recovery and loss-bearing procedures.

## Primary sources

### Executed project and asset-finance documents

- [Long Ridge — 2019 first-lien credit agreement](https://www.sec.gov/Archives/edgar/data/1590364/000159036419000004/firstliencreditagreement-e.htm)
- [Long Ridge Energy — 2025 credit agreement](https://www.sec.gov/Archives/edgar/data/1899883/000114036125005888/ef20044242_ex10-1.htm)
- [Rio Grande LNG Train 5 — credit agreement](https://www.sec.gov/Archives/edgar/data/1612720/000161272026000009/ex1092-4q25.htm)
- [CP2 LNG — 2025 credit agreement](https://www.sec.gov/Archives/edgar/data/2007855/000200785525000066/exhibit104-q32025.htm)
- [FuelCell Energy/NRG — loan and depositary agreement](https://www.sec.gov/Archives/edgar/data/886128/000088612814000017/exhibit1083nrgloanagreement.htm)
- [Spruce SET Borrower — 2024 credit agreement](https://www.sec.gov/Archives/edgar/data/1772720/000162828024030550/ex101-spruxdebtfinancing.htm)
- [Sunnova — 2019 credit agreement](https://www.sec.gov/Archives/edgar/data/1772695/000119312519184324/d709190dex106.htm)

### Data, title and logistics infrastructure

- [DOE — Orange Button solar data standard](https://www.energy.gov/cmei/systems/orange-buttonr-solar-data-standard)
- [UNCITRAL — Model Law on Electronic Transferable Records](https://uncitral.un.org/en/texts/ecommerce/modellaw/electronic_transferable_records)
- [UK Electronic Trade Documents Act 2023](https://www.legislation.gov.uk/ukpga/2023/38/contents)
- [Uniform Law Commission — UCC and Article 7](https://www.uniformlaws.org/acts/ucc)
- [Uniform Law Commission — 2022 UCC amendments and enactment tracker](https://www.uniformlaws.org/committees/community-home?CommunityKey=1457c422-ddb7-40b0-8c76-39a1991651ac)
- [DCSA — electronic bill-of-lading commitment](https://dcsa.org/get-involved/100-percent-ebl)
- [DCSA — June 2026 interoperability state](https://dcsa.org/newsroom/bel-interoperability-with-omer-guy)
- [Singapore IMDA — TradeTrust](https://www.imda.gov.sg/how-we-can-help/international-trade-and-logistics/tradetrust)
- [Singapore IMDA — live interoperable electronic bill-of-lading transaction](https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2023/sg-india-interoperable-electronic-bills-of-lading)

### Named network evidence

- [Hedera / Avery Dennison atma.io](https://hedera.com/blog/avery-dennisons-atma-io-connected-product-cloud-to-utilize-the-hedera-network-to-account-for-carbon-emissions-of-billions-of-unique-items/)
- [Hedera — Kea Credit case study](https://hedera.com/case-study/kea-credit/)
- [cSigma — institutional borrower requirements](https://www.csigma.finance/edge)
- [Lloyds Banking Group — completed tokenized-collateral transaction](https://www.lloydsbankinggroup.com/media/press-releases/2025/lloyds-banking-group-2025/digital-assets-breakthrough.html)
- [Hyperliquid — HIP-3 builder-deployed perpetuals](https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-3-builder-deployed-perpetuals)
- [Hyperliquid — contract specifications](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/contract-specifications)
- [Ripple Prime — $200 million debt facility](https://ripple.com/ripple-press/ripple-prime-secures-usd200-million-debt-facility-from-neuberger-specialty-finance-to-expand-capacity/)
- [Ripple — proposed XRPL Lending Protocol](https://ripple.com/insights/the-xrpl-lending-protocol-bringing-credit-infrastructure-onchain/)
- [Ripple — RLUSD terms](https://ripple.com/legal/stablecoin/)
- [Ripple Treasury](https://ripple.com/ripple-press/ripple-treasury-launches-the-first-treasury-management-system-tms-with-native-digital-asset-capabilities/)

### Federal, banking and settlement framework

- [Executive Order 14363 — Launching the Genesis Mission](https://www.federalregister.gov/documents/2025/11/28/2025-21665/launching-the-genesis-mission)
- [DOE — Scaling the Grid to Power the American Economy](https://www.energy.gov/undersecretaryforscience/genesis-mission/scaling-grid-power-american-economy)
- [DOE — Genesis Mission challenge portfolio](https://www.energy.gov/undersecretaryforscience/genesis-mission/genesis-mission-national-science-and-technology-challenges)
- [BIS — Project Genesis 2.0](https://www.bis.org/publ/othp58.htm)
- [Public Law 119-27 — GENIUS Act](https://www.govinfo.gov/content/pkg/PLAW-119publ27/html/PLAW-119publ27.htm)
- [OCC — Lending and Loan Portfolio Risk Management, June 2026](https://www.occ.treas.gov/publications-and-resources/publications/comptrollers-handbook/files/lending-loan-portfolio-risk-management/pub-ch-lending-loan-portfolio.pdf)
- [Federal Reserve — SR 26-2 model-risk guidance](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm)
