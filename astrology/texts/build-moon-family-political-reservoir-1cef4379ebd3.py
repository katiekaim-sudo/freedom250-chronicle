#!/usr/bin/env python3
"""Build the source-separated political-reservoir index for 2026 Moon families.

This index does not import government research into astrology. It records the
already-authored comparison routes for Full phases that have occurred and
withholds political maturation for future Full phases. Workbench research IDs
and paths remain pointers only; this builder never reads the Workbench.
"""

from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = HERE / "moon_family_political_reservoir_2024_2026.json"
CUTOFF = date.fromisoformat("2026-09-25")
TRIAGE_PATH = "99 - Templates/full_moon_family_triage_2026.json"
CATALOG_PATH = "03 - Astrology/Astrology Files/ASTROLOGY FILES CATALOG.json"
RESERVOIR_NOTE = (
    "03 - Astrology/Astrology Files/Mundane Story Overlaps/"
    "The Seeds Have Earthly Receipts — 2024–2026 Moon-Family Political Reservoir.md"
)


def route(
    companion_astrology_id: str,
    companion_path: str,
    comparison_summary: str,
    *research_routes: tuple[str, str, str],
    comparison_state: str = "retrospective_comparison_complete",
) -> dict:
    return {
        "comparison_state": comparison_state,
        "companion_astrology_id": companion_astrology_id,
        "companion_path": companion_path,
        "comparison_summary": comparison_summary,
        "research_routes": [
            {"research_id": research_id, "read_first": read_first, "role": role}
            for research_id, read_first, role in research_routes
        ],
    }


OVERLAP = "03 - Astrology/Astrology Files/Mundane Story Overlaps"
WORKING = "03 - Astrology/Astrology Files/Working Papers — Sept 2026"

