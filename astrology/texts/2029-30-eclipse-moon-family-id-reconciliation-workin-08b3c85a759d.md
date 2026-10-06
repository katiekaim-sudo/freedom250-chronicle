---
title: "2029–30 Eclipse Moon-Family ID Reconciliation — Working Receipt"
type: astrology_source_integrity_receipt
status: computed_draft_unsealed
created: 2026-10-11
developed_through: 2026-10-11
parent_map: "[[The Sky Through 2030 — Working Story Map]]"
evidence_credit: zero
---

# 2029–30 Eclipse Moon-Family ID Reconciliation

The first [[2029 Eclipse Genealogies — COMPUTED DRAFT.json]] and [[2030 Eclipse Genealogies — COMPUTED DRAFT.json]] drafts reported no admitted Pessin lineage for any of their nine eclipses. That was wrong for **two lunar eclipses**. The eclipse lookup expected an event ID such as `lun-2029-06-26-fu-lunar`, while `moon_lineages.json` registered the same Full Moon under a generic `lunation-2029-06-26-fm` ID. Both generic phase events are marked as eclipses, and each exact phase clock agrees with the eclipse syzygy to less than one second. The corrected working packets carry the registered lineage and retain both IDs with an explicit resolution note.

| Eclipse at exact syzygy | Generic phase event in `moon_lineages.json` | Admitted Pessin role | Clock difference |
|---|---|---|---:|
| **June 26, 2029 Capricorn total lunar** · 03:22:21 UTC | `lunation-2029-06-26-fm` · 03:22:20.640566 UTC | Full of the **December 27, 2027 Capricorn New Moon** | 0.359 s |
| **June 15, 2030 Sagittarius partial lunar** · 18:41:01 UTC | `lunation-2030-06-15-fm` · 18:41:01.219320 UTC | Full of the **December 16, 2028 Sagittarius New Moon** | 0.219 s |

The 2027 Capricorn seed's other registered phases are First Quarter September 25, 2028 and Last Quarter March 26, 2030. The 2028 Sagittarius seed's other registered phases are First Quarter September 15, 2029 and Last Quarter March 16, 2031. Both families are **complete lines already present** in `moon_lineages.json`; their interpretations remain unreviewed. The seed cutoff of January 2029 limits new admitted seeds, **not Full phases of older seeds**.

[[2029 Gemini Double-Eclipse Chapter — Working Hearing]] now gives the June 26, 2029 return a whole-chart hearing beside its immediate Gemini chapter and nested Cancer ingress.

This correction changes Moon-family identity for those two eclipses only. Saros, Metonic, global type and Washington visibility are untouched. The other seven 2029–30 eclipses still have no complete Pessin line admitted in the current projection. The ordinary July 15, 2030 Capricorn Full remains the separate registered Full of the January 14, 2029 Capricorn solar eclipse.

[[2030 Gemini–Cancer Eclipse Relay — Working Hearing]] now hears the June 15, 2030 partial lunar Full as the long phase of the December 2028 Sagittarius seed inside the separate June 2030 Gemini solar chapter. [[2029–30 Moon-Family and Governor Crosswalk — Working Receipt]] also carries these two eclipsed Fulls in a broader date/phase/degree/clock and actual-governor audit of all 13 admitted 2029–30 long Fulls.

**Source return gate:** `build_eclipse_genealogies.py` currently matches a single eclipse-style `phase_event_id` and can recreate the false absence if run again. Its canonical lookup should resolve a unique event by exact UTC phase, kind and eclipse flag, while retaining the source's original ID. The corrected working JSON packets are a dated reconciliation, not a silent change to `moon_lineages.json`. Any future regeneration should recheck these two event identities before replacing the packets.

Sources: `99 - Templates/moon_lineages.json` (`coverage`, `phase_events`, `lineages`); `99 - Templates/build_eclipse_genealogies.py` (`moon_family_for`); [[2029 Eclipse Genealogies — COMPUTED DRAFT.json]]; [[2030 Eclipse Genealogies — COMPUTED DRAFT.json]]; [[2029–30 Lunar Chapters — Computed Working Index]]. No factual Chronicle event or political interpretation was used.
