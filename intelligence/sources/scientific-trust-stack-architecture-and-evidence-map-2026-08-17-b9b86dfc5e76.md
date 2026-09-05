# Scientific Trust Stack — Architecture and Evidence Map

**Evidence cutoff:** 2026-08-17
**State:** active workbench synthesis; operating components and proposed joins kept separate
**Scope:** United States federal science, national-security R&D and adjacent capital/security controls

## Executive ruling

The United States is assembling the components of a Scientific Trust Stack, but
no single instrument or platform joins all of them.

The stack is best understood as a federated claim and permission network:

```text
mission and legal authority
  -> named human / organization / agent / device / artifact
  -> authoritative identity and ownership records
  -> disclosures, attestations and institutional controls
  -> authority-specific screening and human adjudication
  -> typed eligibility receipt
  -> credential, role and task-scoped delegation
  -> controlled data / model / software / compute / instrument / funding access
  -> logged execution with authoritative time
  -> provenance manifest and result
  -> independent scientific validation
  -> release, payment, correction, revocation, appeal or retraction
```

Important components are already operating: FICAM/FPKI, agency identities,
SciENcv Common Forms, SAM UEIs and exclusions, NSF research-security analytics,
DOE RTES due diligence, DCSA FOCI mitigation, CFIUS reviews, export and data
controls, Genesis/Globus delegated workflows and federal logging systems.

The missing object is the joined instrument that makes these components
interoperate for a named scientific workflow while preserving their distinct
legal effects.

## Four different kinds of truth

| Truth class | Question | Example proof | What it cannot prove |
|---|---|---|---|
| Identity truth | Who or what is acting? | verified person, UEI, workload identity, certificate or token | authority, eligibility or scientific correctness |
| Permission truth | What may the actor do now? | role, attribute, license, award term, mitigation agreement or scoped token | that the action is scientifically sound |
| Provenance truth | What produced this artifact and what changed? | execution log, data/model/agent card, versions, timestamps and signatures | that inputs were accurate or conclusion is true |
| Scientific truth | Is the result fit for the asserted use? | calibration, method, uncertainty, validation, replication and expert review | legal permission, ownership or current access rights |

A mature stack must join these truths without collapsing them.

## Layer map

| Layer | Required objects | Current evidence state | Missing join |
|---|---|---|---|
| 0. Mission and authority | statute, strategy, agency mission, classification and purpose | operative but distributed | one system cannot inherit every authority from a broad strategy |
| 1. Subject identity | human, organization, agent, workload, device and instrument identifiers | production in purpose-specific systems | no universal science-wide identity profile |
| 2. Ownership and sponsorship | beneficial owners, parent chain, employer, sponsor, custodian and responsible organization | production in separate award, investment and security systems | cross-authority identity resolution and effective dating |
| 3. Disclosure and attestation | affiliations, support, appointments, capital, software, training and certifications | operating, uneven across agencies | common schema is not a common truth store |
| 4. Institutional controls | cybersecurity, foreign travel, research-security and export-control programs | required for covered institutions; implementation uneven | centralized certification collection and effectiveness evidence |
| 5. Risk and eligibility | proposal review, list screening, FOCI, CFIUS, OISP, export, data and procurement gates | operating by authority | reusable result without erasing native legal effects |
| 6. Credential and delegation | authenticator, certificate, token, role, attributes, sponsor and task scope | production for humans and workloads; agent standards emerging | human-to-agent delegation and card-to-runtime proof |
| 7. Controlled resource access | data, model, code, compute, instrument, facility, award and capital access | operating in separate platforms | science-wide attribute profile for resource policy |
| 8. Execution telemetry | identity, action, resource, privilege, time, inputs, versions and outcome | cyber logging and some scientific workflows operating | cyber log vocabulary joined to experimental method and uncertainty |
| 9. Provenance | chain of custody, versions, cards, manifests, signatures and correction state | designed and partly operating | universal signed-output or PQC profile |
| 10. Scientific validation | method, calibration, uncertainty, reproducibility, peer review and fitness for use | domain-specific and mature in parts | no security credential can substitute for it |
| 11. Consequence and remedy | accept, mitigate, suspend, terminate, pay, release, correct, revoke, appeal or retract | legally available but fragmented | downstream propagation and individual remedy across systems |
| 12. Cryptographic durability | key inventory, crypto agility, PQC, revocation and trusted time | mandatory migration program operating | named scientific-system migration profiles and public receipts |

