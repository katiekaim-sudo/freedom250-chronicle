#!/usr/bin/env python3
"""Shared chart-casting owner for Timeline Machine seed -> astro stages."""
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import minor_points as mp
import swisseph as swe
import wheel_lib as wl
from atomic_io import atomic_write_text
from chart_conventions import DC, DC_TZ

SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio",
         "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
UTC = ZoneInfo("UTC")


def sgn(longitude):
    return SIGNS[int(longitude // 30) % 12]


def dms(longitude):
    degree = int(longitude % 30)
    minute = int(round((longitude % 30 - degree) * 60))
    if minute == 60:
        degree += 1
        minute = 0
    return f"{degree}°{minute:02d}'"


def status_key(status):
    for prefix, key in (("Occurred", "occurred"), ("Public", "position"),
                        ("Proposed", "proposed"), ("Research", "research"),
                        ("Scheduled", "scheduled")):
        if status.startswith(prefix):
            return key
    return "occurred"


def jd_for(date_iso, midnight, swe_module=swe, timezone=DC_TZ):
    parts = [int(part) for part in date_iso.split("-")]
    if len(parts) < 3:
        return None
    year, month, day = parts
    local = datetime(year, month, day, 0 if midnight else 12, 0, tzinfo=timezone)
    utc = local.astimezone(UTC)
    return swe_module.julday(utc.year, utc.month, utc.day, utc.hour + utc.minute / 60.0)


def cast(jd, key, america_pre_grid=None, swe_module=swe, wheel_module=wl,
         minor_points_module=mp, dc=DC):
    planets = (("Sun", swe_module.SUN), ("Moon", swe_module.MOON),
               ("Mercury", swe_module.MERCURY), ("Venus", swe_module.VENUS),
               ("Mars", swe_module.MARS), ("Jupiter", swe_module.JUPITER),
               ("Saturn", swe_module.SATURN), ("Uranus", swe_module.URANUS),
               ("Neptune", swe_module.NEPTUNE), ("Pluto", swe_module.PLUTO))
    flags = swe_module.FLG_MOSEPH | swe_module.FLG_SPEED
    longitudes, positions = {}, []
    for name, code in planets:
        result = swe_module.calc_ut(jd, code, flags)[0]
        longitude = result[0] % 360
        longitudes[name] = longitude
        positions.append([name, sgn(longitude), dms(longitude),
                          1 if result[3] < 0 else 0, round(longitude, 2)])

    node = swe_module.calc_ut(jd, swe_module.TRUE_NODE, flags)[0][0] % 360
    positions.append(["Node", sgn(node), dms(node), 0, round(node, 2)])
    south_node = (node + 180) % 360
    positions.append(["SNode", sgn(south_node), dms(south_node), 0, round(south_node, 2)])
    chiron = swe_module.calc_ut(jd, swe_module.CHIRON)[0][0] % 360
    positions.append(["Chiron", sgn(chiron), dms(chiron), 0, round(chiron, 2)])

    america_pre_grid = america_pre_grid or {}
    america = None
    if key in america_pre_grid:
        america = america_pre_grid[key] % 360
    else:
        try:
            america = minor_points_module.america_lon(jd) % 360
        except ValueError:
            pass
    if america is not None:
        positions.append(["America", sgn(america), dms(america), 0, round(america, 2)])

    ascendant = swe_module.houses(jd, *dc, b"W")[1][0] % 360
    aspects = wheel_module.aspects_between(longitudes)
    aspects += wheel_module.point_aspects({"Node": node}, longitudes)
    aspects += wheel_module.point_aspects({"Chiron": chiron}, longitudes)
    if america is not None:
        aspects += wheel_module.point_aspects({"America": america}, longitudes)
    aspects.sort(key=lambda aspect: aspect["o"])
    return positions, round(ascendant, 2), aspects, america


def build_payload(items, comment, generated, america_pre_grid=None, swe_module=swe,
                  wheel_module=wl, minor_points_module=mp, dc=DC, timezone=DC_TZ):
    charts, without_america = {}, 0
    for item in items:
        midnight = status_key(item["status"]) == "scheduled"
        key = item["date"] + "|" + item["title"]
        jd = jd_for(item["date"], midnight, swe_module, timezone)
        if jd is None:
            continue
        positions, ascendant, aspects, america = cast(
            jd, key, america_pre_grid, swe_module, wheel_module, minor_points_module, dc)
        if america is None:
            without_america += 1
        charts[key] = {
            "pos": positions,
            "asc": ascendant,
            "asp": aspects,
            "convention": "midnight D.C. (day of)" if midnight else "noon D.C.",
            "moonSign": next(position[1] for position in positions if position[0] == "Moon"),
        }
    return {"_comment": comment, "generated": generated, "charts": charts}, without_america


def build_file(seed_path, output_path, comment, generated, america_pre_grid=None):
    with Path(seed_path).open(encoding="utf-8") as handle:
        items = json.load(handle)["items"]
    payload, without_america = build_payload(items, comment, generated, america_pre_grid)
    atomic_write_text(
        Path(output_path), json.dumps(payload, ensure_ascii=False, indent=None)
    )
    return len(payload["charts"]), without_america
