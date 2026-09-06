# Reading the Charter — Ginnie Mae (Government National Mortgage Association)

Motivation, not location. Ginnie Mae is the one member of this batch that isn't hiding the ball — its whole reason for existing is to say, in writing, "the United States will pay." Here's where every claim comes from, chapter and verse.

## 1. Immunities & liability shields

Ginnie Mae can sue and be sued in its own name — but its property can't be touched by the ordinary tools creditors use against everyone else. 12 U.S.C. §1723a (covering both bodies corporate named in §1717(a)(2), i.e. Fannie Mae and Ginnie Mae):

> "in its corporate name, to sue and to be sued, and to complain and to defend, in any court of competent jurisdiction, State or Federal, but no attachment, injunction, or other similar process, mesne or final, shall be issued against the property of the Association or against the Association with respect to its property"

Translation: you can win a judgment against Ginnie Mae, but you cannot attach or enjoin its property to collect it. That's a real, if partial, sovereign-style shield sitting inside an otherwise ordinary "sue and be sued" waiver.

Same section also gives Ginnie Mae a name-monopoly with teeth: no other person or firm may use "Government National Mortgage Association" (or "Federal National Mortgage Association") as its business name, enforceable by injunction plus statutory damages up to $100/day (12 U.S.C. §1723a).

## 2. Tax exemptions

Found and confirmed this session: the **trusts Ginnie Mae administers as trustee** for other federal agencies' obligations (Farmers Home Administration, HUD, VA, Department of Education, Export-Import Bank, SBA — the full list at 12 U.S.C. §1717(c)(2)) carry a flat exemption:

> "The trust or trusts shall be exempt from all taxation." — 12 U.S.C. §1717(c)(2)

Separately, and importantly for the audit/disclosure question below, participations or instruments Ginnie Mae issues under that same subsection get treated as federal-obligation-grade for securities-law purposes (12 U.S.C. §1717(c)(1)) — see §5.

**What I could not confirm this session:** a direct statutory income-tax exemption on the guaranteed mortgage-backed securities themselves (the pass-through MBS retail investors hold), which would likely sit at 12 U.S.C. §1723c. I fetched Cornell LII for §1723c and §1716 (definitions/purposes) four separate times; all four attempts were blocked by a persistent tool-level rate limit (HTTP 429) that did not clear during the session. This is marked as an open gap, not asserted — do not treat GNMA MBS as tax-exempt on the strength of this note; that specific clause needs a follow-up fetch.

## 3. Who appoints, who removes, and for what cause — the control map

This is the one place the assignment brief's assumption needs correcting. Current law does **not** have the HUD Secretary appoint the GNMA President — it has the President of the United States do it, Senate-confirmed. 12 U.S.C. §1723(a):

> "All the powers and duties of the Government National Mortgage Association shall be vested in the Secretary of Housing and Urban Development and the Association shall be administered under the direction of the Secretary. Within the limitations of law, the Secretary shall determine the general policies which shall govern the operations of the Association, and shall have power to adopt, amend, and repeal bylaws governing the performance of the powers and duties granted to or imposed upon it by law. There is hereby established in the Department of Housing and Urban Development the position of President, Government National Mortgage Association, who shall be appointed by the President, by and with the advice and consent of the Senate. The Secretary shall select and effect the appointment of qualified persons to fill the offices of vice president, and such other offices as may be provided for in the bylaws."

So the split is: **policy control** sits with the HUD Secretary (who "shall be administered under the direction of the Secretary," sets "general policies," writes/amends the bylaws); **the top office** (President of GNMA) is a presidential, Senate-confirmed appointment sitting inside HUD; **everyone below that** (VPs, other officers) is Secretary-appointed. This was not always so: per the editorial/amendment note under §1723, the 1968 partition act (Pub. L. 90-448) had the Secretary directly appoint the GNMA President; it was Pub. L. 94-375, §17(a) (1976) that moved the top job to a presidential/Senate-confirmed appointment. No removal-for-cause clause appears anywhere in §1723 — the statute is silent on removal, which for a presidentially-appointed, Senate-confirmed executive-branch officer defaults to at-will removal by the President under ordinary constitutional practice; nothing in the fetched text carves out a "for cause" protection the way some independent agencies get.

