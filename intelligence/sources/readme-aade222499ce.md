# Congressional Committee Control Plane

Status: active workbench package  
Evidence cutoff: 2026-07-26  
Scope: 119th Congress committee structure, jurisdictional relationships, official proceedings, and story monitoring

## Read first

This package adds a distinct congressional-committee layer to the Freedom 250
entity model. It does **not** treat committees as executive subsidiaries and it
does not assign SFFAS 47 consolidation states to them.

Every current committee and subcommittee appears as a node. Depth is
informational, not standardized: each body receives the structure, event
records, sources, and relationships supported by its verified public record.
Sparse public disclosure remains sparse; a large evidentiary record is allowed
to become large. No body is compressed or expanded to make the tree visually
symmetrical, and no storyline is a prerequisite for inclusion.

## Package map

- COMMITTEE_RESEARCH_EXECUTION_PLAN.md — canonical five-layer operating plan,
  agent model, merge gates, and completion standard.
- `COMMITTEE_RESEARCH_STATUS_2026-07-28.md` — current exact post-Wave-4 state,
  integrity repair, bounded backlogs and resume order.
- `COMMITTEE_RESEARCH_STATUS_2026-07-26.md` — historical exact completion and
  gap snapshot from before the Wave-4 money-cluster merge.
- `COMMITTEE_FINAL_RESIDUAL_AUDIT_2026-07-26.md` — historical pre-repair
  independent semantic audit and exact remediation map for stale lower-layer
  queues, false objects/edges, finite retrieval work, continuing watches, and
  completion criteria.
- `COMMITTEE_FOUNDATION_FINAL_HANDOFF_2026-07-26.md` — final merged counts,
  evidence-chain rulings, integrity repair, continuing-watch boundary,
  deterministic hashes, and validation result.
- `COMMITTEE_ACTIVITY_SYNTHESIS_2026-07-26.md` — merged read-only analysis of
  what the mapped committees are doing, exact shared-object versus thematic
  convergence, effect boundaries, coverage bias, semantic QA repair, and the
  ranked next research wave.
- `COMMITTEE_OBJECT_DEEP_DIVE_WAVE1_2026-07-26.md` — source-bearing merged
  analysis of the digital-asset market-structure, fraud/payment-control, and
  intelligence/OSINT lanes, including exact object states, negative findings,
  triggers, falsifiers, and vault-story mapping.
- `HOUSE_AGRICULTURE_EVENT_118098_ON_CHAIN_TOOLS_ANALYSIS_2026-07-27.md` —
  formal-transcript analysis of the April 9, 2025 House Agriculture
  on-chain-tools hearing, separating committee framing, member statements,
  witness testimony, procedural action, later bill states, negative findings,
  and exact next-source questions.
- `HOUSE_AGRICULTURE_EVENT_118038_CFTC_AT_50_ANALYSIS_2026-07-27.md` -
  formal-transcript analysis of the March 25, 2025 House Agriculture CFTC
  anniversary hearing, separating framing, member and witness speech,
  procedural actions, durable-object boundaries, later CFTC resource states,
  observed effects, exact gaps, and next-source questions.
- `HPSCI_EVENT_119456_EVIDENCE_STATE_ANALYSIS_2026-07-27.md` —
  formal-transcript and evidence-state analysis of *States on the Frontlines
  of Counterintelligence*, separating committee framing, member speech, five
  witness testimony lanes, Q&A contradictions, state/federal objects, exact
  transcript publication, legal-state gaps, and non-effects.
- `JULY_14_17_PROCEEDINGS_STAGING_RECONCILIATION_2026-07-27.md` — exact
  six-proceeding vault-landing record for the House and Senate Fed and CFPB
  hearings, HSGAC fraud hearing, and HFSC CLARITY field hearing. All six source
  folders, provenance-labelled transcripts, and factual event notes landed in
  the live vault on July 27 EDT; central admission of the local provenance
  locators remains separate.
