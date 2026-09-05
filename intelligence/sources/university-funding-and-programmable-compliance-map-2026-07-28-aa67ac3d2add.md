> Source cutoff: 2026-07-28

# University Funding and Programmable Compliance — Factual and Control Map

## Controlling thesis

The university funding system is a multiplex, not a pipeline. A university can
receive student aid, research grants, State appropriations, clinical
reimbursement, donor money and tax-advantaged debt through different legal
entities and identifiers. Public reporting reconstructs those flows later,
through partially overlapping annual surfaces.

The evidenced transition is from:

```text
institution
  → annual report
  → periodic audit
  → finding
  → corrective action
```

to:

```text
identified recipient
  → identified award
  → eligibility screen
  → purpose justification
  → payment decision
  → linked downstream event
  → visible correction or recovery
```

That is programmable compliance. Blockchain is one possible record
architecture, not the established policy state.

## 1. The university is not one object

A complete institutional map may need to reconcile:

| Identifier | Object |
|---|---|
| OPEID | Title IV participating school or branch |
| IPEDS UNITID | Education-statistics institution |
| IRS EIN | Tax filer or exempt legal entity |
| SAM / FAC UEI | Federal award recipient or Single Audit auditee |
| Medicare CCN | Participating clinical provider |
| CUSIP | Municipal security |

The core university, system office, research foundation, hospital, faculty
practice, endowment foundation, athletics entity, housing entity and bond
obligated person can sit behind different identifiers and consolidation
boundaries. No located federal public source supplies a reliable universal
crosswalk.

## 2. Funding-flow map

| Inflow | Operating path | Public visibility | Principal funding gate |
|---|---|---|---|
| Title IV loans, Pell and campus-based aid | Education/Treasury → G6/COD → institution → student account → eligible charges or credit balance | Near-term institutional reporting; quarterly public aggregates with revisions | Program Participation Agreement, reconciliation, program review, cash monitoring, limitation, suspension or termination |
| Tuition and fees | Family, Title IV, State aid, lender, employer or 529 plan → student ledger | IPEDS annual net tuition; no public student-level transaction record | Title IV cash rules where federal aid is involved; accreditation, State law and contract |
| Federal research | HHS/NIH, Defense, NSF, Energy, NASA, USDA and others → prime award → sponsored-programs office / PI → subaward or vendor | USAspending obligations and selected agency project data; controlled cash-draw and financial-reporting systems | Uniform Guidance remedies, agency award terms, suspension/debarment, future-award eligibility |
| State and local support | Legislature or locality → system/coordinating board → institution or project | Budgets, ACFRs, audits and delayed IPEDS aggregates | Appropriation riders, allotment, State audit, board controls and clawbacks |
| Endowment and donors | Donor, foundation or DAF → university or supporting foundation → restricted or unrestricted pool → payout | Aggregate Form 990/Schedule D; contributor identities generally withheld; separate related entities | Tax law, charitable-trust law, donor restriction and gift agreement |
| Tax-exempt debt | Conduit issuer → investors → trustee → project | Official statement and agreement-specific continuing disclosure on EMMA | Bond covenants, trustee remedies, SEC antifraud and IRS qualified-use rules |
| Clinical revenue and GME | Medicare, Medicaid, commercial insurer and patient → hospital/health-system entity | Cost reports, claims aggregates and privacy-limited datasets on separate clocks | CMS participation, cost settlement, recoupment, HHS-OIG and False Claims Act |

FY2024 higher-education R&D totaled $117.7 billion. Federal sources supplied
$64.6 billion, or 55 percent. HHS supplied $35.5 billion; Defense $10.2 billion;
NSF $7.2 billion; Energy $2.9 billion; NASA $2.4 billion; and USDA $2.0 billion.
Life sciences constituted 57 percent of academic R&D. The health-research
university is therefore the highest-density junction between Education, HHS,
national security and federal financial control.

