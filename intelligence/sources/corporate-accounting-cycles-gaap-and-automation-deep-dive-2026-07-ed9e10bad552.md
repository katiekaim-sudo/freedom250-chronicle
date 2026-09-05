# Corporate Accounting Cycles, GAAP, and Automation Deep Dive

**Research date:** 2026-07-30  
**Scope:** Nongovernmental U.S. corporate accounting. Primary sources only: FASB, SEC, PCAOB, and IRS where tax-basis accounting must be distinguished from financial reporting.  
**Status convention:** “Current GAAP” means the FASB Accounting Standards Codification as amended by effective guidance. FASB Concepts Statements are explicitly nonauthoritative. Proposed ASUs, research projects, and tentative Board decisions are identified separately and do not change current GAAP.

## Executive finding

Blockchain and smart-contract systems can radically change the **bookkeeping, evidence, control, reconciliation, and reporting machinery** of accounting without eliminating the **recognition, measurement, presentation, and disclosure judgments** that U.S. GAAP exists to govern.

The most useful distinction is:

1. **Business-event layer:** what happened, to whom, under what authority, when, with what asset or obligation, and with what counterparty evidence.
2. **Accounting-policy layer:** which reporting rule transforms that event into recognized assets, liabilities, revenue, expense, equity, tax, and disclosures.
3. **Judgment layer:** estimates, classifications, forecasts, legal interpretations, control determinations, materiality, and management assumptions.
4. **Assurance layer:** evidence that the event population is complete, the data reliable, the rules correctly applied, judgments supportable, controls effective, and reports not materially misstated.

A signed, append-only event record can make layer 1 far more complete and layers 2–4 more inspectable. It cannot make layers 2–4 disappear.

This follows directly from the FASB’s conceptual description of accrual accounting: accrual accounting depicts economic effects in the periods in which they occur even when cash receipts and payments occur in another period. Cash-only information is therefore not a substitute for GAAP financial performance. The SEC likewise requires public-company records and controls sufficient to prepare GAAP financial statements, while PCAOB standards continue to require sufficient appropriate audit evidence and specific work over subjective estimates.

The practical opportunity is not “replace double-entry with blockchain.” It is:

> **Replace fragmented journals and reconciliations with a common, signed event record; preserve double-entry as one deterministic projection of those events; and make policy, judgment, override, correction, and assurance metadata inspectable.**

The often-used label “triple-entry accounting” should therefore be handled carefully. A counterparty-signed shared receipt can be a powerful third evidence object, but it is not a third balancing side added to debit and credit. The accounting equation and double-entry projection remain; the shared receipt improves agreement, provenance, and assurance.

## 1. What is actually automatable

### A. Deterministic functions — high automation potential

- identity and authorization checks;
- timestamping and sequence;
- order, invoice, receipt, shipment, payroll, custody, and settlement state changes;
- three-way match and exception routing;
- arithmetic, allocation formulas, interest schedules, and depreciation schedules once assumptions are approved;
- subledger-to-general-ledger posting;
- intercompany matching and routine eliminations;
- bank, custodian, and on-chain reconciliation;
- covenant and threshold alerts;
- evidence attachment, signature verification, and version history;
- XBRL tagging and report assembly;
- population-wide exception analytics;
- append-only correction through reversal and supersession rather than silent overwrite.

### B. Rules that can be encoded but still require governance

- revenue allocation and recognition schedules after contract interpretation;
- expense versus capitalization rules after the unit of account and asset conclusion are approved;
- cost-flow and overhead-allocation rules;
- lease amortization;
- tax-rate application and jurisdictional mapping;
- foreign-currency translation;
- debt amortization and selected hedge-accounting calculations;
- consolidation eliminations after the reporting-entity boundary is decided;
- disclosure thresholds;
- close checklists and certification routing.

Encoding these rules does not make them self-validating. Someone must control the rule version, effective date, exception authority, data source, and upgrade process.

### C. Judgment-intensive functions — technology can support, not decide autonomously

- identifying contract terms, side agreements, enforceable rights, and performance obligations;
- principal-versus-agent and control determinations;
- variable consideration and returns;
- collectibility and expected credit losses;
- asset-versus-expense classification and the unit of account;
- useful lives, residual values, impairment triggers, and forecast cash flows;
- inventory obsolescence and net realizable value;
- fair value when markets or inputs are unobservable;
- litigation, warranty, restructuring, environmental, and other contingencies;
- debt-versus-equity and embedded-derivative analysis;
- hedge designation, forecast probability, and effectiveness judgments;
- pension and other actuarial assumptions;
- deferred-tax realization and uncertain tax positions;
- voting-interest, variable-interest-entity, and de facto control analysis;
- functional currency, segment identification, going concern, subsequent events, and materiality;
- whether an oracle proves the real-world condition the code claims it proves.

