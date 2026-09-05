# Insurance and reinsurance — factual field registry

Updated: 2026-07-12  
Status: working research protocol  
Purpose: make the insurance layer repeatable, factual, and capable of tracing both the transfer of risk and the investment of the capital supporting it.

## Governing proposition

Insurance is not only a claims business. It is an access gate, a risk-transfer chain, a capital pool, and a public/private backstop system.

The research object is therefore not merely the named insurer. It is the full chain:

`risk owner → broker/MGA → primary carrier → reinsurer → retrocessionaire/ILS investor → guaranty, residual, or government backstop`

At the same time, trace the capital chain:

`premium/reserve → insurer or affiliated asset manager → invested asset → valuation/rating → capital charge → liquidity or impairment outcome`

## 1. Entity vocabulary

Do not collapse these bodies into one brand:

| Entity type | Function to establish | Common confusion to avoid |
|---|---|---|
| Parent / holding company | owns regulated and unregulated subsidiaries; allocates group capital | parent is not automatically the policy obligor |
| Admitted insurer | state-licensed carrier whose policy is generally inside the state guaranty framework | brand may use several writing companies |
| Surplus-lines insurer | writes non-admitted coverage through the surplus-lines system | non-admitted does not mean unregulated or uncapitalized |
| Reinsurer | assumes risk from a cedent | policyholder usually has no direct claim against it |
| Retrocessionaire | reinsures a reinsurer | often invisible in the original policy record |
| Lloyd's Corporation | market infrastructure, oversight, central assets, and franchise | Lloyd's is not one insurance company |
| Lloyd's syndicate | annual underwriting pool supported by members' capital | syndicate is not identical to its managing agent |
| Managing agent | operates one or more Lloyd's syndicates | manages underwriting but is not necessarily the risk-bearing member |
| Broker | places insurance or reinsurance and may control market access/data | broker is not usually the carrier |
| MGA / MGU / program administrator | delegated underwriting or claims authority | visible product may sit on another carrier's paper |
| P&I club | mutual marine-liability insurer owned by shipowner members | club pooling and group reinsurance must be traced separately |
| Captive insurer | insurer formed primarily for its owner or group risks | captive may also be a financing or reserve-transfer tool |
| Protected/segregated cell | legally or contractually separated account within a vehicle | cell and sponsor liabilities may differ by jurisdiction |
| Special-purpose insurer / reinsurer | fully or partly collateralized transformer for ILS or sidecar risk | note investors and policyholders hold different claims |
| Asset manager | selects and manages assets supporting insurer liabilities | may be affiliated with the insurer owner or originator |
| Rating organization / model vendor | affects price, capital, counterparty acceptance, and market access | rating/model output is not a regulatory finding |
| State residual market | coverage mechanism for risks the voluntary market will not take | may be an insurer, association, plan, or facility with different assessment powers |
| Guaranty association | post-insolvency statutory protection within stated limits | not pre-failure supervision and not unlimited insurance |
| Government insurer / guarantor | directly writes, reinsures, guarantees, or shares defined risks | taxpayer exposure depends on statute, trigger, cap, and recoupment |

## 2. Contract vocabulary

| Object | Required distinction |
|---|---|
| Policy | legal contract between named policyholder/insured and writing carrier |
| Binder | temporary evidence of coverage; not necessarily the final policy wording |
| Endorsement | changes the policy; capture whether it broadens, restricts, or clarifies cover |
| Exclusion | removes a peril, cause, territory, actor, or loss class |
| Limit / sublimit | maximum payable amount; keep occurrence, aggregate, and sublimits separate |
| Deductible / retention | first-loss amount borne by insured; do not confuse with reinsurance attachment |
| Claims-made / occurrence | determines which policy period responds |
| Parametric trigger | payment depends on a stated index or event rather than adjusted indemnity loss |
| Treaty reinsurance | covers a defined portfolio or class automatically under treaty terms |
| Facultative reinsurance | separately underwritten risk or placement |
| Quota share | proportional transfer of premium and loss |
| Excess of loss | reinsurer responds above an attachment point up to a limit |
| Aggregate stop loss | responds after aggregate loss or loss ratio crosses a threshold |
| Catastrophe cover | responds to defined catastrophe aggregation; occurrence definitions matter |
| Retrocession | transfer by a reinsurer to another risk bearer |
| Funds withheld / modco | assets supporting ceded liabilities may remain with the cedent while economics pass to reinsurer |
| Commutation | negotiated termination and settlement of reinsurance obligations |
| Collateral | assets securing obligations; identify owner, custodian, control, and release conditions |
| Sidecar | limited-purpose capital vehicle taking a share of a book or layer |
| Catastrophe bond | security whose principal or interest is exposed to a defined insurance trigger |

## 3. Status vocabulary

- **RUMOR / LEAD:** attributed report or market signal without a located operative record.
- **ANNOUNCED:** company or official has stated an intended action.
- **FILED / APPLIED:** rate, form, transaction, license, or approval request is before an authority.
- **AUTHORIZED / APPROVED:** competent body has granted the stated permission; conditions remain part of the status.
- **BOUND / PLACED:** insurance or reinsurance contract is effective under stated terms.
- **OPERATING:** entity or program is writing, assuming, servicing, or paying real business.
- **TRIGGERED:** contract or public program trigger has occurred; payment remains a separate clock.
- **PAID / RECOVERED:** claim, reinsurance recovery, or public share has been paid.
- **NONRENEWED / CANCELLED:** coverage ended according to the stated policy or statutory mechanism.
- **RUNOFF:** no or limited new business; old liabilities remain.
- **REHABILITATION / RECEIVERSHIP / LIQUIDATION:** use the exact court or regulator status.
- **SCHEDULED / TARGET:** future state; not a historical event.

