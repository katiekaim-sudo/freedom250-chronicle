> Source cutoff: 2026-09-30T19:11:32-04:00

# Open USD (OUSD) × Mastercard × Open Standard — Launch and Control Map

## Question

What did the September 30 Open USD launch establish, what is Mastercard's
actual role, and did “Open Standard” create an open or permissionless money
system?

## Scope and exclusions

This is a launch-day return to the July 29 card-network stablecoin package. It
tests issuer, reserve, redemption, governance, chain, distribution and
Mastercard-integration claims through **September 30, 2026 at 7:11 p.m. EDT**.
It does not treat minted supply as transaction volume, launch liquidity as
third-party adoption, a partner name as completed integration, or a public
blockchain transfer as final bank-money settlement.

## Short answer

**OUSD is live, and Mastercard's role is materially deeper than a logo on a
partner list.** Mastercard is one of Open Standard's five initial founding
partners, is investing in the company, is helping establish OUSD supply, and
advertises a Mastercard API-or-portal route for OUSD minting, redemption,
conversion, wallets and settlement. Mastercard also completed its acquisition
of stablecoin-orchestrator BVNK on August 3.

But the roles remain split:

- **Bridge Building Inc., a Stripe company, is the issuer and redemption
  obligor.**
- **Open Standard LLC is the company organizing partner economics and future
  shareholder governance.**
- **Mastercard is a founding partner/investor and integration/distribution
  route, not the issuer or reserve owner; the exact equity terms are not
  public.**
- **BlackRock, Lead Bank and BNY are named reserve institutions, but their
  exact account, custody, fund and liability roles are not itemized publicly.**
- **Base, Ethereum, Solana and Tempo carry the token state; none turns a
  Mastercard card authorization, clearing obligation or final bank payment
  automatically into an OUSD transfer.**

The important new model is therefore not “card networks displaced by an open
coin.” It is **incumbent distributors sharing reserve economics and corporate
governance around a Bridge-issued stablecoin while keeping institutional
control of minting, redemption, freezing, burning, wallets, access and
customer routes.**

## What changed on September 30

| Object | Launch-day state | What it proves | What it does not prove |
|---|---|---|---|
| OUSD | Live with exact native contract addresses on four chains | The token exists and material supply has been minted | Broad holder distribution, payment volume, recurring use or stress performance |
| Bridge Building Inc. | Named issuer | Exact legal issuer and direct eligible-user redemption obligor are now public | A federal payment-stablecoin approval, bank charter or deposit insurance |
| Reserve dashboard | Live; issuer-reported supply and assets matched at the cutoff | A public current reserve composition and supply control surface exists | Independent assurance; the first monthly attestation had not yet been published |
| Open Standard | Operating company with five named initial founders and 200+ signed-up partners | Corporate incentive/governance layer is real | A published charter, board roster, voting agreement or partner-by-partner ownership table |
| Mastercard | Founder/investor plus public OUSD product route | Mastercard has moved from general support to an explicit access and distribution role | A named Mastercard client, public API documentation, settled volume or migration of ordinary card settlement to OUSD |
| BVNK | Mastercard acquisition completed August 3 | Mastercard now owns a stablecoin-native send/receive/store/convert orchestration stack | That every OUSD flow uses BVNK or that BVNK is the issuer |

## Exact actor and control map

