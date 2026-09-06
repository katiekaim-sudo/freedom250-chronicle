# SEC Investor Advisory Committee — 2026 analysis

## Factual result first

The Investor Advisory Committee is a Dodd-Frank §911 advice body. Its 2025–2026
public record is a running design argument about how U.S. equity plumbing
should change: who owns a tokenized share, who may intermediate it, whether
Reg NMS still applies, how often issuers must report, and how retail gets
into private markets.

The Committee **did** adopt recommendations. It **did not** authorize a
venue, a token, a chain, a transfer agent, a TSV, or a change to Rule 611.
Those clocks belong to Commission orders, proposals, and later operating
notices.

The object we were missing is the March 12, 2026 **Recommendation of the
Investor Advisory Committee Regarding the Tokenization of Equity Securities**.
It was adopted 12–0–2. It told the Commission:

1. do **not** grant a blanket innovation exemption;
2. if the Commission uses a limited/narrow exemption **or** rule-by-rule
   reform, run notice and comment;
3. do not compromise three protections — ownership-right disclosure,
   regulated intermediaries, and best terms for orders;
4. preserve state authority consistent with NSMIA.

On September 17, 2026 — seven days after the latest IAC meeting, and six
months after that recommendation — the Commission issued effective
Release 34-106402.
That order is the permission object. The IAC text is the advice object.
Whether the order is “narrow” or “blanket,” and whether it kept the three
protections, is a comparison of two official documents, not a vote result
and not an operating fact.

## What the 2026 meetings changed

| Object | Before | Now established | Still not established |
|---|---|---|---|
| Tokenized equity advice | Dec. 4, 2025 panel (Coinbase, BlackRock, Robinhood, Nasdaq, Citadel Securities, Galaxy) | March 12 rec adopted 12 in favor, 2 abstentions | Commission adoption of the rec; any named token, chain, TSV, or operating market |
| Tokenized NMS trading permission | staff statements and the IAC rec | Sept. 17, 2026 Release 34-106402, effective conditional order through 2031 | a complete 30-day TSV notice, issuer non-objection, transfer-agent record, custody, clearing, cash, or first trade |
| Quarterly reporting | Commission proposal File S7-2026-15 (May 5, 2026) to replace 10-Q with optional 10-S | June 4 IAC rec: **do not** drop the quarterly mandate | final rule, withdrawal, or issuer election |
| Fund proxy plumbing | March 12 panel on quorum/cost failure | June 4 rec: sequenced modernization, starting with opt-in retail voting programs | staff no-action, rule, or first fund using a new mechanism |
| Private-market retail access | Sept. 18, 2025 rec: registered funds as the preferred path | June 4 panel on gating, fees, valuation, FINRA advertising review | a 1940 Act rule change or accredited-investor rewrite |
| AI disclosure rec | Dec. 4, 2025 rec adopted 14–2–2, Gulliver dissent | still advice | a Commission AI line-item rule |
| AI in the filing stack | structured-data mandate already live | Sept. 10 staff/XBRL panel: machine-readable data as the AI input layer | a new taxonomy, validation rule, or issuer AI-drafting standard |
| Rule 611 / trade-through | June 2026 Commission proposal to rescind Rules 611 and 610(e) | Sept. 10 IAC panel plus Atkins calling 611 a “policy misstep” from his first commissioner term | final rescission, a replacement NBBO integrity rule, or a sequencing order for other NMS changes |
| IAC officers | Brian Schorr chair through March 12 | Georgiev / Seidt / McGarrity / Gulliver | — |
| Investor Advocate seat | Firvida through Dec. 4, 2025 | listed vacant | a named successor |
| Commissioner Peirce | sitting | Sept. 10 remarks: “likely my last” IAC meeting | her actual departure date |

## 1. The tokenization recommendation is the load-bearing IAC object

Approved text, March 12, 2026. Minutes: motion seconded; voice vote 12 in
favor (two by proxy), two abstaining (one by proxy). Brian Schorr was still
chair that day. Atkins, Peirce, and Uyeda spoke in the morning and were not
in the afternoon vote session.

### What the Committee said a tokenized equity security is

A crypto asset whose ownership record exists, in whole or in part, on a
distributed ledger **and** that meets the definition of an equity security.
Federal and state securities law, SEC rules, and FINRA requirements therefore
already apply. New rules or exemptions are still needed because issuance and
trading differ from the DTC/NSCC database model.

Two splits, kept separate in the rec:

- **native** (issued on a chain) versus **wrapped** (an underlying share is
  custodied and a token represents that position);
- **issuer or issuer-directed** tokenization versus **unaffiliated third
  party**.

A wrapped third-party token may not carry the same voting, dividend, or
bankruptcy rights as a native issuer token. The rec uses ADRs / VIE
structures as the warning analog: economic exposure without clear legal
ownership.

### What it said the current plumbing is

Ownership and trading of equities run through centralized databases at
broker-dealers, DTC, and NSCC — “the plumbing” — facilitating over $1.9
trillion in daily volume. Tokenization is framed as a possible replacement
of those databases, not as a coin listing.

Claimed benefits, as Committee advice, not demonstrated results:

- atomic delivery-versus-payment, collapsing T+1 settlement risk;
- issuer visibility into the shareholder base now hidden in street name;
- cheaper corporate actions (dividends, proxy);
- a technical path to 24/7 equity trading.

Claimed costs, also advice:

- atomic settlement can destroy multilateral netting and raise capital
  needs for brokers and institutions;
- error-correction windows shrink;
- DeFi-style trading without a broker can drop best execution, 605/606
  reports, front-running rules, kill switches, and circuit breakers;
- fully anonymous wallets break beneficial-owner records, insider-trading
  enforcement, issuer/transfer-agent notice, quorum, and KYC against
  sanctioned persons.

### The three non-negotiable principles

```text
tokenized equity
  → disclosure of what the holder actually owns
       (vote, dividend, pari passu on splits/M&A/bankruptcy)
  → intermediaries still under SEC, state, and/or FINRA
       (no fully anonymous, unregulated matching)
  → best terms for orders
       (Reg NMS goals: order protection, fair access, ticks, execution reports)
  → NSMIA-consistent state authority retained
```

The Committee explicitly declined to define “intermediary” for new
tokenization entities and deferred that to Congress. It did say KYC can
move from repeated manual checks to reusable cryptographic wallet
credentials after an initial verification. That is a design suggestion,
not a rule.

### The exemption grammar

The rec rejects a **blanket** innovation exemption. It accepts a
**limited/narrow** exemption **or** rule-by-rule reform. Either path, it
says, should go through public notice and comment. It cites Atkins’s
July 31, 2025 “American Leadership in the Digital Finance Revolution”
speech as the Commission’s public innovation-exemption signal, then tells
the Commission not to use that signal as a general off-switch for
investor-protection rules.

## 2. Crosswalk to today’s Innovation Exemption — two clocks, not one story

The controlling legal object is Release 34-106402, already read in
`sec-tokenized-nms-stock-innovation-exemption`. This package does not
re-litigate that order. It only joins the IAC advice to it.

| IAC March 12 rec | Release 34-106402 (Sept. 17) | Join, without collapsing |
|---|---|---|
| Do not grant a blanket exemption | Temporary, conditional exchange-definition exemption for a Tokenized Securities Venue and a dealer-definition exemption for qualifying own-account LPs, through Sept. 17, 2031 | The order is not unlimited in time or unconditioned. Whether those conditions are the IAC’s “narrow” exemption is a legal comparison, not a Committee finding. |
| Use notice and comment | Order is **already effective**; comment is requested on File 4-927 | Advice asked for comment *before* the permission. The Commission issued permission and opened a comment file. Those are different sequences. |
| Ownership-right disclosure, including third-party wrappers | Order does not itself authorize issuance. It gives the NMS-stock issuer an objection path for a third-party tokenized stock in a TSV pool | Issuance, recordkeeping, and trading-venue permission remain separate. The objection right is not the IAC’s proposed EDGAR ownership-rights document. |
| Keep intermediaries regulated | TSV is exempted from the Exchange Act *definition of exchange* if conditions are met; LPs may be exempted from *dealer* | This is the sharpest tension. The IAC said technology should not let tokenized equity “operate without an adequate regulatory regime.” The order creates a permissioned AMM on public permissionless DLT under listed conditions. Conditions are not the same as broker-dealer / exchange registration. |
| Best terms for orders / Reg NMS goals | TSV trading is the subject of an exchange-definition exemption; ordinary NMS stock trading remains on the other clock | Sept. 10 IAC panel was about rescinding Rule 611 in the *existing* NMS, not about TSV AMMs. Do not treat the 611 proposal as the tokenization exemption. |
| Atomic settlement vs. netting | Order does not authorize clearing, NSCC netting replacement, or legal settlement finality | IAC named the netting cost. The order leaves that gate closed. |
| 24/7 as a possible benefit | Order does not itself authorize 24-hour NMS trading | Same-day (Sept. 17) roundtable is the 24-hour clock. Atkins there pointed to DTCC 23×5 trade capture as already live. That is DTCC operations, not IAC advice and not the TSV order. |

