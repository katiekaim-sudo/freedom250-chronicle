# Government Open Ledger Deep Dive — 2026-07-30

**Research date:** 2026-07-30  
**Scope:** U.S. federal public-money record, with an education-grant case map  
**Method:** Primary federal sources only. Current operations, legal requirements, prototypes, and proposed designs are kept separate.

## Executive finding

The United States does not have one public, transaction-level record that follows a dollar through:

> appropriation → apportionment → agency allotment → obligation/award → payment request → agency certification → Treasury issuance/settlement → recipient receipt → subrecipient/vendor/payroll use → performance evidence → audit finding → management decision → debt → collection/recovery → correction

It has a **federation of authoritative records**. Different entities control different facts:

- Congress controls enacted budget authority and program law.
- OMB controls executive-branch apportionments.
- Each agency controls allotments, obligations, program eligibility, entitlement, and its general ledger.
- Treasury controls federal account symbols, central cash-accounting records, payment processing, and central collection services.
- Prime recipients and pass-through entities control downstream accounting, subaward classification, and much of the performance evidence.
- Independent auditors control audit opinions and findings.
- Awarding agencies or pass-through entities—not auditors—control management decisions that sustain or reject findings and establish required corrective action.
- Creditor agencies control the validity and official accounting record of federal debts even when Treasury services or collects them.

The strongest factual design is therefore not “put all government spending on a public blockchain.” It is:

1. preserve each protected authoritative system;
2. require a common signed event envelope and durable cross-system identifiers;
3. make corrections additive through reversals and superseding events;
4. publish a privacy-filtered public projection and cryptographic commitments to protected evidence;
5. give auditors read-only access to the full authorized record; and
6. keep legal responsibility attached to the entity that made each assertion.

This is a **hybrid append-only record architecture**, not proof that blockchain is necessary. Treasury and JFMIP’s own work supports the potential for shared transactional visibility and lower reconciliation burden, while expressly identifying legal, cybersecurity, governance, legacy-integration, and audit-methodology challenges.

## 1. The public-money chain: who owns each fact