- `_Working/Congressional Committee Control Plane Vault Patch 2026-07-28/`
  (from the workbench root) — incorporated June 12 Fed-structure source-folder
  memo and vault landing handoff. The memo, corrected transcript path, Benjamin
  Keen spelling, and spent open-item repair landed in the live vault.
- `COMMITTEE_OBJECT_BRIDGE_WAVE2_HANDOFF_2026-07-26.md` — merged Wave-2
  canonicalization of the intelligence-authorization, fraud/payment-control,
  and CFTC authority/funding/staffing lanes: 12 objects, one HPSCI action, 14
  factual relationships, 14 bounded outcomes, exact non-promotions, validation,
  hashes, and live-chart injection state.
- `build_committee_wave2_object_bridge.py` and
  `validate_committee_wave2_object_bridge.py` — deterministic Wave-2 lane
  builder and strict boundary validator; the bridge retires the HPSCI markup
  action gap and generic FY2027 IAA candidate without inferring reported text,
  enactment, data transfer, automatic payment stops, or measured savings.
- `RESPONSE_EFFECT_CLOSEOUT_WAVE3_HANDOFF_2026-07-26.md` — source-bearing
  closeout for the Kansas City Fed, Treasury, and GAO chains; preserves zero
  admitted responses/effects and the Treasury letter's August 4, 2026 due date.
- `layer4_review_lanes/RUDD_APPOINTMENT_INSTRUMENT_WATCH_HANDOFF_2026-07-26.md`
  — nine-surface negative-source audit separating confirmation, grade date,
  appointment/commission/oath, and office entry.
- `build_committee_lower_layer_integrity_repair.py` and
  `validate_committee_lower_layer_integrity_repair.py` — exact controls for
  three stale action gaps, one false object, five stale/final-disposition
  object candidates, two false relationships, 26 replacement edges, and 105
  stale relationship candidates.
- `build_committee_final_closeout.py` and
  `validate_committee_final_integration.py` — administrative watch retirement,
  two-pass deterministic rebuild, semantic queue checks, and final exact-count
  validation without fabricating an outcome.
- `build_committee_semantic_state_repair.py`,
  `layer2_lanes/final_semantic_status_repair_activity_event_inventory.json`,
  and
  `layer3_lanes/final_semantic_status_repair_object_inventory.json` — generated
  cross-layer repair for fifteen stale durable-object states and one stale event
  state, with later verified outcomes preserved at their own exact clocks.
- `COMMITTEE_EXISTING_CORPUS_AUDIT.md` — Layer-0 map of prior committee work,
  beginning with Financial Services, monetary, oversight, fraud, and
  intelligence material.
- `COMMITTEE_EXISTING_CORPUS_REGISTRY.json` — merged machine-readable Layer-0
  artifact crosswalk, built from `layer0_lanes/`.
- `COMMITTEE_FUNCTION_SCHEMA.json` and
  `COMMITTEE_FUNCTION_REGISTRY_119TH.json` — Layer-1 institutional-function
  contract and complete body census.
- `COMMITTEE_ACTIVITY_EVENT_SCHEMA.json` and
  `COMMITTEE_ACTIVITY_EVENT_REGISTRY_119TH.json` — Layer-2 public-event contract
  and available-corpus House/Senate/joint event baseline with exact coverage
  states for every body.
- `COMMITTEE_ACTIVITY_ACTION_SCHEMA.json` and
  `COMMITTEE_ACTIVITY_ACTION_REGISTRY.json` — Layer-2 official-action contract
  and available existing-corpus action baseline; proceedings and later
  outcomes remain separate.
- `COMMITTEE_SOURCE_OBJECT_SCHEMA.json` and
  `COMMITTEE_SOURCE_OBJECT_REGISTRY_119TH.json` — deduplicated Layer-2 evidence
  objects for event pages, videos, transcripts, captions, and written
  materials; aggregate material counts without item locators remain gaps.
