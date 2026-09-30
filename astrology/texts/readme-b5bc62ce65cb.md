# Inside-Planet Conjunction Persona Review

> **Frozen 2026-09-25 (DR-080).** This package's chart math lived in the Sentient Sun folder
> (`chart_calculator.py`, `reading_engine.py`, `canonical_traditional_tables.py`), which was rebuilt on
> 2026-09-25 and no longer contains those files, and its seed charts were computed on the Moshier
> ephemeris. Its builders can no longer run. The persona material stays as dated, zero-vote provenance.
> The conjunction radix layer now lives in the vault — `99 - Templates/long_clock_radices.json`
> (Swiss/JPL DE441, with an angle-determinacy receipt). Treat any radix ASC/MC or clock in this package
> as superseded by that file.

**Status:** `proposal_for_review`  
**Presentation route:** Astrology Reference → Sky & Charts  
**Official Research evidence credit:** `0`  
**Live-vault or Observatory admission:** none

## Answer first

The conjunction chart and persona layer is useful, but not uniformly so.

- Every one of the **73** exact passes in the **55** phaseable Mercury-, Venus-, and Mars-led families now has a factual Washington, D.C., Whole Sign conjunction chart.
- All **six** Mercury–Venus crossings have factual charts, but no false phase family or persona.
- **35** first-later solar-crossing personas are calculated as review candidates.
- **Three** candidates are withheld because the next conjunction family begins first.
- **Seventeen** future bracketing families are withheld because their successor boundary is not present.
- The five governing multipass families use the earliest pass only as a **proposed** display/persona coordinate. The family remains the seed, and Katie's disposition is still required.

The absence of a persona is therefore visible information about the method's gate. It is never silently treated as failed or unfinished work.

## What this package tests

The parent relationship clock asks what developmental chapter a planetary pair occupies. The exact conjunction chart adds the condition and operating structure of the family seed. A persona candidate then asks whether the conjunction degree, when carried by the Sun in the first later crossing, exposes a useful operating arena, public route, focal distinction, or hidden term.

That extra layer may narrow a storyline question. It cannot discover a fact, prove an event, add a convergence vote, own a plot, or change timing.

## Read order

1. `CONJUNCTION PERSONA METHOD.md` — identity, gates, reading order, and prohibited inferences.
2. `LIFECYCLE AND ANCHOR FINDINGS.md` — why 35 candidates exist while 20 families have none.
3. `CONJUNCTION PERSONA SYNTHESIS.md` — pair-level yield and the strongest pilot hearings.
4. `FIVE STRONGEST PILOT STRESS TEST.md` — fixed-record seed-only versus seed-plus-persona tests, dependency findings, falsifiers, and two prospective observation locks.
5. `hearings/` — one cycle-level review note for each of the 17 phaseable delivery clocks.
6. `charts/index.html` — linked factual chart gallery.
7. `data/index.json` — machine index and lifecycle census.

## Package map

| Path | Role |
|---|---|
| `data/families/*.json` | Full pass charts, candidate gate, persona facts, focal lenses, overlay, and provenance for all 55 families. |
| `FIVE STRONGEST PILOT STRESS TEST.md` | Anti-cherry-pick comparison showing which pilot personas add discrimination, restate governing charts, depend on adjacent events, or remain unresolved. |
| `data/exceptions/mercury-venus.json` | Six exact crossing charts and the no-family/no-persona ruling. |
| `charts/seeds/` | 79 standalone conjunction charts: 73 phaseable passes plus 6 Mercury–Venus crossings. |
| `charts/personas/` | 35 calculated standalone persona candidates. |
| `charts/overlays/` | 35 seed/persona biwheels. |
| `PACKAGE_ARTIFACT_MANIFEST.csv` | Workbench custody delegation for the rebuildable generated sidecars, with producer, visibility, byte count, and hash. |
| `manifest.json` | Detailed custody metadata for every package artifact plus pinned method/code/source hashes and artifact hashes. |
| `build_inside_planet_conjunction_personas.py` | Reproducible factual builder. |
| `validate_inside_planet_conjunction_personas.py` | Fail-closed identity, root, gate, authority, route, and custody validator. |

## Rebuild and validate

```bash
python3 "03 - Astrology/Astrology Files/Persona & Relationship Work/Inside Planet Conjunction Persona Hearings 2026-08-30/build_inside_planet_conjunction_personas.py"
python3 "03 - Astrology/Astrology Files/Persona & Relationship Work/Inside Planet Conjunction Persona Hearings 2026-08-30/validate_inside_planet_conjunction_personas.py"
```

Expected result:

```text
PASS families=55 passes=73 conjunction_charts=79 personas=35 successor_collisions=3 bracketing=17 mercury_venus=6
```

Returned ephemeris flags show Moshier fallback in the present runtime. Independent Astro Gold comparison remains pending. No artifact in this package changes the ten governed Long Clocks, the live chart hierarchy, a factual plotline, a watch, the Forecast Ledger, the vault, or the installed app.