## 4. Money: self-funding vs. appropriations

Mixed model, not purely off-budget:

- **Fee-funded guaranty business:** 12 U.S.C. §1721(g)(1) — "The Association shall collect from the issuer a reasonable fee for any guaranty under this subsection and shall make such charges as it may determine to be reasonable for the analysis of any trust or other security arrangement proposed by the issuer." Fee ceilings are capped by statute for FHA/VA-backed 1-4 family pools at 6 basis points (§1721(g)(3)(A)), with other fees set "at a level not more than necessary to create reserves sufficient to meet anticipated claims" (§1721(g)(3)(B)) — i.e., break-even by design, not a profit center.
- **Appropriations backstop for credit subsidy cost:** §1721(g)(2) — "There are authorized to be appropriated to cover the costs (as such term is defined in section 661a of title 2) of guarantees issued under this chapter by the Association such sums as may be necessary" — this ties Ginnie Mae's guaranty program into the Federal Credit Reform Act cost-accounting framework (2 U.S.C. §661a), meaning Congress can (and does, procedurally) appropriate to cover projected subsidy cost even though the guaranty fees are designed to cover it.
- **Treasury borrowing authority for the management/liquidation side:** §1721(b) and (d) let the Association issue obligations — (b) to substitute private financing for Treasury debt (explicitly **not** government-guaranteed: "such obligations... are not guaranteed by the United States and do not constitute a debt or obligation of the United States"), and (d) directly to the Secretary of the Treasury, maturing within 5 years, to fund its liquidating functions.
- Historical annual guaranty-commitment ceilings were set by statute/appropriations act (e.g., "$110,000,000,000 during fiscal year 1996" in §1721(g)(2) as it then read) — the aggregate-amount mechanism still operates via "any funding limitation approved in appropriation Acts."

## 5. Audit & disclosure carve-outs

Found: a securities-law disclosure exemption for the trust instruments Ginnie Mae issues as trustee. 12 U.S.C. §1717(c)(1):

> "Participations or other instruments issued by the Association pursuant to this subsection shall to the same extent as securities which are direct obligations of or obligations guaranteed as to principal or interest by the United States be deemed to be exempt securities within the meaning of laws administered by the Securities and Exchange Commission."

That's a real disclosure/registration carve-out — Ginnie Mae paper is treated like direct Treasury paper for SEC purposes, not like ordinary corporate securities.

**Not located this session:** an explicit GAO-audit exemption or FOIA-status clause specific to Ginnie Mae. I did not find language in §1716b, §1717, §1721, §1723, or §1723a addressing GAO audit scope or FOIA applicability — either it lives in a section not fetched this session (a strong candidate is 31 U.S.C. chapter 91, the Government Corporation Control Act, which §1723a itself points to: "Except as may be otherwise provided in this subchapter, in chapter 91 of title 31, or in other laws specifically applicable to Government corporations...") or it wasn't surfaced by the sections pulled. Flagging as a gap rather than guessing.

## 6. Amendment & withdrawal clauses

