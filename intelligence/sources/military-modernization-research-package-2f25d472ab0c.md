# Military Modernization — Research Package

**Status:** `pending`  
**Cutoff:** 2026-07-15  
**Scope:** the command, data, communications, space, AI, autonomy, continuity and acquisition architecture of the U.S. military  
**Method:** primary-source factual spine first; synthesis and vault routing kept separate

## Short answer

The useful story is not “the military is buying new weapons.” It is that the Department is reorganizing around a shared **sensor → transport → data → decision → effect → sustainment** chain.

The strongest current evidence is organizational and contractual:

- the Army has moved Next Generation Command and Control (NGC2) from prototyping toward delivery around a named common data baseline led by Anduril, Palantir and Raft;
- the Navy created Portfolio Acquisition Executive Mission Systems as a central integrator for Overmatch, long-range fires, C4I, digital services, logistics and multiple systems commands;
- Space Development Agency's proliferated low-Earth-orbit architecture is joining missile sensing, low-latency transport, tactical data links and battle management;
- the Department's 2026 AI strategy expressly includes AI agents for battle management, decision support and “kill chain execution”;
- cloud, identity, zero trust, software delivery and data rights are now warfighting infrastructure rather than back-office IT;
- strategic continuity is being recapitalized through the E-4C Survivable Airborne Operations Center, Evolved Strategic SATCOM, TACAMO and supporting NC3 services;
- acquisition reform is changing the machinery that decides which commercial technology crosses from prototype into the force.

This is a real Freedom 250 crosscut. It is **not** grounds for a new top-level plotline.

## Read order

1. `MILITARY_MODERNIZATION_FIELD_REGISTRY.md` — ontology, status rules and clocks.
2. `MILITARY_COMMAND_DATA_CONTROL_STACK.md` — the integrated architecture.
3. `MILITARY_MODERNIZATION_ENTITY_PROGRAM_REGISTRY.md` — who owns each function and program.
4. `MILITARY_MODERNIZATION_TRANSITION_TIMELINE.md` — occurred, contracted, fielded and scheduled events.
5. `MILITARY_MODERNIZATION_CLAIM_AUDIT.md` — corrections and non-findings.
6. `MILITARY_MODERNIZATION_VAULT_INTEGRATION_MAP.md` — what belongs in the live vault.
7. `MILITARY_MODERNIZATION_SOURCE_WATCHBOARD.md` — sources and promotion triggers.

## Strongest findings

### 1. The data layer is becoming an acquisition object

On 2026-06-22 the Army announced an NGC2 common data-layer baseline after operational validation. Anduril leads the baseline; Anduril's Lattice and Palantir's Foundry provide the edge-to-cloud data mesh; Raft provides data and service registries, transformation tools and federation. This is more load-bearing than a generic AI announcement because it names the responsible vendors, the interface functions, the divisions implementing it and the next validation gate.

