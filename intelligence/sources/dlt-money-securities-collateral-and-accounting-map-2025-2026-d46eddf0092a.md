> Source evidence cutoff: 2026-08-31T12:08:12-04:00

# DLT Money, Securities, Collateral and Accounting Map, 2025–2026

## Purpose

“Tokenization” often collapses legally different assets and transaction states.
This map keeps the object, issuer, record, settlement and recognition layers
separate.

## Typed money objects

| Object | Legal/economic claim | Typical authoritative record | Core risk / boundary |
|---|---|---|---|
| tokenized central-bank reserve / wCBDC | direct claim on the central bank or legally equivalent representation of a reserve balance, subject to design | central-bank/approved DLT and reserve accounts | access, legal finality, monetary-policy control, operating hours, privacy and emergency liquidity |
| synchronized RTGS money | conventional central-bank balance moved conditionally against external DLT state | RTGS record | bridge/oracle trust, weak versus same-ledger atomicity, timing and outage |
| tokenized commercial-bank deposit | deposit claim on a named bank | bank core/BDA and authorized DLT record | bank credit/insolvency, deposit law, conversion, eligible participants and liquidity |
| omnibus-backed settlement unit | claim or entitlement backed by pooled central-bank/commercial-bank money | operator ledger plus omnibus account | holder's indirect legal claim, segregation, operator failure and redemption |
| reserve-backed stablecoin | redemption claim on private issuer/trust and specified reserve assets | issuer/token ledger, custodian and reserve records | run/liquidity risk, reserve quality, legal priority, access to backstop, freeze/redeem rules |
| unbacked / crypto-native token | protocol-defined asset without traditional issuer liability | protocol ledger | price, governance, operational, market and legal-recognition risk |

No row becomes “central-bank money” merely because it ultimately redeems through
a bank or omnibus account.

## Typed asset objects

| Object | What the token means | Record question |
|---|---|---|
| native DLT security | the legally issued security is created/recorded within the DLT/CSD constitution | Does governing law and the operator rulebook make the ledger the issuance/title record? |
| tokenized security entitlement | token represents an intermediated claim to a security held by a CSD/custodian | Does movement change participant entitlement, beneficial interest or registered ownership? |
| digital twin | token mirrors an external asset or position for workflow/mobility | Which external record remains conclusive and how is supply reconciled? |
| tokenized fund interest | token represents a share/unit administered by a fund/transfer agent | Which register and administrator establish ownership, NAV, subscriptions/redemptions? |
| tokenized depositary receipt | token represents a receipt while a depositary holds the underlying asset | What claim exists against the depositary; where is the underlying held? |
| tokenized real/physical asset | token represents title, receipt, inventory, receivable or contractual rights | Which property/warehouse/contract registry makes the claim effective and perfected? |

## Securities transition chain

```text
issuer authorization
  -> instrument terms and governing law
     -> issuance / creation record
        -> investor or participant entitlement
           -> trading and matching
              -> asset transfer
                 -> cash settlement
                    -> corporate actions and servicing
                       -> collateral use
                          -> maturity / redemption / default
```

DLT can compress the middle of this chain. It does not automatically close the
first or last steps.

### Strongest current securities receipts

- **SDX:** regulated DLT CSD issuance and lifecycle infrastructure.
- **D7 DLT / EIB CP:** DLT-native issuance crossed into triparty collateral and
  Bundesbank financing.
- **Euroclear D-FMI:** recurring digital-note issuance at reported aggregate
  scale, with cash/finality detail still case-specific.
- **DTC:** limited-production participant-entitlement use across several
  workflows, without first-phase digital DTC cash settlement.
- **Project Samara:** a real closed experiment joining tokenized bond and
  wholesale central-bank digital money across issuance, sale and trading.

## Collateral transition chain

```text
asset exists
  -> owner has power to pledge
     -> title / entitlement is authoritative
        -> collateral taker recognizes asset class
           -> legal lien or control is perfected
              -> price, haircut and eligibility apply
                 -> collateral is mobilized to secured obligation
                    -> funding or margin credit is granted
                       -> release, substitution, liquidation or loss
```

“Collateral mobility” often proves only the instruction and visibility layers.
The EIB D7 DLT transaction is more important because the instrument was actually
mobilized through Clearstream triparty and ECMS for central-bank financing.

### Why 24/7 collateral can increase stress

- automated calls can accelerate liquidity demand;
- asset mobility can outrun cash and settlement-system hours;
- assets may be trapped on a venue where the lender/CCP/central bank does not
  recognize them;
- multiple networks may require duplicated liquidity buffers;
- gross real-time settlement may sacrifice netting efficiencies; and
- fast liquidation can amplify price moves.

