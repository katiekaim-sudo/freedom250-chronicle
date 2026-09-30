#!/usr/bin/env python3
"""Build the February 2025 Pisces Moon-family comparison.

This is calculation evidence for a contextual companion reread. It leaves the
locked August 28, 2026 eclipse reading unchanged and grants astrology no
factual, causal, convergence, or Forecast Ledger credit.
"""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

import swisseph as swe

from build_aquarius_moon_family import (
    PLANETS,
    angular_distance,
    apply_governed_positions,
    calculated_chart,
    cross_chart_contacts,
    parse_utc,
    sky_separation,
)


HERE = Path(__file__).resolve().parent
HISTORY = HERE / "mundane_history.json"
LINEAGES = HERE / "moon_lineages.json"
FULL_BONE = HERE / "chart_reading_bones" / "lun-2026-08-28-fu-lunar.json"
BONES_INDEX = HERE / "chart_reading_bones" / "index.json"
ECLIPSE_LOCAL = HERE / "eclipse_local_circumstances.json"
MARS_PLUTO_CYCLE = HERE / "mars_pluto_cycle_continuity.json"
OUTPUT = HERE / "pisces_moon_family_2025_2026.json"


def node_state(chart: dict, governed_node_lon: float | None = None) -> dict:
    jd = chart["julian_day_ut"]
    node = governed_node_lon
    if node is None:
        node = swe.calc_ut(jd, swe.TRUE_NODE, swe.FLG_SWIEPH | swe.FLG_SPEED)[0][0] % 360
    south = (node + 180.0) % 360
    moon = chart["bodies"]["Moon"]
    nearest = min(angular_distance(moon["longitude_deg"], node), angular_distance(moon["longitude_deg"], south))
    return {
        "true_north_node_longitude_deg": round(node, 9),
        "true_south_node_longitude_deg": round(south, 9),
        "moon_distance_to_nearest_node_axis_deg": round(nearest, 9),
        "moon_ecliptic_latitude_deg": moon["ecliptic_latitude_deg"],
    }


def local_horizon(chart: dict) -> dict:
    above = [body for body in PLANETS if chart["bodies"][body]["true_altitude_deg"] > 0]
    return {
        "above_true_horizon": above,
        "below_or_on_true_horizon": [body for body in PLANETS if body not in above],
        "above_count": len(above),
        "below_or_on_count": len(PLANETS) - len(above),
    }


def station_after(jd_start: float, body: int, days: float = 4.0) -> dict:
    flags = swe.FLG_SWIEPH | swe.FLG_SPEED
    lo, hi = jd_start, jd_start + days
    speed = lambda jd: swe.calc_ut(jd, body, flags)[0][3]
    if speed(lo) * speed(hi) >= 0:
        raise RuntimeError("station root is not bracketed")
    for _ in range(80):
        mid = (lo + hi) / 2.0
        if speed(lo) * speed(mid) <= 0:
            hi = mid
        else:
            lo = mid
    jd = (lo + hi) / 2.0
    moment = dt.datetime(2000, 1, 1, 12, tzinfo=dt.timezone.utc) + dt.timedelta(days=jd - 2451545.0)
    return {
        "julian_day_ut": round(jd, 9),
        "exact_utc": moment.isoformat().replace("+00:00", "Z"),
        "hours_after_seed": round((jd - jd_start) * 24.0, 6),
        "direction_before": "direct" if speed(jd - 1e-4) > 0 else "retrograde",
        "direction_after": "direct" if speed(jd + 1e-4) > 0 else "retrograde",
    }


