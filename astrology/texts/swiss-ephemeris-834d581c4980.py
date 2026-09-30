"""One ephemeris for the Freedom 250 astrology engine.

Every engine module that computes planetary positions imports FLAGS from here.
Importing this module points pyswisseph at the vendored Swiss Ephemeris data
files in ``99 - Templates/ephe`` (sepl_18 / semo_18 from the JPL DE441 release,
plus seas_18 for asteroids; coverage 1800-2400 AD). The earlier DE406-based
files are kept in ``ephe/de406`` only for reproducing pre-correction numbers:
DE406 is ~0.5" off for Pluto and ~0.25" for Neptune in the 2020s.

Why this exists (2026-09-25 ephemeris correction): several builders forced the
analytical Moshier ephemeris. That is harmless for ordinary lunation and
ingress charts, but slow outer-planet conjunctions close at ~0.01°/day, so a
one-arcsecond position error moves the exact moment by ~45 minutes and the
conjunction chart's Ascendant by several degrees. Requesting FLG_SWIEPH
without setting the path is not enough either: pyswisseph then falls back to
Moshier silently. ``require_swiss`` refuses that silent fallback.
"""

from __future__ import annotations

from pathlib import Path

import swisseph as swe

EPHE_DIR = Path(__file__).resolve().parent / "ephe"
FLAGS = swe.FLG_SWIEPH | swe.FLG_SPEED
EPHEMERIS_LABEL = "Swiss Ephemeris files (JPL DE441-based sepl_18/semo_18), 99 - Templates/ephe"
PRIOR_RELEASE_DIR = EPHE_DIR / "de406"  # pre-2026-09-25 vendored files, kept only for reproducing old numbers
COVERAGE_JD = (swe.julday(1800, 1, 1), swe.julday(2399, 12, 31))

swe.set_ephe_path(str(EPHE_DIR))


def require_swiss(jd_ut: float = 2451545.0) -> int:
    """Assert that the Swiss files (not Moshier) answer a calculation at jd_ut."""
    swe.set_ephe_path(str(EPHE_DIR))
    returned = swe.calc_ut(jd_ut, swe.PLUTO, FLAGS)[1]
    if not returned & swe.FLG_SWIEPH:
        raise RuntimeError(
            f"Swiss Ephemeris files were not used (returned flags {returned}); "
            f"expected data files in {EPHE_DIR}. Refusing a silent Moshier fallback."
        )
    return FLAGS


require_swiss()
