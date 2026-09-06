> Source evidence cutoff: 2026-09-17T11:32:00-04:00

# CFTC Passive Software No-Action Position — Full Reading and CFTC-Only Technology Impact

## Question

What did CFTC Market Participants Division Letter 26-25 actually change for
providers of “passive software,” what remains outside the position, and how
does the change affect Freedom 250's existing CFTC, crypto, prediction-market,
perpetual, agentic-finance and private-rail plotlines?

## Controlling answer

CFTC Letter 26-25 is a material **distribution-layer opening inside the
existing registered derivatives constitution**. It takes the March 17 Phantom
position—which only Phantom could rely on—and makes substantially the same
Market Participants Division no-action position broadly available to
qualifying passive software providers (`PSPs`). The class is expressly **not
limited to crypto software**.

The opening is commercially larger than the phrase “passive software” sounds.
A qualifying PSP may:

- display market, position and product information;
- let a user submit orders for CFTC-regulated derivatives directly to a
  registered venue or intermediary;
- receive a share of a registrant's relevant revenue;
- charge the user a transaction-based fee;
- market its service and the availability of particular derivatives,
  including event contracts and perpetuals;
- introduce and solicit users to engage with specific registered entities; and
- provide the interface as a standalone product or an embedded feature of
  wallet software.

“Passive” therefore describes the PSP's relationship to **the particular
order, customer assets and execution decision**, not an absence of commercial
promotion, referral or transaction-linked revenue.

The constitutional boundary is equally important. The user must trade on a
designated contract market (`DCM`), directly as a member or through a
registered futures commission merchant (`FCM`) or introducing broker (`IB`).
Position-supporting funds or property remain in custody with the DCM's
derivatives clearing organization (`DCO`) and/or an FCM. The PSP may not hold
or control user assets, generate express buy/sell signals, exercise discretion
over order routing or execution, or become affirmatively involved in a
particular order.

This is not a general DeFi safe harbor, a spot-market regime, an artificial-
intelligence trading-agent permission, a Commission rule, or a Commission
exemption. It is an interim staff enforcement position concerning only the IB
and associated-person registration requirements, available while its exact
facts and ten conditions are satisfied and until Commission rulemaking or
guidance becomes effective.

## Exact legal state and clocks

| Object | State on September 17, 2026 | What it does | What it does not do |
|---|---|---|---|
| CFTC Release 9300-26 | Agency announcement | Announces that Letter 26-25 is broadly available to passive software providers | Does not supply the controlling conditions by itself |
| MPD Letter 26-25 | Staff no-action position | MPD will not recommend an enforcement action for failure to register as an IB or AP solely because a qualifying PSP engages in the covered activities | Does not bind the Commission or another office/division; does not amend the CEA or regulations |
| MPD Letter 26-09 | Phantom-specific predecessor | Supplied the same basic position to Phantom for an embedded self-custodial-wallet interface | Only Phantom could rely on it; it was not a general class position |
| Future Commission rulemaking or guidance | Not yet effective in the reached sources | Would terminate the letter's interim clock when effective | No calendar expiration or final durable regime is created by Letter 26-25 |
| Reliance/operation | Provider-specific future state | A PSP must file the required notice and PSP–registrant undertakings and satisfy all conditions | Publication of the letter does not prove that any new PSP has relied, connected, launched or transmitted an order |

The letter was issued by MPD to “Ladies and Gentlemen,” lists the requester as
the CFTC on the staff-letter index, and states that a position for **all PSPs**
on substantially the Phantom terms is warranted. The practical result is a
class-like pathway, but its legal form remains division-level no-action
forbearance under Commission Regulation 140.99—not a Commission vote or a
Section 4(c) exemptive order.

## From old TSV doctrine to the new pathway

The older technology-service-vendor (`TSV`) letters treated a vendor as safely
outside IB registration only on restrictive facts. Among other things, the
customer generally already had an independent FCM/IB relationship; the vendor
did not recommend a particular intermediary; it did not solicit orders; its
fees were not connected to execution fees; and it had no DCM trading
membership.

Letter 26-09 stepped beyond those restrictions for Phantom. Letter 26-25 now
generalizes that step. The significant deltas are:

