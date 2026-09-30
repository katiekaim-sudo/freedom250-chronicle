#!/usr/bin/env python3
"""Shared access to the chart's minor points (added 2026-06-10):

  - Chiron     — swisseph + the vendored ephemeris files in `99 - Templates/ephe/`
                 (seas_18.se1 et al., shipped so this works on any machine)
  - True Node  — swisseph (analytic, no files needed)
  - 916 America— daily JPL Horizons longitudes from the canonical
                 `america_ephemeris.json` cache, via `america.py`; exact natal
                 epochs remain in `minor_points.json`

Importing this module sets the swisseph ephemeris path, which also upgrades
Sun..Pluto from Moshier to the Swiss files (sub-arcsecond; visually identical).

Usage:
    from minor_points import all_points, america_natal, GLY_ORDER
    pts = all_points(jd)   # {"Chiron": (lon, speed), "Node": ..., "America": ...}
"""
import json, os
from datetime import datetime, timedelta, timezone
import swisseph as swe
from america import america_lon as _cached_america_lon, available as _america_available

HERE = os.path.dirname(os.path.abspath(__file__))
swe.set_ephe_path(os.path.join(HERE, "ephe"))

_MP = json.load(open(os.path.join(HERE, "minor_points.json")))
_AM = _MP["America"]

GLY_ORDER = ["Chiron", "Node", "America"]   # canonical extra-point order

def america_lon(jd):
    """Apparent geocentric longitude from the one daily Horizons cache."""
    y, m, d, hour = swe.revjul(jd, swe.GREG_CAL)
    dt = datetime(y, m, d, tzinfo=timezone.utc) + timedelta(hours=hour)
    lon = _cached_america_lon(dt)
    if lon is None:
        _, message = _america_available()
        raise ValueError(f"jd {jd} outside the cached America span: {message}")
    return lon

def america_speed(jd):
    h = 2.0
    center = america_lon(jd)
    try:
        before = america_lon(jd - h)
    except ValueError:
        before = None
    try:
        after = america_lon(jd + h)
    except ValueError:
        after = None

    def delta(newer, older):
        return (newer - older + 180) % 360 - 180

    if before is not None and after is not None:
        return delta(after, before) / (2 * h)
    if after is not None:
        return delta(after, center) / h
    if before is not None:
        return delta(center, before) / h
    raise ValueError(f"America cache has no neighboring rows around jd {jd}")

def america_natal(slug):
    """Exact-epoch natal longitude for a cast slug (from Horizons TLIST)."""
    return _AM["natal"][slug]

def chiron(jd):
    r = swe.calc_ut(jd, swe.CHIRON)[0]
    return r[0], r[3]

def true_node(jd):
    r = swe.calc_ut(jd, swe.TRUE_NODE)[0]
    return r[0], r[3]

def all_points(jd, with_america=True):
    """{"Chiron": (lon, speed), "Node": (lon, speed), "America": (lon, speed)}.
    Set with_america=False outside the cached grid (e.g. deep past)."""
    c, n = chiron(jd), true_node(jd)
    out = {"Chiron": c, "Node": n}
    if with_america:
        out["America"] = (america_lon(jd), america_speed(jd))
    return out
