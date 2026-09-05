> Source created: 2026-07-12

> **The entity census + the five-layer rule (parent / licensed person / network / asset / customer). The field schema for future additions.**
> *Verbatim as delivered. Audit + provenance: [Private Monetary Stack — Source Documents](../sources/private-monetary-stack-source-documents-0ecbb7f450f9.html).*

# Fintech and crypto company registry

**Status:** working company census for the Freedom 250 monetary-infrastructure track  
**As of:** 2026-07-11  
**Purpose:** map the private firms trying to issue, route, record, custody, settle, tokenize, or govern the new monetary pipes

---

## Governing rule

This registry does not treat a token ticker, protocol, foundation, software company, licensed financial institution, and customer-facing brand as the same entity.

For every company family, keep five layers separate:

1. **parent and capital layer** — the company, foundation, consortium, shareholders, and material investors;
2. **licensed legal person** — the bank, trust company, broker-dealer, transfer agent, exchange, custodian, money transmitter, or stablecoin issuer that may lawfully act;
3. **network and software layer** — the ledger, protocol, messaging adapter, smart-contract system, validator set, or orchestration software;
4. **asset and liability layer** — the token, stablecoin, tokenized deposit, fund share, security entitlement, reserve asset, or settlement claim;
5. **customer and contract layer** — the branded interface, user agreement, custody terms, redemption promise, freeze/burn power, and bankruptcy treatment.

The same branded product may cross several legal persons. The same company may occupy several functions. Record the role for each dated action rather than assigning one permanent label to the group.

## ISO 20022 rule

