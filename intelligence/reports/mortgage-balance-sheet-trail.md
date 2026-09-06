# One mortgage, several accounting layers

Research ID: `mortgage-balance-sheet-trail`. Accounting extension checked September 7, 2026, America/New_York. Read alongside the process and current Fed endpoint.

The organizing question is: **Which entity debits which asset, credits which liability or asset, and what survives at the next reporting level?** The entries below are constructed examples consistent with the cited reporting policies. They are not recovered internal journals or a traced household mortgage.

## The base case and accounting boundaries

Begin with an existing $300,000 mortgage funded by a nonbank originator. Its temporary funding is $294,000 warehouse borrowing plus $6,000 of its own funds. Follow a cash sale to Fannie, a consolidated trust, an outside investor, an optional repo and an optional Fed purchase. Everything is at par; the main sequence omits fees, interest, credit allowances, premiums, discounts, taxes and hedges. Separate examples add those layers below. The $300,000 represents a proportional slice of a larger MBS pool.

Debits increase assets and expenses; credits increase liabilities, equity and revenue. The opposite entry reduces those accounts. Every journal balances **within its own entity**. An asset on one party’s books often corresponds to a liability on another’s, but the assets and liabilities may have different measurement bases.

Keep four reporting boundaries distinct:

| Boundary | What belongs inside it | What can be eliminated |
|---|---|---|
| Individual legal entity | Its own recognized assets, obligations and income | Only qualifying offsets under its accounting rules |
| Fannie consolidated group | Fannie and trusts/subsidiaries it consolidates | Intra-group balances and transactions; not the homeowner or outside investor |
| Combined Reserve Banks | The twelve Reserve Banks and relevant consolidated entities | Reciprocal Reserve Bank positions; not commercial-bank deposits or GSE debt |
| Analyst-selected economic perimeter | Whichever parties the analyst explicitly chooses | Matched internal claims for that analytical presentation only |

