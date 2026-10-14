# SR 26-6: Verifiable Digital Credentials Inside the Bank Identity Gate

**Evidence cutoff:** September 8, 2026, 21:30 EDT  
**Geographic scope:** United States  
**Research state:** Current Workbench answer; primary-source deep dive  
**Authority boundary:** This report records public law, regulation, guidance,
technical standards infrastructure and demonstrated architecture. It does not
treat a proposed rule, draft NIST practice guide, reference implementation,
industry request, technical capability or Workbench interpretation as an
implemented legal mandate.  
**Promotion state:** Registered as Workbench Research Desk supporting evidence.
Not promoted to the Chronicle vault or rebuilt/shipped into the wrapper or
installed Observatory app.

## Bottom line

SR 26-6 is a narrow but consequential identity-infrastructure change. On
September 8, 2026, the Federal Reserve Board transmitted joint interagency FAQs
that say an unexpired, qualifying government-issued verifiable digital
credential (VDC), including a state mobile driver's license (mDL), **may count
as the government-issued identification used in the documentary branch of a
bank or credit union's existing Customer Identification Program (CIP)**. The
same release also updates a 2005 FAQ to say an electronic credential, including
a VDC, may be used as **one non-documentary verification method** when the
institution's CIP permits it.[^1]

The agencies did not create a digital-ID mandate, a right to have an mDL
accepted, a new account type, a new payment rail or a new Bank Secrecy Act
obligation. They did something more specific: they removed an interpretive
barrier that could keep a digitally signed state credential outside the
regulation's familiar category of an unexpired government-issued identity
document. The 2003 rule, the bank's written risk-based CIP, the required
identity fields, the reasonable-belief standard, fraud escalation,
recordkeeping and examination remain in place.[^2]

The practical effect is therefore **permission plus a supervisory pathway, not
automatic implementation**. A financial institution must choose to accept the
credential, write that method into its CIP, deploy technology capable of
extracting and validating the relevant information, decide what additional
checks are needed, preserve the required records and defend the result to its
regulator. The institution retains the compliance risk even when a state,
wallet provider, verification vendor or trust-list service supplies part of the
technical chain.

For the working Fed-castration theory, the result cuts in two directions. It
moves a high-volume identity operation toward state issuers, private wallets,
verification software and a non-Federal trust-list utility. But the legal gate
remains a Treasury/interagency BSA rule interpreted centrally and distributed
through all twelve Reserve Banks to supervised institutions and examiners.
This is better described as **technical outsourcing inside an incumbent
supervisory constitution** than as a transfer of monetary, account-access or
central-bank authority.

## What changed, and what did not

| Question | September 8 answer | Legal or operational effect |
|---|---|---|
| What is a VDC? | A data structure containing individual information, digitally signed by its issuing source, cryptographically bound to a device and protected by an activation factor. | Creates a specific interagency working definition. It is not a definition of every object marketed as a “verifiable credential.” |
| Can a government-issued VDC be a documentary method? | Yes, if unexpired, evidences nationality or residence, bears a photograph or similar safeguard, the institution has appropriate extraction technology and its CIP allows the method. | A qualifying mDL can occupy the same regulatory category as a physical driver's license or passport. |
| Can an electronic credential be a non-documentary method? | Yes, as one method allowed by the institution's CIP. | Updates the 2005 electronic-credential FAQ and expressly names VDCs. |
| Who bears responsibility for a non-government third-party credential? | The bank or credit union must ensure the third party uses the same level of authentication the institution itself would use. | Vendor or issuer involvement does not move the CIP duty off the institution. |
| Must an institution accept an mDL? | No. The rule neither requires nor prohibits reliance. | No customer acceptance right and no institution implementation deadline. |
| Did the agencies amend 31 CFR 1020.220? | No. | No new final rule, statutory duty or compliance date. |
| Did the agencies establish a new supervisory expectation? | They expressly say no. | Examiners receive the clarification, but the underlying risk-based standard remains the examination anchor. |
| Does the release cover legal entities? | The new government-VDC question concerns natural-person customers. | Corporate existence and beneficial-owner requirements remain separate. |
| Does the release create a national credential or identity database? | No. | It permits reliance on credentials issued elsewhere; it does not create an issuer, wallet, registry of people or federal identity number. |
| Does it authorize a payment, stablecoin or Federal Reserve account? | No. | Identity verification is upstream of product eligibility, account approval, sanctions, transaction monitoring and rail access. |

## The exact legal move

### 1. The statute supplied the identity duty

