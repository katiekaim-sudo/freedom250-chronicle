> Source cutoff: 2026-08-26T12:55:35-04:00

# SEC Tokenization Approval Census — What Was Actually Approved

**Question:** Which U.S. tokenization projects have actually been approved or otherwise permitted by the Securities and Exchange Commission?

**Mode:** bounded legal-state and operating-state census.

**Scope:** public SEC Commission orders, SRO rule filings, staff no-action letters, Investment Company Act orders, EDGAR effectiveness records and the SEC staff tokenized-money-market-fund census. The search covers projects that tokenize securities, security entitlements or fund-share records. It excludes ordinary crypto-asset offering relief unless the project also performs securities tokenization.

**Cutoff:** 2026-08-26 12:55:35 EDT. A bounded negative means “not located on the official surfaces reached through this cutoff,” not proof that no private or unpublished action exists.

**Mutation boundary:** workbench research only. No vault event, canonical watch, plotline or app state was changed.

## Controlling answer

“SEC-approved tokenization” is usually too broad. The current public record supports **three Commission-level tokenization-linked actions**, but only **two are core market-infrastructure approvals**:

1. **Nasdaq’s DTC-pilot tokenized-trading rule** — a true Commission approval order.
2. **Paxos Securities Settlement Company (PSSC)** — a true Commission order approving temporary clearing-agency registration, with an 18-month limit and a mandatory ramp-up before operation.
3. **WisdomTree’s WTGXX dealer-principal model** — a true Commission exemptive order that enables continuous fixed-$1 dealer transactions in qualifying government money-market-fund shares. The SEC notice expressly says the applicants did **not** seek relief for whether or how blockchain maintains shareholder records.

Everything else in the material public field falls into a different legal state: an immediately effective exchange filing, a revocable staff no-action position, an effective registration statement, a registered intermediary, or a pending application/announcement.

This is not merely semantic. Each state answers a different question:

| State | What it establishes | What it does not establish |
|---|---|---|
| Commission approval/order | The Commission made the findings required for the exact rule, registration or exemption in the order. | Approval of the sponsor, every product, every blockchain, or every future use. |
| Immediately effective SRO filing | An exchange rule became effective on filing under the cited statutory route. | An affirmative Commission approval order or an operating launch. |
| Staff no-action position | Staff will not recommend enforcement under named provisions if stated facts and conditions hold. | A Commission rule, legal conclusion, registration, exemption order or endorsement. |
| Effective registration statement | The disclosure/registration process reached effectiveness and the security may be offered under that filing. | SEC approval of the security, merits, token architecture or investment. Prospectuses state the opposite. |
| Registered broker-dealer, transfer agent or ATS | The intermediary has the specified regulatory status. | SEC approval of the platform’s tokenization project or of securities traded through it. Form ATS is a notice, not an approval application. |
| Application, notice or announcement | A project or requested relief is public. | Approval, effectiveness, launch or observed operation. |

## 1. Commission-level actions

### 1.1 Nasdaq: approved exchange rule, not yet shown live

The Commission approved Nasdaq file **SR-NASDAQ-2025-072**, Release **34-105047**, on 2026-03-18. The rule permits eligible Nasdaq participants to attach a tokenization preference to orders in DTC-eligible securities. The tokenized and traditional forms must be fungible, share the same CUSIP and symbol, confer the same rights and trade on the same order book with the same execution priority. The initial scope is Russell 1000 securities and major-index ETFs eligible under the DTC pilot.

This is a **post-trade form instruction**, not a separate token exchange. Nasdaq sends the preference to DTC after execution. If the participant, security, blockchain or wallet is ineligible, DTC settles the trade traditionally. T+1, existing surveillance and the national-market-system order book remain.

The rule becomes usable only after DTC establishes the required infrastructure, and Nasdaq must issue an Equity Trader Alert at least 30 calendar days before starting tokenized trading. No such commencement alert was located through the cutoff. The approved rule therefore is `approved / activation not established`, not `live tokenized Nasdaq trading`.

