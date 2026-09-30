#!/usr/bin/env python3
"""build_america_ephemeris.py — cache 916 AMERICA so every chart can carry her.

WHY THIS EXISTS
---------------
Katie's ruling, 2026-07-12: **"that asteroid should be in every chart."**

916 America is not a planet, so pyswisseph will not compute her without an asteroid
ephemeris file (`se00916s.se1`), which we do not ship. Every builder that wanted her had to
either skip her or fetch JPL Horizons live — so `build_astro_map.py` fetched her ONLY at the
eight ingress epochs, and everything else in the vault simply had no America at all.

That gap cost a real finding. On 2026-07-12 the watch calendar said "Venus on the America
point" on Jul 18, a Claude could not compute the asteroid, and so it wrote the claim off as
UNVERIFIED. It was true. Venus is exact on America at **04:17 UTC on 2026-07-18** — twenty-three
minutes before the Uranus-Pluto trine perfects. A body the vault could not see was sitting on
the most important date in the queue.

WHAT IT DOES
------------
Fetches 916 America's apparent geocentric **ecliptic-of-date longitude** (Horizons QUANTITIES=31
— the same quantity `build_astro_map.py` uses, so the two agree by construction), daily, across
the chronicle's whole live span, and writes:

    99 - Templates/america_ephemeris.json    {"916 America": {"YYYY-MM-DD": lon_deg, ...}, ...}

Then `america.py` reads that cache and hands any builder a longitude for any moment, with
interpolation. No network at read time; no builder ever needs Horizons again.

WHERE IT RUNS
-------------
**The Mac.** It needs the network. It is NOT in the nightly chain — America's orbit does not
change, so the cache is regenerated only when the span needs extending (roughly yearly), or
when Horizons publishes a new orbit solution.

    python3 "99 - Templates/build_america_ephemeris.py"                 # default span
    python3 "99 - Templates/build_america_ephemeris.py" 2024 2032       # explicit span

ACCURACY
--------
Horizons apparent ecliptic-of-date, geocentric, light-time + deflection + aberration — i.e. the
position an astrologer means. Daily rows; America moves ~0.34°/day, so linear interpolation
between them is good to well under an arcminute. **Verify against Astro Gold before anything
load-bearing** (the house rule: never write a degree from memory — compute it, then check it).
"""
import json, os, sys, urllib.parse, urllib.request
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(HERE, "america_ephemeris.json")
API  = "https://ssd.jpl.nasa.gov/api/horizons.api"

# The body. Keyed by name so a future Katie can add more minor points (Chiron is already in
# swisseph; 916 America is the one that needs Horizons) without touching the reader.
BODIES = {"916 America": "916"}


def fetch(cmd: str, start: str, stop: str) -> dict:
    """One Horizons pull: daily apparent ecliptic-of-date longitude, geocentric."""
    q = {
        "format":     "text",
        "COMMAND":    cmd,
        "OBJ_DATA":   "NO",
        "MAKE_EPHEM": "YES",
        "EPHEM_TYPE": "OBSERVER",
        "CENTER":     "500@399",     # geocentric
        "START_TIME": start,
        "STOP_TIME":  stop,
        # Horizons API 1.2 rejects the formerly accepted spaced form "1 d"
        # as two constants. The compact form is the current execution-control
        # syntax and still means one calendar day.
        "STEP_SIZE":  "1d",
        "QUANTITIES": "31",          # ObsEcLon / ObsEcLat — ecliptic of date, apparent
    }
    url = API + "?" + urllib.parse.urlencode(q)
    with urllib.request.urlopen(url, timeout=120) as r:
        txt = r.read().decode("utf-8", "ignore")

    if "$$SOE" not in txt:
        raise RuntimeError(f"Horizons returned no ephemeris block for {cmd} "
                           f"({start}→{stop}). First 300 chars:\n{txt[:300]}")

    MONTH = {m: i for i, m in enumerate(
        ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"], 1)}
    rows = {}
    body = txt.split("$$SOE", 1)[1].split("$$EOE", 1)[0]
    for line in body.strip().splitlines():
        p = line.split()
        if len(p) < 4:
            continue
        y, mon, d = p[0].split("-")             # 2026-Jul-18
        rows[f"{int(y):04d}-{MONTH[mon]:02d}-{int(d):02d}"] = float(p[2])
    if not rows:
        raise RuntimeError(f"Horizons block parsed to zero rows for {cmd}")
    return rows


def main():
    y0 = int(sys.argv[1]) if len(sys.argv) > 1 else 2024
    y1 = int(sys.argv[2]) if len(sys.argv) > 2 else date.today().year + 4

    out = {}
    for name, cmd in BODIES.items():
        rows = {}
        for y in range(y0, y1 + 1):            # a year at a time — Horizons caps a single pull
            rows.update(fetch(cmd, f"{y}-01-01", f"{y+1}-01-01"))
            print(f"  {name}: {y} … {len(rows):,} days cached")
        out[name] = dict(sorted(rows.items()))

    meta = {
        "_source": "JPL Horizons — apparent geocentric ecliptic-of-date longitude (QUANTITIES=31)",
        "_units": "degrees, 0-360 from the vernal point",
        "_generated": date.today().isoformat(),
        "_why": "Katie 2026-07-12: 916 America belongs in every chart. Read it via america.py.",
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump({**meta, **out}, f, indent=1)

    for name in BODIES:
        d = out[name]
        k = sorted(d)
        print(f"✓ {name}: {len(d):,} daily rows, {k[0]} → {k[-1]}  →  {os.path.basename(OUT)}")


if __name__ == "__main__":
    main()