- `COMMITTEE_DURABLE_OBJECT_SCHEMA.json` and
  `COMMITTEE_OBJECT_RELATIONSHIP_SCHEMA.json` — Layer-3 contracts for canonical
  research objects, separated object clocks and status dimensions, exact
  evidence locators, and factual committee/event/action/object relationships.
- `COMMITTEE_DURABLE_OBJECT_REGISTRY.json` — merged available-corpus Layer-3
  object baseline; unresolved official-source and external-entity joins remain
  visible queues.
- `COMMITTEE_OBJECT_RELATIONSHIP_REGISTRY.json` — merged factual Layer-3
  event/committee/source/action/object relationship baseline, including 142
  admitted `action_affected_object` edges; unresolved and withheld joins remain
  explicit queues.
- `COMMITTEE_ENTITY_VIEW_REGISTRY_119TH.json` — chart-facing variable-depth
  join of every current body with its function, activity, action, evidence,
  durable-object, existing-corpus, and gap routes; House bodies also carry
  their complete Repository discovery listings, detail-retrieval state, and
  exact/candidate/unresolved cross-registry identity states,
  Senate bodies carry their official archive discoveries, and permanent joint
  bodies keep proceedings separate from publications. Linked bodies also carry
  their complete factual story monitors, open questions, checked response/effect
  routes, evidence gates, and non-triggers.
- `COMMITTEE_OUTCOME_SCHEMA.json` and
  `COMMITTEE_OUTCOME_CLAIM_REVIEW_SCHEMA.json` — Layer-4 verification
  contracts for results and observed effects across legislation, nominations,
  authorization/appropriation, oversight/investigation,
  publication/declassification, and program/agency effects. They require exact
  official locators, separate action/result/publication/effective/
  implementation/operation clocks, institutional-voice classification, and
  explicit authority-conflict review.
- `COMMITTEE_OUTCOME_REGISTRY.json` — independently verified Layer-4 outcomes
  plus the remaining unresolved/rejected candidate queue.
- `COMMITTEE_OUTCOME_CLAIM_REVIEW_REGISTRY.json` — merged audit trail preserving
  each original claim, exact claim context, official evidence, identity,
  institutional-voice, six-clock, scope, and outcome-chain rulings, corrected
  narrow claim, and verified-outcome link where one exists.
- `COMMITTEE_STORY_MONITOR_SCHEMA.json` and
  `COMMITTEE_STORY_MONITOR_REGISTRY.json` — Layer-5 factual follow-through
  contract and deterministic variable-depth monitor set. Each monitor preserves
  the current verified state, open downstream questions, exact promotion
  evidence, non-triggers, official source surfaces, and distinct clock roles;
  it is not an interpretive storyline or an outcome assertion.
- `layer4_lanes/house_legislation_wave1_outcome_inventory.json` — bounded House
  legislation lane with 70 separately verified committee, reporting, chamber,
  presentation, enactment, and effectiveness outcomes across 17 measures; it
  resolves 17 original candidate IDs without collapsing later clocks.
- `layer4_review_lanes/house_legislation_wave1_claim_review_inventory.json` —
  18 machine-readable reviews for the original House legislation claims,
  including the preserved wrong-object review for H. Rept. 119-7.
- `HOUSE_LEGISLATION_WAVE1_OUTCOME_HANDOFF_2026-07-26.md`,
  `build_house_legislation_wave1_outcomes.py`, and
  `validate_house_legislation_wave1_outcomes.py` — reproducible builder,
  strict lane validator, source boundary, counts, and merge-neutral handoff
  for the bounded House wave.
- `layer4_lanes/senate_legislation_nomination_outcome_inventory.json` and
  `layer4_review_lanes/senate_legislation_nomination_claim_review_inventory.json`
  — bounded Senate result lane with 21 exact outcomes and 18 Senate-owned candidate reviews;
  committee reporting and full-Senate confirmation remain separate, while
  appointment and entry into office remain unresolved unless separately
  sourced.
