# Sovereign Communications — Research Package

**Status:** `pending`  
**Cutoff:** 2026-07-15  
**Scope:** United States communications infrastructure, ordinary rights and permissions, federal security control, emergency activation and public warning  
**Method:** primary sources first; asset, right, operator and clock kept separate

## Read order

1. `SOVEREIGN_COMMUNICATIONS_FIELD_REGISTRY.md`
2. `SOVEREIGN_COMMUNICATIONS_ENTITY_REGISTRY.md`
3. `SOVEREIGN_COMMUNICATIONS_INFRASTRUCTURE_RIGHTS_MAP.md`
4. `SOVEREIGN_COMMUNICATIONS_EMERGENCY_RAILS_MAP.md`
5. `SOVEREIGN_COMMUNICATIONS_CLAIM_AUDIT.md`
6. `SOVEREIGN_COMMUNICATIONS_SOURCE_WATCHBOARD.md`

## Short answer

The United States does not operate one national Internet. It governs a layered public-private communications field.

- Private firms and public bodies own or lease land, poles, conduits, fiber, cable systems, towers, satellites, data centres, routers and radio equipment.
- The FCC controls major federal permission gates for non-federal radio use, satellite communications, cable landings, international telecommunications authority, regulated ownership transfers and equipment authorization.
- NTIA authorizes federal spectrum use. It does not regulate private radio users.
- State and local bodies control much of the physical placement clock through property, public rights-of-way, construction, zoning, franchises, utility access and emergency management.
- ICANN/IANA, ARIN and network operators coordinate names, numbers and routes. They do not sit under an ordinary FCC packet-routing command.
- CISA is the federal communications-sector risk and emergency coordinator. It usually coordinates private operators rather than running their networks.
- Federal agencies authorize and control their own systems. NSA's national-manager role applies to national security systems, not to the whole public Internet.
- Emergency rails add priority, reporting, mutual aid, public warning, restoration and backup paths. Only the highest statutory tier reaches exceptional presidential use or control of facilities.

The controlling model is:

> **OWNER -> ACCESS RIGHT -> LICENSE/PERMISSION -> OPERATOR -> SERVICE CONTRACT -> SECURITY AUTHORITY -> EMERGENCY ACTIVATION**

No arrow should be presumed from the one before it.

## Strongest findings

### 1. Critical infrastructure is not a title transfer

Communications and Information Technology are critical-infrastructure sectors because their loss can damage security, the economy, health or safety. The designation creates a protection, coordination and resilience mission. It does not nationalize a cable, tower, satellite or cloud region. The statutory policy expressly uses public-private partnership. Sources: [42 U.S.C. § 5195c](https://uscode.house.gov/view.xhtml?edition=prelim&f=treesort&jumpTo=true&num=0&req=%28title%3A42+section%3A5195c+edition%3Aprelim%29+OR+%28granuleid%3AUSC-prelim-title42-section5195c%29); [CISA Communications Sector](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/resilience-services/infrastructure-dependency-primer/learn/communications); [CISA Information Technology Sector](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors/information-technology-sector).

### 2. National security system is a narrower legal object

A government or contractor system qualifies when it performs defined military, intelligence, cryptologic, weapons, direct mission or classified-information functions. Routine administrative systems do not enter merely because government uses them. Source: [44 U.S.C. § 3552(b)(6)](https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title44-section3552%28b%29%286%29).

### 3. The deepest ordinary control is a bundle of small rights

The network is held together by deeds, leases, easements, public rights-of-way, pole and conduit rights, fiber ownership, capacity leases, indefeasible rights of use, spectrum licenses, cable-landing licenses, equipment authorizations, interconnection agreements, peering contracts, autonomous-system and IP allocations, domain registrations, cloud contracts, identity credentials and encryption keys. These rights can sit in different legal persons.

### 4. Emergency control is a ladder, not a switch

Most incidents never reach presidential control. The operating sequence is usually:

1. carrier detects and repairs;
2. FCC outage reporting and sector information sharing;
3. priority calling or circuit restoration;
4. disaster roaming and mutual aid;
5. FEMA/CISA ESF #2 coordination and deployable support;
6. public alerts through IPAWS-linked channels;
7. alternate paths such as SHARES HF radio;
8. procurement or production priority if formally invoked;
9. exceptional presidential powers only after the statutory findings required by 47 U.S.C. § 606.

### 5. The emergency field contains three different flows

- **Command-to-public:** IPAWS -> EAS / WEA / NOAA Weather Radio and other alert distributors.
- **Public-to-responder:** 911 / NG911 -> emergency communications centre -> dispatch and field responder.
- **Responder-to-responder:** land-mobile radio, FirstNet, GETS, WPS, TSP, public-safety networks, satellite and SHARES.

An alert rail, a distress-call rail and an operational command rail are not the same thing.

### 6. FirstNet is the closest live sovereign-network model

Congress created a federal authority, assigned spectrum and funding, and required a nationwide public-safety broadband network. The FirstNet Authority oversees the network; AT&T builds and operates it; the system uses a dedicated core plus priority and pre-emption. This is a public-governed service plane on commercial infrastructure, not a wholly federal replacement Internet. Source: [FirstNet Authority](https://firstnet.gov/about).

### 7. The SpaceX approval chain is plural

FCC constellation and spectrum authority, FAA launch authority, Commerce remote-sensing authority when applicable, government procurement and NSS security approval are different clocks. A commercial Starlink authorization does not itself approve a classified Starshield implementation. Sources: [FCC Gen2 authorization](https://docs.fcc.gov/public/attachments/DOC-417881A1.pdf); [FAA launch review](https://www.faa.gov/space/stakeholder_engagement/spacex_starship/license_review_process); [NOAA private remote-sensing rule](https://www.nesdis.noaa.gov/s3/2021-08/15%20CFR%20Part%20960%20Regs%202020.pdf).

### 8. One current correction matters

DIRS began as voluntary. For covered cable, wireless, wireline and interconnected-VoIP providers, daily DIRS infrastructure reporting became mandatory when the FCC activates DIRS in their service area, effective 2025-02-20. DIRS Lite remains voluntary. Sources: [FCC compliance notice](https://docs.fcc.gov/public/attachments/DA-25-74A1.pdf); [FCC reconsideration order](https://docs.fcc.gov/public/attachments/FCC-25-45A1_Rcd.pdf).

## Package boundary

Included:

- public and private communications assets;
- rights of access, use and control;
- federal, state, local and private entity boundaries;
- national-security and federal-system controls;
- emergency priority, reporting, warning, restoration and backup rails;
- the highest-level emergency statutes;
- privacy, lawful-access and government-speech boundaries needed to understand rights.

Not yet included:

- a parcel-by-parcel terrestrial-fiber census;
- a complete ownership ledger for every U.S. cable, tower, IX or data centre;
- classified continuity systems;
- state-by-state emergency-power and public-utility law;
- legal advice about any specific provider, property or surveillance demand.

## Vault placement

This is a cross-machine factual package. It belongs beside sovereign compute, Information War, federal entity control, emergency activation and infrastructure logistics. It should not become a new top-level plotline until repeated events move one or more of these control points:

- ownership or landing rights;
- spectrum or operating authority;
- dedicated government core or identity boundary;
- emergency priority or restoration;
- routing, naming or trust-anchor governance;
- presidential or statutory control;
- private-to-public operating transfer.
