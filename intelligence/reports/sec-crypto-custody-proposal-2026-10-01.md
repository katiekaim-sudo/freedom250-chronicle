# SEC Adviser and Regulated Fund Crypto Custody Proposal — October 1, 2026

<!-- plain-english-entry:start -->
## In plain English

**Question:** What would the SEC's October 1, 2026 crypto-custody proposal for advisers and funds actually require, cost and leave unresolved?

**Answer:** Holding any piece of a private key would count as custody; the SEC puts the cost at $433.7 million a year and the measurable benefit at $176,472.

**Evidence checked through:** 2026-10-01T17:35:03-04:00

The detailed record below keeps the legal wording, source limits and open questions.
<!-- plain-english-entry:end -->

## Controlling finding

The SEC did **not** adopt operative crypto-custody rules on October 1. It issued a 760-page **proposal**: File No. **S7-2026-35**, Release Nos. **IA-7023 / IC-36353**, RIN **3235-AN46**. The proposal would create two conditional crypto-custody routes for registered investment advisers and regulated funds, modernize the surrounding custody rules, permit qualifying regulatory records to be maintained onchain, and add public reporting. The comment period will run for 60 days after Federal Register publication; at this cutoff the release still contains publication-date placeholders and no Federal Register publication, final rule, effective date, compliance date, or first-use receipt exists.

The proposal fits the Observatory's existing architecture unusually well because it regulates custody as a layered control system:

> asset and account scope → legal actor → key possession → permitted route → segregation → authorization → cybersecurity → independent attestation → client and regulatory record → Article 8 property status → board and Commission oversight → loss and remedy.

It does **not** collapse those layers into “the blockchain.” It explicitly permits an onchain record only when the record remains true, accurate, current, retained, examiner-accessible, human-readable, and supplemented offchain when ownership or client metadata is missing (pp. 347–353).

## Research question

What would the Commission's proposal actually authorize, require, disclose, and leave unresolved for adviser and regulated-fund crypto custody—and how does that change the Crypto Infrastructure Hub's custody, record, insolvency, audit, trading, and DeFi questions?

## Scope and exclusions

Included:

- the full Commission proposing release, including proposed rule text, economic analysis, Paperwork Reduction Act analysis, forms, and 342 numbered comment questions;
- the October 1 SEC press release and statements by Chair Atkins and Commissioners Peirce and Uyeda;
- exact joins to the Hub's Legal process room.

Excluded unless separately proved:

- any claim that the proposal is final, effective, or currently usable;
- custody of every crypto asset in every account;
- broker-dealer, exchange, clearing, transfer-agent, banking, commodities, or payment authority not actually supplied by this proposal;
- a finding that any named adviser, fund, custodian, State trust company, wallet, network, or DeFi protocol qualifies;
- a finding that onchain confirmation establishes legal title, settlement finality, client ownership, or accounting completeness.

## The four clocks

| Object | State at cutoff | What would move it |
|---|---|---|
| Commission proposal | Issued October 1, 2026 | Federal Register publication opens the 60-day comment clock. |
| Final rule | Not issued | Commission adoption after the comment record and any revision. |
| Effective/compliance dates | Not established | Final release and Federal Register publication. |
| Actual use | None under the proposed routes | A final operative rule plus asset-, adviser-, fund-, custodian-, board-, contract-, control-, and record-specific compliance. |

The existing 2025 State Trust Company staff no-action letter remains a separate, nonbinding staff position. The proposal says a final rule could supersede or lead staff to withdraw it (pp. 397–398). The Commission withdrew its 2023 Safeguarding Advisory Client Assets proposal in June 2025; the October 1 proposal is a different rulemaking object.

## Who and what are covered

The crypto-specific provisions are narrower than the phrase “crypto custody rules” suggests (pp. 25–38):

- For an ordinary advisory client, the Advisers Act custody rule would apply only to a crypto asset that is a **fund or security**.
- For the account of a regulated fund, the Advisers Act route would extend to a crypto asset that is a **security or similar investment**.
- The Investment Company Act routes would apply to regulated-fund crypto assets that are **securities or similar investments**.
- Bitcoin, ether, solana, or another crypto asset does not enter the ordinary-client custody rule merely because it is crypto. Account type and legal classification still matter.
- Advisers may give non-discretionary advice concerning an asset outside custody scope when the client—not the adviser—makes and maintains the investment.

