> Source cutoff: 2026-07-30

# Education Grant Administration and Ledger Interlock — 2026-07-30

## Controlling finding

The education-grant transition is a concrete test of the accounting architecture
described in this package.

The evidenced change is not that Congress has generally repealed the education
programs, converted them into unrestricted block grants, or transferred all
legal authority out of the Department of Education (ED). The evidenced change
is that ED has used Economy Act interagency agreements (IAAs) to place parts of
grant administration, personnel, systems and payment operations at the
Departments of Labor (DOL), Health and Human Services (HHS), Interior (DOI) and
State while retaining specified statutory, policy, oversight or final-authority
functions.

That separates functions that a conventional agency-level report can compress:

```text
Congress and program statute
  → ED appropriation and statutory responsibility
  → Economy Act IAA
  → Form 7600B obligation and/or IPAC interagency transfer
  → servicing agency administration
  → grant-management and payment system
  → State, LEA, university or other recipient
  → subrecipient, vendor, payroll or beneficiary use
  → performance evidence
  → audit finding, correction, debt or recovery
```

The architecture can reduce duplicate interfaces for recipients while
increasing the importance of a joined government record. Without stable
identifiers and explicit responsibility fields, the appropriation owner,
ordering agency, servicing agency, award issuer, payment-system operator,
recipient-facing official, performance reviewer and audit-resolution owner can
appear to describe different transactions.

## 1. Relationship to existing Observatory research

This note extends rather than replaces the July 28, 2026 package:

`Education/University Funding and Programmable Compliance 2026-07-28`

That package already established:

- a university is a multi-entity funding junction rather than one ledger
  object;
- Title IV aid, research grants, State support, tax-exempt debt, clinical
  revenue and donations use different legal paths and identifiers;
- Form 990, IPEDS, Single Audit, USAspending and agency payment systems operate
  on different objects and clocks;
- Treasury and GAO built a permissioned research-grant blockchain prototype,
  but it moved no real grant money and did not become policy or production;
- federal controls are moving toward recipient identity, award identity,
  eligibility and payment-purpose evidence before disbursement.

The new contribution is the **interagency administration seam**: the same
legally authorized education program can now be owned, administered, paid,
reported, audited and corrected through more than one federal entity or system.

## 2. What changed, by pathway

Status words in this table are deliberately narrow. “Announced” is not
“operating”; an IAA is not proof that every covered award has migrated.

