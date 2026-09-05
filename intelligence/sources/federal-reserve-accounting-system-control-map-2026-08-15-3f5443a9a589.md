# Federal Reserve accounting-system control map — August 15, 2026

**Status:** pending; complete for human review; workbench-only; not promoted to
the vault, Research Desk catalog, Observatory, wrapper, or installed app

**Prepared:** 2026-08-15 19:22 EDT

**Fresh official-source cutoff:** 2026-08-15 19:22 EDT

**Evidence rule:** legal entity, reporting entity, accounting policy, software
system, general-ledger account, managerial cost object, allocation driver,
service operator, asset controller, settlement event, cash movement and audit
surface remain separate until an operative record joins them.

## Objective

Map the Federal Reserve Banks' accounting machinery end to end: the policy
manuals, software systems, posting and reporting paths, inter-Bank settlement,
cost allocation, service billing and revenue recognition, shared-service
reimbursements, software-asset accounting, combination/elimination process and
audit perimeter.

This is a focused extension of the broader
`FEDERAL_RESERVE_SYSTEM_ENTITY_TRANSACTION_AND_SOFTWARE_MAP.md` and the
vault-incorporated `Federal Reserve Financial Constitution — Source Document`.
It does not replace either artifact.

## Scope questions

1. What distinct jobs are performed by FAM, EASy, ISA/InterFRB, FR 34,
   RFARS/WTB, CASPR, Reserve Bank budgets, priced-service pro formas and the
   combined financial statements?
2. Which Bank or System actor creates, approves, posts, reports, allocates,
   eliminates, audits and corrects each record?
3. How do customer fees, shared-service costs, National IT charges, software
   assets and SOMA/ISA positions travel through the machinery?
4. Which changes are established—such as the April 2018 billing-host change and
   July 2021 CASPR adoption—and which 2025–26 changes remain presentation,
   budget or governance effects rather than proved system migrations?
5. Which decisive system charters, data dictionaries, allocation drivers,
   service agreements, application registers and audit-scope schedules remain
   nonpublic?

## Map contents

- system and record dictionary;
- actor–action–record–posting–control matrix;
- end-to-end transaction/accounting walkthroughs;
- twelve-Bank host and cost-location topology;
- change timeline;
- accounting-to-control claim audit;
- bounded public gaps and exact next retrievals.

## Executive result

The Reserve Banks have undergone a genuine accounting-operating
centralization, but not a merger of their legal books.

The documented structural change is:

1. branch accounting was consolidated into each District head office in 2014;
2. a new enterprise-resource program transformed financial-management,
   human-resources and procurement processes and moved the Banks from a
   District-specific solution to a Systemwide solution in 2021;
3. CASPR replaced PACS as the uniform cost-accounting framework for
   transactions beginning July 1, 2021; and
4. the new ERP tool and CASPR were officially grouped as the Reserve Banks'
   new “planning system.”

The Systemwide ERP and CASPR can change where costs appear across Banks, cost
centers and business lines. They do not turn the twelve Reserve Banks into one
legal entity, combine their audited balance sheets into a single legal ledger,
or prove that a managerial allocation moved cash.

The public record also establishes a distributed accounting topology:

- Boston houses all-twelve finance shared services and accounting-technology
  support;
- Minneapolis is the priced-service billing host;
- Boston, New York, Atlanta and Chicago recognize named service-family revenue;
- Richmond houses National IT, System Financial Planning & Management,
  Enterprise Resource Planning support and selected national procurement;
- each Bank retains its own legal books and internal-control responsibility;
  and
- RBOPS receives Bank reporting and manages the combined presentation.

The decisive application interfaces remain nonpublic. EASy, the unnamed
centralized ISA posting system, the Systemwide ERP, CASPR and Boston's
Centralized Accounting Technology Services must not be collapsed into one
machine.

## 1. Evidence and claim states

- **Disclosed:** directly stated in a current official record.
- **Computed:** arithmetic on disclosed values with the formula shown.
- **Bounded inference:** follows from disclosed architecture but is not an
  operative charter, interface specification or journal record.
- **Proposed:** advocated, budgeted or under evaluation; not implemented merely
  because it was announced.
- **Not public:** the reviewed official record did not disclose the object by
  the cutoff; this is not proof that the object does not exist.

## 2. Architecture at a glance

~~~mermaid
flowchart TB
    B["Branch or operational source event"]
    G["District head-office books<br/>Bank GL and subledgers"]
    F["FAM policy and FR 34 chart<br/>Board / RBOPS"]
    P["Systemwide ERP + CASPR<br/>officially grouped as planning system"]
    E["EASy<br/>selected accounting/reporting/settlement uses"]
    X["InterFRB procedure"]
    U["Unnamed centralized ISA posting engine"]
    I["Reciprocal Bank entries<br/>ISA 180-025"]
    R["Daily FR 34"]
    W["WTB"]
    Z["Specified RFARS schedules"]
    C["RBOPS combined financial statements"]
    L["Inter-Bank eliminations"]
    A["Individual Bank statements<br/>and ICFR audit"]
    K["Combined financial-statement audit"]
    Q["CASPR annual cost reports"]
    S["Priced-service pro forma + PSAF"]

    F --> G
    B --> G
    P -. "planning, costing and budget relationship;<br/>internal field sequence not public" .-> G
    E -. "FR 34-Back and selected posting uses" .-> G
    G --> R
    G --> X
    X --> U
    U --> I
    I --> G
    G --> W
    G --> Z
    R -. "reconciliation" .-> W
    R -. "specified reconciliation" .-> Z
    R --> L
    W --> L
    L --> C
    G --> A
    C --> K
    P --> Q
    Q -. "year-end agreement control" .-> G
    P -- "CASPR-derived cost input" --> S
