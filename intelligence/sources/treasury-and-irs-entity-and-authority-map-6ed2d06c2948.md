> Source created: 2026-07-16 · Source updated: 2026-07-16

# Treasury and IRS — Entity and Authority Map

Updated: 2026-07-16  
Status: factual institutional map  
Rule: the legal actor, operating actor, data holder, payment rail and recipient of funds remain separate until an operative record joins them.

## 1. Legal stack

| Entity / office | Location | Authority or function | Current state | Boundary not to collapse |
|---|---|---|---|---|
| Congress | Legislative branch | enacts taxes, customs statutes, appropriations and reporting duties | active | proposals and sense-of-Congress language are not enacted authority |
| Department of the Treasury | Executive department | supervises federal finance and, under 26 U.S.C. §7801, administration/enforcement of the Internal Revenue Code | active | Treasury is not identical to IRS or Fiscal Service |
| Treasury Secretary | Head of Treasury | statutory supervisory authority; retains functions of vacant Commissioner office under current vacancy posture | active | political head is not automatically the statutory Commissioner |
| Commissioner of Internal Revenue | IRS / Treasury | presidentially appointed, Senate-confirmed five-year office under 26 U.S.C. §7803; administers, manages, directs and supervises internal-revenue-law execution | **vacant** | do not label the CEO or Secretary as Commissioner |
| IRS Chief Executive Officer | IRS operational layer | newly created IRS position managing day-to-day operations under Treasury's announced structure; Frank J. Bisignano is separately Senate-confirmed as SSA Commissioner | active | Bisignano was not appointed to the Senate-confirmed §7803 IRS Commissioner office; operational/delegated authority is not §7803 appointment |
| IRS Chief Counsel | IRS / Treasury legal office | statutory tax-law counsel and litigation coordination functions | **vacant on current chart** | Chief Counsel's legal role is distinct from IRS operations and DOJ litigation |
| IRS Independent Office of Appeals | IRS | independent administrative tax-dispute resolution | active | an administrative appeal is not a federal-court judgment |
| National Taxpayer Advocate | IRS | taxpayer assistance and systemic advocacy under Title 26 | active | advocacy/reporting does not itself change tax liability |
| IRS Criminal Investigation | inside IRS | criminal investigation of Internal Revenue Code offenses and related financial crimes | active | IRS-CI is not a separate Treasury bureau and is not the same as civil examination |
| TIGTA | inside Treasury, outside IRS | independent audit, investigation and oversight of IRS/tax administration; reports to Secretary and Congress | active | TIGTA findings are oversight findings, not IRS operating orders |
| Bureau of the Fiscal Service | Treasury bureau | governmentwide collections, disbursements, EFTPS and financial-agent/payment infrastructure | active | Fiscal Service moves government money; it does not assess income tax |
| U.S. Customs and Border Protection | DHS bureau | entry administration and collection of customs duties; collects some IRS-set import excise taxes | active | CBP is not Treasury and is not ERS |
| Immigration and Customs Enforcement | DHS bureau | immigration and customs enforcement; recipient/requester in the 2025 §6103 data arrangement | active, data use constrained | data receipt is not revenue collection |
| External Revenue Service | proposed concept | proposed centralized tariff/duty/foreign-trade revenue body or system | **proposed / not established** | no founded date, charter, appropriation, staff or operative transfer established |
| Private collection agencies | Treasury/IRS contractors | contact and payment-arrangement assistance for assigned inactive receivables | active, bounded | cannot levy, lien, compromise or receive payments directly |
| Free File providers | private tax-software participants | return-preparation/filing interfaces under public-private program | active | software interface does not assess tax or hold sovereign collection power |
| Zero Paper contractors | private contractors | receive, scan, extract and transmit selected paper return/correspondence data | operating with readiness limits | document intake is not adjudication of liability |
| Remittance-transfer providers | private financial intermediaries | collect, deposit and report the §4475 remittance-transfer excise tax | statutory collection duty effective; proposed regulations pending; actual receipt state not independently evidenced | provider is collection agent and can become liable; sender is normally taxpayer |
| Custodial digital-asset brokers | private intermediaries | report covered digital-asset dispositions on Form 1099-DA; some basis/withholding duties phase in | operational / phased | information reporting is not tax determination; noncustodial DeFi rule was revoked |
| Banks / ACH / Fedwire / card processors | public-private payment rail | execute tax payments and refunds through Treasury/Fiscal Service systems | active | settlement node does not determine taxpayer liability |

