# Federal Transaction Record — Open Accounting, Audit Limits, and the State-NGO Gap

Evidence cutoff: 2026-07-23  
Status: canonical factual map; adoption thesis and forecast are labeled separately  
Workbench evidence: `FEDERAL_TRANSACTION_RECORD_DEEP_DIVE_2026-07-23.md`; `FEDERAL_FUNDS_LEDGER_ADOPTION_WATCHBOARD_2026-07-23.md`

## Short answer

The federal government does not have one public record that follows a dollar from legal authority through payment, State or NGO custody, downstream expenditure, correction and recovery.

2026-07-30 - The Accounting Transition — Shared Events, Executable Rules, and the Judgment Layer
extends this control map into the corporate and standards layer. It separates
the underlying event, accounting rule, judgment and user-specific report and
tests which functions can be automated without treating a recorded event as
proof of legal, economic or performance truth.

The 2025–2026 education-grant interagency agreements are the strongest live
entity test. For covered programs, ED may retain statutory, policy, control,
reporting or audit-resolution duties while DOL, HHS, DOI or State performs
administration and a different system records the award or draw. The federal
transaction spine must therefore preserve the legal owner, ordering agency,
servicing agency, Form 7600B/IPAC layer, payment operator, recipient, auditor
and recovery owner rather than forcing one agency label to describe them all.

It has a **federation of legally distinct records**:

```text
appropriation
  → obligation / award
  → draw authorization
  → certified payment
  → Treasury release and settlement
  → State or NGO receipt
  → subaward / contract / payroll / provider payment
  → performance evidence
  → correction / questioned cost / debt / recovery
  → public disclosure
```

Different systems and officials control different facts. Financial statements summarize the result; an audit supplies bounded assurance over those statements or selected programs; Form 990 supplies annual organizational information; USAspending publishes award data; Treasury and agency systems retain payment and accounting events. None currently gives the public a joined transaction chronology across the whole chain.

That gap is the factual basis for the open-accounting thesis. It does **not** establish that blockchain has been selected. The strongest current architecture would combine:

```text
protected authoritative records
  + common transaction and supersession identifiers
  + mandatory downstream flow-down
  + public transaction and correction proofs
```

Whether those proofs are held in a conventional append-only database, a permissioned ledger, or anchored to a public blockchain remains an open implementation branch.

## 1. Terminology firewall

Do not merge or total these categories:

| Category | What it establishes | What it does not establish |
|---|---|---|
| adjudicated fraud | fraud found through a controlling legal process | the size of all suspected or undetected fraud |
| alleged or suspected fraud | an accusation, referral, indictment or active inquiry | guilt or loss finally proved |
| fraud risk | exposure to a scheme or control weakness | an improper transaction |
| improper payment | payment that should not have been made, was made in the wrong amount, went to an ineligible recipient, or lacked required support | intentional deception |
| unsupported or questioned cost | missing support or an auditor's challenge under award rules | fraud or a final debt |
| legal or award-term noncompliance | failure to comply with a controlling requirement | necessarily a financial loss |
| waste | careless, extravagant or inefficient use | deception or illegality |
| abuse or mismanagement | deficient administration or misuse of position/process | a single uniform statutory fraud standard |
| program ineffectiveness or poor value | weak outcomes relative to cost | improper accounting |
| lawful but objectionable spending | an authorized policy choice a taxpayer rejects | fraud, waste or noncompliance |

GAO defines fraud around willful misrepresentation used to obtain something of value. An improper payment can arise from fraud, error, ineligibility, incorrect amount or missing documentation. A grant may be authorized, accurately paid and properly reported yet still be ineffective or politically objectionable.

**Binding rule:** every number must keep its evidence state. A modeled loss range, risk flag, indictment amount, questioned cost, improper-payment estimate, recovery and adjudicated theft are different objects.