The proposal would redesignate Advisers Act rule 206(4)-2 as rule 223-1, add adviser self-custody rule 223-1(b)(7), add regulated-fund State trust company rule 17f-8, and add regulated-fund self-custody rule 17f-9.

## Route 1 — adviser self-custody is a residual lane

The proposal defines adviser self-custody by **actual possession of any portion of the key materials**, not merely by contractual authority. Possession of one key share can be enough. If a qualified custodian or qualified-custodian related person possesses all key materials, the qualified-custodian route applies instead (pp. 39–79).

An adviser could self-custody a client's covered crypto asset only if all core conditions are met:

1. **No qualified custodian will maintain that particular asset.** Before taking custody, the adviser must make a written reasonable-basis determination after due inquiry. Cost cannot support the finding (pp. 80–88).
2. **The market must be re-tested.** The written determination must be reassessed no less frequently than quarterly. If a qualified custodian becomes available, the adviser must transfer the asset as soon as reasonably practicable (pp. 80–88).
3. **Advice and custody stay joined.** The route is limited to crypto assets for which the adviser provides investment advice.
4. **Designated people control the keys.** Only supervised persons designated by the adviser may possess key materials; a regulated-fund board designates the persons by resolution (pp. 89–120, 166–178).
5. **No single-person control.** Systems must require joint authorization by at least two designated people, including at least one management person; for a regulated fund that person must also be a fund officer. The release says a single-employee adviser could not use this route. Multisignature or multiparty computation can be used, but is not mandated.
6. **One client, one address perimeter.** Each client's assets must be maintained in one or more addresses containing only that client's crypto assets. Adviser self-custody does not permit an omnibus address (pp. 89–120).
7. **Outside technology cannot become outside custody.** Third-party cybersecurity or wallet software can support the system only if the provider cannot access key materials or unilaterally move the assets. The adviser remains responsible.
8. **Crypto-asset-specific expertise and controls.** The adviser must document a reasonable basis for believing it has the safeguarding expertise and systems appropriate to each asset (pp. 89–120).
9. **Cybersecurity is a custody control.** Written risk assessments must occur before custody and periodically, at least annually, with earlier updates for material changes. Systems must address prevention, detection, mitigation, remediation, incident response, and recovery (pp. 121–130).
10. **Annual control review.** The adviser must review safeguarding and cybersecurity effectiveness in writing at least annually (pp. 131–133).
11. **Independent controls attestation.** An independent public accountant must issue an internal control report within six months after self-custody begins and at least annually while the adviser retains the assets. A SOC 1 Type 2 can qualify; a Type 1 cannot. The report must include reconciliation to the crypto network (pp. 134–145).
12. **Client-facing record.** At least quarterly, the adviser must provide a statement or qualifying human-readable electronic transmission showing the address, network, period-end balances, and transactions, with a prompt to compare the information to the network. Privacy assets need supplemental accessible information. Pooled vehicles may use the audit route; regulated funds are excepted because of their audited reporting (pp. 146–158).
13. **Article 8 election.** The adviser and client must agree in writing that every self-custodied asset is a “financial asset” and that the adviser acts as a “securities intermediary” under the governing State law. The proposal uses this to create a securities-entitlement/property-interest frame and improve priority against the adviser's general creditors; it does not create FDIC or SIPC protection (pp. 159–165).
14. **Distributed assets are not ignored.** An airdrop or similar distributed asset would not create an immediate violation if the adviser complies with the self-custody rule or moves it to a permitted custodian as soon as reasonably practicable.

This is not “self-custody whenever it is better, cheaper, or preferred.” It is an asset-specific exception conditioned on the **absence** of a qualified custodian and designed to end when that absence ends.

## Route 2 — State trust companies become a conditional custodian class

