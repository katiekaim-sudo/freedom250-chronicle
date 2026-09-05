# White House Research Hub — corpus and action-coverage audit

**Evidence cutoff:** 2026-07-21  
**Status:** incorporated 2026-07-21  
**Source class:** White House-hosted Council of Economic Advisers research  
**Machine authorities:** `WHITE_HOUSE_RESEARCH_INVENTORY.generated.json`,
`PDF_TEXT_INVENTORY.generated.json`, `LOCAL_COVERAGE_AUDIT.generated.json`

## Short answer

Yes: this is a missing Freedom 250 evidence lane. But it is not mainly a set of
missing executive orders.

The active White House Research index contains 26 PDF papers spanning 349
physical pages. None of the 26 paper titles appears in active vault Markdown or
JSON at the cutoff. The site's live `Related` graph exposes 164 distinct
presidential-action pages. Of those, 123 resolve to the vault's generated
Executive Orders corpus; the remaining 41 are a mix of proclamations,
presidential memoranda, permits, determinations and uncategorized presidential
pages. Exact-title absence is not proof of substantive absence, but it gives us
the right next audit lane.

**The real gap:** the vault has the orders, but not the administration's own
economic models, implementation arguments and forward-policy signals that make
those orders legible as a program.

## Evidence firewalls

1. **CEA paper is not executive action.** It is an Executive Office research
   product. It can explain, defend or signal policy; it does not create legal
   authority.
2. **Model output is not observed effect.** Dollar, GDP, lending, price and
   welfare estimates remain model-dependent claims until matched to later data.
3. **Site adjacency is not legal linkage.** The `Related` carousel is dynamic
   and, at the cutoff, includes actions published after many of the papers.
4. **Paper publication is not the policy clock.** Keep action signature,
   Federal Register publication, effective date, agency rule, litigation,
   voluntary agreement and production state separate.
5. **The White House is the issuer, not an independent validator.** These are
   primary sources for administration framing and methods, not neutral proof
   that the estimated benefits or costs occurred.

## Highest-value joins

### 1. Balance of payments → the Section 122 tariff theory

**Paper:** `Measuring Balance of Payments Deficits` (2026-07-15)  
**Route:** Currency Watch → U.S. Section 122 episode → tariff/BOP transmission

This is the most time-sensitive paper in the corpus. CEA argues that a
current-account deficit remains a valid balance-of-payments deficit under a
floating exchange-rate regime, notes the 2024 current-account deficit at 4.1%
of GDP, and compares it with the much smaller deficit visible when Congress
enacted Trade Act section 122. It also treats many modern securities as liquid,
money-like claims rather than durable long-term capital.

**Why it matters:** the paper was released while the February 20, 2026 section
122 temporary import surcharge was still on its stated expiry clock. It is an
economic/legal-rationale object for the proclamation, not a new tariff action.

**Audit limit:** the paper does not cure a statutory defect by itself. The
operative proclamation, section 122 text, customs implementation, litigation
and expiry/extension clocks continue to control.

### 2. Stablecoin yield → GENIUS/CLARITY and the deposit-demand fight

**Paper:** `Effects of Stablecoin Yield Prohibition on Bank Lending`
(2026-04-08)  
**Route:** Congressional Monetary Infrastructure → banking/deposits → fintech
rails → monetary cross-cuts

CEA models the GENIUS Act's issuer-yield prohibition and the proposed CLARITY
variants that would reach affiliate or third-party yield. Its baseline estimate
is that eliminating yield adds only $2.1 billion of bank lending, including
$500 million at community banks, while imposing an $800 million net welfare
cost. CEA's stated conclusion is that a broad yield prohibition does little to
protect lending and sacrifices consumer returns.

**Why it matters:** this is not merely a defense of the enacted GENIUS rule. It
is an administration-side argument against closing the affiliate/third-party
yield channel. That makes it a live legislative signal for CLARITY and for the
bank-versus-token deposit fight.

**Audit limit:** the result depends on reserve allocation, deposit
re-intermediation, stablecoin scale and the Fed's abundant-reserves framework.
The paper's extreme case expressly assumes several conditions CEA calls
implausible.

### 3. CFPB cost paper → the institutional dismantling record

**Paper:** `Estimating the Cost of the Consumer Financial Protection Bureau to
Consumers` (2026-02-17)  
**Route:** Fed/clearing/Treasury → government-wide CFPB audit → judicial money

CEA estimates cumulative consumer costs of $237-$369 billion from 2011-2024,
including higher borrowing costs, reduced originations and fiscal cost. The
paper derives a mortgage cost wedge from a claimed natural experiment, then
extends the wedge to auto loans and credit cards.

**Why it matters:** this is the administration's quantitative case for shrinking
or restructuring the CFPB. It belongs next to staffing, injunction,
appropriation, director-confirmation and statutory-floor clocks.

**Audit limit:** extrapolation across unlike credit products is the load-bearing
method choice. The paper must not be used as an observed $237-$369 billion loss
ledger, and its cost comparison does not itself resolve the CFPB's legal status.

