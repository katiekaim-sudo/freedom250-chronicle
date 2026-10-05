> Source cutoff: 2026-09-26

# Official Record Authority and Blockchain Crosswalk — 2026-09-26

<!-- plain-english-entry:start -->
## In plain English

**Question:** What does official record mean across federal records management, CFTC recordkeeping, securities ownership, corporate accounting, audit and public disclosure, and what changes when blockchain or DLT is permitted to hold the record?

**Answer:** A record is not official because it sits on a blockchain; it is official because a law or regulator gives it a specific job, a named institution is responsible for it, and something legally follows from it.

**Evidence checked through:** 2026-09-26

The detailed record below keeps the legal wording, source limits and open questions.
<!-- plain-english-entry:end -->

## Question

What does **official record** mean across federal records management, CFTC
recordkeeping, securities ownership, corporate accounting, audit and public
disclosure—and what changes when blockchain or distributed-ledger technology
is permitted to hold the record?

## Scope and cutoff

This is a primary-source, U.S.-federal crosswalk through **September 26,
2026**. It answers the term inside the Freedom 250 accounting and tokenization
research. It is not a general survey of every state title registry, UCC filing
system, court record, tax record or property-record regime.

The September 24 CFTC FAQ is current **staff guidance** under existing rules.
It is not a Commission rule, amendment or no-action position. The September
2026 SEC transfer-agent modernization object remains a proposal. The SEC
Trading and Markets FAQ discussed below is also staff guidance.

## Bottom line

**Official record is not one universal legal status.** The phrase is used for
different institutional jobs. A record can be official for one purpose and
noncontrolling for another.

The most useful project definition is:

> An **official record** is recorded information that a governing authority
> requires, designates or relies upon as the institutional account of a
> defined act, status, right, obligation or transaction; it is maintained by
> an accountable recordkeeper under specified controls and is given a defined
> consequence within that authority's jurisdiction.

That definition has four indispensable parts:

1. **Authority:** the statute, rule, contract, charter, court, issuer or agency
   that gives the record its job.
2. **Object:** the exact act, right, obligation, position, transaction or
   decision the record describes.
3. **Accountable keeper:** the person or institution responsible for accuracy,
   retention, production, correction and recovery.
4. **Consequence:** what changes because the record says what it says—regulatory
   compliance, registered ownership, accounting input, audit evidence,
   admissibility, payment, settlement, disclosure or public memory.

The medium is not a fifth source of authority. Paper, an ERP database, a
permissioned ledger or a public blockchain can hold an official record if the
governing regime permits it and the responsible keeper satisfies that regime.
Consensus, immutability or public visibility does not by itself make a record
official.

## The term must be unpacked

| Record concept | What makes it official or operative | What it does **not** automatically establish |
|---|---|---|
| **Federal record** | Made or received by a federal agency in public business and preserved, or appropriate for preservation, as evidence or for informational value | Public availability, accuracy, permanence or legal effect on a private right |
| **Record copy / recordkeeping copy** | The copy designated for official retention by the responsible unit or kept in the recordkeeping system | That every other copy is a nonrecord; multiple copies can each have record status because of use |
| **Regulatory record** | A statute or regulator requires the person to create, retain and produce specified books, records, data or memoranda | Ownership, GAAP recognition, audit sufficiency, public disclosure or settlement finality |
| **Authoritative / controlling record** | Governing law, contract, issuer or responsible institution gives the record precedence when systems disagree | That every data field is public, on one system or immune from correction |
| **Ownership or position record** | The recognized registrar, transfer agent, depository, intermediary or issuer records the legally relevant holder or position under the governing structure | Beneficial ownership outside the recorded tier, freedom from liens, value, liquidity or cash settlement |
| **Books, records and accounts** | Corporate law and securities regulation require a reporting issuer to maintain records that accurately and fairly reflect transactions and asset dispositions | That a single source document determines GAAP recognition, measurement, consolidation or disclosure |
| **Audit evidence** | Information is relevant and reliable for a financial-statement assertion and the auditor obtains sufficient appropriate evidence | That a regulator-required or immutable record is sufficient by itself |
| **Public record / published record** | A government body or other authority makes the object available as a public or evidentiary record | That it is the controlling operational copy, complete, current or true in every respect |
| **Settlement or finality record** | The governing payment, securities, clearing or property regime specifies the entry or event that discharges an obligation or fixes a position | Accounting close, economic performance, legal title in every layer or absence of reversal/remedy |

