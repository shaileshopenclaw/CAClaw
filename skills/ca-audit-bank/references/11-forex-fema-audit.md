# FOREX, FEMA & TRADE FINANCE AUDIT — COMPLETE GUIDE
## ICAI Guidance Note on Audit of Banks (2025 Edition) | RBI FEMA Compliance

---

## PART 1: NOSTRO / VOSTRO ACCOUNT AUDIT

```
NOSTRO ACCOUNTS (Our account with a Foreign Bank):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DEFINITION: Indian bank's account maintained with a foreign bank
  abroad in foreign currency (e.g., our USD account with Citi NY)

AUDIT PROCEDURE:
[ ] Obtain NOSTRO statement from each correspondent bank (SWIFT)
[ ] Reconcile each NOSTRO with CBS NOSTRO GL balance
[ ] Prepare NOSTRO Reconciliation Statement:
    As per correspondent bank:      $XXX
    Add: Credits in transit (debit in our books, not in theirs yet)
    Less: Debits in transit (credit in our books, not in theirs)
    = Reconciled balance:           $XXX (should match CBS)
[ ] OLD UNRECONCILED ITEMS (CRITICAL):
    Items >30 days unreconciled → LFAR adverse comment
    Items >90 days → potential fraud / loss → MOC + LFAR
[ ] Stale items: investigate each item individually
[ ] SWIFT confirmations: obtained for all significant items
[ ] Inter-NOSTRO transfers: correctly routed?

VOSTRO ACCOUNTS (Foreign Bank's account with us):
[ ] Foreign bank's balance confirmed (they send us statement)
[ ] Match against our books
[ ] Interest on VOSTRO: per bilateral agreement; correctly accrued
[ ] VOSTRO for NRI remittances: routing correctly?
```

---

## PART 2: FOREIGN EXCHANGE OPERATIONS AUDIT

```
FOREX DEALING ROOM:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERNAL CONTROLS (RBI guidelines on forex risk):
[ ] FRONT OFFICE: Dealers; execute transactions; report to Treasury Head
[ ] MID OFFICE: Risk management; monitors limits; independent from front
[ ] BACK OFFICE: Settlement; reconciliation; confirmation; independent
    (Three-way separation is mandatory per RBI)

POSITION LIMITS:
[ ] Daylight Limit (Intraday open position): Board-approved
[ ] Overnight Limit (Open position at day-end): Board-approved + RBI prescription
[ ] Stop-Loss Limit: per dealer + aggregate; breach → mandatory close
[ ] Gap Limit (ALM — interest rate risk in forex book): per tenor bucket

DEAL TICKET CONTROLS:
[ ] Each deal: deal slip / deal ticket with dealer ID, timestamp, counterparty, rate
[ ] Confirmation from counterparty: obtained within specified time
[ ] Settlement instructions: matched via SWIFT confirmation
[ ] Unauthorised / verbal deals: none; all through approved systems
[ ] Over-the-counter: CCIL reporting for eligible OTC derivatives

REVALUATION (MTM):
[ ] End-of-day open position revalued at RBI reference rate / FEDAI rate
[ ] P&L impact of daily revaluation: correctly booked
[ ] 31 March revaluation: at closing rate — P&L finalised
```

---

## PART 3: EXPORT FINANCE AUDIT

```
PRE-SHIPMENT CREDIT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EPC (Export Packing Credit — Rupee):
  Period: Up to 180 days from disbursement (360 days for project exports)
  Interest: Competitive; RBI Master Direction sets benchmark
  Condition: Against firm export order / Letter of Credit
  
PCFC (Pre-Shipment Credit in Foreign Currency):
  Currency: USD/EUR/GBP etc. (as per buyer's LC)
  Rate: Not to exceed SOFR + 200 bps (as of FY 2024-25; LIBOR replaced by SOFR)
  Period: Up to 180 days
  Conversion: PCFC converted to EPC/PSCFC at end of period if not liquidated

AUDIT CHECKS:
[ ] Export order / LC on file before PCFC disbursement
[ ] PCFC rate: within permissible ceiling (SOFR + 200 bps)?
[ ] Period: not exceeded without extension authorisation
[ ] Liquidation: against export bills (bill proceeds → PCFC repayment)
[ ] Bills not presented: follow up by bank (FEMA obligation)
[ ] PCFC-NPA: overdue pre-shipment credit → NPA with 90-day rule (NOT crop rule)

POST-SHIPMENT CREDIT:
PSCFC (Post-Shipment Credit in Foreign Currency):
  Against export bills; usance period
  Bill proceeds repay PSCFC
  
FSCFC / Rupee Post-Shipment:
  Against documents; advance against export bills

OVERDUE EXPORT BILLS:
[ ] Export bills outstanding > 6 months from shipment date: OVERDUE
[ ] Bank's obligation: report to EDPMS; regularise within 12 months
[ ] FEMA Section 25: penalty on exporters/banks for non-realisation
[ ] AML: proceeds from export bills going to unexpected jurisdictions?
```