| Earlier TSV posture | Letter 26-25 pathway |
|---|---|
| Pre-existing customer/intermediary relationship expected | PSP may introduce and solicit a user to a specific registrant; the registrant onboards the user |
| No recommendation or encouragement toward a particular FCM/IB | PSP may market its registrant relationships and promote particular derivatives contracts |
| Execution-linked compensation disfavored | Registrant revenue share and direct user transaction fees are expressly within covered activities |
| Vendor mainly transmits information/order-entry communications | PSP may provide an integrated market-data, position, product and order-submission front end |
| Separate, entity-specific interpretive letters | Broadly available interim no-action pathway after notice and undertakings |

The old legal concern has not disappeared. The CEA and Regulation 1.3 define
an IB around soliciting or accepting orders for compensation or profit, and
the Commission has long read “soliciting or accepting” broadly enough to reach
customer referrals and per-trade compensation. That is why Letter 26-25 is
no-action relief rather than a simple declaration that every covered PSP is
outside the IB definition.

## The ten conditions

1. The PSP, its principals and soliciting personnel must avoid statutory
   disqualification unless MPD grants a waiver, and later disqualification
   must be reported.
2. The PSP must disclose its registrant relationships and potential conflicts,
   including fees, and obtain user acknowledgement.
3. The PSP must give relevant Regulation 1.55(b) risk disclosure and retain
   acknowledgement unless the registered counterparty already has the duty.
4. The DCM, FCM or IB—not the PSP—must onboard the user as a member or customer,
   and the user must remain able to reach that registrant independently.
5. The PSP must adopt and enforce public-communications and marketing policies
   as if it were a registered IB.
6. The PSP may not use advertising or promotions that would require NFA
   pre-approval if it were an IB.
7. The PSP and every registrant partner must execute and file an undertaking
   making them jointly and severally liable for CEA/regulatory violations by
   the PSP or its personnel in covered activity, and both consent to CFTC
   investigation and enforcement jurisdiction.
8. The PSP must maintain compliance and CFTC-business records consistently
   with Regulation 1.31.
9. The PSP must notify MPD of insolvency or bankruptcy.
10. The PSP must file a notice agreeing to all conditions and consenting to
    CFTC jurisdiction; a governmental or tribal PSP must supply any sovereign-
    immunity waiver needed to make that consent enforceable.

This is not “no regulation.” It is **registration relief paired with a
contractual supervision membrane**. The registered DCM/FCM/IB becomes the
onboarding and custody anchor, and the PSP–registrant undertaking becomes the
liability bridge.

## What changed

### 1. A one-company letter became a reusable market-access route

Letter 26-09 was a concrete Phantom pathway. Letter 26-25 removes the need for
each similarly situated provider to obtain its own bespoke letter, provided it
files the prescribed notices and undertakings and remains within the covered
facts. That lowers time, legal-cost and uncertainty barriers to embedding
regulated derivatives in wallets, finance apps and other front ends.

### 2. Distribution can move outward while regulation remains anchored inward

The customer-facing surface may now sit in a software company that is not an
IB. The trade, customer relationship, custody and clearing chain still routes
through DCM/FCM/IB/DCO infrastructure. This is the project’s “authority through
the adapter” pattern in unusually clean form: the interface decentralizes;
the legally authoritative account, asset custody, execution venue, clearing
and enforcement anchors do not.

### 3. “Passive” now accommodates active marketing economics

The PSP may solicit users, promote named contracts and earn transaction-linked
fees. The functional boundary is not whether the PSP influences market demand;
it is whether the PSP becomes involved in the particular order, gives an
express trading signal, controls routing/execution, or holds customer assets.

### 4. CFTC staff is using existing authority after CLARITY stalled

On September 15, Senate cloture on the motion to proceed to H.R. 3633 failed
49–50. On September 17, CFTC staff issued Letter 26-25. The sequence does not
prove that the Senate result caused the letter, but it matches Chairman Selig's
August statement that CFTC staff would use existing authority if CLARITY
stalled.

This is an observable CFTC branch change: congressional spot-market legislation
is stalled while the agency expands the distribution perimeter of its existing
registered derivatives system through staff relief. It does not create the
missing ordinary spot-market constitution.

## What did not change

- **No ordinary spot-crypto constitution.** Letter 26-25 covers
  Commission-regulated derivatives accessed through registered derivatives
  entities. It does not create CFTC registration or conduct rules for ordinary
  unleveraged spot platforms.
