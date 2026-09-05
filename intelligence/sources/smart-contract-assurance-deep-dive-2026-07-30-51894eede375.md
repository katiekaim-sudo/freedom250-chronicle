# Smart-Contract and Blockchain Accounting Controls and Assurance Map

## Executive conclusion

A blockchain can make a transaction history tamper-evident and, after sufficient finality, difficult to rewrite. It can also make deterministic rules and reconciliations executable rather than manual. Those are real control improvements. They do **not** establish that:

- the off-chain business event was real;
- every asset, liability, side agreement, or chain was included;
- the address belongs to the reporting entity or is legally available to it;
- an oracle input was accurate;
- a token has the reported value or accounting classification;
- code faithfully represents the legal agreement;
- a transaction signed with a valid key was economically authorized; or
- a point-in-time reserve balance covers all customer claims.

The practical assurance model is therefore not “trustless accounting.” It is a shift in the trust boundary:

> **Ledger-mutation risk falls; input, identity, key, administrator, governance, valuation, legal-rights, and reporting-layer risks become the control center.**

PCAOB AS 1105 is the right baseline. Electronic evidence is more reliable when the relevant IT general controls and automated application controls are effective; information used by the auditor still must be tested for accuracy, completeness, precision, and detail. More copies of the same unreliable chain extract do not cure poor-quality evidence.

## 1. Scope and control model

This map applies to:

- crypto assets held directly or through custodians;
- tokenized financial or real-world assets;
- smart contracts that execute payments, revenue sharing, collateral, lending, derivatives, royalties, grants, or procurement;
- permissionless and permissioned distributed ledgers;
- on-chain subledgers feeding an ERP or general ledger; and
- proof-of-reserves, continuous monitoring, and related assurance.

The control model has five layers:

1. **Economic and legal layer** — parties, rights, obligations, ownership, enforceability, side agreements, and accounting policy.
2. **Input layer** — identities, business approvals, oracles, source documents, market data, and physical-world evidence.
3. **Execution layer** — smart-contract code, contract addresses, network rules, keys, administrators, governance, upgrades, bridges, and finality.
4. **Accounting layer** — chart-of-account mapping, valuation, cutoff, classification, consolidation, eliminations, corrections, and disclosures.
5. **Assurance layer** — independent evidence acquisition, reperformance, confirmations, exception investigation, control testing, and reporting.

No single layer can substitute for the others.

## 2. Assertion-level practical control matrix

