#!/usr/bin/env python3
"""Astro-Cart-Tography for the Observatory — builds `Cross-cuts/Astro Map.html`.

For each of the 8 cardinal ingress charts (2025–2026), computes apparent
equatorial positions (RA/Dec) for Sun..Pluto + Chiron + True Node + 916 America
and embeds them with the Greenwich sidereal time of the moment. The page's JS
draws the four ACG angle lines per body on an offline equirectangular world map:

  MC  line — vertical at lon = RA − GST            (planet culminates)
  IC  line — MC + 180°                             (planet anti-culminates)
  ASC curve — lon(φ) = RA − arccos(−tanφ·tanδ) − GST   (planet rising)
  DSC curve — lon(φ) = RA + arccos(−tanφ·tanδ) − GST   (planet setting)

Sources:
  - Sun..Pluto, Chiron, True Node: Swiss Ephemeris (FLG_EQUATORIAL, apparent),
    vendored ephe files in `99 - Templates/ephe/` (set via minor_points import).
  - 916 America: JPL Horizons apparent RA/Dec, geocentric, airless — fetched
    2026-06-11 for the exact ingress epochs (swisseph lacks the asteroid file).
    Quantity 2, ANG_FORMAT=DEG. See AMERICA_EQ below.
  - Globe geography: Natural Earth 1:110m admin-0 country GeoJSON, reduced to
    the geometry and label fields used by the renderer and embedded so the
    page is fully offline / local-file: safe.
  - Renderer: pinned Globe.GL 2.46.2, owned in `astro-map-assets/` and copied
    beside the generated view for offline / local-file: operation.

Architecture note: ACG_DATA keeps the reusable group contract across ingresses,
lunations, and timed character charts; the daily sky is stored column-wise to
keep the generated offline page compact enough for the host.

Re-run any time: rewrites the whole HTML (no patch markers to drift).
"""
import json, math, os, re, shutil, sys
from zoneinfo import ZoneInfo
from datetime import datetime, timedelta, timezone

HERE  = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(HERE)
OUT   = os.path.join(VAULT, "04 - Synthesis", "Cross-cuts", "Astro Map.html")
LW    = os.path.join(VAULT, "04 - Synthesis", "Cross-cuts", "Lunar Weather.html")
COUNTRIES = os.path.join(HERE, "astro_map_countries.geojson")
GLOBE_TEMPLATE = os.path.join(HERE, "astro_map_globe_template.html")
ASSET_DIR = os.path.join(HERE, "astro-map-assets")
sys.path.insert(0, HERE)
import minor_points            # sets swe ephe path (Chiron + Swiss files)
import swisseph as swe

SIGNS = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio",
         "Sagittarius","Capricorn","Aquarius","Pisces"]
PL    = {0:"Sun",1:"Moon",2:"Mercury",3:"Venus",4:"Mars",5:"Jupiter",
         6:"Saturn",7:"Uranus",8:"Neptune",9:"Pluto"}
INGRESSES = [(2025,3,0,"2025 Aries"),(2025,6,90,"2025 Cancer"),
             (2025,9,180,"2025 Libra"),(2025,12,270,"2025 Capricorn"),
             (2026,3,0,"2026 Aries"),(2026,6,90,"2026 Cancer"),
             (2026,9,180,"2026 Libra"),(2026,12,270,"2026 Capricorn")]
GOVERNING = {"2025 Aries","2026 Aries","2026 Cancer","2026 Libra"}

# 916 America — JPL Horizons apparent RA/Dec (deg) at the exact ingress epochs.
# Fetched 2026-06-11; geocentric (500@399), airless apparent, equinox of date.
AMERICA_EQ = {
    "2025 Aries":     ( 24.77805,  18.36970),
    "2025 Cancer":    ( 83.62633,  30.25864),
    "2025 Libra":     (134.43974,  23.22277),
    "2025 Capricorn": (156.85836,  14.28754),
    "2026 Aries":     (139.52687,  15.27403),
    "2026 Cancer":    (151.56752,   8.25053),
    "2026 Libra":     (181.52518,  -5.87123),
    "2026 Capricorn": (211.52606, -20.64291),
}

def find_ingress(year, mg, target):
    f = lambda j: ((swe.calc_ut(j,0)[0][0]-target+180)%360)-180
    lo = hi = swe.julday(year, mg, 15, 0.0); hi += 20
    while f(lo) > 0: lo -= 5
    while f(hi) < 0: hi += 5
    for _ in range(50):
        mid = (lo+hi)/2
        if f(mid) < 0: lo = mid
        else: hi = mid
    return (lo+hi)/2

