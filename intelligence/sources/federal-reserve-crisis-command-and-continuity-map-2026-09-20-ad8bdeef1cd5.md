# Federal Reserve crisis command and continuity map

**Date:** September 20, 2026
**Evidence cutoff:** September 20, 2026
**Campaign position:** Wave 6 of the Federal Reserve structure research campaign
**Question:** Who decides, operates, books, communicates, bears risk and ends the response when a bank, market, payment rail, Reserve Bank or fiscal-agent function fails?
**Status:** public-authority and operating-constitution synthesis; security-sensitive incident playbooks remain nonpublic

## Bottom line

There is no single Federal Reserve “crisis commander.” Congress and the Federal Reserve have built **scenario-specific command chains**:

- an insured-bank failure is closed by its chartering authority and resolved by the FDIC—not by the Federal Reserve;
- ordinary Discount Window credit is a secured Reserve Bank lending decision under Board rules, with interdistrict continuity capable of preserving the originating Bank’s books while another Bank performs the work;
- a section 13(3) facility requires a broad-based program, at least five affirmative Governors, prior Treasury Secretary approval, solvency and collateral protections, and a Reserve Bank to extend the credit;
- a market-liquidity or monetary-policy response is directed by the FOMC and executed through the selected Reserve Bank and the Open Market Desk;
- a Fedwire, FedNow, NSS or FedLine incident is an FRFS/Reserve Bank operating event governed by operating circulars, service procedures, continuity infrastructure and participant obligations—not an FOMC monetary-policy vote;
- a cyber incident at a supervised institution invokes the institution, its service providers and supervisory reporting/response chain; a cyber incident in Federal Reserve infrastructure also invokes the nonpublic National IT/FRFS enterprise incident chain;
- a cash or Treasury-service disruption uses physical redistribution, alternate sites, manual channels and fiscal-agent recovery arrangements rather than the legal authorities for central-bank lending; and
- 12 U.S.C. §248(h) is an institutional enforcement and receivership-like power for a Reserve Bank that violates law. It is **not** the ordinary business-continuity authority used when a site, application or staff unit is impaired.

The public record therefore reveals the legal principals, several operating fallbacks, the books on which some emergency credit remains and the public communication channels. It does **not** reveal the complete named incident commander, severity matrix, emergency-change authority, cyber containment thresholds, physical topology, application failover order, liability allocation or after-action archive. Those gaps are properly treated as **not public**, not silently filled by the title of the host Bank or product office.

## 1. Never collapse these eight clocks

| Clock | Trigger question | Controlling proof |
|---|---|---|
| **Operational continuity** | Can the same authorized function continue through another site, channel, staff or Bank? | operating circular, continuity agreement, board resolution, service playbook |
| **Liquidity** | Does an otherwise eligible institution lack immediately available funds? | Regulation A, Reserve Bank credit decision, collateral and account records |
| **Solvency / resolution** | Is the institution viable, or has the chartering authority closed it? | supervisory/chartering determination, FDIC appointment and receivership record |
| **Monetary policy / market functioning** | Should reserve conditions or market liquidity change systemwide? | FOMC directive, authorization and Desk operation |
| **Settlement finality** | Was a payment or securities transfer actually accepted and posted? | Regulation J, operating circular, service transaction and reconciliation records |
| **Legal authorization** | Which actor may act, on what asset and under what conditions? | statute, regulation, Board/FOMC vote, Treasury approval, delegation |
| **Recovery and normalization** | When are processing and ordinary access restored, reconciled and tested? | service-status notice, gap reports, incident closure, restoration tests |
| **Loss allocation / exit** | Who holds the asset or loss, and who ends the extraordinary measure? | loan/booking record, receivership priority, indemnity, facility termination and audit trail |

A system can be operational while a participant is insolvent; a participant can be liquid while its access channel is down; a service can be restored while its users are still unreconciled; and a legally final transfer is not undone merely because the system later fails. The command map must therefore identify the clock before identifying the commander.

## 2. Whole-system scenario matrix