ROUTES = {
    "lun-2024-07-05-ne": route(
        "cancer-moon-family-2024-2026",
        f"{WORKING}/The Burden and the Rule Change Places — 2024–2026 Cancer Moon Family.md",
        "Five independently selected federal burden-and-control objects reach rescission, operation, retained exclusion or unfinished rewrite states.",
        (
            "july-2024-protection-financial-control-window",
            "Research Packages/July 2024 Protection and Financial Control Window/README.md",
            "fixed-window lifecycle control",
        ),
    ),
    "lun-2024-08-04-ne": route(
        "leo-moon-family-2024-2026",
        f"{WORKING}/The Public Reaches the Horizon — 2024–2026 Leo Moon Family.md",
        "The exchange-hours object receives regulatory permission while shared market infrastructure and operation remain separate future gates.",
        (
            "fed-clearing-treasury",
            "Research Packages/Fed, Clearing and Treasury/NYSE_ARCA_EXTENDED_HOURS_TRANSITION_TIMELINE_2024_2026.md",
            "same-market permission-to-operation lifecycle",
        ),
    ),
    "lun-2024-09-03-ne": route(
        "virgo-moon-family-2024-2026",
        f"{WORKING}/The Evidence Leaves the Stage — 2024–2026 Virgo Moon Family.md",
        "Six public SEC recordkeeping orders route part of their remedy through nonpublic consultant processes, proving mandated review but not completion.",
        (
            "sec-credit-rating-recordkeeping-orders-2024-2026",
            "Research Packages/SEC Credit Rating Recordkeeping Orders 2024-2026/SEC_CREDIT_RATING_RECORDKEEPING_ORDERS_MATURATION_2024_2026.md",
            "same-order enforcement and remedy lifecycle",
        ),
    ),
    "lun-2024-10-02-ne-solar": route(
        "libra-moon-family-2024-2026",
        f"{WORKING}/The Terms Outlive the Shadow — 2024–2026 Libra Moon Family.md",
        "The ILA–USMX strike interruption proceeds through tentative settlement, ratification and signed operating contract before the Full phase.",
        (
            "contested-logistics",
            "Research Packages/Contested Logistics/ILA_USMX_MASTER_CONTRACT_TIMELINE.md",
            "same-contract negotiation-to-operation lifecycle",
        ),
    ),
    "lun-2024-11-01-ne": route(
        "scorpio-moon-family-2024-2026",
        f"{WORKING}/The Test Acquires a Foundation — 2024–2026 Scorpio Moon Family.md",
        "Hong Kong's sandbox, ordinance, licence and later operation are retained as different clocks rather than collapsed into one launch.",
        (
            "international-monetary-transition",
            "Research Packages/International Monetary Transition/13 - International Crypto Map 2026/country_research/HK_PRIMARY_SOURCE_BASELINE_2026-09-15.md",
            "same-jurisdiction sandbox-to-licence control",
        ),
    ),
    "lun-2024-12-01-ne": route(
        "sagittarius-moon-family-2024-2027",
        f"{WORKING}/The Story Must Become the Filing — 2024–2027 Sagittarius Moon Family.md",
        "The CTA reporting perimeter moves from nationwide injunction through suspension and interim narrowing into a final foreign-entity-only rule.",
        (
            "december-2024-beneficial-ownership-reporting-perimeter",
            "Research Packages/December 2024 Beneficial Ownership Reporting Perimeter/README.md",
            "same-statute reporting-perimeter lifecycle",
        ),
    ),
    "lun-2024-12-30-ne": route(
        "capricorn-moon-family-2024-2026",
        f"{WORKING}/The Obligation Changes Perimeter — 2024–2026 Capricorn Moon Family.md",
        "The exact DeFi rule is disapproved while a distinct custodial reporting rail operates; a same-window control finds a second annulled perimeter and one durable EDGAR identity system.",
        (
            "treasury-irs",
            "Research Packages/Treasury and IRS/TREASURY_IRS_TRANSITION_TIMELINE.md",
            "same-rule backbone and adjacent custodial control",
        ),
        (
            "december-2024-rule-perimeter-operating-identity-window",
            "Research Packages/December 2024 Rule Perimeter and Operating Identity Window/README.md",
            "same-window counter-control; not an additional astrology vote",
        ),
    ),
    "lun-2025-01-29-ne": route(
        "aquarius-moon-family-2025-2026",
        f"{WORKING}/The Command Acquires a Body — 2025–2026 Aquarius Moon Family.md",
        "Four fixed-window authority objects acquire named administrative carriers, procedures or operating machinery without becoming one coordinated program.",
        (
            "january-2025-authority-operations-window",
            "Research Packages/January 2025 Authority to Operations Window/README.md",
            "fixed-window authority-to-operations control",
        ),
    ),
    "lun-2025-02-28-ne": route(
        "pisces-moon-family-2025-2026",
        f"{WORKING}/The Record Enters Shadow — 2025–2026 Pisces Moon Family.md",
        "EO 14222's payment-justification architecture reaches a bounded operating feed while government-wide coverage and final rules remain open.",
        (
            "fraud-payment-integrity",
            "Research Packages/Fraud and Payment Integrity/FEDERAL_FUNDS_LEDGER_ADOPTION_WATCHBOARD_2026-07-23.md",
            "same-order and adjacent-policy payment-control lifecycle",
        ),
    ),
    "lun-2025-03-29-ne-solar": route(
        "libra-capricorn-2026-governing-stack",
        f"{WORKING}/The Image Becomes an Order — 2026 Aries Full Moon Reread.md",
        "The fixed March authority window follows removals, tariffs, labor exclusions, D.C. machinery, Smithsonian review and the Investment Accelerator into later legal or operating states.",
        (
            "march-2025-aries-eclipse-authority-window",
            "Research Packages/March 2025 Aries Eclipse Authority Window/README.md",
            "fixed-window authority-to-machinery reservoir",
        ),
        (
            "dvd-third-country-removal-authority-2025-2026",
            "Research Packages/DVD Third-Country Removal Authority 2025-2026/README.md",
            "same-case legal spine",
        ),
        comparison_state="pre_full_comparison_prepared",
    ),
}

FUTURE = {
    "lun-2025-04-27-ne": "Taurus",
    "lun-2025-05-27-ne": "Gemini",
    "lun-2025-06-25-ne": "Cancer",
}

LATE_YEAR_COMPANION = (
    f"{WORKING}/The Family Survives Degree Drift — Late-2026 Moon-Family Controls.md"
)


def load_json(relative_path: str) -> dict:
    return json.loads((ROOT / relative_path).read_text(encoding="utf-8"))


