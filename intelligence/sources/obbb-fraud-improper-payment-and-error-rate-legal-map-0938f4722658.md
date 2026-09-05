> Source created: 2026-07-16 · Source updated: 2026-07-16

# OBBB — Fraud, Improper-Payment and Error-Rate Legal Map

Updated: 2026-07-16  
Status: active factual legal map; incorporated 2026-07-16  
Law: Public Law 119-21, enacted 2025-07-04, 139 Stat. 72  
Scope: enacted text first; implementation and FY2025 trigger data second; structural implications kept separate

Sibling (eligibility / fiscal-federalism, not this note): [OBBB — Eligibility and Fiscal-Federalism Companion](../sources/obbb-eligibility-and-fiscal-federalism-companion-35a40a201a22.html)

## Short answer

The One Big Beautiful Bill Act does contain a substantial fraud-and-administrative-error architecture, but the operative mechanism is narrower than the political language.

1. **The enacted statute never uses the word `mismanagement`.** USDA began using that characterization during implementation.
2. **There is no governmentwide fraud-rate trigger.** The two numeric error-rate mechanisms are program-specific:
   - SNAP: a State's payment error rate determines whether the State must fund 0%, 5%, 10% or 15% of benefit costs beginning in fiscal year 2028.
   - Medicaid: the Act tightens an existing 3% erroneous-excess-payment rule and the Secretary's good-faith waiver beginning in fiscal year 2030.
3. **Neither rate is a fraud rate.** SNAP's rate includes overpayments and underpayments caused by State or household error. Medicaid improper-payment measurement includes payments that failed legal, regulatory or documentation requirements. Both can include fraud, but neither proves fraud.
4. **The larger enacted pattern is `verify -> match -> measure -> shift cost -> recapture/remove`.** OBBB adds or tightens eligibility verification, cross-State matching, Death Master File checks, renewal frequency, tax-credit recapture, family-member audits and enforcement.
5. **The Act does not itself order blockchain, digital-wallet or unified-profile implementation.** It does create stronger fiscal incentives for shared identity, address, eligibility and payment-integrity systems.

