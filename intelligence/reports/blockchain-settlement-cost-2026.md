# Blockchain settlement cost and intermediary legitimacy audit

<!-- plain-english-entry:start -->
## In plain English

**Question:** Is blockchain settlement actually cheaper than today's payment and securities systems, and which middlemen does it really threaten?

**Answer:** Ledgers threaten the record-copying middlemen, not the ones who supply money and liquidity; instant settlement gives up netting.

**Evidence checked through:** 2026-08-02

The detailed record below keeps the legal wording, source limits and open questions.
<!-- plain-english-entry:end -->

**Cutoff:** 2026-08-02 ET  
**Status:** complete cross-package claim audit; bounded synthesis incorporated in the live vault  
**Scope:** Federal Reserve payment services, CHIPS, RTP, ACH, cards,
correspondent banking, DTC/NSCC, public blockchains, stablecoins, tokenized
deposits and permissioned shared ledgers  
**Accounting rule:** price, revenue, operating expense, capital expenditure,
liquidity opportunity cost, collateral, credit loss, fraud loss and legal-remedy
cost are different objects.  
**Finality rule:** technical state, verified event, legal right, funded
settlement, accounting recognition and final discharge are different clocks.

## I. Ruling

Katie's proposition is directionally right, but the comparison becomes more
interesting after the objects are separated.

> Blockchain and shared-ledger architectures place the greatest legitimacy
> pressure on intermediaries whose economic function is copying messages,
> maintaining duplicative state, reconciling breaks and controlling access to
> information. They do not by themselves replace the institutions that supply
> money, credit, liquidity, legally enforceable netting, finality, custody,
> correction, fraud allocation or a default waterfall.

The strongest evidence does **not** show that a public blockchain is simply
cheaper than the Federal Reserve's core rails. The core rail can already be
extremely cheap. The Federal Reserve's 2024 FedACH operating and imputed cost,
for example, works out to approximately **$0.00828 per commercial item** on a
simple service-cost-to-volume division. The expensive object is often the
institutional path surrounding the core entry: customer acquisition, account
access, fraud, compliance, FX, liquidity, credit, exception processing,
reconciliation, dispute rights and profit.

The serious threat is therefore architectural:

```text
cheap shared state
  -> fewer duplicated records and hand-offs
  -> fewer reconciliation and exception events
  -> faster collateral and cash visibility
  -> pressure on opaque access, processing and information rents
  -> surviving intermediaries must justify fees by an observable risk,
     liquidity, legal, balance-sheet or remedy function
```

That is a genuine legitimacy test. It is not yet evidence of wholesale
disintermediation.

## II. Claim audit

| Claim | Ruling | Reason |
|---|---|---|
| “Blockchain transactions are cheaper than bank payments.” | **NOT COMPARABLE AS STATED** | A gas fee is one price on one technical clock. A bank-payment price may include deposit funding, compliance, fraud allocation, credit, FX, payout and remedy. Fix the path, money object, corridor, amount, timing and finality standard first. |
| “A same-token, same-chain transfer can be cheaper and simpler than a multi-intermediary transfer.” | **SUPPORTED — BOUNDED** | One signed instruction can update a shared record and be verified by both parties without separate bilateral message reconciliation. Entry, exit, FX, custody and legal-remedy costs can remain. |
| “Shared state can remove reconciliation cost.” | **SUPPORTED AS A DESIGN CAPABILITY; REALIZED SAVINGS NOT GENERALLY QUANTIFIED** | BIS, MIT and industry experiments support the mechanism. The reviewed public record rarely supplies an audited before-and-after cost ledger or proves retirement of the duplicate process. |
| “Atomic settlement lowers every cost.” | **FALSE** | It may reduce settlement lag, replacement-cost exposure and failures, but gross or instant settlement can increase prefunding and liquidity demand and can sacrifice multilateral netting. |
| “Blockchains eliminate clearinghouses.” | **FALSE IN THE REVIEWED PRODUCTION STACK** | A ledger can match and transfer state; it does not automatically novate obligations, mutualize default risk, collect margin, run a loss waterfall or guarantee completion. |
| “Stablecoins eliminate banks.” | **FALSE IN THE REVIEWED PATHS** | Banks remain inside reserve custody, fiat entry/exit, issuer treasury, settlement and often distribution. Secondary holders may lack direct issuer redemption. |
| “The Federal Reserve's rail price equals its cost.” | **FALSE** | Mature services are priced for long-run recovery, while FedNow is still outside mature-service recovery. The 2024 FedNow average system cost per processed transaction was radically different from its posted per-item price. |
| “Blockchain threatens intermediary legitimacy.” | **SUPPORTED — FUNCTION SPECIFIC** | The threat is strongest where an intermediary supplies little beyond message relay, private state, reconciliation or access scarcity. It is weaker where the intermediary supplies balance sheet, legal finality, netting, liquidity, custody, fraud remedy or loss absorption. |
| “The incumbent will disappear if its old process is compressed.” | **NOT THE LEADING DOCUMENTED PATH** | SWIFT, DTCC, card networks and banks are adding shared-ledger and stablecoin functions inside existing constitutions. The likely first transition is cost compression plus institutional absorption. |