- `layer4_lanes/build_senate_legislation_nomination_outcomes.py`,
  `layer4_lanes/validate_senate_legislation_nomination_outcomes.py`, and
  `layer4_lanes/SENATE_LEGISLATION_NOMINATION_OUTCOME_HANDOFF_2026-07-26.md`
  — reproducible builder, strict validator, and merge-neutral handoff for that
  Senate lane.
- `layer4_lanes/legislation_wave2_outcome_inventory.json`,
  `layer4_review_lanes/legislation_wave2_claim_review_inventory.json`,
  `build_legislation_wave2_outcomes.py`,
  `validate_legislation_wave2_outcomes.py`, and
  `LEGISLATION_WAVE2_OUTCOME_HANDOFF_2026-07-26.md` — second exact legislative
  wave with 11 state changes across H.R. 3633, S. 1582, and S. 4802. It resolves
  two original candidates; its then-explicit March 13 vehicle conflict is
  corrected to S. 919 by Wave 3,
  and supersedes three earlier provisional Senate reviews without duplicating
  the canonical House H. Rept. 119-7 review.
- `layer3_lanes/senate_nomination_wave2_object_inventory.json`,
  `layer4_lanes/senate_nomination_wave2_outcome_inventory.json`,
  `layer4_review_lanes/senate_nomination_wave2_claim_review_inventory.json`,
  and the companion builder, validator, and handoff — 17 exact HSGAC nomination
  objects plus 20 nominee-specific committee-report outcomes across the HSGAC
  and SSCI lanes. Hearing, report, confirmation, appointment, and office entry
  remain separate; the then-unresolved Rudd role/PN object conflict is resolved
  by the Wave-3 PN711 lane.
- `layer2_source_object_lanes/oversight_publication_wave2_source_object_inventory.json`,
  `layer3_lanes/oversight_publication_wave2_object_inventory.json`,
  `layer4_lanes/oversight_publication_wave2_outcome_inventory.json`,
  `layer4_review_lanes/oversight_publication_wave2_claim_review_inventory.json`,
  and `layer4_watch_lanes/oversight_publication_wave2_monitor_routes.json` —
  exact Wave-2 publication and follow-through lane with five durable transcript
  or report objects, nine release/report/service outcomes, seven current
  claim reviews, and three checked response/effect routes. No response,
  compliance, enforcement, or remedial-effect outcome is inferred.
- `layer2_source_object_lanes/legislation_wave3_source_object_inventory.json`,
  `layer2_lanes/legislation_wave3_committee_action_inventory.json`,
  `layer3_lanes/legislation_wave3_object_inventory.json`,
  `layer3_lanes/legislation_wave3_relationship_inventory.json`,
  `layer4_lanes/legislation_wave3_outcome_inventory.json`,
  `layer4_review_lanes/legislation_wave3_claim_review_inventory.json`,
  `build_legislation_wave3_residuals.py`,
  `validate_legislation_wave3_residuals.py`, and
  `LEGISLATION_WAVE3_RESIDUAL_HANDOFF_2026-07-26.md` — exact resolution of
  both legislative residuals. H. Rept. 119-7 is the publication accompanying
  H.J. Res. 25; S. 919 is the March 13, 2025 GENIUS vehicle. The lane uses
  explicit action/object/relationship enrichments and removals so corrected
  central state does not duplicate or silently overwrite history.
- `layer3_lanes/senate_nomination_wave3_rudd_object_inventory.json`,
  `layer4_lanes/senate_nomination_wave3_rudd_outcome_inventory.json`,
  `layer4_review_lanes/senate_nomination_wave3_rudd_claim_review_inventory.json`,
  and the companion builder, validator, and handoff — exact PN711 lifecycle
  from receipt through March 20 office entry. PN711 remains an Army-grade
  nomination; Director of NSA remains a related office object. No separate
  role-nomination or appointment-instrument outcome is admitted.
