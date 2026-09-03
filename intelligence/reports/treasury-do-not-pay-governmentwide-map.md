# Treasury Do Not Pay — Governmentwide Structural Map

## Research contract

- **Question:** What is Treasury's Do Not Pay program, how far across federal,
  State, territorial, tribal and local-government payment activity does it
  reach, and what does a match legally do?
- **Mode:** question-led legal and operating-architecture deep dive.
- **Scope:** the Treasury Bureau of the Fiscal Service Do Not Pay Initiative and
  Working System; current products and data families; statutory users; State
  program channels; the 2025–2026 expansion architecture; and OPM Retirement
  Services as a current agency-specific implementation.
- **Exclusions:** no claim of an exhaustive agency-by-agency usage census; no
  inference that purely State or local funds are universally screened; no
  individual eligibility, fraud, collection or recovery conclusion from a
  database match; no appraisal of nonpublic matching logic or vendor models.
- **Frozen cutoff:** August 29, 2026, Eastern Time.
- **Live-canon boundary:** the Chronicle remains authoritative for promoted
  Government Fraud doctrine and watches. This is a Workbench Reference Object;
  it does not create a vault event, watch, rule or app shipment.
- **Source families:** U.S. Code and Public Law; Treasury Fiscal Service; OMB;
  Federal Register; OPM.
- **Stop rule:** stop when the legal object, operating products, actor/decision
  boundaries, cross-government reach, current OPM clock and future expansion
  gates are source-resolved through the cutoff.

## Bottom line

Treasury Do Not Pay is a **governmentwide shared screening network with
distributed legal decision-making**. Treasury operates the Working System,
data connections, portal, API, State-program hubs and a payment-verification
checkpoint. Federal agencies and authorized State-program users compare payee
or recipient data with designated sources before an award or payment, during
continuous monitoring, or during post-payment review.

The returned object is a **match, data response or risk signal**. It is not a
single federal blacklist, an adjudication of eligibility, proof of fraud or an
automatic lawful denial. The agency or State program administering the payment
must verify the information and apply its own program authority. Treasury can
return a payment file for further review at the payment-verification gate, but
the program still owns certification, eligibility and adverse action.

The architecture therefore separates:

`identity/data response -> program eligibility review -> payment gate -> payment or return -> post-payment accounting/recovery`

Do not collapse any adjacent states in that sequence.

## 1. The objects that are easy to blur

| Object | Owner | Function | What it is not |
|---|---|---|---|
| Do Not Pay Initiative | Treasury Fiscal Service | Governmentwide payment-integrity program and service family | A new program created in 2025 |
| Do Not Pay Working System | Treasury Fiscal Service | The statutory working system through which available databases are reviewed | One master source database |
| DNP Connect | Treasury Fiscal Service | Real-time or batch system-to-system API access | A legal eligibility decision engine |
| DNP Portal | Treasury Fiscal Service | Single queries, batch searches, continuous monitoring alerts and reports | Unrestricted public access |
| Treasury Payment Verification | Treasury Fiscal Service | Screening of federal-agency disbursements using Treasury payment rails | A substitute for earlier agency eligibility checks |
| PARIS and the UI Integrity Data Hub | HHS/ACF and DOL partner channels | State-program matching for public assistance and unemployment integrity | Universal control over State spending |
| Designated and partner datasets | Source owners plus Treasury access controls | Death, debt, exclusion, identity, entity, bank, incarceration, audit and related signals | A uniform dataset available to every user |
| Program determination | Paying or awarding agency/State program | Applies the governing eligibility and payment law after verification | A Treasury database result |

