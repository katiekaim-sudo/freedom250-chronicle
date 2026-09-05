# Congressional Committees — Activity and Cross-Committee Synthesis

Evidence cutoff: 2026-07-26  
Artifact state: finished workbench research; not promoted to the live vault  
Scope: current 119th-Congress committee structure plus the official-source
activity, action, object, outcome, and monitor records admitted by the
Congressional Committee Control Plane

## Bottom line

The committee layer does not show one consolidated congressional control
plane. It shows separate institutional gates through which durable objects
move: bills, nominations, reports, subpoenas, requests, transcripts,
authorizations, and implementation products.

The strongest current findings are:

1. **Publication is the dominant proved output.** The mapped committees are
   producing hearings, transcripts, reports, drafts, and evidentiary records
   faster than the current corpus proves downstream legal or operating effects.
2. **Dollar plumbing is the cleanest multi-committee legislative story.**
   H.R. 3633 has exact House Agriculture, House Financial Services, and Senate
   Banking states. The Senate Agriculture/Banking EHF26654 product remains a
   separate public-draft object, not a completed four-committee legislative
   chain.
3. **Fraud control is converging on an identity-to-payment architecture.**
   House Oversight, HSGAC, Treasury, GAO, program-integrity systems, and
   anti-fraud bills occupy a coherent factual field. The graph does not yet
   prove one binding, government-wide operating object.
4. **Intelligence oversight is two systems at once:** a mostly closed recurring
   briefing system and a publicly auditable personnel/authorization system.
   PN711 is the cleanest exact cross-committee personnel chain.
5. **Oversight activity is not oversight effect.** Three exact request chains
   currently prove issuance and source checks, but no recipient response,
   compliance, request-caused action, or measured effect.

This is a strong foundation, not a complete activity census. Structural
coverage is complete for all current bodies; normalized public-event scanning
is not.

## What the project now contains

| Layer | Current admitted state | What it means |
|---|---:|---|
| Current top-level bodies | 46 | House, Senate, and permanent joint bodies |
| Current subcommittees | 180 | Variable-depth structural census |
| Function records | 226 | One for every current body |
| Normalized proceedings | 263 | Available-corpus event baseline |
| Source objects | 545 | Event pages, transcripts, materials, result objects, and other official sources |
| Committee actions | 132 | Exact action records from the mapped corpus |
| Durable objects | 417 | Bills, nominations, reports, agencies, requests, programs, and other stable objects |
| Factual relationships | 1,149 | Event, source, committee-role, action, and object edges |
| Verified outcomes | 242 | Exact state changes with separated clocks |
| Factual monitors | 156 | Object-specific later-state questions and official routes |

The activity registry marks 16 bodies `scanned` and 210 `not_scanned`. This is a
normalization boundary, not a public-source discovery boundary. The separate
House Repository discovery lane found 1,179 unique EventIDs across 117 current
House bodies. The Senate archive lane found 945 official archive rows across
20 top-level Senate adapters, plus the separately maintained 77-row SSCI
registry before cross-registry deduplication. Discovery proves that a listing
exists; it does not by itself prove occurrence, action, publication, or result.

The Layer-1 census is also structurally complete but uneven in substantive
depth. Of 226 function records, 223 carry an explicit gap, 174 have no
body-specific jurisdiction text, 104 have no functions, and 106 have no
powers. One hundred four of 110 House subcommittees have all three fields
empty. All 70 Senate subcommittees lack body-specific jurisdiction text,
although generic function and power language is present. These are official-
rules retrieval gaps, not permission to infer jurisdiction from a title.

## What the committees are doing

### 1. Producing the institutional record

The 263 normalized proceeding rows contain:

- 152 hearings, including eight nomination hearings and two open oversight
  hearings;
- 66 closed briefings;
- 21 markup, business, or organizational meetings;
- 18 roundtables;
- one deposition; and
- five rows whose current occurrence state is scheduled, postponed, or
  not-occurred rather than occurred.

The 132 admitted actions are even more publication-heavy:

- 94 transcript or declassification releases;
- 25 legislative consideration or reporting actions;
- four committee-governance actions;
- two letters or document requests;
- two subpoenas;
- two report, finding, or referral actions;
- one nomination batch;
- one GAO review request; and
- one task-force or working-group action.

The 242 verified outcomes preserve the same shape:

- 99 publication or declassification outcomes;
- 86 legislative state changes;
- 48 nomination state changes; and
- nine oversight or investigation outcomes.

The downstream tail is narrow: one effective clock, one implementation-start
clock, no operation clocks, and no measured-effect outcomes. Publication is
real work, but it is not enactment, compliance, implementation, operation, or
effect.

### 2. Running a high-volume House process layer

The broad House Repository discovery pass—not the narrower normalized event
registry—shows the largest current listing counts under:

| Body | Discovery listings |
|---|---:|
| House Rules | 48 |
| House Financial Services | 48 |
| House Small Business | 30 |
| House Foreign Affairs | 30 |
| House Ways and Means | 29 |
| House Judiciary | 27 |
| House Armed Services | 26 |
| Energy and Commerce — Energy | 23 |
| House Oversight | 23 |
| House Administration | 22 |

These are calendar/discovery counts, not activity or consequence rankings.
They are useful for deciding where the next normalization wave should go.

### 3. Building dollar, token, and market-structure law through multiple gates

The cleanest multi-committee legislative object is H.R. 3633:

- object: `congress.119.hr3633`;
- monitor: `monitor.object.4ee8074d7c7a72`;
- exact committee chain: `house.ag00`, `house.ba00`, and `senate.ssbk`;
- current proved state: House passage plus later Senate committee activity;
- not proved: full Senate passage, bicameral agreement, enactment, or
  implementation.

The July 22 EHF26654 product is a separate object:

- monitor: `monitor.object.1539c279d54b62`;
- outcome:
  `outcome.congress-119-draft-ehf26654.released.2026-07-22`;
- proved state: public discussion-draft release with Senate Banking and Senate
  Agriculture authority;
- not proved: formal filing, amendment identity, floor action, enactment, or
  effectiveness.

The “four-committee assembly line” is therefore a sound synthesis of parallel
institutional work. The current graph does not yet contain one completed
four-body legal chain.

### 4. Using Congressional Review Act machinery against digital-asset tax reporting

House Ways and Means supplies the only committee-attributed chain in the
current outcome registry that reaches an effective clock:

- object: `congress.119.hjres25`;
- subject: disapproval of Treasury's digital-asset broker gross-proceeds
  reporting rule;
- committee markup and ordered reporting: 2025-02-26;
- H. Rept. 119-7 publication: 2025-02-28;
- House passage: 2025-03-11;
- Senate passage and both-chambers state: 2025-03-26;
- presentation: 2025-04-01; and
- signature, enactment, and effectiveness: 2025-04-10.

The resolution and H. Rept. 119-7 are separate durable objects. Report
publication does not itself supply the resolution's legal state.

### 5. Turning fraud control into an identity-to-payment architecture

The House Oversight record supplies the densest existing factual sequence:

1. identity and eligibility checks;
2. prevention before payment;
3. Do Not Pay, PRAC, and analytic-network use;
4. Treasury or agency payment barriers;
5. state-administered-program controls;
6. continuous monitoring; and
7. correction, appeal, surveillance, and due-process objections.

Four House-passed objects are especially important:

- H.R. 8312 — `monitor.object.e8dff1d9691664`;
- H.R. 8463 — `monitor.object.0a92d8b7e1a2c7`;
- H.R. 8464 — `monitor.object.0e1ef8119263cb`; and
- H.R. 8467 — `monitor.object.28103851575291`.

The evidence supports a common architecture question. It does not yet support
a claim that these measures became one enacted, effective, or operating
government-wide system. HSGAC's fraud work is a verified parallel lane, but
the relationship registry does not yet join House Oversight and HSGAC to one
shared durable fraud-system object.

The follow-on official-source audit sharpens that boundary:

