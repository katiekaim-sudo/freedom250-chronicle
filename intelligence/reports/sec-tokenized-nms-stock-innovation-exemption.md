# SEC Tokenized NMS Stock Innovation Exemption

## Research contract

**Question:** What did the SEC actually authorize on September 17, 2026, how
does the order interact with the transfer-agent proposal and 24-hour-trading
initiative, and what does it change—or not change—for Ripple, XRPL, RLUSD, XRP
and the broader tokenization thesis?

**Controlling authority:** Securities Exchange Act Release No. 34-106402,
File No. 4-927, read in full through all 60 pages. The order outranks the press
release, fact sheet and commissioner statements where descriptions differ.

**Evidence cutoff:** September 17, 2026 at 09:46 EDT. The same-day SEC
roundtable on preparations for 24-hour trading had not yet begun at the cutoff.
It is an adjacent policy inquiry, not part of the order.

**Mutation boundary:** Workbench research only. No Chronicle, watch, app or
generated-projection mutation is authorized by this save.

## Bottom line

This is bigger than the September 1 transfer-agent proposal in one immediate
sense: the transfer-agent release is still a proposal, while Release 34-106402
is an operative five-year exemption. It creates a new federal securities
trading container in which permissioned participants may trade tokenized NMS
stocks through AMM liquidity pools deployed on a public, permissionless
distributed ledger—without the venue registering as an exchange or ATS and
without the venue itself being subject to the specified Regulation NMS venue
rules.

It is not a wholesale escape from securities law. The order preserves
Securities Act registration, antifraud and antimanipulation law, issuer rights,
the underlying NMS stock's rights, trading halts, books and examinations. It
does not itself authorize issuance, custody, clearing, transfer agency,
Investment Company Act activity, broker-dealer participants' separate duties,
bank money, stablecoin issuance or legal settlement finality.

The architecture is therefore a **permissioned market on a permissionless
chain**, surrounded by retained legal and operational institutions. It opens a
meaningful onchain secondary-market lane while making the record, identity,
liquidity, cash, custody, settlement and remedy layers more—not less—important.

## Exact legal state and clocks

| Object | State at cutoff | Clock or boundary |
|---|---|---|
| TSV exemption | Effective Commission order under Exchange Act section 36(a)(1) | Effective September 17, 2026; expires September 17, 2031 unless modified |
| Covered Firm exemption | Effective Commission order under the same authority | Same fixed term; only specified own-account TSV liquidity activity |
| First TSV operation | Not established | Complete public notice at least 30 calendar days before operating; SEC notice within one business day |
| Third-party tokenized stock | Not established | Written notice to issuer; no trading for at least 30 days; issuer may object by the thirtieth day |
| Issuer-sponsored tokenized stock | Eligible category, not an approval | No third-party issuer-objection process, but all TSV and securities-law conditions remain |
| Comments | Requested, no closing date stated in the order or docket at cutoff | Federal Register/comment clock remains separate |
| 24-hour trading | Same-day roundtable, not a rule | Questions surveillance, close prices, clearing, resilience and 24x7 operation |

**Derived earliest-operating boundary:** if a complete TSV notice had been
posted on September 17, the earliest conceivable operation under the 30-day
condition would be October 17, 2026. That is arithmetic from the order, not an
announced launch date. A third-party tokenized stock would independently need
its issuer-notice period satisfied; the two clocks could run concurrently.

## The two exemptions

### 1. Tokenized Securities Venue

A TSV is an organization, association or group that brings together buyers and
sellers through one or more **permissioned AMM liquidity pools** and sets the
standards for access. If all conditions are satisfied, it is exempt from the
Exchange Act definition of `exchange`. It therefore need not register as a
national securities exchange or use the broker-dealer/ATS route for this
activity.

The order also says a qualified TSV is not a market, trading center or market
center for the venue-directed provisions of Regulation NMS. The identified
relief includes the exchange/ATS/trading-center architecture behind quote,
trade-through and sub-penny constraints. Registered broker-dealers that
participate do not automatically receive the same relief; the Commission asks
whether additional relief for them is needed.

### 2. Covered Firm

A Covered Firm may supply Tokenized NMS Stock liquidity to one or more TSV AMM
pools for its **own account** without registering as a dealer solely because
the activity exhibits additional dealer-like features such as customer-facing
pricing or committed-capital arrangements.

The exemption does not authorize customer custody. The firm must maintain
records showing its financial ability and liquid assets, liquidity
contributions, agreements, compensation, fees, rebates and token incentives;
make public disclosures; notify the SEC; acknowledge statutory-disqualification
and oversight conditions; and respond to Commission information requests.

## What may trade

Each eligible pool must contain at least one **Tokenized NMS Stock**. The other
leg may be:

- another Tokenized NMS Stock;
- any non-security crypto asset; or
- a tokenized money market fund.

The order expressly declines to limit the type of non-security crypto asset
that may be paired. That is the most direct new crypto-theory opening. It is a
permission category, not evidence that any particular token has been selected.

Tokenized NMS Stock includes issuer-sponsored and unaffiliated third-party
models. It excludes synthetic exposure, security-based swaps, rights and
warrants. The token must carry the same company interest and rights as the
underlying stock, including dividends, voting and residual claims. A
third-party tokenizer must pass through proxy materials and issuer
communications without charging the issuer or shareholder.

The TSV may not conduct a primary issuance or initial offering. Every offer and
sale still must be registered or exempt. The order grants no Investment Company
Act relief, so the presence of a tokenized money market fund as a pair asset
does not waive fund-law requirements.

## The hybrid control model

```text
issuer / third-party tokenizer
  -> same legal and economic stock rights
     -> transfer agent / official ownership and correction record
        -> permissioned TSV participant set
           -> public, permissionless DLT application
              -> permissioned AMM pool
                 -> Tokenized NMS Stock <-> stock / nonsecurity crypto / tokenized MMF
                    -> separate custody, clearing, settlement, cash and remedy chain
```

The smart contracts and distributed-ledger applications must be auditable,
public and deployed on a public, permissionless DLT. Access to the market is
nevertheless permissioned. The TSV may select pools, set parameters and fees,
pause trading and hold upgrade or override keys. This is not permissionless
market access; it is permissionless infrastructure underneath controlled
admission and administration.

## Conditions that shape the market

### Issuer protection and rights

- An unaffiliated third-party tokenizer must give the issuer written notice.
- Trading cannot begin for at least 30 days after the issuer receives it.
- An issuer objection by the thirtieth day blocks the token from the TSV.
- Silence permits the route; the condition is objection-based, not affirmative
  issuer approval.
- Token holders must receive equivalent economic and governance rights.

### Volume and symbol limits

| Tier | Stocks | Symbol cap | Per-stock volume cap |
|---|---|---:|---:|
| Tier 1 | S&P 500, Russell 1000 and qualifying ETPs | 75 | 0.25% of prior-month ADV |
| Tier 2 | Other eligible NMS stocks | 250 | 2.5% of prior-month ADV |

Affiliates aggregate. A first volume exceedance receives no retrospective
action if future compliance is restored. A subsequent exceedance triggers an
immediate three-month pause for that tokenized stock across affiliates.
Exceeding the symbol cap falls outside the exemption.

### Transparency and market data

The TSV must publish machine-readable, U.S.-dollar transaction data covering
the preceding 30 days and update it within ten minutes. Required fields include
pair symbols, price, size, UTC execution time, direction, pool or contract
address, daily pair volume and end-of-day pool size.

This is meaningful public observability, but it is not the same as consolidated
real-time SIP data. The ten-minute lag, lack of a general fair-access regime and
ability to differentiate participant treatment create a semi-detached market
whose relationship to the primary NMS price remains an empirical question.

### Halts and operational events

The token must halt whenever the underlying stock is halted or suspended on
its primary listing exchange. The TSV must immediately notify participants.
Significant operational events require immediate participant notice, prompt SEC
notice, remediation as soon as practicable and notice when remediation is
complete.

### No financing on the venue

The TSV cannot finance transactions, extend credit to buy a tokenized stock, or
borrow, lend or hypothecate assets on the TSV. This blocks an on-venue leverage
layer. It does not decide every external financing, custody or collateral
question.

### Public notice, records and examinations

The public notice must expose the control system: owners and affiliates,
liquidity-provider governance, registered activities, participant types,
permissioning and identity, tokenization model, legal and technical reviews,
issuer objections, affiliated issuance or trading, conflicts and differentiated
treatment, network and contract addresses, interoperability, upgrade/pause keys,
on- and off-chain functions, price curves, hours, oracles, displays, fees,
complaints, privacy, PII and MEV controls, cybersecurity, audits, BCDR,
clearing/settlement, service providers, surveillance or its absence, halts,
corporate actions, and burn/detokenization exits.

The TSV must preserve detailed interest, execution, permissioning, wallet,
compensation, halt, ADV, event and notice records for the life of the exemption
and three years afterward, in the United States, in human-readable and usable
electronic form. It consents to Commission examination at any time.

The venue must also say plainly that it is not SEC-registered or approved, that
the Commission has not passed on merits or accuracy, and that the TSV is not
subject to the ordinary exchange/ATS fair-access and specified Regulation NMS
regime.

## What the order does not do

