#!/usr/bin/env python3
"""Build factual conjunction and governed persona charts for 17 inside clocks.

The package is proposal-only.  Every exact pass gets a conjunction chart.  A
family gets at most one persona candidate, from its earliest exact pass, and a
candidate is rendered only when it occurs before the next family's first pass.
Mercury-Venus crossings remain a separately calculated, non-phaseable lane.
"""

from __future__ import annotations

import csv
import hashlib
import html
import importlib.util
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ASTROLOGY_PACKAGES = HERE.parent
SOURCE_PACKAGE = ASTROLOGY_PACKAGES / "Planetary Relationship Clocks 2026-08-30"
FAMILY_SOURCE = SOURCE_PACKAGE / "inside_planet_conjunction_families.json"
RELATIONSHIP_REGISTRY = SOURCE_PACKAGE / "planetary_relationship_registry.json"
RELATIONSHIP_METHOD = SOURCE_PACKAGE / "METHOD AND DOCTRINE REVIEW.md"
LONG_PACKAGE = ASTROLOGY_PACKAGES / "Long Clock Persona Hearings 2026-08-23"
LONG_HELPER_PATH = LONG_PACKAGE / "build_long_clock_personas.py"
SENTIENT_SUN = Path("[local-path-removed] Sun")
TRADITIONAL_TABLES = SENTIENT_SUN / "canonical_traditional_tables.py"
VAULT = Path("Chronicle/")
READING_START = VAULT / "00 - Index/Reading the Charts — START HERE.md"
DECISION_LOG = VAULT / "00 - Index/DECISION LOG.md"

DATA_DIR = HERE / "data"
FAMILY_DIR = DATA_DIR / "families"
EXCEPTION_DIR = DATA_DIR / "exceptions"
CHARTS_DIR = HERE / "charts"
SEED_CHARTS_DIR = CHARTS_DIR / "seeds"
PERSONA_CHARTS_DIR = CHARTS_DIR / "personas"
OVERLAY_CHARTS_DIR = CHARTS_DIR / "overlays"
INDEX_PATH = DATA_DIR / "index.json"
EXCEPTION_PATH = EXCEPTION_DIR / "mercury-venus.json"
CHART_INDEX_PATH = CHARTS_DIR / "index.html"
MANIFEST_PATH = HERE / "manifest.json"
ARTIFACT_CSV_PATH = HERE / "PACKAGE_ARTIFACT_MANIFEST.csv"


