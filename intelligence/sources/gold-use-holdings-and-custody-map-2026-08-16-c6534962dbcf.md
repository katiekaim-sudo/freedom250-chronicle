# Gold in Use and in Custody — Broad Current Map

Updated: 2026-08-16 ET  
Status: pending workbench research; not reviewed or landed in the vault  
Evidence cutoff: 2026-08-16 ET; every quantity retains its own reporting date  
Scope assumption: Katie's “hosting” means holdings, storage, custody, vaulting and the records that control claims to gold  
Scope boundary: this pass maps current uses and holding structures. It does **not** decide when any of them is monetary.

Companion controls:

- [GOLD_MONETARY_USE_MECHANISM_MAP_2026-08-16.md](../sources/gold-monetary-use-mechanism-map-2026-08-16-740aee22a4fc.html) — the monetary, monetized and mobilized mechanism layer built on this map
- [WHOLESALE_METALS_MARKET_INFRASTRUCTURE_DEEP_DIVE.md](../sources/wholesale-metals-market-infrastructure-deep-dive-622e4608aaff.html)
- WHOLESALE_METALS_DATA_SPINE_SPEC.md
- WHOLESALE_METALS_CLAIM_AUDIT.md
- LONDON_BULLION_DOCUMENT_RETRIEVAL_AND_DATA_REGISTRY.md

---

## Short answer

Gold is not one market object doing one job. It is a durable material moving through two independent maps:

1. **Object and use:** ore, doré, bars, powder, leaf, wire, coating, alloy, fabricated article, compound, coin or scrap used for adornment, saving, official holding, electronics, aerospace, dentistry, medicine, decoration, collateral, market exposure or recovery.
2. **Holder and claim:** direct possession, allocated property, unallocated bank credit, sovereign stock, official custody, trust property, warehouse title, pledged collateral or an issuer-defined token claim.

The physical form does not prove the owner's purpose. The place where gold sits does not prove who owns it. A vault total does not reveal beneficial owners, free float, encumbrance or monetary status. A security, derivative or token linked to gold is not automatically title to a bar.

The defensible current result is therefore a **role-and-claim topology**, not a universal bar-to-owner census.

## Five findings that control the map

1. **Most gold is a stock, not a consumed input.** It accumulates as jewelry, bars, coins, official holdings, fabricated goods and recoverable scrap, then can be remobilized or refined again.
2. **Use and form must remain separate.** A high-karat necklace can be adornment, inherited wealth and loan collateral at different times. A coin can be a collectible, a bullion product or legal tender at face value without functioning as a circulating payment instrument.
3. **“Held at” has several meanings.** Owner, beneficiary, custodian, vault operator, account provider, trustee, clearing member and recordkeeper may all be different entities.
4. **Public totals overlap.** London vault data include Bank of England, ETF and commercial holdings. New York Fed vault totals include many official customers, while the U.S.-owned portion is only one subset. ETF and token reserves may already sit inside a vault aggregate.
5. **Monetary status is a later proof problem.** Reserve designation, tariff classification, legal tender, collateral eligibility, an actual pledge or settlement, and convertibility are separate facts and separate clocks.

---

## 1. Current scale without false joins

The following series answer different questions. They must not be added or reconciled by subtraction.

