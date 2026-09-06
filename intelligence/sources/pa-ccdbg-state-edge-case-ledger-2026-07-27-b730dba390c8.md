# Pennsylvania CCDBG State-Edge Case Ledger

Completed: 2026-07-27  
Status: current Workbench answer  
Evidence cutoff: 2026-07-27  
Case ID: `PA-CCDBG-2501PACCDD-2025-04-17`

## Short answer

The April 17, 2025 public payment can be joined to a real Pennsylvania CCDBG
assistance award. Pennsylvania's own published operating materials then show a
substantial internal accounting trail:

```text
PELICAN allocation
  → provider attendance and invoice
  → PELICAN invoice ID
  → PELICAN payment ID
  → payment / return / reissue / adjustment / recoupment states
  → SAP line, internal order, fund, cost center, general-ledger and federal-program coding
  → fiscal reconciliation
  → ACF-696 aggregate reporting
```

But the public materials do not expose the join from the federal payment to a
specific Pennsylvania receipt, SAP journal or PELICAN allocation. The missing
public proof is therefore a **cross-system identifier and reconciliation
problem**, not proof that Pennsylvania lacks downstream records.

## 1. Federal case fingerprint

| Field | Observed value | What it proves |
|---|---|---|
| FAIN | `2501PACCDD` | Award identifier shared by the public payment row and federal award record. |
| Public payment date | 2025-04-17 | Date reported by the Defend the Spend public feed. It is not independently proved here as State receipt or bank settlement. |
| Public payment amount | `$37,065,525.14` | Amount reported by the public feed. |
| Recipient label | `PA ST DEPARTMENT OF PUBLIC WELFARE` | Public-feed recipient label. |
| Recipient UEI | `FYVAZVJGDFA4` | Federal recipient identity on the USAspending award object. |
| Assistance Listing | `93.575` | Child Care and Development Block Grant. |
| Federal account | `075-1515` | AID plus main account exposed by USAspending. It is not the award-specific full TAS. |
| Award signed | 2024-10-16 | Award-action clock; not the April cash-payment clock. |
| Award period | 2024-10-01 through 2027-09-30 | Performance period, not proof of expenditure. |
| DOGE award ID | `ASST_NON_2501PACCDD_7590` | Program Support Center/public-feed identifier. |
| USAspending award ID | `ASST_NON_2501PACCDD_075` | USAspending canonical award identifier. |

Federal source chain: the incorporated
`FEDERAL_TRANSACTION_RECORD_DEEP_DIVE_2026-07-23.md`, based on the official
Defend the Spend and USAspending APIs. This pilot preserves that verified seed
and tests only the State edge.

Current verification on July 27, 2026 adds:

- four USAspending/FABS obligation actions — `$52,558,049` on 2024-10-16,
  `$63,093,420` on 2025-01-13, `$112,735,924` on 2025-05-22 and `$43,240,580`
  on 2025-07-01 — sum to the award's `$271,627,973` obligation;
- those are assistance-award obligation actions, not the April 17 cash event;
- the current USAspending award object reports `$265,051,096.62` in cumulative
  award-level File C outlay state, but no File C row equals the April payment;
  monthly/cumulative award-account reporting is not a settlement trace; and
- `075-1515` is the federal-account grouping. The exact award/payment TAS,
  period-of-availability and subaccount remain unproved.

### 1.1 Live public-data contradictions

The same verified case also contains four public-data defects:

1. Defend the Spend uses award ID suffix `_7590`; USAspending canonicalizes the
   same FAIN to suffix `_075`. Alias resolution works, but neither payload
   publishes the alias rule.
2. Defend the Spend labels the recipient `PA ST DEPARTMENT OF PUBLIC WELFARE`;
   the USAspending/SAM-derived record uses `PA DEPARTMENT OF HUMAN SERVICES`.
3. The Defend the Spend agency-lead justification calls the expense consistent
   with a **Head Start** grant. The award, FAIN description and Assistance
   Listing identify CCDBG `93.575`; Head Start is `93.600`.
4. The OpenAPI example presents an ISO date, while live payment rows use
   `MM/DD/YYYY`.

These defects do not disprove the payment row. They show why FAIN, typed
identifiers, controlled program codes and validation rules matter more than a
free-text label.

## 2. What Pennsylvania's own documents establish

### 2.1 The State describes the operating chain

The current FFY 2025–2027 Pennsylvania CCDF State Plan says:

- State and federal funding is provided to ELRCs through an allocation in
  PELICAN Child Care Works;
- after month-end, providers report attendance and invoice the regional ELRC
  for the previous month's services;