def receipt(relative_path: str) -> dict:
    path = ROOT / relative_path
    if not path.is_file():
        raise FileNotFoundError(relative_path)
    return {
        "path": relative_path,
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def build_payload() -> dict:
    triage = load_json(TRIAGE_PATH)
    catalog = load_json(CATALOG_PATH)
    catalog_ids = {row["astrology_id"] for row in catalog["packages"]}
    if triage["family_count"] != 13 or len(triage["families"]) != 13:
        raise ValueError("Moon-family control population drift")
    if set(ROUTES) | set(FUTURE) != {row["seed"]["chart_id"] for row in triage["families"]}:
        raise ValueError("political-reservoir route map does not cover the thirteen families exactly")

    records = []
    companion_paths = {RESERVOIR_NOTE}
    for family in triage["families"]:
        seed = family["seed"]
        full = family["full"]
        seed_id = seed["chart_id"]
        full_date = date.fromisoformat(full["exact_local"][:10])
        record = {
            "lineage_id": family["lineage_id"],
            "seed": {
                "chart_id": seed_id,
                "exact_local": seed["exact_local"],
                "moon_sign": seed["moon_sign"],
                "eclipse": seed["eclipse"],
            },
            "full_phase": {
                "chart_id": full["chart_id"],
                "exact_local": full["exact_local"],
                "moon_sign": full["moon_sign"],
                "eclipse": full["eclipse"],
                "clock_state_at_cutoff": "occurred" if full_date <= CUTOFF else "future",
            },
        }
        if seed_id in ROUTES:
            mapped = ROUTES[seed_id]
            if not mapped["research_routes"]:
                raise ValueError(f"research-backed route has no research pointers for {seed_id}")
            if full_date <= CUTOFF and mapped["comparison_state"] != "retrospective_comparison_complete":
                raise ValueError(f"occurred Full phase is not retrospective-complete: {seed_id}")
            if full_date > CUTOFF and mapped["comparison_state"] != "pre_full_comparison_prepared":
                raise ValueError(f"future Full phase has an invalid prepared-route state: {seed_id}")
            if mapped["companion_astrology_id"] not in catalog_ids:
                raise ValueError(f"unknown companion astrology_id for {seed_id}")
            companion_paths.add(mapped["companion_path"])
            record.update(mapped)
        else:
            if full_date <= CUTOFF:
                raise ValueError(f"occurred Full phase lacks retrospective route: {seed_id}")
            companion_paths.add(LATE_YEAR_COMPANION)
            record.update({
                "comparison_state": "prospective_maturation_withheld",
                "companion_astrology_id": "late-year-moon-family-controls-2026",
                "companion_path": LATE_YEAR_COMPANION,
                "comparison_summary": (
                    f"The {FUTURE[seed_id]} Full phase is future at the cutoff; no political maturation is assigned."
                ),
                "research_routes": [],
            })
        records.append(record)

    completed = sum(row["comparison_state"] == "retrospective_comparison_complete" for row in records)
    prepared = sum(row["comparison_state"] == "pre_full_comparison_prepared" for row in records)
    withheld = sum(row["comparison_state"] == "prospective_maturation_withheld" for row in records)
    if (completed, prepared, withheld) != (9, 1, 3):
        raise ValueError("political-reservoir state count drift")

    sources = sorted({TRIAGE_PATH, CATALOG_PATH} | companion_paths)
    return {
        "schema": "freedom250.moon-family-political-reservoir/v1",
        "developed_through": CUTOFF.isoformat(),
        "purpose": "Route each 2026 Full-Moon family to its independently researched political comparison or an explicit future-withheld state without importing factual payloads into astrology.",
        "counts": {
            "families": len(records),
            "retrospective_comparisons_complete": completed,
            "pre_full_comparisons_prepared": prepared,
            "prospective_maturations_withheld": withheld,
        },
        "records": records,
        "authority_boundary": {
            "workbench_content_imported": False,
            "astrology_selected_evidence": False,
            "same_window_objects_are_extra_votes": False,
            "thematic_similarity_is_maturation": False,
            "locked_readings_changed": False,
            "forecast_ledger_credit": "zero",
            "evidence_credit": "zero",
        },
        "admission_rule": "A retrospective route requires an independently selected official object or bounded window with a traceable state change. Same-window controls remain controls, not extra confirmations.",
        "source_receipts": [receipt(path) for path in sources],
    }


def main() -> None:
    payload = build_payload()
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(
        f"Wrote {OUT.name}: {payload['counts']['retrospective_comparisons_complete']} retrospective routes, "
        f"{payload['counts']['pre_full_comparisons_prepared']} pre-Full route, "
        f"{payload['counts']['prospective_maturations_withheld']} future-withheld routes."
    )


if __name__ == "__main__":
    main()
