#!/usr/bin/env python3
"""Fail-closed validator for the inside-planet conjunction persona package."""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import swisseph as swe


HERE = Path(__file__).resolve().parent
BUILDER_PATH = HERE / "build_inside_planet_conjunction_personas.py"
INDEX_PATH = HERE / "data/index.json"
FAMILY_DIR = HERE / "data/families"
MV_PATH = HERE / "data/exceptions/mercury-venus.json"
MANIFEST_PATH = HERE / "manifest.json"
CSV_PATH = HERE / "PACKAGE_ARTIFACT_MANIFEST.csv"


def load_module(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BUILD = load_module(BUILDER_PATH, "f250_inside_persona_validator_builder")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def jd_of(value: str) -> float:
    return BUILD.LONG.BASE.jd_of(datetime.fromisoformat(value).astimezone(timezone.utc))


def body_state(jd_ut: float, body: str) -> tuple[float, float, int]:
    position, flags = swe.calc_ut(
        jd_ut,
        BUILD.LONG.PLANET_CODES[body],
        swe.FLG_MOSEPH | swe.FLG_SPEED,
    )
    return float(position[0] % 360.0), float(position[3]), int(flags)


def validate_pass(
    record: dict[str, Any], pair: list[str], label: str, errors: list[str]
) -> None:
    moment = jd_of(record["utc"])
    a_lon = body_state(moment, pair[0])[0]
    b_lon = body_state(moment, pair[1])[0]
    residual = BUILD.LONG.BASE.angular_distance(a_lon, b_lon) * 3600.0
    target = float(record["target_longitude"])
    target_delta = max(
        BUILD.LONG.BASE.angular_distance(target, a_lon),
        BUILD.LONG.BASE.angular_distance(target, b_lon),
    ) * 3600.0
    check(residual <= 0.01, f"{label}: pair root residual {residual} arcsec", errors)
    check(target_delta <= 0.01, f"{label}: stored target delta {target_delta} arcsec", errors)
    verification = record["verification"]
    check(
        float(verification["pair_residual_arcseconds"]) <= 0.01,
        f"{label}: recorded root residual exceeds tolerance",
        errors,
    )
    chart = record["chart"]
    check(
        chart["event"]["utc"] == datetime.fromisoformat(record["utc"]).astimezone(timezone.utc).isoformat(timespec="microseconds"),
        f"{label}: chart event identity drift",
        errors,
    )
    check(
        chart["ephemeris_flags"]["fallback_observed"],
        f"{label}: expected explicit Moshier fallback receipt",
        errors,
    )
    chart_path = HERE / record["chart_file"]
    check(chart_path.exists(), f"{label}: missing chart {chart_path}", errors)


def validate_persona(
    family: dict[str, Any], label: str, errors: list[str]
) -> None:
    lifecycle = family["persona_lifecycle"]
    status = lifecycle["status"]
    persona = family["persona"]
    overlay = family["radix_persona_overlay"]
    if status == BUILD.ELIGIBLE:
        check(persona is not None, f"{label}: eligible persona missing", errors)
        check(overlay is not None, f"{label}: eligible overlay missing", errors)
        if persona is None:
            return
        candidate = lifecycle["persona_candidate"]
        target = float(persona["target_longitude"])
        event_jd = jd_of(candidate["utc"])
        sun_lon = body_state(event_jd, "Sun")[0]
        residual = BUILD.LONG.BASE.angular_distance(sun_lon, target) * 3600.0
        check(residual <= 0.01, f"{label}: persona solar residual {residual}", errors)
        gate = lifecycle["successor_gate"]
        check(gate is not None, f"{label}: missing successor gate", errors)
        if gate:
            check(
                event_jd < jd_of(gate["successor_first_pass_utc"]),
                f"{label}: eligible candidate does not precede successor",
                errors,
            )
            check(
                gate["candidate_precedes_successor"] is True,
                f"{label}: eligible gate flag false",
                errors,
            )
        files = persona["chart_files"]
        check(len(files) == 2, f"{label}: eligible persona needs two chart files", errors)
        for relative in files:
            check((HERE / relative).exists(), f"{label}: missing {relative}", errors)
        fast_scope = overlay["seed_to_persona_change_gate"].get("fast_body_scope", {})
        check(
            fast_scope.get("bodies") == ["Mercury", "Venus", "Mars"],
            f"{label}: fast-body change gate missing",
            errors,
        )
    elif status == BUILD.SUPERSEDED:
        check(persona is None, f"{label}: successor-collision persona was rendered", errors)
        check(overlay is None, f"{label}: successor-collision overlay was rendered", errors)
        candidate = lifecycle["persona_candidate"]
        gate = lifecycle["successor_gate"]
        check(candidate is not None and gate is not None, f"{label}: supersession receipt incomplete", errors)
        if candidate and gate:
            check(
                jd_of(candidate["utc"]) >= jd_of(gate["successor_first_pass_utc"]),
                f"{label}: successor-collision candidate actually precedes successor",
                errors,
            )
            check(
                gate["candidate_precedes_successor"] is False,
                f"{label}: successor-collision gate flag true",
                errors,
            )
        check(
            "explicit gate result" in lifecycle["meaning"],
            f"{label}: missing explicit gate-result wording",
            errors,
        )
    elif status == BUILD.NO_SUCCESSOR:
        check(persona is None, f"{label}: bracketing persona was rendered", errors)
        check(overlay is None, f"{label}: bracketing overlay was rendered", errors)
        check(
            lifecycle["persona_candidate"] is None,
            f"{label}: bracketing candidate should be withheld",
            errors,
        )
        check(
            family["identity"]["window_role"] == "first_after_window",
            f"{label}: no-successor family is not bracketing-only",
            errors,
        )
    else:
        errors.append(f"{label}: unknown persona status {status}")


def current_artifacts() -> list[dict[str, Any]]:
    paths = sorted(
        path
        for path in HERE.rglob("*")
        if path.is_file()
        and path not in {MANIFEST_PATH, CSV_PATH}
        and "__pycache__" not in path.parts
    )
    return [
        {
            "path": str(path.relative_to(HERE)),
            **BUILD.artifact_metadata(path),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in paths
    ]


def main() -> int:
    errors: list[str] = []
    for required in (INDEX_PATH, MV_PATH, MANIFEST_PATH, CSV_PATH):
        check(required.exists(), f"missing required artifact {required}", errors)
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    family_paths = sorted(FAMILY_DIR.glob("*.json"))
    check(index["schema"] == BUILD.SCHEMA, "index schema mismatch", errors)
    check(index["status"] == BUILD.STATUS, "index status mismatch", errors)
    check(len(family_paths) == 55, f"expected 55 family files, found {len(family_paths)}", errors)
    check(len(index["families"]) == 55, "index family count mismatch", errors)

    status_counts = {BUILD.ELIGIBLE: 0, BUILD.SUPERSEDED: 0, BUILD.NO_SUCCESSOR: 0}
    total_passes = 0
    multipass_count = 0
    observed_ids: set[str] = set()
    persona_paths: list[str] = []
    index_by_id = {row["seed_family_id"]: row for row in index["families"]}
    for path in family_paths:
        family = json.loads(path.read_text(encoding="utf-8"))
        identity = family["identity"]
        family_id = identity["seed_family_id"]
        label = family_id
        observed_ids.add(family_id)
        check(family["schema"] == BUILD.SCHEMA, f"{label}: schema mismatch", errors)
        check(family["status"] == BUILD.STATUS, f"{label}: status mismatch", errors)
        check(
            family["persona_lifecycle"]["one_shared_persona_maximum"] is True,
            f"{label}: one-persona maximum weakened",
            errors,
        )
        boundary = family["authority_boundary"]
        for field in (
            "official_research_evidence",
            "event_proof",
            "timing_or_forecast_authority",
            "plot_ownership",
            "independent_vote",
            "live_vault_promotion",
        ):
            check(boundary[field] is False, f"{label}: authority field {field} weakened", errors)
        check(
            boundary["astrology_reference_only"] is True,
            f"{label}: Astrology Reference fence weakened",
            errors,
        )
        passes = family["exact_passes"]
        total_passes += len(passes)
        multipass_count += len(passes) > 1
        check(
            identity["provisional_display_anchor_pass_id"] == passes[0]["pass_id"],
            f"{label}: provisional display anchor is not earliest pass",
            errors,
        )
        check(
            family["anchor_decision"]["proposed_pass_id"] == passes[0]["pass_id"],
            f"{label}: anchor decision drift",
            errors,
        )
        expected_review = (
            "proposed_earliest_pass_pending_human_disposition"
            if len(passes) > 1
            else "unambiguous_single_pass_coordinate_pending_clock_adoption"
        )
        check(
            family["anchor_decision"]["review_status"] == expected_review,
            f"{label}: anchor review status drift",
            errors,
        )
        for position, record in enumerate(passes):
            validate_pass(record, identity["pair"], f"{label}/p{position + 1}", errors)
        status = family["persona_lifecycle"]["status"]
        if status in status_counts:
            status_counts[status] += 1
        if family["persona"]:
            persona_paths.extend(family["persona"]["chart_files"])
        index_row = index_by_id.get(family_id)
        check(index_row is not None, f"{label}: missing from index", errors)
        if index_row:
            check(index_row["persona_status"] == status, f"{label}: index status drift", errors)
            check(index_row["pass_count"] == len(passes), f"{label}: index pass count drift", errors)
            check(
                index_row["data_file"] == f"data/families/{family_id}.json",
                f"{label}: index data route drift",
                errors,
            )
        validate_persona(family, label, errors)

    check(total_passes == 73, f"expected 73 exact passes, found {total_passes}", errors)
    check(multipass_count == 7, f"expected 7 multipass families, found {multipass_count}", errors)
    check(status_counts[BUILD.ELIGIBLE] == 35, f"eligible count {status_counts[BUILD.ELIGIBLE]}", errors)
    check(
        status_counts[BUILD.SUPERSEDED] == 3,
        f"successor-collision count {status_counts[BUILD.SUPERSEDED]}",
        errors,
    )
    check(status_counts[BUILD.NO_SUCCESSOR] == 17, f"bracketing count {status_counts[BUILD.NO_SUCCESSOR]}", errors)
    check(set(index_by_id) == observed_ids, "index-to-family identity parity failed", errors)
    check(len(persona_paths) == len(set(persona_paths)) == 70, "persona chart paths are not unique", errors)
    check(
        index["coverage"]["persona_status_counts"] == status_counts,
        "index persona status summary drift",
        errors,
    )
    expected_successor_collisions = {
        "mercury-uranus-2025",
        "venus-jupiter-2025",
        "venus-uranus-2025",
    }
    actual_successor_collisions = {
        path.stem
        for path in family_paths
        if json.loads(path.read_text(encoding="utf-8"))["persona_lifecycle"]["status"]
        == BUILD.SUPERSEDED
    }
    check(
        actual_successor_collisions == expected_successor_collisions,
        f"successor-collision set {actual_successor_collisions}",
        errors,
    )

    mv = json.loads(MV_PATH.read_text(encoding="utf-8"))
    check(len(mv["crossings"]) == 6, "Mercury-Venus crossing count mismatch", errors)
    check(
        sum(row["window_relation"] == "in_window" for row in mv["crossings"]) == 4,
        "Mercury-Venus in-window count mismatch",
        errors,
    )
    check(
        mv["persona_lifecycle"]["status"] == BUILD.NON_PHASEABLE,
        "Mercury-Venus persona status mismatch",
        errors,
    )
    check(
        mv["persona_lifecycle"]["persona_candidate"] is None,
        "Mercury-Venus persona candidate should not exist",
        errors,
    )
    for position, record in enumerate(mv["crossings"]):
        validate_pass(record, ["Mercury", "Venus"], f"mercury-venus/x{position + 1}", errors)

    seed_files = list((HERE / "charts/seeds").glob("*.svg"))
    persona_files = list((HERE / "charts/personas").glob("*.svg"))
    overlay_files = list((HERE / "charts/overlays").glob("*.svg"))
    check(len(seed_files) == 79, f"seed chart count {len(seed_files)}", errors)
    check(len(persona_files) == 35, f"persona chart count {len(persona_files)}", errors)
    check(len(overlay_files) == 35, f"overlay chart count {len(overlay_files)}", errors)

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    required_sources = {
        str(BUILD.READING_START),
        str(BUILD.DECISION_LOG),
        str(BUILD.RELATIONSHIP_METHOD),
        str(BUILD.LONG.PERSONA_METHOD_PATH),
    }
    check(
        required_sources.issubset(manifest["source_hashes"]),
        "governing method sources are not all pinned",
        errors,
    )
    for raw_path, expected_hash in manifest["source_hashes"].items():
        source = Path(raw_path)
        check(source.exists(), f"manifest source missing {source}", errors)
        if source.exists():
            check(sha256(source) == expected_hash, f"source hash drift {source}", errors)
    actual_artifacts = current_artifacts()
    for row in actual_artifacts:
        for field in (
            "artifact_role",
            "custody_class",
            "producer",
            "rebuildability",
            "search_visibility",
        ):
            check(bool(row[field]), f"artifact {row['path']} missing {field}", errors)
    check(
        manifest["artifacts"] == actual_artifacts,
        "artifact manifest differs from current package files",
        errors,
    )
    with CSV_PATH.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        check(
            set(reader.fieldnames or [])
            == {
                "relative_path",
                "bytes",
                "sha256",
                "custody_class",
                "artifact_role",
                "producer_path",
                "rebuildability",
                "search_visibility",
            },
            "CSV custody manifest columns do not match Workbench schema",
            errors,
        )
        csv_rows = list(reader)
    normalized_csv = [
        {
            "relative_path": row["relative_path"],
            "bytes": int(row["bytes"]),
            "sha256": row["sha256"],
            "custody_class": row["custody_class"],
            "artifact_role": row["artifact_role"],
            "producer_path": row["producer_path"],
            "rebuildability": row["rebuildability"],
            "search_visibility": row["search_visibility"],
        }
        for row in csv_rows
    ]
    check(
        normalized_csv == BUILD.delegation_rows(actual_artifacts),
        "CSV custody manifest mismatch",
        errors,
    )

    if errors:
        print(f"FAIL {len(errors)} error(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "PASS families=55 passes=73 conjunction_charts=79 "
        "personas=35 successor_collisions=3 bracketing=17 mercury_venus=6"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
