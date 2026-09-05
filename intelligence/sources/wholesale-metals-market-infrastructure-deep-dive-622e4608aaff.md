# The Wholesale Metals Market Infrastructure

## How title, clearing, vaults, borders, and benchmarks turn metal into money

Updated: 2026-07-12  
Status: integrated first deep dive  
Scope: COMEX/CME, London/LBMA/LPMCL, Shanghai SGE/SHFE, the emerging Hong Kong bridge, and the legal conversion paths among them

Companion records:

- `COMEX_CME_LEGAL_INFRASTRUCTURE_DEEP_DIVE.md`
- `LONDON_BULLION_LEGAL_INFRASTRUCTURE_DEEP_DIVE.md`
- `SHANGHAI_GLOBAL_METALS_INFRASTRUCTURE_DEEP_DIVE.md`
- `WHOLESALE_METALS_CLAIM_AUDIT.md`

---

## The story in one line

Gold and silver do not move through one global market. They move through a federation of legally distinct claims—futures positions, unallocated bank debts, allocated bars, electronic warrants, vault ledgers, benchmark trades, exchange bullion accounts, and border permits—whose prices normally converge but whose conversion rules become visible under stress.

The grouped change is:

> **The wholesale physical core is becoming more provenance-aware, digitally legible, collateralized, and continuously connected at the same moment price access is becoming smaller, cash-settled, cloud-based, and nearly continuous. Hong Kong is now being built as a translation layer between London-style unallocated bullion and Shanghai's allocated physical-account system.**

This is a synthesis of public documents, not a claim that the institutions share one hidden plan. The overlap is architectural.

---

## 1. The machine: one price story, several legal objects

| Object | Holder actually owns or is owed | Controlling institution/document | Principal failure seam |
|---|---|---|---|
| COMEX futures position | Contractual position against CME Clearing through a clearing member | COMEX product rules; CME Chapter 8; FCM agreement | Clearing-member default, margin, recovery/tear-up, emergency rule |
| COMEX warrant | Electronic UETA transferable record and UCC Article 7 document of title to conforming metal | NYMEX/COMEX Chapter 7; issuing depository; CME delivery system | Control, lien priority, duplicate/error, facility/custodian failure |
| Pledged COMEX warrant | Encumbered document of title posted as CME performance bond | CME Rule 817, UCC-1 filing, collateral program | CME/liquidity-lender lien; unavailable for delivery while pledged |
| London unallocated balance | Contractual obligation of bullion-bank account provider to transfer equivalent metal | LPMCL model agreement; bilateral bank ledger; AURUM | Bank credit/resolution risk; allocation not completed |
| London allocated account | Identified bars recorded as customer property and held by custodian/bailee | Executed allocated agreement and bar list | Lien, sub-custody, identification, insurance, sanctions, release delay |
| Bank of England allocated gold | Customer title to identified bars on the Bank's custody ledger | BoE account terms and official custody books | Access, withdrawal timing, sanctions, undisclosed account terms |
| SGE bullion-account balance | Bullion ownership/entitlement within SGE's physical registry and certified-vault network | SGE clearing/delivery rules; member/customer accounts | Member insolvency, border permission, vault/warrant records |
| SHFE standard warrant | Receipt entitling holder to physical commodity at an approved storage facility | SHFE delivery and product rules | Warehouse performance, tax invoice, member default, eligibility |
| Hong Kong HKPMCC balance | Trial unallocated, commingled entitlement to approximately 400-ounce gold | HKPMCC clearing rulebook and participant terms | Full rulebook not yet public; allocation/finality/insolvency unresolved |
| ETF share | Security representing a trust/fund interest, not direct ownership of the custodian's own assets | Prospectus, trust deed, custodian/AP agreements | Share/bar conversion gates, custody chain, AP concentration |

The research rule is simple: **never use “gold,” “silver,” “inventory,” “delivery,” “clearing,” or “ownership” without naming the legal object and institution.**

---

## 2. New York: contract becomes title before title becomes possession

