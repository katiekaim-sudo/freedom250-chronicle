#!/usr/bin/env python3
"""Build one shared persona chart for the exact 1891 Neptune-Pluto conjunction.

The exact first perfection is root-solved with Swiss Ephemeris. Its shared
longitude becomes one fused persona target. The first post-conjunction moment
when the tropical geocentric Sun reaches that fixed longitude produces:

  * one standalone Neptune-Pluto Conjunction Persona wheel;
  * one conjunction-radix / persona biwheel;
  * one machine-readable facts record;
  * one review gallery with separate Neptune and Pluto focal dossiers.

The live Sentient Sun chart, structure, and wheel engines are imported at
runtime. This is research-only and does not amend the live Freedom 250 vault.
"""

from __future__ import annotations

import html
import json
import math
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import swisseph as swe


HERE = Path(__file__).resolve().parent
OUTPUT_DIR = HERE / "charts"
DATA_PATH = HERE / "NEPTUNE_PLUTO_1891_CONJUNCTION_PERSONA.json"
MANIFEST_PATH = OUTPUT_DIR / "conjunction_persona_manifest.json"
GALLERY_PATH = (
    OUTPUT_DIR
    / "Neptune–Pluto 1891 — Conjunction Persona Gallery.html"
)

SENTIENT_SUN = Path("[local-path-removed] Sun")
WHEEL_ENGINE = SENTIENT_SUN / "chart-wheel-engine.html"
DEEP_CURRENT_ENGINE = Path(
    "Chronicle/"
    "99 - Templates/synodic_cycles.py"
)
PERSONA_METHOD = Path(
    "[local-path-removed] General/"
    "outputs/persona_charts_research_2026-07-22/"
    "PERSONA_CHARTS_CLEAN_METHOD_REFERENCE.md"
)

sys.path.insert(0, str(SENTIENT_SUN))
import make_reading as mr  # noqa: E402
import reading_engine as re  # noqa: E402


LATITUDE = 38.8951
LONGITUDE = -77.0364
PLACE = "Washington, D.C."
ZONE_NAME = "America/New_York"
ZONE = ZoneInfo(ZONE_NAME)
FLAGS = swe.FLG_MOSEPH | swe.FLG_SPEED

BODY_ORDER = [
    "Sun",
    "Moon",
    "Mercury",
    "Venus",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
    "Pluto",
    "Chiron",
    "Node",
]


def julian_day(dt_utc: datetime) -> float:
    hour = (
        dt_utc.hour
        + dt_utc.minute / 60.0
        + dt_utc.second / 3600.0
        + dt_utc.microsecond / 3_600_000_000.0
    )
    return swe.julday(dt_utc.year, dt_utc.month, dt_utc.day, hour)


def jd_to_utc(jd_ut: float) -> datetime:
    return datetime(2000, 1, 1, 12, tzinfo=timezone.utc) + timedelta(
        days=jd_ut - 2451545.0
    )


def signed_delta(a: float, b: float) -> float:
    return ((a - b + 540.0) % 360.0) - 180.0


def angular_distance(a: float, b: float) -> float:
    return abs(signed_delta(a, b))


def body_state(jd_ut: float, body: int) -> tuple[float, float]:
    result = swe.calc_ut(jd_ut, body, FLAGS)[0]
    return result[0] % 360.0, result[3]


def conjunction_delta(jd_ut: float) -> float:
    neptune, _ = body_state(jd_ut, swe.NEPTUNE)
    pluto, _ = body_state(jd_ut, swe.PLUTO)
    return signed_delta(neptune, pluto)


def bisection_root(
    function, lo: float, hi: float, iterations: int = 100
) -> float:
    flo = function(lo)
    fhi = function(hi)
    if flo == 0.0:
        return lo
    if fhi == 0.0:
        return hi
    if flo * fhi > 0:
        raise RuntimeError(
            f"Root not bracketed: f(lo)={flo}, f(hi)={fhi}"
        )
    for _ in range(iterations):
        mid = (lo + hi) / 2.0
        fm = function(mid)
        if flo * fm <= 0:
            hi = mid
            fhi = fm
        else:
            lo = mid
            flo = fm
    return (lo + hi) / 2.0