- `layer2_source_object_lanes/transcript_publication_wave3_source_object_inventory.json`,
  `layer3_lanes/transcript_publication_wave3_object_inventory.json`,
  `layer3_lanes/transcript_publication_wave3_relationship_inventory.json`,
  `layer4_lanes/transcript_publication_wave3_outcome_inventory.json`,
  `layer4_review_lanes/transcript_publication_wave3_claim_review_inventory.json`,
  `build_transcript_publication_wave3.py`,
  `validate_transcript_publication_wave3.py`, and
  `TRANSCRIPT_PUBLICATION_WAVE3_HANDOFF_2026-07-26.md` — row-level replacement
  for the former aggregate transcript gap: 22 new exact publication objects
  and outcomes, plus 70 preserved residual rows divided into 49 missing-clock
  and 21 missing-locator cases.
- `build_transcript_publication_wave4_clock.py`,
  `validate_transcript_publication_wave4_clock.py`, and
  `TRANSCRIPT_PUBLICATION_WAVE4_CLOCK_HANDOFF_2026-07-26.md` — exact recovery
  of all 49 item-specific House Repository transcript-material `Added`
  timestamps. Eight objects are Congress 118 parent-committee publications;
  no current-event or current-subcommittee edge is manufactured.
- `build_transcript_publication_wave4_locator.py`,
  `validate_transcript_publication_wave4_locator.py`, and
  `layer4_lanes/TRANSCRIPT_PUBLICATION_WAVE4_LOCATOR_HANDOFF_2026-07-26.md` —
  exact GovInfo package recovery for all 15 House and six SSCI missing-locator
  rows. MODS dates are represented narrowly as GovInfo first-documented
  package availability/ingest, not original committee-release clocks.
- `build_transcript_publication_wave4_integration.py`,
  `validate_transcript_publication_wave4_integration.py`, and the companion
  object-control, outcome-control, and claim-review lanes — deterministic
  retirement of the seventy-row aggregate candidate, removal of its resolved
  object candidates from the current queue, seventy exact row-level reviews,
  and one same-claim aggregate replacement. All 93 formal-transcript action
  rows now resolve independently.
- `COMMITTEE_ACTIVITY_COVERAGE_GAPS.md` — exact Layer-2 backfill ledger for all
  210 `not_scanned` bodies, grouped by chamber and parent with official routes
  and controls forbidding false zero-event interpretations.
- `CONGRESSIONAL_COMMITTEE_CONTROL_PLANE.md` — factual architecture, clocks,
  evidence rules, and chart integration posture.
- `CONGRESSIONAL_COMMITTEE_ENTITY_SCHEMA.json` — committee-node contract.
- `CONGRESSIONAL_COMMITTEE_ENTITY_REGISTRY.json` — current committee shell and
  intelligence-committee records supported by the current official sources.
- `CONGRESSIONAL_COMMITTEE_RELATIONSHIP_TYPES.json` — controlled edge
  vocabulary.
- `CONGRESSIONAL_COMMITTEE_RELATIONSHIPS.json` — typed committee/chamber/
  jurisdiction relationships.
- `INTELLIGENCE_COMMITTEE_EVENT_REGISTRY_119TH.json` — HPSCI and SSCI official
  event/source census.
- `HPSCI_EVENT_REGISTRY_119TH.json` and `SSCI_EVENT_REGISTRY_119TH.json` —
  chamber-specific, source-preserving event censuses.
- `INTELLIGENCE_COMMITTEE_SOURCE_MANIFEST.md` — human source and evidence-tier
  router.
- `COMMITTEE_STORY_WATCHBOARD.md` — dated triggers, falsifiers, and source
  routes.
- `validate_committee_package.py` — read-only structural validator.
- `build_committee_registry.py`, `build_intelligence_event_registry.py`, and
  `build_congressional_committee_tree.py` — reproducible registry, event-merge,
  and entity-view builders. The tree's committee control resets even a fully
  expanded federal chart to a focused, progressively expandable Congress path;
  its direct finder indexes all 226 current committees and subcommittees and
  opens an exact body's full variable-depth evidence drawer.