Commodity Exchange, Inc. is a New York not-for-profit corporation and CFTC-regulated designated contract market. It is a wholly owned CME Group subsidiary legally controlled through NYMEX's sole New York not-for-profit membership. It owns the COMEX rulebook and products.

It is not the clearing house. Chicago Mercantile Exchange Inc., through its CME Clearing division, is the registered systemically important derivatives clearing organization. CME Clearing becomes buyer to seller and seller to buyer and deals with clearing members, not the beneficial customer.

The conversion chain is:

```text
market position
    → CME Clearing obligation
    → clearing-member/FCM account
    → delivery tender and assignment
    → cash against electronic warrant
    → UCC title at approved depository
    → optional later cancellation and physical load-out
```

Delivery therefore occurs when payment and electronic warrant transfer pass title. A truck leaving a vault is a later event.

### The warrant is the METAL × PLUMBING hinge

COMEX Rule 705 defines a metal warrant as both an electronic transferable record and a UCC Article 7 document of title. A clearing member holds it for the metal owner. It can be:

- **registered:** a conforming bar has a warrant;
- **eligible:** a conforming bar in an approved facility has no warrant;
- **pledged:** a registered warrant is posted to CME Clearing and cannot simultaneously be used for futures delivery.

CME accepts qualifying COMEX gold warrants and London gold bullion as performance-bond collateral subject to a 15% haircut and a combined program cap. It perfects its interest through UCC-1 filings; Rule 817 permits a lien in favor of liquidity lenders.

That is the central discovery. Physical gold is not merely the thing under a derivative. **Its electronic title is itself an asset inside the clearing house's collateral and liquidity constitution.**

Phase 2 located the executed lender-facing instrument behind that statement: CME's SEC-filed syndicated clearing-house credit agreement, amended through April 22, 2026. Chicago Mercantile Exchange Inc. is borrower; Bank of America is administrative agent; Citibank is collateral agent and collateral-monitoring agent. The agreement expressly brings Gold Warrant Collateral Documents, the warrants, the gold they represent, clearing-member joinders, UCC/PPSA filings, control agreements, custodian data, liquidation proceeds, and lender foreclosure into the secured-liquidity package. The current public execution copy therefore proves that Rule 817's possible lender lien is operational contract architecture, not merely reserved rulebook language.

The still-missing layer is now specific: the incorporated Security and Pledge Agreement, individual Gold Warrant Collateral Documents, actual UCC filings, clearing-member joinders, control/custody acknowledgements, and approved warrant form.

### The guarantee has boundaries

CME's base-products waterfall uses defaulting-member resources, a $100 million CME contribution, the mutual guaranty fund, and assessments. Chapter 8 also contains gains haircutting, tear-up, limited-recourse, and non-petition provisions. COMEX emergency rules permit changed delivery points or methods, liquidation-only trading, forced position reduction, fixed settlement, transfer, suspension, and temporary rule suspension.

Physical delivery is real. It is not an unconditional bar-for-bar promise outside the rulebook.

### Current direction

New York is simultaneously strengthening the physical core and widening abstract price access:

- 2022: warrants expressly modernized as UETA/UCC electronic title; insurance-contingency mechanics added.
- 2024–26: Loomis and Malca-Amit facilities expand custody capacity.
- 2024–26: production-date, brand, refiner, and origin eligibility becomes more granular.
- February 2026: new per-warrant registration, transfer, and cancellation/load-out fees.
- February 2026: financially settled 100-ounce silver futures follow financially settled 1-ounce gold.
- May 2026: post-cutoff production from two Chinese silver brands loses delivery eligibility; legacy bars remain eligible.
- July 24, 2026 scheduled: financially settled 1-ounce gold moves to 24/7 Globex execution.
- Q4 2026 onward: Globex begins staged Google Cloud migration; metals date still unannounced.
- Later: metals are an upcoming SPAN 2 margin-model migration, not yet a dated production event.

The signal is segmentation: a legally explicit wholesale title core supporting broader, smaller, continuous cash-settled exposure.

---

## 3. London: metal begins as bank debt and may become property

London's core market is not a COMEX-style exchange and LPMCL is not publicly documented as a universal CCP.