| Layer | Actor/object | Publicly evidenced control |
|---|---|---|
| Token issuer | **Bridge Building Inc.** | Issues OUSD; promises eligible users one-dollar redemption under Bridge Stablecoin Terms; maintains the reserve; may suspend support, freeze addresses and burn tokens |
| Parent/infrastructure | **Stripe / Bridge** | Bridge issuance and orchestration stack; Stripe/Bridge/Privy integration route |
| Consortium company | **Open Standard LLC** | Partner program, economics, product direction and prospective shareholder-board governance |
| Initial founding partners | **Coinbase, Mastercard, Shopify, Stripe and Visa** | Each is described as investing and helping establish supply; together they were expected to support more than $1 billion of near-term launch liquidity |
| Mastercard route | **Mastercard + BVNK** | Advertised API/portal access for buy/sell, swaps, send/receive, settlement and wallets; Mastercard page separately advertises wholesale mint/redeem access and distributor benefits |
| Other launch routes | **Bridge/Stripe/Privy, Coinbase, Visa** | Different onboarding, custody, trading, wallet, settlement and orchestration paths; they are not one common service agreement |
| Reserve institutions | **BlackRock, Lead Bank and BNY** | Named as places where reserves are held; dashboard separately reports cash and Treasury/money-market allocation |
| Token ledgers | **Tempo, Solana, Base and Ethereum** | Exact native token contracts and on-chain supply state |
| User legal route | **Eligible Bridge user through a partner** | Direct redemption right is conditioned on becoming and remaining an eligible user and on the applicable partner/user terms |

## Launch-day operating receipt

Open Standard published the exact four-chain identity of OUSD:

| Chain | Official contract/mint | `totalSupply` observed at 7:11 p.m. EDT |
|---|---|---:|
| Tempo | `0x20c0000000000000000000006a37DA5C996874BE` | 435,220,743.50 OUSD |
| Solana | `ousd2mJsPEckLHcSCDxyKD7NDGARZcfLbDZkKiatYHB` | 18,010,955.40 OUSD |
| Base | `0xB2000000000000000000002fEb517dFeC7415344` | 15,000,528.32 OUSD |
| Ethereum | `0x9f6F3991D525015a6F8CaF062C83b62fD3AC4436` | 10,239,757.80 OUSD |
| **Total** | — | **478,471,985.02 OUSD** |

The direct RPC sum reconciled, to dashboard rounding, to Bridge's 11:00 p.m.
UTC reserve page: **478,471,985 OUSD in circulation** and **$478,471,985 of
reserve assets**. That is a real issuance and reconciliation receipt. It is not
a use receipt. `totalSupply` does not show how much belongs to founders,
liquidity accounts, market makers, exchanges, customers or idle treasury
wallets, and it does not measure transaction volume.

The distribution is also structurally revealing: about **91 percent of minted
supply was on Tempo** at the cutoff. This proves a launch allocation on the
Stripe-incubated payments chain, not organic customer preference for Tempo.

## Reserve, redemption and remedy constitution

Bridge's live reserve page reported:

- **$267,241,277 cash (55.9 percent)**;
- **$211,230,708 Treasury category (44.1 percent)**, with the page explaining
  that the category includes money-market funds made from Treasury-bill ladders
  of less than three months; and
- **100.00 percent issuer-reported collateralization** at 11:00 p.m. UTC.

Bridge's stablecoin terms add the controlling legal boundaries:

1. Bridge Building Inc. maintains reserve market value at least equal to
   outstanding Bridge stablecoins as of 5:00 p.m. New York time on each New
   York Fed business day.
2. Permitted reserve forms include short Treasury bills, overnight Treasury
   reverse repos, government money-market funds, deposits and specified
   tokenized versions of those assets.
3. A holder receives no direct property interest in, or withdrawal right
   against, reserve assets.
4. Eligible-user redemption is promised at one dollar and ordinarily processed
   within two business days after Bridge determines the order complies with the
   user terms.
5. OUSD is not a bank deposit, is not FDIC- or SIPC-insured, is not legal
   tender, and may trade away from one dollar on third-party venues.
6. Bridge may reject or suspend transactions, blacklist addresses and burn
   tokens under law or its compliance policies; the terms do not always require
   replacement tokens after a burn.

The launch announcement says future monthly reserve attestations will be
published. The real-time dashboard is useful, but it is still issuer-published
data rather than the first independent monthly attestation.

## What “Open Standard” means—and does not mean

**Open Standard is the proper name of a company, not proof that OUSD is a
permissionless technical standard.** The public design is open in three bounded
ways:

- many distributors can integrate the asset;
- most reserve economics are intended to flow to partners that create supply
  and activity, less a management fee; and
