# SWIFT ledger — what has actually gone live?

> September 9 follow-up: Funding, binding commitments, cross-network liquidity and FX is the maintained four-question deepening, with the Siemens sequence, illustrative accounting and public-term gaps. Earlier dated findings retain their original cutoff.

**Answer:** SWIFT's shared ledger has progressed from readiness to bank-reported live transactions in a controlled rollout. The strongest newly located evidence includes named interbank pairings, HKD and USD payments, a dated weekend Singapore–New York payment, identified bank deposit systems, matching/netting, and a report of completed correspondent settlement. General commercial availability, recurring network volume and a publicly inspectable legal-finality constitution remain unestablished by these disclosures.

**Scope:** official SWIFT architecture and participant-bank disclosures available through September 9, 2026, 9:35 p.m. EDT. The later bank review covered all 17 roster participants and material adjacent programmes; it is not exhaustive coverage of every bank project or a fresh legal-regulatory review. Three agents supplied bank lanes; the lead reconciled material sources and the recovered BNP PDF. Publication dates below are not transaction dates unless explicitly stated.

**Relationship to saved research:** extend the existing `swift-shared-ledger` identity. The Chronicle's July architecture dossier remains the detailed historical architecture/retrieval baseline, with its September 3 limited refresh. Its statement that completed transactions had not been established is now superseded by the evidence below. The later bank/partnership expansion is saved in the Workbench; this research pass did not update the Chronicle or build/install the app.

## What the offering does