## III. The cost constitution

### 3.1 Eight cost layers

Every comparison in this package uses the following stack.

| Layer | Object | Examples |
|---|---|---|
| C0 | visible transaction price | gas, wire fee, interchange, processor charge, issuer mint/redemption fee |
| C1 | network processing and validation | hardware, software, validators, sequencer, node operations, message processing |
| C2 | access and integration | participant fees, FedLine/API connection, wallet, custody integration, implementation and certification |
| C3 | duplicate-state and exception work | matching, reconciliation, investigations, returns, failed trades, manual repair, corporate actions |
| C4 | liquidity and timing | prefunding, daylight liquidity, nostro balances, collateral opportunity cost, settlement delay |
| C5 | credit and loss absorption | issuer balance sheet, chargebacks, CCP guarantee, margin, default fund, committed facilities, capital |
| C6 | compliance, fraud and remedy | KYC, sanctions, transaction monitoring, identity attribution, disputes, reversals, consumer protection |
| C7 | legal, accounting and governance | title, finality, custody, rulebook, insolvency, correction authority, books and records, audit, supervision |

A claim that one system is cheaper is admissible only if it states which layers
are included and which institution still bears the excluded layers.

### 3.2 Six clocks

```text
instruction
  -> network acceptance / technical state
  -> guarantee, reservation or commitment
  -> money or title settlement
  -> legal finality / discharge
  -> accounting recognition
  -> correction, remedy or loss allocation
```

The same ledger event can be cheap at clock two while leaving clocks three
through six to a bank, issuer, custodian, CCP, court or insurer.

### 3.3 Required denominators

Never compare these as though they were interchangeable:

- cost per message;
- cost per originated item;
- price charged to each side;
- cost per gross obligation;
- cost per net settlement entry;
- cost per dollar of value;
- cost per legally final payment;
- cost per successfully redeemed token;
- cost per exception, fraud event or failed settlement; and
- annual participant or platform cost.

## IV. Quantitative public surface

These figures are useful precisely because they expose unlike accounting
objects. They are **not** a league table.