def fmt_lon(l):
    return "%d°%02d' %s" % (int(l%30), int((l%1)*60), SIGNS[int(l//30)])

def local_str(jd):
    y,m,d,h = swe.revjul(jd)
    ut = datetime(y,m,d, tzinfo=timezone.utc) + timedelta(hours=h)
    loc = ut.astimezone(ZoneInfo("America/New_York"))
    return loc.strftime("%m/%d/%Y · %-I:%M %p %Z") + ut.strftime(" (%H:%M UT)")

# ---- 916 America RA/Dec cache (JPL Horizons; see america_eq_grid.json) ----
_EQG = json.load(open(os.path.join(HERE, "america_eq_grid.json")))
_un = [_EQG["ra"][0]]
for _x in _EQG["ra"][1:]:
    _d = (_x - _un[-1] + 180) % 360 - 180
    _un.append(_un[-1] + _d)
_g0 = [int(v) for v in _EQG["grid_start"].split("-")]
_EQG_JD0 = swe.julday(_g0[0], _g0[1], _g0[2], 0.0)

def america_eq_at(jd):
    """Daily-grid linear interpolation (apparent RA/Dec). Grid 2024→2028-01-03."""
    i = (jd - _EQG_JD0) / _EQG["step_days"]
    if i < -0.01 or i > len(_un) - 0.99:
        raise ValueError(f"jd {jd} outside america_eq_grid")
    lo = max(0, min(len(_un) - 2, int(i))); f = i - lo
    ra  = (_un[lo] + (_un[lo+1] - _un[lo]) * f) % 360
    dec = _EQG["dec"][lo] + (_EQG["dec"][lo+1] - _EQG["dec"][lo]) * f
    return round(ra, 5), round(dec, 5)

def bodies_at(jd, america):
    """Common body table. `america` = (ra, dec, ecl_lon_for_label, retro)."""
    bodies = {}
    EQ = swe.FLG_SWIEPH | swe.FLG_EQUATORIAL
    for p in sorted(PL):
        eq = swe.calc_ut(jd, p, EQ)[0]
        ec = swe.calc_ut(jd, p)[0]
        bodies[PL[p]] = {"ra":round(eq[0],5), "dec":round(eq[1],5),
                         "pos":fmt_lon(ec[0]), "rx":1 if ec[3]<0 else 0}
    for pid, nm in ((swe.CHIRON,"Chiron"), (swe.TRUE_NODE,"Node")):
        eq = swe.calc_ut(jd, pid, EQ)[0]
        ec = swe.calc_ut(jd, pid)[0]
        bodies[nm] = {"ra":round(eq[0],5), "dec":round(eq[1],5),
                      "pos":fmt_lon(ec[0]), "rx":1 if ec[3]<0 else 0}
    ra, dec, lon, rx = america
    bodies["America"] = {"ra":round(ra,5), "dec":round(dec,5),
                         "pos":fmt_lon(lon), "rx":1 if rx else 0}
    return bodies

def astrocartography_longitudes(ra, dec, gst, lat):
    """Return MC/IC/ASC/DSC longitudes for one apparent RA/Dec position.

    ASC/DSC are None at circumpolar latitudes where the body does not cross
    the horizon. Longitudes are normalized to [-180, 180).
    """
    norm = lambda value: ((value + 180.0) % 360.0) - 180.0
    mc = norm(ra - gst)
    ic = norm(mc + 180.0)
    horizon_term = -math.tan(math.radians(lat)) * math.tan(math.radians(dec))
    if horizon_term < -1.0 or horizon_term > 1.0:
        return {"MC": mc, "IC": ic, "As": None, "Ds": None}
    hour_angle = math.degrees(math.acos(horizon_term))
    return {
        "MC": mc,
        "IC": ic,
        "As": norm(ra - hour_angle - gst),
        "Ds": norm(ra + hour_angle - gst),
    }

def geometry_checks(charts):
    """Python-owned check vectors consumed by the browser renderer at boot."""
    samples = []
    chart = next(c for c in charts if c["id"] == "2026-cancer")
    for body, lat in (("Sun", 0.0), ("Moon", 38.9072), ("Saturn", -33.8688)):
        b = chart["bodies"][body]
        expected = astrocartography_longitudes(b["ra"], b["dec"], chart["gst"], lat)
        samples.append({
            "chart": chart["id"], "body": body, "lat": lat,
            "expected": {key: None if value is None else round(value, 6)
                         for key, value in expected.items()},
        })
    return samples

def chart_for(name):
    y, mg, t = [(a,b,c) for a,b,c,n in INGRESSES if n == name][0]
    jd  = find_ingress(y, mg, t)
    gst = (swe.sidtime(jd) * 15.0) % 360.0
    ra, dec = AMERICA_EQ[name]            # exact Horizons values for the ingresses
    bodies = bodies_at(jd, (ra, dec, minor_points.america_lon(jd),
                            minor_points.america_speed(jd) < 0))
    return {"id": name.lower().replace(" ","-"), "title": name + " Ingress",
            "date": local_str(jd), "jd": round(jd,5), "gst": round(gst,5),
            "gov": 1 if name in GOVERNING else 0, "bodies": bodies}

PHASES = ["New Moon","First Quarter","Full Moon","Last Quarter"]

def lunation_charts():
    html = open(LW, encoding="utf-8").read()
    luns = {}
    # New Moons carry "sign"; quarters/fulls carry "moon_sign" — parse the record
    # head, then sniff the next ~300 chars for the variant fields.
    head = (r'\{"type":"(New Moon|First Quarter|Full Moon|Last Quarter)",'
            r'"date":"(\d{4}-\d{2}-\d{2})","time_utc":"(\d{2}):(\d{2})"')
    for m in re.finditer(head, html):
        typ, date, hh, mm = m.groups()
        tail = html[m.end():m.end()+320]
        sg  = re.search(r'"(?:moon_)?sign":"(\w+)"', tail)
        dg  = re.search(r'"degree":([\d.]+)', tail)
        ec  = re.search(r'"eclipse":(true|false)', tail)
        if not (sg and dg and ec):
            raise SystemExit(f"lunation parse failed at {date} — Lunar Weather format changed?")
        luns[date] = (typ, int(hh), int(mm), sg.group(1), float(dg.group(1)), ec.group(1) == "true")
    charts = []
    for date, (typ, hh, mm, msign, deg, ecl) in sorted(luns.items()):
        y, mo, dd = (int(x) for x in date.split("-"))
        jd = swe.julday(y, mo, dd, hh + mm/60.0)
        gst = (swe.sidtime(jd) * 15.0) % 360.0
        ra, dec = america_eq_at(jd)
        bodies = bodies_at(jd, (ra, dec, minor_points.america_lon(jd),
                                minor_points.america_speed(jd) < 0))
        charts.append({"id":"lun-"+date, "title":typ+" — "+str(int(round(deg)))+"° "+msign,
                       "date":local_str(jd), "jd":round(jd,5), "gst":round(gst,5),
                       "gov":0, "kind":"lun", "ph":PHASES.index(typ), "ecl":1 if ecl else 0,
                       "y":y, "mo":mo, "dd":dd, "bodies":bodies})
    return charts

BODY_ORDER = ["Sun","Moon","Mercury","Venus","Mars","Jupiter","Saturn",
              "Uranus","Neptune","Pluto","Chiron","Node","America"]

def daily_sky():
    """Per-day equatorial positions, midnight UT (Katie's Almanac convention),
    2025-01-01 → 2027-12-31. Compact parallel arrays; lines drawn client-side."""
    from datetime import date as D, timedelta as TD
    d0, d1 = D(2025,1,1), D(2027,12,31)
    n = (d1 - d0).days + 1
    gst = []
    B = {name: {"ra": [], "dec": []} for name in BODY_ORDER}
    EQ = swe.FLG_SWIEPH | swe.FLG_EQUATORIAL
    for i in range(n):
        d = d0 + TD(days=i)
        jd = swe.julday(d.year, d.month, d.day, 0.0)
        gst.append(round((swe.sidtime(jd) * 15.0) % 360.0, 4))
        for p in sorted(PL):
            eq = swe.calc_ut(jd, p, EQ)[0]
            B[PL[p]]["ra"].append(round(eq[0], 4)); B[PL[p]]["dec"].append(round(eq[1], 4))
        for pid, nm in ((swe.CHIRON, "Chiron"), (swe.TRUE_NODE, "Node")):
            eq = swe.calc_ut(jd, pid, EQ)[0]
            B[nm]["ra"].append(round(eq[0], 4)); B[nm]["dec"].append(round(eq[1], 4))
        ra, dec = america_eq_at(jd)                 # grid is daily-midnight → exact
        B["America"]["ra"].append(round(ra, 4)); B["America"]["dec"].append(round(dec, 4))
    return {"start": "2025-01-01", "n": n, "gst": gst, "bodies": B}

def eclipse_layers(luns):
    """Real shadow geography for the eclipse lunations.

    Solar (New Moon): central path sampled from swe.sol_eclipse_where between
    the center-line begin/end times (tret[6]/tret[7]); partials get the
    greatest-eclipse point only. Lunar (Full Moon): the sub-lunar point at
    maximum — the Moon stands overhead there; the whole night side sees it.
    """
    out = {}
    for c in luns:
        if not c["ecl"]:
            continue
        jd = c["jd"]
        if c["ph"] == 0:                                    # solar
            try:
                retflag, tret = swe.sol_eclipse_when_glob(jd - 2)
            except Exception:
                continue
            tmax = tret[0]
            if abs(tmax - jd) > 3:
                continue                                    # found a different eclipse
            kind = ("total"   if retflag & swe.ECL_TOTAL else
                    "annular" if retflag & swe.ECL_ANNULAR else
                    "hybrid"  if retflag & swe.ECL_ANNULAR_TOTAL else "partial")
            path = []
            t0, t1 = tret[6], tret[7]                       # center line begin/end
            if t0 and t1 and t1 > t0:
                N = 160
                for i in range(N + 1):
                    t = t0 + (t1 - t0) * i / N
                    try:
                        rf, geo, attr = swe.sol_eclipse_where(t)
                    except Exception:
                        continue
                    if rf & (swe.ECL_TOTAL | swe.ECL_ANNULAR | swe.ECL_ANNULAR_TOTAL):
                        path.append([round(geo[1], 2), round(geo[0], 2)])   # [lat, lon]
            rf, geo, attr = swe.sol_eclipse_where(tmax)
            out[c["id"]] = {"kind": kind, "solar": 1, "path": path,
                            "max": [round(geo[1], 2), round(geo[0], 2)]}
        else:                                               # lunar
            try:
                retflag, tret = swe.lun_eclipse_when(jd - 2)
            except Exception:
                continue
            tmax = tret[0]
            if abs(tmax - jd) > 3:
                continue
            kind = ("total lunar"   if retflag & swe.ECL_TOTAL else
                    "partial lunar" if retflag & swe.ECL_PARTIAL else "penumbral lunar")
            eq  = swe.calc_ut(tmax, 1, swe.FLG_SWIEPH | swe.FLG_EQUATORIAL)[0]
            gst = (swe.sidtime(tmax) * 15.0) % 360.0
            lon = ((eq[0] - gst + 180) % 360) - 180
            out[c["id"]] = {"kind": kind, "solar": 0, "path": [],
                            "max": [round(eq[1], 2), round(lon, 2)]}
    return out

def character_charts():
    cast = json.load(open(os.path.join(HERE, "characters_data.json")))["cast"]
    charts = []
    for c in cast:
        if not c.get("time_known"):          # Katie's call: timed charts only —
            continue                          # untimed MC lines swing 15°/hour
        hh, mm = (int(x) for x in c["time"].split(":"))
        y, mo, dd = (int(x) for x in c["date"].split("-"))
        loc = datetime(y, mo, dd, hh, mm, tzinfo=ZoneInfo(c["tz"]))
        ut  = loc.astimezone(timezone.utc)
        jd  = swe.julday(ut.year, ut.month, ut.day,
                         ut.hour + ut.minute/60.0 + ut.second/3600.0)
        gst = (swe.sidtime(jd) * 15.0) % 360.0
        ra, dec = _EQG["natal"][c["slug"]]
        bodies = bodies_at(jd, (ra, dec, minor_points.america_natal(c["slug"]), 0))
        sub = c["date"][5:7]+"/"+c["date"][8:10]+"/"+c["date"][0:4]+" "+c["time"]+" · "+c["place"]+" · Rodden "+c["rodden"]
        if c.get("asc_override"): sub += " · Katie's rectification"
        charts.append({"id":"char-"+c["slug"], "title":c["name"],
                       "date":sub, "jd":round(jd,5), "gst":round(gst,5),
                       "gov":0, "kind":"chr", "grp":c["group"], "bodies":bodies})
    return charts

CITIES = [
    # [name, lat, lon, major?]  major=1 always labeled at any zoom
    ["Washington D.C.",38.9072,-77.0369,2],["New York",40.71,-74.01,1],["Los Angeles",34.05,-118.24,1],
    ["Chicago",41.88,-87.63,0],["Houston",29.76,-95.37,0],["Miami",25.76,-80.19,0],["Seattle",47.61,-122.33,0],
    ["Denver",39.74,-104.99,0],["San Francisco",37.77,-122.42,0],["Anchorage",61.22,-149.90,0],
    ["Toronto",43.65,-79.38,0],["Ottawa",45.42,-75.70,0],["Vancouver",49.28,-123.12,0],
    ["Mexico City",19.43,-99.13,1],["Havana",23.11,-82.37,0],["Panama City",8.98,-79.52,0],
    ["Bogotá",4.71,-74.07,0],["Caracas",10.48,-66.90,0],["Lima",-12.05,-77.04,0],["Quito",-0.18,-78.47,0],
    ["São Paulo",-23.55,-46.63,1],["Rio de Janeiro",-22.91,-43.17,0],["Brasília",-15.79,-47.88,0],
    ["Buenos Aires",-34.60,-58.38,1],["Santiago",-33.45,-70.67,0],
    ["Reykjavík",64.15,-21.94,0],["Nuuk",64.18,-51.72,0],["Dublin",53.35,-6.26,0],
    ["London",51.51,-0.13,1],["Paris",48.86,2.35,1],["Madrid",40.42,-3.70,0],["Lisbon",38.72,-9.14,0],
    ["Berlin",52.52,13.40,1],["Rome",41.90,12.50,0],["Vienna",48.21,16.37,0],["Geneva",46.20,6.14,0],
    ["Brussels",50.85,4.35,0],["Amsterdam",52.37,4.90,0],["Oslo",59.91,10.75,0],["Stockholm",59.33,18.07,0],
    ["Copenhagen",55.68,12.57,0],["Warsaw",52.23,21.01,0],["Kyiv",50.45,30.52,1],["Minsk",53.90,27.57,0],
    ["Moscow",55.76,37.62,1],["Saint Petersburg",59.93,30.34,0],["Istanbul",41.01,28.98,1],
    ["Ankara",39.93,32.86,0],["Athens",37.98,23.73,0],["Bucharest",44.43,26.10,0],["Belgrade",44.79,20.45,0],
    ["Tbilisi",41.72,44.79,0],["Yerevan",40.18,44.51,0],["Baku",40.41,49.87,0],
    ["Jerusalem",31.77,35.21,1],["Tel Aviv",32.07,34.78,0],["Beirut",33.89,35.50,0],["Damascus",33.51,36.29,0],
    ["Amman",31.95,35.93,0],["Cairo",30.04,31.24,1],["Baghdad",33.31,44.36,1],["Kuwait City",29.38,47.99,0],
    ["Riyadh",24.71,46.68,1],["Jeddah",21.49,39.19,0],["Doha",25.29,51.53,0],["Dubai",25.20,55.27,0],
    ["Abu Dhabi",24.45,54.38,0],["Muscat",23.59,58.41,0],["Sanaa",15.35,44.21,0],
    ["Tehran",35.69,51.39,1],["Isfahan",32.65,51.67,0],["Mashhad",36.30,59.61,0],["Shiraz",29.59,52.58,0],
    ["Kabul",34.56,69.21,0],["Islamabad",33.68,73.05,0],["Karachi",24.86,67.01,0],["Lahore",31.55,74.34,0],
    ["New Delhi",28.61,77.21,1],["Mumbai",19.08,72.88,1],["Bengaluru",12.97,77.59,0],["Kolkata",22.57,88.36,0],
    ["Colombo",6.93,79.86,0],["Dhaka",23.81,90.41,0],["Kathmandu",27.71,85.32,0],
    ["Tashkent",41.30,69.24,0],["Almaty",43.24,76.89,0],["Astana",51.17,71.43,0],["Ulaanbaatar",47.89,106.91,0],
    ["Beijing",39.90,116.41,1],["Shanghai",31.23,121.47,1],["Hong Kong",22.32,114.17,0],["Taipei",25.03,121.57,1],
    ["Chongqing",29.56,106.55,0],["Ürümqi",43.83,87.62,0],["Lhasa",29.65,91.10,0],
    ["Seoul",37.57,126.98,1],["Pyongyang",39.04,125.76,0],["Tokyo",35.68,139.69,1],["Osaka",34.69,135.50,0],
    ["Vladivostok",43.12,131.89,0],["Novosibirsk",55.01,82.94,0],["Yekaterinburg",56.84,60.61,0],
    ["Hanoi",21.03,105.85,0],["Bangkok",13.76,100.50,1],["Yangon",16.87,96.20,0],["Phnom Penh",11.56,104.92,0],
    ["Kuala Lumpur",3.14,101.69,0],["Singapore",1.35,103.82,1],["Jakarta",-6.21,106.85,1],["Manila",14.60,120.98,1],
    ["Rabat",34.02,-6.84,0],["Algiers",36.75,3.06,0],["Tunis",36.81,10.18,0],["Tripoli",32.89,13.19,0],
    ["Tamanrasset",22.79,5.53,0],["Nouakchott",18.08,-15.98,0],["Dakar",14.72,-17.47,0],["Bamako",12.64,-8.00,0],
    ["Niamey",13.51,2.13,0],["Khartoum",15.50,32.56,0],["Addis Ababa",9.03,38.74,0],["Mogadishu",2.05,45.32,0],
    ["Nairobi",-1.29,36.82,1],["Kampala",0.35,32.58,0],["Kinshasa",-4.44,15.27,0],["Lagos",6.52,3.38,1],
    ["Abuja",9.06,7.49,0],["Accra",5.60,-0.19,0],["Luanda",-8.84,13.23,0],["Lusaka",-15.39,28.32,0],
    ["Harare",-17.83,31.05,0],["Johannesburg",-26.20,28.05,1],["Cape Town",-33.92,18.42,0],
    ["Perth",-31.95,115.86,0],["Adelaide",-34.93,138.60,0],["Melbourne",-37.81,144.96,1],
    ["Sydney",-33.87,151.21,1],["Brisbane",-27.47,153.03,0],["Townsville",-19.26,146.82,0],
    ["Darwin",-12.46,130.84,0],["Hobart",-42.88,147.33,0],["Auckland",-36.85,174.76,0],["Wellington",-41.29,174.78,0],
    ["Honolulu",21.31,-157.86,0],["Suva",-18.14,178.44,0],
]

def main():
    charts = [chart_for(n) for _,_,_,n in INGRESSES]
    luns   = lunation_charts()
    chars  = character_charts()
    eclp   = eclipse_layers(luns)
    days   = daily_sky()
    print(f"charts: {len(charts)} ingresses, {len(luns)} lunations, {len(chars)} characters (timed only), "
          f"{len(eclp)} eclipse layers, {days['n']} daily skies")
    country_source = json.load(open(COUNTRIES, encoding="utf-8"))
    countries = {"type": "FeatureCollection", "features": []}
    for source_feature in country_source["features"]:
        props = source_feature["properties"]
        countries["features"].append({
            "type": "Feature",
            "properties": {
                "name": props.get("NAME_EN") or props.get("ADMIN") or props.get("NAME"),
                "label_x": props.get("LABEL_X"),
                "label_y": props.get("LABEL_Y"),
                "labelrank": props.get("LABELRANK", 99),
                "min_zoom": props.get("MIN_ZOOM", 0),
                "tiny": props.get("TINY", -99),
            },
            "geometry": source_feature["geometry"],
        })

    # reuse the wheel engine's hand-drawn glyph paths + planet colors
    wl  = open(os.path.join(HERE, "wheel_lib.py")).read()
    i   = wl.find("const GLY={");  j = wl.find("};", i)
    GLY = wl[i:j+2]
    i   = wl.find("const PCOL={"); j = wl.find("}", i)
    PCOL= wl[i:j+1] + ";"

    acg = {"groups":[{"id":"ingresses","label":"Ingresses","charts":charts},
                     {"id":"lunations","label":"Lunations","charts":luns},
                     {"id":"characters","label":"Characters","charts":chars}],
           "geometry_checks": geometry_checks(charts)}

    html = open(GLOBE_TEMPLATE, encoding="utf-8").read()
    html = html.replace("%%ACG%%",    json.dumps(acg, separators=(",",":")))
    html = html.replace("%%COUNTRIES%%", json.dumps(countries, separators=(",",":")))
    html = html.replace("%%ECLP%%",   json.dumps(eclp, separators=(",",":")))
    html = html.replace("%%DAYS%%",   json.dumps(days, separators=(",",":")))
    html = html.replace("%%CITIES%%", json.dumps(CITIES, separators=(",",":")))
    html = html.replace("%%GLY%%",    GLY)
    html = html.replace("%%PCOL%%",   PCOL)
    chart_images = os.path.join(os.path.dirname(OUT), "chart-images")
    os.makedirs(chart_images, exist_ok=True)
    for asset in ("globe.gl.min.js", "globe.gl.LICENSE", "earth-topology.png"):
        shutil.copy2(os.path.join(ASSET_DIR, asset), os.path.join(chart_images, asset))
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote", OUT, "—", len(html)//1024, "KB,",
          len(charts)+len(luns)+len(chars), "charts total")

TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Astro Map — Freedom 250</title>
<style>
:root{--paper:#faf8f3;--paper2:#f3efe6;--card:#fffdf8;--ink:#2b2620;--ink2:#5a5246;
--faint:#8a8174;--line:#e2dccd;--accent:#8c6d1f;--ocean:#e9eef0;--landfill:#f1ecdf;--coast:#b8ad97}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);
font-family:Georgia,'Times New Roman',serif}
.hdr{text-align:center;padding:14px 16px 6px}
.hdr h1{font-size:21px;margin:0 0 2px;letter-spacing:.3px}
.hdr .sub{font-size:12px;color:var(--faint);font-style:italic}
.bar{display:flex;flex-wrap:wrap;justify-content:center;gap:6px;padding:8px 12px 4px}
.chip{padding:5px 12px;font-size:12.5px;cursor:pointer;border:1px solid var(--line);
border-radius:14px;background:var(--card);color:var(--ink2);font-family:inherit}
.chip:hover{border-color:var(--accent)}
.chip.on{background:var(--accent);border-color:var(--accent);color:#fffdf8;font-weight:700}
.chip .gv{font-size:9px;letter-spacing:.5px;opacity:.75;margin-left:4px;font-style:italic}
.ctl{display:flex;flex-wrap:wrap;justify-content:center;gap:4px;padding:2px 12px 6px;align-items:center}
.pchip{display:inline-flex;align-items:center;gap:3px;padding:2px 7px;font-size:11px;cursor:pointer;
border:1px solid var(--line);border-radius:11px;background:var(--card);color:var(--ink2);user-select:none}
.pchip.off{opacity:.32}
.pchip svg{display:block}
.achip{padding:2px 9px;font-size:11px;cursor:pointer;border:1px solid var(--line);border-radius:11px;
background:var(--card);color:var(--ink2);user-select:none}
.achip.off{opacity:.32}
.sep{width:1px;height:16px;background:var(--line);margin:0 5px}
.mapwrap{position:relative;margin:4px auto 8px;max-width:1500px;padding:0 10px}
#stage{position:relative;border:1px solid var(--line);border-radius:6px;overflow:hidden;background:var(--ocean)}
#map{display:block;width:100%;height:auto;cursor:grab}
#map.panning{cursor:grabbing}
#gutter{position:absolute;left:0;top:0;width:100%;height:24px;pointer-events:none;overflow:visible}
#tip{position:absolute;display:none;pointer-events:none;background:var(--card);border:1px solid var(--accent);
border-radius:6px;padding:7px 10px;font-size:12px;max-width:280px;box-shadow:0 2px 10px rgba(60,50,30,.18);z-index:5}
#tip .t1{font-weight:700}
#tip .t2{color:var(--ink2);font-size:11.5px;margin-top:2px}
#tip .t3{color:var(--faint);font-size:11px;font-style:italic;margin-top:3px}
#panel{position:absolute;right:14px;top:30px;width:265px;max-height:78%;overflow:auto;display:none;
background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 12px;font-size:12px;
box-shadow:0 3px 14px rgba(60,50,30,.16);z-index:6}
#panel h3{margin:0 0 2px;font-size:13px}
#panel .ph{color:var(--faint);font-size:11px;font-style:italic;margin-bottom:7px}
#panel .row{display:flex;align-items:baseline;gap:6px;padding:3px 0;border-top:1px dashed var(--line)}
#panel .row b{font-size:12.5px}
#panel .row .o{margin-left:auto;color:var(--faint);font-size:11px;white-space:nowrap}
#panel .mn{color:var(--ink2);font-size:11px;font-style:italic;margin:-1px 0 2px 0}
#panel .x{position:absolute;top:6px;right:9px;cursor:pointer;color:var(--faint);font-size:14px}
.legend{text-align:center;font-size:11px;color:var(--faint);padding:0 14px 12px;font-style:italic}
.legend .sw{display:inline-block;width:26px;height:0;border-top:2px solid var(--ink2);vertical-align:middle;margin:0 4px 2px 10px}
.legend .d1{border-top-style:dashed}
.legend .d2{border-top-style:dotted}
.zoomui{position:absolute;right:10px;bottom:10px;display:flex;flex-direction:column;gap:4px;z-index:4}
.zoomui button{width:26px;height:26px;border:1px solid var(--line);background:var(--card);color:var(--ink);
border-radius:5px;cursor:pointer;font-size:15px;line-height:1}
.note{font-size:10.5px}
/* satellite imagery must stay true-color under the Observatory dark-mode invert */
html[data-theme="dark"] #map image{filter:invert(1) hue-rotate(180deg)}
</style>
</head>
<body>
<div class="hdr">
  <h1>Astro-Cart-Tography</h1>
  <div class="sub" id="sub">Where each planet of the moment culminates, roots, rises and sets — the chart laid over the Earth itself</div>
</div>
<div class="bar" id="chartbar"></div>
<div class="ctl" id="pbar"></div>
<div class="ctl" id="abar"></div>
<div class="mapwrap">
  <div id="stage">
    <svg id="map" xmlns="http://www.w3.org/2000/svg"></svg>
    <svg id="gutter" xmlns="http://www.w3.org/2000/svg"></svg>
    <div id="tip"></div>
    <div id="panel"></div>
    <div class="zoomui">
      <button id="zin" title="Zoom in">+</button>
      <button id="zout" title="Zoom out">−</button>
      <button id="zfit" title="Reset" style="font-size:11px">⤢</button>
    </div>
  </div>
</div>
<div class="legend">
  <b>MC</b> culminates<span class="sw"></span> · <b>IC</b> anti-culminates<span class="sw d1"></span> ·
  <b>As</b> rises<span class="sw"></span> · <b>Ds</b> sets<span class="sw d2"></span>
  &nbsp;|&nbsp; small dot = planet exactly overhead &nbsp;|&nbsp; ★ = Washington D.C. (where the mundane charts are cast — the lines themselves are global)
  <div class="note">Click anywhere on the map to read the lines over that spot · drag to pan · scroll to zoom ·
  satellite ↔ parchment style toggle above · Swiss Ephemeris (916 America: JPL Horizons) ·
  NASA Blue Marble + Natural Earth borders, fully offline · equirectangular</div>
</div>
<script>
const ACG=%%ACG%%;
const LAND=%%LAND%%;
const BORDERS=%%BORDERS%%;
const CITIES=%%CITIES%%;
const EARTH_IMG="chart-images/earth-blue-marble.jpg";   // NASA Blue Marble, bundled — no internet needed
const ECLP=%%ECLP%%;   // eclipse shadow geography (solar central paths, lunar sub-lunar points)
const DAYS=%%DAYS%%;   // per-day RA/Dec + GST, midnight UT, 2025-01-01 → 2027-12-31
%%GLY%%
%%PCOL%%
const ORDER=["Sun","Moon","Mercury","Venus","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto","Chiron","Node","America"];
const PMEAN={Sun:"sovereignty — the leader, the state itself",Moon:"the public — crowds, mood, the home front",
Mercury:"the word — press, trade, transport",Venus:"diplomacy — treaties, treasury, culture",
Mars:"the military — strikes, conflict, fire",Jupiter:"expansion — law, courts, faith, plenty",
Saturn:"contraction — borders, tests, the establishment",Uranus:"shock — revolt, sudden breaks, technology",
Neptune:"dissolution — ideology, oil and seas, deception",Pluto:"deep power — purges, the underworld, rebirth",
Chiron:"the wound — where it aches and teaches",Node:"collective destiny — the meeting point",
America:"the American thread itself"};
const AMEAN={MC:"culminates here — out on the world stage",IC:"runs underground here — roots, land, the base",
As:"rises here — arrives in body and name",Ds:"sets here — met in others, allies and enemies"};
const D2R=Math.PI/180,R2D=180/Math.PI;
const W=1440,H=720,PXD=4;            // 4 px per degree
const xOf=lon=>(lon+180)*PXD, yOf=lat=>(90-lat)*PXD;
const lonOfX=x=>x/PXD-180, latOfY=y=>90-y/PXD;
const n180=a=>{a=(a+180)%360; if(a<0)a+=360; return a-180;};
function f1(v){return Math.round(v*10)/10}

// ---------- line math ----------
function linesFor(b,gst){
  const mc=n180(b.ra-gst), ic=n180(mc+180), asc=[], dsc=[];
  for(let lat=-88;lat<=88;lat+=0.5){
    const t=-Math.tan(lat*D2R)*Math.tan(b.dec*D2R);
    if(t<-1||t>1) continue;
    const h=Math.acos(t)*R2D;
    asc.push([lat,n180(b.ra-h-gst)]);
    dsc.push([lat,n180(b.ra+h-gst)]);
  }
  return {mc:mc,ic:ic,asc:asc,dsc:dsc};
}
function polyPath(pts){ // split on antimeridian wrap
  let d="",prev=null;
  pts.forEach(p=>{
    const x=xOf(p[1]),y=yOf(p[0]);
    if(prev!==null&&Math.abs(p[1]-prev)>180)d+="M"+f1(x)+" "+f1(y);
    else d+=(d===""?"M":"L")+f1(x)+" "+f1(y);
    prev=p[1];
  });
  return d;
}
function curveLonAt(b,gst,lat,which){ // exact lon of asc/dsc at a latitude, or null
  const t=-Math.tan(lat*D2R)*Math.tan(b.dec*D2R);
  if(t<-1||t>1)return null;
  const h=Math.acos(t)*R2D;
  return n180(which==="As"?b.ra-h-gst:b.ra+h-gst);
}

// ---------- state ----------
const ALLCHARTS=ACG.groups.flatMap(g=>g.charts);
// ---- Daily Sky: charts built on the fly from the DAYS arrays ----
const SIGNS=["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"];
const OBLIQ=23.4365*Math.PI/180;       // mean obliquity (label use only; lines use RA/Dec exactly)
const dayCache={};
function dayIndex(ds){
  const p=ds.split("-").map(Number);
  return Math.round((Date.UTC(p[0],p[1]-1,p[2])-Date.UTC(2025,0,1))/86400000);
}
function dsOf(i){
  const t=new Date(Date.UTC(2025,0,1)+i*86400000);
  return t.getUTCFullYear()+"-"+String(t.getUTCMonth()+1).padStart(2,"0")+"-"+String(t.getUTCDate()).padStart(2,"0");
}
function dayChart(ds){
  if(dayCache[ds])return dayCache[ds];
  const i=dayIndex(ds);
  if(i<0||i>=DAYS.n)return null;
  const bodies={};
  ORDER.forEach(p=>{
    const A=DAYS.bodies[p], ra=A.ra[i], dec=A.dec[i];
    const lon=(Math.atan2(Math.sin(ra*Math.PI/180)*Math.cos(OBLIQ)+Math.tan(dec*Math.PI/180)*Math.sin(OBLIQ),Math.cos(ra*Math.PI/180))*180/Math.PI+360)%360;
    const pos=Math.floor(lon%30)+"°"+String(Math.floor((lon%1)*60)).padStart(2,"0")+"' "+SIGNS[Math.floor(lon/30)];
    const i0=Math.max(0,i-1),i1=Math.min(DAYS.n-1,i+1);
    const dr=((A.ra[i1]-A.ra[i0]+540)%360)-180;
    bodies[p]={ra:ra,dec:dec,pos:pos,rx:(dr<0&&p!=="Sun"&&p!=="Moon"&&p!=="Node")?1:0};
  });
  const p=ds.split("-");
  const c={id:"day-"+ds,title:"The Sky — "+p[1]+"/"+p[2]+"/"+p[0],
    date:"midnight UT positions (Almanac convention) · the Moon shifts ~13°/day",
    gst:DAYS.gst[i],gov:0,kind:"day",ds:ds,bodies:bodies};
  dayCache[ds]=c;return c;
}
function todayDS(){  // LOCAL date, clamped to the DAYS span — never toISOString
  const d=new Date();
  const ds=d.getFullYear()+"-"+String(d.getMonth()+1).padStart(2,"0")+"-"+String(d.getDate()).padStart(2,"0");
  const i=Math.max(0,Math.min(DAYS.n-1,dayIndex(ds)));
  return dsOf(i);
}
const byId=id=>id&&id.indexOf("day-")===0?dayChart(id.slice(4)):ALLCHARTS.find(c=>c.id===id);
const GRP={ing:ACG.groups[0],lun:ACG.groups[1],chr:ACG.groups[2]};
let mode="ing";
let chart=GRP.ing.charts[0];
let OV=null;                 // overlay chart (synastry on Earth) or null
const PH_G=["●","◐","○","◑"];  // New / First Quarter / Full / Last Quarter
// lunation picker state — nearest to TODAY by LOCAL date (never toISOString)
const _now=new Date();
let lunY=_now.getFullYear(), lunM=_now.getMonth()+1;
function nearestLun(){
  const t=new Date(_now.getFullYear(),_now.getMonth(),_now.getDate()).getTime();
  let best=null,bd=1e18;
  GRP.lun.charts.forEach(c=>{
    const d=Math.abs(new Date(c.y,c.mo-1,c.dd).getTime()-t);
    if(d<bd){bd=d;best=c;}
  });
  return best;
}
const pOn={}, aOn={MC:true,IC:true,As:true,Ds:true};
ORDER.forEach(p=>pOn[p]=true);
let k=1,tx=0,ty=0;    // zoom + pan (screen px of the unscaled W×H space)
const MAXK=9;
let eclOn=true;       // eclipse shadow layer (only renders on eclipse lunations)
let STYLE="sat";      // "sat" (Blue Marble) | "parchment"
try{STYLE=localStorage.getItem("f250-am-style")||"sat";}catch(_){}

// ---------- chrome ----------
function glyphSVG(name,size,color){
  return '<svg width="'+size+'" height="'+size+'" viewBox="0 0 20 20"><g color="'+color+
  '" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" fill="none">'+(GLY[name]||"")+"</g></svg>";
}
function setChart(c){chart=c;buildBars();draw();}
function buildBars(){
  const cb=document.getElementById("chartbar");
  cb.innerHTML="";
  // --- mode switcher ---
  [["ing","Ingresses"],["lun","Lunations"],["chr","Characters"],["day","Daily Sky"]].forEach(mm=>{
    const b=document.createElement("button");
    b.className="chip mode"+(mode===mm[0]?" on":"");
    b.textContent=mm[1];
    b.onclick=()=>{
      mode=mm[0];
      if(mode==="ing"&&chart.kind)chart=GRP.ing.charts[0];
      if(mode==="lun"&&chart.kind!=="lun"){const n=nearestLun();if(n){chart=n;lunY=n.y;lunM=n.mo;}}
      if(mode==="chr"&&chart.kind!=="chr")chart=GRP.chr.charts[0];
      if(mode==="day"&&chart.kind!=="day")chart=dayChart(todayDS());
      buildBars();draw();
    };
    cb.appendChild(b);
  });
  const sep=document.createElement("span");sep.className="sep";cb.appendChild(sep);
  if(mode==="ing"){
    GRP.ing.charts.forEach(c=>{
      const b=document.createElement("button");
      b.className="chip"+(c.id===chart.id?" on":"");
      b.innerHTML=c.title.replace(" Ingress","")+(c.gov?'<span class="gv">GOV</span>':"");
      b.onclick=()=>setChart(c);
      cb.appendChild(b);
    });
  }else if(mode==="lun"){
    // year chips
    [...new Set(GRP.lun.charts.map(c=>c.y))].forEach(y=>{
      const b=document.createElement("button");
      b.className="chip"+(y===lunY?" on":"");
      b.textContent=y;
      b.onclick=()=>{lunY=y;const f=GRP.lun.charts.find(c=>c.y===y&&c.mo===lunM)||GRP.lun.charts.find(c=>c.y===y);if(f){lunM=f.mo;chart=f;}buildBars();draw();};
      cb.appendChild(b);
    });
    const s2=document.createElement("span");s2.className="sep";cb.appendChild(s2);
    // month chips for the chosen year
    const MN=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
    [...new Set(GRP.lun.charts.filter(c=>c.y===lunY).map(c=>c.mo))].forEach(mo=>{
      const b=document.createElement("button");
      b.className="chip"+(mo===lunM?" on":"");
      b.textContent=MN[mo-1];
      b.onclick=()=>{lunM=mo;const f=GRP.lun.charts.find(c=>c.y===lunY&&c.mo===mo);if(f)chart=f;buildBars();draw();};
      cb.appendChild(b);
    });
    // the month's lunations as cards
    const row=document.createElement("div");
    row.style.cssText="flex-basis:100%;display:flex;justify-content:center;gap:6px;flex-wrap:wrap;margin-top:4px";
    GRP.lun.charts.filter(c=>c.y===lunY&&c.mo===lunM).forEach(c=>{
      const b=document.createElement("button");
      b.className="chip"+(c.id===chart.id?" on":"");
      b.innerHTML=PH_G[c.ph]+" "+String(c.mo).padStart(2,"0")+"/"+String(c.dd).padStart(2,"0")+" · "+c.title.split("— ")[1]+(c.ecl?' <span class="gv">ECLIPSE</span>':"");
      b.onclick=()=>setChart(c);
      row.appendChild(b);
    });
    cb.appendChild(row);
  }else if(mode==="day"){
    const stepBtn=(lbl,d)=>{
      const b=document.createElement("button");
      b.className="chip";b.textContent=lbl;
      b.onclick=()=>{const c=dayChart(dsOf(dayIndex(chart.ds)+d));if(c)setChart(c);};
      return b;
    };
    cb.appendChild(stepBtn("‹ day",-1));
    const inp=document.createElement("input");
    inp.type="date";inp.className="chip";
    inp.min=DAYS.start;inp.max=dsOf(DAYS.n-1);inp.value=chart.ds;
    inp.onchange=()=>{const c=dayChart(inp.value);if(c)setChart(c);};
    cb.appendChild(inp);
    cb.appendChild(stepBtn("day ›",1));
    const td=document.createElement("button");
    td.className="chip";td.textContent="today";
    td.onclick=()=>setChart(dayChart(todayDS()));
    cb.appendChild(td);
    const note=document.createElement("span");
    note.style.cssText="font-size:10px;color:var(--faint);font-style:italic;align-self:center";
    note.textContent="tip: overlay an ingress or lunation below — the day's sky against the season's promise";
    cb.appendChild(note);
  }else{
    const sel=document.createElement("select");
    sel.className="chip";
    [...new Set(GRP.chr.charts.map(c=>c.grp))].forEach(g=>{
      const og=document.createElement("optgroup");og.label=g;
      GRP.chr.charts.filter(c=>c.grp===g).forEach(c=>{
        const o=document.createElement("option");
        o.value=c.id;o.textContent=c.title;o.selected=c.id===chart.id;
        og.appendChild(o);
      });
      sel.appendChild(og);
    });
    sel.onchange=()=>setChart(byId(sel.value));
    cb.appendChild(sel);
    const note=document.createElement("span");
    note.className="gv";note.style.cssText="font-size:10px;color:var(--faint);font-style:italic;align-self:center";
    note.textContent="timed births only — untimed (sunrise) charts excluded: MC lines swing 15°/hour";
    cb.appendChild(note);
  }
  const pb=document.getElementById("pbar");
  pb.innerHTML="";
  ORDER.forEach(p=>{
    const s=document.createElement("span");
    s.className="pchip"+(pOn[p]?"":" off");
    s.innerHTML=glyphSVG(p,13,PCOL[p])+p;
    s.onclick=()=>{pOn[p]=!pOn[p];buildBars();draw();};
    pb.appendChild(s);
  });
  const all=document.createElement("span");
  all.className="achip";all.textContent="all / none";
  all.onclick=()=>{const v=!ORDER.every(p=>pOn[p]);ORDER.forEach(p=>pOn[p]=v);buildBars();draw();};
  pb.appendChild(all);
  const ab=document.getElementById("abar");
  ab.innerHTML="";
  ["MC","IC","As","Ds"].forEach(a=>{
    const s=document.createElement("span");
    s.className="achip"+(aOn[a]?"":" off");
    s.textContent=a+" — "+AMEAN[a].split(" — ")[0].replace(" here","");
    s.onclick=()=>{aOn[a]=!aOn[a];buildBars();draw();};
    ab.appendChild(s);
  });
  if(chart.kind==="lun"&&chart.ecl&&ECLP[chart.id]){
    const ec=document.createElement("span");
    ec.className="achip"+(eclOn?"":" off");
    ec.textContent="◗ eclipse shadow";
    ec.onclick=()=>{eclOn=!eclOn;buildBars();draw();};
    ab.appendChild(ec);
  }
  const sp=document.createElement("span");sp.className="sep";ab.appendChild(sp);
  const st=document.createElement("span");
  st.className="achip";
  st.textContent=STYLE==="sat"?"◐ parchment style":"◐ satellite style";
  st.title="toggle map style";
  st.onclick=()=>{STYLE=STYLE==="sat"?"parchment":"sat";try{localStorage.setItem("f250-am-style",STYLE);}catch(_){}buildBars();draw();};
  ab.appendChild(st);
  // --- overlay: synastry on Earth ---
  const sp2=document.createElement("span");sp2.className="sep";ab.appendChild(sp2);
  const lbl=document.createElement("span");
  lbl.className="achip";lbl.style.cursor="default";
  lbl.textContent="+ overlay:";
  ab.appendChild(lbl);
  const ov=document.createElement("select");
  ov.className="achip";
  const none=document.createElement("option");none.value="";none.textContent="none";ov.appendChild(none);
  const addOG=(label,list,name)=>{
    const og=document.createElement("optgroup");og.label=label;
    list.forEach(c=>{
      const o=document.createElement("option");
      o.value=c.id;o.textContent=name(c);o.selected=!!OV&&OV.id===c.id;
      og.appendChild(o);
    });
    ov.appendChild(og);
  };
  addOG("Ingresses",GRP.ing.charts,c=>c.title);
  [...new Set(GRP.lun.charts.map(c=>c.y))].forEach(y=>
    addOG("Lunations "+y,GRP.lun.charts.filter(c=>c.y===y),
      c=>PH_G[c.ph]+" "+String(c.mo).padStart(2,"0")+"/"+String(c.dd).padStart(2,"0")+" "+c.title+(c.ecl?" · ECLIPSE":"")));
  addOG("Characters",GRP.chr.charts,c=>c.title);
  ov.onchange=()=>{OV=ov.value?byId(ov.value):null;draw();};
  ab.appendChild(ov);
  if(OV){
    const x=document.createElement("span");
    x.className="achip";x.textContent="✕ clear overlay";
    x.onclick=()=>{OV=null;buildBars();draw();};
    ab.appendChild(x);
  }
}

// ---------- drawing ----------
const NS="http://www.w3.org/2000/svg";
function draw(){
  const svg=document.getElementById("map");
  svg.setAttribute("viewBox","0 0 "+W+" "+H);
  const SAT=STYLE==="sat";
  let s='<g id="world" transform="translate('+tx+' '+ty+') scale('+k+')">';
  if(SAT){
    s+='<image href="'+EARTH_IMG+'" x="0" y="0" width="'+W+'" height="'+H+'" preserveAspectRatio="none"/>';
  }else{
    s+='<rect x="0" y="0" width="'+W+'" height="'+H+'" fill="var(--ocean)"/>';
  }
  // graticule
  const grat=SAT?"rgba(255,255,255,0.16)":"#d3ccba";
  for(let lon=-150;lon<=150;lon+=30)s+='<line x1="'+xOf(lon)+'" y1="0" x2="'+xOf(lon)+'" y2="'+H+'" stroke="'+grat+'" stroke-width="0.5" vector-effect="non-scaling-stroke"/>';
  for(let lat=-60;lat<=60;lat+=30)s+='<line x1="0" y1="'+yOf(lat)+'" x2="'+W+'" y2="'+yOf(lat)+'" stroke="'+grat+'" stroke-width="'+(lat===0?0.9:0.5)+'" vector-effect="non-scaling-stroke"/>';
  if(!SAT){
    // land (evenodd so lake/sea holes stay water — single-path fill bug fixed)
    let lp="";
    LAND.forEach(r=>{r.forEach((c,i)=>{lp+=(i?"L":"M")+f1(xOf(c[0]))+" "+f1(yOf(c[1]));});lp+="Z";});
    s+='<path d="'+lp+'" fill="var(--landfill)" fill-rule="evenodd" stroke="var(--coast)" stroke-width="0.7" vector-effect="non-scaling-stroke"/>';
  }
  // country borders (Natural Earth 50m, interior boundaries)
  let bp="";
  BORDERS.forEach(r=>{let prev=null;r.forEach(c=>{bp+=(prev!==null&&Math.abs(c[0]-prev)>180?"M":(bp===""?"M":(prev===null?"M":"L")))+f1(xOf(c[0]))+" "+f1(yOf(c[1]));prev=c[0];});});
  s+='<path d="'+bp+'" fill="none" stroke="'+(SAT?"rgba(255,255,255,0.5)":"#c4baa3")+'" stroke-width="0.6" vector-effect="non-scaling-stroke"/>';
  // cities — halo drawn as a separate outline copy under the fill (works in every renderer)
  const cFill=SAT?"#ffffff":"#8a8174", cTxt=SAT?"#ffffff":"#6d655a";
  const txt=(x,y,size,fill,extra,str)=>{
    const base='x="'+f1(x)+'" y="'+f1(y)+'" font-size="'+size+'"'+extra;
    let o="";
    if(SAT)o+='<text '+base+' fill="none" stroke="rgba(8,18,32,0.8)" stroke-width="'+(size*0.32)+'" stroke-linejoin="round">'+str+"</text>";
    return o+'<text '+base+' fill="'+fill+'">'+str+"</text>";
  };
  CITIES.forEach(c=>{
    const x=xOf(c[2]),y=yOf(c[1]);
    if(c[3]===2){
      const star=SAT?"#ffd76a":"#7a2e1d";
      s+=txt(x,y+1.5,9/Math.sqrt(k),star,' text-anchor="middle"',"★");
      s+=txt(x,y-4/Math.sqrt(k),8/Math.sqrt(k),star,' text-anchor="middle" font-style="italic"',c[0]);
    }else{
      s+='<circle cx="'+f1(x)+'" cy="'+f1(y)+'" r="'+1.4/Math.sqrt(k)+'" fill="'+cFill+'"'+(SAT?' opacity="0.85"':'')+'/>';
      if(c[3]===1||k>2.1)s+=txt(x+2.4/Math.sqrt(k),y-1.5/Math.sqrt(k),(c[3]?8:7)/Math.sqrt(k),cTxt,'',c[0]);
    }
  });
  // ACG lines
  hitLines.length=0;
  const haloLn=SAT?'rgba(255,253,248,0.65)':null;   // white underlay so colors pop on imagery (AG look)
  const drawChart=(ch,dim)=>{
    let o="";
    const fade=dim?0.42:1, wf=dim?0.75:1;
    ORDER.forEach(p=>{
      if(!pOn[p])return;
      const b=ch.bodies[p]; if(!b)return;
      const L=linesFor(b,ch.gst), col=PCOL[p];
      const vline=(lon,wd,dash,op)=>{
        const seg='x1="'+f1(xOf(lon))+'" y1="0" x2="'+f1(xOf(lon))+'" y2="'+H+'" fill="none" vector-effect="non-scaling-stroke"';
        let q="";
        if(haloLn&&!dim)q+='<line '+seg+' stroke="'+haloLn+'" stroke-width="'+(wd+1.6)+'"/>';
        return q+'<line '+seg+' stroke="'+col+'" stroke-width="'+(wd*wf)+'"'+(dash?' stroke-dasharray="'+dash+'"':'')+' opacity="'+(op*fade)+'"/>';
      };
      const cline=(pts,wd,dash,op)=>{
        const d=polyPath(pts);
        let q="";
        if(haloLn&&!dim)q+='<path d="'+d+'" fill="none" stroke="'+haloLn+'" stroke-width="'+(wd+1.6)+'" vector-effect="non-scaling-stroke"/>';
        return q+'<path d="'+d+'" fill="none" stroke="'+col+'" stroke-width="'+(wd*wf)+'"'+(dash?' stroke-dasharray="'+dash+'"':'')+' opacity="'+(op*fade)+'" vector-effect="non-scaling-stroke"/>';
      };
      if(aOn.MC)o+=vline(L.mc,1.7,null,0.95);
      if(aOn.IC)o+=vline(L.ic,1.2,"7 4",0.9);
      if(aOn.As)o+=cline(L.asc,1.4,null,0.92);
      if(aOn.Ds)o+=cline(L.dsc,1.2,"2 3.4",0.92);
      // zenith dot — planet exactly overhead
      o+='<circle cx="'+f1(xOf(L.mc))+'" cy="'+f1(yOf(b.dec))+'" r="'+(dim?1.8:2.6)/Math.sqrt(k)+'" fill="'+col+'" stroke="#fffdf8" stroke-width="0.8" opacity="'+fade+'" vector-effect="non-scaling-stroke"/>';
    });
    return o;
  };
  if(OV)s+=drawChart(OV,true);   // overlay beneath the main chart
  s+=drawChart(chart,false);
  // eclipse shadow geography
  let eclNote="";
  const E=chart.kind==="lun"&&chart.ecl?ECLP[chart.id]:null;
  if(E&&eclOn){
    const mx=xOf(E.max[1]),my=yOf(E.max[0]);
    if(E.path.length>1){
      const d=polyPath(E.path);
      s+='<path d="'+d+'" fill="none" stroke="rgba(255,253,248,0.8)" stroke-width="4.6" vector-effect="non-scaling-stroke"/>'+
         '<path d="'+d+'" fill="none" stroke="#7a1020" stroke-width="2.4" vector-effect="non-scaling-stroke"/>';
      eclNote=" · <b>"+E.kind+" solar eclipse</b> — shadow path drawn";
    }else if(E.solar){
      eclNote=" · <b>partial solar eclipse</b> — no central path; ◎ marks greatest eclipse";
    }else{
      eclNote=" · <b>"+E.kind+" eclipse</b> — ◎ Moon overhead at max; the night side watches";
    }
    s+='<circle cx="'+f1(mx)+'" cy="'+f1(my)+'" r="'+7/Math.sqrt(k)+'" fill="none" stroke="#7a1020" stroke-width="1.6" vector-effect="non-scaling-stroke"/>'+
       '<circle cx="'+f1(mx)+'" cy="'+f1(my)+'" r="'+2.2/Math.sqrt(k)+'" fill="#7a1020"/>';
  }
  s+="</g>";
  svg.innerHTML=s;
  drawGutter();
  let sub="<b>"+chart.title+"</b> — "+chart.date;
  if(chart.kind==="lun")sub+=(chart.ecl?" · <b>ECLIPSE</b>":"")+eclNote;
  else if(!chart.kind)sub+=chart.gov?" · <i>governing chart</i>":" · <i>nuance layer</i>";
  if(OV)sub+=' &nbsp;<span style="color:var(--faint)">+ overlay: '+OV.title+(OV.kind==="lun"?" ("+OV.date.split(" ·")[0]+")":"")+"</span>";
  document.getElementById("sub").innerHTML=sub;
}
// glyph labels pinned to the top edge (screen space, track pan/zoom)
function drawGutter(){
  const g=document.getElementById("gutter"),svg=document.getElementById("map");
  const r=svg.getBoundingClientRect(),scale=r.width/W;
  g.setAttribute("width",r.width);g.setAttribute("height",Math.max(24,24*scale));
  let s="";
  const put=(lon,p,a,solid)=>{
    let sx=(xOf(lon)*k+tx)*scale;
    if(sx<-10||sx>r.width+10)return;
    s+='<g transform="translate('+f1(sx)+' 2)">'+
       '<rect x="-9" y="0" width="18" height="19" rx="3" fill="#fffdf8" stroke="'+PCOL[p]+'" stroke-width="0.8" opacity="0.92"/>'+
       '<g transform="translate(-7 -1) scale(0.7)" color="'+PCOL[p]+'" stroke="currentColor" stroke-width="2" stroke-linecap="round" fill="none">'+(GLY[p]||"")+"</g>"+
       '<text x="5" y="16" font-size="6.5" fill="'+PCOL[p]+'" font-family="Georgia,serif" font-style="italic">'+a+"</text></g>";
  };
  ORDER.forEach(p=>{
    if(!pOn[p])return;
    const b=chart.bodies[p];if(!b)return;
    const L=linesFor(b,chart.gst);
    if(aOn.MC)put(L.mc,p,"Mc");
    if(aOn.IC)put(L.ic,p,"Ic");
    if(aOn.As){const lo=curveLonAt(b,chart.gst,latOfY((12-ty)/k),"As");const eq=curveLonAt(b,chart.gst,0,"As");if(eq!==null)put(lo!==null?lo:eq,p,"As");}
    if(aOn.Ds){const lo=curveLonAt(b,chart.gst,latOfY((12-ty)/k),"Ds");const eq=curveLonAt(b,chart.gst,0,"Ds");if(eq!==null)put(lo!==null?lo:eq,p,"Ds");}
  });
  g.innerHTML=s;
}

// ---------- interaction ----------
const hitLines=[];
const svgEl=document.getElementById("map"),tip=document.getElementById("tip"),panel=document.getElementById("panel");
function mapXY(ev){
  const r=svgEl.getBoundingClientRect(),scale=W/r.width;
  const px=(ev.clientX-r.left)*scale,py=(ev.clientY-r.top)*scale;
  return {x:(px-tx)/k,y:(py-ty)/k};
}
function activeCharts(){return OV?[chart,OV]:[chart];}
function nearest(ev){
  const m=mapXY(ev),lat=latOfY(m.y),lon=lonOfX(m.x);
  let best=null,bd=9/k;          // ~9 map px tolerance, tighter when zoomed
  activeCharts().forEach(ch=>{
    ORDER.forEach(p=>{
      if(!pOn[p])return;
      const b=ch.bodies[p];if(!b)return;
      const L=linesFor(b,ch.gst);
      const cand=[];
      if(aOn.MC)cand.push(["MC",Math.abs(m.x-xOf(L.mc))]);
      if(aOn.IC)cand.push(["IC",Math.abs(m.x-xOf(L.ic))]);
      ["As","Ds"].forEach(a=>{
        if(!aOn[a])return;
        const lo=curveLonAt(b,ch.gst,lat,a);
        if(lo!==null)cand.push([a,Math.abs(m.x-xOf(lo))*Math.cos(lat*D2R)+0.0001]);
      });
      cand.forEach(c=>{if(c[1]<bd){bd=c[1];best={p:p,a:c[0],ch:ch};}});
    });
  });
  return best;
}
svgEl.addEventListener("mousemove",ev=>{
  if(panning)return;
  const hit=nearest(ev);
  if(!hit){tip.style.display="none";return;}
  const b=hit.ch.bodies[hit.p];
  tip.innerHTML='<div class="t1">'+hit.p+" "+hit.a+(b.rx?" ℞":"")+(OV&&hit.ch===OV?' <span style="color:var(--faint);font-weight:400">(overlay)</span>':"")+'</div>'+
   '<div class="t2">'+hit.ch.title+" · "+hit.p+" at "+b.pos+'</div>'+
   '<div class="t3">'+PMEAN[hit.p]+"<br>"+AMEAN[hit.a]+"</div>";
  const r=document.getElementById("stage").getBoundingClientRect();
  tip.style.left=Math.min(ev.clientX-r.left+14,r.width-290)+"px";
  tip.style.top=(ev.clientY-r.top+10)+"px";
  tip.style.display="block";
});
svgEl.addEventListener("mouseleave",()=>tip.style.display="none");
svgEl.addEventListener("click",ev=>{
  if(moved)return;
  const m=mapXY(ev),lat=latOfY(m.y),lon=lonOfX(m.x);
  const rows=[];
  activeCharts().forEach(ch=>{
    ORDER.forEach(p=>{
      if(!pOn[p])return;
      const b=ch.bodies[p];if(!b)return;
      const L=linesFor(b,ch.gst);
      const push=(a,lo)=>{if(lo===null)return;const d=Math.abs(n180(lon-lo));if(d<=6)rows.push({p:p,a:a,d:d,ch:ch});};
      push("MC",L.mc);push("IC",L.ic);
      push("As",curveLonAt(b,ch.gst,lat,"As"));push("Ds",curveLonAt(b,ch.gst,lat,"Ds"));
    });
  });
  rows.sort((a,b)=>a.d-b.d);
  let near=null,nd=1e9;
  CITIES.forEach(c=>{const d=Math.hypot((c[2]-lon)*Math.cos(lat*D2R),c[1]-lat);if(d<nd){nd=d;near=c[0];}});
  let s='<span class="x" onclick="this.parentNode.style.display=\'none\'">✕</span>'+
   "<h3>"+f1(Math.abs(lat))+"°"+(lat>=0?"N":"S")+" "+f1(Math.abs(lon))+"°"+(lon>=0?"E":"W")+"</h3>"+
   '<div class="ph">near '+near+" · "+chart.title+" · lines within 6°</div>";
  if(!rows.length)s+='<div class="ph">no lines within 6° of this spot — quiet ground for this chart</div>';
  rows.forEach(r=>{
    const b=r.ch.bodies[r.p], isOv=OV&&r.ch===OV;
    s+='<div class="row"'+(isOv?' style="opacity:0.72"':'')+'>'+glyphSVG(r.p,13,PCOL[r.p])+"<b>"+r.p+" "+r.a+(b.rx?" ℞":"")+"</b>"+
       (isOv?'<span style="font-size:10px;color:var(--faint);font-style:italic">overlay</span>':"")+
       '<span class="o">'+(r.d<0.05?"EXACT":"Δ"+f1(r.d)+"°")+"</span></div>"+
       '<div class="mn">'+PMEAN[r.p].split(" — ")[0]+" "+AMEAN[r.a].split(" — ")[0]+"</div>";
  });
  panel.innerHTML=s;panel.style.display="block";
});
// pan / zoom
let panning=false,moved=false,px0=0,py0=0;
svgEl.addEventListener("mousedown",ev=>{panning=true;moved=false;px0=ev.clientX;py0=ev.clientY;svgEl.classList.add("panning");});
window.addEventListener("mousemove",ev=>{
  if(!panning)return;
  const r=svgEl.getBoundingClientRect(),scale=W/r.width;
  const dx=(ev.clientX-px0)*scale,dy=(ev.clientY-py0)*scale;
  if(Math.abs(ev.clientX-px0)+Math.abs(ev.clientY-py0)>3)moved=true;
  if(!moved)return;
  tx+=dx;ty+=dy;px0=ev.clientX;py0=ev.clientY;clamp();draw();
});
window.addEventListener("mouseup",()=>{panning=false;svgEl.classList.remove("panning");});
svgEl.addEventListener("wheel",ev=>{
  ev.preventDefault();
  const m=mapXY(ev),f=ev.deltaY<0?1.25:0.8,nk=Math.min(MAXK,Math.max(1,k*f));
  tx-=m.x*(nk-k);ty-=m.y*(nk-k);k=nk;clamp();draw();
},{passive:false});
function clamp(){
  tx=Math.min(0,Math.max(W-W*k,tx));
  ty=Math.min(0,Math.max(H-H*k,ty));
  if(k===1){tx=0;ty=0;}
}
document.getElementById("zin").onclick=()=>{const c={x:(W/2-tx)/k,y:(H/2-ty)/k};const nk=Math.min(MAXK,k*1.4);tx-=c.x*(nk-k);ty-=c.y*(nk-k);k=nk;clamp();draw();};
document.getElementById("zout").onclick=()=>{const c={x:(W/2-tx)/k,y:(H/2-ty)/k};const nk=Math.max(1,k*0.7);tx-=c.x*(nk-k);ty-=c.y*(nk-k);k=nk;clamp();draw();};
document.getElementById("zfit").onclick=()=>{k=1;tx=0;ty=0;draw();};
window.addEventListener("resize",drawGutter);
// cross-view navigation: goToMap('2025-aries') from the shell
window.addEventListener("message",ev=>{
  const d=ev.data||{};
  if(d.type==="astromap"&&d.chart){
    const c=byId(d.chart);
    if(c){
      chart=c;
      mode=c.kind==="lun"?"lun":(c.kind==="chr"?"chr":(c.kind==="day"?"day":"ing"));
      if(c.kind==="lun"){lunY=c.y;lunM=c.mo;}
      k=1;tx=0;ty=0;buildBars();draw();
    }
  }
});
buildBars();draw();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