- PELICAN CCW information is interfaced with SAP, the Commonwealth accounting
  system; and
- the federal ACF-696 report is prepared using grant and expenditure coding
  available in SAP.

Locator: `PA_CCDF_STATE_PLAN_FFY_2025_2027.pdf`, PDF p. 199.

This establishes the **generic operating route**. It does not prove that the
April 17 federal payment followed a particular SAP line or funded a particular
provider invoice.

### 2.2 PELICAN carries accounting bridge fields

The official PELICAN Reports Manual's RE107 Cost Function Report identifies:

- SAP line number;
- invoice number;
- internal order;
- county;
- fund;
- cost center;
- general ledger;
- CFDA number;
- amount; and
- apply-start date.

The manual describes internal order, fund, cost center and general ledger as
numbers used to track payments or expenditures by funding stream,
program/office and grant type. It describes the SAP line number as the unique
identifier for each line of fund coding needed by the Commonwealth accounting
system.

Locator: `PA_PELICAN_REPORTS_MANUAL_SECTION_600.pdf`, PDF p. 11.

This is the strongest public evidence that an internal PELICAN-to-SAP
reconciliation key exists. The public document is a report specification, not
the current interface mapping or a 2025 transaction extract.

### 2.3 Provider-level lineage is more detailed than a monthly total

The same manual defines records for:

- PELICAN-generated invoice ID;
- PELICAN-generated payment ID;
- check number;
- service period;
- payment amount and issue status;
- returned payment date, reason, amount and remaining balance;
- original invoice ID;
- adjustment amount; and
- recoupment amount and date.

It also preserves invoice-status progression including `Need Invoice`,
`Have Invoice`, `Calculated`, `Authorized`, `Payment Requested`, `Paid`, and
`Paid Pending Adjustment`.

Locators: manual PDF pp. 104–107.

Those are distinct state transitions. In particular:

```text
authorized ≠ payment requested ≠ paid ≠ paid pending adjustment
returned ≠ recouped ≠ collected recovery
service period ≠ invoice period ≠ payment date ≠ adjustment date
```

### 2.4 The reconciliation logic is explicit

RE415, the Payment Activity by Service Period Report, lists payments and
processed adjustments for a provider and is designed for fiscal reconciliation.
The manual says an office can match its general ledger to the original payment
and subsequent payments caused by positive adjustments. Its example separates:

- March service;
- April invoice processing and payment; and
- a May adjustment paid against the March service period.

It warns that one Payment ID may include more than one invoice.

Locator: manual PDF p. 120.

RE417 is designed to reconcile provider payments with year-to-date child-care
expenditures by funding program and allows provider-level detail. Its totals
match RE703, used for monthly reconciliation.

Locator: manual PDF p. 122.

### 2.5 The State monitors pending and available-fund states

The ELRC Operations Monitoring Tool guide instructs program representatives to
use the live PELICAN CCW invoice-search surface, Report 704 and Report 403 to
review payment timeliness, including pending invoices over 60 days. It also
uses PELICAN reports for obligated and available funds.

Locator: `PA_ELRC_OPERATIONS_MONITORING_TOOL_GUIDE_FY_2021_2022.pdf`, PDF
pp. 14 and 48–50.

This proves that invoice status and available/obligated funding are monitored
as separate operational states. The guide is historical operating
documentation; current layouts and retention rules still need confirmation.

## 3. The proof boundary

### Publicly proved

```text
FAIN 2501PACCDD
  → federal award identity
  → April 17, 2025 public payment row for $37,065,525.14

Pennsylvania program design
  → PELICAN allocation
  → provider attendance/invoice
  → PELICAN payment and correction fields
  → PELICAN/SAP coding interface
  → fiscal reconciliation
  → ACF-696 aggregate report
```

### Not publicly joined

```text
April 17 payment
  ╳ exact PMS draw request / subaccount
  ╳ Treasury schedule, trace and settlement
  ╳ Pennsylvania receipt date and cash-account entry
  ╳ SAP document / journal / internal order
  ╳ PELICAN allocation batch
  ╳ ELRC allocation
  ╳ provider invoice and payment IDs
  ╳ later adjustment, recoupment, receivable or collected recovery
  ╳ corresponding ACF-696 line and reporting period
```

No assertion should jump across a `╳`.

## 4. What the accounting problem actually is

The trace breaks for several independent reasons:

1. **Authority changes.** The award, draw, Treasury settlement, State book
   entry, provider payment, federal expenditure report and recovery are
   authoritative in different systems.