## Officialness is a bundle, not a Boolean

Before calling any object an official record, capture this constitution:

```yaml
record_authority:        # statute, regulation, rule, contract, charter, order
record_purpose:          # compliance, ownership, accounting, audit, disclosure...
recorded_object:         # exact right, event, position, transaction or decision
record_owner:            # institution accountable for the record's meaning
record_keeper:           # operator/custodian responsible for maintenance
required_contents:
creation_or_effective_event:
authoritative_copy_or_system:
conflict_precedence:     # which record wins if systems disagree
retention_period:
production_and_access:
correction_method:
outage_and_recovery:
privacy_and_publicity:
evidentiary_scope:
legal_or_operational_consequence:
supersession_or_finality_rule:
```

If **authority**, **accountable keeper**, **conflict precedence** and
**consequence** cannot be named, “official record” is usually rhetoric rather
than a completed legal or operational description.

## 1. Federal records: official because government business is documented

The Federal Records Act definition is media-neutral. NARA explains that a
federal record is information, regardless of format, made or received by the
government in the course of business and preserved—or appropriate for
preservation—because it evidences government organization, functions,
policies, decisions, procedures or activities, or has informational value.

This is a **custody and public-business** definition, not a truth warranty.
NARA also makes three points that matter for blockchain:

- whether a document is an original or copy does not determine record status;
- multiple copies may each be records when they serve different business
  purposes; and
- a digitized record may replace a source record only when it has sufficient
  authenticity, reliability, usability and integrity under the governing
  requirements.

NARA's archival terminology defines the **record copy** as the copy designated
for official retention in the files of the administrative unit principally
responsible for producing, implementing or disseminating the document.

Therefore a blockchain copy of an agency record might be:

- a recordkeeping copy;
- a second record serving a distinct function;
- a preservation or verification layer;
- an input to another system; or
- a nonrecord convenience copy.

The answer depends on agency use, control and disposition authority—not on the
chain alone.

## 2. Electronic validity: accuracy, accessibility and reproducibility

The federal E-SIGN Act supplies a general electronic-record bridge. When law
requires a transaction record to be retained, an electronic record can satisfy
the requirement if it accurately reflects the information, remains accessible
to entitled persons for the required period and can be accurately reproduced
for later reference. Even an “original form” requirement can be satisfied by
an electronic record meeting those conditions.

This is important but technology-neutral. E-SIGN does not appoint a blockchain
as the authoritative record, identify the responsible keeper, decide which
system wins a conflict or determine the legal effect of the underlying event.
It removes paper as a necessary condition when the performance requirements
are satisfied.

## 3. CFTC: a native on-chain regulatory record can satisfy the duty

### What Regulation 1.31 actually defines

Commission Regulation 1.31 defines **regulatory records** as all books and
records required by the Commodity Exchange Act or Commission regulations,
including records of corrections or amendments. For electronic records it also
includes the data needed to access, search or display the records and the
electronically stored data describing how and when the records were created,
formatted or modified.

That last piece is crucial. The official compliance object is not only a
transaction hash or final state. It includes the metadata and system context
needed to retrieve and understand the record.

Regulation 1.31 requires:

- authenticity and reliability;
- security, signatures and data needed to authenticate the information;
- availability and production during an emergency or system disruption;
- an up-to-date inventory of record systems;
- retention for the applicable period; and
- prompt production in the form and medium requested by CFTC staff, with the
  records open to CFTC and Department of Justice inspection.

### What Regulation 45.2 adds

Regulation 45.2 requires covered swap entities and counterparties to keep
**full, complete and systematic records**, together with pertinent data and
memoranda, for swap activity. The records must remain retrievable and open to
specified regulators for inspection. The required record is therefore a
defined compliance population, not merely the subset of fields visible on a
public ledger.

### What the September 24 FAQ changes