Primary architecture: [Treasury DNP About](https://fiscal.treasury.gov/payment-integrity/do-not-pay-dnp/about),
[DNP Products](https://fiscal.treasury.gov/payment-integrity/do-not-pay-dnp/products),
and [31 U.S.C. § 3354](https://www.govinfo.gov/link/uscode/31/3354).

## 2. Operational flow and decision ownership

| Stage | Actor | Record or action | Boundary |
|---|---|---|---|
| 1. Data supply | SSA, Treasury, SAM, HHS OIG, OFAC, BOP, State vital-record owners and other authorized sources | Source-owner record made available or designated for matching | The source owner controls correction of its underlying record |
| 2. Query or monitoring | Federal agency or authorized State-program user through DNP | Single, batch, API or continuous-monitoring query | Access depends on purpose, agreement, legal authority and dataset restrictions |
| 3. Response | DNP | Match, nonmatch, attribute, alert, risk indicator or confidence information | A result is not eligibility adjudication or proof of intent |
| 4. Independent review | Paying/awarding agency or State program | Corroboration, program-law analysis and due process | Program authority, not Treasury, controls the substantive decision |
| 5. Payment verification | Treasury for covered federal disbursements | Payment is cleared, returned for agency review or otherwise handled through the payment process | A Treasury return is not by itself a final benefit or award denial |
| 6. Post-payment action | Program, debt/recovery owner, inspector general or law-enforcement actor as authorized | Correction, overpayment determination, debt collection, recovery, referral or case | Improper payment, debt, fraud risk, allegation and adjudicated fraud remain separate states |

Treasury's Help Center expressly says DNP does not make payment determinations
and that a match or elevated risk does not itself stop payment. Agencies and
States must perform additional due diligence. See [DNP Help
Center](https://fiscal.treasury.gov/payment-integrity/do-not-pay-dnp/help-center).

## 3. How far across government it reaches

| Governmental or recipient layer | Current legal/operating relationship | Claim limit |
|---|---|---|
| Treasury | Operates the system and central payment-verification infrastructure | Treasury does not own every program's eligibility law |
| Federal executive agencies | Must review payments and awards through the Working System, subject to governing authority and available data | A statutory screening duty does not prove every payment used every dataset |
| Federal judicial and legislative branches | May access the system for payment and award eligibility review under the statute | Permission is not evidence of universal or identical usage |
| States administering federally funded programs | May access and use DNP for program-integrity review; State hubs support public-assistance and unemployment programs | This is not blanket jurisdiction over wholly State-funded disbursements |
| State contractors, subcontractors, agents, auditors and programs | May participate for federally funded State-administered program integrity within the statutory and agreement perimeter | They do not receive independent, purpose-free access |
| District of Columbia, territories and federally recognized tribes | Included in the newer routine-use and federally funded disbursement framework | Exact access and datasets still depend on authority and implementation objects |
| Local governments | Commonly appear as recipients, subrecipients, vendors or payees and may operate inside a State/pass-through program | Local-government status alone does not create unrestricted DNP access |
| Nonprofits, vendors, grantees, providers and individuals | Can be subjects of screening and later program review | They are not DNP users merely because they receive public money |

Section 3354 gives States and their contractors, agents, auditors and relevant
programs access for federally funded State-administered programs. It also
recognizes that a payment may still be required by law even when screening
identifies potential ineligibility. That clause is a direct statutory warning
against treating the system as a conclusive blacklist.

## 4. Current State-program pathways

The State layer is already operational in bounded program channels:

- **PARIS:** coordinated with HHS's Administration for Children and Families;
  supports State public-assistance matching involving Medicaid, TANF, workers'
  compensation, child care, SNAP and duplicate interstate participation. State
  agencies may also use authorized veterans and death data.
- **Unemployment Insurance Integrity Data Hub:** coordinated with the
  Department of Labor for State unemployment agencies, including pre- and
  post-payment integrity checks.
- **Direct matching agreements:** Treasury's privacy page lists current
  agreements involving CMS, VA, HUD and the Washington State Health Care
  Authority. These program-specific instruments show how legal purpose and
  controls attach to an actual user; they do not prove that every State agency
  participates.

Sources: [DNP Products](https://fiscal.treasury.gov/payment-integrity/do-not-pay-dnp/products)
and [DNP Privacy and matching
agreements](https://fiscal.treasury.gov/payment-integrity/do-not-pay-dnp/privacy).

## 5. What data is in the network

DNP is a routing and controlled-access layer across multiple sources. Its
current published inventory includes:

| Data family | Published examples | Primary use boundary |
|---|---|---|
| Death | SSA death records, State data, EVVE vital events, Defense records and commercial obituary/probate information | Verify living/deceased status; a match still requires identity confirmation |
| Debt and delinquency | Treasury Offset Program debt check and HUD CAIVRS | Debt or delinquency signal; not a universal prohibition on payment |
| Registration and exclusion | SAM registration/exclusions, HHS OIG LEIE and OFAC | Entity status, suspension/exclusion or sanctions screening within governing law |
| Identity | SSA Numident and related verification data | Name, SSN and date-of-birth validation; not a permanent trust score |
| Bank/account | Account Verification Service | Account ownership or validity signal subject to access and vendor/source limits |
| Incarceration | Federal Bureau of Prisons | Federal incarceration only; it does not cover all State, local or private custody |
| Tax-exempt organizations | IRS revocation, Publication 78 and Form 990-N information | Public tax-exempt status checks, not access to unrestricted individual tax-return information |
| Audit and organization | Federal Audit Clearinghouse and OpenCorporates | Audit/entity-status and organizational-risk information; not proof of misconduct |

Dataset access is not uniform. Treasury publishes federal/State usage and
restriction fields for individual data sources. A source must satisfy data
quality, usefulness, legal-authority, privacy, security and public-notice
requirements. Corrections generally begin with the source owner, after which
DNP should reflect the corrected source record. Current inventory: [DNP
Data](https://fiscal.treasury.gov/payment-integrity/do-not-pay-dnp/data).

## 6. Legal and privacy control stack

### Statutory base

The Payment Integrity Information Act architecture, codified in part at 31
U.S.C. § 3354, requires prepayment and preaward review using available databases
and the DNP Working System. The statute names a minimum database set and permits
additional designation through public notice and comment. It preserves Privacy
Act rights and recognizes that screening does not displace other legal payment
duties.

### 2025 access acceleration

Executive Order 14249, signed March 25, 2025, directed agencies and Treasury to
strengthen pre-certification controls, improve payment data and revise privacy
notices where needed. It accelerated and standardized an existing system; it
did not create DNP.

OMB Memorandum M-25-32, issued August 20, 2025, supplied standardized Privacy
Act routine-use language and a four-year waiver from the separate computer-
matching-agreement requirement for qualifying federal and federally funded
State-program matching. The waiver concerns 5 U.S.C. § 552a(o); it does not
erase public notice, data minimization, independent verification, notice,
contest or correction protections. Primary text: [OMB
M-25-32](https://www.whitehouse.gov/wp-content/uploads/2025/08/M-25-32-Preventing-Improper-Payments-and-Protecting-Privacy-Through-Do-Not-Pay.pdf).

### Privacy mechanics

Actual use remains bounded by system-of-record notices, privacy impact
assessments, routine uses, access controls, agreements or applicable waivers,
and source-specific restrictions. Treasury identifies DNP Payment Verification
Records in Treasury SORN .017 and publishes current matching instruments on its
privacy page.

## 7. Material 2025–2026 structural changes

| Clock | Object | State at cutoff | Structural effect | Claim limit |
|---|---|---|---|---|
| 2025-03-25 | EO 14249, *Protecting America's Bank Account Against Fraud, Waste, and Abuse* | Signed direction | Pushes stronger pre-certification review, standardized payment data and privacy-notice changes | Direction is not proof of implementation in every program |
| 2025-08-20 | OMB M-25-32 | Issued | Standard routine-use template plus four-year computer-matching-agreement waiver for qualifying uses | Does not waive all Privacy Act or due-process controls |
| 2026-02-10 | Public Law 119-77, Ending Improper Payments to Deceased People Act | Enacted; amendments effective 2026-12-27 | Strengthens SSA-to-DNP State death-data sharing and error notification; requires clear and convincing evidence before SSA records a death | Future effective date at this cutoff; enactment is not current operation |
| 2026-05-29 | OMB governmentwide financial-assistance rule, 91 FR 32198 | Proposed rule; comments closed 2026-07-13 | Would require States to review relevant data before disbursing federal funds, using DNP or a qualifying alternative, and would require federal-agency DNP review before covered federal-assistance payments | Not a final or operative rule through 2026-08-29 |
| 2026-08-19 | OpenCorporates U.S. legal-entity dataset added | Available according to Treasury | Extends organization-status screening for businesses, vendors and grantees | Entity-status data is not proof of misconduct or payment ineligibility |
| 2026-08-26 | OPM–Treasury Retirement Services DNP matching notice | Published; legal start 2026-09-25 | Creates a program-specific retirement eligibility, prepayment and recovery match under the M-25-32 waiver architecture | Publication is not matching operation, an individual match or an adverse action |

Sources: [Public Law
119-77](https://www.govinfo.gov/content/pkg/PLAW-119publ77/html/PLAW-119publ77.htm),
[OMB proposed financial-assistance
rule](https://www.federalregister.gov/documents/2026/05/29/2026-10817/regulation-for-federal-financial-assistance),
and [Treasury OpenCorporates
announcement](https://fiscal.treasury.gov/about-us/news/new-do-not-pay-dataset-strengthens-program-ability-to-prevent-improper-payments).

## 8. OPM Retirement Services: the current agency case

OPM's August 26 notice is a child implementation of DNP, not the creation of
the governmentwide system.

| Field | Source-controlled state |
|---|---|
| Participants | OPM and Treasury Bureau of the Fiscal Service |
| OPM program | Retirement Services; CSRS and FERS payment integrity |
| Covered categories | Former employees, annuitants, survivors and beneficiaries |
| OPM identifiers/records | Name, SSN, claim number, TIN, date of birth, address and payment information as specified in the notice |
| Purpose | Continued eligibility, prepayment review and recovery of erroneous retirement payments |
| Publication clock | August 26, 2026 |
| Legal operating clock | September 25, 2026, absent a modification required by comments or review |
| Stated duration | Through September 10, 2029 unless terminated or superseded earlier |
| Decision firewall | DNP information may not be the sole basis for suspension, termination, denial or recoupment |
| Required program action | OPM independently verifies and supplies the applicable notice, opportunity to contest, appeal and recovery process |

Primary notice: [OPM–Treasury DNP matching
program](https://www.federalregister.gov/documents/2026/08/26/2026-17369/privacy-act-of-1974-new-matching-program).

## 9. Claim firewall

| Unsafe shorthand | Controlled statement |
|---|---|
| “DNP is a blacklist.” | DNP is a controlled-access network of multiple data sources, matching products and payment-integrity services. |
| “Treasury decides eligibility.” | The paying or awarding program applies its own authority after independent verification; Treasury operates the shared screening and payment gate. |
| “A match proves fraud.” | A match is a data or risk signal. Intent, eligibility, overpayment, debt and fraud require separate records and legal processes. |
| “Every government payment is checked against everything.” | Federal screening duties are broad, but dataset availability, authority, user access and implementation differ. State reach is principally tied to federally funded State-administered programs. |
| “States now must use DNP for every federal subpayment.” | OMB proposed a State prepayment-review rule in May 2026, with DNP or an alternative; it was not final through this cutoff. |
| “OPM started matching on August 26.” | August 26 is publication. The notice's legal start is September 25, 2026. Operation and individual outcomes remain later evidence clocks. |
| “The $11.7 billion is audited fraud savings.” | Treasury reports a combined FY2025 amount helped prevented, identified or recovered as improper payments. The issuer aggregate mixes categories and is not one audited fraud-loss or savings measure. |

## 10. Why this is structurally material to Freedom 250

The important object is not one list. It is the construction of a reusable
federal screening fabric across three seams:

1. **Identity and entity state:** person, organization, account and source-owner
   attributes are resolved before money moves.
2. **Program eligibility and legal judgment:** the program must translate a
   signal into a lawful, reviewable decision.
3. **Payment release:** Treasury increasingly sits as a common checkpoint just
   before federal disbursement.

The State layer makes the system federated rather than merely federal. State
programs can both supply records and consume controlled matches when spending
federal funds. The unresolved next structural question is whether the May 2026
grants proposal becomes final and pushes a formal prepayment-review duty more
consistently below the federal prime-payment gate.

This fits the Chronicle's Government Fraud definition because it changes **how
public money is watched**, while preserving the project's controlling
distinction between machine eyes and legal judgment.

## 11. Return gates

### OPM Retirement Services first-operation gate — September 25, 2026

Return on or after September 25 for an OPM or Treasury object confirming that
the DNP matching program began unchanged, was modified, or was delayed. Record
operation separately from the first match, payment return, verified eligibility
finding, adverse action, correction or recovery. Do not infer any of those
states from the effective date alone.

### Deceased-person data amendments — December 27, 2026

Recheck SSA and Treasury for the effective State death-data sharing method,
cost agreement, correction notification and first implementation receipt under
Public Law 119-77. Enactment and effectiveness do not by themselves prove a
particular corrected or blocked payment.

### Uniform Guidance flow-down — source-triggered

Recheck Federal Register, OMB and agency adoption surfaces for a final or
withdrawn disposition of the May 29 proposed financial-assistance rule. A final
rule would need its own publication, effective, agency-adoption, State-
implementation and first-operation clocks.

## 12. Primary-source ledger

| Object | Publisher / legal actor | Object type | Controlling clock | URL | Proves | Does not prove |
|---|---|---|---|---|---|---|
| 31 U.S.C. § 3354 | Congress / United States Code | Statute | Current through cutoff | [GovInfo](https://www.govinfo.gov/link/uscode/31/3354) | DNP review duty, minimum sources, State and branch access, payment-required caveat, Privacy Act preservation | Current use by every eligible user or dataset |
| DNP About | Treasury Fiscal Service | Official program page | Retrieved through 2026-08-29 | [Treasury](https://fiscal.treasury.gov/payment-integrity/do-not-pay-dnp/about) | Program owner, purpose and issuer-reported FY2025 aggregate | Independent audit of savings or fraud |
| DNP Products | Treasury Fiscal Service | Official operating-page inventory | Retrieved through 2026-08-29 | [Treasury](https://fiscal.treasury.gov/payment-integrity/do-not-pay-dnp/products) | API, portal, Payment Verification, PARIS and UI hub functions | Universal user participation |
| DNP Data | Treasury Fiscal Service | Official dataset inventory | Page current through 2026-08-19 | [Treasury](https://fiscal.treasury.gov/payment-integrity/do-not-pay-dnp/data) | Published data families and access/restriction architecture | Uniform access or a conclusive outcome |
| DNP Help Center | Treasury Fiscal Service | Official operational guidance | Retrieved through 2026-08-29 | [Treasury](https://fiscal.treasury.gov/payment-integrity/do-not-pay-dnp/help-center) | DNP does not make payment determinations; additional due diligence required | That every agency follows one identical procedure |
| DNP Privacy | Treasury Fiscal Service | Privacy and agreement hub | Page updated 2026-08-27 | [Treasury](https://fiscal.treasury.gov/payment-integrity/do-not-pay-dnp/privacy) | SORN/privacy controls and listed matching agreements | Agreement-level operation beyond each instrument |
| OMB M-25-32 | OMB | Memorandum | 2025-08-20 | [White House PDF](https://www.whitehouse.gov/wp-content/uploads/2025/08/M-25-32-Preventing-Improper-Payments-and-Protecting-Privacy-Through-Do-Not-Pay.pdf) | Routine-use template and limited four-year matching-agreement waiver | Waiver of all Privacy Act or contest protections |
| Public Law 119-77 | Congress / President | Enacted law | Approved 2026-02-10; effective 2026-12-27 | [GovInfo](https://www.govinfo.gov/content/pkg/PLAW-119publ77/html/PLAW-119publ77.htm) | State death-data sharing, correction notice and evidence threshold amendments | Current implementation before effective date |
| OMB financial-assistance revisions | OMB and adopting agencies | Proposed rule, 91 FR 32198 | Published 2026-05-29; comments closed 2026-07-13 | [Federal Register](https://www.federalregister.gov/documents/2026/05/29/2026-10817/regulation-for-federal-financial-assistance) | Proposed State and federal prepayment screening requirements | Final or operative rule |
| OpenCorporates dataset addition | Treasury Fiscal Service | Official announcement | 2026-08-19 | [Treasury](https://fiscal.treasury.gov/about-us/news/new-do-not-pay-dataset-strengthens-program-ability-to-prevent-improper-payments) | Treasury says U.S. entity-status data became available in DNP | Ineligibility or misconduct of a particular entity |
| OPM Retirement Services match | OPM and Treasury | Privacy Act matching notice | Published 2026-08-26; effective 2026-09-25 | [Federal Register](https://www.federalregister.gov/documents/2026/08/26/2026-17369/privacy-act-of-1974-new-matching-program) | Program scope, identifiers, clocks, verification and contest safeguards | Operation before effective date or an individual outcome |

## 13. Completion receipt

- **Question answered:** legal object, operating products, datasets,
  government-level reach, OPM implementation and future expansions mapped.
- **Source boundary:** primary federal law, Treasury, OMB, OPM and Federal
  Register sources reached through August 29, 2026.
- **Disposition:** `keep` as an Official Research Desk Reference Object under
  `fraud-payment-integrity`; Workbench artifact lifecycle `pending` for any
  later Chronicle disposition.
- **Duplicate handling:** folded into the existing Fraud and Payment Integrity
  family rather than creating a second top-level family.
- **Return Ledger:** added `ret-opm-dnp-first-operation-2026-09-25`, pointing
  to the literal gate above. The December death-data and proposed-rule states
  remain package context unless Katie separately chooses active return
  tracking.
- **Actions not taken:** no Chronicle promotion, event note, canonical watch,
  app sync, build, install, commit or push.
- **Projection receipt:** the Workbench Catalog/Registry/Return Ledger are
  current and globally healthy. The authorized live Research Desk rebuild was
  attempted on August 29 but failed closed before completion because existing
  live watch `w-2026-09-28-itar-ase-comments` references unknown research ID
  `ss-2026-08-28`. That unrelated watch was not changed; generated Desk/Search
  and app surfaces must not be described as refreshed by this save.
