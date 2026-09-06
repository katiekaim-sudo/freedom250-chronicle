# GENIUS Act x Scientific Trust Stack Crosswalk

**Evidence cutoff:** 2026-08-17  
**State:** active workbench bridge; not vault-canonical  
**Authority rule:** enacted law outranks proposals; final rules outrank forms,
questions and guidance; transaction-specific instruments and operating evidence
determine the exact issuer, token and intermediary state.

## Executive ruling

GENIUS supplies the monetary specimen of the Scientific Trust Stack.

```text
statutory authority and regulatory perimeter
  -> named issuer, intermediary, custodian and token object
  -> ownership, control, disclosures and certifications
  -> authority-specific eligibility decisions
  -> exact contract, chain, administrator keys and delegated functions
  -> controlled mint, redeem, custody, offer and sale actions
  -> logged issuance, transfer, freeze, burn and redemption events
  -> reserve, supply, custody and contract provenance
  -> independent accounting, technical and supervisory validation
  -> distribution, suspension, revocation, correction, appeal or insolvency remedy
  -> cryptographic migration sufficient to keep the evidence verifiable
```

At the current cutoff, this architecture can issue only
`pre-effective-readiness` or `design-validation` receipts. It cannot publish a
live GENIUS eligibility list because the located record contains no named PPSI
approval, SCRC certification, foreign comparability determination or foreign
issuer registration.

The Act does not put law on a blockchain. It makes named issuers,
cryptographic capabilities, reserve arrangements and distribution
intermediaries answerable to law.

## Four truth classes translated into money

| Scientific Trust Stack truth | Stablecoin translation | Best available proof | What the proof cannot establish |
|---|---|---|---|
| Identity truth | Which legal person is the issuer, reserve owner, custodian, DASP, token administrator or holder-facing obligor? Which contract and key represent the technical object? | charter/application/approval, legal identifier, contract address, chain ID, code hash, public key or key identifier | authority to issue; legal title to reserves; current key control; economic truth |
| Permission truth | May this issuer issue, this DASP offer or sell, this custodian hold, or this key mint, burn, freeze or upgrade this exact object now? | regulator decision, final rule, registration, scoped role, multisignature policy, signed configuration | reserve sufficiency; wisdom or legality of the underlying policy; correct exercise of the permission |
| Provenance truth | Which mint, burn, bridge, wrapper, contract version, reserve report and status change produced the current state? | ledger history, signed event, code hash, bridge lineage, report hash, authoritative time, supersession link | completeness of off-chain facts; legal classification; solvency; absence of hidden liabilities |
| Economic and legal truth | Is each token backed as required, redeemable under the disclosed policy, legally segregated and subject to the correct holder and insolvency rights? | custodian and bank records, reserve composition, registered-accounting-firm examination, CEO/CFO certification, supervisory examination, legal instruments | cryptographic signatures cannot make false source data true or cure an unlawful order |

## Thirteen-layer crosswalk