| Stage | Controlling entity / authoritative record | Important identifiers | Public state today | Protected or missing state | Correction / reversal reality |
|---|---|---|---|---|---|
| Program authorization and appropriation | Congress; enrolled public law and Statutes at Large | Public law, account/program language, fiscal year | Public text | Legislative drafting and pre-enactment material may be nonpublic | Later statute, rescission, transfer, reprogramming where authorized |
| Treasury account establishment and warrant | Treasury Fiscal Service, in collaboration with OMB and agency; FAST Book and CARS | TAS/TAFS: agency identifier, availability period, main/subaccount | FAST Book publishes account symbols/titles; Treasury reports are public | Detailed agency request/approval workflow and user records | Account amendment; warrant/account adjustment; CARS history |
| Apportionment | OMB under 31 U.S.C. §§ 1512–1513; OMB apportionment system | TAFS, line category, time/program/project, footnote, approval iteration | Approved apportionment documents are posted at `apportionment-public.max.gov`; statutory direction requires release within two business days | Internal formulation, deliberation, system access, some supporting material | Reapportionment is a new approved iteration; “A” footnotes have legal effect |
| Allotment / suballotment / allocation | Agency funds-control official and agency core financial system | Internal fund code, organization, program, project, object class, allotment document | No government-wide public allotment dataset | Usually internal; may contain operational plans and sensitive program detail | Agency funds-control adjustment within legal/apportioned limits |
| Commitment | Agency program/procurement office and core financial system | Requisition/commitment ID, TAS, internal coding | Generally not public as a government-wide record | Internal planning/reservation before an obligation | Release, modification, or conversion to obligation |
| Obligation and award | Agency grants/procurement official; agency award system and general ledger | FAIN for assistance; PIID for procurement; UEI; Assistance Listing; TAS; USSGL budgetary accounts | FABS/FPDS/SAM-derived award actions and USAspending transaction histories; periodic DATA Act financial data | Full award files, evaluations, legal reviews, invoices and sensitive recipient data | Award modification/deobligation; FABS correction/delete; agency ledger adjustment—these are not automatically the same event |
| Recipient payment request / draw | Recipient plus awarding agency/payment platform such as G6/G5, PMS or ASAP | Award ID, payee account, request ID, amount, period | Usually reflected later as award outlay data, not as a complete public draw-request object | User credentials, bank data, supporting cash need, detailed request and review | Recipient adjustment/return; payment-system correction; award/ledger adjustment |
| Payment certification | Agency certifying officer in SPS/ASAP/other approved workflow | ALC, SPS schedule, SF 1166 summary, CO credential/signature, TAS/BETC | No complete public schedule-and-signature record | Payee/TIN/bank information, officer/security records and payment details | Pre-release schedule rejection, cancellation, replacement, or corrected schedule |
| Treasury issuance and settlement | Fiscal Service disbursing officer and PAM; ACH/Fedwire/check rails; PIR/PACER/TCIS for status and post-payment | Schedule/control totals, payment ID, ACH trace/check serial/wire reference, issue/settlement/return status | Aggregate fiscal reports; some vendors can see their own payment status; USAspending may publish related award outlays | Individual payment records, TIN, bank account, offset and claims details | Return, cancellation, reclamation, reissue, offset, or post-payment claim |
| Central cash classification | Treasury CARS | ALC + TAS + BETC + source transaction | MTS/Combined Statement and other aggregates | Transaction-level central accounting and reconciliation access is controlled | Reclassification, reversal, agency adjustment, corrected TAS/BETC |
| Agency accrual/budgetary accounting | Agency core ledger using USSGL; GTAS adjusted trial balances; CARS Fund Balance with Treasury | TAS, USSGL account, trading partner, program activity, object class and other attributes | Audited agency statements and government-wide reports; DATA Act extracts | Journal detail, subledgers, support, manual adjustments, control evidence | Journal/reversal, GTAS resubmission, CARS correction; may not alter public award record automatically |
| Prime-recipient expenditure | State, local government, university, nonprofit or other recipient’s financial system | FAIN, UEI, recipient fund/project, payroll/vendor/invoice IDs | Usually summarized in reports/audits; not transaction-level government-wide public data | General ledger, payroll, invoices, eligibility files, procurement files | Recipient journal, refund, credit, cost transfer, reclassification |
| Subaward | Prime/pass-through entity; subaward agreement and recipient accounting | Parent FAIN, subrecipient UEI, subaward ID, Assistance Listing | FFATA subaward reporting through SAM/FSRS and USAspending provides bounded public visibility | Full agreement, invoices, detailed expenditure and monitoring files | Subaward amendment; upstream reporting correction; recipient ledger adjustment |
| Vendor / payroll / beneficiary use | Recipient or subrecipient | Vendor ID, employee ID, invoice/payroll/beneficiary eligibility record | Generally not public transaction data | PII, bank/tax/payroll, procurement-sensitive and student/health data | Refund, payroll correction, void, chargeback, disallowance |
| Performance | Recipient/subrecipient, pass-through entity, and program agency | Award ID plus performance measure, reporting period and evidence reference | Program-specific aggregate reports and open datasets; uneven award linkage | Source evidence, case-level data and PII; many narrative reports live in grant systems | Amended report, restatement, data-quality correction |
| Single Audit | Auditee and independent auditor; Federal Audit Clearinghouse | UEI, report ID, Assistance Listing, finding reference, questioned cost | FAC publishes report packages and API data, except protected Tribal submissions | Audit workpapers and some Tribal data; audit is risk-based and periodic | FAC resubmission/version; auditor correction |
| Management decision | Awarding federal agency, cognizant agency, or pass-through entity | Audit finding reference, decision, disallowed amount, corrective action | Not available as one complete, government-wide structured public dataset | Agency case files, legal analysis, appeals | Decision can sustain, modify, or reject finding; appeal may alter result |
| Federal debt | Creditor agency; agency receivable/debt record | Agency debt ID, debtor/TIN, award/finding linkage if retained | Aggregate receivables/debt reporting | Debtor identity, due-process notices, evidence, dispute and account status | Adjustment, compromise, suspension, termination, discharge |
| Treasury servicing / recovery | Fiscal Service CRS, Cross-Servicing and TOP; creditor agency remains owner | Agency debt ID, collection case, payment/offset transaction | Program aggregates and general process information | Case-level debt and offset data | Collection, offset, refund, reversal, compromise; servicing transfer is not collection |
| Public correction | Source agency + Data Broker/USAspending/FAC or other publisher | Source key, correction/delete indicator, report version | FABS and FAC have explicit correction/version mechanics | No universal causal or supersession link across all systems | A public correction does not itself reverse cash, change the general ledger, determine allowability, or collect debt |

### Governing non-equivalences

These objects must never be collapsed:

- appropriation ≠ apportionment ≠ allotment;
- commitment ≠ obligation;
- obligation ≠ outlay;
- agency-certified payment ≠ Treasury settlement;
- Treasury settlement ≠ recipient allowable expenditure;
- prime-recipient expenditure ≠ subrecipient/vendor/payroll expenditure;
- program output ≠ verified outcome;
- improper payment ≠ fraud;
- audit finding ≠ sustained finding;
- questioned cost ≠ disallowed cost;
- disallowed cost ≠ established debt;
- debt referral ≠ collection;
- deobligation ≠ cash refund;
- USAspending correction ≠ ledger reversal or cash reversal.

GAO describes the appropriations-accounting sequence as appropriation → apportionment → allotment → obligation → payment/liquidation. The chain is legally important because recording an obligation reduces unobligated allotment authority, while payment liquidates the obligation. FASAB separately requires reconciliation between accrual net cost and budgetary net outlays because depreciation, liabilities, asset acquisitions, inventory, and other timing/measurement items make those views different.

## 2. What is already open—and what “open” means

### 2.1 Open-source software

Open-source software means the program code can be inspected and reused. It does **not** establish that data are complete, authentic, legally authoritative, or public.