Primary source: [NSF NCSES, Higher Education Research and Development FY2024](https://ncses.nsf.gov/pubs/nsf26305)

## 3. The public reporting clocks

| Surface | Governing clock | Visibility boundary |
|---|---|---|
| Form 990 | Fifteenth day of fifth month; automatic six-month extension | A June 30 filer can wait until May 15, 10.5 months after year-end, before IRS processing; public institutions can be exempt |
| Single Audit / FAC | Earlier of 30 days after audit report or nine months after year-end | Selective compliance audit; absence can mean below threshold, not due, late, suppressed or missing |
| Education eZ-Audit below Single Audit threshold | Financial statements within six months | May be compiled or reviewed rather than audited; no located public search surface |
| IPEDS Finance | Spring collection for the latest fiscal year ending before October 1; provisional release roughly nine months after close | Common June 30 institution can first appear provisionally about 18 months after year-end |
| USAspending | Agency award submissions on File C/D2 clocks | Obligation or award action is not cash, recipient expenditure or outcome |
| EMMA | Annual date promised in each continuing-disclosure agreement | No universal university deadline; coverage depends on the security and obligated person |
| Medicare cost report | Last day of fifth month after provider year-end | Hospital legal entity and later settlement do not necessarily equal the university |

Primary sources:

- [IRS annual exempt-organization return due date](https://www.irs.gov/charities-non-profits/annual-exempt-organization-return-due-date)
- [IRS Form 990 instructions](https://www.irs.gov/instructions/i990)
- [Federal Audit Clearinghouse threshold and submission guidance](https://www.fac.gov/audit-resources/submission-guide/about/)
- [Education Single Audit submission guidance](https://fsapartners.ed.gov/knowledge-center/library/electronic-announcements/2024-05-15/audit-submission-requirements-institutions-under-single-audit-act-updated-april-8-2026)
- [IPEDS survey methodology](https://nces.ed.gov/ipeds/ReportYourData/IpedsSurveyMethodology)
- [IPEDS release schedule](https://nces.ed.gov/ipeds/survey-components/data-release-schedule)
- [USAspending data sources and gaps](https://www.usaspending.gov/submission-statistics/data-sources)
- [CMS cost-report data](https://www.cms.gov/data-research/statistics-trends-and-reports/cost-reports)

## 4. Why Form 990 cannot answer the transaction question

Form 990 produces organizational visibility, not award-level traceability:

- incoming government grants are compressed into annual revenue categories;
- expenses are annual natural and functional totals;
- Schedule I reports outgoing domestic grants and assistance, not every
  incoming federal award;
- Schedule F reports foreign activity by bounded categories and regions;
- Schedule R maps selected related organizations, not a consolidated
  transaction chronology;
- audited financial statements are not independently required to be attached
  or published under federal tax law;
- most contributor names and addresses are withheld from public disclosure;
- qualifying State institutions and governmental affiliates may have no
  institution-level Form 990.

A foundation's Form 990 is not the public university's consolidated books. An
accepted filing is not an IRS audit of the underlying transactions.

Primary sources: [Form 990 instructions](https://www.irs.gov/instructions/i990) ·
[Schedule I instructions](https://www.irs.gov/instructions/i990si) ·
[Schedule F instructions](https://www.irs.gov/instructions/i990sf) ·
[IRS public-disclosure boundary](https://www.irs.gov/charities-non-profits/public-disclosure-and-availability-of-exempt-organization-returns-and-applications-public-disclosure-overview)

## 5. The direct blockchain antecedent

Treasury's Bureau of the Fiscal Service and GAO built a federal research-grants
blockchain prototype. NSF, Commerce, HUD, federal grant stakeholders and
grantees/subgrantees—including universities—contributed to the use-case design.

The model included:

- tokenized grant awards;
- private, permissioned Ethereum with Proof of Authority;
- ERC-1155 grant tokens;
- digital wallets;
- grant and subgrant creation;
- drawdown requests, approval, rejection, redemption and return;
- direct and indirect expenses, salaries and travel;
- transaction history down to subgrantees;
- potential near-contemporaneous reporting to FFATA and USAspending.

The controlling boundary is equally important:

- it was a minimally viable prototype in a nonproduction environment;
- it affected no actual grant transaction;
- the report was not policy or a recommendation;
- taking it to pilot required an alternatives analysis and further evaluation;
- GAO reported that Treasury had no plan at the located 2023 status point to
  advance the proof of concept.

Primary sources:

- [JFMIP-24-01, Harnessing Blockchain in the Federal Government](https://www.cfo.gov/assets/files/JFMIP-24-01.pdf)
- [Fiscal Service, Testing Blockchain to Streamline Grant Payment Processes](https://fiscal.treasury.gov/about-us/news/fiscal-service-testing-blockchain-to-streamline-grant-payment-processes.html)
- [GAO-23-106051, Blockchain in Government](https://www.gao.gov/assets/gao-23-106051.pdf)
- [GAO-22-104625, Blockchain Technical Assessment](https://www.gao.gov/assets/gao-22-104625.pdf)

## 6. The operating transition now visible

Executive Order 14249 directs Treasury-centered pre-certification, Do Not Pay
screening, richer payment identifiers and consolidation of federal
disbursement and financial-management functions. It does not select
distributed-ledger technology.

OMB's May 29, 2026 proposed Uniform Guidance rewrite would:

- require federal agencies to review recipient eligibility through Do Not Pay
  before disbursement;
- require States to screen relevant data before disbursing federal award funds;
- require non-State recipients and subrecipients to attach a brief written
  justification to each payment request once capable systems become available;
- require agency payment systems to record those justifications.

The proposed rule expressly does not require States to adopt a specific payment
system or technology. It remains proposed, not final.

Primary sources:

- [EO 14249 — Protecting America's Bank Account](https://www.whitehouse.gov/wp-content/uploads/2025/03/eo-14249.pdf)
- [OMB proposed Regulation for Federal Financial Assistance](https://www.federalregister.gov/documents/2026/05/29/2026-10817/regulation-for-federal-financial-assistance)
- [Treasury Do Not Pay](https://fiscal.treasury.gov/dnp/)
- [Defend the Spend](https://www.doge.gov/payments)

The strongest current description is:

> The federal system is attaching identity, purpose and risk evidence to the
> payment decision. That is transaction instrumentation even when the payment
> still settles through ACH, FedNow or another centralized rail.

## 7. Education, health and national security converge

The university research system already carries institution- and
individual-level certification gates:

- NSF-funded institutions submit foreign-financial disclosures for qualifying
  support from foreign countries of concern.
- Senior/key personnel certify disclosures and prohibited malign foreign talent
  recruitment participation.
- Institutions receiving more than $50 million annually in federal science and
  engineering support must certify an operating research-security program.
- Defense applies risk-based security reviews to fundamental research;
  classified and controlled-unclassified research use additional regimes.
- Energy applies research-security training and foreign-influence controls to
  R&D financial assistance.
- HHS's July 2026 high-risk life-sciences policy adds institutional review,
  monitoring, training, attestation and potential funding consequences to
  federally funded life-science institutions.

Primary sources:

- [NSF research security](https://www.nsf.gov/research-security)
- [Defense academic research security](https://basicresearch.defense.gov/Programs/Academic-Research-Security/)
- [Energy research-security training requirement](https://www.energy.gov/ia/research-security-training-requirement)
- [GAO-26-107544, Research Security](https://files.gao.gov/reports/GAO-26-107544/index.html)

The federal government does not need to place classified, health, tax or student
records on a public chain. A plausible hybrid separates:

```text
protected authoritative record
  + signed transaction event
  + persistent award and recipient identifiers
  + public amount, authority, purpose, chronology and correction proof
```

Sensitive detail can remain encrypted, permissioned, redacted or delayed while
the public receives evidence that a governed event occurred and was not
silently overwritten.

## 8. Adoption ladder

| State | Current assessment |
|---|---|
| Common recipient and award identifiers | Operating but fragmented |
| Pre-payment recipient screening | Operating and expanding |
| Per-payment purpose justification | Directed in bounded form; government-wide rule proposed |
| Public transaction-like feed | Bounded-live through Defend the Spend |
| Downstream recipient-to-subrecipient trace | Incomplete |
| Reconciled award, cash, accounting and correction record | Not established government-wide |
| Permissioned grant ledger | Prototype precedent only |
| Binding award term requiring DLT or wallet | Not located |
| Public cryptographic anchor | Not located as federal grant requirement |
| Public-chain grant settlement | Not located |
| Government-wide public blockchain | Forecast branch, not law or operating fact |

The likely legal-operating chain is:

```text
final rule or statute
  → financial data and interface standard
  → agency system authorization
  → NOFO or award term
  → subaward and procurement flow-down
  → privacy, security and records approval
  → production transaction
```

## 9. The larger story

Universities are unusually exposed because federal money reaches them through
students, grants, health systems, tax policy and debt while federal conditions
reach them through accreditation, research security, biosecurity, foreign
funding, civil rights and award compliance.

The structural change is not simply a funding cut:

> Federal money is becoming a conditional operating rail. Continued access
> increasingly depends on an institution's ability to emit timely,
> machine-readable evidence about identity, purpose, authorization and
> compliance.

The university may remain the employer and legal award recipient, but the
transaction—not the annual organizational report—is becoming the government's
preferred control object.

## 10. Claim firewall

Use:

> Federal university funding is moving toward transaction-level,
> pre-payment-controlled and machine-readable accountability. Treasury has
> previously prototyped a permissioned research-grant ledger, but current
> production systems and proposed rules remain technology-neutral.

Do not use:

> The government has decided to put all university grants or expenditures on a
> public blockchain.

No located primary object establishes that decision.
