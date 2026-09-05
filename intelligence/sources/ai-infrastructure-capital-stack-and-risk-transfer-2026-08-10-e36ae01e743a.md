> Source evidence cutoff: 2026-08-10 America/New_York

# AI Infrastructure Capital Stack and Risk Transfer — 2026-08-10

## Governing question

For the emerging AI-infrastructure asset class:

1. who owns the GPUs;
2. who owes the debt;
3. what cash flow services it; and
4. who absorbs loss if utilization or residual value collapses?

## Controlling answer

There is no single AI-infrastructure financing model. The public record shows
five distinct asset and cash-flow structures:

| Model | Financed asset | Direct debt-service cash flow | First exposed party if demand fails | Residual-value object |
|---|---|---|---|---|
| GPU-owning lease fund | identified compute equipment | tenant lease payments | fund / project equity, subject to lease and support | GPUs and related systems |
| GPU project-finance SPV | GPU servers plus assigned compute contract | controlled customer-service payments | project equity; then secured lenders after collateral recovery | pledged GPUs, contract and cash accounts |
| AI-cloud operating company | owned and leased GPU fleet plus service platform | corporate customer-service revenue | operating-company equity across a wider debt, lease and capex stack | mixed owned/leased equipment and enterprise value |
| data-center real-estate SPV | land interest, powered shell, cooling and power plant | tenant rent and expense reimbursements | property equity; then project lenders | building, power and lease—not necessarily GPUs |
| dedicated-power project | generation equipment | long-term power purchase / take-or-pay payments | project equity; then project creditors | energy equipment and contract |

The central mistake is therefore to ask who bears “AI factory” risk without
first identifying the legal asset. A property lender may have no claim on the
GPUs. A GPU lender may have no claim on the land or power plant. A compute
customer may be obligated under a take-or-pay service contract without owning
or controlling the underlying hardware.

## 1. The August 10 NVIDIA platforms are a distribution architecture, not funded capacity

NVIDIA announced memoranda of understanding with Apollo, BlackRock,
Blackstone, Brookfield, Goldman Sachs and KKR to establish independent
financing platforms intended to mobilize more than $500 billion of third-party
capital over time. NVIDIA says final agreements remain to be executed.

The announcement identifies no per-partner allocation, owner, borrower, SPV,
instrument, customer contract, collateral package, funding draw or loss
waterfall. Jensen Huang's companion article says financial institutions would
independently underwrite customer demand, utilization, cash flow and residual
value. NVIDIA may provide residual-value support for up to 25 percent of an
opportunity in some cases, assessed project by project. The form, trigger,
duration, beneficiary and priority of that support are not disclosed.

**Ruling:** the initiative is evidence that compute credit is being organized as
a repeatable capital-market product. It is not evidence that $500 billion is
committed, raised, lent, spent or operating.

