# Reading the Charter — FHFA

## 0. Housekeeping — what got captured, what didn't

Full verbatim source is in the companion file in this folder: `2008 - Housing and Economic Recovery Act — FHFA provisions (current codified) (verbatim).md`.

- **§4511 (Establishment)** — captured FULL.
- **§4512 (Director)** — captured FULL.
- **§4513 (Duties and authorities of Director)** — captured PARTIAL. Only a trailing fragment (Fed Reserve consultation + suit/process provisions) could be pulled before the web-fetch tool hit a hard rate limit for the rest of this session (confirmed tool-wide, not source-specific, by testing an unrelated domain — every retry, on every host, returned HTTP 429). **The opening Duties subsection(s) of §4513 are NOT captured** — this is where general regulatory-authority language and (per the cross-references found inside §4511(b)(2) and §4512(e)(3), both of which point to "section 4513(d)") a "differences between the enterprises and the Federal Home Loan Banks" subsection (d) live. **The exact assessments/self-funding clause could not be located or verbatim-captured this session** — it may sit in §4513 itself or in the neighboring §4516 ("Assessments"), neither of which finished fetching. This is flagged below wherever it matters and should NOT be treated as confirmed until a follow-up session re-pulls both sections.
- **§4617 (Conservatorship/receivership)** — captured FULL, subsections (a) through (k) — the entire section. No omissions.

Below, every claim is cited to the subsection actually captured. Where the underlying clause was not fetched this session, that is stated plainly instead of guessed.

---

## 1. Immunities & liability shields

The suit/process clause actually captured, from the §4513 fragment: **the Director can be sued (other than for money damages) by a regulated entity**, in the district where the regulated entity sits or in D.C., and can be served under the Federal Rules — but the Director acts "in the Director's own name and through the Director's own attorneys" when enforcing the law. That is a real, if narrow, door into court against the man running the Agency — narrower than the total lockout you'd expect. (§4513, fragment captured — exact subsection letter not confirmed, see housekeeping note above.)

The much bigger shield lives in §4617, the receivership/conservatorship statute:

- **§4617(a)(7)** — "the Agency shall not be subject to the direction or supervision of any other agency of the United States or any State in the exercise of the rights, powers, and privileges of the Agency" when acting as conservator/receiver. No other federal agency can tell it what to do.
- **§4617(b)(11)(C)** — "No attachment or execution may issue by any court upon assets in the possession of the receiver, or upon the charter, of a regulated entity for which the Agency has been appointed receiver." Nobody can grab the assets by court order while FHFA holds them.
- **§4617(b)(11)(D)** — "Limitation on judicial review — Except as otherwise provided in this subsection, no court shall have jurisdiction over (i) any claim or action for payment from, or any action seeking a determination of rights with respect to, the assets or charter of any regulated entity for which the Agency has been appointed receiver; or (ii) any claim relating to any act or omission of such regulated entity or the Agency as receiver." Courts are locked out of the whole receivership except the narrow claims process Congress built in.
- **§4617(b)(2)(K)(i)** — appointing the Agency as receiver "terminate[s] all rights and claims that the stockholders and creditors" had against the entity or the Agency arising from their status as stockholders/creditors — except the narrow payment rights Congress carved out.
- **§4617(g)** — directors and officers CAN be personally sued for gross negligence or worse by the Agency, but the Agency itself faces no equivalent exposure.

## 2. Tax exemptions

- **§4617(i)(5)** — a limited-life regulated entity (the bridge-bank the Agency can spin up in receivership) "shall be exempt from all taxation now or hereafter imposed by the United States, by any territory, dependency, or possession thereof, or by any State, county, municipality, or local taxing authority." Total exemption, federal and state and local, franchise/property/income all covered.
- **§4617(j)(2)** — the Agency itself, "including its franchise, its capital, reserves, and surplus, and its income, shall be exempt from all taxation imposed by any State, county, municipality, or local taxing authority," with one carve-out: real property it holds IS subject to state/local property tax like anyone else's real property.
- **§4617(j)(3)** — Agency property can't be levied, attached, garnished, foreclosed, or sold without the Agency's own consent; no involuntary lien can attach.
- **§4617(j)(4)** — the Agency owes no penalties or fines, including for late real-property, personal-property, probate, or recording taxes/fees.

