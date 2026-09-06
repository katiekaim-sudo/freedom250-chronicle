> Source created: 2026-07-10

# Reading the Charter — SEC

Every citation below points to a section actually captured verbatim in this folder. Where the vault's own Entity Theory dataset (`entity_founding_dates.json`) has a gap, it's flagged.

## 1. Immunities & liability shields

None captured. The Exchange Act gives the SEC investigative and enforcement teeth (§21), not a liability shield for itself — this is not an IMF-style "immune from suit" creature. §21(h)(7)(A)-(C), by contrast, actually EXPOSES the Commission to civil penalties, injunctive relief, and even employee discipline referrals to the Office of Personnel Management if it abuses its bank-records subpoena power. The SEC can be sued and disciplined for overreach in ways a true immune international body cannot.

## 2. Tax exemptions

Not addressed in the sections captured. The Exchange Act doesn't grant the Commission itself a tax exemption (it's a federal agency, not a separately chartered corporation like the Fed banks) — nothing to report here from this material.

## 3. Who appoints, who removes, and for what cause

**§4(a):** five commissioners "appointed by the President by and with the advice and consent of the Senate," five-year terms, staggered so no President seats a full board in one term, "not more than three... of the same political party." No removal-for-cause language appears anywhere in the captured text of §4 — the 1934 Act is silent on removal, which is the historically load-bearing silence: *Humphrey's Executor v. United States* (1935, not captured here — outside statutory text) read that silence as an implied for-cause protection for FTC-style commissioners, and the SEC has always been assumed to sit in the same bucket. The statute itself grants no explicit removal protection; the protection, such as it is, is judge-made and currently contested at the Supreme Court level (outside this charter's text, flagged for awareness only).

**§4(g)/(i):** the Investor Advocate and the Advocate for Small Business Capital Formation are Commission/Chairman appointees with built-in independence-from-the-Commission features — reports go straight to Congress "without any prior review or comment from the Commission... or the Office of Management and Budget" (§4(g)(6)(iii)). Small internal watchdogs the Commission itself cannot edit before they reach the Hill.

## 4. Money: self-funding vs. appropriations — THE FAULT LINE

This is the section that actually answers the "who holds the leash" question, and the honest answer is: **both** Congress and the SEC hold pieces of it, wired together in an unusual loop.

- **§31 (§78ee) is the mechanism.** The Commission does NOT get to spend whatever it collects. §31(a): fees are "designed to recover the costs to the Government of the annual appropriation to the Commission by Congress" — the fee target is set BY the appropriation, not the other way around.
- **§31(i)(1)(A):** fees are "deposited and credited as offsetting collections to the account providing appropriations to the Commission" — money in, but routed back to Congress's own appropriations account, not a freestanding SEC fund.
- **§31(i)(1)(B):** fees "shall not be collected for any fiscal year except to the extent provided in advance in appropriation Acts" — Congress can zero this out by not appropriating.
- **§31(j):** twice a year the Commission literally recalculates its own transaction-fee rate (the per-$1,000,000 charge on every stock trade in America) to hit whatever dollar figure Congress appropriated — an automatic dial, not a discretionary SEC decision about how much money it wants.
- **§31(k):** if Congress fails to pass an appropriation on time, the SEC keeps collecting at the OLD rate as a bridge — so a government shutdown doesn't zero out SEC funding, it just freezes the rate.
- **§4(i) — REPEALED 2025** (Pub. L. 119-21 §30003(a), the reconciliation-bill sweep dated July 4, 2025): struck the SEC Reserve Fund, a standalone reserve the Commission had held outside the annual appropriations cycle since Dodd-Frank §991(e)(1) created it in 2010. Fifteen years of a genuine off-books cushion, killed in one line of a 2025 reconciliation act. Whatever margin of true independence that Reserve Fund gave the Commission is now gone; every dollar again has to clear the annual appropriations gate.

**The contrast that matters (Entity Theory read requested it explicitly):**