| Pathway | Located operative object | Administration and system state | Authority retained by ED | Evidence state at cutoff |
|---|---|---|---|---|
| Perkins V and WIOA Title II | May 2025 ED-DOL workforce-development IAA and July 2025 implementation announcement | DOL performs day-to-day administration; ED reported all grantees onboarded to GrantSolutions and PMS. The January 2026 K-12 fact sheet reports 1,627 payment requests totaling $575 million from 51 States and territories under this predecessor partnership. | ED states it retains statutory responsibility, policy authority and oversight. | **Operating, with quantified payment activity reported by ED** |
| K-12 ESEA and related programs | November 2025 ED-DOL IAA and official four-page fact sheet | DOL is to provide grant-administration services for Title I Parts A-D, Title II-A, Title III-A, Title IV-A/B, rural programs, Impact Aid and listed competitive programs. ED says States will receive covered formula funds from DOL. Program-by-program migration timing remains an implementation question. | ED maintains statutory responsibilities and oversight; statutory eligibility is stated to remain unchanged. | **IAA established; servicing model specified; full program migration not demonstrated by one aggregate record** |
| OPE postsecondary grants | November 2025 ED-DOL IAA, January 2026 staff-detail announcement and official fact sheet | ED Higher Education Programs staff began detail to DOL in the week of January 20. FY2025 and earlier awards use ED G5; FY2026 and later awards use DOL GrantSolutions and HHS PMS for drawdowns. | ED retains responsibility, policy authority, civil-rights jurisdiction for ED statutes and oversight. | **Implementation underway; award-cohort system split expressly documented** |
| Native education | November 2025 ED-DOI IAA and fact sheet | DOI takes a greater role in elementary, secondary, higher, career-technical and vocational-rehabilitation program administration for Native students and Tribes. | ED retains statutory responsibility and policymaking/oversight as described by the partnership. | **IAA established; program implementation must be tested by award and system** |
| CCAMPIS | November 2025 ED-HHS partnership | HHS is to manage existing competitions and technical assistance and integrate the program with HHS child-care grant expertise. | The source describes ED oversight but does not support treating the Higher Education Act authority as repealed or transferred by statute. | **Partnership established; transaction-level migration evidence not yet joined here** |
| Family engagement and school support | February 20, 2026 ED-HHS IAA, with July 23 addendum | HHS supports monitoring, drawdown oversight, program administration, technology and new awards. ED transfers funding; IPAC may be used; quarterly reconciliation and written issue resolution are required. | ED retains program leadership, internal-control monitoring, audit resolution, GPRA/Congress reporting, annual report review, certain State award operations and final statutory authority. | **Executed IAA with unusually detailed funding, reconciliation and responsibility clauses** |
| Foreign-language and international education | November 2025 ED-State partnership | State takes a greater role in Fulbright-Hays administration and related funding/data coordination. | Program law and ED functions must be read from the operative agreement and award terms; the press release alone does not prove complete legal transfer. | **Partnership announced; exact operating handoff requires program-level instruments** |
| Workforce Pell | Final rule effective July 1, 2026 | Expands Pell eligibility to qualifying short-term workforce programs. This is a Title IV student-aid change, not evidence that the OPE grant IAA moved Pell administration to DOL. | ED/Federal Student Aid authority and Title IV systems remain the relevant starting point unless a separate operative instrument says otherwise. | **Final program rule; separate from the grant-administration IAA path** |

## 3. The most revealing documents

### A. OPE's award-cohort split

The postsecondary fact sheet says the intended recipient experience is a single
administering agency, but the actual system of record depends on the award's
initial fiscal year:

```text
FY2025 or earlier award → ED G5
FY2026 or later award   → DOL GrantSolutions + HHS Payment Management System
```

This is not described as duplicative reporting because each award cohort uses
one path. It is still a major accounting fact: the same recipient and statutory
program can have concurrent awards on two system stacks. Entity-level totals,
draw histories, receivables, advances, closeout status and audit samples must
retain the award vintage and source system.

### B. The ED-HHS agreement's internal federal ledger

The February 2026 ED-HHS agreement makes the hidden interagency layer visible:

- ED transfers appropriated amounts and carryover needed for the covered work;
- HHS performs reimbursable services and makes/administers new awards;
- ED initiates any agreed IPAC transfer as provider; HHS is receiver;
- the agencies reconcile revenue and expense balances at least quarterly;
- reconciliation issues must be written and their resolution documented within
  30 calendar days;
- the umbrella IAA itself obligates no funds; individual Form 7600B orders do;
- ED may send lump sums for grants and contracts;
- personnel details are governed and paid under separate agreements;
- each agency remains responsible for liability arising from its own conduct.

That is already a multi-party event model, even though it is not a blockchain.
The federal accounting objects are not interchangeable:

```text
IAA authority
≠ Form 7600B obligation
≠ IPAC transfer
≠ HHS revenue/expense recognition
≠ recipient award
≠ recipient cash draw
≠ allowable expenditure
≠ program outcome
≠ audit resolution
```

## 4. The responsibility matrix

The accounting system should not force one agency label to carry every meaning.