def exact_first_conjunction() -> float:
    """First exact Neptune-Pluto perfection on the canonical 1891 seed date."""
    lo = julian_day(datetime(1891, 8, 2, 0, tzinfo=timezone.utc))
    hi = julian_day(datetime(1891, 8, 3, 0, tzinfo=timezone.utc))
    return bisection_root(conjunction_delta, lo, hi)


def sun_lon(jd_ut: float) -> float:
    return (
        swe.calc_ut(jd_ut, swe.SUN, swe.FLG_SWIEPH | swe.FLG_SPEED)[0][0] % 360
    )


def find_solar_contact(
    jd_radix: float, radix_sun: float, target_lon: float
) -> tuple[float, float]:
    """Swiss solcross result plus independent scan/bisection verification."""
    jd_swiss = float(
        swe.solcross_ut(target_lon, jd_radix + 1e-7, swe.FLG_SWIEPH)
    )
    arc = (target_lon - radix_sun) % 360.0
    if arc < 1e-10:
        arc = 360.0

    step = 0.25
    previous_jd = jd_radix + 1e-7
    previous_lon = sun_lon(previous_jd)
    travelled = 0.0
    while previous_jd < jd_radix + 370.0:
        current_jd = previous_jd + step
        current_lon = sun_lon(current_jd)
        travelled += (current_lon - previous_lon) % 360.0
        if travelled >= arc:
            lo, hi = previous_jd, current_jd
            break
        previous_jd, previous_lon = current_jd, current_lon
    else:
        raise RuntimeError("Could not bracket the first solar contact")

    jd_bisect = bisection_root(
        lambda jd: signed_delta(sun_lon(jd), target_lon), lo, hi
    )
    return jd_swiss, jd_bisect


def compute_chart(local_dt: datetime) -> dict:
    seconds = local_dt.second + local_dt.microsecond / 1_000_000.0
    offset = local_dt.utcoffset().total_seconds() / 3600.0
    return mr.compute(
        local_dt.year,
        local_dt.month,
        local_dt.day,
        local_dt.hour,
        local_dt.minute,
        LATITUDE,
        LONGITUDE,
        offset,
        seconds=seconds,
    )


def compact_position(position: dict) -> dict:
    return {
        "lon": round(position["lon"], 9),
        "sign": position["sign"],
        "degree_in_sign": round(position["lon"] % 30.0, 6),
        "whole_sign_house": position["house"],
        "retrograde": bool(position["retro"]),
        "speed_deg_day": round(position["speed"], 8),
        "declination": round(position.get("decl", 0.0), 6),
    }