| Unopened gate | Why it remains separate |
|---|---|
| Security issuance | No primary issuance on the TSV; Securities Act registration or exemption remains required |
| Authoritative ownership record | The order requires equivalent rights but does not make the AMM or wallet the issuer's official record |
| Transfer-agent status | No transfer-agent exemption or registration is conferred |
| Broker-dealer duties | A participant's existing regulatory status remains; Reg NMS relief for broker-dealers is itself a comment question |
| Custody and customer property | TSV and Covered Firm relief does not create custody authority or customer-priority rules |
| Clearing and settlement | Near-instant settlement is described as a possible benefit, not imposed or legally completed by the order |
| Clearing-agency status | No general clearing-agency exemption appears in the order |
| Money-market-fund law | Tokenized MMFs may be pair assets, but Investment Company Act relief is expressly absent |
| Stablecoin authorization | A non-security crypto pairing permission does not authorize an issuer, reserve, redemption or distribution regime |
| Bank cash or Fed access | No account, liquidity or final-dollar-settlement right is created |
| Token selection | XRP, RLUSD and every other named token remain unselected absent an actual TSV notice and pool |

## Relationship to the transfer-agent proposal

The September 1 proposal and September 17 order occupy adjacent but different
constitutional seats:

| Question | Transfer-agent proposal | Innovation Exemption |
|---|---|---|
| Core function | Authoritative securityholder record, reconciliation, transfer and correction | Secondary execution venue and proprietary AMM liquidity |
| Legal state | Proposal | Effective conditional order |
| Primary accountable actor | One registered recordkeeping transfer agent for a fungible issue | TSV operator; Covered Firm for its own exempt liquidity activity |
| Chain posture | Linked electronic/DLT records may support one accountable master file | Public, permissionless DLT required; access and pools permissioned |
| What it does not settle | Venue, cash, custody, clearing, asset demand | Official title, transfer agency, issuance, custody, clearing and cash finality |

Together they reveal a deliberate decomposition: the official record can remain
with a registered transfer agent while a separate, conditionally exempt AMM
venue performs execution. The architecture is federated, not collapsed into
the token or chain.

## What changes for the existing theory

### Regulatory architecture thesis

The August 26 thesis survives, but one important state flips. The innovation
exemption is no longer a possible future adapter; it is an operative, bounded
adapter. The counter-thesis that U.S. tokenized securities will be admitted
only through incumbent exchange/ATS plumbing is materially weakened.

It is not destroyed. The new lane still depends on issuer rights, controlled
identity, public notice, caps, halts, recordkeeping, exams and external legal,
custody, settlement and remedy layers. The better formulation is now:

> The SEC has created a controlled exterior lane beside the NMS venue stack,
> while retaining the security, issuer, record, participant and failure
> constitution around it.

### Ripple, XRPL, RLUSD and XRP

The order creates a genuine new demand *possibility*: a Tokenized NMS Stock may
trade directly against **any non-security crypto asset** in a qualifying pool.
It also creates a dealer-registration exemption under which own-account
liquidity providers may maintain and be compensated for working inventory.
That is the nearest legal bridge yet to the existing persistent-inventory
theory.

But it does not prove the asset-level thesis:

- **Ripple:** no TSV, Covered Firm or role is named.
- **XRPL:** a public-chain implementation could be technically relevant only if
  it satisfies the order's public, permissionless, auditable application and
  permissioned-pool conditions. No qualifying TSV deployment is established.
- **RLUSD:** a dollar stablecoin could be a conceptually natural cash-side pair
  if it is a non-security asset and all separate issuer, reserve, redemption and
  distribution gates are satisfied. RLUSD is not named or selected.
- **XRP:** the order permits, but does not select, a non-security crypto pair.
  XRP demand requires an actual TSV pool, route share, depth, inventory,
  turnover, holding duration, financing and hedge evidence.

The critical distinction remains:

```text
regulatory permission for a category
  != venue selection of a network
  != pool selection of a token
  != recurring route wins
  != persistent net token inventory
  != token value capture
```

### Securitize and the securities control plane

Securitize's transfer-agent, broker-dealer/ATS, adviser and fund-administration
capabilities make it relevant to the issuance, rights, record and servicing
side of the architecture. Those registrations do not automatically convert an
affiliate or product into a TSV. The order requires registered activities to
remain distinct from the exempt TSV activity; an affiliate may operate the TSV
only through the order's own notice, separation and conflict disclosures.

BUIDL, VBILL and their RLUSD conversion path are not proof of this order's use.
They concern tokenized fund interests, not an operating Tokenized NMS Stock AMM
pool, and the order grants no Investment Company Act relief.

## Why the 24-hour-trading initiative matters—but remains separate

The same-day roundtable asks how overnight and potentially 24x7 trading would
affect surveillance, the closing price, clearing and settlement, operational
resilience, Reg SCI, failover, cybersecurity and staffing. Those are exactly
the interfaces the TSV order exposes: the AMM may operate outside ordinary
hours, but the underlying NMS stock still anchors halts, corporate actions and
much of price discovery.

