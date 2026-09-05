> Source evidence cutoff: 2026-08-31T12:08:12-04:00

# The Overall DLT Transition, 2025–2026

## Bottom line

The institutional DLT transition has crossed out of the “blockchain pilot” era,
but it has not crossed into one new financial system.

The observable system is becoming a **federation of programmable legal ledgers
and adapters**. Regulated banks, central securities depositories, central banks,
market infrastructures and selected public networks are moving different pieces
of a transaction onto DLT while preserving—or deliberately rebuilding—the legal
constitution around the claim.

The transition is most advanced in:

- token representation and DLT-native issuance;
- shared workflow and lifecycle state;
- 24/7 or extended-hours movement inside a defined participant perimeter;
- controlled or narrow-production delivery-versus-payment and
  payment-versus-payment;
- reusable collateral instructions and visibility; and
- rule-based execution and reconciliation.

It is less advanced in:

- cross-network authoritative title;
- routine central-bank-money settlement on the same ledger as the asset;
- collateral eligibility across venues and central banks;
- interoperable liquidity without duplicated buffers;
- accounting recognition and correction shared across firms;
- public first-failure, insolvency, fork, outage and exit evidence; and
- measured cost, liquidity or end-user gains at systemic scale.

That makes the real transition object neither “the token” nor “the chain.” It is
the conversion point between technical state and legal/economic consequence:

```text
code state
  -> represented claim
     -> authoritative record
        -> eligible collateral
           -> funded settlement
              -> legal discharge
                 -> accounting close
                    -> correction, recovery and loss
```

## The cleanest phase model

### Phase 1 — digital representation

A token represents an existing deposit, security, fund interest, commodity or
other claim. The underlying legal object and authoritative book remain
recognizable outside the token system.

Examples include DTC-tokenized entitlements, tokenized bank deposits and digital
twins used in collateral pilots. Representation can improve mobility without
changing the legal issuer, registered holder, custodian or insolvency treatment.

### Phase 2 — shared execution

Multiple parties use a shared state machine to validate commitments, coordinate
conditions and execute linked steps. This is where smart contracts and DLT are
already most useful: the system reduces sequential messages and reconciliation
between parties that previously kept separate workflow states.