Primary legal sources: [26 U.S.C. §7801](https://uscode.house.gov/view.xhtml?edition=2010&num=0&req=granuleid%3AUSC-2010-title26-section7801) · [26 U.S.C. §7803](https://uscode.house.gov/view.xhtml?edition=prelim&f=treesort&num=0&req=%28%28title%3A%2826%29+AND+section%3A%287803%29%29%29) · [current IRS organization](https://www.irs.gov/about-irs/irs-organization) · [IRS vacancy update](https://www.irs.gov/newsroom/update-on-irs-commissioner-position) · [TIGTA authority](https://www.tigta.gov/about-tigta)

## 2. Current IRS control geometry

The current organization chart places a vacant Commissioner office above a divided operating structure:

```text
Treasury Secretary
├── vacant statutory Commissioner functions / supervision
└── IRS CEO — day-to-day management
    ├── Taxpayer Services
    ├── Chief Tax Compliance Officer
    ├── Criminal Investigation
    ├── Chief Financial Officer
    ├── Chief Information Officer
    ├── Human Capital
    ├── Data and Analytics
    ├── Risk and Control
    └── other operating functions

Commissioner-side offices on the chart
├── Chief Counsel — vacant
├── Appeals
├── National Taxpayer Advocate
└── Chief of Staff
```

The chart is an operating map, not by itself the complete delegation record. The missing operative object is the current written delegation chain for the CEO.

## 3. Revenue and payment chains

### Internal income / payroll revenue

```text
Congressional tax law
  → taxpayer / employer / withholding agent
  → return and third-party information reporting
  → IRS assessment and taxpayer account
  → taxpayer, bank, payroll provider or processor
  → Fiscal Service / Federal Reserve payment rail
  → Treasury General Account or designated trust fund
```

### Customs revenue

```text
tariff statute / delegated trade authority
  → import transaction
  → importer of record and customs broker
  → CBP assessment and collection
  → Treasury settlement and receipt accounting
```

The proposed ERS does not currently sit in this chain.

### Remittance-transfer excise tax

```text
domestic sender
  → cash-like funding of U.S.-to-foreign transfer
  → private remittance provider collects 1%
  → semimonthly deposit + quarterly Form 720
  → IRS account / Treasury receipt rail
```

### Refund chain

```text
return / amended return / credit claim
  → IRS validates and authorizes refund
  → Fiscal Service disburses
  → ACH, prepaid account, other electronic option or permitted exception
  → taxpayer
```

Do not merge the receipt chain and the refund chain. A paperless-payment policy changes execution, not the underlying entitlement.

## 4. Tax-data chain

```text
taxpayer + third-party reporters
  → IRS return information / FTI
  → statutory disclosure authority, consent or contract
  → federal/state agency or private contractor
  → recipient safeguard, matching and use controls
```

The controlling questions are:

1. Which subsection of 26 U.S.C. §6103 authorizes disclosure?
2. Is the request facially valid and is the actual data transfer compliant?
3. What exact fields moved?
4. Who received, matched, stored and acted on them?
5. What safeguard findings or court orders constrain use?

The 2025 IRS–ICE event moved 47,289 address records corresponding to about 46,965 people. TIGTA reported matching defects, incomplete safeguard remediation and that IRS said DHS/ICE would not inspect, use, copy, distribute, rely on or act upon the transferred data pending litigation. That is an attributed IRS representation through TIGTA's review period, not independent proof of the recipient's behavior or a live July 2026 use state. The event did not transfer a tax account or create an immigration tax.

## 5. Required clocks

1. **Tax-law clock** — introduced → enacted → effective → amended/repealed.
2. **Organization clock** — office created → appointment/confirmation → delegation → vacancy → succession.
3. **Assessment clock** — return/info report → examination → assessment → administrative review → final liability.
4. **Collection clock** — notice → payment arrangement → lien/levy → collection suspension/expiration.
5. **Payment clock** — instruction → processor/bank acceptance → settlement → Treasury posting.
6. **Refund clock** — claim → validation → authorization → Fiscal Service disbursement → receipt/offset.
7. **Data clock** — request → legal review → transfer → match → use → correction/deletion/litigation.
8. **Capacity clock** — appropriation → hiring/departure → contract → readiness → production performance.
9. **Tariff clock** — legal authority → proclamation → entry date → collection → court decision → termination → refund.

## 6. Promotion rules

- A proposed entity becomes established only with competent legal creation plus an operative organization/authority record.
- An appointment does not prove every delegation attributed to the office.
- A collected receipt does not prove who bore the economic cost.
- A private reporting or processing duty does not transfer sovereign assessment power.
- A data-sharing agreement does not prove every requested record was disclosed or lawfully used.
- A contractor award does not prove production readiness or confidentiality compliance.
- A court decision ending tariff authority starts separate termination and refund clocks; it does not erase past collections automatically.
