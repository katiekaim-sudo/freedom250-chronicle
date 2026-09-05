> Source cutoff: 2026-08-23 ET

# SSA, VA and DOJ AI rights and service map

## Bottom line

These three agencies expose three different forms of rights-affecting AI
transition.

1. **SSA has the smallest and most legible high-impact portfolio.** Its current
   inventory reports nine high-impact uses: eight deployed and one pilot. They
   touch disability allowances and denials, continuing-disability reviews,
   hearings triage, SSI redetermination, identity verification and vocational
   assessment. SSA's strategy says AI supplies recommendations or options and
   never decides on its own. The use-case records support that boundary for
   IMAGEN, PAT and VAAT, but several older scoring systems influence which
   claims or reviews receive attention. ID.me is the one high-impact SSA row
   whose testing, independent-review, monitoring and training fields were
   still blank and whose impact assessment was `In-progress` in the published
   2025 inventory.
2. **VA has the largest safety-and-service portfolio and the clearest public
   post-deadline control return.** Its April 2026 workbook still contains 367
   individual cases, 215 high-impact. It now classifies 90 as both deployed and
   high-impact; all 90 say testing, impact assessment, independent review,
   monitoring and operator training are established. VA also contains the
   sharpest automation exception in this wave: `VA-24-1938` says roughly 30%
   of covered National Cemetery Administration certificate determinations are
   completed within 24 hours without human intervention. The blanket phrase
   “a human always makes the final VA decision” is therefore unsafe.
3. **DOJ is the least publicly resolved after the M-25-21 implementation
   deadline.** DOJ's January 30, 2026 page says 315 entries; the latest OMB
   consolidated file located here contains 314 DOJ rows and 312 unique IDs.
   It reports 73 deployed high-impact rows, and every one marks all eight
   minimum-practice fields `In-progress`. As of the cutoff, DOJ had not
   published the promised M-25-21 compliance plan or AI strategy located in
   its FY2025 Chief Data Officer report, nor a public waiver, termination or
   post-April 3 disposition for those rows. This is a material unresolved
   control state, not proof that the practices were not completed internally.
4. **The supplier story is component- and workload-specific, not one federal
   AI cloud.** SSA discloses a hybrid on-premises/cloud/SaaS architecture and
   named ID.me, IBM, Microsoft/OpenAI, AWS and Hyperscience relationships. VA
   discloses Summit Data Platform, VA GPT, AWS enterprise capacity, Microsoft
   services, Oracle Health, Abridge, Knowtex and IBM. DOJ discloses a
   fragmented enforcement/evidence stack—Axon, Palantir, Clearview, PenLink,
   Veritone, Thomson Reuters, SoundThinking, Flock, AWS, Azure, NVIDIA and
   OpenAI—but many component inventories omit the prime or award crosswalk.
5. **Inventory labels are not findings.** A row can say `High-impact`, `Not
   High-impact`, `ATO: Yes`, `ATO: No`, or `PII: No`; none of those labels alone
   proves lawfulness, harmlessness, security, accuracy or the factual absence
   of personal data. This wave preserves the agency's label and separately
   describes the function.

## Method and materiality screen

This wave follows the package's
`FEDERAL_AGENCY_AI_PLAN_MATERIALITY_CONSTITUTION_2026-08-23.md`.
It retains only systems that affect benefits, disability, health, fraud,
identity, surveillance, investigation, detention, evidence, prosecution,
adjudication or a shared compute/data/model plane. DOJ's low-stakes drafting,
training, recruiting, meeting and generic office-product rows are not
enumerated.

The inventory totals are evidence-snapshot counts, not a claim of perfect
coverage. Stage, high-impact status, ATO, PII and risk-practice values below
are agency-reported fields unless an independent official assessment is
expressly identified.

## Controlling source and document inventory