| Layer | Scientific Trust Stack question | GENIUS object and authority | Current evidence state at cutoff | Typed receipt or decision | Evidence required to promote | Change triggers and limits |
|---|---|---|---|---|---|---|
| 0. Mission and authority | What law and purpose authorize the gate? | Public Law 119-27; principally sections 3, 4, 5, 8, 10-13, 18 and 20; codified at 12 U.S.C. 5901 et seq. | enacted; core implementation materially proposal-stage | `authority-in-scope`, `not-in-jurisdiction`, `effective-date-pending` | operative section, implementing final rule, effective date and responsible regulator | statutory amendment, final rule, judicial order, waiver or effective-date acceleration |
| 1. Subject identity | Who or what is acting? | permitted or foreign issuer; DASP; reserve owner; custodian; accountant; token administrator; contract; bridge or wrapper operator | statutory classes exist; exact approvals and classifications unresolved in material part | `identity-resolved`, `identity-ambiguous`, `issuer-unresolved` | legal name and identifier, parent chain, regulator, token brand, chain ID, contract address, code hash and responsible obligor | novation, merger, affiliate transfer, contract migration, new chain, new wrapper or changed administrator |
| 2. Ownership and sponsorship | Who owns, controls, guarantees or operationally administers each box? | applicant and controlling persons; reserve beneficial owner, legal title/account holder, custodian and subcustodian; redemption controller; token administrator; issuer versus distributor; foreign jurisdiction | application and entity-specific; no universal registry joins all boxes | `ownership-resolved`, `control-mitigated`, `control-unresolved` | beneficial ownership, governance rights, reserve legal title and account control, custody/subcustody, redemption control, key-control arrangement, service-provider contracts and effective dates | ownership, governance, financing, account holder, custodian, key quorum, redemption control or service-provider change |
| 3. Disclosure and attestation | What did each responsible party assert? | section 4 monthly reserve composition; outstanding issuance; CEO/CFO certification; redemption policy; foreign-issuer representation under Treasury's proposed section 3 rule | statutory disclosure/certification duties enacted; current Treasury reliance mechanics proposed | `reserve-report-current`, `certification-current`, `representation-unverified` | exact report period, supply value, reserve composition, custody geography, report hash, signatory identity and regulator receipt | month end, corrected filing, reserve change, false certification, issuer or accountant change |
| 4. Institutional controls | Does the organization maintain the required operating control system? | capital, liquidity, diversification, interest-rate, operational, compliance, IT, BSA/AML and sanctions controls under section 4; custody controls under section 10 | statutory requirements enacted; detailed federal/state implementation uneven and partly proposed | `control-attested`, `control-examined`, `deficiency-open`, `control-unresolved` | applicable final standard, policy/control evidence, independent test, supervisory exam, deficiency and remediation state | incident, control failure, regulatory finding, service-provider change, new chain or material scale increase |
| 5. Risk and eligibility | Which authority permits which activity? | section 5 issuer approval; state regime and SCRC route; section 18 foreign comparability/OCC registration; section 3 DASP offer/sale perimeter | no located named GENIUS PPSI approval, SCRC certification, foreign comparability determination or foreign registration through cutoff | `issuer-permitted`, `offer-sale-permitted`, `transition-pending`, `suspended`, `revoked`, `unresolved` | final rule, application, approval/registration, public list entry, conditions, effective time and scope | status change, list update, reserve failure, illicit-finance risk, comparability rescission or noncompliance designation |
| 6. Credential and delegation | Which credential, role or key may perform which action? | issuer officers; administrator/mint/burn/freeze/upgrade keys; custodian roles; DASP compliance decision; accountant signature | cryptographic delegation is implementation-specific; no universal GENIUS credential profile located | `key-active`, `key-rotating`, `key-revoked`, `delegation-scoped`, `delegation-unresolved` | key identifier and algorithm, controller, custody/HSM or MPC arrangement, quorum, role, action scope, validity and revocation route | key compromise, rotation, signer change, quorum/policy change, contract upgrade or quantum migration |
| 7. Controlled resource access | What may the actor touch or do? | issue, redeem, manage reserves, custody stablecoins/reserves/private keys; DASP offer, sale, transfer or custody; lawful-order action | activity limits enacted; precise workflow and whitelist mechanics entity-specific | `mint-authorized`, `redeem-authorized`, `custody-authorized`, `distribution-authorized`, `action-denied` | legal authority plus runtime authorization bound to exact contract, key, amount, network, jurisdiction and time | authorization expiry, status change, transaction limit, incident, lawful order or network migration |
| 8. Execution telemetry | What action occurred, when, under which authority and version? | issuance, redemption, burn, removal from circulation, transfer block, reserve movement, supply report and DASP restriction | public ledgers expose some events; FDIC telemetry and other reporting objects remain proposal/information-collection layers where applicable | `execution-recorded`, `execution-reconciled`, `execution-disputed` | authoritative time/block, actor/key, contract version, instruction, transaction ID, amount, before/after state, off-chain journal and exception | chain reorganization, corrected record, disputed authorization, reporting reconciliation or reversal |
| 9. Provenance | How did this token or report acquire its current identity? | original issuance; redeemed/reissued tokens; chain migration; wrapped or bridged representation; reserve report and contract lineage | Treasury Questions 16-21 expose the classification problem; no final bridge/wrapper rule located | `native-issued-object`, `issuer-authorized-representation`, `third-party-wrapper`, `classification-unresolved` | lock/burn/mint mechanics, controllers, reserve and redemption rights, contractual obligations, supply reconciliation, code and report hashes | new bridge, altered custody, broken peg, contract upgrade, redemption change or loss of underlying assets |
| 10. Independent validation | Is the asserted system fit for the claimed use? | registered-accounting-firm monthly examination; supervisory examination; technical testing of lawful-order and key controls; supply/reserve reconciliation | accounting duty enacted; Treasury asks, but has not finally required, DASP smart-contract examination | `accountant-examined`, `technical-function-tested`, `supervisory-validated`, `validation-unresolved` | examiner identity, standard and scope, test environment, exceptions, sample/coverage, result, date and remediation | new report period, contract/key change, audit exception, incident, reserve shortfall or control redesign |
| 11. Consequence and remedy | What happens when facts, authority or state are wrong? | lawful-order execution; section 8 foreign noncompliance; application denial/appeal; registration rescission/revocation; section 11 holder priority and insolvency; correction and reissuance | remedies enacted in law; many operating pathways await rules and first use | `freeze-required`, `burn-required`, `secondary-trading-prohibited`, `corrected`, `superseded`, `appeal-pending`, `insolvency-priority` | final valid order or decision, exact object, action log, notice, cure, review/appeal, corrected state and downstream propagation | appeal, cure, rescission, court order, mistaken match, key compromise, reserve deficiency or insolvency |
| 12. Cryptographic durability | Will identity, authorization and evidence remain trustworthy through algorithm migration? | wallet and issuer signatures; administrator keys; HSM/MPC; software and report signing; TLS/APIs; long-lived audit records | no reviewed GENIUS instrument expressly mandates PQC, crypto agility or CBOM | `classical-current`, `migration-planned`, `hybrid-tested`, `pqc-operating`, `algorithm-deprecated` | named system, algorithm/profile, inventory, owner, compatibility test, cutover, revocation and archived-proof validation | cryptanalytic break, NIST withdrawal, regulator standard, system upgrade, key lifetime or interoperability failure |