| System/object | Public figure | Derived or reported meaning | Critical exclusion |
|---|---:|---|---|
| FedACH, 2024 | $166,500,000 operating and imputed cost; 20.109 billion commercial items | **~$0.00828 per item**, derived | participant systems, fraud, returns, customer pricing and bank-account economics |
| FedACH, 2024 | $190,000,000 service revenue | **~$0.00945 revenue per item**, derived | revenue/item is not marginal cost or customer all-in price |
| Fedwire Funds + NSS, 2024 | $151,700,000 operating and imputed cost; approximately 210 million Fedwire originations | **~$0.72 per Fedwire origination**, derived allocation proxy | numerator includes NSS and service-wide costs; denominator excludes NSS and receipt-side billable events |
| Fedwire Funds + NSS, 2024 | $170,300,000 revenue | **~$0.81 per Fedwire origination**, derived allocation proxy | fixed, receipt-side and surcharge structure makes this unlike a quoted wire fee |
| Fedwire Funds, 2026 | $0.97 / $0.30 / $0.195 pre-incentive per origin or receipt by volume tier; lower incentive prices | posted network price | participation, access, bank markup, compliance and liquidity |
| FedNow, 2024 | $231,100,000 operating and imputed cost; 1.5 million transactions | **~$154.07 per transaction**, derived launch-stage average cost | not marginal cost; fixed network cost at deliberately low early volume |
| FedNow, 2026 | $0.045 customer-credit origination; first 2,500 monthly originations discounted to zero | posted participant price | long-run cost recovery remains outside mature-service reporting |
| Debit cards, 2023 | $34.12 billion interchange; $0.34 average per transaction; $0.129 average network fee | issuer compensation and network charges | merchant acquirer/processor fees, fraud, rewards, credit and other retail costs |
| Debit cards, 2024 | $0.23 covered / $0.51 exempt average interchange per transaction | current Board network survey | not the merchant discount or network operating cost |
| Retail remittances, 2025-Q3 | 6.36% global average customer price | fee plus FX-margin methodology | not infrastructure operating cost; corridor and payout method vary |
| CHIPS, 2025 | 26:1 liquidity efficiency; operator-estimated $5.5 billion annualized economic savings | liquidity-saving algorithm and continuous net settlement | operator estimate, not audited network operating expense or customer fee schedule |
| NSCC | 2024: $2.2 trillion average daily gross trade activity to $33.5 billion net settlement obligations; May 2026 netting rate 98.76% | multilateral netting and funding-compression benefit | does not state participant all-in cost; periods and denominators must remain separate |
| Circle, 2026-Q1 | $652,508,000 reserve income; $41,625,000 other revenue; $405,402,000 distribution and transaction costs | issuer economics are funded principally by reserve yield and shared with distribution partners | company-wide quarter, not per-transfer cost; distribution and chain transaction costs are combined |
| Public-chain stablecoin transfer | visible chain fee | C0 network price for the on-chain state transition | issuer, reserve, bank, FX, custody, bridge, compliance, off-ramp, remedy and security-subsidy layers |

### 4.1 What the Federal Reserve numbers actually say

The incumbent core is not one bloated price surface.

- **FedACH is already a sub-cent core processor.** A blockchain cannot establish
  an economy-wide saving merely by posting a low fee against this object.
- **Fedwire is inexpensive relative to its value and legal function.** It
  provides immediate final central-bank-money settlement, but its participant
  access, liquidity and bank-customer layers are separate.
- **FedNow shows why price is not cost.** Its 2026 $0.045 posted origination fee
  and 2024 launch-stage average cost of approximately $154 per processed
  transaction are not contradictory; they are different accounting clocks in
  a network whose fixed cost is being spread across early volume and whose
  long-run recovery period extends beyond the ordinary mature-service horizon.

This same warning applies to crypto. Gas can be below full economic cost when
security is also financed through token issuance, reserve income, sequencer
economics, venture subsidy or another product line.

### 4.2 Where the visible rents appear

The larger customer prices sit above or around core settlement:

- debit interchange and network charges;
- issuer/acquirer/processor economics;
- correspondent and nostro access;
- FX spread;
- compliance and fraud control;
- custody and wallet conversion;
- exception and dispute handling; and
- the value of credit, delayed repayment or guaranteed merchant receipt.

The World Bank's remittance measure is useful here. A 6.36% customer price on a
$200 remittance is $12.72, but that does not mean the payment rail costs $12.72
to operate. It means the complete customer/corridor/FX/payout stack is priced
that way. A stablecoin can attack several components, but only an end-to-end
quote from bank money in to usable money out can establish the saving.

## V. The netting trap

