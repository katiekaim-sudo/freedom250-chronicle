# KOREA MARKET STRESS AND DIGITAL-MONEY TRANSITION — RESEARCH PACKAGE

**Status:** `pending` — merged workbench research; not vault authority  
**Cutoff:** 2026-07-29 after the Seoul close  
**Question:** Did the Korean equity crash remain a concentrated market-structure
unwind, or did it cross into currency, collateral, bank-funding, settlement or
policy layers in a way that changed Korea's monetary-transition path?

## Read order

1. `KOREA_MARKET_EVENT_LEVERAGE_AND_CONTROL_LEDGER_2026-07-29.md`
2. `KOREA_CROSS_ASSET_AUTHORITY_AND_LIQUIDITY_MAP_2026-07-29.md`
3. `KOREA_DIGITAL_MONEY_DEFI_AND_SETTLEMENT_BRIDGE_TEST_2026-07-29.md`
4. `KOREA_MARKET_STRESS_CLAIM_AUDIT_2026-07-29.md`
5. `KOREA_MARKET_STRESS_WATCHBOARD_2026-07-29.md`

## Bottom line

**Yes, South Korea's equity market experienced a verified crash. No, the
evidence available at the cutoff does not show that the crash was caused by
DeFi, absorbed by DeFi, or that it activated a new monetary rail.**

The KOSPI fell 10.84% on July 28 and 5.98% on July 29, a compounded two-session
loss of 16.17%. From its June 19 intraday record of 9,385.59 to the July 29
intraday low of 5,262.77, it fell 43.93%. The June 22 record close of 9,114.55
to the July 29 close of 5,663.24 was a 37.87% drawdown. Both the intraday and
closing-peak clocks are valid; they are different endpoints.

The strongest causal architecture is:

> **global AI/memory-semiconductor repricing → Korea's exceptional Samsung/SK
> hynix concentration → foreign cash selling and marketwide liquidation →
> possible amplification by daily-reset single-stock 2x products and other
> unmeasured leverage → exchange cooling controls.**

That is not yet a monetary-system break. On the first crash day the won
strengthened against the dollar and three- and five-year Korean Treasury yields
fell. Corporate-credit spreads widened, which is the principal cross-asset
warning. A KRW28 trillion Bank of Korea 14-day repo purchase occurred, but its
tenor, auction channel and 2.75% clearing rate matched ordinary open-market
operations; no exceptional terms or emergency authority were identified.

Korea's digital-money transition was already under way before this event:
Project Hangang had completed a bounded real-user Phase I pilot and formally
started Phase II; BOK-Wire+ remained the production wholesale-finality rail;
securities-token legislation had passed but was not yet effective; and
stablecoin, Agorá and other adapter work remained legally or operationally
separate. No measured equity/deposit migration into crypto, a won stablecoin,
deposit tokens or DeFi was established. A pre-event July 1-22 estimate placed
five-exchange crypto turnover at only about 1.59% of KOSPI turnover, and public
price reporting had bitcoin falling during the July 28 risk-off move. Turnover
is not net flow, but neither observation supports a simple crypto-refuge story.
The crash therefore belongs in the project as a **stress test of the transition
architecture**, not as proof that the transition caused or accelerated it.

## What happened

### Exact market spine

| Date | KOSPI | KOSDAQ | Control and flow |
|---|---:|---:|---|
| 2026-07-28 | 6,023.66, **-10.84%** | 705.85, **-7.72%** | Sell-side sidecars and phase-1 marketwide circuit breakers; foreign KOSPI net selling about KRW4.97tn; 875 decliners against 36 advancers |
| 2026-07-29 | 5,663.24, **-5.98%**; intraday low 5,262.77 | 662.68, **-6.12%** | Second KOSPI sidecar and circuit breaker; foreign and retail net selling against about KRW3.16tn institutional net buying; 804 decliners against 91 advancers |

The circuit breakers establish that published index thresholds persisted long
enough to activate KRX controls. They do not identify the seller or the cause,
and they are not price floors. The observable trigger-pause-reopen sequence
functioned; continued losses do not by themselves prove operational failure.