## 2. Operating-cycle map

## Order to cash

### Canonical events

Customer identity and authority → contract accepted → performance obligations/rights mapped → goods shipped or service milestones completed → customer acceptance/return window → invoice/contract asset → cash receipt → refund, credit memo, write-off, or recovery.

### What an event-sourced or smart-contract system can automate

- preserve the executed contract, amendments, approvals, signatures, and side-letter references;
- issue a persistent contract and performance-obligation ID;
- obtain signed delivery, acceptance, usage, or milestone attestations;
- trigger billing or escrow release when approved conditions are met;
- post receivable, contract asset/liability, revenue schedule, cash receipt, refund, and sales-tax entries;
- reconcile processor, bank, custodian, and general-ledger records;
- maintain a complete chronology of contract modifications, credits, returns, and collections;
- surface cut-off exceptions and transactions with missing external evidence.

### What GAAP still requires

Topic 606 is not a cash-receipt rule. It requires analysis of the contract, promised goods and services, performance obligations, transaction price, allocation, and satisfaction of obligations. Judgment remains in:

- whether a contract exists and rights are enforceable;
- whether promises are distinct performance obligations;
- whether the entity is principal or agent;
- estimation and constraint of variable consideration;
- material rights, options, warranties, returns, bill-and-hold, consignment, and contract modifications;
- whether control transferred over time or at a point in time;
- collectibility and the expected-credit-loss allowance on receivables and contract assets.

Topic 326 expressly requires expected credit losses based on historical experience, current conditions, and reasonable and supportable forecasts; the FASB does not prescribe one method and acknowledges judgment.

### Residual manipulation surface

Shared, signed delivery and acceptance records can narrow fictitious sales and period-end cut-off games. Manipulation can migrate to contract drafting, undisclosed side concessions, control of the acceptance oracle, related-party customers, estimates of returns or rebates, and collectibility assumptions.

