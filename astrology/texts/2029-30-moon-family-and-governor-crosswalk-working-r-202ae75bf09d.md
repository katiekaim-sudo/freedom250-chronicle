---
title: "2029–30 Moon-Family and Governor Crosswalk — Working Receipt"
type: astrology_source_integrity_receipt
status: computed_draft_unsealed
created: 2026-10-11
developed_through: 2026-10-11
technical_packet: "2029–30 Moon-Family and Governor Crosswalk — COMPUTED DRAFT.json"
parent_map: "[[The Sky Through 2030 — Working Story Map]]"
evidence_credit: zero
---

# 2029–30 Moon-Family and Governor Crosswalk

The current `moon_lineages.json` projection admits **13 long Full phases from January 2029 through July 2030**. Most later Fulls are recorded as generic `lunation-…-fm` events with no chart ID, and the registered members keep `ingress-2028-aries` after that annual chart has ended. A date-only join would be too weak. [[2029–30 Moon-Family and Governor Crosswalk — COMPUTED DRAFT.json]] matches each admitted Full to one DE441 D.C. chart by **Full-Moon kind, UTC date, sign, degree and exact clock**; the largest clock difference is **2.097 seconds**. It retains the original event and member objects and computes the actual governor from exact ingress instants. The 2029 and 2030 chart packets agree with that ingress timeline where they print a governor.

| Current Full | Older New-Moon seed at long Full | Current Full's governor | Source governor agrees? |
|---|---|---|---|
| Jan 30, 2029 Leo | Aug 2, 2027 Leo solar eclipse | 2028 Aries | Yes |
| Feb 28 Virgo | Aug 31, 2027 Virgo | 2028 Aries | Yes |
| Mar 30 Libra | Sep 30, 2027 Libra | **2029 Aries** | No |
| Apr 28 Scorpio | Oct 29, 2027 Scorpio | **2029 Aries** | No |
| May 27 Sagittarius | Nov 28, 2027 Sagittarius | **2029 Aries** | No |
| Jun 26 Capricorn total lunar eclipse | Dec 27, 2027 Capricorn | **2029 Aries** | No |
| Jul 25 Aquarius | Jan 26, 2028 Aquarius solar eclipse | **2029 Aries** | No |
| Aug 24 Pisces | Feb 25, 2028 Pisces | **2029 Aries** | No |
| Mar 19, 2030 Virgo | Sep 18, 2028 Virgo | **2029 Capricorn** | No |
| Apr 18 Libra | Oct 18, 2028 Libra | **2030 Aries** | No |
| May 17 Scorpio | Nov 16, 2028 Scorpio | **2030 Aries** | No |
| Jun 15 Sagittarius partial lunar eclipse | Dec 16, 2028 Sagittarius | **2030 Aries** | No |
| Jul 15 Capricorn | Jan 14, 2029 Capricorn solar eclipse | **2030 Aries** | No |

Only the first two stored member governors agree with the governor in force at their Full. The later **11** entries still say `ingress-2028-aries`; this does **not** move their older seeds or make the old year govern the later Full. The March 30, 2029 Full follows the March 20 Aries ingress; the March 19, 2030 Full precedes the March 20 Aries reset and remains under 2029 Capricorn; the April–July 2030 Fulls fall under fixed Taurus-rising 2030 Aries. Each older seed keeps the chart and governor of its own date.

The April 28 and May 27, 2029 source phase clocks differ from the DE441 chapter casts by **2.096** and **1.562 seconds**, respectively; they still match uniquely by date, phase, sign and degree. A hard one-second threshold would falsely discard these admitted lines. The June 26, 2029 and June 15, 2030 eclipsed Fulls are the two eclipse-genealogy misses already documented in [[2029–30 Eclipse Moon-Family ID Reconciliation — Working Receipt]]. The February/March 2029 details and March governor error were first documented in [[2029 February–March Moon-Family ID and Governor Reconciliation — Working Receipt]]. This register broadens the same source issue across the remaining admitted Fulls; it does not create new lunar families.

**Reading boundary:** a current Full reveals its immediate New-Moon chapter *and* may be the admitted long Full of an older seed. Saros, Metonic, direct planetary aspect, synodic seed and Moon-family phase remain separate clocks. A lineage join supplies ancestry, not a verdict about what happened in the country. New 2029–30 seeds lacking a complete line in the current projection remain unadmitted, not disproved.

**Producer return gate:** a future `moon_lineages.json` or eclipse-genealogy regeneration should resolve a unique chart by phase/date/degree/clock while preserving both IDs, derive each member's governor from the exact ingress timeline at its own phase instant, and reject stale-governor output. Keep this dated draft crosswalk until the canonical producers and regenerated packets pass those checks. No factual Chronicle record or political interpretation was used.

Sources: `99 - Templates/moon_lineages.json` (`phase_events`, `lineages`); [[2028 Lunar Chart Packet — COMPUTED DRAFT.json]]; [[2029 Lunar Chart Packet — COMPUTED DRAFT.json]]; [[2030 Lunar Chart Packet — COMPUTED DRAFT.json]]; [[2029–30 Moon-Family and Governor Crosswalk — COMPUTED DRAFT.json]]; [[2029–30 Eclipse Moon-Family ID Reconciliation — Working Receipt]]; [[2029 February–March Moon-Family ID and Governor Reconciliation — Working Receipt]]; `build_chart_reading_bones_2025.py`, `swiss_ephemeris.py`.