- **CFPB** (Dodd-Frank, 12 U.S.C. §5497): funded by a straight percentage-of-Federal-Reserve-System-expenses TRANSFER, capped by formula, explicitly declared NOT to be "Government funds" once transferred, and walled off from the congressional appropriations process almost entirely — the single most insulated funding structure in the federal government. Congress doesn't touch the CFPB's money at all in ordinary years.
- **CFTC** (7 U.S.C., not captured in this folder but confirmed by the vault's existing CFTC extraction note): runs on **bare appropriations** — no meaningful self-funding mechanism, no fee-offsetting-collections loop. The CFTC is the most Congress-dependent of the three.
- **SEC** sits in the middle: it LOOKS self-funded (the fee mechanism is real, sophisticated, and automatically recalibrating) but the money still flows through — and is capped by — the annual appropriations act. It's self-funding on a leash Congress holds at both ends: Congress sets the appropriation number, the SEC's fee formula is legally required to chase that number, and the money lands back in the same appropriations account it came from. This is NOT financial independence in the CFPB sense. It's a self-billing mechanism for a bill Congress still writes.

**Entity Theory dataset gap:** `entity_founding_dates.json` currently has `"own": null` for SEC — no self-funding flag set. Based on §31 captured here, that field should read something like `"own": "fee-offset, capped by annual appropriation (not free-standing)"` — distinct from CFPB's `"own": "Fed-transfer, appropriations-independent"` and CFTC's presumed `"own": null` (genuinely appropriated). Flagging for the dataset maintainer; not editing the JSON from this note.

## 5. Audit & disclosure carve-outs

**§4(j):** all public data the Commission publishes under the securities laws and Dodd-Frank must be an "open Government data asset," "freely available for download," "human-readable," and "accessible via application programming interface where appropriate" — a transparency mandate running the other direction (SEC must disclose to the public), not a carve-out shielding the SEC from disclosure.

**§21(h)(6), struck 2015** (Pub. L. 114-113 §708): until 2015 the Commission had to compile an "annual tabulation" for Congress of how often it used each bank-secrecy-bypass power under §21(h)(2) — repealed. A transparency requirement on the Commission's OWN surveillance-adjacent power, removed, not added.

No GAO-exemption or FOIA-carve-out language appears in the sections captured here.

## 6. Amendment & withdrawal clauses

Not applicable in the international-charter sense (there's no "withdrawal" from a domestic regulatory agency) — but the amendment TRAIL itself is instructive and captured in each verbatim file's amendment-history summary: §4 has been amended at least fifteen times since 1934 (most recently July 4, 2025); §31 rewritten wholesale in 1996, 2002, and 2010; §36 added whole-cloth in 1996 and expanded in 2010; §21 amended at least twelve times, most recently 2021. Congress treats this charter as a living document it edits on a roughly-annual cadence — nothing here is static 1934 text still governing 2026 practice.

## 7. Emergency powers

**§21(h)(2)(A)-(D)** is the closest thing to an emergency-powers clause in the material captured: the Commission can get an EX PARTE court order for a customer's bank records, with NO advance notice to the customer, bypassing the Right to Financial Privacy Act's normal notice requirement, if it can show a district judge (in a sealed, in camera proceeding) a risk of flight from prosecution, evidence destruction, asset flight overseas, "improper conversion of investor assets," fraud/loss that "remains uncorrected" or "substantially uncompensated," or conduct that could "endanger the stability of any financial or investment intermediary." That last clause — systemic-risk language sitting inside a subpoena-secrecy provision from 1980 — is decades ahead of its time; it's essentially a mini bank-run/contagion trigger baked into an investigative-powers subsection, forty years before "systemic risk" became Dodd-Frank vocabulary.

## 8. The definitions section

**§3(a)(10) "security"** is the load-bearing one: the definition is a long enumerated list (note, stock, bond, investment contract, "any instrument commonly known as a 'security'"...) plus a catch-all — "investment contract" is the word doing the most work, since that's the term courts have stretched (via the *Howey* test, not captured here — case law, not statute) to reach everything from land-sale schemes to, in ongoing litigation the vault already tracks, crypto tokens. The statute itself doesn't define "investment contract" further — it just lists it as one more type of security and lets the courts fill in the boundary. That undefined term is the entire jurisdictional battlefield for whether the SEC can regulate a given asset.

**§3(a)(4)/(5) "broker"/"dealer"** definitions are broad on their face ("any person engaged in the business of effecting transactions... for the account of others" / "buying and selling securities... for such person's own account") but are immediately hollowed out by an enormous bank-exception apparatus (eleven separate carve-out categories for banks under "broker" alone, added by Gramm-Leach-Bliley in 1999) — the definition expands to cover banks, then a wall of exceptions pulls most ordinary bank activity back out. Classic pattern: broad statutory language, narrow regulatory reality, negotiated industry-by-industry.

**§3(a)(1) "exchange"** is function-based, not form-based — "any organization... which constitutes, maintains, or provides a market place or facilities... for otherwise performing... the functions commonly performed by a stock exchange" — meaning the SEC's jurisdiction over what counts as an "exchange" turns on what the thing DOES, not what it calls itself. That's the same functional-test structure that later let the SEC argue crypto trading platforms could be "exchanges" without ever being chartered as one.

## 9. Succession/perpetuity & dissolution

Not addressed in the captured sections — the SEC has no stated corporate life span or dissolution clause; it exists as an ongoing executive-branch commission, dissolvable only by a later Act of Congress (not addressed anywhere in this charter's text).

## 10. Anything strange

**§36 (§78mm), added 1996 out of nowhere:** the SEC can exempt "any person, security, or transaction... from any provision" of the ENTIRE Exchange Act, so long as it finds the exemption "necessary or appropriate in the public interest" and "consistent with the protection of investors" — and under §36(a)(2) the Commission can refuse to even hear an exemption request "in its sole discretion." That is about as close to a statutory blank check as a regulatory agency gets: Congress handed the SEC the power to waive its own rulebook, wholesale, subject only to a standard the SEC itself applies. The only hard boundary (§36(b)) walls off the government-securities rules; the only OTHER boundary (§36(c), added 2010) walls off the new Dodd-Frank swaps title unless a specific provision reopens it. Two carve-outs guarding one otherwise-total discretion.

**§4(i), repealed July 4, 2025:** a fifteen-year-old SEC Reserve Fund — real, standalone, off-annual-cycle money — killed in a reconciliation bill on Independence Day. The date is almost too on-the-nose for a vault built around a "Freedom 250" framing: 2025's Independence Day gutted a piece of SEC financial independence.

## Layer map

- **1934 — Securities Exchange Act, original enactment (ch. 404, 48 Stat. 881 et seq.):** creates the Commission (§4), the master definitions (§3), and the investigate/subpoena/injunct enforcement core (§21). Funding at this point ran through Treasury general revenue, not offsetting collections (see §31's pre-1996 text, condensed in that file's amendment history).
- **1975 — Securities Acts Amendments (Pub. L. 94-29):** extends §31 transaction fees to over-the-counter trades in listed securities (not just exchange-floor trades) and extends §21 enforcement reach to clearing agencies and their participants — the national-market-system build-out era.
- **1996 — National Securities Markets Improvement Act (NSMIA, Pub. L. 104-290):** adds §36 whole-cloth (the blank-check general exemptive authority) and rewrites §31 to add the fee-adjustment/lapse-of-appropriation/baseline-estimate machinery that turns the SEC into a self-calibrating fee engine.
- **2002 — Sarbanes-Oxley-adjacent legislation (Pub. L. 107-123, 107-204):** §31 fee cuts and restructure into the current offsetting-collections model; §21 rewired throughout to bring the newly created Public Company Accounting Oversight Board (PCAOB — Sarbanes-Oxley's own creature, chartered the same year, not itself captured in this folder) into the SEC's investigate/injunct/mandamus/SRO-deference architecture as if it were just another self-regulatory organization.
- **2010 — Dodd-Frank Wall Street Reform Act (Pub. L. 111-203):** the biggest single expansion — adds §4(g) Office of the Investor Advocate, §4(h) dedicated examiner staffs, §4(i) the (now-repealed) SEC Reserve Fund; rewrites §31(a) to the current "recover the cost of the appropriation" formula and adds the budget-transmittal-to-Congress requirement (§31(m)); adds §36(c), carving swaps/security-based swaps out of the general exemptive grant; expands §21's enforcement reach (former associated persons, former clearing-agency participants) and adds the disgorgement cross-reference to the whistleblower Fair Fund (§78u-6).
- **2015-2021 — cleanup and codification (Pub. L. 114-113, 114-284, 115-141, 116-283, 117-263):** strikes the §21(h)(6) annual bank-secrecy-power tabulation (2015); adds §4(j) open-data mandate (2016); adds hurricane/natural-disaster language to the small-business advocate mandate (2018); most significantly, **2021's Pub. L. 116-283** finally writes an express statutory disgorgement power and 5-/10-year limitations periods into §21(d)(7)-(9) — direct legislative response to the Supreme Court narrowing the SEC's judge-made disgorgement remedy in *Kokesh* (2017) and *Liu* (2020).
- **2025 — reconciliation-bill sweep (Pub. L. 119-21 §30003(a), signed July 4, 2025):** strikes the SEC Reserve Fund from §4. The most recent amendment captured, and a funding contraction rather than an expansion — worth watching for whether it's the leading edge of a broader push to tighten the SEC's fiscal leash.

## Entity Theory read

The SEC is a committee-creature wearing an independence costume it can't fully afford. Five commissioners, staggered terms, one party can't dominate the board — on paper, insulated the way the CFTC and FTC are insulated, no President seats a full board in a single term. But the money tells a different story than the org chart. Unlike the CFPB, which Congress deliberately built to never need Congress again, the SEC's self-funding is a leash disguised as independence: the fee formula is real and clever (it recalibrates itself twice a year to a moving target), but that target is set by the same appropriations bill Congress passes for every other agency, and the money is credited right back into that same appropriations account. Whoever writes the SEC's line item still writes the SEC's real budget — the fee mechanism just means industry pays the bill instead of the general taxpayer, not that the SEC escapes the bill. Then 2025 took away the one piece of genuine cushion — the Reserve Fund — that let the SEC hold money outside that yearly cycle at all. Does this survive a change of control? Yes, easily — the five-seat structure and the fee-offset machinery are built to be dominated by NO single administration; the FIVE-YEAR SEC that outlasts any one President is the point. What doesn't survive unchanged is the SEC's fiscal slack: that's a dial Congress can and does turn, most recently in 2025, and it's the mechanism to watch, not the org chart.

## Sources

- 15 U.S.C. §78d (Securities Exchange Act §4) — Cornell LII, https://www.law.cornell.edu/uscode/text/15/78d — retrieved 2026-07-10.
- 15 U.S.C. §78ee (Securities Exchange Act §31) — Cornell LII, https://www.law.cornell.edu/uscode/text/15/78ee — retrieved 2026-07-10.
- 15 U.S.C. §78mm (Securities Exchange Act §36) — Cornell LII, https://www.law.cornell.edu/uscode/text/15/78mm — retrieved 2026-07-10.
- 15 U.S.C. §78u (Securities Exchange Act §21) — Cornell LII, https://www.law.cornell.edu/uscode/text/15/78u — retrieved 2026-07-10 (partial capture — see verbatim file's capture note for elisions).
- 15 U.S.C. §78c(a) (Securities Exchange Act §3(a), definitions) — Cornell LII, https://www.law.cornell.edu/uscode/text/15/78c — retrieved 2026-07-10 (partial capture — four definitions only, see verbatim file's capture note).
- `04 - Synthesis/Entity Theory/entity_founding_dates.json` (this vault) — cross-checked for SEC classification and self-funding flag (currently `null` — flagged above for maintainer follow-up).
- `04 - Synthesis/Entity Theory/Federal Group — Consolidation Map.html` (this vault) — SEC classified as `cat: "indep"`.
- CFPB and CFTC "Reading the Charter" notes (this vault, `05 - Sources/Charters/CFPB/` and `05 - Sources/Charters/CFTC/`) — used as the funding-model comparators cited in §4 above.

> [!graph]- Graph links (6 notes — auto-generated, do not edit)
> 1934 - Securities Exchange Act §21 — 15 U.S.C. §78u (verbatim, partial)
> 1934 - Securities Exchange Act §3(a) — 15 U.S.C. §78c (definitions, verbatim, partial)
> 1934 - Securities Exchange Act §31 — 15 U.S.C. §78ee (verbatim)
> 1934 - Securities Exchange Act §4 — 15 U.S.C. §78d (verbatim)
> 1996 - Securities Exchange Act §36 — 15 U.S.C. §78mm (verbatim)
> [The Entity Theory — Working Note](../sources/the-entity-theory-working-note-e6145374fc35.html)
