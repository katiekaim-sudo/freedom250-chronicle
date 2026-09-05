> Source evidence cutoff: 2026-09-02

# PRWORA, Education, Grants and Payment Interlock — 2026-09-02

## Controlling finding

The Education connection is material because education now contains two
different but increasingly adjacent control systems:

1. a **person-level student-aid eligibility rail** that already matches FAFSA
   applicants against SSA and DHS/SAVE before or around disbursement; and
2. an **institution- and State-level grant/payment rail** moving award
   administration across ED, DOL, HHS GrantSolutions and HHS Payment Management
   System, while Treasury/OMB develops wider prepayment screening and
   transaction-justification controls.

The September OLC opinion potentially adds a third function: a participating
State education component that obtains qualifying actual knowledge may sit
inside the State-wide PRWORA reporting perimeter.

That is a direct **control-architecture** join. It is not yet evidence that
FAFSA, school records, GrantSolutions, PMS or DNP transmits student immigration
information to DHS for enforcement.

## 1. The person-level Federal Student Aid rail is already operating

The 2025–2026 Federal Student Aid Handbook states:

- every FAFSA application is matched with SSA to verify name, date of birth,
  SSN and citizenship as recorded;
- an applicant who identifies as an eligible noncitizen and supplies an
  A-number is also matched with DHS;
- DHS verification is conducted through USCIS SAVE;
- the school receives match flags and a DHS case number in the ISIR;
- unresolved or conflicting records can require additional SAVE verification;
- SAVE verifies immigration status or category, while the school decides Title
  IV eligibility; and
- a successful identity or status match is not the entire aid determination.

The operating chain is:

```text
student FAFSA record
  -> SSA identity/citizenship match
  -> DHS/SAVE status/category match when applicable
  -> ISIR flags and case reference
  -> school documentary review / conflict resolution
  -> school Title IV eligibility decision
  -> award and disbursement controls
```

Primary sources:

- [Federal Student Aid Handbook — U.S. Citizenship and Eligible Noncitizens](https://fsapartners.ed.gov/knowledge-center/fsa-handbook/2025-2026/vol1/ch2-us-citizenship-eligible-noncitizens)
- [2026–2027 FAFSA Specifications, Volume 8 — Agency Matches](https://fsapartners.ed.gov/sites/default/files/2025-05/202627FSGVol8AgencyMatches.pdf)

## 2. Why the OLC opinion changes the legal question

Under the old 1998/2000 approach, PRWORA State reporting was confined to named
benefit-administration entities and required an unusually formal immigration
finding. The Education Department, a State education agency or a school did not
become a reporting entity merely because an education process encountered
citizenship or immigration information.

Under the new opinion, the inquiry changes:

```text
Is this actor legally attributable to the participating State?
  +
Does the actor possess actual knowledge, not merely a mismatch or suspicion?
  +
Does a Federal confidentiality rule constrain the name/address/identifier disclosure?
  =
Possible State reporting obligation requiring implementation guidance
```

This makes several education actors potentially relevant but not identical:

| Actor | Why it may encounter status information | PRWORA reporting boundary |
|---|---|---|
| State education department | State aid, adult education, workforce, grant and student-data administration | Strong State-component candidate; knowledge and confidentiality still must be proved |
| Local education agency or school district | Enrollment, residency, language, services and benefit-linked records | OLC signals possible local reach but does not define every district's legal status or attribution |
| Public college or university | State legal status, institutional aid, residency and enrollment records | State-component status varies; affiliated foundations and hospitals may be separate legal persons |
| Private college or career school | Administers Federal Student Aid under program agreements | Federal funding and SAVE access do not by themselves make it a State component |
| Financial-aid office | Receives SSA/DHS match results and documents for Title IV eligibility | A failed match, C code or ineligible benefit category is not automatically knowledge of unlawful presence |
| State grant recipient or contractor | May administer publicly funded education services | Recipient or contractor status alone is not sovereign State identity |

## 3. Failed eligibility is not unlawful presence

This is the most important education claim limit.

Federal Student Aid recognizes multiple categories of eligible noncitizens and
requires institutions to resolve documentary and SAVE conflicts. A person can
be ineligible for a particular aid program without being unlawfully present.
Conversely, an SSA mismatch, missing A-number, SAVE no-record result or
unconfirmed citizenship response can arise from stale records, data error,
citizenship acquired abroad, pending verification or the wrong identifier.

Therefore:

```text
SSA mismatch
≠ noncitizen
≠ Title IV ineligibility
≠ unlawful presence
≠ PRWORA knowledge
```

and:

```text
SAVE status/category response
-> school applies Title IV law

does not automatically become

SAVE response
-> DHS administrative enforcement
```

The 2000 notice explicitly protected this separation. The 2026 opinion rejects
the notice's categorical final-order threshold, but it does not convert every
student-aid mismatch or ineligible category into actual knowledge.

## 4. Education grant administration is moving across agencies and systems

Separate from student aid, ED has placed portions of education-grant
administration with other Federal agencies through interagency agreements.
The existing Research Desk education package establishes:

- DOL administration for selected workforce, elementary/secondary and
  postsecondary programs;
- HHS support or administration for selected family-engagement, school-support
  and child-care-related programs;
- DOI and State roles for specified programs;
- FY2025-and-earlier postsecondary grants remaining in ED G5 while qualifying
  FY2026-and-later grants move to GrantSolutions and HHS PMS; and
- a responsibility chain in which ED can retain statutory or policy authority
  while another agency administers awards, payment access or servicing.

One documented postsecondary path is:

```text
ED program law and appropriation
  -> ED/DOL interagency agreement
  -> DOL grant administration
  -> GrantSolutions award record
  -> HHS PMS drawdown and cash management
  -> State, university or other recipient
```

Primary sources:

- [ED–DOL postsecondary implementation](https://www.ed.gov/about/news/press-release/us-department-of-education-and-us-department-of-labor-take-next-steps-implement-postsecondary-education-partnership)
- [March 16, 2026 transition letter](https://www.ed.gov/media/document/dear-colleague-letter-ed-and-dol-grants-partnership-march-16-2026-113460.pdf)
- [ED–HHS family-engagement and school-support agreement](https://www.ed.gov/media/document/interagency-agreement-ed-and-hhs-family-engagement-and-school-support-february-23-2026-113311.pdf)

## 5. The grant-payment control layer

The education grant transition already increases the importance of persistent
recipient, award, system and responsibility identifiers. The same program can
have different actors for:

- statutory authority;
- appropriation and budget execution;
- interagency ordering and servicing;
- award creation;
- grant administration;
- recipient cash draw;
- payment release;
- performance acceptance;
- audit findings; and
- debt, correction or recovery.

Treasury DNP separately offers Federal and authorized State-program users
real-time or batch identity and eligibility screening. OMB's May 29, 2026
proposed Uniform Guidance revisions would broaden prepayment review for Federal
assistance and federally funded State-administered programs and would require
purpose justification in capable payment systems. Through the September 2
cutoff, that OMB rule remained proposed and targeted an October 1 effective
date if finalized.

Primary sources:

- [Treasury Do Not Pay products](https://fiscal.treasury.gov/payment-integrity/do-not-pay-dnp/products)
- [OMB proposed Regulation for Federal Financial Assistance](https://www.federalregister.gov/documents/2026/05/29/2026-10817/regulation-for-federal-financial-assistance)

## 6. The three-layer convergence

The material education join is:

```text
PERSON LAYER
student identity + citizenship/status evidence
  -> SSA / DHS-SAVE verification
  -> school eligibility decision

INSTITUTION / PAYMENT LAYER
recipient identity + award + conditions + purpose
  -> ED / DOL / GrantSolutions / HHS PMS / Treasury controls
  -> award or payment decision

STATE REPORTING LAYER
qualifying actual knowledge held by a participating State component
  -> PRWORA periodic/requested report
  -> DHS
```

They can share institutions, programs and identifiers without being one legal
system. The September opinion makes the third layer newly important; the
Education and payment changes make the first two increasingly structured and
machine-readable.

The operational risk and plotline importance lie in a later implementation
that explicitly connects them—for example, a State education directive that
defines qualifying knowledge, requires an export from a student or grant
system, names the DHS recipient and establishes correction and audit rules.

## 7. What would prove the direct Education join

A strong operating receipt would identify all of the following:

| Required field | Why it matters |
|---|---|
| State legal actor | Proves that the reporter is attributable to the participating State |
| Education program and record | Identifies where the knowledge arose |
| Knowledge predicate | Separates actual knowledge from a mismatch or program ineligibility |
| Federal and State confidentiality authority | Proves that names, addresses and identifiers may be disclosed |
| Reporting instrument and official | Establishes procedure and accountability |
| File/API schema and identifier | Shows the actual data movement |
| DHS recipient system and component | Distinguishes receipt from generic agency coordination |
| Correction and redress process | Shows how error or changed status propagates |
| Payment relationship | Establishes whether a separate grant or student-aid decision occurred |
| Downstream DHS action | Distinguishes report receipt from immigration enforcement |

Without those fields, the tie remains a high-confidence structural convergence,
not a demonstrated data or enforcement join.

## 8. Privacy and institutional boundaries

### FERPA

Education records are governed by Federal and State restrictions. PRWORA
§ 434 addresses prohibitions on exchanging immigration-status information, but
the September opinion does not separately resolve whether and how FERPA permits
disclosure of a student's name, address, identifiers and education-record
context. Status information and the surrounding education record should not be
treated as one indivisible disclosure object.

### Public universities and affiliated entities

A flagship university, system office, research foundation, hospital, athletics
entity and financial-aid office may have different legal identities. Public
funding, State creation or consolidated financial reporting does not answer
which entity is a State component for § 404.

### Servicing agencies

When DOL or HHS services an ED award, publication or system operation does not
move every underlying statutory responsibility. Likewise, a Federal servicing
agency does not become the State reporter merely because a State grantee uses
its platform.

## 9. Claim firewall

| Unsafe shorthand | Controlled statement |
|---|---|
| “FAFSA now reports undocumented students to ICE.” | FAFSA already uses SSA and DHS matching for eligibility; no new enforcement-reporting flow is established. |
| “A failed SAVE match proves unlawful presence.” | SAVE verifies status/category records; program eligibility, lawful presence and actual PRWORA knowledge are distinct determinations. |
| “Every school must report students.” | OLC broadens the State-component reading; school, district, university and private-recipient identity and confidentiality remain fact-specific. |
| “Education grants are now immigration enforcement.” | Grant servicing and payment controls operate at award and recipient levels unless a later object joins them to person-level immigration reporting. |
| “DNP will automatically stop the grant.” | DNP supplies match or risk information; the program retains independent eligibility and adverse-action responsibility. |
| “One shared platform merged ED, DOL, HHS and the States.” | Interagency servicing uses multiple legal actors and systems; stable identifiers and agreements, not platform adjacency, establish a join. |

## 10. Research disposition

This lane supports the dedicated PRWORA Research Desk project and creates a
formal relationship to `education-university-funding`. It does not alter the
existing Education package's controlling conclusions.

The first promotion-quality Education event will be one of:

- a State education-agency implementation directive under the September OLC
  interpretation;
- revised Federal Student Aid or SAVE guidance addressing PRWORA reporting;
- an Education/HHS/DOL grant or payment instrument adding the reporting duty;
- a named State or institution transmission with a documented legal basis; or
- a court order resolving the education/confidentiality perimeter.