**State at cutoff:** the Commission has now acted on tokenization of NMS
stock through an exemptive order. It has not published a document that
says “we accept” or “we reject” the March IAC recommendation. Do not
infer either.

## 3. September 10, 2026 — AI in the filing stack, then Rule 611

No minutes, no official transcript, no recommendation vote. Official
written objects control the openings. The webcasts are the discussion
record.

### Atkins (pre-recorded)

Customary personal-views disclaimer. AI may help investors distill
filings; it does not give the Commission “latitude to depart from its
longstanding principle of materiality.” Issuer cost does not disappear
because AI can read the file afterward. AI is a complement to human
judgment, not a substitute; hallucinations remain a disclosure problem.
The Commission will not prescribe models — “we are not a merit
regulator.”

On NMS: Rule 611 is a “significant policy misstep” from his first tour
as commissioner. He and then-Commissioner Glassman warned it would
substitute regulatory judgment for the “market for markets.” The
Commission proposed in June to rescind Rules 611 and 610(d)/(e) (locked
and crossed). Staff is reviewing comments. The panel is input, not the
decision.

### Peirce — “Lame Duck”

Likely her last IAC meeting. Questions she wanted on the table:

- Does issuer AI improve disclosure or produce boilerplate?
- Will AI entrench current structured-data conventions?
- Is the large/small issuer gap widening?
- Are any AI issues ripe, or is premature rulemaking the larger risk?

On 611: commenters worry the NBBO’s integrity falls if 611 dies. How
should a post-611 NBBO stay a reliable benchmark? How do retail and
institutions diverge? How should other NMS changes be sequenced?

### Uyeda

SEC site downloads of structured data have risen; some of that is
probably AI. Rule 611 has shaped equity markets for two decades; the
panel is about investor effects of rescinding the trade-through
prohibition. Closing remarks are a 9/11 anniversary note, not a market-
structure holding.

### What the posted AI decks actually say

Julie Marlowe (Assistant Director, Office of Data Standards and
Innovation, DERA), in her official capacity, not speaking for the
Commission: machine-readable data (US GAAP taxonomy, Inline XBRL) is
the context layer that makes AI accurate. Filers define their data.
Use cases named: tagging vendors drafting narratives from tables;
audit firms hunting anomalies; aggregators; the SEC AI Task Force.
Staff quality reminders: scaling errors, stale tags, custom-tag
abuse. An example table of FY 2025 R&D tagged amounts is a taxonomy
demo, not a new Commission ranking.

Campbell Pryde (XBRL US): retail is at a cost disadvantage to
institutions; LLM costs are currently rising as funders recoup;
unstructured PDFs/HTML tokenize badly; structured XBRL gives the model
the same meaning every time. That is a vendor/standards argument, not
a Commission finding.

Gregory Landegger (BitDigest) had no posted deck at cutoff.

**State:** the Sept. 10 AI panel is about the **information-production
pipeline** (how filings are tagged, filed, and machine-read). It is
not a reopening of the December 2025 operations-disclosure
recommendation, and it is not an AI-in-trading-agents rule.

**State:** the NMS panel is investor-facing comment on a **live
proposal** to rescind the trade-through rule. Panelist claims on that
video are not verified here because no official transcript or minutes
exist and auto-captions were not retrieved.

## 4. June 4, 2026 — two adopted recs, still advice

Minutes are not on the committee page. The recommendations page lists
both as adopted, so the votes occurred. Atkins missed the morning and
spoke in the afternoon.

**Quarterly vs. semiannual reporting.** The Commission’s May 5, 2026
proposal (File S7-2026-15) would replace mandatory 10-Qs with a
semiannual Form 10-S, leaving quarterly reports optional. The IAC,
after the March disclosure-reform panel, recommends **keeping the
quarterly mandate**. Rationale in the rec: 10-Q cadence is structural
to price formation, governance, and monitoring; short-termism and cost
arguments do not, in the Committee’s view, justify dropping it;
voluntary quarterly reporting by some issuers would split the
information set. This is a direct disagreement with a live Commission
proposal. It is not a veto.

