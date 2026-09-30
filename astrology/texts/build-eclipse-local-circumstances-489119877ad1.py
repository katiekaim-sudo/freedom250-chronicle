#!/usr/bin/env python3
"""Build Washington-local circumstances for the 2024-2026 eclipse sequence.

The global eclipse type, the Washington chart, and what an observer in
Washington could physically witness are different facts.  This producer keeps
those lanes separate and emits the local horizon circumstances needed by the
mundane reading method.

Swiss Ephemeris conventions used here:

* longitude is east-positive, so Washington is negative;
* solar ``when_loc`` returns an observable maximum at sunrise or sunset when
  the geometric local maximum is below the horizon;
* lunar global phase contacts are intersected with local moonrise/moonset to
  show how much of each phase was actually above the Washington horizon.
"""

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import swisseph as swe

from chart_conventions import DC_LAT, DC_LON, DC_TZ_NAME


HERE = Path(__file__).resolve().parent
OUT = HERE / "eclipse_local_circumstances.json"
GEOPOS = (DC_LON, DC_LAT, 7.0)
UTC = timezone.utc

EVENTS = (
    ("2024-10-02", "solar"),
    ("2025-03-14", "lunar"),
    ("2025-03-29", "solar"),
    ("2025-09-07", "lunar"),
    ("2025-09-21", "solar"),
    ("2026-02-17", "solar"),
    ("2026-03-03", "lunar"),
    ("2026-08-12", "solar"),
    ("2026-08-28", "lunar"),
)


def event_type(flags: int) -> str:
    if flags & swe.ECL_ANNULAR_TOTAL:
        return "hybrid"
    if flags & swe.ECL_TOTAL:
        return "total"
    if flags & swe.ECL_ANNULAR:
        return "annular"
    if flags & swe.ECL_PARTIAL:
        return "partial"
    if flags & swe.ECL_PENUMBRAL:
        return "penumbral"
    return "none"


def jd_from_date(date_iso: str, offset_days: int = 0) -> float:
    date = datetime.fromisoformat(date_iso).replace(tzinfo=UTC) + timedelta(days=offset_days)
    return swe.julday(date.year, date.month, date.day, 0.0)


def jd_datetime(jd: float) -> datetime:
    year, month, day, decimal_hour = swe.revjul(jd, swe.GREG_CAL)
    return datetime(year, month, day, tzinfo=UTC) + timedelta(hours=decimal_hour)


def instant(jd: float) -> dict | None:
    if not jd:
        return None
    moment = jd_datetime(jd)
    return {
        "jd_ut": round(jd, 9),
        "utc": moment.isoformat(timespec="seconds").replace("+00:00", "Z"),
        "washington": moment.astimezone(ZoneInfo(DC_TZ_NAME)).isoformat(timespec="seconds"),
    }


def minutes(begin_jd: float, end_jd: float) -> float | None:
    if not begin_jd or not end_jd or end_jd < begin_jd:
        return None
    return round((end_jd - begin_jd) * 1440.0, 3)


def signed_minutes(begin_jd: float, end_jd: float) -> float:
    return round((end_jd - begin_jd) * 1440.0, 3)


def phase_visibility(begin_jd: float, end_jd: float, rise_jd: float, set_jd: float) -> dict | None:
    if not begin_jd or not end_jd:
        return None
    visible_begin = max(begin_jd, rise_jd) if rise_jd and begin_jd <= rise_jd <= end_jd else begin_jd
    visible_end = min(end_jd, set_jd) if set_jd and begin_jd <= set_jd <= end_jd else end_jd
    if visible_end <= visible_begin:
        return {"visible": False, "minutes_above_horizon": 0.0}
    return {
        "visible": True,
        "visible_begin": instant(visible_begin),
        "visible_end": instant(visible_end),
        "minutes_above_horizon": minutes(visible_begin, visible_end),
        "full_phase_minutes": minutes(begin_jd, end_jd),
    }


def rounded(value: float, places: int = 6) -> float:
    return round(float(value), places)


def phase_error(jd: float, target: float) -> float:
    sun = swe.calc_ut(jd, swe.SUN, swe.FLG_SWIEPH)[0][0]
    moon = swe.calc_ut(jd, swe.MOON, swe.FLG_SWIEPH)[0][0]
    return (moon - sun - target + 180.0) % 360.0 - 180.0


