#!/usr/bin/env python3
"""Build the controlled Mars-to-planetary-node corridor around the 2026 Aries Full Moon."""

from __future__ import annotations

import argparse
import datetime as dt
import json
from collections import Counter
from pathlib import Path
from zoneinfo import ZoneInfo

import swisseph as swe


HERE = Path(__file__).resolve().parent
DEFAULT_OUT = HERE / "mars_planetary_node_corridor.json"
import sys as _sys  # noqa: E402
if str(HERE) not in _sys.path:
    _sys.path.insert(0, str(HERE))
from swiss_ephemeris import FLAGS, EPHEMERIS_LABEL  # noqa: E402  2026-09-25: Swiss/JPL files, never silent Moshier
ET = ZoneInfo("America/New_York")
UTC = dt.timezone.utc
SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces",
]
NODE_BODIES = {
    "Jupiter": swe.JUPITER,
    "Pluto": swe.PLUTO,
    "Saturn": swe.SATURN,
    "Neptune": swe.NEPTUNE,
}


def parse(value: str) -> dt.datetime:
    moment = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if moment.tzinfo is None:
        raise ValueError("moment must be timezone-aware")
    return moment.astimezone(UTC)


def jd(moment: dt.datetime) -> float:
    moment = moment.astimezone(UTC)
    hour = (
        moment.hour
        + moment.minute / 60
        + moment.second / 3600
        + moment.microsecond / 3_600_000_000
    )
    return swe.julday(moment.year, moment.month, moment.day, hour)


def moment_from_jd(value: float) -> dt.datetime:
    year, month, day, hour = swe.revjul(value, swe.GREG_CAL)
    return dt.datetime(year, month, day, tzinfo=UTC) + dt.timedelta(hours=hour)


def signed_delta(a: float, b: float) -> float:
    return ((a - b + 180.0) % 360.0) - 180.0


def position(moment: dt.datetime, body: int) -> float:
    return swe.calc_ut(jd(moment), body, FLAGS)[0][0] % 360.0


def ascending_node(moment: dt.datetime, body: int) -> float:
    return swe.nod_aps_ut(jd(moment), body, swe.NODBIT_OSCU)[0][0] % 360.0


def mars_node_delta(moment: dt.datetime, body: int) -> tuple[float, float, float]:
    mars = position(moment, swe.MARS)
    node = ascending_node(moment, body)
    return signed_delta(mars, node), mars, node


