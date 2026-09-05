# Accounting Functions and Smart-Contract Automation Map

Evidence cutoff: 2026-07-30

## Ruling

Double-entry bookkeeping and blockchain solve different problems.

- Double entry represents the effect of an event on an entity's accounts and
  forces debits and credits to balance.
- A shared or distributed ledger can make multiple parties rely on one
  time-ordered, signed record of state changes.
- A smart contract can execute a specified rule when specified inputs arrive.

The technical opportunity is to put them in layers:

```text
real-world event and evidence
  → signed canonical event
  → authorization and control checks
  → versioned recognition / measurement rules
  → derived journals and subledgers
  → cash, GAAP, tax, regulatory and management views
  → disclosures, assurance, correction and recovery
```

The shared event is not a third debit or credit. “Triple-entry accounting” is
useful shorthand for a mutually verifiable receipt, but the external receipt
does not replace the entity-level double-entry representation.

## 1. What accounting actually does

Accounting is not one function. It is a stack of operational, legal,
measurement, control and communication functions.

| Function | Question answered | Automatable from reliable events? | Irreducible or off-chain issue |
|---|---|---:|---|
| entity and perimeter | Whose assets, liabilities and activity are reported? | partly | control, beneficial ownership, VIEs, agents, related parties |
| identity | Which legal person or account acted? | strongly | stolen credentials, nominees, beneficial owner |
| authority | Was the transaction permitted? | strongly | validity of law/contract, delegation, collusion |
| occurrence / existence | Did the event or asset exist? | partly | physical delivery, service performance, inventory existence |
| rights and obligations | Who owns the asset or owes the duty? | partly | title, side agreements, liens, legal interpretation |
| classification | What kind of economic event is it? | strongly when facts are complete | novel instruments, substance over form |
| recognition | When does it enter the accounts? | partly | performance obligations, contingencies, control transfer |
| measurement | At what amount? | mixed | fair value, impairment, useful life, probability, model inputs |
| allocation | Which period, product, award or program bears the cost? | strongly for fixed rules | causal allocation and policy choices |
| settlement | When and how did money or an asset move? | strongly | off-chain bank finality, reversals, custody perimeter |
| internal control | Who approved, segregated and reviewed it? | strongly | override, coercion, shared keys, corrupt approvals |
| reconciliation | Do subledgers, banks and counterparties agree? | strongly | missing or unreliable source systems |
| close and consolidation | What adjustments and eliminations produce the reporting entity? | partly | estimates, intercompany perimeter, late information |
| reporting and disclosure | What must users be told? | strongly after judgments | materiality, aggregation, narrative context |
| assurance | Is evidence sufficient and appropriate? | partly | source reliability, physical facts, estimates, professional judgment |
| correction and recovery | How is an error, reversal, restatement or collection preserved? | strongly | legal cause, responsibility, collectibility |

The closer a function is to **identity, authorization, arithmetic, sequencing
and reconciliation**, the more programmable it is. The closer it is to
**economic substance, legal rights, uncertain measurement and materiality**,
the more judgment remains.

## 2. Operating-cycle map

### Order to cash

```text
customer / credit approval
  → order
  → delivery or service performance
  → invoice
  → receivable
  → collection
  → refund / dispute / credit loss
```

Smart contracts can verify approved customers, match orders to delivery
receipts, issue invoices, age receivables, apply cash and enforce discounts.
They cannot know that a service was genuinely performed unless a trustworthy
person, device or external system supplies that fact. They also cannot remove
the need to estimate collectibility or interpret multi-part performance
obligations.

### Procure to pay

```text
requisition
  → budget / authority check
  → purchase order
  → receipt
  → vendor invoice
  → three-way match
  → payable
  → payment
  → return / recovery
```

This is one of the strongest automation candidates. A signed purchase order,
receipt and invoice can form the payable and release payment only after
required approvals. The residual risks are false vendors, collusive approvals,
false receipt/performance evidence, change-order manipulation and compromised
oracle or identity systems.

### Payroll

Identity, employment status, approved time, rate, withholding, benefits and
bank instructions can be joined into a reproducible payroll event. Judgment
and law remain around worker classification, incentive accruals, equity
compensation, pension obligations and disputes.

### Inventory and cost of sales

Provenance, custody transfers, lot identity and counts can be recorded as
events. Accounting still must determine cost-flow assumptions, overhead
allocation, net realizable value, obsolescence and whether physical inventory
matches the digital record.

### Long-lived assets