Primary text: [Public Law 119-21, GovInfo](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) · [enrolled H.R. 1 text](https://www.congress.gov/119/bills/hr1/BILLS-119hr1enr.htm)

## 1. Literal-language audit

| Term or phrase | Enacted-text result | Legal significance |
|---|---|---|
| `mismanagement` | **No occurrence** | Not a statutory standard, defined term or cause of action. |
| `fraud` / `fraudulent` | Present in targeted provisions and headings | Used for specific penalties, risk assessments, immigration enforcement/funding and claim identity checks; not converted into a general rate. |
| `payment error rate` | SNAP §10105 | Drives State benefit cost sharing. |
| `allowable error rate of 0.03` | Medicaid §71106, amending 42 U.S.C. §1396b(u) | Limits federal participation in specified erroneous excess Medicaid payments. |
| `improperly claimed` / `erroneous claim` | Tax title, especially §70605 | Extends enforcement and penalties for COVID-era Employee Retention Credit claims. |
| `waste, fraud, and abuse` | Health-title headings | Descriptive organization of provisions; the headings do not themselves create a universal fraud definition or metric. |

**Source-control finding:** the enacted law uses measurable payment and eligibility errors as the operative objects. Later agency rhetoric often compresses those objects into `fraud`, `waste` or `mismanagement`.

## 2. SNAP: administrative accuracy becomes State fiscal liability

### 2.1 The enacted formula — §10105

Beginning in fiscal year 2028, the federal and State shares of SNAP benefit allotments change according to the State payment error rate:

| State payment error rate | Federal share | State share |
|---:|---:|---:|
| below 6% | 100% | 0% |
| 6% to under 8% | 95% | 5% |
| 8% to under 10% | 90% | 10% |
| 10% or more | 85% | 15% |

This is a structural change. Before OBBB, the federal government funded SNAP benefit allotments. The Act turns a quality-control measurement into a recurring State match for benefit costs.

### 2.2 The clocks

- **FY2028:** a State may elect to use its FY2025 or FY2026 payment error rate.
- **FY2029 and later:** USDA uses the rate from the third preceding fiscal year.
- **High-error delay:** if a State's FY2025 rate multiplied by 1.5 is at least 20%, implementation is delayed to FY2029. If the FY2026 rate meets that test, implementation is delayed to FY2030. The arithmetic cutoff is 13 1/3%.
- A delay is not an exemption. It gives the highest-error States more time before the cost share begins.

Source: [P.L. 119-21 §10105](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) · [CRS nutrition comparison, R48552](https://www.congress.gov/crs-product/R48552)

### 2.3 What the SNAP rate measures

The SNAP payment error rate measures the accuracy of State eligibility and benefit calculations. It is the sum of:

- overpayments, including benefits paid to an ineligible household or benefits above the correct amount; and
- underpayments, when an eligible household receives less than the correct amount.

Errors can be caused by the State agency or the household and are largely unintentional. Retailer trafficking is measured separately and is not included in this payment error rate. USDA and CRS both state directly that the payment error rate is **not a fraud rate**.

Sources: [USDA SNAP Quality Control](https://www.fns.usda.gov/snap/qc) · [CRS, SNAP: Errors and Fraud, IF10860](https://www.congress.gov/crs-product/IF10860)

### 2.4 The House's zero-tolerance language did not become law

The House-passed version contained a separate `Quality Control Zero Tolerance` section that would have reduced the monthly dollar tolerance for counting a SNAP error to $0. The enrolled and enacted Act omitted that section and retained the existing indexed tolerance.

- FY2025 tolerance: $57 in the sample month.
- FY2026 tolerance: $58 in the sample month.

An error at or below the tolerance is excluded from the official payment error rate. This is important version control: **the State cost-share formula passed; zero tolerance did not.**

Version-control sources: [House-engrossed H.R. 1](https://www.govinfo.gov/app/details/BILLS-119hr1eh) · [enacted P.L. 119-21](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) · [CRS R48552](https://www.congress.gov/crs-product/R48552) · [USDA error-tolerance table](https://www.fns.usda.gov/snap/qc/ett)

### 2.5 Separate administrative-cost shift — §10106

The federal share of State SNAP administrative costs falls from 50% through FY2026 to 25% beginning in FY2027. The State share therefore rises from 50% to 75%.

This change is **not conditional on an error rate**. It lands before the benefit cost-share rule and makes the State pay more of the systems, staffing, training and case-processing cost required to lower its rate.

### 2.6 First live trigger-year data — FY2025

USDA released the first rate that may be used under OBBB on 2026-06-24:

| Jurisdiction | Overpayment rate | Underpayment rate | Total payment error rate | OBBB tier if FY2025 is used |
|---|---:|---:|---:|---:|
| United States | 9.28% | 1.33% | **10.62%** | national rate; State shares are jurisdiction-specific |
| New York | 12.06% | 1.12% | **13.18%** | 15% State share |

New York's FY2025 rate is just below the 13 1/3% threshold that would delay implementation on the FY2025 clock. This does **not** yet fix New York's liability. New York's election between its FY2025 and FY2026 rate for FY2028 tiering is one mechanism; the statutory high-error delay is separate. The seven jurisdictions whose FY2025 rates meet the delay test move to FY2029. A qualifying FY2026 rate can independently set FY2030.

The FY2025 table shows seven jurisdictions at or above the 13 1/3% delayed-implementation threshold: Alaska, Delaware, the District of Columbia, Georgia, Illinois, New Mexico and Oregon.

USDA's June 2026 release calls the law's effect `real financial consequences for states that mismanage taxpayer dollars`. That is agency characterization, not language enacted in §10105.

Sources: [USDA FY2025 State table](https://www.fna.usda.gov/sites/default/files/resource-files/snap-qcfy25-per.pdf) · [USDA 2026 release](https://www.fna.usda.gov/newsroom/usda-0082.26)

## 3. Medicaid: an existing 3% disallowance becomes harder to waive

### 3.1 The pre-existing legal base

42 U.S.C. §1396b(u) already provided that federal payment is reduced by defined `erroneous excess payments for medical assistance` above the allowable 3% rate. The Secretary could waive all or part of the reduction when a State could not meet the rate despite a good-faith effort.

The defined object was narrower than all Medicaid improper payments. It centered on payments for ineligible individuals and certain eligibility-related overpayments, excluded specified technical errors and used quality-control/PERM evidence.

Source: [42 U.S.C. §1396b(u), official U.S. Code](https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title42-section1396b)

### 3.2 What OBBB §71106 changes

Effective beginning in FY2030, §71106:

1. allows the relevant audits to be conducted by the Secretary or, at the Secretary's option, by the State;
2. limits the amount the Secretary can waive under the good-faith exception;
3. adds payments where there is insufficient information to confirm eligibility; and
4. adds payments for items or services furnished to a person not eligible for those items or services.

The core sentence keeps the **3% allowable error rate** but narrows executive discretion above it. It changes the financial consequence of evidence and missing evidence; it does not create a finding that a recipient, provider or State committed fraud.

Source: [P.L. 119-21 §71106](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) · [CRS health report, R48633](https://www.congress.gov/crs-product/R48633)

### 3.3 Do not substitute the headline PERM rate

CMS's broad Medicaid improper-payment rate covers fee-for-service, managed care and eligibility components. CMS explicitly says the improper-payment rate is not a fraud rate; it measures payments that did not meet statutory, regulatory or administrative requirements. Missing or insufficient documentation can generate an improper-payment finding even when the provider or beneficiary was legitimate.

The §1396b(u) disallowance ratio is a specific statutory subset. The current national rolling PERM rate is useful context but is not automatically the State's §71106 liability rate.

Sources: [CMS PERM overview](https://www.cms.gov/data-research/monitoring-programs/improper-payment-measurement-programs/payment-error-rate-measurement-perm) · [CMS improper-payments fact sheet](https://www.cms.gov/newsroom/fact-sheets/improper-payments-fact-sheet)

## 4. Medicaid/CHIP companion controls: the data layer behind the rate

The surrounding `Reducing Fraud and Improving Enrollment Processes` subchapter builds the verification and matching machinery that can change future error findings.

| Section | Operative change | Clock |
|---|---|---|
| §71103 | States regularly obtain enrollee address data; CMS builds a system to detect simultaneous Medicaid/CHIP enrollment in multiple States; States submit SSNs and other necessary data at least monthly and act on matches. | Address process from 2027-01-01; national system by 2029-10-01. |
| §71103 | Approved address sources include returned USPS mail, the National Change of Address database, managed-care entities and other approved sources. | From 2027-01-01. |
| §71103 | Appropriates $10 million in FY2026 to establish the system and $20 million in FY2029 to maintain it. | Appropriated / implementation pending. |
| §71104 | States check the Death Master File at least quarterly for Medicaid enrollees, stop post-death payments and retroactively reinstate people misidentified as dead. | From 2027-01-01. |
| §71105 | States check the Death Master File during provider enrollment/revalidation and at least quarterly while the provider remains enrolled. | From 2028-01-01. |
| §71107 | Most Medicaid expansion adults receive eligibility redeterminations every six months rather than annually. | Redeterminations scheduled on or after 2027-01-01. |

CMS is actively implementing these provisions. It issued §71107 guidance in March 2026 and implementation material in April 2026.

Sources: [P.L. 119-21 §§71103-71107](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) · [CMS implementation hub](https://www.medicaid.gov/resources-for-states/working-families-tax-cut-legislation)

## 5. ACA premium-tax-credit controls

The health-tax title places `Preventing Waste, Fraud, and Abuse` above three provisions. They do not create an error rate.

| Section | Mechanism | Effective clock |
|---|---|---|
| §71303 | An Exchange must verify eligibility before a month qualifies for the premium tax credit. Inputs include household income and size, immigration eligibility, other health coverage and residence. Exchanges may use available data and reliable third-party sources. | Tax years beginning after 2027-12-31. |
| §71304 | Disallows the premium tax credit for coverage obtained through certain income-based special enrollment periods not tied to a specified life event or change in circumstances. | Plan years beginning after 2025-12-31. |
| §71305 | Removes the income-based cap on repayment when advance premium tax credits exceed the final allowed credit. | Tax years beginning after 2025-12-31. |

The legal movement is from post-payment reconciliation and limited recapture toward pre-payment verification and full recapture. CMS reported in January 2026 that it was already implementing the statutory verification direction alongside renewed Medicaid/CHIP and Exchange matching.

Source: [P.L. 119-21 §§71303-71305](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) · [CMS Exchange-integrity actions](https://www.cms.gov/newsroom/fact-sheets/cms-actions-protect-consumers-strengthen-exchange-program-integrity)

## 6. FEHB: the clearest literal fraud-risk mandate

Section 90101, the `FEHB Protection Act of 2025`, requires OPM to:

- verify qualifying life events and family-member eligibility;
- include ineligible covered persons in every future FEHB fraud risk assessment;
- conduct a comprehensive family-member eligibility audit during the three-year statutory window beginning one year after enactment;
- develop a process to remove ineligible people within 180 days; and
- use $66 million set aside for the verification, assessment, audit and removal work.

Current implementation state:

- OPM says the removal process was completed in December 2025.
- OPM's family-member verification final rule was published on 2026-06-02 and became effective on 2026-07-02.
- The comprehensive audit window runs from 2026-07-04 through 2029-07-04.

Sources: [P.L. 119-21 §90101](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) · [OPM FY2027 implementation report](https://www.opm.gov/about-us/fy-2027-congressional-budget-justification/appendix-gao-ig-act-reporting-for-budget-fiscal-year-2026/) · [OPM final rule, 91 Fed. Reg. 24364](https://www.govinfo.gov/content/pkg/FR-2026-06-02/pdf/2026-11022.pdf)

## 7. Other targeted fraud, improper-claim and oversight provisions

| Section | Object | Operative language/effect |
|---|---|---|
| [§70605](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) | COVID Employee Retention Credit | $1,000 per-failure due-diligence penalty for defined promoters; closes late claims unless filed by 2024-01-31; extends the assessment period to six years; extends erroneous-refund penalties to employment tax. |
| [§70204 / new IRC §6659](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) | Trump Account pilot improper or fraudulent election | $500 penalty for negligence/disregard and $1,000 for fraud when the child is not eligible. |
| [§90102](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) | Pandemic Response Accountability Committee | $88 million for oversight and extends the committee's statutory endpoint from 2025 to 2034. |
| [§90103](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) | OMB | $100 million through 2029-09-30 to find executive-branch budget and accounting efficiencies. No fraud rate or mandatory savings target. |
| [§100003](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) | Immigration benefit fraud | USCIS retains 25% of employment-authorization-document fees, with at least half of the retained share used to detect and prevent immigration-benefit fraud. |
| [§100054](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) | DOJ immigration enforcement | A $3.33 billion multi-purpose appropriation includes investigation and prosecution of fraud relating to title IV public-benefit restrictions. The Act does not assign a discrete amount to that fraud purpose. |
| [§100204](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) | Manhattan Project waste claims | Attorney General must certify claimant identity is not fraudulent or misrepresented. |

These are targeted enforcement and funding rules. They should not be collapsed into the SNAP or Medicaid error-rate mechanisms.

## 8. Clock spine

| Date / period | Status | Event |
|---|---|---|
| 2025-07-04 | `occurred / enacted` | Public Law 119-21 signed. |
| 2025-12 | `occurred / implementation` | OPM reports completion of FEHB removal-process requirement. |
| plan/taxable years beginning after 2025-12-31 | `effective` | ACA special-enrollment restriction applies to plan years beginning after 2025-12-31; full advance-credit recapture applies to taxable years beginning after that date. The separate remittance-transfer tax became effective on 2026-01-01. |
| 2026-06-24 | `occurred / measurement` | USDA releases FY2025 SNAP rates, the first possible OBBB cost-share input. |
| 2026-06-02 | `occurred / final rule published` | OPM publishes the FEHB family-member verification final rule. |
| 2026-07-02 | `effective` | OPM FEHB family-member verification final rule takes effect. |
| 2026-07-04 | `deadline reached / audit window begins` | FEHB statutory verification deadline is reached; three-year audit window begins. |
| 2026-10-01 | `scheduled` | FY2027 begins; States' SNAP administrative-cost share rises to 75%. |
| 2027-01-01 | `scheduled` | Medicaid address checks and quarterly deceased-enrollee screening begin; affected expansion-adult redeterminations scheduled on or after this date use the six-month cycle. |
| 2027-10-01 | `scheduled / conditional by State` | FY2028 SNAP benefit cost sharing begins, subject to the statutory delay clauses. |
| 2028-01-01 | `scheduled` | Quarterly Medicaid deceased-provider checks begin. |
| taxable years beginning after 2027-12-31 | `scheduled` | ACA pre-payment premium-tax-credit verification applies. |
| 2029-10-01 | `scheduled` | CMS cross-State Medicaid/CHIP duplicate-enrollment system deadline. |
| FY2030 | `scheduled` | Medicaid §71106 3% waiver and expanded-error amendments apply. |

## 9. Structural read for the larger Observatory story

### Documented machinery

OBBB makes administrative accuracy a balance-sheet object. It joins five layers:

```text
identity / status evidence
  -> address, SSN, income, family and death-record matching
  -> eligibility or payment determination
  -> sampled error / improper-payment evidence
  -> recapture, disenrollment, corrective action or prosecution
  -> State or household financial liability
```

The strongest example is SNAP: an error statistic that includes both overpayment and underpayment becomes the formula for shifting benefit costs from the federal government to States. The Medicaid rule separately turns specified eligibility and documentation failures above 3% into reduced federal financial participation, with less waiver room.

### Working inference — keep separate from the law

This can feed the broader federal identity/data-control story because States now have a direct fiscal incentive to improve:

- cross-State identity resolution;
- current address and residency data;
- death-record matching;
- income and coverage verification;
- documentation completeness; and
- pre-payment controls.

The architecture remains **federated**, not one merged citizen database: program-specific records and State systems connect to shared matching services and federal payment/funding rules. OBBB supplies a powerful incentive layer under that structure.

### What would be an overclaim

- `The OBBB fraud rate proves 10.62% of SNAP is fraud.` — **False.**
- `The Act punishes only recipient wrongdoing.` — **False.** State calculation errors and underpayments count.
- `The Act enacted SNAP zero tolerance.` — **False.** That House provision was removed.
- `The Medicaid 3% rule is the same as the national PERM rate.` — **False.** The statutory disallowance has a defined subset and its own exclusions.
- `The Act created one federal profile or database.` — **False.** It created and strengthened specific verification and matching pathways.
- `The Act mandates blockchain or tokenized government payments.` — **False.** No such mandate appears in these provisions.

## 10. Evidence that would change this map

1. USDA's FY2026 State payment error rates — the second and elective FY2028 input.
2. State budget enactments for the FY2027 75% SNAP administrative share.
3. State announcements choosing FY2025 or FY2026 for the first SNAP benefit-cost share.
4. USDA election procedure/deadline and guidance on how elections and high-error delays interact.
5. State corrective-action plans and system/vendor procurements tied to payment accuracy.
6. CMS design and procurement records for the 2029 cross-State duplicate-enrollment system.
7. State implementation of six-month Medicaid renewals and error-correction/due-process rates.
8. OPM evidence that the comprehensive FEHB audit has begun, then the first results and the split among error, ineligibility and actual fraud.
9. Any later law that links these eligibility systems to Treasury payment rails, Login.gov or a broader federal-person record. That link is **not yet supplied by OBBB itself**.

## Source shelf

### Primary legal and implementation sources

- [Public Law 119-21 — GovInfo](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm)
- [Enrolled H.R. 1 text](https://www.congress.gov/119/bills/hr1/BILLS-119hr1enr.htm)
- [House-engrossed H.R. 1 — GovInfo](https://www.govinfo.gov/app/details/BILLS-119hr1eh)
- [42 U.S.C. §1396b(u) — official U.S. Code](https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title42-section1396b)

### SNAP

- [USDA OBBB implementation hub](https://www.fns.usda.gov/obbb)
- [USDA SNAP Quality Control](https://www.fns.usda.gov/snap/qc)
- [USDA error-tolerance thresholds](https://www.fns.usda.gov/snap/qc/ett)
- [USDA SNAP payment error-rate landing page](https://www.fns.usda.gov/snap/qc/per)
- [USDA FY2025 State payment error rates](https://www.fna.usda.gov/sites/default/files/resource-files/snap-qcfy25-per.pdf)
- [USDA FY2025 release](https://www.fna.usda.gov/newsroom/usda-0082.26)

### Medicaid / ACA / FEHB

- [CMS PERM overview](https://www.cms.gov/data-research/monitoring-programs/improper-payment-measurement-programs/payment-error-rate-measurement-perm)
- [CMS Medicaid P.L. 119-21 implementation hub](https://www.medicaid.gov/resources-for-states/working-families-tax-cut-legislation)
- [CMS Exchange-integrity implementation](https://www.cms.gov/newsroom/fact-sheets/cms-actions-protect-consumers-strengthen-exchange-program-integrity)
- [OPM FEHB implementation report](https://www.opm.gov/about-us/fy-2027-congressional-budget-justification/appendix-gao-ig-act-reporting-for-budget-fiscal-year-2026/)
- [OPM FEHB verification final rule — permanent GovInfo PDF](https://www.govinfo.gov/content/pkg/FR-2026-06-02/pdf/2026-11022.pdf)

### Official secondary analysis

- [CRS R48552 — SNAP and Related Nutrition Programs in P.L. 119-21](https://www.congress.gov/crs-product/R48552)
- [CRS IF10860 — SNAP: Errors and Fraud](https://www.congress.gov/crs-product/IF10860)
- [CRS R48633 — Health Provisions in P.L. 119-21](https://www.congress.gov/crs-product/R48633)
