#!/usr/bin/env python3
"""Read-only structural validator for the Freedom 250 mundane organism mold."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
ATLAS = ROOT / "mundane_method_atlas.json"
PLANET_OWNER = ROOT / "mundane_planet_function_owner.json"
PLANET_CANDIDATES = ROOT / "MUNDANE_PLANET_OWNER_CANDIDATES.json"
SIGN_OWNER = ROOT / "mundane_sign_owner_registry.json"
SIGN_CANDIDATES = ROOT / "MUNDANE_SIGN_OWNER_CANDIDATES.json"
HOUSE_OWNER = ROOT / "mundane_house_owner_registry.json"
HOUSE_CANDIDATES = ROOT / "MUNDANE_HOUSE_OWNER_CANDIDATES.json"
STANDARD_PLANET_IDS = [
    "sun",
    "moon",
    "mercury",
    "venus",
    "mars",
    "jupiter",
    "saturn",
    "uranus",
    "neptune",
    "pluto",
]
STANDARD_SIGN_IDS = [
    "aries", "taurus", "gemini", "cancer", "leo", "virgo",
    "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces",
]
STANDARD_HOUSE_IDS = list(range(1, 13))


def unique_ids(records: list[dict], field: str, label: str, errors: list[str]) -> None:
    values = [record.get(field) for record in records]
    missing = [index for index, value in enumerate(values) if value in {None, ""}]
    if missing:
        errors.append(f"{label}: missing {field} at indexes {missing}")
    duplicates = sorted({value for value in values if values.count(value) > 1})
    if duplicates:
        errors.append(f"{label}: duplicate {field}: {duplicates}")


def main() -> int:
    data = json.loads(ATLAS.read_text(encoding="utf-8"))
    planet_owner = json.loads(PLANET_OWNER.read_text(encoding="utf-8"))
    planet_candidates = json.loads(PLANET_CANDIDATES.read_text(encoding="utf-8"))
    sign_owner = json.loads(SIGN_OWNER.read_text(encoding="utf-8"))
    sign_candidates = json.loads(SIGN_CANDIDATES.read_text(encoding="utf-8"))
    house_owner = json.loads(HOUSE_OWNER.read_text(encoding="utf-8"))
    house_candidates = json.loads(HOUSE_CANDIDATES.read_text(encoding="utf-8"))
    errors: list[str] = []

    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")

    boundary = data.get("governing_boundary", {})
    if set(boundary.get("semantic_adaptation_owners", [])) != {"planets", "signs", "houses"}:
        errors.append("semantic adaptation owners must be exactly planets, signs, and houses")
    if set(boundary.get("substantive_mundane_translation_owners", [])) != {"planets", "signs", "houses"}:
        errors.append("substantive mundane translation owners must be exactly planets, signs, and houses")
    if set(boundary.get("shared_core_review_owners", [])) != {"aspects"}:
        errors.append("shared-core review owners must contain only aspects")
    if "aspects" not in boundary.get("shared_operator_owners", []):
        errors.append("aspects must remain a shared operator owner")
    if boundary.get("natal_donor_policy") != "architecture_only_no_semantic_fallback":
        errors.append("natal donor must remain architecture-only with no semantic fallback")

    planets = data.get("planets", [])
    signs = data.get("signs", [])
    houses = data.get("houses", [])
    aspects = data.get("aspect_operators", [])
    chart_types = data.get("chart_types", [])
    owner_families = data.get("owner_families", [])

    if len(planets) != 10:
        errors.append(f"expected 10 Planets, found {len(planets)}")
    if [record.get("planet_id") for record in planets] != STANDARD_PLANET_IDS:
        errors.append("atlas Planet roster and order must be the canonical ten")
    if len(signs) != 12:
        errors.append(f"expected 12 Signs, found {len(signs)}")
    if len(houses) != 12:
        errors.append(f"expected 12 Houses, found {len(houses)}")

    unique_ids(planets, "planet_id", "Planets", errors)
    unique_ids(signs, "sign_id", "Signs", errors)
    unique_ids(houses, "house_no", "Houses", errors)
    unique_ids(aspects, "aspect_id", "Aspects", errors)
    unique_ids(chart_types, "chart_type_id", "Chart types", errors)
    unique_ids(owner_families, "owner_id", "Owner families", errors)

    if [record.get("sign_id") for record in signs] != STANDARD_SIGN_IDS:
        errors.append("atlas Sign roster and order must be the canonical twelve")
    if [record.get("house_no") for record in houses] != STANDARD_HOUSE_IDS:
        errors.append("House numbers must be exactly 1 through 12")

    sign_construction = data.get("sign_construction", {})
    modalities = sign_construction.get("modalities", [])
    elements = sign_construction.get("elements", [])
    unique_ids(modalities, "modality_id", "Modalities", errors)
    unique_ids(elements, "element_id", "Elements", errors)
    if len(modalities) != 3:
        errors.append(f"expected 3 Modality movement owners, found {len(modalities)}")
    if len(elements) != 4:
        errors.append(f"expected 4 Element shaping owners, found {len(elements)}")
    modality_counts = {
        key: sum(sign.get("modality_id") == key for sign in signs)
        for key in ("cardinal", "fixed", "mutable")
    }
    element_counts = {
        key: sum(sign.get("element_id") == key for sign in signs)
        for key in ("fire", "earth", "air", "water")
    }
    if any(count != 4 for count in modality_counts.values()):
        errors.append(f"each Modality must be referenced by exactly 4 Signs: {modality_counts}")
    if any(count != 3 for count in element_counts.values()):
        errors.append(f"each Element must be referenced by exactly 3 Signs: {element_counts}")

    dignity = data.get("dignity_construction", {})
    required_dignity_prohibitions = {
        "not_strength_score",
        "not_importance_score",
        "not_prominence",
        "not_whole_chart_judgment",
    }
    if not required_dignity_prohibitions.issubset(set(dignity.get("prohibitions", []))):
        errors.append("dignity must remain Sign-tool condition, not score/prominence/Judgment")
    if any(record.get("mode") != "shared" for record in aspects):
        errors.append("every Aspect operator must be marked shared")
    required_aspect_ids = {"conjunction", "sextile", "square", "trine", "quincunx", "opposition"}
    if {record.get("aspect_id") for record in aspects} != required_aspect_ids:
        errors.append("shared Aspect roster must be conjunction, sextile, square, trine, quincunx, and opposition")

    relationship_time = data.get("relationship_time_construction", {})
    if relationship_time.get("status") != "katie_doctrine_adopted_2026_08_30_runtime_unbuilt":
        errors.append("relationship-time doctrine status must preserve the adopted-but-unbuilt boundary")
    required_state_identity_fields = {
        "relationship_ref",
        "exact_instant_ref",
        "coordinate_frame_ref",
        "ephemeris_ref",
        "engine_version_ref",
    }
    if set(relationship_time.get("state_identity_fields", [])) != required_state_identity_fields:
        errors.append("relationship state must be keyed by pair, exact instant, coordinate frame, ephemeris, and engine version")
    if set(relationship_time.get("observation_reference_fields", [])) != {"chart_ref", "snapshot_ref", "relationship_state_ref"}:
        errors.append("charts and snapshots must reference rather than own the astronomical relationship state")
    if set(relationship_time.get("chart_observation_projection_fields", [])) != {"direct_geometry_visibility", "phase_narration_admission", "phase_narration_grounds", "seed_echo_refs"}:
        errors.append("chart observation must keep direct geometry, phase-narration admission, and seed echoes separate")
    if set(relationship_time.get("phase_narration_ground_ids", [])) != {"chart_root", "chart_ruler", "outer_pair_era", "exact_us_natal_contact"}:
        errors.append("phase-narration grounds must be exactly the DR-020 root, ruler, era, and exact-U.S.-natal gates")
    if relationship_time.get("projection_lane_rule") != "direct_geometry_is_visible_regardless_of_phase_narration_phase_narration_is_chart_dependent_under_DR_020_and_seed_echoes_remain_separate":
        errors.append("relationship chart projection must preserve the three independent Long Clock lanes")
    if set(relationship_time.get("seed_identity_fields", [])) != {"seed_family_ref_when_applicable", "pass_ref_when_applicable"}:
        errors.append("relationship-time owner must preserve separate seed-family and exact-pass identities")
    if relationship_time.get("state_sharing_rule") != "co_temporal_charts_may_reference_one_astronomical_state_while_preserving_distinct_chart_snapshot_locality_and_house_frame_identities":
        errors.append("co-temporal chart state sharing must preserve distinct chart and house-frame identities")
    if relationship_time.get("state_fields") != ["computed_phase_or_governed_exception", "direct_relationship_aspect_or_null", "orb_or_null", "immediate_relative_motion"]:
        errors.append("relationship state fields must keep phase, governed direct Aspect, orb, and immediate motion separate")
    direct_policy = relationship_time.get("relationship_direct_aspect_policy", {})
    if direct_policy.get("policy_ref") != "relationship_clock_major_five_v1":
        errors.append("relationship-clock direct-Aspect policy must be versioned")
    if direct_policy.get("admitted_aspect_ids") != ["conjunction", "sextile", "square", "trine", "opposition"]:
        errors.append("relationship-clock direct dialogue must use only the governed five major Aspects")
    if direct_policy.get("inactive_value", "missing") is not None:
        errors.append("relationship-clock direct dialogue must use null when no governed Aspect is active")
    if direct_policy.get("whole_chart_quincunx_policy") != "remains_in_whole_aspect_web_not_relationship_clock_direct_dialogue":
        errors.append("whole-chart quincunx must remain outside relationship-clock direct dialogue")
    if "exact_pass_within_seed_family" not in relationship_time.get("history_events", []):
        errors.append("relationship history must distinguish an exact pass within its seed family")
    if "seed_family_pass" in relationship_time.get("history_events", []):
        errors.append("ambiguous seed_family_pass history event is forbidden")
    if relationship_time.get("retrograde_rule") != "geometry_may_reverse_or_reopen_but_chronological_history_and_state_identity_never_rewind":
        errors.append("retrograde rule must separate reversible geometry from irreversible chronology")
    if relationship_time.get("ingress_rule") != "aries_always_resets_mundane_year_non_aries_cardinal_ingress_succeeds_only_when_incumbent_rising_modality_term_permits_and_no_ingress_resets_synodic_history":
        errors.append("relationship-time ingress rule must preserve Aries reset, conditional non-Aries succession, and synodic continuity")
    if relationship_time.get("plot_rule") != "many_to_many_no_planet_or_pair_ownership":
        errors.append("relationship-time owner must prohibit fixed Planet or pair plot ownership")
    braid_policy = relationship_time.get("braid_projection_policy", {})
    if braid_policy.get("status") != "katie_doctrine_adopted_2026_08_30_runtime_unbuilt":
        errors.append("relationship-braid doctrine must remain adopted but runtime-unbuilt")
    if braid_policy.get("owner_scope") != "chart_or_period_interpretation_projection_not_shared_astronomical_state_and_not_evidence":
        errors.append("relationship braids must remain interpretation projections rather than shared state or Evidence")
    if set(braid_policy.get("strand_role_ids", [])) != {"lead_mechanism", "co_mechanism", "supporting_context", "outcompeted", "unresolved"}:
        errors.append("relationship-braid strands must use the five adopted role dispositions")
    if set(braid_policy.get("presence_mode_ids", [])) != {"inherited_substrate", "active_dialogue", "seed_echo"}:
        errors.append("relationship-braid strands must distinguish substrate, dialogue, and echo")
    if set(braid_policy.get("required_braid_fields", [])) != {"plot_ref", "factual_cutoff", "governing_chart_checkpoint_ref", "strand_refs"}:
        errors.append("relationship braids must retain plot, cutoff, checkpoint, and strand identities")
    if set(braid_policy.get("required_strand_fields", [])) != {"relationship_state_ref", "role", "presence_mode", "win_lose_test", "continuity_case", "counterevidence"}:
        errors.append("relationship-braid strands must retain state, role, presence, test, continuity, and counterevidence")
    if braid_policy.get("non_additivity_rule") != "multiple_symbolic_fits_never_add_convergence_evidence_or_forecast_confidence":
        errors.append("relationship braids must not stack symbolic fits into convergence or forecast confidence")
    if braid_policy.get("tempo_hypothesis_rule") != "long_cycle_condition_faster_carrier_lunation_or_eclipse_visibility_is_testable_not_mandatory":
        errors.append("the nested-tempo braid must remain a testable hypothesis rather than a fixed hierarchy")
    relationship_permissions = relationship_time.get("permissions", {})
    if relationship_permissions != {"evidence_credit": 0, "convergence_credit": 0, "plot_ownership": "none", "forecast_authority": "none"}:
        errors.append("relationship-time owner must retain zero Evidence/convergence credit and no plot/Forecast authority")
    if relationship_time.get("current_runtime_result") != "fail_closed_no_relationship_time_owner_loadable":
        errors.append("unbuilt relationship-time runtime must fail closed")
    if relationship_time.get("runtime_coverage_rule") != "only_separately_governed_pair_rosters_may_load":
        errors.append("relationship-time runtime may load only a separately governed pair roster")

    planet_construction = data.get("planet_construction", {})
    if planet_construction.get("owner_mold_ref") != PLANET_OWNER.name:
        errors.append("atlas Planet construction must reference the Planet owner mold")
    if planet_construction.get("candidate_registry_ref") != PLANET_CANDIDATES.name:
        errors.append("atlas Planet construction must reference the candidate registry")
    if planet_construction.get("current_runtime_result") != "fail_closed_no_planet_semantics_loadable":
        errors.append("unratified Planet semantics must fail closed")

    owner_ids = planet_owner.get("required_planet_ids", [])
    owner_records = planet_owner.get("records", {})
    if owner_ids != STANDARD_PLANET_IDS:
        errors.append("Planet owner required roster must be the canonical ten")
    if list(owner_records) != STANDARD_PLANET_IDS:
        errors.append("Planet owner records must be the canonical ten in canonical order")
    for planet_id in STANDARD_PLANET_IDS:
        record = owner_records.get(planet_id, {})
        if record.get("record_ref") != f"mundane-planet-function:{planet_id}":
            errors.append(f"Planet owner record_ref mismatch for {planet_id}")
        if record.get("canonical_body_ref") != f"planet:{planet_id}":
            errors.append(f"Planet owner canonical body mismatch for {planet_id}")
        if record.get("record_state") != "unreviewed":
            errors.append(f"unratified Planet owner must remain unreviewed: {planet_id}")
        if record.get("active_revision_ref") is not None:
            errors.append(f"unratified Planet owner has active revision: {planet_id}")
        if record.get("promotion_receipt_ref") is not None:
            errors.append(f"unratified Planet owner has promotion receipt: {planet_id}")

    permissions = planet_owner.get("permissions", {})
    for field in ("prominence_credit", "evidence_credit", "convergence_credit"):
        if permissions.get(field) != 0:
            errors.append(f"Planet owner {field} must be zero")
    for field in (
        "connector_authority",
        "analytical_order_authority",
        "judgment_authority",
        "timing_authority",
        "translation_authority",
        "forecast_authority",
        "client_authority",
    ):
        if permissions.get(field) != "none":
            errors.append(f"Planet owner {field} must be none")

    candidate_planets = planet_candidates.get("planets", [])
    if [record.get("planet_id") for record in candidate_planets] != STANDARD_PLANET_IDS:
        errors.append("Planet candidate registry must contain the canonical ten in canonical order")
    unique_ids(candidate_planets, "planet_id", "Planet candidates", errors)
    unique_ids(candidate_planets, "candidate_ref", "Planet candidates", errors)
    required_candidate_fields = (
        "collective_motivation",
        "civic_function",
        "possible_carriers",
        "institutional_expressions",
        "gift_pole",
        "shadow_pole",
        "mythic_register",
        "scale_rule",
        "scope_conditions",
        "review_questions",
        "source_refs",
    )
    for record in candidate_planets:
        planet_id = record.get("planet_id")
        if record.get("candidate_ref") != f"candidate:mundane-planet-function:{planet_id}:v1":
            errors.append(f"Planet candidate_ref mismatch for {planet_id}")
        if record.get("candidate_state") != "complete_for_review":
            errors.append(f"Planet candidate is not complete_for_review: {planet_id}")
        if record.get("katie_disposition") != "pending":
            errors.append(f"unreviewed Planet candidate must have pending Katie disposition: {planet_id}")
        for field in required_candidate_fields:
            if not record.get(field):
                errors.append(f"Planet candidate {planet_id} lacks {field}")
        if record.get("gift_pole") == record.get("shadow_pole"):
            errors.append(f"Planet candidate poles collapse for {planet_id}")
        if not any(str(ref).startswith("workbook_planets:") for ref in record.get("source_refs", [])):
            errors.append(f"Planet candidate lacks workbook lineage: {planet_id}")

    candidate_by_id = {record.get("planet_id"): record for record in candidate_planets}
    moon = candidate_by_id.get("moon", {})
    if not any("DR-009" in str(ref) for ref in moon.get("source_refs", [])):
        errors.append("Moon candidate must preserve the sanctioned DR-009 Campion people sense")
    for planet_id in ("uranus", "neptune", "pluto"):
        condition = f"formal_governance_uses_the_traditional_seven_while_{planet_id}_may_define_an_era_field"
        if condition not in candidate_by_id.get(planet_id, {}).get("scope_conditions", []):
            errors.append(f"outer-Planet formal-governance condition missing for {planet_id}")

    for record in planets:
        planet_id = record.get("planet_id")
        if record.get("record_ref") != f"mundane-planet-function:{planet_id}":
            errors.append(f"atlas Planet owner reference mismatch for {planet_id}")
        if record.get("candidate_ref") != f"candidate:mundane-planet-function:{planet_id}:v1":
            errors.append(f"atlas Planet candidate reference mismatch for {planet_id}")
        if record.get("review_state") != "candidate_pending_katie":
            errors.append(f"atlas Planet review state mismatch for {planet_id}")

    sign_construction = data.get("sign_construction", {})
    if sign_construction.get("owner_registry_ref") != SIGN_OWNER.name:
        errors.append("atlas Sign construction must reference the Sign owner registry")
    if sign_construction.get("candidate_registry_ref") != SIGN_CANDIDATES.name:
        errors.append("atlas Sign construction must reference the Sign candidate registry")
    if sign_construction.get("current_runtime_result") != "fail_closed_no_sign_semantics_loadable":
        errors.append("unratified Sign semantics must fail closed")
    if sign_owner.get("required_sign_ids") != STANDARD_SIGN_IDS:
        errors.append("Sign owner required roster must be the canonical twelve")
    sign_owner_records = sign_owner.get("records", {})
    if list(sign_owner_records) != STANDARD_SIGN_IDS:
        errors.append("Sign owner records must be the canonical twelve in canonical order")
    for sign_id in STANDARD_SIGN_IDS:
        record = sign_owner_records.get(sign_id, {})
        if record.get("record_ref") != f"mundane-sign-owner:{sign_id}":
            errors.append(f"Sign owner record_ref mismatch for {sign_id}")
        if record.get("record_state") != "unreviewed":
            errors.append(f"unratified Sign owner must remain unreviewed: {sign_id}")
        if record.get("active_revision_ref") is not None or record.get("promotion_receipt_ref") is not None:
            errors.append(f"unratified Sign owner is loadable or promoted: {sign_id}")

    candidate_signs = sign_candidates.get("signs", [])
    if [record.get("sign_id") for record in candidate_signs] != STANDARD_SIGN_IDS:
        errors.append("Sign candidate registry must contain the canonical twelve in canonical order")
    unique_ids(candidate_signs, "candidate_ref", "Sign candidates", errors)
    for record in candidate_signs:
        sign_id = record.get("sign_id")
        if record.get("candidate_ref") != f"candidate:mundane-sign-expression:{sign_id}:v1":
            errors.append(f"Sign candidate_ref mismatch for {sign_id}")
        if record.get("candidate_state") != "complete_for_review" or record.get("katie_disposition") != "pending":
            errors.append(f"Sign candidate lifecycle mismatch for {sign_id}")
        for field in ("modality_id", "element_id", "unique_collective_configuration", "collective_provisions", "gift_potential", "shadow_potential", "review_questions", "source_refs"):
            if not record.get(field):
                errors.append(f"Sign candidate {sign_id} lacks {field}")
        owner_record = sign_owner_records.get(sign_id, {})
        if owner_record.get("modality_ref") != f"modality:{record.get('modality_id')}":
            errors.append(f"Sign Modality reference mismatch for {sign_id}")
        if owner_record.get("element_ref") != f"element:{record.get('element_id')}":
            errors.append(f"Sign Element reference mismatch for {sign_id}")
    for record in signs:
        sign_id = record.get("sign_id")
        if record.get("owner_ref") != f"mundane-sign-owner:{sign_id}":
            errors.append(f"atlas Sign owner reference mismatch for {sign_id}")
        if record.get("candidate_ref") != f"candidate:mundane-sign-expression:{sign_id}:v1":
            errors.append(f"atlas Sign candidate reference mismatch for {sign_id}")
        if record.get("review_state") != "candidate_pending_katie":
            errors.append(f"atlas Sign review state mismatch for {sign_id}")
        for forbidden in ("operator", "field", "gift", "shadow", "ruler", "house"):
            if forbidden in record:
                errors.append(f"atlas Sign index contains inline semantic or cross-family field {forbidden}: {sign_id}")

    house_construction = data.get("house_construction", {})
    if house_construction.get("owner_registry_ref") != HOUSE_OWNER.name:
        errors.append("atlas House construction must reference the House owner registry")
    if house_construction.get("candidate_registry_ref") != HOUSE_CANDIDATES.name:
        errors.append("atlas House construction must reference the House candidate registry")
    if house_construction.get("current_runtime_result") != "fail_closed_no_house_semantics_loadable":
        errors.append("unratified House semantics must fail closed")
    if house_owner.get("required_house_ids") != STANDARD_HOUSE_IDS:
        errors.append("House owner required roster must be exactly 1 through 12")
    house_owner_records = house_owner.get("records", {})
    if list(house_owner_records) != [str(number) for number in STANDARD_HOUSE_IDS]:
        errors.append("House owner records must be exactly 1 through 12 in order")
    for house_no in STANDARD_HOUSE_IDS:
        record = house_owner_records.get(str(house_no), {})
        if record.get("record_ref") != f"mundane-house-arena:{house_no}":
            errors.append(f"House owner record_ref mismatch for {house_no}")
        if record.get("record_state") != "unreviewed":
            errors.append(f"unratified House owner must remain unreviewed: {house_no}")
        if record.get("active_revision_ref") is not None or record.get("promotion_receipt_ref") is not None:
            errors.append(f"unratified House owner is loadable or promoted: {house_no}")

    candidate_houses = house_candidates.get("houses", [])
    if [record.get("house_no") for record in candidate_houses] != STANDARD_HOUSE_IDS:
        errors.append("House candidate registry must contain exactly 1 through 12 in order")
    unique_ids(candidate_houses, "candidate_ref", "House candidates", errors)
    for record in candidate_houses:
        house_no = record.get("house_no")
        if record.get("candidate_ref") != f"candidate:mundane-house-arena:{house_no}:v1":
            errors.append(f"House candidate_ref mismatch for {house_no}")
        if record.get("candidate_state") != "complete_for_review" or record.get("katie_disposition") != "pending":
            errors.append(f"House candidate lifecycle mismatch for {house_no}")
        for field in ("title", "arena_definition", "topic_records", "review_questions", "source_refs"):
            if not record.get(field):
                errors.append(f"House candidate {house_no} lacks {field}")
        for forbidden in ("planet", "sign", "ruler", "angle", "cusp", "occupant", "derivative_routes"):
            if forbidden in record:
                errors.append(f"House candidate contains cross-family field {forbidden}: {house_no}")
    for record in houses:
        house_no = record.get("house_no")
        if record.get("owner_ref") != f"mundane-house-arena:{house_no}":
            errors.append(f"atlas House owner reference mismatch for {house_no}")
        if record.get("candidate_ref") != f"candidate:mundane-house-arena:{house_no}:v1":
            errors.append(f"atlas House candidate reference mismatch for {house_no}")
        if record.get("review_state") != "candidate_pending_katie":
            errors.append(f"atlas House review state mismatch for {house_no}")
        for forbidden in ("domain", "includes", "planet", "sign", "ruler", "angle", "cusp"):
            if forbidden in record:
                errors.append(f"atlas House index contains inline semantic or cross-family field {forbidden}: {house_no}")

    house_five = next(record for record in candidate_houses if record.get("house_no") == 5)
    house_eleven = next(record for record in candidate_houses if record.get("house_no") == 11)
    if house_five.get("unresolved_allocations") != ["upper_legislative_chamber"]:
        errors.append("House 5 upper-chamber allocation must remain unresolved")
    if house_eleven.get("unresolved_allocations") != ["lower_legislative_chamber"]:
        errors.append("House 11 lower-chamber allocation must remain unresolved")

    for label, records in (("Planet", planets), ("Sign", signs), ("House", houses)):
        for record in records:
            if not str(record.get("source_ref", "")).startswith("workbook:"):
                errors.append(f"{label} record lacks workbook source_ref: {record}")

    required_chart_types = {
        "cardinal_ingress",
        "new_moon",
        "full_moon",
        "solar_eclipse",
        "lunar_eclipse",
        "national_radix",
        "entity_radix",
        "event_chart",
    }
    present_chart_types = {record.get("chart_type_id") for record in chart_types}
    missing_chart_types = sorted(required_chart_types - present_chart_types)
    if missing_chart_types:
        errors.append(f"missing required mundane chart types: {missing_chart_types}")

    major_conjunction = next(
        (record for record in chart_types if record.get("chart_type_id") == "major_conjunction"),
        None,
    )
    if major_conjunction is None:
        errors.append("missing major_conjunction specialist chart type")
    else:
        if major_conjunction.get("clock_requirement") != "exact_perfection":
            errors.append("major_conjunction chart clock must be exact_perfection")
        if major_conjunction.get("cycle_test_policy") != "co_presence_window_required_in_period_weather":
            errors.append("major-conjunction cycle test must route to Period Weather co-presence")

    scope_ids = {record.get("scope_id") for record in data.get("scopes", [])}
    if scope_ids != {"single_chart_skin", "period_skin"}:
        errors.append(f"scope roster must be single_chart_skin + period_skin, found {scope_ids}")
    scopes_by_id = {record.get("scope_id"): record for record in data.get("scopes", [])}
    if set(scopes_by_id.get("single_chart_skin", {}).get("references", [])) != {"relationship_state_refs", "relationship_observation_projection_refs"}:
        errors.append("single-chart skin must reference both astronomical states and chart-specific relationship projections")
    if scopes_by_id.get("period_skin", {}).get("references") != ["relationship_history_slice_refs"]:
        errors.append("period skin must reference, not own or copy, relationship-history slices")

    period_roles = set(data.get("period_member_roles", []))
    required_roles = {"relationship_clock_slice", "era_driver", "governing_ingress", "trigger_lunation", "eclipse", "anchor_radix", "observed_event"}
    missing_roles = sorted(required_roles - period_roles)
    if missing_roles:
        errors.append(f"missing period roles: {missing_roles}")

    invariants = set(data.get("invariants", []))
    for invariant in (
        "calculate_each_fact_once",
        "one_chart_snapshot_one_house_frame_owner",
        "one_aspect_one_canonical_relationship",
        "one_pair_one_stable_relationship_identity",
        "every_relationship_state_and_exact_pass_has_distinct_time_identity",
        "co_temporal_charts_may_reference_one_astronomical_relationship_state",
        "chronology_moves_forward_when_relative_geometry_reverses",
        "period_skin_references_intact_charts",
        "period_skin_references_relationship_history_without_reset_or_copy",
        "missing_mundane_semantics_fail_closed",
    ):
        if invariant not in invariants:
            errors.append(f"missing invariant: {invariant}")

    owner_ids = {record.get("owner_id") for record in owner_families}
    if "planetary_relationship_time" not in owner_ids:
        errors.append("missing planetary_relationship_time owner family")

    gates = set(data.get("gates", []))
    for gate in (
        "no_ingress_boundary_resets_a_synodic_relationship",
        "no_retrograde_return_reuses_a_state_or_pass_identity",
        "no_planet_or_pair_receives_fixed_plot_ownership",
        "no_relationship_braid_stacks_symbolic_fits_into_convergence",
        "no_quincunx_in_relationship_clock_direct_dialogue",
        "no_temporal_co_occurrence_as_causation_or_evidence",
        "no_arc_scores_inside_universal_mundane_doctrine",
        "no_forecast_without_separate_registry_record",
    ):
        if gate not in gates:
            errors.append(f"missing relationship-time gate: {gate}")

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        print(f"MUNDANE MOLD: NEEDS REVIEW ({len(errors)} errors)")
        return 1

    print(
        "MUNDANE MOLD VALID: "
        f"{len(planets)} Planet owner shells + {len(candidate_planets)} complete candidates, "
        f"{len(signs)} Sign owner shells + {len(candidate_signs)} complete candidates, "
        f"{len(houses)} House owner shells + {len(candidate_houses)} complete candidates, "
        f"{len(modalities)} Modalities, {len(elements)} Elements, "
        f"{len(aspects)} shared Aspects, {len(chart_types)} chart types, "
        f"{len(owner_families)} owner families"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
