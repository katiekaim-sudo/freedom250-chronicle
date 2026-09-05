# KOREA STRESS TRANSMISSION — DEEP DIVE

**Status:** `pending` — completed workbench research; not vault authority  
**Parent event cutoff:** 2026-07-29 after the Seoul close  
**Follow-on rule:** a series unavailable at cutoff remains `NR`; later
publication must retain its observation and release clocks

## Governing question

Did the Korean equity crash produce a verifiable chain from asset-price losses
through leverage, funding, collateral, clearing/finality or alternative digital
rails?

## Bottom line

The deep dive **changes the broad-pass conclusion in two important ways**:

1. It weakens the popular forced-liquidation story. KOFIA's public series shows
   July 28 credit-financing balances rising and actual forced-sale amounts
   falling. A July 29 liquidation wave remains possible but was not yet
   observable.
2. It prevents an early “plumbing held” conclusion. July 28 and July 29 cash
   equities settle T+2, on July 30 and July 31. Those deadlines were still in
   the future at the cutoff.

The strongest merged model is:

> **regional AI/memory-semiconductor repricing → unusually concentrated Korean
> index and large foreign selling → broad price decline and exchange controls
> → higher collateral pressure and possible product rebalancing, but no
> observed July 28 public broker-credit liquidation surge → ordinary BOK repo
> rollover and a corporate-credit warning → post-trade outcome not yet due →
> crypto trades risk-off without a demonstrated Korean DeFi flow.**

This is an asset-market and collateral **stress event**, not a demonstrated
monetary-system or DeFi-transition event.

## Causal-chain verdict

| Arrow | Verdict | Decisive observation |
|---|---|---|
| Regional chip repricing → Korean equity loss | **Strongly supported** | Taiwan and Japan fell concurrently; Korea's two largest chip issuers were 52% of KOSPI capitalization |
| Korea concentration / foreign selling → larger Korean fall | **Supported, not fully decomposed** | Concentration and flow are observed; exact index-point/price-impact contribution missing |
| Equity loss → collateral pressure | **Supported as pressure, not failure** | Derivatives deposits and unpaid receivables rose |
| Collateral pressure → July 28 forced-sale wave | **Weakened / not supported by KOFIA series** | Actual forced sale fell to KRW13.890bn from KRW22.961bn |
| Product reset → extra spot/futures selling | **Plausible / unquantified** | Mechanism verified; hedge tape missing |
| Equity loss → systemic secured-funding break | **Not established** | KOFR/volume incomplete; ordinary RP operation observed |
| Equity loss → corporate-credit freeze | **Not established** | Roughly 71bp AA-/KTB spread warning, but outright yields fell and issuance data missing |
| Crash trades → clearing/settlement failure | `NR` | T+2 deadlines postdate cutoff |
| Crash → crypto liquidation | **Not established** | No Korean-attributed collateral/liquidation data |
| Crash → equity-to-DeFi flight | **Not established and price narrative weakened** | BTC fell modestly; turnover rose but net/source-attributed flows missing |
| Crash → activation of new digital rail | **Rejected on current evidence** | Hangang, tokenized securities and Kinexys clocks predate the crash and remained separate |

## What the official leverage data say

On July 28, in KRW million:

| Field | Jul 27 | Jul 28 | Change |
|---|---:|---:|---:|
| Credit financing | 32,741,063 | 33,194,040 | +452,977 |
| Investor deposits | 109,167,491 | 107,199,449 | -1,968,042 |
| Derivatives deposits | 45,921,759 | 48,326,943 | +2,405,184 |
| Unpaid receivables | 1,078,329 | 1,223,729 | +145,400 |
| Actual forced sale | 22,961 | 13,890 | -9,071 |
| Forced-sale ratio | 2.2% | 1.3% | -0.9pp |

This looks like **greater collateral and receivable pressure without a same-day
surge in the retrieved realized forced-sale field**. It does not cover all
derivatives, CFDs, funds or OTC structures.

