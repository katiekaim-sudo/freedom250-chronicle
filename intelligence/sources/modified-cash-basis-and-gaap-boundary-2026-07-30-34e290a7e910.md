# Modified Cash Basis and the GAAP Boundary

Evidence cutoff: 2026-07-30

## Short answer

Cash plus internal accounts-receivable and accounts-payable tracking can be an
excellent operating system for some small or uncomplicated businesses. It is
not, by itself, U.S. GAAP.

If AR and AP are recognized in the statements, the system has already begun to
use accrual accounting. If they are only internal schedules, the statements
remain cash basis and omit economic resources and obligations that external
users may need.

The stronger design is:

> one event ledger, a simple operator interface, and multiple accounting views.

That preserves simplicity without forcing the cash view to answer questions it
cannot answer.

## 1. Five bases that must not be confused

| Basis | Core timing | Typical role | U.S. GAAP? |
|---|---|---|---:|
| cash basis | receipts when received; disbursements when paid | internal books, some tax and special-purpose reporting | no |
| modified cash basis | cash basis plus selected accrual-like adjustments | special-purpose/private reporting | no |
| accrual basis | recognizes effects when economic events occur, subject to GAAP rules | general-purpose business financial reporting | yes, when all applicable GAAP is followed |
| GASB modified accrual | current-financial-resources focus for governmental fund statements | state/local governmental funds | yes in that specific GASB presentation |
| federal budgetary + proprietary accounting | legal budget authority/obligations plus accrual-based financial effects | federal entities | federal GAAP and Treasury architecture |

“Modified cash basis” and “modified accrual” are not synonyms. GASB Statement
34 requires government-wide statements on the economic-resources/accrual basis
and governmental fund statements on the current-financial-resources/modified-
accrual basis, with reconciliation between them.

## 2. Why cash plus AR/AP is powerful—but incomplete

For a service business with little inventory, no external investors, simple
fixed assets and low financing complexity, the operating facts that matter
daily are often:

- bank balances;
- open customer invoices;
- open vendor bills;
- payroll and tax deadlines;
- recurring obligations;
- project or customer profitability; and
- expected cash.

Modern software can make that experience feel like cash accounting. But a
complete external account of financial position and performance may also need:

- inventory and cost of sales;
- prepaid costs and deferred revenue;
- contract assets and contract liabilities;
- fixed assets, depreciation and impairment;
- leases;
- debt, interest and covenants;
- credit-loss allowances;
- contingencies and warranties;
- stock compensation and pensions;
- deferred and uncertain taxes;
- fair-value measurements;
- consolidation and related-party analysis; and
- subsequent events and disclosures.

Once the system adds the modules needed for those objects, it is functionally
building an accrual engine behind a simple interface.

## 3. Six examples that expose the boundary

### Customer pays one year in advance

Cash view:

```text
cash received → income now
```

Accrual view:

```text
cash received → contract liability
service performed over time → revenue
```

The cash receipt is certain; the performance period is the accounting fact.

### December wages paid in January

Cash view records the expense in January. Accrual accounting records December
employee service as a December expense and liability.

### Equipment purchased for cash

Cash view shows a large current disbursement. GAAP ordinarily records an asset
and allocates cost through depreciation, subject to impairment and disposal
rules.

### Sale invoiced before collection

Cash view waits for collection. Accrual recognition depends on performance,
rights and collectibility; the receivable and any credit-loss allowance matter
before cash arrives.

### Inventory purchased and later sold

Cash view follows the purchase payment. Accrual accounting carries inventory
and recognizes cost of goods sold with the related sale, subject to valuation
rules.

### Loan proceeds

Cash increases, but revenue does not. A liability arises. Cash movement alone
does not classify economic meaning.

## 4. What U.S. GAAP currently says

FASB's conceptual framework states that accrual accounting attempts to record
financial effects in the periods in which transactions, other events and
circumstances occur. It provides information about assets, liabilities and
changes in them that cash receipts and outlays alone cannot provide.

The framework is not itself authoritative GAAP, but it explains why a
cash-only reporting model is not a substitute for general-purpose accrual
statements.

For SEC domestic issuers, Regulation S-X and U.S. GAAP apply. SEC staff
guidance says financial statements not prepared in accordance with U.S. GAAP
are presumed inaccurate or misleading for that filing purpose.

The technology has not produced a current FASB project to make modified cash
basis general-purpose GAAP. What is changing is narrower and observable:

- ASU 2023-08 requires qualifying crypto assets to be measured at fair value
  with changes in net income.
- The SEC's SAB 122 rescinded the former safeguarding treatment in SAB 121 and
  directs entities back to applicable contingency guidance for safeguarding
  loss obligations.
- FASB is considering classification of certain digital assets as cash
  equivalents and accounting for transfers of crypto assets. Those
  deliberations were tentative as of the cutoff.
- FASB is researching whether disclosures could replace the statement of cash
  flows for certain entities. That is a live signal of reporting-model
  reconsideration, not adoption of cash-basis GAAP.

## 5. A better simplification proposal

Instead of weakening the external reporting basis, separate the layers:

```text
simple operator actions
  → canonical business events
  → automated subledgers
  → transparent rule engine
  → cash / GAAP / tax / management outputs
```

The user should not need to understand every debit and credit to record an
invoice, receipt, delivery, asset placement or payment. The accounting system
should explain:

- which rule fired;
- which facts it used;
- which journal it generated;
- which estimate or exception required judgment; and
- how a later correction superseded the earlier result.

That is a plausible path to simpler accounting and less hidden manipulation.
It is better described as **event-sourced, multi-view accounting** than
modified cash basis.

## 6. What would have to change in GAAP

Technology alone does not amend GAAP. FASB uses a due-process path: identify an
issue, add a project, deliberate publicly, expose proposed amendments for
comment, redeliberate and issue an Accounting Standards Update.

A major technology-driven GAAP change would therefore require evidence that
current recognition, measurement, presentation or disclosure produces
pervasive user problems—not merely that a new ledger can execute entries more
efficiently.

The most plausible standard-setting pressure points are:

- digital-asset classification, custody and transfer;
- settlement and cash-equivalent definitions;
- machine-readable and more disaggregated disclosures;
- treatment of programmable or contingent rights;
- continuous or event-level reporting;
- control and audit evidence for automated systems; and
- private-company simplifications where user benefit does not justify cost.

The least plausible near-term change is abandonment of accrual information
about assets, liabilities and performance.