Section 326 of the USA PATRIOT Act added 31 U.S.C. 5318(l), directing Treasury
and the federal functional regulators to establish minimum procedures for
verifying the identity of people seeking to open financial accounts,
maintaining verification records and checking designated government lists.[^3]

### 2. The 2003 rule supplied a technology-neutral structure

The joint final rule was published May 9, 2003, became effective June 9, 2003
and required compliance by October 1, 2003. Now codified for banks at
31 CFR 1020.220, it requires a written CIP appropriate to the institution's
size and business and incorporated into its AML program.[^4]

Before opening an account, the institution generally must obtain at least:

- name;
- date of birth for an individual;
- address; and
- an identification number.

Verification can occur within a reasonable time after account opening. The
procedures must be risk-based and must let the institution form a reasonable
belief that it knows the customer's true identity. They must specify when the
institution uses documents, non-documentary methods or both.[^4]

The documentary branch already referred to “unexpired government-issued
identification” evidencing nationality or residence and bearing a photograph
or similar safeguard, with a driver's license and passport as examples. The
rule did not say the identification had to be plastic, paper or visually
inspected by a teller. The September 2026 interpretation uses that
technology-neutral language to admit the digital form.[^1]

### 3. The 2005 FAQ had already admitted electronic credentials—but only as a
non-documentary method

The agencies' April 28, 2005 FAQs said a bank could obtain an electronic
credential, such as a digital certificate, as one non-documentary method. SR
26-6 amends that FAQ to use current terminology and expressly include VDCs.
The old FAQ survives; it is not superseded wholesale. SR 05-9's page now records
both a June 2, 2026 revision removing reputational-risk references and the
separate September 8 amendment made by SR 26-6.[^5]

### 4. SR 26-6 opens a second route

The new FAQ's important language is that a qualifying government-issued VDC
“would qualify” as government-issued identification for the documentary
method. That is the substantive clarification. A digitally presented state
license no longer has to be treated only as an electronic, non-documentary
signal simply because it is not a physical card.[^1]

The two routes should not be collapsed:

| Route | Typical object | What the institution records | Key residual question |
|---|---|---|---|
| Documentary | Qualifying unexpired state mDL or other government VDC | Description of the document: type, identification number, place of issuance and, if present, issuance and expiration dates | Is it valid, within the CIP and sufficient to support reasonable belief? |
| Non-documentary | Electronic credential or VDC used as one electronic signal, including one issued or maintained by a non-government third party | Description of the method and its results | Is the source/authentication level adequate, and what corroboration is required? |
| Combination | VDC plus database, customer contact, biometric/liveness or other check | Both document description and method/results as applicable | Do the joined checks resolve discrepancies and presentation risk? |

A government-issued mDL can be the object used in a documentary method. The
same general class of digital credential can also participate in a
non-documentary method. Classification depends on the issuer, credential and
institutional use—not on the marketing label alone.

## What a bank must actually build

SR 26-6 does not install a reader or rewrite an institution's CIP. A plausible
implementation chain, synthesized from the rule, FAQ and NIST/AAMVA public
architecture, is:

1. **Policy gate.** The board- or management-approved CIP identifies which
   government VDCs, channels, customers and account types the institution will
   accept and whether the method is documentary, non-documentary or combined.
2. **Presentation request.** In a branch or remote flow, the bank's reader or
   verifier requests the identity attributes needed for the account-opening
   process.
3. **Holder activation.** The wallet requires an activation factor such as a
   PIN, password, face or fingerprint before releasing the credential.
4. **Issuer-signature validation.** The verifier checks that the credential and
   attributes were digitally signed by a trusted issuing authority and have
   not been altered.
5. **Device-binding/session checks.** The system checks proof tied to the
   credential's device and protects the presentation against replay or session
   substitution.
6. **Attribute extraction.** The system extracts the relevant fields. SR 26-6
   conditions acceptance on the institution having the technology or systems
   to do this.
7. **Fraud and person-to-credential checks.** The institution considers fraud
   signals, discrepancies and whether another method is needed to connect the
   presenter to the state-issued identity.
8. **Reasonable-belief decision.** The institution—not the wallet—decides
   whether it knows the customer's true identity to the regulatory standard.
9. **Account outcome.** Its CIP governs whether to open, restrict, delay or
   close the account and whether suspicious-activity reporting should be
   considered.
10. **Record creation and retention.** The institution records the required
    customer data and the description of the document or methods/results.