- **No permission for free-standing DeFi protocols.** A user-facing wallet may
  be self-custodial for its ordinary crypto functions, but covered derivatives
  positions use the custodial DCM/DCO/FCM structure described in the letter.
- **No autonomous-agent permission.** Express buy/sell signals and discretion
  over routing or execution are outside the covered facts. Software that
  recommends, decides, routes or executes as an agent needs separate analysis.
- **No customer-property rewrite.** Funds/property supporting the position
  remain at a DCO and/or FCM under the existing derivatives constitution.
- **No product approval.** Event contracts, perpetuals and other derivatives
  are examples of accessible product types, not newly approved products.
- **No state-law/preemption settlement.** The letter is not a CEA Section 4(c)
  Commission exemption and does not itself decide the live state gaming and
  prediction-market disputes.
- **No durable Commission law.** MPD can condition, modify, suspend, terminate
  or restrict the position; the Commission and other divisions are not bound.
- **No operating evidence yet.** The reached official record identifies no new
  PSP notice, registrant undertaking, user, order, volume, incident or
  examination under Letter 26-25.

## Freedom 250 plotline effect

### The CFTC regulatory turn — direct continuation, high materiality

The August IAC record left “developer protection based on function” as a future
gate. Letter 26-25 partially closes it for the **interface/distribution
function**, but not for protocols generally. This belongs in the regulatory-
turn thread as a real administrative state change: individualized relief became
a broadly available staff pathway.

### The institutional flip — stronger

Regulated derivatives can be distributed through consumer software, including
an embedded wallet interface, while the venue, account, custody and clearing
stack remains institutional. That makes regulated derivatives more portable
without making the institutional substrate disappear.

### Prediction markets — materially stronger distribution, unresolved sovereignty

Event contracts are expressly named covered products. A PSP may market
particular contracts and introduce users to specific DCMs/FCMs/IBs, subject to
the conditions. This can multiply prediction-market storefronts without each
storefront registering as an IB. It does not decide whether state gaming law
can reach a provider, contract or access surface; the separate federal-
preemption litigation and any future Section 4(c)/Parts 38–40 action remain
controlling.

### Perpetuals and 24/7 markets — the access seam opens, the funding seam does not

Perpetual contracts are expressly named. The software distribution channel can
scale, but the letter does not make collateral, DCO operations, bank money,
margin funding or settlement continuously available. It solves storefront
access, not the weekend cash-and-risk constitution.

### Agentic finance — a newly visible boundary, not an authorization

The letter draws a useful line for the IAC's agentic-finance plot. A user-
controlled interface that passively transmits an order may fit. Software that
generates an express signal or exercises routing/execution discretion does not
fit the represented facts. The missing constitution remains: principal and
agent identity, delegated authority, wallet/key control, limits, telemetry,
loss allocation, revocation and remedy.

### Onchain developer protection — partial and incumbent-anchored

Chairman Selig directed staff in August to develop lawful paths for onchain
finance protocols. Letter 26-25 supplies one path for front-end software into
registered derivatives markets. It does not protect protocol developers,
smart-contract deployers, governance participants or noncustodial peer-to-peer
derivatives on the same terms. The developer-protection gate should therefore
be marked **partially reached**, not closed.

### Authority through the adapter — strengthened

The relief is a compact example of constitutional refactoring. Distribution
and user experience can move to an outside software layer, while the legal
claim, customer account, custody, order destination, clearing, records,
marketing standards and enforcement remain anchored in named regulated actors.
The provider is not simply “outside”: it enters through filed consents,
recordkeeping duties and joint liability with each registrant partner.

## CFTC-only technology overlap map

This map isolates Letter 26-25. It does not carry any permission, architecture
or inference from the SEC's separate September 17 action. The CFTC position
opens a conditional **software distribution interface** into the existing
registered derivatives system; it does not open a new securities, spot-crypto,
blockchain, custody or settlement regime.

```text
user or supervised agent
  -> wallet / app / passive software interface                 [CFTC 26-25]
     -> DCM / FCM / IB account, execution and customer chain
        -> DCO / FCM collateral, custody and clearing
```