**Primary authority:** [FASB Topic 606 project summary](https://fasb.org/projects/recently-completed-projects/revenue-recognition-summary); [FASB Topic 326 project summary](https://fasb.org/projects/recently-completed-projects/accounting-standards-update-2016-13-financial-instrument-credit-losses); [FASB ASU 2025-05 on current Topic 606 receivables and contract assets](https://fasb.org/page/PageContent?pageId=%2Fprojects%2Frecently-completed-projects%2Fcredit-losses-topic-606-receivables.html).

## Procure to pay

### Canonical events

Vendor identity → budget/authority → requisition → purchase order → contract → goods/service receipt → inspection/acceptance → invoice → three-way match → payable/accrual → payment authorization → settlement → return, dispute, credit, or recovery.

### What can be automated

- approved-vendor and beneficial-ownership checks;
- segregation-of-duties and authorization thresholds;
- purchase-order/invoice/receipt three-way match;
- duplicate invoice and split-purchase detection;
- signed receipt and quality-inspection evidence;
- posting to AP, inventory, prepaid, fixed-asset construction, or expense queues;
- discount, due-date, withholding, and payment execution;
- settlement and vendor-statement reconciliation;
- exception routing and immutable approval history.

### What GAAP still requires

- determining when goods or services have been received and an obligation incurred;
- classifying the acquired item as expense, prepaid, inventory, PP&E, software/intangible, lease right-of-use asset, or another asset;
- separating lease and nonlease components and identifying embedded leases;
- accruing unbilled services, bonuses, warranties, rebates, litigation, and other obligations;
- estimating loss contingencies when loss is probable and reasonably estimable;
- distinguishing a liability extinguishment from a payment instruction or disputed claim;
- assessing related-party terms and disclosures.

A payment contract can prove that money moved. It does not determine what was acquired, whether the service occurred, whether the expenditure should be capitalized, or whether an off-chain obligation exists.

### Residual manipulation surface

Duplicate invoices and unauthorized payments can fall sharply. Games can move to sham vendors, collusive acceptance, false receiving data, misclassification of expenses as assets, undisclosed commitments, and oracle or administrator control.

**Primary authority:** [FASB summary of loss contingencies carried into Topic 450](https://fasb.org/page/PageContent?bcpath=tff&pageId=%2Freference-library%2Fsuperseded-standards%2Fsummary-of-statement-no-5.html); [FASB Topic 842 leases summary](https://fasb.org/projects/current-projects/leases-398331); [SEC Exchange Act Section 13(b) books-and-records and internal-control provisions](https://www.sec.gov/spotlight/fcpa/fcpa-recordkeeping.pdf).

## Payroll and employee compensation

### Canonical events

Worker identity/classification → approved employment terms → time or service record → gross pay → bonus/commission entitlement → benefit elections → withholding → payroll liability → payment and remittance → equity-award grant, vesting, exercise, forfeiture, or settlement → pension/postretirement service and actuarial remeasurement.

### What can be automated

- time, rate, commission, and approved-benefit calculations;
- withholding and remittance mechanics;
- approved payroll posting and settlement;
- accrual reversal upon payment;
- equity-award cap-table state, vesting conditions, exercises, forfeitures, and settlement;
- service-period schedules and disclosure data;
- exception flags for ghost employees, duplicate identities, incompatible bank accounts, or unauthorized rate changes.

### What GAAP still requires

- employee versus contractor conclusions and the economic substance of arrangements;
- accrual of earned but unpaid compensation and leave;
- estimation of discretionary bonuses and other contingent compensation;
- classification and measurement of stock compensation under Topic 718, including valuation inputs and award modifications;
- pension and postretirement measurement using actuarial present values, discount rates, participant behavior, expected future benefits, and plan-asset values;
- disclosure of significant assumptions and funded status.

The underlying grant and vesting events may be machine-verifiable. Option value, liability-versus-equity classification, probability conditions, actuarial assumptions, and modification accounting are not simply payment facts.

**Primary authority:** [FASB ASU 2024-01, Topic 718 scope for profits interests and similar awards](https://fasb.org/Page/Document?pdf=ASU+2024-01.pdf&title=ACCOUNTING+STANDARDS+UPDATE+2024-01%E2%80%94Compensation%E2%80%94Stock+Compensation+%28Topic+718%29%3A+Scope+Application+of+Profits+Interest+and+Similar+Awards); [FASB Topic 715 pension-cost presentation, ASU 2017-07](https://storage.fasb.org/ASU%202017-07.pdf); [FASB summary of recognized pension funded status](https://fasb.org/page/PageContent?bcpath=tff&pageId=%2Freference-library%2Fsuperseded-standards%2Fsummary-of-statement-no-158.html).

## Inventory and cost of sales

### Canonical events

Purchase/production authority → material receipt → custody/location → consumption into work in process → labor/overhead attachment → completion → transfer or consignment → shipment/delivery → return/scrap/shrinkage → count adjustment → obsolescence or write-down.

### What can be automated

- unique lot, serial, batch, custody, and location histories;
- signed handoffs across suppliers, warehouses, manufacturers, and customers;
- perpetual quantity records and physical-count exception lists;
- standard/actual-cost accumulation and approved overhead formulas;
- FIFO/average-cost layers and routine cost-of-sales release;
- recall provenance and damaged/expired inventory controls;
- cut-off testing against shipping, receiving, and acceptance evidence.

### What GAAP still requires

- determining title, control, consignment, bill-and-hold, and goods in transit;
- selecting and consistently applying the cost-flow method;
- identifying inventoriable costs and normal versus abnormal production costs;
- deciding the unit of account;
- assessing shrinkage, excess/obsolete stock, estimated selling price, completion costs, and disposal/transportation costs;
- applying lower-of-cost-and-net-realizable-value to inventory within ASU 2015-11’s scope, while LIFO and retail-method inventory retain separate guidance.

Token existence is not evidence of physical existence, condition, salability, ownership, or lack of obsolescence unless trusted real-world controls support those assertions.

**Primary authority:** [FASB ASU 2015-11, Inventory (Topic 330)](https://storage.fasb.org/ASU%202015-11.pdf); [PCAOB AS 1105, including observation and evidence reliability](https://pcaobus.org/oversight/standards/auditing-standards/details/AS1105).

## Fixed assets, intangibles, software, and leases

### Canonical events

Project authorization → acquisition/construction costs → asset component and location → ready/placed in service → maintenance versus improvement → depreciation/amortization → impairment indicator → valuation or recoverability test → transfer, retirement, sale, or abandonment → asset-retirement performance.

### What can be automated

- project and asset IDs, custody, component, location, and maintenance history;
- approved cost accumulation and capitalization queues;
- placed-in-service attestations;
- depreciation/amortization after policy inputs are approved;
- lease payment schedules and right-of-use/liability rollforwards;
- impairment-trigger alerts from operational data;
- disposal proceeds, derecognition, and gain/loss arithmetic;
- asset-retirement funding or settlement mechanics.

### What GAAP still requires

- asset versus expense and repair versus improvement;
- unit of account and componentization;
- useful life, residual value, depreciation method, and changes in estimate;
- whether software capitalization criteria are met;
- recoverability, forecast cash flows, fair value, and impairment;
- goodwill reporting-unit identification and impairment;
- whether a contract contains a lease, lease classification, term, options, and discount rate;
- existence, timing, probability, and fair value of an asset-retirement obligation.

The FASB’s final ASU 2025-06 modernizes internal-use-software capitalization by requiring capitalization when management has authorized and committed funding and completion/use is probable, considering significant development uncertainty. It is **issued final guidance but not mandatorily effective until annual periods beginning after December 15, 2027**; early adoption is permitted. It is evidence that technology changes can cause GAAP to update, but the update still centers on recognition thresholds and judgment.

**Primary authority:** [FASB ASU 2025-06 / internal-use software](https://storage.fasb.org/ASU%202025-06.pdf); [FASB Topic 842 leases summary](https://fasb.org/projects/current-projects/leases-398331); [FASB long-lived asset impairment summary](https://fasb.org/page/pageContent?isPrintView=true&pageId=%2Freference-library%2Fsuperseded-standards%2Fsummary-of-statement-no-144.html); [FASB asset-retirement-obligation summary](https://fasb.org/page/PageContent?bcpath=tff&pageId=%2Freference-library%2Fsuperseded-standards%2Fsummary-of-statement-no-143.html).

## Treasury, cash, debt, equity, derivatives, and crypto assets

### Canonical events

Bank/custodian/wallet authorization → deposit/withdrawal/transfer → trade or issuance → confirmation → settlement → interest/dividend → collateral or covenant state → modification/exchange → maturity/extinguishment → equity issuance/repurchase/distribution → derivative designation and valuation → digital-asset custody, transfer, or restriction.

### What can be automated

- authorized signer/key policies and multisignature release;
- near-real-time bank, custodian, wallet, and general-ledger reconciliation;
- interest, fee, premium/discount, and amortized-cost schedules;
- covenant calculations and breach alerts;
- collateral and restricted-asset tracking;
- cap-table updates and distribution calculations;
- trade confirmation, settlement, and digital-asset quantity/ownership evidence;
- market-price feeds and selected Level 1 valuation updates;
- exception controls for unexplained transfers, dormant accounts, and incompatible duties.

### What GAAP still requires

- cash versus cash-equivalent, restricted-cash, investment, or crypto-asset classification;
- debt versus equity and liability-versus-equity-classified instruments;
- modification versus extinguishment;
- control and derecognition;
- embedded derivative and Topic 815 scope analysis;
- hedge designation, probability of forecast transactions, effectiveness, and discontinuation;
- fair value hierarchy and valuation when markets are inactive or inputs unobservable;
- crypto-asset scope under Subtopic 350-60, restrictions, related parties, and issuer/customer rights;
- safeguarding contingencies and bankruptcy/legal-control analysis.

ASU 2023-08 currently requires qualifying in-scope crypto assets to be measured at fair value each reporting period with changes in net income and additional disclosures; it is effective for fiscal years beginning after December 15, 2024. The SEC’s SAB 122, effective January 30, 2025, rescinded SAB 121 and directs safeguarding entities to assess loss-contingency recognition under Topic 450 rather than automatically recognizing the former safeguarding asset and liability.

A token transfer is excellent settlement evidence but does not by itself establish legal ownership, whether control was transferred, whether the token represents another asset or claim, or which reporting category applies.

**Primary authority:** [FASB ASU 2023-08 / crypto assets](https://storage.fasb.org/ASU%202023-08.pdf); [SEC SAB 122](https://www.sec.gov/rules-regulations/staff-guidance/staff-accounting-bulletins/staff-accounting-bulletin-122); [FASB Topic 820 fair-value summary](https://fasb.org/page/pagecontent?bcpath=tff&isPrintView=true&pageid=%2Freference-library%2Fsuperseded-standards%2Fsummary-of-statement-no-157.html); [FASB debt-exchange project, including description of current modification/extinguishment analysis](https://fasb.org/projects/current-projects/accounting-for-debt-exchanges-420130).

## Income tax

### Canonical events

Tax identity/jurisdiction → taxable transaction tag → book/tax basis difference → current liability/payment → carryforward/credit → deferred tax asset/liability → valuation allowance → uncertain position/examination → settlement → rate-law change → jurisdictional disclosure.

### What can be automated

- transaction-level jurisdiction and tax-code tagging;
- sales, payroll, withholding, and selected excise calculations;
- book-to-tax mapping and temporary-difference rollforwards;
- enacted-rate updates with controlled effective dates;
- current-tax payable and remittance;
- return workpapers and jurisdictional payment disclosures;
- expiration alerts for losses and credits.

### What GAAP and tax law still require

- separating tax-basis accounting from GAAP financial reporting;
- identifying temporary versus permanent differences;
- deciding whether deferred-tax assets are more likely than not realizable and measuring valuation allowances;
- uncertain-tax-position recognition and measurement;
- interpreting tax law, nexus, entity classification, and cross-border arrangements;
- estimating future taxable income and tax-planning strategies;
- determining the effect of enacted versus proposed law.

IRS cash or combination-method eligibility is a **tax rule**, not permission to call cash-basis financial statements GAAP. IRS Publication 334 states that qualifying taxpayers can generally use combinations of cash, accrual, and special methods subject to consistency and clear-reflection restrictions; it also describes inventory exceptions for qualifying small businesses. This is a different reporting objective from GAAP.

**Primary authority:** [FASB ASU 2023-09 income-tax disclosure standard](https://fasb.org/news-and-meetings/in-the-news/fasb-issues-standard-that-enhances-income-tax-disclosures-398823); [FASB Topic 740 GAAP Taxonomy implementation guide](https://xbrl.fasb.org/impdocs/IT_TIG/incometaxes.htm); [IRS Publication 334 (2025), cash, accrual, combination methods and small-business inventory](https://www.irs.gov/publications/p334); [IRS Publication 538](https://www.irs.gov/publications/p538).

## Consolidation and close

### Canonical events

Entity/control relationship → chart-of-accounts mapping → subledger close → accrual/estimate entries → intercompany confirmation and elimination → foreign-currency remeasurement/translation → consolidation → top-side adjustment → subsequent-event update → management certification → period lock/restatement.

### What can be automated

- continuous subledger reconciliation and close status;
- period cut-off exception reports;
- standard accrual reversals;
- intercompany invoice, balance, and settlement matching;
- routine eliminations and ownership allocations;
- approved currency-rate ingestion and translation;
- journal provenance, preparer/reviewer separation, and period locks;
- automated rollforwards and disclosure checklists;
- restatement through linked reversal/supersession events.

### What GAAP still requires

- identifying the reporting entity and which entities must be consolidated;
- voting-interest, variable-interest, primary-beneficiary, power, economics, related-party, and de facto-agent analyses;
- whether a transaction is a business combination, asset acquisition, or common-control transaction;
- purchase-price allocation, identifiable intangibles, goodwill, and contingent consideration;
- functional currency and highly inflationary conclusions;
- segment identification, subsequent events, going concern, materiality, and disclosure sufficiency;
- evaluating estimates and management bias.

This is one of the clearest limits of a legal-entity ledger: the on-chain legal wrapper is not necessarily the GAAP reporting boundary. Economic control and exposure can require consolidation beyond formal voting ownership.

**Primary authority:** [FASB summary of the VIE model’s control/economic characteristics](https://fasb.org/page/pagecontent?bcpath=tff&isPrintView=true&pageid=%2Freference-library%2Fsuperseded-standards%2Fsummary-of-interpretation-no-46-revised-december-2003.html); [FASB current consolidation research](https://fasb.org/projects/current-projects/objective-research); [FASB January 28, 2026 tentative consolidation decisions](https://fasb.org/page/PageContent?bcpath=tff&pageId=%2Fnews_and_meetings%2Fpast-meetings%2F01-28-26.html).

## External reporting and audit

### Canonical events

Trial balance → financial statements → note population → management review/certification → XBRL tagging → audit evidence and testing → audit adjustments → filing/publication → subsequent correction/restatement.

### What can be automated

- generation of statements and notes from the same controlled event/rule set;
- lineage from each reported number to transactions, rules, estimates, and approvals;
- XBRL/Inline XBRL tagging and validation;
- reconciliations and disclosure rollforwards;
- continuous-control monitoring and full-population anomaly analysis;
- auditor read-only access to authorized evidence;
- reproducible reports at any valid policy version and reporting date.

### What still requires management and auditor judgment

- completeness: omitted off-chain contracts do not appear merely because the ledger is immutable;
- relevance and reliability of internal and external electronic information;
- authenticity and authority of the source event;
- management estimates and bias;
- materiality and aggregation;
- control design, override, key management, access, and rule-upgrade governance;
- physical existence, condition, performance, and legal enforceability;
- contradictory evidence and exceptions;
- sufficient appropriate audit evidence and the auditor’s independent opinion.

PCAOB AS 1105 states that the auditor must obtain sufficient appropriate evidence and that electronic information is more reliable when relevant controls, including IT general and automated application controls, are effective. AS 2501 defines accounting estimates as recognition or measurement involving subjective assumptions and measurement uncertainty and requires auditors to test management’s process, develop an independent expectation, and/or evaluate later evidence. The PCAOB’s technology-assisted-analysis amendments, effective for audits of fiscal years beginning on or after December 15, 2025, modernize audit procedures but retain evidence-reliability and investigation responsibilities.

Inline XBRL demonstrates a current, functioning form of machine-readable reporting. It structures filed financial statements, footnotes, and schedules; it is not a public transaction ledger and does not independently verify the underlying facts.

**Primary authority:** [PCAOB AS 1105](https://pcaobus.org/oversight/standards/auditing-standards/details/AS1105); [PCAOB AS 2501](https://pcaobus.org/oversight/standards/auditing-standards/details/AS2501); [PCAOB technology-assisted-analysis amendments](https://pcaobus.org/oversight/standards/standard-setting-research-projects/amendments-related-to-certain-aspects-of-designing-and-performing-audit-procedures-that-involve-technology-assisted-data-analysis); [SEC Inline XBRL](https://www.sec.gov/data-research/structured-data/inline-xbrl).

## 3. The modified-cash thesis: where it is right and where it breaks

### What is right

For a simple, owner-managed service business, an operational system centered on:

- cash receipts and payments;
- outstanding customer invoices;
- outstanding vendor bills;
- payroll and taxes due;
- signed contracts;
- bank reconciliation; and
- a small fixed-asset register

may provide most day-to-day management information. IRS rules may also allow some qualifying taxpayers to use a cash or combination method for tax.

An event-sourced system can make this much better than traditional “modified cash” bookkeeping because AR/AP are not informal side schedules: they are first-class rights and obligations tied to contracts, acceptance, and settlement.

### Why it is not GAAP

The FASB’s nonauthoritative but foundational Concepts Statement says accrual accounting reports economic effects when they occur, not merely when cash moves, because that gives a better basis for assessing performance than cash receipts and payments alone. Current Codification topics then require recognition and measurement of noncash assets and liabilities such as:

- receivables and expected credit losses;
- contract assets and liabilities;
- inventory and cost of sales;
- prepaid and accrued expenses;
- property, software, depreciation, and impairment;
- right-of-use assets and lease liabilities;
- warranties and other contingencies;
- debt premium/discount, derivatives, and equity compensation;
- pension obligations;
- deferred taxes;
- consolidation of controlled entities;
- fair-value changes for applicable instruments and qualifying crypto assets.

If a “modified cash” system faithfully adds these modules, it is converging toward accrual accounting. If it omits them, it cannot produce GAAP statements where those omitted items are material.

Public-company law reinforces the distinction. Regulation S-X requires filed financial statements to comply with GAAP, and Exchange Act Section 13(b) requires books, records, and internal accounting controls sufficient to permit GAAP preparation. The law does not prescribe a particular ledger technology.

**Primary authority:** [FASB Concepts Statement 8, Chapter 1, paragraph OB17](https://storage.fasb.org/Concepts_Statement_8-Chapter_1_%28As_Amended%29.pdf); [FASB official standards page](https://fasb.org/standards); [SEC Financial Reporting Manual, Topic 1](https://www.sec.gov/about/divisions-offices/division-corporation-finance/financial-reporting-manual/frm-topic-1); [SEC Exchange Act Section 13(b)](https://www.sec.gov/spotlight/fcpa/fcpa-recordkeeping.pdf).

## 4. A more powerful replacement model: one event log, multiple accounting views

The strongest design is an **event constitution**, not one journal:

### Canonical event object

- unique event ID;
- event type and effective time;
- legal entities and authorized actors;
- contract/right/obligation ID;
- asset, service, or performance object;
- quantity and consideration;
- jurisdiction and currency;
- external evidence and signatures;
- parent, causal, reversal, and supersession links;
- oracle/source identity and confidence;
- privacy/classification permissions;
- rule-set version;
- accounting outputs by basis;
- estimate/judgment record and approver;
- audit/control status;
- settlement/correction/recovery state.

### Derived views

1. **Cash view:** actual receipts, payments, and settlement.
2. **GAAP view:** accrual recognition, measurement, presentation, and disclosure.
3. **Tax view:** federal, state, local, and foreign tax methods and timing.
4. **Management view:** budgets, unit economics, commitments, forecasts, and operating metrics.
5. **Regulatory/statutory view:** industry-specific capital, solvency, or statutory reporting.

This architecture makes non-equivalences explicit:

> order ≠ contract ≠ performance ≠ invoice ≠ receivable ≠ cash receipt ≠ revenue  
> purchase order ≠ receipt ≠ payable ≠ expense ≠ cash payment ≠ settlement  
> token transfer ≠ legal ownership ≠ control ≠ derecognition ≠ revenue

The same facts can legitimately generate different outputs under different bases. Transparency comes from publishing the transformation rules and preserving the judgment record—not from forcing every purpose into cash timing.

## 5. How “accounting games” change

### Games that become harder

- backdated or deleted entries;
- untraceable top-side journals;
- duplicate payments;
- missing three-way match;
- unexplained reconciliation differences;
- inconsistent intercompany records;
- period-end cut-off without delivery/acceptance evidence;
- silent policy changes;
- altered supporting documents;
- restatements that overwrite rather than supersede history.

### Games that remain or migrate

- omitting a contract or side agreement from the system;
- collusive counterparties or validators;
- false physical or performance attestations;
- sham related-party entities;
- manipulating oracle inputs;
- classifying expense as asset;
- choosing favorable units of account;
- optimistic credit, impairment, useful-life, return, warranty, pension, or tax assumptions;
- controlling the code upgrade, emergency pause, permission, or private key;
- drafting legal terms to obtain a preferred accounting result;
- keeping economically important activity outside the shared record.

An immutable ledger preserves a false authorized assertion just as faithfully as a true one. Fraud prevention therefore depends on identity, authority, segregation of duties, counterparty evidence, real-world verification, correction, recovery, and independent assurance.

The SEC’s books-and-records framework is compatible with this conclusion: controls must provide **reasonable**, not absolute, assurance; records must accurately and fairly reflect transactions in reasonable detail; and transaction authorization and asset accountability matter alongside GAAP reporting.

## 6. What may actually change in GAAP

### Likely

- new recognition, classification, measurement, derecognition, and disclosure rules for digital assets and tokenized rights;
- more machine-readable and disaggregated disclosures;
- standards that assume better access to granular data and reduce cost-based practical limitations;
- clearer accounting for code-executed rights, custody, transfers, and programmable settlement;
- audit standards that accommodate full-population analysis while strengthening data reliability and IT-control requirements;
- more explicit provenance for estimates and rule versions.

### Less likely

- GAAP becoming cash basis for general-purpose external reporting;
- elimination of accrual assets and liabilities;
- elimination of management estimates;
- removal of consolidation analysis merely because legal entities have separate ledgers;
- treating code execution as sufficient evidence of economic substance;
- replacing independent audit with consensus validation.

The crypto example is instructive: FASB changed the measurement model for qualifying crypto assets to fair value because the prior cost-less-impairment result did not reflect the economics. It did **not** discard recognition, scope, measurement, disclosure, or judgment.

## 7. Current standard-setting watchlist — not current GAAP unless stated

| Item | Status at 2026-07-30 | Why it matters |
|---|---|---|
| Crypto assets, ASU 2023-08 | **Final and effective** for fiscal years beginning after 2024-12-15 | Demonstrates a GAAP measurement change prompted by a new asset class. |
| SEC SAB 122 | **Effective 2025-01-30** | Rescinded SAB 121; safeguarding loss risk returns to contingency analysis. |
| Internal-use software, ASU 2025-06 | **Final; mandatory 2027+, early adoption permitted** | Modernizes recognition for iterative software development but retains probable-completion judgment. |
| Expense disaggregation, ASU 2024-03/2025-01 | **Final; annual 2027, interim 2028 for PBEs** | Uses more granular expense data without replacing the income statement. |
| Crypto transfers, wrapped/receipt tokens | **Technical-agenda project; initial deliberations/tentative** | FASB is considering scope expansion and derecognition guidance. No current-GAAP change yet. |
| Certain digital assets as cash equivalents | **Project; Board directed staff to draft a proposed ASU in April 2026** | Stablecoin classification is under active consideration. No current-GAAP change yet. |
| Consolidation for business entities | **Research/tentative** | Board directed research on harmonizing VIE and voting-interest models. No current-GAAP change yet. |
| Statement of cash flows | **Research project** | FASB is considering improvements and disclosures; no current-GAAP change yet. |
| Accounting for and disclosure of intangibles | **Research project** | Could affect internally developed intangible recognition; no current-GAAP change yet. |

**Primary project sources:** [FASB cash-equivalents/digital-assets project history](https://fasb.org/projects/current-projects/projects-history/cash-equivalents%E2%80%94disclosure-enhancement-and-classification-of-certain-digital-assets-423255); [FASB April 2026 crypto-transfer meeting listing](https://fasb.org/news-and-meetings/past-meetings); [FASB May 2026 PMAC crypto-transfer recap](https://fasb.org/about-us/Advisory-Groups/pmac/pmac-meeting-materials/pmac-meeting-recap-may-14-2026); [FASB objective research projects](https://fasb.org/projects/current-projects/objective-research); [FASB ASU 2024-03 expense disclosures](https://storage.fasb.org/ASU%202024-03.pdf).

## 8. Research conclusion

The user’s intuition is strongest when reframed this way:

- Most accounting labor is not the economic theory of GAAP; it is capturing fragmented facts, reconciling incompatible systems, posting repetitive entries, documenting controls, and rebuilding lineage at close.
- Event-sourced, cryptographically signed systems can collapse much of that labor and make correction, authorization, and provenance visible.
- A small company may operate on a cash-centered interface with AR/AP and a few modules, while the system derives accrual, tax, and management views underneath.
- Open-source accounting rules can make transformations inspectable and challengeable.
- But GAAP remains necessary wherever cash timing fails to represent economic resources, obligations, performance, uncertainty, or control.

The true revolution is therefore not a return from accrual to cash. It is the separation of:

> **shared facts → published accounting rules → signed judgments → reproducible reports → independent assurance**

That could make the system far more understandable without pretending that every difficult accounting question is merely a bookkeeping problem.

## Primary-source ledger

### FASB foundations and authority

- [FASB Standards page — Codification is the single official source of authoritative nongovernmental U.S. GAAP; Concepts Statements are nonauthoritative](https://fasb.org/standards)
- [Concepts Statement 8, Chapter 1 — accrual accounting and reporting objective](https://storage.fasb.org/Concepts_Statement_8-Chapter_1_%28As_Amended%29.pdf)
- [Concepts Statement 8, Chapter 4 — assets, liabilities, revenues, expenses, and other elements](https://storage.fasb.org/Concepts_Statement_8-Chapter_4-Elements.pdf)
- [Conceptual Framework for Financial Reporting, September 2024](https://storage.fasb.org/Conceptual%20Framework%20for%20Financial%20Reporting%20%28September%202024%29.pdf)

### FASB operating topics

- [Topic 606 revenue recognition](https://fasb.org/projects/recently-completed-projects/revenue-recognition-summary)
- [Topic 326 credit losses](https://fasb.org/projects/recently-completed-projects/accounting-standards-update-2016-13-financial-instrument-credit-losses)
- [ASU 2015-11 inventory](https://storage.fasb.org/ASU%202015-11.pdf)
- [Topic 842 leases and Topic 326 summary](https://fasb.org/projects/current-projects/leases-398331)
- [ASU 2025-06 internal-use software](https://storage.fasb.org/ASU%202025-06.pdf)
- [Topic 450 loss-contingency summary](https://fasb.org/page/PageContent?bcpath=tff&pageId=%2Freference-library%2Fsuperseded-standards%2Fsummary-of-statement-no-5.html)
- [Topic 820 fair-value measurement summary](https://fasb.org/page/pagecontent?bcpath=tff&isPrintView=true&pageid=%2Freference-library%2Fsuperseded-standards%2Fsummary-of-statement-no-157.html)
- [ASU 2023-08 crypto assets](https://storage.fasb.org/ASU%202023-08.pdf)
- [ASU 2023-09 income-tax disclosures](https://fasb.org/news-and-meetings/in-the-news/fasb-issues-standard-that-enhances-income-tax-disclosures-398823)
- [ASU 2024-03 expense disaggregation](https://storage.fasb.org/ASU%202024-03.pdf)
- [VIE/consolidation model summary](https://fasb.org/page/pagecontent?bcpath=tff&isPrintView=true&pageid=%2Freference-library%2Fsuperseded-standards%2Fsummary-of-interpretation-no-46-revised-december-2003.html)

### SEC reporting, records, and crypto

- [Exchange Act Section 13(b) books, records, and internal accounting controls](https://www.sec.gov/spotlight/fcpa/fcpa-recordkeeping.pdf)
- [SEC Financial Reporting Manual, Topic 1](https://www.sec.gov/about/divisions-offices/division-corporation-finance/financial-reporting-manual/frm-topic-1)
- [SEC Inline XBRL](https://www.sec.gov/data-research/structured-data/inline-xbrl)
- [SEC SAB 122](https://www.sec.gov/rules-regulations/staff-guidance/staff-accounting-bulletins/staff-accounting-bulletin-122)

### PCAOB assurance

- [AS 1105, Audit Evidence](https://pcaobus.org/oversight/standards/auditing-standards/details/AS1105)
- [AS 2501, Auditing Accounting Estimates, Including Fair Value Measurements](https://pcaobus.org/oversight/standards/auditing-standards/details/AS2501)
- [Technology-assisted-analysis amendments to AS 1105 and AS 2301](https://pcaobus.org/oversight/standards/standard-setting-research-projects/amendments-related-to-certain-aspects-of-designing-and-performing-audit-procedures-that-involve-technology-assisted-data-analysis)

### IRS tax-basis distinction

- [IRS Publication 334 (2025), Tax Guide for Small Business](https://www.irs.gov/publications/p334)
- [IRS Publication 538, Accounting Periods and Methods](https://www.irs.gov/publications/p538)