London Precious Metals Clearing Limited is a private English company owned by HSBC, ICBC Standard Bank, JPMorgan, and UBS. Its AURUM system coordinates matched instructions and bilateral net settlement through reciprocal unallocated accounts. Citi joined on July 6, 2026 through the published non-equity User Member route, widening access without changing the four-owner structure visible on the public site.

The central chain is:

```text
customer trade obligation
    → bullion-bank customer ledger
    → AURUM matched instruction
    → reciprocal unallocated clearer accounts
    → bilateral net transfer / allocation call
    → optional identified bars in custody
```

### Unallocated is credit; allocated is identified property—with qualifications

Under LPMCL's model unallocated agreement, the provider owes the customer an amount of metal. The customer does not own specific bars and bears account-provider credit risk.

Under the allocated model, specific bars are identified as customer property and the provider acts as custodian/bailee. But the same form permits:

- third-party and affiliate sub-custody;
- sharply limited responsibility for a sub-custodian's insolvency absent bad appointment conduct;
- a broad general lien and sale power for actual or contingent obligations;
- bar substitution for like-quality bars;
- no duty to insure unless the schedule says otherwise;
- broad force majeure;
- sale of bars after six months if the customer fails to arrange acceptable delivery following termination.

Allocated metal greatly improves the customer's title position. It does not eliminate lien, sub-custody, record, sanctions, insurance, or release risk. The executed schedule and sub-custody chain control.

Phase 2 located executed SEC-filed JPMorgan and HSBC allocated/unallocated agreements for SPDR Gold Trust. They are the best public proof that the LPMCL model is not “the deal”: negotiated accounts specify named vaults/sub-custodians, daily reporting, audit rights, sanctions, corrections/reversals, delivery cutoffs, risk allocation, and tighter substitution rules. They show what a powerful customer can negotiate, but cannot be generalized to ordinary wholesale accounts.

Phase 2 also confirmed that LPMCL/AURUM does not appear on the Bank of England's current list of systems designated under the Financial Markets and Insolvency (Settlement Finality) Regulations. That does not prove a transfer lacks contractual or property-law finality. It means statutory insolvency protection must not be attributed to AURUM without the private Rules, a designation, or an authoritative legal opinion identifying entry, irrevocability, posting, correction, and insolvency-survival points.

### Three different meanings of London clearing

1. **LPMCL/AURUM:** bilateral bullion-bank account settlement and netting.
2. **IBA auction/ICE:** unmatched benchmark-auction volume may become ICE daily futures cleared at ICE Clear US while metal settles through LPMCL unallocated accounts.
3. **CME London products:** centrally cleared London forwards or spot products with separate CME margin/default rules and delivery through LPMCL-member accounts.

One word—“clearing”—therefore describes three different credit constitutions.

### The Bank of England's role

The Bank holds allocated gold for HM Treasury, central banks, and selected commercial firms. Title remains with the customer and ownership changes can be recorded by book entry without moving the bar. The Bank says it is not an LBMA member and does not regulate the bullion market.

Its March 2026 commercial-access criteria explicitly tie accounts to central-bank market access and London liquidity. The Bank is an official deep-custody and title-transfer node embedded in a private market—not the market's guarantor.

### Current direction

London is moving from aggregate trust toward bar-level data governance and broader balance-sheet integration:

- 2025: the distributed-ledger Gold Bar Integrity database goes live.
- Early 2026: LBMA says all Good Delivery refiners are using it.
- December 2026 target: custodians onboard and submit aggregate vault holdings through the platform.
- Longer term: near-real-time data, though LBMA expressly says it does not receive ownership data.
- July 2026: Citi joins LPMCL and becomes an Approved Weigher.
- July 2026: ICE Benchmark Administration now administers all four LBMA precious-metals benchmarks.
- 2025–27 plan: infrastructure/settlement, London FMI, digitalisation/tokenisation, transparency, and advocacy for gold to become HQLA.

Gold is **not** Level 1 HQLA as of this review. The industry is lobbying for that treatment.

---

## 4. Shanghai: the state controls the border, the exchange controls the ledger

China operates two separate precious-metals machines.

### SGE