### 4. Retirement alternatives → private assets as a retail demand rail

**Paper:** `Retail Access to Alternative Investments Via Defined Contribution
Plans` (2025-08-12)  
**Route:** EO 14330 → On-Chain State → retirement/asset-demand layer

Published five days after EO 14330, the paper argues that defined-contribution
plans can provide a large, diversified and sticky capital base for private
markets. It estimates up to $35 billion of GDP benefit from private-equity
access and models gains in risk-adjusted return and lifetime retirement income.

**Why it matters:** EO 14330 is already present in the vault. The missing paper
supplies the demand-side theory: retirement pools are not only beneficiaries;
they are a capital base for private assets.

**Audit limit:** the analysis is a modeled private-equity case, not proof that
all alternatives improve participant outcomes. Fees, valuation, liquidity,
manager selection, litigation risk and ERISA fiduciary duties remain live.

### 5. Deregulation → the paper's own action table

**Paper:** `The Economic Benefits of Current Deregulatory Efforts` (2025-06-19)  
**Route:** Executive Orders → government-shape track → digital finance/AI/energy

The report contains a first-party table of 20 executive orders plus four
memorandum/proclamation objects cited in its analysis. The EO set is already in
the vault. The report itself and the non-EO objects are the gap.

The four non-EO objects named in the paper's table are:

- `Delivering Emergency Price Relief for American Families and Defeating the
  Cost-of-Living Crisis` (2025-01-20);
- `Regulatory Freeze Pending Review` (2025-01-20);
- `Regulatory Relief for Certain Stationary Sources to Promote American Energy`
  (2025-04-08);
- `Directing the Repeal of Unlawful Regulations` (2025-04-09).

CEA estimates up to $907 billion in regulatory relief and 0.29-0.78 percentage
points of additional annual GDP growth under its modeled assumptions.

**Audit limit:** the paper's counterfactual treats estimated regulatory costs
as potentially translating one-for-one into GDP effects and cannot be read as a
measured savings ledger.

### 6. AI divergence → the compute/energy/export program in one paper

**Paper:** `Artificial Intelligence and the Great Divergence` (2026-01-21)  
**Route:** Sovereign Compute → Federal Science Operating System → AI/data-center
EO track

CEA joins Public Law 119-21 investment expensing, the 2025 AI Action Plan,
federal data-center permitting, state-law preemption, federal procurement and
technology exports into one growth strategy. It explicitly frames OBBB's bonus
depreciation as support for data centers, power infrastructure and chip
manufacturing.

**Why it matters:** the vault has much of the operating stack, but not this
White House-authored statement of how tax, energy, permitting, procurement and
exports are meant to work together.

**Audit limit:** cross-country investment, adoption and benchmark indicators do
not establish future productivity, state preemption or operating capacity.

### 7. MFN drugs and hospital contracts → health policy moving through contracts

**Papers:** `Savings from Most-Favored-Nation Drug Pricing Policy` (2026-05-05)
and `Effects of Banning Anti-Competitive Hospital Contracts` (2026-06-18)  
**Route:** health/MAHA → insurance/reinsurance → trade/contract enforcement

The MFN paper says the administration had reached voluntary agreements with 17
large pharmaceutical manufacturers and was seeking statutory codification. It
separates future launches, existing drugs, Medicaid and direct-to-consumer
channels. The hospital paper estimates effects from a nationwide ban on
anti-steering, anti-tiering and all-or-nothing contract clauses while pointing
to pending DOJ complaints against OhioHealth and New York-Presbyterian.

**Why it matters:** these papers show policy being built through private
agreements, purchasing terms, Medicaid conditions and antitrust cases before or
alongside legislation.

**Audit limit:** voluntary agreement, proposed statute, pending complaint and
nationwide ban are four different states. The paper summaries do not provide a
complete public contract set for the 17 claimed manufacturer agreements.

## Full corpus triage

