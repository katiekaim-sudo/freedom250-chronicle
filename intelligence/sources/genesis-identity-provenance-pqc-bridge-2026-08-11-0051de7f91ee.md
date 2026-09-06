# Genesis Identity, Provenance and Post-Quantum Bridge

> Correction checked 2026-09-09: NNSA June 30 notice establishes an enterprise-authorized AWS environment but describes inaugural Genesis workloads prospectively. Original evidence cutoff is retained; this is a bounded wording correction, not a full refresh.

Completed: 2026-08-11  
Evidence cutoff: 2026-08-11  
Status: current Workbench research; no Chronicle landing  
Project scope: Freedom 250 mundane-policy research only  
Retrieval terms: Genesis Mission, American Science and Security Platform,
American Science Cloud, ModCon, Globus Auth, digital provenance, cryptographic
attestation, AI passports, PQC, FIPS 203, FIPS 204, FIPS 205, CNSA 2.0, M7

## Executive ruling

The first public bridge between the Genesis Mission and cryptographic proof has
appeared, but the full Genesis–identity–provenance–post-quantum stack has not yet
been joined in one operative federal instrument.

Three separate layers are now visible:

1. **Genesis identity and workflow controls are operating.** DOE and Globus
   describe federated authentication, delegated tokens, API access for human and
   non-human agents, authenticated production-compute jobs, access groups and
   audit controls.
2. **Genesis provenance is an adopted design requirement and partially
   implemented.** DOE requires traceability, auditability, digital provenance,
   fine-grained access controls and data/model/agent cards documenting origin,
   provider, inputs, outputs, methods, limits and authentication requirements.
3. **Genesis-specific cryptographic attestation is documented as a proposal,
   not an adoption.** DOE's July 2026 analysis of stakeholder responses records
   a proposal for hardware-attested confidential computing, AI passports for
   cryptographic attestation and open verification standards. DOE attributes
   the idea to an outside respondent; the analysis is not a solicitation,
   award, standard or implementation decision.

Government-wide and Department of War post-quantum mandates sit directly beside
these layers. No public Genesis system-security plan, contract, certificate
profile, cryptographic bill of materials or interface agreement located by the
evidence cutoff expressly applies FIPS 203, FIPS 204, FIPS 205 or CNSA 2.0 to a
named Genesis component.

The precise state is therefore:

```text
Genesis + federated identity             = operating
Genesis + provenance/auditability        = designed and partly operating
Genesis + cryptographic attestation      = explicitly proposed
Genesis + system-specific PQC            = not publicly established
Genesis + blockchain/DLT implementation  = not established
```

## The strict joining test

A source qualifies as the missing joined instrument only if it identifies a
named Genesis system, interface, procurement, pilot or standard **and** applies
an algorithm-level or control-level post-quantum requirement to its identity,
signing, provenance or data-transfer function.

Examples that would satisfy the test include:

- an American Science Cloud identity architecture specifying PQC or hybrid
  certificates;
- a Genesis solicitation requiring FIPS 203/204/205 or CNSA 2.0;
- a Genesis system-security plan or authorization package with a dated PQC
  migration profile;
- a cryptographic bill of materials naming Genesis components;
- a signed scientific-output or provenance standard specifying PQC algorithms,
  trusted issuers, revocation and correction; or
- a DoW–DOE interface agreement applying PQC to defense data entering or leaving
  the Genesis platform.

Generic use of the word `secure` does not satisfy this test. OAuth, OpenID
Connect, PKI, TLS, tokens, signatures and hardware attestation are not quantum
safe merely because they are cryptographic.

## Evidence matrix