Shanghai Gold Exchange is a PBoC-supervised membership legal person. It is simultaneously a spot/deferred/benchmark/leasing venue, CCP for centralized trades, bullion-account registry, vault/refiner certifier, settlement organizer, and logistics administrator.

Imported gold must generally be licensed by PBoC, registered, and first traded through a State Council-approved spot gold exchange. PBoC may restrict import/export approvals for macro-control. Gold moving only between overseas and bonded zones is generally treated differently from metal entering mainland circulation.

That border is a monetary valve. A Shanghai premium can persist because price does not confer permission to import, withdraw, pay tax, create the required account, or convert bonded bullion into domestic metal.

### SHFE

Shanghai Futures Exchange is a separate CSRC-supervised futures CCP. Its gold and silver positions clear through members; physical delivery uses standard warrants, approved warehouses, cash settlement, and tax invoices. Natural persons cannot take SHFE gold delivery. QFIs gained access to gold/silver futures and gold options in 2022, but that is not unrestricted international physical access.

### CME–SGE contracts are price bridges

The reciprocal 2019 CME and SGE contracts cash-settle against each other's benchmark prices. They permit direct trading of the New York/Shanghai basis but do not move a bar between COMEX and SGE. Physical conversion still requires refiners, bar eligibility, transport, customs, licenses, vault accounts, and tax compliance.

---

## 5. Hong Kong: the new translation layer

This is the strongest new finding.

In June 2025 SGE opened its first offshore International Board vault at Bank of China (Hong Kong) and introduced Hong Kong-delivery contracts. Hong Kong's government and SGE then formalized cooperation in January 2026.

On July 7, 2026, the government-owned Hong Kong Precious Metals Central Clearing Company began trial operation with eleven banks and launched the first phase of **Delivery Connect**:

- HKPMCC maintains a central ledger for bilateral/OTC gold settlement.
- The trial system holds unallocated, commingled approximately 400-ounce international-standard bars.
- BOC Hong Kong is settlement institution and designated vault.
- HKPMCC became an SGE international member and opened an SGE physical gold account.
- Initial banks completed two-way transfers between HKPMCC and SGE's Hong Kong International Board vault.
- Planned RTGS integration is meant to add cash delivery-versus-payment.

Hong Kong is therefore being designed to translate among:

```text
London-like unallocated 400 oz OTC balances
        ↕ HKPMCC central ledger / BOC(HK) vault
        ↕ Delivery Connect
SGE International Board physical account and vault system
```

The announced program goes further: more than 2,000 tonnes of storage within three years, a thousand-tonne airport facility, refining, specie insurance, tax incentives, HAU reference pricing, ETFs including physical redemption, derivatives, and dispute infrastructure.

The full HKPMCC Clearing Rulebook and Delivery Connect operating manual were not located publicly. Allocation, insolvency rights, finality, bar substitution, haircut, default resources, and conversion mechanics remain open. But the operating bridge—not merely a memorandum—now exists.

---

## 6. The cross-market conversion map

| Conversion | Normal bridge | What can break |
|---|---|---|
| London unallocated → London allocated | Bullion bank allocates identified Good Delivery bars | Bank credit, available bars, credit limit, vault processing, lien |
| London allocated → COMEX warrant | Refining/recasting, approved brand, transport, customs, approved depository, warrant issuance | Bar size/fineness, refinery capacity, tariff, carrier/vault throughput |
| COMEX future → warrant | Delivery tender, clearing assignment, cash against warrant | Clearing-member default, margin, emergency rule, warrant availability |
| COMEX warrant → physical possession | Warrant cancellation and depository load-out | Lien, fees, identity, carrier, vault delay, sanctions |
| London/COMEX price → Shanghai price | Reciprocal cash-settled benchmark futures | FX, time-zone, basis liquidity; no physical bridge implied |
| Offshore/bonded gold → mainland SGE gold | PBoC license, customs, member eligibility, registration/first-sale rules | Macro-control, permit quota, tax, account/border status |
| HK unallocated → SGE physical account | HKPMCC Delivery Connect through SGE Hong Kong vault | Unpublished conversion/finality rules, bar form, member eligibility |
| ETF share → bullion/contract | Authorized participant or SGE ETF creation/redemption path | AP gate, minimum unit, prospectus rights, custody and account rules |