- `build_existing_corpus_registry.py` — strict Layer-0 lane merger and
  duplicate-path/ID gate.
- `audit_existing_corpus_candidates.py` — read-only registry sweep for
  committee/hearing artifacts not yet mapped or explicitly excluded.
- `build_committee_function_registry.py` — strict Layer-1 House/Senate/joint
  lane merger with exact 46/180 scope enforcement.
- `build_committee_activity_registry.py` — strict Layer-2 event and body-coverage
  merger.
- `build_permanent_joint_committee_activity_lane.py` — bounded official-surface
  builder for the four permanent joint committees; separates proceedings,
  occurrence state, publications, result evidence, and surface-specific zeroes.
- `layer2_lanes/permanent_joint_committee_activity_discovery_119th.json` —
  source-preserving 119th-Congress checkpoint for JEC, JCT, the Joint Committee
  on the Library, and the Joint Committee on Printing through July 26, 2026.
- `build_permanent_joint_publication_object_lanes.py` — exact-identifier/URL
  deduplicator that converts the verified permanent-joint publications into
  candidate Layer-3 objects and exact committee/publication relationships.
- `layer3_lanes/permanent_joint_publication_object_inventory.json` and
  `layer3_lanes/permanent_joint_publication_relationship_inventory.json` —
  publication-only candidate objects and issuer edges with exact official URLs
  and clocks; publication never implies legal effect or another result.
- `build_permanent_joint_publication_link_candidates.py` and
  `layer3_lanes/permanent_joint_publication_link_candidate_inventory.json` —
  explicit-identifier and formal-name audit for legislative/legal references
  in the 104 publications; exact identity resolution remains separate from
  relationship admission and unresolved references are retained.
- `layer3_lanes/permanent_joint_publication_reference_relationship_inventory.json`
  — six neutral `publication_references_object` edges admitted from exact
  official-title identifiers; 102 unresolved references remain candidates and
  no legal, legislative, implementation, or result effect is asserted.
- `build_committee_action_registry.py` — strict Layer-2 action-lane merger with
  body, source-artifact, and event-link validation.
- `build_committee_source_object_registry.py` — deterministic Layer-2
  event-source extractor and URL/locator deduplicator.
- `build_committee_durable_object_registry.py` — strict Layer-3 object-lane
  merger with nested status, clock, evidence-locator, and source-object
  foreign-key validation.
- `build_committee_object_relationship_registry.py` — strict Layer-3
  relationship-lane merger with type/domain/range and all registry
  foreign-key checks.
- `build_committee_entity_view_registry.py` — deterministic variable-depth
  chart-view join across the validated research layers.
- `build_committee_outcome_registry.py` — strict Layer-4 outcome-lane merger
  with object, committee, event, action, source, clock-role, and verification
  gates.
- `build_committee_outcome_claim_review_registry.py` — strict claim-review
  merger with original-claim, locator, object, clock, voice, scope, chain,
  conflict, and verified-outcome foreign-key checks. Explicit lane
  supersessions replace provisional reviews only through a same-claim
  replacement audit; stale unresolved-queue entries are removed without
  deleting the underlying lane history.
- `build_committee_story_monitor_registry.py` — deterministic Layer-5 builder
  that groups verified outcomes and unresolved candidates by exact durable
  object, preserves detached candidates without promotion, and emits factual
  state-transition watches with named evidence gates and non-triggers.
- `layer4_lanes/oversight_publication_wave1_outcome_inventory.json` and
  `layer4_review_lanes/oversight_publication_wave1_claim_review_inventory.json`
  — exact-official Wave-1 adjudication of subpoena, request, draft-release,
  report, and transcript-publication candidates. Six narrow outcomes are
  admitted; service, responses, remedial effects, and objectless
  report/transcript publications remain explicit gaps.
