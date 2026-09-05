> Source evidence cutoff: 2026-08-23 ET

# Gold Balance of Payments and Currency Adjustment 2025-2026

## Executive ruling

Gold can be a large current-account swing item and a powerful BOP-financing
asset. Those are different mechanisms.

1. **Nonmonetary-gold trade** creates goods credits and debits when economic
   ownership changes between a resident and nonresident.
2. **Monetary gold** is a reserve asset. Transactions between monetary
   authorities enter the financial account; monetization, demonetization and
   price changes are not ordinary trade flows.
3. **Gold-backed liquidity** can exchange an illiquid or encumbered gold
   position for usable foreign currency, but a loan or swap is not a gold sale.
4. **Gold appreciation** can lift the market value of reserves and improve
   ratios without producing export receipts, cash or a BOP transaction.
5. **Currency pressure** depends on the financing counterpart: who receives the
   payment currency, whether it is converted or retained, whether a central bank
   absorbs it, and whether intervention, hedging or reserve accumulation offsets
   the initial trade flow.

Tariffs belong in this packet only as a timing, routing and landed-cost shock.
They do not own the BOP or currency mechanism.

## What the completed comparison shows

| Case | Demonstrated balance-of-payments role | Currency conclusion |
|---|---|---|
| United States | Gold balance swung **US$96.577bn** from 2025Q1 to Q2 | Dollar effect unresolved because financing and conversion mix are unpublished |
| Australia | 2025 national BOP gold surplus **A$41.092bn** | AUD conversion and RBA absorption unobserved |
| Switzerland | Precious-metals-inclusive customs book lowered 2025 balance by **CHF16.2bn**; exact quarterly BOP gold component remains blank | CHF settlement/conversion unobserved; reserve quantity stayed flat while value rose |
| United Kingdom/London | Large mixed-precious-metals BOP deficits coexisted with falling BoE custody | Ownership and location books can move in opposite directions |
| Ghana | Gold dominated exports and sat inside a **7.9%-of-GDP** CA surplus plus large official FX intermediation | Material aggregate role at `R3`; exclusive share of cedi appreciation not isolated |
| Uganda | One domestic pilot test, no scaled reserve result | Nearly US$3.5bn FX purchases damped appreciation; gold link remains `R1` |
| Sierra Leone | Gold was eligible in the NIR definition but no stock/transaction was reported | Negative control: no demonstrated gold contribution |
| India 1991 | US$600m of gold-backed liquidity during a US$9.7bn CA-deficit crisis | Financing bridge, not sole cause of devaluation or BOP closure |

## Why the role can be large

The completed upstream packet already owns the current U.S. BOP observations.
It reports U.S. nonmonetary-gold exports of US$15.461bn and imports of
US$78.486bn in 2025Q1 (`SER-GTIMF-021`, `SER-GTIMF-026`), producing a derived
net gold contribution of **−US$63.025bn**. In 2025Q2 exports were US$37.395bn
and imports US$3.843bn (`SER-GTIMF-022`, `SER-GTIMF-027`), producing
**+US$33.552bn**. The gold component therefore swung **US$96.577bn** quarter to
quarter.

These figures demonstrate magnitude, not a dollar-price effect. They are part
of the U.S. goods/current account, while their financing counterparts sit in
financial claims, liabilities, trade credit or reserve behavior. The public
table does not disclose invoice currency, conversion, hedge or beneficial
owner.

## The balancing question

For each gold flow the packet will answer:

| Gate | Required fact |
|---|---|
| External boundary | Which party is resident and which is nonresident? |
| Ownership | Did economic ownership change, or did only a bar or warrant move? |
| Account | Goods/current account, financial account, other-volume change, valuation or domestic-only event? |
| Counterpart | Deposit, security, trade credit, loan, reserve asset, liability or unmeasured statistical discrepancy? |
| Currency stack | Quote, invoice, payment, funding, hedge, collateral, reserve and intervention currencies—which are actually disclosed? |
| Intermediation | Did an exporter retain FX, sell it to a bank, or deliver it to the monetary authority? |
| Policy result | Reserve accumulation, FX sale, import/debt-service financing, sterilization, base-money effect or none? |
| Currency result | What exchange-rate, forward, liquidity or intervention movement was observed, and can gold's contribution be isolated? |

## Accounting identities to materialize

All derived values must point to canonical source-series IDs.