**Fund proxy voting.** After the March panel (Invesco, Hennessy, ICI,
CFA, Dechert), the rec describes a system that still needs a 1940 Act
majority for advisory contracts, fundamental policies, and many
mergers, while retail participation and broker discretionary voting
have collapsed. ICI figures cited in the rec: 145 campaigns 2012–2019
cost $373 million; since 2020, $675 million to $1.14 billion, with
single campaigns above $100 million. Failures in a 2025 ICI survey
were quorum failures, not “shareholders voted no.” Near-term ask:
permit opt-in retail standing-voting programs on the model of the
Exxon Mobil staff no-action letter (Sept. 15, 2025). That is a request
for staff/Commission action, not the action.

**Passive voting panel** (Copland moderating; Fisch, SIFMA, activists,
academics): Atkins’s afternoon remarks treat adviser proxy voting as a
fiduciary-duty problem and name proxy-advisor influence as a
leadership priority. No recommendation was scheduled on that panel.

**Private-market confusion panel:** continues the Sept. 18, 2025 rec
(registered funds as the preferred retail path; sophistication-not-
wealth if direct access expands; valuation and liquidity disclosure).
June 4 added FINRA advertising review and gating/fee/valuation
confusion. No new rec that day on this topic.

## 5. December 4, 2025 — the tokenization hearing before the rec

The afternoon panel is the industry map the March rec sits on: Coinbase,
BlackRock, Robinhood, Nasdaq, Citadel Securities, Galaxy. Minutes
record that it happened. Working captions now preserve the discussion
for navigation; quote-check the webcast before using a sentence. The
design language is in §6.

Same meeting: AI operations-disclosure rec adopted 14–2–2. Gulliver’s
dissent: Atkins had just said (Dec. 2, 2025) he wants **less** issuer
disclosure; the rec asks for an AI definition, board-oversight
disclosure, and material operations/customer-impact line items;
Gulliver called that burden, boilerplate, and a reason not to go
public. Crenshaw was still a commissioner that morning. Firvida closed
out as Investor Advocate.

## 6. What the discussion actually said (working captions)

Working transcripts exist for all eight webcast parts under
`Transcripts/`. No speaker diarization. Captions mangle names
(`tokenization` → `tokalization`, `wrapper` → `rapper`, `Peirce` →
`Purse`). The sentences below are **locators**. Confirm against the
video before quoting.

### December 4, 2025 afternoon — three issuance/trading models on the table

Moderators split the sitting: issuance, then trading, then settlement
(`PART2` ~00:04:44–00:04:53). That is the grammar the March rec later
wrote down.

**Nasdaq (Chuck Mack)** described a **first step that keeps DTC**:
member firms would trade tokenized equity on Nasdaq; clearing and
settlement would still leverage DTC; tokenized shares would keep the
same CUSIP, rights, and execution rules as today’s shares, including
NMS price discovery, transparency, and best execution
(`PART2` ~00:08:42–00:09:31). He called it a multi-step evolution, not
a replacement of the national market system. He pointed to a Nasdaq
proposal submitted that September. A proposal is not an approved SRO
rule.

**Robinhood (Coy Garrison)** split **native on-chain issuance** from
the **wrapper**. Native: a tokenized book-entry security is still a
security; issuers face a chicken-and-egg because secondary-trading
infrastructure is immature; state corporate law may or may not let the
issuer keep the stock ledger on chain; he asked the SEC to confirm net-
capital treatment and that blockchain consensus participants are not
clearing agencies or transfer agents (`PART2` ~00:14:37–00:16:17).
Wrapper: a third party custodies traditional shares at a broker and
issues tokens; rights passed through may be the full bundle or only
some (e.g. dividends); offered to U.S. persons, those tokens are
securities or security-based swaps depending on facts
(`PART2` ~00:16:33–00:17:00). He said Robinhood already uses a wrapper
**in Europe**, not for U.S. persons, as a derivative contract giving
economic exposure to U.S. stocks (`PART2` ~00:17:31–00:17:58). He also
named 24/7 trading, programmability for KYC/AML and corporate actions,
fractionalization, and accredited-investor reform as the payoff list
(`PART2` ~00:12:51–00:13:58). That list is advocacy, not a rule.

**AMM as code, not a firm.** In the trading block, a panelist (caption
does not reliably name them) defined an AMM as Uniswap-style
**unchanging pool software**: not an entity running an algorithm; any
person can make or take against predefined rules; new features mean a
new deployment, not an edit (`PART2` ~01:21:04–01:22:16). That
sentence is why Release 34-106402’s exchange-definition exemption for
a Tokenized Securities Venue later matters. The IAC rec still wanted
regulated intermediaries. The order later exempts a qualifying TSV from
the *definition of exchange*. Those are the two clocks.