The cross-market price is maintained by the cost and availability of these conversions. A basis blowout is evidence that conversion has become expensive or slow; it is not automatically proof that an exchange defaulted.

---

## 7. Dated transition spine

| Date | Event | Structural meaning |
|---|---|---|
| 2019 | CME and SGE launch reciprocal Shanghai/New York contracts | Formal price bridge without physical fungibility |
| Mar–Apr 2020 | Refinery/logistics shock blows out London–COMEX basis; COMEX adds 4GC enhanced delivery | Contract adapts to bar-form and location bottleneck |
| 2021 | SGE revises clearing rules; London accelerates vault reporting | More formal CCP/default mechanics and transparency |
| 2022 | COMEX warrants expressly become UETA/UCC electronic title; SGE/SHFE operate under new Futures and Derivatives Law; QFIs gain SHFE metals access | Commercial-law title and statutory modernization |
| 2022–23 | LBMA code and LPMCL model agreements/rules refreshed | Conduct and bilateral custody constitution updated, core architecture retained |
| 2024 | COMEX expands depository capacity; provenance-date rules; LPMCL publishes SOC 2 and adds independent NED; LBMA selects GBI platform provider | Physical capacity, controls, and digital provenance |
| Jan–Jun 2025 | GBI live; SGE bank/member/ETF rules revised; SGE Hong Kong vault opens | Bar-level assurance and international physical perimeter expansion |
| 2025 | London–New York tariff dislocation moves substantial gold toward COMEX | Logistics/tariff-risk stress reveals conversion machinery |
| Dec 2025–Jan 2026 | COMEX clearing-member and bylaws changes support supplemental/longer trading; current bylaws take effect | Governance and operating-clock modernization |
| Feb 2026 | COMEX adds warrant fees and cash-settled 100-ounce silver | Title infrastructure monetized; small price access widened |
| Mar–Jul 2026 | BoE access criteria, all refiners on GBI, Citi joins LPMCL, all benchmarks at IBA | Official liquidity, data, access, and benchmark consolidation |
| May 2026 | Malca-Amit approved as COMEX depository; collateral-custodian application pending; Chinese silver brands cut off by production date | Capacity expansion and granular provenance control |
| Jun–Jul 2026 | HKPMCC/Delivery Connect launches; COMEX schedules 24/7 1-ounce gold | Cross-border physical-account bridge and continuous price execution |
| By Dec 2026 | LBMA custodian GBI target; planned HK RTGS/DvP development; CME cloud pilot begins in other assets | Data, cash finality, and technology migration; metals-specific dates require confirmation |

---

## 8. Website watchboard

### COMEX/CME

Watch weekly/monthly:

- COMEX Chapter 7 service-provider and brand files;
- depository stock reports, including registered, eligible, pledged, receipts and withdrawals;
- delivery issues/stops, warrant registrations/cancellations, EFP volume, margin, and position-limit filings;
- Malca-Amit collateral-custodian approval;
- 24/7 1-ounce gold production launch and any expansion to deliverable GC/SI;
- metals dates for Google Cloud and SPAN 2;
- new lien, custody, liquidity-facility, or collateral-program terms.

### London

Watch:

- new LPMCL User Members and executed/public terms;
- GBI custodian onboarding and the December 2026 reporting milestone;
- whether bar-level data becomes near-real-time and what remains private;
- changes to allocated/unallocated model agreements and the UK-sanctions drafting anomaly;
- BoE commercial-account criteria and withdrawal/access language;
- HQLA advocacy versus actual Basel/FCA/PRA rule change;
- tokenization projects that specify legal title rather than merely a digital twin.

### Shanghai/Hong Kong

Watch:

- HKPMCC Clearing Rulebook, participant agreement, and Delivery Connect manual;
- RTGS/DvP activation, bank additions, HAU methodology, and operating volumes;
- vault/refinery/storage build against the 2,000-tonne target;
- final PBoC/Customs import-export rules after the 2026 consultation;
- SGE/SHFE current vault, bank, refiner, and member lists;
- tax and ETF rules governing physical redemption;
- whether Delivery Connect expands beyond Hong Kong-held gold or into silver.