| Tracked technology | What Letter 26-25 changes | What Letter 26-25 does not change |
|---|---|---|
| Wallets and consumer finance apps | **Direct opening.** A standalone or embedded wallet interface may display market, product and position information; market particular derivatives; solicit users; transmit their orders to registered entities; and earn revenue-share or transaction fees. | The wallet may not custody or control derivatives collateral, give express buy/sell signals, control routing/execution or become affirmatively involved in the particular order. |
| Market-data dashboards and order-entry software | **Direct opening.** A software surface may combine information display with order submission and compensated referrals without MPD recommending IB/AP enforcement solely for the covered activity. | Data integrity, antifraud, marketing, records and the underlying registrant's duties remain. A recommendation or execution decision is outside the represented passive function. |
| Prediction-market interfaces | **Direct opening.** Event contracts are expressly named, so a lawfully available DCM product may be exposed through multiple outside software storefronts. | The letter does not approve any event contract or decide state gaming-law and federal-preemption disputes. |
| Perpetual and 24/7 market interfaces | **Direct opening at distribution.** Perpetuals are expressly named and transaction-linked software compensation is permitted. | No continuous bank cash, collateral movement, margin funding, DCO operation or settlement is created. |
| Agentic software and smart wallets | **Boundary clarification, not authorization.** A user-controlled tool that transmits an order already decided by the user may fit. | Recommendation, express signals, route selection, execution discretion, key control and autonomous loss allocation remain outside the position. |
| DeFi protocols, smart contracts and decentralized governance | **No general opening.** A front end may qualify only when its activity routes the user into the registered DCM/FCM/IB/DCO chain and satisfies the letter. | The position does not protect protocol developers, smart-contract deployers, validators, governance participants or peer-to-peer derivatives as classes. |
| Ripple, XRPL, RLUSD and XRP | **No technology or token selection.** A Ripple-related wallet or software product could matter only if the exact provider qualifies as a PSP and connects to named registered derivatives entities under the letter. | The letter does not approve XRPL execution, RLUSD settlement, XRP pairing, XRP collateral or Ripple-company market infrastructure. |
| Stablecoins, tokenized deposits and payment rails | **No new permission.** Their only possible relevance is through separately lawful funding, collateral or payment arrangements outside the PSP relief. | Letter 26-25 does not authorize issuance, reserve custody, redemption, deposit tokenization, Fed access, bank settlement or use of a digital asset as CFTC customer collateral. |
| Chainlink, Wormhole, or other oracle and interoperability middleware | **No category-wide relief.** A provider could be relevant only to the extent its exact software activity stays within passive display or transmission and all conditions are met. | Oracle publication, cross-chain messaging, protocol execution and discretionary routing are not independently authorized by the letter. |
| Custody, prime brokerage, FCMs, DCOs and DCMs | **They remain the required anchors.** Wider front-end distribution can send more users toward the registered account, execution, custody and clearing chain. | The letter grants no new registration, custody, clearing, collateral or product authority to those institutions; their existing rules continue to control. |
| Public blockchains, AMMs and tokenized securities | **No direct change.** Letter 26-25 is technologically neutral and expressly reaches non-crypto software as well as crypto-related interfaces. | It does not authorize an AMM, securities venue, blockchain settlement system, tokenized security or transfer-agent arrangement. |
| x402 and machine-native payment orchestration | **No direct change.** The architectural similarity is that software can hide a regulated rail behind a simple request. | Payment authorization is not a derivatives order, and the letter does not authorize autonomous purchasing, payment settlement or delegated trading authority. |

The CFTC-only change is therefore narrower and cleaner: **regulated derivatives
may be distributed through many more software surfaces without every qualifying
surface registering as an IB, while the account, order destination, collateral,
custody, clearing, supervision and remedies remain anchored in registered
derivatives institutions**. It is a front-end distribution change, not a new
blockchain, token, spot-market or settlement constitution.

## Claim audit