| Assertion / objective | What a blockchain can improve | Principal residual or migrated risk | Minimum control design | Auditor / assurance procedure |
|---|---|---|---|---|
| **Existence / occurrence** | A finalized transaction and balance can be independently observed on a specified chain. Digital signatures demonstrate use of a key. | A balance may be borrowed temporarily, held for another party, encumbered, inaccessible, or controlled by a compromised key. A transaction may be wash activity between related wallets. Token state does not prove an off-chain asset exists. | Maintain an approved inventory of chain IDs, contract addresses, wallets, custodians, and beneficial owners. Perform key-control challenge procedures. Independently confirm custodial balances and restrictions. For tokenized real-world assets, reconcile to registries, physical inspection, third-party confirmations, and legal title. Screen related wallets and circular flows. | Query an independent full/archive node; verify block hash and finality; challenge-sign a nonce or execute a low-risk control transfer; confirm custodian and legal title directly; inspect subsequent disposition; analyze address clusters and circular transactions. A signature proves key control, not legal ownership. |
| **Completeness** | A canonical on-chain history can reduce missing records inside a known scope and make sequence gaps detectable. | Management can omit wallets, contracts, chains, bridges, custodians, side letters, off-chain liabilities, pending transactions, or failed/reverted calls. Indexers may omit events or chain reorganizations. | Board-/controller-approved population definition; discovery scans for addresses and contracts; reconcile all known wallets to custodian, bank, tax, legal, exchange, and counterparty records; ingest native transfers, token events, internal calls, bridge locks/mints/burns, staking, rewards, fees, failed transactions, and admin events. Maintain block-range completeness controls and an address-change log. | Obtain population independently where possible; test first/last block and sequential ranges; reconcile state balances to transaction rollforwards; compare multiple data sources/nodes; search legal, bank, tax, and vendor records for unrecorded addresses or obligations; test omitted and reverted transactions. |
| **Rights and obligations** | The ledger can show which address holds a token and which key can instruct a contract. | Address control is not necessarily beneficial ownership. Customer assets may be in omnibus wallets. Tokens may be encumbered, staked, bridged, pledged, frozen, subject to clawback, or bankruptcy-contested. Legal contract and code may diverge. | Legal ownership memo for each material asset/arrangement; wallet-to-legal-entity register; custody and bankruptcy-remoteness analysis; lien/pledge and protocol-term review; customer subledger reconciliation; explicit hierarchy between prose and code; approved treatment of forks, airdrops, staking, wrapping, and bridges. | Inspect legal contracts and protocol terms; obtain attorney evidence where necessary; confirm restrictions and claims; test customer allocation records; examine approvals and subsequent use. Apply PCAOB AS 1105 Appendix A when legal expertise is used as audit evidence. |
| **Valuation / allocation** | On-chain prices, liquidity, and transactions can provide observable data and an exact unit count at a specified block. | Quoted prices can be thin, fragmented, manipulated, related-party, non-orderly, or unavailable at the reporting time. Oracle feeds may be stale or attacked. Wrapped, bridged, locked, staked, vesting, or restricted assets may not equal the underlying spot asset. Smart-contract liabilities may contain nonlinear or contingent exposures. | Document principal market and valuation time; independent price-source hierarchy; liquidity/orderliness tests; related-party and wash-trade filters; multi-venue dispersion checks; oracle staleness/deviation limits; valuation models for restrictions, liquidity, credit, smart-contract, bridge, and depeg risk; model validation and governance. Apply FASB scope and fair-value requirements asset by asset. | Apply PCAOB AS 2501: test management's process and significant assumptions, develop an independent expectation or use subsequent events where appropriate, and evaluate management bias. Reperform unit counts, price selection, fair-value hierarchy, model inputs, and disclosures. |
| **Cutoff** | Block height and transaction order give a precise protocol timestamp and settlement sequence. | Block timestamp is not necessarily the economic-event time, legal transfer time, or reporting-zone time. Mempool transactions, probabilistic finality, reorgs, delayed bridges, and after-close admin actions create cutoff risk. | Formal cutoff policy by transaction type: trade date, legal settlement, protocol finality threshold, and time zone. Snapshot exact block height/hash at close. Define confirmations/finality by chain. Monitor reorgs and bridge completion through the close-plus window. Separate initiated, pending, reverted, finalized, and legally settled states. | Inspect transactions before and after the close; verify the closing block hash against independent nodes; test finality and subsequent reorgs; reconcile pending and failed calls; compare protocol settlement with legal and accounting recognition criteria. |
| **Classification / presentation / disclosure** | Standardized token and event schemas can support automated mappings and consistent rollforwards. | “Token” is a technical form, not an accounting classification. Assets may be cash equivalents, investments, intangibles, inventory, receivables, derivatives, customer property, or something else depending on facts. Smart contracts can embed leases, guarantees, derivatives, variable consideration, or contingencies. | Accounting-policy committee approval for each product type; product-to-ASC mapping; contract feature inventory; embedded-feature and principal/agent analysis; customer-vs-company asset controls; current/noncurrent and operating/nonoperating policy; disclosure checklist for concentration, custody, restrictions, liquidity, and technology/legal risk. | Read code, prose, marketing, governance, and operational practice together. Test whether the substance matches the accounting memo. Reconcile unit rollforwards and presentation. FASB ASU 2023-08 applies only to assets meeting all six scope criteria; do not generalize it to every token. |
| **Authorization** | Cryptographic signatures and deterministic permission checks can make authorization machine-verifiable. | A valid signature only proves use of a key. The key may be stolen, shared, coerced, or used outside policy. Admin roles may bypass ordinary controls. Governance voters may be related or captured. | HSM/MPC or well-governed multisignature; role-based transaction policies; transaction simulation; allowlists and limits; dual approval; independent review of unusual destinations and admin calls; key lifecycle and compromise plan; governance concentration monitoring. | Inspect key ceremony, access roles, signer independence, approval evidence, and logs. Select transactions and reperform authorization. Test whether one individual can propose, approve, sign, deploy, upgrade, pause, and record. |
| **Accuracy / deterministic processing** | The same validated input produces the same smart-contract output, and execution can be reperformed. | Deterministic code can be consistently wrong. Compiler, library, proxy, initialization, rounding, decimal, overflow, fee, and ordering defects may produce systematic misstatements. | Formal specification; code-to-accounting-requirement traceability; peer review; static/dynamic analysis; unit, integration, property, fuzz, boundary, and adversarial tests; independent security review; reproducible builds; bytecode/source verification; deployment and initialization checklist. | Reperform high-risk functions with independent tooling; compare deployed bytecode to approved source/build; inspect proxy implementation and storage; test boundary cases, decimals, fees, and state transitions; evaluate whether controls operated for every deployed version. |
| **Consolidation / counterparty** | Shared ledgers can reduce bilateral reconciliation differences. | Pseudonymous addresses conceal related parties, common control, or intra-group transactions. DAOs and token governance complicate control/VIE analysis. | Address ownership and related-party registry; blockchain analytics plus legal/KYC evidence; governance-token concentration and delegation analysis; intercompany address tagging and eliminations; periodic control/VIE reassessment. | Search common funders, signers, withdrawal addresses, governance delegates, and circular transfers. Confirm counterparties. Test consolidation and eliminations independently. |

## 3. Cross-cutting technology and governance risk matrix

