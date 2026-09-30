#!/usr/bin/env python3
"""Cast 2027–2028 cardinal ingresses and project them into Ingress Charts.

Method: Reading the Charts / Mundane Engine spec. Washington D.C., Whole Sign,
exact Sun at 0° of the cardinal sign, traditional rulers, 916 America, Greer
standing with Aries always resetting the year. Bones only — no readings.

Re-run is idempotent. Does not rewrite the 2025–2026 interpretive cards.
Does not add Chart Readings Pass 1s or chart_reading_bones rows.
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import swisseph as swe

import mundane_engine as ME
from chart_conventions import DC_LAT, DC_LON, DC_TZ, clock_label
from minor_points import all_points

HERE = Path(__file__).resolve().parent
VAULT = HERE.parent
TARGET = VAULT / "04 - Synthesis" / "Cross-cuts" / "Ingress Charts.html"
ING_JSON = HERE / "ing_data.json"
ASTRO = VAULT / "03 - Astrology"
HISTORY = HERE / "mundane_history.json"

CARDINAL = ("Aries", "Cancer", "Libra", "Capricorn")
YEARS = (2027, 2028)
PLANET_ORDER = ("Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto")
GLYPH = {
    "Sun": "☉", "Moon": "☽", "Mercury": "☿", "Venus": "♀", "Mars": "♂",
    "Jupiter": "♃", "Saturn": "♄", "Uranus": "♅", "Neptune": "♆", "Pluto": "♇",
    "Chiron": "⚷", "Node": "☊", "America": "★",
}
ABBR = {
    "Sun": "Su", "Moon": "Mo", "Mercury": "Me", "Venus": "Ve", "Mars": "Ma",
    "Jupiter": "Ju", "Saturn": "Sa", "Uranus": "Ur", "Neptune": "Ne", "Pluto": "Pl",
    "Chiron": "Ch", "Node": "NN", "America": "Am",
}
SIGN_ABBR = {
    "Aries": "Ari", "Taurus": "Tau", "Gemini": "Gem", "Cancer": "Can",
    "Leo": "Leo", "Virgo": "Vir", "Libra": "Lib", "Scorpio": "Sco",
    "Sagittarius": "Sag", "Capricorn": "Cap", "Aquarius": "Aqu", "Pisces": "Pis",
}
SIGN_ELEMENT = {
    "Aries": "fire", "Taurus": "earth", "Gemini": "air", "Cancer": "water",
    "Leo": "fire", "Virgo": "earth", "Libra": "air", "Scorpio": "water",
    "Sagittarius": "fire", "Capricorn": "earth", "Aquarius": "air", "Pisces": "water",
}
ASPECT_GLYPH = {
    "conjunction": "☌", "sextile": "⚹", "square": "□", "trine": "△", "opposition": "☍",
}
WORKBOOK_ORB = {0: 8.0, 60: 5.0, 90: 7.0, 120: 7.0, 180: 8.0}
MONTHS = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
)
START = "/* F250-INGRESS-2027-2028-START */"
END = "/* F250-INGRESS-2027-2028-END */"
DECL_START = "/* F250-DECL-2027-2028-START */"
DECL_END = "/* F250-DECL-2027-2028-END */"


def utc_from_jd(jd: float) -> datetime:
    year, month, day, hour = swe.revjul(jd, swe.GREG_CAL)
    return datetime(year, month, day, tzinfo=timezone.utc) + timedelta(hours=hour)


def fmt_dms(lon: float, *, force_sign: str | None = None) -> tuple[str, str, float]:
    lon = lon % 360
    sign = force_sign or ME.sign_of(lon)
    if force_sign:
        d = 0.0 if abs(((lon - ME.SIGNS.index(force_sign) * 30 + 180) % 360) - 180) < 1e-6 else (lon % 30)
        if force_sign == "Aries" and lon > 359.5:
            d = 0.0
        if abs(d - 30) < 1e-6:
            d = 0.0
    else:
        d = ((lon % 360) + 1e-6) % 30
        if d >= 29.999:
            d = 0.0
            sign = ME.SIGNS[(ME.SIGNS.index(sign) + 1) % 12]
    deg = int(d)
    minute = int(round((d - deg) * 60))
    if minute == 60:
        deg += 1
        minute = 0
    return f"{deg}°{minute:02d}' {sign}", sign, lon


def fmt_decl(dec: float) -> str:
    hemi = "N" if dec >= 0 else "S"
    ad = abs(dec)
    deg = int(ad)
    minute = int(round((ad - deg) * 60))
    if minute == 60:
        deg += 1
        minute = 0
    return f"{deg:02d}°{hemi}{minute:02d}'"


def fmt_speed(spd: float) -> str:
    sign = "+" if spd >= 0 else "−"
    return f"{sign}{abs(spd):.2f}"


def standing_for(year: int, sign: str, history: dict[str, dict]) -> str:
    row = history.get(f"ingress-{year}-{sign.lower()}")
    return (row or {}).get("standing") or "nested_cardinal_stage"


def year_king(year: int) -> str:
    return f"{year} Aries"


def validity_line(year: int, sign: str, modality: str, standing: str) -> str:
    if standing == "governing" and sign == "Aries":
        return f"Full year (Mar {year} – Mar {year + 1})"
    if standing == "governing":
        months = ME.validity_months(modality)
        if months == 12:
            return f"Full year ({year})"
        if months == 6:
            return f"Six months (does not yield to the next cardinal)"
        return "Three months, then the next cardinal takes over"
    return f"Nested cardinal stage — does not replace {year_king(year)}"


def compute_chart(year: int, sign: str, history: dict[str, dict]) -> dict:
    ch = ME.cast_ingress(year, sign)
    jd = ch["jd"]
    utc = utc_from_jd(jd)
    local = utc.astimezone(DC_TZ)
    extras = all_points(jd)
    sun_lon = float(ME.SIGNS.index(sign) * 30)
    standing = standing_for(year, sign, history)
    modality = ch["asc_modality"]
    chart_id = f"{year}-{sign.lower()}"

    planets = []
    lons = {"Sun": sun_lon}
    for name in PLANET_ORDER:
        pl = ch["pos"][name]
        lon = sun_lon if name == "Sun" else pl["lon"]
        lons[name] = lon
        pos_s, sgn, _ = fmt_dms(lon, force_sign=sign if name == "Sun" else None)
        xx = swe.calc_ut(jd, ME.PLANETS[name])[0]
        eq = swe.calc_ut(jd, ME.PLANETS[name], swe.FLG_SWIEPH | swe.FLG_EQUATORIAL)[0]
        combust_label = None
        if name != "Sun":
            orb = abs((lon - sun_lon + 180) % 360 - 180)
            if orb <= 8.5:
                combust_label = f"COMBUST ({orb:.1f}°)"
        conds = []
        for tag in pl.get("cond") or []:
            if tag == "combust":
                continue
            conds.append(tag.upper() if tag != "peregrine" else "Peregrine")
        if combust_label:
            conds.append(combust_label)
        if pl.get("retro") and "RETROGRADE" not in conds:
            conds.append("RETROGRADE")
        if not conds:
            conds.append("Peregrine")
        planets.append({
            "name": name, "glyph": GLYPH[name], "abbr": ABBR[name],
            "pos": pos_s.replace(f" {sgn}", f" {sgn}") if False else pos_s,
            "sign": sgn, "deg": round(lon, 2), "house": pl["house"],
            "speed": fmt_speed(xx[3]), "conditions": conds, "retro": bool(xx[3] < 0),
            "decl": fmt_decl(eq[1]),
        })

    extra_rows = []
    for extra_name in ("Chiron", "Node", "America"):
        lon, spd = extras[extra_name]
        pos_s, sgn, _ = fmt_dms(lon)
        house = ((int(((lon % 360) + 1e-6) // 30) - int(ch["asc"] // 30)) % 12) + 1
        if extra_name == "Chiron":
            eq = swe.calc_ut(jd, swe.CHIRON, swe.FLG_SWIEPH | swe.FLG_EQUATORIAL)[0][1]
        elif extra_name == "Node":
            eq = swe.calc_ut(jd, swe.TRUE_NODE, swe.FLG_SWIEPH | swe.FLG_EQUATORIAL)[0][1]
        else:
            eq = None
        extra_rows.append({
            "name": extra_name, "glyph": GLYPH[extra_name], "abbr": ABBR[extra_name],
            "pos": pos_s, "sign": sgn, "deg": round(lon % 360, 2), "house": house,
            "speed": fmt_speed(spd), "conditions": [], "retro": bool(spd < 0),
            "decl": fmt_decl(eq) if eq is not None else "",
        })
        lons[extra_name] = lon

    aspects = []
    names = list(PLANET_ORDER)
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            sep = abs((lons[a] - lons[b] + 180) % 360 - 180)
            for ang, quality in ME.ASPECTS.items():
                if abs(sep - ang) <= WORKBOOK_ORB[ang]:
                    aspects.append({
                        "p1": a, "type": ASPECT_GLYPH[quality], "p2": b,
                        "orb": f"{abs(sep - ang):.1f}°", "quality": quality,
                    })
                    break
    aspects.sort(key=lambda row: float(row["orb"][:-1]))

    chain = ch["dispositor_chain"]
    bits = []
    for name in chain:
        pl = ch["pos"][name]
        bits.append(f"{name} ({SIGN_ABBR[pl['sign']]}/{pl['house']})")
    dispositor = " → ".join(bits)
    if ch["dispositor_loop"]:
        dispositor += " ⟲"

    asc_s, _, _ = fmt_dms(ch["asc"])
    mc_s, _, _ = fmt_dms(ch["mc"])
    date_label = f"{MONTHS[local.month - 1]} {local.day}, {local.year}"
    time_label = f"{utc.strftime('%H:%M:%S')} UTC ({clock_label(local, seconds=True)})"
    rising = ch["asc_sign"]
    role = "governing" if standing == "governing" else "nuance"
    summary = (
        f"{rising} rising, {modality.title()}. "
        + ("Governs the year." if role == "governing" else f"Nested under {year_king(year)}.")
        + " Bones only — no reading."
    )
    verdict = (
        f"Bones only. No reading yet. Chart ruler {ch['chart_ruler']}. "
        f"Dispositor: {dispositor}. "
        f"Greer standing: {standing.replace('_', ' ')}."
    )
    card = {
        "id": chart_id,
        "group": year,
        "role": role,
        "title": f"{year} {sign} Solar Ingress",
        "date": date_label,
        "time": time_label,
        "rising": rising,
        "risingElement": SIGN_ELEMENT[rising],
        "risingModality": modality.title(),
        "validity": validity_line(year, sign, modality, standing),
        "asc": asc_s,
        "ascDeg": round(ch["asc"], 2),
        "mc": mc_s,
        "mcDeg": round(ch["mc"], 2),
        "chartRuler": ch["chart_ruler"],
        "summary": summary,
        "planets": planets + extra_rows,
        "aspects": aspects[:12],
        "dispositorText": dispositor,
        "verdict": verdict,
        "astroGold": False,
        "standing": standing,
        "jd": jd,
        "utc": utc.isoformat(),
        "iso_date": ch["date"],
        "sign": sign,
        "year": year,
    }
    if role == "nuance":
        card["nuanceTo"] = year_king(year)
    overlay = {
        "id": chart_id,
        "title": f"{year} {sign} Solar Ingress",
        "date": date_label,
        "rising": rising,
        "asc_deg": round(ch["asc"], 2),
        "p": {
            name: [round(lons[name], 2), next(p["sign"] for p in planets if p["name"] == name),
                   next(p["house"] for p in planets if p["name"] == name)]
            for name in PLANET_ORDER
        },
    }
    decl = {p["name"]: p["decl"] for p in planets + extra_rows if p.get("decl")}
    return {"card": card, "overlay": overlay, "decl": decl, "engine": ch}


def js_object(value) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2)


def replace_marked(text: str, start: str, end: str, body: str) -> str:
    block = f"{start}\n{body}\n{end}"
    if start in text and end in text:
        return re.sub(
            re.escape(start) + r"[\s\S]*?" + re.escape(end),
            block,
            text,
            count=1,
        )
    return text


def insert_ingress_cards(html: str, cards_js: str) -> str:
    block = f"  {START}\n{cards_js}\n  {END}"
    if START in html:
        return replace_marked(html, START, END, cards_js)
    marker = "    verdict: \"The winter bridge to 2027"
    idx = html.find(marker)
    if idx < 0:
        raise SystemExit("Could not find 2026 Capricorn card to append after")
    close = html.find("\n];", idx)
    if close < 0:
        raise SystemExit("Could not find INGRESS_DATA close")
    return html[:close] + ",\n" + block + html[close:]


def patch_ing_data(html: str, overlays: list[dict]) -> str:
    match = re.search(r"const ING_DATA = (\[.*?\]);", html, re.S)
    if not match:
        raise SystemExit("ING_DATA missing")
    data = json.loads(match.group(1))
    data = [row for row in data if not re.match(r"202[78]-", row["id"])]
    data.extend(overlays)
    compact = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    return html[: match.start(1)] + compact + html[match.end(1) :]


def patch_decl(html: str, decls: dict[str, dict[str, str]]) -> str:
    body = ",\n".join(
        f'  "{cid}": {json.dumps(rows, ensure_ascii=False)}'
        for cid, rows in decls.items()
    )
    block = f"{DECL_START}\n{body}\n{DECL_END}"
    if DECL_START in html:
        return replace_marked(html, DECL_START, DECL_END, body)
    close = html.rfind("};", html.find("const DECL_DATA = {"))
    if close < 0:
        raise SystemExit("DECL_DATA close missing")
    return html[:close] + ",\n" + block + "\n" + html[close:]


def patch_astro_gold_img(html: str) -> str:
    if "chart.astroGold !== false" in html:
        return html
    start = html.find("    // Astro Gold reference screenshot")
    end = html.find("    // Planet Table", start)
    if start < 0 or end < 0:
        raise SystemExit("Astro Gold image block not found")
    original = html[start:end]
    wrapped = (
        "    if (chart.astroGold !== false) {\n"
        + original
        + "    }\n\n"
    )
    return html[:start] + wrapped + html[end:]


def write_bones_note(card: dict) -> Path:
    year, sign = card["year"], card["sign"]
    path = ASTRO / f"{year} {sign} Solar Ingress.md"
    standing = card["standing"]
    rising = card["rising"]
    modality = card["risingModality"]
    utc = datetime.fromisoformat(card["utc"])
    time_utc = utc.strftime("%H:%M:%S")
    role = "governing" if standing == "governing" else "nuance"
    links = ""
    if role == "nuance":
        links = f'governing_chart: "[[{year} Aries Solar Ingress]]"\n'
    lines = [
        "---",
        f'title: "{year} {sign} Solar Ingress — Washington, D.C."',
        "type: chart",
        "chart_type: ingress",
        f"ingress: {sign}",
        f"year: {year}",
        f"date: {card['iso_date']}",
        f'time_utc: "{time_utc}"',
        'location: "Washington, D.C."',
        "house_system: Whole Sign",
        f"rising_sign: {rising}",
        f"rising_modality: {modality}",
        f'validity: "{card["validity"]}"',
        f"chart_ruler: {card['chartRuler']}",
        f"role: {role}",
        f"{links}computed_via: \"Swiss Ephemeris (pyswisseph) · mundane_engine.py\"",
        "reading: none",
        "---",
        "",
        f"# {year} {sign} Solar Ingress — Washington, D.C.",
        "",
        "> **Bones only.** Computed positions and conditions. No reading yet.",
        ">",
        f"> {card['validity']}. Chart ruler {card['chartRuler']}. "
        f"{'Governs the year.' if role == 'governing' else f'Nested under {year} Aries.'}",
        "",
        "---",
        "",
        "## The Chart",
        "",
        f"**Date/Time:** {card['date']}, {card['time']}",
        "**Location:** Washington, D.C. (38.9072°N, 77.0369°W)",
        "**House System:** Whole Sign",
        f"**Ascendant:** {card['asc']}",
        f"**MC:** {card['mc']}",
        f"**Rising Modality:** {modality}",
        f"**Greer standing:** {standing.replace('_', ' ')}",
        "",
        "### Planet Positions",
        "",
        "| Planet | Position | Sign | House | Speed | Condition |",
        "|--------|----------|------|-------|-------|-----------|",
    ]
    for p in card["planets"]:
        cond = ", ".join(p["conditions"]) if p["conditions"] else "—"
        if cond not in ("—", "Peregrine") and "Peregrine" not in cond:
            cond = f"**{cond}**"
        house = p["house"]
        ordinal = {1: "1st", 2: "2nd", 3: "3rd"}.get(house, f"{house}th")
        lines.append(
            f"| {p['name']} | {p['pos']} | {p['sign']} | {ordinal} | {p['speed']}°/d | {cond} |"
        )
    lines += [
        "",
        "### Dispositor chain",
        "",
        card["dispositorText"],
        "",
        "Astro Gold verification is pending. Degrees are engine-computed, never from memory.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> None:
    history_rows = {
        row["id"]: row
        for row in json.loads(HISTORY.read_text(encoding="utf-8"))["charts"]
        if row["chart_type"] == "ingress"
    }
    computed = [compute_chart(year, sign, history_rows) for year in YEARS for sign in CARDINAL]
    cards = [row["card"] for row in computed]
    overlays = [row["overlay"] for row in computed]
    decls = {row["card"]["id"]: row["decl"] for row in computed}

    html = TARGET.read_text(encoding="utf-8")
    cards_js = ",\n".join(js_object(card) for card in cards)
    # Unquote top-level-ish is unnecessary; quoted JSON is valid JS.
    html = insert_ingress_cards(html, cards_js)
    html = patch_ing_data(html, overlays)
    html = patch_decl(html, decls)
    html = patch_astro_gold_img(html)
    TARGET.write_text(html, encoding="utf-8")

    ing = json.loads(ING_JSON.read_text(encoding="utf-8"))
    ing = [row for row in ing if not re.match(r"202[78]-", row["id"])]
    ing.extend(overlays)
    ING_JSON.write_text(json.dumps(ing, ensure_ascii=False) + "\n", encoding="utf-8")

    notes = [write_bones_note(card) for card in cards]
    print(f"✓ Ingress Charts: added {len(cards)} bones-only 2027–2028 charts")
    print(f"✓ ing_data.json: {len(ing)} overlay frames")
    for path in notes:
        print(f"  {path.relative_to(VAULT)}")


if __name__ == "__main__":
    main()