| Public object | What it establishes | Authority state | Missing boundary |
|---|---|---|---|
| Executive Order 14363, Launching the Genesis Mission | American Science and Security Platform; cybersecurity-risk controls; user vetting/authentication; metadata and provenance; standard partnership, data and model agreements | operative presidential direction | no PQC algorithm, ledger or signature profile |
| DOE Genesis Data Team fact sheet | federated governance, fine-grained access control, licensing, auditability, digital provenance and traceability for verification and reproducibility | current DOE architecture | no disclosed signing or PQC schema |
| DOE Genesis Infrastructure Team fact sheet | federated secure ecosystem spanning open, restricted and classified systems; secure multi-agent workflows and access to facilities | current DOE architecture | no disclosed certificate, token or PQC control profile |
| DOE ModCon / American Science Cloud architecture | agent cards, data cards and model cards; a common onboarding and registration path; platform-handled identity, data, compute and inference | current implementation architecture | card contents are not proof that every card or result is digitally signed |
| May 2026 DOE ModCon/AmSC presentation | authenticated production workflows using Globus Auth and the ALCF IRI API; data transfer, job submission, monitoring and result retrieval; SSO, group permissions, tracing and evaluation work | demonstrated on production national-lab systems | unified AmSC token and several interfaces were still incomplete; no PQC named |
| Globus April 2026 Genesis presentation | Globus Auth already supports Genesis scientific-AI applications, non-human agents, delegated tokens and secure API access | provider-reported production use | no PQC or hybrid-key claim |
| DOE July 2026 Genesis RFI analysis | outside proposal for hardware-attested confidential computing, AI passports for cryptographic attestation and open verification standards | stakeholder idea preserved in a DOE synthesis | not DOE adoption, solicitation, award or standard; no PQC named |
| NNSA Secret/Restricted Data AWS environment | first enterprise-authorized cloud environment for Secret/Restricted Data, intended to host inaugural Genesis workloads | authorized classified-cloud environment; running Genesis workloads not established | public notice omits detailed cryptographic control profile |
| Argonne Genesis supercomputing-center sources-sought notice | market research for secure, scalable AI infrastructure, software, services and testbeds | planning; not a solicitation or award | no public PQC or provenance-signature requirement |
| DoW–Genesis partnership | DoW data, design loops and substantial planned investment flow into the DOE platform | announced interdepartmental program | no public interface-security or PQC annex |
| DoW 2026 PQC Strategy | DoW-wide deadlines for PQC support and use across PKI, signing, cloud, browsers, networks and contractor integrations | operative department strategy | never names Genesis or a specific DoW–DOE connection |
| EO 14412 and OMB M-26-15 | government-wide PQC inventory, planning, shared implementation and pilot clocks | operative government-wide program | no public DOE/Genesis migration plan located at cutoff |

## The strongest Genesis-specific cryptographic evidence

DOE's `Genesis Mission RFI Analysis 2026` is the first located public Genesis
document to use the relevant proof language directly. At pages 10–11 it records
this stakeholder proposal:

> “Verifiable AI Infrastructure” using hardware-attested confidential computing
> environments, AI passports for cryptographic attestation, and open
> verification standards.

The document identifies Lucid Computing as the respondent. It also says the RFI
was market research for strategic planning and did not constitute a
solicitation or promise to issue one. The idea has therefore entered DOE's
documented Genesis option set, but it has not crossed the adoption gate.

This is closer to the trust-stack thesis than a generic blockchain reference.
It names the proof objects needed to establish which agent, model or protected
environment produced an output. It still does not establish:

- which party issues an AI passport;
- what fact the passport attests;
- which key or trust registry validates it;
- whether the attestation covers code, model, data, hardware, result or all of
  them;
- how revocation and correction work;
- which post-quantum algorithms are required; or
- whether any ledger is involved.

## The production identity and provenance rail

The operating structure reconstructed from DOE and Globus sources is:

```text
human or non-human agent identity
  -> Globus Auth / delegated token
  -> authorized Genesis service or workflow
  -> DOE data + national-laboratory compute or instrument
  -> result + execution logs
  -> agent card + data card + model card
  -> provenance, audit and reproducibility record
```

