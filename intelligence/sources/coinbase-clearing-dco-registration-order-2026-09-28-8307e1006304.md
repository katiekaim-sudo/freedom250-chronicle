> Source evidence cutoff: 2026-09-28T22:09:00-04:00

# Coinbase Clearing DCO Registration Order — Authority, Structure and Operating Gates

## Question

Did the CFTC approve Coinbase to clear derivatives, what exactly did the order
authorize, and does it establish live in-house clearing, USDC-native settlement
or approval of Coinbase's proposed single-stock perpetual futures?

## Controlling answer

**Yes.** On September 28, 2026, the Commodity Futures Trading Commission issued
a Commission order registering **Coinbase Clearing LLC** as a derivatives
clearing organization (`DCO`) under Commodity Exchange Act section 5b and CFTC
Regulation 39.3(a). This is a real Commission authorization, not a proposal,
staff statement or no-action letter.

The order is materially narrower than “Coinbase can clear anything.” Coinbase
Clearing may clear **fully collateralized futures, options on futures and
swaps**. It is not authorized by this order to clear ordinary spot crypto,
securities transactions or margined derivatives outside that fully
collateralized model. The order approves the clearing organization; it does not
approve any particular exchange product, asset, blockchain, stablecoin,
settlement institution, clearing member or customer launch.

The approved rulebook is important. It allows both FCM-intermediated customers
and self-clearing members, including natural persons that qualify for
membership. Every transaction must pass a pre-acceptance full-collateral check.
Because the DCO accepts only fully collateralized positions, its rulebook says
it does not maintain a member-default financial-resource package. That avoids a
traditional mutualized default-fund structure; it does **not** eliminate
collateral-value, custody, settlement-institution, liquidation, operational,
affiliate-conflict or legal risk.

The operating clock remains separate. Coinbase's existing domestic margined
perpetual-style futures were still publicly described on September 28 as
cleared by **Nodal Clear**, with initial and variation margin and twice-daily
funding/variation processing. No reached primary source establishes that
Coinbase Clearing has accepted its first transaction, enrolled a first member,
designated an initial product, named a settlement institution, published an
eligible-collateral notice or migrated existing open interest from Nodal.

**Current state:** `DCO registration effective; fully collateralized clearing
permission live; first-product and first-clearing operating receipt not yet
located`.

**Mutation boundary:** Workbench research only. No Chronicle promotion,
canonical watch, app state, product forecast or investment conclusion was
changed.

## 1. The legal actor and ownership chain

The regulated actor is **Coinbase Clearing LLC**, not Coinbase Global, Inc. as
an undifferentiated company and not Coinbase Derivatives, LLC.

The application supplies this exact chain:

`Coinbase Global, Inc. (Texas)`  
`→ 100% The Clearing Company of San Francisco, LLC (Delaware)`  
`→ 100% Coinbase Clearing LLC (Delaware)`

The middle company matters. Coinbase announced an agreement in December 2025
to acquire The Clearing Company, describing it as a prediction-markets company.
The September 2026 DCO application now records Coinbase Global's 100% ownership
through that entity. This turns the old acquisition story into a current
regulated-entity constitution, but it does not merge the legal obligations of
the parent, DCM, FCM and DCO.

| Coinbase entity/function | Regulatory state | What it does not prove |
|---|---|---|
| Coinbase Derivatives, LLC | CFTC-designated contract market (`DCM`); the trading venue | Not the DCO and not itself the clearing counterparty |
| Coinbase Financial Markets, Inc. | Registered futures commission merchant (`FCM`) | FCM registration does not authorize operation of a clearinghouse |
| Coinbase Clearing LLC | DCO registered by the September 28 order | Does not automatically activate a product or replace Nodal Clear |
| Coinbase Global, Inc. | Public parent and ultimate owner | Parent ownership is not a single omnibus regulatory license |

The result is a more vertically complete Coinbase derivatives stack on the
**authority** plane: venue, intermediary and clearing permissions now exist in
separate affiliates. The operating, membership, product, collateral and
settlement planes still need their own receipts.

## 2. What the Commission order actually authorizes

The three-page order:

1. finds the application demonstrates compliance with the DCO requirements in
   CEA section 5b and Regulation 39.3(a);
2. registers Coinbase Clearing as a DCO;
3. permits it to clear fully collateralized futures, options on futures and
   swaps, using the Regulation 39.2 definition of a fully collateralized
   position;
4. makes the order dependent on Coinbase's representations and supporting
   material; and
5. reserves Commission power to condition, modify, suspend, terminate or
   otherwise restrict the order.