This is the largest correction to a simple “blockchain is cheaper” thesis.

### 5.1 What currently settles is the residual, not the gross market

Much of modern settlement is not a separate movement of cash for every trade.
Execution creates obligations; the clearing constitution then determines which
obligations can offset, which are guaranteed or novated, what collateral must
be posted, and which residual debit or credit must finally settle.

```text
millions of executed obligations
  -> validation and CCP guarantee / novation
  -> bilateral and multilateral netting
  -> margin, clearing-fund and liquidity controls
  -> one net debit or credit per participant / settlement set
  -> cash and securities settlement of the residual
```

NSCC's current reporting makes the transformation concrete. Its 2024 average
day compressed approximately $2.2 trillion of gross trade activity into $33.5
billion of net settlement obligations; its separately reported May 2026
netting rate was 98.76%. The periods and denominators cannot be blended, and
the figures are operator reports, but the economic function is clear. The CCP
turns a huge field of debits and credits into a much smaller funded residual
while placing a guarantee, margin system and default waterfall around the
interval.

That is why “the ledger only shifts debits and credits” is incomplete but
directionally important. The shifts are enforceable obligations inside a
credit, collateral and default constitution. The comparatively small residual
cash movement is possible because the system recognizes offset and manages the
risk that a participant fails before or at settlement.

### 5.2 What “real funds” means under atomic settlement

Atomic delivery-versus-payment requires the platform to be able to complete
both legs together or neither leg at all. Unless the design includes credit,
netting or a liquidity-saving mechanism, the buyer must control sufficient
eligible settlement money and the seller must control the deliverable asset at
the execution point. Those balances normally must be reserved, locked or
otherwise unavailable for conflicting use during execution.

“Real” does not mean physical cash. It means **funded and legally effective for
that settlement rule**.

| Atomic cash-leg object | What is actually available | What atomicity does not prove |
|---|---|---|
| central-bank reserves or tokenized reserve claim | liability of the central bank, available to eligible holders | universal access, unlimited intraday liquidity or customer-level title |
| commercial-bank deposit token | liability of the issuing bank on the governed platform | central-bank-money settlement, deposit insurance in every case or freedom from issuer credit risk |
| stablecoin | claim governed by the issuer's reserve and redemption constitution | direct holder redemption, bankruptcy remoteness, par in secondary markets or central-bank finality |
| prefunded participant balance | value already placed under the system's control | that the participant did not borrow, repo or encumber assets to fund it |
| intraday credit or overdraft | lender's balance sheet makes the payment possible | that the payment was pre-existing unlevered cash; credit and collateral costs remain |
| CCP guarantee / settlement promise | risk is mutualized and completion is supported under rules | present cash; the guarantee still needs liquidity and a loss waterfall |
| blockchain state transition alone | protocol state changed according to code | that the state is money, title, par-redeemable, legally final or recoverable |

The change from net deferred obligations to atomic gross settlement can
therefore make funding more “real” in the specific sense that the asset must be
present and controlled at the moment of exchange. It can also convert a system
that economizes on money through offset and credit into one that consumes much
more money or collateral intraday.

### 5.3 The balance-sheet consequence

The trade is not merely speed versus safety. It is a change in how the financial
system uses promises.

| Net/credit constitution | Atomic gross constitution |
|---|---|
| permits obligations to offset before cash moves | requires each included leg to be funded at execution |
| economizes on reserves and settlement balances | increases prefunding or intraday-liquidity demand |
| carries replacement, principal and participant-default exposure during the interval | compresses or removes the included settlement interval |
| uses CCP guarantee, margin and default resources to support the interval | uses locks, escrow, smart-contract conditions and immediate failure if funding is absent |
| lets participants source cash/securities before final settlement | demands earlier inventory and treasury readiness |
| can support higher balance-sheet velocity through netting and credit | can reduce leverage while increasing collateral immobility unless liquidity-saving features are rebuilt |

This is the deepest economic question in the tokenization transition:

