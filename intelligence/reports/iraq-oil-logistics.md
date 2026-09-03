# Iraq Oil Provenance Logistics Ledger

Updated: 2026-07-15  
Status: pending — primary-source factual layer; not yet folded into the live vault  
Scope: Qayarah production and road movement; Khor al-Zubayr and Berth/Jetty 41; floating storage and ship-to-ship transfer; cargo documents; vessel identity; insurance; bank routing; sovereign receipt  
Source rule: Iraqi government and state-company records, U.S. Treasury/OFAC, CBI, MoF, EITI official records, official corporate/ship/insurance registries. Treasury narrative allegations remain allegations unless an operative or adjudicative record independently establishes them.

## Short answer

The logistics plotline is not one chain. It is five records that can agree, diverge or be falsified independently:

```text
PHYSICAL   field → truck/pipeline → tank/floater → terminal/STS → vessel
TITLE      allocation → sale contract → loading receipt → bill of lading
IDENTITY   assay → quantity/quality certificate → declared origin → customs/sanctions attestation
PERMISSION flag/class → port/STS license → P&I/war cover → OFAC state/license → bank acceptance
PAYMENT    invoice/LC → paying bank → correspondent/custodian → sovereign or private receipt → final beneficiary
```

The strongest verified overlap is geographic and procedural:

- SOMO publicly reports authorized Qayarah crude cargoes loaded from named floating storage units near Khor al-Zubayr.
- OFAC identifies designated VS Oil Terminal FZE at Khor al-Zubayr Freezone Road, Jetty 41, and alleges that its tanks and nearby STS transfers were used to blend Iranian and Iraqi oil.
- SOMO later offered expressly Iraqi-origin fuel oil from Berth 41 and obtained a transaction-specific OFAC license for sale to non-sanctioned parties.
- The license preserves a lawful cargo lane at the same location. Its existence does not prove why the license was required or validate Treasury's entire narrative.

The operative question is therefore not whether Khor al-Zubayr or Berth 41 is "licit" or "illicit." It is which cargo, tank, vessel, document, bank and license applied at a particular time.

## Evidence and status vocabulary

| Label | Meaning |
|---|---|
| `A-OPERATIVE` | Contract term, tender, license statement, sanctions listing, registry entry or other record that changes legal/operating state. |
| `B-OFFICIAL-REPORTING` | Government or state-company report describing an occurred cargo, movement, account or institutional practice. |
| `C-OFFICIAL-ALLEGATION` | Factual allegation in an official sanctions or enforcement narrative; not automatically adjudicated. |
| `D-ENTITY-CLAIM` | Entity statement about its own role, ownership, cover or operations without an independent operative record. |
| `GAP` | Required document or join key not publicly located. |

Use one event status and one clock per row. Do not turn a missing field into the status of the whole transaction.

## Controlling non-conflations

1. Iraqi public ownership of the resource is not SOMO corporate ownership, CBI custody, FRBNY custody or buyer title.
2. A truck route can be authorized. The presence of trucks is not evidence of diversion.
3. A terminal or berth can host both authorized and alleged illicit traffic.
4. Physical blending, documentary origin and legal title are separate questions.
5. A bill of lading proves defined loading facts; it does not prove origin, final buyer, payment or sovereign receipt by itself.
6. A P&I entry or certificate does not prove voyage-specific cover, sanctions legality or claim payability.
7. An OFAC designation, OFAC license and court judgment are different legal objects.
8. TBI's documented petroleum-product role is not proof that every crude-oil payment passes through TBI.
9. Iraq 2/OPRA at FRBNY is the documented sovereign oil-receipt rail; private shadow-sale proceeds must not be inserted into it without a payment record.
10. The 2021 SOMO-versus-CBI receipt difference is an unreconciled accounting/cash gap, not established theft and not evidence of the alleged VS Oil chain.

## Master logistics map

### Authorized Qayarah path documented in public records

```text
Qayarah field, Nineveh
  operator/development role: Sonangol
  Iraqi beneficiary/field company: North Oil Company
        ↓
SOMO allocation or public tender
        ↓
buyer takes title/risk at the contractually stated gate
        ↓
road tanker and/or other authorized transport
        ↓
field exit, refinery, authorized terminal or floating storage
        ↓
SOMO vessel nomination/loading controls
        ↓
bill of lading + commercial invoice + quantity/quality certificate
        ↓
documentary credit or advance payment under the applicable contract
```