The order also records two institutional commitments: Coinbase Clearing will
perform DCO self-regulatory functions, including member-eligibility and rule
enforcement, and it will keep clearing-member funds separate from its own funds.
It characterizes funds held in a clearing-member account as member property
under the Bankruptcy Code. That sentence should not be converted into a claim
that every end customer's assets have the same legal status; FCM customer
segregation and cleared-swaps collateral rules remain account- and product-
specific.

## 3. The approved clearing model

### Access

The rulebook creates two principal membership routes:

- an FCM may become a clearing member and clear for itself and FCM customers;
- a qualifying person may become a self-clearing member for its own account.

The definition of member and the eligibility rules do not exclude natural
persons. The structure can therefore support the direct/non-intermediated and
hybrid retail-clearing models that CFTC staff examined in its December 2025
request for comment. Registration does not prove that a retail member has been
admitted or that direct access is commercially open.

### Novation and product reach

For accepted transactions, the DCO substitutes itself through novation as the
central clearing counterparty. Its application says it plans to serve DCMs and
SEFs that agree to its rules, procedures and risk requirements. The rulebook is
not limited by text to Coinbase Derivatives or to crypto products.

That general capacity is not a product admission. A DCM or SEF must still have
the relevant product and rule authority, designate or connect to the DCO, and
complete the required integrations and filings.

### Full collateralization

The clearest risk-design choice is Rule 6.1:

- all trades must remain fully collateralized;
- the DCO checks the relevant member or sub-account before accepting a trade;
- FCMs must reserve sufficient customer funds before submitting the order; and
- the DCO says it maintains no member-default financial-resource package
  because it clears only fully collateralized positions.

This is not ordinary portfolio-margin clearing. It attempts to cap the DCO's
credit exposure by collecting the full required resources before acceptance.
Risk remains in what collateral is accepted and valued, whether it can be
liquidated when needed, where it is held, whether systems and affiliates fail
together, and whether the legal security interest and segregation structure
survive insolvency and operational disruption.

### Collateral, custody and finality

The rulebook does not name USDC, another token or a blockchain. Instead it lets
Coinbase Clearing identify acceptable collateral through participant notices
and its website, value that collateral, and hold it at a `Settlement
Institution`, defined as an approved settlement bank or qualified custodian.
Participants grant the DCO a first-priority security interest and control over
posted financial assets. Participant collateral must be legally and
operationally segregated from Coinbase Clearing's property, and cleared-swaps
customer collateral receives its separate Part 22 treatment.

Settlement must occur at least once each business day, with intraday capacity.
The rulebook treats payments and transfers as irrevocable and unconditional
when the relevant Coinbase Clearing or settlement-institution account is
debited or credited, subject to error corrections. Deposit availability and
withdrawal timing still refer to settlement-institution business days. That is
not, by itself, a proven 24/7 on-chain legal-finality constitution.

## 4. What the order does **not** approve

| Headline claim | Ruling |
|---|---|
| “CFTC approved Coinbase clearing” | **Yes**, if this means Commission registration of Coinbase Clearing LLC as a DCO for the exact fully collateralized scope. |
| “Coinbase can now clear all of its derivatives” | **No.** The order is limited to fully collateralized positions; existing Coinbase margined products remain a different risk and operating model. |
| “Coinbase's current perpetual futures moved in-house” | **Not established.** Current Coinbase product pages still name Nodal Clear. |
| “CFTC approved single-stock perpetuals” | **No.** Coinbase Derivatives' security-futures product rules were still awaiting CFTC approval, and its SEC customer-margin filing remains proposed. |
| “CFTC approved USDC as native settlement collateral” | **No.** Neither the order nor the approved rulebook names USDC. Eligible-collateral notices, custody, valuation, redemption and an operating receipt remain necessary. |
| “CFTC approved an on-chain/Base clearinghouse” | **No.** No chain, smart contract or ledger is named in the order or rulebook. |
| “Coinbase can clear spot crypto or stocks” | **No.** DCO registration is a derivatives permission; it is not SEC clearing-agency registration or a comprehensive spot-market license. |
| “Registration proves launch, customers or volume” | **No.** The application anticipated clearing upon registration, but no first-product, first-member or first-trade receipt was located. |

## 5. The single-stock-perpetual boundary

Coinbase Derivatives' September security-futures package is a separate legal
chain:

- its proposed Chapter 12 for cash-settled futures on individual stocks and ETF
  shares, including perpetual single-stock futures, was filed with both the SEC
  and CFTC;
- the SEC notice explicitly said the CFTC had **not yet approved** the rule
  change;
- the distinct SEC customer-margin filing is still proposed, with comments due
  October 15 and a later approval/disapproval clock; and