| Date | Paper | Class | Freedom 250 route | Priority |
|---|---|---|---|---|
| 2026-07-15 | Measuring Balance of Payments Deficits | current legal/economic rationale | Currency Watch; section 122 | A |
| 2026-06-18 | Effects of Banning Anti-Competitive Hospital Contracts | forward policy/enforcement model | Health; insurance; antitrust | B |
| 2026-05-05 | Savings from Most-Favored-Nation Drug Pricing Policy | implementation/status claim | Health; trade; Medicaid | A |
| 2026-04-08 | Effects of Stablecoin Yield Prohibition on Bank Lending | live legislative signal | GENIUS; CLARITY; banking | A |
| 2026-02-17 | Estimating the Cost of the CFPB to Consumers | restructuring rationale | CFPB; judicial money | A |
| 2026-01-28 | Economic Impact of State Income Tax Elimination | state fiscal model | State money/fiscal policy | C |
| 2026-01-21 | Artificial Intelligence and the Great Divergence | program synthesis | Compute; AI; energy; exports | A |
| 2025-12-23 | Year-Over-Year Inflation Across Conservative and Liberal States | political/macro comparison | Inflation narrative | C |
| 2025-12-03 | Savings from Resetting CAFE Standards | deregulatory model | Autos; energy; regulation | B |
| 2025-10-01 | Economic Consequences of a Government Shutdown | fiscal scenario | Government continuity | C |
| 2025-09-26 | Expansion of HSA Eligibility Under OBBB | enacted-law explanation | OBBB; health accounts | B |
| 2025-08-29 | Trump Accounts Give the Next Generation a Jump Start on Saving | enacted-program rationale | Fiscal rails; household savings | B |
| 2025-08-12 | Retail Access to Alternative Investments Via DC Plans | post-EO demand model | EO 14330; private assets | A |
| 2025-07-12 | Economic Benefits of Unleashing American Energy | multi-action program model | Energy; critical minerals; shipping | B |
| 2025-07-07 | Imported Goods Have Been Getting Cheaper Relative to Domestic Goods | tariff-incidence argument | Trade; prices; FX | B |
| 2025-07-01 | OBBB Chart Book: Deficits and Debt | pre-signature fiscal case | OBBB; debt | B |
| 2025-06-30 | OBBB and No Tax on Social Security | pre-signature tax case | OBBB; Social Security | B |
| 2025-06-25 | OBBB: Prosperity and Deficit Reduction | pre-signature omnibus case | OBBB | B |
| 2025-06-19 | Economic Benefits of Current Deregulatory Efforts | action-program crosswalk | EO/government shape | A |
| 2025-06-12 | Deterioration of Housing Affordability in Rural America | problem definition | Housing/credit | C |
| 2025-06-10 | Medicaid Community Engagement Requirements and the Value of Work | benefit-gate rationale | OBBB; Medicaid | B |
| 2025-06-04 | Igniting a Second Blue-Collar Boom with Tax Cuts | pre-enactment advocacy | OBBB; labor | C |
| 2025-06-04 | Ramifications of Not Passing OBBB | pre-enactment counterfactual | OBBB | C |
| 2025-05-19 | Preserving and Expanding Low Tax Rates | pre-enactment tax model | OBBB; TCJA | C |
| 2025-05-17 | Health Insurance Opportunity Cost if Reconciliation Fails | pre-enactment counterfactual | OBBB; health | C |
| 2025-04-03 | Economic Impact of Extending Expiring TCJA Provisions | pre-enactment tax model | TCJA; OBBB | C |

## Non-EO action lane: relevant exact-title gaps

The generated coverage audit finds 41 research-adjacent presidential-action
pages that do not resolve to the EO corpus. Most are outside the core project or
already covered under variant wording. The following are the highest-value
objects for an instrument-level follow-up:

| Date | Object | Why it matters |
|---|---|---|
| 2025-01-20 | America First Trade Policy | foundational trade investigation and report clock; already mentioned in the vault but needs instrument routing |
| 2025-01-20 | Regulatory Freeze Pending Review | first-day regulatory-state clock |
| 2025-02-21 | America First Investment Policy | foreign-capital and national-security investment gate |
| 2025-04-09 | Directing the Repeal of Unlawful Regulations | agency repeal instruction outside the EO lane |
| 2025-06-06 | Eliminating Waste, Fraud, and Abuse in Medicaid | direct join to benefit-integrity and payment-control work |
| 2025-09-18 | U.S.-UK Technology Prosperity Deal MOU | compute/export/standards agreement object |
| 2026-01-14 | Processed Critical Minerals import proclamation | metals, tariffs and defense supply chain |
| 2026-02-20 | Temporary Import Surcharge proclamation | already tracked; this paper supplies the missing BOP rationale |
| 2026-04-20 | DPA section 303 natural-gas determination | emergency authority and industrial capacity |
| 2026-05-29 | Critical-position pay for national-security investment workforce | implementation capacity for the investment-security state |
| 2026-07-13 | Chemical-manufacturing security regulatory-relief proclamation | industrial policy and emergency/regulatory authority |
| 2026-07-20 | Three Canada discrimination duty proclamations | new trade-pressure objects; outside the research-paper publication clocks |

## Vault landing completed

The corpus landed as a source layer, not 26 narrative syntheses:

1. one vault source index plus 26 compact source cards under
   `05 - Sources/Executive Office/White House Research/`;
2. all 26 official PDFs, hash-matched to this package, under its `PDFs/`
   subfolder;
3. a searchable `White House Research.html` view that exposes class, route and
   priority while keeping the issuer/model boundary visible;
4. an `Executive Office.html` wrapper that keeps Executive Orders and White
   House Research as separate sublayers under the existing `obs-eo` shell ID;
5. registered builders and stale-scan coverage for both new views.

The physical `03 - Executive Orders/` folder and its builder remain unchanged
for compatibility. The non-EO presidential-instrument registry and standing
delta watch remain follow-up lanes; neither was implied by merely preserving
the complete research corpus. Stablecoin, CFPB, MFN and balance-of-payments
estimates still require claim audits before their numbers enter synthesis.