- `build_oversight_publication_wave1_outcomes.py`,
  `validate_oversight_publication_wave1.py`, and
  `OVERSIGHT_PUBLICATION_WAVE1_HANDOFF_2026-07-26.md` — reproducible builder,
  strict independent validator, and clock-separated handoff for that lane.
- `harvest_house_repository_daily_index.py` — reproducible official House
  Repository ByDay discovery harvest for the full 119th-Congress date window;
  listings never imply occurrence or results.
- `resolve_house_repository_event_codes.py` and
  `house_repository_event_resolution_overrides.json` — reproducible
  Repository-event identity resolution using official material codes,
  previously validated event XML, and four exact official committee-site
  resolutions; identity resolution never implies occurrence or result.
- `house_repository_daily_discovery_119th.json` — complete dated House
  Repository discovery manifest through the cutoff, kept separate from the
  normalized activity registry until event state and source objects are
  verified.
- `harvest_senate_committee_archives.py`,
  `senate_committee_archive_discovery_119th.json`, and
  `validate_senate_archive_discovery.py` — bounded official Senate
  committee-archive discovery machinery and checkpoint, with SSCI delegation,
  targeted unresolved-only official-label reconciliation, conservative
  multi-body withholding, retrieval hashes, exact residual queues, and no
  listing-to-occurrence promotion.
- `source_snapshots/2026-07-26__senate-archive-discovery-wave1.json` —
  recoverable 726-row Wave 1 checkpoint retained for exact Wave 2
  before/after attribution and adapter comparisons.
- `source_snapshots/2026-07-26__senate-archive-discovery-wave2.json` —
  recoverable 945-row, 900-resolved Wave 2 checkpoint retained for the exact
  Wave 3 official-label reconciliation comparison.
- `SENATE_ACTIVITY_DISCOVERY_HANDOFF_2026-07-26.md` — exact Senate Layer-2
  checkpoint, archive boundaries, counts, defects, and next merge wave.
- `build_sasc_ndaa_markup_lane.py`,
  `validate_sasc_ndaa_markup_lane.py`, and
  `SASC_NDAA_MARKUP_BACKFILL_HANDOFF_2026-07-27.md` — deterministic,
  independently validated 17-record SASC FY2026/FY2027 NDAA markup backfill.
  The isolated lane preserves official discovery IDs, parent/child
  attribution, unknown occurrence and event-result states, the unresolved
  FY2027 two-page clock question, and `not_scanned` body coverage; only the
  official 26–1 and 18–9 full-committee completion results are admitted, with
  no forced event link, numbered-bill identity, or central merge.
- `build_hfsc_markup_material_disposition_premerge.py`,
  `validate_hfsc_markup_material_disposition_premerge.py`, and
  `HFSC_MARKUP_MATERIAL_DISPOSITION_PREMERGE_HANDOFF_2026-07-27.md` —
  isolated audit of the five Wave-4 HFSC disposition-less markup materials.
  Two rows resolve from exact official result objects, one narrows without
  procedural inference, and two remain unresolved. The lane also isolates the
  FC-206 H.R. 5270/H.R. 5317 mechanical conflict for review; none of its
  outputs are visible to the central action merge glob.
- `build_hfsc_event_118290_object_identity_premerge.py`,
  `validate_hfsc_event_118290_object_identity_premerge.py`, and
  `HFSC_EVENT_118290_OBJECT_IDENTITY_PREMERGE_HANDOFF_2026-07-27.md` —
  first deterministic tranche of the 362-action HFSC object-identity backlog.
  The isolated lane resolves all 60 EventID `118290` actions to 25 exact bill
  and 35 exact committee-amendment objects plus 95 factual relationships,
  leaving 302 actions for later tranches. Bill material locators establish
  measure identity only, not the reported-as-amended text; no output is
  visible to the central Layer-3 merge globs.
