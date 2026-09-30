#!/usr/bin/env python3
"""Build the selectable Chart Comparison workbench.

The generated view exposes the continuous 2016-January 2029 D.C. mundane-history shelf,
the current quarter-phase shelf, and the full Main Characters natal catalog
through four selectable rings.  The original
Cancer-ingress/August-eclipse/Trump/progression comparison remains the default
preset.  Exactly one eligible chart owns the shared houses; every other chart is
an overlay whose angles remain markers.

The view is deliberately calculation-first: Swiss Ephemeris produces every
longitude and cusp, Python precomputes the cross-chart contact inventory, and
the browser only filters and draws that trusted bundle.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import html
import json
import math
from pathlib import Path
import re
from zoneinfo import ZoneInfo

import swisseph as swe

from chart_conventions import DC_LABEL, DC_LAT, DC_LON, DC_TZ, clock_label
from minor_points import all_points, america_natal
from wheel_lib import WHEEL_JS, placidus_cusps


HERE = Path(__file__).resolve().parent
VAULT = HERE.parent
OUT = VAULT / "04 - Synthesis" / "Cross-cuts" / "Chart Comparison.html"
CHARACTERS = HERE / "characters_data.json"
BONES = HERE / "chart_reading_bones"
BONES_INDEX = BONES / "index.json"
READING_REGISTRY = VAULT / "03 - Astrology" / "chart_reading_registry.json"
LUNAR_WEATHER = VAULT / "04 - Synthesis" / "Cross-cuts" / "Lunar Weather.html"
MUNDANE_HISTORY = HERE / "mundane_history.json"
EPHE = HERE / "ephe"

SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
BODY_IDS = [
    ("Sun", swe.SUN), ("Moon", swe.MOON), ("Mercury", swe.MERCURY),
    ("Venus", swe.VENUS), ("Mars", swe.MARS), ("Jupiter", swe.JUPITER),
    ("Saturn", swe.SATURN), ("Uranus", swe.URANUS),
    ("Neptune", swe.NEPTUNE), ("Pluto", swe.PLUTO),
]
ASPECTS = [(0, "conjunct"), (60, "sextile"), (90, "square"), (120, "trine"), (150, "quincunx"), (180, "opposite")]
HARD = {"conjunct", "square", "opposite"}
DEFAULT_ORDER = [
    "lun-2026-08-12-ne-solar",
    "ingress-2026-cancer",
    "character-trump",
    "special-trump-progressed-2026-08-12",
]
LAYER_COLORS = ["#b07d2b", "#9b6a3f", "#3a6ea5", "#6e3d5e"]


def jd_from_datetime(moment: datetime) -> float:
    utc = moment.astimezone(timezone.utc)
    hour = utc.hour + utc.minute / 60 + (utc.second + utc.microsecond / 1_000_000) / 3600
    return swe.julday(utc.year, utc.month, utc.day, hour, swe.GREG_CAL)


def datetime_from_jd(jd: float) -> datetime:
    year, month, day, hour = swe.revjul(jd, swe.GREG_CAL)
    return datetime(year, month, day, tzinfo=timezone.utc) + timedelta(hours=hour)


def refine_phase(seed_jd: float, target: float) -> float:
    flags = swe.FLG_SWIEPH | swe.FLG_SPEED
    jd = seed_jd
    for _ in range(10):
        sun = swe.calc_ut(jd, swe.SUN, flags)[0]
        moon = swe.calc_ut(jd, swe.MOON, flags)[0]
        error = ((moon[0] - sun[0] - target + 180) % 360) - 180
        jd -= error / (moon[3] - sun[3])
        if abs(error) < 1e-11:
            break
    return jd


def dms(lon: float) -> str:
    degree = lon % 30
    total_seconds = int(round(degree * 3600))
    if total_seconds >= 30 * 3600:
        total_seconds = 0
    deg, remain = divmod(total_seconds, 3600)
    minute, second = divmod(remain, 60)
    return f"{deg}°{minute:02d}′{second:02d}″"


def point(name: str, lon: float, speed: float = 0.0, group: str = "planet") -> dict:
    lon %= 360
    return {
        "name": name,
        "lon": round(lon, 8),
        "sign": SIGNS[int(lon // 30) % 12],
        "dms": dms(lon),
        "retro": speed < 0,
        "group": group,
    }


def calculated_points(
    jd: float, america_mode: str = "event", america_key: str | None = None
) -> list[dict]:
    flags = swe.FLG_SWIEPH | swe.FLG_SPEED
    out = []
    for name, body_id in BODY_IDS:
        result = swe.calc_ut(jd, body_id, flags)[0]
        out.append(point(name, result[0], result[3]))
    extras = all_points(jd, with_america=(america_mode == "event"))
    for name in ("Chiron", "Node"):
        lon, speed = extras[name]
        group = "chiron" if name == "Chiron" else "node"
        out.append(point(name, lon, speed, group))
        if name == "Node":
            out.append(point("SNode", lon + 180, speed, "node"))
    if america_mode == "event":
        lon, speed = extras["America"]
        out.append(point("America", lon, speed, "america"))
    elif america_mode == "natal":
        if not america_key:
            raise ValueError("Natal 916 America requires a governed chart key")
        out.append(point("America", america_natal(america_key), 0.0, "america"))
    return out


def angles_and_cusps(jd: float, lat: float, lon: float) -> tuple[float, float, list[float]]:
    _cusps, ascmc = swe.houses(jd, lat, lon, b"P")
    cusps, mc = placidus_cusps(jd, lat, lon)
    return ascmc[0] % 360, mc, cusps


def asc_from_mc(mc_lon: float, lat: float) -> float:
    eps = math.radians(23.4368)
    mcr = math.radians(mc_lon)
    ramc = math.atan2(math.sin(mcr) * math.cos(eps), math.cos(mcr))
    phi = math.radians(lat)
    asc = math.atan2(
        math.cos(ramc),
        -(math.sin(ramc) * math.cos(eps) + math.tan(phi) * math.sin(eps)),
    )
    return math.degrees(asc) % 360


def character_rows() -> list[dict]:
    data = json.loads(CHARACTERS.read_text(encoding="utf-8"))
    return data["cast"] if isinstance(data, dict) else data


def frame_layer(
    layer_id: str, label: str, short: str, kind: str, color: str,
    jd: float, moment: datetime, place: str, lat: float, lon: float,
    points: list[dict], source: str, frame_eligible: bool = True,
) -> dict:
    asc, mc, cusps = angles_and_cusps(jd, lat, lon)
    return {
        "id": layer_id, "label": label, "short": short, "kind": kind,
        "color": color, "jd": round(jd, 9), "utc": moment.astimezone(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z"),
        "local": clock_label(moment.astimezone(DC_TZ), seconds=True) if place == DC_LABEL else moment.strftime("%B %-d, %Y · %-I:%M:%S %p %Z"),
        "place": place, "lat": lat, "lon": lon, "points": points,
        "asc": round(asc, 8), "mc": round(mc, 8), "cusps": cusps,
        "frameEligible": frame_eligible, "source": source,
    }


def label_from_source(source: str) -> str:
    name = Path(source).name
    for suffix in (" — A Reading.md", " — A reading.md", ".md"):
        if name.endswith(suffix):
            name = name[: -len(suffix)]
            break
    return name


def governed_chart_sources() -> tuple[dict, dict, dict]:
    index = json.loads(BONES_INDEX.read_text(encoding="utf-8"))["charts"]
    registry = json.loads(READING_REGISTRY.read_text(encoding="utf-8"))["readings"]
    sources = {row["id"]: row["source"] for row in registry if row.get("kind") == "pass1"}
    meta_by_id = {row["id"]: row for row in index}
    bones_by_date = {}
    for row in index:
        if row["type"] == "lunation":
            bones_by_date[row["date"]] = row["id"]
    return sources, meta_by_id, bones_by_date


def lunation_records() -> dict:
    text = LUNAR_WEATHER.read_text(encoding="utf-8")
    head = (r'\{"type":"(New Moon|First Quarter|Full Moon|Last Quarter)",'
            r'"date":"(\d{4}-\d{2}-\d{2})","time_utc":"(\d{2}):(\d{2})"')
    records = {}
    for match in re.finditer(head, text):
        phase, date, hour, minute = match.groups()
        tail = text[match.end():match.end() + 360]
        sign = re.search(r'"(?:moon_)?sign":"(\w+)"', tail)
        degree = re.search(r'"degree":([\d.]+)', tail)
        eclipse = re.search(r'"eclipse":(true|false)', tail)
        if not (sign and degree and eclipse):
            raise ValueError(f"Lunar Weather chart record changed at {date}")
        records[date] = {
            "phase": phase, "hour": int(hour), "minute": int(minute),
            "sign": sign.group(1), "degree": float(degree.group(1)),
            "eclipse": eclipse.group(1) == "true",
        }
    return records


def lunation_layers() -> list[dict]:
    sources, meta_by_id, bones_by_date = governed_chart_sources()
    targets = {"New Moon": 0.0, "First Quarter": 90.0, "Full Moon": 180.0, "Last Quarter": 270.0}
    layers = []
    for number, (date, rec) in enumerate(sorted(lunation_records().items())):
        year, month, day = map(int, date.split("-"))
        seed_jd = swe.julday(year, month, day, rec["hour"] + rec["minute"] / 60.0)
        jd = refine_phase(seed_jd, targets[rec["phase"]])
        moment = datetime_from_jd(jd)
        chart_id = bones_by_date.get(date, f"lunation-{date}")
        source = sources.get(chart_id, "04 - Synthesis/Cross-cuts/Lunar Weather.html · exact phase catalog")
        if chart_id in sources:
            label = label_from_source(source)
        elif rec["eclipse"]:
            label = f"{date} {rec['sign']} {'Solar' if rec['phase'] == 'New Moon' else 'Lunar'} Eclipse"
        else:
            label = f"{date} {rec['sign']} {rec['phase']}"
        category = "Eclipses" if rec["eclipse"] else "Lunations"
        short = "E" if rec["eclipse"] else {"New Moon": "N", "Full Moon": "F", "First Quarter": "Q", "Last Quarter": "Q"}[rec["phase"]]
        layer = frame_layer(
            chart_id, label, short, "mundane eclipse" if rec["eclipse"] else rec["phase"].lower(),
            LAYER_COLORS[number % len(LAYER_COLORS)], jd, moment,
            DC_LABEL, DC_LAT, DC_LON, calculated_points(jd), source,
        )
        bone = None
        if chart_id in meta_by_id:
            bone = json.loads((BONES / f"{chart_id}.json").read_text(encoding="utf-8"))
        layer.update({
            "category": category, "date": date, "phase": rec["phase"],
            "moonSign": rec["sign"], "degree": rec["degree"],
            "root": bone.get("root_members", []) if bone else [],
            "governing": meta_by_id.get(chart_id, {}).get("governing"),
            "greerQuiet": meta_by_id.get(chart_id, {}).get("greer_quiet"),
            "placidusEligible": True, "timeKnown": True,
        })
        layers.append(layer)
    if len(layers) != 198:
        raise ValueError(f"Expected 198 saved lunation charts, found {len(layers)}")
    return layers


def history_layers() -> list[dict]:
    """Project the calculate-once mundane-history corpus into comparison layers."""
    payload = json.loads(MUNDANE_HISTORY.read_text(encoding="utf-8"))
    if payload.get("schema") != "freedom250.mundane-history/v1":
        raise ValueError("Unsupported mundane-history catalog schema")
    history = payload["charts"]
    ingress_labels = {row["id"]: row["label"] for row in history if row["chart_type"] == "ingress"}
    layers = []
    for number, row in enumerate(history):
        eclipse = row.get("eclipse")
        category = "Ingresses" if row["chart_type"] == "ingress" else "Eclipses" if eclipse else "Lunations"
        kind = "mundane ingress" if category == "Ingresses" else "mundane eclipse" if eclipse else row["phase"].lower()
        short = "I" if category == "Ingresses" else "E" if eclipse else "N" if row["kind"] == "new" else "F"
        moment = datetime.fromisoformat(row["utc"])
        layer = {
            "id": row["id"], "label": row["label"], "short": short, "kind": kind,
            "color": LAYER_COLORS[number % len(LAYER_COLORS)], "jd": row["jd_ut"],
            "utc": moment.astimezone(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z"),
            "local": clock_label(moment.astimezone(DC_TZ), seconds=True),
            "place": DC_LABEL, "lat": DC_LAT, "lon": DC_LON, "points": row["points"],
            "asc": row["asc"], "mc": row["mc"], "cusps": row["placidus_cusps"],
            "frameEligible": True,
            "source": row.get("reading_source") or row["calculation_authority"],
            "category": category, "date": row["date"], "utcDate": row["utc"][:10],
            "year": int(row["date"][:4]), "aliases": row.get("aliases", []),
            "root": row.get("root_members", []), "placidusEligible": True, "timeKnown": True,
            "firstTerm": row.get("first_term", False),
            "verification": row.get("verification", {}),
        }
        if row["chart_type"] == "ingress":
            layer.update({"standing": row["standing"], "ascModality": row["asc_modality"]})
        else:
            layer.update({
                "phase": row["phase"], "moonSign": row["sign"], "degree": row["degree"],
                "governing": ingress_labels.get(row["governing_ingress_id"], row["governing_ingress_id"]),
                "governingId": row["governing_ingress_id"], "greerQuiet": row.get("greer_quiet"),
                "eclipseMeta": eclipse,
            })
        layers.append(layer)
    return layers


def retained_quarter_layers() -> list[dict]:
    """Preserve the current 2024-2027 quarter shelf during authority migration."""
    rows = [row for row in lunation_layers() if row.get("phase") in {"First Quarter", "Last Quarter"}]
    if len(rows) != 99:
        raise ValueError(f"Expected 99 retained quarter charts, found {len(rows)}")
    for row in rows:
        row["legacyQuarter"] = True
        row["year"] = int(row["date"][:4])
        row["aliases"] = []
    return rows


def character_jd(row: dict) -> tuple[float, datetime, bool]:
    tz = ZoneInfo(row["tz"])
    date_part = datetime.fromisoformat(row["date"])
    if row.get("time_known"):
        hour, minute = map(int, row["time"].split(":"))
        local = datetime(date_part.year, date_part.month, date_part.day, hour, minute, tzinfo=tz)
        return jd_from_datetime(local), local, True
    local_midnight = datetime(date_part.year, date_part.month, date_part.day, 0, 0, tzinfo=tz)
    seed_jd = jd_from_datetime(local_midnight)
    result, times = swe.rise_trans(
        seed_jd, swe.SUN, swe.CALC_RISE, (row["lon"], row["lat"], 0.0)
    )
    if result != 0:
        raise RuntimeError(f"No sunrise frame for {row['name']}")
    jd = times[0]
    return jd, datetime_from_jd(jd).astimezone(tz), False


def character_layers() -> list[dict]:
    layers = []
    for number, row in enumerate(character_rows()):
        jd, local, time_known = character_jd(row)
        layer = frame_layer(
            f"character-{row['slug']}", row["name"], "N", "natal chart",
            LAYER_COLORS[number % len(LAYER_COLORS)], jd, local,
            row["place"], row["lat"], row["lon"],
            calculated_points(jd, "natal", row["slug"]),
            "99 - Templates/characters_data.json",
            frame_eligible=time_known,
        )
        if row.get("asc_override") is not None:
            layer["asc"] = float(row["asc_override"])
            layer["placidusEligible"] = False
        else:
            layer["placidusEligible"] = time_known
        layer.update({
            "category": "Main Characters",
            "date": row["date"],
            "role": row.get("role", ""),
            "rodden": row.get("rodden"),
            "timeKnown": time_known,
            "frameEligible": time_known,
        })
        if not time_known:
            layer["frameCaution"] = "No recorded birth time: sunrise display only; angles and houses cannot own the comparison frame."
            layer["kind"] = "natal planets · sunrise display"
            layer["local"] = f"{local.strftime('%B %-d, %Y')} · sunrise display · {local.tzname()}"
        elif row.get("asc_override") is not None:
            layer["frameCaution"] = "Katie's rectified Ascendant; Whole Sign frame only."
        layers.append(layer)
    return layers


def progressed_trump_layer(catalog: list[dict]) -> dict:
    eclipse = next(row for row in catalog if row["id"] == "lun-2026-08-12-ne-solar")
    natal = next(row for row in catalog if row["id"] == "character-trump")
    trump = next(row for row in character_rows() if row["slug"] == "trump")
    birth_jd = natal["jd"]
    eclipse_jd = eclipse["jd"]
    eclipse_moment = datetime.fromisoformat(eclipse["utc"].replace("Z", "+00:00"))
    birth_local = datetime.fromisoformat(f"{trump['date']}T{trump['time']}").replace(tzinfo=ZoneInfo(trump["tz"]))
    progressed_jd = birth_jd + (eclipse_jd - birth_jd) / 365.25
    progressed_moment = datetime_from_jd(progressed_jd)
    progressed_points = calculated_points(progressed_jd, "progressed")
    natal_sun = next(p["lon"] for p in natal["points"] if p["name"] == "Sun")
    progressed_sun = next(p["lon"] for p in progressed_points if p["name"] == "Sun")
    solar_arc = (progressed_sun - natal_sun) % 360
    progressed_mc = (natal["mc"] + solar_arc) % 360
    progressed_asc = asc_from_mc(progressed_mc, trump["lat"])
    progressed = {
        "id": "special-trump-progressed-2026-08-12", "label": "Trump Secondary Progressed · Aug 12", "short": "P",
        "kind": "secondary-progressed planets · Solar-Arc ASC/MC", "color": "#6e3d5e",
        "jd": round(progressed_jd, 9), "utc": eclipse["utc"], "local": eclipse["local"],
        "symbolicEpochUtc": progressed_moment.isoformat(timespec="milliseconds").replace("+00:00", "Z"),
        "place": trump["place"], "lat": trump["lat"], "lon": trump["lon"],
        "points": progressed_points, "asc": round(progressed_asc, 8), "mc": round(progressed_mc, 8),
        "cusps": [], "frameEligible": False, "placidusEligible": False,
        "category": "Progressions", "date": "2026-08-12", "timeKnown": True,
        "source": "Project personal-chart method in 99 - Templates/build_katie.py",
        "method": {"rate": "1 ephemeris day = 1 tropical year", "yearDenominatorDays": 365.25,
                   "solarArc": round(solar_arc, 8), "angleMethod": "Solar-Arc MC by longitude; Ascendant reconstructed at natal latitude"},
        "unavailable": ["916 America: no approved exact JPL Horizons value at the 1946 symbolic epoch"],
    }

    return progressed


def build_catalog() -> tuple[list[dict], dict]:
    catalog = history_layers()
    catalog.extend(retained_quarter_layers())
    catalog.extend(character_layers())
    catalog.append(progressed_trump_layer(catalog))
    ids = [row["id"] for row in catalog]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate chart IDs in comparison catalog")
    missing = [chart_id for chart_id in DEFAULT_ORDER if chart_id not in ids]
    if missing:
        raise ValueError("Missing default comparison charts: " + ", ".join(missing))
    counts = {}
    for row in catalog:
        counts[row["category"]] = counts.get(row["category"], 0) + 1
    eclipse = next(row for row in catalog if row["id"] == "lun-2026-08-12-ne-solar")
    aliases = {}
    for row in catalog:
        for alias in row.get("aliases", []):
            if alias in aliases and aliases[alias] != row["id"]:
                raise ValueError(f"Ambiguous legacy chart alias: {alias}")
            aliases[alias] = row["id"]
    meta = {
        "title": "Saved Chart Comparison",
        "targetUtc": eclipse["utc"], "targetLocal": eclipse["local"],
        "defaultFrame": "lun-2026-08-12-ne-solar", "defaultHouseSystem": "W",
        "defaultSelection": DEFAULT_ORDER,
        "aliases": aliases,
        "catalogCounts": counts,
        "progressionClock": "Targeted to the exact eclipse instant, not the app-open date",
        "chartClock": "Exact Sun–Moon ecliptic-longitude conjunction; greatest eclipse is a separate astronomical clock",
        "locationRule": "Mundane charts are cast for Washington, D.C.",
    }
    return catalog, meta


def angular_distance(a: float, b: float) -> float:
    return abs((a - b + 180) % 360 - 180)


def contact_points(layer: dict) -> list[dict]:
    untimed_natal = layer.get("category") == "Main Characters" and not layer.get("timeKnown")
    out = [p for p in layer["points"] if not (untimed_natal and p["name"] == "Moon")]
    if layer.get("frameEligible"):
        out.append(point("ASC", layer["asc"], group="angle"))
        out.append(point("MC", layer["mc"], group="angle"))
    return out


def build_contacts(layers: list[dict]) -> list[dict]:
    contacts = []
    for ai, a in enumerate(layers):
        for b in layers[ai + 1:]:
            aid, bid = a["id"], b["id"]
            for p in contact_points(a):
                for q in contact_points(b):
                    # South Node duplicates the North Node axis in cross-chart work.
                    if p["name"] == "SNode" or q["name"] == "SNode":
                        continue
                    separation = angular_distance(p["lon"], q["lon"])
                    for angle, aspect in ASPECTS:
                        orb = abs(separation - angle)
                        if orb > 3.000001:
                            continue
                        minor = p["group"] in {"node", "chiron", "america"} or q["group"] in {"node", "chiron", "america"}
                        contacts.append({
                            "id": f"{aid}-{p['name']}-{bid}-{q['name']}-{aspect}".lower().replace(" ", "-"),
                            "a": aid, "b": bid, "p1": p["name"], "p2": q["name"],
                            "lon1": p["lon"], "lon2": q["lon"], "pos1": f"{p['dms']} {p['sign']}", "pos2": f"{q['dms']} {q['sign']}",
                            "aspect": aspect, "angle": angle, "orb": round(orb, 8),
                            "minor": minor, "anglePoint": p["group"] == "angle" or q["group"] == "angle",
                            "hard": aspect in HARD,
                        })
    contacts.sort(key=lambda c: (c["orb"], c["a"], c["b"], c["p1"], c["p2"]))
    return contacts


def glyph_source() -> str:
    match = re.search(r"  const GLY=(\{.*?\n  \});", WHEEL_JS, flags=re.S)
    if not match:
        raise RuntimeError("Could not derive the governed hand-drawn glyph paths from wheel_lib.py")
    return "const F250_GLY=" + match.group(1) + ";"


HTML_TEMPLATE = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Chart Comparison — Freedom 250 Observatory</title>
<style>
:root{--paper:#faf8f3;--card:#fffdf7;--ink:#29251f;--muted:#7c7468;--hair:#d9cfb8;--soft:#eee6d5;--burg:#7a2e1d;--gold:#b07d2b;--blue:#3a6ea5;--plum:#6e3d5e;--russet:#9b6a3f}
*{box-sizing:border-box}html,body{margin:0;min-height:100%;background:var(--paper);color:var(--ink);font-family:"Iowan Old Style",Palatino,Georgia,serif}button,select,input{font:inherit}
body{padding:16px}.wrap{max-width:1180px;margin:0 auto}.eyebrow{font:700 10px/1.2 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;letter-spacing:.16em;text-transform:uppercase;color:var(--burg)}
h1{font-size:clamp(21px,2.7vw,31px);line-height:1.06;font-weight:500;margin:5px 0 6px}.dek{max-width:80ch;color:var(--muted);font-size:13px;line-height:1.45;margin:0 0 10px}.clockbar{display:flex;flex-wrap:wrap;gap:5px 16px;padding:7px 11px;border:1px solid var(--hair);background:rgba(255,253,247,.72);font-size:11.5px;color:var(--muted)}.clockbar b{color:var(--ink)}
.controls{margin-top:10px;border:1px solid var(--hair);background:var(--card);padding:9px 11px;display:grid;gap:7px}.control-row{display:flex;align-items:center;gap:7px;flex-wrap:wrap}.control-row label{font:700 10px/1.2 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
select,.plain-btn{border:1px solid #cbbd9d;border-radius:16px;background:#f7f1e5;color:var(--ink);padding:4px 10px;cursor:pointer}.plain-btn:hover,.plain-btn:focus-visible,select:focus-visible{outline:2px solid rgba(122,46,29,.25);outline-offset:1px}.segment{display:inline-flex;border:1px solid #cbbd9d;border-radius:16px;overflow:hidden}.segment button{border:0;border-right:1px solid #cbbd9d;background:#f7f1e5;padding:4px 9px;color:var(--burg);cursor:pointer}.segment button:last-child{border-right:0}.segment button.on{background:var(--burg);color:#fff}
.picker-row{align-items:flex-end;padding-bottom:7px;border-bottom:1px solid var(--soft)}.picker-slot{display:grid;gap:3px;min-width:180px;flex:1 1 210px}.picker-slot span{font:700 9px/1.2 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}.picker-slot select{width:100%;border-radius:4px;background:#fffdf7}.catalog-note{font-size:11px;color:var(--muted)}
.stack-end{font:700 9px/1 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);opacity:.8}.layer-row{gap:6px}.layers{display:flex;gap:6px;flex-wrap:wrap;align-items:center}.layer-chip{display:inline-flex;align-items:center;gap:6px;border:1px solid var(--layer);border-radius:18px;background:transparent;color:var(--layer);padding:4px 9px;cursor:pointer;font-size:13px}.layer-chip .badge{display:grid;place-items:center;width:17px;height:17px;border-radius:50%;background:var(--layer);color:#fff;font:700 10px/1 sans-serif}.layer-chip.off{opacity:.35;text-decoration:line-through}.layer-chip.frame{box-shadow:inset 0 0 0 1px var(--layer);background:color-mix(in srgb,var(--layer) 9%,transparent)}
.aspect-chip{border:1px solid #cbbd9d;border-radius:14px;background:transparent;padding:3px 8px;color:var(--muted);cursor:pointer;font-size:12px}.aspect-chip.on{background:#5b554a;color:#fff;border-color:#5b554a}.points label{font-size:12px;text-transform:none;letter-spacing:0;font-weight:400;color:var(--ink);display:inline-flex;align-items:center;gap:4px}.points input{accent-color:var(--burg)}
details.connections{border-top:1px solid var(--soft);padding-top:7px}details.connections>summary{cursor:pointer;list-style:none;display:inline-flex;align-items:center;gap:6px;font:700 10px/1.2 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--burg);border:1px solid #cbbd9d;border-radius:14px;padding:4px 10px;background:#f7f1e5}details.connections>summary::-webkit-details-marker{display:none}details.connections>summary::after{content:"▸";font-size:11px}details.connections[open]>summary::after{content:"▾"}details.connections>summary:focus-visible{outline:2px solid rgba(122,46,29,.3)}details.connections .control-row{margin-top:7px}
.frame-note{font-size:12px;color:var(--muted);padding-top:6px;border-top:1px solid var(--soft)}.frame-note strong{color:var(--burg)}
.workspace{display:block;margin-top:12px}.wheel-card,.ledger-card,.method-card{border:1px solid var(--hair);background:var(--card)}.wheel-card{margin:0 auto;padding:0;position:relative}
.zoombar{display:flex;align-items:center;gap:7px;padding:6px 9px;border-bottom:1px solid var(--soft);flex-wrap:wrap}.zoombar .zlabel{font:700 10px/1.2 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin-right:1px}
.zbtn{border:1px solid #cbbd9d;border-radius:14px;background:#f7f1e5;color:var(--ink);padding:3px 10px;cursor:pointer;font-size:12px;line-height:1.35}.zbtn:hover,.zbtn:focus-visible{outline:2px solid rgba(122,46,29,.25);outline-offset:1px}.zbtn.zstep{width:28px;padding:3px 0;text-align:center;font-weight:700}.zbtn.on{background:var(--burg);color:#fff;border-color:var(--burg)}
#zRange{width:150px;accent-color:var(--burg);cursor:pointer}.zpct{font:600 12px/1 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:var(--burg);min-width:42px;text-align:right;font-variant-numeric:tabular-nums}
.wheel-viewport{height:clamp(500px,82vh,940px);overflow:auto;display:flex;background:#fdfbf5;position:relative}.wheel-viewport.pannable{cursor:grab}.wheel-viewport.panning{cursor:grabbing}.wheel-stage{margin:auto;flex:none;line-height:0}.wheel-stage svg{display:block;width:100%;height:100%}
.wheel-card [data-body]{cursor:pointer}.wheel-card [data-body]:focus{outline:none}.wheel-card [data-body]:focus-visible .placement-glyph{filter:drop-shadow(0 0 3px rgba(122,46,29,.75))}.wheel-card .dim{opacity:.16}
.ledger-card{max-height:520px;margin-top:14px;display:flex;flex-direction:column}.ledger-head{padding:12px 14px;border-bottom:1px solid var(--hair)}.ledger-head h2{font-size:17px;font-weight:500;margin:0 0 3px}.ledger-head p{font-size:12px;color:var(--muted);margin:0}.ledger{overflow:auto;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));align-items:start}.pair-head{grid-column:1/-1;position:sticky;top:0;background:#f5efe2;padding:6px 12px;border-bottom:1px solid var(--hair);font:700 10px/1.2 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);z-index:1}.contact{width:100%;border:0;border-bottom:1px solid var(--soft);background:transparent;text-align:left;padding:8px 12px;cursor:pointer;color:var(--ink)}.contact:hover,.contact:focus-visible,.contact.active{background:#f8f1e5;outline:none}.contact-main{display:flex;gap:6px;align-items:baseline;font-size:12px;line-height:1.35}.contact-main .sym{font-weight:700;color:var(--burg);min-width:15px;text-align:center}.contact-sub{font:10px/1.35 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:var(--muted);padding-top:3px}.contact .orb{margin-left:auto;color:var(--burg);font-weight:700;white-space:nowrap}.empty{grid-column:1/-1;padding:30px 18px;text-align:center;color:var(--muted);font-style:italic}.line-toggle{font-size:12px!important;text-transform:none!important;letter-spacing:0!important;font-weight:400!important;color:var(--ink)!important;display:inline-flex;align-items:center;gap:5px}.line-toggle input{accent-color:var(--burg)}
.overlap-card{margin-top:14px;border:1px solid var(--hair);background:var(--card)}.overlap-head{padding:12px 14px;border-bottom:1px solid var(--hair);display:flex;gap:8px 24px;align-items:baseline;justify-content:space-between;flex-wrap:wrap;cursor:pointer;list-style:none}.overlap-head::-webkit-details-marker{display:none}.overlap-head h2{font-size:17px;font-weight:500;margin:0}.overlap-head h2::after{content:" ▸";font-size:12px;color:var(--burg)}.overlap-card[open] .overlap-head h2::after{content:" ▾"}.overlap-head p{font-size:11.5px;color:var(--muted);margin:0;max-width:76ch}.overlap-grid{display:grid;grid-template-columns:minmax(260px,.85fr) minmax(380px,1.4fr)}.overlap-pane{padding:12px 14px}.overlap-pane+ .overlap-pane{border-left:1px solid var(--hair)}.overlap-pane h3{font-size:13px;margin:0 0 3px;color:var(--burg)}.overlap-pane>.pane-note{font-size:10.5px;color:var(--muted);margin:0 0 9px}.pattern-list,.umbrella-list{display:grid;gap:7px}.pattern{border-top:1px solid var(--soft);padding-top:7px}.pattern:first-child{border-top:0;padding-top:0}.pattern b{display:block;font-size:11px;color:var(--ink);margin-bottom:2px}.pattern span{display:block;font-size:10.5px;line-height:1.4;color:var(--muted)}.umbrella{display:grid;grid-template-columns:minmax(145px,.42fr) minmax(0,1fr);gap:8px;border-top:1px solid var(--soft);padding-top:7px}.umbrella:first-child{border-top:0;padding-top:0}.umbrella-name{font-size:11px;line-height:1.3;color:var(--burg);font-weight:700}.umbrella-contacts{display:flex;gap:5px;flex-wrap:wrap}.overlap-contact{border:0;border-bottom:1px dotted #b9aa8b;background:transparent;color:var(--ink);padding:0 0 1px;text-align:left;cursor:pointer;font-size:10.5px;line-height:1.35}.overlap-contact:hover,.overlap-contact:focus-visible{color:var(--burg);outline:none;border-bottom-style:solid}.overlap-empty{font-size:11px;line-height:1.45;color:var(--muted);font-style:italic}.hypothesis-lane{grid-column:1/-1;border-top:1px solid var(--hair);padding:9px 14px;display:flex;align-items:center;gap:8px 16px;flex-wrap:wrap;font-size:10.5px;color:var(--muted)}.hypothesis-lane b{color:var(--burg)}.hypothesis-lane .plain-btn{font-size:10.5px;padding:3px 9px}
.method-card{margin-top:14px;padding:12px 14px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.method-card h3{font-size:13px;margin:0 0 5px;font-weight:600;color:var(--burg)}.method-card p{font-size:11px;line-height:1.45;color:var(--muted);margin:0}.status{position:absolute;left:12px;bottom:12px;max-width:320px;border:1px solid var(--hair);background:rgba(255,253,247,.94);padding:8px 10px;font-size:11px;color:var(--muted);display:none;pointer-events:none}.status.show{display:block}
@media(max-width:1040px){.ledger-card{max-height:460px}.method-card{grid-template-columns:1fr 1fr}.overlap-grid{grid-template-columns:1fr}.overlap-pane+ .overlap-pane{border-left:0;border-top:1px solid var(--hair)}}
@media(max-width:760px){body{padding:11px}.wheel-viewport{height:clamp(440px,74vh,800px)}}
@media(max-width:620px){body{padding:9px}.controls{padding:9px}.ledger{grid-template-columns:1fr}.method-card{grid-template-columns:1fr}.layer-chip{padding:4px 7px}#zRange{width:104px}}
@media(prefers-reduced-motion:reduce){*{scroll-behavior:auto!important}}
</style></head><body>
<main class="wrap">
  <div class="eyebrow">Sky &amp; Charts · Workbench</div>
  <h1>Pick the charts. Keep one house frame.</h1>
  <p class="dek">Build a one- to four-ring comparison from every cardinal ingress, exact New/Full Moon, eclipse, retained quarter phase, and Main Character chart on the saved shelf. Governing and nested ingress standing remain visibly distinct.</p>
  <div class="clockbar"><span><b>Catalog:</b> __CATALOG_SUMMARY__</span><span><b>Mundane clock:</b> exact D.C. chart moments</span><span><b>Natal caution:</b> untimed sunrise displays cannot own houses</span></div>
  <section class="controls" aria-label="Chart comparison controls">
    <div class="control-row picker-row" id="chartPickers"></div>
    <div class="control-row"><label for="frameSelect">House frame</label><select id="frameSelect"></select><div class="segment" aria-label="House system"><button type="button" data-house="W" class="on">Whole Sign</button><button type="button" data-house="P">Placidus</button></div><button class="plain-btn" id="resetBtn" type="button">Reset</button><button class="plain-btn" id="fullBtn" type="button">Full screen</button><button class="plain-btn" id="exportBtn" type="button">Export SVG</button></div>
    <div class="control-row layer-row"><label>Rings</label><span class="stack-end">inner</span><div class="layers" id="layerChips"></div><span class="stack-end">outer</span></div>
    <details class="connections" id="connectionsPanel">
      <summary>Connections &amp; points</summary>
      <div class="control-row"><label for="relationSelect">Relations</label><select id="relationSelect"><option value="primary">Primary connections</option><option value="frame">Current frame contacts</option><option value="all">All cross-chart pairs</option></select><label for="orbSelect">Orb</label><select id="orbSelect"><option value="project">Project policy</option><option value="1">1° tight</option><option value="2">2° standard</option><option value="3">3° explore</option></select><label>Aspects</label><div id="aspectChips"></div><label class="line-toggle"><input type="checkbox" id="aspectLines"> draw lines</label></div>
      <div class="control-row points"><label>Points</label><label><input type="checkbox" data-point-group="planet" checked disabled> planets</label><label><input type="checkbox" data-point-group="angle" checked> angles</label><label><input type="checkbox" data-point-group="node" checked> nodes</label><label><input type="checkbox" data-point-group="chiron" checked> Chiron</label><label><input type="checkbox" data-point-group="america" checked> 916 America</label></div>
    </details>
    <div class="frame-note" id="frameNote"></div>
  </section>
  <section class="workspace">
    <div class="wheel-card">
      <div class="zoombar" role="group" aria-label="Wheel zoom">
        <span class="zlabel">Zoom</span>
        <button class="zbtn" id="zFit" type="button" title="Fit the whole wheel in the panel">Fit</button>
        <button class="zbtn zstep" id="zOut" type="button" aria-label="Zoom out">−</button>
        <input type="range" id="zRange" min="55" max="150" step="1" value="100" aria-label="Zoom level">
        <button class="zbtn zstep" id="zIn" type="button" aria-label="Zoom in">+</button>
        <span class="zpct" id="zPct">100%</span>
        <button class="zbtn" id="zReset" type="button" title="Return the wheel to Fit">Reset view</button>
      </div>
      <div class="wheel-viewport" id="wheelViewport"><div class="wheel-stage" id="wheelStage"></div></div>
      <div id="status" class="status"></div>
    </div>
    <aside class="ledger-card"><div class="ledger-head"><h2>Connection ledger</h2><p id="ledgerCount">Exact cross-chart contacts under the selected policy.</p></div><div class="ledger" id="ledger"></div></aside>
  </section>
  <details class="overlap-card" open aria-labelledby="overlapTitle">
    <summary class="overlap-head"><h2 id="overlapTitle">Natural overlaps</h2><p>Geometry first: recurring structures and shared archetypal rooms among the selected charts. One contact may belong to several umbrellas; none is assigned to a Chronicle storyline automatically.</p></summary>
    <div class="overlap-grid">
      <div class="overlap-pane"><h3>Recurrence hearing</h3><p class="pane-note">Hard contacts ≤1°; sextiles and trines ≤0.5° support but never establish recurrence. Eclipse lights are one configuration.</p><div class="pattern-list" id="recurrenceList"></div></div>
      <div class="overlap-pane"><h3>Archetypal umbrellas</h3><p class="pane-note">Shared symbolic rooms, not scores or event predictions. Select a contact to isolate its exact geometry on the wheel.</p><div class="umbrella-list" id="umbrellaList"></div></div>
      <div class="hypothesis-lane"><b>Chronicle hypothesis</b><span>No storyline is attached automatically. Authored prospective watches remain separate.</span><button class="plain-btn" id="openSpine" type="button">Open Astrology Spine</button></div>
    </div>
  </details>
  <section class="method-card"><div><h3>One house owner</h3><p>Only the selected frame supplies houses, spokes, Ascendant, and MC. Every other chart remains an overlay; changing the frame recomputes each shown placement’s house.</p></div><div><h3>Historical D.C. shelf</h3><p>Exact New/Full Moons, eclipses, and every cardinal ingress run from the 2016 governing prologue through January 2029. Ingresses are visibly separated into governing and nested stages; current quarter phases remain available during their calculation-authority migration.</p></div><div><h3>Timing honesty</h3><p>Washington local dates drive display and filtering while UTC instants remain attached. Unknown-time natal charts cannot own houses; computed charts retain a visible independent-verification status.</p></div></section>
</main>
<script>__GLYPHS__
const DATA=__DATA__;
const SGN=["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"];
const SAB2={Aries:"Ar",Taurus:"Ta",Gemini:"Ge",Cancer:"Cn",Leo:"Le",Virgo:"Vi",Libra:"Li",Scorpio:"Sc",Sagittarius:"Sg",Capricorn:"Cp",Aquarius:"Aq",Pisces:"Pi"};
const SAB={Aries:"Ari",Taurus:"Tau",Gemini:"Gem",Cancer:"Can",Leo:"Leo",Virgo:"Vir",Libra:"Lib",Scorpio:"Sco",Sagittarius:"Sag",Capricorn:"Cap",Aquarius:"Aqu",Pisces:"Pis"};
const ELEM={Aries:"#b3402e",Leo:"#b3402e",Sagittarius:"#b3402e",Taurus:"#4a7d5f",Virgo:"#4a7d5f",Capricorn:"#4a7d5f",Gemini:"#a8821f",Libra:"#a8821f",Aquarius:"#a8821f",Cancer:"#3a6ea5",Scorpio:"#3a6ea5",Pisces:"#3a6ea5"};
const ASPC={conjunct:"#c9a227",sextile:"#3a6ea5",square:"#b3402e",trine:"#3a6ea5",quincunx:"#5a8a4a",opposite:"#b3402e"};
const ASYM={conjunct:"☌",sextile:"⚹",square:"□",trine:"△",quincunx:"⚻",opposite:"☍"};
const BODYC={Sun:"#c56f12",Moon:"#b98918",Mercury:"#b12674",Venus:"#16806f",Mars:"#df3b30",Jupiter:"#9a7021",Saturn:"#963f32",Uranus:"#356fbd",Neptune:"#1595a8",Pluto:"#8a2638",Node:"#3e3a34",SNode:"#3e3a34",Chiron:"#2f6c57",America:"#76539a"};
const SLOT_COLORS=["#b07d2b","#9b6a3f","#3a6ea5","#6e3d5e"];
const CATALOG_BY_ID=Object.fromEntries(DATA.catalog.map(x=>[x.id,x]));
const CHART_ALIASES=DATA.meta.aliases||{};
function resolveChartId(id){return CATALOG_BY_ID[id]?id:CHART_ALIASES[id]||null}

/* ===== Radial architecture ===============================================
   One square 1000x1000 design space: small clear centre, house-number band,
   four broad chart annuli, shared outer zodiac band. The annuli are graduated
   because crowding is measured per unit of ARC, not per degree: the innermost
   ring has the least circumference and therefore needs the most radial room
   to open a third lane. House spokes run hub -> zodiac through every ring.  */
const VB=1000,CX=500,CY=500;
const HUB=38,HOUSE_OUT=66,ZOD_IN=428,ZOD_OUT=470,ANGLE_LBL=488;
const BAND_IN=66,BAND_OUT=428,RING_FILL=["#f4f9ee","#f3f1f8"];
/* Hiding a chart does not leave an empty ring behind: the visible charts
   re-divide the whole annular band, so four charts is a quadwheel, three a
   triwheel, two a biwheel and one a single wheel. Inner rings keep a slightly
   larger share because they have the least circumference to spend.         */
function ringPlan(n){
 const w=Array.from({length:Math.max(1,n)},(_,i)=>1-.02*i),sum=w.reduce((a,b)=>a+b,0),span=BAND_OUT-BAND_IN,out=[];
 let r=BAND_IN;
 w.forEach(x=>{const h=span*x/sum;out.push({inner:r,outer:r+h});r+=h});
 return out;
}
let RING_SLOTS=ringPlan(4);
function visibleOrder(){return layerOrder().filter(id=>state.visible.has(id))}
const WHEEL_WORD={1:"single wheel",2:"biwheel",3:"triwheel",4:"quadwheel"};
const RING_EDGE=3;
const BLOCK={normal:{gs:1.12,gh:22.4,fs:12.5,fs2:10.8,gapE:2},mid:{gs:1.0,gh:20,fs:11,fs2:9.6,gapE:1.8},compact:{gs:.92,gh:18.4,fs:10,fs2:8.7,gapE:1.3},tight:{gs:.82,gh:16.4,fs:9.2,fs2:8.1,gapE:1.4}};
const PAIR_EPS=.35,SHIFT_OK=4.2,TANG_PAD=3.8,RAD_PAD=1.2,LANE_SWITCH=1.2,LEADER_MIN=.8;
/* Displacement is clamped by ARC LENGTH, not degrees, so an inner ring may
   swing a label further in degrees than an outer ring for the same ink.    */
function shiftCap(ring){const rm=(ring.inner+ring.outer)/2;return Math.min(12,Math.max(3.6,44/rm*180/Math.PI))}
const MEASURED=new Map();

const state={selected:DATA.meta.defaultSelection.slice(),frame:DATA.meta.defaultFrame,house:"W",visible:new Set(DATA.meta.defaultSelection),relation:"primary",orb:"project",aspects:new Set(["conjunct","sextile","square","trine","quincunx","opposite"]),groups:new Set(["planet","angle","node","chiron","america"]),showLines:false,isolate:null,point:null,houseFilter:null};
let layers=[],byId={},activeContacts=DATA.contacts.slice();
function esc(s){return String(s).replace(/[&<>\"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));}
function f2(x){return Math.round(x*100)/100} function norm(x){return ((x%360)+360)%360}
function angDist(a,b){return Math.abs(norm(a-b+180)-180)}
function pairKey(a,b){return [a,b].sort((x,y)=>state.selected.indexOf(x)-state.selected.indexOf(y)).join("|")}
function naturalPair(a,b){const A=byId[a],B=byId[b],cats=new Set([A.category,B.category]);if(cats.has("Progressions"))return cats.has("Main Characters")||cats.has("Eclipses");if(cats.has("Ingresses"))return cats.has("Lunations")||cats.has("Eclipses")||cats.has("Main Characters");if(cats.has("Main Characters"))return cats.has("Lunations")||cats.has("Eclipses");return false}
function projectCap(c){if(c.minor)return c.hard?2:-1;const A=byId[c.a],B=byId[c.b];if(A.category==="Progressions"||B.category==="Progressions")return 1;if((A.category==="Ingresses"&&["Lunations","Eclipses"].includes(B.category))||(B.category==="Ingresses"&&["Lunations","Eclipses"].includes(A.category)))return c.hard?3:-1;return 2}
function pointGroup(layer,name){if(name==="ASC"||name==="MC")return "angle";const p=byId[layer].points.find(x=>x.name===name);return p?p.group:"planet"}
function passesBase(c){if(!state.visible.has(c.a)||!state.visible.has(c.b))return false;if(!state.aspects.has(c.aspect))return false;if(!state.groups.has(pointGroup(c.a,c.p1))||!state.groups.has(pointGroup(c.b,c.p2)))return false;if(state.relation==="primary"&&!naturalPair(c.a,c.b))return false;if(state.relation==="frame"&&c.a!==state.frame&&c.b!==state.frame)return false;const cap=state.orb==="project"?projectCap(c):Number(state.orb);if(cap<0||c.orb>cap+1e-8)return false;if(state.point&&state.point!==c.a+":"+c.p1&&state.point!==c.b+":"+c.p2)return false;if(state.houseFilter){const f=byId[state.frame];if(houseOf(c.lon1,f)!==state.houseFilter&&houseOf(c.lon2,f)!==state.houseFilter)return false}return true}
function houseOf(lon,frame){if(state.house==="W")return ((Math.floor(norm(lon)/30)-Math.floor(norm(frame.asc)/30)+12)%12)+1;const c=frame.cusps;for(let i=0;i<12;i++){const start=c[i],end=c[(i+1)%12],span=norm(end-start),rel=norm(lon-start);if(rel<span||Math.abs(rel-span)<1e-7)return i+1}return null}
function orbText(o){let sec=Math.round(o*3600),d=Math.floor(sec/3600);sec-=d*3600;let m=Math.floor(sec/60);sec-=m*60;return (d?d+"°":"")+String(m).padStart(2,"0")+"′"+String(sec).padStart(2,"0")+"″"}
function pt(cx,cy,r,L,cusp){const a=(180+(L-cusp))*Math.PI/180;return [cx+r*Math.cos(a),cy-r*Math.sin(a)]}
function arcPath(cx,cy,r1,r2,a1,a2,cusp){const p1=pt(cx,cy,r2,a1,cusp),p2=pt(cx,cy,r2,a2,cusp),p3=pt(cx,cy,r1,a2,cusp),p4=pt(cx,cy,r1,a1,cusp);return `M${f2(p1[0])} ${f2(p1[1])} A${r2} ${r2} 0 0 0 ${f2(p2[0])} ${f2(p2[1])} L${f2(p3[0])} ${f2(p3[1])} A${r1} ${r1} 0 0 1 ${f2(p4[0])} ${f2(p4[1])} Z`}
function annulusPath(cx,cy,inner,outer){return `M${cx+outer} ${cy}A${outer} ${outer} 0 1 0 ${cx-outer} ${cy}A${outer} ${outer} 0 1 0 ${cx+outer} ${cy}M${cx+inner} ${cy}A${inner} ${inner} 0 1 1 ${cx-inner} ${cy}A${inner} ${inner} 0 1 1 ${cx+inner} ${cy}`}
function layerOrder(){return [state.frame].concat(state.selected.filter(id=>id!==state.frame))}
function glyph(name,x,y,scale,color){if(!F250_GLY[name])return `<text x="${f2(x)}" y="${f2(y)}" text-anchor="middle" dominant-baseline="central" font-size="${f2(9*scale)}" font-weight="700" fill="${color}">${esc(name)}</text>`;return `<g transform="translate(${f2(x-10*scale)} ${f2(y-10*scale)}) scale(${f2(scale)})" color="${color}" stroke="currentColor" stroke-width="2.05" stroke-linecap="round" fill="none">${F250_GLY[name]}</g>`}
function anglePoint(layer,name){return {name,lon:layer[name.toLowerCase()],dms:"",sign:SGN[Math.floor(layer[name.toLowerCase()]/30)],group:"angle"}}
function dmsLon(lon){let sec=Math.round(norm(lon)*3600)%1296000,d=Math.floor(sec/3600),m=Math.floor((sec-d*3600)/60);return `${String(d%30).padStart(2,'0')}°${String(m).padStart(2,'0')}′`}
function selectedLayers(){return state.selected.map((id,i)=>({...CATALOG_BY_ID[id],color:SLOT_COLORS[i]}))}
function contactPointsJS(layer){const untimedNatal=layer.category==="Main Characters"&&!layer.timeKnown,pts=layer.points.filter(p=>!(untimedNatal&&p.name==="Moon"));return layer.frameEligible?pts.concat([anglePoint(layer,"ASC"),anglePoint(layer,"MC")]):pts}
function computeContactsJS(){const out=[],defs=[[0,"conjunct"],[60,"sextile"],[90,"square"],[120,"trine"],[150,"quincunx"],[180,"opposite"]];for(let i=0;i<layers.length;i++)for(let j=i+1;j<layers.length;j++){const A=layers[i],B=layers[j];for(const p of contactPointsJS(A))for(const q of contactPointsJS(B)){if(p.name==="SNode"||q.name==="SNode")continue;const separation=angDist(p.lon,q.lon);for(const [angle,aspect] of defs){const orb=Math.abs(separation-angle);if(orb>3.000001)continue;const minor=["node","chiron","america"].includes(p.group)||["node","chiron","america"].includes(q.group);out.push({id:`${A.id}-${p.name}-${B.id}-${q.name}-${aspect}`.toLowerCase().replace(/[^a-z0-9-]+/g,"-"),a:A.id,b:B.id,p1:p.name,p2:q.name,lon1:p.lon,lon2:q.lon,pos1:`${p.dms||dmsLon(p.lon)} ${p.sign}`,pos2:`${q.dms||dmsLon(q.lon)} ${q.sign}`,aspect,angle,orb,minor,anglePoint:p.group==="angle"||q.group==="angle",hard:["conjunct","square","opposite"].includes(aspect)})}}}return out.sort((a,b)=>a.orb-b.orb||a.a.localeCompare(b.a)||a.p1.localeCompare(b.p1))}
function refreshSelection(useDefaultContacts=false){layers=selectedLayers();byId=Object.fromEntries(layers.map(x=>[x.id,x]));const eligible=layers.filter(x=>x.frameEligible);if(!eligible.length)throw new Error("Comparison requires at least one chart with a trustworthy house frame");if(!byId[state.frame]||!byId[state.frame].frameEligible)state.frame=eligible[0].id;if(state.house==="P"&&!byId[state.frame].placidusEligible)state.house="W";state.visible=new Set(state.selected);activeContacts=useDefaultContacts?DATA.contacts.slice():computeContactsJS();RING_SLOTS=ringPlan(state.selected.length)}

/* ===== Placement chains ==================================================
   Astro Gold's composure comes from RADIAL placement chains: a placement is
   a thin column of upright elements - glyph row, degree, house number,
   minutes - running along the radius at its angle. A chain spends its ink on
   radius, which every ring has, and almost none on arc, which is the scarce
   resource. There are no lanes and no stacks: one chain per placement,
   fanned tangentially, with a leader back to its exact-longitude tick when
   it has had to move. All spacing runs on MEASURED element bounds.        */
function posParts(p){const m=p.dms.match(/^(\d+)°(\d+)/)||[];return {deg:`${m[1]||"0"}°`,min:`${m[2]||"00"}′${p.retro?"℞":""}`}}
function posText(p){const q=posParts(p);return q.deg+" "+q.min}
const EL_EST={g:(b,m)=>({w:b.members.length*m.gh*.95,h:m.gh}),d:(b,m)=>({w:b.parts.deg.length*m.fs*.58,h:m.fs}),h:(b,m)=>({w:String(b.house??"").length*m.fs2*.55,h:m.fs2*.9}),m2:(b,m)=>({w:b.parts.min.length*m.fs2*.56,h:m.fs2})};
function elKey(b,kind){return b.metric.fs+"|"+kind+"|"+(kind==="g"?b.members.map(p=>p.name).join("+"):kind==="d"?b.parts.deg:kind==="h"?String(b.house):b.parts.min)}
function elBounds(b,kind){return MEASURED.get(elKey(b,kind))||EL_EST[kind](b,b.metric)}
function chainElems(b){const ks=b.house!=null?["g","d","h","m2"]:["g","d","m2"];return ks.map(k=>({kind:k,...elBounds(b,k)}))}
/* Radial and tangential footprints of an upright box sitting on a ray.     */
function supports(w,h,a){const A=(180+a)*Math.PI/180,ca=Math.abs(Math.cos(A)),sa=Math.abs(Math.sin(A));return {rad:w*ca+h*sa,tan:w*sa+h*ca}}
function chainShape(b,angle){let len=0,wt=0,wtAt=0;chainElems(b).forEach((e,i)=>{const s=supports(e.w,e.h,angle);if(i)len+=b.metric.gapE;const c=len+s.rad/2;len+=s.rad;if(s.tan>wt){wt=s.tan;wtAt=c}});return {len,wt,wtAt}}
function buildBlocks(layer,metric,frame){
 const pts=layer.points.filter(p=>state.groups.has(p.group)).slice().sort((a,b)=>a.lon-b.lon),out=[];
 for(let i=0;i<pts.length;i++){
  const members=[pts[i]];
  while(i+1<pts.length&&members.length<3&&angDist(pts[i+1].lon,members[0].lon)<=PAIR_EPS&&posText(pts[i+1])===posText(members[0]))members.push(pts[++i]);
  const lon=members[0].lon+members.reduce((s,p)=>s+(norm(p.lon-members[0].lon+180)-180),0)/members.length;
  const hs=frame?houseOf(members[0].lon,frame):null;
  out.push({members,lon:norm(lon),text:posText(members[0]),parts:posParts(members[0]),house:hs,metric,paired:members.length>1});
 }
 return out;
}
/* Required tangential gap between two chains, priced at the radius where
   the pair's widest element actually sits - honest in narrow rings (chains
   reach deep) and in wide ones (chains hug the outer edge).                */
function needGap(A,B){return ((A.wt+B.wt)/2+TANG_PAD)/Math.min(A.rm,B.rm)*180/Math.PI}
/* Bounded relaxation: push tangentially, keep zodiacal order, clamp every
   displacement by arc length. Wrap-aware - the ring is a circle, so the
   last and first chains are neighbours too. Fixed ASC/MC labels take part
   but never move.                                                          */
function sweep(items,maxShift){
 items.sort((a,b)=>a.target-b.target);
 for(let pass=0;pass<9;pass++){
  let moved=false;
  for(let k=1;k<=2;k++)for(let i=0;i+k<items.length;i++){
   const A=items[i],B=items[i+k];if(A.fixed&&B.fixed)continue;
   const g=needGap(A,B),d=B.angle-A.angle;
   if(d<g-1e-6){const need=g-d;if(A.fixed)B.angle+=need;else if(B.fixed)A.angle-=need;else{A.angle-=need/2;B.angle+=need/2}moved=true}
  }
  const n=items.length;
  (n>=3?[[n-1,0],[n-2,0],[n-1,1]]:n===2?[[1,0]]:[]).forEach(([ia,ib])=>{
   const A=items[ia],B=items[ib];if(A.fixed&&B.fixed)return;
   const g=needGap(A,B),d=B.angle+360-A.angle;
   if(d<g-1e-6){const need=g-d;if(A.fixed)B.angle+=need;else if(B.fixed)A.angle-=need;else{A.angle-=need/2;B.angle+=need/2}moved=true}
  });
  items.forEach(it=>{if(!it.fixed)it.angle=it.target+Math.max(-maxShift,Math.min(maxShift,it.angle-it.target))});
  for(let i=1;i<items.length;i++)if(!items[i].fixed&&items[i].angle<items[i-1].angle)items[i].angle=items[i-1].angle;
  if(!moved)break;
 }
 let worst=0,clean=true;
 items.forEach(it=>{if(!it.fixed)worst=Math.max(worst,Math.abs(it.angle-it.target))});
 for(let k=1;k<=2;k++)for(let i=0;i+k<items.length;i++){const g=needGap(items[i],items[i+k]);if(items[i+k].angle-items[i].angle<g-.35)clean=false}
 const N=items.length;
 (N>=3?[[N-1,0],[N-2,0],[N-1,1]]:N===2?[[1,0]]:[]).forEach(([ia,ib])=>{
  const g=needGap(items[ia],items[ib]);
  if(items[ib].angle+360-items[ia].angle<g-.35)clean=false});
 return {worst,clean};
}
/* Packed runs get EVEN intervals: the sweep resolves collisions but leaves
   clusters at ragged spacings; Astro Gold's clusters read as even fans. Only
   applied when every resulting gap still clears its pair requirement and
   every member stays inside its displacement budget - else left alone.     */
function evenFan(items,maxShift){
 const n=items.length;if(n<3)return;
 let i=0;
 while(i<n-1){
  let j=i;
  while(j<n-1&&items[j+1].angle-items[j].angle<=needGap(items[j],items[j+1])+1.4)j++;
  if(j-i>=2){
   const span=items[j].angle-items[i].angle,prop=[];
   let ok=span>0;
   for(let k=i;k<=j;k++){const a=items[i].angle+span*(k-i)/(j-i);prop.push(a);
    if(items[k].fixed&&k!==i&&k!==j)ok=false;
    if(!items[k].fixed&&Math.abs(a-items[k].target)>maxShift)ok=false}
   if(ok)for(let k=i;k<j;k++)if(prop[k-i+1]-prop[k-i]<needGap(items[k],items[k+1])-.05)ok=false;
   if(ok)for(let k=i+1;k<j;k++)items[k].angle=prop[k-i];
  }
  i=Math.max(j,i+1);
 }
}
function layoutRing(layer,ring,cusp,only){
 const maxShift=shiftCap(ring);
 const fixed=(state.groups.has("angle")&&layer.id!==state.frame)
   ?[layer.asc,layer.mc].map(L=>({fixed:true,target:norm(L-cusp),angle:norm(L-cusp),wt:30,rm:ring.inner+16}))
   :[];
 const usable=(ring.outer-8)-(ring.inner+2);
 let best=null;
 for(const metric of (only?[only]:[BLOCK.normal,BLOCK.mid,BLOCK.compact,BLOCK.tight])){
  const blocks=buildBlocks(layer,metric,byId[state.frame]);
  let fits=true;
  blocks.forEach(b=>{b.unwrapped=norm(b.lon-cusp);const sh=chainShape(b,b.unwrapped);b.len=sh.len;b.wt=sh.wt;b.rm=Math.max(ring.inner+8,ring.outer-8-sh.wtAt);if(sh.len>usable)fits=false});
  blocks.sort((a,b)=>a.unwrapped-b.unwrapped);
  const items=blocks.map(b=>({b,target:b.unwrapped,angle:b.unwrapped,wt:b.wt,rm:b.rm})).concat(fixed);
  const res=sweep(items,maxShift);
  if(res.clean)evenFan(items,maxShift);
  let worst=0;items.forEach(it=>{if(!it.fixed)worst=Math.max(worst,Math.abs(it.angle-it.target))});
  best={items:items.filter(x=>!x.fixed),ring,worst,clean:res.clean&&fits};
  if(best.clean)break;
 }
 return best;
}
/* Chart identity has to be readable FROM THE WHEEL, not from a caption below
   it. The inscribed circle leaves the square's corners empty; the legend goes
   there, and each ring's outer rim is stroked in the same colour as its swatch. */
function ringLegend(order){
 const s=['<g class="ring-legend" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,sans-serif">'];
 s.push(`<text x="12" y="19" font-size="10" font-weight="700" letter-spacing="1.3" fill="#8a8377">INNER → OUTER</text>`);
 order.forEach((id,i)=>{
  const L=byId[id],y=39+i*25,isF=id===state.frame;
  s.push(`<circle cx="20" cy="${y}" r="8.5" fill="${L.color}"/><text x="20" y="${y}" text-anchor="middle" dominant-baseline="central" font-size="10.5" font-weight="700" fill="#fffdf7">${i+1}</text>`);
  s.push(`<text x="34" y="${y-(isF?4:0)}" dominant-baseline="central" font-size="11.5" font-weight="${isF?700:400}" fill="#3a352e">${esc(L.label)}</text>`);
  if(isF)s.push(`<text x="34" y="${y+7}" dominant-baseline="central" font-size="8.5" fill="${L.color}">houses · ${state.house==="W"?"Whole Sign":"Placidus"}</text>`);
 });
 s.push(`<text x="12" y="${39+order.length*25+4}" font-size="8.5" fill="#9a8f7c">raised number = house in this frame</text>`);
 return s.join("")+"</g>";
}
/* Type size is chosen for the WHEEL, not per ring: a chart whose rings are set
   at three different sizes reads as improvised. Take the largest size at which
   every visible ring is collision-free. Collapsing to a biwheel therefore also
   buys a bigger, more legible face across the whole chart.                    */
function layoutWheel(order,cusp){
 let last=null;
 for(const metric of [BLOCK.normal,BLOCK.mid,BLOCK.compact,BLOCK.tight]){
  const plans=order.map((id,i)=>layoutRing(byId[id],RING_SLOTS[i],cusp,metric));
  last=plans;
  /* Largest size at which every visible ring is collision-free. */
  if(plans.every(p=>p&&p.clean))return plans;
 }
 return last;
}
function wheelSVG(){
 const frame=byId[state.frame],cusp=state.house==="W"?Math.floor(frame.asc/30)*30:frame.asc,order=visibleOrder(),s=[];
 RING_SLOTS=ringPlan(order.length);
 s.push(`<svg id="comparisonSvg" viewBox="0 0 ${VB} ${VB}" width="${VB}" height="${VB}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Four broad chart rings sharing one house frame" font-family="Iowan Old Style,Palatino,Georgia,serif"><title>Chart Comparison · inner to outer: `+order.map(id=>esc(byId[id].label)).join(", ")+`</title>`);
 order.forEach((id,index)=>{const ring=RING_SLOTS[index];s.push(`<path class="chart-annulus" data-ring-layer="${id}" d="${annulusPath(CX,CY,ring.inner,ring.outer)}" fill="${RING_FILL[index%2]}" fill-rule="evenodd" stroke="none"/>`)});
 for(let i=0;i<12;i++){s.push(`<path class="zodiac-sector" d="${arcPath(CX,CY,ZOD_IN,ZOD_OUT,i*30,i*30+30,cusp)}" fill="${ELEM[SGN[i]]}" fill-opacity=".075" stroke="#b8aa77" stroke-width=".7"/>`);const q=pt(CX,CY,449,i*30+15,cusp);s.push(`<text x="${f2(q[0])}" y="${f2(q[1])}" text-anchor="middle" dominant-baseline="central" font-size="18" font-style="italic" fill="${ELEM[SGN[i]]}">${SAB[SGN[i]]}</text>`)}
 for(let L=0;L<360;L+=5){if(L%30===0)continue;const r2=L%10===0?418:422,a=pt(CX,CY,ZOD_IN,L,cusp),b=pt(CX,CY,r2,L,cusp);s.push(`<line x1="${f2(a[0])}" y1="${f2(a[1])}" x2="${f2(b[0])}" y2="${f2(b[1])}" stroke="#cbbf99" stroke-width=".65"/>`)}
 s.push(`<circle cx="${CX}" cy="${CY}" r="${ZOD_OUT}" fill="none" stroke="#aa9760" stroke-width="1.1"/><circle cx="${CX}" cy="${CY}" r="${ZOD_IN}" fill="none" stroke="#aa9760" stroke-width="1"/><circle cx="${CX}" cy="${CY}" r="${HOUSE_OUT}" fill="none" stroke="#cbbf99" stroke-width=".75"/><circle cx="${CX}" cy="${CY}" r="${HUB}" fill="#fffdf7" stroke="#b8aa77" stroke-width=".9"/>`);
 order.forEach((id,i)=>s.push(`<circle class="ring-rim" data-rim-layer="${id}" cx="${CX}" cy="${CY}" r="${f2(RING_SLOTS[i].outer)}" fill="none" stroke="${byId[id].color}" stroke-opacity=".5" stroke-width="1.2"/>`));
 s.push(`<circle cx="${CX}" cy="${CY}" r="${BAND_IN}" fill="none" stroke="${byId[order[0]].color}" stroke-opacity=".5" stroke-width="1.2"/>`);
 const cusps=state.house==="W"?Array.from({length:12},(_,i)=>(Math.floor(frame.asc/30)+i)*30):frame.cusps;
 cusps.forEach((L,i)=>{const next=cusps[(i+1)%12],mid=norm(L+norm(next-L)/2),a=pt(CX,CY,HUB,L,cusp),b=pt(CX,CY,ZOD_IN,L,cusp),q=pt(CX,CY,52,mid,cusp),angular=[0,3,6,9].includes(i);s.push(`<line class="house-spoke" x1="${f2(a[0])}" y1="${f2(a[1])}" x2="${f2(b[0])}" y2="${f2(b[1])}" stroke="${angular?"#ad914e":"#d5c9a6"}" stroke-width="${angular?1.3:.68}"/><text class="house-number" x="${f2(q[0])}" y="${f2(q[1])}" text-anchor="middle" dominant-baseline="central" font-size="11" fill="#8e7b4b">${i+1}</text>`)});
 let lineContacts=activeContacts.filter(passesBase).sort((a,b)=>a.orb-b.orb);if(state.isolate)lineContacts=lineContacts.filter(c=>c.id===state.isolate);else if(state.showLines)lineContacts=lineContacts.slice(0,12);else lineContacts=[];
 lineContacts.forEach(c=>{const a=pt(CX,CY,HUB-4,c.lon1,cusp),b=pt(CX,CY,HUB-4,c.lon2,cusp);s.push(`<line class="contact-line" data-contact="${c.id}" x1="${f2(a[0])}" y1="${f2(a[1])}" x2="${f2(b[0])}" y2="${f2(b[1])}" stroke="${ASPC[c.aspect]}" stroke-width="${c.orb<=.3?2:1}" stroke-opacity=".72"/>`)});
 const PLANS=layoutWheel(order,cusp);
 order.forEach((id,index)=>{
  const layer=byId[id],ring=RING_SLOTS[index],isFrame=id===state.frame;
  PLANS[index].items.forEach(it=>{
   const b=it.b,m=b.metric,shift=Math.abs(it.angle-it.target);
   const tickOut=pt(CX,CY,ring.outer-2.5,it.target,0),tickIn=pt(CX,CY,ring.outer-9.5,it.target,0);
   const key=id+":"+b.members[0].name,dim=state.point&&!b.members.some(p=>state.point===id+":"+p.name)?" dim":"";
   const tip=b.members.map(p=>`${esc(p.name)} ${esc(p.dms+" "+p.sign)} · house ${houseOf(p.lon,frame)}`).join(" · ");
   s.push(`<g class="placement body${dim}${b.paired?" paired":""}" tabindex="0" data-body="${key}" data-layer="${id}" data-name="${esc(b.members[0].name)}" data-block="${b.members.map(p=>esc(p.name)).join("+")}"><title>${esc(layer.label)} · ${tip}</title>`);
   s.push(`<line class="exact-tick" x1="${f2(tickIn[0])}" y1="${f2(tickIn[1])}" x2="${f2(tickOut[0])}" y2="${f2(tickOut[1])}" stroke="${layer.color}" stroke-width="1.9"/>`);
   let rPos=ring.outer-8;
   if(shift>LEADER_MIN){const top=pt(CX,CY,rPos-1,it.angle,0);s.push(`<line class="leader" x1="${f2(tickIn[0])}" y1="${f2(tickIn[1])}" x2="${f2(top[0])}" y2="${f2(top[1])}" stroke="${layer.color}" stroke-opacity=".45" stroke-width=".75" ${layer.category==="Progressions"?'stroke-dasharray="3 2"':""}/>`)}
   chainElems(b).forEach(e=>{
    const sp=supports(e.w,e.h,it.angle),rc=Math.max(ring.inner+2+sp.rad/2,rPos-sp.rad/2),P=pt(CX,CY,rc,it.angle,0);
    if(e.kind==="g"){
     const dTh=(m.gh*.95)/Math.max(rc,30)*180/Math.PI;
     s.push(`<g class="placement-glyph" data-measure="${esc(elKey(b,"g"))}">`);
     b.members.forEach((p2,k)=>{const Q=pt(CX,CY,rc,it.angle+(k-(b.members.length-1)/2)*dTh,0);s.push(glyph(p2.name,Q[0],Q[1],m.gs,BODYC[p2.name]||"#4d4942"))});
     s.push(`</g>`);
    }else if(e.kind==="d"){
     s.push(`<text class="placement-degree" data-measure="${esc(elKey(b,"d"))}" x="${f2(P[0])}" y="${f2(P[1])}" text-anchor="middle" dominant-baseline="central" font-size="${m.fs}" font-weight="600" fill="#4a453c">${esc(b.parts.deg)}</text>`);
    }else if(e.kind==="h"){
     s.push(`<text class="placement-house" data-measure="${esc(elKey(b,"h"))}" x="${f2(P[0])}" y="${f2(P[1])}" text-anchor="middle" dominant-baseline="central" font-size="${f2(m.fs2*.85)}" fill="#9a8f7c">${b.house}</text>`);
    }else{
     s.push(`<text class="placement-minute" data-measure="${esc(elKey(b,"m2"))}" x="${f2(P[0])}" y="${f2(P[1])}" text-anchor="middle" dominant-baseline="central" font-size="${m.fs2}" fill="#6d675c">${esc(b.parts.min)}</text>`);
    }
    rPos=rc-sp.rad/2-m.gapE;
   });
   s.push(`</g>`);
  });
  if(state.groups.has("angle")&&!isFrame)[["ASC",layer.asc],["MC",layer.mc]].forEach(([name,L])=>{const a=pt(CX,CY,ring.inner+3,L,cusp),b=pt(CX,CY,ring.outer-4,L,cusp),q=pt(CX,CY,ring.inner+17,L,cusp);s.push(`<g class="overlay-angle" data-body="${id}:${name}" data-layer="${id}" data-name="${name}"><title>${esc(layer.label)} · ${name} ${dmsLon(L)}</title><line x1="${f2(a[0])}" y1="${f2(a[1])}" x2="${f2(b[0])}" y2="${f2(b[1])}" stroke="${layer.color}" stroke-width="1.1" stroke-opacity=".8" ${name==="MC"?'stroke-dasharray="3 2"':""}/><g transform="translate(${f2(q[0])} ${f2(q[1])})"><text class="angle-label" x="0" y="-6" text-anchor="middle" dominant-baseline="central" font-size="12" font-weight="700" fill="${layer.color}">${name==="ASC"?"As":"Mc"}</text><text class="angle-degree" x="0" y="6.5" text-anchor="middle" dominant-baseline="central" font-size="8" fill="${layer.color}">${dmsLon(L)}</text></g></g>`)});
 });
 if(state.groups.has("angle"))[["ASC",frame.asc],["MC",frame.mc]].forEach(([name,L])=>{const a=pt(CX,CY,ZOD_IN-6,L,cusp),b=pt(CX,CY,ZOD_OUT+6,L,cusp),q=pt(CX,CY,ANGLE_LBL-6,L,cusp);s.push(`<g class="main-angle" data-body="${frame.id}:${name}" data-layer="${frame.id}" data-name="${name}"><title>${esc(frame.label)} · ${name} ${dmsLon(L)}</title><line x1="${f2(a[0])}" y1="${f2(a[1])}" x2="${f2(b[0])}" y2="${f2(b[1])}" stroke="${frame.color}" stroke-width="${name==="ASC"?2.3:1.7}" ${name==="MC"?'stroke-dasharray="3 2"':""}/><g transform="translate(${f2(q[0])} ${f2(q[1])})"><text x="0" y="-7.5" text-anchor="middle" dominant-baseline="central" font-size="14.5" font-weight="700" fill="${frame.color}">${name==="ASC"?"As":"Mc"}</text><text x="0" y="7" text-anchor="middle" dominant-baseline="central" font-size="8.5" fill="${frame.color}">${dmsLon(L)}</text></g></g>`)});
 s.push(ringLegend(order));
 s.push("</svg>");return s.join("")
}

/* ===== Zoom / fit viewport ==============================================
   Fit is computed from the wheel viewport's own content box - both axes - so
   the complete zodiac circle is inside the card at every window size. 100%
   IS Fit; the slider spans 55%-150% of it.                                  */
const ZMIN=.55,ZMAX=1.5;let fitScale=1,zoom=1;
const vpEl=()=>document.getElementById("wheelViewport"),stageEl=()=>document.getElementById("wheelStage");
function computeFit(){const el=vpEl();if(!el)return 1;const w=el.clientWidth-20,h=el.clientHeight-20;if(w<40||h<40)return 1;return Math.max(.05,Math.min(w,h)/VB)}
function applyZoom(){const st=stageEl();if(!st)return;const px=Math.max(60,Math.round(VB*fitScale*zoom));st.style.width=px+"px";st.style.height=px+"px";const svg=document.getElementById("comparisonSvg");if(svg){svg.setAttribute("width",px);svg.setAttribute("height",px)}const pct=Math.round(zoom*100),rng=document.getElementById("zRange");document.getElementById("zPct").textContent=pct+"%";if(document.activeElement!==rng)rng.value=pct;document.getElementById("zFit").classList.toggle("on",Math.abs(zoom-1)<.005);vpEl().classList.toggle("pannable",zoom>1.005)}
function setZoom(z){zoom=Math.min(ZMAX,Math.max(ZMIN,z));applyZoom()}
function zoomAround(z,clientX,clientY){const el=vpEl(),r=el.getBoundingClientRect(),old=zoom,px=clientX-r.left+el.scrollLeft,py=clientY-r.top+el.scrollTop;setZoom(z);const k=zoom/old;el.scrollLeft=px*k-(clientX-r.left);el.scrollTop=py*k-(clientY-r.top)}
function refit(){const f=computeFit();if(Math.abs(f-fitScale)>.0008){fitScale=f;applyZoom()}}
function measurePass(){let changed=false;document.querySelectorAll("#comparisonSvg [data-measure]").forEach(g=>{const k=g.getAttribute("data-measure");let b=null;try{b=g.getBBox()}catch(_){return}if(!b||!b.width||!isFinite(b.width))return;const prev=MEASURED.get(k);if(!prev||Math.abs(prev.w-b.width)>.5||Math.abs(prev.h-b.height)>.5){MEASURED.set(k,{w:b.width,h:b.height});changed=true}});return changed}
function paintWheel(){const st=stageEl();st.innerHTML=wheelSVG();if(measurePass()){st.innerHTML=wheelSVG();measurePass()}applyZoom()}

function layerName(id){return byId[id].label} function pointName(n){return n==="Node"?"N. Node":n==="SNode"?"S. Node":n}
function renderLedger(){const rows=activeContacts.filter(passesBase),ledger=document.getElementById("ledger");document.getElementById("ledgerCount").textContent=`${rows.length} exact cross-chart contact${rows.length===1?"":"s"} shown · click one to draw only that connection`;if(!rows.length){ledger.innerHTML='<div class="empty">No contacts match this combination of layers, aspects, points, and orb.</div>';return}const groups={};rows.forEach(c=>(groups[pairKey(c.a,c.b)]??=[]).push(c));ledger.innerHTML=Object.entries(groups).map(([key,cs])=>`<div class="pair-head">${key.split("|").map(layerName).join(" ↔ ")}</div>`+cs.sort((a,b)=>a.orb-b.orb).map(c=>{const f=byId[state.frame],h1=houseOf(c.lon1,f),h2=houseOf(c.lon2,f);return `<button class="contact ${state.isolate===c.id?"active":""}" data-contact-row="${c.id}" type="button"><div class="contact-main"><span style="color:${byId[c.a].color}">${esc(pointName(c.p1))}</span><span class="sym">${ASYM[c.aspect]}</span><span style="color:${byId[c.b].color}">${esc(pointName(c.p2))}</span><span class="orb">${orbText(c.orb)}</span></div><div class="contact-sub">${esc(c.pos1)} · H${h1} ↔ ${esc(c.pos2)} · H${h2}</div></button>`}).join("")).join("")}
const UMBRELLAS=[
 {label:"Authority & public direction",points:["Sun","Jupiter","MC"]},
 {label:"Public mood & belonging",points:["Moon","ASC"]},
 {label:"Record, speech & exchange",points:["Mercury"]},
 {label:"Value, alliance & resources",points:["Venus"]},
 {label:"Force, operation & contest",points:["Mars"]},
 {label:"Structure, law & constraint",points:["Saturn"]},
 {label:"System change & rupture",points:["Uranus"]},
 {label:"Collective image & dissolution",points:["Neptune"]},
 {label:"Power, exposure & regeneration",points:["Pluto"]},
 {label:"Wound, remedy & repair",points:["Chiron"]},
 {label:"Directional threshold",points:["Node"]},
 {label:"National-symbolic field",points:["America"]},
];
const SLOW_POINTS=new Set(["Saturn","Uranus","Neptune","Pluto"]),PHASE_CATEGORIES=new Set(["Lunations","Eclipses"]);
function strictMajorContacts(){return activeContacts.filter(c=>state.visible.has(c.a)&&state.visible.has(c.b)&&((c.hard&&c.orb<=1.000001)||(["sextile","trine"].includes(c.aspect)&&c.orb<=.500001))&&state.groups.has(pointGroup(c.a,c.p1))&&state.groups.has(pointGroup(c.b,c.p2)))}
function phaseAxis(layer){if(!PHASE_CATEGORIES.has(layer.category))return null;const sun=layer.points.find(p=>p.name==="Sun"),moon=layer.points.find(p=>p.name==="Moon");if(!sun||!moon)return null;const d=angDist(sun.lon,moon.lon);return d<=.100001?"lights":Math.abs(d-180)<=.100001?"axis":null}
function lightConfiguration(c){const A=byId[c.a],B=byId[c.b];if(PHASE_CATEGORIES.has(A.category)&&!PHASE_CATEGORIES.has(B.category)&&["Sun","Moon"].includes(c.p1)){const kind=phaseAxis(A);if(kind)return {key:`${A.id}|${B.id}|${c.p2}|${kind}`,event:A,target:B,targetPoint:c.p2,kind}}if(PHASE_CATEGORIES.has(B.category)&&!PHASE_CATEGORIES.has(A.category)&&["Sun","Moon"].includes(c.p2)){const kind=phaseAxis(B);if(kind)return {key:`${B.id}|${A.id}|${c.p1}|${kind}`,event:B,target:A,targetPoint:c.p1,kind}}return null}
function collapseLightConfigurations(rows){const map=new Map;for(const c of rows){const cfg=lightConfiguration(c),key=cfg?cfg.key:c.id;if(!map.has(key)){map.set(key,{...c,_cfg:cfg,_n:1});continue}const old=map.get(key);old._n++;if(c.orb<old.orb){const n=old._n;map.set(key,{...c,_cfg:cfg,_n:n})}}return [...map.values()]}
function overlapContactLabel(c){const a=state.selected.indexOf(c.a)+1,b=state.selected.indexOf(c.b)+1;if(c._cfg&&c._n>1){const e=state.selected.indexOf(c._cfg.event.id)+1,t=state.selected.indexOf(c._cfg.target.id)+1;return `${e} eclipse ${c._cfg.kind} ↔ ${t} ${pointName(c._cfg.targetPoint)} · ${orbText(c.orb)}`}return `${a} ${pointName(c.p1)} ${ASYM[c.aspect]} ${b} ${pointName(c.p2)} · ${orbText(c.orb)}`}
function recurrencePatterns(rows){const patterns=[],hard=rows.filter(c=>c.hard&&c.orb<=1.000001);
 const carries=hard.filter(c=>c.aspect==="conjunct"&&c.p1===c.p2&&SLOW_POINTS.has(c.p1)&&byId[c.a].category!=="Main Characters"&&byId[c.b].category!=="Main Characters").slice(0,4);
 if(carries.length)patterns.push({title:"Slow-body carry",body:carries.map(c=>`${pointName(c.p1)} remains within ${orbText(c.orb)} from ring ${state.selected.indexOf(c.a)+1} to ${state.selected.indexOf(c.b)+1}; this is continuity, not another vote.`).join(" · ")});
 const natalGroups=new Map;
 for(const c of hard){const A=byId[c.a],B=byId[c.b],char=A.category==="Main Characters"?A:B.category==="Main Characters"?B:null;if(!char)continue;const event=char===A?B:A;if(event.category==="Main Characters"||event.category==="Progressions")continue;const natalPoint=char===A?c.p1:c.p2,cfg=lightConfiguration(c),eventPoint=cfg&&cfg.target.id===char.id?"Eclipse axis":char===A?c.p2:c.p1,key=char.id+":"+natalPoint;const g=natalGroups.get(key)||{char,natalPoint,events:new Set,eventPoints:new Set,contacts:[]};g.events.add(event.id);g.eventPoints.add(eventPoint);g.contacts.push(c);natalGroups.set(key,g)}
 [...natalGroups.values()].filter(g=>g.events.size>=2).slice(0,4).forEach(g=>patterns.push({title:g.eventPoints.size===1&&SLOW_POINTS.has([...g.eventPoints][0])?"Sustained natal pressure":"Reactivated natal point",body:`${g.char.label} ${pointName(g.natalPoint)} is reached from ${g.events.size} selected chart moments by ${[...g.eventPoints].map(pointName).join(", ")}.`}))
 const ing=layers.filter(x=>x.category==="Ingresses"),phases=layers.filter(x=>PHASE_CATEGORIES.has(x.category)),chars=layers.filter(x=>x.category==="Main Characters");
 const between=(x,y)=>hard.filter(c=>(c.a===x.id&&c.b===y.id)||(c.a===y.id&&c.b===x.id)),pointAt=(c,id)=>c.a===id?c.p1:c.p2,chainKeys=new Set,chainChars=new Set;
 outer:for(const i of ing)for(const p of phases)for(const ch of chars){if((p.governing&&!i.label.startsWith(p.governing))||chainChars.has(ch.id))continue;let found=false;for(const ic of between(i,ch)){for(const pc of between(p,ch)){const anchor=pointAt(ic,ch.id);if(pointAt(pc,ch.id)!==anchor)continue;const iFactor=pointAt(ic,i.id),rawPFactor=pointAt(pc,p.id),axis=phaseAxis(p)&&["Sun","Moon"].includes(rawPFactor),pFactor=axis?"Eclipse axis":rawPFactor,bridge=between(i,p).find(c=>pointAt(c,i.id)===iFactor&&pointAt(c,p.id)===rawPFactor),chainKey=`${i.id}|${p.id}|${ch.id}|${anchor}|${iFactor}|${pFactor}`;if(!bridge||(iFactor===rawPFactor&&SLOW_POINTS.has(iFactor))||chainKeys.has(chainKey))continue;chainKeys.add(chainKey);chainChars.add(ch.id);patterns.push({title:"Governed three-layer bridge",body:`${i.label} ${pointName(iFactor)} ↔ ${p.label} ${pointName(pFactor)} converge on ${ch.label} ${pointName(anchor)}.`});found=true;break}if(found)break}if(chainChars.size>=2)break outer}
 return patterns;
}
function renderOverlaps(){const strict=strictMajorContacts(),collapsed=collapseLightConfigurations(strict),patterns=recurrencePatterns(strict),r=document.getElementById("recurrenceList"),u=document.getElementById("umbrellaList");r.innerHTML=patterns.length?patterns.map(p=>`<div class="pattern"><b>${esc(p.title)}</b><span>${esc(p.body)}</span></div>`).join(""):'<div class="overlap-empty">No repeated structure clears the strict 1° recurrence screen in this selection. That is a valid result, not an absence of astrology.</div>';
 const groups=UMBRELLAS.map(def=>({def,contacts:collapsed.filter(c=>def.points.includes(c.p1)||def.points.includes(c.p2))})).filter(x=>x.contacts.length);u.innerHTML=groups.length?groups.map(({def,contacts})=>`<div class="umbrella"><div class="umbrella-name">${esc(def.label)}</div><div class="umbrella-contacts">${contacts.slice(0,4).map(c=>`<button type="button" class="overlap-contact" data-overlap-contact="${c.id}" title="${esc(layerName(c.a))} ↔ ${esc(layerName(c.b))}">${esc(overlapContactLabel(c))}</button>`).join("")}${contacts.length>4?'<span class="catalog-note">more in ledger</span>':""}</div></div>`).join(""):'<div class="overlap-empty">No tight major contacts appear under the current selected charts and point groups.</div>'}
const CATEGORY_ORDER=["Ingresses","Lunations","Eclipses","Main Characters","Progressions"];
function pickerOptions(value,slot){let out='<option value="">None</option>';for(const category of CATEGORY_ORDER){const rows=DATA.catalog.filter(x=>x.category===category);if(!rows.length)continue;const historical=["Ingresses","Lunations","Eclipses"].includes(category);const years=historical?[...new Set(rows.map(x=>x.year||String(x.date||"").slice(0,4)))]:[null];for(const year of years){const group=year==null?rows:rows.filter(x=>(x.year||String(x.date||"").slice(0,4))===year);out+=`<optgroup label="${esc(year==null?category:`${category} · ${year}`)}">`;for(const row of group){const duplicate=state.selected.includes(row.id)&&state.selected[slot]!==row.id;const standing=row.standing==="nested_cardinal_stage"?" · nested stage":"";out+=`<option value="${row.id}" ${row.id===value?"selected":""} ${duplicate?"disabled":""}>${esc(row.label+standing)}</option>`}out+='</optgroup>'}}return out}
function renderControls(){document.getElementById("chartPickers").innerHTML=Array.from({length:4},(_,i)=>`<label class="picker-slot"><span>Ring ${i+1}${i===0?" · inner":i===3?" · outer":""}</span><select data-chart-slot="${i}" aria-label="Chart for ring ${i+1}">${pickerOptions(state.selected[i]||"",i)}</select></label>`).join("");const frame=document.getElementById("frameSelect");frame.innerHTML=layers.filter(x=>x.frameEligible).map(x=>`<option value="${x.id}" ${x.id===state.frame?"selected":""}>${esc(x.label)}</option>`).join("");const vis=visibleOrder();document.getElementById("layerChips").innerHTML=layerOrder().map(id=>{const x=byId[id],rank=vis.indexOf(id);return `<button type="button" class="layer-chip ${state.visible.has(x.id)?"":"off"} ${state.frame===x.id?"frame":""}" style="--layer:${x.color}" data-layer-chip="${x.id}" ${state.frame===x.id?'aria-pressed="true"':""}><span class="badge">${rank<0?"·":rank+1}</span>${esc(x.label.replace("Donald Trump ","Trump "))}${state.frame===x.id?" · house frame":""}</button>`}).join("");document.getElementById("aspectChips").innerHTML=["conjunct","opposite","square","trine","sextile","quincunx"].map(a=>`<button type="button" class="aspect-chip ${state.aspects.has(a)?"on":""}" data-aspect="${a}">${ASYM[a]} ${a}</button>`).join("");document.querySelectorAll("[data-house]").forEach(b=>{b.classList.toggle("on",b.dataset.house===state.house);b.disabled=b.dataset.house==="P"&&!byId[state.frame].placidusEligible});document.getElementById("relationSelect").value=state.relation;document.getElementById("orbSelect").value=state.orb;document.getElementById("aspectLines").checked=state.showLines;document.querySelectorAll("[data-point-group]").forEach(i=>i.checked=state.groups.has(i.dataset.pointGroup));const f=byId[state.frame],caution=f.frameCaution?`<br><strong>Frame note:</strong> ${esc(f.frameCaution)}`:"";document.getElementById("frameNote").innerHTML=`<strong>INNER → OUTER:</strong> ${vis.map((id,i)=>`${i+1} ${esc(byId[id].label.replace("Donald Trump ","Trump "))}`).join(" · ")} <em>(${WHEEL_WORD[vis.length]||"wheel"})</em><br>Houses and sign orientation belong only to <strong>${esc(f.label)}</strong>${f.place===DATA.meta.locationRule.replace("Mundane charts are cast for ","").replace(".","")?" in Washington, D.C.":""}.${caution}`}
function render(){renderControls();paintWheel();renderLedger();renderOverlaps();const st=document.getElementById("status");if(state.point){const [lid,name]=state.point.split(":"),layer=byId[lid],p=name==="ASC"?anglePoint(layer,"ASC"):name==="MC"?anglePoint(layer,"MC"):layer.points.find(x=>x.name===name);st.innerHTML=`<b style="color:${layer.color}">${esc(layer.label)} · ${esc(pointName(name))}</b><br>${esc((p.dms?p.dms+" ":"")+p.sign)} · house ${houseOf(p.lon,byId[state.frame])} in the ${esc(byId[state.frame].label)} frame`;st.classList.add("show")}else st.classList.remove("show")}

let pan=null,suppressClick=false;
document.addEventListener("click",ev=>{if(suppressClick){suppressClick=false;return}const chip=ev.target.closest("[data-layer-chip]");if(chip){const id=chip.dataset.layerChip;if(id!==state.frame){state.visible.has(id)?state.visible.delete(id):state.visible.add(id);state.isolate=null;render()}return}const asp=ev.target.closest("[data-aspect]");if(asp){const a=asp.dataset.aspect;state.aspects.has(a)?state.aspects.delete(a):state.aspects.add(a);state.isolate=null;render();return}const hs=ev.target.closest("[data-house]");if(hs&&hs.tagName==="BUTTON"){state.house=hs.dataset.house;state.isolate=null;render();return}const body=ev.target.closest("[data-body]");if(body){state.point=state.point===body.dataset.body?null:body.dataset.body;state.isolate=null;render();return}const overlap=ev.target.closest("[data-overlap-contact]");if(overlap){state.isolate=state.isolate===overlap.dataset.overlapContact?null:overlap.dataset.overlapContact;render();return}const row=ev.target.closest("[data-contact-row]");if(row){state.isolate=state.isolate===row.dataset.contactRow?null:row.dataset.contactRow;render();return}});
document.addEventListener("change",e=>{const picker=e.target.closest("[data-chart-slot]");if(!picker)return;const slot=Number(picker.dataset.chartSlot),value=picker.value,next=state.selected.slice();if(!value){if(next.length===1){renderControls();return}next.splice(slot,1)}else if(slot<next.length)next[slot]=value;else next.push(value);if(new Set(next).size!==next.length){renderControls();return}if(!next.some(id=>CATALOG_BY_ID[id]&&CATALOG_BY_ID[id].frameEligible)){renderControls();return}state.selected=next.slice(0,4);state.isolate=null;state.point=null;state.houseFilter=null;refreshSelection();render()});
document.getElementById("frameSelect").addEventListener("change",e=>{state.frame=e.target.value;if(state.house==="P"&&!CATALOG_BY_ID[state.frame].placidusEligible)state.house="W";state.visible.add(state.frame);state.isolate=null;state.houseFilter=null;render()});document.getElementById("relationSelect").addEventListener("change",e=>{state.relation=e.target.value;state.isolate=null;render()});document.getElementById("orbSelect").addEventListener("change",e=>{state.orb=e.target.value;state.isolate=null;render()});document.getElementById("aspectLines").addEventListener("change",e=>{state.showLines=e.target.checked;state.isolate=null;render()});document.querySelectorAll("[data-point-group]").forEach(i=>i.addEventListener("change",e=>{e.target.checked?state.groups.add(e.target.dataset.pointGroup):state.groups.delete(e.target.dataset.pointGroup);state.isolate=null;render()}));
document.getElementById("resetBtn").addEventListener("click",()=>{state.selected=DATA.meta.defaultSelection.slice();state.frame=DATA.meta.defaultFrame;state.house="W";state.relation="primary";state.orb="project";state.aspects=new Set(["conjunct","sextile","square","trine","quincunx","opposite"]);state.groups=new Set(["planet","angle","node","chiron","america"]);state.showLines=false;state.isolate=null;state.point=null;refreshSelection(true);document.getElementById("connectionsPanel").open=false;setZoom(1);const el=vpEl();el.scrollLeft=0;el.scrollTop=0;render()});
document.getElementById("openSpine").addEventListener("click",()=>window.parent.postMessage({action:"navigateTo",tab:"astrology-spine"},"*"));
document.getElementById("fullBtn").addEventListener("click",()=>{document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen()});
/* Export serialises the full 1000x1000 design space, never the clipped or
   zoomed viewport the reader happens to be looking at.                      */
document.getElementById("exportBtn").addEventListener("click",()=>{const live=document.getElementById("comparisonSvg");if(!live)return;const svg=live.cloneNode(true);svg.setAttribute("width",VB);svg.setAttribute("height",VB);svg.setAttribute("viewBox",`0 0 ${VB} ${VB}`);svg.setAttribute("xmlns","http://www.w3.org/2000/svg");const blob=new Blob(['<?xml version="1.0" encoding="UTF-8"?>\n'+new XMLSerializer().serializeToString(svg)],{type:"image/svg+xml"}),a=document.createElement("a");a.href=URL.createObjectURL(blob);a.download="freedom-250-chart-comparison.svg";a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000)});
document.getElementById("zFit").addEventListener("click",()=>setZoom(1));
document.getElementById("zReset").addEventListener("click",()=>{setZoom(1);const el=vpEl();el.scrollLeft=0;el.scrollTop=0});
document.getElementById("zIn").addEventListener("click",()=>{const r=vpEl().getBoundingClientRect();zoomAround(zoom+.1,r.left+r.width/2,r.top+r.height/2)});
document.getElementById("zOut").addEventListener("click",()=>{const r=vpEl().getBoundingClientRect();zoomAround(zoom-.1,r.left+r.width/2,r.top+r.height/2)});
document.getElementById("zRange").addEventListener("input",e=>setZoom(Number(e.target.value)/100));
vpEl().addEventListener("wheel",e=>{if(!(e.ctrlKey||e.metaKey))return;e.preventDefault();zoomAround(zoom*(e.deltaY<0?1.09:1/1.09),e.clientX,e.clientY)},{passive:false});
vpEl().addEventListener("pointerdown",e=>{if(zoom<=1.005||e.button!==0)return;const el=vpEl();pan={x:e.clientX,y:e.clientY,sl:el.scrollLeft,st:el.scrollTop,moved:false}});
window.addEventListener("pointermove",e=>{if(!pan)return;const dx=e.clientX-pan.x,dy=e.clientY-pan.y;if(!pan.moved&&Math.hypot(dx,dy)<4)return;pan.moved=true;const el=vpEl();el.classList.add("panning");el.scrollLeft=pan.sl-dx;el.scrollTop=pan.st-dy});
window.addEventListener("pointerup",()=>{if(pan&&pan.moved)suppressClick=true;pan=null;vpEl().classList.remove("panning")});
document.addEventListener("keydown",e=>{if(e.key==="Escape"&&(state.isolate||state.point)){state.isolate=null;state.point=null;render()}});
window.addEventListener("message",e=>{const m=e.data||{};if(m.action==="openComparison"&&Array.isArray(m.chartIds)){const ids=m.chartIds.map(resolveChartId).filter(Boolean).slice(0,4);const frameId=resolveChartId(m.frameId);if(ids.length&&ids.some(id=>CATALOG_BY_ID[id].frameEligible)){state.selected=ids;state.frame=ids.includes(frameId)&&CATALOG_BY_ID[frameId].frameEligible?frameId:ids.find(id=>CATALOG_BY_ID[id].frameEligible);refreshSelection();render()}return}if(m.action==="goToDate"&&m.date){const phase=x=>["Eclipses","Lunations"].includes(x.category),found=DATA.catalog.find(x=>x.date===m.date&&phase(x))||DATA.catalog.find(x=>x.utcDate===m.date&&phase(x))||DATA.catalog.find(x=>x.date===m.date&&x.category==="Ingresses");if(found){state.selected=[found.id].concat(state.selected.filter(id=>id!==found.id)).slice(0,4);if(found.frameEligible)state.frame=found.id;refreshSelection();render()}}});
new ResizeObserver(refit).observe(vpEl());window.addEventListener("resize",refit);
refreshSelection(true);fitScale=computeFit();render();refit();
</script></body></html>'''


def render_html() -> str:
    swe.set_ephe_path(str(EPHE))
    catalog, meta = build_catalog()
    catalog_by_id = {row["id"]: row for row in catalog}
    default_layers = [catalog_by_id[chart_id] for chart_id in DEFAULT_ORDER]
    contacts = build_contacts(default_layers)
    bundle = {"meta": meta, "catalog": catalog, "contacts": contacts}
    summary = " · ".join(
        f"{meta['catalogCounts'][category]} {category.lower()}"
        for category in ("Ingresses", "Lunations", "Eclipses", "Main Characters")
    )
    return (
        HTML_TEMPLATE
        .replace("__GLYPHS__", glyph_source())
        .replace("__DATA__", json.dumps(bundle, ensure_ascii=False, separators=(",", ":")))
        .replace("__CATALOG_SUMMARY__", html.escape(summary))
    )


def validate(text: str) -> None:
    required = [
        "Pick the charts. Keep one house frame.", "const DATA=", "Trump Secondary Progressed",
        "Project policy", "Connection ledger", "no approved exact JPL Horizons value",
        "defaultSelection", 'data-chart-slot=', "function computeContactsJS(",
        "function refreshSelection(", "Washington, D.C.", "F250_GLY",
        'class="chart-annulus"', "showLines:false", "INNER → OUTER",
        # responsive zoom viewport
        'id="wheelViewport"', 'id="wheelStage"', 'id="zRange"', 'id="zFit"',
        "function computeFit(", "ResizeObserver", 'class="zoombar"',
        # measured-bounds label engine
        "data-measure=", "function measurePass(", "function supports(",
        "function needGap(", "function layoutRing(", "function layoutWheel(", "function chainShape(", "function evenFan(",
        "const MEASURED=new Map()", 'class="placement-house"',
        # recurrence and archetypal overlap hearing
        "Natural overlaps", "Recurrence hearing", "Archetypal umbrellas", "Chronicle hypothesis",
        "function strictMajorContacts(", "function recurrencePatterns(", "function renderOverlaps(",
        'id="openSpine"', "this is continuity, not another vote", "return layer.frameEligible?pts.concat",
    ]
    missing = [marker for marker in required if marker not in text]
    if missing:
        raise RuntimeError("Chart Comparison validation failed: " + ", ".join(missing))
    expected = {"Ingresses": 50, "Lunations": 344, "Eclipses": 55, "Main Characters": 27, "Progressions": 1}
    for category, count in expected.items():
        if text.count(f'"category":"{category}"') != count:
            raise RuntimeError(f"Expected {count} {category} catalog rows")
    if text.count('"frameEligible":false') != 11:
        raise RuntimeError("Expected ten untimed natal overlays and one progression overlay")
    if "NaN" in text or "Infinity" in text:
        raise RuntimeError("Non-finite chart datum in output")
    bundle_match = re.search(r"const DATA=(.*?);\nconst SGN=", text, flags=re.S)
    if not bundle_match:
        raise RuntimeError("Chart Comparison data bundle is unreadable")
    bundle = json.loads(bundle_match.group(1))
    for contact in bundle["contacts"]:
        for layer_key, point_key in (("a", "p1"), ("b", "p2")):
            if contact[layer_key] == "special-trump-progressed-2026-08-12" and contact[point_key] in {"ASC", "MC"}:
                raise RuntimeError("Overlay-only progression angles leaked into default contacts")
    for marker in ("function ringPlan(", "function visibleOrder(", "WHEEL_WORD", "function ringLegend(", 'class="ring-legend"', 'class="ring-rim"'):
        if marker not in text:
            raise RuntimeError(f"Collapsing ring plan missing: {marker}")
    if "wheelSVGLegacy" in text:
        raise RuntimeError("Dead legacy wheel renderer is still present")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    text = render_html()
    validate(text)
    if args.check:
        existing = args.output.read_text(encoding="utf-8")
        validate(existing)
        if existing != text:
            raise SystemExit(f"STALE: {args.output}; run {Path(__file__).name}")
        catalog, meta = build_catalog()
        defaults = {row["id"]: row for row in catalog}
        print(f"Chart Comparison check OK · {len(catalog)} selectable charts · "
              f"{len(build_contacts([defaults[x] for x in DEFAULT_ORDER]))} default contacts · {args.output}")
        return
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    catalog, _meta = build_catalog()
    defaults = {row["id"]: row for row in catalog}
    print(f"Built {args.output} · {len(catalog)} selectable charts · "
          f"{len(build_contacts([defaults[x] for x in DEFAULT_ORDER]))} default contacts")


if __name__ == "__main__":
    main()
