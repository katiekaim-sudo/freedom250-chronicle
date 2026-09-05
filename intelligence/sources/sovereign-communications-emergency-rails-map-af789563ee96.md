# Sovereign Communications — Emergency Rails Map

**Status:** `pending`  
**Cutoff:** 2026-07-15  
**Scope:** congestion, outage, disaster, public warning, restoration, continuity, national emergency and war

## 1. The activation ladder

| Tier | Condition | Main legal/operating change | What does not automatically happen |
|---|---|---|---|
| 0 — standing readiness | normal operations | WPS/GETS enrollment, TSP coding, FirstNet priority, EAS/IPAWS tests, PACE planning, SHARES readiness | no declared incident; no public takeover |
| 1 — congestion/local outage | network is busy or impaired | WPS/GETS call priority; carrier repair; NORS if thresholds are met; local mutual aid | no Stafford declaration required for standing priority tools |
| 2 — FCC/state disaster activation | FCC activates DIRS/MDRI or qualifying state/ESF trigger occurs | mandatory covered-provider DIRS reports; mobile disaster roaming/mutual aid; restoration status | no transfer of network title |
| 3 — federal incident response | Stafford or other federal response; ESF #2 activation | FEMA/CISA government-industry coordination, tactical support, deployables, infrastructure restoration help | CISA does not become the owner of private networks |
| 4 — NSEP/national emergency | executive NSEP functions and formal priority/resource tools | national coordination, priority communications, possible DPA-rated orders or allocations under the proper authority | not every emergency invokes DPA or 47 U.S.C. § 606 |
| 5 — war/threat of war and statutory findings | President invokes the required §606 conditions | priority directions and, within statutory bounds, closing/use/control of specified radio or wire facilities with compensation | not a permanent title transfer; scope and trigger matter |

## 2. Standing rails: available before a declaration

### Government Emergency Telecommunications Service — GETS

**Function:** priority treatment for authorized calls through landline and long-distance network segments during congestion or degradation.  
**User object:** an enrolled person with a PIN; calls can originate from ordinary phones.  
**Operator:** participating service-provider networks under the federal priority-services structure.  
**Limit:** priority raises completion odds; it does not repair a cut cable or guarantee the call.