The proper benefit test is not “the token moved quickly.” It is measured
reduction in funding cost, trapped inventory, settlement fails, margin shortfall
or loss—after accounting for liquidity and operational risk.

## Accounting transition chain

DLT can provide a transaction-native event record:

```text
identified parties
  + signed instruction
  + contract/rule version
  + asset and cash state
  + timestamps
  + approvals and exceptions
  -> attributable shared event
```

Each legal entity must still determine:

```text
entity boundary
  -> asset/liability/equity classification
     -> recognition and derecognition
        -> measurement / valuation / impairment
           -> tax and regulatory treatment
              -> journal and control accounts
                 -> disclosure, audit and correction
```

The ledger can improve provenance and reconciliation. It does not eliminate
judgment or create universal accounting truth.

### Four truths to keep separate

| Truth | Question |
|---|---|
| economic | What changed in value, risk or obligation? |
| legal | What right, duty, title or priority exists? |
| settlement | What asset/account movement discharged the transaction? |
| accounting | How and when does each entity recognize and report it? |

A transaction can be technically complete while one or more of the other truths
remain disputed, conditional or unrecognized.

## Identity, compliance and permission

Permissioned DLT moves part of finance from bilateral onboarding toward shared
credentials, but credentials must remain typed:

| Credential | What it can prove | What it cannot prove alone |
|---|---|---|
| legal-entity identity / LEI | entity identifier and asserted identity | sanctions clearance, account authority or solvency |
| KYC credential | a party passed defined checks at a time | universal access or current compliance status |
| wallet binding | a key/address is associated with a participant | beneficial ownership of every asset or human authorization of every transfer |
| asset provenance | history and attestations | legal title, quality, valuation or collateral eligibility |
| oracle / event attestation | an external event was reported under a method | contract interpretation or payment authorization |
| regulator/operator admission | entity may use a service under conditions | entitlement to central-bank credit or every network function |

Identity truth is not permission truth. Provenance is not title. A verified
physical event is not automatically a payable obligation.

## Industrial and project-finance application

The strongest prospective use is to join evidence and controlled finance:

```text
physical event
  -> signed provenance / inspection / milestone
     -> contract and covenant state
        -> borrowing base or draw authorization
           -> collateral/title control
              -> cash instruction and settlement
                 -> journal and reporting
                    -> correction, default and loss
```

For a real industrial project, require:

1. named borrower/SPV and definitive instrument;
2. authoritative project, receivable, inventory or equipment record;
3. lender/collateral-agent recognition and perfected rights;
4. conditions precedent and controlled draw process;
5. identified settlement money and completed cash movement;
6. accounting recognition by borrower and lender;
7. correction/default/enforcement path; and
8. physical delivery or operating outcome.

The current project-finance audit found no named DLT, stablecoin or tokenized-
collateral rail in the six flagship industrial financing stacks reviewed.
Adjacent institutional DLT is not evidence that those projects are financed
through it.

## Transition by layer

| Layer | Current general state | Strong evidence | Missing phase-change evidence |
|---|---|---|---|
| representation | mature in selected markets | DTC, funds, deposits, digital twins | legal uniformity across venues |
| shared execution | moving rapidly | Swift design, Kinexys, Agorá, Canton applications | public production failure handling |
| authoritative securities record | real but bounded | SDX, D7 DLT, Euroclear, DTC participant entitlement | broad multi-jurisdiction title portability |
| tokenized commercial-bank money | production inside bank/defined perimeters | Kinexys/BDA, selected pilots | multi-bank par convertibility and common finality at scale |
| wholesale central-bank money | live pilot / production-bound | Helvetia, Pontes, Samara, Agorá | routine multi-asset production and emergency-liquidity integration |
| collateral eligibility | selectively crossed | Eurosystem rule + EIB/D7/ECMS/Bundesbank | cross-venue use, stressed liquidation and broad eligible set |
| legal finality | case/rule specific | T2 anchor, regulated CSD rules, wCBDC designs | common cross-network/cross-border finality |
| accounting | shared-event potential; recognition remains local | DLT event provenance and existing controlled packages | audited multi-entity transaction-native close and correction at scale |
| failure / resolution | least evidenced | rulebook powers and pilot runbooks | public incident, insolvency, unwind, exit and named loss allocation |

## Net ruling

The deepest DLT change is not asset digitization. Finance was already digital.
It is the attempt to make money, securities, collateral, identity, contract
conditions and transaction evidence executable within shared state.

The transition succeeds only when those shared events connect cleanly to legal
claims, central-bank/commercial-bank balance sheets, collateral law, accounting,
correction and resolution. That is why the final third of the transaction—not
the token mint—is where the Observatory should concentrate.
