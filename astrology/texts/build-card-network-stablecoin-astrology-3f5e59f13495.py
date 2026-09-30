#!/usr/bin/env python3
"""Compute the card-network stablecoin Money × Sky research dataset.

Clock policy supplied by Katie on 2026-07-29:
- use a sourced event time when available;
- if the event is known to have occurred during the day but no precise time is
  established, cast 12:00 local as an explicit noon research convention;
- if no event time is known, cast 00:00 local as an explicit midnight research
  convention.

No assumed angle or house is represented as an observed event clock.
"""

from __future__ import annotations

import json
import importlib.util
import sys
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import swisseph as swe


HERE = Path(__file__).resolve().parent
OUT = HERE / "CARD_NETWORK_STABLECOIN_ASTROLOGY_DATA_2026-07-29.json"
VAULT_TEMPLATES = Path(
    "Chronicle/99 - Templates"
)
sys.path.insert(0, str(VAULT_TEMPLATES))
_mp_spec = importlib.util.spec_from_file_location(
    "f250_minor_points", VAULT_TEMPLATES / "minor_points.py"
)
minor_points = importlib.util.module_from_spec(_mp_spec)
assert _mp_spec.loader
_mp_spec.loader.exec_module(minor_points)

DC_LAT = 38.8951
DC_LON = -77.0364

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
    "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury",
    "Cancer": "Moon", "Leo": "Sun", "Virgo": "Mercury",
    "Libra": "Venus", "Scorpio": "Mars", "Sagittarius": "Jupiter",
    "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter",
}