> Does shared state merely make the same promises easier to see, or does it
> require the financial system to replace netted and credit-supported promises
> with funded assets at the point of execution?

The first path mainly attacks reconciliation. The second changes liquidity,
leverage, collateral velocity and the role of every institution that supplies
credit or guarantees completion.

### 5.4 Faster is not automatically cheaper

Atomic or real-time gross settlement can:

- remove settlement lag;
- reduce replacement-cost exposure;
- reduce some fails and reconciliation;
- make cash and assets reusable sooner; and
- automate conditional delivery-versus-payment.

It can also:

- require both legs to be prefunded;
- eliminate the time participants use to source cash or securities;
- sacrifice bilateral or multilateral netting;
- increase the quantity and velocity of intraday liquidity needed; and
- move credit risk into liquidity, custody, bridge or smart-contract risk.

The relevant optimization is not minimum transaction fee. It is:

```text
processing + reconciliation + exceptions
+ liquidity + collateral + capital
+ credit and default protection
+ failure, correction and legal-remedy cost
```

### 5.5 Incumbent algorithms already matter

Blockchain is not the only computational alternative to gross sequential
processing.

- CHIPS uses queuing, bilateral and multilateral offsetting, and continuous
  net settlement. The Clearing House reports that $1 of funding supported $26
  of 2025 settled value and estimates $5.5 billion of annualized liquidity
  savings. Its 2025 illustration compares approximately $96 billion of CHIPS
  funding for approximately $2 trillion of daily value with an estimated
  $442 billion of funding under a traditional RTGS path. This is an operator
  estimate, but it identifies the right cost object: liquidity, not message
  processing.
- NSCC states that multilateral netting reduces the value of payments requiring
  exchange by an average of 98–99%.
- MIT 14.129's strongest contribution to this question is therefore not
  “blockchain wins.” It is the design rule that common state, liquidity-saving
  mechanisms and algorithmic set-off must be compared by function.

A tokenized system that reproduces legally enforceable netting and liquidity
saving may be superior. A tokenized system that replaces a netted obligation
with millions of prefunded gross transfers may be computationally elegant and
economically worse.

## VI. What shared ledgers can remove, compress, retain or create

| Function | Likely effect | Legitimacy ruling |
|---|---|---|
| message relay between known institutions | **compress / commoditize** | An intermediary charging mainly for transport faces strong pressure. |
| bilateral books and post-event reconciliation | **compress materially** | Strongest displacement lane if one accepted state actually retires duplicate records. |
| matching and workflow sequencing | **automate / relocate** | Value remains in the rule and exception design, not manual handling. |
| operating-hours mismatch | **compress technically** | Liquidity, asset availability and legal operating hours may remain. |
| settlement asset | **retain** | A token representation needs an issuer or authoritative monetary liability. |
| FX and market making | **retain / automate partly** | Pricing, inventory and risk-bearing do not disappear because execution is coded. |
| netting and liquidity saving | **retain / redesign** | Removing it can destroy more value than reconciliation savings create. |
| credit and balance sheet | **retain** | Code cannot fund a queue, redemption, margin call or default. |
| CCP novation and default waterfall | **retain unless legally rebuilt** | Matching or atomic DvP is not a guarantee of completion. |
| custody | **change form** | Omnibus books may shrink, but key custody, recovery and entitlement law remain. |
| sanctions, KYC and fraud control | **retain / redistribute** | Public visibility can aid analytics; identity attribution and lawful intervention remain institutional. |
| chargeback, reversal and error correction | **reduce or relocate** | Irreversibility lowers one class of operational cost by shifting loss and remedy risk to users/providers. |
| accounting and audit | **compress evidence collection; retain judgment** | A common event record can reduce compilation, but authority, classification, estimates and assurance survive. |
| network governance and cyber resilience | **new or retained cost** | Validators, sequencers, upgrades, bridges, keys, incident response and forks form a new constitution. |

## VII. Public chain, stablecoin and permissioned-ledger economics

### 7.1 Public blockchain

