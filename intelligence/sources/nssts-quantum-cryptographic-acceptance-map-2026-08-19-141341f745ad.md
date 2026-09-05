# NSSTS Quantum and Cryptographic Acceptance Map

**As of:** August 19, 2026  
**State:** pending Workbench evidence; not vault canon  
**Automatic monitoring:** false  
**Investment use:** false

## Controlling finding

The important company layer is not just the maker of a quantum computer or the
vendor that says it supports post-quantum cryptography. It is the chain that can
turn a capability claim into evidence an acquiring authority can accept.

```text
quantum component
  -> traceable measurement / calibration
  -> independent government V&V
  -> manufacturing or deployment instrument
  -> lot, subsystem and system acceptance

PQC implementation
  -> algorithm conformance (CAVP)
  -> entropy / random-bit evidence
  -> accredited laboratory test
  -> module validation (CMVP / FIPS 140-3)
  -> exact product, version and environment mapping
  -> PKI / protocol interoperability
  -> system authorization (ATO)
  -> production lifecycle, revocation and key custody
```

The first chain makes **Rydberg Technologies, SRI International, Qunnect,
Maybell, AOSense, Photon Spot and the cryogenic/photonics suppliers** more
interesting than a headline-only quantum-computer list. The second makes
**Entrust, WidePoint, Crypto4A, SafeLogic and the small accredited testing-lab
population** pivotal even when they never build the end application.

## Wave 1 — quantum truth and acceptance

### Rydberg Technologies is the strongest hidden referee

DARPA's $3.599 million Phase II STTR with **RYDBERG TECHNOLOGIES INC** funds the
Quantum Calibration Lab through June 23, 2028. Its intended output is unusually
important: SI-traceable calibration methods, protocols and benchmarks for
Rydberg RF sensors, with supporting laser and nanophotonic characterization.
That gives it a PATH4 relationship to an adjacent federal test architecture.

It is not the final acceptor. Rydberg and the University of Michigan can create
calibration evidence; DARPA and later acquiring programs decide whether to use
that evidence and whether a device passes. The promotion object is an operating
lab with accepted protocols, public access rules and a Phase III or acquisition
recognition path—not the Phase II announcement alone.

### Three federal architectures must remain separate

- **QBI Stage B** is planning, risk retirement and prototype work. It is not
  government V&V.
- **QBI Stage C** applies government V&V to Microsoft and PsiQuantum designs,
  but does not itself build and accept a utility-scale machine.
- **DARPA's QBI IV&V call** remains open through October 15, 2026. No public
  awardee exists yet, and a company accepting the independent-referee role may
  face organizational-conflict limits on performer work.

The same separation applies to Commerce's nine **Quantum CHIPS letters of
intent**. They expose a major proposed foundry and system-manufacturing field,
but the proposed $2.013 billion is not a ledger of final agreements or
obligations. Exact project entities, federal equity instruments, milestones and
accepted capacity remain future evidence objects.

### SRI becomes a manufacturing membrane

NIST's initial $20 million agreement with **SRI International** to establish the
Quantum Manufacturing Engineering Center is one of the most consequential new
joins. QMEC is designed to work on cryostats, lasers, components and scalable
manufacturing processes—the layer between laboratory device and repeatable
product. It should be watched for partner work packages, qualified processes,
manufacturing-transfer records and customer acceptance, not simply a center
membership list.

### Timing, sensing and networking are closer to field truth

- **IonQ / Vector Atomic:** DARPA's manufacturing-development action concerns
  capacity and 25 Evergreen-05 clocks; a separate 100-unit option remains
  unexercised. Capacity is not accepted units.
- **AOSENSE, INC.:** its QuAIS II marine-relevant quantum-IMU effort ends August
  28, 2026. The meaningful return object is the released field result and a
  platform/follow-on qualification.
- **QUNNECT, INC. / Qunnect LLC:** DOE and USAF records expose a quantum-buffer
  and entanglement-validation path, but the Inc.-to-LLC entity change is not
  resolved publicly. The Air Force—not the device—decides test acceptance.