| Measurement | Cutoff | Current reported result | What it measures | Boundary |
|---|---:|---|---|---|
| Estimated above-ground gold stock | 2025-12-31 | **219,891 t**: jewelry 97,645 t (44%); bars and coins including gold-backed ETFs 50,978 t (23%); central banks 38,666 t (18%); other 32,602 t (15%) | Modeled stock distribution | World Gold Council/Metals Focus industry estimate, not an audited global title registry. Categories assign a primary form/use and cannot show mixed motives or encumbrance. [Source](https://www.gold.org/goldhub/data/how-much-gold) |
| U.S. material balance | Calendar 2025 estimate | Mine production 160 t; primary refinery output 170 t; secondary output 90 t; imports for consumption 320 t; exports 260 t; reported consumption 150 t | Official U.S. commodity balance | Supply-chain fields have defined but different perimeters; they are not a U.S. end-use census. [USGS MCS 2026, pp. 90–91](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf) |
| Broad global consumption mix | 2025 estimate | Jewelry 40%; physical bars 24%; central banks/institutions 21%; coins, medals and imitation coins 7%; electrical/electronics 7%; other 1% | USGS-published global use shares, excluding ETFs and similar products | Based on World Gold Council data available for the first nine months of 2025. This denominator is not the same as annual demand, above-ground stock or vault holdings. [USGS MCS 2026](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf) |
| Detailed annual demand | Calendar 2025 | Total 5,002.3 t; jewelry fabrication 1,638.0 t; technology 322.8 t; bar and coin 1,374.1 t; ETF inflow 801.2 t; central banks/institutions 863.3 t | Industry-estimated annual demand flows | ETF figures are net flows, not total holdings. WGC/Metals Focus methodology differs from USGS. [WGC Gold Demand Trends 2025](https://www.gold.org/goldhub/research/gold-demand-trends/gold-demand-trends-full-year-2025) |
| Latest quarterly demand | 2026 Q2 | Total including OTC 1,268.9 t; jewelry consumption 278.2 t; technology 80.4 t; bar and coin 307.1 t; ETFs and similar products **−44.8 t**; central banks/institutions 288.9 t; OTC and other 327.1 t | Industry-estimated quarterly flows | Negative ETF demand is a net disinvestment flow, not negative stock. OTC is estimated. [WGC Gold Demand Trends Q2 2026](https://www.gold.org/goldhub/research/gold-demand-trends/gold-demand-trends-q2-2026) |
| Latest quarterly supply | 2026 Q2 | Mine production 965.6 t; recycled gold 326.1 t; net producer hedging −22.8 t | Industry-estimated new and remobilized supply | Recycling is supply returned to market, not an end use. [WGC Gold Demand Trends Q2 2026](https://www.gold.org/goldhub/research/gold-demand-trends/gold-demand-trends-q2-2026) |

### What the apparent conflicts mean

- USGS's 2025 world mine estimate of 3,300 t and WGC/Metals Focus's 3,671.6 t are separate estimates with different methodologies. This map preserves both rather than silently selecting one.
- USGS's 150 t of reported U.S. consumption cannot be compared directly with a sum of WGC's U.S. jewelry, technology and bar-and-coin demand. The category perimeters differ.
- A demand flow can change ownership without increasing above-ground stock. A recycled flow changes market supply without creating new metal. A vault transfer can change a ledger without moving a bar.

---

## 2. Broad current-use map

### 2.1 Material, cultural and holding uses

| Use family | Common forms | Immediate users and function | Current scale signal | What the evidence does **not** prove |
|---|---|---|---|---|
| Jewelry, adornment and cultural or ritual objects | Karat alloys; cast or worked jewelry; religious insignia; plated objects; leaf | Households, jewelers, artisans and institutions use gold for adornment, marriage and ritual objects, inheritance, symbolic display and durable portable goods | USGS places jewelry at about 40% of its global consumption estimate. WGC estimates 1,638.0 t of jewelry fabrication and 1,542.3 t of jewelry consumption in 2025 | “Cultural wealth” is not a separate measured series. Form does not reveal whether an object is being worn, inherited, stored, sold or pledged |
| Direct physical saving and investment | Cast or minted bars; bullion coins; rounds and medals | Households, institutions, dealers and mints acquire tangible metal for direct holding, resale or diversification | WGC estimates 1,374.1 t of 2025 bar-and-coin demand: 1,068.2 t bars, 170.5 t official coins and 135.4 t medals/imitation coins. The U.S. Mint reports 360,000 gold ounces sold in FY2025, about 11.2 t. [Mint report](https://www.usmint.gov/content/dam/usmint/reports/2025-annual-report.pdf) | A bar or coin is not evidence of payment use, official reserve designation or the buyer's motive. Mint sales do not cover imported products or secondary turnover |
| Official institutional holding | Standard bars, coins and other reserve forms held directly or through official custodians | Treasuries, central banks and international institutions hold gold under entity-specific mandates, accounting and custody arrangements | USGS places central banks/institutions at 21% of its consumption split; WGC estimates 38,666 t of official above-ground stock at end-2025 and 288.9 t of net institutional demand in 2026 Q2 | Official ownership or custody alone does not establish the exact reserve-accounting classification, encumbrance, transaction use or legal effect. Those are deferred to the monetary phase |
| Electronics and information technology | Bonding wire; plated contacts and connectors; PCB finishes; semiconductor packaging; thin films and salts | Electronics, communications, server, automotive-sensor and device manufacturers use conductivity, corrosion resistance and high-reliability connections | USGS places electrical/electronics at about 7% of global consumption. WGC estimates 270.4 t of electronics use within 322.8 t of total technology use in 2025 | Device shipment counts and trade values do not reveal embedded gold mass. Current official U.S. electronics-only tonnage is not published |
| Aerospace, space, optical and high-reliability systems | Connector plating; wire bonds; vapor-deposited films; infrared mirrors, baffles and visor coatings | Spacecraft, aviation, defense and optical-system builders use reflectivity, thermal control, oxidation resistance and electrical reliability | No defensible standalone tonnage. NASA reports the Webb mirrors carry a coating about 100 nm thick totaling only 48.25 g of gold. [NASA](https://science.nasa.gov/mission/webb/webbs-mirrors/) | Webb demonstrates functional leverage, not sector scale. Gold-colored spacecraft blankets may be aluminized polymer rather than gold. [NASA boundary](https://science.nasa.gov/learn/basics-of-space-flight/chapter11-4/) |
| Dentistry | High-noble alloys; crowns, bridges, copings, solders, inlays and abutments | Dental laboratories, dentists and patients use workable, durable and corrosion-resistant restorative material | WGC estimates 8.2 t globally in 2025. FDA continues to recognize gold-based noble-metal dental alloys under Class II controls. [FDA](https://www.fda.gov/medical-devices/guidance-documents-medical-devices-and-radiation-emitting-products/dental-noble-metal-alloys-class-ii-special-controls-guidance-document-industry-and-fda-staff) | No current official U.S. dental tonnage is available. The FDA source establishes a regulated use, not market scale |
| Medical, pharmaceutical and biotechnology | Gold compounds; nanoparticles; device markers and coatings; research colloids | Manufacturers, researchers and patients use a small mature pharmaceutical niche and experimental imaging, sensing or photothermal applications | A current auranofin label confirms a marketed gold compound. [DailyMed](https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=43ba3de1-ab2e-06f6-e054-00144ff8d46c&type=display) NIH reported a 2025 mouse study using gold nanoparticles. [NIH/NEI](https://www.nei.nih.gov/research-and-training/research-news/nei-funded-researchers-test-new-visual-prosthesis-system-restore-vision) | Gold-compound mass is not metallic-gold demand. Preclinical nanoparticle research is not deployed clinical use, and no defensible bulk tonnage series was found |
| Other industrial, optical and decorative fabrication | Powder; wire; sheet; leaf; plating salts; clad metal; coatings and specialty articles | Platers, textile producers, optical and specialty manufacturers use gold for corrosion-resistant surfaces, reflectivity, decoration and specialized material properties | WGC estimates 44.2 t of “other industrial” demand in 2025 | This residual category mixes unrelated functions and cannot be assigned wholesale to aerospace, chemicals, art or plating |
| Awards, medals, art, gilding and household or religious wares | Leaf; plated surfaces; cast medals; ornaments and goldsmith wares | Artists, gilders, award bodies, museums, religious institutions and decorative finishers use gold for symbolic honor, surface treatment and conservation | No art-only tonnage exists. WGC's 135.4 t medals/imitation-coins category is the nearest measured bucket but includes investment and commemorative products. The U.S. Mint documents Congressional Gold Medals. [Mint](https://www.usmint.gov/learn/coins-and-medals/medals/Congressional-Gold-Medals) | A gold-colored object may contain no gold; an award may be solid alloy or carry only a microscopic coating |
| Recovery and recycling | Jewelry and industrial scrap; electronics; dental scrap; offcuts; residues; recovered bullion, granulation or sponge | Refiners, recyclers, manufacturers and government programs return metal to another fabrication or holding cycle | USGS estimates 90 t of U.S. secondary output in 2025, about 60% of reported consumption. WGC estimates 1,404.3 t of global recycled supply in 2025. DLA operates a government precious-metals recovery program. [DLA](https://www.dla.mil/Troop-Support/Construction-and-Equipment/Metals/) | Recycling is a supply flow, not demand. Gross scrap weight is not contained-gold weight, and fabrication scrap differs from end-of-life recovery |

### 2.2 Gold-linked claims and financing uses

These are uses of gold, or of a claim linked to gold, but the underlying legal object must remain visible.

| Use lane | Gold or claim involved | Current function | Boundary held for later research |
|---|---|---|---|
| Pledge and secured credit | Jewelry, bars, warrants or allocated interests | Gold can secure household loans, commercial credit or clearing obligations | Eligibility is only an open legal door. We need an observed pledge, lien, loan and release/default path before claiming actual use |
| Exchange delivery and warehouse title | Conforming bar plus COMEX electronic warrant; SGE bullion account; SHFE standard warrant | A ledger/document of title can deliver a contract or transfer control while the metal stays in a warehouse | Warrant transfer is not physical load-out; public stock reports do not disclose beneficial owners |
| Futures, options and other derivatives | Contractual price exposure; sometimes deliverable through specified title objects | Hedging, price discovery, speculation and portfolio exposure | A position is not ownership of exchange inventory. Open interest is not a claim on every warehouse bar |
| ETF or trust share | Security or beneficial trust interest supported by product-specific bullion assets | Transferable price exposure with institutional custody and authorized creation/redemption | A shareholder generally does not own a named bar or have retail redemption rights. Each trust constitution controls |
| Allocated bullion account | Customer property in identified bars | Custody, trading, transfer, collateral and possible withdrawal | Allocation needs a bar list and executed agreement; liens, subcustody and release conditions still matter |
| Unallocated bullion account | Account provider's contractual obligation to deliver an equivalent quantity | Wholesale trading and settlement credit | The customer is a creditor, not owner of a specified bar. The account balance proves no physical location |
| Gold deposit or metal loan | Entity-specific deposit liability, gold loan or government/bank program | Mobilizes held gold into a lending, refining, jewelry or repayment chain | Title transfer, accounting, maturity, repayment form and reserve treatment are product-specific. India's current Gold Monetization framework is one example. [RBI](https://www.rbi.org.in/scripts/NotificationUser.aspx?Id=10084) |
| Gold-linked token | Issuer-defined property or contractual claim connected to allocated or other custodial gold | Transfer, fractional exposure and product-gated redemption | The blockchain is not necessarily the authoritative bar-title record. Custodian, allocation, insolvency, freeze/upgrade powers and redemption gates control the claim |

---

## 3. Physical-form and lifecycle map

```text
resource / reserve estimate
        ↓ extraction
ore and concentrate
        ↓ smelting
doré / precipitate / other unwrought gold
        ↓ refining
standard bars / grain / powder / compounds
        ↓ allocation, fabrication or minting
identified bullion    jewelry / electronics / dental / coatings    coins / medals
        ↓ transfer, pledge, use, wear or discard
held stock / custodied claim / fabricated stock / scrap
        ↓ remelting and refining
recovered gold re-enters the refined-material cycle
```

| Form or trade family | Representative classification | What it can establish | What it cannot establish |
|---|---|---|---|
| Ore and concentrate | HS 2616 | Material stage and cross-border movement | Refined quantity, owner motive or end use |
| Gold compounds | HS 2843.30 | Chemical form | Equivalent metallic-gold demand or clinical use |
| Powder | HS 7108.11 | Refined physical form | Industrial application or owner |
| Bullion, doré and other unwrought forms | HS 7108.12 | Unwrought form and trade movement | Investment, reserve, custody or payment use |
| Leaf and other semimanufactured forms | HS 7108.13 | Fabrication stage | Ultimate decorative, electronic or industrial use |
| Base metal or silver clad with gold | HS 7109 | Composite material form | Contained-gold mass from gross article weight |
| Waste, ash and scrap | HS 7112 | Recovery-oriented material movement | Contained gold, recoverability or final destination |
| Jewelry and parts | HS 7113 | Fabricated article class | Whether worn, stored, inherited, pledged or remelted |
| Goldsmith wares and other articles | HS 7114–7115 | Fabricated article class | Art, award, household or industrial motive |
| Coins | HS 7118 | Coin form | Circulation, market-value convertibility or official reserve status |
| “Monetary gold” customs line | HS 7108.20 | A tariff classification under its own legal definition | Monetary-authority title, reserve designation or an observed monetary transaction; this line is deferred |

[USITC Chapter 71](https://hts.usitc.gov/search?query=7108) and [Census gold-export guidance](https://www.census.gov/newsroom/blogs/global-reach/2024/04/report-exporting-gold.html) control the U.S. trade-form vocabulary. Trade data remain a **movement layer**, not an end-use proxy. UN Comtrade likewise separates monetary gold and legal-tender coin from the nonmonetary merchandise series. [UN classification note](https://uncomtrade.org/docs/non-monetary-gold-in-trade-classifications-sitc-hs/)

---

## 4. The holdings and “hosting” topology

The controlling question is not merely “where is the gold?” It is:

> **Which legal person owns which object, who possesses it, which record controls the claim, what can encumber or move it, and what does the public actually see?**

| Holding structure | Underlying owner or beneficiary | Physical possessor / host | Authoritative record | Claim type | Public evidence boundary |
|---|---|---|---|---|---|
| Direct possession / self-custody | Individual or entity holding the object | Same person or its premises | Purchase/title records plus possession | Direct property, subject to local law | No comprehensive public household or private-institution census exists |
| Safe-deposit box or private vault | Customer, if the contract and title support it | Bank, nonbank vault or security provider | Customer agreement, inventory and custody ledger | Bailment/custody or another contract-specific claim | Aggregate operator capacity rarely reveals owner, bar, lien or insurance detail |
| Sovereign internal storage | Government | Mint, treasury or other government facility | Government stock accounts and facility records | Direct sovereign property | Public quantity may omit operational details, encumbrance or bar-level record |
| Official third-party custody | Government, central bank or international institution customer | Central-bank custodian such as FRBNY or BoE | Custodian allocation/bar ledger and customer books | Customer property if allocated under governing terms | Vault total usually hides customer identity and exact allocation |
| Commercial allocated account | Customer | Bullion bank, commercial vault or subcustodian | Executed agreement, account ledger and numbered bar list | Property in identified bars, subject to terms | Model agreements do not prove executed liens, insurance, subcustody or release rights |
| Commercial unallocated account | Customer is creditor; account provider is debtor | No customer-specific bar location follows | Bullion-bank account ledger and settlement records | General contractual entitlement to a quantity of metal | Balance is not ownership of identified bars and does not prove backing ratio |
| ETF / trust custody | Trust or fund owns product assets; shareholder owns a security or beneficial interest | Named custodian and possible subcustodians | Trustee/share register plus custodian bar ledger | Product-specific trust/security interest | Shareholder normally cannot point to or withdraw a named bar; product terms differ |
| Exchange depository and warrant | Beneficial owner may sit behind clearing member | Approved depository | Warehouse ledger, warrant system and clearing-member books | Document of title or exchange-defined warehouse claim | Registered, eligible and pledged are status fields, not owner identities |
| Clearing collateral | Pledgor subject to clearing-house security interest | Approved custodian/depository | Collateral ledger, control agreement and lien records | Encumbered title object | Collateral schedule proves eligibility; only account-level evidence proves actual pledge |
| Gold-backed loan custody | Borrower retains ownership until contract/default effects change it | Lender or approved custodian | Loan, pledge/lien, appraisal and safekeeping record | Secured-credit relationship | Physical possession by lender is not purchase or reserve use |
| Token custody | Product-specific holder interest | Issuer/trust company and named or unnamed vault chain | Blockchain, issuer allocation ledger and custodian bar ledger | Contractual or property claim defined by terms | Token count alone does not prove bars, allocation, bankruptcy remoteness or redemption performance |

### Why “recordkeeper” is not a clerical detail

Different records answer different questions:

- the **vault ledger** records possession and bar location;
- the **allocated bar list** identifies customer property;
- the **unallocated account ledger** records a bank liability;
- the **warehouse warrant** controls a document of title;
- the **clearing ledger** records contract and collateral status;
- the **trust share register** records securities ownership;
- the **blockchain** records token control;
- the **government balance sheet** records entity-specific accounting classification.

One record cannot be substituted for another.

---

## 5. Current institutional exemplars

This table maps roles and claims. It is not a ranking, and its quantities are not additive.

| System / reporting date | Reported owner or beneficiary | Host / custodian and quantity signal | Controlling claim / record | Hard boundary |
|---|---|---|---|---|
| **U.S. government gold — 2026-07-31** | U.S. Government; Treasury administers the stock | Fort Knox 147.342m fine troy oz (4,582.844 t); West Point 54.067m (1,681.682 t); Denver 43.854m (1,364.003 t); Mint working stock 2.783m (86.568 t); FRBNY bullion and coins 13.450m (418.355 t); small displays 2,371 fine oz (0.074 t). **Total: 261.499m fine oz / 8,133.526 t** | Treasury and Mint stock records; FRBNY custody record for its portion | Location does not change sovereign ownership. “Working stock” and deep storage are different operational categories. [Treasury API](https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/gold_reserve?filter=record_date:eq:2026-07-31&sort=src_line_nbr) |
| **Federal Reserve gold certificates — 2026-08-12** | Federal Reserve Banks own certificates, not the backing bullion | Treasury holds the gold; FRBNY makes issuance/redemption accounting entries for Treasury | Dollar-denominated statutory book-entry asset; H.4.1 reports $11.037bn in certificates against $11.041bn statutory gold stock | Certificates are not public claims redeemable in gold and do not identify bar location. [Fed FAQ](https://www.federalreserve.gov/faqs/does-the-federal-reserve-own-or-hold-gold.htm), [H.4.1](https://www.federalreserve.gov/releases/h41/current/) |
| **FRBNY official custody — vault statistic as of 2024** | Foreign governments, central banks, official international organizations and the U.S. government; none belongs to the New York Fed | 33 Liberty Street, New York; about 507,000 bars / 6,331 t total. Customer deposits are returned as the same bars | Segregated locker and custody ledgers | No private customers. Total is not U.S. gold and does not identify each customer. The 418.355 t U.S. portion above is one dated subset. [FRBNY](https://www.newyorkfed.org/aboutthefed/goldvault.htm) |
| **Bank of England official custody — current page 2026-03-12** | UK reserve owner plus foreign central banks and official customers; BoE says it owns only two display bars | Nine London vaults; roughly 400,000 bars across customers | Allocated bar ledger; customer assets are off the BoE balance sheet | BoE custody is not BoE ownership. Customer-by-customer bar allocation is not public. [BoE Gold](https://www.bankofengland.co.uk/gold) |
| **London vault aggregate — end-2026-06** | Many undisclosed official, bank, trust, institutional and other owners | 9,464 t held by the BoE and named commercial London vault operators | Each operator's ledger; LBMA publishes aggregate tonnes | Includes BoE and commercial holdings, plus ETFs and multiple physical forms. It excludes jewelry and many smaller/private locations. It reveals neither beneficial owner nor free float. [LBMA](https://www.lbma.org.uk/prices-and-data/london-vault-data) |
| **London clearing — 2026-06 average** | Clearing members and their customers hold account claims | LPMCL clearers transferred a net daily average 16.7m oz, $70.9bn, across 7,227 transfers | Bullion-bank ledgers and AURUM settlement matching | Ledger turnover is not vault stock and ordinarily is not physical movement. Most settlement starts unallocated. [LBMA clearing data](https://www.lbma.org.uk/prices-and-data/clearing-data) |
| **IMF — audited 2025-04-30** | IMF | Designated member depositories in the U.S., UK, France and India; 90.474m fine oz / 2,814 t total; site allocation undisclosed | IMF accounts and depository books | IMF property is not member-country property. Depository and encumbrance detail is not public. [IMF financial statements](https://www.imf.org/external/pubs/ft/ar/2025/pdfs/imf-annual-report-2025-financial-statements.pdf) |
| **BIS — 2026-03-31** | Separate BIS-owned and client pools | BIS reports 102 t of its own investment gold; it can use central-bank custody and also accept client gold deposits/custody | BIS banking ledger plus holding-central-bank records | BIS-owned gold must not be combined with client gold. A gold deposit is a BIS liability unless terms create identified property. [BIS annual report](https://www.bis.org/about/areport/areport2026.htm) |
| **GLD — 2025-09-30 filing** | SPDR Gold Trust owns bullion; investors own shares | HSBC and JPMorgan custodians; 32.528m oz / 1,011.741 t, reported as 100% allocated London Good Delivery bars | Trustee/share register and custodian bar ledger | A shareholder does not own a named bar; physical creation/redemption is Authorized-Participant and basket gated. [SEC 10-K](https://www.sec.gov/Archives/edgar/data/1222333/000143774925036305/gld20250930_10k.htm) |
| **IAU — 2025-12-31 filing** | iShares Gold Trust owns bullion; each share is a fractional undivided beneficial interest in net assets | JPMorgan London branch custodian, with authorized locations | BNY Mellon share/trustee records and JPMorgan custody ledger | Share is not a warehouse receipt; retail holder does not have direct bar redemption. Product terms prohibit generalizing from GLD. [SEC 10-K](https://www.sec.gov/Archives/edgar/data/1278680/000143774926006055/iau20251231_10k.htm) |
| **COMEX** | Beneficial customer may sit behind a clearing member | Approved depository physically holds conforming bars | Warehouse ledger, electronic warrant system, clearing-member books and CME Clearing | Eligible means conforming but unwarranted; registered means warrant issued; pledged means encumbered. None discloses the beneficial owner in public inventory reports. [COMEX Rulebook](https://www.cmegroup.com/rulebook/COMEX/), [registrar reports](https://www.cmegroup.com/clearing/operations-and-deliveries/registrar-reports.html) |
| **SGE and SHFE** | Member/customer recorded through exchange bullion account or warrant | Certified Chinese delivery warehouses | SGE bullion-account or SHFE standard-warrant ledger | Exchange clearing/recordkeeping and warehouse possession are distinct. Border and member-account rules still govern conversion and withdrawal. [SGE delivery rules](https://en.sge.com.cn/upload/file/202001/17/Pqj7uZPO401JZezZ.pdf), [SHFE gold rules](https://www.shfe.com.cn/regulation/exchangerules/productrules/202512/t20251231_829960.html) |
| **HKPMCC trial — launched 2026-07-07** | Participant has a trial ledger balance/claim | Bank of China (Hong Kong) is disclosed as settlement institution and designated vault | Government-owned HKPMCC central ledger | Disclosed trial balances are unallocated and commingled. Operative allocated-conversion, finality and insolvency rules remain missing. [Hong Kong government](https://www.info.gov.hk/gia/general/202607/07/P2026070700223.htm) |
| **PAXG — terms modified 2025-12-12** | Terms grant tokenholder a fractional beneficial ownership interest in allocated London Good Delivery gold | Paxos Trust is custodian through LBMA-approved security-carrier vaults in London | Blockchain plus Paxos allocation/bar ledger | Token control is not possession. Identity and minimum-bar gates apply to physical redemption; executed subcustody and insolvency evidence remain incomplete. [Terms](https://www.paxos.com/terms-and-conditions/pax-gold-terms-conditions), [transparency](https://www.paxos.com/paxg-transparency) |
| **XAUT — assurance 2026-03-31** | Issuer represents tokenholder as owning one fine ounce on a specified bar | TG Commodities uses an unnamed third-party custodian in a Swiss vault | Blockchain, issuer allocation ledger and custodian record | Full-bar redemption, KYC, access, custodian identity and insolvency terms remain material gates. [FAQ](https://gold.tether.to/faq), [assurance](https://gold.tether.to/docs/reports/attestations/ISAE_3000R_-_Opinion_TGRR_31.03.2026_RC187322026DV0089.pdf) |
| **India gold-collateral and deposit frameworks** | Borrower/depositor rights depend on the loan or deposit agreement | Regulated entity holds pledged jewelry or accepts/processes eligible deposited gold | Loan/lien/safekeeping record or gram-denominated deposit account | Custody by lender is not ownership before contract/default effects. New medium/long-term government deposits ended in March 2025; short-term bank deposits and related gold-metal-loan machinery continue. [RBI collateral directions](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12893), [RBI gold monetization](https://www.rbi.org.in/scripts/NotificationUser.aspx?Id=10084) |
| **U.S. government industrial recovery** | U.S. Government / participating agencies | DLA manages recovered stocks and supplies refined metal as government-furnished material | Program inventory and requisition records | This is an industrial procurement/recovery lane, not evidence of reserve or payment use. [DLA](https://www.dla.mil/Troop-Support/Construction-and-Equipment/Metals/), [DFARS 208.73](https://www.acquisition.gov/dfars/subpart-208.73-use-government-owned-precious-metals) |

---

## 6. Non-additivity and non-inference rules

1. **Stock ≠ flow ≠ turnover.** Above-ground stock, annual mine supply, quarterly demand, daily clearing transfers and monthly vault totals answer different questions.
2. **Vault stock ≠ owner census.** A location aggregate cannot identify ultimate owners, liens, loans, swaps or free float.
3. **LBMA includes BoE.** Do not add BoE bar counts to LBMA London tonnes. ETF and some token bullion can also already be inside that London aggregate.
4. **FRBNY total ≠ U.S. reserve.** The 6,331 t vault figure spans official customers. The separately reported U.S.-owned portion was about 418.355 t on 2026-07-31.
5. **Allocated ≠ unallocated.** Identified customer property and a bank liability denominated in gold are different legal objects.
6. **ETF share ≠ bar title.** The trust owns product assets; the investor holds a share under product terms.
7. **Token record ≠ vault title record.** The token ledger, issuer allocation ledger and custodian bar list must reconcile, and the terms determine holder rights.
8. **Warrant transfer ≠ truck movement.** COMEX delivery can transfer a document of title while the bar remains in the depository.
9. **Registered/eligible/pledged ≠ owner identity.** These are warehouse or encumbrance states.
10. **Eligibility ≠ use.** A rule allowing gold as collateral does not prove it was pledged. A legal-tender statute does not prove circulation. A custody mandate does not prove a reserve transaction.
11. **Trade code ≠ end use.** Import/export records show declared form and movement, not purchaser, beneficial title, motive or final fabrication.
12. **Recycling ≠ consumption.** Recovered gold is a secondary supply flow returning durable stock to the market.

---

## 7. Evidence gates retained for the monetary phase

The later phase should not use one binary `monetary: yes/no`. Each object or event needs independent findings:

| Gate | Required fact | Current broad-map treatment |
|---:|---|---|
| 1 | Object/form exists | Mapped here |
| 2 | Reported holder | Mapped where public |
| 3 | Beneficial/legal title | Mapped where the governing document is public; otherwise unresolved |
| 4 | Custodian, subcustodian and authoritative record | Mapped at system level; executed chains often missing |
| 5 | Allocation and encumbrance | Allocated/unallocated/pledged distinctions mapped; account-level states mostly unknown |
| 6 | Accounting classification and valuation | Deferred except to distinguish the record involved |
| 7 | Reserve-asset designation | Deferred |
| 8 | Legal-tender or payment status | Deferred |
| 9 | Collateral eligibility | May be mapped as an open legal door |
| 10 | Observed pledge, settlement, swap, loan, purchase or payment | Deferred until transaction evidence exists |
| 11 | Unit-of-account, redemption and convertibility effect | Deferred |

### The word “monetary” already has at least two official clocks

- IMF-style reserve classification turns on monetary-authority title/control and reserve-asset designation.
- U.S. customs classification under HTS 7108.20 turns on the tariff line's own coinage/currency rule.

Those are not interchangeable. Neither may be inferred from the object's shape, its location, its custodian or its ability to be sold.

---

## 8. Highest-priority unresolved evidence

### Owner and custody visibility

- No comprehensive current census of household self-custody, safe-deposit holdings or private non-reporting vaults.
- No universal bar-to-ultimate-owner map for London, New York, COMEX, ETFs or token products.
- Executed FRBNY and BoE customer agreements, customer-by-customer allocation and current site detail are not public.
- Executed bullion-bank agreements, subcustody chains, liens, insurance and insolvency opinions remain mostly private; public LPMCL forms are models.
- COMEX beneficial ownership behind clearing-member names, depository agreements, electronic-warrant control terms and account-level pledges remain unavailable.

### Product constitutions

- ETF/ETC product terms and bar lists need product-by-product review; no “gold ETF” generalization is safe.
- Token products need exact issuer, custodian, bar allocation, reconciliation, bankruptcy treatment, smart-contract control, freeze/upgrade powers and tested redemption.
- XAUT's unnamed custodian is a more basic identity gap than a missing market statistic.

### Quantification

- No official current U.S. end-use table separates jewelry, electronics, dental, aerospace and other industrial tonnage.
- Art, awards, aerospace and medical uses are real but lack defensible standalone mass series.
- Global detailed end-use tonnage below USGS's broad shares currently depends heavily on WGC/Metals Focus industry estimation.
- London, FRBNY and COMEX public data do not show owner-level free float or encumbrance.

---

## 9. Flexible handoff to the monetary research phase

The broad map does not prescribe one thesis. It creates branching tests:

| If new evidence concentrates in… | Follow first with… | Promotion test |
|---|---|---|
| Official reserve accounts or revaluation | Treasury, central-bank and IMF accounting/title lane | Current title + reserve designation + valuation rule + dated balance-sheet effect |
| State or federal legal-tender programs | Enacted-law and actual-payment lane | Effective law + implementing operator/custodian terms + first funded account/redemption/payment |
| Gold certificates or public balance-sheet claims | Treasury–Fed accounting lane | Exact obligor/holder + statutory amount + backing rule + redemption/convertibility boundary |
| COMEX, London or central-bank collateral | Settlement and secured-credit lane | Eligibility + executed lien/control terms + observed pledge/credit + release/default path |
| Deposits, swaps, leases or gold loans | Contract and encumbrance lane | Counterparty + principal + title transfer + maturity + repayment form + accounting treatment |
| ETF/ETC growth or redemption | Trust-constitution lane | Exact trust property + custodian chain + bar list + creation/redemption + investor right |
| Token issuance or state electronic-gold claims | Digital-title lane | Exact legal issuer + holder property right + authoritative title record + custody + insolvency + tested redemption |
| Cross-border gold movements | Customs/title/border lane | Exact code/form + declared owner/consignee + title clock + destination + no end-use inference |

This lens should change if the evidence changes. The invariant is not the branch order; it is the requirement to identify the **object, owner, custodian, record, authority and observed transaction** before making a monetary claim.

---

## 10. Source and evidence register

Ranks follow the Wholesale Metals data-spine hierarchy: A = machine-readable official data; B = official rules, reports or signed public instruments; C = official web description; D = audited filing or product custody disclosure; E = institutional/industry research. Rank is not a truth score; the source must still answer the right question.

| Source | Rank | Cutoff / publication state | Used for |
|---|:---:|---|---|
| [Treasury FiscalData gold reserve API](https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/gold_reserve?filter=record_date:eq:2026-07-31&sort=src_line_nbr) | A | Record date 2026-07-31 | U.S.-owned quantity by facility and stock category |
| [Federal Reserve H.4.1](https://www.federalreserve.gov/releases/h41/current/) | A/B | Week ended 2026-08-12 | Gold certificate and statutory gold-stock accounting amounts |
| [USGS Mineral Commodity Summaries 2026](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf) | B | Revised 2026-05-27; 2025 estimates | U.S. material balance, broad world consumption, recycling and reserve estimate |
| [U.S. Mint FY2025 Annual Report](https://www.usmint.gov/content/dam/usmint/reports/2025-annual-report.pdf) | B | FY2025 | Mint bullion-sales scope and government custody context |
| [FRBNY Gold Vault](https://www.newyorkfed.org/aboutthefed/goldvault.htm) and [CBIAS](https://www.newyorkfed.org/markets/central-bank-and-international-account-services) | C | Vault statistic as of 2024 | Official-customer custody role and total-vault boundary |
| [Bank of England Gold](https://www.bankofengland.co.uk/gold) | C | Updated 2026-03-12 | Allocated official custody, vault role and ownership boundary |
| [LBMA London Vault Data](https://www.lbma.org.uk/prices-and-data/london-vault-data) | C | End-2026-06 | Aggregate London stock and included/excluded perimeter |
| [LBMA Clearing Data](https://www.lbma.org.uk/prices-and-data/clearing-data) | C | 2026-05 average | Net clearing transfers; turnover-versus-stock boundary |
| [LPMCL allocated model](https://cdn.lbma.org.uk/downloads/LPMCL/1.-Allocated-Account-Agreement-2018-Clean-20231103.pdf) and [unallocated model](https://cdn.lbma.org.uk/downloads/LPMCL/2.-Unallocated-Account-Agreement-2018-Clean-20231103.pdf) | B | Current public model forms | Property-versus-credit distinction; not proof of executed customer terms |
| [COMEX Rulebook](https://www.cmegroup.com/rulebook/COMEX/) and [CME registrar reports](https://www.cmegroup.com/clearing/operations-and-deliveries/registrar-reports.html) | A/B | Current at cutoff | Warrant, warehouse, delivery and public-inventory boundaries |
| [IMF 2025 audited financial statements](https://www.imf.org/external/pubs/ft/ar/2025/pdfs/imf-annual-report-2025-financial-statements.pdf) | B | 2025-04-30 | IMF-owned quantity and depository framework |
| [BIS 2025/26 Annual Report](https://www.bis.org/about/areport/areport2026.htm) | B | 2026-03-31 | BIS-owned gold and separation from client banking liabilities |
| [GLD 2025 10-K](https://www.sec.gov/Archives/edgar/data/1222333/000143774925036305/gld20250930_10k.htm) | D | 2025-09-30 | Trust ownership, quantity, allocation, custodian and redemption boundary |
| [IAU 2025 10-K](https://www.sec.gov/Archives/edgar/data/1278680/000143774926006055/iau20251231_10k.htm) | D | 2025-12-31 | Trust/share/custodian legal topology |
| [Paxos PAXG terms](https://www.paxos.com/terms-and-conditions/pax-gold-terms-conditions) and [transparency](https://www.paxos.com/paxg-transparency) | D | Terms modified 2025-12-12; attestations through 2026-05 | Issuer-defined beneficial interest, allocation and redemption gates |
| [XAUT FAQ](https://gold.tether.to/faq), [assurance](https://gold.tether.to/docs/reports/attestations/ISAE_3000R_-_Opinion_TGRR_31.03.2026_RC187322026DV0089.pdf) and [risk disclosure](https://gold.tether.to/legal/riskdisclosurestatement) | D | Assurance 2026-03-31 | Token/bar representation and unresolved custodian/access risks |
| [WGC above-ground stock](https://www.gold.org/goldhub/data/how-much-gold), [2025 annual demand](https://www.gold.org/goldhub/research/gold-demand-trends/gold-demand-trends-full-year-2025) and [2026 Q2 demand](https://www.gold.org/goldhub/research/gold-demand-trends/gold-demand-trends-q2-2026) | E | End-2025 through 2026 Q2 | Modeled stock allocation and detailed current demand/supply flows |
| [RBI Gold Monetization Scheme](https://www.rbi.org.in/scripts/NotificationUser.aspx?Id=10084) and [gold/silver collateral directions](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12893) | B | Current at cutoff | Deposit, metal-loan, pledge and safekeeping lanes |
| [DLA Precious Metals Recovery Program](https://www.dla.mil/Troop-Support/Construction-and-Equipment/Metals/) and [DFARS 208.73](https://www.acquisition.gov/dfars/subpart-208.73-use-government-owned-precious-metals) | B/C | Current at cutoff | Government industrial recovery and reuse |

## Bottom line

The broad plotline is not “gold is becoming money” or “gold is merely a commodity.” The current evidence shows one unusually durable substance simultaneously serving as fabricated material, cultural object, private holding, official asset, collateral base, title object and substrate for financial claims.

The next phase can ask where those roles become monetary, but it must do so one mechanism at a time. The first questions are now stable:

> **What is the object? Who owns it? Who holds it? Which record controls it? Is it allocated or encumbered? What authority classifies it? What transaction actually occurred?**

Until those are answered, “gold held,” “gold backed,” “gold eligible,” “gold settled” and “gold used as money” remain different claims.