Proposed rules 223-1(d)(13)(v) and 17f-8 would recognize a State trust company as a permitted custodian for covered crypto assets and related cash or cash equivalents (pp. 179–202). The company must be a State-law entity supervised and examined by a State banking authority and authorized to exercise fiduciary powers.

Before use and annually thereafter, the adviser or regulated fund would need a written reasonable basis after due inquiry that the company:

- is authorized by the relevant State banking authority to provide crypto custody;
- maintains and implements written policies and procedures reasonably designed to protect the assets from theft, loss, misuse, and misappropriation;
- supplies U.S. GAAP audited financial statements;
- supplies an internal control report with an independent accountant's operating-effectiveness opinion; and
- segregates customer assets from its proprietary assets.

A regulated fund would also need a written custodial-services agreement. This is **not** blanket federal approval of every State trust company. Qualification remains company-, State-, asset-, contract-, report-, and date-specific. Capital, insurance, collateral, indemnity, rehypothecation, and Federal minimum-standard questions are mostly left to the comment record rather than resolved in the proposed text.

## Regulated-fund overlay

A regulated fund may use adviser self-custody only with board oversight (pp. 166–178):

- before custody and at least quarterly, the board, including a majority of independent directors, reviews the adviser's no-qualified-custodian determination;
- initially and at least annually, the board determines that the adviser is using reasonable care;
- the board receives the adviser's expertise/system basis, annual reviews, and independent internal control reports; and
- loss, theft, misuse, misappropriation, significant cyber events, or modified/adverse internal-control opinions trigger board notice.

The proposal also modernizes Investment Company Act custody rules by expressly including business development companies, allowing all SEC-registered broker-dealers subject to rule 15c3-3 customer-protection requirements to act as regulated-fund custodians rather than only exchange members, and rescinding the obsolete $500 free-cash-account rule 17f-3 (pp. 216–264).

## Onchain records become admissible—not self-proving

The proposed Advisers Act and Investment Company Act recordkeeping amendments would allow required records relating to crypto assets to be maintained on a crypto network (pp. 327–353). The permission has four gates:

1. the onchain record must contain a true, accurate, and current record of the required information;
2. the adviser or fund must retain access for the full required period;
3. the record must be produced promptly to the Commission in human-readable, reasonably usable electronic form—interpreted in this context as generally within 24 hours; and
4. offchain records must supplement the chain when beneficial ownership, client identity, contact data, authorization, metadata, or another required field is absent.

The proposal therefore recognizes onchain custody records without making a public address a complete customer ledger. This is a direct match to the Observatory's distinction between network event, authoritative record, beneficial owner, accounting book, and examiner-ready evidence.

For self-custody, proposed records include the qualified-custodian determination and quarterly rechecks; expertise basis; designated persons; cyber assessments; annual reviews; internal control reports; client statements or transmissions; Article 8 agreement; and enough data to reconstruct every position and transaction by client, account, address, amount, destination, authorization, and relevant metadata.

## DeFi and trading are not quietly authorized

The Commission proposes no special DeFi custody rule (pp. 203–211). If participation requires a covered asset to leave a permitted custodian or compliant self-custody arrangement, the existing custody constraint remains. The release asks about staking, control and ownership, receipt/claim tokens, protocol due diligence, insurance, indemnification, collateral, and recourse. Questions are not permissions.

The Commission also declined to propose a general trading-platform custody exception (pp. 212–215, 628–630). It asks about a possible construct allowing covered assets to remain on a non-custodian crypto trading platform for limited periods, including 24 hours and subject to controls, but adopts no such route in the proposed text. Cold storage, affiliated permitted custodians, omnibus structures at qualified custodians, smart-contract execution, or separate permitted counterparties remain possible only under their own facts and law.

## Disclosure, reporting, and examiner visibility

The proposal would expand Form ADV and Form N-CEN (pp. 362–396):

- Form ADV would identify whether the adviser uses self-custody, approximate value and client counts, total address counts, the internal-control accountant and opinion, statement method, and private-fund or separately managed account use; Schedule D would ask tokenized private funds for applicable crypto-network names.
- Adviser risk disclosures would address loss, conflicts, cybersecurity, DeFi, recourse, bankruptcy, and insurance.
- Form N-CEN would add self-custody, State trust company, and tokenized-fund reporting.
- The proposal does not currently require a standalone SEC loss report, but asks whether one should be added.

