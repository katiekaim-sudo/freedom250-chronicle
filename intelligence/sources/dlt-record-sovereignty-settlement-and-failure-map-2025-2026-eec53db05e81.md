> Source evidence cutoff: 2026-08-31T12:08:12-04:00

# DLT Record Sovereignty, Settlement and Failure Map, 2025–2026

## Controlling question

When several ledgers, books and legal systems describe the same transaction,
which one has the power to make the change operative?

DLT research fails when “the blockchain record” is treated as a universal fact.
One transaction may have distinct authoritative records for the legal claim,
participant entitlement, beneficial ownership, settlement money, collateral,
accounting and regulatory reporting.

## The record-sovereignty stack

| Record | What it answers | Possible authoritative owner | DLT transition question |
|---|---|---|---|
| instrument / issuer record | What obligation or security exists? | issuer, registrar, transfer agent, statute, contract | Is the token itself the issued object or a representation of one? |
| registered ownership | Who is recognized directly by issuer/property law? | issuer register, CSD nominee, land/company registry | Does an on-chain transfer change registered title or only an intermediated entitlement? |
| participant entitlement | What does an intermediary owe its participant? | CSD/custodian/bank books and governing law | Is the DLT entry itself the operative entitlement, or reconciled to another conclusive book? |
| beneficial / customer record | Which customer has economic rights? | broker, custodian, fund administrator, bank | Can the network see the customer, or only a participant wallet? |
| cash liability | Who owes the money? | central bank, commercial bank, stablecoin issuer, settlement institution | Is the token a direct claim, an omnibus-backed representation or a redemption claim? |
| collateral record | Which asset secures which obligation? | collateral agent, CCP, triparty, lender, registry | Has the asset merely moved, or has a valid lien/pledge and eligible value been created? |
| accounting record | When and how is the event recognized? | each legal entity's controlled books | Does shared event data flow into consistent journals without becoming one universal accounting truth? |
| supervisory / legal record | What is enforceable under stress? | regulator, court, resolution authority, operator rules | Which record prevails after insolvency, freeze, fork or mismatch? |

## Three archetypes

### A. DLT as representation beside an incumbent conclusive record

DTC is the clearest case. DTC-tokenized assets can move between participant
wallets, but the underlying security remains held within DTC's indirect-holding
constitution. DTC controls eligible networks, wallet registration,
reconciliation and administrative adjustment; the legal relationship among DTC,
participants, issuer and beneficial owner does not change merely because the
entitlement is tokenized.

This is genuine participant-level state migration inside retained record
sovereignty.

### B. DLT as regulated CSD / issuance record

SDX and D7 DLT show the stronger form. A regulated CSD can make the DLT record
part of issuance, custody, settlement and lifecycle servicing. The old
institutional role has not disappeared; its authoritative record has migrated
into a DLT architecture governed by the CSD and applicable law.

### C. DLT as shared orchestration over separate authorities

Swift and many interoperability systems record commitments, validations and
conditions without becoming the issuer of the money or owner of final
settlement. The shared ledger can determine that participating processes agree
to proceed, but the banks' asset, funding and RTGS/correspondent records remain
decisive for cash discharge.

## Settlement is a vector, not one timestamp

Record at least these clocks:

| Clock | Exact event |
|---|---|
| instruction | payer, trader or smart contract submitted an instruction |
| acceptance | operator or counterparty accepted it under rules |
| technical execution | ledger validators recorded or conditionally linked the state change |
| title / entitlement | authoritative asset record changed |
| cash | identified settlement money was debited and credited |
| legal finality | governing law/rules made the transfer irrevocable against ordinary unwind and insolvency |
| accounting close | parties recognized, reconciled and closed the event |
| outcome | beneficiary had usable value or the project/economic state changed |

“Instant,” “atomic” and “settled” must name the clock.

## Strong finality cases and boundaries

### Pontes

Hash-linked coordination can condition the asset and cash legs, but the
Eurosystem's initial legal cash finality attaches when T2 completes the cash leg.
The intended later phase would move settlement finality to an Eurosystem DLT
platform. Those are separate legal states, not implementation details.

### Helvetia / SDX

Same-ledger delivery-versus-payment using SNB wholesale CBDC gives a strong
technical and legal alignment: the cash token represents an SNB sight-deposit
liability and the digital security settles in the regulated SDX environment.
The pilot boundary and absence of public failure data still matter.

### Agorá

The prototype recorded real tokenized reserves and deposits, but funding and
redemption linked back to RTGS and bank core systems. The test's runbook,
approval and reconciliation chain is part of the constitution, not background
administration.