| Risk domain | Failure mode | Key preventive controls | Detective / recovery controls |
|---|---|---|---|
| **Oracle / external data** | False, stale, delayed, manipulated, unavailable, or ambiguously defined input triggers a correct execution on bad facts. GAO notes that blockchains have no inherent mechanism to check oracle accuracy. | Multiple independent sources; signed feeds; quorum/median; time-weighted prices; staleness limits; deviation thresholds; source concentration limits; exact unit/time-zone definitions; legal ownership of source rights; separate oracle administrators; fallback source approved in advance. For physical events, independent attestations or IoT-control assurance. | Cross-source divergence alerts; heartbeat monitoring; circuit breaker or fail-closed mode; post-event source reconciliation; incident review; compensating transaction process; preserved oracle payload and signature. |
| **Private keys / custody** | Key theft, loss, sharing, weak backup, insider misuse, compromised vendor, or single signer causes asset loss or unauthorized execution. | NIST-aligned key lifecycle; HSM/MPC; M-of-N multisig with organizational and geographic independence; least privilege; no seed sharing; key-generation ceremony; dual control; signer-device hardening; address allowlists; transaction limits; periodic rotation; vendor due diligence. | Immutable signer and access logs; independent wallet monitoring; compromise indicators; rapid revoke/rotate/migrate process; tested recovery shares; inventory of every key and contract it controls; documented compromise-recovery plan. |
| **Admin / upgrade / pause / mint authority** | “Decentralized” system is effectively controlled by one key or concentrated governance. Admin can change economics, mint, seize, pause, redirect, or destroy evidence. | Complete privileged-function inventory; multisig and timelock; independent approver groups; proposal simulation; on-chain notice; limits on emergency powers; separate development, deployment, security, treasury, oracle, and accounting roles; board/audit-committee visibility for financially material privileges. | Real-time admin-event alerts; compare deployed implementation hash with approved release; periodic access recertification; governance-concentration monitoring; post-emergency review; forced expiration of temporary privileges. |
| **Change management** | Unapproved source, compiler, library, proxy, parameter, or initialization change alters financial processing. | Version-controlled specification and source; signed commits/releases; peer and security review; segregated development/test/production; reproducible builds; testnet/staging; deployment checklist; explicit migration plan; accounting approval for economically material changes. | Bytecode and proxy-slot monitoring; parameter-change alerts; release-to-deployment reconciliation; rollback/migration readiness; independent post-deployment verification. |
| **Network / consensus / finality** | Reorg, chain halt, validator concentration, censorship, 51% attack, hard fork, or fee spike prevents or reverses settlement. | Approved-chain risk assessment; finality threshold; validator/concentration limits where relevant; node/provider diversification; fork and chain-halt policy; avoid relying on a single RPC or block explorer. | Independent nodes in multiple regions/providers; reorg and liveness alerts; closing block/hash archive; alternate settlement procedure; fork inventory and legal/accounting decision log. |
| **Bridge / wrapper / cross-chain** | Lock-and-mint accounting becomes unbacked because of bridge exploit, validator compromise, replay, or asynchronous failure. | Approved bridge list; economic and technical due diligence; caps; multi-party control; independent reserve reconciliation; message finality rules; replay protection; clear legal claim on underlying asset. | Continuous underlying-to-wrapped supply reconciliation; bridge-admin monitoring; depeg alerts; emergency caps/pause; impairment and incident escalation. |
| **Node, API, indexer, and ETL** | Reporting layer misses internal calls, token events, failed calls, reorgs, or historical states even though the chain is correct. | Independently operated archive node or diversified providers; documented extraction logic; schema/version control; complete contract/address inventory; idempotent ingestion; block-height/hash checkpoints; inclusion of native transfers, logs, traces, and status. | Gap/duplicate checks; state-to-flow reconciliation; provider comparison; replay from checkpoint; data-quality dashboard; independent auditor extraction. |
| **Privacy / confidentiality** | Public, replicated, durable data exposes PII, trade secrets, customer behavior, or linkable pseudonyms; deletion may be impossible. | Put no plaintext PII or secrets on-chain. Store sensitive data off-chain under access, retention, and deletion controls; use salted commitments, selective disclosure, permissioned channels, or zero-knowledge techniques only after privacy/security review; minimize public metadata. | Privacy-impact assessments; address-linkage testing; breach monitoring; key revocation and off-chain deletion; incident response. Key destruction does not erase copies of plaintext or linkable metadata already replicated. |
| **Zero-knowledge / privacy proofs** | A mathematically valid proof attests to the wrong statement, incomplete population, defective circuit, compromised trusted setup, or manipulated public inputs. | Formal statement definition; independent circuit review; reproducible build; trusted-setup governance or transparent scheme; controlled public-input generation; versioned verification key; population completeness controls. | Independent proof verification and sample reperformance; circuit/version monitoring; compare committed totals to accounting records; rotate or migrate after compromise. |
| **Failure and recovery** | Contract bug, oracle outage, lost key, cyberattack, governance capture, chain halt, or insolvency leaves no operational remedy. | Scenario-based business continuity and disaster recovery; upgrade/migration design; bounded pause; alternate payment/settlement channel; protected backups and recovery shares; incident authority matrix; liquidity plan; legal remedies and insurance review. | Tested recovery exercises; real-time alerting; forensic evidence preservation; controlled pause/migration; reconciliation after recovery; independent verification before reopening; customer and regulator communication playbook. |

