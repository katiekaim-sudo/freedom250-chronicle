# The Federal Cryptographic Trust Stack

Completed: 2026-08-11  
Status: current Workbench research; not vault canon  
Evidence cutoff: 2026-08-11

## Executive ruling

The federal trust stack is not waiting to be invented. Its core cryptographic
components are already in production, but they are split across separate legal
and operational domains.

```text
authoritative source record
  -> identity proofing
  -> credential or account binding
  -> issuer-signed assertion / attribute bundle
  -> key and issuer trust registry
  -> verification by a relying party
  -> authorization or eligibility adjudication
  -> signed transaction / payment certification
  -> execution and settlement
  -> audit, revocation, correction and appeal
  -> optional public proof or shared ledger
```

The first major efficiency gain is therefore not “put the government on a
blockchain.” It is **stop making every agency re-prove the same person, re-check
the same issuer and reconcile the same authorization by hand**. Public-key
cryptography, federation and portable signed attributes can do much of that
without exposing a complete central profile.

The strongest production connector from identity to money is Treasury's Secure
Payment System (SPS). A federal employee's authority is established through
designation and role controls; the person enters SPS with a PKI credential; a
Data Entry Operator and a Certifying Officer perform separate functions; their
digital signatures are attached to the schedule; and Treasury retains the
signatures in the audit record. Cryptography proves who signed what and whether
the record changed. The Certifying Officer remains legally responsible for
whether the payment is legal, proper and correct.

That separation is the entire thesis in miniature:

> A signature can make accountability much sharper. It cannot make the signed
> assertion substantively true.

## 1. The layers and their present state

| Layer | Trust question | Current federal object | State | What it cannot prove |
|---|---|---|---|---|
| 0. Source | Who owns the fact? | SSA Numident, state vital records and DMVs, USCIS records, agency award/benefit systems | production, fragmented | that the record is current, complete or legally sufficient for another purpose |
| 1. Proofing | Is the applicant the claimed person? | Login.gov, agency proofing, PIV enrollment, commercial validation services | production | citizenship, benefit eligibility, honesty or future account control |
| 2. Credential | What authenticator is bound to the account/person? | PIV/CAC certificate, Login.gov authenticators, state mDL, agency account | production, uneven | authorization to every service |
| 3. Claim | What did an issuer attest? | SAML/OIDC assertion, PKI certificate, mDL signed data, NIST attribute bundle | production for some formats; emerging for portable public attributes | that the underlying source or policy is correct |
| 4. Trust registry | Why should a verifier trust this key/issuer? | Federal PKI roots and bridge; AAMVA VICAL; bilateral/multilateral trust agreements | production | that every issuer uses the same evidence or law |
| 5. Verification | Is the signature valid, unexpired, unreplayed and meant for this relying party? | FICAM federation, Login.gov integrations, mDL readers, PKI validation | production | permission to grant the requested service |
| 6. Adjudication | Does the verified fact satisfy this program's rule now? | agency policy engine, caseworker, certifying/authorizing official | production, agency-specific | that the rule itself is lawful or wise |
| 7. Signed action | Who authorized this transaction? | Treasury SPS payment certification and permanent signature audit trail | production | underlying eligibility or performance |
| 8. Execution | Did money or legal state actually change? | PAM/SPS, ACH, Fedwire, FedNow, card/digital payout, agency systems | production | final program outcome or absence of fraud |
| 9. Remedy | Can bad data, a compromised key or wrongful decision be corrected? | certificate revocation, account recovery, Privacy Act correction, program appeal, payment reversal/recovery | production but fragmented | automatic restoration across every downstream copy |
| 10. Public/shared proof | Can outsiders or peer agencies verify a common event history? | USAspending/open APIs; bounded public payment feeds; JFMIP permissioned-ledger prototype | public feeds production; DLT prototype only | oracle truth, legality or protection of PII |

## 2. The oldest live blockchain-adjacent idea is PKI, not blockchain