def syzygy_near(global_max: float, target: float) -> float:
    points = [global_max - 0.5 + i / 100.0 for i in range(101)]
    brackets = []
    previous_jd = points[0]
    previous_value = phase_error(previous_jd, target)
    for jd in points[1:]:
        value = phase_error(jd, target)
        if previous_value == 0 or value == 0 or previous_value * value < 0:
            brackets.append((previous_jd, jd))
        previous_jd, previous_value = jd, value
    if not brackets:
        raise RuntimeError(f"No syzygy bracket near JD {global_max}")
    lower, upper = min(brackets, key=lambda pair: abs(sum(pair) / 2.0 - global_max))
    lower_value = phase_error(lower, target)
    for _ in range(60):
        middle = (lower + upper) / 2.0
        middle_value = phase_error(middle, target)
        if lower_value * middle_value <= 0:
            upper = middle
        else:
            lower, lower_value = middle, middle_value
    return (lower + upper) / 2.0


def solar_record(date_iso: str) -> dict:
    start = jd_from_date(date_iso, -2)
    global_flags, global_times = swe.sol_eclipse_when_glob(start)
    global_max = global_times[0]
    syzygy = syzygy_near(global_max, 0.0)
    where_flags, maximum_geopos, global_attr = swe.sol_eclipse_where(global_max)
    local_flags, local_times, local_attr = swe.sol_eclipse_when_loc(start, GEOPOS)
    visible = abs(local_times[0] - global_max) < 1.0 and bool(local_flags & swe.ECL_VISIBLE)
    how_flags, how_attr = swe.sol_eclipse_how(global_max, GEOPOS)
    syzygy_flags, syzygy_attr = swe.sol_eclipse_how(syzygy, GEOPOS)

    record = {
        "date": date_iso,
        "kind": "solar",
        "global": {
            "type": event_type(global_flags),
            "maximum": instant(global_max),
            "syzygy": instant(syzygy),
            "syzygy_minus_maximum_minutes": signed_minutes(global_max, syzygy),
            "partial_phase_begin": instant(global_times[2]),
            "partial_phase_end": instant(global_times[3]),
            "total_or_annular_begin": instant(global_times[4]),
            "total_or_annular_end": instant(global_times[5]),
            "maximum_location": {
                "longitude_east_positive": rounded(maximum_geopos[0]),
                "latitude": rounded(maximum_geopos[1]),
            },
            "magnitude": rounded(global_attr[8]),
            "saros": int(global_attr[9]),
            "saros_member_engine_value": int(global_attr[10]),
        },
        "washington": {
            "visible": visible,
            "sun_true_altitude_at_global_max_deg": rounded(how_attr[5]),
            "sun_apparent_altitude_at_global_max_deg": rounded(how_attr[6]),
            "local_eclipse_state_at_global_max": event_type(how_flags),
            "sun_true_altitude_at_syzygy_deg": rounded(syzygy_attr[5]),
            "sun_apparent_altitude_at_syzygy_deg": rounded(syzygy_attr[6]),
            "local_eclipse_state_at_syzygy": event_type(syzygy_flags),
        },
    }

    if visible:
        sunrise = local_times[5]
        sunset = local_times[6]
        observable_begin = sunrise or local_times[1]
        observable_end = sunset or local_times[4]
        status = "visible"
        if sunrise:
            status = "visible_at_sunrise"
        elif sunset:
            status = "visible_at_sunset"
        record["washington"].update(
            {
                "status": status,
                "local_type": event_type(local_flags),
                "observable_maximum": instant(local_times[0]),
                "first_contact": instant(local_times[1]),
                "fourth_contact": instant(local_times[4]),
                "sunrise_during_eclipse": instant(sunrise),
                "sunset_during_eclipse": instant(sunset),
                "observable_begin": instant(observable_begin),
                "observable_end": instant(observable_end),
                "observable_minutes": minutes(observable_begin, observable_end),
                "magnitude_at_observable_maximum": rounded(local_attr[0]),
                "obscuration_at_observable_maximum": rounded(local_attr[2]),
                "sun_true_altitude_at_observable_maximum_deg": rounded(local_attr[5]),
                "sun_apparent_altitude_at_observable_maximum_deg": rounded(local_attr[6]),
                "azimuth_at_observable_maximum_deg": rounded(local_attr[4]),
            }
        )
    else:
        record["washington"].update({"status": "not_visible", "local_type": "none"})
    return record