## 4. Oracle control standard

An oracle is not merely a technical integration. For accounting purposes, it is a source of evidence and often an automated authorization trigger.

### Required oracle inventory

For each oracle-dependent accounting or settlement outcome, document:

- exact smart-contract function and financial statement accounts affected;
- source name, legal owner, independence, and licensing;
- observation definition, unit, precision, time zone, and market;
- update frequency, permitted age, and finality;
- number and independence of sources;
- aggregation rule;
- administrator and signing keys;
- fallback, pause, and dispute process; and
- evidence retained for every financially material update.

### Price oracle controls

- Prefer independent, economically active sources rather than issuer-controlled prices.
- Use a median/quorum and time-weighted logic where flash manipulation is plausible.
- Reject stale, missing, zero, negative, out-of-range, or excessive-deviation inputs.
- Limit the financial effect of one update.
- Separate oracle administration from protocol administration and treasury signing.
- Preserve signed raw observations so the auditor can reperform the aggregation.
- Evaluate whether the underlying trades are orderly, arm's-length, and in the principal market; on-chain observability alone does not satisfy fair-value requirements.

### Physical-world oracle controls

A sensor, shipper, warehouse, employee, or government registry can put false information on an immutable ledger. For inventory, delivery, emissions, title, identity, or milestone assertions, the oracle must be supported by conventional controls: calibration, access restriction, chain of custody, independent confirmation, inspection, exception review, and legal accountability.

## 5. Keys, administrators, and segregation of duties

### Treat every privileged key as a financial-system superuser

The privileged-access inventory should include:

- treasury and custody keys;
- mint/burn/seize/freeze keys;
- proxy upgrade and implementation keys;
- pause and emergency keys;
- oracle publisher and aggregator keys;
- bridge validator and relayer keys;
- governance proposal, voting, delegation, and veto rights;
- compiler/release signing keys;
- node/RPC credentials; and
- ERP mapping and journal-interface administrators.

### Minimum key controls

- M-of-N authorization with signers from genuinely separate functions.
- HSM, MPC, or similarly controlled signing; no seed phrase in ordinary collaboration tools.
- Key generation and recovery ceremonies with witnesses and retained evidence.
- Transaction simulation and human-readable intent before signing.
- Address and function allowlists, value limits, velocity limits, and time locks.
- Periodic access recertification and immediate revocation after role changes.
- Documented key states, cryptoperiods, rotation, archival, destruction, and compromise.
- Recovery designed so no single custodian, vendor, or executive can seize or permanently strand assets.

NIST SP 800-57 emphasizes the key-management lifecycle and compromise-recovery planning. GAO's Green Book and FISCAM support separation of authorization, custody, processing/recording, and review, as well as controlled system changes and contingency planning.

### Smart-contract segregation-of-duties pattern

No one person or colluding function should be able to complete this chain:

`specify economics → write code → approve code → build bytecode → deploy/upgrade → set oracle → sign treasury transaction → map to GL → clear exception → certify control`

At minimum, segregate:

- business owner / accounting policy;
- developer;
- security and test reviewer;
- deployer / upgrade proposer;
- upgrade approver or multisig signer;
- oracle administrator;
- asset custodian / treasury signer;
- accounting interface administrator;
- reconciler;
- control owner; and
- internal audit / assurance.

Where headcount prevents full separation, use timelocks, lower limits, independent external co-signers, immutable alerts, and retrospective board/audit-committee review as compensating controls.

## 6. Legal contract versus code

“Smart contract” can mean executable code, a legally binding agreement expressed partly in code, or both. The CFTC's educational primer states that a smart contract may be binding depending on facts and circumstances and remains subject to otherwise applicable law. GAO notes that enforceability varies among U.S. jurisdictions.

### Contract-design rule

For every financially material arrangement, the parties should expressly state:

- their legal identities and authority;
- whether prose, code, or a specified component controls if they conflict;
- chain ID, contract address, source/bytecode version, and initialization parameters;
- the meaning of each oracle input and the source that controls;
- who may upgrade, pause, migrate, mint, burn, seize, or change parameters;
- treatment of bugs, exploits, front-running, accidental transfers, and compromised keys;
- treatment of forks, reorgs, chain halts, bridge failures, and replaced tokens;
- effective time and finality of performance;
- cancellation, correction, rescission, and restitution rights;
- governing law, forum, dispute mechanism, and evidence;
- privacy and records-retention duties; and
- insolvency, custody, collateral, lien, and setoff treatment.

### Code-to-prose control

Maintain a bidirectional requirements matrix:

`legal clause / accounting conclusion → code function and tests → emitted event / retained evidence → GL mapping and disclosure`

Legal, accounting, security, and business owners should approve the same version. A code audit that never tests the legal or accounting specification is not enough; a legal review that never examines deployed bytecode is not enough.

## 7. Corrections, error accounting, and restatements

Immutability changes the mechanics of correction, not the obligation to correct.

### Correction design