- founders and participating partners can earn equity and a future voice in
  company governance.

The public record does not yet include the governance charter, board roster,
voting thresholds, shareholder allocations, reward formula, management-fee
schedule, removal rights, issuer-change procedure or failure waterfall.
Open Standard said the board will be established over time from founders and
shareholders. “Collaborative governance” is therefore a launched corporate
design with incomplete public mechanics, not a proven neutral constitution.

The token layer is institutionally controlled. Bridge's generic stablecoin
terms preserve freeze and burn authority, and the verified Ethereum
implementation exposes role-based minting, pausing, address blocking, blocked-
address burning and upgrade functions. Open distribution does not remove the
issuer's lawful-order, compliance, correction and software-control powers.

There is also an undisclosed contractual seam: Bridge's generic terms say the
issuer is entitled to the reserve's net returns, while Open Standard says most
reserve revenue will be shared with partners. The public materials do not show
the agreement that transfers those economics, its seniority, or what happens
if Open Standard, Bridge or a major distributor fails.

There is a second terms seam. Open Standard markets all integration paths as
supporting 1:1 mint/burn at no cost, while Bridge's stablecoin terms preserve
redemption “less Fees, as applicable” and the general user terms place the fee
schedule in the partner account. No public Mastercard/OUSD fee schedule was
located at the cutoff.

## Mastercard's exact role

Mastercard now occupies four adjoining positions:

1. **Founder/investor/governance:** initial Open Standard founding partner and
   investor, with a future board route but no public equity allocation.
2. **Supply/distribution:** helps establish launch supply and can earn rewards
   and equity based on OUSD supply and activity driven through its platforms.
3. **Customer adapter:** advertises API or portal access for OUSD mint/redeem,
   conversion, send/receive, settlement and wallets.
4. **Owned orchestration:** BVNK became part of Mastercard on August 3, giving
   Mastercard an in-house fiat–stablecoin send, receive, store and convert
   stack.

The launch page nevertheless says businesses could begin building **that day**
with BVNK, Stripe and Visa, and with Coinbase on October 1; it did not name the
Mastercard route in that immediate-availability sentence. Mastercard's own page
says “Start testing” and markets the stack as production-ready. The safest
state is therefore:

> **Founding partner + completed infrastructure acquisition + advertised OUSD
> access/testing route; no named Mastercard customer flow or public Mastercard
> OUSD operating volume yet.**

Mastercard does not become the OUSD issuer, reserve custodian or final
redemption obligor. Nor does OUSD make every Mastercard checkout, clearing
message or settlement entry an on-chain OUSD payment.

## Why this matters to the Private Monetary Stack thesis

This is one of the clearest operating examples yet of **authority through the
adapter**:

`customer/platform → Mastercard or another distributor → Bridge issuer and
reserve constitution → exact OUSD contract → destination wallet or venue →
redemption or downstream bank-money settlement`

The reserve-yield model moves economic value capture away from a single issuer
and toward the distribution coalition. The founding payment networks and
platforms are paid to make OUSD the default inventory inside their own routes.
That gives Visa, Mastercard, Stripe, Coinbase and Shopify a reason to hold and
route a common dollar claim without requiring them to merge their customer,
fraud, card, wallet, settlement or accounting systems.

The result supports the Workbench's existing reading: incumbent networks are
not simply being bypassed by stablecoins. They are becoming the gateways that
select the token, admit the customer, abstract the chain, collect the data,
control the remedy path and now share the reserve economics.

## Claims that remain unproved

- OUSD has not been shown to settle ordinary Mastercard card obligations at
  scale.
- The roughly $478.5 million launch supply is not customer payment volume or
  independent demand.
- The promised $1 billion-plus near-term founder liquidity is not the same as
  launch-day circulating supply and had not yet been fully realized at the
  cutoff.
- A 100 percent issuer dashboard is not an independent reserve attestation.
- Named reserve institutions do not disclose exact account title, custody
  priority, fund identity, insolvency treatment or intraday liquidity.
