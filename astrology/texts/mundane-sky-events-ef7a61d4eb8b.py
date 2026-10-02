#!/usr/bin/env python3
"""Sky events for the Mundane Astrology section (Katie, 2026-10-03).

Computes, with the vendored Swiss Ephemeris (swiss_ephemeris.py), every sky event the
crossover matcher lines up against research dates:

  lunation        New and Full Moons (with the eclipse flag when one falls on it)
  eclipse         solar and lunar eclipses
  ingress         Sun into Aries/Cancer/Libra/Capricorn (the season charts) and
                  Jupiter-Pluto changing sign (including retrograde re-entries)
  station         Mercury-Pluto turning retrograde or direct
  aspect          exact conjunction, sextile, square, trine, opposition between
                  Mars, Jupiter, Saturn, Uranus, Neptune and Pluto
  conjunction     exact conjunctions of any two of Sun-Pluto (the conjunction charts),
                  linked to the long-cycle radix when the pair has one
  transit         Jupiter-Pluto exact conjunction/square/opposition to the key charts
                  (the U.S. chart and the entity charts in Entity Theory)

Read-only. Returns plain dicts; build_mundane_astrology.py caches them.
"""
from __future__ import annotations

import json
import math
import os
from datetime import datetime, timedelta, timezone

import swiss_ephemeris  # sets the ephemeris path and refuses a silent Moshier fallback
import swisseph as swe

FLAGS = swiss_ephemeris.FLAGS
HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(HERE)
SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
P = {"Sun": swe.SUN, "Moon": swe.MOON, "Mercury": swe.MERCURY, "Venus": swe.VENUS, "Mars": swe.MARS, "Jupiter": swe.JUPITER,
     "Saturn": swe.SATURN, "Uranus": swe.URANUS, "Neptune": swe.NEPTUNE, "Pluto": swe.PLUTO}
SLOW = ["Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
ASPECTS = {0: "conjunct", 60: "sextile", 90: "square", 120: "trine", 180: "opposite"}
KEY_CHARTS = {  # Entity Theory chart name -> how the research side names it (for resonance)
    "United States": r"\b(U\.S\.|United States|America|American)\b",
    "Congress": r"\b(Congress|Senate|Speaker)\b|(?<!White )\bHouse\b",
    "Supreme Court": r"\b(Supreme Court|SCOTUS)\b",
    "Executive Office of the President": r"\b(White House|President Trump|the President)\b",
    "Dept of the Treasury": r"\b(Treasury|Bessent|IRS)\b",
    "The Federal Reserve System": r"\b(Fed|Federal Reserve|FOMC|Powell|Warsh)\b",
    "SEC": r"\b(SEC|Securities and Exchange)\b",
    "CFTC": r"\b(CFTC|Commodity Futures)\b",
    "OCC": r"\b(OCC|Comptroller)\b",
    "FDIC": r"\bFDIC\b",
    "Dept of Justice": r"\b(Justice Department|Department of Justice|DOJ|Attorney General)\b",
    "FBI": r"\bFBI\b",
    "Dept of Homeland Security": r"\b(Homeland Security|DHS|ICE)\b",
    "Dept of Defense": r"\b(Pentagon|Defense|Department of War|Hegseth)\b",
}
POINTS = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]


def jd_of(d: datetime) -> float:
    return swe.julday(d.year, d.month, d.day, d.hour + d.minute / 60 + d.second / 3600)


def dt_of(jd: float) -> datetime:
    y, m, d, h = swe.revjul(jd)
    return datetime(y, m, d, tzinfo=timezone.utc) + timedelta(hours=h)


def lon(jd, body):
    return swe.calc_ut(jd, P[body], FLAGS)[0][0]


def spd(jd, body):
    return swe.calc_ut(jd, P[body], FLAGS)[0][3]


def wrap(x):
    return (x + 180.0) % 360.0 - 180.0


def roots(f, start, end, step, near=12.0):
    """Times where f crosses zero going either way, ignoring wrap-around jumps."""
    out, t, a = [], start, f(start)
    while t < end:
        t2 = min(t + step, end)
        b = f(t2)
        if a == 0 or (a < 0 <= b or b < 0 <= a) and abs(a) < near and abs(b) < near:
            lo, hi, fa = t, t2, a
            for _ in range(40):
                mid = (lo + hi) / 2
                fm = f(mid)
                if (fa < 0) == (fm < 0):
                    lo, fa = mid, fm
                else:
                    hi = mid
            out.append((lo + hi) / 2)
        t, a = t2, b
    return out


def ev(kind, jd, label, weight, **extra):
    d = dt_of(jd)
    return {"kind": kind, "date": d.date().isoformat(), "utc": d.strftime("%Y-%m-%dT%H:%MZ"), "label": label, "weight": weight, **extra}