| Claim | Ruling |
|---|---|
| CFTC exempted software developers from regulation | **Reject.** MPD conditionally declines to recommend enforcement for IB/AP registration only; other CEA, CFTC, NFA, marketing, records and antifraud obligations remain. |
| The letter is only about Phantom or crypto wallets | **Reject.** It generalizes the Phantom pathway to PSPs and expressly says the class is not limited to crypto software. |
| “Passive” means the provider cannot market or earn transaction fees | **Reject.** Covered activities include contract promotion, user solicitation, registrant revenue share and direct transaction fees. |
| The letter legalizes DeFi derivatives | **Reject.** Covered activity routes to registered DCM/FCM/IB/DCO infrastructure and excludes custody, signals and execution discretion. |
| Wallets can now hold CFTC customer collateral under this letter | **Reject.** The represented model keeps position-supporting funds/property at the DCO and/or FCM. |
| This settles state prediction-market lawsuits | **Reject.** The letter is not a Commission Section 4(c) order and does not adjudicate state-law or preemption disputes. |
| This helps regulated event-contract and perpetual distribution | **Carry.** Both are named covered product examples, but each underlying product and venue must already be lawfully available. |
| This authorizes autonomous AI trading agents | **Reject.** Express signals and routing/execution discretion are outside the letter's facts. |
| Letter 26-25 shows the CFTC using existing authority after CLARITY stalled | **Carry as an observable CFTC sequence; label motive as inference.** The Senate failure and later CFTC letter are verified and the move matches Chairman Selig's stated fallback plan, but Letter 26-25 does not itself cite the Senate vote. |

## Highest-value next receipts

1. First PSP notice relying on Letter 26-25 and the provider's exact software
   function.
2. First filed PSP–registrant joint-liability undertaking.
3. First named embedded wallet/app launch and exact DCM/FCM/IB/DCO chain.
4. First event-contract or perpetual order transmitted through the pathway,
   with customer, custody, fee and volume evidence.
5. Any MPD interpretation of recommendation, routing optimization, order
   aggregation or AI assistance at the passive/agentic boundary.
6. Commission rulemaking or guidance that replaces the interim letter.
7. Any court or state action testing whether an access provider receives the
   same federal-preemption treatment claimed for the underlying DCM contract.
8. Any failure, insolvency or customer-remedy event that tests the PSP–
   registrant joint-liability undertaking.

These are package-level return gates. This research does not create a canonical
Watch Calendar entry.

## Primary source spine

- [CFTC Release 9300-26 — CFTC Staff Issues No-Action Position to Providers of Passive Software](https://www.cftc.gov/PressRoom/PressReleases/9300-26)
- [CFTC Staff Letter 26-25 — passive software providers](https://www.cftc.gov/csl/26-25/download)
- [CFTC Staff Letter 26-09 — Phantom-specific predecessor](https://www.cftc.gov/csl/26-09/download)
- [CFTC Release 9197-26 — Phantom announcement](https://www.cftc.gov/PressRoom/PressReleases/9197-26)
- [CFTC Rule 140.99 definitions and legal effect of staff letters](https://www.cftc.gov/LawRegulation/CFTCStaffLetters/lettersdefined)
- [Chairman Selig's August 20 Innovation Advisory Committee remarks](https://www.cftc.gov/PressRoom/SpeechesTestimony/opaselig10)
- [U.S. Senate September 15 floor activity — H.R. 3633 cloture not invoked, 49–50](https://www.senate.gov/legislative/LIS/floor_activity/09_15_2026_Senate_Floor.htm)
- [7 U.S.C. §16(e) — relation to other law and specified gaming-law preemption](https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title7-section16)

## Project routing and mutation boundary

This answer extends the CFTC side of the August 26
`SEC_CFTC_CURRENT_AUTHORITY_AND_OPERATIVE_CHANGE_LEDGER_2026-08-26.md` and
answers open gates in the August 20 CFTC IAC transcript analysis. Cross-agency
and SEC-specific September 17 analysis remains in its separate packages and is
not imported into this answer.

**Disposition:** saved as current Workbench research. No Chronicle event,
plotline, watch, vault source document, generated Observatory view or installed
app was changed. Chronicle landing and app shipment remain separate decisions.

## Coverage receipt

The full seven-page Letter 26-25, its press release and staff-letter index were
read through the cutoff. The full seven-page Phantom predecessor and its
official announcement were compared. The August CFTC roadmap, Senate cloture
result and controlling U.S. Code preemption provision were also checked. No
separate request letter exists on the 26-25 index; the
requester is listed as CFTC. No public list of relying PSPs or filed
undertakings was located by the cutoff.