---

## PART 4: IMPORT FINANCE AUDIT

```
IMPORT LCs AND PAYMENTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ ] Import LC issuance: within sanctioned limits + bank's internal policy
[ ] Documents lodged: UCP 600 compliance; discrepant docs?
[ ] Payment for imports: within 6 months of shipment (FEMA rule)
[ ] Delayed payments: regularisation through bank / RBI compounding
[ ] Import bills outstanding > 6 months: IDPMS (Import Data Processing & Monitoring)
[ ] FEMA compliance: payment only to overseas seller; not to shell entities
[ ] Deferred payment imports: RBI ECB/trade credit norms

BUYER'S CREDIT / SUPPLIER'S CREDIT:
[ ] Short-term trade credit: ≤3 years from date of shipment
[ ] Amount: per RBI norms (varies by type of import)
[ ] Interest: market rate; within SOFR + spread cap
[ ] Registration: with bank/RBI where required

DEVOLVED LCs:
[ ] Importer failed to pay → LC devolves on bank
[ ] Bank makes payment to foreign bank (NOSTRO debit)
[ ] Creates a LOAN to the importer
[ ] If overdue >90 days from devolvement date → NPA!
[ ] Many hidden NPAs are devolved LCs — MUST check CBS
```

---

## PART 5: FORWARD CONTRACTS & DERIVATIVES AUDIT

```
FORWARD EXCHANGE CONTRACTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PURPOSE: Hedging forex risk for importers/exporters
AUDIT CHECKS:
[ ] Genuine underlying transaction: hedge must match underlying
    (No naked speculation by customers on proprietary account)
[ ] Contract terms: currency, amount, rate, settlement date
[ ] MTM on 31 March: bank marks all outstanding contracts to current rate
    Gain: recognised in P&L (realised / to be realised)
    Loss: provided for in P&L (prudence principle)
[ ] Customer cancellation: penalty / gain as per FEDAI rules
[ ] Early delivery: premium/discount at current market rate
[ ] Overdue forwards (not settled): regularisation or cancellation
[ ] NOSTRO impact: delivery/settlement of matured contracts

CURRENCY SWAPS / INTEREST RATE SWAPS (IRS):
[ ] Purpose: hedging or trading?
[ ] Notional principal: disclosed in Notes to Accounts
[ ] Fair value as at 31 March: MTM gain/loss recognised
[ ] ISDA Master Agreement in place with each counterparty?
[ ] Collateral: Initial/Variation Margin requirements met?
[ ] CCIL clearing: mandated for certain derivatives

FEMA COMPLIANCE AUDIT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
R-RETURNS (Regulatory Returns to RBI):
[ ] R-Return (forex transactions): filed correctly with RBI
[ ] BSR-6 Return: outstanding export bills
[ ] FLA Return: Foreign Liabilities and Assets (Annual)
[ ] FCTRS/FC-GPR/FC-TRS: for FDI/ODI investments
[ ] ECB Returns: External Commercial Borrowings

AD-I / AD-II COMPLIANCE:
[ ] Authorised Dealer Category I: full forex powers
[ ] Authorised Dealer Category II: limited forex powers
[ ] Scope of forex operations within AD category permissions
[ ] FEMA violations: any compounding cases? RBI penalties?

NRI ACCOUNTS (FEMA):
[ ] NRE Accounts: INR, fully repatriable; FEMA Schedule 1
[ ] NRO Accounts: INR, limited repatriation (USD 1 million/year)
[ ] FCNR(B): Foreign currency deposits; fully repatriable
    - Currency: USD/GBP/EUR/CAD/AUD/JPY
    - Rate: not to exceed SOFR/LIBOR + spread caps (RBI-prescribed)
    - Principal fully repatriable; interest also repatriable
[ ] RFC Accounts (Residents returning from abroad): foreign currency
[ ] EEFC (Exchange Earners' Foreign Currency): for exporters
    - Can retain up to 100% of forex earnings
    - Must be used for business purposes
```

---

## PART 6: LETTER OF CREDIT (LC) COMPLETE AUDIT