### Alleged shadow branch described by Treasury

```text
favored Iraqi allocation and/or Iranian-origin cargo
        ↓
trucks, pipelines or Iranian-linked vessels
        ↓
VS Oil tanks at Khor al-Zubayr and/or nearby STS transfer
        ↓
physical mixing of Iranian and Iraqi oil
        ↓
forged or improperly authenticated Iraqi provenance
        ↓
sale into a market otherwise restricted to Iranian-origin oil
        ↓
private payment / hard-currency return to Iran or militia-linked beneficiaries
```

Treasury has not publicly supplied the truck manifests, terminal receipts, tank logs, lab assays, bills of lading, buyer invoices or bank messages needed to join that alleged chain cargo by cargo.

## Entity and facility register

| Entity/facility | Exact role in located record | Status | What remains unestablished | Primary source |
|---|---|---|---|---|
| Iraqi people | Constitutional owners of Iraqi oil and gas | `A-OPERATIVE` | Direct transaction role is not applicable | [Iraqi Constitution](https://iq.parliament.iq/en/wp-content/uploads/sites/3/2024/04/Constitution-of-the-Republic-of-Iraq.pdf) |
| Ministry of Oil | Sector ministry; approves SOMO allocations and supervises state oil companies | `A-OPERATIVE` / `B-OFFICIAL-REPORTING` | Cargo-level approval and signatory records | [SOMO policy](https://www.somooil.gov.iq/about/policy) |
| North Oil Company | Iraqi beneficiary named for the Qayarah seismic project | `B-OFFICIAL-REPORTING` | Exact current field-title and operating-agreement terms | [Oil Exploration Company](https://www.oec.oil.gov.iq/en/news/ministry-of-oil-signs-contract-of-implementing-3d-seismic-survey-for-al-qayarah-field-with-the-angolan-sonangol-company/) |
| Sonangol | Named Qayarah operator/developer in the Iraqi OEC record | `B-OFFICIAL-REPORTING` | Current production entitlement, fees and lifting rights | [Oil Exploration Company](https://www.oec.oil.gov.iq/en/news/ministry-of-oil-signs-contract-of-implementing-3d-seismic-survey-for-al-qayarah-field-with-the-angolan-sonangol-company/) |
| SOMO | Sole officially authorized marketer/exporter; allocation, contract, vessel acceptance, pricing, invoice and cargo-document role | `A-OPERATIVE` | Current executed crude contracts and cargo-level payment instructions | [Duties](https://somooil.gov.iq/about/duties), [policy](https://www.somooil.gov.iq/about/policy) |
| Iraqi Higher Maritime Authority | Regulates and licenses STS activity in Iraqi waters under the cited 2019 law | `B-OFFICIAL-REPORTING` | Public STS license register, coordinates and vessel nominations | [SOMO maritime readout](https://somooil.gov.iq/events/108) |
| Khor al-Zubayr Terminal | Authorized Iraqi loading/import/export location; anchorage area for named SOMO floaters | `B-OFFICIAL-REPORTING` | Berth-by-berth concession, lease and operating map | [SOMO export reports](https://somooil.gov.iq/researches) |
| Berth/Jetty 41 | Loading point for authorized SOMO fuel-oil tenders; OFAC lists VS Oil at Jetty 41 | `A-OPERATIVE` | Whether the names describe the same physical property boundary; owner, lessor, tanks and operator by date | [SOMO tender](https://somooil.gov.iq/announcements/view/188), [OFAC action](https://ofac.treasury.gov/recent-actions/20250703) |
| VS Oil Terminal FZE | OFAC-listed UAE entity with physical address at Khor al-Zubayr Freezone Road, Jetty 41 | `A-OPERATIVE` sanctions state; `C-OFFICIAL-ALLEGATION` operations | Land/lease title, tank ownership, public terminal logs | [OFAC action](https://ofac.treasury.gov/recent-actions/20250703), [Treasury narrative](https://home.treasury.gov/news/press-releases/sb0188) |
| VS Tankers FZE / former AISSOT | OFAC-designated network company linked to DIJILAH | `A-OPERATIVE` sanctions state; `C-OFFICIAL-ALLEGATION` conduct | Full historical fleet and transaction ledger | [Treasury](https://home.treasury.gov/news/press-releases/sb0188) |
| Trade Bank of Iraq | Advising/confirming/payment bank in the located 2026 product tender | `A-OPERATIVE` for that tender | Universal role in crude sales is not established | [SOMO tender](https://somooil.gov.iq/announcements/view/188) |
| CBI | Acceptable-bank gate; manager of Iraq 2/DFI-successor structure for MoF | `A-OPERATIVE` | Cargo-level credits and current account agreement | [CBI 2023 statements](https://cbi.iq/static/uploads/up/file-171678915363315.pdf) |
| FRBNY | External account bank/custodian for the documented sovereign receipt structure | `A-OPERATIVE` | Current Iraq 2 statement and authorized-signatory matrix | [CBI 2023 statements](https://cbi.iq/static/uploads/up/file-171678915363315.pdf) |
| Ministry of Finance | Fiscal principal; reconciles oil revenue with CBI and SOMO; finances budget accounts | `B-OFFICIAL-REPORTING` | Cargo-to-ledger-to-budget lineage | [MoF Accounting Service](https://mof.gov.iq/en/Accounting-Service.aspx) |

## Physical movement ledger

| Record | Date/period | Cargo/movement | Origin → logistics gate | Quantity | Evidence state | Primary source and gap |
|---|---|---|---|---:|---|---|
| `PHY-QAY-2019-TENDER` | 2019 tender | Qayarah heavy sour crude by road tanker | Qayarah field, ex-works → named Iraqi exit routes | 30,000 b/d offered | `A-OPERATIVE` tender terms | [SOMO tender](https://www.somooil.gov.iq/announcements/view/12). Buyer took title/risk when loaded and signed for; winning buyer and performed movements not located. |
| `PHY-QAY-2024-TENDER` | Contract term scheduled from 2024-10-01 | Qayarah crude by road tanker | Qayarah field, ex-works → buyer-controlled route | not recorded here | `A-OPERATIVE` tender | [SOMO tender](https://www.somooil.gov.iq/announcements/view/135). Award and truck manifests not located. |
| `PHY-QAY-2025-06` | 2025-06-04 | Qayarah crude loading from M/T VS87 floater | Qayarah supply → VS87 anchorage near Khor al-Zubayr → Almi Navigator | 946,741 reported units; table unit requires source-PDF confirmation | `B-OFFICIAL-REPORTING` | [SOMO June report](https://somooil.gov.iq/storage/227/180bb5cc8f99bef163a9d5811de2fac1.pdf). Buyer, IMO, route into floater and payment absent. |
| `PHY-QAY-2025-07` | B/L 2025-07-29 | Qayarah crude loading from M/T VS87 floater | Qayarah supply → VS87 anchorage near Khor al-Zubayr → V. Progress | 495,645 BBL | `B-OFFICIAL-REPORTING` | [SOMO July report](https://somooil.gov.iq/storage/229/00d989ab6659b9d966663b067c8b634a.pdf). Buyer, IMO, route into floater and payment absent. |
| `PHY-QAY-2025-08` | B/L 2025-08-17 | Qayarah crude loading from M/T VS87 floater | Qayarah supply → VS87 anchorage near Khor al-Zubayr → Twin Castor | 911,178 BBL | `B-OFFICIAL-REPORTING` | [SOMO August report](https://somooil.gov.iq/storage/235/cfe49905661cd40d8d544adc56d8cd60.pdf). Buyer, IMO, route into floater and payment absent. |
| `PHY-QAY-2026-02` | B/L 2026-02-04 | Qayarah crude loading from M/T ST1 floater | Qayarah supply → ST1 anchorage near Khor al-Zubayr → Minerva Kalypso | 971,130 BBL | `B-OFFICIAL-REPORTING` | [SOMO February report](https://somooil.gov.iq/storage/258/fc4f1eb963f20f4adf552e98543d7fd9.pdf). Buyer, IMO, route into floater and payment absent. |
| `PHY-QAY-2026-TENDER` | Posted 2026-05-22 | Qayarah crude by road tanker | Qayarah field → tender-defined buyer route | not recovered from image-based attachment | `A-OPERATIVE` notice | [SOMO notice](https://www.somooil.gov.iq/announcements/view/184). Full machine-readable terms and award needed. |
| `PHY-B41-2026-09` | Posted 2026-06-14 | Iraqi-refinery straight-run fuel oil | tanks described as Berth 41 → FOB Khor al-Zubayr | 127,890 ±5% MT | `A-OPERATIVE` tender | [SOMO announcement 09](https://somooil.gov.iq/announcements/view/188). Successful bidder and actual liftings not located. |
| `PHY-B41-OFAC-LIC` | Announced 2026-06-18 | Licensed sale/export of Iraqi-origin fuel oil | Berth 41 → non-sanctioned buyer | tender quantities | `A-OPERATIVE` entity report of specific license | [SOMO license notice](https://somooil.gov.iq/announcements/view/190). Full OFAC license text, covered property and intermediaries not public. |

### Tank and floater ambiguity

SOMO's Berth 41 tender says the product was stored in the tanks of Berth 41, while the same tender says no onshore storage tanks were available. SOMO's monthly reports separately identify product and Qayarah floaters near Khor al-Zubayr.

Do not resolve this by assumption. Required documents:

- port/terminal plan identifying fixed, floating and leased storage;
- tank numbers, capacities and operator by date;
- Berth 41 concession or lease;
- floater IMO identities and storage contracts;
- inlet/outlet meter and assay records.

## Allegation ledger

| Record | Alleged period/event | Treasury claim | Named entities/assets | Evidence grade | Missing operative join |
|---|---|---|---|---|---|
| `ALG-SAID-2020+` | Since at least 2020 | Iranian oil was falsely declared or blended as Iraqi oil and sold using forged documentation | Salim Ahmed Said; VS Tankers/former AISSOT; VS Oil | `C-OFFICIAL-ALLEGATION` | Cargo IDs, contracts, B/Ls, assays, buyers and payments |
| `ALG-CASINOVA-2024-04` | April 2024 | An unnamed vessel from the VS Tankers claimed fleet conducted four STS transfers with CASINOVA near the Shatt al-Arab mouth | CASINOVA/YING GE, IMO 9280366; unnamed VS vessel | `C-OFFICIAL-ALLEGATION` | Counterparty identity, coordinates, dates, volumes, AIS exhibit and cargo origin |
| `ALG-VSOIL-TANKS` | Described 2025-07-03 | Six VS Oil tanks received Iranian oil for mixing; nearby vessels also performed STS; complicit officials authenticated the blend | VS Oil; Triliance-linked and Sahara Thunder-linked visiting vessels not named | `C-OFFICIAL-ALLEGATION` | Tank log, named vessels, assays, official authentication records and buyers |
| `ALG-HARD-CURRENCY` | Described 2025-07-03 | VS Oil employees moved hard currency into Iran in cars and trucks as oil payment | VS Oil employees not named | `C-OFFICIAL-ALLEGATION` | Vehicle records, amount/date/currency, source of cash and recipients |
| `ALG-MAARIJ-QAYARAH` | Described 2026-05-07 | Ali Maarij authorized trucking several million dollars of oil per day from Qayarah to VS Oil and falsified provenance | Ali Maarij Al-Bahadly; Salim Ahmed Said; VS Oil; AAH | `C-OFFICIAL-ALLEGATION` plus designation | Loading orders, buyer, truck carriers, daily barrels, route, terminal receipts, false documents and final payment |

Primary narratives: [Treasury July 2025](https://home.treasury.gov/news/press-releases/sb0188), [Treasury May 2026](https://home.treasury.gov/news/press-releases/sb0492).

## Vessel identity and permission ledger

### Core vessels

| Vessel | Stable identity | Registry/club fact | Sanctions or allegation state | Insurance state | Open join |
|---|---|---|---|---|---|
| DIJILAH | IMO 9829629; OFAC snapshot: Marshall Islands crude tanker, MMSI 538008147 | Gard's current page shows P&I entry with the `owner` field Nera Shipping S.A. and Lloyd's Register class; do not assume that field is statutory registered ownership | OFAC identified it 2025-07-03 as property in which VS Tankers has an interest; Treasury alleges VS Tankers had operator, manager and beneficial-owner roles since 2019 | Gard P&I club page and certificates located for 2026-02-20 to 2027-02-20 | No public primary record ties DIJILAH to a specific blended cargo or to the four CASINOVA transfers |
| CASINOVA / YING GE | IMO 9280366; OFAC snapshot: Barbados crude tanker, MMSI 314001045 | OFAC linked it to Le Monde Marine Services Limited | Designated 2025-02-24; Treasury alleges four April 2024 STS transfers with an unnamed VS-fleet vessel | No official P&I/club entry located in this pass | Counterparty IMO, coordinates, cargo and insurance |
| MOLECULE / former BABEL | IMO 9209300 | Treasury's 2024 and 2025 releases describe different management clocks involving Global Tech Marine Services and Rhine Shipping | Identified as blocked property 2024-01-12; Treasury later alleged BABEL loaded from an Iranian tanker with transponder disabled | No official P&I/club entry located in this pass | Event date, Iranian counterparty IMO, cargo documents and current owner/manager chain |

Sources: [DIJILAH/VS network](https://home.treasury.gov/news/press-releases/sb0188), [OFAC 2025-07-03](https://ofac.treasury.gov/recent-actions/20250703), [Gard DIJILAH entry](https://gard.no/vessels/74644/), [CASINOVA OFAC entry](https://ofac.treasury.gov/recent-actions/20250224), [MOLECULE action](https://home.treasury.gov/news/press-releases/jy2022).

### Babylon Navigation fleet

OFAC identified the following vessels on 2025-09-02 as property in which Babylon Navigation DMCC has an interest. Treasury alleged network-level blending, nighttime STS, AIS gaps and spoofing, but the public release does not provide vessel-specific event dates, coordinates, counterpart IMOs, volumes or exhibits.

| Vessel | IMO | OFAC flag/type snapshot | Official P&I finding in this pass |
|---|---:|---|---|
| ADENA | 9254862 | Liberia; crude tanker | none located |
| ALEXANDRA | 9273260 | Liberia; crude tanker | none located |
| BELLAGIO | 9299446 | Liberia; chemical/products tanker | none located |
| BIANCA | 9259927 | Liberia; chemical/products tanker | none located |
| CAMILLA | 9254850 | Liberia; crude tanker | none located |
| DELFINA | 9256248 | Liberia; crude tanker | none located |
| LILIANA | 9297905 | Liberia; crude tanker | none located |
| PAOLA | 9299458 | Liberia; chemical/products tanker | none located |
| ROBERTA | 9237008 | Liberia; oil-products tanker | none located |

OFAC's named shell-owner pool is Tryfo Navigation Inc., Keely Shiptrade Limited, Odiar Management S.A., Panarea Marine S.A. and Topsail Shipholding Inc. The public action does not map one shell owner to one vessel. Preserve `registered owner not mapped in public OFAC release`.

Sources: [Treasury narrative](https://home.treasury.gov/news/press-releases/sb0233), [OFAC identifiers](https://ofac.treasury.gov/recent-actions/20250902).

### Insurance rule

The International Group's vessel search and individual club pages are discovery tools, not proof of voyage-specific permission. Record separately:

```text
club entry
certificate/blue-card validity
policy or entry terms
sanctions clause
OFAC legal state
specific license
voyage/cargo facts
claim trigger
legal ability to pay
actual payment
```

Only DIJILAH produced an official club-page result in this pass. The absence of an official P&I page for another vessel is a public evidence gap, not proof that the vessel was uninsured.

## Cargo-document gate

### Long-term crude export procedure

```text
SOMO buyer qualification
→ technical committee review
→ board and minister allocation approval
→ standard sale contract
→ buyer vessel nomination
→ SOMO vessel acceptance and loading window
→ irrevocable LC at a CBI-recognized bank
→ SOMO terminal instruction
→ loading
→ port-issued B/L, quantity, API gravity and destination documents
→ SOMO final OSP-based price
→ buyer payment under contract term
```

Source: [SOMO export policy](https://www.somooil.gov.iq/about/policy).

### Berth 41 product tender document/payment package

The 2026 tender provides the clearest public document stack:

```text
outside-Iraq issuing bank accepted by CBI
→ irrevocable documentary LC
→ advised through TBI
→ confirmed by TBI or another CBI-accepted bank
→ at least seven days before laycan
→ vessel/loading authorization
→ SOMO draws USD within 30 days from B/L
→ original bill of lading
 + SOMO commercial invoice
 + SOMO quantity and quality certificate
```

Alternative: advance wire from outside Iraq to the named SOMO account at TBI before laycan. The tender also requires a USD performance bond and permits invoice adjustments for penalty or demurrage.

Source: [SOMO Berth 41 tender](https://somooil.gov.iq/announcements/view/188).

These are the identity and payment gates an alleged false-provenance scheme would need to defeat, bypass or induce an authorized actor to accept.

## Sovereign receipt and budget rail

```text
legitimate SOMO crude buyer payment
→ Iraq 2/OPRA or related documented sovereign oil-receipt account at FRBNY
→ CBI management/recordkeeping for Ministry of Finance
→ MoF USD account and reconciliation
→ MoF sale of USD to CBI
→ IQD budget financing
```

Public sources establish the structure, not a cargo-level join. CBI's 2023 financial-statement note says DFI balances moved into a CBI account at FRBNY in 2014, a second account named Iraq 2 was opened, oil-shipment balances enter it, and MoF has a current account against it. MoF says its Accounting Department reconciles oil revenue with CBI and SOMO.

Sources: [CBI 2023 statements, Note 36](https://cbi.iq/static/uploads/up/file-171678915363315.pdf), [MoF Accounting Service](https://mof.gov.iq/en/Accounting-Service.aspx).

Do not route alleged private shadow-sale proceeds into Iraq 2 without a buyer payment or bank credit record. Treasury's July 2025 narrative instead alleges that some VS Oil payment moved as hard currency by car or truck.

## Public join matrix

| Join | Publicly possible? | Best key | Missing object |
|---|---|---|---|
| SOMO monthly cargo → vessel/B/L date/quantity/grade/floater | Yes | vessel name + B/L date + quantity | IMO often absent |
| Cargo → exact buyer | Sometimes in historical EITI data, not in current monthly reports | contract/allocation ID | current buyer/allocation roster |
| Cargo → invoice | No | B/L number + invoice number | invoice register/copy |
| Invoice → LC/payment | No | LC number, invoice reference, SWIFT UETR | bank advice/message |
| Payment → Iraq 2 credit | No | payment reference + FRBNY credit reference | transaction statement |
| Iraq 2 credit → MoF account #300600 | No | CBI/MoF reconciliation key | reconciliation schedule |
| MoF USD → CBI FX purchase → IQD budget account | Aggregate only | MoF instruction and appropriation code | cargo lineage is lost publicly |
| Qayarah field loading → road tanker → terminal receipt | No | loading ticket + truck/driver + seal + weighbridge ticket | manifests and gate logs |
| Terminal receipt → tank → blend/STS → export B/L | No | batch/tank ID + assay + meter ticket | tank and terminal books |
| Vessel → P&I club | Sometimes | IMO | full entry/cover record |
| P&I entry → voyage legality or payable claim | No | policy/entry terms + sanctions license + voyage facts | transaction-specific coverage and license analysis |

## Starter cargo record schema

```text
cargo_uid
fact_or_allegation
evidence_grade
source_date

production_field
field_operator
state_oil_company
commodity
grade
physical_origin
declared_origin

allocation_id
contract_id
seller_legal_entity
buyer_legal_entity
incoterm
title_transfer_gate
risk_transfer_gate

truck_carrier
truck_id
driver_id
loading_ticket
seal_id
weighbridge_ticket
road_route
border_or_port_gate
terminal_receipt

storage_terminal
berth_or_jetty
tank_id
floater_name
floater_imo
inlet_meter
outlet_meter
pre_receipt_assay
post_storage_assay
blending_event

vessel_name
vessel_alias
vessel_imo
flag
registered_owner
beneficial_owner_alleged
operator
ism_manager
sts_counterparty
sts_counterparty_imo
sts_date_time
sts_coordinates
ais_state

pi_club
pi_entry_name
pi_cover_period
hull_insurer
war_risk_insurer
reinsurer
sanctions_clause
ofac_state
license_number

nomination_date
acceptance_date
laycan_start
laycan_end
bill_of_lading_number
bill_of_lading_date
loaded_quantity
quantity_unit
api_gravity
quality_certificate_number
commercial_invoice_number
certificate_of_origin
declared_destination

final_unit_price
gross_invoice_usd
credit_note_usd
demurrage_adjustment_usd
net_due_usd
payment_due_date
lc_number
lc_issuing_bank
lc_advising_bank
lc_confirming_bank
lc_beneficiary
payment_value_date
sender_bank
intermediary_banks
swift_uetr

receiving_account
frbny_credit_reference
mof_recognition_date
cbi_fx_purchase_date
destination_budget_account
final_private_beneficiary_alleged

reconciliation_status
open_document
source_url
```

## Claim audit

| Claim | Ruling | Reason |
|---|---|---|
| Qayarah oil has moved by road tanker under official SOMO tenders | `SUPPORTED` | Official tenders expressly use ex-works road-tanker delivery. |
| Every Qayarah truck movement is suspicious | `REJECTED` | Truck transport is an authorized commercial model. The alleged misconduct concerns allocation, destination, mixing, documents and beneficiary. |
| SOMO reports Qayarah cargoes from floaters near Khor al-Zubayr | `SUPPORTED` | Monthly export reports name VS87 and ST1 and list vessel, quantity and B/L date. |
| VS Oil was located at Jetty 41 | `SUPPORTED-AS-OFAC-IDENTIFIER` | OFAC publishes that address. Property ownership and exact facility boundary remain open. |
| All Berth 41 traffic was illicit | `REJECTED` | SOMO published authorized Iraqi-origin cargo tenders and an OFAC-licensed sale route at Berth 41. |
| Treasury proved each blend cargo | `NOT ESTABLISHED` | Treasury published network allegations and designations, not the underlying cargo exhibits. |
| DIJILAH was the vessel that met CASINOVA four times | `NOT ESTABLISHED` | Treasury leaves the VS-fleet counterparty unnamed. |
| DIJILAH lacked insurance after designation | `REJECTED-AS-STATED` | Gard has a current vessel/P&I entry. Voyage-specific legality and claim payability remain separate. |
| No located P&I page means a vessel was uninsured | `REJECTED` | Absence from the public search is an evidence gap. |
| False Iraqi provenance automatically deposits proceeds into Iraq 2 | `NOT ESTABLISHED` | Market access and sovereign receipt are different. The alleged network includes private hard-currency movement. |
| The 2021 $9.59 billion receipt difference proves diversion | `REJECTED` | It is an unreconciled sales/accrual-versus-cash gap without the FRBNY statement; no cargo-level link exists. |

## Source watchboard

| Source/entity | Watch | Status-moving evidence |
|---|---|---|
| SOMO tenders and awards | Qayarah road-tanker awards; Berth 41 award; buyer and vessel nominations | Signed award, contract ID, buyer, quantity, title gate, actual lifting |
| SOMO monthly export reports | Qayarah floater changes and outgoing vessels | Vessel + B/L date + quantity + grade + floater; ideally IMO and buyer |
| Ministry of Oil / North Oil Company | Qayarah production and disposition | Loading orders, production volumes, road/terminal route and contractor role |
| General Company for Ports of Iraq | Berth 41 and Khor al-Zubayr | Facility map, concession/lease, port calls, berth and gate records |
| Iraqi Higher Maritime Authority | STS permissions | License, vessel IMOs, date/time, coordinates, cargo, operator |
| Iraqi customs/border bodies | Road-tanker exits | Manifest, truck, seal, declared cargo, exit gate and consignee |
| OFAC | VS Oil license and designations | Full specific license, amendments, covered property, service providers and expiry |
| Flag states / class societies | Vessel identity | Registered owner, flag, class, manager and effective dates |
| International Group / P&I clubs | Marine liability | Club entry, certificates, cancellation or sanctions notice; still not voyage-specific permission |
| CBI / MoF / Committee of Financial Experts | Sovereign receipt | Iraq 2 statement, external audit and cargo/payment reconciliation |
| EITI Iraq | Buyer and cargo reconciliation | Cargo dates joined to buyer, invoice and receipts |

## Highest-value document requests

1. Full OFAC License `IRAN-EO13902-2026-1448903-1`, including property, services, banks, insurers, vessels, expiry and reporting conditions.
2. Berth 41 concession, lease, operator and tank/floater plan from 2020 onward.
3. Winning bidder and executed contract for the June 2026 Berth 41 sale.
4. Qayarah tender awards, field loading orders, truck-company identities and manifests for 2019, 2024 and 2026.
5. Iraqi Higher Maritime Authority STS license register and the April 2024 CASINOVA counterparty record.
6. Tank-by-tank inlet/outlet meters and quantity/quality assays at VS Oil/Berth 41.
7. Bills of lading, certificates of origin, SOMO invoices and buyer payment records for questioned cargoes.
8. Current registered-owner/manager histories for DIJILAH, CASINOVA and MOLECULE.
9. P&I, hull and war-risk records for the named vessels, plus any sanctions endorsements or cancellations.
10. Cargo-level chain: SOMO invoice → buyer payment → Iraq 2/OPRA credit → MoF recognition.

## Primary source register

- [Iraqi Constitution](https://iq.parliament.iq/en/wp-content/uploads/sites/3/2024/04/Constitution-of-the-Republic-of-Iraq.pdf)
- [Iraqi Oil Exploration Company — Qayarah/Sonangol/North Oil Company](https://www.oec.oil.gov.iq/en/news/ministry-of-oil-signs-contract-of-implementing-3d-seismic-survey-for-al-qayarah-field-with-the-angolan-sonangol-company/)
- [SOMO duties](https://somooil.gov.iq/about/duties)
- [SOMO export policy](https://www.somooil.gov.iq/about/policy)
- [SOMO Qayarah road-tanker tender, 2019](https://www.somooil.gov.iq/announcements/view/12)
- [SOMO Qayarah road-tanker tender, 2024](https://www.somooil.gov.iq/announcements/view/135)
- [SOMO Qayarah road-tanker notice, 2026](https://www.somooil.gov.iq/announcements/view/184)
- [SOMO monthly export reports](https://somooil.gov.iq/researches)
- [SOMO July 2025 export report](https://somooil.gov.iq/storage/229/00d989ab6659b9d966663b067c8b634a.pdf)
- [SOMO February 2026 export report](https://somooil.gov.iq/storage/258/fc4f1eb963f20f4adf552e98543d7fd9.pdf)
- [SOMO Berth 41 product tender](https://somooil.gov.iq/announcements/view/188)
- [SOMO Berth 41 OFAC-license notice](https://somooil.gov.iq/announcements/view/190)
- [SOMO maritime/STS readout](https://somooil.gov.iq/events/108)
- [SOMO AISSOT denial and origin statement](https://somooil.gov.iq/news/26)
- [Treasury — Salim Said / VS Tankers / VS Oil network](https://home.treasury.gov/news/press-releases/sb0188)
- [Treasury — Ali Maarij / Qayarah / AAH allegations](https://home.treasury.gov/news/press-releases/sb0492)
- [OFAC identifiers, 2025-07-03](https://ofac.treasury.gov/recent-actions/20250703)
- [OFAC CASINOVA action, 2025-02-24](https://ofac.treasury.gov/recent-actions/20250224)
- [Treasury/OFAC — Babylon Navigation fleet](https://home.treasury.gov/news/press-releases/sb0233)
- [OFAC Babylon identifiers](https://ofac.treasury.gov/recent-actions/20250902)
- [Gard vessel page — DIJILAH](https://gard.no/vessels/74644/)
- [CBI 2023 financial statements](https://cbi.iq/static/uploads/up/file-171678915363315.pdf)
- [Iraqi Ministry of Finance Accounting Service](https://mof.gov.iq/en/Accounting-Service.aspx)
- [Iraq 2021 EITI Report](https://eiti.org/sites/default/files/2024-01/Iraq%202021%20EITI%20Report.pdf)
- [Iraq EITI validation](https://eiti.org/countries/iraq)