NIST's financial-sector mDL project demonstrates both cross-device and
same-device patterns. In a cross-device flow, a customer may open a bank site
on a computer, scan a session QR code with the phone, review the requested
attributes, unlock the wallet and present the license. The verifier can obtain
trusted issuer keys, validate the signature and send verified attributes to
the bank's identity-management system. NIST labels this a reference
implementation and its March 2026 SP 1800-42A an initial public draft; it is not
the mandated architecture for SR 26-6.[^6]

## The trust chain: what each actor proves—and does not prove

| Actor | Actual function | What its participation can establish | What remains outside that proof |
|---|---|---|---|
| State DMV or other government issuer | Creates the credential and signs an attribute bundle | The data came from the issuer and has not been altered, subject to key and status integrity | That the source record was correct, current in every respect, or presented by the rightful person |
| Wallet / mDL application | Stores or accesses credential, enforces activation and presents requested data | Local possession/activation and controlled release, depending on implementation | Bank-level CIP compliance, account eligibility or freedom from device compromise/coercion |
| Device secure hardware / operating system | Protects keys and supports device binding | The credential or presentation is tied to a device-held key | The human's legal identity by itself |
| AAMVA Digital Trust Service | Collects participating issuer public keys and publishes a Verified Issuer Certificate Authority List (VICAL) | A scalable way for readers to know which issuer keys are trusted | Identity of the individual, accuracy of DMV records, successful presentation or bank compliance |
| Verification vendor / bank verifier | Requests attributes, checks signature/session/status and returns results | Cryptographic authenticity and integrity findings, plus configured policy outputs | Final reasonable belief unless the bank's full process supports it |
| Bank or credit union | Designs CIP, chooses methods, resolves discrepancies and decides the account | Regulatory identity decision for its relationship | It does not become the credential issuer or gain a general national-ID authority |
| FinCEN and federal banking/credit-union regulators | Interpret the BSA framework and examine institutions | Common legal/supervisory treatment | Operation of a wallet, state issuer or universal credential registry |
| Twelve Reserve Banks | Distribute SR 26-6 to Federal Reserve-supervised institutions and examination staff; participate in supervision under Board authority | District delivery and examination path for a common Board/interagency interpretation | No Bank is assigned credential issuance, key-registry ownership, reader operation or a special national identity role |

AAMVA's DTS is a meaningful infrastructure node. It says participating issuer
programs must adhere to ISO/IEC 18013-5, AAMVA's implementation guidelines and
key-management practices; relying parties download the VICAL into their reader
technology before engaging with an mDL. This can remove the need for every bank
to negotiate separately with every DMV for public keys.[^7]

But it is not a federal database of credential holders. The public description
is a repository and distribution service for **issuer public keys**. The bank
still receives the selected credential data from the presentation path. AAMVA's
terms also disclaim warranties and place use risk on relying parties, including
limitations on AAMVA and issuer liability. The operational trust hub therefore
does not absorb the institution's CIP liability.[^8]

## The most important technical distinction: signature validation is not
identity completion

An mDL can improve the answer to “did the state issue this data, and was it
altered?” A physical card inspected over video or submitted as a photograph is
more vulnerable to image manipulation, counterfeit templates and uncertain
security-feature inspection. Public-key verification can make credential
authenticity machine-testable.

That does not answer every identity question:

- Was the DMV record itself obtained fraudulently?
- Is the license revoked or superseded even if its displayed expiration date
  has not passed?
- Was the credential provisioned to the correct wallet and device?
- Is the phone now controlled by the rightful holder?
- Did malware or a malicious application intercept the session?
- Was the user tricked into approving a presentation initiated by an attacker?
- Does a face/fingerprint unlock prove liveness and rightful use at the bank's
  required assurance level?
- Are the presented attributes sufficient to satisfy the institution's CIP and
  risk profile?

NIST's mDL issuance profile makes this residual work explicit. It recommends
comparison of a live facial sample with the DMV system-of-record image,
presentation-attack detection, fraud programs, device and velocity checks,
red-team testing, and a way to invalidate or status-check attribute bundles.
It also warns that status methods should avoid telling the issuer where a
specific person used an mDL. These are recommended controls in an emerging
profile, not requirements added by SR 26-6.[^9]

The interagency definition itself also matters. Its VDC is digitally signed,
device-bound and activation-protected. A generic W3C Verifiable Credential is
not automatically an SR 26-6 VDC, and “verifiable credential,” “digital
certificate,” “mobile ID” and “mDL” should not be treated as interchangeable
without testing those properties.

## Data extraction, copies and retention

The phrase “extract the relevant information” does not mean the bank must copy
the entire credential. The existing CIP rule requires the bank to retain:

- the identifying information collected at account opening;
- a description of any documentary evidence relied on, including document
  type, identification number, place of issuance and any issuance/expiration
  dates;
- a description of non-documentary methods and results; and
- the resolution of substantive discrepancies.

Identifying information is retained for five years after the account closes
(or a credit-card account closes or becomes dormant). Document descriptions,
methods/results and discrepancy resolutions are retained for five years after
the record is made.[^4]

The FFIEC manual is unusually clear: the CIP rule **does not require a copy of
the identifying document**. An institution may keep one, and risk or another
law/purpose may warrant it, but a description can satisfy the CIP record. That
distinction survives the move from plastic to digital.[^10]

This creates three separate data decisions that should not be collapsed:

1. **Presentation:** which attributes the bank requests from the wallet.
2. **Verification processing:** what the verifier temporarily sees while
   validating the presentation.
3. **Institutional retention:** what the bank or its vendors preserve after the
   identity decision.

NIST's draft reference work shows a privacy-preserving design in which only
attributes required for account opening are shared, the verifier deletes mDL
attributes after disclosure to the bank's identity system, and issuer keys can
be used to verify without contacting the issuer at transaction time. That can
reduce overcollection and issuer tracking. It is a demonstrated design choice,
not a privacy guarantee in SR 26-6.[^11]

The reverse is also possible. A bank or verifier could request more attributes,
retain full presentations, create a shadow profile, join wallet metadata to
other activity or call an issuer/status service in a way that reveals use.
NIST's privacy analysis names surveillance by verifier and issuer as risks. SR
26-6 does not prescribe minimization, prohibit correlation, specify deletion,
create a correction right or identify who receives presentation metadata.

## Fraud and control failure map

| Failure mode | Why cryptography does not automatically cure it | Necessary control question |
|---|---|---|
| Fraudulent original issuance | A genuine signature can authenticate bad source data | What proofing and fraud controls did the issuer use? |
| Stolen unlocked or coerced device | Device binding proves a device relationship, not always voluntary rightful presentation | What activation, liveness, transaction confirmation and anomaly checks exist? |
| Deepfake during provisioning or bank onboarding | Digital injection may defeat weak remote biometrics | Are presentation-attack detection and injection controls independently tested? |
| Replay/session swap | A previously valid response may be reused in another session | Are nonce, audience, session binding and back-channel retrieval controls enforced? |
| Expired, revoked or superseded credential | A valid signature can remain mathematically valid after trust should end | How are expiration, revocation and issuer-key changes handled without excessive tracking? |
| Malicious or compromised wallet | The credential may be exposed or presentation intent misrepresented | Which wallets are permitted, how are they evaluated and how is wallet provenance conveyed? |
| Trust-list compromise or stale keys | Readers can trust the wrong issuer key or fail to recognize a valid new one | How often is VICAL refreshed, authenticated, monitored and rolled back? |
| Verification-vendor failure | A vendor can misconfigure checks or overstate an assurance result | What contracts, testing, logs, incident duties and independent validation exist? |
| Attribute overcollection | Selective disclosure is optional in implementation | Which exact fields are necessary for CIP and which are retained for another lawful purpose? |
| False rejection / inaccessible phone | Digital-only design can exclude legitimate customers | Is a physical or non-documentary alternative preserved? |
| Discrepancy across sources | The mDL and bank/vendor data may conflict | Who resolves the conflict, what evidence controls and what correction route exists? |
| Credential accepted beyond onboarding | Staff may treat the mDL as proof for higher-risk actions it was not designed to authorize | Are enrollment, login, account recovery and high-risk transaction policies separately defined? |

The last distinction is essential: **CIP onboarding, account authentication and
transaction authorization are different clocks and control decisions**. NIST's
reference build explores re-presenting an mDL during high-risk transactions,
but SR 26-6 speaks to customer identity verification under CIP. It does not make
an mDL a universal authenticator or payment authorization instrument.[^12]

## The bank still owns the judgment

The FAQ says that if a government VDC shows indications of fraud, the
institution must consider that fact in deciding whether it can form the
required reasonable belief. The existing rule also requires procedures for
when not to open an account, what use is permitted while verification is
pending, when to close after failed verification and when a suspicious activity
report should be considered.[^1][^4]

The bank may use an agent or service provider to perform pieces of the work,
but that is not the same as the rule's tightly conditioned reliance on another
regulated financial institution. Formal reliance requires, among other things,
reasonable reliance, another federally regulated institution subject to an AML
program rule, a contract and annual certification. A wallet or identity vendor
does not become such a relying institution merely by verifying a credential.[^2]

