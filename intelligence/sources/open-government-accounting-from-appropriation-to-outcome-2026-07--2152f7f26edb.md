# Open Government Accounting — From Appropriation to Outcome

Evidence cutoff: 2026-07-30

This is the public-accounting entrance: it asks what “open” means, what may be
published, what must remain protected, and what an integrity architecture can
and cannot establish. The [Government Open Ledger Deep
Dive](../sources/government-open-ledger-deep-dive-2026-07-30-6d826ea3e054.html) owns the full operating
chain and source ledger; the Chronicle's Accounting Transition note owns the
maintained shared answer.

## Ruling

The federal government already has many components of machine-readable,
standardized and partly open accounting. It does not yet have one public,
joined event record from legal authority through downstream use, correction
and recovery.

The relevant transition is therefore not “put the federal budget on a public
blockchain.” It is:

```text
open standards and rule code
  + protected authoritative records
  + persistent cross-system identifiers
  + event-level publication and correction
  + downstream reporting duties
  + independent replay and assurance
```

A blockchain is one possible integrity and coordination component. It is not
the public-accountability objective itself.

## 1. “Open-source accounting” has five separate meanings

| Layer | Meaning | Current federal example | What it does not prove |
|---|---|---|---|
| open code | public can inspect software | open-source DATA Act Broker | source data are true or complete |
| open standard | public definitions and schemas | USSGL; GSDM | every system uses one transaction ID |
| open data | public records can be downloaded or queried | USAspending; Fiscal Data | complete downstream expenditure chain |
| verifiable record | signed or anchored chronology can be independently checked | prototype / design branch | legality, allowability or performance |
| open governance | rule versions, changes and administrators are visible | partial through standards and public process | no discretionary or protected decisions |

Confusing these layers produces false transparency claims. Publishing code is
not the same as publishing the ledger. Publishing an award is not the same as
publishing a payment. Publishing a payment is not the same as proving what a
recipient purchased or achieved.

## 2. The public-money event chain

The [Government Open Ledger Deep
Dive](../sources/government-open-ledger-deep-dive-2026-07-30-6d826ea3e054.html#1-the-public-money-chain-who-owns-each-fact)
owns the complete appropriation-through-recovery chain and the governing
non-equivalences. The Chronicle's `Federal Transaction Record` owns the
detailed system-and-identifier map. Those records keep appropriation,
obligation, payment, settlement, allowable expenditure, outcome, finding,
debt and recovery as separate facts and clocks.

## 3. What should be public

A minimum public event spine could expose:

- legal authority and Treasury account;
- program, award and recipient legal entity;
- event type and amount;
- event time, recorded time and publication time;
- certifying authority;
- parent, causal and supersession IDs;
- downstream recipient or vendor organization where law permits;
- performance category or milestone;
- correction reason and effect;
- debt, refund, recovery or discharge state;
- rule and schema version; and
- integrity proof for protected supporting records.

That would let the public distinguish an original payment, correction,
reallocation, refund and collection instead of reading every negative number
as fraud recovery.

## 4. What should remain protected

Public accountability does not require publishing:

- beneficiary personal information;
- bank account and authentication data;
- protected tax information;
- medical and education records;
- classified or security-sensitive detail;
- procurement information whose disclosure would harm competition or safety;
- active investigative methods or sealed evidence; or
- private keys and operational security controls.

A hybrid design can keep authoritative details in protected systems while
publishing a public event, disclosure-safe attributes and a cryptographic
commitment to supporting evidence.

A hash or anchor proves that a particular data object existed in a particular
form when committed. It does not prove that the invoice was honest, the
beneficiary eligible or the service performed.

## 5. Current federal building blocks

### FASAB

Federal GAAP is maintained through the FASAB Handbook. Its objectives include:

- budgetary integrity;
- operating performance;
- stewardship; and
- systems and controls.

FASAB explicitly treats accrual financial-position indicators as a starting
point that must be supplemented. Its systems-and-control objective asks
whether transactions comply with authority, assets are safeguarded, and
performance information is adequately supported.

### Treasury USSGL and GTAS

The Government Open Ledger source owner maintains the detailed Treasury
USSGL, GTAS, TAS/BETC and central-accounting record. Here, their relevant
limit is the conclusion: standardization and consolidation are not a public
transaction chronology.

### GSDM, DATA Act Broker and USAspending

The Government Open Ledger source owner maintains the detailed GSDM, DATA Act
Broker and USAspending evidence. Here, their relevant limit is the conclusion:
open schemas, validation code and publication remain a federation of
submissions and extracts, not proof of every downstream use, correction or
recovery.

### Treasury and JFMIP blockchain work

The Government Open Ledger source owner maintains the Treasury NSF prototype
and JFMIP evidence. Its bounded conclusion controls here: the work found
potential visibility, reconciliation and control benefits, but did not process
real grant payments and did not adopt a government-wide architecture.

### GAO controls and audit

The 2025 Green Book requires management to design, implement and operate
controls for operations, reporting and compliance. A public ledger can support
information, communication, monitoring and some control activities. It cannot
replace the control environment, risk assessment, segregation of duties,
eligibility decisions or responses to identified risk.

Auditing also remains bounded. A shared ledger can make complete populations
available, but auditors still must assess relevance, reliability, rights,
obligations, valuation and controls.

## 6. Fraud: what the architecture changes

### It can make these questions easier

- Was the payee or recipient the approved legal entity?
- Did the required approval sequence occur?
- Was the same invoice paid twice?
- Did a payment exceed an award or budget rule?
- Which downstream organization received the funds?
- Was an event changed after publication?
- Was a correction a reclassification, refund or recovery?
- Do agency, Treasury and recipient records reconcile?

### It cannot answer these alone

- Was the identity synthetic or controlled by a nominee?
- Was the invoice false?
- Did colluding officials approve a sham vendor?
- Did the service actually occur?
- Was the price reasonable?
- Was the expenditure legally allowable?
- Did the program achieve its outcome?
- Was a judgment corrupt but formally authorized?

An immutable ledger can preserve an authorized fraudulent transaction
perfectly. Fraud prevention still depends on identity, eligibility, authority,
performance evidence, independent data, segregation of duties and recovery
powers.

## 7. Dated adoption possibilities, not a required sequence

These eight July 30 states are separate adoption possibilities, not a
mandatory order or a forecast that each will occur. The hybrid endpoint below
is a research hypothesis to test, not an inevitable destination.

1. **Machine-readable reports** — already operating through XBRL, USSGL,
   GSDM and USAspending.
2. **Common event identifiers and correction semantics** — partly operating,
   incomplete across agency, Treasury, State and recipient systems.
3. **Continuous reconciliations and control checks** — feasible and partly
   present inside systems.
4. **Mandatory downstream event flow-down** — legal and contractual change
   required.
5. **Public transaction and correction spine** — bounded pilots and feeds,
   incomplete.
6. **Protected evidence with public integrity proofs** — architecture branch.
7. **Multi-agency shared ledger used for real payments** — not established by
   the reviewed record.
8. **Government-wide public blockchain** — forecast only.

The likely endpoint is hybrid: authoritative protected records, public
disclosure-safe events, open rule/schema layers and cryptographic integrity
proofs where they add value.