Federal Public Key Infrastructure (FPKI) supplies a mature trust fabric for
certificates, signatures, authentication and encryption. The Federal Common
Policy root and Federal Bridge Certification Authority let separate policy
domains map their certificate rules and establish trust without one system
issuing every identity. Certificate authorities are audited, keys expire or are
revoked, and relying systems validate the chain before trusting a certificate.

This is already a distributed institutional trust arrangement, but it is not a
blockchain. Its key lesson is that **shared trust does not require shared data**.
Agencies can recognize the issuer and validate the signature while retaining
their own source records, local accounts and legal authority.

Primary sources: [FPKI overview](https://www.idmanagement.gov/university/fpki/) ·
[Federal PKI architecture and services](https://www.idmanagement.gov/fpki/) ·
[FICAM trust services](https://www.idmanagement.gov/trust-services/)

## 3. Login.gov is production federation, not a national person database

Login.gov integrates with agency applications using SAML or OpenID Connect. The
partner specifies whether it needs authentication or identity verification and
which attributes it needs; the parties exchange public keys/certificates; and
the agency must complete an interagency agreement before production. The
receiving agency retains its own account, authorization rules and program
decision.

This replaces repeated account and proofing infrastructure, not the agency's
legal adjudication. GAO reported in 2024 that 21 of the 24 CFO Act agencies used
Login.gov; 16 reported improved operations and seven reported reduced costs.
Those are agency reports, not an audited government-wide savings total. GAO's
July 2026 update says GSA has implemented all but one recommendation; the open
item concerns mutually agreed timelines for partner technical problems.

The cost thesis must stay calibrated:

- shared proofing can reduce duplicate agency systems and compliance work;
- GSA publishes a usage-based price rather than making identity proofing free;
- agencies may still need more capable commercial tools;
- false identities can still pass a standards-aligned proofing process; and
- there is no current audited number proving net government-wide savings.

Primary sources: [Login.gov developer guide](https://developers.login.gov/) ·
[GAO-25-106640](https://www.gao.gov/products/gao-25-106640) ·
[GAO-25-107000](https://files.gao.gov/reports/GAO-25-107000/index.html) ·
[GAO-26-109261](https://www.gao.gov/products/gao-26-109261)

## 4. Portable claims are the important new frontier

NIST SP 800-63C-4 now supports two federation models:

1. a conventional identity provider sends a signed assertion to a relying
   party; or
2. a credential service provider issues a signed attribute bundle to a
   subscriber-controlled wallet, which presents only the needed values.

The standard permits both raw attributes and derived claims. A verifier might
receive “over 18” instead of a full birth date. Assertions must be
cryptographically signed and bound to the issuer, audience, subject and validity
window. Pairwise pseudonymous identifiers can make one person's identifier
different at different services, reducing simple cross-service tracking.

This is the architecture most relevant to a fragmented government. It could let
one authority prove a narrow fact without sending the complete source record or
requiring the verifier to maintain a permanent live connection to the source.

The standards are no longer merely conceptual:

- W3C made Verifiable Credentials Data Model 2.0 a Recommendation on May 15,
  2025;
- OpenID has final issuance and presentation specifications;
- NIST's federal digital-identity standard recognizes signed attribute bundles
  and subscriber-controlled wallets; and
- mobile driver's-license standards already provide a common state credential
  format.

But standards maturity is not the same as federal production adoption.

Primary sources: [NIST SP 800-63C federation requirements](https://pages.nist.gov/800-63-4/sp800-63c/Federation/) ·
[W3C VC Data Model history](https://www.w3.org/standards/history/vc-data-model-2.0/) ·
[OpenID4VP 1.0](https://openid.net/specs/openid-4-verifiable-presentations-1_0-final.html) ·
[OpenID4VCI 1.0](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html)

## 5. The first live public-credential trust registry is emerging from the states

AAMVA's mobile driver's-license Digital Trust Service (DTS) is a concrete,
operating issuer-key layer. AAMVA securely obtains participating issuing
authorities' public keys and publishes them through a Verified Issuer
Certificate Authority List (VICAL). A relying party downloads the VICAL and can
verify that a presented mDL was signed by a participating official issuer.

That is important because it solves one of the hardest scale problems: every
merchant, agency and verifier does not need to negotiate separately with every
state DMV merely to learn which issuer keys are genuine.

The federal bridge is not production yet. In January 2026 NIST's NCCoE announced
a government-use demonstration in which an mDL or other verifiable digital
credential could be used with Login.gov to access state or federal services.
The official description calls it a demonstration. It should not be promoted to
“Login.gov accepts every state mDL in production.”

Primary sources: [AAMVA DTS live announcement](https://www.aamva.org/publications-news/aamva-news/aamva-s-mobile-driver-license-digital-trust-service-is-now-live) ·
[AAMVA relying-party/VICAL architecture](https://www.aamva.org/identity/mobile-driver-license-digital-trust-service/for-relying-parties) ·
[NIST government-use demonstration](https://www.nccoe.nist.gov/node/2986)

## 6. Treasury shows where cryptography becomes accountable government action

Treasury's Secure Payment System is the clean production example:

1. an agency designates and enrolls a person for a defined role;
2. the SPS user must possess a PKI token/certificate and exist in the SPS user
   table;
3. the Data Entry Operator prepares or modifies the payment schedule;
4. a separate Certifying Officer certifies it;
5. SPS appends each relevant digital signature; and
6. Treasury permanently retains those signatures in the SPS audit log.

SPS also validates Treasury Account Symbol and Business Event Type Code fields
against Treasury's Shared Accounting Module before accepting a schedule. The
system therefore joins identity, role, separation of duties, accounting
classification, signed authorization and an audit trail before disbursement.

This is more consequential than a generic immutable record. It tells an auditor
**which legally designated person certified which exact schedule under which
role**. It also preserves the liability boundary: the certifying officer must
ensure the payment is legal, proper and correct. A valid signature does not
convert a bad invoice, false eligibility record or unlawful instruction into a
proper payment.

Primary sources: [SPS privacy impact assessment](https://fiscal.treasury.gov/system/files/files/pia/SPS-pia.pdf) ·
[SPS enrollment and designation](https://fiscal.treasury.gov/payments-from-government/secure-payment-systems-sps/forms) ·
[SPS TAS/BETC validation](https://fiscal.treasury.gov/payments-from-government/secure-payment-systems-sps/components) ·
[Certifying Officer training](https://fiscal.treasury.gov/about-us/training-events/cot)

## 7. Where the actual savings can come from

### High-confidence mechanisms

| Waste/friction | Cryptographic or federated remedy | Residual work |
|---|---|---|
| Every agency repeats identity proofing | reuse a shared proofing/federation service | program authorization, error correction and local account security |
| Every verifier separately tracks issuer keys | trusted root/bridge or VICAL-style key registry | issuer governance, audits and revocation |
| Whole records are copied to prove one fact | signed derived attribute or selective disclosure | lawful purpose, source accuracy and correlation controls |
| Manual signatures and unclear responsibility | credential-bound digital signature plus role and time | substantive review and legal accountability |
| Reconciliation cannot identify who changed what | signed event records and append-only audit log | accounting judgment, corrections and reversals |
| Static credentials remain trusted after compromise/change | expiration, status and revocation checking | fast propagation and due-process restoration |
| Separate agencies build the same crypto migration tooling | shared procurement, cloud upgrades, joint training and central support | inventory, legacy replacement and agency-specific risk |

### What is not yet proved

- no audited total shows how much government-wide spending cryptography has
  already eliminated;
- no production evidence shows a federal verifiable-credential layer carrying
  citizenship, benefit eligibility or award authority broadly across agencies;
- no evidence shows that placing the same data on blockchain would improve the
  source record or legal decision;
- the Treasury/JFMIP grant-blockchain prototype processed no real grant payment;
  and
- post-quantum migration is initially a major cost and risk-reduction program,
  even though shared procurement and coordinated modernization may lower its
  expense.

## 8. The failure constitution

Cryptographic systems change the location of failure; they do not abolish it.

| Failure | Cryptography's contribution | Necessary non-cryptographic control |
|---|---|---|
| wrong source data | faithfully proves which authority issued the wrong claim | correction, evidence review and downstream notification |
| compromised private key | exposes unverifiable/forged actions once detected | protected key storage, revocation and incident response |
| stolen but valid account | may show a valid credential controlled the session | phishing resistance, fraud detection, recovery and human review |
| stale eligibility | proves a once-valid claim | expiration, fresh source check and effective-date rule |
| unlawful policy | creates a precise execution record | judicial/administrative review and legal authority |
| excessive correlation | can reduce linkage through pseudonymous identifiers/selective disclosure | purpose limitation, retention rules and enforcement |
| irreversible bad transaction | preserves the mistake perfectly | reversal, compensating entry, restitution and appeal |
| quantum break | makes legacy public-key trust unsafe | inventory, crypto agility and PQC migration |

The correct system is therefore **tamper-evident, not correction-hostile**.
Corrections should be new, signed and linked events that preserve history while
changing operative state. Deleting the evidence of the prior error destroys
auditability; refusing to correct it destroys justice.

## 9. Blockchain's proper place

Most of this stack does not need blockchain.

Use conventional PKI/federation when:

- one recognized authority owns the fact;
- the relying party only needs to validate the issuer's signature;
- revocation and correction must be centrally governed; or
- low latency, privacy and legal accountability matter more than shared
  consensus.

Consider a permissioned ledger or public cryptographic anchor when:

- several institutions jointly create a sequence of events;
- no participant should be able to rewrite the shared history alone;
- reconciliation across those participants is a material cost;
- auditors or the public need independent proof of publication or sequence; and
- privacy-preserving off-chain records and an explicit correction constitution
  remain available.

For federal spending, the plausible design is hybrid:

```text
protected authoritative records and PII off-chain
  + issuer/official digital signatures
  + standardized event identifiers
  + permissioned shared state for authorized participants
  + public API and/or public cryptographic commitments
  + signed corrections, reversals and appeal outcomes
```

This would extend the trust stack. It would not replace appropriations law,
program eligibility, certifying-officer liability, banking settlement,
accounting standards or judicial remedy.

## 10. Post-quantum migration is the decisive live clock

**Targeted reconciliation: September 7, 2026.** The wider study retains its August 11 cutoff. This section joins the original Tech migration question to the issued order, the implementing memorandum and the already-saved GSA coordination return.

### Post-quantum migration: duties and the first coordination receipt

**Research question:** The original guardrail/AI-compute record asks how the defensive side of quantum readiness creates concrete federal migration and contractor obligations. Preserve the link between vulnerable infrastructure and the quantum build while separating risk rationale, mandatory planning, future rulemaking and completed protection.

EO 14412 was signed June 22, 2026 and published June 25. It directs federal PQC migration and supporting guidance; it does not establish that every federal system has migrated or that cryptography is invulnerable. Its high-value/high-impact-system guidance excludes national security systems and targets key establishment by December 31, 2030 and signatures by December 31, 2031. NSS reporting and critical-infrastructure assistance are separate lanes. The order requires a proposed FAR contractor rule within 180 days; it does not itself supply a final contractor rule. OMB issued M-26-15 on June 24: agency plans are due October 22, and its phased approach covers priority migration, signatures and risk-sensitive remaining-system migration through 2035. A concrete later receipt is GSA’s August 24 report of its first FICAM modernization working-group meeting on August 12, with 40 participants from 17 agencies. GSA also describes testing capability in development. These receipts support coordination and preparation, not completed system cutovers or approved PQC products. The existing cryptographic trust study should own these duties and later receipts, with the quantum acceptance study explaining the separate algorithm, module, product and system checks.

**Clocks:** EO signed June 22 and published June 25, 2026, 91 FR 38483–38486, document 2026-12909. OMB M-26-15 is dated June 24; plan deadline October 22 is 120 days from that date. GSA’s August 24 publication reports an August 12 first meeting; neither date is a system migration completion date. Reviewed September 7, 2026 with only the named later return revisited.

**Primary evidence:** [EO 14412, sections 1–7](https://www.federalregister.gov/documents/2026/06/25/2026-12909/securing-the-nation-against-advanced-cryptographic-attacks); [OMB M-26-15, core pages 1–5](https://www.whitehouse.gov/wp-content/uploads/2026/06/M-26-15-Execution-of-the-Migration-to-Post-Quantum-Cryptography.pdf); [GSA August 24 implementation receipt](https://www.gsa.gov/blog/2026/08/24/gsa-leads-the-transition-to-quantumresistant-technology).

**Evidence limits:**

- PQC means algorithms designed to resist quantum and classical attacks, not a guarantee of quantum-proof security. M-26-15 states that a cryptographically relevant quantum computer is not yet known to exist.
- The June 22 EO clock differs from the June 24 memorandum clock. M-26-15 gives 120 days from its date for agency plans; its GSA group instruction says 60 days from publication. August 23 is the calculated group deadline if publication occurred June 24; the meeting receipt itself establishes August 12.
- NSS exclusion from the civilian guidance is not exclusion from every EO duty. Assistance to private critical infrastructure does not impose the civilian-agency deadlines universally, and a proposed FAR rule is not a final contract requirement.
- An inventory, a plan, a working group, a testing capability, an algorithm standard, a module certificate and an agency-authorized operating system require distinct evidence. No system-specific completed migration or product approval was established in this bounded review.
- M-26-15 core pages 1–5 were read fully as text and rendered images, including footnotes; technical appendices were not fully reviewed. No broad agency-return, product-certificate or procurement sweep was undertaken.

| Clock | Required object and scope | Evidence state in this bounded review |
|---|---|---|
| July 22, 2026 | EO: agency migration lead within 30 days of June 22 | Direction verified; no agency-by-agency completion roster reviewed |
| 60 days from M-26-15 publication | GSA FICAM/PQC working group; August 23 if published June 24 | GSA's August 24 article reports the first meeting on August 12, 40 participants from 17 agencies; planned biweekly cadence is not a completed meeting history |
| October 22, 2026 | Agency migration plans, 120 days from the June 24 memorandum date | Issued requirement; submissions not established |
| December 19, 2026 | EO: NIST pilot initiation within 180 days of June 22 | Future requirement in the reviewed order; no operating pilot established here |
| March 19, 2027 | EO: minimum cryptographic bill-of-materials guidance within 270 days | Guidance requirement; no final guidance receipt established here |
| December 31, 2027 | NIST pilot completion | Future target; completion requires a later record |
| December 31, 2030 | Priority non-NSS high-value/high-impact key establishment | Migration target under the order's guidance lane; not a universal private-sector or NSS deadline |
| December 31, 2031 | Priority non-NSS high-value/high-impact signatures | Separate signature target; not evidence that migration is complete |
| Through 2035 | M-26-15 remaining-system migration phase | Risk and commercial-availability conditions remain relevant; not all federal systems have a 2030 deadline |

The GSA formation question has a named return. System inventories, filed plans, procurement, interoperability results and actual cutovers remain separate questions. The acceleration synthesis retains the detailed GSA receipt and civilian/NSS/private-rail distinctions. The quantum acceptance map explains algorithm, module, product and system acceptance. Its company evidence remains dated August 19.

The order directs agencies to seek savings through shared services, procurement, training and support. OMB encourages automation for cryptographic discovery and management. Those are implementation directions; a realized cost reduction requires measured results.

Primary sources: [EO 14412](https://www.whitehouse.gov/presidential-actions/2026/06/securing-the-nation-against-advanced-cryptographic-attacks/) ·
[OMB M-26-15](https://www.whitehouse.gov/wp-content/uploads/2026/06/M-26-15-Execution-of-the-Migration-to-Post-Quantum-Cryptography.pdf) ·
[NIST final PQC standards](https://csrc.nist.gov/News/2024/postquantum-cryptography-fips-approved) ·
[FPKI CITE](https://www.idmanagement.gov/implement/fpkicite/)

## 11. M7 provenance correction

**Source-boundary reconciliation: September 7, 2026.** The mid-2027 ledger-pilot date comes from the Chronicle's historical *Sovereign Ledger* prediction, made June 26 and updated August 20. M7 says **mid-2027**; June 30, 2027 is the broader note's structural check. These are forecast clocks, not dates established by a statute, agency program, award or procurement. The full argument, confidence levels and counter-reading remain in the original Chronicle note:

`04 - Synthesis/Predictions/2026-06-26 - MASTER PREDICTION — The Sovereign Ledger.md`

For government research, the question is whether an official source identifies a federal spending-transparency or payments pilot and the public or permissioned ledger it uses. Keep the named agency, instrument, function and implementation stage attached to that evidence. Federated identity, signed claims, PKI, append-only logs and PQC modernization can operate without such a ledger. Their official implementation dates do not establish that a ledger pilot exists.

This section owns the date-provenance clarification. The original prediction remains outside this Research package; its historical method and forecast are preserved there rather than repeated here. This correction does not reassess or rescore the prediction.

## 12. Watchboard and return gates

1. **FICAM/PQC working group — formation return received.** GSA's August 24
   article reports the August 12 first meeting. Follow the existing question into
   published deliverables, testing, procurement and system cutovers; formation
   does not establish those later results.
2. **September 5, 2026 — EO 14418 agency guidance.** Check whether State, DHS,
   SSA or other agencies propose portable citizenship evidence, new proofing,
   wallet credentials, source queries or data matching. Do not infer it from the
   EO alone.
3. **October 22, 2026 — agency PQC plans.** Determine which plans are public and
   whether identity, PKI, digital signatures, payments or credential wallets are
   named priorities.
4. **December 19, 2026 — NIST pilot initiation.** Identify system, algorithm,
   vendors, budget, legacy interface and success measures.
5. **Login.gov/mDL production bridge.** Promote only when GSA/NIST and a named
   agency show live acceptance, not another demonstration.
6. **Portable federal attribute.** Watch for a production credential carrying a
   bounded federal claim such as veteran status, professional authority,
   citizenship evidence, benefit enrollment or award authority.
7. **Treasury signature modernization.** Watch SPS/PAM, FPKI and ISO 20022 work
   for PQC-ready signatures, signed APIs or shared event proofs.
8. **Federal spending-transparency or payments ledger.** Identify an official
   source naming the federal pilot, its function and the public or permissioned
   ledger it uses. Distinguish a proposal, authorized pilot and observed operation.
   Section 11 explains the historical forecast date; it supplies no program deadline.
9. **Savings proof.** Require a baseline, realized cost comparison, error or
   fraud measure and attribution before claiming that cryptography reduced
   spending.
10. **Remedy proof.** For any portable credential or automated verification,
    locate revocation, individual notice, correction, appeal and downstream
    repair procedures before calling the system trustworthy.

## Conclusion

The government's likely next operating model is not a single national database
and not necessarily a blockchain. It is a **federated claim network**:

- authoritative agencies retain their records;
- trusted issuers sign narrow claims;
- wallets or identity providers present only what a relying service needs;
- registries distribute trusted issuer keys;
- agency law and policy decide what the verified claim permits;
- officials sign consequential actions;
- Treasury and other execution systems move value;
- revocation, correction, appeal and audit remain explicit; and
- public or shared ledgers may add provenance where multi-party reconciliation
  or public verification justifies their cost.

That architecture could genuinely make government faster and cheaper. The
efficiency comes from reusing verified facts and signed authority, not from
pretending that cryptography can replace legal judgment or human remedy.
