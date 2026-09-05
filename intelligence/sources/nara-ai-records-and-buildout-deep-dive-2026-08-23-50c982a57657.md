> Source cutoff: 2026-08-23

# NARA AI records layer and buildout

## Bottom line

NARA now occupies both sides of the federal AI transition.

- **As an AI user**, it reports 14 use cases in its February 2026 inventory:
  four deployed, two pilots and eight pre-deployment. The program spans Google
  Gemini, Azure OpenAI, Amazon Kendra, Vertex AI, an AWS-versus-GCP PII test,
  in-house code and two named contractors.
- **As the federal records authority**, AC 11.2026 tells agencies when prompts,
  outputs, data, audit trails, code, training copies and system documentation
  become federal records and which existing disposal schedules may apply.

The memo is material to **The AI build-out** because it supplies the documentary
constitution beneath AI-assisted government. It determines whether a later
reviewer can reconstruct what an agency asked, what the model returned, which
data or code was used, how the result entered an official process and what the
agency relied upon.

It is not a blanket preservation order. It is also not an AI-governance,
privacy, security, ethics, FOIA-disclosure or e-discovery rule.

## The August 21 legal object

| Field | Exact state |
|---|---|
| Issuer | National Archives and Records Administration, Office of the Chief Records Officer for the U.S. Government |
| Stable object | AC 11.2026, *Guidance on Applying the Federal Records Act to Artificial Intelligence Materials* |
| Public date | August 21, 2026 |
| PDF creation / modification metadata | August 21, 2026, 9:12:47 / 9:16:42 a.m. EDT |
| Workbench observation | The campaign recorded the page publication clock as August 21, 2026, 11:30:01 a.m. EDT; the separate page-modified clock is not the event clock |
| Addressees | Heads of federal agencies and departments, legal counsel, Senior Agency Officials for Records Management and Agency Records Officers |
| Immediate effect | Government-wide FRA guidance; no separate implementation deadline or reporting form stated |
| Claim limit | Records management only; no AI authorization, deployment, outcome, public disclosure or compliance result follows |