- all four bills remain House-passed and Senate-received, not enacted;
- H.R. 8464's Senate analogue, S. 4747, remains referred to HSGAC;
- Executive Order 14395 created exact 30-, 60-, and 90-day agency and task-force
  deadlines, but no public copies or redacted summaries of those deliverables
  were located in the bounded official-source search;
- Fraud.gov has an effective Treasury records system and an active emergency
  OIRA-cleared intake form through 2026-11-30;
- Treasury is operating a death-payment screening and return-for-review
  control, but its reported $99 million is neither a proved recovery nor a
  proved permanent prevention amount;
- Do Not Pay is operational, with record correction still owned by source
  agencies rather than one unified appeal system;
- GSA has effective data-sharing authority for specified systems, which is not
  proof that every authorized dataset was transferred or used; and
- PRAC remains operational through 2034-09-30 within its statutory
  jurisdiction, not as the universal permanent body proposed by H.R. 8312.

The proved architecture is therefore federated and component-level:
`intake -> data authority -> screening/matching -> source-agency review ->
investigation/referral`. A public government-wide chain from flag through
notice, correction, appeal, final payment decision, recovery, and measured
error is still missing.

### 6. Staffing and supervising the intelligence system

The normalized intelligence cluster contains 111 occurred rows across SSCI and
the House intelligence family. Ninety-three are closed, sixteen open, and two
do not state visibility. A generic closed `Intelligence Matters` page proves
the proceeding clock and place, not its topic, witnesses, evidence, or result.

The cleanest exact shared-object chain is PN711:

- object: `nomination.119.pn711.joshua-m-rudd.army-general`;
- monitor: `monitor.object.de67161de4ab7e`;
- committees: Senate Armed Services and SSCI;
- verified stages: referral, hearings, favorable reporting, Senate
  confirmation, Army general date of rank, and entry into the combined
  NSA/CYBERCOM/CSS role;
- unresolved stage: an exact public appointment, commission, execution order,
  oath, or ceremony instrument.

The wider HPSCI/SSCI adjacency to Armed Services, Appropriations—Defense,
Judiciary, Homeland/HSGAC, Foreign Affairs, Oversight, CCP, and financial
committees remains a jurisdiction map. It is not proof that all of those bodies
acted on one intelligence object.

The follow-on authorization audit resolves the FY2027 candidate into two
different legislative objects:

- H.R. 9624 was introduced on 2026-07-09 and passed out of HPSCI after a closed
  2026-07-20 markup, but no public reported composite, House report, floor
  passage, conference, enrolled, or public-law object was located by cutoff.
- S. 4615 was reported by SSCI and placed on the Senate calendar on
  2026-05-20, but no Senate floor passage or later bicameral state was located.
- the public authorization shells differ by $23 million in their visible
  Intelligence Community Management Account figures. That is a text
  divergence, not an appropriation divergence; neither object supplies budget
  authority.

The July 16 House amendment in the nature of a substitute contains a real
proposed OSINT package: future budget-justification detail, an interagency
framework, a possible common dissemination service, instruction/reporting
updates, capability-gap assessments, and a whole-of-government support study.
Because no public reported composite is available, those provisions remain
contained in the ANS rather than proved as final committee-reported text,
enacted authority, appropriation, or operation.

Independent operating evidence predates the bill: the HPSCI OSINT
Subcommittee, Public Law 118-159's IC-element budget-summary requirement, the
IC OSINT Strategy 2024–2026, DoDI 3115.12, DIA's OSINT Integration Center, and
the ODNI solicitation for an IC Data Consortium. These prove oversight,
existing governance, or procurement-stage machinery at their exact states.
They do not prove the FY2027 package is law or that a consolidated production
capability is operating.

The PN711 instrument watch remains correctly open. Confirmation, Army general
date of rank, and assumption of the combined role strongly establish that the
personnel transition occurred; no public signed presidential appointment or
commission, departmental execution order, oath certificate, or ceremony
instrument was located.

### 7. Creating investigative and declassification records

House Oversight is also functioning as a record-production and disclosure hub:
JFK, MLK, UAP, MKULTRA, and Epstein-related hearings, interviews, transcripts,
reports, and subpoenas are preserved as distinct objects.