Swift's shared ledger is an unusually explicit example. Swift operates the
orchestration layer, but banks retain keys, assets, funding and the authority to
settle through RTGS, correspondent or other agreed systems.
[Swift](https://www.swift.com/news-events/news/swifts-blockchain-based-shared-ledger-progresses-mvp-implementation)

### Phase 3 — authoritative on-ledger asset state

The DLT record becomes part of the operative issuance, custody, settlement or
participant-entitlement constitution. This is real in bounded cases.

- SIX/SDX operates a regulated DLT exchange/CSD and has issued and serviced
  digital bonds.
- Clearstream's D7 DLT issued a CSDR-compliant EIB commercial paper that was
  mobilized through triparty collateral management and ECMS for Bundesbank
  financing.
- DTC's July production event moved tokenized participant entitlements, but the
  traditional security remained immobilized at DTC and the first service phase
  did not make the cash leg digitally settled.

The existence of Phase 3 cases falsifies the simplistic claim that “the real
record always remains off-chain.” The proper claim is narrower: **record
authority migrates object by object and remains governed by the relevant
issuer/CSD/operator constitution.**

### Phase 4 — on-ledger money and atomic exchange

The cash claim and asset can be executed conditionally, sometimes on the same
platform. This phase contains legally different objects that must not be
collapsed:

- central-bank wholesale money;
- tokenized commercial-bank deposits;
- omnibus-account-backed settlement units;
- stablecoins; and
- synchronized conventional RTGS balances.

Project Helvetia/SDX has settled digital bonds against SNB wholesale CBDC in a
live but limited pilot. Project Samara used a real tokenized bond and purpose-
built wholesale central-bank digital money in a closed real-world experiment.
Project Agorá processed 30 real-value transactions across 17 scenarios and six
currencies, but issuance/redemption still depended on external RTGS and bank
books, scripted windows, approvals and fallback procedures.
[BIS Agorá](https://www.bis.org/project/agora) ·
[Bank of Canada Samara](https://www.bankofcanada.ca/2026/03/bank-canada-export-development-canada-rbc-td-successfully-complete-bond-issuance-experiment-distributed-ledger-technology/)

“Atomic” describes linked technical execution. It does not, by itself, answer:

- whether each party had legal power to transfer;
- when title became effective against third parties or insolvency;
- whether the cash asset was central-bank, commercial-bank or issuer risk;
- which ledger prevails after divergence;
- who can reverse, correct or compensate; or
- which loss waterfall applies.

### Phase 5 — collateral and liquidity integration

This is where DLT becomes economically consequential rather than merely more
elegant.

The strongest current receipt is Europe's March 2026 change permitting certain
DLT-issued marketable assets at eligible CSDs to enter the Eurosystem collateral
framework. Clearstream then demonstrated a tokenized EIB commercial paper moving
through triparty collateral management and ECMS into Bundesbank financing.
[ECB collateral decision](https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.pr260127_1~a946167ce1.en.html) ·
[Clearstream transaction](https://www.clearstream.com/clearstream-en/newsroom/260629-5355756)

That chain proves more than token issuance:

```text
DLT-native security
  -> eligible CSD instrument
     -> recognized triparty collateral
        -> ECMS mobilisation
           -> central-bank financing
```

It does not prove universal collateral portability. Eligibility, valuation,
haircuts, liens, segregation, hours, settlement compatibility and central-bank
access still govern the usable liquidity value.

### Phase 6 — native public settlement perimeter

This is the next major institutional boundary. The Eurosystem is not merely
connecting private DLT to an unchanged public rail. Pontes combines
synchronisation with an intended Eurosystem-operated DLT capability. At initial
launch, legal cash finality remains anchored in T2; the stated trajectory is
toward finality on the Eurosystem DLT platform, later smart-contract functions
and longer operations. Appia is evaluating a unified European ledger, a public
ledger connected to private networks, and multiple interconnected ledgers.
[ECB Appia roadmap](https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.pr260311~14ddf51a77.en.html) ·
[ECB, Central banks on-chain](https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp260828~fe9afc86e8.en.html)

This is the strongest evidence that “legacy institutions only sit behind the
chain” is also too simple. A monetary sovereign can extend its own operating
perimeter into the new architecture.

### Phase 7 — failure-proven, normalized production

No reviewed platform has publicly closed this phase across the full stack.

The missing receipts include:

- a fork, validator outage or smart-contract error with a documented legal and
  accounting correction;
- a failed PvP/DvP leg after one asset has technically moved;
- a bank, participant or custodian default while value is locked;
- a high-volume detokenization, redemption or legacy exit under stress;
- completed coupon, maturity, default and recovery lifecycles;
- published loss allocation among ledger operator, CSD, custodian, bank, wallet
  provider and client; and
- repeated volumes and measured liquidity/cost benefits sufficient to retire
  legacy operation rather than run in parallel.

Phase 7, not the next launch, determines whether DLT has become durable market
infrastructure.

## What is actually changing

### 1. The database is becoming a governed multi-party state machine

Traditional finance is already digital. DLT's distinctive institutional value
is not that records become electronic; it is that selected parties can share a
consistent, programmable transaction state without every step passing through
sequential bilateral messages and reconciliation.

That can compress issuance, matching, conditional execution, settlement and
lifecycle servicing. It can also make a faulty condition propagate faster.

### 2. The two-tier monetary system is being re-expressed, not automatically
abolished

Project Agorá and the BIS unified-ledger model place tokenized central-bank
reserves and tokenized commercial-bank money on compatible programmable
platforms while preserving the roles of central and commercial banks. Kinexys
similarly makes a bank deposit programmable; it does not turn the holder into a
direct claimant on the central bank.

The competition is increasingly over **which form of regulated money reaches
which ledger with which redemption, liquidity and finality rights**.

### 3. Market infrastructures are becoming protocol governors

DTC, Clearstream, SIX, Euroclear, LSEG and Swift are not simply defending old
databases. They are converting their rulebooks, admission powers, custody and
recordkeeping roles into network and adapter governance.

This can produce a smaller role in routine message handling but a stronger role
at the decisive boundaries:

- approved networks and wallet admission;
- definition of the legal claim;
- authoritative record and reconciliation;
- collateral and settlement eligibility;
- freeze, reversal and correction;
- participant default and orderly exit.

### 4. Interoperability is becoming the base case

The evidence does not point to universal convergence on a single chain.

- DTC is pursuing a multi-chain service.
- LSEG emphasizes connection across digital and traditional systems.
- Swift adds orchestration above banks' own ledgers and payment systems.
- Pontes bridges and then extends into a public DLT rail.
- Appia keeps single-ledger and multi-ledger architectures open.
- SDX and Clearstream connect DLT issuance into existing CSD, collateral and
  central-bank-money infrastructure.

Interoperability preserves specialization and limits technology lock-in, but it
recreates the very interface, trust and liquidity-fragmentation problems DLT is
supposed to reduce. The adapter becomes critical infrastructure.

### 5. Liquidity is the hidden constraint

Faster or continuous execution can increase, not reduce, liquidity needs when:

- obligations settle gross instead of net;
- collateral must be duplicated across ledgers;
- central-bank money is unavailable at the same hours;
- the token cannot yet be pledged in the relevant facility;
- conversion back to the legacy book is slow; or
- conditional smart contracts trigger clustered margin calls.

This is why central-bank settlement, collateral eligibility, bridge hours and
emergency-liquidity access matter more than transaction speed alone.

### 6. Accounting and correction remain institution-specific

DLT can provide a signed, attributable event history and earlier shared
reconciliation. It does not decide GAAP, tax, regulatory capital, entity
boundaries, valuation, impairment, beneficial ownership or when a correcting
entry is legally required.

The future accounting architecture is likely transaction-native at the event
layer and still institution-specific at recognition and reporting layers:

```text
shared signed event
  -> institution-specific classification
     -> legal and accounting recognition
        -> reconciliation to control accounts
           -> correction / restatement / disclosure
```

## The architecture that now looks most likely

The evidence supports a **hybrid federated architecture** through the end of the
current transition window:

```text
public and private asset ledgers
  <-> regulated CSD / bank / market-utility ledgers
      <-> orchestration and interoperability adapters
          <-> tokenized deposits / settlement units / stablecoins
              <-> central-bank RTGS and emerging public DLT money
                  <-> accounting, supervision, courts and resolution
```

This is an inference, not a forecast receipt. It would be weakened by a single
shared infrastructure attaining authoritative multi-asset title, central-bank
money, recurring scale, cross-jurisdiction finality and public failure-proof
operation while legacy systems materially retire.

## What this means for the Observatory's projects

### Critical minerals, energy, data centers and industrial finance

The near-term DLT wedge is not “the project is financed on-chain.” It is better
control over evidence and conditional release:

```text
verified milestone / shipment / inventory / receivable
  -> attributed event
     -> covenant or borrowing-base state
        -> authorized draw / collateral release / payment
           -> settled cash
              -> auditable accounting and correction
```

Current flagship project financings remain conventional and their public files
do not show stablecoin, tokenized debt or DLT settlement. DLT becomes a real
project-finance claim only when a named borrower, executed instrument,
authoritative collateral/title record, controlled account, first draw, settled
cash and default/correction path are documented.

### Cross-border payments and trade

DLT can combine programmable bank money, PvP, compliance evidence and
conditional release. But domestic first/last-mile systems, FX liquidity,
sanctions/AML decisions, privacy law, RTGS access and correspondent relationships
remain. The global rail remains a federation, even if its coordination layer
becomes shared.

### DTCC, Treasury markets and collateral

Token mobility may improve around-the-clock inventory use, but the decisive
question is whether the token can enter DTC settlement value, CCP margin, FICC
delivery, central-bank collateral and final cash settlement without returning
to the traditional book. Until those layers move, “24/7 asset movement” can
open a liquidity clock gap rather than close it.

### Stablecoins and tokenized deposits

These are settlement-asset candidates, not synonyms. Track:

- issuer and direct legal claim;
- reserve or deposit backing;
- redemption at par and at what hour;
- access to central-bank liquidity;
- transfer finality and freeze/reversal power;
- insolvency segregation;
- the ledger and participant perimeter; and
- conversion to other bank money and central-bank money.

### Government and public administration

Public-sector DLT adoption is most plausible where several parties need a common
evidentiary history—grants, procurement, trade documentation, inventory,
provenance or benefits coordination. A prototype does not make an entitlement,
payment, audit or appropriation legally operative. Identity and provenance also
do not confer authority to award, pay, waive, seize or correct.

## The Observatory's new research rule

For every DLT claim, record six separate states:

1. **object** — what legal/economic claim exists;
2. **representation** — what the token or ledger entry says;
3. **authority** — which book, law and operator make it effective;
4. **settlement** — what asset actually discharged the obligation;
5. **recognition** — which accounting/collateral/regulatory systems accepted it;
6. **failure** — who can correct, unwind, fund or absorb the loss.

Then assign an exact maturity. Do not let “pilot,” “real value,” “production
environment,” “launch,” “live,” “atomic,” “collateral” or “central-bank money”
stand without the object and boundary they actually describe.

## Net ruling

The overall DLT transition is best understood as **the programmable
reconstitution of financial authority**.

Execution and shared state are distributing. Incumbent institutions are not
simply disappearing; they are becoming issuers, protocol governors, identity
and access gates, conclusive-record owners, collateral arbiters, liquidity
providers and failure authorities inside a more plural technical system.

Some constitutional state has genuinely moved on-ledger. Much of the final
constitution has not. The next decisive evidence will not be a new token. It
will be:

```text
authoritative title
  + usable collateral
  + on-ledger central-bank money
  + legally final exchange
  + accounting recognition
  + successful correction and loss allocation
  + recurring volume under stress
```

That is the threshold at which a DLT experiment becomes a new financial rail.