## The subject and object registry

The trust stack must distinguish at least these subjects:

- human researcher or official;
- recipient institution and legal award entity;
- investor, beneficial owner and capital vehicle;
- foreign or domestic partner;
- AI agent, software service and workload instance;
- device, sensor, instrument and facility;
- data, model, software, method and experimental result;
- award, contract, license, mitigation agreement and payment authority.

Each object needs its own authoritative owner. ORCID can support researcher
attribution but is not a federal clearance. A UEI identifies an award-facing
organization but does not prove every subsidiary or beneficial owner. An agent
card describes an agent but does not prove that a running binary, model and key
match the card.

## Scientific eligibility receipt

The reusable Observatory object should be a set of typed receipts, not a single
score:

```yaml
eligibility_receipt:
  receipt_id:
  subject_type:
  subject_legal_id:
  aliases_and_parent_chain:
  beneficial_owners_as_of:
  sponsor_or_custodian:
  transaction_or_project_id:
  resource_and_action_scope:
  technology_and_data_scope:
  authority:
  operative_instrument:
  source_lists_checked:
  list_versions_and_dates:
  entity_resolution_confidence:
  jurisdiction_result:
  decision:
  conditions_and_mitigations:
  credential_or_token_binding:
  monitoring_owner:
  reporting_obligations:
  issued_at:
  effective_at:
  expires_or_recheck_at:
  change_triggers:
  correction_and_appeal_route:
  public_operating_evidence:
  unresolved_fields:
```

Valid `decision` values must remain typed, for example:

```text
not-in-jurisdiction
eligible
notify
license-required
prohibited
mitigation-required
award-condition
waiver
conditional-financing
approved-supplier
suspended
revoked
```

## The real research-security rail

The operating chain is not a national scientist passport:

```text
researcher and institution identifiers
  -> Biographical Sketch + Current and Pending Support
  -> MFTRP and training certifications
  -> institutional cybersecurity / travel / export controls
  -> proposal and award analytics
  -> human verification and clarification
  -> mitigation or award decision
  -> recurring and event-triggered updates
  -> validated-incident sharing
  -> award action or formal exclusion
```

NSF supplies the strongest public analytics model. Its research-security office
uses proposal, award and public-source data; its documented safeguards require
verification and human oversight before adverse action or external sharing.

DOE supplies the clearest lifecycle model. The RTES framework reviews the
solicitation, performs preselection due diligence and can reopen review after
award when people, ownership, control or project facts change. DOE calls this a
risk-based approach to continuous monitoring. That does not establish constant
automated surveillance of every awardee.

## Human, agent and workload identity

NIST SP 800-63-4 governs person-focused digital identity and expressly excludes
machine-to-machine authentication and API access on behalf of subjects. The
non-human lane instead draws from federal ICAM policy, workload identity,
zero-trust authorization and GSA's Digital Worker Identity Playbook.

The required joined proof for an autonomous scientific agent is:

```text
named sponsoring human or organization
  + registered agent descriptor
  + exact model / code / tool / environment versions
  + runtime workload identity and active key
  + task, resource, time and spending scope
  + policy decision and human-approval conditions
  + complete execution receipt
  + revocation and correction path
```

No public federal standard currently supplies that entire object. NIST's
Software and AI Agent Identity and Authorization project remains in the
`Reviewing Comments` state.

## Data, artifact and execution provenance

NIST's Research Data Framework defines provenance as the historical,
attributed and documented record of origin, processing and alteration. Genesis
adds data, model and agent cards, fine-grained access, auditability and
traceability. M-26-14 adds a current federal cyber-logging baseline centered on
identity, action, resource, privilege and authoritative time.

These layers can support a scientific execution receipt, but they are not yet
one standard. A cyber log normally does not carry instrument calibration,
experimental method, uncertainty, validation state or retraction history.

The minimum scientific receipt is:

```text
actor identity
  + delegated authority
  + exact data / model / software / instrument versions
  + authoritative time and environment
  + inputs, actions and outputs
  + chain of custody and access history
  + result signature or integrity check
  + validation and uncertainty state
  + correction / supersession / retraction link
```

## Supply-chain and cryptographic composition

Software, hardware and cryptographic inventories remain separate objects:

- SBOM describes software components;
- HBOM describes hardware components;
- CBOM describes cryptographic assets and dependencies;
- supplier due diligence evaluates ownership, FOCI, resilience and practices;
- a signed attestation states what an issuer claims about a build or process.

OMB M-26-05 rescinded the prior government-wide software-attestation memoranda
and shifted agencies toward risk-based collection unless another policy or
contract requires it. CISA's 2025 SBOM minimum-elements update remains draft.
EO 14412 separately requires future minimum CBOM guidance.

PQC migration is operative government-wide, but no public Genesis or American
Science Cloud profile currently applies FIPS 203, 204 or 205 to a named
scientific identity, workflow or output.

## The capital and partner perimeter

The perimeter is a graph of independent gates:

```text
legal identity + ownership + country nexus
  + capital source and governance rights
  + personnel affiliations
  + technology / data / facility classification
  + transaction type
  + receiving federal program
  -> authority-specific decision
  -> conditions, monitoring and expiry
```

The restricted-party lists are increasingly reused as inputs, especially in
the 2026 Department of War fundamental-research decision matrix. Their native
legal effects remain distinct. A BIS Entity List entry, SDN block, 1260H
designation, FCC Covered List entry, UFLPA listing and FASCSA order are not
interchangeable.

The correct rule is:

> A list match is a routing signal. The receiving authority determines the
> legal effect.

## Protect and promote

The perimeter is no longer purely exclusionary.

CFIUS's Known Investor Pilot pre-collects information from repeat foreign
investors without changing transaction-specific jurisdiction or review. The
new Strategic Vendor Program then seeks to route companies that have undergone
CFIUS review toward resilient U.S. suppliers and capital-access programs.
Department of War and other federal capital tools can provide direct credit,
loans or equity support to eligible capabilities.

This yields a two-sided control plane:

```text
DEFENSIVE
CFIUS + OISP + FOCI + export/data controls + procurement exclusions

AFFIRMATIVE
known-investor profiles + strategic-vendor routing + federal credit/capital
```

That is why the stack is better described as permissioned scientific-capital
routing than as a security wall.

## Continuing eligibility

Eligibility must be recomputed when any material object changes:

- employer, appointment, support or talent-program status;
- beneficial ownership, governance rights or financing;
- partner, subcontractor or affiliate;
- technology, data, classification or end use;
- agent model, code, tools, environment or sponsor;
- certificate, key, algorithm or trust registry;
- award, license, mitigation or list state;
- security incident, disclosure correction or validated allegation.

Recurring certification and change-triggered review exist. There is no public
evidence of one continuously calculated government-wide trust score.

## Failure constitution

| Failure | What the stack should do | What it must not do |
|---|---|---|
| mistaken entity match | preserve confidence, require human verification and permit correction | treat an alias match as final |
| inaccurate disclosure | distinguish mistake, omission and intent; preserve supporting evidence | infer guilt from foreign identity or collaboration alone |
| discriminatory screening | measure outcomes, enforce civil-rights safeguards and document criteria | use nationality, ethnicity or name as a proxy |
| compromised credential | revoke, reissue, inspect affected actions and propagate status | assume prior source facts were false |
| changed ownership | reopen the applicable authority-specific receipt | silently reuse an old clearance |
| incorrect scientific result | supersede or retract with linked evidence | claim a valid signature proves truth |
| bad automated action | stop delegation, preserve logs, reverse where lawful and review sponsor responsibility | hide behind agent autonomy |
| expired cryptography | inventory, replace and preserve validation history | call a legacy signature permanently trustworthy |
| adverse decision | give notice, grounds, response and appeal where law permits | create an unchallengeable permanent blacklist |

## Observable state ladder

```text
doctrine
  -> policy
  -> approved standard
  -> implementation guidance
  -> procurement or award requirement
  -> demonstrated workflow
  -> operating component
  -> joined cross-system workflow
  -> cryptographically verified output
  -> independently validated scientific result
```

Never promote an entire stack because one lower layer advances.

## Strongest promotion test

Call a named scientific workflow a complete trust-stack implementation only
when the record identifies:

> the actor, authoritative identity, credential issuer, exact delegated
> authority, protected resource, policy decision, software/model/data/instrument
> versions, execution record, provenance object, signature scheme, independent
> validation state and correction path.

Anything less is a real but partial layer.