- Never “correct” by deleting the original record from the reporting layer.
- Post a reversing or compensating transaction that references the original transaction hash and error case.
- Preserve original state, corrected state, approver, rationale, legal conclusion, accounting treatment, and affected periods.
- Distinguish:
  - protocol-valid but business-invalid transactions;
  - code defects;
  - oracle errors;
  - compromised-key transactions;
  - accounting mapping/valuation errors;
  - legal rescission or dispute; and
  - changes in estimate or principle.
- Reconcile the on-chain correction to the ERP journal and disclosure.
- If migration or fork is required, preserve both histories and an approved bridge from old to new balances.

### Financial-reporting escalation

An immutable erroneous transaction is not self-curing. Management still evaluates materiality under quantitative and qualitative factors, including whether an intentional small misstatement masks trends or affects compliance. SEC SAB 108 requires considering both current-period (“rollover”) and cumulative balance-sheet (“iron curtain”) effects.

The incident playbook should require:

1. freeze/pause decision under preapproved authority;
2. evidence preservation and wallet/contract containment;
3. legal, cybersecurity, accounting, tax, sanctions, and disclosure assessment;
4. period-by-period quantification under both SAB 108 approaches;
5. ICFR deficiency assessment under AS 2201;
6. audit committee and auditor notice;
7. correction, revision, or reissuance determination;
8. non-reliance communication where required; and
9. independent validation before restart.

PCAOB AS 2905 addresses subsequently discovered facts existing at the auditor-report date and may require revised financial statements or steps to prevent future reliance on the report. Blockchain history provides evidence of what occurred; it does not decide whether prior financial statements must be revised.

## 8. Privacy and auditability

Public transparency and privacy are opposing design pressures.

### Core privacy rule

Do not put personal information, confidential contracts, credentials, seed material, or secrets on a public blockchain. A hash is not automatically anonymous: low-entropy data can be guessed, addresses can be linked, and replicated records may remain available even when the organization's own copy is deleted.

Use:

- off-chain encrypted records with on-chain commitments;
- salted commitments when dictionary attacks are plausible;
- minimum necessary public metadata;
- selective-disclosure credentials;
- permissioned channels for restricted business data;
- retention and deletion controls for off-chain records;
- privacy impact and legal assessments before deployment; and
- audit access that reveals only what is required.

GAO-22-104625 specifically highlights privacy risk from the distributed storage of sensitive data and the possibility of linking transactions to individuals.

### Assurance over privacy-preserving systems

A zero-knowledge proof may demonstrate that a computation is consistent with its inputs. Assurance must also cover:

- whether the proof statement represents the accounting assertion;
- whether the input population is complete;
- who generated the inputs;
- circuit and verifier correctness;
- trusted setup or verification-key governance;
- version control; and
- side information or metadata that defeats privacy.

## 9. Proof of reserves: useful procedure, not a balance-sheet audit

The PCAOB Office of the Investor Advocate says proof-of-reserve reports are inherently limited, are not audits, and do not provide meaningful assurance to investors or the public. Typical reports may show assets at one moment but omit:

- liabilities;
- customer rights and obligations;
- beneficial ownership and restrictions;
- borrowed or temporarily transferred assets;
- encumbrances, liens, pledges, staking, or rehypothecation;
- off-chain balances and side agreements;
- affiliated entities and consolidation;
- subsequent withdrawals or transfers;
- valuation and liquidity;
- internal control; and
- going concern.

### Minimum credible reserve-and-liability assurance

If a reserve report is used at all, require:

- clearly identified legal entity and reporting perimeter;
- asset and liability definitions;
- full customer-liability population, including negative accounts and pending items;
- independent control/ownership evidence for each wallet and custodian account;
- encumbrance and borrowing confirmations;
- valuation and haircut policy;
- proof that the snapshot was unannounced or sustained over a period, not window-dressed;
- subsequent-event testing;
- reconciliation to audited financial statements;
- examination-level criteria and a clearly described assurance standard; and
- explicit limitations that prevent the report from being marketed as a financial-statement audit.

A Merkle-root customer liability proof can allow a customer to test inclusion. It does not, by itself, prove that all customers and liabilities were included, that no negative balances were suppressed, or that management did not create false accounts.

## 10. Continuous monitoring versus continuous audit

### What is feasible

Blockchain data can support near-real-time control monitoring:

- wallet and contract balance reconciliation;
- admin, mint, burn, pause, and upgrade alerts;
- oracle freshness and deviation checks;
- reserve-to-recorded-liability coverage;
- related-address and circular-flow alerts;
- closing block/hash certification;
- bridge and wrapped-supply reconciliation;
- transaction-limit and allowlist exceptions; and
- proof that an approved code version remains deployed.

### Reference architecture

1. Read from at least two independent sources, including an entity-controlled full/archive node for material chains where practical.
2. Ingest blocks idempotently and retain block height, block hash, parent hash, chain ID, transaction status, logs, traces, and finality status.
3. Detect gaps, duplicates, reorganizations, and provider disagreement.
4. Reconcile state balances to transaction rollforwards and the ERP subledger.
5. Run governed rules with versioned thresholds and retained results.
6. Route exceptions to named owners with severity, evidence, remediation, and deadline.
7. Preserve an audit evidence package and allow independent read-only reperformance.
8. Periodically test the monitors themselves, including planted failures.