A public blockchain buys something an ordinary database does not: open access
to a shared state whose update rules are enforced across independently operated
nodes. Replicated validation is a security and governance choice, not a free
efficiency gain.

Its visible fee can be low while total economic support also includes:

- protocol issuance or token dilution;
- validator or staking rewards;
- priority fees and MEV;
- L2 sequencer margin and L1 data-availability cost;
- node, RPC, indexer and wallet infrastructure;
- bridge security and losses; and
- volatile native-token funding of fees.

The correct public-chain comparison is not “server bill versus gas.” It is the
cost of maintaining the agreed security, availability and governance standard
per completed, economically distinct transaction.

### 7.2 Stablecoin

A stablecoin adds a private monetary liability and conversion constitution to
the chain.

```text
bank money in
  -> issuer eligibility and compliance
  -> reserve bank/custodian
  -> mint
  -> chain transfer
  -> custody or merchant acceptance
  -> redemption or exchange
  -> bank money / local money out
```

Low or zero issuer charges can be supported by reserve income. That is an
economic subsidy from the holder's forgone yield, not proof that issuance,
redemption, compliance and banking are costless. Circle's public terms also
make the legal perimeter visible: network and bank fees remain; direct
redemption depends on account eligibility; third-party prices may depart from
par; and on-chain transfers are generally irreversible.

Circle's first-quarter 2026 filing makes the economic engine measurable. It
reported $652,508,000 of reserve income, compared with $41,625,000 of other
revenue, and $405,402,000 of distribution and transaction costs. Circle says
transaction costs include blockchain network fees, but the combined caption is
dominated by distribution economics, including $330,600,000 paid under its
Coinbase arrangements in the quarter. The cheap visible token transfer sits on
top of a large reserve-yield and distribution machine.

### 7.3 Permissioned shared ledger

This is the most credible institutional cost-compression lane in the existing
corpus.

- SWIFT's shared-ledger design coordinates funded interbank commitments while
  bank-issued tokenized deposits and existing settlement systems remain
  authoritative at the relevant edges.
- DTC tokenization represents controlled securities entitlements while DTC
  retains record, freeze, reversal, reconciliation and correction powers.
- Project Agorá demonstrates atomic cross-border settlement in a prototype
  using tokenized commercial-bank deposits and jurisdiction-specific
  central-bank-reserve ledgers; real-value testing and production governance
  remain later clocks.

The likely first-order result is not no intermediary. It is **fewer duplicated
institutional records inside a permissioned federation**.

## VIII. The intermediary legitimacy test

An intermediary's fee remains economically legible when it can answer all six
questions.

1. **What scarce function is supplied?** Liquidity, balance sheet, risk
   transformation, legal finality, custody, correction, identity, insurance or
   default management?
2. **What exposure does the intermediary actually bear?** Principal, credit,
   fraud, operational, legal, liquidity or market risk?
3. **What record or decision is authoritative?** Is it creating legal effect or
   merely copying another institution's state?
4. **What happens on failure?** Who advances funds, returns value, corrects the
   record and absorbs the loss?
5. **Can the cost be tied to the function?** Is the charge a price, pass-through,
   risk premium, cross-subsidy or rent?
6. **Would the function still be required on a common ledger?** If yes, the
   institution may survive in altered form. If no, its legitimacy is exposed.

### 8.1 Pressure ranking

| Pressure | Intermediary function |
|---|---|
| **highest** | pure message relay; manual reconciliation; proprietary status lookup; redundant bilateral recordkeeping; avoidable operating-hours delay |
| **high** | closed integration gateways; opaque correspondent hops; noncompetitive conversion and data access; manual collateral movement |
| **mixed** | custody, payment orchestration, card networks, transfer agents and depositories—many old tasks compress, but control and remedy functions survive |
| **lower** | central-bank settlement asset, deposit issuer, liquidity provider, legally enforceable netting, CCP default management, fraud remedy, court and resolution authority |

The result is not a defense of every incumbent fee. It is a demand for a
function-level invoice.

