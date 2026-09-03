# Turbine Asset Management and U.S. Buildout — Source Document

## Controlling ruling

The United States is contracting a large 2027-and-later turbine and service wave now, but the order book is expanding much faster than the operating fleet. The digital operating layer is also advancing quickly, though not as a single jump to autonomous plants. Remote monitoring, anomaly detection, plant-specific performance models and controlled-work systems are established. Computer vision, robotic inspection, maintenance copilots and workflow agents are moving into production or early deployment. AI already makes narrow closed-loop adjustments inside engineered safety envelopes. General-purpose AI authority over turbine protection, component life, maintenance approval or return to service is not established.

The durable model is therefore:

`physical signal -> contextualized condition -> anomaly -> diagnosis -> engineering decision -> controlled work -> validation`

Measurement and anomaly detection are substantially automated. Diagnosis and work preparation are increasingly AI-assisted. High-consequence engineering, safety, compliance and return-to-service authority normally remain explicit human gates.

## Scope and evidence posture

This note covers the U.S. physical buildout, with global OEM evidence used only to establish manufacturing pressure, service-fleet scale or technology maturity relevant to U.S. projects. Gas turbines and combined-cycle plants are the main lane. Wind is the comparison lane because distributed-fleet monitoring, inspection and robotics are often deployed at greater scale there.

Government, regulator and owner records control physical project state. Public-company filings and named contract records establish OEM order, backlog and manufacturing states. Vendor documentation establishes what a vendor offers or reports deploying; it is not independent proof of customer savings, fleet-wide adoption or transferred operating authority. Research and demonstration records establish bounded validation, not general production status.

## The operating technology stack

| Layer | Working technology | Function | Authority boundary |
|---|---|---|---|
| Asset and measurement | Turbine, generator, HRSG, auxiliaries; pressure, temperature, vibration, combustion, emissions, electrical and inspection sensors | Produces power and observes condition | Every signal must resolve to the correct unit, component, configuration, units and time. |
| Protection and control | Turbine controller, DCS, PLC, protection and trip logic | Executes deterministic control and safe shutdown | AI does not inherit permission to bypass or rewrite certified protection. |
| Edge and history | Secure gateways, industrial protocols, historians, asset hierarchy, configuration and work history | Moves and contextualizes operational data | Connectivity expands cyber, identity and change-control risk. |
| Fleet monitoring | OEM or owner remote center, fleet benchmarking, alerts and case management | Detects deviations and brings remote expertise to the site | Remote monitoring is not remote operating authority. |
| APM and digital twins | Rules, normal-behavior models, physics models, fault libraries, performance and remaining-life analytics | Estimates health, degradation, performance loss and candidate failure modes | A twin is authoritative only for its represented configuration, condition and purpose. |
| EAM/CMMS | Asset master, notification, work order, inspection, labor, parts, cost and closeout | Converts an approved need into controlled work and durable history | A software transaction does not prove diagnosis, work quality or restoration. |
| Commercial layer | Warranty, LTSA, outage plan, spares, dispatch value, lifecycle capital and portfolio ranking | Connects physical state to service, risk and money | Physical work, contract coverage, accounting recognition and cash are separate objects. |
| AI interface | Vision, anomaly detection, retrieval, workflow agents, scheduling and bounded optimization | Automates defined observations, analyses or actions | Authority must be granted for each use case; “AI-enabled” does not mean autonomous. |

The limiting object is often not the model but the plant's information constitution: correct asset and tag identity; synchronized and calibrated sensors; configuration, repair and software history; a common fault/work taxonomy; integration with parts, cost and outage workflows; approved remote access; an accountable decision owner; and feedback from as-found condition and post-work performance.

## Deployment ruling: now, next and unproven

### Deployed at commercial scale

