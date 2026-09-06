# Visible Ledger, Hidden Constitution — Object Matrix

## Audience rule

Record transparency separately for:

- `USER`: payer or payee;
- `OPERATOR`: bank, network, processor, issuer, VASP or custodian;
- `AUTHORITY`: regulator, central bank, tax or law-enforcement body; and
- `PUBLIC`: anyone without privileged access.

## Comparative matrix

| Instrument | What moves / is presented | USER sees | OPERATOR sees | AUTHORITY sees | PUBLIC sees | Hidden constitution |
|---|---|---|---|---|---|---|
| physical cash | sovereign bearer note | note, amount, possession | cash handler sees deposit/withdrawal, not full history | aggregate issuance/distribution plus reported cash events | issuer, design and aggregate supply | distribution, handling cost, source of funds and transaction history |
| paper check | signed order against deposit | names, amount, date, bank; later account record | account, image/data, collection and return status | bank records under legal process/reporting | nothing transaction-specific | provisional credit, return risk, interbank settlement |
| Check 21 image/substitute | authoritative electronic image/data representation | image or substitute check and statement | image exchange and collection data | bank/clearing records | nothing transaction-specific | same bank settlement and return path beneath electronic representation |
| credit/debit card | network credential and authorization message | approval, receipt, statement | issuer/acquirer/network/processor each see structured fields | supervised entity records and lawful access | almost nothing | rulebooks, interchange, netting, fraud models, settlement banks, chargebacks |
| Apple Pay card payment | device token plus cryptogram | device confirmation and Wallet record | issuer/network/processor map token and authorize; Apple has bounded platform data | records obtainable from relevant entities under law | nothing transaction-specific | underlying card account, token vault, network routing and card settlement |
| public-chain stablecoin | issuer claim represented by ledger token | wallet balance, transaction hash, chain status | issuer/VASP/custodian sees customer and platform data | can combine regulated records with chain analytics subject to law/access | addresses, transfers, contracts and some supply/admin events | identity, reserves, banks, direct-redemption eligibility, omnibus ownership, off-chain fees and remedies |
| permissioned deposit token | bank deposit claim on controlled ledger | wallet/account record | bank and platform see full controlled state | central bank/regulator can receive designated data | little or none | operator access, bank balance sheet, central-bank settlement and pilot rules |

## The money-object test

| Instrument | Holder's claim | Immediate settlement object | Later settlement / conversion | Principal failure path |
|---|---|---|---|---|
| cash | direct holder of central-bank note | the note | bank redeposit optional | loss, theft, counterfeit |
| check | claim remains on drawer's bank account until paid | instruction | bank collection and settlement | return, fraud, insufficient funds |
| card credit | contractual credit/account relationship with issuer | authorization, not final payment | network obligations, merchant payout, cardholder repayment | fraud, credit loss, reversal, processor/acquirer failure |
| Apple Pay card | same underlying issuer relationship | tokenized authorization | same card clearing and settlement | device/account compromise plus inherited card failures |
| USDC | conditional redemption right under issuer terms; direct redemption eligibility varies | chain token transfer | issuer redemption or secondary-market sale; bank payout | depeg, reserve/bank/issuer/access failure, wrong transfer |
| JPYSC | specified trust-beneficiary claim | account-ledger transfer | redemption under trust/distributor terms | issuer/trust/operational or access failure |
| Hangang token | participating-bank deposit | permissioned token transfer | participating bank and BOK pilot settlement structure | bank/platform/pilot failure under deposit and system rules |

## Fee visibility

| Layer | Typical public visibility |
|---|---|
| cash handling | usually embedded in merchant/bank operations |
| check account and return fees | disclosed by bank to customer; not public transaction data |
| card interchange/network/processor/acquirer economics | partially public at category/rule level; transaction allocation and contracts often private |
| Apple Pay platform economics | underlying card fees persist; commercial platform terms are not a public transaction field |
| blockchain network fee | visible on-chain for the transaction |
| stablecoin exchange spread | visible only by reconstructing matched quotes/order execution |
| issuer mint/redemption fee | terms or account schedule; eligibility-dependent |
| bank wire/FX/off-ramp fee | off-chain, account/corridor-specific |

The visible gas fee is not the total cost of moving usable money from sender's
bank account to recipient's bank account.

## Finality and remedy firewall

| Event | Do not confuse with |
|---|---|
| cash received | proof of lawful source or recoverability |
| check deposited | check finally paid |
| card authorized | merchant finally settled |
| merchant paid | cardholder debt finally collected |
| Apple Pay authenticated | new settlement rail |
| stablecoin transaction confirmed | fiat redemption completed |
| token burned | recipient bank credited |
| public address observed | beneficial owner identified |
| issuer attestation published | full financial-statement audit or real-time reserve control |