def objects(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from objects(child)
    elif isinstance(value, list):
        for child in value:
            yield from objects(child)


def distribution_control() -> list[dict]:
    index = json.loads(BONES_INDEX.read_text())
    rows = []
    for record in index["charts"]:
        date = record["date"]
        if not ("2026-06-01" <= date <= "2026-12-31"):
            continue
        bone = json.loads((HERE / "chart_reading_bones" / f"{record['id']}.json").read_text())
        rows.append({
            "chart_id": record["id"],
            "date": date,
            "shape": bone["shape"],
            "largest_empty_arc_deg": bone["empty_deg"],
            "empty_from": bone["empty_from"],
            "empty_to": bone["empty_to"],
        })
    return sorted(rows, key=lambda row: (row["date"], row["chart_id"]))


def main() -> None:
    history = json.loads(HISTORY.read_text())
    lineages = json.loads(LINEAGES.read_text())
    full_bone = json.loads(FULL_BONE.read_text())
    eclipse_local = json.loads(ECLIPSE_LOCAL.read_text())
    mars_pluto_cycle = json.loads(MARS_PLUTO_CYCLE.read_text())

    seed_source = next(row for row in history["charts"] if row["id"] == "lun-2025-02-28-ne")
    lineage = next(row for row in lineages["lineages"] if row["lineage_id"] == "pessin:lun-2025-02-28-ne")
    phase_index = {row["phase_event_id"]: row for row in lineages["phase_events"]}
    quarter_source = phase_index["lunation-2025-11-28-fq"]
    full_source = phase_index["lun-2026-08-28-fu-lunar"]

    seed = calculated_chart(parse_utc(seed_source["utc"]))
    quarter = calculated_chart(parse_utc(quarter_source["exact_utc"]))
    full = calculated_chart(parse_utc(full_source["exact_utc"]))
    seed = apply_governed_positions(
        seed,
        {row["name"]: row["lon"] for row in seed_source["points"] if row["name"] in PLANETS},
        asc=seed_source["asc"],
        mc=seed_source["mc"],
    )
    quarter = apply_governed_positions(
        quarter,
        {"Sun": quarter_source["sun_lon_deg"], "Moon": quarter_source["moon_lon_deg"]},
    )
    full = apply_governed_positions(
        full,
        {body: full_bone["pos"][body]["lon"] for body in PLANETS},
        asc=full_bone["asc"],
        mc=full_bone["mc"],
        declinations={body: full_bone["pos"][body]["dec"] for body in PLANETS},
    )

    seed_node = next(row["lon"] for row in seed_source["points"] if row["name"] == "Node")
    for chart, node in ((seed, seed_node), (quarter, None), (full, full_bone["node"]["lon"])):
        chart["node_geometry"] = node_state(chart, node)

    phase_eclipse_states = {
        "seed": bool(seed_source["eclipse"]),
        "first_quarter": bool(quarter_source["eclipse"]),
        "full": bool(full_source["eclipse"]),
    }
    first_quarter_to_full_delta = angular_distance(
        quarter["bodies"]["Moon"]["longitude_deg"],
        full["bodies"]["Moon"]["longitude_deg"],
    )
    seed_to_full_delta = angular_distance(
        seed["bodies"]["Moon"]["longitude_deg"],
        full["bodies"]["Moon"]["longitude_deg"],
    )

    control = distribution_control()
    first_splay = next(row for row in control if row["shape"] == "splay")
    prior = control[control.index(first_splay) - 1]
    local_eclipse = next(row for row in eclipse_local["events"] if row["date"] == "2026-08-28")
    venus_station = station_after(seed["julian_day_ut"], swe.VENUS)
    mars_pluto_contra = next(
        row for row in objects(mars_pluto_cycle)
        if row.get("kind") == "contra_parallel" and row.get("exact_utc", "").startswith("2026-08-26")
    )
    mars_pluto_contra = dict(mars_pluto_contra)
    mars_pluto_contra["hours_before_full_phase"] = round(
        (full["julian_day_ut"] - mars_pluto_contra["julian_day_ut"]) * 24.0, 6
    )

    result = {
        "schema": "freedom250.pisces-moon-family/v1",
        "developed_through": "2026-09-25",
        "lineage_id": lineage["lineage_id"],
        "interpretation_status_before_reread": lineage["interpretation_status"],
        "story_verdict_before_reread": lineage["story_verdict"],
        "authority_boundary": {
            "calculation": "Registered longitudes and angles inherit governed mundane_history, moon_lineages and chart-bone coordinates; Swiss Ephemeris supplies the missing First-Quarter frame and secondary quantities",
            "verification": "Astro Gold remains pending where the source registry says pending",
            "interpretation": "contextual companion only; locked Pass 1 remains unchanged",
            "evidence_credit": "zero",
        },
        "family_members": lineage["members"],
        "phase_eclipse_states": phase_eclipse_states,
        "charts": {
            "seed_2025_02_28": seed,
            "first_quarter_2025_11_28": quarter,
            "full_2026_08_28": full,
        },
        "degree_relays": {
            "seed_moon_degree_deg": round(seed["bodies"]["Moon"]["degree_in_sign"], 9),
            "first_quarter_moon_degree_deg": round(quarter["bodies"]["Moon"]["degree_in_sign"], 9),
            "full_moon_degree_deg": round(full["bodies"]["Moon"]["degree_in_sign"], 9),
            "seed_to_full_moon_delta_deg": round(seed_to_full_delta, 9),
            "first_quarter_to_full_moon_delta_deg": round(first_quarter_to_full_delta, 9),
            "meaning_boundary": "same-sign Pessin phase lineage; degree proximity describes continuity but is not an additional factual or causal vote",
        },
        "node_approach": {
            "seed_nearest_axis_deg": seed["node_geometry"]["moon_distance_to_nearest_node_axis_deg"],
            "first_quarter_nearest_axis_deg": quarter["node_geometry"]["moon_distance_to_nearest_node_axis_deg"],
            "full_nearest_axis_deg": full["node_geometry"]["moon_distance_to_nearest_node_axis_deg"],
            "finding": "an ordinary non-eclipse seed reaches Full phase as a visible partial lunar eclipse; the shadow condition arrives at harvest rather than persisting from the seed",
        },
        "root_handoff": {
            "seed": {
                "chart_ruler": "Venus",
                "chart_ruler_condition": "Venus in Aries, detriment, slowing toward retrograde station",
                "terminal_structure": seed["dispositors"],
                "venus_station": venus_station,
            },
            "first_quarter": {
                "terminal_structure": quarter["dispositors"],
            },
            "full": {
                "chart_ruler": "Mercury",
                "chart_ruler_condition": "Mercury in Virgo, domicile and exaltation, combust",
                "terminal_structure": full["dispositors"],
            },
            "finding": "the family moves from a Jupiter-Mercury circuit under a compromised stationing Venus, through a Jupiter-Moon circuit, into independent Mercury and Venus finals: record and value become separately authoritative at harvest",
        },
        "cross_chart_contacts_within_1_5_deg": {
            "seed_to_first_quarter": cross_chart_contacts(seed, quarter, 1.5),
            "seed_to_full": cross_chart_contacts(seed, full, 1.5),
            "first_quarter_to_full": cross_chart_contacts(quarter, full, 1.5),
        },
        "house_migrations": {
            body: [
                seed["bodies"][body]["whole_sign_house"],
                quarter["bodies"][body]["whole_sign_house"],
                full["bodies"][body]["whole_sign_house"],
            ]
            for body in PLANETS
        },
        "astronomical_geometry": {
            "local_horizon": {
                "seed": local_horizon(seed),
                "first_quarter": local_horizon(quarter),
                "full": local_horizon(full),
            },
            "full_phase": {
                "sun_mercury_true_sky_separation_deg": round(sky_separation(full["bodies"]["Sun"], full["bodies"]["Mercury"]), 6),
                "moon_uranus_true_sky_separation_deg": round(sky_separation(full["bodies"]["Moon"], full["bodies"]["Uranus"]), 6),
                "moon_true_altitude_deg": full["bodies"]["Moon"]["true_altitude_deg"],
                "washington_visible": local_eclipse["washington"]["visible"],
                "washington_local_type": local_eclipse["washington"]["local_type"],
                "washington_moon_altitude_at_maximum_deg": local_eclipse["washington"]["moon_true_altitude_at_global_max_deg"],
                "washington_partial_phase_minutes": local_eclipse["washington"]["partial_phase"]["minutes_above_horizon"],
                "umbral_magnitude": local_eclipse["global"]["umbral_magnitude"],
            },
            "scale_boundary": "geocentric geometry, eclipse visibility and local altitude provide physical context only; they do not prove causation or assign interpretive weight",
        },
        "declination_bridge": {
            "exact_mars_pluto_contra_parallel": mars_pluto_contra,
            "eclipse_chart_orb_deg": next(
                row["orb_deg"] for row in full["declination_relationships_within_1_deg"]
                if row["a"] == "Mars" and row["b"] == "Pluto" and row["kind"] == "contra_parallel"
            ),
            "finding": "the later Mars-Pluto confrontation enters the Pisces eclipse through declination before it becomes a longitude opposition in October; this is one relationship history, not another vote",
        },
        "distribution_control": {
            "registered_charts_2026_06_through_12": control,
            "first_splay_chart": first_splay,
            "immediately_prior_chart": prior,
            "largest_gap_contraction_into_first_splay_deg": round(prior["largest_empty_arc_deg"] - first_splay["largest_empty_arc_deg"], 6),
            "finding": "August 28 is the first registered splay frame in the late-2026 sequence, but it follows a gradual locomotive contraction and does not establish that the eclipse caused the classification change",
        },
        "dual_family_position": {
            "long_family": "Full phase of the 2025-02-28 Pisces New Moon family",
            "monthly_eclipse_chapter": "disclosure point inside the 2026-08-12 Leo total-solar-eclipse month",
            "boundary": "two legitimate clocks, not duplicate confirmations",
        },
        "factual_comparison": {
            "research_id": "fraud-payment-integrity",
            "path": "Research Packages/Fraud and Payment Integrity/FEDERAL_FUNDS_LEDGER_ADOPTION_WATCHBOARD_2026-07-23.md",
            "seed_object": "EO 14222 signed 2025-02-26: centralized payment-justification, pause, review and maximum-practicable publication architecture for covered contract and grant payments",
            "maturation": "a bounded HHS Payment Management System public feed and API became operational; OMB later proposed technology-neutral payment-justification and prepayment-control rules for federal assistance",
            "open_gates": "government-wide coverage, final OMB rule, exact agency implementations, correction lineage and any distributed-ledger specification remain separate and unresolved",
            "selection_boundary": "source-first factual chain selected independently of the astrology; same-object and adjacent-policy steps are not merged",
        },
        "source_paths": [
            "99 - Templates/mundane_history.json",
            "99 - Templates/moon_lineages.json",
            "99 - Templates/chart_reading_bones/lun-2026-08-28-fu-lunar.json",
            "99 - Templates/eclipse_local_circumstances.json",
            "99 - Templates/mars_pluto_cycle_continuity.json",
        ],
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {OUTPUT}")
    print(f"Seed -> Full Moon degree drift: {seed_to_full_delta:.6f}°")
    print(f"First Quarter -> Full Moon degree drift: {first_quarter_to_full_delta:.6f}°")
    print(f"Node approach: {result['node_approach']}")


if __name__ == "__main__":
    main()