Primary source: [GAO-26-109100](https://www.gao.gov/products/gao-26-109100) · OBBB — Fraud, Improper-Payment and Error-Rate Legal Map

## 2. What an audit opinion actually says

An audit does account for fraud—but only within a bounded objective. In a financial-statement audit, the auditor seeks **reasonable, not absolute, assurance** that the statements as a whole are free of **material** misstatement due to fraud or error.

An unmodified opinion does **not** mean:

- every transaction, vendor, beneficiary or award was tested;
- the complete general ledger was published or independently replayed;
- every program complied with every requirement;
- every payment had adequate value;
- no fraud occurred.

Materiality is both quantitative and qualitative. Government auditors may use lower thresholds when public accountability, legal sensitivity or management misconduct makes a smaller item important. That does not convert a financial-statement audit into a payment-by-payment fraud investigation.

Sampling, analytical procedures and risk-based selection are normal. Large consolidated denominators can make individually striking payments immaterial to the statements even while a population of similar small payments is systemically important.

Primary sources: [GAO Government Auditing Standards, 2024 Revision](https://www.gao.gov/assets/d24106786.pdf) · [GAO Financial Audit Manual, June 2026](https://www.gao.gov/assets/gao-26-108577.pdf)

### 2.1 Single Audit is not universal transaction assurance

Under current Uniform Guidance:

- a nonfederal entity generally becomes subject to Single Audit when it expends **$1 million or more** in federal awards during its fiscal year;
- the audit focuses on major programs and direct-and-material compliance requirements;
- required major-program coverage can be 20 percent of federal expenditures for a low-risk auditee or 40 percent otherwise;
- the reporting package may be submitted as late as nine months after the audit period closes;
- known or likely fraud affecting a federal award is reportable, but sensitive public disclosure may be withheld to protect an investigation.

That framework is important oversight. It is still periodic, selective and retrospective.

Primary sources: [2 CFR 200.501](https://www.ecfr.gov/current/title-2/section-200.501) · [2 CFR 200.512](https://www.ecfr.gov/current/title-2/section-200.512) · [2 CFR 200.516](https://www.ecfr.gov/current/title-2/section-200.516) · [2 CFR 200.518](https://www.ecfr.gov/current/title-2/section-200.518)

## 3. The Form 990 boundary

Form 990 creates **organizational visibility**, not transaction-level accountability.

- Government grants benefiting the public are generally combined into an annual revenue total. The return does not identify every funding agency, FAIN, draw, payment date or award restriction.
- Expenses are annual totals by natural category and broad function—not general-ledger entries, invoices, bank transactions or award-level cost allocations.
- Schedule I reports the organization's **outgoing** domestic grants and assistance. It does not itemize incoming federal awards.
- Schedule F reports foreign activity principally by region, purpose and amount and intentionally omits certain recipient-identifying fields.
- Schedules L and R reveal selected interested-person and related-organization relationships, not a complete vendor or payment ledger.
- Audited financial statements generally are not attached to the public Form 990.
- Smaller organizations can use Form 990-EZ or 990-N; churches and certain affiliated organizations may have no annual-return requirement.

The return is annual, can be extended, and then must still be processed and published. Acceptance is not an IRS audit or verification of the underlying transaction record.

Missing or incomplete schedules are a recognized persistent problem. The defensible claim is **not** that official evidence proves most accepted Forms 990 are wrong. It is that filing acceptance does not establish the truth, completeness or award-level traceability of the underlying transactions.

Primary sources: [2025 Form 990 instructions](https://www.irs.gov/instructions/i990) · [Schedule I instructions](https://www.irs.gov/instructions/i990si) · [Schedule F instructions](https://www.irs.gov/instructions/i990sf) · [IRS filing timetable and exceptions](https://www.irs.gov/charities-non-profits/exempt-organizations-annual-reporting-requirements-overview) · [IRS incomplete-return guidance](https://www.irs.gov/charities-non-profits/exempt-organizations-annual-reporting-requirements-filing-procedures-incomplete-returns)

## 4. The government-to-State-to-NGO gap

The public cannot currently join:

```text
federal award
  → payment or draw
  → State / NGO receipt
  → restricted fund
  → subaward / vendor / payroll / provider
  → service, milestone or beneficiary
  → correction / refund / recoupment
```

The records may exist among multiple parties. The missing public object is a persistent key and joined chronology across them.

GAO's July 23 report explains why the break occurs. Federal agencies generally oversee States or prime recipients; States oversee subrecipients; lower tiers oversee contractors and subcontractors. Each additional layer creates another entry point and another legal boundary. A technical ledger cannot skip those instruments. Every award, subaward and procurement layer must carry a duty to emit the next transaction event.

GAO found documentation consistent with identifying and prioritizing fraud risks for only five of 20 selected programs. It also identified severe and persistent Single Audit findings in 18 of the 20 programs during the review period and highlighted incomplete, duplicative and impossible subaward data.

The lesson is not merely “make the database immutable”:

> Immutability can preserve the provenance of an assertion. It cannot make an invalid amount, false invoice, corrupt eligibility decision or fictitious performance event true.

Primary source: 2026-07-23 - GAO - Combating Fraud in State-Administered Programs

## 5. Current record constitution

No single database is legally superior for every fact:

| Stage | Controlling record or actor | Typical identifier | Correction object |
|---|---|---|---|
| appropriation / fund authority | statute, Treasury account and agency funds-control record | TAS / TAFS | warrant, availability or account adjustment |
| award obligation | agency award and accounting record | agency + FAIN, UEI, modification | amendment, deobligation or negative obligation |
| draw authorization | PMS or ASAP account | PAN/document/subaccount or ASAP account | authorization change, suspension or closure |
| payment request | recipient request in PMS/ASAP | request or confirmation number | rejection, netted correction, journal voucher or return |
| payment certification | agency certifying official and voucher/schedule | SPS schedule, payee, TAS/BETC | pre-release correction |
| Treasury release / settlement | Treasury and payment-network records | payment ID, ACH trace, check serial or Fedwire record | return, reclamation, cancellation or recertification |
| federal cash classification | CARS | ALC + TAS + BETC + source transaction | reversal and restatement |
| financial reporting | agency general ledger, USSGL and GTAS | TAS + USSGL attributes | journal, resubmission or documented manual adjustment |
| State / recipient expenditure | State or recipient accounting system | State fund, project, voucher and vendor IDs | State journal, void, refund or recoupment |
| public award disclosure | FABS/File C/Data Broker/USAspending | FAIN/PIID/URI and generated IDs | source correction, correction/delete or off-cycle correction |
| debt / recovery | creditor agency; later Treasury collection systems | agency debt ID and debtor identifier | collection, compromise, offset, repayment or discharge |

Critical non-equivalences:

```text
obligation ≠ payment
payment ≠ settlement
settlement ≠ allowable expenditure
deobligation ≠ refund
refund ≠ accounting reclassification
reclassification ≠ award amendment
USAspending correction ≠ cash reversal
audit finding ≠ final debt
debt referral ≠ collection
```

“Real time” must identify which clock becomes visible. A daily website refresh does not make a monthly agency submission or annual recipient report contemporaneous.

## 6. What the first public-payment tests proved

### 6.1 Defend the Spend

The beta public payment feed exposes a bounded set of HHS Payment Management System grant-payment records, including payment date, amount, agency, organization, award description, FAIN and agency/recipient justifications. It proves that transaction-level public accounting is moving from theory to operating function.

It does not expose a complete general-ledger, settlement, State-expenditure, supporting-document, correction or recovery chain. It is a centralized public API—not proof of blockchain or government-wide coverage.

Primary sources: [Defend the Spend](https://www.doge.gov/payments) · [public API documentation](https://api.doge.gov/docs)

### 6.2 Pennsylvania CCDBG — the chain breaks at the State edge

A $37,065,525.14 Pennsylvania Child Care and Development Block Grant payment dated April 17, 2025 can be joined through FAIN to the correct USAspending award, recipient, Assistance Listing and federal account.

The chain cannot be joined publicly from that draw to a Pennsylvania PELICAN allocation, regional Early Learning Resource Center, provider invoice, attendance record, State SAP journal, provider payment or later recoupment.

The federal agency justification also labels the CCDBG payment as consistent with the “Head Start Grant program”—the wrong program. That is a live machine-readable classification error in the new public record.

The case proves two things at once:

1. the public federal payment line is real and joinable at award level; and
2. the record breaks before downstream expenditure and already needs a visible correction mechanism.

### 6.3 Georgia CCDF — a negative payment is not self-explanatory

Georgia's May 8, 2025 public entries move child-care costs among discretionary, mandatory and matching funding streams. The negative and positive records document a funding-source correction, not a fraud recovery, and the three amounts are not zero-sum.

A useful public record must distinguish:

```text
corrects
reverses
restates
reallocates
refunds
recovers
```

An amount and sign alone cannot tell the public which legal or accounting event occurred.

## 7. Minimum public transaction object

A meaningful public event needs more than an amount and a wallet:

| Object group | Minimum public or verifiable fields |
|---|---|
| authority | appropriation, program statute, Treasury account, availability period |
| award | FAIN, UEI or protected equivalent, assistance listing, terms, recipient, period |
| accounting | obligation, disbursement, expenditure/outlay, object class, program activity |
| payment | draw/request ID, certification, schedule, amount, rail and settlement state |
| downstream edge | State/recipient receipt, fund, voucher, subaward or procurement instrument |
| performance | milestone, invoice/cost category, acceptance and supporting-record commitment |
| control | eligibility screen, duplicate check, human review and approval |
| correction | prior event, superseding event, reason, authority, effective time and appeal |
| recovery | finding, management decision, debt, offset/refund and closure |
| disclosure | public, redacted, protected or classified state and legal basis |

Every event should preserve:

- `parent_object_id`;
- `caused_by_event_id`;
- `reverses_event_id` or `supersedes_event_id`;
- `source_authority`;
- separate effects on legal obligation, cash, accounting classification, recipient entitlement, public disclosure and debt.

## 8. Adoption ladder

The current evidence supports this sequence:

1. **Machine-readable publication and standardization — operating but incomplete.** USAspending, DATA Act reporting and open APIs provide the vocabulary.
2. **Federal every-payment justification — directed and bounded-live.** EO 14222 ordered justification records; Defend the Spend publishes a subset.
3. **Prepayment screening and Treasury centralization — operating and expanding.** EO 14249, Do Not Pay and Treasury payment controls move inspection before release.
4. **State eligibility/control flow-down — proposed, not final.** OMB's May 29, 2026 Uniform Guidance proposal would require State review of relevant data before disbursement but expressly does not select a technology.
5. **Prospective award-condition flow-down — legally plausible, not yet located as a ledger mandate.** New discretionary, milestone, reconstruction and reimbursement awards are the cleanest insertion points.
6. **Shared ledger or public proof — prototype precedent only.** Treasury and GAO tested a private, permissioned Ethereum grant model in 2021–2023 without an actual grant transaction or production recommendation.
7. **Government-wide public blockchain — forecast, not present law or operating fact.**

Likely binding chain:

```text
final policy rule
  → financial-management data/interface standard
  → agency system modification
  → NOFO / award / Treasury-State term
  → subaward and procurement flow-down
  → privacy, security and records approval
  → production transaction
```

The most plausible constitution is hybrid:

```text
protected operating record
  + standardized signed transaction events
  + public API and/or public cryptographic anchor
```

That design can expose amount, authority, recipient class, purpose, chronology and revision proofs without publishing beneficiary PII, bank details, tax data, classified spending or protected investigative information.

Primary sources: [EO 14222](https://www.federalregister.gov/documents/2025/03/03/2025-03527/implementing-the-presidents-department-of-government-efficiency-cost-efficiency-initiative) · [EO 14249](https://www.whitehouse.gov/presidential-actions/2025/03/protecting-americas-bank-account-against-fraud-waste-and-abuse/) · [OMB proposed Uniform Guidance rule](https://www.federalregister.gov/documents/2026/05/29/2026-10817/regulation-for-federal-financial-assistance) · [Treasury/GAO JFMIP blockchain report](https://www.cfo.gov/assets/files/JFMIP-24-01.pdf)

## 9. Adoption proof states

Do not collapse these:

| State | Required evidence |
|---|---|
| public feed | a live endpoint returns transaction-like records |
| reconciled publication | the public record joins to agency accounts and Treasury cash |
| downstream trace | the federal record joins to State, NGO, subrecipient and vendor expenditure |
| tamper-evident history | signed or cryptographically committed revision lineage |
| permissioned ledger | multiple authorized parties maintain or validate shared state |
| public-chain proof | a public network holds the transaction or an independently verifiable commitment |
| binding adoption | statute, final rule, award term or accepted agreement requires use |
| fraud-control result | audited evidence shows prevention, detection, recovery or reduced loss |

Defend the Spend currently satisfies the first state for a bounded data set. The Treasury/GAO prototype satisfies prototype evidence only. Neither proves the remaining states.

## 10. What to watch

Promote the thesis only when the evidence moves:

- OMB publishes a final Uniform Guidance rule with operative State or subrecipient flow-down;
- Treasury's FY2027 Federal Financial Management Capability Framework adds common transaction, justification, correction or public-proof fields;
- an actual NOFO, award term, Treasury-State agreement or procurement clause requires the interface;
- Defend the Spend expands agencies/programs and publishes correction or recovery history;
- a State vendor-payment or grant system exposes an award-to-voucher join;
- an agency names a production permissioned ledger or public-chain anchor;
- an audit shows measurable control results rather than architectural promise.

Falsifiers and competing branches:

- a conventional append-only federal database meets the transparency objective without shared validation;
- agencies publish justifications but never reconcile them to authoritative cash and accounting records;
- States remain outside the justification flow-down;
- privacy, records, correction and due-process requirements prevent public-chain treatment of the operative record;
- public data quality remains too weak for reliable automation;
- a ledger preserves false inputs without improving source validation or performance proof.

## Core framing

> Government accountability was built around documents about organizations. The coming fight is over evidence about transactions.

> Financial statements tell the public whether the bucket is roughly right. They do not let the public inspect what was placed in the bucket.

> Open accounting asks whether each dollar went where government said it went. Open performance asks whether taxpayers received anything worth buying.

The open ledger does not end the argument about government spending. It makes the argument legible.