CFTC staff says covered entities may use blockchain or DLT to create and
maintain on-chain records that satisfy Regulations 1.31 and 45.2. Staff would
not object solely because the entity did not also maintain an off-chain
version. For a public permissionless network, the entity must still be able to
retain and produce records if the network or block explorer is unavailable.

The result is meaningful:

> Within this CFTC perimeter, an on-chain record may be the native
> compliance record rather than merely a duplicate proof of an off-chain
> record.

But the result is bounded:

- the FAQ is staff guidance, not a Commission rule or enforceable right;
- the records entity remains responsible;
- the underlying rule determines the required content and retention period;
- the record must remain producible independently of ordinary public-chain
  access; and
- the FAQ does not say the record controls ownership, GAAP recognition,
  settlement finality or an auditor's conclusion.

The CFTC has accepted **representation portability for regulatory records**.
It has not merged all institutional truths into blockchain consensus.

## 4. SEC transfer-agent records: the stronger rights-record example

SEC Trading and Markets staff uses the phrase directly: a registered transfer
agent may use DLT as its **official Master Securityholder File**, or as a
component of that file, if the transfer agent satisfies the applicable
recordkeeping, reporting, examination, turnaround, safeguarding and accounting
control requirements. Staff says a duplicate off-chain “digital twin” is not
required solely because DLT is used.

The file may be federated. Transaction information—wallet, balance, ownership
percentage, units, purchase date and transaction ID—may be on-chain while
identity and other nonpublic information remains in proprietary systems. The
transfer agent must keep the whole record secure, accurate, current, readable,
producible and retained for the required period.

This is stronger than the CFTC example because the master securityholder file
has a defined **registered-holder and position** function. Still, the chain is
official only inside an accountable transfer-agent constitution:

```text
issuer and governing law
  -> registered transfer agent
  -> master securityholder file or linked file system
  -> recognized record holder / position
  -> distributions, communications, transfers and correction
```

The September 2026 transfer-agent proposal would make this structure more
explicit for electronic and linked systems while keeping an accountable
recordkeeping transfer agent responsible. It is not yet a final rule.

This comparison yields an important distinction:

| CFTC September 24 FAQ | SEC transfer-agent FAQ |
|---|---|
| Blockchain may satisfy required regulatory recordkeeping | Blockchain may constitute the official Master Securityholder File or a component |
| Primary consequence is compliance, retention and production | Primary consequence includes the recognized registered-holder/position record |
| The FAQ does not supply a cross-system conflict rule | Transfer-agent and issuer arrangements identify the accountable record and can state which component controls |
| Does not by itself determine ownership | Can be part of the record that determines registered ownership at that tier |

## 5. Corporate books and records: the accounting bridge

Exchange Act Section 13(b)(2)(A) requires covered issuers to make and keep
books, records and accounts that, in reasonable detail, accurately and fairly
reflect transactions and dispositions of assets. The SEC's internal-control
definition then connects those records to three different jobs:

1. reflect transactions and asset dispositions;
2. record transactions as necessary to prepare GAAP financial statements and
   maintain accountability for assets; and
3. prevent or timely detect unauthorized acquisition, use or disposition of
   assets that could materially affect the statements.

That is the accounting opening—but it is not a collapse of the layers.

```text
business or market event
  -> source / regulatory / ownership record
  -> controlled accounting record and subledger
  -> recognition and measurement rules
  -> journal and general ledger
  -> consolidation and close
  -> financial statements and disclosure
```

An on-chain regulatory or ownership record can become a stronger source for
the accounting system. It does not decide:

- which entity reports the asset or obligation;
- when recognition occurs;
- how the item is classified or measured;
- whether another obligation, lien or side agreement exists;
- whether consolidation or elimination is required; or
- what must be disclosed.

The likely first revolution is therefore **record architecture**, not a new
debit-credit or recognition rule. Journals can become reproducible outputs from
signed events while accounting policy and judgment remain separate,
inspectable objects.

## 6. Audit evidence: official does not mean sufficient