- `HOUSE_REPOSITORY_EVENT_DETAIL_SCHEMA.json`,
  `build_house_repository_event_details.py`, and
  `HOUSE_REPOSITORY_EVENT_DETAIL_MANIFEST_119TH.json` — resumable,
  circuit-broken ByEvent/XML normalization lane with checksummed official
  fetches, exact status-code boundaries, witness/material routes, canonical
  XML/package gates, and an explicit retry queue; no row is admitted to the
  activity registry by this builder.
- `HOUSE_REPOSITORY_EVENT_DETAIL_CHECKPOINT_2026-07-26.md` — exact partial-run
  handoff after the official Repository began returning HTTP 403, including
  preserved counts, checksum, resume command, and remaining evidence gaps.
- `validate_house_repository_event_details.py` — standalone strict validator
  for complete or partial detail checkpoints, EventID/body foreign keys,
  official vocabularies, count reconciliation, retry-queue identity, and the
  activity-admission withholding rule.
- `HOUSE_EVENT_IDENTITY_CROSSWALK_SCHEMA.json`,
  `build_house_event_identity_crosswalk.py`, and
  `HOUSE_EVENT_IDENTITY_CROSSWALK_119TH.json` — no-network exact-identity lane
  between every House discovery EventID and the activity, HPSCI, merged
  intelligence, and source-object registries; official EventID/URL/XML
  identities are separated from title/date/body candidates and no merge is
  authorized.
- `HOUSE_EVENT_IDENTITY_CROSSWALK_HANDOFF_2026-07-26.md` — exact overlap,
  unresolved, reverse-gap, ambiguity, body-conflict, checksum, and next-review
  summary for the cross-registry identity lane.
- `validate_house_event_identity_crosswalk.py` — independent recomputation of
  exact target identities, source-object foreign-key paths, candidate pairs,
  reverse unmatched queues, counts, and merge-neutrality.
- `HOUSE_EVENT_IDENTITY_CANDIDATE_REVIEW_SCHEMA.json`,
  `build_house_event_identity_candidate_review.py`, and
  `HOUSE_EVENT_IDENTITY_CANDIDATE_REVIEW_119TH.json` — bounded adjudication of
  the 59 body/date/title-exact candidates plus EventID 118279, admitting
  identity only through a checksum-pinned local exact Repository locator and
  reciprocal official committee page while retaining all ambiguity and body
  conflicts.
- `HOUSE_EVENT_IDENTITY_CANDIDATE_REVIEW_HANDOFF_2026-07-26.md` — exact
  47-admitted/13-ambiguous result, EventID 118279 GO05 body-scope finding,
  unresolved EventID list, checksum, and no-central-merge boundary.
- `validate_house_event_identity_candidate_review.py` — independent local proof
  reopening, checksum, exact Repository-locator, reciprocal-page,
  meeting-code/body, scope, count, and merge-neutrality validator.
- `build_action_object_relationship_lane.py` — exact unique-identity joins from
  committee actions to durable objects, with all absent or ambiguous candidates
  retained for later backfill.
- `build_committee_object_role_relationship_lane.py` — explicit issuer-role
  edges for committee reports, document requests, subpoenas, and discussion
  drafts.
- `source_snapshots/` — hashed 2026-07-26 House Clerk and Senate directory
  captures used to reproduce the current structural registry.

## Authority order

1. Chamber rules, committee-establishing resolutions, and enacted statutes.
2. House Clerk / House Committee Repository and Senate committee/calendar
   records.
3. Official committee event pages, videos, witness files, and transcripts.
4. Congress.gov and GovInfo publication objects.
5. Local transcript derivatives, always labeled by evidence tier.

Committee website archive pages are discovery surfaces, not sufficient proof
that an event occurred or that a transcript is public.

## Promotion boundary

The workbench registries remain the research machinery. The vault should receive
only:

- the separate committee tree and its chart-ready node fields;
- the typed relationship layer needed by the entity view;
- source and record routes sized to the available information; and
- event source packets with their actual public evidence objects.

Raw event-census mechanics and local transcript recovery stay here.