## IX. Corpus map and what this pass adds

### 9.1 What was already established

The corpus already had most of the architecture:

- the Federal Reserve payment-stack audit separated access, operating control,
  liquidity, finality and cost allocation;
- the Federal Reserve financial constitution separated legal Bank, reporting
  entity, CASPR cost object, internal allocation, reimbursement and combined
  elimination;
- the MIT 14.129 package framed shared state as an information, coordination
  and liquidity design problem rather than a blockchain-adoption claim;
- the crypto/banking overlap map preserved issuer, settlement-asset,
  authoritative-record, liquidity and correction boundaries;
- the payment-transparency package established that gas is not all-in cost and
  that stablecoins can simplify transfer without simplifying the money
  lifecycle;
- the private-stack package mapped the incumbent-led absorption path through
  SWIFT, DTCC, banks, card networks, issuers, custodians and adapters; and
- the accounting-transition package supplied the transaction-native chain from
  authority and contract through performance, finality, correction, accounting
  and assurance.

### 9.2 What was genuinely missing

This pass adds the controlling comparative cost constitution:

1. one eight-layer cost stack for incumbents and tokenized rails;
2. one denominator discipline for price, average cost, liquidity and legal
   discharge;
3. direct 2024 Federal Reserve cost-to-volume calculations;
4. card, remittance, CHIPS and NSCC comparison surfaces;
5. the netting-versus-atomic-settlement trade-off as the central economic
   falsifier;
6. a pressure ranking for which intermediary functions are actually exposed;
   and
7. a documentary standard for proving realized savings rather than repeating
   pilot or marketing language.

## X. Evidence required for a demonstrated saving

A production claim should not be promoted without a before-and-after pack
containing:

1. named legal operators and participants;
2. identical transaction family, value range, corridor and service level;
3. old and new entity paths;
4. old and new C0–C7 costs;
5. volume and capacity assumptions;
6. liquidity, collateral and capital treatment;
7. fraud, exception and failed-settlement rates;
8. title, cash-finality and correction rules;
9. accounting treatment for capitalized development and recurring expense;
10. whether any cost is subsidized by issuance, reserve income, another product
    or loss shifting;
11. proof that a material legacy process was retired; and
12. independent assurance or regulator acceptance where the claim depends on
    books, records or legal finality.

## XI. Open gaps and falsifiers

### 11.1 Highest-value documentary gaps

- audited 2025 service-line Federal Reserve actuals and FedNow cumulative
  development-to-recovery bridge;
- CHIPS public participant fee schedule and independently reproducible
  liquidity-savings methodology;
- DTC/NSCC tokenization service fees and an event-level cash/title/finality
  record;
- SWIFT shared-ledger participant fees, cost allocation, default rules and one
  bank-confirmed live transaction with external settlement evidence;
- stablecoin end-to-end corridor quotes including bank-in, mint, transfer,
  bridge, FX, off-ramp and bank-out;
- audited public-chain or L2 full economic cost including issuance, sequencer,
  validator, infrastructure and bridge layers;
- before-and-after staffing, exception, reconciliation and failure data from a
  production institutional deployment; and
- an accounting/audit case in which a common event record actually retired a
  duplicate ledger or reconciliation control.

### 11.2 Falsifiers

The strong legitimacy-pressure thesis weakens if:

- shared-ledger deployments retain the same duplicate books and exception
  staffing;
- integration, cyber, bridge, custody and compliance costs exceed eliminated
  reconciliation cost;
- gross prefunding and lost netting consume the savings;
- incumbents can provide shared state at equal or lower cost without DLT;
- stablecoin entry/exit and FX keep end-user cost near incumbent levels;
- production failure rates or remedy losses rise materially; or
- legal and accounting authorities continue to require a separate controlling
  record.

The thesis strengthens if a named production family publishes audited evidence
that it retired a material reconciliation process, reduced total C0–C7 cost,
preserved or improved liquidity efficiency, and retained accepted finality,
correction and loss allocation.