def load_module(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


LONG = load_module(LONG_HELPER_PATH, "f250_inside_persona_long_helpers")
TABLES = load_module(TRADITIONAL_TABLES, "f250_inside_persona_traditional_tables")

# The current Sentient Sun calculator intentionally moved dignity ownership to
# canonical_traditional_tables.py.  The reviewed Long Clock chart constructor
# predates that cleanup, so this compatibility bridge points it to the current
# canonical owner without restoring deleted API to Sentient Sun.
LONG.calculator.dignity_label = TABLES.dignity_classification
LONG.calculator.dignity_labels = TABLES.dignity_labels
LONG.TRACKED_CHANGE_BODIES = (
    "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"
)

BODY_NAME = {
    "mercury": "Mercury",
    "venus": "Venus",
    "mars": "Mars",
    "jupiter": "Jupiter",
    "saturn": "Saturn",
    "uranus": "Uranus",
    "neptune": "Neptune",
    "pluto": "Pluto",
}

SCHEMA = "proposal.freedom250.inside-planet-conjunction-persona-hearings/v1"
STATUS = "proposal_only_not_vault_authority"
ELIGIBLE = "calculated_review_candidate_conditional_zero_vote"
SUPERSEDED = "withheld_successor_seed_precedes_persona_crossing"
NO_SUCCESSOR = "withheld_no_successor_boundary"
NON_PHASEABLE = "withheld_non_phaseable_relationship"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def parse_source() -> tuple[dict[str, Any], list[dict[str, Any]], dict[str, Any]]:
    source = json.loads(FAMILY_SOURCE.read_text(encoding="utf-8"))
    cycle_meta = {
        row[0]: {
            "cycle_id": row[0],
            "tier_id": row[1],
            "nominal_cadence_days": row[2],
            "nominal_cycle_years": row[3],
            "phase_contract": row[4],
        }
        for row in source["cycles"]
    }
    families: list[dict[str, Any]] = []
    for cycle_id, family_id, window_role, anchor_id, pass_rows in source["families"]:
        pair = [BODY_NAME[value] for value in cycle_id.split("-")]
        passes = [
            {
                "pass_id": row[0],
                "utc": row[1],
                "longitude_deg": float(row[2]),
                "sign": row[3],
                "degree_in_sign": float(row[4]),
                "relative_motion": row[5],
            }
            for row in pass_rows
        ]
        families.append(
            {
                **cycle_meta[cycle_id],
                "pair": pair,
                "seed_family_id": family_id,
                "window_role": window_role,
                "display_anchor_pass_id": anchor_id,
                "passes": passes,
            }
        )
    return source, families, source["mercury_venus_exception"]


def next_family_map(families: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for cycle_id in sorted({row["cycle_id"] for row in families}):
        rows = sorted(
            (row for row in families if row["cycle_id"] == cycle_id),
            key=lambda row: row["passes"][0]["utc"],
        )
        for current, successor in zip(rows, rows[1:]):
            result[current["seed_family_id"]] = successor
    return result


def pass_root(family: dict[str, Any], pass_row: dict[str, Any]) -> dict[str, Any]:
    governed = LONG.verify_seed_root(family, pass_row)
    return {
        "seed_utc": governed["seed_utc"],
        "seed_jd": governed["seed_jd"],
        "target_longitude": governed["target_longitude"],
        "verification": governed["verification"],
    }


def persona_lifecycle(
    family: dict[str, Any], successor: dict[str, Any] | None
) -> dict[str, Any]:
    anchor = family["passes"][0]
    root = pass_root(family, anchor)
    common = {
        "one_shared_persona_maximum": True,
        "anchor_pass_id": anchor["pass_id"],
        "coordinate_review_status": (
            "proposed_earliest_pass_pending_human_disposition"
            if len(family["passes"]) > 1
            else "unambiguous_single_pass_coordinate_pending_clock_adoption"
        ),
        "anchor_rule": (
            "The conjunction family remains the cycle seed. Its earliest chronological "
            "exact pass supplies the deterministic display and persona coordinate. "
            "Later passes are revision, development, or completion context and receive "
            "no additional persona chart or independent vote."
        ),
    }
    if family["window_role"] == "first_after_window":
        return {
            **common,
            "status": NO_SUCCESSOR,
            "persona_candidate": None,
            "successor_gate": None,
            "meaning": (
                "This family is retained only as the first bracket after the chart "
                "window. Without its successor family, a solar-return candidate "
                "cannot pass the anti-supersession gate."
            ),
        }
    if successor is None:
        raise RuntimeError(f"Missing successor for governing family {family['seed_family_id']}")
    event = LONG.find_persona_event(root["seed_jd"], root["target_longitude"])
    successor_utc = datetime.fromisoformat(successor["passes"][0]["utc"]).astimezone(
        timezone.utc
    )
    successor_jd = LONG.BASE.jd_of(successor_utc)
    margin_days = successor_jd - event["jd_ut"]
    status = ELIGIBLE if margin_days > 0 else SUPERSEDED
    later_family_passes = [
        row for row in family["passes"] if LONG.BASE.jd_of(
            datetime.fromisoformat(row["utc"]).astimezone(timezone.utc)
        ) > event["jd_ut"]
    ]
    return {
        **common,
        "status": status,
        "persona_candidate": {
            "utc": event["utc"].isoformat(timespec="microseconds"),
            "local": event["local"].isoformat(timespec="microseconds"),
            "jd_ut": round(float(event["jd_ut"]), 12),
            "days_after_anchor": round(event["jd_ut"] - root["seed_jd"], 12),
            "verification": event["verification"],
        },
        "successor_gate": {
            "successor_family_id": successor["seed_family_id"],
            "successor_first_pass_id": successor["passes"][0]["pass_id"],
            "successor_first_pass_utc": successor_utc.isoformat(timespec="microseconds"),
            "candidate_precedes_successor": margin_days > 0,
            "margin_successor_minus_candidate_days": round(margin_days, 12),
            "rule": (
                "A conjunction persona is heard only if its first later solar "
                "crossing occurs before the next seed family begins."
            ),
        },
        "family_pass_context_at_candidate": {
            "candidate_precedes_family_final_pass": bool(later_family_passes),
            "later_same_family_pass_ids": [row["pass_id"] for row in later_family_passes],
            "meaning": (
                "The persona candidate occurs while the multipass family still has exact "
                "recontacts ahead. Those recontacts remain revision or completion chapters, "
                "not new seeds or new personas."
                if later_family_passes
                else "The family has no later exact recontact after the persona candidate."
            ),
        },
        "meaning": (
            "The conjunction remained the governing family long enough to reach "
            "its first later solar crossing; a conditional zero-vote persona may be heard."
            if status == ELIGIBLE
            else "The candidate solar crossing occurs after the successor family's first "
            "exact pass. The persona is withheld under the proposed successor gate. This "
            "missing persona is an explicit gate result, not an incomplete calculation."
        ),
    }


def seed_chart(
    family: dict[str, Any],
    pass_row: dict[str, Any],
    *,
    paired_persona_utc: datetime | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    root = pass_root(family, pass_row)
    comparison_utc = paired_persona_utc or root["seed_utc"]
    coverage = LONG.america_pair_coverage(root["seed_utc"], comparison_utc)
    chart, raw = LONG.calculate_chart(
        root["seed_utc"], bool(coverage["include_in_both_charts"]), coverage
    )
    record = {
        "pass_id": pass_row["pass_id"],
        "utc": pass_row["utc"],
        "target_longitude": pass_row["longitude_deg"],
        "target_sign": pass_row["sign"],
        "target_degree_in_sign": pass_row["degree_in_sign"],
        "relative_motion": pass_row["relative_motion"],
        "verification": root["verification"],
        "chart": chart,
        "america_916_coverage": coverage,
        "raw_jd_receipt": round(float(raw["jd"]), 12),
    }
    return record, raw


def render_seed_chart(family: dict[str, Any], pass_record: dict[str, Any]) -> Path:
    pair_label = "–".join(family["pair"])
    local = datetime.fromisoformat(pass_record["chart"]["event"]["local"])
    record = LONG.wheel_record(
        pass_record["chart"],
        f"{pair_label.upper()} CONJUNCTION · {pass_record['pass_id']}",
        f"{local.strftime('%d %b %Y · %H:%M:%S %Z')} · {LONG.PLACE}",
        f"family {family['seed_family_id']} · exact pass · proposal only",
    )
    path = SEED_CHARTS_DIR / f"{pass_record['pass_id']}__conjunction.svg"
    path.write_text(LONG.BASE.render_svg(record), encoding="utf-8")
    return path


def amend_fast_gate(gate: dict[str, Any]) -> dict[str, Any]:
    gate["rule"] = (
        "Mercury, Venus, and Mars are tracked for station, direction, sign, and "
        "relationship changes because those changes can distinguish delivery. "
        "Jupiter through Pluto retain the Long Clock slow-body dependency rule: "
        "positional persistence within 31 days is automatically dependent, and "
        "proximity after 31 days is never independently additive. Every retained "
        "difference remains conditional and zero-vote."
    )
    gate["fast_body_scope"] = {
        "bodies": ["Mercury", "Venus", "Mars"],
        "role": "tracked delivery context, never slow-body carryover or independent vote",
    }
    gate.pop("mercury_scope", None)
    return gate


def render_persona_charts(
    family: dict[str, Any],
    anchor_chart: dict[str, Any],
    persona_chart: dict[str, Any],
) -> tuple[Path, Path]:
    family_id = family["seed_family_id"]
    pair_label = "–".join(family["pair"])
    local = datetime.fromisoformat(persona_chart["event"]["local"])
    event_label = local.strftime("%d %b %Y · %H:%M:%S %Z")
    standalone_record = LONG.wheel_record(
        persona_chart,
        f"{pair_label.upper()} CONJUNCTION PERSONA",
        f"{event_label} · {LONG.PLACE}",
        f"family {family_id} · conditional subsidiary · zero vote",
    )
    seed_record = LONG.wheel_record(
        anchor_chart,
        f"{pair_label.upper()} SEED + PERSONA",
        f"{family['display_anchor_pass_id']} inside",
        f"persona outside · {event_label}",
    )
    outer_map = {
        row[0]: float(row[4]) for row in LONG.wheel_positions(persona_chart)
    }
    standalone = PERSONA_CHARTS_DIR / f"{family_id}__persona-standalone.svg"
    overlay = OVERLAY_CHARTS_DIR / f"{family_id}__seed-persona-biwheel.svg"
    standalone.write_text(LONG.BASE.render_svg(standalone_record), encoding="utf-8")
    overlay.write_text(
        LONG.BASE.render_svg(
            seed_record,
            outer_name=f"{pair_label} Conjunction Persona",
            outer_map=outer_map,
        ),
        encoding="utf-8",
    )
    return standalone, overlay


def build_family(
    family: dict[str, Any], successor: dict[str, Any] | None
) -> tuple[dict[str, Any], dict[str, Any]]:
    lifecycle = persona_lifecycle(family, successor)
    candidate = lifecycle["persona_candidate"]
    persona_utc = (
        datetime.fromisoformat(candidate["utc"]).astimezone(timezone.utc)
        if lifecycle["status"] == ELIGIBLE
        else None
    )
    pass_records: list[dict[str, Any]] = []
    seed_files: list[str] = []
    anchor_record: dict[str, Any] | None = None
    anchor_raw: dict[str, Any] | None = None
    for pass_row in family["passes"]:
        paired = persona_utc if pass_row["pass_id"] == family["display_anchor_pass_id"] else None
        record, raw = seed_chart(family, pass_row, paired_persona_utc=paired)
        path = render_seed_chart(family, record)
        record["chart_file"] = str(path.relative_to(HERE))
        seed_files.append(record["chart_file"])
        pass_records.append(record)
        if pass_row["pass_id"] == family["display_anchor_pass_id"]:
            anchor_record, anchor_raw = record, raw
    if anchor_record is None or anchor_raw is None:
        raise RuntimeError(f"Anchor not found for {family['seed_family_id']}")

    persona_record: dict[str, Any] | None = None
    overlay_record: dict[str, Any] | None = None
    persona_files: list[str] = []
    if lifecycle["status"] == ELIGIBLE:
        coverage = anchor_record["america_916_coverage"]
        persona_chart, persona_raw = LONG.calculate_chart(
            persona_utc,
            bool(coverage["include_in_both_charts"]),
            coverage,
        )
        anchor_chart = anchor_record["chart"]
        seed_jd = LONG.BASE.jd_of(datetime.fromisoformat(anchor_record["utc"]))
        persona_jd = LONG.BASE.jd_of(persona_utc)
        gate = amend_fast_gate(
            LONG.change_gate(seed_jd, persona_jd, anchor_chart, persona_chart)
        )
        focal = {
            body: {
                "position": persona_chart["positions"][body],
                "distance_from_persona_sun_deg": round(
                    LONG.BASE.angular_distance(
                        persona_chart["positions"][body]["longitude"],
                        persona_chart["positions"]["Sun"]["longitude"],
                    ),
                    9,
                ),
                "governance_route": persona_chart["governance_routes"][body],
                "huber_contacts": LONG.BASE.contacts_for(
                    body, persona_chart["huber_aspects"]
                ),
                "mundane_major_contacts": LONG.BASE.contacts_for(
                    body, persona_chart["mundane_major_aspects"]
                ),
            }
            for body in family["pair"]
        }
        standalone, biwheel = render_persona_charts(
            family, anchor_chart, persona_chart
        )
        persona_files = [str(standalone.relative_to(HERE)), str(biwheel.relative_to(HERE))]
        persona_record = {
            "definition": (
                "first later geocentric tropical Sun crossing of the fixed earliest-pass "
                "conjunction longitude, admitted to a hearing only before the successor family"
            ),
            "target_longitude": anchor_record["target_longitude"],
            "days_after_anchor": candidate["days_after_anchor"],
            "verification": candidate["verification"],
            "chart": persona_chart,
            "focal_lenses": focal,
            "chart_files": persona_files,
            "raw_jd_receipt": round(float(persona_raw["jd"]), 12),
        }
        overlay_record = {
            "orb_policy": (
                "major cross contacts at 2 degrees; minor points hard-only and "
                "planet-facing; all conditional and zero-vote"
            ),
            "contacts": LONG.cross_contacts(
                anchor_chart,
                persona_chart,
                tuple(family["pair"]),
                bool(coverage["include_in_both_charts"]),
            ),
            "seed_to_persona_change_gate": gate,
        }

    payload = {
        "schema": SCHEMA,
        "status": STATUS,
        "identity": {
            "cycle_id": family["cycle_id"],
            "tier_id": family["tier_id"],
            "pair": family["pair"],
            "seed_family_id": family["seed_family_id"],
            "window_role": family["window_role"],
            "provisional_display_anchor_pass_id": family["display_anchor_pass_id"],
        },
        "authority_boundary": {
            "review_posture": "proposal_for_review",
            "astrology_reference_only": True,
            "official_research_evidence": False,
            "event_proof": False,
            "timing_or_forecast_authority": False,
            "plot_ownership": False,
            "independent_vote": False,
            "live_vault_promotion": False,
            "astro_gold_verification": "pending",
        },
        "cycle_context": {
            "nominal_cadence_days": family["nominal_cadence_days"],
            "nominal_cycle_years": family["nominal_cycle_years"],
            "phase_contract": family["phase_contract"],
            "delivery_role": (
                "fast relationship clock that can differentiate delivery inside a larger "
                "umbrella; it does not displace the ten Long Clocks"
            ),
        },
        "anchor_decision": {
            "proposed_pass_id": family["passes"][0]["pass_id"],
            "selection_basis": "earliest_chronological_exact_pass",
            "review_status": (
                "proposed_earliest_pass_pending_human_disposition"
                if len(family["passes"]) > 1
                else "unambiguous_single_pass_coordinate_pending_clock_adoption"
            ),
            "multipass_family": len(family["passes"]) > 1,
            "later_pass_role": (
                "revision_development_completion_context_no_extra_persona_or_vote"
                if len(family["passes"]) > 1
                else "single_pass_anchor_and_family_pass_are_identical"
            ),
        },
        "persona_lifecycle": lifecycle,
        "exact_passes": pass_records,
        "persona": persona_record,
        "radix_persona_overlay": overlay_record,
        "dependency_ledger": {
            "guaranteed": [
                "The persona Sun repeats the fixed anchor longitude.",
                "The conjunction pair shares one target and at most one family persona.",
            ],
            "dependent": [
                "Later exact passes remain members of the same family until an opposition boundary intervenes.",
                "Slow-body positional persistence is not independent news.",
                "A persona withheld by the successor gate is an explicit gate result, not missing work.",
            ],
            "potentially_additive_but_zero_vote": [
                "derived angles, houses, rulers, and dispositors",
                "focal-lens differentiation between the two conjunction bodies",
                "condition, station, sign, or material relationship changes",
                "non-mechanical tight radix-persona cross contacts",
            ],
        },
        "settings": {
            "zodiac": "tropical",
            "center": "geocentric",
            "houses": "Whole Sign",
            "place": LONG.PLACE,
            "latitude": LONG.LATITUDE,
            "longitude": LONG.LONGITUDE,
            "rulers": "traditional",
            "node": "true",
            "ephemeris_runtime": "returned flags recorded per chart; Moshier fallback is explicit",
        },
        "provenance": {
            "family_ledger": str(FAMILY_SOURCE),
        "reviewed_long_clock_helper": str(LONG_HELPER_PATH),
            "canonical_dignity_tables": str(TRADITIONAL_TABLES),
            "builder": str(Path(__file__).resolve()),
        },
    }
    summary = {
        "cycle_id": family["cycle_id"],
        "seed_family_id": family["seed_family_id"],
        "window_role": family["window_role"],
        "pair": family["pair"],
        "pass_count": len(pass_records),
        "provisional_anchor_pass_id": family["passes"][0]["pass_id"],
        "persona_status": lifecycle["status"],
        "persona_candidate_utc": candidate["utc"] if candidate else None,
        "successor_family_id": (
            lifecycle["successor_gate"]["successor_family_id"]
            if lifecycle["successor_gate"]
            else None
        ),
        "data_file": f"data/families/{family['seed_family_id']}.json",
        "seed_chart_files": seed_files,
        "persona_chart_files": persona_files,
    }
    return payload, summary


def build_mercury_venus(exception: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    family_stub = {"cycle_id": "mercury-venus", "pair": ["Mercury", "Venus"]}
    records: list[dict[str, Any]] = []
    chart_files: list[str] = []
    for index, row in enumerate(exception["crossings"], start=1):
        pass_row = {
            "pass_id": f"mercury-venus-{row[0][:10].replace('-', '')}-x{index}",
            "utc": row[0],
            "longitude_deg": float(row[1]),
            "sign": row[2],
            "degree_in_sign": float(row[3]),
            "relative_motion": row[4],
            "window_relation": row[5],
        }
        record, _raw = seed_chart(family_stub, pass_row)
        path = render_seed_chart(
            {
                "pair": ["Mercury", "Venus"],
                "seed_family_id": "non-phaseable-crossing-lane",
            },
            record,
        )
        record["window_relation"] = row[5]
        record["chart_file"] = str(path.relative_to(HERE))
        chart_files.append(record["chart_file"])
        records.append(record)
    payload = {
        "schema": "proposal.freedom250.mercury-venus-conjunction-crossings/v1",
        "status": STATUS,
        "identity": {"cycle_id": "mercury-venus", "pair": ["Mercury", "Venus"]},
        "phase_contract": "non_phaseable_under_current_geocentric_eight_phase_grammar",
        "persona_lifecycle": {
            "status": NON_PHASEABLE,
            "persona_candidate": None,
            "meaning": (
                "Exact conjunction crossings are real and receive factual charts, but the "
                "relationship has no geocentric opposition or unique conjunction-to-opposition "
                "family. A persona would falsely imply a governed seed family."
            ),
        },
        "exception_wording": exception["exception_wording"],
        "cadence_warning": exception["cadence_warning"],
        "crossings": records,
        "authority_boundary": {
            "proposal_for_review": True,
            "astrology_reference_only": True,
            "official_research_evidence": False,
            "persona_authorized": False,
            "live_vault_promotion": False,
        },
    }
    summary = {
        "cycle_id": "mercury-venus",
        "crossing_count": len(records),
        "in_window_crossing_count": sum(
            row["window_relation"] == "in_window" for row in records
        ),
        "persona_status": NON_PHASEABLE,
        "data_file": "data/exceptions/mercury-venus.json",
        "seed_chart_files": chart_files,
    }
    return payload, summary


def build_chart_index(family_rows: list[dict[str, Any]], mv_row: dict[str, Any]) -> str:
    cards = []
    for row in family_rows:
        seed_links = " ".join(
            f'<a href="{html.escape(path.replace("charts/", ""))}">{html.escape(Path(path).stem)}</a>'
            for path in row["seed_chart_files"]
        )
        persona_links = " ".join(
            f'<a href="{html.escape(path.replace("charts/", ""))}">{html.escape(Path(path).stem)}</a>'
            for path in row["persona_chart_files"]
        ) or "<span>no rendered persona</span>"
        cards.append(
            f'<article><h2>{html.escape("–".join(row["pair"]))} · {html.escape(row["seed_family_id"])}</h2>'
            f'<p><b>{html.escape(row["persona_status"].replace("_", " "))}</b></p>'
            f'<p class="links"><strong>Pass charts</strong> {seed_links}</p>'
            f'<p class="links"><strong>Persona</strong> {persona_links}</p>'
            f'<p><a href="../{html.escape(row["data_file"])}">Factual JSON receipt</a></p></article>'
        )
    mv_links = " ".join(
        f'<a href="{html.escape(path.replace("charts/", ""))}">{html.escape(Path(path).stem)}</a>'
        for path in mv_row["seed_chart_files"]
    )
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Inside Planet Conjunction Persona Hearings</title>
<style>body{{margin:auto;max-width:1120px;padding:32px;font:16px/1.5 Georgia,serif;background:#f7f3e9;color:#29251f}}article{{background:#fffdf7;border:1px solid #d8cdbb;border-radius:14px;padding:18px;margin:16px 0}}h1,h2{{font-weight:400}}h2{{font-size:1.2rem}}a{{color:#564875}}.links{{display:grid;grid-template-columns:8rem 1fr;gap:8px}}span{{color:#786f63}}</style></head><body>
<h1>Inside-planet conjunction charts and persona hearings</h1>
<p>Proposal-only Astrology Reference surface. Every exact pass is visible. A rendered persona candidate means only that the first later solar crossing of the proposed coordinate preceded the successor family; it remains conditional and zero-vote. A missing persona is an explicit gate result.</p>
{''.join(cards)}
<article><h2>Mercury–Venus · non-phaseable exception</h2><p><b>no persona authorized</b></p><p>{mv_links}</p><p><a href="../{mv_row['data_file']}">Factual JSON receipt</a></p></article>
</body></html>"""


def source_hashes() -> dict[str, str]:
    candidates = [
        FAMILY_SOURCE,
        RELATIONSHIP_REGISTRY,
        RELATIONSHIP_METHOD,
        LONG_HELPER_PATH,
        LONG.BASE_BUILDER_PATH,
        LONG.SYNODIC_PATH,
        LONG.CONVENTIONS_PATH,
        LONG.WHEEL_PATH,
        LONG.AMERICA_PATH,
        Path(LONG.america.CACHE),
        SENTIENT_SUN / "chart_calculator.py",
        SENTIENT_SUN / "reading_engine.py",
        TRADITIONAL_TABLES,
        LONG.PERSONA_METHOD_PATH,
        READING_START,
        DECISION_LOG,
        Path(__file__).resolve(),
    ]
    missing = [str(path) for path in candidates if not path.exists()]
    if missing:
        raise RuntimeError(f"Missing source dependencies: {missing}")
    return {str(path): sha256(path) for path in candidates}


def artifact_metadata(path: Path) -> dict[str, str]:
    relative = path.relative_to(HERE)
    text = str(relative)
    name = path.name
    if name == "README.md":
        return {
            "artifact_role": "router",
            "custody_class": "workbench_controls",
            "producer": "authored_workbench_source",
            "rebuildability": "authored_not_regenerated",
            "search_visibility": "sky_and_charts_candidate",
        }
    if name == "CONJUNCTION PERSONA METHOD.md":
        return {
            "artifact_role": "method",
            "custody_class": "workbench_controls",
            "producer": "authored_workbench_source",
            "rebuildability": "authored_not_regenerated",
            "search_visibility": "sky_and_charts_candidate",
        }
    if path.suffix == ".md":
        return {
            "artifact_role": "answer",
            "custody_class": "workbench_controls",
            "producer": "authored_workbench_source",
            "rebuildability": "authored_not_regenerated",
            "search_visibility": "sky_and_charts_candidate",
        }
    if name.startswith("build_") and path.suffix == ".py":
        return {
            "artifact_role": "builder",
            "custody_class": "workbench_controls",
            "producer": "authored_workbench_source",
            "rebuildability": "authored_not_regenerated",
            "search_visibility": "technical_internal",
        }
    if name.startswith("validate_") and path.suffix == ".py":
        return {
            "artifact_role": "validator",
            "custody_class": "workbench_controls",
            "producer": "authored_workbench_source",
            "rebuildability": "authored_not_regenerated",
            "search_visibility": "technical_internal",
        }
    if text == "charts/index.html":
        return {
            "artifact_role": "deliverable",
            "custody_class": "export_only",
            "producer": Path(__file__).name,
            "rebuildability": "rebuildable_by_builder",
            "search_visibility": "sky_and_charts_candidate",
        }
    if path.suffix == ".svg":
        return {
            "artifact_role": "visual",
            "custody_class": "export_only",
            "producer": Path(__file__).name,
            "rebuildability": "rebuildable_by_builder",
            "search_visibility": "technical_sidecar",
        }
    if path.suffix == ".json":
        return {
            "artifact_role": "generated_projection",
            "custody_class": "producer_controls",
            "producer": Path(__file__).name,
            "rebuildability": "rebuildable_by_builder",
            "search_visibility": "technical_sidecar",
        }
    return {
        "artifact_role": "other",
        "custody_class": "workbench_controls",
        "producer": "authored_workbench_source",
        "rebuildability": "authored_not_regenerated",
        "search_visibility": "technical_internal",
    }


def artifact_rows() -> list[dict[str, Any]]:
    paths = sorted(
        path
        for path in HERE.rglob("*")
        if path.is_file()
        and path not in {MANIFEST_PATH, ARTIFACT_CSV_PATH}
        and "__pycache__" not in path.parts
    )
    return [
        {
            "path": str(path.relative_to(HERE)),
            **artifact_metadata(path),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in paths
    ]


def delegation_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Project generated sidecars into the Workbench custody-manifest schema."""

    delegated_prefixes = (
        "data/families/",
        "data/exceptions/",
        "charts/seeds/",
        "charts/personas/",
        "charts/overlays/",
    )
    return [
        {
            "relative_path": row["path"],
            "bytes": row["bytes"],
            "sha256": row["sha256"],
            "custody_class": "generated",
            "artifact_role": row["artifact_role"],
            "producer_path": Path(__file__).name,
            "rebuildability": "rebuildable",
            "search_visibility": "technical",
        }
        for row in rows
        if row["path"].startswith(delegated_prefixes)
    ]


def main() -> None:
    for directory in (
        FAMILY_DIR,
        EXCEPTION_DIR,
        SEED_CHARTS_DIR,
        PERSONA_CHARTS_DIR,
        OVERLAY_CHARTS_DIR,
    ):
        directory.mkdir(parents=True, exist_ok=True)
    source, families, exception = parse_source()
    successors = next_family_map(families)
    summaries: list[dict[str, Any]] = []
    for family in families:
        payload, summary = build_family(
            family, successors.get(family["seed_family_id"])
        )
        write_json(FAMILY_DIR / f"{family['seed_family_id']}.json", payload)
        summaries.append(summary)
        print(
            f"BUILT {family['seed_family_id']} passes={summary['pass_count']} "
            f"persona={summary['persona_status']}"
        )
    mv_payload, mv_summary = build_mercury_venus(exception)
    write_json(EXCEPTION_PATH, mv_payload)
    status_counts = {
        status: sum(row["persona_status"] == status for row in summaries)
        for status in (ELIGIBLE, SUPERSEDED, NO_SUCCESSOR)
    }
    index = {
        "schema": SCHEMA,
        "status": STATUS,
        "created_utc_date": "2026-08-30",
        "source_family_ledger": str(FAMILY_SOURCE),
        "chart_window": source["chart_window"],
        "coverage": {
            "phaseable_pair_count": 17,
            "family_count": len(summaries),
            "exact_pass_count": sum(row["pass_count"] for row in summaries),
            "governing_family_count": sum(
                row["window_role"] != "first_after_window" for row in summaries
            ),
            "bracketing_only_family_count": sum(
                row["window_role"] == "first_after_window" for row in summaries
            ),
            "persona_status_counts": status_counts,
            "rendered_persona_count": status_counts[ELIGIBLE],
            "mercury_venus_crossing_count": mv_summary["crossing_count"],
            "mercury_venus_in_window_crossing_count": mv_summary[
                "in_window_crossing_count"
            ],
        },
        "governing_rules": {
            "anchor": (
                "the conjunction family remains the seed; this package proposes its earliest "
                "exact pass as the one fixed display and family-persona coordinate, pending "
                "human disposition for multipass families"
            ),
            "multipass": "later passes remain family context and get conjunction charts, never extra personas or votes",
            "successor_gate": "persona candidate must precede the next family's first exact pass",
            "missing_persona": "an explicit lifecycle-gate result, never silently omitted",
            "mercury_venus": "crossing charts only until a separate inferior-planet family doctrine exists",
        },
        "families": summaries,
        "mercury_venus_exception": mv_summary,
        "authority_boundary": {
            "proposal_for_review": True,
            "astrology_reference_only": True,
            "official_research_evidence": False,
            "forecast_or_timing_authority": False,
            "plot_ownership": False,
            "live_vault_promotion": False,
        },
    }
    write_json(INDEX_PATH, index)
    CHART_INDEX_PATH.write_text(build_chart_index(summaries, mv_summary), encoding="utf-8")
    rows = artifact_rows()
    manifest = {
        "schema": "proposal.freedom250.inside-planet-persona-manifest/v1",
        "status": STATUS,
        "source_hashes": source_hashes(),
        "artifact_count_excluding_manifests": len(rows),
        "artifacts": rows,
    }
    write_json(MANIFEST_PATH, manifest)
    with ARTIFACT_CSV_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=(
                "relative_path",
                "bytes",
                "sha256",
                "custody_class",
                "artifact_role",
                "producer_path",
                "rebuildability",
                "search_visibility",
            ),
        )
        writer.writeheader()
        writer.writerows(delegation_rows(rows))
    print(
        "COMPLETE "
        f"families={len(summaries)} passes={sum(row['pass_count'] for row in summaries)} "
        f"personas={status_counts[ELIGIBLE]} successor_collisions={status_counts[SUPERSEDED]} "
        f"bracketing={status_counts[NO_SUCCESSOR]} mercury_venus={mv_summary['crossing_count']}"
    )


if __name__ == "__main__":
    main()