- **Qubitekk / IonQ:** the ORNL–EPB grid-QKD work is an operating comparator,
  but IonQ bought operating assets rather than publicly novating every historic
  contract and obligation.

## Wave 2 — the less-obvious quantum bill of materials

The hidden quantum supply chain is dominated by thermal, RF, optical, packaging
and measurement constraints:

| Node | Actual leverage | What would promote it |
|---|---|---|
| **Maybell Quantum Industries** | Low-thermal-load cryogenic wiring and control infrastructure | Target order, lot qualification, reliability and accepted system integration |
| **Amphenol / XMA** | Cryogenic RF attenuation, termination and interconnect | Exact legal seller, qualified part numbers and target BOM |
| **Bluefors Cryocooler Technologies** | Cold-head refurbishment and low-temperature uptime | Target service order and accepted return-to-service test |
| **Photon Spot** | Compact, low-vibration cryogenics for SNSPDs | Phase II/III, yield/reliability and customer qualification |
| **Vescent** | Laser/frequency-control subsystems | Resolve VESCENT TECHNOLOGIES INC. vs Vescent Photonics, LLC; then delivery/qualification |
| **FormFactor / Quantum Opus / Triton / Northrop Grumman** | Cryogenic test and component R&D | Company-specific transition and customer qualification |
| **PHIX Photonics Assembly** | Photonic integrated-circuit packaging | U.S. target order, eligibility review and qualified process |

Two consolidation seams matter. Amphenol acquired XMA, so **Amphenol RF and
XMA cannot be counted as independent suppliers without exact entity evidence**.
IonQ's acquisition of Qubitekk operating assets likewise does not prove that all
historic agreements followed the assets.

QED-C membership and NIST-matched project completion are useful discovery
signals. Neither is a production qualification, government endorsement or
target award.

## Wave 3 — the cryptographic validation economy

### The real bottleneck is CAVP-to-ATO, not algorithm availability

FIPS 203, 204 and 205 are final. FIPS 206 remains in development, and HQC is a
selected future backup KEM rather than a current final FIPS. A vendor can have
an ML-KEM or ML-DSA CAVP certificate while its product remains unvalidated,
while its FIPS 140-3 submission remains in process, or while the validated
module's security policy excludes the PQC service from approved mode.

This makes the following boundaries non-negotiable:

1. **CAVP validates algorithm implementation conformance.**
2. **NVLAP-accredited laboratories test a specific module.**
3. **NIST CMVP validates that module and operating boundary.**
4. **The buyer must map the exact product/version/environment to the certificate.**
5. **The agency authorizing official accepts the system configuration and
   residual risk.**

NIST's own LS2 HSM security policy provides the clean disconfirming example:
ML-KEM and ML-DSA services can appear in the module while being marked
non-compliant in the FIPS state. Capability does not equal an approved service.

### PKI is concentrated, but incumbency does not prove PQC readiness

GSA currently lists only **Entrust Corporation** and **WidePoint Cybersecurity
Solutions Corp.** under the PKI shared-service-provider SIN.

- Entrust has a real federal PKI position and an active nShield 5s FIPS 140-3
  certificate, plus separate PQC algorithm evidence. The missing join is a
  security policy showing which PQC services are approved in the exact module,
  followed by a deployed certificate profile and target ATO.
- WidePoint is a live FPKI/ECA operator but has no comparable public PQC
  CAVP/CMVP/product/deployment chain. That makes it a migration chokepoint, not
  a demonstrated PQC-ready incumbent.

### The product-transition candidates

- **Crypto4A Technologies:** unusually close because it has PQC CAVP evidence,
  validated entropy and an HSM product, but its decisive FIPS 140-3 certificate
  was still in process. Its FIPS 140-2 certificate reaches the September 21/22,
  2026 new-system cliff.