| Entity | Strategy / compliance object | Latest inventory reached | Governance and update state |
|---|---|---|---|
| SSA | [Enterprise AI Strategy, Sep. 2025](https://www.ssa.gov/ai/policy/SSA%20Enterprise%20Artificial%20Intelligence%20Strategy%20Report.pdf); [M-25-21 Compliance Plan, Sep. 2025](https://www.ssa.gov/ai/policy/SSA%20AI%20Compliance%20Plan.pdf) | [SSA AI hub and 2025 inventory](https://www.ssa.gov/ai); agency CSV dated Jan. 2026, also consolidated in OMB's official repository | CAIO, Responsible AI Core Team and ATO process; CAIO may terminate a noncompliant system. No separate SSA waiver criteria beyond OMB were published. |
| VA | [2025 AI Strategy](https://department.va.gov/ai/building-the-future-vas-strategy-for-adopting-high-impact-artificial-intelligence-to-improve-services-for-veterans/); [M-25-21 Compliance Plan](https://department.va.gov/ai/department-of-veterans-affairs-compliance-plan-for-omb-memorandum-m-25-21/); [GenAI guidance](https://department.va.gov/ai/guidance-for-generative-ai-use-at-va/) | [April 2026 compliance-update workbook](https://department.va.gov/ai/wp-content/uploads/sites/26/2026/04/VA-AI-Use-Case-Inventory-2025-Web-Compliance-Updates.xlsx) on the [VA inventory page](https://department.va.gov/ai/ai-use-case-inventory/) | AI Impact Assessments and Risk Mitigation Plans for deployed high-impact systems; independent review; DATO/VA-boundary blocking termination route; no waivers issued as of the Sep. 2025 plan. |
| DOJ | No public M-25-21 plan or current AI strategy located. DOJ's public plan is the superseded [M-24-10 compliance plan, Oct. 2024](https://www.justice.gov/media/1373026/dl). The [FY2025 CDO Annual Report](https://www.justice.gov/open/media/1442676/dl?inline=) says DOJ planned an Interim AI Policy, DOJ AI Strategy and Compliance Plan, governance rubric and literacy campaign. | [DOJ AI inventory page](https://www.justice.gov/ai/ai-inventory), updated Jan. 30, 2026, says 315 entries; OMB's latest consolidated file has 314 rows / 312 unique IDs | Public post-Apr. 3, 2026 minimum-practice, waiver, termination and CAIO disposition remains unresolved. |

Official cross-agency inventory shelf: [OMB 2025 Federal Agency AI Use Case
Inventory repository](https://github.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory).

### Snapshot counts and reconciliation

| Entity / source | Total | Deployed | Pilot | Pre-deployment | Retired | High-impact total | High-impact deployed |
|---|---:|---:|---:|---:|---:|---:|---:|
| SSA / Jan. 2026 agency file | 33 | 27 | 4 | 2 | 0 | 9 | 8 |
| VA / OMB consolidated source | 367 | 138 | 21 | 136 | 72 | 215 | 94 |
| VA / current Apr. 2026 agency workbook | 367 | 134 | 21 | 138 | 74 | 215 | 90 |
| DOJ / OMB consolidated source | 314 rows | 163 | 25 | 107 | 19 | 114 | 73 |

The current VA agency workbook is the controlling stage snapshot in this wave;
the OMB row is retained to show that the current workbook reclassified part of
the portfolio after the consolidated source was assembled. DOJ's OMB file has
two repeated public IDs: `DOJ-0357` is duplicated identically, while
`DOJ-0160` appears for both FBOP and OJP with conflicting high-impact labels.
Therefore `row`, `entry`, `use case` and `unique ID` are not interchangeable.

## SSA — benefits, disability and identity

### Material high-impact uses

SSA's submission leaves the public `id` field blank for all 33 rows. The exact
published use-case names below are therefore the public identifiers.

| Published use case | Stage / supplier | Rights-affecting function | Human / control boundary at cutoff |
|---|---|---|---|
| Policy Assistance Tool (PAT) | Pilot; Microsoft / OpenAI; ATO yes | Answers policy questions from PolicyNet and returns source links. A wrong answer can alter claim handling. | Users are told to verify the cited policy. Testing and impact assessment say yes; monitoring is in progress. |
| Pre-Effectuation Review / Targeted Denial Review Models | Deployed since 2003; in-house; ATO no | Produces probability scores used to select disability allowances or denials for review. False positives can change processing. | Testing, assessment, CAIO review, monitoring, training and appeal are reported; inventory calls a failsafe not applicable. |
| Continuing Disability Review Model | Deployed since 2023; in-house; ATO no | Scores likelihood of medical improvement and places records in low/medium/high groups. | Controls and appeal are reported established; the score routes review, not a published stand-alone cessation decision. |
| SSI Redetermination Model | Deployed since 1999; in-house; ATO no | Scores likelihood and likely amount of overpayment for redetermination workload. | Controls are reported; appeal is marked not applicable in this AI row. A score is not itself a fraud or debt adjudication. |
| Proactive Triage and Analysis of Hearings (PATH) | Deployed since 2024; in-house; ATO no | Sorts hearings by likelihood of a favorable outcome; the inventory identifies misclassification and bias risk. | Fairness testing and human review are described; appeal is marked not applicable in the AI row. |
| Digital Identity Verification Services | Deployed since 2020; ID.me; ATO yes | Returns verification results, risk indicators and fraud alerts; failure can deny or delay digital access. | Impact assessment `In-progress`; testing, independent review, monitoring and training blank; failsafe yes; appeal `Precluded by Law`. Inventory says `PII: No`; do not convert that field into proof that identity proofing uses no personal data. |
| Intelligent Medical Language Analysis Generation (IMAGEN) | Deployed since 2021; in-house; ATO yes | Extracts and annotates medical evidence with impairment and listing codes for disability processing. | SSA says IMAGEN never suggests an adverse outcome; testing, assessment, CAIO review, monitoring, training and failsafe are reported. |
| Vocational Assessment Assistant Tool (VAAT) | Deployed Sep. 30, 2025; Microsoft / OpenAI; ATO yes | Produces vocational recommendations and structured explanations; inventory identifies risk of wrong grants or denials. | Human adjudicative action remains required; all listed controls are reported established. Public PIA field says `not publicly available`. |
| Quick Disability Determinations Model | Deployed since 2008; IBM; ATO yes | Scores possible allowance and processing time to accelerate likely qualifying claims. | False negatives may delay a claimant; testing, assessment, CAIO review, monitoring, training, failsafe and appeal are reported. |

Across the nine rows, eight report completed testing and eight completed impact
assessments; ID.me is the exception. Five report an ATO and four `ATO: No`.
Seven PIA URL fields are blank, one points to an older eAuthentication PIA and
VAAT says its PIA is not publicly available. A blank URL is a crosswalk gap,
not proof that no privacy analysis exists.

### SSA platform, supplier and capital map

SSA's strategy places these systems in a hybrid on-premises, cloud and SaaS
architecture with external integrators, secure data pipelines and planned
shared services. It targets AI maturity Level 3 of 5 by **September 30, 2026**
and Level 4 by FY2030. The strategy says central shared platforms remain under
exploration, so it is too early to name one proven universal SSA model plane.

| Workload / platform | Award recipient / underlying supplier | Located obligation and clock | Proof limit |
|---|---|---:|---|
| Digital identity verification | ID.ME LLC / ID.me | `28321326FA0010073`; $23,624,100; Mar. 31-Dec. 31, 2026 | Current IAM/SSO licenses and support; not proof of accuracy, coverage or appeal adequacy. Prior V3Gate order totaled $57,407,450.90 and ended Mar. 20, 2026. |
| Hyperscience document processing | Accenture Federal Services / Hyperscience | `28321326FDS030056`; $11,611,420.86; Apr. 24, 2026-Mar. 14, 2027 | Licenses, maintenance and support; does not allocate performance to a named high-impact use case. |
| Quick Disability Determinations scoring | IBM | `28321324FA0010044`; $3,072,342.63; ended Jan. 31, 2025 | Historical scoring-services order; no public successor located by the cutoff. Inventory deployment does not prove contractual cessation. |
| AWS Connect contact-center service | Four Points Technology / AWS | `28321324FA0010214`; $150,447,391; Aug. 1, 2024-Jul. 31, 2027 | Large contact-center cloud rail, not an AI-only amount and not proof every SSA AI workload runs on AWS. |
| PAT and VAAT | SSA / Microsoft / OpenAI | Vendors named in inventory; no award amount directly allocating price located | Do not infer Microsoft prime, OpenAI prime, model version or workload spend. |

### SSA return objects

- SSA OIG's **The Social Security Administration's Use of Artificial
  Intelligence**, entered March 30, 2026 and targeted for FY2027 Q2 on the
  [ongoing-audits page](https://oig.ssa.gov/audit-reports/ongoing-audits/).
- SSA OIG's **SSA Amazon Web Services Contract**, targeted for FY2026 Q4.
- Completed ID.me impact assessment, testing, independent review, monitoring,
  training and any usable appeal/remedy disclosure.
- A current IBM QDD scoring order or a retirement / replacement record.
- Evidence that SSA reached Level 3 maturity by Sep. 30, 2026, including the
  exact shared platform or evaluation service accepted into operation.

## VA — health, claims, fraud and physical security

### Benefits, claims and fraud

| ID / use case | Current stage / impact | Function and material boundary |
|---|---|---|
| `VA-24-1938` Automated Claims Processing | Deployed / high-impact | Hyperscience OCR/NLP/ML/RPA processes Pre-Need and Presidential Memorial certificates. The workbook says about 30% of determinations are completed within 24 hours without human intervention. This is actual bounded automation, not merely recommendation. |
| `VA-24-790` Pension Optimization Initiative | Deployed / high-impact | Vendor-purchased process updates claimant files, starts or stops awards and generates notices. The current row reports all minimum practices and public-feedback solicitation. |
| `VA-24-4722` Automated Decision Support | Deployed / high-impact | Indexes evidence, orders or drafts exams and marks claims Ready for Decision; VA expressly says it does not make final benefits decisions or payments. |
| `VA-24-3291` Payment Redirect Fraud Model | Deployed / high-impact | Identifies roughly 1-2 per 1,000 direct-deposit changes for referral to investigators. A flag or referral is not a fraud finding. |
| `VA-25-1594` Automated Ratings Summarization | Pre-deployment / high-impact | Proposed rating-evidence summarization; no deployed decision state is established. |
| `VA-25-3480` Smart Pension Automation | Pre-deployment / high-impact | Proposed pension workflow with award/off-ramp reporting and audit information for human review. |
| `VA-25-393` Predictive Claims Processing Capability POC | Pre-deployment / high-impact | Proposed education-benefit decisioning without the current rules engine. No deployment or acceptance is established. |
| `VA-25-6965` Smart Ratings Recommendation | Pre-deployment / high-impact | Proposed recommendation that a rating VSR can approve or reject; no final action until a human acts. |

### Clinical care and patient safety

| ID / use case | Current stage / impact | Function and human boundary |
|---|---|---|
| `VA-24-4152` STORM | Deployed / high-impact | Predicts one-year overdose, suicide and mortality risk for team review. VA associates the program with a 22% mortality reduction; the association is an agency-reported outcome, not randomized causal proof. |
| `VA-24-4234` REACH VET | Deployed / high-impact | Predicts one-month suicide mortality risk across active VHA patients and prompts provider review and outreach. |
| `VA-24-1684` GI Genius CADe | Deployed / high-impact | Real-time colonoscopy bounding boxes; clinician conducts and interprets the procedure. VA reports 21% higher odds of adenoma detection and a four-point absolute increase. |
| `VA-24-1803` Aidoc BriefCase | Deployed / high-impact | Cloud triage and preview; VA states the preview is not for diagnostic use and original images remain subject to clinician review. |
| `VA-24-708` Abridge Ambient Scribe | Pilot / high-impact | Produces draft clinical notes from encounter audio for clinician review. Pilot status is not enterprise clinical acceptance. |
| `VA-25-6426` Knowtex Ambient Scribe | Pilot / high-impact | Produces draft notes for clinician review; same pilot/acceptance boundary. |

### Surveillance and access control

`VA-24-36` Evolv weapons detection is deployed and high-impact; a weapons alert
routes security attention and is not itself a legal finding. `VA-24-77`
Avigilon camera/search is now **retired** and high-impact in the April workbook,
so the older deployed state must not be carried forward. The workbook contains
other medical-device and physical-security systems, but they are excluded here
unless they materially alter care, access or investigative attention.

### VA high-impact and human-review boundary

The April workbook classifies 90 rows as deployed/high-impact. All 90 report
`Yes` for predeployment testing, impact assessment and independent review; all
90 report monitoring and periodic operator training. Eighty-six report a
failsafe and four `Not Applicable`; 79 report an appeal process and 11 `Not
applicable`. Eighteen report direct usability testing, one general public
solicitation and 71 `Other` consultation.

These are VA's self-reported compliance fields. They do not substitute for the
underlying impact assessments, test results, independent-review memoranda,
monitoring thresholds or appeal instructions. Blank fields on pilot,
predeployment and retired rows cannot be read as proof that controls are
absent; the added workbook columns are expressly for deployed high-impact
cases. VA's plan set **April 3, 2026** as the point by which operating systems
needed compliance, waiver or removal. The April workbook is therefore a
material post-deadline self-report, but not an independent audit.

### VA platform, supplier and capital map

- **Summit Data Platform** is VA's disclosed cloud access point for refined
  health and customer-experience data, tools and monitoring. Public sources do
  not disclose the complete cloud/provider allocation for each AI workload.
- **VA GPT** (`VA-24-3086`) is deployed and not classified high-impact. VA says
  it serves roughly 95,000 users on the current page (the compliance plan said
  about 100,000), inside the VA network. VA also identifies Teams Premium and
  Microsoft Copilot Chat integration. User availability is not adoption,
  savings or mission-performance proof.
- VA's strategy targets ten more production AI cases on enterprise data
  platforms in FY2026 and 100% high-impact compliance. These are goal clocks,
  not accepted results.

| Workload / platform | Prime / underlying supplier | Located obligation and clock | Proof limit |
|---|---|---:|---|
| Abridge ambient documentation | Abridge AI Inc. | `36C10G25C0011`; $14,984,720; Jun. 23, 2025-Sep. 28, 2026 | Cloud-hosted COTS SaaS on contractor infrastructure; ATO/FedRAMP terms do not prove clinical accuracy or rollout breadth. |
| Knowtex ambient documentation | Knowtex Inc. | `36C10G25C0013`; $14,996,000; Jul. 21, 2025-Jan. 21, 2027 | Same boundary; award and inventory establish pilot capacity, not accepted enterprise deployment. |
| Pension Optimization Initiative | IBM | `36C10D22N0008`; $60,679,588.63; ends Aug. 31, 2026 | Eight-day successor cliff after the cutoff; a contract end is not proof the workflow stopped. |
| Enterprise Cloud Capacity - AWS | Four Points Technology / AWS | `36C10B22F0207`; $521,824,443.39; Aug. 3, 2022-Feb. 2, 2027 | Enterprise AWS rail, not AI-only spend and not proof every named VA model runs there. |
| EHR modernization substrate | Oracle Health | `36C10B24N0063EHRM`; $299,999,848.61; Sep. 30, 2024-Sep. 29, 2027 | Major clinical data/record substrate; full amount cannot be called AI spend. |
| Automated Claims Processing | VA names Hyperscience product | No directly crosswalked VA award located | Do not import SSA's Accenture/Hyperscience award into VA or invent a VA prime. |

### VA return objects

- **Resolved continuity receipt:** USAspending modification P00018 exercised
  IBM Option 4 on August 24, 2026, obligated $14,941,471.41 and moved the
  current award-period end to August 31, 2027. This proves contractual
  continuity, not payment, uninterrupted operation, performance quality,
  claimant accuracy, savings or remedial outcomes.
- Abridge disposition by Sep. 28, 2026: renewal, successor, scale acceptance,
  pause or termination; Knowtex disposition by Jan. 21, 2027.
- The underlying impact assessments, independent reviews and monitoring
  results for Automated Claims Processing, Pension Optimization, PRF, STORM,
  REACH VET, GI Genius and Aidoc.
- FY2026 proof of the ten additional production launches: exact IDs, acceptance
  dates, platforms, populations and retirement/replacement edges.
- Operating explanation for the current workbook's shift from 138 to 134
  deployed cases and from 72 to 74 retired cases relative to the OMB snapshot.

## DOJ — surveillance, investigation, evidence and adjudication

### Materiality-screened investigative and surveillance systems

| ID / component | Stage / impact | Supplier / function | Boundary and proof limit |
|---|---|---|---|
| `DOJ-0028` ATF ShotSpotter | Deployed / high-impact | SoundThinking; state/local gunshot-detection access | An alert is an investigative input, not proof of a shooting or suspect. ATF is not the operating system owner. |
| `DOJ-0035` ATF commercial LPR | Deployed / high-impact | Flock Safety through HIDTA partners | Partner access does not establish ATF control of model, retention, watchlists or corrective process. |
| `DOJ-0048` CRM CLEAR LPR | Deployed / high-impact | Thomson Reuters; images and location history | `ATO: No` in inventory; location output is an investigative lead, not guilt. |
| `DOJ-0064` DEA commercial LPR | Deployed / high-impact | Vendor not publicly named | Preserve vendor as unknown. |
| `DOJ-0084` DEA financial and cryptocurrency analysis | Deployed / high-impact | Vendor not publicly named; profiles, alerts, chatbot and link analysis | A profile, alert or link is not a fraud, laundering or criminal finding. |
| `DOJ-0121` FBI data synthesis, sentiment, filtering and location linking | Deployed / high-impact | Vendor not named | Inventory reports PII yes and ATO no; neither field establishes legality or operational weight. |
| `DOJ-0122` FBI facial recognition | Deployed / high-impact | In-house | Produces potential leads. Inventory says `PII: No`; preserve as agency field, not a factual conclusion about face data. |
| `DOJ-0126` FBI facial recognition and mapping | Deployed / high-impact | Vendor not named | Candidate matches go to human review; ATO no in inventory. |
| `DOJ-0135` FBI Next Generation Identification | Deployed / high-impact | Vendor-purchased; vendor not named | Biometric/name candidate leads; ATO yes. Candidate generation is not identification adjudication. |
| `DOJ-0226` USMS facial recognition | Deployed / high-impact | Clearview AI | Inventory says output is a lead only, never grounds for action, and must be corroborated. |
| `DOJ-0327` USMS AWS Rekognition | Pre-deployment / high-impact | AWS product named | Proposed face index to flag possible duplicate Capture records; no deployment or decision state established. |

### Evidence, prosecution, incarceration and immigration

| ID / component | Stage / impact | Material function and boundary |
|---|---|---|
| `DOJ-0015` ATF Axon Evidence.com | Deployed / high-impact | Evidence store includes head-recognition/redaction features, but ATF says the AI features are not operationally used. The product's deployment is not AI-feature deployment. |
| `DOJ-0025` ATF Palantir via state system | Deployed / high-impact | ATF says it performs standard search only and does not know the partner's AI-feature use. Do not call this an ATF Palantir AI deployment. |
| `DOJ-0088` DEA PenLink PLX | Deployed / high-impact | Transcribes/translates seized, correctional or authorized communications; human translators and analysts review outputs. |
| `DOJ-0103` departmentwide Digital Forensics | Deployed / high-impact | Cellebrite, Magnet Axiom and Griffeye extract and analyze device/media evidence. Tool output remains evidence-processing support, not authentication, admissibility or guilt. |
| `DOJ-0244` departmentwide Veritone | Deployed / high-impact | Preliminary transcription/translation; DOJ expressly says it is not the official evidence translation. |
| `DOJ-0117` EOUSA Evidence.com | Deployed Mar. 2025 / high-impact | Axon reports, narratives and summaries; inventory says ATO no. A generated narrative is not a filed allegation or admitted exhibit. |
| `DOJ-0272` EOUSA Palantir | Deployed Jun. 2025 / high-impact | Integrates case information and produces summaries; inventory says ATO no. |
| `DOJ-0313` EOUSA CoCounsel AI | Pilot / high-impact | Thomson Reuters transcription, tagging and object/facial-recognition support; no production acceptance established. |
| `DOJ-0160` PATTERN | Deployed / conflicting public label | Produces recidivism-risk calculations. The same ID appears as FBOP `Not High-impact` and OJP `High-impact`; component and label must travel with the row. |
| `DOJ-0287` EOIR immigration filing intake | Pre-deployment / high-impact | Proposed automated accept/reject above a threshold with manual processing below it. No operating adjudication is proven. |
| `DOJ-0298` EOIR adjudicator notice/order assistance | Pre-deployment / high-impact | Proposed drafting with citations and source links for adjudicator review; not an issued order. |
| `DOJ-0324` EOIR background searches | Deployed / high-impact | TransUnion searches support character-and-fitness review for accredited representatives; ATO and PII both yes. |

### DOJ minimum-practice and privacy boundary

For all 73 rows that the OMB file classifies both deployed and high-impact,
DOJ reports predeployment testing, impact assessment, independent review,
monitoring, training, failsafe, appeal and public consultation as
`In-progress`. Of all 114 DOJ high-impact rows, 30 report an ATO, 50 `No` and
34 are blank. All 114 leave the PIA URL field blank.

The blank PIA column is not proof of no privacy assessment. DOJ's Office of
Privacy and Civil Liberties publishes PIAs outside the inventory, including
the [EOUSA Palantir PIA](https://www.justice.gov/opcl/media/1427686/dl), the
[Joint Automated Booking System PIA](https://www.justice.gov/opcl/media/1397866/dl?inline=)
and the [OIG Axon body-camera PIA](https://www.justice.gov/opcl/page/file/1497856/dl?inline=).
The Palantir PIA describes records from warrants, subpoenas and discovery; the
JABS PIA describes a face probe that can return up to 20 candidates to trained
examiners. DOJ's inventory therefore has a public crosswalk problem: use case,
system, PIA, ATO and component do not reliably join in one file.

The [FBI's official face-services explanation](https://www.justice.gov/archives/opa/speech/associate-deputy-attorney-general-sujit-raman-delivers-remarks-community-oriented)
says candidate photos cannot alone support enforcement and must be
investigated and corroborated. That is an announced policy boundary, not proof
that every use, match or downstream action complied.

### DOJ compute, data, supplier and capital map

No public source located establishes one accepted departmentwide AI platform.
The inventory instead shows component stacks and partner-controlled systems.
Material shared or enabling edges include:

- `DOJ-0090` DEA Generative AI R&D Sandbox, a **pilot/high-impact** NVIDIA-named
  environment; `DOJ-0316` DEA employee policy chatbot is a separate
  **pilot/high-impact** OpenAI-named use. Vendor naming does not establish the
  prime, model version, hosting location or award allocation.
- AWS supports DEA, EOUSA, BOP, Antitrust and USMS component clouds; Azure is
  also present. Cloud capacity is not proof a particular AI model runs there.
- Axon, Palantir, PenLink, Veritone, Clearview, Thomson Reuters, SoundThinking,
  Flock, Cellebrite, Magnet Axiom and Griffeye are named workload suppliers;
  partner-managed access and direct DOJ operation remain separate.

| Workload / platform | Prime / underlying supplier | Located obligation and clock | State / proof limit |
|---|---|---:|---|
| EOUSA Case360 / Palantir | Palantir | `15JPSS25F00000911`; $4,729,656.52; ended Jun. 8, 2026 | Inventory still says deployed; no keyword-located successor. Award-gap watch, not proof of system cessation. |
| Axon Evidence High ELA | Axon | `15M10426PA4700003`; $4,377,002.42; Jan. 1-Dec. 31, 2026 | Active license rail; does not prove every AI feature is operational. |
| USMS Clearview | Clearview AI | `15M10226PA4700083`; $78,750; Mar. 12, 2026-Mar. 11, 2027 | Active investigative-lead capability. |
| FBI Clearview | Clearview AI | `15F06726P0000453`; $150,000; Jan. 26, 2026-Jul. 27, 2027 | Separate component award; do not merge populations or controls with USMS. |
| DEA PenLink | PenLink | `15DDHQ26P00000152`; $90,429.78; structured end Nov. 30, 2026 | Award description says support through Jan. 28, 2027, conflicting with structured period. Both clocks require resolution. |
| Veritone translation/transcription | Veritone | `15JPSS25F00000938`; $72,500; Oct. 1, 2025-Sep. 30, 2026 | Evidence-assistance rail; not official evidentiary translation. |
| DEA AWS | AWS capacity award | `15DDHQ25F00000860`; $8,021,505; Oct. 1, 2025-Sep. 30, 2026 | Component cloud, not AI-only spend. |
| EOUSA AWS | AWS capacity award | `15JPSS21F00000961`; $10,870,099.08; through Jul. 17, 2027 | Same boundary. |
| BOP AWS | Effectual / AWS | `15BPCC26F00000053`; $21,611,764; Apr. 1, 2026-Mar. 31, 2027 | Managed component cloud; not a PATTERN allocation. |
| USMS AWS | AWS capacity award | `15JPSS26F00000971`; $1,448,800.69; ended Jul. 16, 2026 | No direct successor located; expiry is not proof workloads stopped. |
| FBI NVIDIA GPUs | NVIDIA equipment via award `15F06725F0001743` | $33,220.16; Sep. 19, 2025-Sep. 18, 2026 | FBI award is not proof of the DEA sandbox's compute source. |
| USMS Azure | Microsoft Azure capacity | `15JPSS25F00000883`; $215,439.48; ended Apr. 30, 2026 | No current successor located; do not infer migration or cessation. |

Award amounts and periods are from the official
[USAspending API](https://api.usaspending.gov/) as updated through the cutoff;
PIIDs are the durable lookup keys. Values are located obligations/current award
amounts, not contract ceilings or AI-only allocations unless expressly stated.

### DOJ return objects

- The promised M-25-21 DOJ AI Strategy and Compliance Plan, Interim AI Policy,
  governance rubric and literacy campaign named in the FY2025 CDO report.
- A post-Apr. 3, 2026 disposition for the 73 deployed/high-impact rows: completed
  control fields, named waivers, discontinuations or other CAIO decisions.
- Underlying AI Impact Assessments, independent-review reports, monitoring
  thresholds, failsafe procedures, appeal routes and public-consultation
  records for facial recognition, LPR, data synthesis, financial/crypto
  analysis, PATTERN, evidence and immigration uses.
- Reconciled DOJ inventory export: 315-page count versus 314 rows, duplicate
  `DOJ-0357`, and component-conflicting `DOJ-0160`.
- Workload-to-PIA-to-ATO crosswalk, especially for Palantir, Axon, Clearview,
  NGI, JABS, LPR and evidence-processing systems.
- Palantir Case360 successor or retirement record; USMS AWS and Azure successor
  or migration record; DEA AWS/Veritone Sep. 30, 2026 dispositions; PenLink's
  Nov. 30, 2026 versus Jan. 28, 2027 contract-clock reconciliation.
- Prime/hosting/model/version disclosure for the DEA NVIDIA sandbox and OpenAI
  policy chatbot. Unknowns remain unknown until a public award or architecture
  object returns.

## Cross-agency human-review boundary

| Boundary | SSA | VA | DOJ |
|---|---|---|---|
| Recommendation / triage | PAT, VAAT, IMAGEN, QDD, PATH and review models inform staff or workload routing | Smart Ratings proposal, Automated Decision Support, PRF referrals, clinical alerts and image triage | Facial-recognition candidates, LPR/location links, analytic profiles, translations and case summaries inform investigators, counsel or adjudicators |
| Bounded automation | No public high-impact row reviewed here is described as a stand-alone final adverse decision | `VA-24-1938` expressly reports some certificate determinations without human intervention; Pension Optimization also changes awards/files and notices | EOIR filing intake proposes threshold-based automated accept/reject but is pre-deployment; no deployed final prosecutorial or judicial decision was established |
| Human-review claim limit | “Human centered” does not disclose automation weight, override frequency or time pressure | A human role in most uses cannot erase the specific automated-claims exception | “Lead only” or “human review” does not prove corroboration quality, disclosure to affected persons, admissibility or non-reliance |
| Remedy | Appeals reported for some disability models; ID.me says appeal precluded by law | 79 of 90 deployed/high-impact rows say appeal established; 11 say not applicable | 73 deployed/high-impact rows still say appeal process in progress in the inventory snapshot |

## Existing-research overlaps and genuine deltas

| Existing Observatory research | Overlap | New state supplied by this wave | Ruling |
|---|---|---|---|
| `Human Systems Full-Surface Wave 2026-08-04` and the Aug. 22 health sublane | SSA/VA benefit, health and publisher surfaces | Exact disability, claims, suicide/overdose, imaging, ambient-scribe and control states plus award clocks | **Complement, not duplicate.** Prior work found no short-window SSA/VA policy change; this is a system/infrastructure baseline. |
| `EMERGING_FRAUD_HEARING_RESEARCH_PACKAGE.md`, `OBBB_FRAUD_ERROR_RATE_LEGAL_MAP.md` and federal-funds watchboard | Identity, eligibility, risk scoring, payment redirection and fraud referral | ID.me control gap, SSA selection models, VA PRF and DOJ financial/crypto analytic systems | **Join with firewall.** A risk score, flag, match or referral is not fraud, ineligibility, debt or guilt. |
| `SSA_CITIZENSHIP_IDENTITY_AND_ELIGIBILITY_ARCHITECTURE.md` | SSA identity and eligibility data/control layer | Digital front-door ID.me award and high-impact AI control fields | **New supplier/control edge; no claim that digital identity verification decides citizenship or benefit eligibility.** |
| `Justice Homeland Civil Administration Full-Surface Wave 2026-08-04` and justice freshness lanes | DOJ publisher, enforcement, court and accountability coverage | Material inventory screen across surveillance, evidence, prosecution, detention and EOIR; control and award gaps | **Complement.** Do not turn an AI lead into a DOJ allegation, charge, exhibit, order or judgment. |
| `NARA_COMPUTE_AND_INFRASTRUCTURE_SUPPLIER_MAP_2026-08-23.md` and `MILITARY_COMMAND_DATA_CONTROL_STACK.md` | Multi-cloud, reseller/prime/provider separation, Palantir and AI infrastructure control | Civil rights/service workloads and component-level cloud cliffs | **Structural overlap only.** NARA, Defense, SSA, VA and DOJ supplier edges must not be collapsed into one governmentwide platform. |

## Priority return-object watchboard

| Priority | Return object | Exact clock / trigger | State change it could prove |
|---|---|---|---|
| P0 | DOJ M-25-21 plan plus post-deadline controls, waivers and terminations | Already due / unresolved at Aug. 23, 2026 | `in-progress snapshot -> completed control`, `waiver`, or `discontinued` for deployed high-impact systems |
| Resolved | VA IBM Pension Optimization Option 4 | P00018 action Aug. 24, 2026; current period through Aug. 31, 2027 | `deployed under expiring award -> contractual Option 4 continuity`; payment and operating outcomes remain unproved |
| P0 | SSA ID.me completed high-impact controls | Next inventory / assessment publication; current award ends Dec. 31, 2026 | Resolves testing, assessment, review, monitoring, training and remedy state |
| P1 | DOJ DEA AWS and Veritone dispositions | Sep. 30, 2026 | Component cloud/evidence rail renewed, migrated or ended |
| P1 | SSA Level 3 maturity evidence | Sep. 30, 2026 | Strategy target becomes measured operating state or remains unmet/unproved |
| P1 | VA Abridge disposition | Sep. 28, 2026 | Pilot capacity becomes scaled/accepted, renewed, paused or ended |
| P1 | DOJ Axon ELA and SSA ID.me renewal | Dec. 31, 2026 | Supplier continuity or replacement |
| P1 | SSA OIG AWS audit | FY2026 Q4 | Independent cost, governance or performance finding |
| P1 | SSA OIG AI audit | FY2027 Q2 | Independent use-case, control or performance finding |
| P2 | VA ten additional FY2026 production cases | FY2026 close and next inventory | Named launch/acceptance, not strategy language |

## Safe claims and proof limits

Safe at the cutoff:

- SSA publicly reports nine high-impact AI rows, VA 215 and DOJ 114 in the
  official 2025 inventory family; the agencies use different schemas and
  update clocks.
- The current VA workbook self-reports completed core practices across all 90
  deployed/high-impact rows.
- DOJ's latest public inventory snapshot self-reports those practices in
  progress for all 73 deployed/high-impact rows, and a later public
  compliance/waiver/termination disposition was not located.
- Named products and awards establish specific supplier/workload or
  infrastructure relationships only to the extent stated above.
- SSA, VA and DOJ all contain systems that route attention or produce
  recommendations; VA also publishes a bounded claims-automation case.

Do **not** claim:

- that an inventory label proves compliance, legality, accuracy, lack of bias,
  absence of PII, security, ATO validity or a completed privacy review;
- that a deployed product means every embedded AI feature is operational;
- that human review proves meaningful independence, low automation weight or a
  usable remedy;
- that a fraud alert, disability score, facial match, LPR hit, risk profile or
  evidentiary translation is a final agency finding;
- that a contract end proves workload cessation, or that an active cloud
  contract proves a named model runs on that cloud;
- that a reseller, prime, hyperscaler, model maker and application operator are
  the same entity;
- that VA's reported health-outcome associations are independent causal proof;
  or
- that the absence of a public DOJ post-deadline disposition proves controls
  were not completed internally.

## Official primary source shelf

### Governmentwide

- [OMB M-25-21 — Accelerating Federal Use of AI through Innovation,
  Governance, and Public Trust](https://www.whitehouse.gov/wp-content/uploads/2025/04/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf)
- [OMB official 2025 Federal Agency AI Use Case Inventory
  repository](https://github.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory)
- [USAspending](https://www.usaspending.gov/) and [USAspending
  API](https://api.usaspending.gov/)

### SSA

- [SSA AI hub, policies and inventory](https://www.ssa.gov/ai)
- [SSA Enterprise AI Strategy](https://www.ssa.gov/ai/policy/SSA%20Enterprise%20Artificial%20Intelligence%20Strategy%20Report.pdf)
- [SSA M-25-21 Compliance Plan](https://www.ssa.gov/ai/policy/SSA%20AI%20Compliance%20Plan.pdf)
- [SSA OIG ongoing audits](https://oig.ssa.gov/audit-reports/ongoing-audits/)

### VA

- [VA AI hub](https://department.va.gov/ai/)
- [VA current AI inventory page](https://department.va.gov/ai/ai-use-case-inventory/)
- [VA April 2026 compliance-update workbook](https://department.va.gov/ai/wp-content/uploads/sites/26/2026/04/VA-AI-Use-Case-Inventory-2025-Web-Compliance-Updates.xlsx)
- [VA 2025 AI Strategy](https://department.va.gov/ai/building-the-future-vas-strategy-for-adopting-high-impact-artificial-intelligence-to-improve-services-for-veterans/)
- [VA M-25-21 Compliance Plan](https://department.va.gov/ai/department-of-veterans-affairs-compliance-plan-for-omb-memorandum-m-25-21/)
- [VA guidance for generative AI](https://department.va.gov/ai/guidance-for-generative-ai-use-at-va/)

### DOJ

- [DOJ AI hub](https://www.justice.gov/ai)
- [DOJ AI Inventory](https://www.justice.gov/ai/ai-inventory)
- [DOJ FY2025 Chief Data Officer Annual Report](https://www.justice.gov/open/media/1442676/dl?inline=)
- [DOJ M-24-10 Compliance Plan, retained as superseded baseline](https://www.justice.gov/media/1373026/dl)
- [DOJ OPCL privacy compliance process](https://www.justice.gov/opcl/privacy-compliance-process)
- [EOUSA Palantir PIA](https://www.justice.gov/opcl/media/1427686/dl)
- [Joint Automated Booking System PIA](https://www.justice.gov/opcl/media/1397866/dl?inline=)
- [OIG Axon Body Worn Camera System PIA](https://www.justice.gov/opcl/page/file/1497856/dl?inline=)

## Lifecycle boundary

This is a retained Research Desk wave, not live-vault authority. It does not
create an Observatory event, watch, synthesis, generated view or app state.
Promotion and downstream interpretation remain separate review gates.
