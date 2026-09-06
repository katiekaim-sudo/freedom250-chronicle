# 2020 COVID Authority Spine

**Evidence cutoff:** July 27, 2026  
**Status:** `active` workbench package  
**Scope:** bounded 2020 comparison baseline; official primary sources, not a
news archive

## Purpose

This package preserves the small set of 2020 source objects needed to compare
later COVID releases, testimony and retrospective claims against what the
responsible institution actually issued, knew, authorized or changed at the
time.

It is not a general pandemic history. It does not attempt to collect every
briefing, state order, CDC update, clinical paper, grant, contract or social
post.

## Admission rule

A source object enters only if it did at least one of the following:

1. created or materially changed legal authority;
2. stated official knowledge or guidance at a major turning point;
3. authorized, revised or revoked a major intervention;
4. documented a material funding, oversight or intelligence-process object; or
5. became a direct comparison object in a later official disclosure.

Official source material may be preserved locally or routed to an already
preserved package or live-vault record. Stable pointers are preferred over
duplicate copies.

## Time-and-place rule

Preserve the finest source-supported clock available: date, exact time, time
zone and place. Signing, occurrence, filing, publication, effective,
emergency-beginning, declassification and later-release clocks remain separate.
Use `NR` when a source does not report a time or place; do not infer one from a
filename, retrieval time or surrounding chronology. Scheduled and observed
times must also remain distinct.

## Read order

1. `COVID_2020_AUTHORITY_SPINE.md` - merged chronological and comparison view.
2. `AUTHORITY_SPINE_REGISTRY.json` - machine-readable object and clock registry.
3. Lane handoffs:
   - `lanes/LEGAL_AUTHORITY_LANE.md`
   - `lanes/PUBLIC_HEALTH_GUIDANCE_LANE.md`
   - `lanes/ORIGINS_FUNDING_LANE.md`
   - `lanes/COUNTERMEASURES_AND_VACCINES_LANE.md`
4. `SOURCE_INVENTORY.generated.json` - local captures, sizes, hashes and PDF
   page counts.
5. `Source Documents/` - preserved official source files.

## Evidence firewalls

| Do not collapse | Into |
|---|---|
| announcement or stated goal | legal authority or completed implementation |
| declaration date | publication, effective or emergency-beginning date |
| guidance at one date | permanent institutional position |
| expert input or briefing | authorship or control of a finished assessment |
| prime award | subaward, expenditure, recipient or payment |
| research capability | identity or origin of SARS-CoV-2 |
| advisory committee vote | FDA authorization |
| EUA | approval |
| authorization | clinical effectiveness in every population or later variant |
| declassification or later release | contemporaneous public availability |

## Existing-holdings rule

- Relevant 2020 executive orders already preserved in the live vault are
  referenced, not copied.
- Records already preserved inside the 2026 ODNI COVID and biolab package are
  addressed by exact local path and packet page where possible.
- The workbench remains outside-model research. If selected material later lands
  in the live vault, the vault copy wins.

## Excluded by design

- news articles and headline collections;
- daily press briefings;
- redundant versions of unchanged agency guidance;
- comprehensive state and local order collections;
- broad social-media retrospectives;
- every clinical or epidemiological paper;
- every COVID contract, grant or enforcement matter.

## Rebuild and validation

Run with the bundled Python environment:

```bash
python3 tools/build_source_inventory.py
python3 tools/validate_authority_spine.py
```