Do not call XRP, XLM, HBAR, ALGO, XDC, IOTA, QNT, or any other cryptocurrency an “ISO 20022-compliant coin.” The ISO 20022 Registration Authority says cryptocurrencies are not inherently ISO 20022 compliant, are not managed or registered by ISO 20022, and that there is no official ISO 20022 certification authority. A blockchain company, exchange, payment processor, gateway, or software product can implement ISO 20022 messages or connect its system to an ISO 20022-using community. That is an interoperability fact about the implementation—not a certification of the native token. [ISO 20022 FAQ](https://www.iso20022.org/frequently-asked-questions)

Use one of these factual labels instead:

- **registered ISO 20022 message or repository role**;
- **documented ISO 20022 messaging support**;
- **documented integration with an ISO 20022 rail or institution**;
- **company claim not independently confirmed**;
- **community label only / unsupported as an ISO status**.

## Functional groups

### A. Public and interoperability networks — core portraits

| Company / ecosystem | Entity distinction to preserve | Main functions to test | Initial priority |
|---|---|---|---|
| Ripple / XRP Ledger | Ripple companies; Ripple National Trust Bank; Standard Custody; XRPL governance/validators; XRP; RLUSD | cross-border payments, stablecoin issuance, custody, prime brokerage, treasury, public-chain asset layer | Tier 1 |
| Stellar Development Foundation / Stellar | nonprofit foundation; network validators; XLM; third-party anchors and issuers | payments, remittances, token issuance, public-chain asset layer, DTC connection | Tier 1 |
| Hedera / Hashgraph | Hedera Council; Hedera Foundation; Hashgraph company/software; HBAR; issuers such as Wyoming FRNT | governed public network, token service, identity, state stable token | Tier 1 |
| Algorand ecosystem | Algorand Foundation; Algorand Technologies; validator/consensus layer; ALGO | public-chain payments and tokenization | Tier 2 |
| XDC Network | foundation/company/operator roles; validators; XDC | trade finance, tokenization, messaging adapters | Tier 2 |
| IOTA ecosystem | IOTA Foundation; network/governance; IOTA token | public infrastructure, identity, trade/logistics, tokenization | Tier 2 |
| Quant / Overledger | Quant Network company; Overledger software; QNT utility role | enterprise interoperability and gateway/orchestration | Tier 2 |

### B. Institutional ledgers and wholesale-market infrastructure — core portraits

| Company / system | Entity distinction to preserve | Main functions to test | Initial priority |
|---|---|---|---|
| Digital Asset / Canton Network | Digital Asset company; Canton Foundation; Global Synchronizer operators; Canton Coin; application providers | privacy-preserving institutional ledger, synchronized markets, collateral and securities | Tier 1 |
| R3 / Corda | R3 company/owners; Corda software; operator-specific networks | enterprise DLT, regulated asset and payment workflows | Tier 2 |
| Chainlink | Chainlink Labs; foundation/ecosystem; oracle operators; LINK | data, proof of reserve, cross-chain messaging, workflow/orchestration | Tier 1 |
| Fnality International | company; shareholder banks; national payment systems; settlement asset and central-bank account arrangements | tokenized wholesale cash and DvP/PvP settlement | Tier 1 |
| Partior | company; bank shareholders; network participants; settlement claims | multi-bank wholesale clearing and settlement | Tier 2 |
| Broadridge DLR | Broadridge parent; DLR platform; participating banks and settlement agents | repo workflow, tokenized collateral, intraday liquidity | Tier 1 |
| J.P. Morgan Kinexys | JPMorgan Chase entities; Kinexys brand/platform; JPM Coin or deposit-token liabilities | bank-led payments, deposit tokens, programmable wholesale settlement | Tier 1 |

### C. Market access, custody, issuance, and tokenization — core portraits

| Company / group | Entity distinction to preserve | Main functions to test | Initial priority |
|---|---|---|---|
| Coinbase | public parent; exchange/broker entities; Coinbase Custody; proposed national trust; Base; USDC economics | exchange, custody, distribution, chain, payments, institutional access | Tier 1 |
| Kraken | Payward parent/exchange; Kraken Financial SPDI; proposed national trust; limited Fed account; Ink/xStocks roles | exchange, banking gate, custody, tokenized assets | Tier 1 |
| Circle | public parent; stablecoin issuers; First National Digital Currency Bank/Circle National Trust; USDC/EURC; Arc | stablecoin issuance, reserve management, custody, payment network | Tier 1 |
| Paxos | parent; trust-bank entities; stablecoin issuers; partner-branded coins; custody/brokerage | regulated issuance, tokenization, custody, settlement | Tier 1 |
| Securitize | parent; broker-dealer, transfer agent, ATS, fund administration entities | tokenized securities issuance, transfer agency, distribution, lifecycle control | Tier 1 |
| Ondo | corporate/foundation/protocol layers; product issuers and custodians; tokenized-security platform | tokenized Treasuries/stocks, distribution, cross-chain liquidity | Tier 1 |
| Fireblocks | software company; wallet/custody control stack; network participants | wallet policy, key orchestration, settlement connectivity | Tier 2 |
| Anchorage Digital | parent; Anchorage Digital Bank N.A.; custody and institutional platform entities | federally chartered custody, staking, settlement and bank access | Tier 1 |
| BitGo | parent; state trust; national-bank conversion; custody and settlement entities | qualified custody, stablecoin support, prime services | Tier 1 |
| Zero Hash | parent and regulated subsidiaries; proposed national trust; partner-facing embedded rails | embedded crypto/stablecoin infrastructure, settlement and custody | Tier 2 |
| Stripe / Bridge | Stripe parent; Bridge entities; proposed Bridge National Trust Bank; Tempo links | merchant payments, stablecoin orchestration, issuance infrastructure | Tier 1 |

### D. Incumbent orchestrators and the expansion ring

These bodies are required comparison points even when they are not crypto-native. They can absorb the new asset and keep the old gate.

| Entity / company | Why it belongs | Status anchor |
|---|---|---|
| Swift | ISO 20022 Registration Authority, global messaging, tokenized-asset orchestration, blockchain shared ledger | Its ledger moved from design to initial-use readiness in July 2026; 17 banks were preparing live pilots. [Swift, 2026-07-09](https://www.swift.com/news-events/press-releases/swifts-blockchain-ledger-ready-use-17-banks-set-pioneer-tokenised-cross-border-payments-trusted-global-infrastructure) |
| Visa | card-network settlement, stablecoin settlement, multi-chain reach | Visa said its stablecoin settlement pilot supported nine chains and reached a $7 billion annualized run rate in April 2026. [Visa, 2026-04-29](https://investor.visa.com/news/news-details/2026/Visa-Accelerates-Stablecoin-Momentum-Adding-Five-Blockchains-for-Settlement/default.aspx) |
| Mastercard | card-network settlement, Multi-Token Network, stablecoins and tokenized deposits | Mastercard announced regulated-stablecoin settlement across multiple chains and a planned acquisition of BVNK in 2026. [Mastercard settlement](https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-expands-settlement-capabilities-to-include-stablecoin.html); [BVNK acquisition](https://www.mastercard.com/global/en/news-and-trends/press/2026/march/Mastercard-to-acquire-BVNK-to-connect-on-chain-payments-and-fiat-rails.html) |
| Fiserv / FIUSD | core-bank and merchant distribution, configurable stablecoin infrastructure | Fiserv markets FIUSD as a bank- and merchant-facing stablecoin layer integrated into existing systems. [Fiserv FIUSD](https://www.fiserv.com/en/solutions/embedded-finance/fiusd-stablecoin.html) |
| PayPal / PYUSD | consumer wallet and merchant distribution; Paxos-issued liability | PYUSD runs through PayPal/Venmo distribution while Paxos remains the issuer; the network/product and legal issuer must stay separate. [PayPal PYUSD developer center](https://developer.paypal.com/dev-center/pyusd/) |
| SoFi / Galileo / SoFiUSD | insured national bank issuer plus fintech distribution platform | Mastercard described SoFiUSD as issued by SoFi Bank, N.A., with planned card-settlement and Galileo distribution uses. [Mastercard and SoFi](https://www.mastercard.com/sea/en/news-and-trends/press/2026/march/sofi-and-mastercard-partner-to-enable-sofiusd-settlement-across-.html) |
| DTCC / DTC | authoritative securities record, tokenization eligibility, collateral and clearing interface | Reference utility; covered in the Clearing-House Transition records. |
| The Clearing House | bank-owned payment and tokenized-deposit coordination layer | Reference utility; compare with Swift, Fnality, Kinexys, and public stablecoin rails. |

### E. Charter and surveillance ring

The company census must not stop at the best-known names. The OCC's public digital-asset application list showed a much wider 2026 queue, including World Liberty Trust Company, PAYO Digital Bank, zerohash national trust bank, Revolut Bank US, EDX Trust, Bastion Platforms National Trust Company, Lorum National Trust Bank, OpenReserve Bank, Agora National Trust Bank, Catena Trust Bank, Payward National Trust Company, and CBW Bank. [OCC digital-asset licensing applications](https://www.occ.gov/topics/charters-and-licensing/digital-assets-licensing-applications/index-digital-assets-licensing-applications.html)

The broader approval record also includes or references Ripple National Trust Bank, First National Digital Currency Bank, Paxos Trust Company N.A., BitGo Bank & Trust N.A., Fidelity Digital Assets N.A., Coinbase National Trust Company, National Digital Trust Company, Foris DAX National Trust Bank, Laser Digital National Trust Bank, Morgan Stanley Digital Trust N.A., and Connectia Trust N.A. [OCC interpretations and decisions](https://www.occ.gov/topics/charters-and-licensing/interpretations-and-decisions/index-interpretations-and-decisions.html)

These entities form a surveillance ring because a charter application is not the same as an operating bank, a conditional approval is not final approval, and a trust charter is not deposit insurance or automatic Federal Reserve account access.

## Required fields for each full portrait

- company family and brands;
- legal parent and material subsidiaries;
- nonprofit foundation, consortium, or governance council;
- licensed entity and regulator;
- charter/application/approval/consummation status;
- deposit insurance and central-bank-account status;
- native token, stablecoin, tokenized deposit, or settlement asset;
- reserve owner and reserve custodian;
- software/network and validator/operator control;
- issuance, mint, burn, freeze, pause, correction, and recovery powers;
- customer-property and bankruptcy posture;
- products and monetary function;
- production, limited production, pilot, test, announced, or proposed status;
- named banks, central banks, clearinghouses, depositories, card networks, asset managers, and government partners;
- acquisitions, investments, and key counterparties;
- dated action timeline;
- public/private seam;
- single points of failure and shared dependencies;
- source facts, company claims, inference, and speculation;
- confirmation markers, weakening markers, and open watches.

## Two clocks

Each company should carry two clocks, adapted from the Judicial Money Map:

1. **company build clock** — incorporation/founding → product → partnership → pilot → production → acquisition or integration;
2. **legal operating clock** — application → conditional approval → final approval/consummation → account access → rule effective date → litigation or supervisory constraint.

A press release can move the first clock while leaving the second untouched. A charter can move the legal clock while the advertised product remains unlaunched. Keep both.

## Status vocabulary

- **LIVE — PRODUCTION:** real customer or institutional transactions are occurring.
- **LIVE — LIMITED:** production exists but only for named participants, assets, chains, or windows.
- **PILOT / TEST:** controlled transactions; do not call this adoption.
- **ANNOUNCED:** a dated plan or target without a live service.
- **PROPOSED / APPLIED:** an application or design request, not an approval.
- **CONDITIONAL APPROVAL:** legal permission subject to conditions; not consummation.
- **FINAL / CONSUMMATED:** the legal entity or authority is operative.
- **COMPANY CLAIM:** not independently confirmed by a regulator or counterparty.
- **COMMUNITY CLAIM:** unsupported marketing or social-media label.