## XII. Primary source spine

### Federal Reserve

- [2024 Payment System and Reserve Bank Oversight](https://www.federalreserve.gov/publications/2024-ar-payment-system-and-reserve-bank-oversight.htm)
- [2026 Federal Reserve service-pricing notice](https://www.federalreserve.gov/newsevents/pressreleases/files/other20251204a1.pdf)
- [2026 FRFS fee schedules](https://www.frbservices.org/resources/fees/)
- [FedACH annual volume and value](https://www.federalreserve.gov/paymentsystems/fedach_yearlycomm.htm)
- [FedNow 2026 fee schedule](https://www.frbservices.org/resources/fees/fednow-2026)
- [Fedwire Funds 2026 fee schedule](https://www.frbservices.org/resources/fees/wires-2026)
- [2023 debit interchange, network fees, issuer costs and fraud losses](https://www.federalreserve.gov/paymentsystems/2023-interchange-fee.htm)
- [2024 debit interchange by network](https://www.federalreserve.gov/paymentsystems/data-previous-years-accessible.htm)

### Liquidity, clearing and settlement

- [CHIPS 2025 value and liquidity report](https://www.theclearinghouse.org/payment-systems/Articles/2026/04/CHIPS-Delivers-Record-Value-and-Resilience-for-Participants-in-2025)
- [CHIPS annual statistics](https://www.theclearinghouse.org/payment-systems/CHIPS/chips-annual-statistics)
- [DTCC T+1 / NSCC netting FAQ](https://www.dtcc.com/ust1/faqs)
- [DTCC 2025 annual report](https://annuals.dtcc.com/)

### Tokenization, stablecoins and comparative economics

- [BIS Annual Economic Report 2026 — Anchoring trust in money](https://www.bis.org/publ/arpdf/ar2026e3.htm)
- [BIS Annual Economic Report 2025 — The next-generation monetary and financial system](https://www.bis.org/publ/arpdf/ar2025e3.htm)
- [CPMI — Tokenisation in the context of money](https://www.bis.org/cpmi/publ/d225.pdf)
- [BIS — On the future of securities settlement](https://www.bis.org/publ/qtrpdf/r_qt2003i.htm)
- [Project Agorá 2026 prototype results](https://www.bis.org/press/p260527.htm)
- [World Bank Remittance Prices Worldwide](https://remittanceprices.worldbank.org/)
- [World Bank remittance-price methodology](https://remittanceprices.worldbank.org/methodology)
- [Circle USDC terms](https://www.circle.com/legal/usdc-terms)
- [Circle Mint user agreement](https://www.circle.com/legal/user-agreement)
- [Circle 2026-Q1 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1876042/000187604226000150/crcl-20260331.htm)
- [Ethereum gas and fees](https://ethereum.org/developers/docs/gas/)
- [Solana fee structure](https://solana.com/docs/core/fees)

## XIII. Internal corpus spine

- `Research Packages/Fed, Clearing and Treasury/FED_PAYMENT_STACK_CONTROL_FINALITY_AND_COST_AUDIT_2026-07-25.md`
- `Research Packages/Monetary Cross-Cuts/CRYPTO_BANKING_SETTLEMENT_OVERLAP_DEEP_DIVE_2026-07-28.md`
- `Research Packages/Monetary Cross-Cuts/MIT_14129_SPRING_2025_COURSE_SYNTHESIS_2026-07-28.md`
- `Research Packages/Monetary Cross-Cuts/OPEN_SOURCE_REAL_TIME_ACCOUNTING_TRANSITION_MAP_2026-07-25.md`
- `Research Packages/Fintech and Private Rails/Payment Transparency and Hidden Constitution 2026-07-31/`
- `Research Packages/Fintech and Private Rails/Accounting Transition and Open Public Ledger 2026-07-30/`
- `Research Packages/Fintech and Private Rails/Retail Payment Terminal Transition 2026-07-28/`
- `Research Packages/Federal Government Whole-Site Recertification 2026-08-01/`