- that filing contemplated a separately registered third-party clearing house,
  not automatic clearing by the exchange itself.

Coinbase Clearing is now a possible affiliated DCO candidate, but the public
record does not yet designate it for those products. More importantly, the new
DCO's order permits only fully collateralized clearing, while Coinbase's
existing domestic perpetual-style futures use initial margin, variation margin
and funding flows through Nodal Clear. A product-specific filing must show how
any proposed security future fits the DCO's permitted risk model. The DCO order
does not answer that question.

## 6. Why this matters

This is a meaningful institutional step, not a cosmetic registration. Coinbase
can now place a regulated central-counterparty function inside its corporate
group rather than relying only on an outside DCO. That may shorten product and
integration chains, give Coinbase more control over participant admission,
collateral policy, settlement operations and data, and support direct or hybrid
clearing models.

The change also concentrates functions and conflicts. The important map is now:

`customer/interface → FCM or direct member → Coinbase-affiliated venue →`
`Coinbase-affiliated DCO → settlement bank/qualified custodian → collateral`
`liquidation, correction and legal remedy`.

The authority-through-the-adapter thesis therefore strengthens, with a
qualification: Coinbase is no longer merely the customer-facing adapter in
this lane; it can own more of the regulated core. But the order preserves
separate legal entities, CFTC core principles, member rules, segregation,
collateral control, external settlement institutions and Commission
supervision. “Vertically integrated” does not mean “one ledger” or “outside the
old constitution.”

## 7. Exact operating receipts to watch

Re-open this answer when the public record shows any of the following:

1. Coinbase Clearing publishes its live website, final operative rulebook,
   participant notices or fee schedule;
2. the DCO names accepted collateral, settlement banks or qualified custodians;
3. a DCM or SEF publicly designates Coinbase Clearing for a named product;
4. Coinbase Derivatives amends its clearing-house designation or transfers
   open interest from Nodal Clear;
5. a first FCM, self-clearing member or retail direct member is admitted;
6. a first clearing, open-interest, settlement or volume record is published;
7. an official notice identifies USDC, a blockchain or real-time 24/7
   settlement and shows the rights, custody, redemption and failure process;
8. the CFTC approves or rejects Coinbase's proposed security-futures rules; or
9. the SEC approves, disapproves or institutes proceedings on the customer-
   margin filing.

## Source spine

1. [CFTC Coinbase Clearing DCO filing page and registration state](https://www.cftc.gov/IndustryOversight/IndustryFilings/ClearingOrganizations/64361)
2. [CFTC Commission order registering Coinbase Clearing LLC, September 28, 2026](https://www.cftc.gov/media/14681/Coinbase%20Clearing%20LLC%20-%20DCO%20Registration%20Order%20%289-28-26%29/download)
3. [Coinbase Clearing application rulebook, Exhibit A-2](https://www.cftc.gov/media/14646/Coinbase%20Clearing%20LLC%20DCO%20Application%20-%20Exhibit%20A-2%20Proposed%20Rulebook%20/download)
4. [Narrative summary of proposed clearing activities, Exhibit A-3](https://www.cftc.gov/media/14651/Coinbase%20Clearing%20LLC%20DCO%20Application%20-%20Exhibit%20A-3%20Summary%20of%20Proposed%20Clearing%20Activities/download)
5. [Corporate ownership structure, Exhibit A-7](https://www.cftc.gov/media/14656/Coinbase%20Clearing%20LLC%20DCO%20Application%20-%20Exhibit%20A-7%20Corporate%20Organizational%20Structure/download)
6. [CFTC registered DCM entry for Coinbase Derivatives and existing Nodal Clear relationship](https://www.cftc.gov/IndustryOversight/IndustryFilings/TradingOrganizations)
7. [Coinbase current perpetual-style futures margin and Nodal Clear operating description](https://help.coinbase.com/en/derivatives/perpetual-style-futures/margin-and-clearing)
8. [SEC Release 34-106420, Coinbase security-futures rule filing](https://www.sec.gov/files/rules/sro/coin/2026/34-106420_0.pdf)
9. [SEC Release 34-106443, proposed security-futures customer-margin rules](https://www.sec.gov/files/rules/sro/coin/2026/34-106443.pdf)
10. [CFTC staff request for comment on direct clearing by retail participants](https://www.cftc.gov/PressRoom/PressReleases/9158-25)
11. [Coinbase announcement of agreement to acquire The Clearing Company](https://www.coinbase.com/blog/coinbase-to-acquire-the-clearing-company-powering-the-future-of-prediction-markets)

**Disposition:** `current`. First-class Workbench answer; no Chronicle landing,
canonical watch or app shipment authorized.