## 4. Required entity record

```markdown
## Legal entity / operating brands

**Entity type:**
**Parent and material owners:**
**Domicile / formation jurisdiction:**
**Primary regulator(s):**
**Licensed writing entities:**
**Core lines / perils:**
**Policyholder or cedent counterparties:**
**Distribution / broker / MGA layer:**
**Reinsurance and retrocession structure:**
**Affiliated asset manager / originator:**
**Material reserve and investment exposures:**
**Ratings and capital framework:**
**Guaranty / public-backstop posture:**
**Runoff / resolution posture:**

### Dated actions

### Risk transfer map

### Capital and reserve map

### Public/private seam

### Shared dependencies

### What remains unestablished

### Open watches
```

## 5. Required transaction or program record

- transaction/program name and aliases;
- legal parties and each party's role;
- policy line, insured peril, and territory;
- direct, assumed, ceded, retroceded, or capital-markets layer;
- effective, attachment, maturity, renewal, and termination dates;
- premium or consideration, if public;
- gross, ceded, and net exposure, if public;
- attachment point, exhaustion point, limit, aggregate, and reinstatement;
- trigger type: indemnity, industry loss, modeled loss, parametric, mortality, longevity, cyber, or other;
- collateral owner, custodian, permitted assets, valuation, and release mechanics;
- reserve credit and accounting treatment;
- rating, model, and risk-based-capital treatment;
- public guarantee, assessment, recoupment, or taxing authority;
- governing law, regulator, court, and dispute mechanism;
- current state and next formal watch date;
- primary sources and explicit unknowns.

## 6. The seven clocks

1. **Policy clock** — quote → bind → endorsement → renewal/nonrenewal → cancellation.
2. **Claims clock** — loss → notice → reserve → adjustment → payment/denial → suit → subrogation.
3. **Risk-transfer clock** — cession → placement → attachment → recovery → dispute → commutation.
4. **Capital clock** — premium → reserve → asset purchase → valuation → capital charge → liquidity/impairment.
5. **Entity clock** — formation → acquisition → block transfer → runoff → receivership/liquidation.
6. **Regulatory clock** — filing → approval → examination → remediation → enforcement.
7. **Public-backstop clock** — private-market withdrawal/failure → statutory trigger → public payment → assessment, surcharge, borrowing, or taxpayer recoupment.

A single event may move more than one clock, but the clocks must not be merged. A rate approval does not prove a policy was renewed. A catastrophe does not prove a reinsurance layer attached. A reinsurance recovery booked as receivable does not prove cash was collected.

## 7. Event capture template

```markdown
### YYYY-MM-DD — action title

**Status:** Lead / Announced / Filed / Approved / Bound / Operating / Triggered / Paid / Runoff / Scheduled
**Entity acting:**
**Other legal entities:**
**Line / peril / territory:**
**Clock:** Policy / claims / risk-transfer / capital / entity / regulatory / public-backstop
**Before state:**
**After state:**
**Gross exposure:**
**Ceded/net exposure:**
**Policyholders/accounts/assets affected:**
**Location / legal locus:**
**Time:** Publicly stated / not publicly stated

One neutral paragraph stating the act. Then state separately what changed in coverage, price, risk bearer, reserves/assets, claims rights, and public exposure.

**Primary source:** Label
**Secondary corroboration:** Label, if needed
**What remains unestablished:**
**Open document request:**
```

## 8. Evidence labels

- **SOURCE FACT:** directly stated in a primary legal, regulatory, financial, or contractual record.
- **COMPANY CLAIM:** statement by a party about its product, strength, performance, or intention.
- **MARKET ESTIMATE:** estimate by broker, rating agency, model vendor, data firm, or trade body; name method and date.
- **INFERENCE:** conclusion drawn from established facts; state the chain.
- **SPECULATION:** possibility or hypothesis without enough evidence to call an inference.
- **UNVERIFIED LEAD:** potentially important claim awaiting an operative source.

## 9. Promotion rules

### Entity action

A source becomes an entity action only when it establishes the legal actor, date, affected business or liability, and changed state. A group press release does not prove which writing company, reinsurer, or account bears the risk.

### Risk transfer

A risk-transfer claim becomes confirmed only when the record establishes:

1. cedent or insured risk owner;
2. assuming risk bearer;
3. covered book, peril, or population;
4. effective period;
5. transfer form and layer;
6. stated limit, share, or testable selection rule;
7. primary source or statutory/regulatory filing.

### Market withdrawal

Do not infer insolvency from a carrier's nonrenewal, moratorium, rate request, or geographic exit. Capture separately whether the action reflects price, reinsurance, capital, claims, regulation, strategy, or an unstated reason.

### Public backstop

Do not say taxpayers bear a loss until the statute or operative record establishes the trigger, payment source, cap, recoupment, assessment, borrowing, and repayment structure.

### On-chain or AI claim

Do not treat a technology pilot as a change in legal policy, title, reserve ownership, settlement finality, or claims obligation unless the operative contract and regulated entity record establish that change.

## 10. Boundaries

The first sweep includes commercial and personal P&C, life and annuities, reinsurance, insurance-linked securities, strategic/public backstops, cyber/AI, and digital-asset seams.

The following remain adjacent and enter only when they move the risk-transfer machine:

- deposit and credit-union share insurance;
- health-plan reimbursement and Medicaid/Medicare financing;
- unemployment and social insurance;
- pensions and PBGC;
- securities investor protection;
- warranty and service contracts;
- derivatives described loosely as insurance.

These are not declared unimportant. They require their own statutory and accounting grammars and should not be folded into the carrier/reinsurance layer merely because they contain the word “insurance.”