def degree_record(longitude: float) -> dict[str, object]:
    longitude %= 360.0
    sign_index = int(longitude // 30)
    degree = longitude % 30.0
    total_seconds = round(degree * 3600.0)
    d, rem = divmod(total_seconds, 3600)
    minute, second = divmod(rem, 60)
    return {
        "longitude_deg": round(longitude, 9),
        "sign": SIGNS[sign_index],
        "degree_in_sign": round(degree, 9),
        "dms": f"{d}°{minute:02d}′{second:02d}″ {SIGNS[sign_index]}",
    }


def exact_crossings(
    start: dt.datetime, end: dt.datetime, *, step: dt.timedelta = dt.timedelta(hours=1)
) -> list[dict[str, object]]:
    crossings: list[dict[str, object]] = []
    for node_body, planet_code in NODE_BODIES.items():
        roots: list[dt.datetime] = []
        previous_time = start
        previous_delta = mars_node_delta(start, planet_code)[0]
        cursor = start + step
        while cursor <= end:
            delta = mars_node_delta(cursor, planet_code)[0]
            if previous_delta * delta < 0.0 and abs(previous_delta - delta) < 10.0:
                low, high = previous_time, cursor
                low_delta = previous_delta
                for _ in range(64):
                    middle = low + (high - low) / 2
                    middle_delta = mars_node_delta(middle, planet_code)[0]
                    if low_delta * middle_delta <= 0.0:
                        high = middle
                    else:
                        low = middle
                        low_delta = middle_delta
                roots.append(low + (high - low) / 2)
            previous_time = cursor
            previous_delta = delta
            cursor += step
        if len(roots) != 1:
            raise RuntimeError(f"expected one Mars/{node_body} NN crossing, got {len(roots)}")
        moment = roots[0]
        residual, mars, node = mars_node_delta(moment, planet_code)
        crossings.append(
            {
                "node_body": node_body,
                "node_kind": "ascending",
                "exact_utc": moment.isoformat(timespec="microseconds").replace("+00:00", "Z"),
                "exact_local": moment.astimezone(ET).isoformat(timespec="microseconds"),
                "mars": degree_record(mars),
                "node": degree_record(node),
                "residual_arcsec": round(abs(residual) * 3600.0, 6),
            }
        )
    crossings.sort(key=lambda row: row["exact_utc"])
    return crossings


def chart_hit_control() -> dict[str, object]:
    index = json.loads((HERE / "chart_reading_bones" / "index.json").read_text())
    hits: list[dict[str, object]] = []
    for chart in index["charts"]:
        path = HERE / "chart_reading_bones" / f"{chart['id']}.json"
        bone = json.loads(path.read_text())
        for hit in bone.get("node_hits", []):
            hits.append({"chart_id": chart["id"], **hit})
    flags = Counter("unflagged" if hit.get("flag") is None else hit["flag"] for hit in hits)
    mars_hits = [hit for hit in hits if hit["planet"] == "Mars"]
    return {
        "registered_chart_count": len(index["charts"]),
        "all_node_hit_count": len(hits),
        "flag_counts": dict(sorted(flags.items())),
        "mars_node_hit_count": len(mars_hits),
        "mars_node_hits": mars_hits,
        "control_boundary": (
            "The Full-Moon Mars/Saturn-node hit is one of five Mars-node snapshots "
            "and one of thirty planetary-node hits in the registered thirty-chart corpus."
        ),
    }


def interval_hours(a: dt.datetime, b: dt.datetime) -> float:
    return round((b - a).total_seconds() / 3600.0, 6)


def build_payload() -> dict[str, object]:
    choreography = json.loads((HERE / "aries_mars_pluto_choreography.json").read_text())
    event_by_id = {event["event_id"]: event for event in choreography["events"]}
    full_moon = parse(event_by_id["aries-full-moon"]["exact_utc"])
    mars_enters_leo = parse(event_by_id["mars-enters-leo"]["exact_utc"])
    opposition = parse(event_by_id["mars-opposite-pluto"]["exact_utc"])
    virgo_new = parse(json.loads((HERE / "chart_reading_bones" / "lun-2026-09-11-ne.json").read_text())["utc"])
    taurus_full = parse(json.loads((HERE / "chart_reading_bones" / "lun-2026-10-26-fu.json").read_text())["utc"])

    crossings = exact_crossings(
        dt.datetime(2026, 9, 1, tzinfo=UTC),
        dt.datetime(2026, 11, 15, tzinfo=UTC),
    )
    by_body = {row["node_body"]: row for row in crossings}
    crossing_times = {body: parse(row["exact_utc"]) for body, row in by_body.items()}

    full_delta, full_mars, full_saturn_node = mars_node_delta(full_moon, swe.SATURN)
    opp_delta, opp_mars, opp_saturn_node = mars_node_delta(opposition, swe.SATURN)
    cancer_nodes = [by_body[name]["node"]["longitude_deg"] for name in ["Jupiter", "Pluto", "Saturn"]]

    return {
        "schema": "freedom250.mars-planetary-node-corridor/v1",
        "status": "generated_context_zero_evidence_or_forecast_credit",
        "title": "Mars crosses the collective-node corridor — September to October 2026",
        "method": {
            "frame": "geocentric tropical ecliptic longitude",
            "ephemeris": EPHEMERIS_LABEL,
            "planet_flags": "FLG_SWIEPH | FLG_SPEED",
            "node_method": "swe.nod_aps_ut with NODBIT_OSCU",
            "root_condition": "Mars longitude equals the epoch-specific osculating ascending-node longitude",
            "scan_step_hours": 1,
            "root_refinement": "64-step bisection",
            "chart_bone_orb_policy_deg": 2.5,
        },
        "exact_crossings": crossings,
        "anchor_sequence": [
            {"event": "Virgo New Moon", "utc": virgo_new.isoformat(), "role": "governing lunar chapter opens"},
            {"event": "Mars conjunct Jupiter NN", "utc": by_body["Jupiter"]["exact_utc"]},
            {"event": "Mars conjunct Pluto NN", "utc": by_body["Pluto"]["exact_utc"]},
            {"event": "Aries Full Moon", "utc": full_moon.isoformat(), "role": "eclipse-family Full phase"},
            {"event": "Mars conjunct Saturn NN", "utc": by_body["Saturn"]["exact_utc"]},
            {"event": "Mars enters Leo", "utc": mars_enters_leo.isoformat()},
            {"event": "Mars opposite Pluto", "utc": opposition.isoformat()},
            {"event": "Mars conjunct Neptune NN", "utc": by_body["Neptune"]["exact_utc"]},
            {"event": "Taurus Full Moon", "utc": taurus_full.isoformat(), "role": "next registered Full Moon"},
        ],
        "intervals_hours": {
            "virgo_new_to_jupiter_node": interval_hours(virgo_new, crossing_times["Jupiter"]),
            "jupiter_node_to_pluto_node": interval_hours(crossing_times["Jupiter"], crossing_times["Pluto"]),
            "pluto_node_to_full_moon": interval_hours(crossing_times["Pluto"], full_moon),
            "full_moon_to_saturn_node": interval_hours(full_moon, crossing_times["Saturn"]),
            "saturn_node_to_mars_enters_leo": interval_hours(crossing_times["Saturn"], mars_enters_leo),
            "saturn_node_to_opposition": interval_hours(crossing_times["Saturn"], opposition),
            "opposition_to_neptune_node": interval_hours(opposition, crossing_times["Neptune"]),
            "neptune_node_to_taurus_full_moon": interval_hours(crossing_times["Neptune"], taurus_full),
            "entire_jupiter_to_neptune_corridor": interval_hours(crossing_times["Jupiter"], crossing_times["Neptune"]),
        },
        "full_moon_saturn_node_snapshot": {
            "mars": degree_record(full_mars),
            "saturn_ascending_node": degree_record(full_saturn_node),
            "orb_deg": round(abs(full_delta), 6),
            "inside_chart_bone_orb": abs(full_delta) <= 2.5,
        },
        "opposition_saturn_node_snapshot": {
            "mars": degree_record(opp_mars),
            "saturn_ascending_node": degree_record(opp_saturn_node),
            "orb_deg": round(abs(opp_delta), 6),
            "inside_chart_bone_orb": abs(opp_delta) <= 2.5,
        },
        "clustering_control": {
            "jupiter_pluto_saturn_nodes_all_in_cancer": True,
            "cancer_node_span_deg": round(max(cancer_nodes) - min(cancer_nodes), 6),
            "neptune_node_sign": by_body["Neptune"]["node"]["sign"],
            "deduplication_rule": (
                "Jupiter, Pluto and Saturn ascending nodes share one Cancer corridor. "
                "Mars traversing Cancer therefore creates one ordered corridor, not three independent votes."
            ),
        },
        "registered_chart_control": chart_hit_control(),
        "interpretive_boundaries": [
            "A planetary node is an epoch-specific orbital intersection coordinate, not a material body.",
            "Longitude equality does not mean Mars physically meets the node body or crosses that body's orbital plane.",
            "The inherited escalation/resolution flag is a Jones hypothesis, not an admitted event prediction.",
            "The Chronicle backtest found the Saturn/Pluto-node escalation rule null; the Neptune-node de-escalation result was suggestive but small-n and unratified.",
            "The corridor supplies one contextual continuity lane and no evidence, convergence, causation or Forecast Ledger credit.",
        ],
        "source_files": [
            "99 - Templates/aries_mars_pluto_choreography.json",
            "99 - Templates/chart_reading_bones/index.json",
            "99 - Templates/chart_reading_bones/*.json",
            "99 - Templates/backtest-2026-06-18/node_test.py",
            "00 - Index/Astrology Backtest — 2026-06-18.md",
            "_Holding/Claude memory mirror — retired 2026-10-02/memory/planetary_nodes_knowledge.md",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build_payload()
    if args.check:
        if not args.out.exists():
            raise SystemExit(f"missing generated artifact: {args.out}")
        stored = json.loads(args.out.read_text())
        if stored != payload:
            raise SystemExit("MARS PLANETARY NODE CORRIDOR CHECK: STALE")
        print("MARS PLANETARY NODE CORRIDOR CHECK: CLEAN")
        return 0
    args.out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
