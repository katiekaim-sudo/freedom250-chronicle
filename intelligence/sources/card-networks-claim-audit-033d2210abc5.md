> Source created: 2026-07-29

# Card-Network Stablecoin Product-Line Claim Audit

> **Read before synthesis.** This is the card/stablecoin correction ledger for
> [Card Networks — Stablecoin Product Lines](../sources/card-networks-stablecoin-product-lines-8bca609f0991.html) and [Card Networks — Entity and Flow Map](../sources/card-networks-entity-and-flow-map-d2b978d0ade2.html).

## Carry / correct ledger

| ID | Tempting claim | Verdict | Carry instead |
|---|---|---|---|
| CN-01 | Credit cards are moving onto stablecoin rails. | **Too broad.** | Card networks are adding several stablecoin product lines; most preserve the card credential and merchant constitution. |
| CN-02 | A stablecoin-funded card means the merchant accepted stablecoin. | **False.** | In the dominant T1 model, the program converts/reserves against the balance and the merchant receives ordinary card settlement. |
| CN-03 | Visa's $7B annualized run rate was spread across nine chains. | **Unsupported.** | Visa reported one overall annualized settlement run rate and separately reported nine supported pilot chains; it disclosed no chain allocation. |
| CN-04 | Visa's 130+ programs are all one Visa-issued card. | **False.** | They are a portfolio of program-specific issuers, managers, assets and country clocks using Visa acceptance. |
| CN-05 | “Millions of customers” means millions of active Bridge cards. | **False.** | The phrase describes potential reach through named wallet platforms, not issued cards, spend or active users. |
| CN-06 | Mastercard's five named stablecoins are all live on all named chains. | **False.** | USDC supports early flows; other assets are rollout objects, and Mastercard publishes no asset-by-chain compatibility matrix. |
| CN-07 | Mastercard's named banks are all settling now. | **False.** | The June 2026 release describes named institutions as expected early participants. |
| CN-08 | Mastercard settlement to an acquirer proves merchant stablecoin payout. | **False.** | Acquirer receipt and the acquirer's downstream merchant payout are separate clocks and contracts. |
| CN-09 | Stripe's stablecoin card line is still only future. | **Stale.** | Stripe reports cards across 30 countries; Phantom is a named production example. Deel's specific card retains its own clock. |
| CN-10 | Stripe stablecoin acceptance works through Stripe Terminal. | **Not established.** | Current evidence supports web/mobile wallet checkout; Terminal documentation does not list a native physical stablecoin method. |
| CN-11 | PayPal's crypto checkout pays the merchant in PYUSD. | **False under current terms.** | The crypto/PYUSD conversion chain ends in fiat merchant credit. Hyperwallet PYUSD payout is a separate product. |
| CN-12 | Checkout.com stablecoin acceptance and stablecoin settlement are one flow. | **False.** | Coinbase-powered customer acceptance with USD merchant settlement and Fireblocks-powered merchant stablecoin receipt are separate products. |
| CN-13 | FIUSD is already a general Clover payment method. | **Unsupported.** | FIUSD remains a deployment watch; public material does not establish an operative Clover method or complete issuer constitution. |
| CN-14 | JCB now accepts stablecoins at all JCB merchants. | **False.** | JCB has exploration and PoC objects; production merchants, terms, applications and remedies are not established. |
| CN-15 | Square Bitcoin proves stablecoins are live on ordinary card terminals. | **False.** | It proves a supported merchant surface can host a native non-card Lightning method; it is Bitcoin and uses a separate constitution. |
| CN-16 | Apple Pay and stablecoins are the same tokenization technology. | **False.** | Apple Pay tokenizes a card credential; a stablecoin is a monetary/legal claim and ledger asset. The architectural rhyme is modular insertion behind a stable interface. |
| CN-17 | American Express, Discover, UnionPay and Adyen have no stablecoin work. | **Overclaim.** | No official public product was located in the targeted review; classify each `NR`, not absent. |
| CN-18 | Mastercard already owns BVNK. | **False at cutoff.** | The definitive agreement is signed; closing and acquired control remain future, conditional events. |

## Scale firewall

| Number | Object | Safe use | Unsafe use |
|---|---|---|---|
| Visa $5.2B | 2025 aggregate stablecoin-linked card volume | Company-reported portfolio adoption | Bridge-only volume or universal stablecoin checkout |
| Visa 0.04% | Stablecoin-linked volume share of Visa's $14.2T total global volume | Scale denominator | Evidence the product is irrelevant or permanent |
| Visa 130+ / 50+ | Programs / countries reported in March–April 2026 | Portfolio footprint | Active-card count or one uniform product |
| Visa 160+ | Programs “live or in development” by June 2026 | Pipeline plus live portfolio | 160 live programs |
| Visa $7B annualized | Overall stablecoin-settlement run rate | Institutional settlement signal | Total settled volume or nine-chain distribution |
| Phantom “thousands” | Cards issued within weeks after GA | Named program adoption | Stripe portfolio volume |
| Bridge “millions” | Potential users of wallet platforms | Addressable reach | Active cards or spend |

Primary:
[Visa linked-card metrics](https://www.visa.com/en-us/thought-leadership/innovation/stablecoin-linked-cards-monetize-money-movement);
[Visa–Bridge expansion](https://investor.visa.com/news/news-details/2026/Visa-and-Bridge-Expand-Collaboration-with-Plans-to-Bring-Stablecoin-Linked-Cards-to-Over-100-Countries/default.aspx);
[Visa nine-chain expansion](https://investor.visa.com/news/news-details/2026/Visa-Accelerates-Stablecoin-Momentum-Adding-Five-Blockchains-for-Settlement/);
[Phantom](https://stripe.com/en-dk/customers/phantom-spotlight).

## Product-line firewall

The following clocks must never be collapsed:

1. credential issuance;
2. customer-account funding;
3. transaction authorization;
4. network clearing;
5. issuer/acquirer settlement;
6. acquirer-to-merchant payout;
7. issuer redemption;
8. blockchain confirmation;
9. chargeback or refund resolution;
10. acquisition signing and closing.

The following legal objects must never be collapsed:

- card-account claim;
- credit receivable;
- bank deposit;
- stablecoin redemption claim;
- network settlement obligation;
- processor balance;
- merchant payout instruction;
- wallet custody relationship;
- blockchain transfer;
- refund or chargeback right.

## Promotion rule

A marketing page can establish that a product is being offered. It cannot by
itself establish:

- the exact contracting entity;
- the issuer or redemption obligor;
- a completed deployment;
- general availability;
- transaction volume;
- merchant activation;
- accounting or legal finality.

Promotion needs the product's own operative terms, a named participant or
merchant, an observed transaction/volume object, and a dated production state.
