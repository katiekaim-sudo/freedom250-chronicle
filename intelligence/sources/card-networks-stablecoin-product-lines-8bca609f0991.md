> Source created: 2026-07-29

# Card Networks Add Stablecoin Product Lines

> **Vault ruling:** this note extends [FINTECH_CRYPTO_INFRASTRUCTURE_DEEP_DIVE](../sources/fintech-crypto-infrastructure-deep-dive-08df4391c59f.html)
> and FINTECH_SWEEP_PAYMENT_ORCHESTRATORS. Read its correction ledger
> [Card Networks — Claim Audit](../sources/card-networks-claim-audit-033d2210abc5.html) before carrying a card/stablecoin claim into
> synthesis. Exact roles and money objects: [Card Networks — Entity and Flow Map](../sources/card-networks-entity-and-flow-map-d2b978d0ade2.html). Research-only sky layer: Card Networks — Money × Sky.

## Controlling ruling

The current transition is not accurately described as “credit cards moving onto
stablecoin rails.” The stronger, source-supported formulation is:

> Card networks, issuers, processors and acquirers are adding stablecoin-funded
> cards, stablecoin settlement, merchant stablecoin payout and wallet
> infrastructure as separate product lines. In the dominant card-linked paths,
> the customer still presents a network credential and the merchant still uses
> its existing acceptance contract. The stablecoin changes the funding,
> conversion, settlement or payout layer behind that interface.

This is the precise rhyme with the earlier transitions. A check could fund a
card account without the merchant accepting a check at checkout. Apple Pay
could replace the exposed card number with a device token without replacing the
issuer, acquirer, network or merchant rulebook. A stablecoin can now fund a card
or settle a network obligation without becoming the merchant-facing payment
method.

## 2026-07-31 transparency extension

[2026-07-31 - The Visible Ledger and the Hidden Constitution — From Cash to Stablecoins](../sources/2026-07-31-the-visible-ledger-and-the-hidden-constitution-from-ca-3eb1a2bcb2e6.html)
adds an audience-specific transparency test. Cards and Apple Pay make
transactions highly legible to issuers, networks, processors and regulators
without making them public. Public-chain stablecoins invert part of that
design: address-level transfers and contract state can be publicly inspected,
while beneficial ownership, reserves, direct-redemption eligibility, exchange
inventory, full conversion cost and legal remedy remain partly or wholly
off-chain.

The product-line grammar below must therefore retain two additional
questions: **who can inspect the transfer record, and who can inspect the
monetary claim behind it?**

The field also contains real alternatives to this adapter model. Coinbase and
PayPal now offer native online wallet payment methods, while Square Bitcoin
provides a live non-card point-of-sale path. Those are different products with
different contracts, finality and dispute rules; they should not be counted as
card-network stablecoin adoption.

## What changed after the 2026-07-28 package

The July 28 package remains structurally sound. This supplement makes four
material additions or repairs:

1. **Stripe/Bridge card maturity moved upward.** The July 28 memo used Deel as
   the principal example and described the complete card path as future.
   Stripe's 2026 product disclosures now support stablecoin-backed consumer and
   commercial cards in 30 countries, and the Phantom Card supplies a named
   production example. This does not mean every announced country, chain or
   issuer is live under one program.
2. **JCB entered the map.** JCB disclosed both a USDC internal-fund-transfer
   proof of concept and a separate physical-store stablecoin experiment in
   Japan. Both remain exploration or PoC objects, not production acceptance.
3. **Mastercard needs asset-specific and product-specific clocks.** USDC has
   early on-chain settlement flows in select markets; the other announced
   stablecoins, chains and institutions cannot be flattened into one live
   matrix. Card funding, network settlement, acquirer receipt, merchant payout,
   wallet payout and Multi-Token Network activity remain distinct.
4. **The native counterexample is now visible.** Square Bitcoin is a live
   non-card checkout product on Square POS. It demonstrates that the terminal
   can carry a new rail, but only when the payment application, merchant terms,
   finality and refund model also change.

## Product-line grammar