| Scenario | Legal principal / final decision | Operating lead | Booking and exposure | Public communication | Exit / remaining unknowns |
|---|---|---|---|---|---|
| **Insured depository institution failure** | Chartering authority closes; FDIC becomes receiver. Systemic-risk exception and Title II routes have their own statutory actors | FDIC resolution team; acquirer or bridge institution if used | Failed-bank estate/FDIC receivership; any valid Reserve Bank loan and collateral must be separately accounted for | FDIC and chartering authority | Receivership, sale, bridge wind-down or liquidation. Fed liquidity does not itself decide solvency or recapitalize the failed institution |
| **Ordinary Discount Window need** | Lending Reserve Bank, under Regulation A and Board policy; no institution has a right to a loan | Local Discount Window/credit-risk team, with national/interdistrict support | Loan is secured to the lending Bank’s satisfaction and ordinarily carried on the relevant Reserve Bank’s books | Direct borrower channel; public aggregates and delayed transaction disclosure as law requires | Repayment, renewal, collateral release/liquidation or resolution; detailed credit file remains protected |
| **Local Discount Window operation impaired** | Originating Bank’s authorized corporate/Discount Committee route; Board rules continue | Contingency site or another Reserve Bank may answer, process collateral and perform credit-risk functions | Public St. Louis bylaw model expressly keeps credit **on the originating Bank’s books**; Atlanta/Dallas records confirm interdistrict planning but not every counterparty or term | District toll-free number is rerouted; another Bank may assist | Return to local operation; nonpublic resolution must prove activation, delegation, liability and termination |
| **Section 13(3) emergency facility** | Board: at least five affirmative Governors; prior Treasury Secretary approval; statutory/regulatory program conditions | A designated Reserve Bank extends credit under the Board-approved program | On lending Reserve Bank’s books, subject to collateral/lendable-value, loss-protection and program terms; Treasury equity or guarantee is separate if supplied | Board/Treasury announcements plus statutory reports and transaction disclosures | Board periodically reviews unusual and exigent circumstances and need; program must terminate in a timely, orderly way. Facility is not an ad hoc rescue of one failing firm |
| **Market-liquidity / monetary-policy emergency** | FOMC; between meetings the FOMC Chair has bounded authority under the current authorization | Selected Reserve Bank/Open Market Desk executes for SOMA | SOMA, allocated among Reserve Banks under Committee procedures | FOMC/Desk statements, operation results and later minutes | FOMC/Chair instruction changes or ends operations; Desk does not originate independent monetary policy |
| **Selected Bank cannot operate SOMA** | FOMC Chair may appoint another Reserve Bank as temporary SOMA agent | Substitute Bank and temporarily appointed SOMA manager | Still SOMA activity, not the substitute Bank’s independent policy portfolio | Public disclosure timing depends on event and FOMC rules | Ends when ordinary selected-Bank operation resumes or Committee acts |
| **National-security emergency and FOMC unreachable/nonfunctional** | Each Reserve Bank may use the FOMC’s narrow emergency authorization after specified consultation efforts | Acting Reserve Bank, coordinated with reachable Banks where feasible | Bank’s own account for the authorized U.S.-obligation transactions; specified foreign operations only on authorized Treasury request | Event-dependent | Authority ends when communication with a functioning FOMC is restored |
| **Fedwire Funds outage** | Reserve Banks as service operator under Regulation J/OC 6; extensions use published FRFS criteria | FRFS/wholesale operations with National IT infrastructure and support | Transfers already posted remain final; unresolved messages require transaction-level reconciliation | Service Status, FedLine Home/email, Wholesale Customer Support | Recover to disruption point, reconcile, avoid duplicates, then resume; exact internal incident commander and thresholds are nonpublic |
| **Fedwire Securities or collateral-settlement outage** | Reserve Banks under OC 7 and applicable book-entry rules; PSR credit controls remain with the relevant Reserve Bank | Securities operations/FRFS/National IT; limited offline arrangements may apply | Posted securities/funds debits and credits remain final; collateral availability and daylight exposure are separate | Service Status and customer support | Reconcile endpoint totals/gaps and resume. An operational outage does not authorize reversal of a completed final transfer |
| **FedNow interruption** | Reserve Banks under Regulation J subpart C and OC 8 | FedNow/FRFS operations with National IT and participant/service-provider continuity | Accepted/posted transfers governed by the service’s finality rules; interruption may delay messages and requires position reconciliation under Reserve Bank instructions | Service Status, support channels and participant notices | Restore, reconcile and resume under current procedures; fraud-tool unavailability is not itself a settlement stop |
| **Participant or service-provider outage** | Participant controls its own continuity; Reserve Banks control service access and risk exposure | Participant, its service provider, correspondent or prearranged third party; FRFS supports but does not run the participant | Participant/correspondent accounts; alternative routing can create separate exposures | Participant communications plus Service Status/FRFS support | Restore own channel and reconcile before resending. Participant “buddy bank” is a third-party service arrangement, not a Buddy Reserve Bank |
| **Excessive daylight-credit / collateral risk** | Relevant Reserve Bank under Board PSR policy | Administrative Reserve Bank and credit-risk/operations teams | Participant’s master account and pledged collateral; Reserve Bank bears residual exposure | Direct institutional contact; not necessarily a public incident | Cap reduction, added balances/collateral, delayed/rejected transactions or, in extreme cases, offline/Fedwire prohibition |
| **Cyber incident at supervised institution** | Institution’s management/board contains the event; primary federal regulator exercises supervisory authority | Institution and service providers, then Board/Reserve Bank supervisory incident process | Institution/vendor losses and obligations; payment finality and Reserve Bank credit remain separate | Board-regulated banking organization must notify the Board within 36 hours after determining a notification incident; covered service providers notify affected banking customers of qualifying disruption | Containment, recovery, supervisory remediation and enforcement if warranted; notification is not transfer of incident command to the Fed |
| **Cyber incident in Federal Reserve infrastructure** | Service/Bank/National IT governance under Board oversight; policy or credit decisions remain with their statutory bodies | National IT Enterprise Incident Management and FRFS/service teams at the public high level | Depends on affected Bank, application, account and contract; Richmond hosting does not by itself allocate liability | Service Status and protected institutional channels; law-enforcement/CISA coordination as applicable | Technical recovery, reconciliation, control remediation and governance review. Named commander, severity thresholds and emergency-change rights are nonpublic |
| **Reserve Bank statutory violation** | Board under 12 U.S.C. §248(h) | Board may suspend Bank operations, take possession and administer | Board controls the institution during statutory intervention; liquidation/reorganization may follow | Board/Congress/court record as applicable | Liquidate, reorganize or restore. This is not ordinary site failover and no public evidence located shows current activation |
| **Physical cash disruption** | Reserve Banks operate cash distribution under Board policy; Treasury/BEP and Mint retain their separate production/coin roles | Local FedCash office, another Reserve Bank office, armored carriers and manual ordering channels | Currency inventory and Bank/customer cash-order accounting; delayed debit/credit possible | Service Status, local office, FedLine/email and carrier contacts | Restore office/automation; redirection and temporary order limits do not change dollar issuance authority |
| **Treasury fiscal-agent outage** | Treasury remains fiscal principal; Reserve Banks act as fiscal agents under Treasury designation and agreement | Relevant fiscal-agent Bank/product office; TRSO coordinates the System relationship; backup sites/redistribution depend on service | Treasury accounts and fiscal-agent records—not SOMA or the Reserve Bank’s own policy account merely because a Reserve Bank operates the system | Treasury/Fiscal Service and FRFS service channels | Restore/reroute and reconcile under the service plan. Treasury Auction has published backup mechanisms; the complete application-by-application command matrix is not public |

