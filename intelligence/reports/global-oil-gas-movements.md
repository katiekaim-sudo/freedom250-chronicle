# Global Oil and Gas Movements 2026

Status: active multi-wave Research Desk project; Waves 0, 3, 4, 5 and 7 have
initial governed products; Wave 6 has a validated working globe; Waves 1 and 2
remain in source recovery  
Evidence cutoff: 2026-09-15, America/New_York  
Research ID: `global-oil-gas-movements`

## The question

How are oil and gas physically moving, who owns and permits each movement, how
are war, sanctions and commercial agreements changing the route, and which
announced changes have actually reached production, lifting, payment and final
receipt?

## Short answer

There is no single honest "oil flow" layer. The project must keep at least six
records separate and join them only when a shared cargo, vessel, contract or
payment key permits it:

```text
PHYSICAL    field → gathering → pipeline/truck → storage → terminal/STS → vessel → discharge
COMMERCIAL  allocation → contract → nomination → title/risk transfer → buyer
IDENTITY    grade/assay → quantity certificate → B/L → origin → destination
PERMISSION  port/flag/class → insurance → sanctions/license → customs/import authority
PAYMENT     invoice/LC → bank/correspondent → controlled or sovereign account → beneficiary
OBSERVATION AIS/port call/customs/market estimate → confidence + clock + known blind spots
```

The first live read is already material. The Middle East war has made Hormuz,
the Red Sea and bypass capacity the dominant near-term supply constraint; the
September IEA and EIA estimates show Gulf crude and product trade still far
below its pre-war pattern. Russia matters not only as crude supply but as a
second simultaneous refined-product disruption. Venezuela is a different kind
of hinge: permissions, U.S.-controlled payment accounts, a new NABEP
governance/offtake arrangement, and separate Chevron and Eni operating
agreements now exist. Venezuela already produces about 1.15–1.20 million b/d
and the latest preliminary U.S. receipt was about 0.60 million b/d, but no
audited public source establishes a large uncommitted tank pool. Brownfield
repairs and workovers are the sub-one-year opportunity; major drilling,
upgrader/refinery rehabilitation and offshore gas exports sit on longer clocks.
The United States is already a material production-processing-trading hub:
June gross exports were 4.735 million b/d of crude plus 7.805 million b/d of
petroleum products, while 1H26 LNG exports averaged 17.4 Bcf/d. Venezuela can
improve Gulf Coast heavy-crude feed and product conversion but is not required
for the United States to remain a major exporter. The May China trade framework
did not publish an oil or LNG quantity; the separate PetroChina–Sabine Pass LNG
contract is the firmer commercial object and must now be joined to named cargos.
The current “shortage” is selective rather than universal: global inventories
are drawing and diesel/distillate is genuinely tight, especially on the U.S.
East Coast, while U.S. commercial crude is nearly flat year over year and jet,
propane and forecast natural-gas storage do not show a national shortage.
Removing Russia sanctions would first lower shipping/payment friction and
reroute existing crude; it would not count already-exported barrels again or
repair Russia's disrupted refineries. Diesel now has a dedicated route layer:
ten material June 2026 U.S. destination lanes account for about 0.953 million
b/d, or 66.5% of national distillate exports, led by Mexico, Brazil and the
Netherlands. Historical Russian rerouting and Northwest Europe replacement
lanes remain visible as baselines, not current 2026 movement. The deeper
supplier test finds that the Middle East-replacement explanation is direct for
the United Kingdom and Netherlands and combines with Russian displacement for
Brazil. Most selected Latin American buyers were already predominantly supplied
from the United States or nearby systems, so their exposure is indirect
competition for the same Atlantic barrels. The current June routes now resolve
to PADD origin: PADD 3/Gulf Coast overwhelmingly carries the material network,
with PADD 5 providing meaningful support to Mexico, Chile and Peru.
The monetary companion now decomposes the “petrodollar” into benchmark,
contract, invoice, funding, hedging, settlement, receipt, conversion and
reinvestment layers. It finds no controlling public 50-year Saudi
oil-only-in-dollars covenant and treats non-dollar capacity separately from a
proved cargo payment.

## Read first

1. Project Constitution and Wave Plan
2. Live Baseline — September 15, 2026
3. Middle East Route State Matrix
4. Russia Route and Sanctions Matrix
5. Global Replacement Supply and Buyer Rewiring Matrix
6. Global Gas and LNG Network
7. U.S. Energy Hub and Buyer-Deal Execution Matrix
8. Shortage Reality and Russia Sanctions-Relief Test
9. Global Diesel Route Network
10. Diesel Supplier Dependence and Substitution Test
11. Venezuela Deal Execution Ledger
12. Venezuela OFAC Permission Matrix
13. Venezuela Early-2027 Flow and Readiness Test
14. Venezuela Resource-to-Usable-Supply Ladder
15. Petrodollar System monetary companion
16. Return Trigger and Source-Gap Matrix
17. Working Global Oil and Gas Globe
18. Map Data Contract
19. Globe Reuse Decision
20. Map Asset Provenance
21. Route Edge Starter

## Working globe

The package-local globe currently projects 113 selected map features and 82
nodes from 148 governed route/state records. It provides theatre, commodity,
layer, effective-date and text filters; every mapped record exposes its source,
state, quantity/unit, clock, claim limit and next receipt.

Globe.GL/WebGL remains the preferred renderer. If the host browser or embedded
app cannot create a WebGL context, the same governed data automatically renders
through a native SVG orthographic compatibility globe with drag, zoom, filters
and route/node selection preserved.

Owners and build chain:

- `ROUTE_EDGE_STARTER.csv` owns route/state/quantity claims.
- `energy_map_registry.json` owns approximate node and route geometry.
- `energy_globe_template.html` owns presentation.
- `build_energy_globe.py` regenerates the output and build receipt.
- `validate_energy_globe.py` is read-only and checks custody, vocabulary,
  sources, coordinates, assets, compatibility fallback, output hash and
  JavaScript syntax.

Rebuild and check from the Workbench root:

```bash
python3 "Research Packages/Global Oil and Gas Movements 2026/build_energy_globe.py"
python3 "Research Packages/Global Oil and Gas Movements 2026/validate_energy_globe.py"
```

## Existing research retained as owners

- `Research Packages/Iraq Oil and Logistics/` remains the cargo-level ancestor
  for Qayarah, Khor al-Zubayr/Berth 41, tank/floater/STS, vessel identity,
  insurance, documentary credit and sovereign receipt. This project links to
  it; it does not flatten or replace it.
- `Research Packages/Iran Financial Pressure and Banking System 2026-08-07/`
  remains the owner for Iran's banking, sanctions and foreign-earnings pressure
  lanes.
- `Research Packages/International Monetary Transition/14 - Petrodollar System 1945-2026/`
  owns the dollar-oil history, transaction and balance-sheet explanation. This
  physical-route package does not infer payment currency or reserve allocation
  from cargo origin alone.
- `Research Packages/Federal Government Weekly Delta 2026-09-03/` retains the
  original bounded OFAC Venezuela 51D/54C/55A finding.
- Chronicle event notes remain event evidence. They are not imported into this
  Research Desk package and do not substitute for the controlling official
  object.

## Boundary

This package is factual research. It contains no astrocartography or astrology
interpretation. A later Sky & Charts comparison may notice overlaps only after
this factual record and a separately computed astrology record each stand on
their own.

No Chronicle watch, Chronicle synthesis change, installed-app build, public
site publication, commit or push is authorized or implied by this package.