Operating examples:

- Treasury’s DATA Act Broker backend is public code. It ingests agency financial and award-system submissions, validates them, and standardizes them against the Governmentwide Spending Data Model.
- The USAspending API and website code are public.
- The GSA Federal Audit Clearinghouse works in the open and exposes code/project work as well as a public API.
- Treasury published code from an early blockchain proof of concept.

An open-source front end can faithfully display a false or incomplete source submission. Code openness is valuable for rule transparency and reproducibility, but authenticity requires signed source events, control ownership, and lineage.

### 2.2 Open standards

Open standards define how records should be classified or exchanged:

- Treasury Account Symbols / TAFS identify appropriation and fund accounts.
- USSGL supplies a uniform federal chart of accounts, account descriptions, attributes, transaction guidance, crosswalks, and GTAS validations.
- TAS-BETC classifies CARS payment, collection, and intragovernmental events.
- The Governmentwide Spending Data Model (formerly DAIMS) defines DATA Act elements, file interfaces, domains, and validation rules.
- Treasury’s federal financial-management standards define business functions, activities, capabilities, use cases, data elements, and information exchanges.

Standards improve comparability. They do not prove that an underlying invoice, student, service, or performance claim is true.

### 2.3 Open data

Open data are public records or extracts:

- statutes, appropriation acts, and program authorities;
- the FAST Book;
- approved OMB apportionments and associated footnotes;
- USAspending award, account, and subaward data and APIs;
- FiscalData and Treasury fiscal reports;
- FAC Single Audit packages and APIs, subject to Tribal suppression;
- agency financial statements and selected program-performance datasets.

USAspending is a publication and analysis layer, not the federal general ledger or the bank-settlement ledger. Its own architecture imports agency Data Broker submissions, reformats some fields, and creates award “holder” objects from transaction records for usability. DATA Broker validation includes exact cross-file checks, but several rules warn that the Broker cannot determine which upstream element is wrong and directs the agency back to source information.

### 2.4 A verifiable authoritative record

A verifiable record requires more than public data:

- the authoritative owner of the fact;
- the actor’s authority and digital signature;
- an event timestamp and durable event ID;
- the source record and evidence hash;
- lineage to parent, causal, reversal and superseding events;
- immutable history or equivalent tamper-evident controls;
- access classification and privacy policy;
- a correction mechanism that does not silently overwrite history; and
- reconciliation to the legally relevant system of record.

Today, pieces exist. SPS uses designated officers, PKI credentials, legal certification, ALC matching and separation of duties. PAM validates certified control totals and payment formats. CARS is Treasury’s electronic system of record for government financial data and requires TAS-BETC classification. FAC preserves resubmission/version relationships. FABS uses explicit correction/delete indicators and unique award-action keys. There is no common event envelope joining them all.

## 3. Where the record breaks

### 3.1 The allotment gap

OMB apportionments are now machine-accessible public documents, but agency allotments and suballotments are not a government-wide public dataset. That leaves a gap between OMB’s legally binding release of budgetary resources and the internal funds-control limits under which an agency official incurs an obligation.

### 3.2 The entitlement–certification–settlement split

Treasury’s PAM privacy/control documentation states:

- payment data come from federal program agencies;
- each agency is responsible for accuracy;
- the agency certifies data as complete and accurate;
- PAM validates the file and certified control totals; and
- Fiscal Service maintains no file establishing the payee’s underlying program entitlement.

Therefore a Treasury-settled payment proves payment processing and settlement, not underlying eligibility, allowability, delivery, or performance.

### 3.3 The recipient-use gap

Uniform Guidance requires a pass-through entity to identify each subaward with FAIN, UEI, Assistance Listing, obligated amount and other fields; assess fraud/noncompliance risk; review financial and performance reports; monitor significant developments; resolve award-specific audit findings; and verify Single Audit compliance.

Those requirements create records, but the records mainly remain with the pass-through entity. FFATA subaward reporting publishes a bounded award-level edge; it does not publish every downstream invoice, payroll charge, beneficiary determination, cost transfer, refund or performance artifact.

### 3.4 The finding–debt–recovery gap

Under 2 CFR 200.521, a management decision must state whether the audit finding is sustained, explain why, and state whether repayment, financial adjustment or other action is required. The responsible federal agency or pass-through entity has six months after FAC acceptance to issue it.

Only after the recipient is determined to have received more than it was entitled to does 2 CFR 200.346 characterize the excess as a debt to the federal government. Treasury may then provide receivables servicing, cross-servicing or offset, but the creditor agency continues to maintain the official debt and accounting records.

FAC exposes the finding. There is no complete public government-wide join from:

> FAC finding reference → management decision → disallowed amount → agency debt ID → Treasury referral → collection transaction → final closure.

### 3.5 The correction gap

Each system corrects a different fact:

- OMB reapportions budgetary resources.
- Agencies adjust allotments and ledgers.
- Award systems modify or deobligate awards.
- FABS corrects or deletes a published award-action record.
- SPS/PAM cancels, rejects, returns or reissues payments.
- CARS reclassifies TAS/BETC accounting.
- Recipients post credits, refunds and cost transfers.
- FAC accepts resubmissions.
- Management decisions sustain or reject findings.
- Debt systems adjust, compromise, collect or discharge debt.

Without common causal and supersession identifiers, a negative amount can be mistaken for a recovery, a deobligation for a refund, or a public-data correction for a cash reversal.

## 4. A workable hybrid append-only design

### 4.1 Design principle

Do not copy every sensitive record onto a public chain. Create a shared, signed **event constitution** across authoritative systems.

Each system continues to own its legal fact. It emits a common envelope:

```text
event_id
event_type
authoritative_entity
authoritative_system
actor_role
actor_credential_or_signature
event_time
effective_time
amount_and_unit
legal_basis
TAS_TAFS
FAIN_or_PIID
UEI
ALC
program_activity_object_class
parent_event_id
causal_event_id
reverses_event_id
supersedes_event_id
evidence_hash
evidence_location
visibility_class
retention_rule
control_result
dispute_or_appeal_state
```

Payment-specific identifiers such as SPS schedule, PAM payment ID, ACH trace, check serial, bank account and TIN should be tokenized or kept in a protected object store. The public layer can expose a non-reversible public correlation ID and cryptographic commitment.

### 4.2 Three layers

1. **Protected operational event layer**
   - Permissioned participants: Congress/OMB where relevant, agencies, Treasury, pass-through entities and authorized recipients.
   - Full signed events, protected identifiers, evidence pointers and role-based access.
   - Append-only correction semantics.

2. **Auditor and oversight layer**
   - Read-only nodes or equivalent query access for GAO, OIGs, independent auditors and authorized program monitors.
   - Complete history plus control evidence and evidence retrieval subject to law.
   - Audit access does not confer transaction authority.

3. **Public projection and proof layer**
   - Public fields, event lineage, amounts and correction states.
   - Aggregation or suppression for PII, law-enforcement, procurement-sensitive, tax, national-security, Tribal and student records.
   - Hash commitments or Merkle roots make later evidence substitution detectable without disclosing protected contents.

### 4.3 What executable rules can automate

Good candidates:

- confirm TAS/TAFS and period of availability;
- confirm obligation does not exceed apportioned/allotted authority;
- confirm award and recipient identifiers;
- enforce separation of duties;
- validate FAIN/PIID/UEI/ALC and GSDM fields;
- enforce draw limits and cash-timing rules;
- require subaward flow-down fields;
- tie a payment request to an authorized award and available balance;
- flag duplicate invoices or payment requests;
- require performance/certification artifacts before a milestone payment;
- propagate reversals and supersession notices to subscribed systems;
- maintain an auditable rule version and explanation.

Rules that still require accountable judgment or external evidence:

- whether a student, vendor, beneficiary or recipient is genuinely eligible;
- whether goods/services were delivered and meet quality requirements;
- whether a cost is reasonable, allocable and allowable;
- whether a subrecipient or contractor classification is substantively correct;
- whether reported performance caused a social outcome;
- whether an exception, waiver or appeal should be granted;
- whether noncompliance is material, fraudulent, or an established debt.

An immutable false eligibility assertion remains false. Immutability improves provenance; it does not transform an assertion into truth.

### 4.4 Why a permissioned ledger is plausible but not yet selected

Treasury’s NSF grants prototypes found potential for:

- visibility as funds moved from prime recipient to subrecipient;
- reduced reporting through shared transactional data;
- standardized processes, near-real-time transactions and improved internal controls.

The prototype did not process real payments. Treasury identified legal, technical, governance, infrastructure, legacy-integration and regulatory challenges. A later task order aimed to culminate in a grant payment and examine nodes, wallets, cryptography and cross-agency authority. The JFMIP initiative expanded the prototype architecture across Treasury and GAO; its 2023 report was a learning tool, not a prescribed government-wide framework.

JFMIP specifically identified:

- potential reduction in reconciliation from one integrated validated data source;
- potential auditor efficiencies from read-only nodes;
- complexity in multi-agency coordination and Authority to Operate;
- cybersecurity, network, cloud/vendor-lock-in and methodology issues; and
- continued need for audit procedures over controls and financial-statement assertions.

The functional architecture can also be built with signed append-only databases, event streaming and public hash anchoring. “Blockchain” is an implementation option, not the control objective.

## 5. Education-grant case map

Education makes the ownership problem unusually visible because the legal funding record, State/local accounting record, payment rail, student-level evidence, performance dataset, and audit record belong to different entities.

### 5.1 Formula-grant path: Title I / Perkins / IDEA pattern

```text
Congress appropriates to an ED TAFS
  → OMB apportions the TAFS
  → ED records allotment/formula award
  → State educational agency receives award authority
  → SEA draws federal cash as needed
  → SEA allocates/subawards to LEAs or eligible institutions
  → LEA/school/college pays payroll, vendors, contractors or subrecipients
  → SEA/LEA reports financial and program performance
  → student-level evidence remains protected
  → auditee includes expenditures in SEFA / Single Audit
  → FAC publishes audit package (subject to exceptions)
  → ED or pass-through entity issues management decision
  → disallowed excess becomes debt only after determination
  → refund, offset or other collection closes the financial consequence
```