## 3. Bank failure is not a Federal Reserve receivership

For an insured bank, the ordinary failure sequence is: the chartering authority revokes or terminates the charter and closes the institution; the FDIC is appointed receiver; the FDIC transfers assets and liabilities to an acquirer or bridge bank where authorized, pays insured deposits and administers the remaining estate. The Federal Reserve can supervise certain institutions before failure, supply eligible secured liquidity, operate the master account and coordinate on resolution planning, but it is not the ordinary statutory receiver.

That distinction limits the claim “the Fed saved/closed/took over the bank.” A Reserve Bank may lend against collateral before failure, and the FDIC or a bridge bank may assume an obligation after failure, as occurred in the 2023 failures. But a central-bank loan is an asset/liability relationship; it does not itself transfer the charter, determine receivership priority or make an insolvent institution solvent.

Primary routes: [FDIC failing-bank resolutions](https://www.fdic.gov/resources/resolutions/); [FDIC Resolutions Handbook](https://www.fdic.gov/bank-failures/resolutions-handbook); [FDIC 2025 discussion of receiver borrowing and the 2023 bridge banks](https://www.fdic.gov/news/speeches/2025/resolution-readiness-and-lessons-learned-recent-large-bank-failures).

## 4. The three central-bank liquidity lanes

### A. Intraday credit supports settlement

Board Payment System Risk policy lets Reserve Banks provide daylight overdrafts to support payment flows while managing their own credit exposure. The relevant Reserve Bank can lower a net-debit cap, require balances or more collateral, delay or reject transactions and, in an extreme case, take an institution offline or prohibit Fedwire use. The administrative Reserve Bank holds overall risk-management responsibility for specified multidistrict structures.

This is a payment-liquidity and risk-control lane. It is not the same as an overnight Discount Window loan, a section 13(3) program or an FDIC solvency determination.

Source: [Federal Reserve Policy on Payment System Risk](https://www.federalreserve.gov/paymentsystems/files/psr_policy.pdf).

### B. Discount Window credit supports eligible depository institutions

Regulation A distinguishes primary, secondary and seasonal credit. Primary credit is for institutions in generally sound condition; secondary credit can provide very short-term backup funding to an institution not eligible for primary credit and can be extended longer when it facilitates orderly resolution of serious difficulties, subject to the special restrictions for undercapitalized and critically undercapitalized institutions. A Reserve Bank has no general obligation to lend and requires collateral satisfactory to it.

Continuity does not change the credit principal. The national continuity page says calls can be rerouted to a contingency site or another Reserve Bank. St. Louis’s current bylaws make the accounting result explicit: another Bank can exercise full authority on St. Louis’s behalf and **on St. Louis’s books** under a board-authorized contingency. Atlanta and Dallas board materials confirm Buddy/interdistrict mechanisms but do not publicly identify all counterparties, triggers, loss allocation or termination records.

Primary routes: [Discount Window business continuity](https://www.frbdiscountwindow.org/rightnavpages/business-continuity); [St. Louis Reserve Bank bylaws](https://www.stlouisfed.org/about-us/leadership-governance/bank-bylaws); [Regulation A, 12 C.F.R. part 201](https://www.federalreserve.gov/supervisionreg/reglisting.htm#A); [Operating Circular 10](https://www.frbservices.org/resources/rules-regulations/operating-circulars.html).

### C. Section 13(3) is a Board/Treasury emergency-program lane

Section 13(3), as rewritten by Dodd–Frank, is not a roving power of a Reserve Bank president. The Board must establish a program or facility with broad-based eligibility; at least five Board members must vote affirmatively; the Secretary of the Treasury must give prior approval; the program may not be designed to aid a single failing firm; credit may not go to an insolvent borrower; and lending must be secured to the Reserve Bank’s satisfaction under loss-protection and lendable-value rules. A Reserve Bank then extends the credit under the program.

The Board must review whether unusual and exigent circumstances and the facility’s market-restoring need continue, and terminate the program in a timely and orderly fashion. Treasury approval is therefore a real statutory veto at activation, not daily operational command over every loan. Likewise, the lending Reserve Bank performs and books the extension but does not create the program unilaterally.

Primary routes: [12 U.S.C. §343](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title12-section343&num=0&edition=prelim); [Regulation A emergency-lending final rule](https://www.federalreserve.gov/newsevents/pressreleases/bcreg20151130a.htm); [Board crisis-response overview](https://www.federalreserve.gov/financial-stability/responding-to-financial-system-emergencies.htm).

## 5. FOMC crisis command is a different constitution

The FOMC directs open-market policy; the selected Reserve Bank and Open Market Desk execute for SOMA. Under the authorization effective January 27, 2026, the FOMC Chair may, between meetings and within the authorization’s boundaries, instruct the selected Bank to adjust somewhat the policy stance in exceptional circumstances or undertake eligible-securities transactions addressing temporary operational or highly unusual disruptions in dollar funding markets. Consultation with the Committee is required whenever feasible.

Two continuity rules matter:

1. If the selected Bank cannot function, the FOMC Chair may temporarily appoint another Reserve Bank as SOMA agent and a temporary SOMA manager.
2. During and following a national-security emergency, if a Bank cannot reach the FOMC after reasonable efforts or the Committee cannot function, the current emergency authorization permits limited own-account U.S.-obligation operations and specified foreign-currency operations, after the stated consultation efforts. That authority ends once communication with a functioning Committee returns.

These rules do not make the FOMC the incident commander for Fedwire, FedNow, National IT, cash distribution or an individual failed bank. They preserve the monetary-policy and market-operations function.

Primary routes: [2026 FOMC authorizations and continuing directives](https://www.federalreserve.gov/monetarypolicy/files/FOMC_AuthorizationsContinuingDirectivesOMOs.pdf); [FOMC rules and authorizations index](https://www.federalreserve.gov/monetarypolicy/rules_authorizations.htm).

## 6. Payment-service continuity: finality survives the outage

### Fedwire Funds

The public continuity guide identifies out-of-region backup facilities, testing for facility/hardware/network/staff loss, Service Status communications, alternate access, a limited contingency service for critical transactions, operating-hour extensions and post-restoration gap/endpoint reconciliation. A transfer is final and irrevocable once the debit and credit are made. The guide warns users not to resend uncertain messages because duplicates can occur.

The 2025 FedPayments Manager–Funds Contingency Service replaced the telephone Fedwire Funds Offline Service as the last-resort option for a small number of critical transactions. It is not a substitute for high-volume participant continuity. Nor does an extension request give a participant command over the service; the Reserve Banks apply the published extension criteria.

Source: [Fedwire Funds business continuity](https://www.frbservices.org/financial-services/wires/business-continuity); [wholesale-service extension guidelines](https://www.frbservices.org/resources/financial-services/wires/extension-guidelines.html); [Operating Circular 6](https://www.frbservices.org/resources/rules-regulations/operating-circulars.html).

### Fedwire Securities and collateral settlement

Fedwire Securities combines a securities account and central securities depository with final gross delivery-versus-payment settlement. Once the securities and related funds debits and credits are made, the transfer is final and irrevocable. A later reversal is a new, separately coded transfer; it does not erase the original finality.

During an outage, users must distinguish messages that never reached the service, messages whose acknowledgment is missing and transfers already processed. Gap Reports, Endpoint Grand Totals and detailed summaries support the recovery. Collateral and daylight-credit consequences still follow the applicable PSR, lending and custody records; “securities service down” is not itself permission to treat pledged collateral as free or a settled delivery as void.

Sources: [Fedwire Securities business continuity](https://www.frbservices.org/financial-services/securities/business-continuity.html); [Fedwire Securities PFMI disclosure](https://www.frbservices.org/binaries/content/assets/crsocms/financial-services/securities/securities-service-disclosure.pdf).

### FedNow

Current OC 8 and the April 28, 2026 operating procedures govern the 24×7 service with Regulation J subpart C. The circular assigns participants their own continuity/testing duties, permits contingency service-provider arrangements and requires position reconciliation under Reserve Bank instructions following a qualifying emergency or service failure. The Reserve Banks communicate operational problems through Service Status and other protected channels.

The library’s April 2026 procedures finding remains important: a fraud tool can be unavailable or time out while message processing continues. A warning or after-cycle notice is not necessarily a settlement gate. Operational status, fraud screening, transaction acceptance and finality must be proved separately.

Sources: [current operating circulars and procedures](https://www.frbservices.org/resources/rules-regulations/operating-circulars.html); [FedNow resources](https://www.frbservices.org/resources/financial-services/fednow).

### The two meanings of “buddy bank”

1. **Participant buddy bank:** the Fedwire continuity guide uses the lowercase concept for a participant’s pre-established third-party service-provider arrangement. It is the participant’s alternate route.
2. **Buddy Reserve Bank:** Atlanta minutes, St. Louis bylaws and Dallas minutes evidence an interdistrict Federal Reserve continuity mechanism for Discount Window/credit-risk work. It is a delegation among separately incorporated Reserve Banks and can preserve the originating Bank’s books.

The two mechanisms should never be cited interchangeably.

## 7. Cyber command: operator, supervisor and national coordinator are different roles

A cyber event at a bank is first the bank’s incident. Management and its service providers detect, contain, recover and communicate. Under the federal notification rule, a Board-regulated banking organization must notify the Board as soon as possible and no later than 36 hours after it determines that a qualifying notification incident occurred; a covered bank service provider must notify affected banking customers as soon as possible when a qualifying incident is likely to cause material disruption or degradation for four or more hours. Supervision can demand remediation or bring enforcement, but the notice does not automatically transfer technical incident command to the regulator.

A cyber event affecting Federal Reserve infrastructure follows another route. Public National IT material identifies Enterprise Incident Management coordination and public FRFS material identifies service communication and recovery channels. Board oversight, Bank boards, FRFS product leadership, National IT and affected service teams remain legally distinct. No public application-level instrument recovered by the cutoff identifies the named incident commander, severity levels, emergency-change approver, isolation authority, recovery priority, evidence-custody chain and loss allocation for each core rail.

The OIG’s 2023 evaluation is a warning against assuming clarity from organizational labels: for supervised-institution cyber response, it found that guidance did not clearly describe the mission or governance structure and that staff did not always follow the established process. That finding concerns the supervisory response process, not proof of an incident in Federal Reserve production systems.

Primary routes: [Board cybersecurity and operational resilience](https://www.federalreserve.gov/supervisionreg/cybersecurity-and-operational-resilience.htm); [OIG supervised-institution incident-response evaluation](https://oig.federalreserve.gov/reports/board-cyber-incident-response-jun2023.htm); [Richmond/National IT governance RACI](../sources/richmond-national-it-governance-and-control-raci-2026-08-15-c1fc308bb01b.html).

## 8. Reserve Bank impairment versus statutory forfeiture

An inaccessible building, disabled application, staff shortage or disrupted communications normally invokes continuity mechanisms. Another site, staff unit or Reserve Bank can perform defined work without dissolving the originating corporation or transferring its assets generally.

Section 11(h) of the Federal Reserve Act, codified at 12 U.S.C. §248(h), is different. When a Reserve Bank violates the Act, the Board may suspend the Bank’s operations, take possession, administer it and, when advisable, liquidate or reorganize it. This is the violation-based institutional intervention that sits behind the Act’s statement that Reserve Banks continue for twenty years from organization and thereafter until dissolved by Congress or forfeiture of franchise for violation of law.

No public record located for this wave shows §248(h) activated against a Reserve Bank. A continuity exercise, another Bank answering a phone, interdistrict credit performance or a technical failover is not evidence of franchise forfeiture. Conversely, §248(h) should not be cited as the ordinary source of FRFS or National IT emergency authority.

Primary routes: [12 U.S.C. §248](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title12-section248&num=0&edition=prelim); [12 U.S.C. §341](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title12-section341&num=0&edition=prelim).

## 9. Physical cash and Treasury fiscal-agent continuity

### Cash

FedCash continuity uses manual email/fax ordering when automated channels are unavailable, another Federal Reserve office when a location is inaccessible, carrier redirection, temporary quantity restrictions and delayed cash-order/deposit accounting. Fulfilling currency orders is the published highest priority. The Board’s delegated Uniform Cash Access Policy also permits a temporary waiver for special circumstances such as a natural disaster.

Those actions concern distribution of currency already authorized and supplied through the statutory note/coin structure. They do not allow a cash office, armored carrier or FRFS manager to redefine the dollar, order Federal Reserve notes outside the Board/Treasury process or mint coins.

Sources: [FedCash continuity guide](https://www.frbservices.org/financial-services/cash/business-continuity); [Uniform Cash Access Policy](https://www.federalreserve.gov/frrs/regulations/federal-reserve-uniform-cash-access-policy.htm); [Board currency and coin roles](https://www.federalreserve.gov/paymentsystems/coin_about.htm).

### Treasury fiscal-agent services

The Treasury remains the legal and policy principal; the Reserve Banks act as fiscal agents and service providers. St. Louis’s TRSO manages the Systemwide relationship and coordinates Reserve Bank commitments and technology strategy, but service ownership is distributed. The public Treasury continuity guide says Treasury Auction has multiple backup/recovery mechanisms and that retail-securities work can be redistributed or rerouted if the Minneapolis site is inoperable. Fiscal Service also publishes separate emergency routes for Treasury General Account deposits.

This proves a coordinated fiscal-agent continuity layer. It does not prove that TRSO commands every Treasury application incident, that a Reserve Bank may alter Treasury debt or payment policy, or that a Treasury-owned system becomes Federal Reserve property. The missing application-level RACI must still name Treasury authorizer, product owner, operating Bank, software controller, National IT or vendor host, incident commander, alternative site, accounting owner and termination authority.

Sources: [Treasury Services continuity guide](https://www.frbservices.org/treasury-services/business-continuity.html); [St. Louis 2025 fiscal-agent work](https://www.stlouisfed.org/annual-report/2025/our-people-our-work/supporting-the-us-treasury-as-fiscal-agent); [Fiscal Service TGA emergency procedures](https://fiscal.treasury.gov/payments-to-government/treasury-general-account-tga/emergency-procedures).

## 10. Public command sequence by event phase

| Phase | What public evidence can establish | What remains necessary for a full incident constitution |
|---|---|---|
| **Detect / classify** | service status, statutory threshold, institution notice, public continuity category | severity matrix, cyber/operational classifier, who declares the incident |
| **Authorize** | Board/FOMC/Treasury vote or approval; Bank-board resolution; operating circular and delegated authority | exact emergency delegation, materiality threshold and reserved matters |
| **Contain / keep running** | alternate sites/channels, another Bank, transaction rejection/delay, operating-hours extension | named commander, emergency-change authority, isolation and override rules |
| **Book / protect value** | originating Bank/SOMA/Treasury/receivership account; collateral and finality rules | transaction-level journal, collateral custody, indemnity and loss-sharing terms |
| **Communicate** | Service Status, FedLine/email, regulatory report, Board/FOMC/Treasury/FDIC public release | protected contact tree, interagency escalation, customer-remedy script |
| **Recover / reconcile** | recovery to disruption point, gap reports, endpoint totals, position reconciliation | recovery objectives, test evidence, unresolved-item ledger and exception approvals |
| **Normalize / exit** | facility termination, loan repayment, service-normal notice, returned local operation | exit signer, temporary delegation rescission and after-action remediation closure |
| **Review / disclose** | audit, statutory reports, minutes, delayed transaction data, oversight hearing | complete incident archive, root-cause report, control-owner acceptance and sanctions |

## 11. Corrections and non-claims

1. **Continuity is not authority expansion.** A backup performs only the function authorized by the continuity instrument.
2. **Another Bank’s labor does not automatically move the asset.** St. Louis’s bylaw proves that performance can shift while the loan stays on the originating Bank’s books.
3. **Section 248(h) is not a “buddy Bank” clause.** It is a Board enforcement power for statutory violation.
4. **Hosting is not incident command.** Richmond-hosted National IT, FRFS business control, an operating Bank, a software-controlling Bank and a legal account Bank can all differ.
5. **Service restoration is not reconciliation.** Users must still establish which messages were processed and avoid duplicates.
6. **Finality is not availability.** An outage can prevent future transfers without reversing completed ones.
7. **Liquidity is not solvency.** Discount Window, daylight credit and market operations can supply liquidity within their authorities; FDIC/chartering and insolvency rules govern failure.
8. **Supervisory notice is not operational command.** A cyber notification lets the regulator respond; it does not make the regulator the bank’s technical incident commander.
9. **Treasury approval is not a general Federal Reserve command right.** It is a specific statutory key for section 13(3), while Treasury also remains principal for fiscal-agent work.
10. **“Buddy bank” is ambiguous.** Participant third-party continuity and inter-Reserve-Bank credit continuity are different instruments.

This map does not conclude that a cited contingency has been activated; that every unpublished detail should be public; that an extension request will be granted; that backup operation transfers ownership; that a clean audit certifies resilience; that a service notice proves root cause; or that the Federal Reserve can rescue an insolvent firm outside the conditions Congress enacted.

## 12. Exact missing records and falsifiers

The next evidence layer is not another organization chart. It is the operative incident record:

1. each Reserve Bank’s current interdistrict Discount Window/Buddy Bank resolution, named counterparties, delegation, activation and rescission record;
2. the Systemwide Inter-District Discount Window Operations Contingency Plan approved in Dallas minutes, with booking, collateral custody, legal opinion, indemnity and loss allocation;
3. service-specific FRFS/National IT incident RACI for Fedwire Funds, Fedwire Securities, NSS, FedNow, FedACH, Check, FedLine and common collateral systems;
4. Enterprise Incident Management severity definitions, command succession, emergency-change authority and closure criteria, excluding exploitable topology and credentials;
5. application recovery objectives, last exercise result, exception ledger and corrective-action closure;
6. complete non-security-sensitive service incident archive with start, impact, status changes, restoration, reconciliation and unresolved loss/remedy;
7. Treasury/Federal Reserve application-level fiscal-agent continuity agreements and TRSO escalation matrix;
8. FOMC temporary-SOMA-agent activation record if the authority has ever been used;
9. section 13(3) facility vote, Treasury approval, lending-Bank accounting, collateral valuation, loss protection and termination files for each future activation; and
10. any Board order invoking §248(h), which would falsify the current “no located activation” conclusion.

## Connected library routes

- [Federal Reserve Purse, Audit and Stopping-Power Map](../sources/federal-reserve-purse-audit-and-stopping-power-map-2026-09-20-3b7f8c63f5dc.html)
- [Federal Reserve Committee and Shared-Operations Constitution](../sources/federal-reserve-committee-and-shared-operations-constitution-refr-9d9e4336cfde.html)
- [Federal Reserve Appointment, Removal and Succession Chain](../sources/federal-reserve-appointment-removal-and-succession-chain-2026-09--c657d00873e0.html)
- [Federal Reserve Safe and Efficient Payment-System Mandate Map](../sources/federal-reserve-safe-efficient-payment-system-mandate-map-2026-09-31fbecce7acd.html)
- [Twelve Reserve Banks Whole-Site Recertification](../sources/twelve-reserve-banks-whole-site-recertification-2026-09-08-85ce18d82e99.html)
- [Federal Reserve Payment Stack Control, Finality and Cost Audit](../sources/fed-payment-stack-control-finality-and-cost-audit-2026-07-25-42694c28bdc5.html)
- [Richmond National IT Governance and Control RACI](../sources/richmond-national-it-governance-and-control-raci-2026-08-15-c1fc308bb01b.html)
- Twelve-Bank / FRFS Operating Constitution and RACI
- Public-Only FRFS / National IT / Finance / Technology Layer Sweep

## Wave 6 ruling

The Federal Reserve’s crisis structure is a **federated switchboard of bounded authorities**, not a unitary emergency executive. Congress reserved bank resolution to the FDIC/chartering structure, assigned lending conditions to the Board and Reserve Banks, required Treasury’s prior key for section 13(3), placed market policy with the FOMC, and left payment/cash/fiscal-agent continuity to service-specific operating constitutions. The System’s ability to move work across sites and Reserve Banks is real. So are the legal boundaries: booking, finality, solvency, policy and loss do not automatically follow the operator.