Source: [CISA Priority Telecommunications Services](https://www.cisa.gov/sites/default/files/publications/pts-fact-sheet-022022-508.pdf).

### Wireless Priority Service — WPS

**Function:** priority calling for authorized cellular devices, invoked with the service code or supported dialer.  
**Manager/rules:** CISA manages; FCC rules and categories govern; carriers participate.  
**Important limit:** WPS calls do not pre-empt calls already in progress and do not deny public use. All WPS calls outrank ordinary calls in congestion; categories allocate priority among WPS users in extreme cases.  
**Declaration:** not required; WPS is a standing capability.

Source: [CISA WPS](https://www.cisa.gov/resources-tools/services/wireless-priority-service-wps).

### Telecommunications Service Priority — TSP

**Function:** priority provisioning and restoration of enrolled critical voice and data circuits.  
**Object:** the circuit/service, not merely a person or phone.  
**Effect:** service vendors must put coded work ahead of lower-priority work, including ordinary service-level commitments.  
**Limit:** TSP does not create a spare physical route; route diversity and power still matter.

Sources: [CISA WPS portal description of TSP](https://www.gwids.cisa.gov/WPSWelcome/); [CISA priority-services brochure](https://www.cisa.gov/sites/default/files/publications/Priority%20Telecommunications%20Services%20Brochure_0.pdf).

### FirstNet priority and pre-emption

**Function:** eligible public-safety traffic uses a dedicated core, always-on priority and pre-emption within the FirstNet service architecture.  
**Difference from WPS:** FirstNet can include pre-emption of lower-priority traffic; WPS does not drop calls already in progress.  
**Operator:** AT&T under FirstNet Authority oversight.  
**Limit:** radio-site power, backhaul, device condition and coverage can still fail.

Source: [FirstNet Authority](https://firstnet.gov/about).

## 3. Outage visibility rails

### Network Outage Reporting System — NORS

**Function:** covered communications providers report service disruptions that meet FCC Part 4 thresholds.  
**Information:** notification, initial and final outage data; filings are generally protected because they expose network vulnerabilities.  
**Use:** FCC reliability analysis, situational awareness and emergency decisions.  
**Clock:** incident threshold and reporting deadlines, not a general emergency declaration.

Source: [FCC NORS description](https://docs.fcc.gov/public/attachments/FCC-12-22A1.pdf).

### Disaster Information Reporting System — DIRS

**Function:** daily infrastructure and restoration status in an FCC-defined disaster area.  
**Trigger:** FCC Public Safety and Homeland Security Bureau activates DIRS for stated geographies, on its own or in coordination with state emergency agencies, FEMA and CISA.  
**Current duty:** since 2025-02-20, covered cable, wireless, wireline and interconnected-VoIP providers must file daily when DIRS is activated where they serve, plus a final report after deactivation. NORS duties are suspended for qualifying outages reported in DIRS.  
**Separate rail:** DIRS Lite remains an informal voluntary process.

Sources: [FCC compliance date](https://docs.fcc.gov/public/attachments/DA-25-74A1.pdf); [FCC 25-45](https://docs.fcc.gov/public/attachments/FCC-25-45A1_Rcd.pdf).

DIRS gives the government a status picture. It does not itself give the government operational possession of the network.

## 4. Mobile-network disaster rail — MDRI

The Mandatory Disaster Response Initiative applies to facilities-based mobile wireless providers when one of its activation conditions is met.

### Triggers

- an authorized entity activates ESF #2 for the incident;
- the FCC activates DIRS; or
- the FCC Public Safety and Homeland Security Bureau activates MDRI after a qualifying state request and state action.

### Required functions

1. reasonable roaming under disaster arrangements when technically feasible;
2. mutual-aid arrangements among facilities-based mobile providers;
3. reasonable measures for municipal preparedness and restoration;
4. reasonable measures for consumer readiness;
5. public and stakeholder information on service and restoration.

Source: [FCC MDRI rule](https://docs.fcc.gov/public/attachments/FCC-22-50A1_Rcd.pdf).

### Rights and limits

- A failed-network subscriber may roam on another provider only within the rule's feasibility and capacity conditions.
- The host provider keeps its own-subscriber protection.
- The rule creates a temporary disaster operating duty, not permanent interconnection or network ownership.
- Post-event performance reporting is separate from the live roaming/aid duty.

## 5. Federal response rail — ESF #2 Communications

**Framework:** Emergency Support Function #2 under the National Response Framework.  
**Federal coordination:** CISA coordinates national-level communications infrastructure and service restoration; FEMA coordinates the wider federal incident structure and support.  
**Partners:** FCC, other federal agencies, state/local/tribal/territorial bodies and private communications firms.  
**Functions:** restore critical communications, support incident command, provide tactical communications, assess infrastructure, coordinate industry and government resources, and stabilize cyber/communications services.

Sources: [FEMA ESF #2 course](https://training.fema.gov/is/courseoverview.aspx?amp=&code=IS-802.a&lang=en); [FEMA ESF #2 annex](https://www.fema.gov/sites/default/files/documents/fema_NRF-ESF-2-annex_102021.pdf).

### Incident chain

> local/tribal/state need -> EOC and incident command -> state/federal request or activation -> FEMA coordination -> CISA communications coordination -> FCC regulatory/reporting support -> private operator repair/deployables -> restoration and demobilization

Private firms still normally dispatch crews, reroute traffic, fuel generators and restore facilities. ESF #2 coordinates the field and fills gaps.

## 6. National Coordinating Center and industry interface

The CISA National Coordinating Center for Communications maintains a 24-hour watch and a trusted government-industry environment. Federal agencies and private communications/IT firms share incident information and advice for the NSEP mission. It also links sector coordination, SHARES and mutual-aid tools. Source: [CISA NCC](https://www.cisa.gov/resources-tools/programs/national-coordinating-center-communications).

This is the public-private switchboard of the emergency system. It is not a federal network-operations centre for all private carriers.

## 7. Public-to-responder rail — 911 and NG911

911 is an inbound emergency rail: the public reaches a public-safety answering point or emergency communications centre, which then routes the incident into dispatch and field response.

47 U.S.C. § 615a-1 requires IP-enabled voice providers to provide 911 and enhanced 911 under FCC rules. It also gives such a provider a defined right of access to needed 911 capabilities, including interconnection, on parity terms for the sole purpose of meeting that duty. This is a rare example where an emergency service creates both a provider duty and a narrow infrastructure-access right. Source: [47 U.S.C. § 615a-1](https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title47-section615a-1).

Next Generation 911 replaces legacy analog call delivery with an IP-based system built from Emergency Services IP Networks, NG911 core services, geographic data, call-taking systems and policy/operating procedures. The national goal is an interoperable “system of systems,” not one federally operated call centre. State, local, tribal, carrier and vendor entities retain distinct roles. Sources: [National 911 Program — NG911](https://www.911.gov/issues/ng911/); [NG911 roadmap](https://www.911.gov/projects/ng911-roadmap/).

### Emergency sequence

> caller/device -> originating service provider -> 911 selective routing/NG911 core -> correct PSAP/ECC -> CAD/dispatcher -> responder network -> field unit

### Failure and emergency rights

- Covered service providers have 911 routing/location and outage-notification duties under FCC rules.
- PSAPs/ECCs control call taking and local dispatch under state/local/tribal governance.
- NG911 interconnection and data-sharing rights depend on statute, state plans, standards and contracts.
- TSP may prioritize restoration of 911 circuits; FirstNet and land-mobile radio carry responder traffic after dispatch.
- IPAWS warns a population; it does not replace the public's ability to request aid through 911.

## 8. Public warning rails

### IPAWS operating chain

> authorized alerting authority -> approved alert-origination software -> authenticated Common Alerting Protocol message -> IPAWS-OPEN -> channel distributors -> public

An alerting authority needs a FEMA memorandum of agreement, a Collaborative Operating Group identity and digital certificate. State/local/tribal law and plans determine who in the jurisdiction may originate which alerts. Sources: [FEMA IPAWS MOA application](https://www.fema.gov/sites/default/files/2020-07/fema_ipaws_form-007-0-25_moa-application.pdf); [FEMA IPAWS toolkit](https://www.fema.gov/vi/emergency-managers/practitioners/integrated-public-alert-warning-system/public-safety-officials/toolkit).

### Emergency Alert System — EAS

**Path:** broadcast, cable and other EAS participants relay encoded alerts under FCC technical and participation rules.  
**National rail:** a National Emergency Message takes priority and pre-empts an alert already in progress. Primary Entry Point stations are private/commercial broadcasters that cooperate with FEMA and receive hardened backup communications and power.  
**Boundary:** national presidential activation and state/local alert use have different legal/operating rules.

Source: [FCC EAS rule update and National Public Warning System description](https://docs.fcc.gov/public/attachments/DOC-387026A1.pdf).

### Wireless Emergency Alerts — WEA

**Path:** authenticated alerts are geographically broadcast by participating commercial mobile providers to compatible devices.  
**Object:** one-to-many cell broadcast, not a person-to-person call or ordinary text message.  
**Boundary:** alert origination, FEMA authentication and carrier delivery are separate entities and clocks.

### NOAA Weather Radio All Hazards — NWR

**Operator:** National Weather Service.  
**Path:** VHF broadcast with SAME/geographic coding and tone-alert capability; carries weather and specified non-weather hazards in coordination with emergency authorities and EAS.  
**Strength:** independent radio receiving path with battery-capable consumer receivers; does not require a working household broadband subscription.

Source: [NOAA Weather Radio](https://www.weather.gov/nwr/).

## 9. Alternate and last-resort rails

### SHARES HF Radio

The SHAred RESources High Frequency Radio program gives the NSEP community another path when landline and cellular systems are down. It uses interoperable HF resources and procedures across participating government and industry entities. Source: [CISA NCC/SHARES](https://www.cisa.gov/resources-tools/programs/national-coordinating-center-communications).

### Public-safety land-mobile radio

Local, tribal, state and federal public-safety bodies operate radio systems that may function apart from the public Internet, though modern dispatch, backhaul and interoperability gateways can still create shared dependencies. Statewide Interoperability Coordinators and CISA programs build plans and shared procedures. Source: [CISA SLTT coordination](https://www.cisa.gov/resources-tools/programs/emergency-communications-state-local-tribal-and-territorial-coordination).

### Satellite and deployable systems

Deployable cells, portable satellite terminals, mobile command vehicles, microwave, temporary fiber and generator-backed sites can restore an access island. They still require spectrum authority, equipment, trained crews, power and backhaul.

### Amateur and auxiliary radio

Volunteer and amateur resources may support health-and-welfare, local coordination or agency auxiliary missions under FCC rules and incident arrangements. They do not replace authenticated classified or public-safety command systems.

## 10. PACE continuity method

PACE means Primary, Alternate, Contingency and Emergency. The key rule is path independence: a backup that shares the failed dependency is not a real backup. If IP data is down, VoIP over the same data path is weak as the alternate. If terrestrial fiber is cut, a separately powered satellite or HF path may be stronger.

Source: [CISA PACE guide](https://www.cisa.gov/sites/default/files/2023-05/23_0426_ncswic_PACE-Plan_508.pdf).

### Example sovereign PACE stack

| Tier | Illustrative path | Hidden dependency to test |
|---|---|---|
| Primary | domestic fiber + commercial mobile + secure IP core | grid, shared conduit, cloud identity, DNS |
| Alternate | second carrier on physically diverse fiber | common bridge, building entry, exchange or power feed |
| Contingency | satellite/LEO service with separate gateway route | shared cloud/core, terminal power, gateway geography, spectrum |
| Emergency | HF/land-mobile radio and preplanned message forms | trained operators, antennas, propagation, key/call-sign control |

## 11. Defense Production Act priority rail

50 U.S.C. § 4511 lets the President require priority performance of contracts or orders needed for national defense and, under its limits, allocate materials, services and facilities. Executive delegation and agency regulations determine which department rates or allocates the object. This can accelerate equipment, services, construction materials or other scarce inputs; it is not a free-standing Internet takeover power. Source: [50 U.S.C. § 4511](https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title50-section4511).

Keep these separate:

- TSP prioritizes telecom provisioning/restoration;
- DPA prioritizes contracts/orders or allocates resources after proper invocation;
- emergency procurement buys services;
- §606 can reach facility use/control at the highest trigger.

## 12. Presidential war/emergency communications power

47 U.S.C. § 606 contains several powers with different triggers:

| Subsection | Trigger | Power |
|---|---|---|
| §606(a) | war in which the United States is engaged plus national-defense finding | direct essential communications to receive preference or priority |
| §606(b) | war | use armed forces to prevent physical obstruction of interstate/foreign wire or radio communications when public interest requires |
| §606(c) | proclaimed war/threat, public peril/disaster/other national emergency, or neutrality condition plus necessity finding | suspend/amend rules for certain emitting stations/devices; close or authorize government use/control of specified radio stations/devices with compensation |
| §606(d) | proclaimed state or threat of war involving the United States plus necessity finding | suspend/amend rules, close, or authorize government use/control of wire facilities with compensation for the statutory period |

Source: [47 U.S.C. § 606](https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title47-section606).

### Boundary

There is no single statutory “Internet kill switch” sentence. The law speaks in older communications categories and ties different powers to different findings. Any modern application would require exact analysis of the facility, subsection, proclamation, delegation, compensation and constitutional limits.

## 13. Rights during an emergency

Emergency status does not, by itself, erase ordinary rights.

- Property use/control under §606 requires the statute's trigger and just compensation language.
- Lawful interception still needs the authority required by the Wiretap Act, Stored Communications Act, FISA or other applicable law; infrastructure emergency status is not itself an intercept order.
- Public alerts must come through an authorized originator and authenticated channel.
- WPS creates priority, not disconnection of ordinary calls in progress.
- MDRI roaming is bounded by technical feasibility and host-network protection.
- DIRS supplies protected infrastructure reporting, not public title.
- First Amendment and judicial-review limits continue to apply to government acts.

## 14. Scenario chains

### A. Hurricane destroys cell sites and fiber

1. Operators detect alarms and dispatch crews.
2. NORS obligations attach if thresholds are met.
3. FCC activates DIRS for named counties; covered providers file daily.
4. DIRS activation also triggers MDRI for mobile providers.
5. Disaster roaming and mutual-aid arrangements turn on where feasible.
6. TSP-coded circuits move ahead in provisioning/restoration queues.
7. FirstNet priority/pre-emption and deployables support eligible responders.
8. FEMA/CISA ESF #2 coordinates federal help, fuel/power and tactical support.
9. IPAWS channels warn the public.
10. DIRS/MDRI deactivate by public notice; final/restoration reports follow.

### B. Cyberattack disables a carrier core

1. Carrier isolates and restores under its incident plan.
2. Regulatory and contractual reporting clocks attach according to the service and incident.
3. NORS/DIRS may supply outage status; CISA/NCC shares sector intelligence.
4. Traffic shifts to alternate carriers/routes if contracts and capacity permit.
5. GETS/WPS help with congestion; TSP helps restore coded services.
6. ESF #2 may activate if incident scale requires federal response.
7. Law enforcement/intelligence response runs on its own legal clock.

As of the cutoff, CISA's general CIRCIA reporting rule remains in rulemaking rather than being treated here as a final operative duty. Source: [2026 CISA town-hall notice](https://public-inspection.federalregister.gov/2026-02948.pdf).

### C. Undersea cable cut

1. Cable operator confirms fault and shifts capacity under network agreements.
2. Consortia/maintenance authority mobilizes a repair vessel and permits.
3. Carriers reroute through other cables, terrestrial paths or satellite where capacity exists.
4. TSP can prioritize affected coded services, but cannot create unused international capacity.
5. FCC/CISA/NCC coordinate if national impact warrants.
6. Landing-license or national-security action is separate from physical marine repair.

### D. National warning without network takeover

1. authorized national originator creates the message;
2. FEMA/IPAWS authenticates and distributes;
3. EAS/PEP, WEA and other paths relay;
4. NWR and local systems carry relevant warning;
5. responders use FirstNet, LMR, GETS/WPS and other command paths;
6. private carrier title and ordinary operation remain in place.

## 15. Real sovereign-resilience test

A network is not sovereign merely because the satellite or fiber owner is American. Test whether the system has:

- separate physical routes and landing/gateway sites;
- domestic operational control;
- independent power and fuel;
- owned or enforceable capacity rights;
- government-defined identity and access;
- government-controlled encryption/signing keys where required;
- route and DNS recovery authority;
- enrolled priority circuits and users;
- public-warning authentication;
- cross-carrier roaming and mutual aid;
- trained PACE fallbacks;
- a clear statutory activation and deactivation chain.

That is the difference between an American transport vendor and a resilient sovereign communications plane.