## The legal-to-runtime join

The core join is a two-key system:

```text
LEGAL KEY
  regulator + authority + decision + scope + effective time

CRYPTOGRAPHIC KEY
  exact controller + algorithm + role + contract + network + validity

JOINED ACTION
  this legal person, acting through this currently valid key,
  may perform this action on this exact token object under this authority
```

Neither key can substitute for the other. A regulator approval does not prove
which key controls a deployed contract. A valid signature does not prove that
the signer possessed legal authority.

## The reserve-oracle seam

GENIUS combines an on-chain liability surface with reserves that may include
cash, Federal Reserve balances, deposits, Treasury securities, repos,
government money market funds and permitted tokenized forms.

```text
on-chain supply at authoritative block/time
  + redeemed but not yet burned or removed objects
  + off-chain customer and omnibus liabilities
  -> reconciled outstanding liability

custodian/bank/depository records
  + legal title and segregation
  + asset eligibility, tenor, geography and valuation
  + liens, reuse and encumbrance state
  -> reconciled eligible reserve

registered-accounting-firm examination
  + CEO/CFO certification
  + regulator receipt/examination
  -> authority-backed monthly reserve assertion
```

A public-key signature can authenticate each component. It cannot establish
that an omitted account, lien, liability or side agreement does not exist.

## The bridge and wrapper identity test

A bridged or wrapped object must not inherit the underlying token's eligibility
by ticker or brand alone. Resolve at least:

1. who controls lock, mint, burn, release and upgrades;
2. who owes redemption and under which contract;
3. whether the underlying token remains segregated and available;
4. whether supply is one-for-one and continuously reconcilable;
5. whether a new legal claim or issuer has been created;
6. whether lawful-order functions reach both the underlying and representation;
7. which DASP offers or sells the representation in the United States; and
8. which failure, correction, insolvency and appeal regime applies.

Until those fields resolve, issue a `bridge-wrapper-classification` receipt
with status `unresolved`. Do not inherit `issuer-permitted` automatically.

## Lawful-order capability is three separate receipts

```text
CAPABILITY
  the exact deployed contract/key arrangement can perform the required action

AUTHORITY
  a final valid order identifies the stablecoin or account with sufficient
  particularity and preserves the applicable review or appeal

EXECUTION
  the responsible issuer/intermediary performed the action and logged the
  resulting state, exceptions and remedy
```

Treasury's August 17 proposal asks whether a DASP should examine smart contracts
and verify seize, freeze and burn functions. That is evidence of a possible
future capability test, not a current final duty.

## The distribution whitelist

The blockchain may continue to produce blocks while the legal perimeter changes
at issuers, custodians, exchanges, processors and other covered intermediaries.

```text
issuer/token status change
  -> authority-specific decision receipt
  -> DASP due diligence and product configuration
  -> buy/mint/deposit/transfer/offer/sale restrictions
  -> notice, wind-down, correction or appeal
```

This is why distribution eligibility must identify the exact DASP, product,
jurisdiction, token contract and time. It is not a universal property of the
underlying network.