- **SafeLogic:** PQC CAVP plus entropy and an OEM-embeddable provider, but CMVP
  review and exact OEM product mapping remain gates.
- **Secure Micro Technologies:** a promising classical/PQC HSM bridge, but only
  at the SBIR prototype state.
- **PQSecure, Securosys, Bouncy Castle and Geomys:** important because their
  cores and libraries can propagate into many products. That same propagation
  makes exact dependency, version and approved-mode mapping essential.
- **SB Technology Federal / SandboxAQ:** the federal join is a completed Air
  Force Phase I for inventory analysis and benchmarking. DISA's general
  technology-watch status does not prove SandboxAQ deployment.

## Wave 4 — independent evidence and the Genesis no-join

### Validation capacity is itself a strategic supply chain

NIST paused new applications to the cryptographic/security-testing laboratory
program because of resource constraints. Existing laboratories—**Lightship,
atsec, Intertek Acumen, Gossamer, Leidos AT&E, AEGISOLVE, Penumbra and Advanced
Data Security**—therefore sit on a scarce migration path.

They do not issue a federal system authorization. A clean decision chain is:

```text
vendor -> NVLAP-accredited test lab -> NIST CMVP -> product integrator
       -> agency assessment evidence -> agency authorizing official
```

The NCCoE PQC migration consortium helps create reference architectures and
interoperability evidence. Its CRADA participants are not awardees, endorsed
products or validated modules by virtue of membership.

### Genesis has operating trust rails, but no public PQC configuration

There is a firm public-record **no-join** between a named Genesis component and
a system-specific PQC control set as of the cutoff. No public Genesis SSP/ATO,
certificate profile, CBOM, signing/admission policy, KMS/HSM configuration or
explicit FIPS 203/204/205 deployment was located.

The operating joins are narrower:

- **University of Chicago / Globus:** ALCF's Inference Service is a Genesis/AmSC
  tool using Globus Compute and Auth. Globus brokers federated identity and
  delegated access; the institution/resource owner still authenticates and
  authorizes. Its operating role does not establish a PQC token or transport
  profile.
- **Amazon Web Services, Inc.:** NNSA's enterprise-authorized S/RD cloud will
  host inaugural Genesis workloads. AWS offers ML-KEM and ML-DSA capabilities,
  but they require exact client, endpoint, key and policy choices. Product
  capability is not target activation.
- **Saviynt and CILogon:** these are important upstream entitlement/federation
  nodes. Neither has a public Genesis-specific assignment, and Saviynt is not
  DOE's authoritative identity source.

The deciding actor is the DOE/NNSA authorizing official. A test lab, CMVP,
certificate authority, identity broker, cloud KMS or audit firm can create an
evidence object, but none can accept residual risk for the Genesis system.

## What to watch next

1. **August 28, 2026:** AOSense QuAIS II contract end and any released field
   result.
2. **September 21/22, 2026:** FIPS 140-2 modules move to historical status for
   new-system acquisition use.
3. **October 15, 2026:** QBI IV&V response close; watch for exact awardee and
   organizational-conflict terms.
4. **October 22, 2026:** non-NSS agency PQC plans due under OMB M-26-15; watch
   for DOE priorities and named high-value systems.
5. **Quantum CHIPS:** final agreements, exact subsidiaries, obligations,
   milestones and federal equity instruments.
6. **QMEC and QCAL:** named partner work packages, operating access, accepted
   protocols and customer qualification.
7. **CMVP queue:** issued 140-3 certificates whose security policies expressly
   identify ML-KEM, ML-DSA or SLH-DSA as approved services.
8. **Genesis:** CBOM, SSP/ATO excerpt, target KMS/HSM mapping, certificate
   profile or signed artifact plus an enforced admission policy.

## Governing boundary

This registry adds 40 acceptance-chain cases. It is a discovery and promotion
map, not an award forecast, vendor endorsement or investment screen. No entry
may move into a target supplier state without its named evidence object and
decision authority.