| Function | Required responsible-party field |
|---|---|
| Program statute and policy | statutory owner / policy authority |
| Appropriation and budget execution | Treasury account and budgetary owner |
| Interagency ordering | ordering agency and ordering official |
| Servicing work | servicing agency and program office |
| Obligation | obligating instrument, Form 7600B or award action and official |
| Interagency settlement | IPAC sender, receiver, amount, date and reference |
| Recipient award | awarding agency shown to recipient, FAIN, UEI and program |
| Grant administration | grants officer, system and award cohort |
| Cash draw | payment system, draw request, approval, release and settlement |
| Program performance | reporting recipient, reviewer and acceptance state |
| Internal control | control owner and operating evidence |
| Civil rights / privacy | enforcing office and protected-data authority |
| Single Audit / finding | cognizant or oversight agency and finding owner |
| Corrective action / recovery | decision authority, collector and superseded event |

## 5. Minimum event schema for an education grant

The record should preserve one chronology without pretending all fields belong
on a public chain.

| Event class | Minimum fields |
|---|---|
| `appropriation_authorized` | public law, program authority, Treasury account, period of availability, amount |
| `interagency_service_authorized` | IAA ID, Economy Act determination, ordering agency, servicing agency, scope, start/end, version |
| `interagency_order_obligated` | Form 7600B/order ID, appropriation, amount, purpose, obligating official |
| `ipac_transfer_posted` | IPAC reference, sender, receiver, amount, date, accounting treatment |
| `award_created_or_modified` | FAIN, assistance listing, UEI, recipient, award cohort, funding source, servicing agency, award terms |
| `draw_requested` | award ID, amount, purpose category, requester, source system, timestamp |
| `draw_approved_or_rejected` | decision, official/control, reason code, available balance, supersession link |
| `cash_settled` | Treasury/payment reference, settlement date, amount, receiving account token or protected reference |
| `downstream_commitment` | subaward/contract/payroll class, downstream UEI/vendor/employee token, amount, flow-down rule |
| `cost_incurred` | cost class, service period, source evidence, allowability rule version, related obligation |
| `performance_submitted` | metric, period, population, methodology, submitter, protected evidence reference |
| `performance_accepted_or_challenged` | reviewer, decision, exception, remediation clock |
| `audit_finding_opened` | audit/report ID, questioned cost, criteria, responsible entity, response due |
| `correction_or_recovery` | original event, corrected state, debt/return amount, authority, cash settlement, public explanation |

Every material amendment should append a superseding event. Silent overwrites
destroy the chronology needed to decide which agency, rule, system and award
state controlled at the time.

## 6. Public, protected and restricted layers

Education is a strong argument for a hybrid record, not for publishing student
files.

### Public transaction and authority layer

- program and appropriation authority;
- ordering and servicing agencies;
- IAA and Form 7600B identifiers;
- award, recipient UEI and public FAIN;
- amount, purpose category, draw status and settlement date;
- program-level performance metrics and methodology;
- audit findings, questioned costs, corrections and recoveries;
- event hashes and supersession links.

### Protected evidence layer

- student-level eligibility and enrollment;
- FAFSA and tax-derived identity attributes;
- disability and individualized education records;
- grades, attendance and personally identifiable performance records;
- employee payroll and bank information;
- investigative leads and fraud models;
- commercially or security-sensitive vendor information.

Public proof can show that a protected record existed, was signed by an
authorized party, satisfied a named rule version and was later corrected,
without publishing the underlying student data. FERPA and other program-specific
privacy rules remain legal constraints; a hash is not a waiver of those rules.

## 7. What smart contracts could and could not do here

### Strong automation candidates

- reject a draw above the available award balance;
- route a request to the servicing agency while preserving ED as statutory
  owner;
- require the applicable award cohort and payment-system identifier;
- enforce period-of-availability and matching requirements whose inputs are
  objective;
- require a subaward flow-down event before release of a later tranche;
- open reconciliation exceptions when IPAC, award and payment totals diverge;
- carry the exact program-rule and award-term version used for a decision;
- publish a correction that points to, rather than erases, the original event.

### Judgment and evidence that remain outside the code

