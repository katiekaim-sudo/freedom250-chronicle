# SWIFT ledger — activation, legal constitution and finality

**Research cutoff:** 2026-07-21  
**Status:** ready for initial use; named banks preparing live pilots; no first completed SWIFT-ledger transaction publicly established  
**Control:** hypotheses are marked. A product announcement, transaction execution, customer credit, external cash settlement and legal finality are separate states.

## Executive ruling

The ledger's strategic object is not a SWIFT coin. It is a **funded interbank commitment** that SWIFT records, validates, synchronises and—in the March 2026 Payments Market Practice Group description—notarises across bank-controlled liabilities.

The public architecture is:

1. participating banks retain their own tokenised-deposit environments, keys, assets, funding and settlement authority;
2. SWIFT operates a shared Besu/EVM orchestration and notary layer;
3. the payer-side commitment is funded and confirmed before execution;
4. a receiving bank may make customer funds available overnight or on weekends; and
5. final cash settlement remains outside the ledger through RTGS, correspondent accounts or another participant-agreed mechanism.

Two objects remain undisclosed:

- **the funding object** — reservation, segregated balance, collateral, credit line, correspondent balance, net position or something else;
- **the gap bearer** — the bank or provider carrying principal and liquidity exposure if customer funds become usable before external settlement completes.

## Factual findings

### 1. The ledger is a notary for bank liabilities

The March 2026 PMPG minutes describe a central 24/7 infrastructure focused initially on tokenised-deposit corporate payments and acting as a **notary for interbank liabilities**. Participants also explored external-settlement connections for liquidity management and discussed clearing, atomic settlement and netting across central- and commercial-bank systems.

“Explored” is design evidence. It does not prove that every discussed function is implemented in the MVP.