PCAOB AS 1105 defines audit evidence as the information used by the auditor to
reach conclusions and requires evidence that is sufficient and appropriate.
Appropriateness depends on relevance and reliability. Electronic information
is more reliable when controls over the information—including applicable IT
general and automated application controls—are effective. Company-produced
information must be tested for accuracy, completeness, precision and detail.

A blockchain can strengthen some evidence properties:

- time order and modification history;
- signatures and authorization traces;
- population completeness inside a known chain-and-address perimeter;
- reproducibility of deterministic processing; and
- independent observation from multiple nodes.

It does not by itself prove:

- the real-world event occurred;
- the signer was authorized rather than compromised or coerced;
- the address holder owns the asset beneficially;
- the population includes every wallet, chain, side agreement or liability;
- the recorded amount is the correct GAAP measurement; or
- management's classification, estimate or disclosure is reasonable.

So one object may be an official CFTC record and still require corroboration
for a different financial-statement assertion.

## 7. Official, authoritative, true, public and final are separate claims

| Claim | Required question |
|---|---|
| **Official** | Which authority assigned this record a job? |
| **Authoritative** | Does it prevail if another record conflicts? |
| **Authentic** | Is it what it purports to be, created or approved by the claimed actor? |
| **Reliable** | Are the source, controls, completeness and processing fit for this use? |
| **Accurate** | Does it correctly describe the recorded fact? |
| **Complete** | Does it include the entire required population and context? |
| **True** | Did the underlying economic, legal or physical reality actually occur as represented? |
| **Public** | Who can see it, under what privacy and access constraints? |
| **Final** | What event makes it no longer provisional, reversible or contestable? |
| **Controlling** | Which institution and rule say it wins a conflict? |

These attributes can diverge. A confidential transfer-agent file can be
official and controlling. A public blockchain can be authentic as a network
history but noncontrolling for legal ownership. A regulator-required record
can be official but inaccurate. An audited balance can be publicly reported
without exposing its underlying transaction population.

## 8. The project rule for using “official record”

Do not write **official record** alone. Use one of these more precise forms:

- federal record;
- designated recordkeeping copy;
- CFTC regulatory record;
- official master securityholder file;
- authoritative ownership or position record;
- corporate books, records and accounts;
- source accounting record;
- audit evidence;
- filed public disclosure;
- settlement-system record; or
- court/public-agency record.

If ordinary prose needs the umbrella phrase, attach the purpose:

> “Official for CFTC recordkeeping compliance under Regulation 1.31”

is materially different from:

> “The controlling ownership record,”

and both are different from:

> “Sufficient appropriate audit evidence for the financial statements.”

## 9. What the September 24 CFTC movement means for accounting

The CFTC did not change GAAP. It did something upstream:

1. reaffirmed that required regulatory records are technology-neutral;
2. accepted on-chain creation and maintenance as capable of satisfying the
   regulatory duty;
3. removed a presumed need for a parallel off-chain copy solely because DLT is
   used; and
4. preserved accountable production, metadata, retention, inspection and
   disaster recovery.

That can reduce the structural gap between:

```text
transaction event
  -> regulatory record
  -> accounting source
  -> reconciliation
  -> regulatory report and financial statement
```

The huge accounting change becomes plausible when a named implementation
proves that the same governed event object can serve several of those jobs
without each institution recreating and reconciling a private version.

The missing proof is not another statement that blockchain is allowed. It is
an operating case showing:

- the exact required record population and metadata;
- one accountable record owner and keeper;
- declared precedence across chain, private identity, custody and ERP systems;
- controlled corrections rather than silent overwrites;
- a tested outage/fork/migration recovery path;
- regulator production and examination;
- mapping into subledger and general ledger;
- auditor reperformance and assertion testing; and
- observed reduction in reconciliation, exception or close work without loss
  of legal or accounting information.

## 10. Do not carry

Do not carry any of these formulations:

- “Blockchain consensus makes a record official.”
- “Official means public.”
- “An official record is necessarily true.”
- “The CFTC made blockchain the official books.”
- “No off-chain duplicate means no off-chain data or controls.”
- “A token balance proves legal or beneficial ownership.”
- “A regulatory record determines GAAP recognition or measurement.”
- “An immutable record cannot or need not be corrected.”
- “A continuously available ledger creates continuous legal or cash finality.”
- “Official record status eliminates the auditor.”