| Code | Product line | Stablecoin's role | Merchant-facing event |
|---|---|---|---|
| **T1** | Stablecoin-funded card | Customer balance or collateral behind a Visa or Mastercard credential | Ordinary card authorization and card-network settlement unless the program separately uses stablecoin settlement |
| **T2** | Processor-converted wallet checkout | Customer tenders a stablecoin; the PSP converts or orchestrates it | New wallet payment method under PSP terms; merchant may receive fiat |
| **T3** | Direct wallet-to-merchant rail | Native asset moves through a non-card network | New merchant payment application, finality and refund/dispute constitution |
| **T4** | Card-network stablecoin settlement | Issuer or acquirer uses a stablecoin to settle network obligations | Customer and merchant checkout can remain unchanged |
| **T5** | Merchant or payee stablecoin payout | Processor/acquirer converts an ordinary settlement or funded payout into a stablecoin | Merchant or payee elects a different receipt asset; customer tender is not implied |
| **T6** | Stablecoin platform and treasury tooling | Mint, burn, custody, wallet, prefunding or cross-border movement | Infrastructure capability; no merchant acceptance follows automatically |

Architecture path and evidence maturity are separate fields. **Production,
limited production, pilot, rollout, beta, signed agreement, planned and
marketing** are not synonyms.

## Card-network product families

### Visa

| Product line | Exact path | Evidence state at cutoff | Boundary |
|---|---|---|---|
| Stablecoin-linked cards (**T1**) | Stablecoin balance → program manager/issuer conversion or reservation → Visa credential → ordinary Visa merchant transaction | Production portfolio; Visa reports more than 130 programs across more than 50 countries | Merchant acceptance is Visa acceptance, not direct stablecoin acceptance |
| Principal-member stablecoin settlement (**T1 + T4**) | Stablecoin-funded card transaction → participating principal member settles an enabled obligation to Visa in USDC → downstream merchant payout remains under existing acquiring flow | Emerging/limited | The card program and the network-settlement election are two separate contractual objects |
| U.S. issuer/acquirer USDC settlement (**T4**) | Participating issuer or acquirer settles VisaNet obligations in USDC | Limited production beginning with Cross River Bank and Lead Bank over Solana; broader 2026 availability planned | Not universal Visa settlement; not a new consumer tender |
| Visa Direct stablecoin prefunding (**T6**) | Originator funds its Visa Direct payout inventory with stablecoin; downstream recipient receives local fiat | Pilot; named partners, token, chain and geography remain undisclosed | Stablecoin-in/fiat-out treasury funding is not card checkout |
| Visa Direct stablecoin wallet payout (**T5/T6**) | U.S. originator funds in fiat; Visa Direct routes or converts the payout to a compatible stablecoin wallet | Pilot; broader rollout was planned for the second half of 2026 | Fiat-in/stablecoin-out is the reverse flow and remains separate from merchant acquiring |
| Visa Stablecoin Platform / Open USD (**T6**) | Wallet-as-a-Service, mint/burn and stablecoin-management functions linked to Visa products | Select-client beta disclosed 2026-07-16 | Platform availability does not prove an issuer launch, merchant acceptance or production volume |

Visa's company-reported metrics must retain their measurement dates and
denominators. Its March 2026 stablecoin-linked-card review reported about
$5.2 billion of 2025 card volume—319% year over year, but only 0.04% of Visa's
$14.2 trillion total global volume. An earlier annual-report snapshot reported
different card and settlement figures on a different clock. These are adoption
signals, not proof that card money has migrated wholesale.

The global settlement pilot lists Avalanche, Ethereum, Solana, Stellar, Arc,
Base, Canton, Polygon and Tempo. Visa does not publish a token-by-chain or
participant-by-chain volume matrix. Visa's separate Tokenized Asset Platform and
its Brale/Canton proof of concept concern bank-issued tokens and institutional
settlement architecture; neither establishes checkout acceptance.

Primary sources:

- [Visa stablecoin product family](https://www.visa.com/en-us/solutions/stablecoins)
- [Visa stablecoin-linked card architecture and 2025 metrics](https://www.visa.com/en-us/thought-leadership/innovation/stablecoin-linked-cards-monetize-money-movement)
- [Visa–Bridge card expansion](https://investor.visa.com/news/news-details/2026/Visa-and-Bridge-Expand-Collaboration-with-Plans-to-Bring-Stablecoin-Linked-Cards-to-Over-100-Countries/default.aspx)
- [Visa U.S. issuer/acquirer USDC settlement](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-launches-stablecoin-settlement-in-the-united-states.html)
- [Visa nine-chain settlement-pilot expansion](https://investor.visa.com/news/news-details/2026/Visa-Accelerates-Stablecoin-Momentum-Adding-Five-Blockchains-for-Settlement/)
- [Visa Direct stablecoin prefunding](https://investor.visa.com/news/news-details/2025/Visa-Direct-Taps-Stablecoins-to-Unlock-Faster-Funding-for-Businesses/default.aspx)
- [Visa Direct stablecoin wallet payout](https://investor.visa.com/news/news-details/2025/Visa-Direct-Stablecoin-Payouts-Pilot-Speeds-Up-Access-to-Funds-for-Creators--Gig-Workers/default.aspx)
- [Visa annual-report CEO message](https://annualreport.visa.com/chairman-and-ceo-message/default.aspx)
- [Visa Stablecoin Platform](https://investor.visa.com/news/news-details/2026/Visa-Introduces-Platform-for-Stablecoin-Minting-Movement-and-Management/)
- [Visa Tokenized Asset Platform](https://investor.visa.com/news/news-details/2024/Visa-Introduces-the-Visa-Tokenized-Asset-Platform/default.aspx)
- [Visa–Brale Canton proof of concept](https://investor.visa.com/news/news-details/2026/Visa-and-Brale-Explore-Private-Stablecoin-Settlement-for-Institutional-Payments/default.aspx)

### Mastercard

| Product line | Exact path | Evidence state at cutoff | Boundary |
|---|---|---|---|
| Wallet-linked Mastercard programs (**T1**) | Crypto/stablecoin wallet → program issuer/manager → Mastercard credential → ordinary merchant card flow | Mixed by program; portfolio includes named production and rollout relationships | MetaMask, Kraken, Gemini, Bybit, Crypto.com, Binance, Monavate and Bleap cannot be assigned one common launch state |
| MoonAgents Card (**T1**) | Self-custody wallet → Monavate on-chain funding and real-time authorization → virtual Mastercard debit credential → online merchant | Limited production disclosed 2026-05-01 for an agent/CLI use case in the UK and Latin America | No proof of NFC, Apple Pay, broad consumer availability or transaction volume |
| Global network settlement (**T4**) | Enabled issuer or acquirer settles Mastercard obligations using an enabled stablecoin | USDC supports early on-chain flows in select markets; broader asset and participant set is rollout/expected | The release lists assets and chains but does not provide a pairwise asset-by-chain matrix |
| Circle EEMEA acquirer settlement (**T4**) | Mastercard settles participating acquirer in USDC or EURC; acquirer separately settles merchants | Limited regional production/rollout with Arab Financial Services and Eazy Financial Services named first | Acquirer receipt is not proof every downstream merchant elects stablecoin |
| Merchant settlement capability (**T5**) | Nuvei/acquirer infrastructure converts merchant settlement to USDC or an enabled Paxos-family asset | Partnership/capability; availability varies | Customer stablecoin tender is not implied; all assets are not proven live |
| Mastercard Move/Thunes wallet payout (**T5**) | Cross-border payout endpoint delivers value to a recipient stablecoin wallet | Integration/rollout language | Separate money-movement product, not card-network settlement |
| Multi-Token Network (**T6**) | Governed institutional platform connects bank money, tokenized assets and ledger environments | Operational platform with specific integrations and pilots | MTN evidence does not establish retail card settlement |
| BVNK acquisition | Mastercard would acquire on-chain/fiat orchestration capabilities | Definitive agreement signed; not closed at cutoff | No acquired control should be attributed until closing |

The June 2026 settlement release needs three different clocks:

- **USDC:** early live on-chain settlement flows in select markets.
- **PYUSD, USDG, USDP, RLUSD and SoFiUSD:** announced support or rollout.
- **ARQ/DolarApp, CBW Bank, Cross River Bank, Lead Bank and Nuvei:** expected
  early participants, not one proven live cohort.

The legal issuers of Paxos-associated assets also differ. “Paxos asset” is an
infrastructure-family label, not proof that Paxos Trust Company is the obligor
for every coin.

Primary sources:

- [Mastercard end-to-end stablecoin capabilities](https://www.mastercard.com/news/press/2025/april/mastercard-unveils-end-to-end-capabilities-to-power-stablecoin-transactions-from-wallets-to-checkouts)
- [Mastercard global stablecoin settlement expansion](https://www.mastercard.com/global/en/news-and-trends/press/2026/june/mastercard-expands-settlement-capabilities-to-include-stablecoin.html)
- [Mastercard–Circle EEMEA acquirer settlement](https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2025-1/august/mastercard-expands-partnership-with-circle-to-transform-digital-settlement-for-merchants-and-acquirers-in-region)
- [MoonPay MoonAgents Card](https://www.moonpay.com/ro/newsroom/moonagents-card)
- [Mastercard Move–Thunes](https://www.mastercard.com/news/ap/en/newsroom/press-releases/en/2025/mastercard-and-thunes-bring-stablecoin-payouts-to-the-mainstream/)
- [Mastercard–BVNK agreement](https://www.mastercard.com/global/en/news-and-trends/press/2026/march/Mastercard-to-acquire-BVNK-to-connect-on-chain-payments-and-fiat-rails.html)
- [Mastercard Q1 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1141391/000114139126000031/ma-20260331.htm)

### JCB

JCB supplies the clearest new **watch** lane, not a production claim:

- On 2026-07-14, **JCB Co., Ltd.** and an unnamed affiliate of Circle Internet
  Group signed an MOU. The initial PoC concerns JCB's internal cross-border fund
  transfers using USDC. A second exploration lane concerns in-store stablecoin
  payment experiences in Japan and multi-chain interoperability.
- JCB's separate work with Digital Garage and Resona announced a physical-store
  PoC involving dollar- and yen-denominated stablecoins, merchant settlement
  into yen and operational testing.

This does not prove that ordinary JCB Contactless terminals, Apple Pay or the
JCB merchant rulebook already accept a native stablecoin. The named payment
application, conversion provider, merchant contract, refund process and final
production route remain program-specific research objects.

Primary sources:

- [JCB–Circle MOU](https://www.global.jcb/en/press/2026/202607141000_products.html)
- [JCB–Digital Garage–Resona collaboration](https://www.global.jcb/ja/press/2026/202601161100_others.pdf)
- [JCB physical-store PoC announcement](https://www.global.jcb/ja/press/2026/202602191600_others.pdf)

### American Express, Discover, UnionPay and Adyen

A targeted primary-source review through the cutoff did not locate an official
stablecoin-funded credential, native stablecoin merchant product, merchant
stablecoin payout or network stablecoin-settlement program for:

- **American Express**
- **Capital One / Discover Global Network**
- **UnionPay International**
- **Adyen N.V.**

These rows are **NR — not located in the reviewed public sources**, not proof
that no private development, partner pilot or future product exists.

Capital One's completed acquisition of Discover and planned migration of some
Capital One volume onto the Discover network remain important card-network
verticalization evidence. They are not stablecoin evidence.

Adyen's current product catalogue and settlement documentation continue to
describe cards, wallets, bank methods and fiat payouts. That is a useful
processor/acquirer control case, but it does not establish stablecoin
acceptance, merchant payout or on-chain settlement.

Control sources:

- [American Express contactless merchant acceptance](https://www.americanexpress.com/uk/merchant/contactless-payments.html)
- [Capital One completion of Discover acquisition](https://www.capitalone.com/about/newsroom/capital-one-completes-acquisition-of-discover/)
- [UnionPay Pay+ wallet ecosystem](https://www.unionpayintl.com/en/mediaCenter/newsCenter/companyNews/6524.shtml)
- [Adyen payment-method catalogue](https://docs.adyen.com/payment-methods)
- [Adyen settlement flow](https://docs.adyen.com/platforms/settle-funds)

## Processor, acquirer and wallet additions

### Stripe / Bridge: production card evidence

Stripe now describes stablecoin-backed consumer and commercial cards across 30
countries, with further availability staged on separate 2026 clocks. The
Phantom Card provides a named production example:

```text
Phantom CASH stablecoin balance
→ Bridge stablecoin infrastructure
→ Stripe Issuing
→ card credential
→ ordinary card merchant
```

Phantom reported a spring 2026 general-availability rollout and thousands of
cards issued within weeks. This corrects the broad July 28 statement that the
“full card path is not yet live.” The narrower Deel statement remains valid:
Deel's wallet and Deel Card had their own rollout clocks.

Stripe's native stablecoin acceptance is a separate **T2** online/web-mobile
payment method. Its regional Stripe entity and settlement providers control
custody, conversion and fiat payout under the operative terms. Current Stripe
Terminal documentation does not establish a physical stablecoin payment method.

Primary sources:

- [Stripe Sessions 2026 product map](https://stripe.com/blog/everything-we-announced-at-sessions-2026)
- [Phantom Card case study](https://stripe.com/en-dk/customers/phantom-spotlight)
- [Stripe stablecoin payment terms](https://stripe.com/legal/stablecoin-payments)
- [Stripe stablecoin acceptance documentation](https://docs.stripe.com/payments/accept-stablecoin-payments)
- [Stripe Terminal documentation](https://docs.stripe.com/terminal)

### PayPal: two operative non-card lanes

PayPal's current legal terms show two distinct products:

1. **Pay with Crypto / T2:** a buyer's crypto is accessed or converted through
   Mesh and PYUSD; PayPal converts the value to fiat for the merchant. The
   merchant does not receive stablecoin and the transaction is not ordinary
   card settlement.
2. **Hyperwallet PYUSD payout / T5:** merchant-funded fiat is converted to PYUSD
   and sent to an eligible Solana wallet. This is a payee-disbursement product,
   not proof of customer stablecoin tender.

Primary sources:

- [PayPal Pay with Crypto terms](https://www.paypal.com/us/legalhub/paypal/crypto-payment-method?locale.x=en_US)
- [Hyperwallet PYUSD payout terms](https://www.paypal.com/us/legalhub/paypal/hyperwallet-pyusd-payouts-tnc?country.x=US&locale.x=en_US)

### Coinbase and Checkout.com: native online acceptance versus payout

Coinbase Payment Acceptance offers authorization, capture, void and refund-like
merchant primitives for USDC. Checkout.com separately disclosed:

- Coinbase-powered customer stablecoin acceptance with merchant settlement in
  USD (**T2**); and
- Fireblocks-powered merchant settlement to a USDC or USDT wallet (**T5**).

The two Checkout.com products cannot be merged into “merchant accepts
stablecoin and receives stablecoin.” Customer tender and merchant receipt are
independent elections. Coinbase's newer multi-chain API documentation also
needs an exact contract-and-entity match before its full architecture is treated
as legally complete.

Primary sources:

- [Coinbase Payment Acceptance](https://docs.cdp.coinbase.com/payments/payment-acceptance/overview)
- [Checkout.com–Coinbase acceptance](https://www.checkout.com/newsroom/checkout-com-enables-stablecoin-acceptance-for-merchants-in-partnership-with-coinbase)
- [Checkout.com–Fireblocks merchant settlement](https://www.checkout.com/newsroom/checkout-com-scales-stablecoin-settlement-for-us-merchants-in-partnership-with-fireblocks)

### Worldpay and Fiserv

- **Worldpay:** direct merchant USDC settlement is an established product lane.
  Its separately announced BVNK third-party payout pilot was not verified as
  production through the cutoff.
- **Fiserv:** FIUSD remains a deployment watch. Public materials describe
  settlement, cash management, cross-border, merchant conversion and loyalty,
  but do not yet supply an operative issuer/redemption constitution, contract
  address, named production transaction or proof that Clover exposes FIUSD as a
  payment method. Fiserv's INDX real-dollar settlement product is a separate,
  off-chain cash-settlement object.

Primary sources:

- [Worldpay current USDC settlement description](https://worldpay.com/en-GB/insights/articles/usdc-stablecoin-circle)
- [Worldpay–BVNK payout announcement](https://corporate.worldpay.com/news-releases/news-release-details/worldpay-enable-stablecoin-payouts-global-businesses)
- [Fiserv FIUSD announcement](https://investors.fiserv.com/news-releases/news-release-details/fiserv-launches-new-fiusd-stablecoin-financial-institutions)
- [Fiserv INDX announcement](https://investors.fiserv.com/news-releases/news-release-details/fiserv-introduces-indx-real-time-cash-settlement-platform)

## Native point-of-sale counterexample: Square Bitcoin

Square Bitcoin is the strongest live falsifier of a card-only terminal thesis.
Eligible U.S. Square sellers can accept Bitcoin over Lightning:

```text
buyer Lightning wallet
→ QR code, or NFC phone tap on supported second-generation Square Register
→ Lightning transfer
→ merchant elects BTC in a Square wallet or immediate USD conversion
```

This is **T3**, not a stablecoin and not card-network settlement. Its differences
from a card transaction are constitutionally important:

- device and geographic eligibility are narrower;
- transaction and daily caps apply;
- the payment has no card chargeback process;
- refunds follow Square's specified alternative process;
- merchant receipt can be BTC or immediate USD.

The hardware can look familiar while the payment system underneath is genuinely
different. That is the correct test for the next transition: not whether the
same terminal can display a new option, but whether authorization, routing,
merchant contract, finality and remedy have moved together.

Primary sources:

- [Square Bitcoin terms](https://squareup.com/us/en/legal/general/square-bitcoin-alpha-terms)
- [Square Bitcoin device and payment rules](https://squareup.com/help/us/en/article/8622-accept-and-manage-bitcoin-payments)

## The Apple Pay parallel, stated precisely

Apple Pay changed the **credential-presentment and security layer**:

```text
plastic PAN exposure
→ device token + cryptogram
→ existing issuer authorization
→ existing network routing
→ existing acquirer and merchant contract
```

The dominant stablecoin card transition changes the **funding and settlement
options**:

```text
bank deposit or credit balance only
→ optional stablecoin-funded account and/or stablecoin settlement asset
→ existing credential
→ existing network routing
→ existing merchant acceptance
```

The parallel is therefore not “Apple Pay put cards on a new rail, and now
stablecoins will do the same.” It is:

> Apple Pay proved that a mass-market payment interface can remain familiar
> while a new tokenization and control layer is inserted behind it. Stablecoin
> products are extending that modularity into funding, treasury, network
> settlement and payout.

## Constitutional test: product line or new rail?

Treat a product as an **added card-rail line** when most of these remain under
the incumbent card constitution:

- credential and acceptance mark;
- issuer authorization;
- network routing and clearing;
- acquirer/merchant contract;
- fraud allocation and chargebacks;
- interchange and network pricing;
- merchant settlement obligation.

Treat it as a **native alternative rail** only when the new system materially
controls several of these:

- the customer payment instruction;
- authorization or validity rules;
- transaction routing;
- merchant onboarding and acceptance terms;
- finality;
- refunds, disputes and fraud loss;
- the settlement asset and recipient claim;
- transaction pricing.

By that test, today's field is mixed:

- **Visa/Mastercard/Stripe stablecoin-backed cards:** added product lines inside
  card rails.
- **Visa/Mastercard stablecoin network settlement:** new settlement option
  inside card rails.
- **PayPal/Coinbase/Checkout.com wallet acceptance:** native online payment
  method mediated by a PSP.
- **Worldpay/Checkout.com/Hyperwallet stablecoin payout:** treasury or
  disbursement choice after, or separate from, acceptance.
- **Square Bitcoin:** native alternative POS rail.
- **JCB:** controlled exploration whose final constitutional placement is not
  yet proven.

## Watchboard

Promote or reclassify only on exact evidence:

| Trigger | What it would prove | What it would not prove |
|---|---|---|
| Named issuer launches a stablecoin-funded card with operative terms and volume | T1 production for that program | Direct merchant stablecoin acceptance |
| Named issuer/acquirer settles a disclosed network obligation in a disclosed asset | T4 production for that participant/asset/network | Universal network settlement |
| Acquirer terms let merchant elect stablecoin receipt | T5 contractual availability | Customer stablecoin tender |
| Terminal documentation lists a native wallet/stablecoin method | In-person application support | General merchant activation or legal finality |
| Operative merchant rules replace card chargebacks with on-chain finality/remedies | Movement toward a native rail constitution | Mass adoption |
| BVNK acquisition closes | Mastercard obtains corporate control of the acquired entity | Immediate integration into every Mastercard product |
| FIUSD publishes issuer, redemption, reserve, contract and live participant evidence | FIUSD legal/technical production state | Automatic Clover enablement |
| JCB names production merchants and operative payment/settlement terms | JCB production path | Automatic JCB Contactless or Apple Pay interoperability |

## Research conclusion

The credit-card companies are not abandoning the card. They are attempting to
make the card network the compatibility layer across more kinds of money:

- bank deposits and credit remain customer funding sources;
- stablecoin balances become an additional funding source;
- regulated stablecoins become optional issuer/acquirer settlement assets;
- processors offer merchant stablecoin receipt after ordinary acceptance;
- network companies add wallet, mint/burn and cross-border orchestration tools.

That is economically important precisely because it is incremental. The
merchant does not need to wait for a wholly new installed base. The incumbent
networks can sell a new product line while preserving the credential,
acceptance footprint, risk controls and dispute machinery that make their
networks valuable.

The genuine competitive threat appears where a provider reproduces enough of
that merchant constitution outside the card network. Square Bitcoin is a live,
bounded example. Coinbase, PayPal and Checkout.com show the online version.
That is the seam to watch: whether stablecoins remain an asset carried by the
card-and-processor stack, or whether native payment applications become a
complete merchant operating system of their own.