2. **Identifiers change.** FAIN survives on the federal side, while the
   published State specifications expose SAP line, internal order, invoice and
   payment IDs without showing a public FAIN-to-State crosswalk.
3. **Money may be pooled.** A federal draw can support a program funding pool.
   A public one-dollar-to-one-provider claim requires an allocation rule or
   transaction bridge; it cannot be assumed.
4. **Clocks differ.** Service, invoice, authorization, payment, return,
   adjustment, reporting and recovery can occur in different months.
5. **Corrections have different effects.** A negative or revised entry may
   change obligation, cash, accounting classification, recipient entitlement,
   public disclosure, receivable or collection — or only some of them.
6. **Public feeds are derivative.** They can expose a useful assertion while
   omitting the authoritative journal, settlement record or downstream
   reconciliation.

This is why a public blockchain alone would not solve the case. The first
requirement is a legally required event and identifier constitution across the
systems that already control the money.

## 5. Correction firewall

Every correction event in the pilot must answer all seven questions:

| Dimension | Required question |
|---|---|
| Legal obligation | Did the amount the government is legally obligated to provide change? |
| Cash | Did cash move, reverse, refund or offset? |
| Accounting classification | Was the same cost moved between grants, funds, periods or programs? |
| Recipient entitlement | Did the provider or recipient's entitlement change? |
| Public disclosure | Did only the published representation change? |
| Receivable | Was a debt or receivable created? |
| Collection | Was the receivable actually collected? |

The Georgia May 8, 2025 CCDF case in the incorporated deep dive remains the
control example: a negative discretionary-stream entry and two positive
matching-stream entries described a funding-stream reallocation. The public
rows did not, by themselves, prove a fraud recovery, zero-sum cash reversal or
collected debt.

A negative amount is not necessarily returned cash.

## 6. Questions this pilot raises

1. Does Pennsylvania retain FAIN, PMS account/subaccount, Treasury schedule,
   ALC or other federal settlement identifiers in SAP?
2. Which SAP field maps to the PELICAN `SAP Line Number`, and is that mapping
   versioned?
3. Can a current RE107/RE415/RE417/RE703 extract be joined to SAP document
   number and ACF-696 grant/expenditure coding without creating a new record?
4. Is the April 17 draw treated as an advance into a pooled cash position or as
   reimbursement for already incurred expenditure?
5. What allocation method assigns pooled federal and State funding to ELRC and
   provider expenditures?
6. Which system is authoritative when PELICAN invoice/payment status differs
   from SAP cash or general-ledger status?
7. How do returns, reissues, positive and negative adjustments, recoupments,
   offsets, receivables and collections propagate into SAP and ACF-696?
8. Are historical interface mappings and correction histories retained after
   system changes?
9. Can masked transaction bridges be disclosed without child, household,
   provider-bank or security-sensitive data?
10. Who acknowledges that a correction propagated through every downstream
    public and authoritative record?

### 6.1 Banking-layer update

The companion
`PA_CCDBG_EXISTING_SETTLEMENT_CROSSWALK_AND_BANKING_MAP_2026-07-27.md`
now narrows several of these questions:

- Pennsylvania's FY2025 Treasury-State Agreement names **Wells Fargo** as the
  CMIA fiscal agent for CCDBG Assistance Listing `93.575`.
- The agreement assigns 96% of the local-agency/vendor/operating component to
  **Reimbursement** and 4% to **Payroll**. Exact classification of the April 17
  payment still requires the PMS request and State draw support.
- Pennsylvania BAFM must retain a Report of Drawdowns Processed by Funding
  Source and the federal draw-system confirmation.
- Pennsylvania's cash directive requires bank/SAP reconciliation and a central
  file of approved agency bank accounts, but the CCDBG receiving-account class
  is not publicly identified.
- The latest publicly listed ELRC audit guide says grant funds must be held in
  an interest-bearing account, permits co-mingling if interest is properly
  credited, and expressly contemplates temporary use of any available funding
  source followed by later OCDEL accounting after final recaps.

The remaining problem is therefore a transaction-specific reconciliation
problem, not an unresearched generic settlement-rail problem.

## 7. Smallest useful public proof layer

A workable public layer does not need to expose protected operational records.
For each event it needs:

- durable event and object IDs;
- authoritative system and actor;
- the identifiers asserted at that stage;
- amount and amount state;
- separate event clocks;
- predecessor, successor, reversal and supersession relationships;
- evidence locator or hash;
- correction-effect booleans;
- disclosure/protection state; and
- explicit unresolved joins.

The pilot schema and registry implement that minimum. They are a factual test
instrument, not evidence that any proposed public system has been adopted.