The correct chain is:

`proceeding -> testimony/exhibit -> transcript/report publication -> committee
action -> later legal or institutional result`

No link may be skipped. A released transcript proves publication and content
availability. It does not by itself prove the truth of the testimony, a
committee finding, criminal liability, enforcement, or remediation.

### 8. Publishing technical law outside the hearing count

The permanent Joint Committee on Taxation is a hidden publication factory:
102 durable publication objects are represented even though this work is not
visible as a comparable event count. The relationship graph records
publication roles and seven exact legal-reference edges. It does not infer
adoption, legal effect, implementation, or policy outcome from publication
alone.

This is an important design lesson: committee work cannot be measured from
hearing calendars alone.

## Exact shared-object convergence versus thematic convergence

Only two current factual monitors contain more than one committee ID:

| Shared object | Exact committee chain | Current evidentiary meaning |
|---|---|---|
| H.R. 3633 | House Agriculture; House Financial Services; Senate Banking | Multi-gate monetary legislation with later states still open |
| PN711 | Senate Armed Services; SSCI | Military-grade nomination plus intelligence-role chain |

The following are strong thematic or parallel-record stories, but not yet
single shared-object chains:

- House Oversight + HSGAC fraud and payment integrity;
- intelligence authorization across HPSCI, SSCI, Armed Services, and
  Appropriations—Defense;
- national-security economic infrastructure across Armed Services, Foreign
  Affairs, CCP, financial committees, and appropriators; and
- Treasury, GAO, Federal Reserve, and financial-regulator oversight.

Those stories remain worth following. They must be promoted by exact object
identity, not by similar subject labels.

## Current watchdog-without-outcome chains

Three exact monitors have been checked against eighteen official surfaces:

| Monitor | Proved state | Still unproved |
|---|---|---|
| `monitor.object.52f99a98bb4972` — HFSC/Kraken account inquiry | March 26 request; April 10 response date | acknowledgment, response, compliance, request-caused account change, measured effect |
| `monitor.object.96985565035c91` — Senate Banking Treasury/DOGE inquiry | July 21 request; August 4 response date | response, access-control change, implementation, effect |
| `monitor.object.42242d5b66dcd7` — Senate Banking GAO/CFTC staffing request | July 22 request | GAO acceptance, engagement ID, product, CFTC remediation, effect |

The Kansas City Fed's March 4 Kraken account approval predates the March 26
request and cannot be its response or effect. A missed deadline or silence is
also not affirmative proof of nonresponse.

## Coverage and QA findings

### Coverage bias

The 99-artifact existing corpus is concentrated in House Oversight, House
Financial Services, Senate Banking, SSCI, and HPSCI. The 16 scanned-body event
baseline therefore cannot support a ranking of all 226 bodies by importance,
activity, or effect.

The concentration is measurable: the House Oversight, House Financial
Services, HPSCI, and SSCI families account for 258 of 263 normalized event
rows. Only 24 bodies have any normalized event row. Fifteen of the 16
fully-scanned bodies belong to the House Oversight or HPSCI families; SSCI is
the only fully-scanned Senate body.

The broad discovery passes partly reduce this blind spot, but discovery rows
still require occurrence, action, source-object, and outcome normalization.
`not_scanned` means unknown, not inactive.

### Cross-layer current-state repair

The first synthesis pass found four semantic lags. The follow-on repair wave
now resolves all four without collapsing event, action, result, publication,
effective, implementation, operation, or effect clocks:

1. `congress.119.s875` now carries the verified legislative
   `ordered_reported` state dated 2025-03-13.
2. `congress.119.hjres25` now carries the verified legislative
   `passed_both_chambers` state dated 2025-03-26 and legal `effective` state
   dated 2025-04-10, while preserving the intervening exact clocks.
3. `congress.119.hr2392` now carries the verified legislative `reported`
   state dated 2025-05-06.
4. event `house-119492` now carries `occurred` at
   `2026-07-22T10:00:00-04:00`; the linked action and result clocks remain
   separate.