The conjunction is strategically important but not a combined legal act. The
roundtable is evidence gathering; the exemption is operative law. A future SEC
move that aligns the NMS trading clock, clearing clock and tokenized-venue clock
would be a separate and larger step.

## Primary risks and seams

1. **Price bifurcation:** a 24/7 AMM can trade when the primary market is closed,
   yet its underlying rights and halt logic remain tied to the listed stock.
2. **Protection by disclosure:** the notice may disclose that surveillance,
   complaint, system or other protections are absent; disclosure is not the
   same as a substantive protection requirement.
3. **Market-data lag:** ten-minute public reporting is transparent but not
   equivalent to real-time consolidated data.
4. **Selective access:** participants are permissioned, and the venue is not
   subject to the ordinary exchange/ATS fair-access framework described in the
   mandatory disclaimer.
5. **Externalized settlement:** the order does not itself supply a clearing,
   custody, cash-finality or loss-allocation constitution.
6. **Administrative concentration:** upgrade, pause, override, whitelist and
   pool-selection powers remain powerful control points even on a public chain.
7. **Issuer asymmetry:** a third-party token may proceed after issuer silence,
   but the issuer can object during the notice period and equivalent rights
   must be maintained thereafter.

## Evidence that would change the theory next

- the first complete TSV public notice and its proposed operating date;
- the operator, affiliates, registered activities and Covered Firms;
- exact stocks, tokenizer, transfer agent and authoritative record model;
- public chain, smart-contract addresses, keys, pool parameters and oracles;
- chosen non-security crypto or tokenized-MMF pairs;
- issuer objections and the operator's response;
- custody, clearing, settlement, cash and corporate-action arrangements;
- actual hours, route share, spreads, slippage, pool depth and inventory;
- FINRA/SEC treatment of broker-dealer participation and trade reporting;
- Federal Register publication and any comment deadline;
- Commission modification, extension, permanent rulemaking or early withdrawal;
- empirical evidence of fragmentation, manipulation, outages, corrections or
  investor loss.

## Comment questions in the controlling order

The Commission asks about: (1) making either exemption permanent or changing
the five-year term; (2) market effects, overnight trading and transaction
reporting; (3) extending the model beyond NMS stocks and limiting permissible
pair assets or tokenized money market funds; (4) changing any condition;
(5) changing the tier and volume limits; (6) registered broker-dealer
participation and Regulation NMS difficulties; (7) additional broker-dealer
relief; and (8) the Covered Firm exemption's permanence, scope and conditions.

These questions identify the expansion path. The live order is a bounded
pilot; the comment record is the bridge toward a potentially durable market
structure.

## Source ledger

| Source | Authority and admitted use | Limit |
|---|---|---|
| [Release No. 34-106402](https://www.sec.gov/files/rules/exorders/2026/34-106402.pdf) | Controlling Commission order; legal definitions, conditions, clocks and comment questions | Does not prove any venue, asset or token has begun operating |
| [SEC docket 4-927](https://www.sec.gov/rules-regulations/2026/09/4-927) | Official docket and comment interface | No comment close located at cutoff |
| [SEC press release 2026-90](https://www.sec.gov/newsroom/press-releases/2026-90-sec-issues-innovation-exemption-facilitate-trading-tokenized-nms-stock-request-comment) | Official release summary and resource routing | Summary does not replace order text |
| [Chair Atkins statement](https://www.sec.gov/newsroom/speeches-statements/atkins-innovation-exemption-bridge-toward-durable-rulemaking-091726) | Chair's policy rationale and bridge-to-rulemaking framing | Commissioner statement; not operative text |
| [Commissioner Uyeda statement](https://www.sec.gov/newsroom/speeches-statements/uyeda-statement-innovation-exemption-091726) | Commissioner rationale | Commissioner statement; not operative text |
| [24-hour-trading roundtable](https://www.sec.gov/newsroom/meetings-events/roundtable-preparations-24-hour-trading) | Same-day agenda and adjacent operational questions | Roundtable, not rule or exemption |

## Disposition

**Carry:** the SEC has opened a live, conditional, time-limited public-chain AMM
lane for tokenized NMS stocks and a matching own-account liquidity-provider
lane.

**Carry narrowly:** any non-security crypto asset may be a pair leg under the
order, but no token, chain, operator or venue has been selected by the order.

**Correct:** “effective exemption” does not mean “live venue.” The 30-day TSV
notice clock and product-specific issuer clock still must run.

**Reject:** the order approves XRP, RLUSD, XRPL, Securitize, a tokenized stock,
24/7 NMS trading, primary issuance, custody, clearing, bank settlement or
onchain legal title.
