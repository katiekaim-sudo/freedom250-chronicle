# Asset–Obligation–Authority — Control Map

## Controlling conclusion

Atomic settlement can reframe energy-asset management when an operational record becomes an approved predicate for a commercial state transition. It cannot make every technical fact legally conclusive or collapse safety, contract, compliance, funding, accounting and legal-discharge authority into one clock.

The durable unit is not a token. It is an **asset + obligation + authority** graph:

```text
identified physical asset
  -> governed measurement or inspection
  -> authorized technical or contractual determination
  -> obligation, claim, credit or hold
  -> approved payment instruction
  -> funded settlement
  -> entity-specific accounting
  -> correction, dispute and legal discharge
```

The target is **bounded straight-through processing with a constitutional exception path**, not unconditional autonomy.

## Control constitution

| Clock | Controlling object | Current authority | Safe automation | Non-collapse rule |
|---|---|---|---|---|
| physical safety | turbine, protection logic, plant and grid state | operator, certified controls and reliability authorities | detect, recommend, simulate and execute bounded control logic | a financial rule may not override a trip, reliability instruction or safe-return decision |
| identity/configuration | asset, component, sensor, software and model version | owner/OEM records and configuration management | bind evidence to the correct object and version | identity does not prove condition, ownership, origin or sanctions state |
| measurement/evidence | SCADA, historian, revenue meter, test and inspection record | approved meter/test procedure, engineer, operator, ISO/RTO or contract administrator | collect, normalize, sign provenance and detect anomalies | raw telemetry and model output are not automatically contractual truth |
| diagnosis/work | alert, diagnosis, work order, permit and technician action | owner/OEM engineering and operating process | recommend work, reserve parts, schedule labor and assemble records | an AI alert is not causation, warranty coverage or return-to-service approval |
| contractual obligation | LTSA, EPC, PPA, tariff, SLA and warranty | parties, tariff administrator, court or arbitrator | calculate objective fees, credits, penalties and claims from approved evidence | force majeure, causation, exclusions and disputed acceptance remain governed judgments |
| compliance | origin, ECCN, ownership, counterparty, sanctions and license state | law, licenses, public authorities and compliance officers | screen continuously, apply time-versioned policies and impose preflight holds | ledger confirmation cannot make a prohibited export, service or payment lawful |
| payment instruction | invoice, claim, debit, credit and escrow release | contract and treasury permissions | create or release an instruction when predicates pass | instruction is not funding or settlement |
| funding/settlement | deposit, reserve balance, token, prefunded balance and collateral | banks, issuers, central banks and platform rules | reserve liquidity, link transfers and shorten exposure/reconciliation | atomicity cannot create liquidity, credit, loss-bearing capacity or legal discharge |
| accounting/tax | revenue, expense, capital asset, reserve, impairment and tax basis | entity policies, auditors, regulators and law | generate consistent entity-specific entries from a canonical event | cash movement does not determine recognition, capitalization, valuation or consolidation |
| correction/enforcement | dispute, reversal, freeze, seizure, forfeiture and judgment | contract governors, courts, regulators and sanctions administrators | pause, preserve evidence, route exceptions and execute authorized corrections | protocol finality is not legal unassailability |

## What the primary record already establishes

### Physical events already create financial obligations

A Guernsey Power filing describes a GE service agreement with a monthly fixed fee and a variable fee tied to gas-turbine fired hours. A separate SEC-filed GE equipment contract makes delivery delay, output, heat rate and emissions performance financially operative through governed tests and specified operating conditions.

**Boundary:** these are deployed contractual mechanisms. They do not show a raw sensor tick or token transfer settling the obligation automatically.

### Grid measurements already drive financial calculations

FERC Order 825 aligns real-time dispatch and financial settlement at five-minute intervals. PJM's capacity-market rules use metered performance to calculate shortfalls, charges and bonuses, with validation, substitution and correction procedures.

**Boundary:** physical-to-financial calculation exists. Market calculation, invoice, collateral movement, bank payment and final cash settlement remain different states.

### EAM already creates bills, credits and claims

IBM Maximo supports work-order and service billing, SLA penalties and credits, warranty claims, project milestones, customer review, disputed lines and transfer to accounts-payable systems. Maximo 9.2 adds asset-first AI, condition insight and agentic workflow across EAM, ERP and IoT.

**Boundary:** EAM can create the commercial object. The recovered product documentation does not show Maximo supplying the final settlement asset or turning turbine telemetry into irrevocable cash.

### Programmable commercial-bank money is live

JPMorgan's Kinexys materials describe predefined cash movement triggered by external data and operational events; Siemens is an operating programmable-payments client. Citi's tokenized-deposit cash service is live, while its Maersk trade-finance use was a pilot.

**Boundary:** programmable cash rails exist, but no official source recovered in this research joins a named production turbine, LTSA or EAM state to those rails.

### Physical-data-linked instruments remain a precedent, not the final join