EVENTS = [
    {
        "id": "apple_pay_control",
        "label": "Apple Pay reveal frame",
        "date": "2014-09-09",
        "local_time": "10:47",
        "timezone": "America/Los_Angeles",
        "clock_mode": "reported",
        "clock_grade": "B+ reported reveal minute",
        "place": "Cupertino, California",
        "lat": 37.3230,
        "lon": -122.0322,
        "place_basis": "Apple event location",
        "institutional_layer": "credential adapter over card rails",
        "source": "https://www.apple.com/newsroom/2014/09/09Apple-Announces-Apple-Pay/",
        "source_secondary": "https://www.macrumors.com/2014/09/09/iphone-6-iwatch-event-live/",
        "boundary": "Apple establishes the day and place; a contemporaneous liveblog places the reveal near 10:47 a.m. PDT. Carry ±2 minutes.",
    },
    {
        "id": "visa_acquirer_usdc",
        "label": "Visa expands USDC settlement to Worldpay and Nuvei",
        "date": "2023-09-05",
        "local_time": "00:00",
        "timezone": "America/Los_Angeles",
        "clock_mode": "midnight_proxy",
        "clock_grade": "M · midnight convention",
        "place": "San Francisco, California",
        "lat": 37.7749,
        "lon": -122.4194,
        "place_basis": "press-release dateline",
        "institutional_layer": "acquirer-side stablecoin settlement",
        "source": "https://investor.visa.com/news/news-details/2023/Visa-Expands-Stablecoin-Settlement-Capabilities-to-Merchant-Acquirers/",
        "boundary": "Primary source establishes date and San Francisco dateline, not release or operational transaction time. Midnight is an explicit research convention.",
    },
    {
        "id": "visa_bridge_launch",
        "label": "Visa–Bridge stablecoin-linked cards announced",
        "date": "2025-04-30",
        "local_time": "00:00",
        "timezone": "America/Los_Angeles",
        "clock_mode": "midnight_proxy",
        "clock_grade": "M · midnight convention",
        "place": "San Francisco, California",
        "lat": 37.7749,
        "lon": -122.4194,
        "place_basis": "Business Wire dateline",
        "institutional_layer": "stablecoin-funded Visa card",
        "source": "https://investor.visa.com/news/news-details/2025/Visa-and-Bridge-Partner-to-Make-Stablecoins-Accessible-for-Everyday-Purchases/",
        "source_secondary": "https://www.businesswire.com/news/home/20250430334927/en/Visa-and-Bridge-Partner-to-Make-Stablecoins-Accessible-for-Everyday-Purchases",
        "boundary": "Primary release establishes date and San Francisco dateline but no publication or launch minute. Midnight is an explicit research convention.",
    },
    {
        "id": "fiserv_fiusd",
        "label": "Fiserv announces FIUSD",
        "date": "2025-06-23",
        "local_time": "00:00",
        "timezone": "America/Chicago",
        "clock_mode": "midnight_proxy",
        "clock_grade": "M · midnight convention",
        "place": "Milwaukee, Wisconsin",
        "lat": 43.0389,
        "lon": -87.9065,
        "place_basis": "Fiserv corporate-location proxy",
        "institutional_layer": "bank/core/merchant stablecoin platform",
        "source": "https://investors.fiserv.com/news-releases/news-release-details/fiserv-launches-new-fiusd-stablecoin-financial-institutions",
        "boundary": "Announcement date is secure; no release time or transaction time is established. Milwaukee is the corporate-location proxy and midnight is the time convention.",
    },
    {
        "id": "visa_us_settlement",
        "label": "Visa launches U.S. USDC settlement",
        "date": "2025-12-16",
        "local_time": "00:00",
        "timezone": "America/Los_Angeles",
        "clock_mode": "midnight_proxy",
        "clock_grade": "M · midnight convention",
        "place": "San Francisco, California",
        "lat": 37.7749,
        "lon": -122.4194,
        "place_basis": "Business Wire dateline",
        "institutional_layer": "issuer/acquirer network settlement",
        "source": "https://investor.visa.com/news/news-details/2025/Visa-Launches-Stablecoin-Settlement-in-the-United-States-Marking-a-Breakthrough-for-Stablecoin-Integration/default.aspx",
        "source_secondary": "https://www.businesswire.com/news/home/20251216483172/en/Visa-Launches-Stablecoin-Settlement-in-the-United-States-Marking-a-Breakthrough-for-Stablecoin-Integration",
        "boundary": "Announcement date and San Francisco dateline are secure; no announcement or first-settlement minute is published. Midnight is an explicit research convention.",
    },
    {
        "id": "visa_bridge_expansion",
        "label": "Visa–Bridge card expansion announced",
        "date": "2026-03-03",
        "local_time": "00:00",
        "timezone": "America/Los_Angeles",
        "clock_mode": "midnight_proxy",
        "clock_grade": "M · midnight convention",
        "place": "San Francisco, California",
        "lat": 37.7749,
        "lon": -122.4194,
        "place_basis": "Business Wire dateline",
        "institutional_layer": "global card expansion + settlement pilot",
        "source": "https://investor.visa.com/news/news-details/2026/Visa-and-Bridge-Expand-Collaboration-with-Plans-to-Bring-Stablecoin-Linked-Cards-to-Over-100-Countries/default.aspx",
        "boundary": "Primary release establishes date and San Francisco dateline but no publication or activation minute. Midnight is an explicit research convention.",
    },
    {
        "id": "square_bitcoin_terms",
        "label": "Square Bitcoin current terms effective",
        "date": "2026-03-16",
        "local_time": "00:00",
        "timezone": "America/Los_Angeles",
        "clock_mode": "midnight_proxy",
        "clock_grade": "M · midnight convention",
        "place": "San Francisco, California",
        "lat": 37.7749,
        "lon": -122.4194,
        "place_basis": "Block corporate-location proxy",
        "institutional_layer": "native non-card point of sale",
        "source": "https://squareup.com/us/en/legal/general/square-bitcoin-alpha-terms",
        "source_secondary": "https://squareup.com/help/us/en/article/8622-accept-and-manage-bitcoin-payments",
        "boundary": "The legal effective date is charted, not the first merchant transaction. No effective-time clause was located; midnight is the stated convention.",
    },
    {
        "id": "mastercard_bvnk",
        "label": "Mastercard signs BVNK acquisition agreement",
        "date": "2026-03-17",
        "local_time": "00:00",
        "timezone": "America/New_York",
        "clock_mode": "midnight_proxy",
        "clock_grade": "M · midnight convention",
        "place": "Purchase, New York",
        "lat": 41.0409,
        "lon": -73.7146,
        "place_basis": "Mastercard press-release dateline",
        "institutional_layer": "proposed stablecoin orchestration acquisition",
        "source": "https://www.mastercard.com/global/en/news-and-trends/press/2026/march/Mastercard-to-acquire-BVNK-to-connect-on-chain-payments-and-fiat-rails.html",
        "source_secondary": "https://www.sec.gov/Archives/edgar/data/1141391/000114139126000031/ma-20260331.htm",
        "boundary": "Release establishes date and Purchase dateline but not signing or publication time. Midnight is the convention; signing is not closing.",
    },
    {
        "id": "stripe_sessions",
        "label": "Stripe Sessions stablecoin product-line announcements",
        "date": "2026-04-29",
        "local_time": "12:00",
        "timezone": "America/Los_Angeles",
        "clock_mode": "noon_proxy",
        "clock_grade": "N · known morning, noon convention",
        "place": "Moscone West, San Francisco",
        "lat": 37.7843,
        "lon": -122.4016,
        "place_basis": "official conference venue",
        "institutional_layer": "stablecoin cards + wallet/payment infrastructure",
        "source": "https://stripe.com/blog/everything-we-announced-at-sessions-2026",
        "source_secondary": "https://stripe.com/sessions/2022/marketplaces",
        "boundary": "Stripe says the announcements occurred 'this morning' at Sessions in San Francisco. No exact product-announcement minute is used; local noon follows the user's daytime convention.",
    },
    {
        "id": "paypal_crypto_terms",
        "label": "PayPal Pay with Crypto terms effective",
        "date": "2026-05-19",
        "local_time": "00:00",
        "timezone": "America/Los_Angeles",
        "clock_mode": "midnight_proxy",
        "clock_grade": "M · midnight convention",
        "place": "San Jose, California",
        "lat": 37.3382,
        "lon": -121.8863,
        "place_basis": "PayPal corporate-location proxy",
        "institutional_layer": "crypto-funded checkout through PYUSD to fiat",
        "source": "https://www.paypal.com/us/legalhub/paypal/crypto-payment-method?locale.x=en_US",
        "boundary": "The operative date is charted; no effective-time clause or first transaction is established. Midnight is the explicit convention.",
    },
    {
        "id": "mastercard_settlement",
        "label": "Mastercard expands stablecoin settlement",
        "date": "2026-06-03",
        "local_time": "00:00",
        "timezone": "America/New_York",
        "clock_mode": "midnight_proxy",
        "clock_grade": "M · midnight convention",
        "place": "Purchase, New York",
        "lat": 41.0409,
        "lon": -73.7146,
        "place_basis": "Mastercard press-release dateline",
        "institutional_layer": "multi-asset network settlement rollout",
        "source": "https://www.mastercard.com/global/en/news-and-trends/press/2026/june/mastercard-expands-settlement-capabilities-to-include-stablecoin.html",
        "boundary": "Release establishes date and Purchase dateline but no release or settlement minute. Midnight is the explicit convention.",
    },
    {
        "id": "hyperwallet_pyusd",
        "label": "Hyperwallet PYUSD payout terms effective",
        "date": "2026-06-29",
        "local_time": "00:00",
        "timezone": "America/Los_Angeles",
        "clock_mode": "midnight_proxy",
        "clock_grade": "M · midnight convention",
        "place": "San Jose, California",
        "lat": 37.3382,
        "lon": -121.8863,
        "place_basis": "PayPal corporate-location proxy",
        "institutional_layer": "fiat-funded stablecoin payee payout",
        "source": "https://www.paypal.com/us/legalhub/paypal/hyperwallet-pyusd-payouts-tnc?country.x=US&locale.x=en_US",
        "boundary": "The operative date is charted; no effective-time clause or first payout minute is established. Midnight is the explicit convention.",
    },
    {
        "id": "jcb_circle_mou",
        "label": "JCB–Circle stablecoin MOU announced",
        "date": "2026-07-14",
        "local_time": "00:00",
        "timezone": "Asia/Tokyo",
        "clock_mode": "midnight_proxy",
        "clock_grade": "M · midnight convention",
        "place": "Minato-ku, Tokyo",
        "lat": 35.6581,
        "lon": 139.7516,
        "place_basis": "JCB head-office location stated in release",
        "institutional_layer": "cross-border treasury + store-payment PoCs",
        "source": "https://www.global.jcb/en/press/2026/202607141000_products.html",
        "boundary": "Release establishes date and JCB head-office location but no signing or publication time. The URL suffix is not treated as authenticated clock evidence; midnight is the convention.",
    },
    {
        "id": "visa_vsp",
        "label": "Visa Stablecoin Platform announced",
        "date": "2026-07-16",
        "local_time": "00:00",
        "timezone": "America/Los_Angeles",
        "clock_mode": "midnight_proxy",
        "clock_grade": "M · midnight convention",
        "place": "San Francisco, California",
        "lat": 37.7749,
        "lon": -122.4194,
        "place_basis": "Business Wire dateline",
        "institutional_layer": "wallet + mint/burn + network control plane",
        "source": "https://investor.visa.com/news/news-details/2026/Visa-Introduces-Platform-for-Stablecoin-Minting-Movement-and-Management/default.aspx",
        "boundary": "Primary release establishes date and San Francisco dateline but no publication or beta-start minute. Midnight is the explicit convention.",
    },
]