For a non-government credential, the amended FAQ adds a direct responsibility:
the bank or credit union must ensure the third party uses the same level of
authentication the institution itself would use. The FAQ does not specify an
assurance-level number, approved-vendor list, certification regime or audit
test. Those are important unresolved implementation questions.

### A buried citation-lineage problem

The amended FAQ ends with “See also FFIEC guidance titled ‘Authentication in
an Electronic Banking Environment’ (Updated: September 2026).” The original
FAQ cited a July 30, 2001 document under that title. FFIEC later issued
*Authentication in an Internet Banking Environment* in 2005, supplementary
guidance in 2011, and then *Authentication and Access to Financial Institution
Services and Systems* in August 2021. FFIEC says the 2021 guidance replaced the
2005 and 2011 documents.[^20]

The September 2026 parenthetical therefore should not be silently promoted to
proof that FFIEC issued a new authentication framework that month. On the
public record located at cutoff, it appears in the amended FAQ and may date the
FAQ revision rather than a separately published FFIEC instrument. The live
FFIEC cybersecurity page still identifies the August 2021 guidance as the
current resource. The operative prudent reading is: institutions must join SR
26-6 to the current layered, risk-based authentication framework, but a
distinct September 2026 FFIEC authentication release was **not located**.[^20]

## What remains separate

### Legal-entity and beneficial-ownership identity

The new FAQ concerns verification of natural-person customers. It does not
replace the separate documentary rules for proving a corporation, partnership
or trust exists, nor the beneficial-ownership requirements for legal-entity
customers. A human's mDL can help verify that human; it does not by itself prove
the human owns or controls a company.[^13]

### Customer due diligence, sanctions and suspicious-activity monitoring

The rule expressly leaves other BSA obligations unaffected. SR 26-6 does not
complete customer-risk profiling, ongoing monitoring, OFAC screening,
beneficial-ownership work, fraud investigation or SAR analysis. A valid
credential can belong to a sanctioned person, a money launderer or a victim
whose account is controlled by someone else.

### Stablecoin-issuer CIP

The June 18, 2026 joint proposal for permitted payment stablecoin issuers is a
different legal object. It would implement the GENIUS Act's direction to treat
those issuers as BSA financial institutions and require effective CIPs. At this
cutoff, the located official sources still describe it as a **proposed rule**;
no final rule was located.[^14]

SR 26-6 applies existing bank/credit-union CIP interpretation to digital
credentials. It does not finalize the stablecoin proposal, confer stablecoin
issuer status, authorize a wallet as a bank, grant Federal Reserve account
access or determine which entity is the “customer” in every token arrangement.

### A federal digital identity mandate

No such mandate appears in SR 26-6. It is voluntary for the financial
institution, contingent on its CIP and technology, and limited to verifying
customers under an existing law. H.R. 7270, introduced January 27, 2026, is a
separate proposal concerning identity fraud and state digital credentials; its
introduced text would bar requiring a person to obtain or use a digital
credential and preserve physical credentials. It was not established as law in
this review and does not supply SR 26-6's authority.[^15]

## Why the change arrived now: established context and bounded inference

The agencies did not publish a detailed purpose statement with the FAQs. The
following context is established; the causal synthesis is an inference:

- FinCEN and FDIC ran a 2022 digital-identity tech sprint in which proposed
  solutions included W3C credentials and ISO-compliant mDLs.[^16]
- FinCEN's 2024 Identity Project divided failures into validation,
  verification and authentication and said mDLs could address impersonation
  and strengthen AML/CFT compliance amid rising AI threats.[^17]
- NIST's NCCoE began a financial-services mDL use case in September 2024,
  published an initial draft practice guide on March 18, 2026 and worked with
  government, bank, technology, standards and wallet participants.[^6]
- AAMVA's live DTS supplies a common issuer-key distribution layer for
  conforming participating jurisdictions.[^7]
- Industry comments to the FDIC in 2025 reported that compliance teams were
  reluctant to treat novel mDLs as CIP documents without regulatory clarity.
  That comment is stakeholder evidence, not an agency finding.[^18]

The bounded inference is that SR 26-6 follows technical maturation plus demand
for examiner-safe legal classification. The agencies did not order adoption;
they aligned a 2003 technology-neutral rule with an emerging state credential
format after the standards, reference architecture and issuer-key layer became
concrete enough for institutional use.

## Federal Reserve and twelve-Bank role

