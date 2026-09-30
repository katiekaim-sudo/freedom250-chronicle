#!/usr/bin/env python3
"""phases.py — THE CLOCK WITH A HUNDRED HANDS. Every phase, computed. None guessed.

KATIE'S RULING, 2026-07-12 (DR-020)
-----------------------------------
    "Everything is in a phase of everything at all times. All planets are in some phase from
     every synodic cycle. Every planet is in a phase from their homes, from their exaltations,
     from previous aspects. It's a never-ending clock with 100 layers and hands."

She is right, and that is a PROBLEM as much as a truth. Ten planets give 45 synodic pairs; add
each planet's phase from its domicile and its exaltation, and its phase against its own natal
position, and you have ~150 true statements about any given moment. **A reading that names them
all is the address trap at cosmic scale** (Reading the Charts §8.3).

So this module does the half a machine should do — it COMPUTES all of them, exactly — and it
marks which ones a reading is allowed to NAME. The rest stay in the table: available, true,
and unspoken.

THE GRAMMAR — every cycle, whatever it is between, has the same three fields
---------------------------------------------------------------------------
    SEED   the conjunction — 0°. The thing is planted.
    FRUIT  the opposition — 180°. The thing is fully lit, and fully seen.
    DIRECTION  waxing (0→180): building toward the fruit.
               waning (180→360): distributing it, dying back toward the next seed.

Eight phases, after Rudhyar's lunation cycle, applied to ANY pair:
    New 0-45 · Crescent 45-90 · First Quarter 90-135 · Gibbous 135-180
    Full 180-225 · Disseminating 225-270 · Last Quarter 270-315 · Balsamic 315-360

That is the whole vocabulary. A Claude can now say ANY phase in one sentence-shape: *what cycle,
what phase, which direction.*

THE FOUR CLOCKS
---------------
1. SYNODIC   — every pair of bodies. 45 hands. The angle is measured from the SLOWER body to the
               FASTER one, in the direction of the faster body's motion, so "waxing" always means
               "since the last conjunction."
2. DIGNITY   — Katie's layer, and the reason this file exists. A planet is in a phase from its own
               exaltation. Saturn is exalted in Libra, so **Saturn in Aries is the FULL phase of
               its own exaltation** — the same want, the wrong tools, at maximum illumination.
               Run as TWO LAYERS, per Katie:
                 · SIGN  — the standing CONDITION (Whole Sign; Saturn is in its full season for
                           three years, and no single day owns it).
                 · DEGREE — the exact HAND (traditional exaltation degrees), which perfects on a
                           computable date. Condition vs trigger — the vault's own ladder.
               Classical bodies only. Uranus, Neptune and Pluto have NO traditional dignity, and
               this module will not invent one for them.
3. RETURN    — a transiting planet against its own NATAL position. Conjunction = the return.
               Opposition = the halfway house. (This is the clock that caught the 2026-07-22
               Saturn opposition to the founding Saturn, which no queue had logged.)
4. ASPECT-CYCLE — applying or separating, and which pass of a multi-pass transit. Reported as
               `applying` / `separating` on every row; the passes themselves come from
               `perfections()`.

THE DISCIPLINE — what a reading may NAME (Katie's ruling, option B)
-------------------------------------------------------------------
Compute all of it; narrate only what earns it. A row is marked `nameable=True` when ANY of:

    (root)  its cycle involves the chart's ROOT planet(s) or the CHART RULER — the master move
            (a loop terminus = EVERY member is the root; pass them all)
            (Reading the Charts §7.3) applied one layer up;
    (era)   both bodies are OUTER (Uranus, Neptune, Pluto) — these set the era whatever the root
            says, and DR-003 already binds us to read them as cycle seeds;
    (exact) the phase sits within 1° of a perfection against a US NATAL point.

Everything else is `nameable=False`. **It is not false. It is not hidden. It is BACKGROUND.**
This is the fence Katie asked for: *"the more the better, but note it so other Claudes don't get
confused with the bloat."* If you are writing prose and you find yourself naming a background
row, stop — you have left the method and are listing addresses.

USAGE
-----
    python3 "99 - Templates/phases.py" 2026-07-18          # the full table for a moment
    python3 "99 - Templates/phases.py" 2026-07-18 --named  # only what a reading may say

    from phases import phase_table, perfections
"""
import os
import sys
from datetime import datetime, timedelta, timezone

try:
    import swisseph as swe
except ImportError:
    sys.exit("pyswisseph missing — pip install pyswisseph (see nightly_sync_env_gotchas)")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))) if os.path.dirname(os.path.abspath(__file__)) not in sys.path else None
from swiss_ephemeris import FLAGS as FLG  # noqa: E402  2026-09-25: Swiss/JPL files, never silent Moshier
SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
         "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