def sign_of(x):
    return SIGNS[int(x // 30) % 12]


def deg(x):
    return f"{int(x % 30)}°{int(round((x % 1) * 60)):02d}' {sign_of(x)}"


def compute(start: str, end: str) -> list[dict]:
    a = jd_of(datetime.fromisoformat(start))
    b = jd_of(datetime.fromisoformat(end))
    events = []
    # eclipses
    eclipse_dates = {}
    t = a
    while True:
        r, tret = swe.sol_eclipse_when_glob(t, FLAGS, 0)
        if tret[0] > b:
            break
        kind = "total" if r & swe.ECL_TOTAL else "annular" if r & swe.ECL_ANNULAR else "hybrid" if r & getattr(swe, "ECL_ANNULAR_TOTAL", 32) else "partial"
        s = lon(tret[0], "Sun")
        e = ev("eclipse", tret[0], f"{kind.title()} solar eclipse in {sign_of(s)}", 5, sign=sign_of(s), position=deg(s))
        events.append(e); eclipse_dates[e["date"]] = e["label"]
        t = tret[0] + 20
    t = a
    while True:
        r, tret = swe.lun_eclipse_when(t, FLAGS, 0)
        if tret[0] > b:
            break
        kind = "total" if r & swe.ECL_TOTAL else "partial" if r & swe.ECL_PARTIAL else "penumbral"
        m = lon(tret[0], "Moon")
        e = ev("eclipse", tret[0], f"{kind.title()} lunar eclipse in {sign_of(m)}", 5 if kind != "penumbral" else 4, sign=sign_of(m), position=deg(m))
        events.append(e); eclipse_dates[e["date"]] = e["label"]
        t = tret[0] + 20
    # lunations
    elong = lambda jd: wrap(lon(jd, "Moon") - lon(jd, "Sun"))
    for jd in roots(elong, a, b, 0.5, near=40):
        m = lon(jd, "Moon")
        e = ev("lunation", jd, f"{sign_of(m)} New Moon", 3, phase="new", sign=sign_of(m), position=deg(m))
        if e["date"] in eclipse_dates: e["eclipse"] = eclipse_dates[e["date"]]; e["weight"] = 5
        events.append(e)
    for jd in roots(lambda j: wrap(elong(j) - 180), a, b, 0.5, near=40):
        m = lon(jd, "Moon")
        e = ev("lunation", jd, f"{sign_of(m)} Full Moon", 3, phase="full", sign=sign_of(m), position=deg(m))
        if e["date"] in eclipse_dates: e["eclipse"] = eclipse_dates[e["date"]]; e["weight"] = 5
        events.append(e)
    # ingresses
    for body in ["Sun"] + SLOW:
        for k in range(12):
            if body == "Sun" and k not in (0, 3, 6, 9):
                continue
            for jd in roots(lambda j, k=k: wrap(lon(j, body) - 30 * k), a, b, 1.0, near=8):
                into = SIGNS[k]; retro = spd(jd, body) < 0
                if body == "Sun":
                    events.append(ev("ingress", jd, f"Sun enters {into} (the {into} ingress, a season chart)", 4, body=body, sign=into, season=True))
                else:
                    events.append(ev("ingress", jd, f"{body} {'retrogrades back into' if retro else 'enters'} {into}", 4, body=body, sign=into))
    # stations
    for body in ["Mercury", "Venus", "Mars"] + SLOW:
        for jd in roots(lambda j: spd(j, body), a, b, 1.0, near=99):
            turning = "retrograde" if spd(jd + 1, body) < 0 else "direct"
            w = 3 if body in ["Mars"] + SLOW else 2
            events.append(ev("station", jd, f"{body} stations {turning} at {deg(lon(jd, body))}", w, body=body, turning=turning))
    # exact aspects among Mars and the slow planets
    heavy = ["Mars"] + SLOW
    for i, p1 in enumerate(heavy):
        for p2 in heavy[i + 1:]:
            for angle, name in ASPECTS.items():
                targets = [angle] if angle in (0, 180) else [angle, -angle]
                for tg in targets:
                    for jd in roots(lambda j: wrap(lon(j, p1) - lon(j, p2) - tg), a, b, 1.0, near=6):
                        w = 4 if p1 != "Mars" else 3
                        kind = "conjunction" if angle == 0 else "aspect"
                        events.append(ev(kind, jd, f"{p1} {name} {p2}", w, pair=[p1, p2], aspect=name, position=deg(lon(jd, p1))))
    # conjunction charts: every exact conjunction of Sun-Pluto bodies not already covered
    fast = ["Sun", "Mercury", "Venus"]
    for i, p1 in enumerate(fast):
        for p2 in [x for x in POINTS if x not in ("Moon",) and POINTS.index(x) > POINTS.index(p1)]:
            for jd in roots(lambda j: wrap(lon(j, p1) - lon(j, p2)), a, b, 0.5, near=8):
                w = 2 if p2 in SLOW else 1
                events.append(ev("conjunction", jd, f"{p1} conjunct {p2}", w, pair=[p1, p2], aspect="conjunct", position=deg(lon(jd, p1))))
    # transits to the key charts
    charts = json.load(open(os.path.join(VAULT, "04 - Synthesis", "Entity Theory", "entity_charts.json"), encoding="utf-8"))["charts"]
    for name in KEY_CHARTS:
        c = charts.get(name) or {}
        pos = {row[0]: row[4] for row in (c.get("rec") or {}).get("pos", []) if isinstance(row, list) and len(row) > 4 and row[0] in POINTS}
        if (c.get("rec") or {}).get("asc") is not None:
            pos["Ascendant"] = c["rec"]["asc"]
        for natal_body, natal in pos.items():
            for tbody in SLOW:
                for angle, aname in ((0, "conjunct"), (90, "square"), (180, "opposite")):
                    for tg in ([angle] if angle in (0, 180) else [angle, -angle]):
                        for jd in roots(lambda j: wrap(lon(j, tbody) - natal - tg), a, b, 1.0, near=6):
                            w = 4 if name == "United States" and tbody != "Jupiter" else 3 if tbody != "Jupiter" else 2
                            events.append(ev("transit", jd, f"{tbody} {aname} the {name.removeprefix('The ')} chart's {natal_body}", w,
                                             chart=name, natal=natal_body, body=tbody, aspect=aname, resonance=KEY_CHARTS[name]))
    events.sort(key=lambda e: e["utc"])
    return events