- whether a student, school or cost is legally eligible when facts are disputed;
- whether services were actually delivered or educational performance occurred;
- whether a cost is reasonable, allocable and adequately documented;
- whether a disability, privacy or civil-rights rule permits a particular use;
- whether a side agreement changes the economic substance;
- whether colluding parties submitted false but internally consistent evidence;
- whether an outcome measure is valid rather than merely computable;
- how final authority is exercised when ED and a servicing agency disagree.

The code can execute the rule it was given. It cannot prove that the rule was
lawful, the oracle was truthful, the entity perimeter was complete or the
educational claim was real.

## 8. Accounting and audit consequences

### Reconciliation may move rather than disappear

The administration can simplify the grantee's interface while adding an
ED-to-servicing-agency reconciliation. The ED-HHS agreement expressly requires
quarterly balance reconciliation. A common event spine could make that
reconciliation continuous, but only if the agencies share identifiers,
definitions and correction rules.

### Award vintage becomes a control field

For affected postsecondary grants, FY2025-and-earlier awards and FY2026-and-
later awards occupy different stacks. An audit population that queries only G5
or only GrantSolutions/PMS can be incomplete without appearing mathematically
wrong.

### The legal owner and operational actor must remain separable

Reporting a covered payment simply as “DOL education spending” can obscure ED's
appropriation and statutory role. Reporting it only as “ED spending” can
obscure which agency administered, approved and paid the award. Both identities
belong in the event.

### Single Audit does not close the whole chain

A recipient audit can test compliance and selected major programs but does not
by itself reconcile ED's appropriation, the interagency order, IPAC settlement,
the servicing agency's award record, every downstream payment, protected
student evidence and later federal recovery. The federal and recipient records
need a join key.

## 9. Claim audit

| Claim | Ruling | Factual correction |
|---|---|---|
| “The Department of Education has been abolished.” | **False at cutoff** | Only Congress can repeal the department's statutory existence. Functions and staff have been shifted, but ED remains a legal entity with retained duties. |
| “Education funding was sent directly to States with no federal intermediary.” | **Not generally supported** | For covered K-12 programs ED says States will receive formula funds from DOL, while ED retains statutory responsibilities and DOL becomes the servicing federal agency. |
| “The partnerships changed program eligibility.” | **Not supported by the cited fact sheets** | ED states statutory requirements and eligibility remain in effect; later rules or award terms must be assessed separately. |
| “All education grants moved from G5 to PMS.” | **False** | The documented OPE transition is cohort-based: FY2025/prior awards remain in G5; FY2026/future awards use GrantSolutions and PMS. Pell/Title IV should not be swept into this grant list without a separate instrument. |
| “The handoffs decentralize federal control.” | **Mixed** | They redistribute administration among federal agencies and may simplify recipient contact. ED retains enumerated policy, oversight and final-authority functions; shared federal systems may also centralize payment data. |
| “The agreements are a blockchain program.” | **False** | The located agreements use conventional federal agreements, IPAC, GrantSolutions, G5 and PMS. They create a use case for joined event accounting but do not select DLT. |
| “A public ledger should expose student transactions.” | **Reject** | Public authority, organization-level payment, correction and audit events can be disclosed while protected student evidence remains access-controlled. |
| “A single payment-system total proves the whole transition is operating.” | **False** | The reported 1,627 requests/$575 million concerns the predecessor workforce partnership and cannot be imputed to every K-12, OPE, HHS, DOI or State program. |

## 10. Watchboard

Promote the education-grant transition only on a new operative object or
observed system consequence.