A nationwide financial-claims map is not one company’s GAAP balance sheet. A contract, regulatory relationship or settlement account does not by itself put two parties in the same consolidated group. [Fannie Q2 2026, Note 3](https://www.fanniemae.com/media/document/pdf/q22026.pdf), [Fed Financial Accounting Manual, Chapter 4](https://www.federalreserve.gov/aboutthefed/chapter-4-system-open-market-account.htm)

## 1. The mortgage already exists

The opening positions of interest are:

| Books | Asset/claim | Liability or funding |
|---|---|---|
| Household | Home acquired; the mortgage-financed slice is $300,000 | Mortgage payable $300,000 |
| Nonbank originator | Mortgage loan $300,000 | Warehouse payable $294,000; own funds supporting the remaining $6,000 |
| Warehouse bank | Loan to originator $294,000 | The bank’s own funding is a separate layer |

These are selected positions, not full institutional balance sheets. The household’s home value and equity need not equal the amount borrowed.

The originator’s funding and closing entries can be reconstructed separately:

| Books / event | Debit | Credit |
|---|---|---|
| Originator draws warehouse line | Bank deposit $294,000 | Warehouse payable $294,000 |
| Warehouse bank credits originator’s account | Loan to originator $294,000 | Originator deposit liability $294,000 |
| Originator funds mortgage, using the draw and existing $6,000 | Mortgage loan $300,000 | Bank deposit $300,000 |
| Household, mortgage-financed portion of purchase | Home $300,000 | Mortgage payable $300,000 |

The last row is the financed slice of closing, not a second disbursement. The home seller receives the deposit proceeds and derecognizes the property sold. If payment crosses banks, settlement moves reserve assets between banks. A nonbank’s deposit is an asset; the bank records that deposit as a liability. Deposit creation at a bank and subsequent interbank settlement are distinct entries. [Bank of England explanation of lending and deposit mechanics](https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-creation-in-the-modern-economy), [Rocket 2025 funding and sale disclosures](https://www.sec.gov/Archives/edgar/data/1805284/000162828026013283/rkt-20251231.htm)

## 2. Sale to Fannie and repayment of warehouse funding

Assume a qualifying sale for $300,000 with no retained-servicing valuation in this base case.

| Books / event | Debit | Credit |
|---|---|---|
| Originator sells loan | Cash $300,000 | Mortgage loan $300,000 |
| Fannie buys loan | Mortgage loan $300,000 | Cash $300,000 |
| Originator repays warehouse line | Warehouse payable $294,000 | Cash $294,000 |
| Warehouse bank receives repayment | Settlement cash/reserves $294,000 | Loan to originator $294,000 |

If the originator pays from an account **at that warehouse bank**, the bank instead debits its originator-deposit liability and credits the loan asset. Do not also debit reserves for the same same-bank repayment. For different banks, the paying bank debits the originator deposit liability and credits reserves; the receiving warehouse bank uses the final row above.

The originator recovers its original $6,000 cash contribution and extinguishes its warehouse debt. At par, before costs, it has not made $300,000 or $6,000 of profit. Fannie has exchanged one asset for another. The household posts no entry merely because its creditor changes. Fannie’s cash-purchase route and lender-swap route are different executions. [Fannie execution options](https://selling-guide.fanniemae.com/sel/c1-1-01/execution-options)

## 3. Trust formation: legal movement versus consolidated result

For a simple legal-flow illustration, suppose Fannie conveys the mortgage into a trust and initially retains all certificates:

| View / books | Debit | Credit |
|---|---|---|
| Corporate transfer schematic | Certificate interest $300,000 | Mortgage loan $300,000 |
| Trust-administration schematic | Mortgage loan $300,000 | Certificateholders’ beneficial interests $300,000 |
| Consolidation workpaper, while internally held | Internally held certificate interests $300,000 | Corporate certificate asset $300,000 |

The first two rows illustrate the legal structure, **not an assertion about Fannie’s undisclosed standalone journals or standalone sale-accounting conclusion**. The neutral trust-side label is intentional: certificates legally represent beneficial interests. The verified external **debt** classification belongs to the consolidated financial reporting view. [Fannie trust-agreement explanation](https://capitalmarkets.fanniemae.com/mortgage-backed-securities/mbs-trust-agreements)

For the consolidated group, the internal formation has no net external cash, debt or equity effect in this example. One mortgage remains recognized. Fannie’s published policy carries consolidated portfolio securitizations at the existing basis, with no consolidation gain; loans intended for these securitizations are held for investment before and after. [Fannie 2025 Form 10-K, F-10 and F-12](https://www.fanniemae.com/media/56616/display)

Consolidation entries belong to a workpaper. They are not instructions to cancel the underlying contracts or to post the elimination into both parties’ legal books. Trust restrictions continue to apply.

## 4. External MBS issuance: cash comes back, debt remains

When an outside investor buys the certificates for $300,000:

| View / books | Debit | Credit |
|---|---|---|
| Corporate sale schematic | Cash $300,000 | Certificate interest $300,000 |
| Outside investor | MBS investment $300,000 | Cash $300,000 |
| Fannie consolidated economic entry | Cash $300,000 | Debt of consolidated trusts $300,000 |

The corporate and consolidated rows are **alternative reporting views of the same event**. Do not post both into one ledger. Rebuild consolidation from closing balances: after the external sale, there is no internally held certificate asset to eliminate against that external debt.

Relative to before Fannie purchased the mortgage, its consolidated position is now: cash unchanged, mortgage assets +$300,000, external trust debt +$300,000, and equity unchanged before the excluded items. The original mortgage still earns cash flows; issuance supplies funding against those flows. This is how cash can return while the loan stays on the consolidated balance sheet.

There are now two distinct principal claims: Fannie’s consolidated mortgage asset against the household, and the investor’s MBS asset corresponding to trust debt. Adding those two selected assets gives $600,000 of gross financial claims, not $600,000 of housing or household debt. Neither claim is fictitious merely because they are economically connected. [Fannie Q2 2026, consolidated balance sheet and Note 3](https://www.fanniemae.com/media/document/pdf/q22026.pdf)

### What “external trust debt supplies the funding” means

More precisely, **outside investors supply purchase cash; the consolidated trust-debt account records the corresponding external obligation**. “External” means outside Fannie’s consolidated reporting group. It does not mean foreign funding, a Fed loan, or a second warehouse line.

Follow an isolated teaching balance sheet with $300,000 opening cash funded entirely by $300,000 equity. This starting capitalization is invented solely to make the arithmetic visible, not a depiction of Fannie’s actual funding.

| Fannie consolidated teaching balance sheet | Before purchase | After buying mortgage | After selling MBS externally |
|---|---:|---:|---:|
| Cash | $300,000 | $0 | $300,000 |
| Mortgage loan | $0 | $300,000 | $300,000 |
| Total assets | $300,000 | $300,000 | $600,000 |
| External trust debt | $0 | $0 | $300,000 |
| Equity | $300,000 | $300,000 | $300,000 |

The restored cash is financed by the investor’s security purchase. It is not sale revenue or additional equity in this par-only example. If available cash then purchases another eligible mortgage, the group exchanges cash for another loan; it has not reset the first mortgage’s risk or erased its trust debt. Further issuance can recycle liquidity while expanding funded assets and corresponding obligations. Actual activity depends on market demand, pricing, eligibility, risk capacity and governing requirements.

The investor purchases a certificate carrying rights to pool cash flows under the trust documents, with Fannie’s guarantee. It does not buy Fannie common stock. Legally these are beneficial interests; consolidated reporting nevertheless presents outside-held securities as trust debt. [MBS prospectus](https://capitalmarkets.fanniemae.com/media/26506/display)

This is observable in the financial statements: Fannie defines trust debt as MBS from consolidated trusts held by third-party certificateholders, separately from corporate debt issued to fund operations. Its 2025 cash-flow statement reports $255,527,000,000 of proceeds from issuance of consolidated trust debt within financing activities. That is a cash-flow line, not the total face value of every MBS issued; noncash lender swaps must be distinguished. [2025 Form 10-K, consolidated balance-sheet analysis and statement of cash flows](https://www.fanniemae.com/media/56616/display)

This example concerns initial external placement of securities backed by already purchased loans. A later investor-to-investor resale sends money to the selling investor. In a lender swap, the originating lender receives MBS for delivered loans and may itself receive the outside buyer’s cash. Those executions must not be collapsed into a universal claim that Fannie receives cash on every MBS trade.

## 5. Trading and repo add different entries

A secondary-market sale at par replaces the investor:

| Books | Debit | Credit |
|---|---|---|
| Investor A, seller | Cash $300,000 | MBS $300,000 |
| Investor B, buyer | MBS $300,000 | Cash $300,000 |

No household entry; no new trust issuance entry solely because of this resale. Price differing from carrying value introduces seller gain/loss and a different buyer acquisition basis.

Now suppose B already owns the MBS and borrows $294,000 against it:

| Books | Debit | Credit |
|---|---|---|
| Investor B, cash borrower | Cash $294,000 | Repo payable $294,000 |
| Repo counterparty, cash lender | Reverse-repo receivable $294,000 | Cash $294,000 |

Under secured-financing treatment B keeps the MBS asset; the cash lender recognizes a financing receivable, not an additional owned MBS asset. The illustrative 2% haircut is a financing gap, not a fee or newly created equity. The legal repo can be documented as sale and repurchase while meeting financing-accounting conditions. [FFIEC instructions, glossary A-86–88](https://www.ffiec.gov/sites/default/files/data/reporting-forms/FFIEC051_202503_i.pdf), [SIFMA Master Repurchase Agreement, paragraphs 5–7](https://www.sifma.org/wp-content/uploads/2024/06/Master_Repurchase_Agreement_MRA.pdf)

Selected principal claims are now $300,000 mortgage + $300,000 MBS + $294,000 repo receivable = **$894,000 gross**. Their matched obligations reside at the household, trust and investor respectively. This excludes deposits and all other accounts; it is not a total-system asset measure.

An analyst combining investor and repo lender can eliminate their matched $294,000 financing claim and payable for that chosen analytical perimeter. Two independent firms cannot make that elimination in their separate published statements merely because the positions match. Real repayment deadlines, collateral rights and margin risk persist. AGNC’s filing demonstrates MBS assets and repo financing alongside each other. [AGNC Q2 2026, Note 2](https://www.sec.gov/Archives/edgar/data/1423689/000142368926000128/agnc-20260630.htm)

## 6. An outright Fed purchase adds the reserve/deposit layer

Take the unencumbered MBS branch, or first repay the repo and release collateral. Compress dealer intermediation and assume a $300,000 par purchase from a nonbank seller:

| Books | Debit | Credit |
|---|---|---|
| Nonbank seller | Bank-deposit asset $300,000 | MBS asset $300,000 |
| Seller’s commercial bank | Reserve asset $300,000 | Seller deposit liability $300,000 |
| Combined Reserve Banks | MBS asset $300,000 | Bank reserve-deposit liability $300,000 |

Two money layers are visible: the seller owns a claim on its bank; that bank owns a claim on the Fed. The Fed owns the MBS, whose cash flows trace through the trust to mortgages. The seller’s MBS asset has been replaced, not left behind as another holding. [The Fed Explained, securities purchases and reserves](https://www.federalreserve.gov/aboutthefed/files/the-fed-explained.pdf)

The selected chain now contains:

**Household mortgage payable ↔ consolidated trust mortgage asset; trust debt ↔ Fed MBS asset; Fed reserve liability ↔ bank reserve asset; bank deposit liability ↔ seller deposit asset.**

That is $1,200,000 of selected gross financial claims in this par example. It is four connected $300,000 contracts/positions, not a fourfold increase in the household’s borrowing. This selected-claims sum is not a money multiplier or a full financial-system balance sheet; deposits and reserves are fungible and cannot remain permanently earmarked to this mortgage. If an analyst includes every corresponding debtor and creditor at matching values, the financial claims net internally. That exercise does not erase the home, institutional risks or legal contracts, and it is not permission for any participant to net external assets and liabilities in its GAAP statements.

Within the Fed itself, each Reserve Bank has an undivided SOMA participation. For an illustrative $30,000 allocation from New York to another Reserve Bank, New York debits ISA and credits MBS; the other Bank debits MBS and credits ISA. Reciprocal Interdistrict Settlement Account positions eliminate in the combined view. A borrower’s location does not assign that particular mortgage to its regional Reserve Bank. [FAM Chapter 4, section 40.70](https://www.federalreserve.gov/aboutthefed/chapter-4-system-open-market-account.htm)

## 7. Follow $500 of principal back down the claims

This isolated principal-payment example excludes interest and fees. It assumes a proportionate pass-through to a Fed-owned interest, with no timing advances. Commercial-bank routing to the issuer’s Fed account is compressed; issuer/trust deposit labels below describe a combined issuer/trust cash-flow schematic, not an asserted proprietary account title.

| Books / event | Debit | Credit |
|---|---|---|
| Household pays principal | Mortgage payable $500 | Bank deposit $500 |
| Fannie/trust collects | Cash/deposit $500 | Mortgage loan $500 |
| Paying bank settles onward | Customer deposit liability $500 | Reserves $500 |
| Fed receives issuer prefunding | Bank reserve liability $500 | Issuer deposit liability $500 |
| Fannie/trust distributes principal | Trust debt $500 | Cash/deposit $500 |
| Fed receives its distribution | Issuer deposit liability $500 | MBS principal asset $500 |

The household mortgage, consolidated mortgage asset, trust debt and Fed-held MBS principal each fall from $300,000 to $299,500 in this simplified matched slice. The bank loses reserve assets and deposit liabilities. **Reserve reduction can precede MBS reduction:** the issuer may accumulate funds before distribution. [New York Fed’s staged MBS balance-sheet example](https://libertystreeteconomics.newyorkfed.org/2017/07/how-the-fed-changes-the-size-of-its-balance-sheet-the-case-of-mortgage-backed-securities/)

The current July 29, 2026 instruction reinvests agency principal into Treasury bills. For an illustrative secondary-market bill purchase costing $500, face value $501: Fed **Dr Treasury bills $501 / Cr unamortized discount $1 / Cr bank reserves $500**. The initial net bill asset is $500. This replaces the paid-down MBS exposure with a Treasury exposure; it does not pay the household again. [Current implementation instruction](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a1.htm), [FAM Chapter 1, section 2.90](https://www.federalreserve.gov/aboutthefed/chapter-1-balance-sheet.htm)

## 8. Income, retained rights and valuation sit beside principal

These are separate examples; do not add them to the par-only chain without adjusting its assumptions.

| Layer | Illustrative entry | What it measures |
|---|---|---|
| Retained servicing on qualifying sale | Originator Dr cash $300,000; Dr MSR $3,000; Cr loan $300,000; Cr sale gain $3,000 | A valued service right and gain under assumed consideration/basis; not another mortgage principal claim |
| Mortgage interest accrual | Loan holder Dr interest receivable; Cr interest income | Earnings before cash collection |
| Trust debt interest accrual | Consolidated issuer Dr interest expense; Cr interest payable | Cost of funding the mortgage pool |
| Investor coupon accrual | Investor Dr interest receivable; Cr interest income | Earnings on the security, distinct from its principal |
| Repo interest accrual | Borrower Dr interest expense; Cr interest payable; lender mirrors receivable/income | Cost and return on institutional leverage |
| Credit allowance, where the allowance model applies | Loan holder Dr credit-loss expense; Cr allowance | Reduction of net loan carrying value, not borrower forgiveness; fair-value/HFS accounting can differ |
| Charge-off using allowance | Loan holder Dr allowance; Cr loan | Removes recognized gross receivable against the reserve; discharge is a separate legal question |
| Security purchased above par | Buyer Dr MBS principal $300,000; Dr premium $6,000; Cr cash $306,000 | Purchase basis differs from homeowner principal |
| Derivative fair-value gain | Dr derivative asset; Cr gain, subject to applicable hedge accounting | Market value of a separate contract; not its reference notional |

The MSR figures are invented to show arithmetic, not a market quotation. Actual retained-right, consideration and loan-basis allocation must be measured together. Rocket explains its MSR fair-value recognition and subsequent accounting. [Rocket 2025 Form 10-K, MSR accounting](https://www.sec.gov/Archives/edgar/data/1805284/000162828026013283/rkt-20251231.htm)

Fannie’s consolidation presents the mortgage interest and related MBS interest expense through net interest income; legal guaranty-fee economics therefore need not appear as a simple standalone fee-revenue line. Do not automatically add another $300,000 guarantee liability on top of $300,000 consolidated trust debt. Separate unconsolidated guarantees follow their applicable policy. [Fannie 2025 Form 10-K, financial guarantees](https://www.fanniemae.com/media/56616/display)

Fed MBS interest is accrued before receipt: debit interest receivable, credit interest income. Collection then credits that receivable, not a second income entry. Premium amortization and paydown adjustments mean principal face value, carrying value and market value can diverge. [FAM Chapter 4, section 40.13](https://www.federalreserve.gov/aboutthefed/chapter-4-system-open-market-account.htm)

Treasury remittance is further downstream: remittable **net earnings**, after applicable costs and deferred-asset treatment, create a remittance obligation. They are not an immediate transfer of each homeowner’s interest dollar. FAM specifies an expense/payable accrual for earnings remittances. [FAM Chapter 1, sections 11.96 and 12.60](https://www.federalreserve.gov/aboutthefed/chapter-1-balance-sheet.htm)

## What this changes in our research

The original process map now has an accounting companion that distinguishes the same asset changing hands, a new security financing retained assets, new institutional borrowing, money creation at settlement, income recognition and consolidation eliminations.

The next empirical step is to attach actual balances, basis, fees and dates to a selected security/pool. Published accounting policies establish how these layers work; they do not disclose every internal journal, servicing ledger, consolidated workpaper or borrower-to-CUSIP link. Those remain evidence gaps. Credit-scoring reform affects the entrance to this structure; its measured effects still require production and performance data.