EnergyTag uses verified hourly meter data for granular energy certificates with correction and withdrawal rules. BIS Project Genesis 2.0 prototyped IoT-linked environmental instruments, and BIS unified-ledger work describes real-world contingencies entering atomic asset/cash transitions through oracles and APIs.

**Boundary:** the pieces exist separately. A named production turbine event-to-final-money deployment is not established.

## Best first uses

| Use | Governing fact | Suitable automation posture |
|---|---|---|
| fired-hour or cycle LTSA fee | approved usage meter, asset identity and correction rule | calculate automatically; release after an exception window |
| availability/SLA credit | governed outage state, duration and exclusions | create a provisional credit; preserve adjudication |
| performance bonus or liquidated damages | approved acceptance test and corrected report | settle from the approved result, not live SCADA |
| warranty reimbursement | coverage, causation, authorized repair and completed work | assemble the claim automatically; retain coverage approval |
| parts acceptance escrow | part identity/origin, title, license, shipment, inspection and rejection rights | strong conditional-release candidate |
| construction or inspection milestone | signed engineer/inspector record and defined acceptance criteria | strong conditional-release candidate |
| low-risk consumables | approved vendor, inventory threshold, spend limit and compliance screen | bounded machine authority with a human exception queue |
| energy attribute | approved revenue meter and certificate correction/cancellation rule | automate certificate state; do not equate it with cash settlement |

## Minimum production design

Every joined system should preserve:

1. unique asset, component and event identifiers;
2. the source system and signed actor identity;
3. calibration and configuration versions;
4. the effective contract, tariff or policy version;
5. counterparty and beneficial-owner screening;
6. origin, ECCN and export-license state where relevant;
7. funding and settlement-asset reservation;
8. an explicit pause and exception authority;
9. correction, clawback, setoff and dispute rules;
10. separate owner, OEM, regulator, bank and accounting views; and
11. a hard rule preventing financial agents from writing into safety-critical OT controls.

## Return gates

Reopen and strengthen this map when the primary record supplies:

- a named production site, asset, event schema, governing contract, settlement rail and transaction record linking a turbine event to money;
- an operative LTSA/EPC/PPA showing meter authority, formulas, exclusions, setoff, force majeure, sanctions, dispute and correction terms;
- an identity/signature architecture covering credential issuance, revocation, calibration, configuration and compromise;
- a rule deciding which model controls when owner and OEM diagnoses disagree;
- account/issuer rules naming the settlement asset, liquidity provider, prefunding, insolvency treatment and loss allocation; or
- production correction rules covering holds, setoff, clawback, compensating payments, disputes, appeals and accounting restatement.

The joined-management thesis weakens if authoritative operational events cannot be agreed across owner/OEM boundaries, correction costs exceed reconciliation savings, liquidity requirements erase the benefit, institutional users reject the shared record, or OT safety requires a permanent separation that prevents operational evidence from authorizing any commercial state.

## Primary sources

- [Guernsey Power filing describing GE fired-hour service fees](https://www.sec.gov/Archives/edgar/data/1622536/000162253625000013/ex994guernseypowerholdings.htm)
- [SEC-filed GE equipment contract](https://www.sec.gov/Archives/edgar/data/1023734/000110465908069377/a08-25613_1ex10d11.htm)
- [FERC Order 825](https://www.ferc.gov/sites/default/files/2020-05/settlement825.pdf)
- [PJM Manual 18](https://learn.pjm.com/-/media/DotCom/documents/manuals/m18.ashx)
- [PJM billing, settlements and credit](https://www.pjm.com/markets-and-operations/billing-settlements-and-credit.aspx)
- [IBM Maximo service-provider module](https://www.ibm.com/docs/en/maximo-for-aviation/7.6.8?topic=applications-service-provider-module)
- [IBM Maximo billing](https://www.ibm.com/docs/en/maximo-for-aviation/cd?topic=billing-services)
- [IBM Maximo warranty workflow](https://www.ibm.com/support/pages/how-can-i-optimize-benefits-my-asset-warranties-aka-saving-money-asset-maintenance)
- [IBM Maximo Application Suite 9.2](https://www.ibm.com/new/announcements/introducing-maximo-application-suite-9-2)
- [JPMorgan programmable payments](https://www.jpmorgan.com/kinexys/programmable-payments)
- [JPMorgan Siemens deployment](https://www.jpmorgan.com/payments/newsroom/kinexys-siemens-b2c2-blockchain-fx-mandates)
- [Citi Token Services integration](https://www.citigroup.com/global/news/press-release/2025/citi-integrates-citi-token-services-with-24-7-usd-clearing-real-time-cross-border-payments-liquidity-management)
- [EnergyTag hourly-energy accounting initiative](https://energytag.org/projects/global-hourly-energy-accounting-initiative/)
- [BIS Project Genesis 2.0](https://www.bis.org/publ/othp58.htm)
- [BIS unified-ledger blueprint](https://www.bis.org/publ/arpdf/ar2023e3.htm)

## Related research

- DLT Energy-Finance Convergence Timeline
- Iran Energy Settlement — Stress Test
