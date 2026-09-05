> Source cutoff: 2026-08-23 ET

# Federal agency AI transition — cross-agency synthesis

## Answer first

The material federal AI story is no longer a single policy announcement. It is
an uneven transition from inventories and governance plans into **shared model
access, mission-specific deployments, data and evaluation planes, rights- and
safety-affecting workflows, and commercially supplied operating
infrastructure**.

Six conclusions control the Observatory read:

1. **There is one broad civilian policy baseline, but no one federal AI
   system.** OMB M-25-21 and M-25-22 create governance and acquisition duties;
   each entity still has its own legal authority, data, human-decision boundary,
   security environment, supplier chain and operating clock.
2. **The publicly strongest operating states are mission-specific.** DHS
   reports deployed AI across border, screening, immigration and cyber
   missions; VA reports a large deployed high-impact clinical and benefits
   estate; SSA exposes a small but consequential disability and identity
   portfolio; Treasury, the Board, SEC, FHFA and FTC use AI mainly for research,
   triage, anomaly detection, supervision, enforcement support and shared
   services; Defense publicly supports enterprise GenAI.mil deployment and an
   Agent Network launch. HHS has several real component services, but its
   department-wide Commons remains an architecture objective. DOJ has the
   sharpest unresolved public post-deadline governance state.
3. **The highest-risk compression is “human in the loop.”** Most systems route,
   score, summarize, retrieve, recommend or flag for a human. Public records
   rarely disclose decisional weight, override frequency, time pressure or the
   affected person's ability to see and contest the AI evidence. VA also
   discloses a bounded automated-certificate workflow, so a government-wide
   claim that a human always makes the final decision is false.
4. **Commercial concentration is real, but supplier identities must not be
   collapsed.** AWS, Microsoft/Azure/OpenAI, Google/GCP/Gemini, Oracle, IBM and
   Palantir recur across agencies, while specialist identity, biometric,
   surveillance, legal and health vendors sit closer to individual decisions.
   Recurrence does not prove a shared contract, shared data plane, common model,
   government-wide interoperability or equivalent control.
5. **Capital is moving on different clocks.** A strategy, appropriation,
   mandatory allocation, solicitation, award, obligation, platform launch,
   workload deployment and accepted effect are not interchangeable. The
   Defense enterprise-agreement figures are advertised agreement values, not
   obligations or AI spend; the civilian contract values often support broader cloud,
   application or contact-center rails and cannot be divided among AI rows.
6. **NARA supplies the missing evidence constitution.** AC 11.2026 makes
   prompts, outputs, tests, audit trails, code, training material and operating
   documentation records questions when they are captured, controlled,
   circulated or relied upon. It does not make every AI interaction a federal
   record or permanent. Auditability therefore depends on agency capture and
   supplier custody terms before logs and intermediate evidence disappear.

The nine civilian portfolios with comparable row counts in the wave files
contain **1,208 reported rows** in their selected latest snapshots, before HHS
and excluding Defense's non-comparable project framework. That arithmetic is a
disclosure count, not a capability score: DOJ contains duplicate identifiers,
VA has already revised stages between snapshots, agency decomposition differs,
and classified or sensitive uses may be omitted.

## Authority and entity firewall

### OMB coverage does not erase agency boundaries

[OMB M-25-21](https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf)
governs covered agency use of AI at the AI functionality level and requires
agency governance, inventories and minimum practices for high-impact uses.
[OMB M-25-22](https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-22-Driving-Efficient-Acquisition-of-Artificial-Intelligence-in-Government.pdf)
adds acquisition requirements on its own solicitation, option and contract
clocks. Publication of a plan or inventory proves a control object exists; it
does not prove compliance, funding, deployment, acceptance or legal use.

The following seams must remain explicit:

| Seam | Controlling boundary |
|---|---|
| Defense inventory exception | M-25-21 expressly exempts the Department of Defense from the annual public **individual use-case inventory** requirement. That is why the seven-PSP Defense framework is not numerically comparable to the civilian inventories. It is not a blanket exemption from every provision of the memorandum. |
| National Security Systems | M-25-21 does not cover AI used as a component of a National Security System, and M-25-22 does not apply to AI acquired for that use. This is a **system/use exclusion, not a Department-name test**. A particular Defense workload cannot be placed inside or outside the exclusion merely from its owner. NSS AI follows the separate national-security and Defense policy stack. |
| Department name | Public sources use the secondary executive label “Department of War”; the statutory Department of Defense remains a distinct legal fact. This package preserves both and does not infer statutory reorganization. |
| Board versus Reserve Banks | The Board of Governors inventory covers Board work and may reach Board-delegated functions. It does not prove ownership or operation by any of the twelve Reserve Banks, Federal Reserve Financial Services, FRIT, FedNow, Fedwire, National Settlement Service or a Reserve Bank accounting book. |
| Regulator versus regulated entity | SEC, FHFA and FTC internal AI use is not a rule, order, enforcement finding, private-market authorization or regulated-entity deployment. FHFA use is not Fannie Mae, Freddie Mac or Federal Home Loan Bank use. |
| Treasury versus payment rail | A Treasury or IRS model can flag, compare, search or recommend without deciding program eligibility, releasing a payment, settling funds, posting the authoritative account or recovering a debt. |
| Partner access versus agency operation | DOJ, DHS and Defense may access state, local, partner or contractor systems. Access does not prove that the federal component owns the model, data, retention rule, administrator credential or operating system. |
| NARA's role | NARA is a cross-government records authority and a separate AI user. It is not a twelfth entity in this eleven-entity comparison and does not govern AI safety, ethics, privacy, security or mission authorization through AC 11.2026. |

### GAO incompleteness is an audit control