### What it does not mean

Continuous management monitoring is not a continuously updated independent audit opinion. AS 2201 and AS 1105 still require sufficient appropriate evidence, control testing, and auditor judgment. Automated controls can fail systematically; the auditor should test the monitor's design, source completeness, rule logic, change control, and exception follow-up, and should retain independent substantive procedures for significant accounts and assertions.

## 11. Failure and recovery playbook

The recovery design should assume at least these scenarios:

- compromised or lost treasury/admin/oracle key;
- smart-contract logic or initialization defect;
- exploited contract or bridge;
- false or unavailable oracle;
- RPC/indexer/node outage;
- chain reorganization, halt, censorship, or fork;
- governance attack or signer collusion;
- custodian or stablecoin insolvency;
- fee/gas spike or congestion;
- privacy breach;
- erroneous mass execution; and
- accounting interface corruption.

For each scenario define:

- detection threshold and owner;
- authority to pause and maximum pause duration;
- assets and contracts affected;
- alternate settlement and manual accounting;
- evidence preservation;
- legal and regulatory notification;
- key rotation, code migration, replay protection, and customer restitution;
- treatment of in-flight and duplicated transactions;
- accounting cutoff and valuation;
- reconciliation from last trusted block/state;
- independent validation before reopening; and
- post-incident ICFR and disclosure review.

Upgradeability improves recoverability but creates a powerful administrator risk. Immutability limits administrator discretion but can make defects irreversible. The control decision must be explicit and proportional to financial impact.

## 12. Which accounting games are reduced, and which migrate

### Games materially reduced when the full control stack works

| Traditional game | Why it becomes harder | Important condition |
|---|---|---|
| Deleting or silently rewriting source transactions after the fact | Prior finalized records and hashes expose alteration. | Auditor uses an independent chain source and monitors forks/migrations. |
| Backdating an on-chain settlement after the period close | Block order and closing hash are independently observable. | Accounting recognizes that block time may differ from legal/economic event time. |
| Duplicate spending of the same native asset on the same canonical chain | Consensus rejects conflicting finalized spends. | Does not prevent duplicate obligations, wrapped claims, off-chain double counting, or cross-chain bridge failures. |
| Bilateral reconciliation manipulation | Parties can reference the same canonical event and state. | Only for transactions actually represented on that ledger and interpreted consistently. |
| Manual settlement/calculation errors | Tested deterministic code can execute the approved formula consistently. | Code, inputs, decimals, and upgrade controls must be correct. |
| Unauthorized ordinary payments | Signature and role rules can block users lacking required authority. | Keys must be protected; admin bypasses and signer collusion must be controlled. |
| Concealing later changes to automated rules | Version/address/admin events can be publicly monitored. | Proxy implementations, off-chain interfaces, and governance changes must be included. |

### Games that migrate or become more important

| Migrated game | New mechanism | Control response |
|---|---|---|
| Fictitious transactions / round-tripping | Related parties operate pseudonymous wallets or bots. | Address attribution, counterparty confirmation, related-party analytics, economic-substance review. |
| Window-dressed cash or reserves | Borrow assets for the snapshot, return immediately afterward. | Unannounced and period-based testing, liability completeness, borrowing/encumbrance confirmation, subsequent events. |
| Hidden liabilities | Put assets on-chain but keep customer claims, guarantees, side letters, or affiliate obligations off-chain. | Legal and accounting perimeter controls; full liability reconciliation; confirmations and search for unrecorded liabilities. |
| Price manipulation | Trade thin tokens among related wallets or manipulate an oracle/DEX immediately at measurement time. | Principal-market and orderliness testing, multi-source prices, liquidity/related-party filters, TWAP/deviation controls. |
| Management override | Use upgrade, mint, pause, seize, proxy, bridge, or oracle admin keys. | Privilege inventory, independent multisig/timelock, real-time monitoring, board oversight. |
| “Authorized” theft | Attacker uses a compromised valid key or exploits code exactly as deployed. | Key custody, transaction intent controls, anomaly monitoring, legal classification independent of protocol validity. |
| Cutoff manipulation | Select favorable chain, block, time zone, finality threshold, or omit pending/reorged transactions. | Formal cutoff policy, exact close hash, chain-specific finality, subsequent reorg testing. |
| Classification arbitrage | Describe an economically complex token as “cash,” “reserve,” “commodity,” or “utility.” | Product-level accounting/legal memo and embedded-feature analysis. |
| Completeness manipulation | Omit addresses, contracts, chains, internal calls, failed calls, bridges, or custodians from the indexer. | Independent discovery, population reconciliation, block-range and state-to-flow controls. |
| Control theater | Publish source code, a code audit, or proof of reserves as though it were a financial-statement audit. | Clear criteria, scope, assurance level, limitations, and auditor independence; reconcile to full audited statements. |
| Privacy-based selective disclosure | Reveal favorable proof or wallet subset while hiding the population. | Commitment/population completeness controls, verifier and circuit assurance, independent source reconciliation. |
| Error parking | Leave an erroneous immutable transaction in one view while “fixing” only the ERP or presentation layer. | Linked compensating transaction and journal; original-to-correction traceability; period-by-period materiality review. |

