#!/usr/bin/env python3
"""Canonical, fail-closed reader for 916 America's daily Horizons cache.

This is the promotion candidate for ``99 - Templates/america.py``.  The cache
contains one longitude at 00:00 UTC per civil date.  Interpolation always takes
the shortest signed arc, so ordinary retrograde motion is never mistaken for a
360-degree wrap.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
CACHE = Path(os.environ.get("F250_AMERICA_CACHE", HERE / "america_ephemeris.json"))
BODY = "916 America"
MAX_DAILY_MOTION_DEG = 1.0
SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces",
]

_rows: dict[str, float] | None = None


def signed_delta(newer: float, older: float) -> float:
    """Shortest signed angular displacement from ``older`` to ``newer``."""
    return ((float(newer) - float(older) + 180.0) % 360.0) - 180.0


def _load() -> dict[str, float]:
    global _rows
    if _rows is None:
        try:
            raw: dict[str, Any] = json.loads(CACHE.read_text(encoding="utf-8"))
            body = raw.get(BODY)
            if not isinstance(body, dict) or not body:
                raise ValueError(f"{CACHE} has no non-empty {BODY!r} mapping")
            _rows = {str(key): float(value) % 360.0 for key, value in body.items()}
        except Exception:
            # Preserve the established public contract: callers receive None
            # when the canonical cache cannot answer, never a guessed degree.
            _rows = {}
    return _rows


def reset_cache_for_tests() -> None:
    global _rows
    _rows = None


def _bracket(dt_utc: datetime) -> tuple[float, float, float] | None:
    rows = _load()
    d0 = dt_utc.date().isoformat()
    d1 = (dt_utc.date() + timedelta(days=1)).isoformat()
    a = rows.get(d0)
    b = rows.get(d1)
    if a is None:
        return None
    if b is None:
        return a, 0.0, 0.0
    motion = signed_delta(b, a)
    if abs(motion) > MAX_DAILY_MOTION_DEG:
        return None
    # Intentionally retain the pre-repair precision contract: whole seconds,
    # excluding microseconds, so unaffected direct-motion baseline bytes stay
    # stable.  The only numerical change is shortest-arc handling.
    seconds = dt_utc.hour * 3600 + dt_utc.minute * 60 + dt_utc.second
    return a, motion, seconds / 86400.0


def america_lon(dt_value: datetime) -> float | None:
    """Return canonical longitude, or None when the cache cannot answer."""
    if dt_value.tzinfo is None:
        dt_value = dt_value.replace(tzinfo=timezone.utc)
    moment = dt_value.astimezone(timezone.utc)
    bracket = _bracket(moment)
    if bracket is None:
        return None
    start, motion, fraction = bracket
    return (start + motion * fraction) % 360.0


def america_speed(dt_value: datetime) -> float | None:
    """Return the canonical bracketing-row motion in degrees per day."""
    if dt_value.tzinfo is None:
        dt_value = dt_value.replace(tzinfo=timezone.utc)
    bracket = _bracket(dt_value.astimezone(timezone.utc))
    if bracket is None:
        return None
    _start, motion, _fraction = bracket
    return motion


def america_pos(dt_value: datetime) -> str | None:
    longitude = america_lon(dt_value)
    if longitude is None:
        return None
    sign_index = int(longitude // 30.0) % 12
    degree = longitude % 30.0
    whole = int(degree)
    minute = int(round((degree - whole) * 60))
    if minute == 60:
        whole += 1
        minute = 0
        if whole == 30:
            whole = 0
            sign_index = (sign_index + 1) % 12
    return f"{whole}°{minute:02d}' {SIGNS[sign_index]}"


def available() -> tuple[bool, str]:
    try:
        rows = _load()
        keys = sorted(rows)
        for first, second in zip(keys, keys[1:]):
            motion = signed_delta(rows[second], rows[first])
            if abs(motion) > MAX_DAILY_MOTION_DEG:
                return False, (
                    f"916 America cache fails motion validation: {first} -> {second} "
                    f"is {motion:.6f} deg/day"
                )
        return True, f"916 America canonical cache: {len(rows):,} daily rows, {keys[0]} -> {keys[-1]}"
    except Exception as exc:
        return False, str(exc)


if __name__ == "__main__":
    ok, message = available()
    print(("OK " if ok else "FAIL ") + message)