Sources: [NVIDIA announcement](https://nvidianews.nvidia.com/news/nvidia-partners-with-apollo-blackrock-blackstone-brookfield-goldman-sachs-and-kkr-to-establish-ai-compute-infrastructure-financing-platforms-to-mobilize-over-500-billion-of-third-party-capital); [Jensen Huang article](https://x.com/JensenHuang/status/2086934705207959965).

## 2. Goldman–IREN–Microsoft: the cleanest disclosed GPU-credit chain

On May 29, 2026, IREN disclosed definitive financing for **IE US Hardware 3
LLC**, a wholly owned subsidiary that is the borrower/issuer and acquirer/owner
of GPU infrastructure.

| Object | Publicly disclosed state |
|---|---|
| Debt | Approximately $1.5 billion delayed-draw term loan at SOFR + 2.25 percent plus $2.1 billion of 5.96 percent senior notes due 2031. Goldman Sachs Bank USA and JPMorgan were joint lead arrangers/bookrunners. |
| Revenue | A November 2, 2025 Microsoft contract for dedicated GPU services at Childress, Texas. The debt matures December 31, 2031 or, if earlier, after the final Microsoft service fee. |
| Security | All Hardware 3 assets, the GPUs, 100 percent of the borrower's equity and Microsoft-contract cash flows. |
| Controls | Tranche amortization; minimum 1.05x debt-service coverage; equity cures; mandatory prepayment triggers for low coverage or loan-to-cost above 65 percent; interest and power hedges. |
| Residual support | If Microsoft rejects or terminates a service tranche, the GPUs are disposed of or remarketed first. IREN provides a limited parent guarantee for a resulting Hardware 3 payment shortfall attributable to that rejected or terminated tranche. |

**Loss path:** Microsoft service fees → GPU remarketing/disposal → limited IREN
shortfall support → secured lenders retain any deficiency not covered by those
sources. The public documents do not quantify the final lender-loss tail.

Source: [IREN May 29, 2026 8-K and financing exhibits](https://www.sec.gov/Archives/edgar/data/1878848/000114036126023427/ef20075181_8k.htm).

## 3. CoreWeave DDTL 4.0: nonrecourse GPU project finance

The March 2026 DDTL 4.0 facility provides a sharper project-finance model than
CoreWeave's older parent-guaranteed GPU facilities.

| Object | Publicly disclosed state |
|---|---|
| GPU owner / borrower | CoreWeave Compute Acquisition Co. VIII and its subsidiaries. GPU serial-number schedules must be delivered to lenders. |
| Commitment | $8.5 billion delayed-draw commitment through June 30, 2027; maturity March 31, 2032. Only $1.260 billion was drawn/outstanding at March 31, 2026. |
| Revenue | Payments under one assigned customer master-services agreement enter controlled accounts. The customer's identity is redacted; do not promote contextual guesses as fact. |
| Waterfall | Operating expenses → agent, administrative and hedge fees → interest → principal → liquidity reserve → power reserve → cash trap → residual capex/management/distributions. |
| Security | GPUs, customer contract, cash accounts, substantially all project assets and 100 percent of CCAC VIII equity. |
| Parent support | Bad-act carveout only. CoreWeave does not guarantee utilization, residual value or an equity contribution needed to preserve asset value. |

**Loss path:** project equity is first loss. If assigned customer payments fail
and the GPUs/contract/cash collateral do not repay the facility, the project
lenders bear the deficiency. The parent guarantee reaches fraud,
misappropriation, specified misconduct and voluntary bankruptcy conduct—not
ordinary diminution in GPU value.

This must not be generalized to CoreWeave's older DDTL 1.0–3.0 facilities,
which the 2026 first-quarter filing says are unconditionally guaranteed by the
parent.

Sources: [CoreWeave DDTL 4.0 8-K](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000129/crwv-20260330.htm); [credit agreement](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000129/ex1011.htm); [limited guarantee](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000129/ex102.htm); [Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000222/crwv-20260331.htm).

## 4. CoreWeave corporate stack: the wider operating-company exposure

At December 31, 2025, CoreWeave reported $30.557 billion of net property and
equipment, including $20.903 billion of technology equipment and $9.376 billion
of construction in progress. It had $21.615 billion of principal debt and $8.2
billion of operating-lease liabilities. It funds capital investment through
debt and securities issuance, delayed-draw facilities, OEM financing and
balance-sheet cash.

The servicing spine is contracted cloud-compute revenue: $5.1 billion of 2025
revenue, $60.7 billion of remaining performance obligations and a weighted
average committed-contract duration of about five years. One unnamed customer
represented 67 percent of 2025 revenue. Customer arrangements are generally
service contracts rather than leases because customers do not control
identified hardware.

The residual-risk warning is explicit: CoreWeave estimates technology-equipment
life at six years but says failure to redeploy components after contracted use,
or inaccurate useful-life assumptions, could materially harm the business.

**Loss path:** across the consolidated company, equity absorbs enterprise loss;
secured DDTL lenders can foreclose on facility collateral; OEM financiers and
lessors retain their agreement-specific claims; unsecured noteholders depend on
the remaining enterprise. Ring-fencing one GPU project does not isolate
shareholders from the rest of CoreWeave's debt, lease and capex obligations.

Source: [CoreWeave 2025 10-K](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm).

## 5. Apollo–Valor–xAI: asset ownership is clear; the waterfall is not

Apollo-managed funds and affiliates led a $3.5 billion “capital solution” for
Valor Compute Infrastructure LP, a Valor-managed fund, supporting VCI's $5.4
billion acquisition and lease of NVIDIA GB200 compute to an xAI subsidiary.
NVIDIA is an anchor limited partner. Valor says investors receive quarterly
cash distributions and upside through ownership of the compute assets.

| Question | Current answer |
|---|---|
| Who owns the GPUs? | VCI, according to the transaction release. |
| Who pays? | An xAI subsidiary under a triple-net lease. |
| What services investor capital? | xAI lease payments; the triple-net form generally assigns specified operating costs to the tenant, but the release does not publish the executed allocation. |
| Who eats the loss? | VCI equity/investors are residual owners; the priority and loss position of Apollo's $3.5 billion “capital solution” cannot be established because its debt/equity composition and security are undisclosed. |

Missing documents include the xAI guarantee, rent schedule, termination/default
terms, purchase option, residual floor, lien package and instrument seniority.

Source: [Apollo January 7, 2026 transaction release](https://www.apollo.com/insights-news/pressreleases/2026/01/apollo-backs-5-4-billion-valor-and-xai-data-center-compute-infrastructure-transaction-with-3-5-billion-capital-solution-3214463).

## 6. Stargate Abilene: the property loan is not the GPU financing

**Abilene DC 1 LLC** owns, develops, leases and operates the first two buildings,
eight data halls and power station. Longhorn JV owns the SPV; Blue Owl vehicles
hold about 92.3 percent and a Crusoe affiliate about 7.7 percent.

The SPV had a $2.288 billion construction facility, with $2.025861 billion
outstanding at December 31, 2025. Oracle America leases 100 percent of the site
for 15 years. First-year base rent was approximately $244.728 million before
escalation and expense pass-throughs. The rent is the property debt-service
spine.

Abilene DC 1's disclosed owned asset is the property/power layer—not the NVIDIA
GPU fleet. Oracle led hardware and software deployment, but exact GPU title and
the allocation of customer-prepaid versus customer-supplied GPUs at this site
are not public.

**Loss path:** an OpenAI utilization shortfall does not itself end Oracle's
property lease. Oracle first bears the mismatch between fixed property/IT
commitments and its downstream customer revenue. If Oracle defaults, the
Longhorn/Blue Owl/Crusoe equity is first loss, followed by construction lenders
after project-collateral recovery. GPU residual-value loss remains with the
undisclosed rack owner, not automatically the real-estate SPV.

Sources: [Abilene DC 1 audited financial statements](https://www.sec.gov/Archives/edgar/data/1944366/000194436626000020/exhibit993-2025abelinedc1l.htm); [Blue Owl filing](https://www.sec.gov/Archives/edgar/data/1944366/000194436625000100/osnl-20250630.htm); [Crusoe operating update](https://www.crusoe.ai/resources/newsroom/crusoe-announces-flagship-abilene-data-center-is-live); [Stargate launch](https://openai.com/index/announcing-the-stargate-project/).

## 7. AIP–Aligned: data-center equity, not disclosed GPU credit

AIP, MGX and BlackRock's GIP closed the acquisition of 100 percent of Aligned
Data Centers on July 21, 2026 at approximately $40 billion enterprise value and
committed another $5 billion of growth capital. Aligned owns/develops/operates
the land, building, power and cooling platform across 51 campuses. The public
record does not establish that customer GPUs were acquired.

Customer payments for space, power and cooling service the operating platform
and its debt. The acquisition's equity/debt sources, lenders, leverage,
security, tenant concentrations and parent guarantees are not public. Separate
company-level examples include a $2.58 billion revolving development facility
secured by an initial six-asset pool and a $600 million senior-secured
Blackstone facility for a Utah development.

**Loss path:** utilization/default reduces Aligned cash flow and first reaches
consortium equity; secured project/development lenders then enforce their
collateral. GPU obsolescence normally remains outside this perimeter unless a
site contract or equipment vehicle says otherwise. Aligned instead bears
building, power, cooling and refit obsolescence.

Sources: [Aligned acquisition close](https://aligneddc.com/press-release/aip-mgx-and-blackrocks-gip-close-acquisition-of-aligned-data-centers/); [Aligned $2.58 billion facility](https://aligneddc.com/press-release/aligned-data-centers-closes-on-2-58-billion-credit-facility-to-fuel-continued-u-s-expansion/).

## 8. Brookfield–NAVER–NVIDIA: the decisive GPU-title document has not arrived

The July 24 proposal describes a Brookfield nonbinding term sheet for up to $9
billion, a planned $1 billion NVIDIA investment into NAVER Corp. and NAVER
funding the remainder. NVIDIA's investment is conditional on NAVER securing at
least $9 billion of committed financing separate from NVIDIA's investment.

Brookfield subsequently continued to call the arrangement proposed and said
material capital would be committed only after suitable commercial
arrangements. Brookfield's Radiant vehicle may ultimately own or finance GPU
capacity, but no definitive vehicle, title schedule, lease, collateral filing
or customer contract is public.

**Ruling:** NAVER may become borrower, lessee, compute buyer or co-owner. Until a
definitive agreement adjudicates those roles, no final loss allocation is
supportable.

Sources: [NVIDIA–NAVER–Brookfield release](https://investor.nvidia.com/news/press-release-details/2026/NAVER-NVIDIA-and-Brookfield-to-Expand-Koreas-National-AI-Factory-Infrastructure-Buildout/default.aspx); [Brookfield Q2 2026 release](https://bip.brookfield.com/sites/brookfield-bip-v2/files/Brookfield-BIP-IR-V2/2026/Q2/BIP-and-BIPC-Q2-26-Press-Release_vFINAL-a.pdf).

## 9. Brookfield–Bloom: the useful power-equipment comparator

Brookfield and Bloom expanded their AI-infrastructure power-financing framework
to $25 billion on June 30, 2026, but Brookfield's July materials identified only
$2 billion of committed capex under long-term take-or-pay projects. The framework
ceiling and committed projects are different clocks.

Brookfield's AI Fund owns the majority interest in project JVs; Bloom retains
bounded minority stakes. The usual disclosed model is financier-owned Energy
Servers with the end customer paying for consumed power. Long-term take-or-pay
contracts shift much utilization risk to the power purchaser. Bloom still bears
manufacturing, installation, warranty, service-performance and minority-equity
risk; the fund bears the majority residual exposure.

At March 31, 2026 Bloom reported $69.1 million of total JV capital commitments
and $57.8 million maximum exposure to loss. Project-creditor identities and
collateral remain undisclosed.

Sources: [framework expansion](https://www.bloomenergy.com/news/brookfield-and-bloom-energy-expand-ai-infrastructure-partnership/); [Bloom Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/1664703/000162828026028021/be-20260331.htm).

## Cross-case ruling: follow the fixed obligation

When utilization falls, the first consequential question is not “who uses the
GPU?” It is “which fixed obligation survives the demand shortfall?”

```text
end-user demand falls
  -> does a take-or-pay compute contract survive?
  -> does a tenant lease survive?
  -> does a parent or residual-value guarantee respond?
  -> can the asset be redeployed or remarketed?
  -> what collateral can creditors actually seize?
  -> which equity account is subordinated?
  -> which creditor retains the deficiency?
```

The current record supports four strong conclusions:

1. **Contracted cash flow, not the GPU alone, makes debt service credible.**
2. **Asset title and contract assignment determine which creditor can reach which cash and equipment.**
3. **Residual support is not the same as a guarantee of debt, utilization or technology value.**
4. **The $500 billion NVIDIA initiative becomes finance only one project and one executed waterfall at a time.**
