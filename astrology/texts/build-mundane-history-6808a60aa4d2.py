#!/usr/bin/env python3
"""Build the continuous Washington, D.C. mundane-history chart catalog.

The catalog begins with Donald Trump's first inauguration and continues through
January 2029.  It contains every exact New/Full Moon,
eclipses as a typed subset of those syzygies, every cardinal solar ingress, and
both 2016 ingress parents needed to show the actual governing chain into
inauguration day.  It is factual chart infrastructure, not a reading or an
event ledger.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import swisseph as swe

import mundane_engine as ME
from america import available as america_available
from chart_conventions import DC_LABEL, DC_LAT, DC_LON
from minor_points import all_points
from wheel_lib import placidus_cusps


HERE = Path(__file__).resolve().parent
VAULT = HERE.parent
OUT = HERE / "mundane_history.json"
REGISTRY = VAULT / "03 - Astrology" / "chart_reading_registry.json"
BONES_INDEX = HERE / "chart_reading_bones" / "index.json"
EPHE = HERE / "ephe"

SCHEMA = "freedom250.mundane-history/v1"
START = "2016-12-21"
EVIDENCE_START = "2017-01-20"
END = "2029-01-31"
CONTEXT_INGRESSES = {(2016, "Libra"), (2016, "Capricorn")}
FIRST_TERM_START_UTC = dt.datetime(2017, 1, 20, 17, 0, tzinfo=dt.timezone.utc)
FIRST_TERM_END_UTC = dt.datetime(2021, 1, 20, 17, 0, tzinfo=dt.timezone.utc)
CARDINAL = ("Aries", "Cancer", "Libra", "Capricorn")
PLANET_ORDER = tuple(ME.PLANETS)
DC_TZ = ZoneInfo("America/New_York")


def iso_from_jd(jd: float) -> str:
    year, month, day, hour = swe.revjul(jd, swe.GREG_CAL)
    moment = dt.datetime(year, month, day, tzinfo=dt.timezone.utc) + dt.timedelta(hours=hour)
    return moment.isoformat(timespec="microseconds")


def sign_of(longitude: float) -> str:
    return ME.SIGNS[int((((longitude % 360) + 1e-6) % 360) // 30) % 12]


def dms(longitude: float) -> str:
    seconds = int(round((longitude % 30) * 3600))
    if seconds >= 30 * 3600:
        seconds = 0
    degree, remainder = divmod(seconds, 3600)
    minute, second = divmod(remainder, 60)
    return f"{degree}°{minute:02d}′{second:02d}″"


def roots(positions: dict[str, dict[str, Any]]) -> list[str]:
    found: set[str] = set()
    for start in PLANET_ORDER:
        chain: list[str] = []
        current = start
        while current not in chain:
            chain.append(current)
            ruler = ME.RULER[positions[current]["sign"]]
            if ruler == current:
                found.add(current)
                break
            current = ruler
        else:
            found.update(chain[chain.index(current):])
    return sorted(found)


def chart_facts(jd: float, *, exact_sun: float | None = None) -> dict[str, Any]:
    positions: dict[str, dict[str, Any]] = {}
    points: list[dict[str, Any]] = []
    flags = swe.FLG_SWIEPH | swe.FLG_SPEED
    for name, body_id in ME.PLANETS.items():
        result = swe.calc_ut(jd, body_id, flags)[0]
        lon = (exact_sun if name == "Sun" and exact_sun is not None else float(result[0])) % 360
        row = {
            "lon": round(lon, 9), "sign": sign_of(lon), "dms": dms(lon),
            "speed": round(float(result[3]), 9), "retro": bool(result[3] < 0),
        }
        positions[name] = row
        points.append({"name": name, **row, "group": "planet"})
    extras = all_points(jd)
    for name in ("Chiron", "Node"):
        lon, speed = extras[name]
        group = "chiron" if name == "Chiron" else "node"
        row = {
            "name": name, "lon": round(lon % 360, 9), "sign": sign_of(lon),
            "dms": dms(lon), "speed": round(float(speed), 9),
            "retro": bool(speed < 0), "group": group,
        }
        points.append(row)
        if name == "Node":
            south = (lon + 180) % 360
            points.append({"name": "SNode", "lon": round(south, 9), "sign": sign_of(south),
                           "dms": dms(south), "speed": round(float(speed), 9),
                           "retro": bool(speed < 0), "group": "node"})
    america_lon, america_speed = extras["America"]
    points.append({"name": "America", "lon": round(america_lon % 360, 9),
                   "sign": sign_of(america_lon), "dms": dms(america_lon),
                   "speed": round(float(america_speed), 9),
                   "retro": bool(america_speed < 0), "group": "america"})
    _cusps, ascmc = swe.houses(jd, DC_LAT, DC_LON, b"P")
    placidus, mc = placidus_cusps(jd, DC_LAT, DC_LON)
    asc = float(ascmc[0]) % 360
    return {
        "jd_ut": round(jd, 9), "utc": iso_from_jd(jd),
        "local": dt.datetime.fromisoformat(iso_from_jd(jd)).astimezone(DC_TZ).isoformat(),
        "asc": round(asc, 9), "asc_sign": sign_of(asc), "mc": round(mc, 9),
        "placidus_cusps": [round(float(value), 9) for value in placidus],
        "points": points, "root_members": roots(positions),
    }


def eclipse_meta(jd: float, kind: str) -> dict[str, Any] | None:
    if kind == "new":
        flags, times = swe.sol_eclipse_when_glob(jd - 1.0, swe.FLG_SWIEPH, 0)
        family = "solar"
    else:
        flags, times = swe.lun_eclipse_when(jd - 1.0, swe.FLG_SWIEPH, 0)
        family = "lunar"
    greatest = float(times[0])
    if abs(greatest - jd) >= 1.0:
        return None
    if flags & swe.ECL_TOTAL:
        eclipse_type = "Total"
    elif flags & swe.ECL_ANNULAR:
        eclipse_type = "Annular"
    elif flags & swe.ECL_ANNULAR_TOTAL:
        eclipse_type = "Hybrid"
    elif flags & swe.ECL_PARTIAL:
        eclipse_type = "Partial"
    else:
        eclipse_type = "Penumbral"
    return {"family": family, "type": eclipse_type, "greatest_utc": iso_from_jd(greatest)}


def source_maps() -> tuple[dict[str, str], dict[str, dict[str, Any]]]:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    sources = {row["id"]: row["source"] for row in registry.get("readings", []) if row.get("source")}
    bones = json.loads(BONES_INDEX.read_text(encoding="utf-8"))
    meta = {row["id"]: row for row in bones.get("charts", [])}
    return sources, meta


def registered_jd(chart_id: str, computed_jd: float, bones: dict[str, dict[str, Any]]) -> float:
    """A registered chart keeps its registered instant (DR-080).

    The chart-reading bones are frozen chart facts cast before the DE441 switch; their
    instants differ from a fresh DE441 solve by a few hundredths of a second.  Adopting
    the registered instant gives every consumer (stacks, packets, Studio Desk) one clock.
    """
    path = BONES_INDEX.parent / f"{chart_id}.json"
    if chart_id not in bones or not path.is_file():
        return computed_jd
    jd = float(json.loads(path.read_text(encoding="utf-8"))["jd"])
    if abs(jd - computed_jd) * 86400.0 > 5.0:
        raise ValueError(f"registered instant for {chart_id} is {abs(jd - computed_jd) * 86400.0:.1f}s from the solve")
    return jd


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def term_membership(utc_iso: str) -> bool:
    moment = dt.datetime.fromisoformat(utc_iso)
    return FIRST_TERM_START_UTC <= moment < FIRST_TERM_END_UTC


def provenance(chart_id: str, reading_sources: dict[str, str], bones: dict[str, dict[str, Any]]) -> dict[str, Any]:
    return {
        "calculation_authority": "Swiss Ephemeris exact chart calculation · 99 - Templates/build_mundane_history.py",
        "reading_source": reading_sources.get(chart_id),
        "verification": {
            "calculation": "computed_exact",
            "existing_bone": "matched" if chart_id in bones else "not_registered",
            "astro_gold": "pending",
        },
    }


def governing_sequence(year: int, ingress_by_id: dict[str, dict[str, Any]]) -> list[str]:
    sequence: list[str] = []
    index = 0
    while index < len(CARDINAL):
        chart_id = f"ingress-{year}-{CARDINAL[index].lower()}"
        sequence.append(chart_id)
        modality = ingress_by_id[chart_id]["asc_modality"]
        if modality == "fixed":
            break
        index += 2 if modality == "cardinal" else 1
    return sequence


def strict_governor(jd: float, ingress_by_id: dict[str, dict[str, Any]]) -> str:
    year = int(iso_from_jd(jd)[:4])
    aries_candidates = [ingress_by_id[f"ingress-{candidate}-aries"] for candidate in (year - 1, year)
                        if f"ingress-{candidate}-aries" in ingress_by_id and ingress_by_id[f"ingress-{candidate}-aries"]["jd_ut"] <= jd]
    if not aries_candidates:
        raise ValueError(f"No Aries ingress available before {iso_from_jd(jd)}")
    aries = max(aries_candidates, key=lambda row: row["jd_ut"])
    aries_year = int(aries["year"])
    candidates = [ingress_by_id[chart_id] for chart_id in governing_sequence(aries_year, ingress_by_id)
                  if ingress_by_id[chart_id]["jd_ut"] <= jd]
    return max(candidates, key=lambda row: row["jd_ut"])["id"]


def build() -> dict[str, Any]:
    swe.set_ephe_path(str(EPHE))
    america_ok, america_message = america_available()
    if not america_ok:
        raise ValueError(america_message)
    sources, bones = source_maps()
    charts: list[dict[str, Any]] = []
    ingress_by_id: dict[str, dict[str, Any]] = {}
    final_year = int(END[:4])
    for year in range(2016, final_year + 1):
        for sign in CARDINAL:
            chart_id = f"ingress-{year}-{sign.lower()}"
            jd = registered_jd(chart_id, ME.ingress_jd(year, sign), bones)
            facts = chart_facts(jd, exact_sun=ME.SIGNS.index(sign) * 30.0)
            row = {
                "id": chart_id, "chart_type": "ingress", "year": year, "sign": sign,
                "date": facts["local"][:10], "label": f"{year} {sign} Ingress",
                **provenance(chart_id, sources, bones),
                "aliases": [],
                "first_term": term_membership(facts["utc"]),
                "first_term_context": (year, sign) in CONTEXT_INGRESSES,
                "in_primary_window": START <= facts["local"][:10] <= END,
                "context_parent": (year, sign) in CONTEXT_INGRESSES,
                "asc_modality": ME.MODALITY[ME.SIGNS.index(facts["asc_sign"]) % 3],
                "validity_months": ME.validity_months(ME.MODALITY[ME.SIGNS.index(facts["asc_sign"]) % 3]),
                **facts,
            }
            ingress_by_id[chart_id] = row
            if row["in_primary_window"] or row["context_parent"]:
                charts.append(row)

    governing_ids = {chart_id for year in range(2016, final_year + 1)
                     for chart_id in governing_sequence(year, ingress_by_id)}
    for row in ingress_by_id.values():
        row["standing"] = "governing" if row["id"] in governing_ids else "nested_cardinal_stage"

    lunations = ME.lunations(START, END)
    for raw in lunations:
        eclipse = eclipse_meta(float(raw["jd"]), raw["kind"])
        suffix = "ne" if raw["kind"] == "new" else "fu"
        if eclipse:
            suffix += "-solar" if raw["kind"] == "new" else "-lunar"
        chart_id = f"lun-{raw['date']}-{suffix}"
        facts = chart_facts(registered_jd(chart_id, float(raw["jd"]), bones))
        phase = "New Moon" if raw["kind"] == "new" else "Full Moon"
        local_date = facts["local"][:10]
        label = f"{local_date} {raw['sign']} " + (f"{eclipse['family'].title()} Eclipse" if eclipse else phase)
        aliases = sorted({f"lunation-{raw['date']}", f"lunation-{local_date}"} - {chart_id})
        row = {
            "id": chart_id, "chart_type": "lunation", "kind": raw["kind"],
            "phase": phase, "date": facts["local"][:10], "utc_date": raw["date"],
            "sign": raw["sign"], "degree": raw["deg"], "eclipse": eclipse,
            "label": label, **provenance(chart_id, sources, bones), "aliases": aliases,
            "first_term": term_membership(facts["utc"]),
            "first_term_context": START <= facts["local"][:10] < EVIDENCE_START,
            "governing_ingress_id": strict_governor(float(raw["jd"]), ingress_by_id),
            "greer_quiet": bones.get(chart_id, {}).get("greer_quiet"),
            **facts,
        }
        if chart_id in bones and row["root_members"] != bones[chart_id].get("root") and row["root_members"] != bones[chart_id].get("root_members"):
            raise ValueError(f"Root drift for governed chart {chart_id}")
        charts.append(row)

    charts.sort(key=lambda row: (row["utc"], 0 if row["chart_type"] == "ingress" else 1))
    ingress_rows = [row for row in charts if row["chart_type"] == "ingress"]
    lunation_rows = [row for row in charts if row["chart_type"] == "lunation"]
    eclipse_rows = [row for row in lunation_rows if row["eclipse"]]
    first_term_rows = [row for row in charts if row["first_term"]]
    first_term_context = [row for row in charts if row["first_term_context"]]
    return {
        "schema": SCHEMA, "status": "active_factual_catalog",
        "coverage": {"start": START, "evidence_start": EVIDENCE_START, "end": END,
                     "governing_parent": "2016 Libra ingress · fixed rising",
                     "nested_context": "2016 Capricorn ingress",
                     "lunar_context": "2016-12-29 New Moon and 2017-01-12 Full Moon",
                     "chart_count": len(charts), "ingress_count": len(ingress_rows),
                     "lunation_count": len(lunation_rows), "eclipse_count": len(eclipse_rows),
                     "governing_ingress_count": len([row for row in ingress_rows if row["standing"] == "governing"]),
                     "first_term_chart_count": len(first_term_rows),
                     "first_term_with_context_count": len(first_term_rows) + len(first_term_context)},
        "location": {"label": DC_LABEL, "latitude": DC_LAT, "longitude": DC_LON,
                     "timezone": "America/New_York"},
        "calculation_receipt": {
            "config": hashlib.sha256(
                f"{SCHEMA}|{START}|{EVIDENCE_START}|{END}|{DC_LAT}|{DC_LON}|{FIRST_TERM_START_UTC.isoformat()}|{FIRST_TERM_END_UTC.isoformat()}".encode()
            ).hexdigest(),
            "america_ephemeris": sha256(HERE / "america_ephemeris.json"),
            "reading_registry": sha256(REGISTRY),
            "bones_index": sha256(BONES_INDEX),
        },
        "method": {
            "chart_clock": "Exact geocentric Sun-Moon conjunction/opposition; greatest eclipse is separate metadata.",
            "houses": "Whole Sign interpretive frame; Placidus cusps retained for comparison display.",
            "governing_ingress": "Strict chained Greer validity: start at Aries; fixed holds the year, cardinal advances two cardinal ingresses, mutable advances one, and the receiving ingress is judged again.",
            "period_clock": "Trump first-term membership uses exact 2017-01-20T17:00:00Z to 2021-01-20T17:00:00Z instants; the end is exclusive.",
            "america": america_message,
            "standing": "Factual chart corpus only; no storyline assignment, score, event claim, or independent confirmation.",
            "eclipse_metadata_scope": "v1 stores global type and greatest-eclipse clock; visibility path, duration, Saros, and Moon-family joins remain explicit future enrichment.",
        },
        "charts": charts,
    }


def validate(payload: dict[str, Any]) -> None:
    charts = payload["charts"]
    ids = [row["id"] for row in charts]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate mundane-history chart IDs")
    if payload["coverage"]["ingress_count"] != 50:
        raise ValueError("Expected 48 in-window ingresses plus the governing Libra and nested Capricorn 2016 parents")
    if payload["coverage"]["lunation_count"] != 300 or payload["coverage"]["eclipse_count"] != 55:
        raise ValueError("Unexpected 2017-January 2029 New/Full Moon or eclipse census")
    if payload["coverage"]["chart_count"] != 350 or payload["coverage"]["governing_ingress_count"] != 25:
        raise ValueError("Mundane-history corpus or strict-Greer governing census drifted")
    first_term = [row for row in charts if row["first_term"]]
    if len([row for row in first_term if row["chart_type"] == "lunation"]) != 99:
        raise ValueError("Trump first-term lunation census drifted")
    if len([row for row in first_term if row.get("eclipse")]) != 20:
        raise ValueError("Trump first-term eclipse census drifted")
    if payload["coverage"]["first_term_with_context_count"] != 119:
        raise ValueError("Trump first-term hierarchy plus carry-in context drifted")
    by_id = {row["id"]: row for row in charts}
    for row in charts:
        if row["chart_type"] == "lunation" and row["governing_ingress_id"] not in by_id:
            raise ValueError(f"Missing displayed governor for {row['id']}")
        if not any(point["name"] == "America" for point in row["points"]):
            raise ValueError(f"916 America missing from {row['id']}")
    sample = next(row for row in charts if row["id"] == "lun-2020-12-14-ne-solar")
    if sample["governing_ingress_id"] != "ingress-2020-aries":
        raise ValueError("Fixed-rising 2020 Aries did not govern the full year")
    for row in charts:
        if row["chart_type"] != "ingress":
            continue
        sun = next(point for point in row["points"] if point["name"] == "Sun")
        expected = ME.SIGNS.index(row["sign"]) * 30.0
        if sun["sign"] != row["sign"] or abs(sun["lon"] - expected) > 1e-9:
            raise ValueError(f"Ingress Sun boundary drift for {row['id']}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != rendered:
            raise SystemExit(f"STALE: {OUT}")
        print(f"Mundane history check OK · {payload['coverage']['chart_count']} charts · {OUT.name}")
        return
    OUT.write_text(rendered, encoding="utf-8")
    c = payload["coverage"]
    print(f"✓ Mundane history: {c['chart_count']} charts · {c['ingress_count']} ingresses · "
          f"{c['lunation_count']} New/Full Moons · {c['eclipse_count']} eclipses → {OUT.name}")


if __name__ == "__main__":
    main()