**Limited exemption as a learning device.** Near the end, a panelist
argued for a **limited innovation exemption** so the market can figure
settlement windows out instead of the Commission “dictating down
rulemaking” from an ivory tower; they analogized Reg ATS and the
decade it took DTC to hold most certificates
(`PART2` ~01:51:09–01:51:40). The March rec accepted a limited/narrow
exemption **or** rule-by-rule, with notice and comment, and rejected a
blanket off-switch. Citadel-adjacent remarks in the same sitting
flagged two Apple-stock settlement versions as extra complexity
(`PART2` ~01:50:47–01:51:02).

### September 10, 2026 afternoon — Rule 611 is the NMS fight, not the TSV

The panel is about rescinding the trade-through rule and the locked/
crossed prohibition in the **existing** NMS, not about tokenized AMMs.
CII’s Jeff Mahoney (caption-aligned with the agenda) said Rule 611
**should not be rescinded as proposed**; agent brokers have rebate-
routing conflicts; best execution is more effective when it can be
measured and is enforced (`PART2` ~00:21:42–00:23:07). Other voices
tied 611 to U.S. fragmentation and asked what replaces the NBBO if 611
dies (`PART2` ~00:15:16–00:19:26). Atkins’s written remarks remain the
authority for *his* “policy misstep” line. The panel is comment on a
live proposal.

### What this does not do

Working captions do not create minutes for June 4 or September 10.
They do not identify every speaker. They do not make Nasdaq’s
DTC-preserving model, Robinhood’s European wrapper, or an AMM pool
into an operating U.S. market.

## Clocks going forward

| Clock | Next object | Why it matters |
|---|---|---|
| Sept. 10 minutes / any official transcript | IAC page | only then is the NMS and AI *discussion* an official text |
| File 4-927 comments on the Innovation Exemption | SEC docket | tests whether the Commission treats the order as the start of a comment process, as the IAC asked, or as finished permission |
| File S7-2026-15 quarterly-reporting proposal | final, withdrawal, or silence | IAC is on the opposite side of a live proposal |
| Rule 611 / 610(e) proposal | final rescission or not | Atkins’s long-standing position; IAC panel was comment, not the vote |
| 24-hour trading roundtable follow-through | any TM proposal, SRO rule, or DTCC notice | adjacent to IAC 24/7 remarks; not an IAC product |
| Transfer-agent modernization proposal | comment deadline after FR publication | IAC rec’s ownership-record and shareholder-notice problems land here |
| Dec. 3, 2026 IAC meeting | agenda | next advice clock; virtual |
| Investor Advocate appointment | Commission announcement | statutory IAC seat is empty |
| Peirce departure | White House / Commission personnel object | her Sept. 10 “lame duck” line is a statement, not the personnel action |

## Immediate return gates

1. Capture Sept. 10 and June 4 minutes when posted; they are the vote
   and attendance authority those meetings still lack.
2. If an official or corrected transcript appears, it replaces any later
   caption capture as quotation authority for the discussion.
3. Join File 4-927 comment letters, especially any that cite the March
   IAC rec, to the exemption order without treating a comment as a
   Commission reply.
4. Watch File S7-2026-15 and the 611 proposal as separate rule clocks.
5. Do not scrape the webcasts into a fake transcript. If a later pass
   needs the Sept. 10 NMS discussion, watch the official video and
   quote-check.

## Source links

- [IAC home](https://www.sec.gov/about/advisory-committees/investor-advisory-committee)
- [Sept. 10, 2026 event](https://www.sec.gov/newsroom/meetings-events/iac091026)
- [Sept. 10 agenda](https://www.sec.gov/about/advisory-committees/investor-advisory-committee/iac091026-agenda)
- [Atkins Sept. 10 remarks](https://www.sec.gov/newsroom/speeches-statements/atkins-remarks-iac-091026)
- [Peirce Sept. 10 remarks](https://www.sec.gov/newsroom/speeches-statements/peirce-remarks-iac-091026)
- [Uyeda Sept. 10 remarks](https://www.sec.gov/newsroom/speeches-statements/uyeda-remarks-iac-091026)
- [Tokenization recommendation](https://www.sec.gov/files/recommendation-tokenization-equity-securities.pdf)
- [March 12, 2026 minutes](https://www.sec.gov/files/iac-031226-minutes.pdf)
- Release 34-106402 package