# Ordered SLOWEST → FASTEST. The synodic angle is always measured from the slower to the faster,
# so "waxing" reliably means "since the last conjunction."
BODIES = [("Pluto", swe.PLUTO), ("Neptune", swe.NEPTUNE), ("Uranus", swe.URANUS),
          ("Saturn", swe.SATURN), ("Jupiter", swe.JUPITER), ("Mars", swe.MARS),
          ("Sun", swe.SUN), ("Venus", swe.VENUS), ("Mercury", swe.MERCURY), ("Moon", swe.MOON)]
IDX = {n: i for i, (n, _) in enumerate(BODIES)}
OUTER = {"Uranus", "Neptune", "Pluto"}

# Traditional dignities. The outers are ABSENT on purpose — they have none, and a modern
# invention would be a made-up degree, which is the one sin this vault does not forgive.
EXALT_DEG = {"Sun": ("Aries", 19), "Moon": ("Taurus", 3), "Mercury": ("Virgo", 15),
             "Venus": ("Pisces", 27), "Mars": ("Capricorn", 28), "Jupiter": ("Cancer", 15),
             "Saturn": ("Libra", 21)}
DOMICILE = {"Sun": ["Leo"], "Moon": ["Cancer"], "Mercury": ["Gemini", "Virgo"],
            "Venus": ["Taurus", "Libra"], "Mars": ["Aries", "Scorpio"],
            "Jupiter": ["Sagittarius", "Pisces"], "Saturn": ["Capricorn", "Aquarius"]}

PHASES = [(0, "New"), (45, "Crescent"), (90, "First Quarter"), (135, "Gibbous"),
          (180, "Full"), (225, "Disseminating"), (270, "Last Quarter"), (315, "Balsamic")]

# The US natal chart — DR-002. July 2 1776, 5:10 PM LMT, Philadelphia. NOT Sibley, not July 4.
US_NATAL_JD = swe.julday(1776, 7, 2, 17 + 10 / 60 + 75.1652 / 15.0)


def _lon(pl, jd):
    try:
        x, _ = swe.calc_ut(jd, pl, FLG)
    except Exception:
        x, _ = swe.calc_ut(jd, pl, swe.FLG_MOSEPH | swe.FLG_SPEED)
    return x[0], x[3]                      # longitude, speed


def jd_of(dt):
    dt = dt.astimezone(timezone.utc) if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    return swe.julday(dt.year, dt.month, dt.day, dt.hour + dt.minute / 60 + dt.second / 3600)