SWIFT described initial readiness on **July 9, 2026**, with 17 banks preparing live pilots and broader availability to follow controlled activation. Customer availability can precede final settlement. That announcement alone was not transaction evidence. [SWIFT readiness](https://www.swift.com/news-events/press-releases/swifts-blockchain-ledger-ready-use-17-banks-set-pioneer-tokenised-cross-border-payments-trusted-global-infrastructure)

The disclosed architecture uses Hyperledger Besu, compatible with the Ethereum Virtual Machine. SWIFT operates workflow and commitment coordination; banks retain their environments, keys, assets, funding and settlement choices. Programmable corporate flows, FX payment-versus-payment and securities cash movements are described as capabilities the model can support, not universally available products. A separate retail payments scheme is a parallel initiative. EVM compatibility alone does not establish Ethereum-mainnet operation or ETH purchases. [SWIFT implementation](https://www.swift.com/news-events/news/swifts-blockchain-based-shared-ledger-progresses-mvp-implementation)

SWIFT's liquidity explainer describes funding confirmed before execution and shared visibility of commitments. It supplies no measured reduction in liquidity buffers or public specification of the legal funding object. [Liquidity explainer](https://www.swift.com/payments/payment-innovation/blockchain-based-ledger/enabling-bank-liquidity-management-always-world)

Its governance explainer restricts access to regulated institutions and verified entities and describes shared governance. SWIFT disclaims issuance, custody and settlement-agent/FMI roles. These are operator representations; the page is not an executed participant agreement or independent legal determination. [Trust explainer](https://www.swift.com/payments/payment-innovation/blockchain-based-ledger/future-built-trust)

## The operating evidence

| Publication | Bank-reported result | What remains bounded |
|---|---|---|
| August 19 | Standard Chartered and HSBC report their first live interbank transaction. HSBC TDS and Standard Chartered infrastructure recorded deposit obligations; SWIFT matched/netted them before external settlement. [Source](https://www.sc.com/en/press-release/standard-chartered-and-hsbc-execute-first-live-tokenised-deposit-transaction-on-swifts-blockchain-based-ledger/) | Currency, precise endpoints, value and execution date are unspecified. |
| August 26 | UOB and HSBC completed HKD cross-border transactions, using UOB's deposit infrastructure and HSBC TDS. Their obligations were matched/netted before settlement through existing systems. [Source](https://www.uobgroup.com/uobgroup/newsroom/news-releases/2026/uob-cross-border-transactions-on-swift.page) | Exact geographic corridor and transaction dates unspecified; SGD/USD expansion was planned. |
| September 2 | Citi reports completed USD transactions with FAB and OCBC and defines a July–December 2026 controlled proof-of-concept period. [Source](https://www.citigroup.com/global/news/press-release/2026/citi-services-pioneers-live-transactions-swift-ledger-fab-ocbc-redefine-always-on-global-payments) | Separate Citi Token Services volume and clearing-client totals are not SWIFT-ledger metrics. Regional “first” claims have narrower scopes than Standard Chartered's August claim. |
| September 2 | FAB confirms bilateral USD activity with Citi. Deposits stayed on bank balance sheets; SWIFT recorded commitments/liabilities without custody. FAB says separate interbank settlement completed through correspondent channels. [Source](https://www.bankfab.com/en-ae/about-fab/group/in-the-media/completes-tokenized-deposit-milestone-with-citi-swift-ledger) | “At scale” is unquantified. No account-level route, settlement timestamp or legal-finality instrument disclosed. |
| September 4 | BNP Paribas and HSBC report a completed Siemens corporate payment, EUR in France to GBP in the UK. SWIFT coordinated obligations; banks handled FX, funding and external settlement. [Official PDF](https://cashmanagement.bnpparibas.com/sites/default/files/2026-09/POC_SWIFT_HSBC_BNP%20Paribas_PRESSRELEASE.pdf) | Exact execution day, amount, FX rate and finality timestamp not disclosed. |
| September 7 | DBS reports a payment actually executed **September 5**, a Saturday, between Singapore and Citi's New York office, in USD, taking minutes. [Source](https://www.dbs.com/newsroom/DBS_and_Citi_partner_to_enable_instant_247_cross_border_USD_payments_with_tokenised_deposits) | Amount, customer, exact latency, cost and external settlement clock absent. This replaces Citi's earlier prospective DBS status. |

The six pairings above involve **eight named banks**, a count derived from these disclosures, not a census of network activity. A public announcement remains participant-reported evidence, not independent transaction-log verification.

## What changes in our understanding

1. **Readiness → executed activity:** the old blanket absence of completed transactions is stale. The August announcements predate the September 3 architecture-only check; its limited scope explains the missed development.
2. **Generic compatibility → named adapters:** Standard Chartered/HSBC and UOB/HSBC identify the bank deposit environments. Shared membership alone was weaker evidence.
3. **Possible netting → reported matching/netting in named cases:** the bank releases strengthen the implemented-function evidence. They do not disclose enforceability, multilateral netting rules or quantified savings.
4. **Unspecified external settlement → a reported correspondent settlement:** FAB identifies completion and channel class. That does not provide every transaction's finality event or loss rules.
5. **Weekend promise → a dated weekend example:** DBS supplies the clearest execution date, endpoints, currency and coarse duration in this set.

## Observatory interpretation: incumbent banks absorb the new machinery

Our Route–Anchor–Inventory thesis asks which functions move and which institutions still define the claim and carry the risk. This case now supplies operational evidence for that question.

The working interpretation is that banks are making their deposit liabilities easier to coordinate across institutions. A shared state can support payment execution while bank books, bank credit and settlement relationships continue to matter. SWIFT gains a coordinating role beyond sending independent messages. The evidence supports incumbent adaptation and a division of functions; it does not establish central-bank displacement or quantify market-share migration.

The unresolved economic question is **who funds the interval between customer availability and final interbank discharge, on what terms, and at what cost?** Upfront funding and matching may reduce uncertainty, but only actual balances, limits, collateral, settlement timing and failure rules reveal the liquidity burden. A useful stress test would follow a failed external settlement after customer funds became usable.

No reviewed transaction establishes a required XRP, LINK, ETH, stablecoin or CBDC leg. That bounded finding neither rules out future integrations nor converts another bank/network relationship into a selected SWIFT route. Network utility, operator revenue and demand to hold a native token require separate evidence.

## Remaining source gaps and return questions

- Public rulebook, pricing, participant eligibility details, operative netting/finality provisions and loss allocation were not established by this refresh. Restricted MySwift material was not accessed; the prior legal dossier was not exhaustively recertified.
- General availability, recurring customer usage, amounts, costs, measured liquidity savings and corridor-by-corridor settlement clocks require new operating disclosures.
- Citi–UOB and UOB's planned SGD expansion remain unverified here; absence of a located completion report is not proof of nonoccurrence.
- The previous BNP/HSBC/Siemens retrieval gap is resolved by its official September 4 PDF; the payment is now included above.
- SWIFT's product explainers include video objects; no video transcript was inspected. Search/open snapshots of its news index were inconsistent. This pass does not certify that no September 9 announcement exists.

Update the existing Sibos return to seek operating scale, contracts, funding and failure details rather than waiting for a first transaction already reported. This is a saved research return, not a new automation or watch-calendar change.

## Accounting companion

Saved accounting walkthrough and Crypto Hub rule overlap preserves the September 9 explanation, adds explicitly illustrative journal entries and maps the questions to the existing Hub process layers.

## All-bank and adjacent research companion

All 17 banks, testing, partnerships and linked research expands the roster audit, resolves BNP/HSBC/Siemens, and separates earlier SWIFT experiments from Canton, Chainlink, Kinexys, Partior, Agorá and other bank projects. Nine roster banks have no completed shared-ledger receipt located by this cutoff.