Sources: [Yonhap, July 28
close](https://en.yna.co.kr/view/AEN20260728007752320?section=economy-finance%2Feconomy);
[Yonhap, July 29
close](https://en.yna.co.kr/view/AEN20260729006752320?section=economy-finance%2Feconomy);
[KRX circuit-breaker
rules](https://global.krx.co.kr/contents/GLB/06/0602/0602010204/GLB0602010204T2.jsp).

### Concentration without an optical illusion

The FSC measured Samsung Electronics and SK hynix together at 52% of KOSPI
market capitalization on July 15, up from 34% at end-2025. Both fell more than
the index on July 28. That concentration mechanically increased Korea's
sensitivity to a global memory-chip repricing.

But the selloff was not merely a two-stock index illusion. All KOSPI sectors
were negative on July 28 and breadth was extreme on both days. The correct
classification is **concentrated trigger and transmission plus broad
liquidation**, not “only two stocks crashed.”

Source: [FSC, July 16
concentration and product review](https://www.fsc.go.kr/eng/pr010101/87354).

### The leverage mechanism

Korea's single-stock leveraged and inverse products launched on May 27. By July
15, sixteen products had reached KRW11.9 trillion in size and KRW13.0 trillion
in daily trading value. The regulator suspended new listings and marketing on
July 16, accelerated a higher cash-deposit requirement on July 24 and, during
the July 28 decline, asked managers to disperse end-of-day rebalancing.

Daily-reset 2x exposure is procyclical: after an underlying decline, a manager
generally sells exposure to reset the next day's ratio. Korea Capital Market
Institute estimated a modest but non-zero spot-rebalancing share in its earlier
May 27-June 19 sample and explicitly did not establish causality. No
manager-by-manager July 28-29 spot/futures hedge tape was retrieved.

**Ruling:** the products are a verified possible amplifier. Their crash-day
contribution is `NR`; calling them the prime mover is not supported. The broad
claim that the products were themselves liquidated through broker credit is
also weakened because securities-credit trading in the products was barred at
launch. Margin and forced-sale channels elsewhere in portfolios remain
unmeasured.

Sources: [FSC, May 15 product
design](https://www.fsc.go.kr/po010101/86910?curPage=14&srchBeginDt=&srchCtgry=&srchEndDt=&srchKey=&srchText=);
[KCMI rebalancing
analysis](https://www.kcmi.re.kr/publications/pub_detail_view?cno=6801&syear=2026&zcd=002001016&zno=1922);
[FSC, July 24 accelerated
controls](https://www.fsc.go.kr/eng/pr010101/87405).

## Cross-asset and authority transmission

### Observed

- The won closed July 28 at KRW1,462.5 per dollar, six won stronger.
- Three-year and five-year KTB yields fell 3.6 and 4.9 basis points on July 28.
- The three-year KTB/AA- corporate spread widened to 71.6 basis points, the
  widest of 2026 to that date.
- BOK allotted KRW28 trillion in a 14-day repo purchase at 2.75% on July 28.
- No public settlement outage was located on BOK, KRX, KSD or KFTC surfaces.

The first two observations run against a simultaneous equity/won/sovereign
funding spiral. The corporate spread is a real yellow flag. It requires CP,
primary-issuance, dealer, turnover and bank-funding data before promotion to a
credit-market freeze.

The repo operation was large but retained the documentary signature of regular
reserve management: standard series, standard tenor, policy-rate clearing and
same-channel comparators on June 30 and July 21. A crash-day operation is not
automatically a crash-response facility.

Sources: [BOK, July 28 repo
result](https://www.bok.or.kr/portal/bbs/P0001773/view.do?depth=200037&menuNo=200037&nttId=11063233&programType=newsData&relate=Y);
[BOK, July 21 comparator](https://www.bok.or.kr/portal/bbs/P0001773/view.do?depth=200037&menuNo=200037&nttId=11063040&programType=newsData&relate=Y);
[SBS bond-market
report](https://news.sbs.co.kr/english/article.do?news_id=N1008679094).

### Available or pre-positioned, but not shown activated

| Object | Cutoff state |
|---|---|
| BOK liquidity-adjustment loan and intraday credit | `AVAILABLE`; episode use not found |
| Bank of Korea Act Article 65 emergency financial-institution lending | `AVAILABLE-NOT-USED` in the reviewed public record |
| Bank of Korea Act Article 80 enterprise/nonbank credit | `AVAILABLE-NOT-USED` |
| Corporate-loan-receivable collateral framework effective 2026-01-02 | `PRE-POSITIONED`; collateral eligibility is not a draw |
| Extraordinary collateral/counterparty expansion or unlimited fixed-rate RP | `AVAILABLE BY PRECEDENT`; current activation not found |
| Stock/bond stabilization funds and corporate-bond/CP vehicles | `CONTINGENT`; current transaction not found |
| FX intervention or swap-line draw | `NOT-PUBLICLY-STATED` / current draw not found |
| D-SIFI recovery and KDIC resolution plans approved before the crash | `PRE-POSITIONED`; current trigger/activation not found |
| BOK-Wire+, KRX/KSD and retail-payment continuity | no public incident found; measured performance `NR` |

December 2024 and 2020 provide documentary controls. Those episodes produced
irregular designations, widened collateral or counterparties, fixed-rate
full-allotment options, special facilities and explicit expiry clocks. That
signature was absent in the July 28-29 record reviewed here.

## Does it enter the monetary-transition story?

### Yes—as a stress test

This episode pressure-tests five seams already central to the project:

1. whether concentrated listed assets and new leverage wrappers transmit into
   broker, bank or central-bank funding;
2. whether collateral is mobilized under ordinary or emergency authority;
3. whether BOK-Wire+, KRX clearing and KSD settlement preserve finality;
4. whether public authorities respond through conventional facilities or
   tokenized/programmed rails; and
5. whether households or institutions move value into a different money object.

### No—not yet as a transition event

None of the named promotion bridges was demonstrated at cutoff:

- no verified Article 65/80 or other extraordinary facility activation;
- no verified won-stablecoin launch or use in the response;
- no evidence that Hangang deposit tokens settled KRX losses or supplied
  emergency liquidity;
- no effective securities-token substitution for KRX/KSD;
- no public BOK-Wire+ or tokenized-finality change caused by the crash; and
- no measured, attributable equity/deposit migration into crypto or DeFi.

The July 28 KB-Kinexys announcement does not pass the test. It described an
August launch, initially in USD, on an institutional permissioned bank network
developed under an earlier MOU. The announcement shared a calendar date with
the crash; the underlying project clock did not originate in it.

The crash did not create Korea's digital architecture. It arrived while that
architecture was being built.

## Object-and-clock firewall

| Object | Issuer / legal claim | State at cutoff | Crash connection |
|---|---|---|---|
| BOK-Wire+ balances | Central-bank money held by eligible institutions | `PRODUCTION`; hours extended to 20:00 from 2026-03-30 | Conventional finality rail; no public incident or crash-caused rule change found |
| Hangang wholesale digital money | BOK digital settlement object inside a permissioned test architecture | `PILOT` | Supports participating-bank token settlement in the test; not general retail CBDC |
| Hangang deposit token | Liability of a participating commercial bank to its customer | Phase I completed real-user pilot; Phase II formally initiated | No crash-related issuance, flight or emergency use shown |
| Won stablecoin | Prospective private issuer claim under an unsettled regime | `PROPOSED / POLICY DEBATE`; no general launch established | No response role or migration evidence |
| Crypto exchange asset | Property/risk asset traded on regulated domestic exchanges | `PRODUCTION TRADING` | Trading is not DeFi; risk-off co-movement does not show refuge |
| DeFi position | On-chain protocol claim/liquidity position | public Korea-attributable crash-flow evidence `NR` | No measured bridge |
| Tokenized security | Security recorded under future controlled DLT framework | Acts passed; effective 2027-02-04 | Did not replace KRX/KSD in this episode |
| Project Agorá prototype | Cross-border tokenized correspondent-banking prototype | `PROTOTYPE`; future real-value testing separate | No July crash-response use |
| ISO 20022 on BOK-Wire+ | Structured financial messaging, not money | `PRODUCTION` from 2026-05-26 | Interoperability modernization; not a coin or DeFi protocol |
| KB-Kinexys corporate payment service | Initially USD commercial-bank money on a permissioned institutional network | Announced 2026-07-28 for August launch; underlying Kinexys network already production | Same-day coincidence on a pre-existing build; no completed Korean customer transaction at cutoff |

Sources: [BOK, Hangang Phase II
launch](https://www.bok.or.kr/portal/bbs/B0000502/view.do?menuNo=201265&nttId=10097017);
[FSC, securities-token legislation](https://www.fsc.go.kr/eng/pr010101/86076);
[BOK, July 8 tokenization issue
note](https://www.bok.or.kr/eng/bbs/B0000354/view.do?depth=400409&menuNo=400409&nttId=11062710&programType=newsDataEng&relate=Y).

## Five-part event classification

| Pole | Current finding |
|---|---|
| **Trigger** | Global AI/memory-semiconductor repricing, supported by prior U.S. chip losses and synchronized Japan/Taiwan weakness |
| **Korea-specific amplifier** | Samsung/SK hynix concentration, broad foreign selling and a real but unquantified daily-reset leverage channel |
| **Cross-asset transmission** | Corporate-credit warning; no observed first-day won collapse or sovereign selloff; money-market/bank/broker data incomplete |
| **Official response** | KRX controls activated; BOK regular OMO observed; extraordinary liquidity, stabilization, intervention, resolution and settlement changes not established |
| **Monetary/digital bridge** | Pre-existing regulated pilot/legal/adapter build; no crash-caused migration or activation demonstrated |

## Competing hypotheses

| Hypothesis | Ruling | Decisive evidence still needed |
|---|---|---|
| Global chip repricing triggered the crash | **Supported** | precise news/order timing and official cross-market closes |
| KOSPI concentration amplified it | **Strongly supported** | daily index-point contribution |
| It was only a two-stock illusion | **Rejected** | breadth already contradicts it |
| Single-stock 2x products amplified it | **Plausible, unquantified** | manager/LP spot and futures hedge tape |
| Single-stock 2x products caused it | **Not established** | counterfactual price impact and crash-day order attribution |
| Short selling caused it | **NR** | KRX short turnover, balances and stock-level positions |
| Broader margin calls drove the second-day low | **NR** | KOFIA credit, forced-sale and derivative variation-margin data |
| The event became a systemic funding/FX crisis | **Not established** | KOFR/repo/CD/CP, NDF/swap basis, bank deposits/funding, BOK-Wire+ and settlement-fail data |
| DeFi absorbed flight from Korean equities | **Not established and currently weakened** | attributable exchange-to-wallet/on-chain flows and a recipient protocol/money object |
| Authorities used the event to accelerate a digital rail | **Not established** | dated operative decision, legal authority, named rail, participants, value and finality |

## The project-level interpretation

The episode strengthens one part of the larger monetary thesis and weakens
another:

- **Strengthened:** market concentration and procyclical product design can
  generate an asset-side shock that tests collateral, liquidity and finality
  architecture. Korea is an unusually useful observatory because its
  conventional and tokenized layers are institutionally dense.
- **Weakened:** “traditional market breaks, therefore value moves to DeFi” is
  not an observed chain. Korea's own published architecture currently
  prioritizes central-bank money and commercial-bank deposits—including
  tokenized forms—for settlement, with stablecoins supplementary.

The Bank of Korea's July 8 tokenization note is important here. It describes
Korea as early-stage, identifies leverage, rehypothecation, platform
concentration and fragmentation as possible future stability risks, and calls
for combined on-chain/off-chain monitoring. That is a roadmap for how this
research should be conducted; it is not evidence that tokenized markets caused
this equity event.

## Source hierarchy and limits

The merged judgment uses, in descending order:

1. BOK, FSC and KRX law, rule, facility and operating records;
2. BOK/FSC transaction or auction results and official corporate filings;
3. KCMI mechanism research with its causal caveats;
4. Yonhap/KBS/SBS event reports for same-day tape fields not exposed in a
   retrievable KRX release; and
5. other secondary market reporting only as labeled context.

Major unresolved fields are preserved rather than inferred:

- July 29 complete FX/rates/credit close panel;
- KOFR, repo, CD/CP and bank-bond stress;
- KOFIA margin, forced-sale and credit balances;
- KRX short-sale and manager/LP hedge data;
- BOK-Wire+ queues/intraday credit and KSD settlement fails;
- Q3 FX intervention disclosure;
- attributable crypto-exchange, wallet and DeFi flows; and
- any post-cutoff official inter-agency decision.

## Promotion rule

Move this package from a severe asset-market shock to a monetary-transition
event only if a later source identifies:

> **the legal or operating object, the competent entity, the activation or
> transaction time, the amount/value, the settlement/finality path and the exit
> or effective clock.**

Until then, the factual answer is: **historic Korean equity crash; plausible
market-structure amplification; incomplete corporate-credit transmission;
systemic monetary break and DeFi migration not demonstrated.**