No direct capture yet of any tax-exemption clause tied to the Agency's own bonds/obligations or staff salaries — not found in the sections captured this session.

## 3. Who appoints, who removes, for what cause — the control map

**§4512(b)(1)** — the Director is appointed "by the President, by and with the advice and consent of the Senate," from citizens with a demonstrated understanding of financial management/oversight and of capital markets/mortgage securities/housing finance.

**§4512(b)(2)** — the term is 5 years, "unless removed before the end of such term for cause by the President." That's the for-cause removal protection — the same structural design that got Fannie/Freddie's and the CFPB's single-director-agency structures dragged into the Supreme Court (Seila Law, then Collins v. Yellen specifically about THIS agency in 2021). Collins v. Yellen held the for-cause removal restriction on FHFA's single Director was an unconstitutional limit on presidential removal power under the separation-of-powers logic of Seila Law — but the Court left the Agency's actions (the conservatorship itself) intact rather than voiding them, because the structural defect didn't cause the specific harm alleged. The statute as codified STILL reads "for cause" — Congress has not amended the text; it is the removal restriction's enforceability, not the words, that the courts gutted. Cornell's own editorial note flags this directly: "For information regarding the constitutionality of provisions of subsection (b)(2) of this section, see the Table of Laws Held Unconstitutional in Whole or in Part by the Supreme Court" (editorial note under §4512, captured verbatim in the companion file).

**§4512(f)** — Acting Director: on death, resignation, sickness, or absence of the Director, the President designates one of the three Deputy Directors (Enterprise Regulation, FHLBank Regulation, or Housing Mission and Goals) to act until the Director returns or a successor is confirmed.

**§4512(g)** — conflict-of-interest wall: the Director and Deputy Directors may not hold a financial interest in, hold a job at, or have served as an officer/director of any regulated entity in the 3 years before appointment.

Not yet captured: appointment/removal provisions for FHFA staff generally, or any Board (FHFA has no multi-member board — it is a single-Director agency, which is precisely the structural fact Collins v. Yellen turned on).

## 4. Money — self-funding vs. appropriations

**NOT CONFIRMED THIS SESSION.** The exact assessments clause was not fetched before the tool-wide rate limit hit (see housekeeping note). Do not treat "FHFA is funded by assessments on Fannie, Freddie, and the FHLBanks, not congressional appropriations" as sourced yet — it needs a verbatim pull of §4513 (opening subsections) and/or §4516 "Assessments" before it can carry a citation. Flagging for immediate follow-up.

## 5. Audit & disclosure carve-outs

Not captured this session in the sections pulled. §4617(b)(14) does require the Agency, as conservator/receiver, to "make an annual accounting or report available to the Board, the Comptroller General of the United States, the Committee on Banking, Housing, and Urban Affairs of the Senate, and the Committee on Financial Services of the House of Representatives" and to make that report available "upon request to any shareholder of a regulated entity or any member of the public" (§4617(b)(14)(B)–(C)) — so receivership accounting is public-facing by statute. No FOIA-specific or GAO-general-audit-exemption clause located in the sections captured; would need §4517/§4526-range sections not pulled this session.

## 6. Amendment & withdrawal clauses