## Required receipt bundle

For one asserted U.S. distribution pathway, require at least these independent
decision types:

| Decision type | Required scope |
|---|---|
| `authority-and-effective-date` | statutory section, implementing instrument, effective state and clock |
| `issuer-identity` | legal issuer/redemption obligor, parent chain, regulator and jurisdiction |
| `issuer-permission` | approval route, conditions and current state |
| `state-regime-certification` | final Treasury principles, SCRC process, state submission, SCRC decision, cure and annual recertification |
| `foreign-country-comparability` | exact country, SCRC recommendations, Treasury determination, justification and rescission state |
| `foreign-issuer-registration` | exact issuer, OCC filing/receipt, decision or deemed approval, public list and current status |
| `foreign-lawful-order-representation` | issuer representation, DASP due diligence, technical capability evidence and contradictions |
| `foreign-noncompliance-status` | Treasury designation, cure, Federal Register notice, secondary-trading effect and review |
| `token-contract-identity` | brand, symbol, chain ID, contract address, code hash and native/wrapped state |
| `cryptographic-control` | administrator/mint/burn/freeze/upgrade roles, keys, algorithms, quorum and custody |
| `lawful-order-capability` | functions, test evidence, limits, controller and last verification |
| `reserve-and-supply` | authoritative supply, reserve report, custody, valuation, encumbrance and reconciliation |
| `accounting-and-supervision` | accountant examination, CEO/CFO certification and supervisory state |
| `custody-and-segregation` | customer/reserve/private-key custody, segregation, priority and service providers |
| `offer-sale-eligibility` | DASP, jurisdiction, permitted object, diligence, restrictions and wind-down |
| `bridge-wrapper-classification` | underlying, representation, controller, redemption rights and supply lineage |
| `monitoring-and-remedy` | owner, recheck, triggers, incidents, correction, revocation and appeal |
| `cryptographic-durability` | inventory, algorithm state, migration owner, cutover and archived-proof validation |

The foreign receipts are deliberately non-fungible. Country comparability does
not approve an issuer. OCC registration does not prove current lawful-order
capability. Absence of a Treasury section 8 prohibition does not establish that
a DASP's due diligence is sufficient. DASP distribution eligibility must join,
rather than collapse, those results.

## Observable state ladder

```text
statutory class
  -> proposed implementation
  -> final rule
  -> effective requirement
  -> application or registration
  -> regulator decision
  -> contract/key configuration
  -> independent test or examination
  -> operating issuance/distribution/redemption
  -> monitored continuing eligibility
  -> correction, suspension, revocation, appeal or insolvency
```

Never jump from proposal to operating control, from application to approval, or
from valid signature to substantive truth.

## Observatory synthesis

The same architecture now appears in science and money:

| Science | Stablecoin money |
|---|---|
| researcher/institution/agent identity | issuer/DASP/custodian/contract/key identity |
| research-security eligibility | issuer and distribution eligibility |
| delegated data/compute/instrument access | scoped mint/redeem/custody/offer/sale authority |
| execution receipt | issuance, transfer, burn, freeze and redemption receipt |
| data/model/software provenance | contract, supply, reserve-report and wrapper provenance |
| independent scientific validation | accounting, technical and supervisory validation |
| award correction/revocation/appeal | correction, delisting, registration revocation, appeal and insolvency priority |
| PQC durability of scientific evidence | PQC durability of keys, attestations, instructions and audit evidence |

The deeper national story is not that one database or blockchain has become the
source of truth. It is that capital, science and money are moving through
typed, machine-checkable, revocable permission layers whose legitimacy still
depends on law, authoritative source records and human judgment.

## Primary source set

- [Public Law 119-27 - GENIUS Act](https://www.govinfo.gov/content/pkg/PLAW-119publ27/pdf/PLAW-119publ27.pdf)
- [Treasury Section 3 proposal - public-inspection copy, FR Doc. 2026-16796](https://public-inspection.federalregister.gov/2026-16796.pdf)
- [Treasury state-regime substantial-similarity proposal](https://home.treasury.gov/system/files/136/NPRM-GENIUS4c-Principles.pdf)
- [FDIC proposed GENIUS reporting forms and notice](https://www.federalregister.gov/documents/2026/07/20/2026-14589)
- [OCC licensing and registration forms notice](https://www.federalregister.gov/documents/2026/07/27/2026-15088)
- `GENIUS Act Implementation Gap Audit`