DOE's May 2026 ModCon presentation supplies the best implementation proof. It
reports that an AI agent used the ALCF IRI API and Globus to authenticate, move
files, submit an ML training job to Polaris, monitor the job and retrieve the
result on production systems. The presentation also records remaining gaps,
including per-facility accounts, manual whitelisting, unfinished portal and
registry connections and the need for a single American Science Cloud token.

That is a real trust rail, not merely a future diagram. It is not yet public
proof of post-quantum protection or universal cryptographic provenance.

## How PQC enters—and where inference must stop

Executive Order 14412 and OMB M-26-15 require federal agencies to inventory and
migrate vulnerable cryptography. The DoW strategy separately requires its
systems to support PQC by December 31, 2030 and use PQC for key establishment
and digital signatures by December 31, 2031.

The DoW–Genesis partnership makes a future collision highly likely: DoW systems
and data connected to Genesis will need to survive DoW's cryptographic migration
requirements. That is an institutional inference, not a documented
system-specific implementation fact. The public record does not yet identify:

- the DoW or DOE endpoints in the connection;
- the network, API, transfer service or identity provider carrying the data;
- the present classical algorithms;
- the system owner responsible for migration;
- the relevant authorization boundary;
- the contract or interagency agreement allocating responsibility; or
- the planned PQC cutover date.

The NNSA classified-cloud announcement has the same boundary. Security detail
may be withheld for legitimate reasons. Public silence therefore does not prove
that PQC is absent, but it cannot be converted into affirmative evidence that
PQC is present.

## Procurement and standards ruling

The closest procurement-adjacent object located by the cutoff is Argonne's July
21, 2026 sources-sought notice for a National Genesis Mission Supercomputing
Center of Innovation. It asks industry about secure, scalable AI
infrastructure, equipment, software, services, testbeds, financing and
partnership structures. It is market research, not a solicitation or award, and
does not publish an algorithm-level cryptographic requirement.

No public object located by the cutoff satisfied the joining test. Searches
covered DOE, NNSA, DoW, NIST, SAM.gov, USAspending, Globus and ESnet surfaces for
combinations of Genesis/American Science Cloud/ModCon with PQC,
post-quantum, FIPS 203/204/205, CNSA 2.0 and cryptographic bill of materials.

## Relationship to the July 2026 science doctrine

`Science: A New Golden Age` imagines cryptographically signed laboratory
results, contribution records, smart contracts, distributed ledgers and
machine-executable scientific exchange. The report describes a horizon; it
does not select a chain or create a procurement.

The Genesis implementation documents now supply the identity, workflow,
provenance and platform layers underneath that horizon. The PQC program supplies
the coming cryptographic migration layer. The unbuilt connector is the operative
instrument that applies PQC-quality signatures or attestations to a named
Genesis identity, workflow or scientific result.

## M7 firewall

The documented Genesis identity, provenance and cryptographic-attestation work does not by itself establish a federal spending-transparency or payments ledger pilot. Identity assertions, provenance cards, append-only logs, PKI and PQC can operate without distributed consensus.