```
LC AUDIT — STEP BY STEP:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1: LC OUTSTANDING REGISTER
[ ] Obtain complete LC register as at 31 March
[ ] Each LC: amount, currency, expiry, liability type, margin held
[ ] Contingent liability = total unexpired LC outstandings

STEP 2: CLASSIFICATION
[ ] Unexpired LCs (not yet drawn): contingent liability
[ ] Drawn but not yet due: accepted bills (outstanding in books)
[ ] Overdue drawn LCs (devolved): treat as advances; NPA if >90 days

STEP 3: DOCUMENTS & COMPLIANCE
[ ] Sample of LC files: verify document compliance under UCP 600
[ ] Import LCs: bill of lading, invoice, packing list, certificate of origin
[ ] Export LCs: same + ECGC cover (if applicable)
[ ] Discrepant documents: bank's decision to accept/reject documented?
[ ] Usance LC: due date tracked; interest income for bank

STEP 4: DEVOLVEMENTS
[ ] List of devolved LCs during year
[ ] Recovery status: amount received from applicant?
[ ] Overdue devolvement >90 days: NPA classified?
[ ] Provision: NPA provisions applied to devolved LC loans?

STEP 5: COMMISSION INCOME
[ ] LC commission: accrued over period of LC (not upfront)
[ ] Amendment fee: one-time; recognised on amendment date
[ ] Confirmation charges: if bank also confirmed → separate income
[ ] Unrealised commission on unexpired LCs: deferred correctly?
```

---

## PART 7: BANK GUARANTEE AUDIT

```
BG AUDIT — STEP BY STEP:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1: BG OUTSTANDING REGISTER
[ ] Complete register as at 31 March: guarantee number, amount, beneficiary, expiry
[ ] Segregate: unexpired (contingent) vs expired (but possibly invoked) vs invoked

STEP 2: TYPES AND LIMITS
[ ] Financial BGs (FBG): within credit sanctioned limits
[ ] Performance BGs (PBG): within credit/non-credit limits
[ ] Verify: BG value within sanctioned sub-limit for guarantees

STEP 3: EXPIRY TRACKING
[ ] All BGs: expiry date tracked in CBS
[ ] Expired BGs: discharge/return of BG instrument from beneficiary obtained?
[ ] Expired but claims period not yet over: maintain contingency

STEP 4: INVOCATIONS
[ ] Invocations during year: each one verified
[ ] Was invocation legal? (valid claim by beneficiary)
[ ] Payment made under invocation → recovery from applicant initiated?
[ ] If applicant defaults → NPA after 90 days from invocation date
[ ] Provision on invoked BG loans: as per NPA classification

STEP 5: COMMISSION RECOGNITION
[ ] BG commission: MUST be amortised over BG period
[ ] Total commission = Annual rate × Amount × Period
[ ] Deferred commission at year-end = commission for unexpired period
[ ] Upfront recognition = OVERSTATEMENT of income = MOC item
```

---

## PART 8: FEMA OFFENCES — AUDITOR'S ROLE

```
AUDITOR'S RESPONSIBILITY UNDER FEMA:
  Auditors are NOT required to report FEMA violations directly
  However: Material FEMA violations should be:
  (a) Reported in audit report under "Other Matters" para
  (b) Included in LFAR under Forex/FEMA section
  (c) Reported in MOC if financial impact exists
  
COMMON FEMA VIOLATIONS TO WATCH:
[ ] Export realisation not received within 9 months (now 12 months for project exports)
[ ] Import payment for non-genuine imports (capital flight)
[ ] Overseas remittances without RBI approval / LRS limit exceeded
    - LRS (Liberalised Remittance Scheme): USD 250,000 per person per year
[ ] NRE deposits: proceeds from non-repatriable sources deposited
[ ] FCNR renewal without proper documentation
[ ] Hawala / round-tripping through trade accounts
[ ] FEMA Section 13 contravention: penalties 3× amount involved

RBI REPORTING BY BANK (AD-I):
[ ] Suspicious forex transactions: report to RBI + FIU
[ ] Transactions involving high-risk jurisdictions: enhanced monitoring
[ ] Structuring of transactions: splitting to avoid regulatory reporting?
```

---

## PART 9: KEY RBI FOREX CIRCULARS REFERENCE

```
MASTER DIRECTIONS:
  RBI Master Direction on Export of Goods and Services (Jan 2016, updated)
  RBI Master Direction on Import of Goods and Services (Jan 2016, updated)
  RBI Master Direction on Establishment of Liaison/Branch/Project Offices (Mar 2016)
  RBI Master Direction on Risk Management and Inter-bank Dealings (Jul 2016)
  RBI Master Direction on Non-Resident Foreign Currency (FCNR-B) Accounts
  RBI Master Direction on External Commercial Borrowings (ECB) (Jul 2019)
  RBI Forex Derivatives Master Direction (Apr 2020)

FEDAI RULES:
  FEDAI Rule 1: Code of Conduct for Forex Brokers
  FEDAI Rule 6: Foreign Exchange Transactions — Merchant Rates
  FEDAI Rule 7: Export Credit
  FEDAI Rule 8: Guarantees

KEY RATES (FY 2024-25):
  SOFR (Secured Overnight Financing Rate): check current rate
  PCFC/PSCFC ceiling: SOFR + 200 bps
  FCNR(B) deposit ceiling: SOFR + 200 bps (as current)
  LRS limit: USD 250,000 per person per year
```