- Partner count does not establish that 200 integrations are live.
- “Native” four-chain deployment does not establish atomic cross-chain
  fungibility or a common legal-finality moment.
- Coinbase, Kraken and Uniswap availability does not establish deep liquidity,
  one-dollar stress performance or unrestricted direct redemption.
- OUSD's name and ticker must not be confused with Origin Dollar (`OUSD`) or
  the unrelated OpenUSD 3D-content standard.
- “Available globally” is qualified: Open Standard excludes the European
  Economic Area and a separate list of countries and territories from partner
  promotion, and also prohibits named use cases.

## Return gates

Reopen on any of the following:

1. first independent monthly OUSD reserve attestation, including auditor,
   measurement time, account/custodian coverage and exceptions;
2. published Open Standard charter, board, voting, ownership or reward terms;
3. a named Mastercard customer using the Mastercard OUSD route with a
   transaction or settlement receipt;
4. a Mastercard rulebook, fee schedule, API specification or liability map for
   OUSD;
5. public wallet/holder distribution and recurring payment or settlement
   volume separated from founder and liquidity inventory;
6. stress evidence: large redemption, chain outage, freeze, fork, depeg or
   cross-chain imbalance and the resulting correction/loss path;
7. final federal payment-stablecoin regulator classification or approval for
   Bridge Building Inc. and OUSD under the GENIUS implementation regime; or
8. disclosed failure waterfall among OUSD holders, Bridge, Open Standard,
   reserve institutions and distributors.

## Primary sources

- [Open Standard — OUSD is live (September 30, 2026)](https://joinopenstandard.com/blog/ousd-is-live/)
- [Open Standard — Build with Open USD](https://joinopenstandard.com/integrate)
- [Open Standard — company structure and leadership (September 24, 2026)](https://joinopenstandard.com/blog/company-structure-and-leadership)
- [Open Standard — introducing Open USD (June 30, 2026)](https://joinopenstandard.com/blog/introducing-open-usd)
- [Open Standard — about and partner/governance FAQ](https://joinopenstandard.com/about)
- [Open Standard — geographic restrictions and prohibited use cases](https://joinopenstandard.com/legal/geo-restrictions-and-prohibited-use-cases)
- [Mastercard — Digital Asset & Stablecoin Solutions](https://www.mastercard.com/us/en/business/payments/consumer-payments/next-gen-payments/digital-asset-solutions.html)
- [Mastercard — BVNK acquisition completed (August 3, 2026)](https://www.mastercard.com/global/en/news-and-trends/press/2026/august/mastercard-completes-acquisition-of-bvnk-to-advance-global-stabl.html)
- [Bridge — OUSD reserve and supply dashboard](https://reserves.bridge.xyz/ousd)
- [Bridge Building Inc. Stablecoin Terms](https://www.withbridge.com/legal/bridge-stablecoin-terms/bridge-building-inc)
- [Bridge Building Inc. U.S. User Terms](https://www.withbridge.com/legal/us-terms/bridge-building-inc)
- [Bridge Building Inc. U.S. licenses and disclosures](https://www.withbridge.com/legal/licenses/us-licenses-and-registrations)
- [Ethereum verified OUSD contract](https://etherscan.io/address/0x9f6F3991D525015a6F8CaF062C83b62fD3AC4436)
- [Base OUSD contract](https://basescan.org/address/0xB2000000000000000000002fEb517dFeC7415344)
- [Solana OUSD mint](https://solscan.io/token/ousd2mJsPEckLHcSCDxyKD7NDGARZcfLbDZkKiatYHB)
- [Tempo OUSD contract](https://explore.tempo.xyz/address/0x20c0000000000000000000006a37DA5C996874BE)

## Custody and precedence

This is a dated Workbench launch return under the existing Card-Network
Stablecoin Product-Line Stack. It resolves the July 29 public-evidence gaps for
the exact OUSD issuer, reserve constitution, contract identities and BVNK
closing without rewriting the July cutoff. The older July maps remain valid as
dated records; this file controls those facts after September 30.
