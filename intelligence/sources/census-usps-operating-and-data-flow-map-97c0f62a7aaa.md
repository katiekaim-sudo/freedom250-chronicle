# Census–USPS Operating and Data-Flow Map

**Cutoff:** 2026-08-11  
**Evidence rule:** an announcement, approved information collection, signed
interagency agreement, field operation, questionnaire response, later analysis
and 2030 production decision are separate states.

## 1. Current operating state

The August 11 [Commerce post](https://x.com/CommerceGov/status/2087154702064451706)
is public promotion of an existing test, not a new nationwide authorization.

| Date | State change | Primary source | Boundary |
|---|---|---|---|
| 2024-07-22 | Census announced a six-site, six-operation 2026 test | [Site-selection release](https://www.census.gov/newsroom/press-releases/2024/2026-census-test-site-selection.html) | Original design, not the final test |
| 2026-02-02 | Census narrowed the test to Huntsville and Spartanburg and centered USPS in-field enumeration plus field infrastructure | [Census statement](https://www.census.gov/newsroom/press-releases/2026/statement-on-2026-census-test.html) | Four sites and many planned operations removed |
| 2026-02-03 | PRA/OMB collection package entered final review as ICR `202601-0607-004`, OMB `0607-0936` | [Reginfo ICR](https://www.reginfo.gov/public/do/PRAViewICR?ref_nbr=202601-0607-004) | Review package, not field collection |
| 2026-03-23 | Census published the final public staffing, site and employment model | [Test update](https://www.census.gov/newsroom/press-releases/2026/2026-census-test-updates.html) | Public description does not disclose the IAA or field instrument |
| 2026-04-10 | OIRA approved the collection with change | [Reginfo approved-ICR search](https://www.reginfo.gov/public/do/PRASearch?agencyCode=0600&icrStatus=AC&operation=2&sortColumn=5&subAgencyCode=0607) | Approval permits collection; it is not a result |
| 2026-05-01 | English-only internet self-response began | [Respond-now release](https://www.census.gov/newsroom/press-releases/2026/respond-now-to-2026-census-test.html) | No paper or telephone response option |
| 2026-06-01 | Postal and ordinary enumerators began nonresponse follow-up | [Enumeration release](https://www.census.gov/newsroom/press-releases/2026/2026-census-test-enumeration-begins.html) | Operative test, not an official population count |
| 2026-08-31 | Census confirms the Huntsville and Spartanburg test concluded | [Live test page](https://www.census.gov/programs-surveys/2026-census-test.html) | Closure is not a response, completed-case, cost, quality, productivity, USPS-comparison or 2030-design result |

GAO reports that Commerce eliminated four sites and removed or reduced 10 of 19
planned operational activities. A proposed change to administrative-record
enumeration was among the removed experiments. The two surviving priorities are
USPS-assisted in-field enumeration and field infrastructure, staffing and
training. [GAO-26-108848](https://www.gao.gov/products/gao-26-108848)

## 2. Sample and labor constitution

The planning universe is approximately 154,600 housing units:

- Huntsville: 81,000;
- Spartanburg: 73,600.

The approved burden model assumes, but does not yet observe, a 50% split:

- 77,300 online self-responses at 40 minutes; and
- 77,300 in-person nonresponse interviews at 10 minutes.

Public staffing was approximately 25 postal and 25 ordinary Census takers at
each site.

### Huntsville

Postal employees receive a separate Census appointment, work outside postal
duty hours, identify solely as Census employees and receive the same stated
$19.75 hourly pay as other Census takers. This is one person holding two roles;
the Census work does not become ordinary postal work.

### Spartanburg

USPS employees remain in their postal jobs, receive Census Special Sworn
Status, enumerate on their assigned delivery routes during postal work and
receive normal USPS pay. This is the more institutionally novel model because
the Census activity is embedded inside the delivery day.

Both groups undergo background checks and Census training, take the Title 13
oath, use Census-issued equipment and remain bound by Census confidentiality
for life. [Census FAQ](https://www.census.gov/programs-surveys/2026-census-test/faq.html)

## 3. Questionnaire constitution

### Established

- The full online questionnaire uses American Community Survey content.
- Public Census materials say it asks name, sex, age, Hispanic origin, race,
  citizenship and education.
- Nonresponding households receive a shorter in-person subset.
- The OMB package identifies the in-field instrument as `D6-QE-IFE` and assigns
  a 10-minute burden.

### Not public

The OMB package publishes the ACS paper questionnaire but not `D6-QE-IFE`.
Neither Census nor GAO identifies the shorter question set.

The public record therefore supports:

```text
online test asks citizenship
AND
postal workers conduct shorter nonresponse interviews
```

It does not yet support:

```text
postal workers ask citizenship
```

That claim requires the missing field questionnaire, enumerator script or an
official description naming citizenship in the nonresponse subset.

## 4. Systems and data visible in the public paperwork

The OMB supporting statement describes:

- respondent-owned computers, tablets and phones for internet response;
- Census-issued handheld devices for field enumeration;
- automated recruiting, hiring, training and workload management;
- case routing and management reports;
- response processing; and
- an evaluation of whether USPS personnel can enter Census systems without
  disrupting mail delivery.

The governing system-of-record notice authorizes operational paradata including
audit trails, GPS information, IP addresses and mobile-device identifiers. That
is system authority, not proof that every field is collected in every encounter.

The sample invitation says Census may use recent government records and other
data for nonresponding households. [Sample invitation](https://www.census.gov/content/dam/Census/newsroom/press-kits/decennial/2030/2026-census-test/26ct-sample-invitation-letter.pdf)
The narrowed design nevertheless removed the planned experiment that would
have changed administrative-record enumeration. Those two facts should not be
collapsed.

## 5. The signed but unpublished Interagency Agreement

The final Census response to PRA comments says Census and USPS developed an
Interagency Agreement defining legal authority, roles, operational procedures,
organizational capacities and safeguards.

That is material because a proposed 2018 postal-enumerator pilot was canceled
after Census and USPS failed to reconcile Title 13 with Titles 18 and 39 and did
not execute the necessary agreement. [2018 pilot report](https://www2.census.gov/programs-surveys/decennial/2020/program-management/final-analysis-reports/2020-report-postal-carriers-census-enumerators-pilot.pdf)

No executed 2026 IAA or attachments were located in the public OMB package or
on the reached Census, Commerce, USPS, USPS OIG, SAM.gov or USAspending
surfaces. The public record therefore does not disclose:

- reimbursable amount and billing method;
- case, route and task ownership;
- custody of response data and operational metadata;
- device-loss and security-incident procedures;
- agency audit rights;
- retention and deletion duties by record class;
- USPS route/workload data transferred to Census;
- labor-management terms;
- termination, correction and dispute procedures; or
- restrictions beyond the public Title 13 controls.

## 6. Privacy, access and retention

The governing public notice is
[COMMERCE/CENSUS-5](https://www.commerce.gov/opog/privacy-privacy-act/system-records-notices/system-records-notices-commerce-census-5).

It establishes:

- Census ownership and management of the system;
- coverage of decennial tests, field-worker records and operational paradata;
- possible supplementation by administrative records governed under CENSUS-8;
- no routine uses;
- access limited to Census employees and Title 13 Special Sworn personnel;
- encryption, access control, audit, training and FISMA-aligned safeguards; and
- destruction of pilot/cognitive-test records when two years old or when no
  longer needed for program/evaluation purposes, whichever is later.

The no-routine-use clause does not supply a path to release identifiable test
responses to DHS, ICE, election officials or benefits agencies. Postal workers
access the operation through Census appointment or Special Sworn Status, not an
ordinary postal entitlement to Census responses.

The public SORN does not resolve whether USPS retains separate operational
metadata such as hours, route impact or delivery disruption. That remains an
IAA and records-schedule question.

## 7. USPS address infrastructure: baseline, not pilot proof

Census's Master Address File and TIGER geography are maintained through the
Geographic Support Program. The USPS Delivery Sequence File is a longstanding
recurring input and contains address, ZIP Code, route, delivery sequence and
delivery-type information. Census also uses undeliverable-as-addressed codes in
some operations and has used NCOA-derived information in separate programs and
research.

Primary background:

- [Census Address Maintenance Strategy](https://www2.census.gov/geo/pdfs/gsp/Geographic_Support_Program-AMS.pdf)
- [2020 Address Canvassing operational plan](https://www2.census.gov/programs-surveys/decennial/2020/program-management/planning-docs/ADC_detailed_operational_plan_v2.0.pdf)
- [ACS frame methodology](https://www.census.gov/content/dam/Census/library/publications/2010/acs/acs_design_methodology_ch03.pdf)

No final 2026-test document publicly identifies:

- the MAF/TIGER extract used at the two sites;
- the DSF refresh date;
- any NCOA use in sampling, contact, routing or evaluation;
- whether carrier observations update MAF/TIGER;
- the route-to-Census-case matching specification;
- whether delivery metadata appear on field devices; or
- whether carrier knowledge of vacancies, hidden units or household occupancy
  becomes a structured Census input.

Longstanding DSF-to-MAF integration proves institutional adjacency. It does not
prove that the 2026 test uses NCOA, citizenship or immigration records.

## 8. Cost claim and 2030 gates

The approved PRA estimate is $5 million for Census and USPS enumerators,
supervisors, devices, printing, postage and telephone costs. It excludes IT
development and headquarters support and is therefore not a full-cost measure.

Census declined to estimate savings before the test because cost and
productivity are test outputs. The Secretary's August 11 claim that postal
expertise will save taxpayers billions has no quantified support in the post or
the located pilot paperwork.

Decision sequence:

```text
2026 field test
  -> analysis of feasibility, cost, quality and mail disruption
  -> summer 2027 Operational Plan Baseline 2
  -> 2028 Dress Rehearsal
  -> March 30, 2028 proposed-question submission to Congress
  -> summer 2029 Baseline 3
  -> 2030 production census
```

The 2026 test is therefore consequential as a design gate. It is not itself an
official count, population product, apportionment number or immigration action.
