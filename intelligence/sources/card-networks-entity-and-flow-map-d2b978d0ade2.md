> Source created: 2026-07-29

# Card-Network Stablecoin Entity and Flow Map

> Companion to Card Networks — Stablecoin Product Lines. Use this note to
> keep customer tender, credential, issuer, processor, network obligation,
> settlement asset and merchant/recipient receipt from collapsing into one
> event. Corrections: Card Networks — Claim Audit.

## Reading rule

Company, network, money object and payment event must remain separate. A release
that names Visa, Circle and a bank does not make all three the issuer, acquirer
or merchant counterparty. The minimum usable record is:

```text
customer tender / credential
→ wallet or account controller
→ program issuer / processor
→ network authorization and clearing
→ settlement asset and obligor
→ acquirer / payout provider
→ merchant or recipient claim
```

## Card-funded and card-settlement flows

| Product | Named controllers | Customer presents | Stablecoin object | Network obligation | Merchant/recipient receives | Status |
|---|---|---|---|---|---|---|
| Visa–Bridge card | Visa; Bridge; Lead Bank; program-specific wallet/provider | Visa credential funded by stablecoin balance | Program-specific balance and conversion asset | Ordinary Visa obligation unless participant separately uses the settlement pilot | Ordinary local-currency card settlement | Production/expanding |
| Phantom Card | Phantom; Bridge; Stripe Issuing; program bank/network entities | Card credential against Phantom CASH balance | CASH; exact program constitution controls | Ordinary card-network obligation | Ordinary card settlement | Production |
| Mastercard wallet-card portfolio | Mastercard plus program-specific wallet, issuer and manager | Mastercard credential backed by crypto/stablecoin wallet | Program-specific asset | Ordinary Mastercard obligation | Ordinary card settlement | Mixed |
| MoonAgents Card | MoonPay; Monavate; Mastercard | Virtual Mastercard debit credential; self-custody wallet funding | On-chain funding asset under program rules | Mastercard card obligation | Ordinary online-card settlement | Limited production |
| VisaNet USDC settlement | Visa; Circle; Cross River Bank; Lead Bank; other enabled participants | Any ordinary Visa credential | USDC; U.S. initial path uses Solana | Enabled issuer/acquirer settles VisaNet obligation in USDC | Merchant ordinarily receives under acquiring contract | Pilot/limited |
| Visa acquirer USDC settlement | Visa; Circle; Worldpay; Nuvei | Ordinary Visa card transaction | USDC transferred from Visa treasury/Circle account | Visa settles a participating acquirer in USDC | Acquirer may route USDC to electing merchant | Live pilots |
| Mastercard global settlement | Mastercard; enabled issuer/acquirer; coin issuer/infrastructure provider | Any ordinary Mastercard credential | USDC early; PYUSD, USDG, USDP, RLUSD and SoFiUSD on rollout clocks | Enabled participant settles Mastercard obligation in supported asset | Merchant receipt remains a separate acquirer election | Mixed |
| Mastercard–Circle EEMEA | Mastercard; Circle; Arab Financial Services; Eazy Financial Services | Ordinary Mastercard transaction | USDC or EURC | Mastercard settles participating acquirer | Downstream merchant payout remains separately governed | Limited regional |