~~~

The dotted connections are bounded relationships, not a claim that the public
record exposes field order, APIs, master-data ownership or the application in
which CASPR logic executes.

## 3. System and record dictionary

| Object | Disclosed job | Authority or operator | What it is not / public limit |
|---|---|---|---|
| FAM | Financial-accounting policy, FR 34 chart, balance-sheet location, capitalization, depreciation, corrections and close | Board-developed; RBOPS Financial Accounting Policy and Reporting sets, amends and interprets within delegated limits | Not software; expressly does not provide cost-accounting guidance |
| District GL and subledgers | Record all transactions on each Bank's legal books and feed FR 34 | Each Reserve Bank management/accounting function | No public current application catalog, subsidiary chart or journal-approval matrix |
| Systemwide ERP | Systemwide solution replacing District-specific financial-management, HR and procurement processes | Board oversight; current Richmond records identify an Enterprise Resource Planning Support Office | Vendor, modules, GL status, interfaces and master-data ownership not public |
| CASPR | Uniform cost framework for priced, reimbursable, assessed and other central-bank services | Approved by the Conference of First Vice Presidents; applied by all Banks | Not the legal ledger; current manual, administering application and driver dictionary not public |
| PACS | Historical predecessor cost-accounting framework | Reserve Bank System; established 1977 and refreshed in 2001 | Published PACS mechanics cannot be silently treated as current CASPR rules |
| EASy | Enterprise Accounting System used for FR 34-Back and selected accounting/settlement flows | Current FAM names the application; current controller/host not disclosed | Not publicly proved to be the sole GL, Systemwide ERP, CASPR engine or the unnamed ISA engine |
| InterFRB | Inter-Reserve-Bank settlement procedure | Reserve Banks through the centralized accounting process | A procedure, not the ISA account itself |
| ISA 180-025 | Each Bank's cumulative amount due to or from other Banks from InterFRB activity | Entries post to affected Bank books | Not service revenue, a bilateral invoice, an external cash-flow statement or a payment rail |
| Unnamed centralized accounting system | Captures data, effects general InterFRB settlement and posts entries directly to Bank accounts | Not named in FAM §5.00 | Public FAM does not identify it as EASy |
| FR 34 | District balance-sheet and accounting-report form, including daily reporting and a monthly reverse side | Each Bank submits; Board/RBOPS receives | A report and chart, not the underlying application |
| WTB | Working trial balance supplying periodic income and profit/loss detail to RBOPS | Each Bank makes data available to RBOPS | Platform identity, schema, access control and relation to EASy not public |
| RFARS | RBOPS Financial Accounting Reports System for specified electronic schedules | Banks submit specified reports to Board/RBOPS | Not proved to be a GL or WTB platform |
| Service-revenue subledgers | Maintain current service-income detail and add totals to the GL at daily close | Named operating/revenue Bank | Public data dictionary and interface not available |
| Priced-service pro forma | Service-line view of revenue, cost, imputed costs and recovery under the Monetary Control Act | FRFS/System policy process and Board pricing approval | Not a legal-entity statement |
| PSAF | Private-sector adjustment factor adding imputed taxes, debt financing and return-on-equity treatment | Board-approved pricing overlay | Not a CASPR allocation driver |
| Individual Bank financial statement | Bank legal-entity books plus any controlled VIE | Bank management/board; KPMG audit | Does not prove enterprise control of every recorded service or asset |
| Combined Reserve Bank statements | Aggregation of twelve Banks and consolidated VIEs after internal eliminations | RBOPS-managed reporting; KPMG audit | Not a thirteenth corporation or a Bank-by-Bank operating-margin report |