- **Remote monitoring and anomaly detection.** GE Vernova reports more than 1,000 monitored generation plants; Siemens Energy reports more than 800 monitored power units; MHI reported 144 TOMONI-connected thermal units by August 2023. These are vendor-reported fleet counts, but they are plainly beyond pilot status. Sources: [GE Vernova APM](https://www.gevernova.com/software/products/asset-performance-management/cloud-edge), [Siemens Energy performance monitoring](https://www.siemens-energy.com/global/en/home/products-services/product/omnivise-performance-monitoring.html), [MHI Technical Review](https://www.mhi.co.jp/technology/review/pdf/e604/e604030.pdf).
- **Purpose-specific digital twins and predictive maintenance.** EPRI describes fault-inference twins implemented at several gas and nuclear plants, records sensor and model failure modes, and gives a typical implementation interval of six to twelve months. This is production readiness for defined scopes, not one complete digital replica of an asset. Source: [EPRI Plant Modernization Toolbox](https://nuclearplantmod.epri.com/MTA-EN-015).
- **Bounded closed-loop optimization.** GE's Autonomous Tuning changes aeroderivative combustion targets every two seconds within existing safety-critical logic. MHI identifies autonomous combustion-dynamics and cooling-air optimization at T-Point 2. These are real closed loops inside narrow engineered envelopes, not authority over trips, life extension or return to service. Sources: [GE Autonomous Tuning](https://www.gevernova.com/software/products/asset-performance-management/gas-turbine-tuning), [Mitsubishi Power TOMONI](https://power.mhi.com/service/tomoni/smarter).
- **Inspection automation.** GE reports a named thermal-plant ANYmal deployment collecting visual, thermal, acoustic and gas data and feeding APM. In wind manufacturing, GE reported more than 9,000 Digital Blade Certificates after robotic and AI-assisted inspection by April 2026; human reviewers still adjudicated flagged areas. Sources: [GE robotic inspection](https://www.gevernova.com/software/customer-stories/robotic-inspection-data-apm-improves-safety-availability-and-efficiency), [GE two-year review](https://www.gevernova.com/news/articles/two-years-ge-vernova-reshaping-energy-future).
- **Scaled wind fleet analytics.** Vestas reports more than 128 GW and 55,000 turbines on Scipher. RWE says its TPA Next Evolution analysis system is implemented across its full OPEA wind fleet and assists analysts across multiple condition-data modules. Sources: [Vestas Scipher](https://www.vestas.com/en/energy-solutions/service/digital-services/scipher), [RWE digital energy production](https://www.rwe.com/en/research-and-development/digitalisation-at-rwe/digital-energy-production/).

### Moving into the work layer now

- IBM launched Maximo Condition Insight in December 2025 and Maximo 9.2 agentic workflows in June 2026. The products interpret condition data, retrieve operational context, recommend action and orchestrate controlled workflows. Product availability does not establish owner adoption or delegation of safety authority. Sources: [IBM Condition Insight](https://www.ibm.com/new/announcements/maximo-condition-insight), [IBM Maximo 9.2](https://www.ibm.com/new/announcements/introducing-maximo-application-suite-9-2).
- Robotic field inspection is progressing from demonstration to named deployments faster than robotic repair. RWE, DTU and Quali Drone completed an autonomous visual and infrared inspection of an operating, rotating offshore turbine in January 2026. That is a completed demonstration, not a fleet-wide operating state. Source: [RWE AQUADA-GO](https://dk.rwe.com/en/press-and-news/2026-01-15-first-autonomous-inspection-of-operational-offshore-wind-turbines-demonstrated/).
- New plants can preserve commissioning baselines, configuration history, tag identity, secure data access and an integrated asset/work model from the beginning. That makes later analytics, digital twins and continuous finance easier, but it does not establish that every new turbine receives those systems or an LTSA.

### Exceptional or not established

- Siemens Energy and Volkswagen completed a certified 72-hour unattended gas-and-steam plant test in October 2025 after plant-specific hazard analysis and with protection trips retained. The case establishes technical feasibility inside a deliberately engineered envelope, not ordinary fleet practice. Source: [Siemens Energy / Volkswagen reference](https://www.siemens-energy.com/global/en/home/references/vw-power-plant-autonomy72.html).
- DOE CESER released Stormbreaker in July 2026 specifically to test LLM and agent failure modes in dynamic power and operational-technology environments. The existence of the testbed is evidence against assuming that a fluent general agent is ready for safety-significant control. Source: [DOE CESER](https://www.energy.gov/ceser/articles/ceser-releases-new-testbed-advance-llm-and-agentic-ai-evaluation-critical).
- DOE/NREL's offshore-wind O&M roadmap places fully autonomous inspection and intervention in a 2032–2036 research horizon. The roadmap is not a deterministic market forecast, but it is consistent with the present distinction between scaled decision support and unproven general autonomy. Source: [DOE/NREL offshore O&M roadmap](https://www.energy.gov/sites/default/files/2024-05/operations-maintenance-roadmap-us-offshore-wind.pdf).

## The physical buildout clocks

These states must never be collapsed:

| Clock | Evidence that establishes it | It does not establish |
|---|---|---|
| Market interest | Request, proposal or development announcement | Customer commitment or factory capacity |
| Slot reservation | OEM and customer hold a future production slot under stated commercial terms | Firm order, financing, approval or construction |
| Firm equipment order | Executed supply contract enters OEM backlog | Permit, final investment decision, site work or operation |
| Offtake or load agreement | PPA, tolling or large-load service agreement | Complete project documents, permits or construction |
| Regulatory approval or permit | CPCN, IRP approval, air permit or other named authorization | Notice to proceed or physical construction |
| Construction | Owner or regulator confirms site work or installation | Mechanical completion, commissioning or operation |
| Commissioning | Testing, synchronization and performance acceptance | Commercial operation unless the owner or regulator declares it |
| Commercial operation date | Owner, regulator or EIA identifies the unit as operating | Any particular APM, twin, AI or service function |
| Digital-service adoption | Named owner/OEM record identifies the installed system, asset, use and authority | Independent performance validation or autonomous authority |

EIA reported 86 GW of planned U.S. utility-scale additions for 2026, including 6.3 GW of gas capacity—3.3 GW combined cycle and 2.8 GW combustion turbine—and roughly 14% wind. The inventory is preliminary and may be revised; “actual additions” can include uprates or corrections rather than only greenfield units. Sources: [EIA planned additions](https://www.eia.gov/todayinEnergy/detail.php?id=67205), [EIA-860M](https://www.eia.gov/electricity/data/eia860m/index.php).

The queue is a pressure signal, not a construction ledger. Lawrence Berkeley National Laboratory counted 253 GW of gas in active interconnection queues at year-end 2025, but only 18% had a draft or executed interconnection agreement. Historically, 13% of capacity entering queues in 2000–2020 was operating by the end of 2025, and the median request-to-operation interval exceeded five years. Source: [DOE/LBNL queue report](https://emp.lbl.gov/news/backlog-power-plants-seeking-transmission-grid-connection-eased-somewhat-2025-amidst).

OEM commercial pressure is much larger than near-term U.S. COD capacity, but its measures are incompatible and cannot be added. GE Vernova reported 116 GW of gas-equipment backlog plus slot reservations in July 2026; Siemens Energy reported 87 GW of gas commitments in May 2026, including 24 GW related to data centers; MHI reported 35 large-frame orders during FY2025. These are global measures mixing different commercial states. GE separately said reservation-to-order conversion typically takes roughly six to eighteen months and that most recent orders deliver in 2027 and later. Sources: [GE Vernova Q2 2026](https://www.gevernova.com/news/articles/ge-vernova-releases-second-quarter-2026-financial-results), [Siemens Energy Q2 FY2026](https://assets.siemens-energy.com/dam/41a65182-38a3-48d9-a4ee-b4480041e3f9/2026-05-12_Q2_Analyst_presentation_final-pdf_Original%20file.pdf), [MHI FY2025](https://www.mhi.com/finance/library/result/pdf/fy20254q/presentation.pdf), [GE Vernova BofA conference](https://www.gevernova.com/sites/default/files/ge-vernova-bofa-global-industrials-conference-2026.pdf).

## Representative U.S. project states at the cutoff

| Project | Established state | Next clock | Ruling |
|---|---|---|---|
| Pin Oak Creek, Texas | Commercial operation on 2026-04-30 | Operating/service history | Owner-declared COD. [Constellation](https://investors.constellationenergy.com/news-releases/news-release-details/constellation-reports-first-quarter-2026-results) |
| T.H. Wharton, Texas | 415 MW entered commercial operation on 2026-05-26 | Performance-grant testing | Owner-declared COD. [NRG](https://investors.nrg.com/news-releases/news-release-details/nrg-energy-reports-second-quarter-2026-results-and-reaffirms) |
| Cedar Bayou 5 and Greens Bayou 6, Texas | Construction | Mid-2028 target COD | Construction and target clocks only. [NRG](https://investors.nrg.com/news-releases/news-release-details/nrg-energy-reports-second-quarter-2026-results-and-reaffirms) |
| Plant Yates Units 8–10, Georgia | Construction; major equipment for Units 8 and 9 delivered by December 2025 | All three targeted online by end-2027 | Delivery is not operation. [Georgia Power](https://www.georgiapower.com/news-hub/press-releases/turbine-generator-unit-9-plant-yates.html) |
| Homer City, Pennsylvania | Seven GE 7HA.02 turbines under firm order; permit/site activity | Construction completion then targeted in 2027 | Order and site activity do not establish completed capacity. [GE Vernova](https://www.gevernova.com/news/press-releases/ge-vernova-adding-250-new-jobs-part-pennsylvania-factory-expansion-manufacture-more), [Pennsylvania DEP](https://www.pa.gov/agencies/dep/dep-regions/northwest-regional-office/homer-city-generation-redevelopment) |
| Duke Anderson County, South Carolina | Regulatory approval | Construction anticipated in 2027; service targeted for 2031 | Approval is not construction. [Duke Energy](https://news.duke-energy.com/releases/regulators-approve-duke-energys-proposal-for-new-natural-gas-generation-to-support-south-carolinas-growing-energy-needs) |
| Kilby, Texas | Twenty-year PPA; development and permitting | FID expected by end-2026; first power targeted for 2028 | The PPA does not establish FID, construction or 2.67 GW of operating capacity. [Project owner](https://kilby.com/project/) |

## Lender and finance handoff

The asset-management stack can become the physical evidence layer for continuous underwriting and programmable project finance, but it is not financing by itself. The important bridge is an authenticated change of state that all relevant contracts recognize.

Potential finance-grade events include an accepted firm order, permit issuance, equipment delivery, certified construction milestone, commissioning test, COD, metered generation, warranty event, completed inspection and validated work closeout. To move from useful telemetry to a lender-recognized event, the system still needs:

1. durable asset and component identity;
2. an authorized signer, sensor or inspection system;
3. preserved source data, configuration and correction history;
4. an explicit contractual consequence, such as a draw release, borrowing-base change, reserve transfer, covenant exception or payment hold;
5. agreed engineering, OEM, insurer and lender authority boundaries; and
6. a dispute, reversal and loss-allocation procedure.

A sensor signal or AI finding therefore may **inform** a borrowing base, payment or reserve decision before it is allowed to **cause** one. The strongest near-term implementation is likely automated evidence collection and exception detection, followed by human approval of consequential credit and cash actions. New-build projects have an advantage because these identities, access rights and event schemas can be written into equipment, EPC, service, insurance and financing agreements before commissioning.

## Exact negatives

The primary record reviewed does **not** establish that:

- AI is autonomously running U.S. turbine fleets;
- a remote monitoring center has remote operating authority;
- an anomaly score is a diagnosis, approved maintenance decision or return-to-service authorization;
- a digital twin is one complete and authoritative representation of an asset;
- every new turbine includes APM, a twin, remote monitoring, robotic inspection or an LTSA;
- a product launch proves owner adoption, savings or safe control-room use;
- predictive maintenance eliminates inspection or transfers engineering authority to a model;
- a reserved manufacturing slot is a firm order or a plant under construction;
- interconnection-queue capacity is a forecast of construction or completion;
- the GE, Siemens and MHI global commercial measures form one additive U.S. buildout total; or
- a machine event currently changes loan rights, collateral or cash without governing-contract recognition.

## Return gates

Reopen or promote the state only on the following evidence:

- **Physical project:** an owner, regulator or EIA moves a named unit from reservation or order to approval, construction, commissioning or COD; record each transition separately.
- **Digital attachment:** a named owner or contract identifies the actual plant or fleet, system, operating use and service scope—not merely an OEM capability page.
- **Predictive performance:** prospective results disclose as-found condition, false-positive and false-negative behavior, and the work or outage decision changed.
- **Control authority:** a regulator, inspection authority, insurer or owner record states the manipulated variable, safety envelope, fallback, abnormal-condition evidence and accountable authority.
- **Agentic work:** a named operator shows whether an AI drafts, recommends, approves or executes, with controlled-work and audit evidence.
- **Finance bridge:** governing loan, security, insurance, EPC, LTSA or account documents recognize a signed physical event as a covenant, collateral, draw, reserve or payment trigger and allocate error and reversal risk.

Until one of these gates fires, keep the current ruling: the physical and digital buildouts are both moving quickly, but reservation, order, permit, construction, COD, digital deployment and operating authority remain different clocks.
