#!/usr/bin/env python3
"""Compute the research-only credit-card transition astrology dataset.

Method boundary:
- geocentric tropical Swiss Ephemeris;
- locked Freedom 250 U.S. chart (1776-07-02, 17:10 LMT, Philadelphia);
- date-only anchors are cast at 12:00 UTC only as a planetary-position proxy;
- no event angles or houses are emitted for date-only anchors;
- month/year-only anchors are chronology bands and receive no point chart;
- Apple Pay's approximately 10:47 a.m. PDT reveal is a contemporaneously
  reported context clock (±2 minutes), not an Apple-authenticated timestamp.
"""

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import swisseph as swe


OUT = Path(__file__).with_name("CREDIT_CARD_TRANSITION_ASTROLOGY_DATA_2026-07-28.json")

SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces",
]
PLANETS = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mercury": swe.MERCURY,
    "Venus": swe.VENUS,
    "Mars": swe.MARS,
    "Jupiter": swe.JUPITER,
    "Saturn": swe.SATURN,
    "Uranus": swe.URANUS,
    "Neptune": swe.NEPTUNE,
    "Pluto": swe.PLUTO,
    "True Node": swe.TRUE_NODE,
}
OUTERS = ["Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
ASPECTS = [
    ("conjunction", 0.0),
    ("opposition", 180.0),
    ("square", 90.0),
    ("trine", 120.0),
    ("sextile", 60.0),
]
TRADITIONAL_RULERS = {
    "Aries": "Mars",
    "Taurus": "Venus",
    "Gemini": "Mercury",
    "Cancer": "Moon",
    "Leo": "Sun",
    "Virgo": "Mercury",
    "Libra": "Venus",
    "Scorpio": "Mars",
    "Sagittarius": "Jupiter",
    "Capricorn": "Saturn",
    "Aquarius": "Saturn",
    "Pisces": "Jupiter",
}
EVENTS = [
    {
        "id": "bankamericard",
        "label": "BankAmericard “Fresno Drop”",
        "date": "1958-09-18",
        "precision": "day",
        "place": "Fresno, California",
        "clock_grade": "B",
        "institutional_layer": "portable revolving bank credit",
        "source": "https://myemail-api.constantcontact.com/Fresno-City---County-Historical-Society-Grapevine-Newsletter.html?aid=69_GtuGTaaQ&soid=1102885321646",
        "boundary": "Day supported; mailing/delivery had no single public execution time.",
    },
    {
        "id": "interbank",
        "label": "Interbankard, Inc. incorporated",
        "date": "1966-11-03",
        "precision": "day",
        "place": "Delaware filing; exact filing place not load-bearing",
        "clock_grade": "A-",
        "institutional_layer": "multi-bank cooperative network",
        "source": "https://www.sec.gov/Archives/edgar/data/1141391/000119312505208278/ddef14a.htm",
        "source_secondary": "https://s2.q4cdn.com/242125233/files/doc_downloads/organizational_documents/2017/FINAL-Amended-and-Restated-Certificate-of-Incorporation-of-Mastercard-International-Incorporated.pdf",
        "boundary": "Legal incorporation date is supported; the earlier bankers’ organizing meeting has no public exact clock.",
    },
    {
        "id": "tila",
        "label": "Truth in Lending Act signed",
        "date": "1968-05-29",
        "precision": "day",
        "place": "Washington, D.C.",
        "clock_grade": "A-",
        "institutional_layer": "standardized public disclosure wrapper",
        "source": "https://www.govinfo.gov/content/pkg/STATUTE-82/pdf/STATUTE-82-Pg146.pdf",
        "boundary": "Enactment day is secure; enactment place and signing time are withheld.",
    },
    {
        "id": "card_protections",
        "label": "Unsolicited-card and liability amendments",
        "date": "1970-10-26",
        "precision": "day",
        "place": "Enactment place not publicly established",
        "clock_grade": "A date / place withheld",
        "institutional_layer": "issuance, fraud and cardholder-liability rules",
        "source": "https://www.govinfo.gov/content/pkg/STATUTE-84/pdf/STATUTE-84-Pg1114-2.pdf",
        "boundary": "Enactment day and city are secure; signing time is not publicly stated.",
    },
    {
        "id": "base_i",
        "label": "BASE I limited-production start",
        "date": "1973-04-04",
        "precision": "day",
        "place": "Distributed Visa network; no single locality",
        "clock_grade": "B",
        "institutional_layer": "electronic authorization",
        "source": "https://www.visa.co.il/content/dam/VCOM/download/corporate/media/visanet-technology/visa-net-booklet.pdf",
        "source_secondary": "https://era.ed.ac.uk/bitstream/handle/1842/2672/Stearns%20DL%20thesis%2007.pdf",
        "boundary": "Visa supports 1973; April 4 comes from a scholarly history based on contemporary/internal records. No locality-derived chart.",
    },
    {
        "id": "base_ii",
        "label": "BASE II full-scale network operation",
        "date": "1974-11-01",
        "precision": "day",
        "place": "Distributed across 86 processing centers",
        "clock_grade": "A-/B+",
        "institutional_layer": "electronic clearing and settlement",
        "source": "https://fraser.stlouisfed.org/files/docs/publications/weeklybanknews/weeklybanknews_19741106.pdf",
        "source_secondary": "https://www.visa.co.il/content/dam/VCOM/download/corporate/media/visanet-technology/visa-net-booklet.pdf",
        "boundary": "Operation date is supported; no single place or instant exists for the distributed rollout.",
    },
    {
        "id": "marquette",
        "label": "Marquette rate-exportation decision",
        "date": "1978-12-18",
        "precision": "day",
        "place": "Washington, D.C.",
        "clock_grade": "A-",
        "institutional_layer": "national pricing of revolving card credit",
        "source": "https://www.govinfo.gov/app/details/USREPORTS-439/USREPORTS-439-299",
        "boundary": "Decision day and court are secure; announcement time is not publicly stated.",
    },
    {
        "id": "securitization",
        "label": "Credit-card receivables securitization begins",
        "date": "1986–1987",
        "precision": "year-band",
        "place": "United States",
        "clock_grade": "D",
        "institutional_layer": "capital-markets funding of revolving receivables",
        "source": "https://www.fdic.gov/credit-card-securitization-manual/chapter-ii-securitization-transaction-overview",
        "source_secondary": "https://www.minneapolisfed.org/article/1995/will-the-securitization-revolution-spread",
        "boundary": "A March 1986 private placement and the FDIC’s 1987 public-history anchor are definition-sensitive. No point chart.",
    },
    {
        "id": "apple_pay",
        "label": "Apple Pay announced",
        "date": "2014-09-09",
        "precision": "day",
        "place": "Cupertino, California",
        "clock_grade": "A date / B+ reported reveal minute",
        "institutional_layer": "tokenized wallet credential over card rails",
        "source": "https://www.apple.com/newsroom/2014/09/09Apple-Announces-Apple-Pay/",
        "source_secondary": "https://www.macrumors.com/2014/09/09/iphone-6-iwatch-event-live/",
        "boundary": "Apple establishes the day and city. A contemporaneous liveblog timestamps Cook’s reveal at approximately 10:47 a.m. PDT; use ±2 minutes.",
        "context_utc": "2014-09-09T17:47:00Z",
        "context_lat": 37.3230,
        "context_lon": -122.0322,
    },
    {
        "id": "emv_shift",
        "label": "U.S. EMV counterfeit-fraud liability shift",
        "date": "2015-10-01",
        "precision": "day",
        "place": "United States",
        "clock_grade": "A-",
        "institutional_layer": "private liability rule accelerates terminal migration",
        "source": "https://usa.visa.com/content/dam/VCOM/global/partner-with-us/documents/visa-liability-shift.pdf",
        "boundary": "Effective day is secure; this is a distributed rule, not one local event.",
    },
    {
        "id": "stablecoin_settlement",
        "label": "Visa announces U.S. USDC network settlement",
        "date": "2025-12-16",
        "precision": "day",
        "place": "United States",
        "clock_grade": "A-",
        "institutional_layer": "new settlement asset behind unchanged card acceptance",
        "source": "https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-launches-stablecoin-settlement-in-the-united-states.html",
        "boundary": "Announcement day is primary; publication time is not used.",
    },
]


def julday(dt: datetime) -> float:
    dt = dt.astimezone(timezone.utc)
    hour = dt.hour + dt.minute / 60 + dt.second / 3600 + dt.microsecond / 3_600_000_000
    return swe.julday(dt.year, dt.month, dt.day, hour)


def position(jd: float, body: str) -> tuple[float, float]:
    values, _ = swe.calc_ut(jd, PLANETS[body], swe.FLG_SWIEPH | swe.FLG_SPEED)
    return values[0] % 360, values[3]


def sign(longitude: float) -> str:
    return SIGNS[int(longitude // 30) % 12]


def format_position(longitude: float) -> str:
    return f"{longitude % 30:.2f}° {sign(longitude)}"


def angular_distance(a: float, b: float) -> float:
    return abs((a - b + 180) % 360 - 180)


def applying_state(jd: float, moving: str, target: float, aspect_angle: float) -> str:
    now = abs(angular_distance(position(jd, moving)[0], target) - aspect_angle)
    later = abs(angular_distance(position(jd + 0.25, moving)[0], target) - aspect_angle)
    return "applying" if later < now else "separating"


def mutual_applying_state(jd: float, first: str, second: str, aspect_angle: float) -> str:
    now = abs(angular_distance(position(jd, first)[0], position(jd, second)[0]) - aspect_angle)
    later = abs(
        angular_distance(position(jd + 0.25, first)[0], position(jd + 0.25, second)[0])
        - aspect_angle
    )
    return "applying" if later < now else "separating"


def aspect_hit(a: float, b: float, max_orb: float) -> tuple[str, float, float] | None:
    separation = angular_distance(a, b)
    candidates = [(name, angle, abs(separation - angle)) for name, angle in ASPECTS]
    name, angle, orb = min(candidates, key=lambda item: item[2])
    if orb <= max_orb:
        return name, angle, orb
    return None


def midpoint(a: float, b: float) -> float:
    return (a + ((b - a) % 360) / 2) % 360


def whole_sign_house(longitude: float, ascendant: float) -> int:
    return ((int(longitude // 30) - int(ascendant // 30)) % 12) + 1


def traditional_dispositor(body: str, positions: dict) -> str:
    return TRADITIONAL_RULERS[sign(positions[body]["longitude"])]


def dispositor_path(body: str, positions: dict) -> list[str]:
    path = [body]
    seen = {body}
    current = body
    for _ in range(12):
        ruler = traditional_dispositor(current, positions)
        path.append(ruler)
        if ruler == current or ruler in seen:
            break
        seen.add(ruler)
        current = ruler
    return path


# Locked U.S. chart from the live Monetary Chronicle engine.
PHL_LON = -75.1652
US_UT_HOUR = 17 + 10 / 60 - PHL_LON / 15
US_JD = swe.julday(1776, 7, 2, US_UT_HOUR)
US_NATAL = {body: position(US_JD, body)[0] for body in PLANETS}
US_MONEY = {
    body: US_NATAL[body]
    for body in ["Venus", "Jupiter", "Sun", "Mercury", "Moon", "Pluto"]
}
US_MIDPOINTS = {
    "Venus/Jupiter": midpoint(US_NATAL["Venus"], US_NATAL["Jupiter"]),
    "Sun/Jupiter": midpoint(US_NATAL["Sun"], US_NATAL["Jupiter"]),
    "Moon/Pluto": midpoint(US_NATAL["Moon"], US_NATAL["Pluto"]),
    "Saturn/Pluto": midpoint(US_NATAL["Saturn"], US_NATAL["Pluto"]),
}


def point_record(event: dict) -> dict:
    dt = datetime.fromisoformat(event["date"]).replace(
        hour=12, minute=0, second=0, tzinfo=timezone.utc
    )
    jd = julday(dt)
    positions = {}
    for body in PLANETS:
        longitude, speed = position(jd, body)
        positions[body] = {
            "longitude": round(longitude, 6),
            "position": format_position(longitude),
            "retrograde": speed < 0,
        }

    outer_cycles = []
    for i, first in enumerate(OUTERS):
        for second in OUTERS[i + 1:]:
            hit = aspect_hit(positions[first]["longitude"], positions[second]["longitude"], 8.0)
            if hit:
                name, angle, orb = hit
                outer_cycles.append(
                    {
                        "pair": f"{first}–{second}",
                        "aspect": name,
                        "orb": round(orb, 3),
                    }
                )

    us_hits = []
    for moving in OUTERS:
        moving_lon = positions[moving]["longitude"]
        for natal_body, natal_lon in US_MONEY.items():
            hit = aspect_hit(moving_lon, natal_lon, 3.0)
            if hit:
                name, angle, orb = hit
                us_hits.append(
                    {
                        "transit": moving,
                        "aspect": name,
                        "natal": natal_body,
                        "orb": round(orb, 3),
                        "state": applying_state(jd, moving, natal_lon, angle),
                    }
                )

    midpoint_hits = []
    for moving in OUTERS:
        moving_lon = positions[moving]["longitude"]
        for midpoint_name, midpoint_lon in US_MIDPOINTS.items():
            separation = angular_distance(moving_lon, midpoint_lon)
            nearest = min([0, 45, 90, 135, 180], key=lambda angle: abs(separation - angle))
            orb = abs(separation - nearest)
            if orb <= 1.5:
                midpoint_hits.append(
                    {
                        "transit": moving,
                        "midpoint": midpoint_name,
                        "harmonic_angle": nearest,
                        "orb": round(orb, 3),
                    }
                )

    # Moon/sign stability over the civil UTC date. This is metadata only; it
    # prevents a noon proxy from silently manufacturing a lunar sign.
    start_jd = swe.julday(dt.year, dt.month, dt.day, 0)
    end_jd = swe.julday(dt.year, dt.month, dt.day, 24 - 1 / 3600)
    moon_start = position(start_jd, "Moon")[0]
    moon_end = position(end_jd, "Moon")[0]
    moon_stability = {
        "start": format_position(moon_start),
        "end": format_position(moon_end),
        "same_sign_all_utc_date": sign(moon_start) == sign(moon_end),
    }

    record = {
        **event,
        "proxy_utc": dt.isoformat().replace("+00:00", "Z"),
        "positions": positions,
        "outer_cycles": sorted(outer_cycles, key=lambda item: item["orb"]),
        "us_money_axis_hits": sorted(us_hits, key=lambda item: item["orb"]),
        "us_money_midpoint_hits": sorted(midpoint_hits, key=lambda item: item["orb"]),
        "moon_stability": moon_stability,
        "angles_withheld": True,
        "houses_withheld": True,
    }

    if event.get("context_utc"):
        cdt = datetime.fromisoformat(event["context_utc"].replace("Z", "+00:00"))
        cjd = julday(cdt)
        _, ascmc = swe.houses(
            cjd, event["context_lat"], event["context_lon"], b"W"
        )
        context_positions = {}
        for body in PLANETS:
            longitude, speed = position(cjd, body)
            context_positions[body] = {
                "longitude": round(longitude, 6),
                "position": format_position(longitude),
                "retrograde": speed < 0,
                "whole_sign_house": whole_sign_house(longitude, ascmc[0]),
            }
        context_aspects = []
        context_bodies = list(PLANETS)
        for index, first in enumerate(context_bodies):
            for second in context_bodies[index + 1:]:
                max_orb = 8.0 if first in {"Sun", "Moon"} or second in {"Sun", "Moon"} else 6.0
                hit = aspect_hit(
                    context_positions[first]["longitude"],
                    context_positions[second]["longitude"],
                    max_orb,
                )
                if hit:
                    name, angle, orb = hit
                    context_aspects.append(
                        {
                            "pair": f"{first}–{second}",
                            "aspect": name,
                            "orb": round(orb, 3),
                            "state": mutual_applying_state(cjd, first, second, angle),
                        }
                    )
        angle_contacts = []
        for body, p in context_positions.items():
            for angle_name, angle_longitude in (("Ascendant", ascmc[0]), ("MC", ascmc[1])):
                separation = angular_distance(p["longitude"], angle_longitude)
                for aspect_name, aspect_angle in (
                    ("conjunction", 0.0),
                    ("opposition", 180.0),
                    ("square", 90.0),
                ):
                    orb = abs(separation - aspect_angle)
                    if orb <= 3.0:
                        angle_contacts.append(
                            {
                                "planet": body,
                                "aspect": aspect_name,
                                "angle": angle_name,
                                "orb": round(orb, 3),
                            }
                        )
                        break
        ascendant_ruler = TRADITIONAL_RULERS[sign(ascmc[0])]
        record["contextual_container_clock"] = {
            "utc": event["context_utc"],
            "local": "2014-09-09 10:47 PDT",
            "ascendant": {
                "longitude": round(ascmc[0], 6),
                "position": format_position(ascmc[0]),
            },
            "mc": {
                "longitude": round(ascmc[1], 6),
                "position": format_position(ascmc[1]),
            },
            "positions": context_positions,
            "aspects": sorted(context_aspects, key=lambda item: item["orb"]),
            "angle_contacts": sorted(angle_contacts, key=lambda item: item["orb"]),
            "chart_ruler": ascendant_ruler,
            "chart_ruler_path": dispositor_path(ascendant_ruler, context_positions),
            "dispositor_paths": {
                body: dispositor_path(body, context_positions)
                for body in context_positions
            },
            "boundary": "Contemporaneously reported Apple Pay reveal frame (±2 minutes); excluded from cross-event signature counts.",
        }
    return record


records = []
for event in EVENTS:
    if event["precision"] in {"year", "year-band"}:
        records.append(
            {
                **event,
                "point_chart": None,
                "angles_withheld": True,
                "houses_withheld": True,
            }
        )
    else:
        records.append(point_record(event))


def signature_counts(records: list[dict]) -> dict:
    cycle_counts: dict[str, int] = {}
    natal_counts: dict[str, int] = {}
    midpoint_counts: dict[str, int] = {}
    for record in records:
        for hit in record.get("outer_cycles", []):
            key = f"{hit['pair']} {hit['aspect']}"
            cycle_counts[key] = cycle_counts.get(key, 0) + 1
        for hit in record.get("us_money_axis_hits", []):
            key = f"{hit['transit']} {hit['aspect']} US {hit['natal']}"
            natal_counts[key] = natal_counts.get(key, 0) + 1
        for hit in record.get("us_money_midpoint_hits", []):
            key = f"{hit['transit']} {hit['harmonic_angle']}° US {hit['midpoint']}"
            midpoint_counts[key] = midpoint_counts.get(key, 0) + 1
    return {
        "outer_cycles": dict(sorted(cycle_counts.items(), key=lambda item: (-item[1], item[0]))),
        "us_money_axis_hits": dict(sorted(natal_counts.items(), key=lambda item: (-item[1], item[0]))),
        "us_money_midpoint_hits": dict(sorted(midpoint_counts.items(), key=lambda item: (-item[1], item[0]))),
    }


payload = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "method": {
        "ephemeris": "pyswisseph; geocentric tropical",
        "proxy": "12:00 UTC for planetary longitude only on day-precision anchors",
        "house_system": "Whole Sign is project standard; event houses withheld without an exact public clock",
        "us_chart": "1776-07-02 17:10 LMT Philadelphia; locked Sagittarius-rising chart",
        "cross_event_orbs": {
            "outer_mutual": "8° descriptive background",
            "outer_to_us_money_axis": "3°",
            "mod45_money_midpoints": "1.5°",
        },
        "speech_level": "archetypal and structural; not concretely causal or predictive",
    },
    "us_money_axis": {
        body: {
            "longitude": round(longitude, 6),
            "position": format_position(longitude),
        }
        for body, longitude in US_MONEY.items()
    },
    "events": records,
    "cross_event_counts": signature_counts(records),
}

OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(OUT)
print(f"events={len(records)} point_charts={sum('positions' in record for record in records)}")