The [GAO-24-105980 recommendation record](https://www.gao.gov/products/gao-24-105980)
prevents the inventories from being treated as complete ground truth. GAO found
that selected agencies' inventories omitted required information or contained
inaccurate fields; HHS recommendation 15 remained open as of March 2026. DHS's
remaining open recommendation in this wave concerns the required authority
review rather than an unresolved raw row count, but it reinforces the need to
verify the governance artifact rather than infer it from the inventory.

Accordingly:

- absence from an inventory is not proof that a system, supplier or use is
  absent;
- a future-looking date is not deployment proof;
- a high-impact, ATO, PII or control field is an agency declaration, not an
  independent legal, safety, privacy or performance finding; and
- a changed or duplicated row must be reconciled before it is used as a clock.

## Eleven-entity comparative control map

| Entity | Public control and portfolio state | Material decision or mission edge | Infrastructure and supplier edge | Principal unresolved object |
|---|---|---|---|---|
| **HHS** | [Strategy](https://www.hhs.gov/sites/default/files/hhs-artificial-intelligence-strategy.pdf) and [M-25-21 plan](https://tech.hhs.gov/documents/public/2025-hhs-ai-compliance-plan.pdf) published; current inventory files posted but not item-level parsed in Wave 1; GAO inventory recommendation open | Benefits and identity candidates; FDA scientific review; CDC public-health work; department-scale employee access | Proposed OneHHS Commons; current HHS ChatGPT; CDC EDAV/Azure OpenAI; FDA Elsa/HALO on GCP; ACF Credal.ai award | Primary inventory reconciliation, high-impact rows, Commons funding/award/acceptance, supplier and log-custody map, HHS OIG governance audit |
| **DHS** | [Strategy](https://www.dhs.gov/sites/default/files/2025-09/25_0926_cio_dhs_ai_strategy_for_omb_m-25-21_508.pdf), [plan](https://www.dhs.gov/sites/default/files/2025-09/25_0926_cio_dhs_compliance_plan_for_omb_m-25-21_508.pdf) and June 2026 inventory; 235 rows, 109 deployed, 54 high-impact | Border surveillance, passenger screening, biometrics, investigative facial recognition, immigration, cyber and emergency functions | Anduril, NEC, IDEMIA, Clearview, Motorola, Deloitte, IBM and integrators by workload; strategy-level LLM gateway, continuous authorization and shared data/evaluation plane | TSA Answer Engine deployed/high-impact with ATO `No` and an expired historical award; high-impact evidence; biometric and USCIS contract continuity; gateway operating proof |
| **Treasury** | [Strategy](https://home.treasury.gov/system/files/136/Treasury-AI-Strategy.pdf), [plan](https://home.treasury.gov/system/files/136/Treasury-Compliance-Plan.pdf) and January 2026 inventory; 129 rows, 26 deployed, 4 high-impact | Tax fraud indicators, Do Not Pay research, federal-spending and contract analysis, market anomalies, regulatory and procurement support | TCloud, FISMA Moderate chat, FISMA High sandbox and planned Innovation Center; SAIC, Sky Tech, Deloitte, SOKAT, ThunderYard and AnChain on adjacent awards, but inventory names no vendors | Award-to-use-case crosswalk, model/cloud identities, internally inconsistent high-impact fields, waiver/suspension returns and production acceptance |
| **Board of Governors** | [M-25-21 plan](https://www.federalreserve.gov/publications/compliance-plan-for-OMB-memorandum-m-25-21.htm) and [38-row inventory](https://www.federalreserve.gov/AI-use-case-inventory-2025.htm); 16 deployed; all classified not high-impact | Bank-risk analysis, examination quality support, supervisory-data anomalies, public comments, economic and financial-stability research | Approved internal compute, secure commercial platforms and approved open-source models/libraries; supplier and award visibility low | Model weight and validation in ratings/exams, approved provider list, waiver/determination summaries and exact Board-delegated Reserve Bank execution |
| **SEC** | [Plan](https://www.sec.gov/files/2025-sec-ai-compliance-plan.pdf) and [60-row inventory](https://www.sec.gov/files/2025-sec-individual-ai-use-cases.csv); 20 deployed; all classified not high-impact | Examination and enforcement leads, TCR analysis, filing and comment review, legal research, crypto-wallet tracing | NEAT, SEARCH, Enterprise Data Platform and ACES/AWS; Aretec, Elder, IBM, Thomson Reuters, RELX, Flashpoint, Chainalysis and others | Final risk framework and operative waiver/termination controls; validation/human reliance; Chainalysis and expired infrastructure successor paths |
| **FHFA** | [Plan](https://www.fhfa.gov/document/FHFA-2025-AI-Compliance-Plan.pdf) and [16-row inventory](https://www.fhfa.gov/document/fhfa-ai-use-case-inventory-2025.csv); 12 deployed; all classified not high-impact | FMAP neural networks analyze loan-level mortgage data; TechSprint concepts remain exploratory | In-house FMAP; Microsoft SQL predictive functions and operational commercial tools | FMAP model/validation record, completed AI Risk Profile, matched award evidence and any actual regulated-entity adoption or supervisory use |
| **FTC** | [AI Use Policy](https://www.ftc.gov/system/files/ftc_gov/pdf/FTC-AI-Use-Policy.pdf) and [16-row inventory](https://www.ftc.gov/system/files/ftc_gov/data/2025%20Agency%20AI%20Use%20Case%20FTC%20public%20release%20csv.csv); 11 deployed; all classified not high-impact | Complaint classification and graphing, call/mail intake, e-discovery and audiovisual analysis | Leidos Sentinel; Microsoft Azure/Databricks/ML; Amazon contact tools; Complete Discovery Source/Relativity and Veritone | Sentinel successor, Microsoft/Amazon prime paths, redaction and classifier performance, analyst weight and termination/remediation evidence |
| **SSA** | [Strategy](https://www.ssa.gov/ai/policy/SSA%20Enterprise%20Artificial%20Intelligence%20Strategy%20Report.pdf), [plan](https://www.ssa.gov/ai/policy/SSA%20AI%20Compliance%20Plan.pdf) and 33-row inventory; 27 deployed; 9 high-impact | Disability allowance/denial review selection, continuing-disability and SSI review, hearings triage, medical/vocational support and digital identity | Hybrid on-prem/cloud/SaaS; ID.me, IBM, Microsoft/OpenAI, AWS and Hyperscience/Accenture relationships | ID.me testing/assessment/review/monitoring/remedy gap, SSA OIG AI/AWS audits, IBM QDD successor and September 30 maturity return |
| **VA** | [Strategy](https://department.va.gov/ai/building-the-future-vas-strategy-for-adopting-high-impact-artificial-intelligence-to-improve-services-for-veterans/), [plan](https://department.va.gov/ai/department-of-veterans-affairs-compliance-plan-for-omb-memorandum-m-25-21/) and April 2026 workbook; 367 rows, 134 deployed, 215 high-impact, 90 deployed/high-impact | Benefits and pension processing, fraud referrals, suicide/overdose risk, imaging, ambient notes, access and physical security; one bounded automated certificate workflow | Summit Data Platform, VA GPT, AWS capacity, Microsoft, Oracle Health, IBM, Abridge, Knowtex and Hyperscience product relationships; IBM Option 4 now runs contractually through Aug. 31, 2027 | Underlying control artifacts for the 90 self-reported compliant deployed/high-impact uses; IBM payment/performance evidence and 2027 successor state; ambient-scribe dispositions; proof of planned FY2026 launches |
| **DOJ** | No located public M-25-21 plan or current strategy; [inventory page](https://www.justice.gov/ai/ai-inventory) says 315 entries while OMB file has 314 rows/312 unique IDs; 114 high-impact, 73 deployed/high-impact | Facial recognition, LPR, gunshot detection, financial/crypto analysis, evidence processing, prosecution support, detention risk and proposed immigration intake/adjudicator assistance | Fragmented Axon, Palantir, Clearview, PenLink, Veritone, Thomson Reuters, SoundThinking, Flock, AWS, Azure, NVIDIA and OpenAI component stack | Public post-April 3 control/waiver/termination disposition; plan and Interim Policy; inventory/PIA/ATO crosswalk; expired Palantir and cloud/evidence successor rails |
| **Department of War / statutory Defense** | [January 2026 strategy](https://media.defense.gov/2026/Jan/12/2003855671/-1/-1/0/ARTIFICIAL-INTELLIGENCE-STRATEGY-FOR-THE-DEPARTMENT-OF-WAR.PDF); two of seven Pace-Setting Projects have public launch/operating evidence | GenAI.mil enterprise access; Agent Network scans intelligence/operational systems and presents options to commanders; Department says it does not autonomously select or strike targets | JWCC AWS/Google/Microsoft/Oracle; GenAI.mil Gemini with xAI/OpenAI agreement edges; eight-company IL6/IL7 agreements; Palantir C2-innovation and Lumbra orchestration edges described in the Agent Network release; planned government-owned supercompute plus commercial surge | Five PSP implementation returns, provider-specific GenAI.mil production, IL6/IL7 tasking and acceptance, FY2026 obligations, FY2027 site/power/chip/integrator objects and tested exit |

## Material clusters and the human-authority spectrum

### 1. Benefits, identity and the government front door

SSA disability and identity tools, VA claims and pension systems, HHS/CMS/ACF
identity candidates, IRS fraud indicators, DHS immigration and traveler
identity systems, and DOJ/EOIR proposals all sit near access to government
services or legal status. Their outputs have different legal weights:

`identity result or score -> queue / review / referral -> human or automated action -> notice -> appeal or remedy`

The inventories often expose the first one or two steps while leaving the
later decisional weight, notice and contest path incomplete. An ID.me alert, IRS
fraud indicator, disability score or biometric match is not by itself a denial,
debt, fraud finding or identity adjudication.

### 2. Health, clinical care and public safety

HHS and VA show the most consequential health layer. FDA Elsa/HALO and CDC
ChatCDC operate over regulatory-science and public-health data; VA publishes
deployed risk models, imaging aids and clinical triage plus ambient-scribe
pilots. Agency-reported outcome associations, expert review statements and
completed-control fields are not independent clinical validation. The return
objects are the underlying impact assessments, test protocols, performance by
population, monitoring thresholds, override behavior and accepted workflow
boundaries.

### 3. Surveillance, investigation, evidence and force

DHS and DOJ use AI to detect, match, rank, translate, summarize and connect
people, objects, images, locations, communications and case material. Defense's
Agent Network moves the same structural pattern into battle management. Three
boundaries must stay visible:

- a detection, candidate, translation, link or recommendation is not a factual
  or legal finding;
- an agency statement that human confirmation is required does not quantify
  the weight or quality of that confirmation; and
- access to a partner or vendor platform does not transfer its data custody,
  retention or model administration to the federal user.

The Defense release expressly preserves commander authority and denies
autonomous target selection or strike by Agent Network. That is the strongest
public boundary, not proof of the complete targeting chain or operational
validation.

### 4. Money, markets, housing and public rules

Treasury, the Board, SEC, FHFA and FTC use AI mainly upstream of a formal legal
or financial act. Models search, extract, compare, classify, prioritize,
forecast or generate leads. The authoritative state still lives in the tax or
program determination, contract, payment instruction, Reserve Bank book,
settlement record, examination finding, Commission action, FHFA order or FTC
remedy. The agency's internal use cannot silently advance any of those objects.

### 5. Automation is a spectrum, not a binary label

| Publicly supported role | Examples | Safe interpretation |
|---|---|---|
| Retrieval / drafting | HHS ChatGPT, PAT, VA GPT, SEC/FTC/DOJ assistants | Output supports work; official reliance and records capture remain separate |
| Ranking / triage / flagging | SSA PATH/QDD, VA clinical risk and fraud referral, Treasury/SEC/FTC analytics, DHS screening | Attention is shifted; false positives, false negatives and human weight matter even without final automation |
| Recommendation / structured decision support | SSA VAAT, VA ratings proposals, Board risk models, Defense Agent Network | Human authority is stated or implied, but override rate, defaults and time pressure are largely undisclosed |
| Bounded automated action | VA National Cemetery certificate processing reports about 30% completed within 24 hours without human intervention | A real narrow automation edge; scope, exception handling, audit and remedy must be preserved |
| Proposed automated gate | EOIR filing-intake threshold proposal | Pre-deployment only; no operating adjudication proved |
| Lethal or non-kinetic effect | Defense AI strategy and Agent Network adjacency | No reviewed public record establishes department-wide autonomous engagement authority |

## Shared infrastructure and vendor concentration

### The recurring architecture

Across the eleven entities, four infrastructure patterns recur:

1. **Planned common planes:** OneHHS Commons, DHS AI Gateway and data/evaluation
   plane, Treasury TCloud/sandbox/Innovation Center, SSA shared services, and
   Defense's government-owned strategic compute core. A named architecture is
   not a funded, awarded or accepted platform.
2. **Operating enterprise access:** HHS ChatGPT, DHSChat, Treasury and OFR
   services, VA GPT, GenAI.mil and commercial productivity/legal assistants.
   Availability is not adoption, accuracy, savings or mission effect.
3. **Mission data and application layers:** FDA HALO, FTC Sentinel, SEC's
   NEAT/SEARCH/ACES, FHFA FMAP, VA Summit and component-specific DOJ/Defense
   stacks. Platform identity is not a model, cloud, prime or authoritative
   record identity.
4. **Hybrid and classified capacity:** agency data centers, on-premises models,
   ordinary FedRAMP cloud, AWS/Azure/GCP services, JWCC and IL6/IL7 agreements.
   Multiple providers do not prove portability, equivalent authorization or a
   tested exit.

### Recurrence without identity collapse

| Provider family | Confirmed or declared agency edges | Identity firewall |
|---|---|---|
| **AWS** | DHS commercial catalogue; SEC ACES environment; SSA AWS Connect; VA enterprise capacity; multiple DOJ component clouds; Defense JWCC/classified agreements; NARA's separate ERA/cloud rail | Four Points, Oddball, Effectual, CTAC and other primes/resellers can sit between the agency and AWS. A broad cloud award is not workload spend or proof a named model runs there. |
| **Microsoft / Azure / OpenAI** | CDC Azure OpenAI; SSA PAT/VAAT; FTC Azure/Databricks/ML; FHFA SQL; VA Microsoft services; DOJ Azure and OpenAI-named uses; Defense Microsoft/OpenAI agreements; NARA Azure; HHS-wide ChatGPT | Microsoft, Azure and OpenAI are distinct legal/product roles. Model maker, cloud, enterprise-software provider, reseller and application integrator must remain separate. |
| **Google / GCP / Gemini** | FDA Elsa/HALO on GCP; Defense GenAI.mil launch with Gemini and classified Google agreement; NARA Workspace/Gemini and GCP/Vertex routes | Workspace reseller, GCP cloud, Gemini model and workload prime are not one award. No cross-agency data or model plane follows. |
| **Oracle** | Defense JWCC/classified access and broad Oracle enterprise agreement; VA Oracle Health record substrate | Defense enterprise software and VA clinical-record infrastructure are different awards, data domains and workloads; neither proves an Oracle-hosted AI case. |
| **IBM** | SSA QDD scoring; DHS/USCIS application edge; SEC risk analytics; VA pension optimization; Treasury/other adjacent analytics | Each component has its own prime, award, model, data and successor clock. Vendor recurrence is not a shared federal model. |
| **Palantir** | Defense Maven/Agent Network adjacency; DOJ/EOUSA case integration; partner-system access in other enforcement settings | Platform presence does not establish the same instance, data corpus, algorithm, administrator, legal authority or operating feature. |
| **Specialist identity, biometric, surveillance and evidence firms** | ID.me, NEC, IDEMIA, Clearview, Flock, SoundThinking, Motorola, Axon, PenLink, Veritone, Relativity and others | These suppliers sit closest to rights- and evidence-affecting workflows, but a device, data source, algorithm, application and prime can still be different entities. |

The concentration finding is therefore narrow but important: a small number of
cloud and model families recur beneath many agencies, while specialist vendors
control high-value application seams. The public record rarely proves tested
exit, cross-provider failover, complete subcontractor chains, log export,
model-version continuity or government operation through contract interruption.

## Capital and contract clocks

### Keep the money objects separate

| Object | Public amount and state | Correct reading |
|---|---|---|
| Defense FY2026 AI ecosystem | $250 million mandatory allocation: $123 million GenAI.mil and $127 million agentic warfighting/business pilots | Funding allocation, not provider awards, obligations, deployments or accepted effects |
| Defense Microsoft agreement | Approximately $9.7 billion advertised five-year BPA value; Dell Federal Systems is the reseller/awardee | Enterprise ceiling/value across broader software and cloud, not immediate Microsoft payment or AI spend |
| Defense Oracle agreement | Nearly $7 billion advertised over a five-year base plus five-year option | Broad on-premises enterprise software agreement, not immediate obligation or named AI hosting |
| VA enterprise AWS capacity | $521,824,443.39 obligation through February 2, 2027 | Broad enterprise cloud rail, not AI-only spend or proof every VA model runs on AWS |
| SEC historical GDIT infrastructure | $461,106,418.99; period ended July 3, 2026 | Broad infrastructure award and successor watch, not AI-only spend or proof that a still-named workload stopped |
| Treasury SAIC TCloud task | $154,915,476.62 through June 19, 2027 | Cloud implementation/O&M rail adjacent to AI, not an allocation to the 129 inventory rows |
| SSA AWS Connect | $150,447,391 through July 31, 2027 | Contact-center cloud rail, not a universal SSA AI platform or AI-only amount |
| FTC Leidos Sentinel | $93,595,376.01 through November 30, 2026 | Direct platform rail aligned with seven rows, but broader than their AI functions |

### Near-term state-return clocks

An end date is a return trigger, not proof that a workload stopped. Options,
modifications, bridge awards, new vehicles, migration or insourcing may change
the state.

| Date / trigger | Entity and object | Return required before changing the state |
|---|---|---|
| **Resolved Aug. 24, 2026** | VA IBM Pension Optimization | P00018 exercised Option 4, added $14,941,471.41 and extended the current period through Aug. 31, 2027; payment and performance remain separate |
| **Sep. 4, 2026** | Treasury/BFS Deloitte analytics and AI | Option, extension, closeout, successor and exact inventory-row crosswalk |
| **Sep. 26, 2026** | DHS/USCIS Pluribus biometrics | Option/successor, current scope, underlying biometric role and operating continuity |
| **Sep. 28, 2026** | VA Abridge | Renewal, scale acceptance, pause, successor or termination |
| **Sep. 29–30, 2026** | Treasury SOKAT and AnChain; DOJ DEA AWS and Veritone; SSA Level 3 maturity target | Contract dispositions, workload state/model disclosure, and measured maturity evidence kept as separate returns |
| **Oct. 15 and Oct. 31, 2026** | SEC Oddball AWS/data support and Aretec application support | Successor/option and named-workload continuity |
| **Nov. 19 and Nov. 30, 2026** | DHS/USCIS Analytica; FTC Leidos Sentinel; DOJ PenLink structured clock | Successor/option, workload allocation and any conflicting period resolution |
| **Dec. 31, 2026** | SSA ID.me; DOJ Axon ELA | Renewal, replacement, termination and high-impact control/continuity returns |
| **No public instrument date** | Defense IL6/IL7 agreements and FY2027 supercompute | Task order, obligation, site, power, chip, integrator, deployment and acceptance objects |

NARA's own evidence infrastructure has a parallel continuity cluster: the
Fearless ERA 2.0 task ends September 28, and the PICARD cloud-broker BPA and
current AWS call end September 29. Those are not part of the eleven-entity
capital table, but they matter to the federal AI records join because archive,
ingest, storage and export capacity determine whether preserved evidence stays
available.

## NARA records join — from AI output to reconstructable government action

The existing `NARA AI Records Layer and Buildout`
package supplies the documentary chain beneath all eleven entities:

```text
agency authority and AI use
  -> prompt / input / source data / model output
  -> test, impact assessment, independent review and risk acceptance
  -> human review, override, waiver, termination or automated action
  -> notice, appeal, official case / payment / rule / command record
  -> agency capture-and-control determination under the FRA
  -> approved retention schedule
  -> later OIG / GAO / litigation / FOIA / historical review
```

The highest-value record categories in this package are:

- the underlying tests and impact assessments behind agency inventory `Yes`
  fields;
- model/data versions, prompts, retrieved sources, outputs, confidence or
  ranking signals, overrides and correction histories for rights- or
  mission-affecting uses;
- waiver, risk-acceptance, termination and appeal/remedy records;
- source audio, imagery, documents and translations where AI assists evidence
  processing;
- contract/task-order, provider, ATO, performance, incident, retention, audit,
  export, data-right and exit documentation; and
- monitoring records that can show drift, error, discriminatory effect,
  operational effect or non-use.

AC 11.2026 does not say that every item above is permanent or publicly
releasable. Record status depends on agency capture, use, circulation, reliance,
control and legal or business need; approved schedules still govern disposal.
The material vulnerability is that a vendor may retain logs while the agency
never captures or controls them, or an intermediate output may be destroyed as
transitory/intermediary even though it later becomes necessary to reconstruct a
decision. Supplier contracts are therefore part of the evidence-control plane,
not merely procurement metadata.

## Genuine new edges versus existing Observatory homes

| Existing research home | What already existed | What this package adds | Routing ruling |
|---|---|---|---|
| `NARA AI Records Layer and Buildout` | FRA capture, retention and supplier-custody constitution; NARA's own AI and hybrid-cloud build | Eleven-entity workload, control, supplier and contract objects that need those record rules | Join through evidence and custody; do not duplicate NARA as another agency wave |
| [`Military Modernization`](../sources/military-modernization-research-package-2f25d472ab0c.html) | Sensor-to-effect chain, JWCC, Open DAGIR, Maven, NGC2, data rights, tactical edge and acceptance doctrine | GenAI.mil and Agent Network operating returns; IL6/IL7 agreements; FY2026/FY2027 capital; Microsoft/Oracle delta | Existing package remains controlling for the military architecture; Wave 4 is a delta only |
| [`Federal Science Operating System`](../sources/readme-afb8768af3df.html) and [NSSTS company map](../sources/readme-814cc85d1bbe.html) | Genesis/NSSTS compute, labs, research-security, company, site, energy, acquisition and acceptance rails | Civil-agency service and control planes plus Defense enterprise/mission AI | Defense participation in Genesis stays in Federal Science; agency AI access does not become a Genesis award or scientific acceptance object |
| `Fed, Clearing and Treasury` | Board, Reserve Banks, FRFS/FRIT, settlement systems, books and Treasury interfaces separated | Board internal supervisory/analytical AI and Treasury analytical tools | No payment, settlement, accounting or legal rail changes without its own authoritative object |
| `Fraud and Payment Integrity` | Identity, eligibility, payment justification, payment gate, settlement, accounting, recovery and public-ledger hypothesis | AI flags, matches, searches and referrals at Treasury, IRS, SSA, VA, HHS and DOJ | Join upstream as evidence/attention; do not turn a model output into ineligibility, stopped payment, debt, fraud or guilt |
| Health, human-systems and justice/homeland freshness waves | Publisher and short-window policy/change detection | Stable implementation baselines, exact inventory fields, suppliers and successor cliffs | Complement rather than repeat the website sweeps |

The genuinely new Observatory edge is the cross-agency **implementation and
dependency layer**: which federal decisions AI can influence, which shared or
commercial infrastructure makes that possible, what human and records controls
remain visible, and which exact return could move the public state.

## Priority return watchboard

| Priority | Return object | Why it outranks another broad sweep |
|---|---|---|
| **P0** | DOJ M-25-21 strategy/plan and post-April 3 control, waiver or termination disposition for 73 deployed/high-impact rows | Resolves the largest public civilian control gap in the campaign |
| **P0** | DHS TSA Answer Engine ATO, successor award, deployment acceptance and high-impact evidence | Reconciles a deployed/high-impact/ATO-`No` row with an award that ended before the reported deployment date |
| **P0** | HHS primary inventory parse, corrected GAO return and exact high-impact identity/benefits rows | Establishes what the current HHS estate actually contains before the Commons story is advanced |
| **Resolved receipt** | VA IBM Pension Optimization Option 4 through August 31, 2027 | The 2026 continuity cliff is closed; payment, performance, claimant outcomes and the next successor decision remain separate |
| **P0** | NARA September ERA 2.0/PICARD/AWS continuity and agency AI-record implementation objects | Preserves the cross-government evidence and archive rail; a contract cliff alone does not prove loss of service |
| **P1** | SSA ID.me completed controls and December renewal; SSA OIG AI/AWS audits | Tests the digital front door, remedy boundary and independent oversight layer |
| **P1** | Defense five remaining PSP demonstrations; GenAI.mil provider state; IL6/IL7 task orders; FY2027 supercompute site/power/chip/integrator | Moves strategy and agreement language into workload, obligation, deployment and acceptance proof |
| **P1** | Treasury supplier/use-case crosswalk and September dispositions; corrected high-impact fields | Resolves the largest named-inventory / unnamed-supplier mismatch |
| **P1** | SEC risk framework, Chainalysis/current cloud paths and October successors; FTC Sentinel November successor | Tests enforcement-support continuity without treating internal AI as an enforcement outcome |
| **P1** | HHS Commons, DHS Gateway, SSA shared service and FHFA Risk Profile first funded/accepted objects | Distinguishes planned common planes from operating infrastructure |
| **P2** | Next full agency inventories plus underlying public impact, validation, waiver, termination and appeal summaries | Reconciles stages and controls without restarting an undirected government-wide search |

## Safe claims and proof limits

Safe at the cutoff:

- the eleven entities disclose materially different AI governance,
  infrastructure and mission states under a broad common federal policy
  environment;
- reported AI influences benefits, health, identity, border and immigration,
  law enforcement, financial supervision, public comments, consumer complaints,
  housing analytics and military decision support;
- a small group of cloud/model families and a larger specialist application
  layer recur across agencies;
- named awards and obligations prove the published recipient, scope, amount and
  clock only to the degree stated in the waves; and
- NARA has supplied a records-management test for federal AI materials, making
  capture, custody and retention part of the control system.

Do not claim:

- that every inventory is exhaustive, internally consistent or current;
- that `deployed` means accepted, effective, lawful, widely used or present in
  every eligible workflow;
- that `not high-impact`, `ATO: Yes`, `PII: No`, a risk assessment or a human-
  review statement proves safety, accuracy, privacy, security or meaningful
  human independence;
- that a high-impact field is an independent finding rather than an agency
  classification;
- that a platform, prime, reseller, hyperscaler, model maker, integrator and
  application operator are one supplier;
- that a contract ceiling, broad cloud obligation or enterprise-agreement value
  is AI spend or belongs to one use case;
- that an expired award proves workload cessation, or an active award proves
  deployment or acceptance;
- that multi-cloud or an anti-lock-in objective proves portability, tested
  failover, government administration or an operable exit;
- that internal Board, Treasury, SEC, FHFA or FTC AI changes a payment,
  settlement, accounting, rule, order, market, product or regulated-entity
  state;
- that Defense is categorically exempt from M-25-21/M-25-22 merely because it
  is exempt from the individual-use-case inventory requirement, or that every
  Defense use is an excluded NSS use; or
- that NARA made every prompt, output or vendor log a permanent or public
  federal record.

## Primary official source spine

Government-wide and records:

- [OMB M-25-21](https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf)
- [OMB M-25-22](https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-22-Driving-Efficient-Acquisition-of-Artificial-Intelligence-in-Government.pdf)
- [OMB 2025 Federal Agency AI Use Case Inventory repository](https://github.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory)
- [GAO-24-105980 recommendation status](https://www.gao.gov/products/gao-24-105980)
- [NARA AC 11.2026](https://www.archives.gov/records-mgmt/memos/ac-11-2026)

Entity-specific official evidence is linked in the comparison table. Defense's
implementation layer is additionally anchored by the [Agent Network launch](https://www.war.gov/News/Releases/Release/Article/4526862/dow-unleashes-agent-network-to-transform-ai-enabled-battle-management-and-targe/),
[classified-network agreements](https://www.war.gov/serve-from-netstorage/News/Releases/Release/Article/4475177/classified-networks-ai-agreements/index.html),
[FY2026 allocation plan](https://comptroller.war.gov/Portals/45/Documents/news/FY2026_Mandatory_Funding_Allocation_Plan.pdf),
and [FY2027 budget overview](https://comptroller.war.gov/Portals/45/Documents/defbudget/FY2027/FY2027_Budget_Request_Overview_Book.pdf).

## Lifecycle boundary

This is a source-audited Research Desk synthesis at the August 23, 2026 cutoff.
It does not create or promote a live-vault event, implementation watch,
generated view or app state. The next research action is limited to the named
return objects above; it is not authorization to reopen an unbounded
government-wide AI sweep.