Primary object: [NARA AC 11.2026](https://www.archives.gov/records-mgmt/memos/ac-11-2026) · [guidance PDF](https://www.archives.gov/files/records-mgmt/policy/nara-fra-ai-guidance.pdf).

## NARA's own AI buildout

### Inventory state

NARA's official workbook contains 14 use cases and classifies all 14 as
`not high-impact`. That is NARA's classification, not an independent finding
that the systems cannot create material error or public harm.

| Stage in the February 10, 2026 workbook | Use cases | What is proved |
|---|---|---|
| Deployed: 4 | Gemini workplace productivity; A1 Museum personalization; NARA@WORK Kendra search; Amelia Earhart AI search | NARA reported active authorization or use in support of agency functions. Deployment does not prove accuracy, adoption rate, cost savings or public availability beyond the named surface. |
| Pilot: 2 | PII screening/redaction; ArchiAI semantic Catalog search | Limited test capacity. A pilot does not prove production approval, scale or reliable redaction/search performance. |
| Pre-deployment: 8 | Metadata auto-fill; topic/entity extraction; NPRC knowledge interface; EOP 42 semantic search; FOIA discovery/redaction; Archives.gov AI search; archival chat interface; automated data classification | Development or acquisition state only. The workbook's date field includes future or target-like dates and is not operating proof. |

Source: [NARA AI inventory page](https://www.archives.gov/ai) and the official [February 10, 2026 workbook](https://www.archives.gov/files/AI/nara-2025-ai-use-case-inventory-updated-02-10-2026.xlsx).

### Platform and control architecture

| Layer | Officially described state | Boundary |
|---|---|---|
| Workplace assistant | Google Gemini integrated into Google Workspace; workbook says purchased from Google and identifies an ATO | An approved platform does not make every interaction a record or validate every output. |
| Museum discovery | A1 Museum project uses Azure OpenAI; workbook names Cortina and combined contracting/in-house development | Personalization and generated tags do not alter the underlying archival record. Quality and provenance of generated metadata remain separate. |
| Internal search | NARA@WORK uses Amazon Kendra | Contextual retrieval does not prove that suggested answers are authoritative policy. |
| Public archival search | ArchiAI uses Vertex AI; EOP 42 also uses Vertex AI; Archives.gov search and archival chat remain pre-deployment in the workbook | The public inventory does not prove a general semantic-search or chat launch across Archives.gov. |
| PII review | NARA describes a comparison between a custom AWS model and GCP's native service | Pilot comparison does not prove production redaction authority or error rates. |
| Development plane | 2025 compliance plan says NARA has a FedRAMP-authorized hybrid-cloud environment, a centralized Git repository and plans a secure MLOps pipeline | The plan expressly says dedicated MLOps engineers and a dedicated shared-platform funding stream are still needed. |
| Governance | The Enterprise Architecture Governance Board initially performs AI Governance Board functions; CAIO coordinates with CTO, CDO and CISO | A planned or assigned control body does not prove completed review for every current system. |
| Workforce controls | Internal approved-assistant guidance bars classified, PII and CUI inputs, requires human review, and bars high-impact uses without CAIO approval | These are NARA's stated controls. The public record reviewed does not measure compliance or incident frequency. |

Source: [NARA 2025 AI Compliance Plan](https://www.archives.gov/files/nara-2025-ai-compliance-plan-final-v1-09-18-2025.pdf).

### Budget and infrastructure constraint

NARA requested **$419.670 million** in total FY 2027 discretionary budget
authority, including **$404.842 million** for Operating Expenses. The broader
Electronic Records Initiative request falls from **$30 million enacted in FY
2026 to $20 million requested for FY 2027**. That $20 million supports IT
infrastructure, network modernization, cloud storage, digitization equipment
and maintenance; it is **not an identified AI appropriation**.

The same budget describes ERA 2.0 as a system still being built, with an
estimated $94 million lifecycle cost, significant future volume uncertainty and
on-premises storage approaching capacity. NARA is therefore adding AI search,
classification and metadata production while the underlying ingest,
preservation and storage substrate remains a stated management challenge.

Source: [NARA FY 2027 Congressional Justification](https://www.archives.gov/files/about/plans-reports/performance-budget/2026/fy-2027-nara-congressional-justification.pdf), especially OE-15 and the Management Challenges / Annual Performance Plan sections.

## What becomes a federal AI record

The FRA requires agency heads to create and preserve adequate documentation of
agency organization, functions, policies, decisions, procedures and essential
transactions. Recorded information is not a federal record merely because an
agency made or received it. It must also be preserved or appropriate for
preservation because of evidential or informational value.

AC 11.2026 tells agencies to evaluate the circumstances of creation,
maintenance and use. The operative questions are whether the material:

1. was used in official business;
2. was relied upon in decision-making;
3. was circulated or shared;
4. was integrated into an agency system;
5. was subject to agency control; or
6. must be retained for a legal or business obligation.

The Archivist's determination whether recorded information meets the statutory
definition is binding on federal agencies under [44 U.S.C. § 3301(b)](https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title44-section3301).

### Likely record / likely non-record boundary

| AI material | Likely federal record when | Likely non-record when |
|---|---|---|
| Prompt or query | Captured in an agency system and circulated or used for an official purpose | Abandoned preliminary research never captured, circulated or used |
| AI output | Captured and used in official business or relied upon in a decision | Result is never used or acted upon |
| Meeting summary | Circulated or used as the official meeting record | Kept only for the user's recollection |
| Audit trail | Captured and used for an investigation or other agency business | Merely retained inside the tool or kept only for personal convenience |
| Training material | Copies of agency records used to train AI | Vendor-owned data that must be returned under the agreement and is not government-owned |
| Software, model or code | Created by the agency, created by a contractor on its behalf, or a COTS product is significantly modified into unique code | Unmodified commercial software such as Gemini or ChatGPT |
| Procurement / operations documentation | Documents acquisition and general operation of the AI platform | No blanket non-record category applies; use the functional schedule |

The important cloud seam is explicit: information generated by AI and passively
retained by a third-party platform is not necessarily "received" by an agency.
It becomes much harder to claim a federal record when the agency never captures
it into its own system or uses it for an official purpose.

## What may still be destroyed

All AI materials that do qualify as records require a NARA-approved General
Records Schedule or agency-specific schedule before disposal. The memo then
routes many records into existing functional schedules.

- **Transitory records, GRS 5.2 item 010:** needed generally for less than 180
  days and not needed for legal or fiscal obligations or to initiate, sustain,
  evaluate or evidence decision-making. They may be destroyed when no longer
  needed under the approved business rule.
- **Intermediary records, GRS 5.2 item 020:** used to create a subsequent record
  and not needed for the same protected purposes. They may be destroyed after
  the subsequent record is created.
- **Final work product:** the ordinary schedule for the email, report, case
  file, investigation or other output controls. NARA says the fact that AI was
  used is secondary.
- **Administrative AI records:** existing GRS provisions cover procurement,
  development, testing, maintenance, auditing, in-house software,
  documentation, staff training, certain user/access logs and committees.

Two categories do **not** currently have general GRS coverage: agency AI policy
documents and separately managed bodies of AI training data. NARA is
considering a GRS update. Until then, agencies need an applicable existing
agency series or must submit an agency-specific schedule to obtain disposal
authority.

The critical protection is that GRS 5.2 does not cover material required to
provide evidence of decision-making or legal and fiscal obligations. The
critical vulnerability is operational: the agency must recognize that
evidentiary value before the prompt, intermediate output or log is deleted.

Source: [GRS 5.2 FAQ](https://www.archives.gov/records-mgmt/grs/faqs-for-grs-5-2) · [records basics](https://www.archives.gov/records-mgmt/scheduling/basics) · [44 U.S.C. § 3303a](https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title44-section3303a).

## Join to the wider federal AI control plane

OMB M-25-21 requires executive agencies to document high-impact AI testing,
impact assessments, data fitness, potential civil-rights and privacy impacts,
independent review, risk acceptance, monitoring, traceability, human oversight
and appeal processes. AC 11.2026 does not replace those controls. It supplies
the records-management question underneath them: which of those documents,
logs, datasets and decisions must be preserved, and under which schedule?

That makes the two instruments complementary:

`AI use and risk duty (OMB) -> documentary evidence created -> record/non-record determination (NARA) -> retention schedule -> later oversight, litigation, FOIA processing or historical transfer`

This chain is an analytical join, not a statement that every M-25-21 artifact is
permanent, publicly releasable or covered by one retention period.

Source: [OMB M-25-21](https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf).

## Material implications for the Observatory

1. **The governing object is evidence, not the model.** The memo does not
   approve an algorithm. It governs the trace left by federal AI-assisted work.
2. **Auditability is capture-dependent.** A complete vendor log can exist while
   remaining outside the agency's recordkeeping system and therefore outside
   the practical preservation chain.
3. **The final document can outlive the reasoning chain.** An intermediate
   prompt or output may be destroyable after the subsequent report is created,
   unless it is needed to evidence how the agency decided or acted.
4. **Training data is the next live legal object.** NARA has identified a GRS
   gap for training corpora and AI policy records; a proposed or final schedule
   would set a government-wide disposal default.
5. **NARA is building on the same commercial stack it must document.** Its own
   program crosses Google, Microsoft/Azure, AWS and GCP/Vertex while the agency
   says the MLOps engineering and dedicated funding layer is not complete.
6. **Capacity is a limiting rail.** AI-generated metadata, search surfaces and
   newly preserved AI records increase dependence on ERA 2.0, cloud transfer,
   format identification, storage and digital-preservation controls.

## What the current record does not prove

- that every federal prompt, output or audit log is a record;
- that every agency has updated its AI policy or file plan;
- that any agency preserved or destroyed a specific AI interaction correctly;
- that AI records are automatically permanent or publicly releasable;
- that a vendor's retained chat history is under agency control;
- that NARA preserves model chain-of-thought or proprietary model internals;
- that all 14 NARA systems are operational or accurate;
- that the February 2026 inventory reflects every August 2026 stage change;
- that the $20 million Electronic Records Initiative request is an AI budget;
- or that a general Archives.gov semantic search or archival chatbot has
  launched.

## Recommended Observatory object

| Field | Recommendation |
|---|---|
| Atomic event | **August 21, 2026 — NARA applies the Federal Records Act to federal AI materials** |
| Plotline / subplot | Technology/AI · The AI build-out |
| State before | Government AI policy required inventories, risk controls and documentation, but NARA had not issued a dedicated public FRA application guide for prompts, outputs, logs, software and training materials. |
| State after | NARA expressly applied the federal-record definition and approved-schedule disposal regime to AI materials, with capture/use/reliance tests and a stated GRS gap for AI policy and training-data records. |
| Safe claim | NARA created a records-management boundary for the federal AI stack; it did not declare every AI interaction a record or impose general AI governance. |
| Best joins | OMB M-25-21; agency AI inventories and policies; FOIA search declarations; investigations; procurement and vendor logs; ERA 2.0 and digital preservation. |
| Promotion state | Pending Katie keep / revise / reject / hold. |

## Primary source shelf

- [AC 11.2026 landing page](https://www.archives.gov/records-mgmt/memos/ac-11-2026)
- [AC 11.2026 guidance PDF](https://www.archives.gov/files/records-mgmt/policy/nara-fra-ai-guidance.pdf)
- [NARA AI use-case page](https://www.archives.gov/ai)
- [NARA 2025 AI inventory workbook](https://www.archives.gov/files/AI/nara-2025-ai-use-case-inventory-updated-02-10-2026.xlsx)
- [NARA 2025 AI Compliance Plan](https://www.archives.gov/files/nara-2025-ai-compliance-plan-final-v1-09-18-2025.pdf)
- [NARA FY 2027 Congressional Justification](https://www.archives.gov/files/about/plans-reports/performance-budget/2026/fy-2027-nara-congressional-justification.pdf)
- [NARA FY 2026-2030 Strategic Framework](https://www.archives.gov/files/about/plans-reports/strategic-plan/strategic-plan-framework-2026-2030.pdf)
- [OMB M-25-21](https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf)
- [44 U.S.C. § 3101](https://uscode.house.gov/view.xhtml?req=%28title%3A44+section%3A3101+edition%3Aprelim%29)
- [44 U.S.C. § 3301](https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title44-section3301)
- [44 U.S.C. § 3303a](https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title44-section3303a)
- [GRS 5.2 FAQ](https://www.archives.gov/records-mgmt/grs/faqs-for-grs-5-2)