For Title I, federal formulas calculate LEA-level allocations, but funds flow through the SEA. LEAs target funds to eligible schools and programs. The federal allocation record is therefore not the same as the date or amount of a State cash transfer, an LEA expenditure, or a school-level result.

For Perkins V and Adult Education and Family Literacy Act formula grants, ED’s September 8, 2025 operational memorandum documents a concrete system change:

- grant award management transitioned from ED’s G5 to GrantSolutions;
- drawdowns transitioned to HHS’s Payment Management System;
- the transition arose from the May 21, 2025 ED–DOL interagency agreement;
- Perkins financial reporting remained in the Perkins Information Management System / Consolidated Annual Report;
- AEFLA financial reporting remained in the National Reporting System; and
- States had to establish GrantSolutions/PMS access and new PMS payee/banking records.

This change did **not** merge award, cash, performance and audit into one ledger. It distributed them across more clearly named service systems.

### 5.2 Discretionary-grant path

```text
ED publishes NOFO / applicant uses Grants.gov
  → ED program office and grants officer select and make award
  → award is managed in G6/G5 or, for affected new awards, GrantSolutions
  → recipient draws in G6 or PMS
  → recipient posts expenditures and manages subawards/contracts
  → recipient submits annual/final financial and performance reports
  → ED or partner agency performs monitoring/technical assistance
  → Single Audit/OIG/other audit may identify findings
  → legally responsible agency or pass-through entity resolves findings
```

Discretionary grantees often provide annual performance reports demonstrating progress against award objectives. These reports are monitoring assertions; they are not Treasury settlement records and are not generally a public transaction ledger.

### 5.3 Pell and institutional Title IV aid

Pell is a different branch:

- the institution originates and reports student-level awards/disbursements through the Common Origination and Disbursement system;
- the institution requests and reconciles cash through ED’s grants/payment environment;
- the institution’s student account, attendance/eligibility and return-of-funds evidence controls individual entitlement;
- G6/G5 provides award balances, cumulative drawdowns, payment history, expenditure adjustments and returned cash;
- student-level records are protected rather than public spending-line items.

The Title IV record therefore requires a join among program eligibility, COD origination/disbursement, institutional cash draw, student ledger, Treasury/ED payment data and audit/program-review results. A public payment hash cannot expose the underlying student record.

### 5.4 FERPA and why “open accounting” cannot mean public student records

FERPA generally requires consent before disclosure of personally identifiable information from education records. The audit/evaluation exception permits disclosures to authorized representatives for audit/evaluation of federal- or State-supported programs or compliance/enforcement, but requires:

- a written agreement;
- a specified purpose and specified PII;
- limits on use and redisclosure;
- protective policies and procedures; and
- destruction when no longer needed.

FERPA also requires recordation of many disclosures and further disclosures. A viable architecture should therefore publish program/financial events while keeping student records in a protected evidence domain. It can publish proof that an authorized evaluator accessed a defined evidence set under a valid agreement without publishing the evidence itself.

### 5.5 Education performance record

For K–12 programs:

- SEAs supply performance data through EDFacts.
- The Consolidated State Performance Report is an annual required reporting tool for ESEA programs such as Title I, II, III, IV, V and McKinney-Vento.
- ED uses the data for program performance, State monitoring, technical assistance, accountability and evaluation.
- public datasets apply privacy protections and suppression where needed.

For IDEA, States submit State Performance Plans/Annual Performance Reports; ED combines these with monitoring and public information in annual determinations.

Performance records can be linked to FAIN/Assistance Listing, State/LEA and reporting period. They usually cannot demonstrate that a particular Treasury-settled dollar caused a particular student outcome.

### 5.6 Single Audit, correction and recovery in education

As of the current Uniform Guidance, a nonfederal entity that expends at least $1 million in federal awards in its fiscal year generally falls within the Single Audit requirement. The auditor uses a risk-based major-program selection; not every program or transaction is tested. The FAC publishes:

- the independent audit report;
- SF-SAC data;
- federal-award information;
- findings, corrective-action plans and related fields;
- report/version relationships.

Institutions of higher education also submit Single Audit material to ED’s eZ-Audit process.

ED’s Office of Grants Management says it resolves and closes discretionary-grant Single Audit/OIG findings and formula-grant findings involving cash management and subrecipient monitoring. Program offices have additional audit-resolution roles.

The proper chain is:

> audit finding → ED/SEA/pass-through management decision → sustained/disallowed amount → recipient corrective action or appeal → receivable/debt → return/offset/collection → award/ledger/public-data corrections

The finding itself is not proof that cash was stolen or that a debt was collected.

### 5.7 Operative 2025–2026 changes to education-grant delivery

#### Operating, documented changes