SR 26-6 is addressed to the officer in charge of supervision at **each Federal
Reserve Bank**. It applies to all Federal Reserve-supervised financial
institutions subject to the BSA. The Board asks the Reserve Banks to distribute
the letter to supervised domestic and foreign financial institutions and to
supervisory and examination staff.[^19]

That language assigns the same operational role to all twelve Banks:

1. receive the Board's common interagency interpretation;
2. distribute it through district supervisory channels;
3. put examination staff on the same interpretive footing; and
4. field implementation through the Federal Reserve supervisory structure.

The letter does **not** assign a particular Reserve Bank to operate the VDC
technology, maintain a trust list, contract with wallet providers, issue a
credential or make a national policy independently. There is no district
specialization in this release comparable to New York's market operations,
Richmond's National IT concentration or FRFS payment-service assignments.

This is exactly where the Reserve Banks' often-overlooked role matters: the
Board and interagency group can formulate one interpretation, while the
district Banks are the supervisory delivery and examination network. The
technical work may decentralize; the examination lattice does not.

## Theory assessment

### What strengthens the functional-unbundling reading

- A core bank-entry fact can arrive as a portable signed state credential
  rather than through a bank's visual inspection of a physical card.
- State DMVs remain the authoritative source; wallet and verification
  providers mediate presentation; AAMVA can centralize issuer-key discovery.
- Banks can integrate identity proofing into remote, automated customer
  acquisition and later step-up flows.
- Selective disclosure and local key verification can reduce direct issuer
  contact and whole-document copying.
- The technical identity edge can therefore move outside the Reserve Banks and
  outside a bank's branch network.

### What weakens an annihilation or replacement reading

- The duty is still rooted in federal statute and 31 CFR 1020.220.
- FinCEN, the Board, FDIC, NCUA and OCC issued one joint interpretation.
- Every institution must preserve its own written CIP and reasonable-belief
  decision.
- Federal and state supervisors can examine the implementation.
- All twelve Reserve Banks remain distribution and examination nodes for
  Federal Reserve-supervised institutions.
- No monetary-policy, reserve-account, clearing, settlement, liquidity,
  currency-issuance or emergency-lending power moved.

### Controlling ruling

**SR 26-6 mildly strengthens the “functional unbundling” leg and modestly
strengthens the incumbent-control counterweight at the same time.** Identity
evidence becomes more portable and more dependent on state/private technical
infrastructure, but its legal sufficiency is absorbed into a common federal
supervisory framework. The Fed's direct operating role in identity technology
does not expand; its Board-and-district role in defining and examining the
banking gate remains intact.

The release does not establish “castration of the Fed” as a fact. It is a
specific example of the larger mechanism under study: functions can migrate to
external technical layers while the incumbent institution retains the rule,
risk, examination and ultimate access boundary.

## Exact clocks

| Date | Clock | State at cutoff |
|---|---|---|
| October 26, 2001 | Section 326 enacted in the USA PATRIOT Act | Statutory authority |
| May 9, 2003 | Joint bank CIP final rule published | Final rule |
| June 9, 2003 | Final rule effective | Effective |
| October 1, 2003 | Required bank compliance | Operational legal duty |
| April 28, 2005 | Expanded interagency CIP FAQs / SR 05-9 | Interpretive guidance |
| September 2024 | NIST/NCCoE financial-sector mDL use case began | Reference-development program |
| March 18, 2026 | NIST SP 1800-42A initial public draft announced | Draft; comment period later closed |
| June 18, 2026 | Stablecoin-issuer CIP proposal announced | Proposed rule; separate |
| August 27, 2026 | NIST government-use-case public update | Demonstration program, not universal production acceptance |
| September 8, 2026 | Joint VDC FAQs and SR 26-6 issued; SR 05-9 page records amendment | Current interpretive guidance; no implementation deadline |

## Unresolved records and next watches

These are the high-value records needed to see whether interpretive permission
becomes material infrastructure:

1. **Institution adoption:** named banks and credit unions publicly accepting
   mDLs for CIP, with production dates and supported jurisdictions/wallets.
2. **CIP amendments:** institution-level descriptions of documentary versus
   non-documentary treatment, fallback methods and discrepancy handling.
3. **Examiner procedures:** any later FFIEC manual, work-program or examination
   update that turns the FAQ into testable examiner steps.
4. **Authentication citation:** a corrected or clarified interagency pointer
   explaining the FAQ's legacy title, its September 2026 parenthetical and the
   2021 FFIEC replacement guidance; no separate September 2026 framework was
   located.
