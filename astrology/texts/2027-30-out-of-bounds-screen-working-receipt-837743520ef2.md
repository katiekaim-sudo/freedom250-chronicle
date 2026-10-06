---
title: "2027–30 Out-of-Bounds Screen — Working Receipt"
type: astrology_method_audit_working
status: computed_screen_interpretation_pending
created: 2026-10-11
developed_through: 2026-10-11
technical_packet: "2027–30 Out-of-Bounds Screen — COMPUTED DRAFT.json"
parent_map: "[[The Sky Through 2030 — Working Story Map]]"
evidence_credit: zero
---

# 2027–30 out-of-bounds screen

The first fresh re-hearing found that the May 20, 2027 Moon and Mercury were out of bounds, a fact their earlier prose missed. I then screened **all 100 distinct exact New/Full Moon wheels** in the existing 2027–30 complete-bone packets, including the five early-2031 strikes in the final annual window. This is an astronomical **triage layer**, not 100 new readings. The per-chart values and their source packets are in [[2027–30 Out-of-Bounds Screen — COMPUTED DRAFT.json]].

| Calendar year of syzygy | Complete wheels | Wheels with an out-of-bounds actor | Actor contacts |
|---|---:|---:|---:|
| 2027 | 21 | 15 | 26 |
| 2028 | 25 | 17 | 24 |
| 2029 | 24 | 12 | 24 |
| 2030 | 25 | 14 | 18 |
| 2031, within the 2030 Aries year | 5 | 0 | 0 |
| **Distinct total** | **100** | **58** | **92** |

**Method.** Deduplicate the `charts` and `lunar_charts` entries in the complete-bone packets by their exact UTC; require the saved Swiss DE441 position and declination. Compare each non-Sun actor's absolute declination to **true obliquity at that exact JD** from Swiss `ECL_NUT`. The workbook's 23°26′ is a rounded shorthand. This avoids calling the Sun out of bounds or promoting a point on the wrong side of a seconds-of-arc rounding line. For example, Pluto on **July 25, 2029** is beyond a literal 23°26′ cutoff but **inside** the exact true-obliquity bound; the packet does not flag it. The counted 92 actor contacts are confirmed against this physical bound. None of those 92 is tagged out of bounds in its saved `pos.cond` list, even though `pos.dec` holds the value. The chart facts are present; the condition layer and prose have not routinely heard them.

The screen changes what to inspect next, not what history must do:

- **2027:** May 20/June 4 Moon and Mercury, June 19/July 4 Moon; Pluto crosses the bound in the August–December lunar sequence, and Venus/Mars/Mercury join several late-year wheels. [[2027 May–June Declination and Pair Film — Fresh Rehearing]] has interpreted the first cluster and corrected the May 20 declination error. [[2027 Cancer–Leo Eclipse Relay — Fresh Method Rehearing]] and [[2027 Libra–Sagittarius Pair Film — Fresh Method Rehearing]] now interpret the July/August and autumn clusters in context. The late-December/early-2028 eclipse handoff still needs a fresh hearing.
- **2028:** Venus stands far north during the spring Taurus/Uranus-return chapters; Mars is out of bounds around the July/August Cancer eclipse chapter; Pluto recurs south of the bound in the second half. [[2028 Aries–Taurus Motion Gate — Fresh Rehearing]] now weighs the spring Venus/Mercury cluster against the first two lunar chapters, the April 30 pair seed and the May station week. [[2028 Gemini–Cancer Structural Gate — Fresh Rehearing]] now weighs the May/June Moon and Venus conditions and the out-of-bounds Moon at the nested ingress and Cancer seed. [[2028 Cancer–Leo Eclipse and Summer Relay — Fresh Rehearing]] now hears the July/August Mars and Pluto crossing sequence in its solar seed and following Full. [[2028 Virgo–Scorpio Structural Return — Fresh Rehearing]] now hears Pluto’s autumn condition at the nested Libra and second Saturn–Pluto square charts, and the December 2 out-of-bounds Moon/Mercury/Pluto Full. [[2028 Sagittarius–Capricorn Winter Motion — Fresh Rehearing]] now hears the December 16 Moon/Mercury/Pluto cluster and Pluto’s December 26 return inside the bound before the Cancer Full. Repeated Pluto contacts remain standing hue, not new events at every wheel.
- **2029:** Venus and Mars both exceed the southern bound in the October–November Libra/Scorpio handoff, while Pluto remains beyond it; Mercury joins the December double-eclipse run. This may materially change the earlier Venus–Mars loop hearing, but no meaning is assigned from declination alone.
- **2030:** Mars and then Mercury exceed the northern bound around the June/July eclipse relay; Pluto's southern condition resumes late summer through winter, and Mercury/Venus join the November–December eclipse stretch. The Jupiter–Saturn opposition history remains a separate clock.

The Moon can move beyond the bound for a short portion of a month; Pluto's repeated seasonal contacts are slow background. **Neither frequency means more evidentiary votes.** Promote an out-of-bounds condition to interpretation when the actor is a chart ruler or root, sits on an angle, participates in the principal aspect/declination dialogue, or changes the meaning of a lunar or eclipse chapter. Preserve sect, dignity, houses, exact pair phase and the governing ingress. An out-of-bounds actor is a symbol of operating beyond customary range, with constructive and shadow uses; it is not a prediction of illegal conduct or institutional rupture.

This receipt screens the **100 distinct syzygy moments**, not all 16 cardinal ingress wheels or every exact planetary-pair chart. Those require their own motion/declination pass during the annual re-hearings. It does not retype Saros, Metonic or Moon-family ancestry, correct unrelated source producers, compare factual Chronicle records, or register a Forecast Ledger call.

Sources: `00 - Index/Mundane Astrology Reference — Katie's Method.xlsx` (Modifiers, Aspects); [[Reading the Charts — START HERE]]; [[2027–30 Sky Storyline — Coverage and Source Audit]]; all complete-bone packets named per chart in [[2027–30 Out-of-Bounds Screen — COMPUTED DRAFT.json]]; `build_chart_reading_bones_2025.py` and `swiss_ephemeris.py` using the vendored DE441 files.