1. **ED–DOL workforce-development service transfer (May–October 2025).**
   - Authority cited by ED: 20 U.S.C. § 1231(a) and the Economy Act, 31 U.S.C. § 1535.
   - Perkins V and AEFLA grant administration moved to DOL-supported GrantSolutions/PMS workflows.
   - ED’s FY2025 Agency Financial Report states all affected grantees were onboarded and, since October 1, the joint agencies processed more than 1,300 payment requests from 43 States and territories.

2. **Six additional IAAs announced November 18, 2025.**
   - DOL assumed larger administrative-service roles for K–12 and postsecondary grant programs.
   - HHS, Interior and State received defined administrative roles for other program groups.
   - These are administrative/service arrangements under existing law, not congressional repeal or wholesale statutory transfer of ED programs.

3. **Postsecondary new-award migration in FY2026.**
   - ED/DOL stated Higher Education Programs staff would be detailed to DOL.
   - A March 16, 2026 Dear Colleague Letter says **new awards competed and awarded in FY2026** transition to GrantSolutions and PMS.
   - **Current and existing grants remain monitored and managed in ED’s G5/G6 environment** unless separately transitioned.

4. **Additional February 23, 2026 IAAs.**
   - ED announced new State and HHS partnerships and published agreement text citing program statutes and 31 U.S.C. §§ 1501 and 1535.

5. **Workforce Pell / Pell eligibility changes effective July 1, 2026.**
   - ED’s June 4, 2026 implementation notice states the operative statutory date for Workforce Pell and specified Pell ineligibility rules is July 1, 2026, with corresponding 2026–27 COD system changes.
   - This changes eligibility/program processing. It does not by itself create a shared public accounting ledger.

#### Proposed or political, not equivalent to operative architecture

- FY2026 budget requests to consolidate programs do not establish law by themselves.
- Bills proposing transfer or abolition are not operative until enacted.
- Press-release language about “breaking up” ED does not change the statutory program owner unless valid law or delegated authority does so.

### 5.8 Strongest education interlock

The education changes prove why an entity-based ledger is necessary:

> **The statutory owner, grants-management service provider, payment platform operator, recipient, performance-data custodian, auditor and debt owner can all be different entities.**

ED’s OIG states that under the IAAs partner agencies provide grant-administration, monitoring and technical-assistance services, while ED retains statutory responsibilities, including audit resolution/closure, internal-control and risk oversight, and review of annual performance and fiscal reports. The OIG identifies the resulting multi-agency oversight, staff loss, data quality and IT/security burden as a management challenge.

A correct ledger must therefore record at least:

- `legal_program_owner = ED`;
- `administrative_service_provider = DOL/HHS/Interior/State as applicable`;
- `award_system = G6/G5 or GrantSolutions`;
- `payment_system = G6 or PMS`;
- `cash_disburser/settlement = Treasury/Fiscal Service or authorized rail`;
- `prime_recipient = SEA/IHE/LEA/nonprofit`;
- `pass_through_entity = SEA/IHE/other`;
- `performance_custodian = ED program office/EDFacts/recipient system`;
- `audit_decision_owner = ED or pass-through entity under the award`;
- `debt_owner = creditor agency`;
- `collection_service = agency/Treasury`.

If a system merely says “Department of Labor paid an education grant,” it can misstate the legal and accounting reality. DOL may administer the workflow; ED may remain the legal program and audit-resolution owner; PMS may process the draw; Treasury may disburse cash; a State may control downstream use.

## 6. Public versus protected fields for a minimum federal event record

| Object | Public projection | Protected evidence |
|---|---|---|
| Authority | public law, TAS, purpose/time/amount limits | legal advice, predecisional analysis |
| Apportionment | approved document, lines, footnotes, iteration, approver role | internal deliberation and access data |
| Allotment | agency, TAS, amount, program/project category, effective date where releasable | detailed operational plan, sensitive/classified activity |
| Award | FAIN/PIID, UEI, Assistance Listing, agency, amount, action, period, description | application, review, proprietary content, full award file |
| Draw | public correlation ID, award, amount/date or bounded aggregation, status | bank, TIN, user, cash forecast, request support |
| Certification | agency/ALC, schedule commitment/hash, authorized-role proof, timestamp | officer identity/security credential, payee detail |
| Settlement | public correlation, amount/date/status, award/TAS link where lawful | ACH trace/check/wire, bank, TIN, offset reason |
| Subaward | parent FAIN, subrecipient UEI, amount, period, purpose | agreement, invoices, monitoring and protected recipient data |
| Vendor/payroll | category, amount/time aggregate, evidence commitment | vendor bank/tax data, payroll and beneficiary PII |
| Performance | measure, target, aggregate result, reporting period, methodology | student/case records, proprietary research, audit/evaluation files |
| Finding | FAC reference, program, condition, questioned amount, corrective plan | workpapers, investigation-sensitive evidence |
| Management decision | finding reference, sustained/not sustained, disallowed amount, action, date, appeal status | legal analysis, protected evidence and settlement discussions |
| Debt/recovery | public case token, source finding/award, amount/status/date and recovery category | debtor/TIN, due-process record, bank/offset detail |
| Correction | prior public event, reason category, new event, monetary/accounting effects | detailed error analysis and protected source material |