Public address-count and network-name reporting, combined with other public filings and possible future fields, creates its own physical, cyber, privacy, and targeting questions. The proposed Item 9.F asks for a total address count, not every address string. The release asks about those risks; asking does not solve them.

## Scale and economic model

The Commission estimates, for burden analysis rather than as observed adoption, approximately:

- 823 advisers (5% of 16,442) might use adviser self-custody;
- 1,645 advisers (10%) might use State trust companies;
- 715 regulated funds (5% of 14,301) might use fund self-custody; and
- about 19 State trust companies specialized in crypto custody as of its May 2026 review.

The release identifies 10 crypto mutual funds, 122 crypto ETFs, and 72 crypto ETPs as of April 20, 2026, while emphasizing that many products obtain indirect exposure and do not necessarily hold crypto directly.

Its monetized tables estimate $301.9 million in aggregate initial costs and $433.7 million in aggregate annual costs, with annualized costs of roughly $468.6–$475.3 million over ten years. Only $176,472 of administrative benefits are monetized; many claimed investor-choice, competition, protection, and capital-formation benefits are qualitative. The dollar comparison is therefore a comment-record design issue, not a complete measure of total costs and benefits (pp. 593–601).

## The Observatory read

The proposal is best understood as a **custody constitution**, not a crypto approval:

- **Private key → possession:** even a key share can establish custody.
- **Possession → authority:** designated-person and joint-authorization rules allocate human control.
- **Authority → record:** address-level positions and transactions must be reconstructable and client-visible.
- **Record → legal relationship:** Article 8 financial-asset and securities-intermediary elections create a property and insolvency frame.
- **Record → assurance:** SOC 1 Type 2-style operating-effectiveness evidence must reconcile the custodian's books to the network.
- **Record → supervision:** a chain record is acceptable only if it can be retained, completed, translated, and produced to examiners.
- **Custody route → market clock:** self-custody exists only while no qualified custodian will take the asset.

What remains separate: asset classification, investment advice, custody, execution, exchange permission, settlement asset, finality, staking economics, DeFi control, client ownership, accounting recognition, insurance, bankruptcy remedy, and observed operation.

## Highest-value comment pressure points

1. Whether per-client addresses improve segregation enough to justify operational, privacy, fee, and recovery costs.
2. Whether any key share should trigger custody when multiparty computation, recovery, or client-held shares distribute practical control.
3. Whether the ban on client or third-party access to adviser-held key materials conflicts with resilient recovery design.
4. Whether quarterly qualified-custodian re-testing will force risky or costly asset migrations.
5. Whether “no custodian will maintain the asset” is the right gate, instead of a best-interest or capability comparison.
6. Whether the mandatory Article 8 entitlement frame fits clients who believe they hold an asset directly.
7. Whether removing the PCAOB registration/inspection condition from certain accountants is well paired with expanded crypto control reports.
8. Whether public Form ADV address-count and crypto-network reporting creates avoidable targeting and privacy risks or should use more structured, less identifying fields.
9. Whether State trust companies need federal floors for capital, insurance, rehypothecation, indemnity, loss reporting, and recovery.
10. Whether DeFi and trading need a real custody pathway rather than a request for information.
11. Whether onchain records should be acceptable for additional regulatory records beyond crypto assets.
12. Whether the cost model adequately captures key compromise, migration, audit concentration, and recurring client-address operation.

## Primary-source spine

- SEC proposing release, IA-7023 / IC-36353, File S7-2026-35, October 1, 2026.
- SEC press release 2026-100, October 1, 2026.
- Chair Paul S. Atkins, statement on the custody proposal, October 1, 2026.
- Commissioner Hester M. Peirce, “Roller Coaster Ride,” October 1, 2026.
- Commissioner Mark T. Uyeda, statement on proposed custody-rule amendments, October 1, 2026.

See `SEC_CRYPTO_CUSTODY_SOURCE_MANIFEST_2026-10-01.json` for exact URLs, boundaries, and the preserved PDF hash.
