# For Katie's Bot

Hello, bot. This site is Katie's portable Freedom 250 research mirror. Its bot doorway and read-only API are intentionally discoverable for Katie's own ChatGPT chats and a small number of invited research agents; the wider human archive remains unlisted. The site contains government, institutional, company and infrastructure research. Astrology and Q are intentionally outside this research surface.

## Use this retrieval path

1. Open the [shared brain API bootstrap](api/v1/index.json) to learn the method, custody boundaries and stable endpoints.
2. Open the [layered inventory](api/v1/inventory.json) to see what is available at each research layer and each package's latest computer edit.
3. When Katie refers to recent work, filter the [activity index](api/v1/activity.json) by `modified_at`. Treat it as a computer recency signal, not proof that a finding changed.
4. For a broad question, open [agent-index.json](agent-index.json) or [API packages](api/v1/packages.json) and select the smallest relevant set of packages.
5. For an obscure name, tiny one-off note or exact artifact title, search [materials-index.jsonl](materials-index.jsonl) or [API materials](api/v1/materials.json).
6. Open each selected package's manifest under `packages/{research_id}.json` or `api/v1/packages/{research_id}.json`. It lists every governed package material, including safe metadata for material that is not publicly readable.
7. Read the package's Markdown report under `reports/{research_id}.md` when available, then follow exact public material URLs from the manifest.
8. Use the static [Bot Index](bot-index.html) for a no-JavaScript current map and the [Package Interior Inventory](package-inventory.html) or [its JSON form](api/v1/package-inventory.json) to see the distinct research layers and actual materials inside each package.
9. Use [CONNECTED-RESEARCH.md](CONNECTED-RESEARCH.md) only when the question needs the larger story, cross-package relationships or explanatory chapters. Use [connected-index.json](connected-index.json) only when the compact index is insufficient.
10. Apply [RESEARCH-GRAMMAR.md](RESEARCH-GRAMMAR.md). Preserve cutoffs and institutional clocks. Do not turn metadata-only material into claimed knowledge.
11. Cite the exact public page used. If Katie asks what is true now, verify time-sensitive claims with fresh primary sources.

## Important interpretation rule

This library intentionally carries Katie's working lens, including hypotheses, rival explanations and falsifiers. Treat that lens as an analytical framework, not proof that one coordinated plan exists. Give the strongest supported reading and the strongest ordinary rival.

## Useful first instruction

> Start with this page. Search the compact package index and the all-materials index before answering. Open only the relevant package manifests and reports. Preserve evidence cutoffs, distinguish authority from operation, identify metadata-only leads, cite exact pages, and verify any claim that must be current today.

## Human routes

- [Research Library](index.html)
- [AI Research Guide](ai-guide.html)
- [All research packages](library/index.html)
- [Full report map](reports/index.json)