5. **NIST finalization:** final SP 1800-42 volumes, changes from the initial
   draft and any adopted assurance profile.
6. **Trust-list operations:** participating jurisdictions, update frequency,
   revocation behavior, incident history, audit/certification and reader
   conformance.
7. **Wallet governance:** approved-wallet criteria, platform fees,
   interoperability, portability and recovery when a device is lost or a
   platform exits.
8. **Data fields:** actual attributes requested and retained by institutions,
   including whether photographs, device metadata, presentation histories or
   full credential payloads are stored.
9. **Vendor liability:** contracts allocating false-acceptance, false-rejection,
   key-compromise, breach, uptime, evidence-preservation and correction duties.
10. **Customer correction:** routes when DMV data, credential status, bank
    records or a vendor fraud score is wrong.
11. **Equity and fallback:** continued availability of physical and
    non-smartphone identity methods.
12. **Stablecoin rule:** a final rule, effective date and customer/account
    definition for permitted payment stablecoin issuers.
13. **Scope expansion:** later use of VDCs for account recovery, high-risk
    transactions, payments, government benefits or Federal Reserve account
    eligibility; none is established by SR 26-6.
14. **Incident clock:** a public fraud, trust-list, wallet or issuer-key incident
    that tests who actually absorbs loss and remediation duties.

## Claim audit

| Claim | Ruling |
|---|---|
| “Banks can now use a qualifying state mDL as the documentary government ID under CIP.” | **Established, with conditions.** |
| “Every bank must now accept a digital driver's license.” | **False.** Acceptance is optional and CIP-dependent. |
| “The regulation changed on September 8.” | **False.** The agencies issued interpretive FAQs under the existing rule. |
| “A cryptographic signature completes KYC.” | **False.** It authenticates issuer/data integrity; reasonable belief and other BSA controls remain. |
| “The bank no longer carries identity liability.” | **False.** The institution remains responsible for its CIP and third-party authentication. |
| “Banks must retain the full mDL or a license image.” | **Not established; CIP itself does not require a copy.** Required identity information and document/method descriptions must be retained. |
| “Selective disclosure means the bank receives no unnecessary data.” | **Technically possible, not guaranteed by SR 26-6.** |
| “AAMVA now holds a national database of every mDL user.” | **Not established.** Its public DTS role is issuer-public-key distribution, not a holder registry. |
| “The Federal Reserve now operates digital identity.” | **False.** The Board interprets and the Reserve Banks distribute/examine; the release assigns no credential operation. |
| “This is the stablecoin identity rule.” | **False.** The stablecoin-issuer CIP remained a separate proposal at cutoff. |
| “This creates a national digital ID mandate.” | **False.** No mandate, universal issuer or required consumer use appears. |
| “This is irrelevant because it is only an FAQ.” | **Too dismissive.** It is not a new rule, but it supplies a common interagency supervisory interpretation and removes a concrete adoption ambiguity. |
| “FFIEC issued a new authentication framework in September 2026.” | **Not established.** The date appears in the amended FAQ; FFIEC's live public resource still routes to its August 2021 replacement guidance. |

## Sources

### Controlling law, regulation and guidance