Acquisition, location, custody, maintenance and disposal can be tracked.
Capitalization, useful life, componentization, impairment and residual value
remain accounting judgments. A cash purchase is not automatically a current
expense.

### Treasury, debt and equity

Cash movements, debt service, collateral calls and cap-table changes can be
automated. Classification as debt or equity, embedded features, covenant
interpretation, hedge accounting, control of digital assets and fair-value
inputs remain complex.

### Tax

An event log can produce a tax view from separate rules. Tax basis is not the
same as book basis; timing differences, uncertain tax positions,
jurisdictional allocation and changes in law still require distinct logic and
judgment.

### Consolidation and close

Shared identifiers can make intercompany matching, eliminations,
foreign-currency translation and cut-off testing faster. They do not decide
which entities must be consolidated or whether an arrangement transfers
control in substance.

## 3. The event-sourced accounting model

The most useful accounting primitive is not a manual journal entry. It is a
business event with provenance.

### Minimum event object

```yaml
event_id:
event_type:
event_time:
recorded_time:
legal_entities:
counterparties:
economic_object:
quantity:
currency_and_amount:
contract_or_authority:
performance_or_receipt_evidence:
cash_or_asset_settlement_reference:
approvals_and_signatures:
source_systems:
rule_version:
privacy_class:
parent_and_causal_events:
supersedes_or_reverses:
supporting_evidence_hashes:
```

Rules then produce views:

```text
canonical event log
  ├─ cash receipts and disbursements
  ├─ U.S. GAAP accrual journals
  ├─ tax-basis books
  ├─ regulatory capital / prudential reports
  ├─ managerial product and project costing
  └─ federal budgetary and proprietary accounting
```

This is simpler at the user interface even when the rule system remains
sophisticated. A small operator can record “delivered,” “invoiced,” “paid” or
“equipment placed in service.” The system can derive the appropriate journals,
provided the facts, rules and entity context are complete.

### Judgment as a first-class object

The design should not hide estimates inside an unexplained adjusting entry.
It should record:

```yaml
judgment_id:
subject:
accounting_question:
authoritative_rule:
inputs:
assumptions:
method:
range:
selected_amount:
approver:
effective_period:
review_date:
supersedes:
```

That does not remove judgment. It makes its author, rule, inputs, clock and
revision history visible.

## 4. What happens to the “accounting games”

### Games this architecture can constrain

- backdated or silently overwritten entries;
- duplicate invoices and payments;
- orphan journal entries;
- missing approval or segregation-of-duties evidence;
- unreconciled intercompany balances;
- inconsistent versions of the same transaction;
- hidden post-close changes;
- weak lineage between disclosure totals and source events.

### Games it does not inherently stop

- recording a false delivery or performance event;
- channel stuffing and side agreements;
- manipulating useful lives, reserves, probabilities or valuations;
- concealing related parties or controlling interests;
- structuring transactions to achieve a desired classification;
- corrupt approvals or shared private keys;
- controlling the oracle, administrator, upgrade key or permission set;
- keeping material activity outside the ledger.

The games therefore move:

> from arithmetic and reconciliation toward classification, perimeter,
> assumptions, oracle truth and governance.

That is still progress. It narrows the contest and makes many interventions
traceable. It is not an automatic end to manipulation.

## 5. What current standards and systems already show

- FASB's conceptual framework says accrual accounting records financial effects
  in the periods in which transactions and other events occur and supplies
  asset, liability and performance information not available from cash
  receipts and outlays alone.
- SEC Inline XBRL already makes public-company statements and notes both human-
  and machine-readable. It is a reporting taxonomy, not a transaction ledger.
- Treasury's USSGL supplies a uniform federal chart of accounts and transaction
  guidance.
- Treasury's Governmentwide Spending Data Model supplies authoritative terms,
  structures and validation rules for federal spending submissions.
- Treasury's grant-blockchain proof of concept reported improved
  prime-to-subrecipient visibility, less reporting and possible control gains,
  but did not process real payments and identified legal, governance,
  infrastructure and legacy-system barriers.
- The JFMIP multi-agency follow-up found potential value in real-time shared
  data, reduced reconciliation and auditor read-only nodes while stressing
  cybersecurity, authority-to-operate, coordination and existing assurance
  requirements.

## 6. Bottom line

The revolutionary change is not a new debit-credit rule. It is the possible
separation of:

1. the **event**;
2. the **rule applied to the event**;
3. the **judgment added by a responsible party**; and
4. the **view produced for a particular user**.

If those layers become reproducible and inspectable, accounting can become
easier to operate without pretending that economic substance is simple.