---

## 9. Corrections to the existing monetary narrative

The companion claim audit preserves the archive while tightening synthesis. The most consequential corrections are:

- roughly 393 tonnes entered COMEX vaults after the U.S. election, but the evidence does not trace all 393 tonnes directly from Bank of England vaults;
- no primary support was located for JPMorgan beneficially owning 750 million ounces of silver;
- SLV metal held by JPMorgan as custodian is trust property, not automatically JPMorgan proprietary metal;
- open interest divided by registered stock is not a count of multiple property owners or an automatic default ratio;
- registered-to-eligible reclassification can cancel a warrant without moving the bar;
- the alleged Thanksgiving 2025 COMEX failure, secret $65 million settlement, and March roll remain unverified;
- Shanghai/COMEX comparisons require tax, FX, timestamp, contract, location, and border normalization;
- Basel's narrow 0% risk weight for certain matched allocated-bullion exposures is not “gold became Tier 1 capital”; gold is not presently Level 1 HQLA.

These corrections weaken sensational formulations but strengthen the project. The actual machinery is more consequential than the paper-versus-physical slogan.

---

## 10. Fit with the Money Crosswalk

This research should not become a new top-level plotline. It is the missing shared layer beneath:

- `Gold & precious metals`;
- `The Fed & Bessent's gold reset`;
- `The world's money`;
- `The states' money`;
- `Clearing & settlement`;
- the Entity Theory map.

It adds a sixth operational question inside the existing five poles:

| Pole | Metals-market expression |
|---|---|
| METAL | bar, fineness, refiner, reserve, vault, withdrawal |
| PLUMBING | CCP, bilateral ledger, warrant, DvP, margin, collateral, RTGS |
| WALL | import license, sanctions, brand suspension, member gate, tax |
| TOKEN | digital twin, tokenized title claim, collateral representation |
| STATE-LEDGER | SGE bullion account, SHFE warrant system, HK government clearing ledger |

The unifying question becomes:

> **Which ledger defines the claim, which institution guarantees or merely records it, which document creates title, which lien outranks the holder, which vault makes it withdrawable, and which border authority permits conversion?**

That is the commodities contribution to the Freedom 250 monetary thesis.

---

## 11. Next legal-document pulls

1. Full LPMCL Rules, historical redlines, Citi User Member agreement, and bilateral clearer agreements.
2. HKPMCC Clearing Rulebook and Delivery Connect operating manual.
3. Executed vault/depository/regularity, sub-custody, insurance, control, and audit agreements in all three systems.
4. Sample COMEX warrant, electronic-delivery-system terms, UCC control agreement, UCC-1 form, and CME liquidity-lender documents.
5. Bank of England gold custody terms and account-level withdrawal/lien language.
6. SGE/SGEI articles, current Chinese controlling rules, customer-insolvency analysis, and current entity rosters.
7. Primary 2026 PBoC/Customs draft and final redline.
8. Representative EFP confirmations and refinery/carrier contracts linking London, New York, and Shanghai/Hong Kong.
9. Account-specific CASS, English bailment, U.S. UCC, PRC property/bankruptcy, and Hong Kong settlement-finality opinions.
10. Bulk daily data archive from 2019 onward for stocks, warrants, deliveries, EFPs, margins, lease rates, basis, and vault flows.

---

## Bottom line

The project was right that commodities are crucial, but the crucial unit is not simply the ounce.

The monetary unit inside this machine is **a legally recognized claim capable of surviving transfer, collateralization, default, custody, and a border crossing.** New York turns a cleared position into electronic UCC title; London turns bank credit into allocated property when the account holder crosses the allocation seam; Shanghai combines the exchange, CCP, bullion registry, and import gate; Hong Kong is now building the adapter between offshore unallocated gold and SGE's physical accounts.

The prices are the visible surface. The monetary constitution lives underneath—in title, priority, eligibility, finality, withdrawal, and permission.