Primary source: [Nasdaq approval order, Release 34-105047](https://www.sec.gov/files/rules/sro/nasdaq/2026/34-105047.pdf).

### 1.2 Paxos Securities Settlement Company: temporarily registered, not operating

The Commission approved PSSC’s application for **temporary clearing-agency registration**, File **600-39**, Release **34-105562**, on 2026-05-27. The order grants exemptions from Exchange Act sections 17A(b)(3)(A) and (F) for no more than 18 months.

PSSC proposes a private, permissioned Paxos Ledger for bilateral delivery-versus-payment settlement. Securities held through PSSC’s DTC account and cash held through settling banks are represented as digital entitlements. PSSC is a CSD/securities-settlement system, not a central counterparty by default.

The approval is materially narrower than “Paxos may now run a full tokenized stock market”:

- PSSC represented that it would not commence operations sooner than **ten months after approval**, making 2027-03-27 the earliest represented operating date;
- the temporary registration expires no later than 2027-11-27 absent further Commission action;
- for at least the first 12 operating months, PSSC would be limited to ten participants and could not use enhanced netting;
- PSSC still had to become a DTC participant, establish settling-bank and participant arrangements, test systems, publish its rulebook and complete policies, procedures and staffing;
- the Commission expressly did not determine at that time that the application satisfied two exempted statutory requirements.

State: `Commission-approved temporary registration / mandatory ramp-up / operation not yet permitted at cutoff`.

Primary source: [PSSC temporary-registration order, Release 34-105562](https://www.sec.gov/files/rules/other/2026/34-105562.pdf).

### 1.3 WisdomTree WTGXX: approved pricing and dealer relief, not blockchain approval

The Commission issued **Investment Company Act Order IC-35968** on 2026-02-23. It permits covered SEC-registered dealers to buy and sell shares of the WisdomTree Treasury Money Market Digital Fund (**WTGXX**) and qualifying future stable-NAV government MMFs as principal at $1 per share, plus or minus disclosed dealer compensation. The model can provide continuous liquidity and rapid settlement outside ordinary mutual-fund dealing windows.

The approved object is the pricing/distribution and affiliated-dealer arrangement under sections 6(c) and 17(d) and Rule 17d-1. The underlying notice expressly says the applicants were **not seeking exemptive relief regarding whether or how blockchain technology is used to maintain the shareholder record**.

State: `Commission-granted exemptive relief for a tokenized-fund dealing model / token record architecture outside the order`.

Primary sources: [Commission order IC-35968](https://www.sec.gov/files/rules/ic/2026/ic-35968.pdf) and [notice IC-35912](https://www.sec.gov/files/rules/ic/2026/ic-35912.pdf).

## 2. Exchange rules that became effective without affirmative approval orders

After the Nasdaq approval, five NYSE-family exchanges and 24X filed substantially similar rules for immediate effectiveness. These are real operative rule states, but the SEC published **notices**, not Commission approval orders.

| Exchange | File / release | SEC date | Legal and operating state |
|---|---|---:|---|
| NYSE | [SR-NYSE-2026-17 / 34-105260](https://www.sec.gov/files/rules/sro/nyse/2026/34-105260.pdf) | 2026-04-17 | Immediately effective filing; no required 30-day launch notice located. |
| NYSE Texas | [SR-NYSETEX-2026-13 / 34-105338](https://www.sec.gov/files/rules/sro/nysetex/2026/34-105338.pdf) | 2026-04-30 | Immediately effective filing; no launch established. |
| NYSE Arca | [SR-NYSEARCA-2026-45 / 34-105347](https://www.sec.gov/files/rules/sro/nysearca/2026/34-105347.pdf) | 2026-05-01 | Immediately effective filing; no launch established. |
| NYSE National | [SR-NYSENAT-2026-09 / 34-105456](https://www.sec.gov/files/rules/sro/nysenat/2026/34-105456.pdf) | 2026-05-12 | Immediately effective filing; no launch established. |
| NYSE American | [SR-NYSEAMER-2026-36 / 34-105458](https://www.sec.gov/files/rules/sro/nyseamer/2026/34-105458.pdf) | 2026-05-12 | Immediately effective filing; no launch established. |
| 24X | [SR-24X-2026-20 / 34-105697](https://www.sec.gov/files/rules/sro/24x/2026/34-105697.pdf) | 2026-06-16 | Immediately effective filing; no launch communication located. |

All six use the same basic architecture: existing NMS trading, same rights/CUSIP/order book, a post-trade token preference, DTC-pilot eligibility, T+1 settlement and traditional fallback. They do not establish atomic cash settlement, a separate 24/7 blockchain venue or live trading.

No comparable DTC-pilot filing by Cboe, IEX, MEMX or MIAX was located through the cutoff.

## 3. Staff-permitted projects that are not Commission approvals

### 3.1 DTC / DTCC Tokenization Services

On 2025-12-11, Division of Trading and Markets staff issued a no-action position covering the DTC Preliminary Base Version under named provisions of Reg SCI, section 19(b), Rule 19b-4 and clearing-agency standards.

The service tokenizes a DTC participant’s security entitlement; it does not create a new issuer security. Eligible assets initially include Russell 1000 securities, U.S. Treasury bills/notes/bonds and major-index ETFs. DTC controls eligibility, wallet registration, supported blockchains, token protocols and reversal functions. LedgerScan is DTC’s official token-entitlement record, while the underlying securities remain registered to Cede & Co. Tokenized entitlements initially receive zero collateral and settlement value inside DTC risk calculations.

DTCC reported limited real-production transactions with more than 30 firms on 2026-07-15. That changed the operation clock, not the legal-object type. The broader participant-facing service remained scheduled for October 2026, and the SEC letter requires written launch notice to staff. The relief expires three years after that Preliminary Base Version launches and remains modifiable or revocable.

State: `staff no-action / limited production occurred / broader opening not yet established`.

Primary sources: [DTC staff no-action letter](https://www.sec.gov/files/tm/no-action/dtc-nal-121125.pdf) and [DTCC July 15 production report](https://www.dtcc.com/news/2026/july/15/dtcc-turns-tokenization-into-reality).

### 3.2 HQLAx / Clearstream International

On 2026-05-04, Trading and Markets staff said it would not recommend enforcement under section 17A(b)(1) if HQLAx and Clearstream International permit qualifying U.S. institutions to use the existing Luxembourg platform under the represented conditions.

The platform uses tokenized digital collateral records on a private permissioned ledger to transfer ownership on the books of the third-party custodian for repo, securities-lending and collateral transactions executed elsewhere. The three-year position allows up to 15 U.S. participants, imposes institutional thresholds and caps U.S.-linked activity below $25 billion average daily value and 100,000 average daily transactions. No official evidence of an onboarded U.S. participant was located.

State: `staff no-action through 2029-05-04 / U.S. operation not established`.

Primary source: [HQLAx staff no-action letter](https://www.sec.gov/files/tm/no-action/hqlax-nal-request-050426.pdf).

### 3.3 Franklin Templeton / FOBXX custody

On 2026-08-12, Division of Investment Management staff granted a facts-specific no-action position under Investment Company Act section 17(f) and parts of Rule 17f-2. It permits affiliated Franklin funds to custody shares of the Franklin OnChain U.S. Government Money Fund (**FOBXX**) through Franklin Templeton Investor Services under specified wallet, transfer-agent-control, reconciliation, board-review and audit conditions.

The response says it is not a Commission rule or statement, has no legal force and was neither approved nor disapproved by the Commission.

State: `staff custody relief / live registered fund / not Commission approval`.

Primary source: [Franklin Templeton staff no-action page](https://www.sec.gov/rules-regulations/no-action-interpretive-exemptive-letters/division-investment-management-staff-no-action-interpretive-letters/franklin-templeton-081226).

### 3.4 Paxos Settlement Service predecessor pilot

Trading and Markets staff gave Paxos a 24-month de minimis no-action window on 2019-10-28 to operate a private-ledger U.S.-equities settlement feasibility study without clearing-agency registration. It was limited to seven participants, listed U.S. equities, bilateral gross DVP, strict security/counterparty volume caps and a required wind-down.

This was the historical predecessor to PSSC, not a clearing-agency approval. The feasibility phase ended in 2021; the later PSSC order is a separate legal object.

Primary source: [Paxos 2019 staff no-action letter](https://www.sec.gov/divisions/marketreg/mr-noaction/2019/paxos-trust-company-102819-17a.pdf).

## 4. Live registered tokenized funds: eight MMFs, not eight SEC approvals

The SEC Analytics Office’s June 2026 Money Market Fund Statistics identifies six tokenized MMFs, using a record-of-ownership test tied to the staff Statement on Tokenized Securities. They held **$2.306 billion** in aggregate net assets in June. Two BlackRock on-chain share classes became effective and launched after the June census, bringing the defensible public count to eight through this cutoff.

| Fund / ticker | Public state | Approval boundary |
|---|---|---|
| M3Sixty OnChain U.S. Government MMF / MCGXX | Effective 2024; permissioned Hyperledger record with transfer-agent control. | Effective registration; no product-specific Commission order located. |
| BNY Dreyfus Treasury Securities Cash Management, Token-Enabled Shares / TKNXX | Operating since 2025; conventional official record mirrored on blockchain. | Effective class; no product-specific Commission relief located. |
| Fidelity Treasury Digital Fund, OnChain / FYOXX | Operating since 2025; transfer-agent book is official and blockchain is secondary. | Effective registration, not approval of public-chain ownership or P2P trading. |
| Franklin OnChain U.S. Government Money Fund / FOBXX | Effective since 2021; blockchain-integrated official master file; narrow 2026 staff custody relief. | Registration plus staff relief, not Commission product approval. |
| JPMorgan OnChain Liquidity-Token MMF / JLTXX | Effective 2026; transfer agent’s traditional Investor Register is determinative. | Effective registration only. |
| WisdomTree Treasury Money Market Digital Fund / WTGXX | Operating since 2023; blockchain-supported share records and permissioned transfers. | Registration plus narrow dealer/pricing order, not approval of the token architecture. |
| BlackRock Select Treasury Based Liquidity Fund, OnChain / DOLXX | Effective 2026-07-31; launched 2026-08-03. | Post-dates June census; effective registration only. |
| BlackRock Daily Reinvestment Stablecoin Reserve Vehicle, OnChain / RSVXX | Effective 2026-07-31; launched 2026-08-03; official register combines blockchain records and off-chain identity data. | Fund is not a stablecoin; effectiveness is not endorsement or reserve-asset approval. |

Primary universe source: [SEC June 2026 Money Market Fund Statistics](https://www.sec.gov/files/investment/mmf-statistics-06-2026.pdf). Current post-census filing examples: [DOLXX prospectus](https://www.sec.gov/Archives/edgar/data/97098/000119312526327215/d45978d485bpos.htm) and [RSVXX prospectus](https://www.sec.gov/Archives/edgar/data/844779/000119312526327203/d283147d485bpos.htm).

Other operating registered tokenized-security examples include Arca’s ArCoin interval fund, Figure’s YLDS face-amount certificate and the wider WisdomTree Digital Trust fund family. Their registration/effectiveness should be stated as such. Separate Commission orders for Arca’s monthly repurchase frequency and Figure Certificate Company’s custody arrangements did not approve their blockchain architectures.

## 5. Pending, announced and false-positive “approvals”

| Item | Correct state at cutoff |
|---|---|
| ARK Venture Fund Tokenized Class | **Pending application.** Notice IC-36308 was issued 2026-08-24; hearing requests are due 2026-09-18 at 5:30 p.m. ET. No order or launch. [SEC notice](https://www.sec.gov/files/rules/ic/2026/ic-36308.pdf) |
| Superstate USTB conversion to registered MMF | **Pending/un-effective.** Existing USTB remains a private offering; no effectiveness record for the proposed MMF conversion was located. [Superstate SEC submission](https://www.sec.gov/file/ctf-superstate-letter-061725) |
| NYSE standalone 24/7 tokenized platform | **Announced and subject to regulatory approvals.** It is separate from the immediately effective DTC-pilot rule filings. [ICE/NYSE announcement](https://ir.theice.com/press/news-details/2026/The-New-York-Stock-Exchange-Develops-Tokenized-Securities-Platform/default.aspx) |
| BSTX | The 2022 Commission orders approved an NMS equity venue with conventional NSCC/DTC settlement and a blockchain market-data feed. The order expressly did **not** approve digital-token trading. [BSTX order](https://www.sec.gov/files/rules/sro/box/2022/34-94092.pdf) |
| Project Ion | Parallel DLT settlement infrastructure at DTC; no distinct project-specific SEC approval or no-action object was located. |
| tZERO, Securitize Markets, INX Securities, Figure ATS/Liquidity.io, Prometheum | Broker-dealer, transfer-agent, ATS or special-purpose-broker-dealer status is not Commission approval of a tokenization platform or its securities. [SEC ATS explanation](https://www.sec.gov/foia/frequently-requested-documents/alternative-trading-system-ats-list) |
| BlackRock BUIDL, Circle USYC, Ondo OUSG and private tokenized funds | Private/exempt offerings are not SEC-approved products. Form D, Rule 506(c), Investment Company Act exclusions and registered intermediaries are separate legal objects. |
| Northern Trust NDEXX | Effective “Digital Enabled Shares,” but the fund says it does not itself employ blockchain; intermediaries maintain a mirror record. SEC staff therefore excludes it from the tokenized-MMF census. |

## 6. Plotline fit

This census sharpens three existing Freedom 250 conclusions.

### A. The SEC is opening tokenization through adapters, not by creating a parallel securities universe

Nasdaq, the NYSE family and 24X preserve the existing order book, CUSIP, shareholder rights, surveillance and T+1 cycle. The novelty enters as a post-trade form instruction to DTC. The public-policy direction is `same security / same market / optional token entitlement`, not an unregulated duplicate stock.

### B. Tokenization initially strengthens record owners and administrators

DTC retains eligibility, official-record and correction power. Transfer agents remain determinative in several funds. Wallet whitelisting, freeze/correction controls, permitted networks and off-chain identity registers recur across the field. Public or permissioned chains expand mobility and programmability while regulated entities preserve the legal constitution.

### C. Permission and production are different clocks

- DTC has staff relief and a July limited-production event, but the broader October service remains a separate gate.
- Nasdaq has an approval order, but no commencement alert was found.
- Six other exchange rules are effective, but no launch notices were found.
- PSSC is registered, but cannot begin before March 2027 under its representation.
- HQLAx has U.S.-participant relief, but no U.S. onboarding proof was found.
- Eight registered tokenized MMFs can be live without being “SEC-approved tokenization projects.”

The larger storyline is therefore not “the SEC approved blockchain markets.” It is: **the SEC and its staff are admitting tightly bounded token forms into existing securities, fund and clearing constitutions one legal function at a time.**

## 7. Coverage receipt and open return gates

Checked through the stated cutoff:

- SEC Crypto@SEC action index;
- national-securities-exchange SRO dockets and orders;
- Trading and Markets and Investment Management no-action indexes;
- Exchange Act clearing-agency orders;
- Investment Company Act notices and orders;
- EDGAR effectiveness/prospectus records for the identified public fund set;
- SEC Money Market Fund Statistics and staff classification;
- existing Freedom 250 DTC, clearing-transition and private-rail packages.

The next promotion-worthy objects are:

1. Nasdaq, NYSE-family or 24X publishes the required 30-day tokenized-trading launch notice;
2. DTC gives staff its Preliminary Base Version launch notice and publishes participant terms, fees, approved networks and operating evidence;
3. PSSC files completed ramp-up materials, begins operation or receives permanent/extended registration;
4. HQLAx identifies a qualifying U.S. participant or reports U.S.-linked activity;
5. the Commission grants, denies or modifies the ARK tokenized-class application;
6. a future SEC MMF census incorporates DOLXX/RSVXX or changes the staff classification methodology;
7. a Commission order approves a genuinely native or non-fungible tokenized-security architecture rather than a same-security entitlement adapter.

### Return-governance reconciliation — 2026-08-27

| Gate | Disposition | Existing object, if any |
|---|---|---|
| 1. First Nasdaq, NYSE-family or 24X launch notice | `ledger` | — |
| 2. DTC broader-service launch and operating terms | `existing_canonical_watch` | `w-2026-10-01-dtc-tokenization-opening`; Return Ledger row `ret-dtc-tokenization-broader-opening-2026-10-01` |
| 3. PSSC ramp-up, operation or registration disposition | `package_context_only` | — |
| 4. HQLAx U.S.-participant or activity evidence | `package_context_only` | — |
| 5. ARK tokenized-class disposition | `ledger` | — |
| 6. Future SEC tokenized-MMF census | `package_context_only` | — |
| 7. Native/non-fungible architecture approval | `package_context_only` | — |

The labels reconcile return routing only; they do not assert that any gate has
occurred or advance this document's 2026-08-26 evidence cutoff.

**Disposition:** `plotline_support_only` plus `promotion_review` for the legal-state correction. The result consolidates and corrects the approval vocabulary; it does not by itself require a new canonical event because the principal underlying actions already have separate factual clocks.