Not located in the sections captured this session (would typically be in HERA's general amendment provisions, not in the codified 4511–4617 range pulled here).

## 7. Emergency powers

The whole of §4617 IS the emergency-powers architecture — conservatorship/receivership is FHFA's emergency toolkit, triggered on the grounds listed in §4617(a)(3)(A)–(L) (assets less than obligations, dissipation, unsafe/unsound condition, cease-and-desist violations, concealment, inability to pay, ruinous losses, undercapitalization tiers, critical undercapitalization, money-laundering conviction) or mandatorily under §4617(a)(4) once a 60-day insolvency/nonpayment test is met. Once triggered, §4617(b) hands the Agency total operational control (successor to all rights/titles/powers of the entity and its officers/directors/stockholders, §4617(b)(2)(A)) with the court-stripping backstop at (f) — see §10 below.

## 8. Definitions section — expansions beyond plain reading

Not directly captured (the general chapter-wide definitions section, §4502, was cross-referenced repeatedly — e.g. §4513 fragment references "regulated entities (as such term is defined in section 4502 of this title)" — but §4502 itself was not fetched this session). One expansion IS visible inside §4617(d)(8)(D): the term "qualified financial contract" is defined enormously broadly — covering securities contracts, commodity contracts, forward contracts, repurchase agreements, swap agreements, "and any similar agreement that the Agency determines by regulation, resolution, or order to be a qualified financial contract" (§4617(d)(8)(D)(i)) — a self-expanding definition where the Agency itself gets to grow the category. Each sub-definition (securities contract, commodity contract, forward contract, repurchase agreement, swap agreement) further includes catch-alls like "any other agreement or transaction that is similar to any agreement or transaction referred to in this clause" — definitional elastic written directly into the statute.

## 9. Succession/perpetuity & dissolution

- **§4617(a)(4)(D)** — appointing the Agency as RECEIVER "immediately terminate[s] any conservatorship" already in place — receivership swallows conservatorship whole.
- **§4617(k)** — "In no case may the receiver appointed pursuant to this section revoke, annul, or terminate the charter of an enterprise." The receiver can gut the company but cannot kill the charter itself — the corporate shell survives even total operational takeover.
- **§4617(i)** — the "limited-life regulated entity" (bridge entity) mechanism: on Fannie Mae receivership, the bridge entity automatically succeeds to the Fannie Mae Charter Act itself (§4617(i)(2)(A)(i)); same for Freddie Mac under its Charter Act (§4617(i)(2)(A)(ii)). The bridge entity is capped at a 2-year life, extendable by the Director for three additional 1-year periods (§4617(i)(6)(A)-(B)) — so up to 5 years total before Congress-level intervention would be needed. The bridge entity is explicitly declared NOT a federal agency or instrumentality (§4617(i)(10)(A)) — a deliberate wall between the government's fingerprints and the entity's legal status.

## 10. Anything strange — the court-stripping clause

This is the one. **12 U.S.C. §4617(f), captured in full, word for word, from govinfo.gov (U.S. Code 2023 Edition):**

> **"(f) Limitation on court action**
>
> **Except as provided in this section or at the request of the Director, no court may take any action to restrain or affect the exercise of powers or functions of the Agency as a conservator or a receiver."**

Read that again slowly: no court, anywhere, can restrain or even AFFECT what the Agency does as conservator or receiver — unless the statute itself carves out an exception, or unless the Director asks the court to act. The only way into court is the door FHFA itself chooses to leave open. This single sentence is why the 2008 Fannie/Freddie conservatorship has survived over a decade and a half of shareholder litigation (Perry Capital, Collins v. Yellen, and dozens of others) essentially untouched at its core — plaintiffs have chipped at the edges (removal power in Collins) but never gotten a court to unwind the conservatorship itself, because this clause was built to make that structurally almost impossible.

It does not stand alone — it's reinforced by companion provisions in the same section:
- §4617(b)(5)(E) — "No court may review the determination of the Agency ... to disallow a claim" (a separate, narrower court-stripping clause for claims determinations).
- §4617(b)(11)(D) — the "Limitation on judicial review" clause quoted in full above (Section 1), which zeroes out court jurisdiction over claims against receivership assets except the statute's own claims process.
- §4617(b)(11)(C) — no attachment or execution by any court on receivership assets or the charter.

Taken together, §4617 doesn't just give FHFA emergency powers — it insulates the exercise of those powers from the judiciary almost completely, while still preserving narrow statutory review channels (the 30-day "remove yourself as conservator" suit under §4617(a)(5), the claims-determination suit under §4617(b)(6)) that Congress deliberately kept open. It's a fenced garden, not a total lockout — but the fence is built out of the same sentence that reads, on its face, like a total lockout.

---

## Layer map — what HERA changed

The Housing and Economic Recovery Act of 2008 (HERA), Pub. L. 110-289, took three separate, weaker regulators — the Office of Federal Housing Enterprise Oversight (OFHEO, which sat inside HUD and only watched Fannie/Freddie's safety and soundness), the Federal Housing Finance Board (which oversaw the Federal Home Loan Banks), and HUD's own separate "GSE mission" oversight function — and welded them into one independent agency with one Director and real receivership teeth. FHFA didn't exist before July 30, 2008. Within about six weeks of that welding, on September 6, 2008, the brand-new agency used its brand-new §4617 conservatorship power to seize Fannie Mae and Freddie Mac — the single biggest exercise of the tool in the history of the tool, deployed almost the moment the tool was forged. That is not incidental. The conservatorship power and the entities it would first be used against were created in the same statute, weeks apart from the seizure itself.

## Entity Theory read

This is not a watchdog. It is a lockbox with a court-proof lid, built by Congress in a panic in the summer of 2008 and used on the two biggest mortgage companies on earth six weeks after the ink dried. One man runs it — the Director, hired by the President, fireable "for cause" in name only since the Supreme Court gutted that protection in Collins v. Yellen (2021) without actually freeing Fannie and Freddie from the box. Nobody outside the Agency — not another federal agency, not a state, not a court unless the Agency itself allows it — can touch what it does once it declares conservatorship or receivership. Change of control at the top (a new President installing a new Director) can change WHO holds the leash instantly, but it does not open the box; the box stays locked to the outside world either way. Whether it survives a change of control is really a question about whether the next administration wants to keep Fannie and Freddie in the box or finally let them out — the statute gives the Director total freedom to do either, and gives the courts almost no say in stopping him.

## Source list

- U.S. Code, 2023 Edition, Title 12, Chapter 46, Subchapter II, §4617 — https://www.govinfo.gov/content/pkg/USCODE-2023-title12/html/USCODE-2023-title12-chap46-subchapII-sec4617.htm — retrieved 2026-07-10. Full capture.
- Cornell Legal Information Institute, 12 U.S.C. §4511 — https://www.law.cornell.edu/uscode/text/12/4511 — retrieved 2026-07-10. Full capture.
- Cornell Legal Information Institute, 12 U.S.C. §4512 — https://www.law.cornell.edu/uscode/text/12/4512 — retrieved 2026-07-10. Full capture.
- Cornell Legal Information Institute, 12 U.S.C. §4513 — https://www.law.cornell.edu/uscode/text/12/4513 — retrieved 2026-07-10. PARTIAL capture only (fragment); repeated re-fetch attempts (Cornell, govinfo, uscode.house.gov) all blocked by a session-wide tool rate limit (HTTP 429) confirmed not source-specific.
- 12 U.S.C. §4516 "Assessments" — NOT fetched this session (blocked by the same rate limit); flagged for immediate follow-up to confirm the self-funding/assessments clause.

## Follow-up queue (Katie's call / next session)

1. Re-pull §4513 in full (opening Duties subsections, including subsection (d) referenced by §4511(b)(2) and §4512(e)(3)).
2. Pull §4516 "Assessments" in full — this is very likely where the exact "funded by assessments on the regulated entities, not congressional appropriations" clause lives; do not publish that claim as sourced until this is done.
3. Consider pulling §4502 (chapter-wide definitions) given how many cross-references to it appear in the sections already captured.
4. Consider whether the original HERA enacted text (Pub. L. 110-289, Statutes at Large) should be captured separately per the spec's preference for "organic act as enacted" alongside the current codification — this session captured only the current codified U.S. Code text, not the original 2008 Statutes-at-Large text of HERA itself.

> [!graph]- Graph links (2 notes — auto-generated, do not edit)
> 2008 - Housing and Economic Recovery Act — FHFA provisions (current codified) (verbatim)
> [The Entity Theory — Working Note](../sources/the-entity-theory-working-note-e6145374fc35.html)