def fmt(l):
    s, d = int(l // 30) % 12, l % 30
    return f"{int(d)}°{int(round((d % 1) * 60)):02d}' {SIGNS[s]}"


def phase_of(angle):
    """(name, direction) for a 0-360 phase angle. This is the whole vocabulary."""
    a = angle % 360
    name = PHASES[0][1]
    for lo, nm in PHASES:
        if a >= lo:
            name = nm
    return name, ("waxing" if a < 180 else "waning")


def us_natal():
    return {n: _lon(pl, US_NATAL_JD)[0] for n, pl in BODIES}


def _as_load(*groups):
    """root may be one planet or every member of a loop. chart_ruler is usually one name."""
    out = set()
    for g in groups:
        if not g:
            continue
        if isinstance(g, str):
            out.add(g)
        else:
            out.update(p for p in g if p)
    return out


def phase_table(dt, root=None, chart_ruler=None):
    """Every hand on the clock at `dt`. Rows are dicts; `nameable` marks what may be SPOKEN.

    `root` / `chart_ruler` — the planets the chart already made load-bearing (Reading the Charts
    §7.3). If the terminus is a loop, pass every member as `root` (string or iterable).
    Leave them None and only the (era) and (exact) exceptions mark rows nameable — honest, but thinner."""
    jd = jd_of(dt)
    pos = {n: _lon(pl, jd) for n, pl in BODIES}
    nat = us_natal()
    load = _as_load(root, chart_ruler)
    rows = []

    # ── clock 1: the 45 synodic pairs ────────────────────────────────────────────────
    for i, (slow, _) in enumerate(BODIES):
        for fast, _ in BODIES[i + 1:]:
            ls, lf = pos[slow][0], pos[fast][0]
            angle = (lf - ls) % 360
            nm, dr = phase_of(angle)
            rel = pos[fast][1] - pos[slow][1]      # closing or opening?
            rows.append(dict(
                clock="synodic", cycle=f"{slow}–{fast}", angle=angle, phase=nm, direction=dr,
                detail=f"{fast} {fmt(lf)} · {slow} {fmt(ls)}",
                applying=(rel > 0 and angle < 180) or (rel < 0 and angle > 180),
                nameable=({slow, fast} <= OUTER) or bool(load & {slow, fast})))

    # ── clock 2: DIGNITY — Katie's layer, two layers deep ────────────────────────────
    for n, (sign, deg) in EXALT_DEG.items():
        l = pos[n][0]
        seed = SIGNS.index(sign) * 30 + deg          # the exaltation DEGREE = the seed
        angle = (l - seed) % 360
        nm, dr = phase_of(angle)
        cur = SIGNS[int(l // 30) % 12]
        fall = SIGNS[(SIGNS.index(sign) + 6) % 12]
        cond = ("EXALTED" if cur == sign else "FALL" if cur == fall else
                "DOMICILE" if cur in DOMICILE[n] else
                "DETRIMENT" if cur in [SIGNS[(SIGNS.index(s) + 6) % 12] for s in DOMICILE[n]]
                else "peregrine")
        rows.append(dict(
            clock="dignity", cycle=f"{n} from its exaltation ({deg}° {sign})",
            angle=angle, phase=nm, direction=dr,
            # BOTH LAYERS, per Katie: the sign is the standing CONDITION (whole-sign, years long);
            # the degree is the exact HAND, and it perfects on a date you can compute.
            detail=f"{n} {fmt(l)} — sign layer: in {cur}, {cond} · degree layer: "
                   f"{angle:.2f}° from the seed, {abs(180 - angle):.2f}° from FULL",
            applying=(angle < 180) == (pos[n][1] > 0),
            nameable=(n in load) or cond in ("EXALTED", "FALL")))

    # ── clock 3: RETURN — transiting body against its own natal place ────────────────
    for n, _ in BODIES:
        if n == "Moon":
            continue                                  # 27 days; it is noise at this scale
        angle = (pos[n][0] - nat[n]) % 360
        nm, dr = phase_of(angle)
        orb = min(angle % 180, 180 - (angle % 180))
        rows.append(dict(
            clock="return", cycle=f"{n} to the US natal {n}", angle=angle, phase=nm, direction=dr,
            detail=f"transiting {fmt(pos[n][0])} · natal {fmt(nat[n])} — {orb:.2f}° from exact",
            applying=pos[n][1] > 0,
            nameable=(orb <= 1.0) or (n in load)))    # the (exact) exception — this caught Saturn

    return rows


def perfections(body, target_lon, start, stop):
    """Every pass of `body` over `target_lon` — the multi-pass truth (DR-003's discipline).
    A transit is almost never one date: it hits, stations, comes back."""
    pl = dict(BODIES)[body]
    def d(t):
        x = (_lon(pl, jd_of(t))[0] - target_lon) % 360
        return x - 360 if x > 180 else x
    out, cur, prev = [], start, None
    while cur < stop:
        v = d(cur)
        if prev is not None and (prev < 0) != (v < 0) and abs(prev - v) < 5:
            lo, hi = cur - timedelta(days=1), cur
            for _ in range(35):
                m = lo + (hi - lo) / 2
                if (d(lo) < 0) != (d(m) < 0): hi = m
                else: lo = m
            out.append((lo, _lon(pl, jd_of(lo))[1] < 0))     # (when, retrograde?)
        prev = v
        cur += timedelta(days=1)
    return out


def main():
    when = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else None
    dt = datetime.fromisoformat(when).replace(tzinfo=timezone.utc) if when \
        else datetime.now(timezone.utc)
    only = "--named" in sys.argv

    # 2026 Cancer: Mercury ↔ Moon loop. Both members are the root (DR-020 fence).
    rows = phase_table(dt, root=("Mercury", "Moon"), chart_ruler="Mercury")
    print("=" * 78)
    print(f"THE CLOCK WITH A HUNDRED HANDS — {dt:%Y-%m-%d %H:%M} UTC")
    print("  root assumed: Mercury ↔ Moon loop (2026 Cancer). Pass your own; a loop = every member.")
    print("=" * 78)
    for clock in ("dignity", "return", "synodic"):
        sel = [r for r in rows if r["clock"] == clock and (r["nameable"] or not only)]
        named = sum(1 for r in rows if r["clock"] == clock and r["nameable"])
        tot = sum(1 for r in rows if r["clock"] == clock)
        print(f"\n── {clock.upper()} — {named} nameable of {tot}")
        for r in sorted(sel, key=lambda r: (not r["nameable"], r["cycle"])):
            mark = "★" if r["nameable"] else "·"
            print(f" {mark} {r['cycle']:34s} {r['phase']:14s} {r['direction']:7s} "
                  f"{'applying' if r['applying'] else 'separating':10s} {r['detail']}")
    print("\n" + "-" * 78)
    print("★ = a reading MAY name it (root · era · exact-to-natal).  · = BACKGROUND: true,")
    print("    computed, and NOT to be narrated. Naming a background row is the address trap.")


if __name__ == "__main__":
    main()