| Surface | Promotion object | Exact question |
|---|---|---|
| ED/DOL K-12 | grantee notice, award document, system guide or first quantified payment set | Which named ESEA programs have actually begun award and draw activity through DOL? |
| ED/DOL OPE | award notices and system records by fiscal-year cohort | Do FY2026 awards consistently show DOL administration, GrantSolutions and PMS while preserving ED program authority? |
| ED/HHS | Form 7600B, IPAC/reconciliation evidence, award notice or annual report | Can an ED appropriation be joined to the HHS interagency receipt, recipient award, draw and ED audit-resolution record? |
| ED/DOI and ED/State | operative IAAs, notices and system instructions | Which programs, personnel, awards and payment systems have actually migrated? |
| USAspending | agency/program/award attribution changes | Does public data identify both statutory/ordering and servicing agencies or collapse the relationship? |
| Treasury/GSDM | new interagency and award lineage fields | Are IAA, Form 7600B, IPAC, FAIN, payment and correction IDs joined in the governmentwide model? |
| FAC / Single Audit | audit-guidance and cognizant-agency changes | Who resolves findings for awards administered by a servicing agency under ED authority? |
| Privacy | FERPA/program guidance for cross-agency processing | What is the lawful basis, access model, retention rule and correction procedure for protected education data shared with servicing agencies? |
| Workforce Pell | FSA implementation records | Keep Title IV student-aid eligibility and disbursement separate from the OPE grant-administration migration unless an operative document joins them. |

## 11. Bottom line for the accounting-transition thesis

Education grants expose why “one public ledger” cannot mean one undifferentiated
table of payments.

The useful object is a **federated, append-only transaction record** that keeps
legal authority, budget ownership, servicing work, payment, protected evidence,
performance, audit and correction distinct but joinable.

This case strengthens the broader thesis:

> The revolutionary change is not replacing every accounting basis with cash.
> It is replacing repeated, lossy reconstruction with a common signed event
> history from which budgetary, proprietary, cash, compliance, performance and
> public-accountability views can be reproduced.

## Primary sources

- [ED — Six new agency partnerships, November 18, 2025](https://www.ed.gov/about/news/press-release/us-department-of-education-announces-six-new-agency-partnerships-break-federal-bureaucracy)
- [ED-DOL — Workforce partnership implementation, July 15, 2025](https://www.ed.gov/about/news/press-release/us-department-of-education-and-us-department-of-labor-implement-workforce-development-partnership)
- [ED-DOL — Postsecondary implementation steps, January 15, 2026](https://www.ed.gov/about/news/press-release/us-department-of-education-and-us-department-of-labor-take-next-steps-implement-postsecondary-education-partnership)
- [ED-DOL — Elementary and Secondary Education Partnership fact sheet](https://www.ed.gov/media/document/fact-sheet-department-of-education-ed-and-department-of-labor-dol-elementary-and-secondary-education-partnership-112465.pdf)
- [ED-DOL — Postsecondary Education Partnership fact sheet](https://www.ed.gov/media/document/fact-sheet-department-of-education-ed-and-department-of-labor-dol-postsecondary-education-partnership-112464.pdf)
- [ED-DOI — Indian Education Partnership fact sheet](https://www.ed.gov/media/document/fact-sheet-department-of-education-ed-and-department-of-interior-doi-partnership-112463.pdf)
- [ED-HHS — Family Engagement and School Support IAA and July 23 addendum](https://www.ed.gov/media/document/interagency-agreement-ed-and-hhs-family-engagement-and-school-support-february-23-2026-113311.pdf)
- [ED — Four additional agency partnerships, June 16, 2026](https://www.ed.gov/about/news/press-release/us-department-of-education-announces-additional-partnerships-strengthen-coordination-individuals-disabilities-programs-bolster-civil-rights)
- [Federal Student Aid — 2025–2026 Handbook, requesting and managing Title IV funds](https://fsapartners.ed.gov/knowledge-center/fsa-handbook/2025-2026/vol4/ch1-requesting-and-managing-title-iv-funds)
- [ED — Workforce Pell final rule](https://www.ed.gov/about/news/press-release/us-department-of-education-issues-final-rule-create-new-workforce-pell-grant-program)
- [Federal Student Aid — Workforce Pell effective dates](https://fsapartners.ed.gov/knowledge-center/library/electronic-announcements/2026-06-04/effective-dates-workforce-pell-and-federal-pell-grant-ineligibility-provisions)
- [31 U.S.C. § 1535 — Economy Act](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title31-section1535)