Source: [PMPG Monthly Meeting Minutes, 24–26 March 2026, item 5.1, p. 6](https://www.swift.com/swift-resource/252568/download).

### 2. “Funded upfront” is an outcome, not yet a known legal object

SWIFT says commitments are funded before execution and visible to relevant parties in real time. Public material does not establish that the funding is segregated, irrevocably earmarked, bankruptcy-remote, collateralised or immediately available to the receiving bank in final cash.

Source: [SWIFT — enabling bank liquidity management in an always-on world](https://www.swift.com/payments/payment-innovation/blockchain-based-ledger/enabling-bank-liquidity-management-always-world).

### 3. Four clocks sit underneath “instant settlement”

| Clock | Event | Public state |
|---|---|---|
| **Bank token/funding** | payer bank reserves or identifies value behind its commitment | funding outcome stated; mechanism undisclosed |
| **SWIFT commitment** | shared ledger validates, records and coordinates the interbank promise | product capability stated |
| **Customer credit** | receiving bank makes funds usable | intended overnight/weekend capability; first public transaction missing |
| **External cash finality** | the banks' final obligation is discharged through RTGS, correspondent accounts or another mechanism | explicitly off-ledger; corridor-specific rail missing |

No source located by the cutoff collapses those four moments into one universal final-settlement event.

### 4. A participant constitution exists, but its operative documents are missing

SWIFT says access is restricted to regulated institutions and verified entities, rules governing commitments and settlement are defined, and governance is shared among participating institutions. SWIFT also says it is not the money issuer, custodian, settlement agent or financial market infrastructure.

The public ledger rulebook, executed participation form, pricing object, failure/reversal provisions and node/control schedule were not located. The operative constitution may be assembled through the SWIFT General Terms and Conditions, a Swift Solution rulebook, ordering records, activation notices, participant agreements and restricted MySwift Knowledge Centre material.

Source: [SWIFT — a future built on trust](https://www.swift.com/payments/payment-innovation/blockchain-based-ledger/future-built-trust).

### 5. The ordinary public terms did not reveal a ledger-specific amendment

The public legal-site and version audit did not locate a ledger-named change in the ordinary website terms or a public ledger participation agreement. That negative finding does not prove the participant terms are unchanged: product-specific and highest-precedence documents can sit in a rulebook, order, quotation, click-through acknowledgement or controlled customer environment.

The safe statement is **no public ledger-specific terms object located**, not “no terms changed.”

### 6. Belgian law creates the strongest disclosure route

Belgium's Law of 25 May 2025 on the supervision of providers of financial messaging services entered into force on 1 January 2026. SWIFT's 2025 Annual Review says the National Bank of Belgium designated SWIFT in early 2026 and the framework becomes applicable to it on **1 October 2026**. The exact NBB designation-list object and date were not located.

The most relevant statutory hooks are:

- **Article 3(4):** a broad service perimeter including closely related operational and ancillary services;
- **Articles 40–41:** operator responsibility and NBB authorisation/information routes for critical or important outsourcing;
- **Article 46:** enforceable rules and contracts across relevant legal systems;
- **Articles 47–48:** risk incentives, recovery and orderly wind-down;
- **Article 71:** public, non-discriminatory access and orderly suspension/exit criteria;
- **Article 73:** public key rules and procedures, clear service descriptions, rights and obligations, supporting documentation and per-service fees.

The law does not guarantee public disclosure of every bilateral contract, smart contract, security control or node configuration. It creates a statutory route to the public core of the service constitution if the ledger is within the regulated service perimeter.

Sources: [Belgian Law no. 2025004515](https://refli.be/fr/lex/2025004515); [SWIFT Annual Review 2025](https://www.swift.com/sites/default/files/files/2025-swift-annual-review_v08-1.pdf); Reading the Charter — SWIFT.

### 7. The public post is an architecture statement, not a new legal state

On 20 July 2026 at 10:01 UTC, SWIFT said its approach differs because it extends infrastructure already trusted by its member community and is designed to help the existing ecosystem evolve rather than replace it. That confirms the incumbent-orchestrator strategy. It does not promote the ledger beyond “ready for initial use / pilots preparing.”

Event: 2026-07-20-1001 - Why is Swifts approach to blockchain different.

## Control architecture

| Layer | Confirmed authority | Missing activation evidence |
|---|---|---|
| **Bank liability/token** | issuing or participating bank | exact legal debtor, token terms, reservation and bank-book priority |
| **Bank adapter** | bank retains its environment and keys | system of record, interface events and double-commitment prevention |
| **SWIFT commitment/notary** | SWIFT operates shared orchestration | validator roster, contract administration, schema, rollback and governance votes |
| **Customer credit** | receiving bank | provisional/final status, unrestricted availability and reversal rights |
| **External final cash** | banks plus RTGS/correspondent/agreed mechanism | rail, accounts, asset, operating hours, gross/net rule and legal-finality event |
| **Operator oversight** | NBB plus cooperative central-bank oversight | ledger classification, conditions and exact designation object |

## Bank-adapter boundary

HSBC is the only bank in the announced cohort located in this pass expressly connecting a named bank product—its Tokenised Deposit Service—to the SWIFT ledger.

Citi Token Services, DBS Treasury Tokens, Standard Chartered/Ant Whale balances, Lloyds Canton deposits, BNY digital cash, UBS Digital Cash and Kinexys-linked products are adjacent systems operated or used by cohort banks. Shared membership or technical compatibility does not establish that any is the bank's SWIFT adapter.

The common SWIFT proposition must normalise legally different bank objects into a signed commitment with currency, amount, conditions, expiry and authority. The commitment schema—not Besu alone—is the interoperability control point.

## Weekend-liquidity and failure test

Plausible bridges include a gross reservation, prefunded correspondent balance, bilateral credit limit, collateralised facility, deferred netting, a designated settlement bank or an always-open external settlement rail. SWIFT has not publicly selected one universal mechanism; corridor and currency may control.

The minimum failure question is:

> If the receiving customer can use funds before external cash settles, do those funds stand when the external leg fails—and which bank, collateral pool, credit line or loss-sharing rule pays?

The rulebook must also resolve reservation expiry, replay/double use, sanctions or fraud holds, bank insolvency, ledger/book conflict, node failure, reversal, interest/overdraft cost and loss allocation.

A useful non-SWIFT control landed on 9 July: Citi and Siam Commercial Bank announced a US-holiday-weekend USD payment using Citi Token Services and Citi's 24/7 USD Clearing. That case proves one bank can place the token and clearing bridge inside its own controlled network. It does not prove SWIFT's multi-bank bridge.

Source: [Citi/SCB transaction](https://www.citigroup.com/global/news/press-release/2026/siam-commercial-bank-citi-24-7-usd-clearing-near-real-time-cross-border-payments-citi-token-services).

## Stablecoin boundary

No source located by the cutoff establishes a stablecoin as current SWIFT-ledger funding, collateral or settlement value. Tokenised deposits and payment stablecoins preserve different issuers, reserve/redemption structures, insolvency regimes, custody models, freeze powers and chain risks.

A future stablecoin claim requires a named:

- token and issuer;
- legal classification and eligible holder;
- reserve/redemption and insolvency treatment;
- custody, wallet and bank-adapter path;
- SWIFT commitment role;
- external settlement or redemption asset; and
- depeg, blacklist/freeze, fork and issuer-default rule.

The first stablecoin could enter as **funding**, **collateral**, **settlement value** or an **external asset whose movement SWIFT coordinates**. Those are four different architectures.

## Status ladder

| Level | Permitted status | Evidence gate |
|---:|---|---|
| 0 | research hypothesis | adjacent capability only |
| 1 | configured/connected | named legal entity, environment and SWIFT connection |
| 2 | scheduled | both sides, currency, use case and planned live state |
| 3 | executed | occurrence plus a transaction-level field |
| 4 | recipient credited | usable-funds time separated from execution |
| 5 | final cash settlement | external asset/system and finality event identified |
| 6 | legal finality verified | rulebook covers irrevocability, reversal, record priority, default and loss |

## Disclosure clocks

| Date | Surface | Evidence target |
|---|---|---|
| 29 Jul 2026 | Standard Chartered half-year results | Ant/Whale role, SWIFT product, currency or corridor |
| 4 Aug 2026 | HSBC interim results | TDS entity/location, counterparty, transaction or volume |
| 6 Aug 2026 | DBS results | Treasury Tokens-to-SWIFT connection and currency |
| 28 Sep–1 Oct 2026 | Sibos Miami | named transaction, live demonstration, customers, implementation details or rulebook |
| 1 Oct 2026 | Belgian framework stated applicable to SWIFT | designation list, ledger classification, key rules, criteria, service description and fees |
| 13 Oct 2026 | Citi Q3 results | CTS connection or another external-bank live case |

## Exact promotion objects

1. NBB designation-list entry and effective date.
2. Express NBB/SWIFT classification of the ledger service.
3. Ledger rulebook, participation/order object and version history.
4. Commitment schema, reservation/expiry rule and signature method.
5. Node, validator, privacy-group and contract-administration schedule.
6. First transaction with both legal entities, currency, date and transaction-level field.
7. Customer-credit time and provisional/final status.
8. External settlement rail, accounts, asset and finality event.
9. Default, reversal, insolvency and loss-allocation rule.
10. Stablecoin eligibility rule, if one is admitted.

## Research judgment

The evidence does not establish a new universal final-settlement rail. It shows SWIFT moving beyond message transmission into shared execution/notary coordination while leaving issuance, custody, funding and final cash with banks and existing systems.

The product's load-bearing object is therefore its constitution. Besu supplies a state machine. The rulebook determines whose promise counts, when the receiving customer can use it, what record wins and who carries the loss if the external settlement layer does not complete.

Related: FINTECH_SWEEP_PAYMENT_ORCHESTRATORS · FINTECH_CRYPTO_CLAIM_AUDIT · FINTECH_CRYPTO_TRANSITION_TIMELINE · 2026-07-12 - The Private Stack — Who Owns the Gates · The Clearing-House Transition
