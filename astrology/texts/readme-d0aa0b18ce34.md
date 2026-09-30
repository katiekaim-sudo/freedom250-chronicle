# Planetary Relationship Clocks — Review Package

**Status:** `live_reference_review`  
**Authority:** Astrology Files review package; not chart-reading doctrine, political evidence, Forecast Ledger authority, or installed-app state  
**Astrology evidence credit:** `0`

## Result

This package adds the missing relationship layer without redefining the governed Long Clocks:

- Planets retain stable archetypal motivations but receive no fixed plot assignments; the pair's changing relationship carries the arc.
- A chart snapshot records one relationship state, while the ordered relationship history preserves motion across ingresses, lunations, retrograde returns, and repeated exact passes.
- **10** existing Jupiter-through-Pluto Long Clocks remain exactly as governed by DR-065.
- **17** Mercury-, Venus-, and Mars-led pairs receive a continuous geocentric phase clock under the existing DR-020 grammar.
- **1** pair, Mercury–Venus, remains direct geometry only because it has no geocentric opposition and its directed hand reverses.
- The 17 phaseable pairs resolve into **55** bracketing conjunction families with **73** exact passes; Mercury–Venus retains six verified but ungrouped crossings.
- **30** governed ingress/lunation chart bones are projected through all **28** non-luminary relationships.
- The graph contains **840** relationship states: 300 unchanged Long Clock states, 510 phaseable inside-pair states, and 30 Mercury–Venus limited-geometry states.
- Every chart now carries an inspectable direct/phase overlap partition. Its corpus control identifies December 9 as the only 30-chart snapshot with more direct dialogues than phase-nameable relationships and preserves the December 9 → Capricorn ingress → December 24 handoff without converting counts into strength.
- Consecutive equal-count controls expose two hidden cast changes: the March 19 → Aries ingress phase-admission swap from Venus-led to Mars-led relationships with the direct cast unchanged, and the September 11 → Libra ingress four-for-four turnover hidden beneath identical field totals.

The new layer is deterministic. It contains no `generated_at`, daily snapshot, plot ownership, verdict, causal claim, forecast permission, or evidence credit.

## Files

- `planetary_relationship_registry.json` — 28-pair catalog, enduring questions, domains, source paths, and authority fences.
- `planetary_relationship_clock_graph.json` — deterministic 30-chart × 28-pair geometry graph with direct/phase overlap metrics and corpus controls.
- `inside_planet_conjunction_families.json` — proposed 17-pair seed-family/cadence ledger plus unresolved Mercury–Venus crossings.
- `build_planetary_relationship_clocks.py` — graph builder using the live phase, aspect, and chart-bone engines.
- `validate_planetary_relationship_clocks.py` — set, authority, determinism, and 300-state Long Clock parity checks.
- `METHOD AND DOCTRINE REVIEW.md` — the adopted-for-this-test reading grammar and unresolved decisions.
- `WINTER TO ARIES 2026 RELATIONSHIP HISTORY.md` — closed-season all-pair maps, chapter histories, cross-ingress phase turns, storyline continuity, misses, and evidence boundaries.
- `CANCER 2026 RELATIONSHIP CLOCK ANALYSIS.md` — first ingress/lunation stress test across Crypto, Iran, and AI.
- `THE PLOT CHANGES HANDS — LIBRA TO CAPRICORN 2026 RELATIONSHIP HISTORY.md` — prospective late-year all-pair map, chapter-ruler relay, Venus–Pluto three-pass bracket, Mars–Pluto/Mars–Jupiter handoff, December traffic-to-context field handoff, hierarchy correction preserving the September Virgo New Moon as lunar chapter owner, and a story-room grammar translating ingress, lunation, phase strike, quarter, transit, family and dispositors into distinct production jobs.

## Rebuild and validate

```bash
python3 "03 - Astrology/Astrology Files/Persona & Relationship Work/Planetary Relationship Clocks 2026-08-30/build_planetary_relationship_clocks.py"
python3 "03 - Astrology/Astrology Files/Persona & Relationship Work/Planetary Relationship Clocks 2026-08-30/validate_planetary_relationship_clocks.py"
```

Expected result:

```text
RELATIONSHIP CLOCKS VALID: 30 charts · 28 relationships · 840 states · 300 Long Clock parity states · 540 inside-pair states · 55 seed families · 73 exact seed passes
```

## Promotion boundary

Nothing here changes locked chart readings, Transit Weather, Long Clocks,
Daybreak, Chart Readings, Astrology Spine, Forecast Ledger, Research Desk, or
the installed Observatory app. The package is discoverable in Astrology Files;
its authored histories remain contextual review layers. A later reviewed
decision can promote a geometry-only sibling graph; authored interpretations
and story use remain separate decisions.

One existing downstream issue was found during the audit: a Planetary Show mapping package pins an older whole-file hash of the volatile Long Clock stack. The relationship graph deliberately avoids that source-receipt pattern, but this package does not repair the older receipt.