```text
gold_goods_balance = nonmonetary_gold_export_credit
                   - nonmonetary_gold_import_debit

reserve_stock_change = BOP reserve transactions
                     + valuation changes
                     + other changes in volume

program_NIR_change = qualifying liquid external assets at program prices
                   - qualifying short-term external reserve liabilities
                   - specified exclusions and encumbrances
```

`gold_goods_balance` is not total goods balance or current account. A bilateral
gold balance is not a national current-account balance. A program NIR change is
not necessarily the same as the market-valued reserve-stock change.

## Core hypotheses

| Hypothesis | Current state | Promotion receipt |
|---|---|---|
| Gold was a first-order swing item in the U.S. 2025 quarterly goods account | `DEMONSTRATED-MAGNITUDE` | Current BEA Table 2.1 vintage and controlled subtraction |
| Early-2025 Atlantic physical relocation and BOP flows were the same complete transaction chain | `NOT-PROVED` | Owner/consignee/bar/refiner records and resident/nonresident title chain |
| Swiss and Australian gold exports created direct CHF/AUD appreciation pressure | `UNRESOLVED` | Invoice/payment currency, conversion, hedge and central-bank absorption data |
| Ghanaian gold materially supported current account, reserves and FX intermediation | `DEMONSTRATED-AGGREGATE` | IMF/BoG records; ounce-to-export-to-FX reconciliation remains incomplete |
| Higher official-gold prices equal reserve accumulation from BOP flows | `FALSE-AS-GENERAL-CLAIM` | Transactions and valuation must be separately reconciled |
| Pledged gold is fully available for intervention or program NIR | `FALSE-AS-GENERAL-CLAIM` | Contract availability and program exclusions control |
| A gold-driven current-account improvement requires currency appreciation | `FALSE-AS-GENERAL-CLAIM` | Financial-account counterpart and policy response can offset it |

## Materialized outputs

- Country-period, double-entry accounting-leg, currency-counterpart and
  relationship CSVs with twenty-three periods, eighteen accounting legs,
  twelve typed currency records and twenty-two relationship controls. Every
  populated country-period value has validator-enforced non-additivity
  semantics.
- Formula-driven review workbook with the U.S. quarterly swing and six passing
  checks.
- Atlantic and producer/reserve case matrices, the integrated currency map,
  claim audit, forward watchboard and twenty scoped document requests.
- Fourteen exact new official source captures plus hash-frozen upstream
  dependencies.

## Remaining evidence gaps

1. Shipment-level invoice, payment, funding and hedge currency.
2. London/FRBNY/COMEX owner and bar-level continuity.
3. Country-comparable monthly or quarterly nonmonetary-gold BOP series outside
   the United States.
4. Complete Ghana ounce-to-refining-to-retention/export-to-FX reconciliation.
5. Program-NIR and market-reserve reconciliation at both fixed and current gold
   prices.
6. Central-bank intervention records sufficient to separate gold-related FX
   absorption from other intervention.

## Further research plan

### Priority 1 — close one real transaction chain

Use Ghana as the best candidate. Obtain lot/assay/refinery/export/off-take,
invoice/payment, receipt-bank, repatriation, FX-operation and reserve-use records
for a bounded period. This is the only path likely to raise a live case from
aggregate `R3` to transaction-level `R4`.

### Priority 2 — finish comparable national series

Recover the exact SNB 7108.1200 selector/API receipt and freeze the ONS
FSII/FSIF series with the mixed-metals methodology. Continue BEA and ABS
vintage-controlled quarterly panels. Do not use customs mirrors as substitutes.

### Priority 3 — reconcile reserves

Build opening-stock-to-closing-stock bridges for Ghana and any later executing
Uganda case: transactions, monetization/demonetization, availability,
collateral, price/FX valuation, liabilities, current-price GIR and fixed-price
program NIR.

### Priority 4 — test currency disposition

Seek redacted invoices, payment messages, bullion-bank financing, hedge
confirmations and central-bank purpose-tagged FX operations. Until these exist,
keep CHF/AUD/GBP/USD conversion claims unresolved.

### Priority 5 — preserve controls

Keep Sierra Leone as the eligibility-without-presence control and India 1991 as
the liquidity-without-BOP-closure comparator. They stop future research from
promoting rule text or crisis sequence into causal proof.

## Promotion boundary

This document is a review-ready pending research answer and the read-first
document for Research Desk card `gold-bop-currency-adjustment`. The Desk
projection preserves it as Workbench evidence rather than vault doctrine. It
changes no Currency Watch grade, does not claim a gold-caused exchange-rate
move without a causal receipt, and does not create a vault watch or canonical
research landing.