### DTC

A tokenized entitlement transfer is not the whole DTC settlement cycle. At the
first service phase, tokens receive no DTC settlement value and must return to
traditional form for the ordinary end-of-day settlement process. A repo or DvP
workflow shown with tokenized assets therefore does not prove that DTC processed
the final cash leg digitally.

## The failure constitution

### Pre-finality states

```text
invalid instruction
  -> compliance or identity hold
     -> insufficient asset or funding
        -> failed condition / timeout
           -> cancellation before title/cash
              -> one-leg technical movement requiring repair
```

Evidence required:

- who detects the condition;
- whether an automated timeout or human operator acts;
- what state is locked and for how long;
- whether a compensating or reversing transaction is allowed;
- which ledger records the authoritative failure; and
- who funds a liquidity gap.

### Post-finality states

Finality does not end every remedy. A final transfer may be followed by:

- fraud recovery or voluntary return;
- court-ordered transfer or freeze;
- operator administrative correction;
- insurance/guarantee payment;
- accounting restatement;
- participant default assessment;
- resolution/insolvency claim; or
- compensating payment.

These do not necessarily reverse final settlement. They may create a new legal
and accounting event.

### DLT-specific failure modes

| Failure | What can diverge | Required public proof |
|---|---|---|
| fork / probabilistic reorganization | technical ledger history versus legal finality | conclusive branch, operator/legal rule and loss treatment |
| validator or sequencer outage | participant instructions versus committed state | outage clock, safe state, recovery point and duplicate prevention |
| bridge/oracle failure | source-ledger fact versus destination execution | oracle authority, retry/cancel logic, dispute and compensation |
| smart-contract defect | intended obligation versus code result | pause/upgrade power, affected records, correction and liability |
| key or wallet compromise | apparent authorized transfer versus customer/participant intent | key governance, freeze, rekey, return and claimant protection |
| on/off-chain mismatch | token total versus CSD/bank/core total | reconciliation frequency, conclusive book and admin correction |
| liquidity-clock gap | 24/7 obligation versus closed RTGS/collateral venue | prefunding, credit line, fallback settlement and loss allocation |
| participant insolvency | locked assets/cash versus estate rights | segregation, netting, close-out, porting and resolution authority |

CPMI/IOSCO's stablecoin guidance makes the general point explicit: technical
settlement can diverge from legal finality, especially under forks, and a
systemically important arrangement needs clear finality and a mechanism for
losses created by reversal or misalignment.
[CPMI/IOSCO](https://www.bis.org/cpmi/publ/d198.pdf)

## Correction powers are constitutional powers

Immutability should never be used as shorthand for “cannot be corrected.” A
regulated financial system may need to:

- reject an invalid event before execution;
- suspend a participant or asset;
- freeze a wallet or position;
- reverse an erroneous technical state where rules permit;
- create a compensating transfer after finality;
- restate books without deleting historical evidence;
- remap keys or ownership after compromise;
- reconcile a token supply to an issuer/CSD total; and
- allocate loss when the records cannot all be made whole.

The design question is whether those powers are explicit, governed, auditable
and appealable—not whether the system pretends they do not exist.

## Exit is part of finality

An institutional rail is incomplete until a participant or asset can leave.
Track:

1. redemption or detokenization at par / equivalent entitlement;
2. transfer to another wallet, custodian, CSD or bank;
3. portability of transaction and identity records;
4. treatment of pending obligations and locked collateral;
5. key revocation and residual access;
6. accounting close and regulatory reporting; and
7. insolvency or operator-wind-down treatment.

No reviewed cross-system package publicly proves this full exit chain under
stress.

## First-failure research template

```yaml
economic_object:
legal_claim_and_issuer:
participants_and_accounts:
technical_ledgers:
authoritative_asset_record:
authoritative_cash_record:
instruction_time:
technical_execution_time:
title_time:
cash_time:
legal_finality_rule_and_time:
failure_or_divergence:
pause_freeze_reverse_or_compensate_power:
liquidity_source_during_gap:
accounting_correction:
loss_bearer:
court_regulator_or_resolution_action:
exit_or_recovery_outcome:
evidence_state: confirmed | partial | not_public | hypothesis
```

## Net ruling

The DLT transition becomes constitutionally real when the ledger does more than
describe an intended transfer. It must be connected to a governing issuer,
authoritative record, settlement asset, finality rule, correction power,
liquidity source and named loss bearer.

The system's deepest power resides where a mismatch is resolved. The next major
research event is therefore not another successful demo. It is the first public
case showing which record won, who corrected it, and whose balance sheet paid.