The [Cryptographic Trust foundation, section 11](../sources/federal-cryptographic-trust-stack-2026-08-11-1c0e21c343cb.html#11-m7-provenance-correction) owns the official-evidence question and the separate provenance of the historical M7 clock. This September 7 source-boundary correction preserves the bridge's original evidence cutoff and does not refresh Genesis implementation.

## Return gates

1. **2026-08-21 — Argonne sources-sought close.** Recheck SAM.gov for an
   amendment, attachments, response summary, draft solicitation or successor
   procurement containing security requirements.
2. **Federal FICAM/PQC working group — formation return received.** The
   [Cryptographic Trust foundation, section 10](../sources/federal-cryptographic-trust-stack-2026-08-11-1c0e21c343cb.html#10-post-quantum-migration-is-the-decisive-live-clock)
   owns the saved GSA report of its August 12 first meeting. The remaining Genesis
   question is a named DOE/Genesis participant, deliverable, pilot, procurement
   or certificate profile; group formation alone does not establish that join.
3. **Before October 2026 — American Science Cloud identity work.** Recheck the
   single-token, federated-SSO, portal, model-registry and job-API gaps recorded
   in the May presentation.
4. **2026-10-22 — agency PQC plans due.** Determine whether a public DOE plan
   identifies Genesis, AmSC, ModCon, Globus, national-lab APIs, classified cloud
   or scientific-output signatures.
5. **2026-11-24 — Genesis annual-report clock.** Look for implementation
   milestones, cybersecurity architecture, standards, procurements and
   interagency data connections.
6. **2026-12-19 — NIST pilot initiation.** Identify the system, algorithms,
   vendors, budget, success measures and relationship—if any—to identity,
   provenance or scientific workflows.
7. **2027-03-19 — CBOM guidance.** Search for Genesis/AmSC components in public
   agency implementation or acquisition documents using the new minimum
   elements.

## Primary source ledger

- [Executive Order 14363 — Launching the Genesis Mission](https://www.federalregister.gov/documents/2025/11/28/2025-21665/launching-the-genesis-mission)
- [DOE — Genesis Mission Data Team](https://www.energy.gov/documents/data-team-fact-sheet)
- [DOE — Genesis Mission Infrastructure Team](https://www.energy.gov/documents/infrastructure-team-fact-sheet)
- [DOE — ModCon: Transformational AI and Data](https://www.energy.gov/undersecretaryforscience/genesis-mission/modcon-transformational-ai-and-data)
- [DOE — May 2026 ModCon / American Science Cloud presentation](https://www.energy.gov/sites/default/files/2026-07/ModCon-Confab26.pdf)
- [American Science Cloud](https://amsc.energy.gov/)
- [Globus — Federated Identity and Access Management for Scientific AI Systems](https://www.globus.org/events/Improving-Scientific-Software-2026)
- [DOE — Genesis Mission RFI Analysis 2026](https://www.energy.gov/sites/default/files/2026-07/Genesis-Mission-RFI-Analysis.pdf)
- [NNSA — Secret/Restricted Data Enterprise Cloud and Genesis workloads](https://www.energy.gov/nnsa/articles/nnsa-launches-secretrestricted-data-enterprise-cloud-environment-collaboration-amazon)
- [SAM.gov — National Genesis Mission Supercomputing Center of Innovation sources sought](https://sam.gov/opp/e526498e24924e268dfc64c44d243276/view)
- [DoW — Genesis Mission partnership](https://www.war.gov/News/Releases/Release/Article/4551998/department-of-war-partners-with-the-genesis-mission-to-proliferate-ai-for-scien/)
- [DoW — 2026 Post-Quantum Cryptography Strategy](https://dowcio.war.gov/Portals/0/Documents/Library/DoW-PQC-Strategy.pdf)
- [Executive Order 14412 — Securing the Nation Against Advanced Cryptographic Attacks](https://www.whitehouse.gov/presidential-actions/2026/06/securing-the-nation-against-advanced-cryptographic-attacks/)
- [OMB M-26-15 — Execution of the Migration to Post-Quantum Cryptography](https://www.whitehouse.gov/wp-content/uploads/2026/06/M-26-15-Execution-of-the-Migration-to-Post-Quantum-Cryptography.pdf)
- [White House — Science: A New Golden Age](https://www.whitehouse.gov/science/)

## Reference capsule

> As of August 11, 2026, Genesis already has a real federated identity,
> authenticated-agent and provenance architecture. DOE has published—but not
> adopted—a stakeholder proposal for AI passports, hardware-attested computing
> and cryptographic verification. Government-wide and DoW PQC mandates now sit
> beside the platform, but no located public procurement, standard or
> system-security instrument yet applies PQC to a named Genesis component. The
> first document that does so will close the bridge.