Source: [KOFIA FreeSIS](https://freesis.kofia.or.kr/stat/FreeSIS.do?parentDivId=MSIS10000000000000&serviceId=STATSCU0100000060).

## What the BOK operation says

The BOK did not simply add KRW28tn to a standing KRW30tn injection. Its July 16
KRW30tn repo purchase matured on July 28, when a new KRW28tn 14-day operation
was allotted. Bids of KRW30.20tn exceeded supply, showing demand for the
operation, but the terms retained the signature of ordinary OMO at the new
2.75% policy rate.

That is consistent with **routine liquidity management under stress**, not
proof of either “nothing happened” or “emergency rescue.”

Sources: [BOK, July 16 terms](https://www.bok.or.kr/portal/bbs/P0001773/view.do?menuNo=200295&nttId=11062947);
[BOK, July 28 result](https://www.bok.or.kr/portal/bbs/P0001773/view.do?menuNo=200295&nttId=11063233).

## What the regional control says

Two-session compounded declines:

- KOSPI: **-16.17%**;
- TAIEX: **-8.24%**;
- Nikkei 225: **about -5.61%**.

The common direction makes a Korea-only causal story untenable. The magnitude
gap keeps Korea-specific amplifiers in scope. It does not identify their
weights.

Sources: [TWSE July daily table](https://www.twse.com.tw/en/exchangeReport/FMTQIK?response=html&date=20260729);
[Nikkei Indexes historical data](https://indexes.nikkei.co.jp/nkave/archives/data?list=daily).

## Clearing and finality clock

| Trade date | Normal KRX member/CCP completion | Cutoff state |
|---|---|---|
| Jul 28 | Jul 30, by 16:00 | Not yet due |
| Jul 29 | Jul 31, by 16:00 | Not yet due |

The circuit breakers prove that exchange controls activated. They do not prove
that KSD delivery, the cash leg and CCP obligations later completed. The KRX
default waterfall was available but no use was identified.

Sources: [KRX T+2 schedule](https://global.krx.co.kr/contents/GLB/06/0602/0602010201/GLB0602010201T1.jsp);
[KRX default waterfall](https://global.krx.co.kr/contents/GLB/06/0608/0608050501/GLB0608050501.jsp).

## Crypto and DeFi result

Upbit's KRW-BTC price fell 0.50% in the July 28 09:00 KST daily candle while
turnover rose to about KRW89.54bn from KRW69.31bn. The incomplete July 29
candle was also negative at retrieval. This is consistent with risk-off
co-movement, not safe-haven repricing.

No retrieved dataset could match:

- a Korean brokerage sale to a VASP deposit;
- a VASP withdrawal to a wallet;
- a Korean wallet to a bridge or DeFi protocol;
- a collateral position to a liquidation; or
- a stablecoin mint/redemption to a Korean beneficial owner.

Trading intensity is not net migration.

Source: [Upbit public KRW-BTC candles](https://api.upbit.com/v1/candles/days?market=KRW-BTC&to=2026-07-30T00%3A00%3A00Z&count=5).

## Five-pole reading

| Pole | Finding |
|---|---|
| **PLUMBING** | Exchange controls observed; collateral pressure visible; ordinary BOK OMO observed; T+2 finality not yet due |
| **TOKEN** | Crypto traded as a risk asset; no attributable stablecoin/DeFi migration; Kinexys remains a separate permissioned bank rail |
| **STATE-LEDGER** | Hangang test assets remained bounded pilot objects; no emergency or production activation |
| **WALL** | KRX, KSD, BOK and VASP legal/operational perimeters remained distinct; future securities-token and won-stablecoin clocks did not move |
| **METAL** | No event-specific collateral substitution or safe-haven flow established; remains out of scope |

## What changed from the broad pass

| Broad-pass field | Deep-dive correction |
|---|---|
| Broader margin calls drove second-day low: `NR` | July 28 forced-sale story is weakened; July 29 remains `NR` because of publication lag |
| BOK KRW28tn operation looked regular | Stronger: it replaced a maturing KRW30tn operation; gross amount was not a new additive rescue |
| Corporate spread widened | KOFIA closes show about 70.9bp then 71.2bp; SBS's 71.6bp snapshot is preserved as a distinct source |
| No public settlement incident found | Stronger clock boundary: crash-trade T+2 settlement had not occurred |
| No crypto/DeFi bridge established | Stronger: official Upbit probes show negative BTC price with more activity, still without net-flow attribution |
| Regional chip shock supported | Stronger: exact Taiwan two-day loss supplies a close semiconductor control |

## Limits and promotion rule

The package remains `pending` for possible vault review because the decisive
post-event releases did not yet exist at cutoff:

1. KOFIA July 29 forced-sale and credit data;
2. KRX/KSD July 30-31 settlement completion and fails;
3. KOFR and repo-volume/haircut details;
4. CP and primary corporate-bond issuance/rollover;
5. member margin and collateral calls;
6. Korean-attributed VASP, wallet and protocol flows; and
7. date-matched Taiwan/Japan investor flows and index contributions.

Promote the event into the monetary-transition thesis only if one of these
bridges becomes observed: extraordinary public liquidity authority, funding
market impairment, default-waterfall use, failed cash/securities finality, or
an attributable movement into a different monetary claim or settlement rail.