## 11. Exact return gates

Return when one of these objects appears:

1. A named FCM, DCO, SEF, DCM, swap dealer or counterparty identifies a live
   Regulation 1.31 or 45.2 on-chain recordkeeping system.
2. A CFTC examination, enforcement object or court record tests whether that
   system satisfied authenticity, reliability, retention or production duties.
3. A registrant publishes the record constitution: field population, metadata,
   permissioning, identity join, system inventory, correction, fork, outage,
   migration and conflict-precedence rules.
4. A named implementation maps the same event IDs into the CFTC record,
   operational subledger, general ledger and regulatory report.
5. An auditor describes procedures over a native on-chain regulatory record
   and its controls, including completeness outside the chain perimeter.
6. The CFTC Commission adopts a binding rule or interpretation that changes
   the current staff-only posture.
7. The SEC finalizes, materially revises or withdraws its transfer-agent
   modernization proposal.
8. A live official Master Securityholder File encounters a chain fork, outage,
   erroneous transfer, court order or lost-key event and publishes the
   controlling correction and recovery result.

## Primary sources

### Federal-record and electronic-record foundation

- National Archives, [Records Basics](https://www.archives.gov/records-mgmt/scheduling/basics), including the media-neutral definition, copy-status, recordkeeping-copy and electronic-system guidance.
- National Archives, [Archives and Records Management Terminology](https://www.archives.gov/research/alic/reference/archives-resources/terminology.html), definition of “record copy.”
- 44 U.S.C. § 3301, [definition of federal records](https://www.law.cornell.edu/uscode/text/44/3301).
- E-SIGN Act, Pub. L. 106-229 § 101(d)-(e), [electronic retention, accessibility and accurate reproduction](https://www.govinfo.gov/content/pkg/PLAW-106publ229/html/PLAW-106publ229.htm).

### CFTC recordkeeping

- 17 C.F.R. § 1.31, [Regulatory records; retention and production](https://www.ecfr.gov/current/title-17/chapter-I/part-1/section-1.31).
- 17 C.F.R. § 45.2, [Swap recordkeeping](https://www.ecfr.gov/current/title-17/chapter-I/part-45/section-45.2).
- CFTC, [Release 9303-26](https://www.cftc.gov/PressRoom/PressReleases/9303-26), September 24, 2026.
- CFTC divisions, [Frequently Asked Questions Regarding Crypto Asset Activities](https://www.cftc.gov/media/14671/FAQ_CryptoAsset092426/download), updated September 24, 2026, Q13-Q15.

### Securities ownership and accounting records

- SEC Division of Trading and Markets, [Frequently Asked Questions Relating to Crypto Asset Activities and Distributed Ledger Technology](https://www.sec.gov/rules-regulations/staff-guidance/trading-markets-frequently-asked-questions/frequently-asked-questions-relating-crypto-asset-activities-distributed-ledger-technology), Q11.
- SEC, [Transfer Agent Rules proposing release](https://www.sec.gov/files/rules/proposed/2026/34-106246.pdf), Release 34-106246, September 1, 2026.
- SEC, [Exchange Act books-and-records formulation](https://www.sec.gov/rules-regulations/2003/05/improper-influence-conduct-audits), Section 13(b)(2)(A) quoted in the rule release.
- SEC, [Management's Report on Internal Control Over Financial Reporting](https://www.sec.gov/rules-regulations/2003/03/managements-report-internal-control-over-financial-reporting-certification-disclosure-exchange-act), definition of internal control over financial reporting.

### Audit evidence

- PCAOB, [AS 1105: Audit Evidence](https://pcaobus.org/oversight/standards/auditing-standards/details/AS1105), especially paragraphs .02-.10A and .11.

## Relationship to the maintained accounting answer

This crosswalk sharpens rather than replaces the package's controlling ruling:
blockchain and smart contracts can change recording, reconciliation, control
and publication architecture without eliminating recognition, measurement,
entity boundaries, valuation, legal rights, performance, collectibility or
audit judgment.