def frame_record(chart: dict) -> dict:
    positions = chart["pos"]
    ruler = re.RULER[chart["asc_sign"]]
    chain, final_dispositor, kind = re.dispositor_chain(positions, ruler)
    mc_house = (
        (int(chart["mc"] // 30) - int(chart["asc"] // 30)) % 12
    ) + 1
    all_chains = {}
    for body in BODY_ORDER:
        if body in ("Chiron", "Node"):
            continue
        body_chain, terminal, body_kind = re.dispositor_chain(positions, body)
        all_chains[body] = {
            "chain": body_chain,
            "terminal": terminal,
            "kind": body_kind,
        }
    return {
        "asc": round(chart["asc"], 9),
        "asc_sign": chart["asc_sign"],
        "mc": round(chart["mc"], 9),
        "mc_sign": chart["mc_sign"],
        "mc_whole_sign_house": mc_house,
        "chart_ruler": ruler,
        "chart_ruler_house": positions[ruler]["house"],
        "dispositor_chain": chain,
        "final_dispositor": final_dispositor,
        "dispositor_kind": kind,
        "all_dispositor_paths": all_chains,
    }


def chart_structure(chart: dict) -> dict:
    positions = chart["pos"]
    aspects = re.huber_aspects(positions)
    configurations = re.configurations(positions, aspects)
    return {
        "frame": frame_record(chart),
        "positions": {
            body: compact_position(positions[body])
            for body in re.ALL_BODIES
            if body in positions
        },
        "huber_whole_pattern": re.huber_whole_pattern(
            positions, aspects, configurations
        ),
        "configurations": configurations,
        "huber_aspects": aspects,
    }


def contacts_for(body: str, aspects: list[dict]) -> list[dict]:
    return [
        aspect
        for aspect in aspects
        if aspect["a"] == body or aspect["b"] == body
    ]


def calculate() -> dict:
    radix_jd = exact_first_conjunction()
    radix_utc = jd_to_utc(radix_jd)
    radix_local = radix_utc.astimezone(ZONE)
    radix_chart = compute_chart(radix_local)
    radix_positions = radix_chart["pos"]
    target_lon = (
        radix_positions["Neptune"]["lon"]
        + radix_positions["Pluto"]["lon"]
    ) / 2.0

    persona_jd, persona_jd_verify = find_solar_contact(
        radix_jd, radix_positions["Sun"]["lon"], target_lon
    )
    solver_delta_seconds = abs(persona_jd - persona_jd_verify) * 86400.0
    if solver_delta_seconds > 0.1:
        raise RuntimeError(
            f"Solar solvers disagree by {solver_delta_seconds:.6f}s"
        )
    persona_utc = jd_to_utc(persona_jd)
    persona_local = persona_utc.astimezone(ZONE)
    persona_chart = compute_chart(persona_local)
    persona_structure = chart_structure(persona_chart)
    persona_positions = persona_chart["pos"]
    persona_aspects = persona_structure["huber_aspects"]

    focal = {}
    for body in ("Neptune", "Pluto"):
        focal[body] = {
            "position": compact_position(persona_positions[body]),
            "distance_from_persona_sun_degrees": round(
                angular_distance(
                    persona_positions[body]["lon"],
                    persona_positions["Sun"]["lon"],
                ),
                9,
            ),
            "dispositor_path": persona_structure["frame"][
                "all_dispositor_paths"
            ][body],
            "contacts": contacts_for(body, persona_aspects),
        }

    return {
        "status": "research_only_not_adopted",
        "subject": "1891 Neptune-Pluto conjunction persona",
        "definition": (
            "one shared first post-event solar conjunction to the exact fused "
            "Neptune-Pluto radix longitude"
        ),
        "radix": {
            "pass": "first exact perfection",
            "local": radix_local.isoformat(timespec="microseconds"),
            "utc": radix_utc.isoformat(timespec="microseconds"),
            "jd_ut": round(radix_jd, 12),
            "place": PLACE,
            "latitude": LATITUDE,
            "longitude": LONGITUDE,
            "timezone": ZONE_NAME,
            "shared_neptune_pluto_longitude": round(target_lon, 9),
            "neptune_pluto_separation_arcseconds": round(
                angular_distance(
                    radix_positions["Neptune"]["lon"],
                    radix_positions["Pluto"]["lon"],
                )
                * 3600.0,
                6,
            ),
            "time_basis": (
                "First exact geocentric perfection root-solved on the canonical "
                "1891-08-02 seed date; distinct from the live noon proxy"
            ),
            **chart_structure(radix_chart),
        },
        "seed_family": {
            "co_presence_rule": (
                "Outer conjunctions are cycle-seed windows; exact passes are "
                "phase markers within the family, not isolated detonations."
            ),
            "exact_passes_utc": [
                "1891-08-02T16:48:45.629000+00:00",
                "1891-11-05T22:13:09.295000+00:00",
                "1892-04-30T15:49:02.184000+00:00",
            ],
            "persona_radix_choice": (
                "first exact pass, because the live Deep Tide seed is keyed to "
                "1891-08-02"
            ),
        },
        "persona": {
            "target_name": "Neptune-Pluto conjunction",
            "target_radix_longitude": round(target_lon, 9),
            "days_after_radix": round(persona_jd - radix_jd, 9),
            "event": {
                "local": persona_local.isoformat(timespec="microseconds"),
                "utc": persona_utc.isoformat(timespec="microseconds"),
                "jd_ut": round(persona_jd, 12),
                "zone_abbreviation": persona_local.tzname(),
            },
            "verification": {
                "swiss_solcross_vs_bisection_seconds": round(
                    solver_delta_seconds, 6
                ),
                "sun_minus_target_arcseconds": round(
                    signed_delta(
                        persona_positions["Sun"]["lon"], target_lon
                    )
                    * 3600.0,
                    6,
                ),
            },
            **persona_structure,
            "persona_sun": {
                "whole_sign_house": persona_positions["Sun"]["house"],
                "contacts": contacts_for("Sun", persona_aspects),
            },
            "focal_targets_inside_persona": focal,
        },
        "settings": {
            "zodiac": "tropical",
            "center": "geocentric",
            "houses": "Whole Sign",
            "rulers": "traditional",
            "node": "true",
            "aspect_math": "live Sentient Sun Huber web",
            "reference_place_policy": (
                "radix place retained for the persona event"
            ),
            "america_916": (
                "unavailable for this historical epoch in the live Freedom 250 "
                "daily JPL cache; not extrapolated"
            ),
        },
        "dependency_notes": {
            "shared_chart": (
                "The conjunction has one exact longitude, so Neptune and Pluto "
                "share one Persona-Sun trigger and one derived event frame."
            ),
            "two_lenses": (
                "Neptune and Pluto remain separate focal bodies inside the one "
                "shared persona chart; their internal placements, contacts, and "
                "dispositor routes may be read separately."
            ),
            "persona_sun": (
                "The Persona Sun repeats the exact conjunction degree by "
                "construction."
            ),
            "slow_bodies": (
                "Outer-body near-returns during the first solar circuit are "
                "mechanically dependent and receive no independent vote."
            ),
            "evidence_family": "conditional, subordinate, zero_vote",
        },
        "provenance": {
            "deep_current_engine": str(DEEP_CURRENT_ENGINE),
            "persona_method": str(PERSONA_METHOD),
            "chart_math": str(SENTIENT_SUN / "make_reading.py"),
            "structure_engine": str(SENTIENT_SUN / "reading_engine.py"),
            "wheel_engine": str(WHEEL_ENGINE),
        },
    }


def wheel_engine_js() -> str:
    source = WHEEL_ENGINE.read_text(encoding="utf-8")
    start = source.index("<script>") + len("<script>")
    end = source.index("const DATA =", start)
    return source[start:end]


def degree_label(longitude: float) -> str:
    return f"{math.floor(longitude % 30)}°"


def wheel_positions(position_map: dict) -> list[list]:
    return [
        [
            body,
            position_map[body]["sign"],
            degree_label(position_map[body]["lon"]),
            bool(position_map[body]["retrograde"]),
            round(position_map[body]["lon"], 8),
        ]
        for body in BODY_ORDER
    ]


def render_svg(
    record: dict,
    outer_name: str | None = None,
    outer_map: dict | None = None,
) -> str:
    runner = [
        wheel_engine_js(),
        f"\nconst REC={json.dumps(record, ensure_ascii=False)};",
        "REC.asp=aspectsBetween(REC.pos);",
    ]
    if outer_name and outer_map:
        runner.extend(
            [
                f"CHARTS[{json.dumps(outer_name)}]="
                f"{json.dumps(outer_map)};",
                f"process.stdout.write(wheelSVG("
                f"REC,{json.dumps(outer_name)},true));",
            ]
        )
    else:
        runner.append("process.stdout.write(wheelSVG(REC,null,false));")

    with tempfile.NamedTemporaryFile(
        "w", suffix=".mjs", delete=False, encoding="utf-8"
    ) as handle:
        handle.write("".join(runner))
        script_path = Path(handle.name)
    try:
        result = subprocess.run(
            ["node", str(script_path)],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
    finally:
        script_path.unlink(missing_ok=True)
    if result.returncode != 0 or not result.stdout.startswith("<svg"):
        raise RuntimeError(
            f"Wheel engine failed ({result.returncode}): "
            f"{result.stderr[:1000]}"
        )
    return result.stdout


def display_event(event: dict) -> str:
    local = datetime.fromisoformat(event["local"])
    return (
        local.strftime("%d %b %Y · %H:%M:%S ")
        + event["zone_abbreviation"]
    )


def display_exact_local(iso_datetime: str, zone_abbreviation: str) -> str:
    local = datetime.fromisoformat(iso_datetime)
    return (
        local.strftime("%d %b %Y · %H:%M:%S")
        + f".{local.microsecond:06d} {zone_abbreviation}"
    )


def display_degree(longitude: float, seconds: bool = False) -> str:
    signs = [
        "Aries",
        "Taurus",
        "Gemini",
        "Cancer",
        "Leo",
        "Virgo",
        "Libra",
        "Scorpio",
        "Sagittarius",
        "Capricorn",
        "Aquarius",
        "Pisces",
    ]
    sign = signs[int(longitude // 30) % 12]
    value = longitude % 30
    degree = int(value)
    minute_value = (value - degree) * 60
    minute = int(minute_value)
    second = round((minute_value - minute) * 60, 2)
    if seconds:
        return f"{degree}°{minute:02d}′{second:05.2f}″ {sign}"
    return f"{degree}°{minute:02d}′ {sign}"


def aspect_labels(aspects: list[dict]) -> str:
    if not aspects:
        return "No qualifying Huber-web contacts."
    bits = []
    for aspect in aspects:
        other = aspect["b"] if aspect["a"] in ("Neptune", "Pluto") else aspect["a"]
        bits.append(
            f"{html.escape(other)} {html.escape(aspect['type'])} "
            f"({aspect['orb']:.2f}°)"
        )
    return " · ".join(bits)


def render(data: dict) -> dict:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    radix = data["radix"]
    persona = data["persona"]
    event_label = display_event(persona["event"])

    standalone_record = {
        "asc": round(persona["frame"]["asc"], 8),
        "pos": wheel_positions(persona["positions"]),
        "__date": "NEPTUNE–PLUTO CONJUNCTION PERSONA",
        "cap1": f"{event_label} · {PLACE}",
        "cap2": "standalone persona event chart · Whole Sign",
    }
    standalone_svg = render_svg(standalone_record)

    overlay_record = {
        "asc": round(radix["frame"]["asc"], 8),
        "pos": wheel_positions(radix["positions"]),
        "__date": "RADIX + CONJUNCTION PERSONA",
        "cap1": "1891 exact conjunction radix inside · persona outside",
        "cap2": f"outer ring: shared conjunction persona · {event_label}",
    }
    outer_map = {
        body: round(persona["positions"][body]["lon"], 8)
        for body in BODY_ORDER
    }
    biwheel_svg = render_svg(
        overlay_record,
        outer_name="Neptune-Pluto Conjunction Persona",
        outer_map=outer_map,
    )

    standalone_name = (
        "Neptune–Pluto 1891 — Conjunction Persona — Standalone.svg"
    )
    biwheel_name = (
        "Neptune–Pluto 1891 — Conjunction Persona + Radix — Biwheel.svg"
    )
    (OUTPUT_DIR / standalone_name).write_text(
        standalone_svg, encoding="utf-8"
    )
    (OUTPUT_DIR / biwheel_name).write_text(
        biwheel_svg, encoding="utf-8"
    )
    return {
        "event_label": event_label,
        "standalone": standalone_name,
        "biwheel": biwheel_name,
        "standalone_svg": standalone_svg,
        "biwheel_svg": biwheel_svg,
    }


def gallery_html(data: dict, rendered: dict) -> str:
    radix = data["radix"]
    persona = data["persona"]
    frame = persona["frame"]
    focal = persona["focal_targets_inside_persona"]
    standalone_file = html.escape(rendered["standalone"], quote=True)
    biwheel_file = html.escape(rendered["biwheel"], quote=True)
    root_route = " → ".join(frame["dispositor_chain"])
    radix_label = display_exact_local(radix["local"], "EST")

    lens_cards = []
    for body in ("Neptune", "Pluto"):
        lens = focal[body]
        position = lens["position"]
        route = " → ".join(lens["dispositor_path"]["chain"])
        lens_cards.append(
            f"""
<article class="lens">
  <p class="eyebrow">{body.upper()} FOCAL LENS</p>
  <h3>{body} inside the shared persona</h3>
  <dl>
    <dt>Position</dt><dd>{display_degree(position["lon"], seconds=True)}</dd>
    <dt>Whole Sign house</dt><dd>H{position["whole_sign_house"]}</dd>
    <dt>Motion</dt><dd>{"retrograde" if position["retrograde"] else "direct"} · {position["speed_deg_day"]:.8f}°/day</dd>
    <dt>From Persona Sun</dt><dd>{lens["distance_from_persona_sun_degrees"]:.6f}°</dd>
    <dt>Governance route</dt><dd>{html.escape(route)}</dd>
  </dl>
  <p class="contacts"><b>Aspect web:</b> {aspect_labels(lens["contacts"])}</p>
</article>"""
        )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>1891 Neptune–Pluto · Conjunction Persona</title>
<style>
  :root {{
    --paper:#faf8f3; --card:#fffdf7; --ink:#3a3428; --ink2:#5b554a;
    --faint:#8a7d68; --line:#d4c9b0; --accent:#7a2e1d; --wash:#eee6d7;
  }}
  * {{ box-sizing:border-box; }}
  body {{
    margin:0; background:var(--paper); color:var(--ink);
    font-family:"Iowan Old Style",Palatino,Georgia,serif;
  }}
  main {{ width:min(1480px,96vw); margin:0 auto; padding:42px 0 70px; }}
  h1,h2,h3,p {{ margin-top:0; }}
  h1 {{ font-size:clamp(2rem,4vw,3.6rem); font-weight:400; margin-bottom:12px; }}
  h2 {{ font-size:2rem; font-weight:400; margin-bottom:6px; }}
  h3 {{ font-size:1.2rem; font-weight:500; margin-bottom:8px; }}
  p {{ color:var(--faint); line-height:1.55; }}
  .top {{ max-width:1040px; }}
  .eyebrow {{
    color:var(--accent); font-size:.72rem; font-weight:700;
    letter-spacing:.13em; margin-bottom:8px;
  }}
  .notice {{
    background:var(--card); border:1px solid var(--line);
    border-left:4px solid var(--accent); border-radius:12px;
    padding:14px 18px; color:var(--ink2); line-height:1.55; margin:20px 0;
  }}
  .facts {{ display:flex; flex-wrap:wrap; gap:7px; margin:14px 0; }}
  .facts span {{
    padding:5px 9px; background:var(--wash); border-radius:8px;
    color:var(--faint); font-size:.84rem;
  }}
  .pair,.lenses {{
    display:grid; grid-template-columns:1fr 1fr; gap:24px; margin-top:24px;
  }}
  article {{
    background:var(--card); border:1px solid var(--line); border-radius:16px;
    padding:20px; box-shadow:0 8px 30px rgba(72,58,35,.05);
  }}
  .note {{ min-height:2.4em; font-size:.94rem; }}
  .wheel {{ margin:8px auto 12px; max-width:700px; }}
  .wheel svg {{ width:100%; height:auto; display:block; }}
  .lenses {{ margin-top:30px; }}
  .lens dl {{ display:grid; grid-template-columns:auto 1fr; gap:5px 14px; margin:12px 0; }}
  .lens dt {{ color:var(--faint); font-size:.78rem; text-transform:uppercase; letter-spacing:.05em; }}
  .lens dd {{ margin:0; color:var(--ink2); }}
  .contacts {{ font-size:.9rem; }}
  a {{ color:var(--accent); text-underline-offset:3px; }}
  footer {{ margin-top:40px; color:var(--faint); font-size:.86rem; line-height:1.55; }}
  @media(max-width:900px) {{ .pair,.lenses {{ grid-template-columns:1fr; }} }}
</style>
</head>
<body>
<main>
  <header class="top">
    <p class="eyebrow">FREEDOM 250 · THE DEEP TIDE · RESEARCH SET</p>
    <h1>1891 Neptune–Pluto Conjunction Persona</h1>
    <p>One fused persona chart for the conjunction as its own astrological subject, with Neptune and Pluto retained as component lenses inside the same derived world.</p>
    <div class="notice">
      <b>Exact-frame correction.</b> The live Deep Currents wheel uses noon Eastern on 2 August 1891. This research chart uses the actual first exact perfection at {html.escape(radix_label)}: {display_degree(radix["shared_neptune_pluto_longitude"], seconds=True)}. The eleven-minute correction moves the Ascendant back across the sign boundary, so the Whole Sign structure is materially different.
    </div>
    <div class="facts">
      <span><b>Shared target</b> {display_degree(persona["target_radix_longitude"], seconds=True)}</span>
      <span><b>Persona event</b> {html.escape(rendered["event_label"])}</span>
      <span><b>ASC</b> {display_degree(frame["asc"], seconds=True)}</span>
      <span><b>Chart ruler</b> {frame["chart_ruler"]}</span>
      <span><b>Persona Sun</b> H{persona["persona_sun"]["whole_sign_house"]}</span>
      <span><b>MC</b> {display_degree(frame["mc"], seconds=True)} · H{frame["mc_whole_sign_house"]}</span>
      <span><b>Root route</b> {html.escape(root_route)}</span>
    </div>
  </header>

  <div class="pair">
    <article>
      <h2>Conjunction persona alone</h2>
      <p class="note">The shared Persona-Sun event frame: its own Ascendant, Whole Sign houses, planets, and internal aspect web.</p>
      <div class="wheel">{rendered["standalone_svg"]}</div>
      <a href="{standalone_file}">Open standalone SVG</a>
    </article>
    <article>
      <h2>Persona around the exact conjunction radix</h2>
      <p class="note">The first exact 1891 conjunction inside; the shared conjunction persona on the outer ring.</p>
      <div class="wheel">{rendered["biwheel_svg"]}</div>
      <a href="{biwheel_file}">Open biwheel SVG</a>
    </article>
  </div>

  <div class="lenses">
    {''.join(lens_cards)}
  </div>

  <footer>
    Tropical · geocentric · Washington, D.C. · Whole Sign · true node · traditional rulers. Calculated with the live Sentient Sun math and rendered with its production wheel engine. The Persona Sun’s target degree is guaranteed by construction; slow-body persistence is dependent; the whole persona system remains conditional, subordinate, and zero-vote. Asteroid 916 America is unavailable at this historical epoch in the live Freedom 250 daily JPL cache and was not extrapolated.
  </footer>
</main>
</body>
</html>
"""


def main() -> None:
    data = calculate()
    DATA_PATH.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    rendered = render(data)
    GALLERY_PATH.write_text(
        gallery_html(data, rendered),
        encoding="utf-8",
    )
    manifest = {
        "status": "research_only_not_adopted",
        "gallery": GALLERY_PATH.name,
        "source_data": str(DATA_PATH),
        "radix": {
            "pass": data["radix"]["pass"],
            "local": data["radix"]["local"],
            "utc": data["radix"]["utc"],
            "place": data["radix"]["place"],
        },
        "persona": {
            "target": data["persona"]["target_name"],
            "local": data["persona"]["event"]["local"],
            "utc": data["persona"]["event"]["utc"],
        },
        "provenance": data["provenance"],
        "charts": {
            "standalone": rendered["standalone"],
            "biwheel": rendered["biwheel"],
        },
    }
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(GALLERY_PATH)
    print(DATA_PATH)
    print(MANIFEST_PATH)
    print("Rendered one shared persona wheel and one radix biwheel")


if __name__ == "__main__":
    main()
