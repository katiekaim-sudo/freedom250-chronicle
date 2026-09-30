#!/usr/bin/env python3
"""Shared location and clock rules for Freedom 250 mundane charts.

National mundane charts are always cast for Washington, D.C.  Exact stated
event times preserve the real instant, then the wheel is relocated to D.C.;
untimed daytime/date-only records use noon/midnight in Washington itself.

Natal and founding charts are a separate class and keep their actual birthplace.
See DECISION LOG DR-047 and Reading the Charts — START HERE §9.
"""

from __future__ import annotations

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import swisseph as swe


DC_LAT = 38.9072
DC_LON = -77.0369
DC = (DC_LAT, DC_LON)
DC_TZ_NAME = "America/New_York"
DC_TZ = ZoneInfo(DC_TZ_NAME)
UTC = timezone.utc
DC_LABEL = "Washington, D.C."


def julian_day(moment: datetime) -> float:
    """Return a UT Julian day for an aware datetime."""
    if moment.tzinfo is None:
        raise ValueError("julian_day requires a timezone-aware datetime")
    ut = moment.astimezone(UTC)
    hour = ut.hour + ut.minute / 60 + ut.second / 3600 + ut.microsecond / 3_600_000_000
    return swe.julday(ut.year, ut.month, ut.day, hour)


def clock_label(moment: datetime, *, seconds: bool = False) -> str:
    """Human clock label with the zone abbreviation of ``moment``."""
    fmt = "%I:%M:%S %p" if seconds else "%I:%M %p"
    clock = moment.strftime(fmt).lstrip("0")
    return f"{clock} {moment.tzname() or 'ET'}"


def washington_label(moment: datetime, *, seconds: bool = False) -> str:
    """Render any instant as a user-facing Washington local-time caption."""
    return f"{clock_label(moment.astimezone(DC_TZ), seconds=seconds)} · {DC_LABEL}"


def mundane_event_instant(
    date_iso: str,
    *,
    stated_time: str | None = None,
    source_tz: str | None = None,
    date_only: bool = False,
) -> tuple[float, datetime, str]:
    """Resolve an event under DR-047 and return ``(jd_ut, dc_local, basis)``.

    A stated clock is interpreted in the source timezone because it identifies a
    real-world instant.  Without a stated clock, the convention is deliberately
    Washington-local: noon for a known daytime event, midnight for date-only.
    """
    y, month, day = (int(x) for x in date_iso.split("-"))
    if stated_time:
        parts = [int(x) for x in stated_time.split(":")]
        hour, minute = parts[:2]
        second = parts[2] if len(parts) > 2 else 0
        source = ZoneInfo(source_tz or DC_TZ_NAME)
        local = datetime(y, month, day, hour, minute, second, tzinfo=source)
        basis = "exact stated event instant"
    else:
        hour = 0 if date_only else 12
        local = datetime(y, month, day, hour, 0, tzinfo=DC_TZ)
        basis = "midnight D.C. date-only convention" if date_only else "noon D.C. daytime convention"
    dc_local = local.astimezone(DC_TZ)
    return julian_day(local), dc_local, basis