Primary source: [Army NGC2 common data baseline](https://www.army.mil/article-amp/293409/army_and_industry_align_on_common_data_baseline_as_next_generation_command_and_control_moves_from_prototyping_to_delivery)

### 2. “Integration” is being reorganized into an owned mission

The Army's Right to Integrate program treats interoperability as a capability rather than a late engineering task. The Navy's new PAE Mission Systems is explicitly the central integrator for mission-critical systems and kill-chain closure. The institutional change matters: program offices and reporting lines are being redrawn around end-to-end mission threads rather than isolated platforms.

Primary sources: [Army Right to Integrate](https://www.army.mil/article/292189/army_and_defense_sector_announce_right_to_integrate_hackathon_sprint_for_shared_technology); [Navy PAE Mission Systems](https://www.navwar.navy.mil/Media/Article-Display/Article/4483415/department-of-the-navy-launches-pae-mission-systems-to-accelerate-warfighting-c/)

### 3. Commercial firms are inside the architecture, but the control objects remain split

Commercial cloud, software, satellite, antenna, data-platform and autonomy providers are no longer merely selling office tools. They supply components used from enterprise networks to the tactical edge. That does **not** mean a vendor owns the mission, the government data, targeting authority or the whole network. Contract rights, data rights, technical administration, mission command and operational authorization must remain separate.

Primary sources: [JWCC awards](https://dodcio.defense.gov/In-the-News/Article/3267572/department-names-vendors-to-provide-joint-warfighting-cloud-capability/); [Open DAGIR](https://www.defense.gov/News/Releases/Release/Article/3791829/cdao-announces-new-approach-to-scaling-data-analytics-and-ai-capabilities/); [Space Force Commercial Space Strategy](https://www.spaceforce.mil/Portals/2/Documents/Space%20Policy/USSF_Commercial_Space_Strategy.pdf)

### 4. Space is the joint transport and sensing layer, not a separate theatre

SDA calls the PWSA Transport Layer the space backbone for JADC2. Tracking satellites feed a low-latency communications network; battle-management software is hosted across the architecture. The 2026-07-13 awards for 36 additional Tranche 3 tracking satellites connect Golden Dome directly to the proliferated architecture, with future Space Force operations and sustainment.

Primary sources: [PWSA Transport Layer fact sheet](https://www.sda.mil/wp-content/uploads/2024/08/Transport-Layer-Fact-Sheet_V6.9-distro-A.pdf); [2026-07-13 AMDT3 awards](https://www.sda.mil/space-development-agency-issues-awards-to-build-36-accelerated-missile-defense-tracking-layer-satellites-for-tranche-3-in-support-of-golden-dome-for-america/)

### 5. AI is being aimed at the decision chain

The 2026 AI strategy's Agent Network priority is for AI-enabled battle management and decision support from campaign planning to kill-chain execution. Open Arsenal seeks to shorten intelligence-to-capability time. The same memorandum directs component data catalogues, gives CDAO power to direct release of Department data to cleared users with valid purpose subject to security rules, requires denials to be justified and escalated, calls for current commercial models to be deployable within 30 days of public release, and requires modular interfaces/documentation sufficient for third-party integration without prime-contractor support. These are unusually concrete control and tempo directives. They are not proof of autonomous operational control or successful implementation.

Primary source: [2026 Artificial Intelligence Strategy](https://media.defense.gov/2026/Jan/12/2003855671/-1/-1/0/ARTIFICIAL-INTELLIGENCE-STRATEGY-FOR-THE-DEPARTMENT-OF-WAR.PDF)

### 6. Continuity is a separate, harder network

Ordinary warfighting IT, tactical C2 and nuclear command, control and communications are not interchangeable. NC3 includes survivable airborne, satellite, terminal, conferencing and command services designed to remain available through nuclear and non-nuclear attack. The E-4C, Evolved Strategic SATCOM and E-130J TACAMO programmes are separate recapitalization clocks.

Primary sources: [FY2026 Defense Budget Overview](https://comptroller.defense.gov/Portals/45/Documents/defbudget/FY2026/FY2026_Budget_Request_Overview_Book.pdf); [DISA FY2026 budget](https://comptroller.defense.gov/Portals/45/Documents/defbudget/FY2026/budget_justification/pdfs/01_Operation_and_Maintenance/O_M_VOL_1_PART_1/DISA_OP-5.pdf)

### 7. Modernization includes cancellation and fallback

The Space Force accepted GPS OCX contractually in 2025, then cancelled the programme in April 2026 after integrated testing found operational risk. It chose incremental upgrades to the existing control system. This is the best corrective to the idea that every announced upgrade proceeds linearly into operations.

Primary source: [Space Force OCX termination](https://www.spaceforce.mil/News/Article-Display/Article/4465024/ussf-terminates-program-for-the-global-positioning-system-next-generation-opera/)

## Controlling synthesis

The emerging military machine is best understood as a **federated decision fabric**:

> many sensors + many transports + shared data rules + distributed compute + identity gates + human command + networked effects + contested logistics + strategic fallback

It is neither one network nor one vendor platform. Its power and fragility sit at the interfaces:

- which sensor observations can enter;
- which data model becomes authoritative;
- which identities and devices are trusted;
- which vendor can update or administer a component;
- which commander sees the common picture;
- which communications path survives disruption;
- which system may nominate, approve or execute an effect;
- which supply, maintenance and finance records keep the force moving.

## Vault posture

Keep this full package in the Observatory research workspace. Promote only discrete events that change:

- a responsible entity or reporting line;
- a common architecture, data baseline or interface standard;
- a contract or production obligation;
- a prototype/fielding/operational state;
- a commercial dependency or government data-right boundary;
- a continuity or emergency capability;
- a programme's survival, cancellation or replacement path.

General speeches, exercises without a state change, vendor marketing and broad budget rhetoric stay in the source bench.

## Next phase after this package

The next useful expansion is **contested logistics and the military industrial metabolism**: fuel, power, ports, sealift, prepositioned stocks, maintenance data, additive manufacturing, microreactors, munitions capacity and the financial/contract rails beneath mobilisation. That should be a separate factual package, joined to this one through the sustainment layer rather than folded into it.
