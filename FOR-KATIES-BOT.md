# For Katie's Bot

This is the Freedom 250 research mirror. Its bot doorway and read-only shared brain API are intentionally discoverable; the wider human archive remains unlisted. Start with the [crawler-friendly HTML instructions](intelligence/bot-instructions.html), then open the [plain static bot index](intelligence/bot-index.html).

Fast machine routes:

- [Crawler-friendly instructions](intelligence/bot-instructions.html)
- [Static bot index](intelligence/bot-index.html)
- [Package interior inventory](intelligence/package-inventory.html)
- [Package interior inventory JSON](intelligence/api/v1/package-inventory.json)
- [Shared brain API bootstrap](intelligence/api/v1/index.json)
- [Layered research inventory](intelligence/api/v1/inventory.json)
- [Recent computer activity](intelligence/api/v1/activity.json)
- [OpenAPI description](intelligence/api/v1/openapi.json)
- [Compact package index](intelligence/api/v1/packages.json)
- [All package materials](intelligence/api/v1/materials.json)
- [Research grammar](intelligence/RESEARCH-GRAMMAR.md)
- [Human bot doorway](intelligence/for-katies-bot.html)

Every package record declares `public_full_text` and a crawler-friendly `full_text_url`. A public reading provides a static HTML `reading_url`; `access_state: public_machine_data` provides complete structured JSON at `data_url`; private metadata declares `public_full_text: false` and `access_state: private_by_design`. A failed declared public URL is an access or crawler problem, not a privacy signal. Research pages carry a compact `f250-machine-header` JSON block naming their page type, package IDs, clocks and exact API routes. Package interiors separate orientation, findings, evidence, monitoring, methods, presentation and supporting materials. Treat modification times as computer recency signals, not proof that findings changed. Preserve evidence cutoffs, cutoff notes, structured-data as-of dates and evidence vocabularies; distinguish authority from operation; cite exact pages or data objects; and freshly verify claims that must be current today.
