# The World Charts — Method & Sources

Companion to the Observatory view **The World Charts** (`04 - Synthesis/Cross-cuts/The World Charts.html`, builder `99 - Templates/build_world_charts.py`). National natal charts for the main powers, cast the same way as **The American Charts** (build rules in [[VIEWS REGISTRY]]) so they can be read mundanely and receive ingress / lunation / eclipse transits — **without** growing each nation's full lineage.

## Method
- **Engine:** Swiss Ephemeris (pyswisseph), positions never hand-typed. Reuses `wheel_lib.py` (`WHEEL_JS`, `aspects_between`, `placidus_cusps`) — identical wheels, hand-drawn glyphs, WS↔Placidus toggle.
- **Houses:** Whole Sign default (project standard).
- **Location:** each chart cast for **its own founding city** (its capital, or the city of the founding act — e.g. Bonn for FRG 1949, Petrograd for 1917, Nanjing for RoC 1912, Tel Aviv for Israel). Transits to these charts should be read at that capital, not D.C.
- **Selection:** primaries = the **current-state** chart (what the nation legally *is* today); alternates = the standard historical candidates. Founding moments follow the standard mundane sources — principally **Nicholas Campion, _The Book of World Horoscopes_** (the field's reference sourcebook).

## The charts (primary ★ + alternates)

- **Germany 🇩🇪** — ★ Reunification **3 Oct 1990, 00:00 CET, Berlin** · alt Federal Republic **24 May 1949, Bonn** (the Cold-War / MKUltra-era state) · alt Empire **18 Jan 1871, Berlin** (proclaimed Versailles).
- **United Kingdom 🇬🇧** — ★ United Kingdom **1 Jan 1801, 00:00 LMT, London** (Act of Union) · alt Great Britain **1 May 1707, London**.
- **Russia 🇷🇺** — ★ Russian Federation **25 Dec 1991, 19:32 MSK, Moscow** (Soviet flag lowered) · alt Revolution **7 Nov 1917, Petrograd** · alt Sovereignty **12 Jun 1990, Moscow** (Russia Day).
- **China 🇨🇳** — ★ People's Republic **1 Oct 1949, 15:00, Beijing** (Tiananmen) · alt Republic of China **1 Jan 1912, Nanjing**.
- **France 🇫🇷** — ★ Fifth Republic **4 Oct 1958, Paris** · alt First Republic **22 Sep 1792, Paris** (equinox).
- **Japan 🇯🇵** — ★ Postwar State **3 May 1947, 00:00 JST, Tokyo** · alt Meiji Empire **11 Feb 1889, Tokyo**.
- **Israel 🇮🇱** — ★ State of Israel **14 May 1948, 16:00, Tel Aviv** (Ben-Gurion's declaration) · alt Mandate ends **15 May 1948, 00:00**.
- **Iran 🇮🇷** — ★ Islamic Republic **1 Apr 1979, Tehran** · alt Revolution victory **11 Feb 1979, Tehran**.
- **Ukraine 🇺🇦** — ★ Independence **24 Aug 1991, Kyiv** · alt People's Republic **22 Jan 1918, Kyiv**.
- **India 🇮🇳** — ★ Independence **15 Aug 1947, 00:00 IST, New Delhi** ("tryst with destiny") · alt Republic **26 Jan 1950, New Delhi**.

## Provisional-time flags ⚠
These charts have a **solid clock**, so angles/Moon are reliable: Germany 1990, UK 1801, China 1949, Japan 1947, Israel 1948, India 1947.

These have an **uncertain founding time** — the view flags them; treat the **Ascendant, MC, houses and the Moon's exact degree as soft** (planetary *signs* are still solid): Germany 1949 & 1871, GB 1707, Russia 1991/1917/1990, RoC 1912, France 1958 & 1792, Japan 1889, Israel-Mandate, Iran 1979 & Feb-1979, Ukraine 1991 & 1918, India 1950. If any becomes load-bearing, pin the exact time before leaning on its angles.

## Verification
Cross-checked computed Sun/Moon against published chart values: Israel (Sun 23° Taurus, Moon Leo ✓), India (Moon Cancer ✓), China (Sun ~8° Libra ✓), Germany-1990 (Sun ~10° Libra ✓), UK-1801 (Sun 10° Capricorn ✓). The known-sensitive midnight ascendants (India Taurus/Gemini cusp) sit exactly where 00:00 puts them.

## To ship / extend
- **Ship the tab:** app builds run on the Mac only. The HTML is already in `Cross-cuts/` and `observatory-app/public/`; register a tab (`obs-wc` → iframe `The World Charts.html`) in the shell and rebuild on the mini. (Don't hardcode — the Cross-cuts glob will pick it up.)
- **Next passes (optional):** synastry overlay of each nation's chart with the live ingress/lunation (the engine already exists); hand-written mundane reads to replace the auto skeletons; add more nations by extending the `NATIONS` list in the builder.

See also: [[Mundane Astrology — Master Reference]], [[VIEWS REGISTRY]] (canonical method and durable build rules for The American Charts and the Mundane Engine).