No self-amendment clause (Ginnie Mae doesn't get to rewrite its own charter — Congress does, and has, roughly 25 times since 1934 per the public-law string under §1721 alone). But there is a notable **entrenchment-against-implied-repeal** clause, twice repeated, that functions like a mini-amendment-lock: ordinary statutes don't count against it, only an express one naming this subsection does. 12 U.S.C. §1721(g)(1):

> "No State or local law, and no Federal law (except Federal law enacted expressly in limitation of this subsection after October 8, 1980), shall preclude or limit the exercise by the Association of (A) its power to contract with the issuer on the terms stated in the preceding sentence, (B) its rights to enforce any such contract with the issuer, or (C) its ownership rights, as provided in the preceding sentence, in the mortgages constituting the trust or pool against which the guaranteed securities are issued."

Same construction, same date-fenced entrenchment, is repeated for the multiclass-securities program at §1721(g)(3)(E)(iv) (fenced to August 10, 1993 forward). This is Congress locking in Ginnie Mae's contract and ownership rights against being quietly gutted by some unrelated later statute — you have to come after it by name.

## 7. Emergency powers

No general "national emergency" power clause was located in the sections fetched. The closest analog found is a targeted, servicemember-specific shortfall backstop inside the guaranty subsection itself — not a broad emergency power, but functionally an automatic-stabilizer clause triggered by a legally mandated interest-rate cut for military borrowers. 12 U.S.C. §1721(g)(1):

> "In any case in which (I) Federal law requires the reduction of the interest rate on any mortgage backing a security guaranteed under this subsection, (II) the mortgagor under the mortgage is a person in the military service, and (III) the issuer of such security fails to receive from the mortgagor the full amount of interest payment due, the Association may make payments of interest on the security in amounts not exceeding the difference between the amount payable under the interest rate on the mortgage and the amount of interest actually paid by the mortgagor."

This is the Servicemembers Civil Relief Act interaction point — Ginnie Mae quietly eats the interest-rate gap created when a deployed servicemember's mortgage rate is legally capped, so investors in the guaranteed security don't feel it.

## 8. Definitions section — scope expansion

The definitions section proper (likely 12 U.S.C. §1707 or the "purposes" clauses of §1716) was not reachable this session (rate-limited on every attempt — see §2 above). What I did capture directly bears on scope, though, and it's a real definitional trap for anyone reading casually: inside 12 U.S.C. §1717, the word **"Association"** is defined to mean **Ginnie Mae**, and the word **"corporation"** is defined to mean **Fannie Mae** — the opposite of what a casual reader would guess from "Federal National Mortgage Association" sounding more like "the Association." §1717(a)(2):

> "(A) One of such separated portions shall be a body corporate without capital stock to be known as Government National Mortgage Association (hereinafter referred to as the 'Association')... (B) The other such separated portion shall be a body corporate to be known as Federal National Mortgage Association (hereinafter referred to as the 'corporation')..."

Anyone grepping U.S. Code text near these sections for "the Association" needs to know it means Ginnie Mae, not Fannie Mae — a genuine scope/reading trap baked into the statute's own vocabulary.

## 9. Succession/perpetuity & dissolution

Ginnie Mae is chartered to run forever unless Congress itself kills it — no self-destruct clause, no sunset date, no board vote that can end it. 12 U.S.C. §1717(a)(2)(A):

> "The Association shall have succession until dissolved by Act of Congress. It shall maintain its principal office in the District of Columbia and shall be deemed, for purposes of venue in civil actions, to be a resident thereof."

Only Congress, by statute, can end Ginnie Mae. No administrative wind-down path exists in the text fetched.

## 10. Anything strange — THE full faith and credit clause

This is the one that separates Ginnie Mae from every other housing-adjacent entity in this batch. Fannie Mae and Freddie Mac carry an *implied* government backstop that Congress has never put in writing — market assumption, not law. Ginnie Mae's guaranty is not implied. It is written, in the current U.S. Code, in exactly these words. 12 U.S.C. §1721(g)(1):

> "**The full faith and credit of the United States is pledged to the payment of all amounts which may be required to be paid under any guaranty under this subsection.**"

That single sentence is the whole ballgame. Everything upstream of it — the guaranty authority itself ("The Association is authorized... to guarantee the timely payment of principal of and interest on such trust certificates or other securities..."), the subrogation mechanism ("the Association shall make such payment as and when due in cash, and thereupon shall be subrogated fully to the rights satisfied by such payment"), the mortgage-pool-ownership-on-default clause ("the mortgages that constitute such trust or pool shall become the absolute property of the Association") — all of it exists to make that one sentence enforceable. This is a statutory debt of the United States, not a market convention.

## Layer map — the 1968 partition, and what went where

Ginnie Mae did not start life as a separate thing. It was carved out of the old, single Federal National Mortgage Association (chartered 1934, National Housing Act, Title III) by Title VIII of the Housing and Urban Development Act of 1968 (Pub. L. 90-448), effective 1968 per 12 U.S.C. §1716b:

> "The purposes of this title include the partition of the Federal National Mortgage Association as heretofore existing into two separate and distinct corporations... One of such corporations, to be known as Federal National Mortgage Association, will be a Government-sponsored private corporation, will retain the assets and liabilities of the previously existing corporation accounted for under section 1719 of this title, and will continue to operate the secondary market operations authorized by such section 1719. The other, to be known as Government National Mortgage Association, will remain in the Government, will retain the assets and liabilities of the previously existing corporation accounted for under sections 1720 and 1721 of this title, and will continue to operate the special assistance functions and management and liquidating functions authorized by such sections 1720 and 1721."

The split, in one line: **Fannie Mae kept the private, capital-stock, buy-and-resell-mortgages secondary-market business (§1718/§1719); Ginnie Mae kept the government-owned, no-capital-stock, special-assistance/liquidation functions (former §1720) plus the mortgage-backed-securities guaranty function (§1721) — and it was this same 1968 act that added the new §1721(g), the full-faith-and-credit MBS guaranty subsection, giving Ginnie Mae the one power that defines it today.** Fannie Mae got the market-facing mortgage business; Ginnie Mae got the government's signature.

## Entity Theory read

Ginnie Mae isn't a company wearing a government costume — it's the government itself, wearing a corporate name tag so Wall Street has something to trade paper against. No stock, no shareholders, no board with its own interests: the HUD Secretary sets policy directly, a presidentially-appointed officer runs the shop day to day, and Congress wrote the backstop into the actual law instead of leaving it to market vibes. Change who sits in the HUD Secretary's chair or the White House and nothing about the guaranty moves — the promise is bolted into 12 U.S.C. §1721(g), not into anyone's personal credibility. Contrast that with Fannie and Freddie, who spent decades as investor-owned, profit-seeking companies leaning on a government backstop nobody in Congress ever actually wrote down — an implied guaranty everyone bet on and nobody could point to in the statute book until the 2008 conservatorship forced the question. Ginnie Mae never had that ambiguity to trade on, and never will: it is the leash, not the dog.

## Source list

- 12 U.S.C. §1716b — https://www.law.cornell.edu/uscode/text/12/1716b — retrieved 2026-07-10
- 12 U.S.C. §1721 — https://www.law.cornell.edu/uscode/text/12/1721 — retrieved 2026-07-10
- 12 U.S.C. §1723 (Management) — https://www.law.cornell.edu/uscode/text/12/1723 — retrieved 2026-07-10
- 12 U.S.C. §1723a (general corporate powers) — https://www.law.cornell.edu/uscode/text/12/1723a — retrieved 2026-07-10
- 12 U.S.C. §1717 (FNMA/GNMA partition and general provisions) — https://www.law.cornell.edu/uscode/text/12/1717 — retrieved 2026-07-10
- Attempted, not retrieved (persistent rate-limit, HTTP 429, four attempts each): 12 U.S.C. §1723c (tax exemption of obligations — candidate section), 12 U.S.C. §1716 (purposes/definitions). Flagged as open follow-up, not filled from memory.

> [!graph]- Graph links (2 notes — auto-generated, do not edit)
> 1968 - Government National Mortgage Association provisions (current codified) (verbatim)
> [The Entity Theory — Working Note](../sources/the-entity-theory-working-note-e6145374fc35.html)