Primary sources: [FAM overview](https://www.federalreserve.gov/aboutthefed/financial-accounting-manual.htm),
[FAM Chapter 1](https://www.federalreserve.gov/aboutthefed/chapter-1-balance-sheet.htm),
[FAM Chapter 6](https://www.federalreserve.gov/aboutthefed/chapter-6-reporting-requirements.htm),
[2021 Board performance report](https://www.federalreserve.gov/publications/2022-annual-performance-report.htm),
[2022 Reserve Bank budget and addendum](https://www.federalreserve.gov/foia/files/2022ReserveBankBudgets.pdf),
and [2024 supervision-assessment methodology](https://www.federalreserve.gov/supervisionreg/supervision-regulation-assessment-2024.htm).

## 4. What changed, and when

| Date / period | State | Accounting-system event | Correct reading |
|---|---|---|---|
| 1977 | occurred | PACS established as the Reserve Bank cost-accounting system | Historical beginning, not current engine |
| 2001 | occurred | PACS methodology refreshed | Historical driver architecture only |
| 2013-03-20 | occurred | Boston received additional EASy capital-expenditure approval | Boston had an EASy capital role; present ownership/control does not follow |
| 2014 | occurred | All branch accounting consolidated to District head offices; branch balance sheets and three branch/head-office accounts ended | Operational branches remain, but the accounting unit is the District Bank |
| 2014 statement year | occurred / disclosure | San Francisco identified EASy as a major nonreimbursed System service | Cost-location evidence, not permanent ownership |
| 2018-04 | occurred | Minneapolis became billing host for the accrued-service-income receivable; offsetting revenue remained at named operating Banks | Billing asset, product revenue and cash collection are different roles |
| 2017 to 2026 instructions | occurred / documentary change | FAM reporting instructions moved from an Adjusted Trial Balance, Lawson references and several legacy forms to WTB and a streamlined inventory | Proves changed reporting instructions; does not establish whether WTB is a renamed report, replacement application or redesigned interface |
| 2021-05 | occurred | Conference of First Vice Presidents approved CASPR | Approval clock |
| 2021-07-01 | occurred | Transactions began processing under CASPR | Operative cost-accounting transition |
| 2021 | occurred | New enterprise-resource program transformed finance, HR and procurement processes and moved the Banks from a District-specific solution to a Systemwide solution | Genuine operating centralization; not merged legal books |
| 2021-2022 | occurred / implementation | ERP and CASPR were grouped as the planning system; budgets and cost presentations were recast | Large internal reallocations can coexist with a small System top-line change |
| 2022-2023 | occurred / refinement | CASPR refinement materially changed assessed-cost allocations | Trend breaks require methodology controls |
| 2025 statement year | occurred / disclosure | Boston names FSO/CATS; Richmond names System Financial Planning & Management and separately reports large computing/support reimbursements; current Richmond material still identifies ERP support | Current host topology, not a complete system RACI |
| 2026-01 to 2026-03 | occurred | Current FAM retained EASy, WTB and RFARS; 2025 Bank statements and ICFR received unmodified KPMG opinions dated March 12 | Current reporting/audit baseline |
| 2026-04-21 | proposed | Governor Waller proposed single System leaders for finance/accounting, procurement, HR, IT and vendor management, with possible later physical consolidation or outsourcing | Governor proposal stated as his own views; not implemented reorganization |
| 2026-07-23 | occurred / governance | Richmond amended and restated its bylaws, refreshing the corporate baseline for National IT and System-CIO governance | Governance change; not an accounting-platform migration |

Sources: [historical PACS methodology](https://www.federalreserve.gov/frrs/regulations/appendix-methodology-for-computing-costs-for-federal-reserve-priced-services.htm),
[December 2000 PACS memorandum](https://www.federalreserve.gov/boarddocs/meetings/2000/20001213/20001213-OpenMemo5.pdf),
[Boston EASy delegated action](https://www.federalreserve.gov/releases/h2/20130601/delactions.htm),
[FAM Appendix C](https://www.federalreserve.gov/aboutthefed/appendix-c-fr-34-accounts.htm),
[San Francisco 2014 statement](https://www.federalreserve.gov/aboutthefed/files/BSTSanFranciscofinstmt2014.pdf),
[legacy January 2017 FAM Chapter 6](https://www.federalreserve.gov/federal-reserve-banks/fam/chapter-6-reporting-requirements.htm),
[2020 assessment methodology](https://www.federalreserve.gov/supervisionreg/supervision-regulation-assessment-2020.htm),
[2021 assessment methodology](https://www.federalreserve.gov/supervisionreg/supervision-regulation-assessment-2021.htm),
and [Waller, April 21, 2026](https://www.federalreserve.gov/newsevents/speech/waller20260421a.htm).

## 5. System-to-record-to-posting control matrix

| Lane | Source/system event | Receiving record/books | Control and reconciliation | Public gap |
|---|---|---|---|---|
| Branch event | Branch or operational source record | District/head-office GL; one Bank FR 34 | FAM applied Districtwide; branch advises head office where required | Source-application and journal catalog |
| Ordinary Bank transaction | Operational application, subledger or manual journal | Bank GL and FR 34 | Every transaction must reach GL and FR 34 | Local chart, approval matrix, interfaces |
| Currency shipment across Districts | Sending office ISA entry; EASy Inter-FRB setup | Automatic receiving-office interim in-transit debit, later cleared | Sender/receiver balancing; unusual returns/errors require adjustments | EASy message, authorization and journal detail |
| Daylight-overdraft fee | Daylight-overdraft monitoring application finalizes charge | Charge passed to EASy for later settlement to institution account | Institution report; bounded adjustment rules | Exact EASy journal/accounts |
| General InterFRB settlement | Unnamed centralized accounting system captures settlement data | Direct entries to affected Bank accounts; cumulative ISA 180-025 | Reciprocal entries; annual settlement; combination removes internal position | Engine identity and message schema |
| Billing accrual | Service earned; Minneapolis billing-host process | Minneapolis receivable 170-475; revenue at Boston, New York, Atlanta or Chicago through ISA | At least weekly and month-end accrual; estimate should approximate realizable amount; prevent duplicate combined income | Billing application, aging, cash, dispute and write-off flow |
| Billing dispute | Institution question/error; pricing suspense 170-450 | Institution account reversed; item held until resolution | Unresolved/uncollectible items removed under FAM; earnings entry where applicable | Aging and exception queue |
| Principal/Agent cost | Principal estimates monthly Agent processing reimbursement | Principal debits service-cost-incurred expense; Agent receives expense credit through ISA | Following month true-up to actual; customer revenue stays gross | CASPR driver, Agent file, approval roles |
| Service-income subledger | Usage-based service obligation performed | Current income 330-025 and service schedule | Posted currently; daily addition to GL; optional variance reconciliation | Subsidiary schema/application |
| Domestic SOMA transaction | FRBNY executes under FOMC authority; settlement-date event | Each Bank records an undivided participation through ISA | Most participation daily; domestic allocation reset annually; foreign activity uses a separate capital-and-surplus basis | SOMA-to-Bank journal interface and application-control owner |
| Shared software | Product/function office defines and controls asset; development/hosting/contracting may be elsewhere | Controller-hosting Bank capitalizes qualifying asset | FAM Appendix D control and project-stage tests; cross-Bank development cost transferred | Application register and contract chain |
| FR 34 close | District GL and subsidiary totals | Preliminary/final FR 34 to Board | Special correction, Wednesday, month-end and year-end rules | Technical Memorandum No. 15 and transmission spec |
| WTB | Periodic working trial balance | RBOPS Financial Accounting Policy and Reporting | Income/P&L detail reconciles to FR 34 or reconciliation supplied | Schema, platform and ATB-to-WTB transition |
| RFARS | Specified financial schedules | Board/RBOPS | Current published examples include currency and premises/real-estate reporting | Complete inventory and EASy/WTB relation |
| Year-end close | FR 34, WTB, CASPR and service reports | Final Bank books and Board reporting | Amounts removed at January close agree dollar-for-dollar with corresponding annual results reported elsewhere, including CASPR and income-from-services reports; permitted pre-close adjustments route through WTB | Annual instructions, close checklist, exception log |
| External assurance | Statements and ICFR evidence | Individual and combined statements | Each Bank management uses COSO 2013 and KPMG issued each Bank an unmodified financial-statement and ICFR opinion; combined statements received an unmodified financial-statement opinion | Materiality, application scope, significant risks, journal samples and workpapers |

Sources: [FAM Chapter 1](https://www.federalreserve.gov/aboutthefed/chapter-1-balance-sheet.htm),
[FAM Chapter 4](https://www.federalreserve.gov/aboutthefed/chapter-4-system-open-market-account.htm),
[FAM Chapter 5](https://www.federalreserve.gov/aboutthefed/chapter-5-federal-reserve-notes.htm),
[FAM Chapter 6](https://www.federalreserve.gov/aboutthefed/chapter-6-reporting-requirements.htm),
[FAM Appendix D](https://www.federalreserve.gov/aboutthefed/appendix-d-software.htm),
and [Payment System Risk Guide](https://www.federalreserve.gov/paymentsystems/files/psr_guide.pdf).

## 6. Five end-to-end accounting walkthroughs

### 6.1 A customer service fee

~~~text
service performed
  +-> revenue/accrual leg:
  |    usage/service-income subsidiary
  |    -> Minneapolis receivable
  |    -> ISA offset
  |    -> Boston / New York / Atlanta / Chicago gross System revenue
  |
  +-> processing-cost leg:
  |    Principal/Agent month-end estimate through ISA
  |    -> following-month true-up to actual
  |
  +-> CASPR internal cost-accounting allocation
       (complete current driver sequence and its order relative to true-up are not public)

reporting convergence
  -> priced-service pro forma adds service attribution and PSAF
  -> combined statements remove reciprocal inter-Bank entries
  -> external customer receivable/revenue and underlying external cost remain
~~~

These are parallel accounting legs with different clocks, not one
transaction-level journal chain. Together they prove that billing host, revenue
Bank, processing Bank, CASPR cost object and combined service margin can all be
different objects.

### 6.2 Richmond National IT computing/support

~~~text
Richmond books payroll/vendor/asset/other costs
  -> inter-Bank allocation to benefited Banks and functions
     (CASPR role and posting engine for the full reimbursement are not public)
  -> Richmond records computing/support reimbursement as expense credit
  -> recipient Banks bear allocated charges
  -> combined statement removes the internal credit/charges
  -> underlying external System cost remains once
~~~

Richmond received a source-rounded $1,135,000,000 reimbursement in 2025,
compared with $1,052,000,000 in 2024. Its $850,000,000 net operating expense
plus the $1,135,000,000 credit reconstructs $1,985,000,000 of gross
Richmond-booked expense before reimbursement. This is a legal-book
gross-to-net bridge—not a disclosed National IT segment, vendor ledger, profit
or cash-receipt schedule.

Source: [Richmond 2025 financial statements](https://www.federalreserve.gov/aboutthefed/files/richmondfinstmt2025.pdf).

### 6.3 Interdistrict state and domestic SOMA

~~~text
cross-District activity
  -> InterFRB reciprocal entries
  -> each Bank's ISA due-to/from position
  -> annual settlement uses preceding 12-month average ISA through March
  -> gold-certificate settlement plus equal-and-opposite SOMA reallocation
  -> domestic allocation percentage applies until next reset
  -> FRBNY continues executing, but all twelve Banks record undivided shares
~~~

ISA is both cumulative interdistrict state and an input to the annual domestic
SOMA allocation. The December 31 ISA balance is later cumulative state, not the
contemporaneous allocation key.

### 6.4 A shared software project

~~~text
business controller sets requirements and lifecycle
  -> one Bank or vendor may develop
  -> another Bank or cloud vendor may physically host
  -> one or more Banks may hold implementation/hosting contracts
  -> controller-hosting Bank records the asset absent a contrary agreement
  -> qualifying other-Bank development cost transfers into that asset
  -> CASPR can supply benefited-cost allocation
     (the application-level route and driver are not public)
  -> amortization reaches expense over the approved useful life
~~~

The application row therefore needs at least eight fields: controller,
controller-hosting Bank, developer, physical host/cloud provider,
implementation-contracting Bank, hosting-contracting Bank, invoice-paying
Bank and CASPR beneficiary/cost object.

Richmond's net software declined from a source-rounded $35,000,000 to
$27,000,000 during 2025 while combined Reserve Bank net software increased from
$597,000,000 to $646,000,000. This is inconsistent with treating Richmond
ownership as a presumption, but it does not identify which balances are
National IT software. Appendix D still requires an application-by-application
determination.

### 6.5 Close, combination and audit

~~~text
Bank GL/subledgers
  +-> daily FR 34
  +-> periodic WTB, reconciled to FR 34 where required
  +-> specified RFARS schedules

FR 34 + WTB
  -> RBOPS combination and inter-Bank eliminations
  -> combined financial statements
  -> KPMG combined financial-statement opinion

individual Bank records
  -> Bank financial statements + management COSO ICFR assessment
  -> KPMG Bank financial-statement and ICFR opinions
~~~

A clean financial-statement/ICFR opinion addresses materially reliable
financial reporting. It is not an application-by-application uptime, cyber,
service-level, payment-finality, transaction-by-transaction or
application-wide operational-completeness opinion.

## 7. ERP and CASPR: the actual structural change

The 2021 Board performance report says the new enterprise-resource program
transformed financial-management, human-resources and procurement business
processes and moved the Banks from a District-specific solution to a
Systemwide solution.
The 2022 budget addendum calls the ERP tool and new CASPR framework
collectively the “planning system” and describes the budget as fully costed in
the ERP tool.

The following documented effects show why comparisons across the transition
need a methodology bridge:

| Effect | Officially reported consequence | Claim limit |
|---|---|---|
| FRIT redistribution | Approximately $310,000,000 of expense formerly displayed at Richmond was distributed across Districts | Allocation change, not new System spending |
| Cash-access fees | $21,800,000 moved from recovery/net-expense treatment to revenue treatment, increasing displayed gross operating expense | Classification change, not equivalent economic-cost increase |
| Fiscal-services plan | Expense revised down $10,500,000 after full planning-system implementation shifted costs among business lines | Business-line allocation, not a cash saving by itself |
| 2022 final System plan | Top-line change was only $2,600,000 despite material Bank and business-line movements | Demonstrates redistribution beneath a stable total |
| Other-entity fiscal work | 2021 expense fell $14,700,000, or 37.5 percent, attributed primarily to the new framework | Methodology effect must be separated from workload |
| Assessed supervision | Reserve Bank assessment-basis amount rose from $561,400,000 in 2020 to $725,300,000 in 2021; Board cites methodology and pension as major causes | Not a clean workload trend |
| Later refinement | Reserve Bank assessment-basis amount moved from $842,000,000 in 2022 to $554,500,000 in 2023; Board identifies CASPR refinement as a major variance driver | Not a clean operational-efficiency trend |

Primary sources: [2022 Reserve Bank budget and addendum](https://www.federalreserve.gov/foia/files/2022ReserveBankBudgets.pdf),
[2021 Annual Report payment/Reserve Bank chapter](https://www.federalreserve.gov/publications/2021-ar-payment-system-and-reserve-bank-oversight.htm),
[2021 assessment methodology](https://www.federalreserve.gov/supervisionreg/supervision-regulation-assessment-2021.htm),
and [2024 assessment methodology](https://www.federalreserve.gov/supervisionreg/supervision-regulation-assessment-2024.htm).

### 7.1 What the public record says about CASPR drivers

Current public assessment reporting discloses employee time, personnel cost,
direct cost, support/overhead, pension, proportional integral activities and
specified exclusions for assessed supervision. It does not disclose the
complete current CASPR driver engine.

Historical PACS published four broad cost families:

1. direct;
2. internal support;
3. nationally provided support; and
4. corporate overhead.

It also described employee-time surveys, usage surveys, service quantities
multiplied by rates, predetermined assumptions and overhead ratios. These are
candidate questions for CASPR—not proof that the same drivers, weights or
rates remain live.

### 7.2 CASPR is not the priced-service pro forma

CASPR-derived operating cost is one input. The priced-service pro forma
reassigns revenue and cost to services and adds private-sector-equivalent
imputations through PSAF.

For 2024 mature priced services, the Board reported source-rounded revenue of
$524,300,000, total expense of $464,200,000, targeted return on
equity of $9,700,000 and 110.6 percent cost recovery. FedNow remained outside
that mature aggregate. Its forecast operating expense was $235,100,000 for
2025 and $230,300,000 for 2026, but the reviewed public records provided no
FedNow revenue or official recovery ratio.

The 2026 PSAF is $34,100,000. PSAF is a statutory pricing overlay, not a CASPR
driver or Bank legal-book statement.

Sources: [Federal Reserve Act §11A](https://www.federalreserve.gov/aboutthefed/section11a.htm),
[pricing principles](https://www.federalreserve.gov/paymentsystems/pfs_principles.htm),
[2024 Annual Report](https://www.federalreserve.gov/publications/files/2024-annual-report.pdf),
and [2026 service prices and PSAF](https://www.federalregister.gov/documents/2025/12/09/2025-22268/federal-reserve-bank-services).

## 8. Individual-Bank host and cost-location topology

These are major 2025 System functions for which the host Bank said costs were
not reimbursed by other Banks. This is a cost-location table—not an
application-ownership, control or exclusive-benefit table.

| Bank | Named major nonreimbursed System function | Accounting-system significance |
|---|---|---|
| Boston | Financial Support Office; Centralized Accounting Technology Services | All-twelve finance shared services and financial-platform support; no proof CATS owns EASy, ISA engine or CASPR |
| New York | SOMA management; Fedwire Funds and Securities; NSS | Market execution and named payment-service revenue coexist with all-twelve allocation |
| Philadelphia | Collateral Data Support; Collateral Management System; risk/data research; securities-data services | Collateral-data/technology locus; not collateral ownership |
| Cleveland | Cash product/technology; national audit; resilience/support; risk technology; payment efficiency/integrity/accessibility | Control-support functions; application rights remain separate |
| Richmond | Currency Technology Office; System Financial Planning & Management | Distinct from separately redistributed National IT computing/support costs |
| Atlanta | Check and ACH; OEB integrated into Atlanta | Named service revenue plus System pension sponsor accounting |
| Chicago | National customer relations and support | Distinct from electronic-access revenue |
| St. Louis | Treasury Relations and Support; administrative-services technology; learning center | System support; no generic accounting ownership |
| Minneapolis | No named major nonreimbursed function in Note 2 | FAM separately proves its billing-host role |
| Kansas City | Human Resources Product Strategy Center | HR strategy inside the Systemwide operating layer |
| Dallas | National credit-risk-management services | Risk-function location, not ownership of every credit exposure |
| San Francisco | Federal Reserve Financial Services; Statistics and Reserves | Enterprise payment-business cost location, not sole rail control |

The [all-twelve 2025 audited statements](https://www.federalreserve.gov/aboutthefed/audited-annual-financial-statements.htm)
are the primary source, generally Note 2.

### 8.1 Boston's current finance role

Current Boston leadership records say the Financial Support Office provides
accounting shared services to all twelve Banks and optimizes System
financial-technology platforms. Named components include Centralized
Accounting Technology Services, National Accounting and Customer Support,
Financial Management and Shared Services, a financial-planning CBAF and a
program-management office. FSO reports to the Conference of First Vice
Presidents.

This establishes national finance operations and platform management. It does
not identify CATS as the EASy controller, ISA engine, CASPR administrator or
Systemwide ERP owner.

Sources: [Breean Fortier](https://www.bostonfed.org/people/bank/breean-fortier.aspx),
[Christopher Ritchie](https://www.bostonfed.org/people/bank/christopher-h-ritchie.aspx),
and [Carl Madsen](https://www.bostonfed.org/people/bank/carl-madsen.aspx).

### 8.2 Richmond's current finance/technology role

Current Richmond records identify National IT, System Financial Planning &
Management, the National Procurement Office and an Enterprise Resource
Planning Support Office. NPO develops and executes certain national contracts
for collectively sourced goods/services and supports National IT.

Richmond is therefore a technology, financial-planning/ERP-support and
procurement node. Public records do not reveal its division of responsibility
with Boston FSO/CATS, the invoice-paying Bank, contract-specific obligor or
application-level asset owner.

Sources: [Richmond NPO](https://www.richmondfed.org/about_us/doing_business_with_the_bank/procurement_functions/),
[Reginal Bryant](https://www.richmondfed.org/press_room/our_news/2025/20250710_orbie_award),
and [Christin Patel](https://www.richmondfed.org/about_us/our_leadership/patel).

## 9. Evidence-constrained operating RACI

This is a research RACI derived from public records, not a disclosed Federal
Reserve charter.

| Object | Accountable / policy principal | Responsible / posting actor | Unresolved interface |
|---|---|---|---|
| FAM and exceptions | Board/RBOPS | RBOPS Financial Accounting Policy and Reporting | Delegation and exception file detail |
| Individual legal books and ICFR | Each Bank management and board | Bank CFO/accounting function | Common versus local application controls |
| System finance shared services | Conference of First Vice Presidents / FSO governance | Boston FSO/CATS and named groups | Application-by-application accountability |
| Systemwide ERP | System governance not fully public | Richmond ERPSO/support roles identified | Business owner, technical operator, module owners, Bank GL relation |
| Service billing receivable | Not public; Minneapolis's disclosed booking-host role does not establish the accountable business/system owner | Minneapolis billing-host function records the receivable | Application, cash, dispute and write-off chain |
| Named product revenue | Product/system accountability not established by revenue recognition | Boston/New York/Atlanta/Chicago are disclosed operators/revenue recognizers for named services | Provider, billing and cash crosswalk |
| Processing cost | Principal Bank bears transferred cost | Agent Bank performs processing | CASPR driver and monthly allocation file |
| InterFRB/ISA | Board/RBOPS controls FAM policy; operational ISA accountability is not public | Unnamed centralized system posts reciprocal entries | EASy identity, schema and authorization |
| National infrastructure | System IT governance plus Richmond corporate budget governance | System CIO/National IT and distributed workforce | Application control, release, incident and cost RACI |
| Selected national sourcing | Contract-specific authority not public | Richmond NPO | Participating Banks, signer, obligor, invoice payer |
| Software asset | Contract/agreement-designated owner; absent that, controlling CBAF/product/function office | Controller-hosting/capitalizing Bank, subject to Appendix D's contract and cloud-control rules | Developer, physical host and contracting Banks |
| CASPR allocation | Approval occurred through Conference of First Vice Presidents; current policy owner not named publicly | All Banks apply framework | Administrator, application, drivers, weights and change control |
| Combined reporting | RBOPS management | Banks submit FR 34/WTB; RBOPS combines | Elimination software/workpapers and edit controls |
| External audit | Bank audit governance; KPMG independent assurance | Bank management and KPMG | Materiality and application/control scope |

## 10. Combination and elimination map

| Flow | Individual Bank books | Combined twelve-Bank consequence |
|---|---|---|
| Customer billing | Minneapolis receivable; operator revenue; reciprocal ISA entries | External receivable and revenue remain; internal ISA positions net |
| Principal/Agent reimbursement | Principal expense; Agent expense credit | Transfer expense/credit net; Agent external payroll/vendor cost remains once |
| Richmond computing/support | Richmond gross cost and $1,135,000,000 expense credit; recipient charges | Internal credit/charges net; underlying external expense remains once |
| Nonreimbursed host function | Disclosed host-incurred cost remains at the host Bank without a reciprocal reimbursement; this does not prove all function cost resides there | Remains as combined expense because no reciprocal charge exists for the disclosed host-incurred cost |
| ISA | Due-to/from at individual Banks | Net zero; no combined ISA caption |
| Board/currency/CFPB assessments | Expense at Banks | Remain because Board/CFPB are outside twelve-Bank reporting perimeter |
| VIE | Bank-to-VIE position plus external VIE assets/liabilities | Intercompany items explicitly eliminated; external VIE amounts remain |
| Software transfer | Controller Bank records asset; another Bank may record development cost/transfer | Internal inter-Bank transfer nets; qualifying cost survives once in the controller Bank's software asset and later amortization, while noncapitalizable cost survives once as expense |

The general Reserve-Bank elimination workbook is not public. Except for the VIE
row, these are bounded combination consequences derived from FAM entry rules,
ISA's zero-sum design and audited Note 2 disclosures. VIE intercompany
elimination is expressly disclosed in the combined statements.

## 11. Claim audit

| Claim | Ruling |
|---|---|
| The twelve Banks now share one merged legal ledger. | **False / unsupported.** A Systemwide ERP exists, but current FAM and audited statements preserve twelve Bank books and one FR 34 per Bank. |
| The Systemwide ERP is EASy. | **Not publicly established.** Both are named, but no definitive crosswalk was located. |
| EASy is the unnamed centralized system in FAM §5.00. | **Not publicly established.** EASy has demonstrated Inter-FRB functions; §5.00 does not name its engine. |
| Boston CATS operates or owns EASy, CASPR and ISA settlement. | **Unsupported.** Boston's shared finance/platform role is real; application identity is absent. |
| CASPR replaced the legal general ledger. | **False.** CASPR replaced PACS as the cost-accounting framework. |
| A CASPR increase proves more cash was spent. | **False.** Documented reallocations and classification changes moved Bank/business-line cost without equal System spending. |
| Branch offices maintain separate balance sheets. | **False after 2014.** Branch accounting is consolidated to District head offices. |
| Minneapolis owns or operates each priced service because it books the receivable. | **Unsupported.** It is the billing host; revenue and product roles sit elsewhere. |
| New York owns Fedwire because it recognizes revenue. | **Unsupported as stated.** Official records separately establish New York as operator of Fedwire Funds, Fedwire Securities and NSS; revenue recognition alone does not prove infrastructure/application ownership or every control layer. |
| Richmond's $1,135,000,000 reimbursement is National IT vendor spending. | **Not established.** It is aggregate inter-Bank computing/support reimbursement and may redistribute underlying vendor, payroll, asset or other cost, but the mix and National IT segment are not disclosed. |
| Richmond owns all National IT software. | **Unsupported and inconsistent with treating Richmond ownership as a presumption.** Appendix D requires application-by-application control analysis, and no National IT application register is public. |
| The published 2025 National IT capital reduction proves cloud migration. | **Unsupported.** It is a budget/perimeter clock without application, contract, asset, expense and cash bridges. |
| KPMG's clean ICFR opinion certifies all payment rails and applications. | **False.** The opinion is material financial-reporting assurance, not universal cyber/SLA/finality assurance. |
| Waller's 2026 single-leader proposal has been implemented. | **Not established.** It remains a stated proposal/evaluation lane. |

## 12. Publicly unresolved objects

No reviewed official public record supplied:

### System identity and data lineage

- the current Systemwide ERP vendor/product and module inventory;
- the ERP-to-Bank-GL, ERP-to-CASPR, EASy-to-GL, ISA-to-EASy, WTB-to-RFARS or
  source-application field sequence;
- a current EASy system description, controller/host, interface inventory,
  journal-source catalog or data dictionary;
- proof identifying FAM §5.00's unnamed centralized system;
- current FR 34 Technical Memorandum No. 15 or transmission specification;
- the WTB schema, platform or ATB/Lawson-to-WTB migration record; or
- the complete RFARS report inventory and edit rules.

### Cost allocation

- the current complete CASPR Manual;
- current cost object, center, activity and business-line dictionaries;
- driver bases, weights, rates, true-up rules and change-control procedures;
- annual CASPR reports cited by FAM;
- Bank/application-level direct, support and overhead allocations;
- monthly service Principal/Agent estimates and actual true-up files; or
- FedNow revenue, PSAF attribution or official recovery percentage.

### Host, contract, asset and control

- a Boston FSO/CATS versus Richmond ERPSO/System Financial Planning &
  Management decision-rights matrix;
- EASy/CATS/FSO/San Francisco service-transfer history;
- National IT service agreements, catalogs, SLAs, scorecards, remedies and
  gross Bank/application charge schedules;
- NPO contract/award register, participating-Bank schedule, signature
  delegation, obligor, purchase order, invoice and paying Bank;
- application-level controller, developer, physical host, contract holder,
  capitalizing Bank, invoice payer and CASPR beneficiary; or
- software additions, transfers, disposals, impairments, vendors and clouds.

### Combination and assurance

- the combined inter-Bank elimination workbook;
- transaction-level ISA classifications;
- journal-entitlement, approval and segregation-of-duties matrices;
- annual close instructions, adjustment log and exception register; or
- KPMG materiality, significant-risk, IT-general-control, application-scope,
  journal-sample and test-population schedules.

These are bounded public negatives, not findings that the records do not exist.
No document request is authorized or transmitted by this artifact.

## 13. Ranked next retrieval wave

1. **CASPR constitution:** current manual, dictionaries, annual reports and
   change-control record.
2. **Application identity crosswalk:** Systemwide ERP, EASy, ISA engine, FR 34,
   WTB, RFARS and CASPR, with controller/host/vendor/module fields.
3. **Boston–Richmond finance RACI:** FSO/CATS, ERPSO, System Financial Planning
   & Management, NPO and National IT charters and service agreements.
4. **InterFRB/ISA specification:** message schema, journal map, approval rules,
   transaction classes and elimination treatment.
5. **Minneapolis billing constitution:** application, receivable aging,
   invoice-to-cash, suspense, write-off and operator-revenue interfaces.
6. **Shared-application register:** controller, capitalizing Bank, developer,
   physical host/cloud, contracts, invoice payer and CASPR beneficiary for
   EASy, Fedwire, FedNow, FedACH, NSS, FedLine and key accounting platforms.
7. **Gross-to-net ledgers:** Richmond computing/support and Principal/Agent
   service chargebacks tied to external payroll, vendors, assets and cash.
8. **Combined/audit proof:** elimination workpapers, annual close pack and
   KPMG application/control scope.
9. **Change clocks:** EASy host history, ATB/Lawson-to-WTB transition, 2026
   expense-disaggregation work and 2028 internal-use-software preparation.

## 14. Primary-source spine

- [January 2026 FAM](https://www.federalreserve.gov/aboutthefed/files/BSTfinaccountingmanual.pdf)
- [FAM Chapter 1 — Balance Sheet](https://www.federalreserve.gov/aboutthefed/chapter-1-balance-sheet.htm)
- [FAM Chapter 4 — SOMA](https://www.federalreserve.gov/aboutthefed/chapter-4-system-open-market-account.htm)
- [FAM Chapter 5 — Federal Reserve Notes](https://www.federalreserve.gov/aboutthefed/chapter-5-federal-reserve-notes.htm)
- [FAM Chapter 6 — Reporting Requirements](https://www.federalreserve.gov/aboutthefed/chapter-6-reporting-requirements.htm)
- [Legacy January 2017 FAM Chapter 6](https://www.federalreserve.gov/federal-reserve-banks/fam/chapter-6-reporting-requirements.htm)
- [FAM Appendix C — FR 34 Accounts](https://www.federalreserve.gov/aboutthefed/appendix-c-fr-34-accounts.htm)
- [FAM Appendix D — Software](https://www.federalreserve.gov/aboutthefed/appendix-d-software.htm)
- [2020 supervision-assessment methodology](https://www.federalreserve.gov/supervisionreg/supervision-regulation-assessment-2020.htm)
- [2021 supervision-assessment methodology](https://www.federalreserve.gov/supervisionreg/supervision-regulation-assessment-2021.htm)
- [2024 supervision-assessment methodology](https://www.federalreserve.gov/supervisionreg/supervision-regulation-assessment-2024.htm)
- [2021 Board performance report](https://www.federalreserve.gov/publications/files/gpra-performance-report-2021.pdf)
- [2022 Reserve Bank budget and implementation addendum](https://www.federalreserve.gov/foia/files/2022ReserveBankBudgets.pdf)
- [2025 Reserve Bank budget](https://www.federalreserve.gov/foia/files/2025ReserveBankBudgets.pdf)
- [2024 Annual Report budget chapter](https://www.federalreserve.gov/publications/2024-ar-federal-reserve-system-budgets.htm)
- [2024 Annual Report payment/Reserve Bank chapter](https://www.federalreserve.gov/publications/2024-ar-payment-system-and-reserve-bank-oversight.htm)
- [2025 combined Reserve Bank statements](https://www.federalreserve.gov/aboutthefed/files/combinedfinstmt2025.pdf)
- [All-twelve audited statements](https://www.federalreserve.gov/aboutthefed/audited-annual-financial-statements.htm)
- [Richmond 2025 statement](https://www.federalreserve.gov/aboutthefed/files/richmondfinstmt2025.pdf)
- [Boston 2025 statement](https://www.federalreserve.gov/aboutthefed/files/bostonfinstmt2025.pdf)
- [Payment System Risk Guide](https://www.federalreserve.gov/paymentsystems/files/psr_guide.pdf)
- [Waller, April 21, 2026](https://www.federalreserve.gov/newsevents/speech/waller20260421a.htm)

## 15. Controlling parent research

- [Federal Reserve Financial Constitution — vault source document](../sources/federal-reserve-financial-constitution-source-document-203118d0ec33.html)
- Federal Reserve System entity, transaction and software map
- Phase V shared services and reporting perimeters
- Phase VI National IT financial/asset bridge
- Richmond National IT governance/control RACI

## 16. Completion gate

The public accounting-system map is complete for human review when:

- every named system is separated from the record it produces;
- every Bank role is labeled as booking, billing, operating, controlling,
  developing, hosting, contracting, paying, allocating, reporting or auditing;
- the 2014, 2018 and 2021 transitions remain separate clocks;
- Systemwide ERP is not misread as a merged legal ledger;
- historical PACS mechanics are not passed off as current CASPR rules;
- internal allocation/elimination never becomes external spending; and
- unresolved interfaces are marked Not public rather than inferred.