`build_committee_semantic_state_repair.py` generates the object enrichments.
`build_committee_activity_registry.py` now admits exact event enrichments.
`validate_committee_package.py` now fails if a merged object retains
`not_publicly_resolved` after a verified later state, or if an exact outcome
points to an event that still has a non-occurred state. The full deterministic
integration passes with `errors=0`.

### Documentation repair

The three human-facing documentation lags found during the first synthesis
pass are also repaired:

- `COMMITTEE_RESEARCH_STATUS_2026-07-26.md` now reports 545 source objects;
  427 remains correctly identified as the `event_produced_source`
  relationship count.
- The package README now records 141 admitted `action_affected_object` edges
  and preserves unresolved joins as explicit queues.
- `COMMITTEE_FINAL_RESIDUAL_AUDIT_2026-07-26.md` is labeled as a historical
  pre-repair audit and points to the controlling final handoff and follow-on
  deep dive.

## Ranked next research wave

### P0 — live object and response clocks

1. **H.R. 3633 / EHF26654:** retrieve the next exact Senate parliamentary
   object—formal text, proposer, amendment tree, committee/floor action, or
   bicameral resolution. Another discussion draft is not advancement.
2. **Treasury/DOGE:** check the exact August 4 response route; require an
   official request-linked response before changing state.
3. **GAO/CFTC staffing:** require GAO acceptance, an engagement ID, or a
   resulting GAO product; keep later CFTC action causally separate.
4. **FY2027 intelligence authorization:** follow exact bill, report, markup,
   chamber, conference, enactment, and declassification objects.
5. **Semantic repair:** completed in the follow-on wave; retain the new
   validator gates as permanent regression controls.

### P1 — test the strongest project hypotheses

6. **Fraud machine operating proof:** retrieve EO 14395 deliverables, Senate
   states for H.R. 8312/8463/8464/8467, binding data-sharing instruments,
   appeal/correction rules, agency operation records, and measured effects.
7. **CFTC authority versus capacity:** separate authorization, appropriation,
   staffing, technology, examination, and SRO-delegation objects.
8. **HPSCI OSINT:** require a hearing, report, legal provision, appropriation,
   agency reorganization, procurement, or implementation record. A
   subcommittee announcement alone is not operational state.
9. **PN711 instrument:** continue the exact appointment/commission/oath watch;
   confirmation and office entry do not supply the missing instrument.
10. **National-security economic infrastructure:** test exact shared bills,
    reports, authorizations, sanctions objects, programs, projects, or
    appropriations. Multiple committees saying `China`, `supply chains`, or
    `national security` is not an object join.

### P2 — reduce structural coverage bias

Normalize the highest-value currently broad-discovery bodies next:

- House Rules;
- House Armed Services and Appropriations—Defense;
- House Judiciary;
- House Foreign Affairs;
- House CCP;
- House Ways and Means;
- House Energy and Commerce;
- Senate Judiciary;
- Senate Armed Services;
- Senate Commerce;
- Senate Foreign Relations;
- Senate Appropriations; and
- Senate HELP.

Priority should follow exact intersections with current vault objects, not a
quota and not a presumption that the largest calendar count is the most
important story.

## Principal evidence

- `COMMITTEE_FOUNDATION_FINAL_HANDOFF_2026-07-26.md`
- `COMMITTEE_RESEARCH_STATUS_2026-07-26.md`
- `COMMITTEE_ACTIVITY_EVENT_REGISTRY_119TH.json`
- `COMMITTEE_ACTIVITY_ACTION_REGISTRY.json`
- `COMMITTEE_DURABLE_OBJECT_REGISTRY.json`
- `COMMITTEE_OBJECT_RELATIONSHIP_REGISTRY.json`
- `COMMITTEE_OUTCOME_REGISTRY.json`
- `COMMITTEE_STORY_MONITOR_REGISTRY.json`
- `house_repository_daily_discovery_119th.json`
- `senate_committee_archive_discovery_119th.json`
- live vault `02 - Research/Congressional Monetary Infrastructure/Cross-Committee Map.md`
- live vault `04 - Synthesis/The Fraud Machine — Identity, Eligibility, and the Payment Gate.md`