Primary:
[Visa–Bridge expansion](https://investor.visa.com/news/news-details/2026/Visa-and-Bridge-Expand-Collaboration-with-Plans-to-Bring-Stablecoin-Linked-Cards-to-Over-100-Countries/default.aspx);
[Phantom](https://stripe.com/en-dk/customers/phantom-spotlight);
[Mastercard end-to-end](https://www.mastercard.com/news/press/2025/april/mastercard-unveils-end-to-end-capabilities-to-power-stablecoin-transactions-from-wallets-to-checkouts);
[MoonAgents](https://www.moonpay.com/ro/newsroom/moonagents-card);
[Visa U.S. settlement](https://investor.visa.com/news/news-details/2025/Visa-Launches-Stablecoin-Settlement-in-the-United-States-Marking-a-Breakthrough-for-Stablecoin-Integration/default.aspx);
[Visa acquirer settlement](https://investor.visa.com/news/news-details/2023/Visa-Expands-Stablecoin-Settlement-Capabilities-to-Merchant-Acquirers/);
[Mastercard settlement](https://www.mastercard.com/global/en/news-and-trends/press/2026/june/mastercard-expands-settlement-capabilities-to-include-stablecoin.html);
[Mastercard–Circle EEMEA](https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2025-1/august/mastercard-expands-partnership-with-circle-to-transform-digital-settlement-for-merchants-and-acquirers-in-region).

## Wallet acceptance and payout flows

| Product | Contract/control surface | Customer tender | Conversion/custody | Merchant or payee claim | Path |
|---|---|---|---|---|---|
| Stripe stablecoin payments | Regional Stripe contracting entity; Paxos/Bridge provider layer | Supported stablecoin through web/mobile wallet | Provider account receives/custodies/converts; regional Stripe entity pays out | Fiat Stripe balance unless product/region permits otherwise | T2 |
| PayPal Pay with Crypto | PayPal, Inc.; PayPal Digital where applicable; Mesh; Paxos/PYUSD | Supported crypto from buyer wallet | Mesh converts/transfers through PYUSD; PayPal converts to fiat | Merchant fiat claim; Seller Protection excluded under current terms | T2 |
| Coinbase Payment Acceptance | Coinbase entity and API terms; exact newer enterprise contract remains a request | USDC through supported wallet/chain | Coinbase payment infrastructure; USD route needs custodial/fiat layer | USDC or USD according to product configuration | T2 |
| Checkout.com–Coinbase | Country-specific Checkout.com contracting entity; Coinbase integration | Customer USDC/USDT | Coinbase-powered acceptance; Checkout.com processing | Merchant continues to settle in USD | T2 |
| Checkout.com–Fireblocks | Checkout.com; Fireblocks; eligible merchant | Customer tender not implied | Processor converts/routes eligible merchant settlement | Merchant USDC/USDT wallet receipt | T5 |
| Worldpay USDC settlement | Worldpay contracting entity; Circle infrastructure | Customer may pay in ordinary currency | Worldpay converts/routes settlement | Electing merchant receives USDC | T5 |
| Hyperwallet PYUSD payout | PayPal Digital, Inc.; PayPal/Hyperwallet services; Paxos issuer layer | Merchant funds payout in fiat | Fiat converted to PYUSD and sent on Solana | Eligible payee wallet receives PYUSD | T5 |
| Visa Direct prefunding | Visa; unnamed select originators/partners | No checkout credential | Originator prefunds payout inventory with stablecoin | Recipient receives local fiat | T6 |
| Visa Direct wallet payout | Visa; unnamed select U.S. originators/partners | No checkout credential; originator funds fiat | Visa Direct converts/routes to supported stablecoin | Recipient wallet receives stablecoin | T5/T6 |

Primary:
[Stripe terms](https://stripe.com/legal/stablecoin-payments);
[PayPal Pay with Crypto terms](https://www.paypal.com/us/legalhub/paypal/crypto-payment-method?locale.x=en_US);
[Coinbase acceptance](https://docs.cdp.coinbase.com/payments/payment-acceptance/overview);
[Checkout.com–Coinbase](https://www.checkout.com/newsroom/checkout-com-enables-stablecoin-acceptance-for-merchants-in-partnership-with-coinbase);
[Checkout.com–Fireblocks](https://www.checkout.com/newsroom/checkout-com-scales-stablecoin-settlement-for-us-merchants-in-partnership-with-fireblocks);
[Worldpay USDC](https://worldpay.com/en-GB/insights/articles/usdc-stablecoin-circle);
[Hyperwallet PYUSD terms](https://www.paypal.com/us/legalhub/paypal/hyperwallet-pyusd-payouts-tnc?country.x=US&locale.x=en_US);
[Visa Direct prefunding](https://investor.visa.com/news/news-details/2025/Visa-Direct-Taps-Stablecoins-to-Unlock-Faster-Funding-for-Businesses/default.aspx);
[Visa Direct payout](https://investor.visa.com/news/news-details/2025/Visa-Direct-Stablecoin-Payouts-Pilot-Speeds-Up-Access-to-Funds-for-Creators--Gig-Workers/default.aspx).

## Native checkout and platform flows

| Product | Exact system | Finality/remedy constitution | Status | Boundary |
|---|---|---|---|---|
| Square Bitcoin | Lightning wallet → QR or supported Register NFC → Square Bitcoin → BTC or immediate USD election | No card chargeback; Square-specific caps and refund process | Production, eligible U.S. sellers | Bitcoin, not stablecoin |
| JCB store PoC | Program wallet/application → stablecoin transfer/conversion → merchant yen settlement | PoC terms and production remedies undisclosed | PoC | No automatic JCB Contactless/Apple Pay claim |
| MoonPay/WalletConnect/Ingenico | WalletConnect payment through enabled Ingenico checkout implementation | Non-card wallet flow; operative merchant/remedy details are product-specific | Rollout | Explicitly distinct from Mastercard card path |
| Visa Stablecoin Platform | Institutional wallet, bank-account link, Open USD mint/redeem/hold/transfer | Visa control plane plus still-undisclosed exact OUSD issuer/reserve constitution | Select-client beta | No merchant acceptance |
| Mastercard MTN | Governed B2B/tokenized-asset network connecting institutional platforms | Product/integration-specific bank and token finality | Operational platform with pilots/integrations | No retail-card settlement inference |
| FIUSD | Proposed Fiserv stablecoin and white-label infrastructure | Exact issuer, redemption, reserve, custody and contract remain unresolved | Launch/deployment watch | No automatic Clover method |

Primary:
[Square terms](https://squareup.com/us/en/legal/general/square-bitcoin-alpha-terms);
[JCB–Circle](https://www.global.jcb/en/press/2026/202607141000_products.html);
[MoonPay/WalletConnect/Ingenico](https://www.moonpay.com/fr/newsroom/moonpay-iron-walletconnect);
[Visa Stablecoin Platform](https://investor.visa.com/news/news-details/2026/Visa-Introduces-Platform-for-Stablecoin-Minting-Movement-and-Management/default.aspx);
[Mastercard MTN–Kinexys](https://www.mastercard.com/gb/en/news-and-trends/press/2024/november/mastercards-mtn-connects-to-jp-morgans-kinexys-digital-payments-for-settlement.html);
[Fiserv FIUSD](https://investors.fiserv.com/news-releases/news-release-details/fiserv-launches-new-fiusd-stablecoin-financial-institutions).

## Legal-entity gaps that control promotion

1. Exact Bridge program issuer, custodian and conversion counterparty by country.
2. Exact card-network subsidiary and participating-bank contract governing each
   stablecoin settlement route.
3. Open USD issuer, redemption obligor, reserve owner and custodian.
4. FIUSD issuer, redemption obligor, reserve constitution, contract address and
   first named production institution.
5. Current Coinbase enterprise Acceptance API contracting and custody entity.
6. Checkout.com product-specific contracting entity by merchant country.
7. JCB's named Circle affiliate and operative store-PoC payment terms.

Until those edges are disclosed, brand-level architecture may be charted but
should not be promoted into a complete legal constitution.