## 13. Auditor work program

### Planning and scoping

1. Identify every material chain, token, wallet, smart contract, custodian, bridge, oracle, admin key, and reporting interface.
2. Determine whether specialized blockchain, cybersecurity, valuation, tax, or legal skill is required.
3. Document which assertions rely on chain evidence and which require off-chain evidence.
4. Identify service organizations and obtain/assess relevant control reports, but do not assume a generic SOC report covers wallet, smart-contract, oracle, or bridge controls.
5. Assess fraud risk around pseudonymity, related parties, reserve snapshots, valuation, admin override, and omitted liabilities.

### Tests of controls

1. Inspect and reperform key generation, signing, recovery, access recertification, and transaction approval.
2. Compare deployed bytecode, proxy state, and parameters with the approved release.
3. Test change management, code review, deployment, emergency changes, and timelocks.
4. Test oracle source, aggregation, staleness, deviation, and fallback.
5. Test node/indexer completeness, reorg logic, and state-to-flow reconciliation.
6. Inspect exception alerts and evidence of timely investigation.
7. Test accounting mappings, closing snapshot, valuation controls, and correction workflow.

### Substantive procedures

1. Independently obtain balances and transactions; do not rely solely on management's explorer export.
2. Prove key control and separately establish legal rights.
3. Confirm custodians, counterparties, restrictions, and liabilities.
4. Test transactions around close and chain finality.
5. Reperform valuation and principal-market selection.
6. Search for unrecorded wallets, obligations, and related-party flows.
7. Inspect subsequent transfers, depegs, exploits, forks, corrections, and legal disputes.
8. Reconcile on-chain units to the GL and disclosures.

## 14. Source crosswalk and exact URLs

### Auditing and internal control

1. PCAOB, **AS 1105: Audit Evidence**  
   https://pcaobus.org/oversight/standards/auditing-standards/details/AS1105  
   Key application: sufficiency/appropriateness; electronic-information reliability; accuracy and completeness of company-produced information; inspection, confirmation, recalculation, and reperformance.

2. PCAOB, **AS 2501: Auditing Accounting Estimates, Including Fair Value Measurements**  
   https://pcaobus.org/oversight/standards/auditing-standards/details/AS2501  
   Key application: crypto/token fair value, significant assumptions, third-party pricing, model risk, and management bias.

3. PCAOB, **AS 2201: An Audit of Internal Control Over Financial Reporting**  
   https://pcaobus.org/oversight/standards/auditing-standards/details/AS2201  
   Key application: top-down risk-based ICFR scope, automated controls, material weaknesses, and integrated control/financial-statement audit.

4. PCAOB, **AS 2905: Subsequent Discovery of Facts Existing at the Date of the Auditor's Report**  
   https://pcaobus.org/oversight/standards/auditing-standards/details/AS2905  
   Key application: response when an exploit, hidden key, contract defect, or other fact existing at report date is discovered later.

5. GAO, **Standards for Internal Control in the Federal Government (2025 Green Book)**  
   https://www.gao.gov/greenbook  
   Direct report page: https://www.gao.gov/products/gao-25-107721  
   Key application: authorization, segregation of duties, information-system controls, monitoring, and remediation.

6. GAO/CIGIE, **Federal Information System Controls Audit Manual (FISCAM)**  
   https://www.gao.gov/fiscam  
   Current report page: https://www.gao.gov/products/gao-26-108633  
   Key application: access, configuration/change management, segregation of duties, contingency planning, application controls, and audit methodology.

7. Bureau of the Fiscal Service / U.S. Standard General Ledger Board, **USSGL Board Purpose and Bylaws / compliance criteria**  
   https://www.fiscal.treasury.gov/files/ussgl/board-irc-mtgs/2016/irc-may-12-2016/ussgl-board-purpose-bylaws-2016.pdf  
   Key application: transaction-level standard ledger, self-balancing accounts, clear audit trails back to source documents, and traceability from source entry to central reporting.

### Blockchain, smart contracts, keys, and legal risk

8. NIST, **NISTIR 8202: Blockchain Technology Overview**  
   https://www.nist.gov/publications/blockchain-technology-overview  
   Direct PDF: https://nvlpubs.nist.gov/nistpubs/ir/2018/NIST.IR.8202.pdf  
   Key application: tamper evidence/resistance, smart contracts, determinism, oracles, permissions, forks, and technology limitations.

9. GAO, **GAO-22-104625: Blockchain—Emerging Technology Offers Benefits for Some Applications but Faces Challenges**  
   https://www.gao.gov/products/gao-22-104625  
   Direct PDF: https://www.gao.gov/assets/gao-22-104625.pdf  
   Key application: privacy, oracle/data reliability, limited recourse, enforceability differences, governance, interoperability, and implementation tradeoffs.