[^1]: FinCEN, Board, FDIC, NCUA and OCC, [Frequently Asked Questions Regarding Treatment of Verifiable Digital Credentials Under the Customer Identification Program Rule](https://www.fincen.gov/resources/statutes-regulations/guidance/frequently-asked-questions-regarding-treatment-verifiable), September 8, 2026; parallel [NCUA HTML version](https://ncua.gov/regulation-supervision/regulatory-compliance-resources/bank-secrecy-act-resources/frequently-asked-questions-regarding-treatment-verifiable-digital-credentials).

[^2]: FFIEC, [Customer Identification Program overview](https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/01), including documentary and non-documentary verification, third parties, reliance and examination boundaries.

[^3]: Joint agencies, [Customer Identification Programs for Banks, Savings Associations, Credit Unions and Certain Non-Federally Regulated Banks](https://www.govinfo.gov/content/pkg/FR-2003-05-09/pdf/03-11019.pdf), 68 FR 25090, May 9, 2003, statutory background and final rule.

[^4]: Federal Reserve Regulatory Service, [31 CFR 1020.220—Customer Identification Program Requirements for Banks](https://www.federalreserve.gov/frrs/regulations/section-1020220-customer-identification-program-requirements-for-banks.htm), current text reproduced by the Board.

[^5]: Federal Reserve, [SR 05-9, Frequently Asked Questions Relating to Customer Identification Program Rules](https://www.federalreserve.gov/supervisionreg/srletters/SR0509.htm), April 28, 2005, revised June 2 and amended by SR 26-6 on September 8, 2026.

[^6]: NIST NCCoE, [Guidelines on Implementing Mobile Driver's Licenses for Financial Institutions](https://www.nccoe.nist.gov/news-insights/nist-guidelines-implementing-mobile-drivers-licenses-financial-institutions), March 18, 2026; [financial use-case reference architecture](https://pages.nist.gov/nccoe-mdl-project-static-website/architecture/kyc_cip_onboarding.html); [current project hub](https://pages.nist.gov/nccoe-mdl-project-static-website/).

[^7]: AAMVA, [Digital Trust Service for Relying Parties](https://www.aamva.org/identity/mobile-driver-license-digital-trust-service/for-relying-parties), current at cutoff.

[^8]: AAMVA, [DTS Terms and Conditions for Relying Parties](https://www.aamva.org/identity/mobile-driver-license-digital-trust-service/for-relying-parties/terms-and-conditions-for-relying-parties), liability, warranty and use terms.

[^9]: NIST NCCoE, [NIST SP 800-63A Profile for mDL Issuance](https://pages.nist.gov/nccoe-mdl-project-static-website/building_mdl_assurance/nist_800-63a.html), fraud, biometric, revocation and privacy recommendations.

[^10]: FFIEC, [Customer Identification Program—Recordkeeping](https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/01); [Appendix P, BSA Record Retention Requirements](https://bsaaml.ffiec.gov/manual/Appendices/17).

[^11]: NIST NCCoE, [mDL Privacy Risk Assessment Methodology](https://pages.nist.gov/nccoe-mdl-project-static-website/pram.html), financial-account data flow, selective disclosure, disposal and surveillance risks.

[^12]: NIST NCCoE, [Use Case 1 Configuration Guide](https://pages.nist.gov/nccoe-mdl-project-static-website/use-case-1/vol-c.html), verifier, replay-protection and re-verification demonstration.

[^13]: FFIEC, [Beneficial Ownership Requirements for Legal Entity Customers](https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/03).

[^14]: FinCEN, [FinCEN, Agencies Propose Rule to Implement GENIUS Act Customer Identification Program Requirement](https://www.fincen.gov/news/news-releases/fincen-agencies-propose-rule-implement-genius-act-customer-identification), June 18, 2026; joint proposed-rule text, [Permitted Payment Stablecoin Issuer Customer Identification Program](https://public-inspection.federalregister.gov/2026-12460.pdf).

[^15]: Congress.gov, [H.R. 7270 introduced text](https://www.congress.gov/119/bills/hr7270/BILLS-119hr7270ih.pdf), January 27, 2026.

[^16]: FinCEN, [FDIC FinCEN Digital Identity Tech Sprint—Key Takeaways and Solution Summaries](https://www.fincen.gov/news/news-releases/fdic-fincen-digital-identity-tech-sprint-key-takeaways-and-solution-summaries), September 9, 2022.

[^17]: FinCEN, [Prepared Remarks, Identity Project Colloquium](https://www.fincen.gov/system/files/2024-06/PREPARED-REMARKS-IDENTITY-PROJECT-COLLOQUIUM-FINAL-508_0.pdf), June 17, 2024.

[^18]: Better Identity Coalition comment to FDIC, [Digital-identity and mDL comment](https://www.fdic.gov/federal-register-publications/better-identity-coalition-jeremy-grant-rin-3064-za49.pdf), 2025. This is a stakeholder submission and is used only as evidence of the stated industry concern.

[^19]: Federal Reserve, [SR 26-6, Frequently Asked Questions Regarding Treatment of Verifiable Digital Credentials Under the Customer Identification Program Rule](https://www.federalreserve.gov/supervisionreg/srletters/SR2606.htm), September 8, 2026; OCC, [Bulletin 2026-44](https://www.occ.treas.gov/news-issuances/bulletins/2026/bulletin-2026-44.html), parallel distribution and community-bank applicability.

[^20]: FFIEC, [FFIEC Issues Guidance on Authentication and Access to Financial Institution Services and Systems](https://www.ffiec.gov/news/press-releases/2021/pr-08-11), August 11, 2021; FFIEC, [Cybersecurity Awareness resources](https://www.ffiec.gov/resources/cybersecurity-awareness), current routing page; original FAQ text preserved in the [2005 NCUA resource copy](https://bsaaml.ffiec.gov/docs/resources/new_6_2006/NUCA%2005RA%2005.pdf).