def julday(dt: datetime) -> float:
    utc = dt.astimezone(timezone.utc)
    hour = utc.hour + utc.minute / 60 + utc.second / 3600
    return swe.julday(utc.year, utc.month, utc.day, hour)


def position(jd: float, body: str) -> tuple[float, float]:
    values, _ = swe.calc_ut(jd, PLANETS[body], swe.FLG_SWIEPH | swe.FLG_SPEED)
    return values[0] % 360, values[3]


def sign(longitude: float) -> str:
    return SIGNS[int(longitude // 30) % 12]


def format_position(longitude: float) -> str:
    return f"{longitude % 30:.2f}° {sign(longitude)}"


def angular_distance(a: float, b: float) -> float:
    return abs((a - b + 180) % 360 - 180)


def aspect_hit(a: float, b: float, max_orb: float):
    separation = angular_distance(a, b)
    name, angle, orb = min(
        ((name, angle, abs(separation - angle)) for name, angle in ASPECTS),
        key=lambda item: item[2],
    )
    return (name, angle, orb) if orb <= max_orb else None


def applying_state(jd: float, moving: str, target: float, angle: float) -> str:
    now = abs(angular_distance(position(jd, moving)[0], target) - angle)
    later = abs(angular_distance(position(jd + 0.25, moving)[0], target) - angle)
    return "applying" if later < now else "separating"


def mutual_applying_state(jd: float, first: str, second: str, angle: float) -> str:
    now = abs(angular_distance(position(jd, first)[0], position(jd, second)[0]) - angle)
    later = abs(
        angular_distance(position(jd + 0.25, first)[0], position(jd + 0.25, second)[0])
        - angle
    )
    return "applying" if later < now else "separating"


def midpoint(a: float, b: float) -> float:
    return (a + ((b - a) % 360) / 2) % 360


def whole_sign_house(longitude: float, ascendant: float) -> int:
    return ((int(longitude // 30) - int(ascendant // 30)) % 12) + 1


def dispositor_path(body: str, positions: dict) -> list[str]:
    path = [body]
    seen = {body}
    current = body
    for _ in range(12):
        ruler = TRADITIONAL_RULERS[sign(positions[current]["longitude"])]
        path.append(ruler)
        if ruler == current or ruler in seen:
            break
        seen.add(ruler)
        current = ruler
    return path


# Locked Freedom 250 U.S. chart.
PHL_LON = -75.1652
US_UT_HOUR = 17 + 10 / 60 - PHL_LON / 15
US_JD = swe.julday(1776, 7, 2, US_UT_HOUR)
US_NATAL = {body: position(US_JD, body)[0] for body in PLANETS}
US_MONEY = {body: US_NATAL[body] for body in ["Venus", "Jupiter", "Sun", "Mercury", "Moon", "Pluto"]}
US_MIDPOINTS = {
    "Venus/Jupiter": midpoint(US_NATAL["Venus"], US_NATAL["Jupiter"]),
    "Sun/Jupiter": midpoint(US_NATAL["Sun"], US_NATAL["Jupiter"]),
    "Moon/Pluto": midpoint(US_NATAL["Moon"], US_NATAL["Pluto"]),
    "Saturn/Pluto": midpoint(US_NATAL["Saturn"], US_NATAL["Pluto"]),
}


def cast_positions(jd: float, ascendant: float) -> tuple[dict, str]:
    positions = {}
    for body in PLANETS:
        longitude, speed = position(jd, body)
        positions[body] = {
            "longitude": round(longitude, 6),
            "position": format_position(longitude),
            "retrograde": speed < 0,
            "whole_sign_house": whole_sign_house(longitude, ascendant),
        }

    true_node = positions["True Node"]["longitude"]
    south_node = (true_node + 180) % 360
    positions["SNode"] = {
        "longitude": round(south_node, 6),
        "position": format_position(south_node),
        "retrograde": positions["True Node"]["retrograde"],
        "whole_sign_house": whole_sign_house(south_node, ascendant),
    }

    chiron_values, _ = swe.calc_ut(jd, swe.CHIRON, swe.FLG_SWIEPH | swe.FLG_SPEED)
    chiron = chiron_values[0] % 360
    positions["Chiron"] = {
        "longitude": round(chiron, 6),
        "position": format_position(chiron),
        "retrograde": chiron_values[3] < 0,
        "whole_sign_house": whole_sign_house(chiron, ascendant),
    }

    try:
        america = minor_points.america_lon(jd) % 360
        america_speed = minor_points.america_speed(jd)
    except ValueError:
        america = None
        america_speed = 0.0
    if america is not None:
        positions["America"] = {
            "longitude": round(america, 6),
            "position": format_position(america),
            "retrograde": america_speed < 0,
            "whole_sign_house": whole_sign_house(america, ascendant),
        }
        america_status = "available from the canonical daily JPL Horizons cache"
    else:
        america_status = (
            "unavailable outside the canonical 2024-01-01 to 2031-01-01 "
            "America cache; no extrapolation"
        )
    return positions, america_status


def chart_aspects(jd: float, positions: dict) -> tuple[list, list]:
    aspects = []
    bodies = list(PLANETS)
    for index, first in enumerate(bodies):
        for second in bodies[index + 1:]:
            max_orb = 8.0 if first in {"Sun", "Moon"} or second in {"Sun", "Moon"} else 6.0
            hit = aspect_hit(positions[first]["longitude"], positions[second]["longitude"], max_orb)
            if hit:
                name, angle, orb = hit
                aspects.append({
                    "pair": f"{first}–{second}",
                    "aspect": name,
                    "orb": round(orb, 3),
                    "state": mutual_applying_state(jd, first, second, angle),
                })

    point_hits = []
    for point in ("True Node", "Chiron", "America"):
        if point not in positions:
            continue
        for planet in [name for name in PLANETS if name != "True Node"]:
            hit = aspect_hit(
                positions[point]["longitude"],
                positions[planet]["longitude"],
                2.0,
            )
            if hit:
                name, _angle, orb = hit
                point_hits.append({
                    "point": "Node" if point == "True Node" else point,
                    "aspect": name,
                    "planet": planet,
                    "orb": round(orb, 3),
                })
    return (
        sorted(aspects, key=lambda item: item["orb"]),
        sorted(point_hits, key=lambda item: item["orb"]),
    )


def cast_context(
    event: dict,
    jd: float,
    instant_utc: datetime,
    lat: float,
    lon: float,
    place: str,
    timezone_name: str,
    dc_companion: bool = False,
) -> tuple[dict, list, str]:
    local_frame = instant_utc.astimezone(ZoneInfo(timezone_name))
    _, ascmc = swe.houses(jd, lat, lon, b"W")
    positions, america_status = cast_positions(jd, ascmc[0])
    aspects, point_hits = chart_aspects(jd, positions)

    angle_contacts = []
    for body in PLANETS:
        record = positions[body]
        for angle_name, angle_longitude in (("Ascendant", ascmc[0]), ("MC", ascmc[1])):
            separation = angular_distance(record["longitude"], angle_longitude)
            for aspect_name, aspect_angle in (
                ("conjunction", 0.0), ("opposition", 180.0), ("square", 90.0)
            ):
                orb = abs(separation - aspect_angle)
                if orb <= 3.0:
                    angle_contacts.append({
                        "planet": body,
                        "aspect": aspect_name,
                        "angle": angle_name,
                        "orb": round(orb, 3),
                    })
                    break

    assumed = event["clock_mode"] != "reported"
    if event["clock_mode"] == "reported":
        quality = "reported context chart"
        base_cap = "reported reveal frame · ±2 minutes"
        base_caption = (
            "Reported reveal-frame chart; angles and houses carry the stated "
            "±2-minute source boundary."
        )
    elif event["clock_mode"] == "noon_proxy":
        quality = "assumed noon chart"
        base_cap = "synthetic noon chart · daytime convention"
        base_caption = (
            "Synthetic chart because the source establishes a daytime event but "
            "not its precise minute. Angles and houses are convention-derived."
        )
    else:
        quality = "assumed midnight chart"
        base_cap = "synthetic midnight chart · unknown-time convention"
        base_caption = (
            "Synthetic chart because no event time is established. Angles and "
            "houses are convention-derived."
        )

    if dc_companion:
        cap1 = f"{event['label']} · Washington, D.C. companion"
        cap2 = f"Whole Sign · same instant · {base_cap}"
        caption = (
            "Washington, D.C. relocation companion at the same instant. "
            + (
                "Its national mundane angles and houses carry the stated ±2-minute boundary."
                if not assumed
                else "Its angles and houses remain convention-derived and are not observed event geometry."
            )
        )
    else:
        cap1 = f"{event['label']} · {place}"
        cap2 = f"Whole Sign · {base_cap}"
        caption = base_caption

    context = {
        "utc": instant_utc.isoformat().replace("+00:00", "Z"),
        "local": f"{local_frame.strftime('%Y-%m-%d %H:%M')} {local_frame.tzname()}",
        "display": (
            f"{local_frame.strftime('%-d %b %Y · %-I:%M %p')} "
            f"{local_frame.tzname()}"
        ),
        "place": place,
        "ascendant": {"longitude": round(ascmc[0], 6), "position": format_position(ascmc[0])},
        "mc": {"longitude": round(ascmc[1], 6), "position": format_position(ascmc[1])},
        "positions": positions,
        "aspects": aspects,
        "point_aspects": point_hits,
        "angle_contacts": sorted(angle_contacts, key=lambda item: item["orb"]),
        "chart_ruler": TRADITIONAL_RULERS[sign(ascmc[0])],
        "chart_ruler_path": dispositor_path(TRADITIONAL_RULERS[sign(ascmc[0])], positions),
        "cap1": cap1,
        "cap2": cap2,
        "caption": caption,
        "clock_mode": event["clock_mode"],
        "time_assumed": assumed,
        "america_status": america_status,
        "boundary": event["boundary"],
    }
    return context, point_hits, quality


def build_event(event: dict) -> dict:
    hour, minute = (int(value) for value in event["local_time"].split(":"))
    local_dt = datetime.fromisoformat(event["date"]).replace(
        hour=hour,
        minute=minute,
        tzinfo=ZoneInfo(event["timezone"]),
    )
    utc_dt = local_dt.astimezone(timezone.utc)
    jd = julday(local_dt)

    context, point_hits, quality = cast_context(
        event,
        jd,
        utc_dt,
        event["lat"],
        event["lon"],
        event["place"],
        event["timezone"],
    )
    dc_context, _dc_point_hits, _dc_quality = cast_context(
        event,
        jd,
        utc_dt,
        DC_LAT,
        DC_LON,
        "Washington, D.C.",
        "America/New_York",
        dc_companion=True,
    )
    positions = context["positions"]

    outer_cycles = []
    for index, first in enumerate(OUTERS):
        for second in OUTERS[index + 1:]:
            hit = aspect_hit(positions[first]["longitude"], positions[second]["longitude"], 8.0)
            if hit:
                name, angle, orb = hit
                outer_cycles.append({
                    "pair": f"{first}–{second}",
                    "aspect": name,
                    "orb": round(orb, 3),
                    "state": mutual_applying_state(jd, first, second, angle),
                })

    us_hits = []
    for moving in OUTERS:
        for natal, natal_longitude in US_MONEY.items():
            hit = aspect_hit(positions[moving]["longitude"], natal_longitude, 3.0)
            if hit:
                name, angle, orb = hit
                us_hits.append({
                    "transit": moving,
                    "aspect": name,
                    "natal": natal,
                    "orb": round(orb, 3),
                    "state": applying_state(jd, moving, natal_longitude, angle),
                })

    midpoint_hits = []
    for moving in OUTERS:
        for midpoint_name, midpoint_longitude in US_MIDPOINTS.items():
            separation = angular_distance(positions[moving]["longitude"], midpoint_longitude)
            nearest = min([0, 45, 90, 135, 180], key=lambda angle: abs(separation - angle))
            orb = abs(separation - nearest)
            if orb <= 1.5:
                midpoint_hits.append({
                    "transit": moving,
                    "midpoint": midpoint_name,
                    "harmonic_angle": nearest,
                    "orb": round(orb, 3),
                })

    assumed = event["clock_mode"] != "reported"
    return {
        **event,
        "proxy_utc": utc_dt.isoformat().replace("+00:00", "Z"),
        "chart_quality": quality,
        "positions": positions,
        "outer_cycles": sorted(outer_cycles, key=lambda item: item["orb"]),
        "us_money_axis_hits": sorted(us_hits, key=lambda item: item["orb"]),
        "us_money_midpoint_hits": sorted(midpoint_hits, key=lambda item: item["orb"]),
        "minor_point_aspects": point_hits,
        "america_status": context["america_status"],
        "angles_assumed": assumed,
        "houses_assumed": assumed,
        "contextual_container_clock": context,
        "dc_companion_clock": dc_context,
    }


def main() -> None:
    records = [build_event(event) for event in EVENTS]
    payload = {
        "title": "Card-Network Stablecoin Product Lines — Astrology Data",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "cutoff": "2026-07-29",
        "method": {
            "ephemeris": "Swiss Ephemeris; geocentric tropical",
            "houses": "Whole Sign",
            "minor_points": (
                "True Node/South Node and Chiron on every chart; 916 America "
                "from the canonical vault JPL Horizons cache where available"
            ),
            "america_cache_boundary": (
                "2024-01-01 through 2031-01-01; 2014 and 2023 anchors are "
                "marked unavailable and are not extrapolated"
            ),
            "dc_companion": (
                "Every stated-place event carries a Washington, D.C. relocation "
                "companion at the same instant; national mundane angle reading "
                "belongs to the D.C. frame"
            ),
            "clock_policy": {
                "reported": "Use source-supported event time with its stated uncertainty.",
                "noon_proxy": "Known daytime event without precise time: 12:00 local synthetic chart.",
                "midnight_proxy": "Unknown event time: 00:00 local synthetic chart.",
            },
            "us_chart": "1776-07-02 17:10 LMT Philadelphia; locked Sagittarius-rising Freedom 250 chart",
            "outer_mutual_orb": 8.0,
            "outer_to_us_money_axis_orb": 3.0,
            "mod45_money_midpoint_orb": 1.5,
            "score": None,
            "causal_claim": False,
        },
        "clock_counts": {
            mode: sum(event["clock_mode"] == mode for event in records)
            for mode in ["reported", "noon_proxy", "midnight_proxy"]
        },
        "america_counts": {
            "available": sum("America" in event["positions"] for event in records),
            "unavailable": sum("America" not in event["positions"] for event in records),
        },
        "dc_companion_count": sum(bool(event.get("dc_companion_clock")) for event in records),
        "events": records,
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(
        f"wrote {OUT} · {len(records)} charts · "
        f"{payload['clock_counts']}"
    )


if __name__ == "__main__":
    main()