## 7. Conclusions and research gaps

### Strong factual conclusions

1. **Federal money already has multiple authoritative ledgers.** The problem is cross-system lineage and public projection, not absence of all records.
2. **Apportionment transparency is materially stronger than it was before 2022.** The law requires approved documents and footnotes to be posted as open government data, and the official MAX site currently exposes them.
3. **Payment authenticity and program entitlement are deliberately separated.** Agency officers certify; Treasury validates form/control totals and disburses; agencies own entitlement accuracy.
4. **USAspending is standardized publication, not settlement proof.** Open code and validation are valuable but do not replace source-system evidence.
5. **Recipient-use and management-decision records are the major public gaps.**
6. **Audits are bounded, periodic and risk-based.** They cannot be treated as continuous validation of every transaction.
7. **A questioned cost is not a debt.** A management decision and entitlement determination intervene.
8. **Open public accounting must be privacy tiered.** Payment, tax, bank, payroll, student, Tribal, health, procurement-sensitive and investigative records cannot simply be published.
9. **The education system migration is a live example of functional unbundling.** Legal ownership, administration, payment, performance and audit can move or remain with different agencies.
10. **Blockchain can reduce reconciliation and improve provenance, but cannot supply oracle truth.** Treasury/JFMIP’s own prototype record supports both the opportunity and the limitation.

### Missing government-wide joins to monitor

- public agency allotment/suballotment dataset;
- standard public draw-request and payment-certification object;
- durable join from SPS/PAM/PIR/CARS settlement to FAIN/PIID without exposing PII;
- mandatory downstream subrecipient/vendor expenditure lineage;
- performance evidence linked to award events and rule versions;
- structured public management decisions;
- finding → debt → collection/recovery chain;
- universal reversal/supersession semantics across award, cash, accounting and public-data systems;
- public history of rule-code versions used to admit, block or transform records;
- authoritative, machine-readable designation of legal owner versus service provider for interagency grant administration.

## Primary source ledger

### Authority, apportionment, accounting and reporting

- OMB Circular A-11 (2025): https://www.whitehouse.gov/wp-content/uploads/2025/08/a11.pdf
- 31 U.S.C. § 1512, apportionment: https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title31-section1512
- 31 U.S.C. § 1513 and public apportionment requirement: https://uscode.house.gov/quicksearch/get.plx?section=1513&title=31
- Official approved apportionments: https://apportionment-public.max.gov/
- GAO, Principles of Federal Appropriations Law: https://www.gao.gov/legal/appropriations-law
- GAO decision describing the sequential appropriation-accounting chain: https://www.gao.gov/products/b-257905
- Treasury FAST Book: https://tfx.treasury.gov/reference-books/fast-book
- Treasury CARS: https://fiscal.treasury.gov/accounting/central-accounting-reporting-system-cars
- Treasury GTAS: https://fiscal.treasury.gov/accounting/government-wide-treasury-account-symbol-gtas/
- Treasury USSGL: https://fiscal.treasury.gov/accounting/us-standard-general-ledger-ussgl/about
- FASAB SFFAS 7, budgetary and financial accounting: https://files.fasab.gov/pdffiles/handbook_sffas_7.pdf

### Payment, settlement, privacy and debt

- TFM Chapter 3000, payment scheduling/certification: https://tfx.treasury.gov/tfm/volume1/part4a/chapter-3000-requirements-scheduling-payments-disbursed-bureau-fiscal-service
- Treasury PAM FAQs: https://fiscal.treasury.gov/payments-from-government/payment-automation-manager-pam/faqs
- Treasury PAM and related payment-status systems: https://fiscal.treasury.gov/payments-from-government/payment-automation-manager-pam/related-resources
- Treasury SPS PIA: https://fiscal.treasury.gov/system/files/files/pia/SPS-pia.pdf
- Treasury PAM privacy/control assessment: https://fiscal.treasury.gov/system/files/files/pia/pampclia.pdf
- Treasury Privacy Impact Assessments index: https://fiscal.treasury.gov/about-us/pia
- Treasury debt-management programs: https://wwwkc.fiscal.treasury.gov/debt-management/about/about-debt-management-programs.html
- Treasury delinquent-debt collection manual: https://fiscal.treasury.gov/system/files/files/debt-management/chapter6.pdf
- Treasury debt-certification process: https://www.fiscal.treasury.gov/training/annual-debt-certification-process.html
- Treasury Do Not Pay: https://fiscal.treasury.gov/payment-integrity/do-not-pay-dnp/about

### DATA Act, standards and public publication