def lunar_record(date_iso: str) -> dict:
    start = jd_from_date(date_iso, -2)
    global_flags, global_times = swe.lun_eclipse_when(start)
    global_max = global_times[0]
    syzygy = syzygy_near(global_max, 180.0)
    how_flags, how_attr = swe.lun_eclipse_how(global_max, GEOPOS)
    syzygy_flags, syzygy_attr = swe.lun_eclipse_how(syzygy, GEOPOS)
    local_flags, local_times, local_attr = swe.lun_eclipse_when_loc(start, GEOPOS)
    visible = abs(local_times[0] - global_max) < 1.0

    record = {
        "date": date_iso,
        "kind": "lunar",
        "global": {
            "type": event_type(global_flags),
            "maximum": instant(global_max),
            "syzygy": instant(syzygy),
            "syzygy_minus_maximum_minutes": signed_minutes(global_max, syzygy),
            "penumbral_begin": instant(global_times[6]),
            "penumbral_end": instant(global_times[7]),
            "partial_begin": instant(global_times[2]),
            "partial_end": instant(global_times[3]),
            "totality_begin": instant(global_times[4]),
            "totality_end": instant(global_times[5]),
            "umbral_magnitude": rounded(how_attr[0]),
            "penumbral_magnitude": rounded(how_attr[1]),
            "saros": int(how_attr[9]),
            "saros_member_engine_value": int(how_attr[10]),
        },
        "washington": {
            "visible": visible,
            "moon_true_altitude_at_global_max_deg": rounded(how_attr[5]),
            "moon_apparent_altitude_at_global_max_deg": rounded(how_attr[6]),
            "moon_true_altitude_at_syzygy_deg": rounded(syzygy_attr[5]),
            "moon_apparent_altitude_at_syzygy_deg": rounded(syzygy_attr[6]),
            "local_eclipse_state_at_syzygy": event_type(syzygy_flags),
        },
    }

    if visible:
        moonrise = local_times[8]
        moonset = local_times[9]
        status = "visible"
        if moonrise:
            status = "rises_during_eclipse"
        if moonset:
            status = "sets_during_eclipse" if status == "visible" else "rises_and_sets_during_eclipse"
        record["washington"].update(
            {
                "status": status,
                "local_type": event_type(local_flags),
                "maximum": instant(local_times[0]),
                "moonrise_during_eclipse": instant(moonrise),
                "moonset_during_eclipse": instant(moonset),
                "penumbral_phase": phase_visibility(global_times[6], global_times[7], moonrise, moonset),
                "partial_phase": phase_visibility(global_times[2], global_times[3], moonrise, moonset),
                "total_phase": phase_visibility(global_times[4], global_times[5], moonrise, moonset),
                "umbral_magnitude": rounded(local_attr[0]),
                "penumbral_magnitude": rounded(local_attr[1]),
                "azimuth_at_maximum_deg": rounded(local_attr[4]),
            }
        )
    else:
        record["washington"].update({"status": "not_visible", "local_type": "none"})
    return record


def main() -> None:
    swe.set_ephe_path(str(HERE / "ephe"))
    records = [solar_record(date) if kind == "solar" else lunar_record(date) for date, kind in EVENTS]
    payload = {
        "schema_version": 1,
        "title": "Washington-local eclipse circumstances, 2024-2026",
        "authority": "computed_astronomical_context_zero_astrological_evidence_credit",
        "location": {
            "label": "Washington, D.C.",
            "latitude": DC_LAT,
            "longitude_east_positive": DC_LON,
            "altitude_m": GEOPOS[2],
            "timezone": DC_TZ_NAME,
        },
        "engine": {"name": "Swiss Ephemeris", "version": swe.version, "ephemeris_path": "99 - Templates/ephe"},
        "method_notes": [
            "Global eclipse type and Washington-local visibility are separate facts.",
            "Solar observable maximum may be horizon-clipped by sunrise or sunset under Swiss Ephemeris conventions.",
            "Lunar phase visibility is the global phase interval intersected with Washington moonrise or moonset.",
            "True and apparent altitude are preserved separately; apparent altitude includes atmospheric refraction.",
            "Magnitude is a diameter ratio; solar obscuration is the covered fraction of the solar disc area.",
            "The exact Sun-Moon syzygy and greatest eclipse are separate instants and are both preserved.",
            "Saros member is labeled as an engine value because external catalogs can use a different member count.",
        ],
        "source_urls": [
            "https://www.astro.com/swisseph/swephprg.htm",
            "https://eclipse.gsfc.nasa.gov/solar.html",
            "https://eclipse.gsfc.nasa.gov/lunar.html",
            "https://eclipse.gsfc.nasa.gov/SEcirc/SEcircNA/WashingtonDC1+21.html",
        ],
        "events": records,
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {OUT}")
    for record in records:
        washington = record["washington"]
        print(record["date"], record["kind"], record["global"]["type"], washington["status"])


if __name__ == "__main__":
    main()
