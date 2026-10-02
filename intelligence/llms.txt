# For Katie's Bot

Hello, bot. This site is Katie's portable Freedom 250 research mirror. Its bot doorway and read-only API are intentionally discoverable for Katie's own ChatGPT chats and a small number of invited research agents; the wider human archive remains unlisted. The site contains government, institutional, company and infrastructure research. Astrology and Q are intentionally outside this research surface.

## Use this retrieval path

1. Open the crawler-friendly HTML instructions at [bot-instructions.html](bot-instructions.html). The Markdown file is only a redundant mirror.
2. Open the [shared brain API bootstrap](api/v1/index.json) to learn the method, custody boundaries and stable endpoints.
3. Open the [layered inventory](api/v1/inventory.json) to see what is available at each research layer and each package's latest computer edit.
4. When Katie refers to recent work, filter the [activity index](api/v1/activity.json) by `modified_at`. Treat it as a computer recency signal, not proof that a finding changed.
5. For a broad question, open [agent-index.json](agent-index.json) or [API packages](api/v1/packages.json) and select the smallest relevant set of packages.
6. For an obscure name, tiny one-off note or exact artifact title, search [materials-index.jsonl](materials-index.jsonl) or [API materials](api/v1/materials.json).
7. Open each selected package's manifest. If `public_full_text` is true, read its `full_text_url` before treating the summary as the research.
8. For each material, `public_full_text: true` guarantees the complete public object. A normal reading has a crawler-friendly static `reading_url`; `access_state: public_machine_data` has a complete JSON `data_url`. `public_full_text: false` plus `access_state: private_by_design` means metadata only. If a declared public URL fails, report a crawler or delivery failure rather than calling it private.
9. Use the static [Bot Index](bot-index.html) for a no-JavaScript current map and the [Package Interior Inventory](package-inventory.html) or [its JSON form](api/v1/package-inventory.json) to see the distinct research layers and actual materials inside each package.
10. The Research Library is organized into ten Research Rooms. Use [CONNECTED-RESEARCH.md](CONNECTED-RESEARCH.md) for the room map (Katie's thesis, each room's shelves, and which studies sit in more than one room). Every package manifest names its `home_room` and `also_in` rooms under `classification`. Use [connected-index.json](connected-index.json) only when the compact index is insufficient.
11. Apply [RESEARCH-GRAMMAR.md](RESEARCH-GRAMMAR.md). Preserve cutoffs and institutional clocks. Do not turn metadata-only material into claimed knowledge.
12. Cite the exact public page used. If Katie asks what is true now, verify time-sensitive claims with fresh primary sources.

## Important interpretation rule

This library intentionally carries Katie's working lens, including hypotheses, rival explanations and falsifiers. Treat that lens as an analytical framework, not proof that one coordinated plan exists. Give the strongest supported reading and the strongest ordinary rival.

## Useful first instruction

> Start with this page. Search the compact package index and the all-materials index before answering. Open only the relevant package manifests and reports. Preserve evidence cutoffs, distinguish authority from operation, identify metadata-only leads, cite exact pages, and verify any claim that must be current today.

## Human routes

- [Research Library](index.html)
- [AI Research Guide](ai-guide.html)
- [All research packages](library/index.html)
- [Full report map](reports/index.json)