- Treasury DATA Broker source code: https://github.com/fedspendingtransparency/data-act-broker-backend
- USAspending API source code: https://github.com/fedspendingtransparency/usaspending-api
- GSDM architecture: https://fiscal.treasury.gov/files/data-transparency/gsdm-architecture-v1.0.pdf
- TFM Chapter 6000, USAspending reporting: https://tfx.treasury.gov/tfm/volume1/part2/chapter-6000-agency-reporting-requirements-usaspendinggov
- Treasury monthly DATA Act reporting requirements: https://tfx.treasury.gov/monthly-reporting-requirements
- Treasury financial-management standards: https://tfx.treasury.gov/fm-standards

### Internal control, grants and audit

- GAO Green Book: https://www.gao.gov/greenbook
- GAO Yellow Book: https://www.gao.gov/yellowbook
- Current eCFR, 2 CFR § 200.305, federal payment: https://www.ecfr.gov/current/title-2/subtitle-A/chapter-II/part-200/subpart-D/section-200.305
- Current eCFR, 2 CFR § 200.329, performance: https://www.ecfr.gov/current/title-2/subtitle-A/chapter-II/part-200/subpart-D/section-200.329
- Current eCFR, 2 CFR § 200.332, pass-through entities: https://www.ecfr.gov/current/title-2/subtitle-A/chapter-II/part-200/subpart-D/section-200.332
- Current eCFR, 2 CFR § 200.346, amounts due: https://www.ecfr.gov/current/title-2/subtitle-A/chapter-II/part-200/subpart-D/section-200.346
- Current eCFR, 2 CFR § 200.521, management decisions: https://www.ecfr.gov/current/title-2/subtitle-A/chapter-II/part-200/subpart-F/section-200.521
- Federal Audit Clearinghouse data/API: https://www.fac.gov/data/
- FAC data dictionary and report versions: https://www.fac.gov/api/dictionary/
- FAC Tribal suppression: https://www.fac.gov/api/tribal/
- 2025 OMB Compliance Supplement: https://www.fac.gov/assets/compliance/2025-Compliance-Supplement.pdf

### Treasury/JFMIP blockchain research

- JFMIP Blockchain Initiative and 2023 report: https://www.cfo.gov/jfmip/blockchain-initiative/
- Treasury NSF prototype findings: https://fiscal.treasury.gov/financial-management-solutions/financial-innovation-transformation-fit/blog/another-link-in-the-chain
- Treasury 2021 grant-payment task order: https://fiscal.treasury.gov/about-us/news/fiscal-service-testing-blockchain-to-streamline-grant-payment-processes
- Treasury open-source prototype code announcement: https://www.fiscal.treasury.gov/fit/blog/come-git-your-blockchain-code.html

### Education-grant case

- ED Title I data/allocations overview: https://eddataexpress.ed.gov/resources/title-i/title-i-part
- ED Perkins State formula allocations: https://octae.ed.gov/cte/grants/state-formula-grants/state-allocations
- ED OCTAE September 8, 2025 G5 → GrantSolutions/PMS transition memo: https://www.ed.gov/media/document/octae-program-memo-25-5-transition-g5-grantsolutions-and-payment-management-system-formula-grants-under-perkins-and-aefla-110563.pdf
- ED November 18, 2025 six IAAs: https://www.ed.gov/about/news/press-release/us-department-of-education-announces-six-new-agency-partnerships-break-federal-bureaucracy
- ED January 15, 2026 postsecondary partnership: https://www.ed.gov/about/news/press-release/us-department-of-education-and-us-department-of-labor-take-next-steps-implement-postsecondary-education-partnership
- ED March 16, 2026 FY2026 new-award transition letter: https://www.ed.gov/media/document/dear-colleague-letter-ed-and-dol-grants-partnership-march-16-2026-113460.pdf
- ED February 23, 2026 additional IAAs: https://www.ed.gov/about/news/press-release/us-department-of-education-announces-additional-partnerships-break-federal-education-bureaucracy
- ED FY2025 Agency Financial Report: https://www.ed.gov/media/document/fy25-agency-financial-report-113142.pdf
- ED OIG FY2026 Management Challenges: https://oig.ed.gov/reports/top-management-challenges/fiscal-year-2026-management-challenges-facing-us-department
- ED G6/G5 Title IV cash-management description: https://fsapartners.ed.gov/knowledge-center/fsa-handbook/2025-2026/vol4/ch1-requesting-and-managing-title-iv-funds
- ED FERPA regulations and audit/evaluation exception: https://studentprivacy.ed.gov/ferpa
- EDFacts: https://www.ed.gov/data/edfacts-initiative
- Consolidated State Performance Reports: https://www.ed.gov/laws-and-policy/laws-preschool-grade-12-education/birth-grade-12-policy-documents/consolidated-state-performance-reports
- ED OIG Single Audits: https://oig.ed.gov/non-federal-audits/single-audits
- ED grants-management/audit-resolution functions: https://www.ed.gov/about/ed-organization/functional-statements/ofo-functional-statements/ofo-functional-statements-office-of-grants-management
- ED Workforce Pell operative dates: https://fsapartners.ed.gov/knowledge-center/library/electronic-announcements/2026-06-04/effective-dates-workforce-pell-and-federal-pell-grant-ineligibility-provisions