10. NIST, **SP 800-57 Part 1 Rev. 5: Recommendation for Key Management—General**  
    https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final  
    Key application: key lifecycle, protection, accountability, compromise, recovery, rotation, archival, and destruction.

11. CFTC LabCFTC, **A Primer on Smart Contracts**  
    https://www.cftc.gov/sites/default/files/2018-11/LabCFTC_PrimerSmartContracts112718.pdf  
    Alternate official PDF: https://www.cftc.gov/sites/default/files/2018-11/LabCFTC_PrimerSmartContracts112718_0.pdf  
    Key application: operational, technical, cybersecurity, fraud/manipulation, governance, and potentially applicable legal frameworks. It is an educational staff product, not binding CFTC policy.

12. U.S. Treasury, **Illicit Finance Risk Assessment of Decentralized Finance (April 2023)**  
    https://home.treasury.gov/system/files/136/DeFi-Risk-Full-Review.pdf  
    Release: https://home.treasury.gov/news/press-releases/jy1391  
    Key application: actual centralization through administrative keys/governance, cyber vulnerabilities, public-chain transparency limits, and continuing legal/compliance obligations despite automation.

13. Uniform Law Commission, **Guidance Note Regarding UETA, ESIGN, Blockchain Technology and Smart Contracts**  
    https://www.uniformlaws.org/viewdocument/guidance-note-regarding-the-relatio-1?CommunityKey=c63debda-e05e-4cc7-91b2-56aac3e68cbc  
    Key application: interaction of electronic-transaction law with blockchain and smart contracts; state-law adoption must be checked.

### Accounting, error correction, custody, and proof of reserves

14. FASB, **ASU 2023-08: Accounting for and Disclosure of Crypto Assets**  
    https://storage.fasb.org/ASU%202023-08.pdf  
    Key application: defined scope, fair value through net income, separate presentation, unit/cost/fair-value disclosures, restrictions, and annual rollforward.

15. SEC, **Staff Accounting Bulletin No. 122**  
    https://www.sec.gov/rules-regulations/staff-guidance/staff-accounting-bulletins/staff-accounting-bulletin-122  
    Key application: rescission of SAB 121; safeguarding loss contingencies under ASC 450-20/IAS 37 and continued disclosure of safeguarding obligations and risks. Effective January 30, 2025.

16. PCAOB Office of the Investor Advocate, **Exercise Caution With Third-Party Verification / Proof of Reserve Reports**  
    https://pcaobus.org/resources/information-for-investors/investor-advisories/investor-advisory-exercise-caution-with-third-party-verification-proof-of-reserve-reports  
    Key application: PoR is not an audit; point-in-time assets do not establish liabilities, rights, restrictions, or absence of borrowed/window-dressed reserves. This is an investor-advisory staff view, not a Board rule.

17. SEC Chief Accountant, **The Potential Pitfalls of Purported Crypto “Assurance” Work**  
    https://www.sec.gov/newsroom/speeches-statements/munter-statement-crypto-072723  
    Key application: non-audit work is not equivalent to a financial-statement audit; accountants should not allow misleading marketing of limited procedures. It is an official-capacity staff statement, not a Commission rule.

18. SEC, **Staff Accounting Bulletin No. 99—Materiality**  
    https://www.sec.gov/interps/account/sab99.htm  
    Key application: quantitative threshold alone is insufficient; qualitative factors and intentional misstatement matter.

19. SEC, **Staff Accounting Bulletin No. 108—Quantifying Misstatements**  
    https://www.sec.gov/rules-regulations/staff-guidance/staff-accounting-bulletins/staff-accounting-bulletin-no-108  
    Key application: assess both rollover and iron-curtain effects so blockchain/ERP differences or accumulated correction entries do not remain indefinitely.

## 15. Board and audit-committee dashboard

At least quarterly—and immediately after material incidents—report:

- assets and obligations by chain, custodian, bridge, and legal entity;
- all privileged keys, quorum, signer concentration, and recertification status;
- deployed contract versions and unapproved drift;
- admin, mint, burn, pause, seize, oracle, and upgrade activity;
- oracle outages, stale values, and deviations;
- unresolved reconciliation exceptions;
- chain reorganizations, halts, forks, and bridge depegs;
- failed, reversed, compensated, and disputed transactions;
- privacy incidents and on-chain sensitive-data exposures;
- reserve coverage calculated with complete liabilities and encumbrances;
- valuation sources, liquidity exceptions, and Level 3 exposures;
- control deficiencies and remediation aging;
- recovery-test results; and
- any use of “audit,” “assurance,” or “proof” in external marketing that could exceed the actual engagement scope.

## Final design principle

The strongest implementation treats blockchain as a controlled financial subledger—not as a substitute for accounting, law, governance, or audit. The canonical audit trail should connect:

`economic event → legal right/obligation → authorized oracle/input → approved code/version → finalized chain event → complete controlled extraction → accounting classification and valuation → GL/disclosure → independent evidence`

If any link is missing, the ledger may be immutable while the financial statement is still wrong.
