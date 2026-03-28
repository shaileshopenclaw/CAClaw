# NPA Classification, IRACP Norms & Provisioning — Complete Reference
## ICAI Guidance Note on Audit of Banks (2025 Edition) | RBI Master Circular on IRAC

---

## PART 1: INCOME RECOGNITION (IR)

### 1.1 The Core Principle

```
STANDARD (PERFORMING) ASSETS:
→ Interest income recognised on ACCRUAL basis
→ Credit to P&L monthly as it accrues
→ Even if not actually received in cash

NON-PERFORMING ASSETS:
→ ZERO accrual on NPA accounts
→ ALL previously accrued but uncollected interest must be REVERSED
→ Reversals go to "Interest Suspense Account" (not P&L)
→ Income recognised ONLY on ACTUAL CASH RECEIPT

CRITICAL DATE RULE:
→ When account becomes NPA, reverse all unrealised income
   from the date of NPA backwards until all unrealised income is reversed
→ This reversal is a MANDATORY MOC entry if not done by management
```

### 1.2 Specific Asset Classes — Income Recognition

```
ASSET TYPE                   | INCOME RECOGNITION BASIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Term Loans (Performing)      | Accrual monthly
CC/OD (Performing)           | Accrual monthly
Bills (Performing)           | Accrual at discount rate
NPA (any type)               | ONLY on cash receipt
SMA accounts                 | Accrual continues (SMA ≠ NPA)
Restructured accounts        | Accrual continues IF Standard
                             | Cash basis IF NPA after restructure
Government guaranteed accts  | Accrual (even if technically overdue,
                             | if Government guarantee not invoked)
FITL (Funded Interest TL)    | Cash basis (NPA treatment)
```

### 1.3 Fees and Commission

```
PROCESSING FEE:
→ IGAAP: can be recognised upfront (per bank's accounting policy)
→ Ind AS 109: MUST be amortised over effective life of loan
  (included in effective interest rate — EIR calculation)
  If not, this is a qualification risk

COMMISSION ON LETTERS OF CREDIT:
→ Recognised over the tenure of the LC, not upfront
→ Upfront recognition = overstatement of income = MOC item

COMMISSION ON BANK GUARANTEES:
→ Recognised over the tenure of BG
→ Outstanding commission on long-dated BGs: verify deferred recognition

PREPAYMENT FEE / FORECLOSURE CHARGES:
→ Recognised when charged (one-time event)
```

---

## PART 2: ASSET CLASSIFICATION (AC)

### 2.1 Performing Asset — Standard

```
STANDARD ASSET criteria:
→ No overdue in principal or interest
→ OR overdue for 1-30 days (SMA-0 — still Standard)
→ Account operating within sanctioned limits

SPECIAL MENTION ACCOUNTS (SMA) — EARLY WARNING SYSTEM:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SMA-0 | Overdue 1–30 days      | Standard; monitor closely
SMA-1 | Overdue 31–60 days     | Standard; enhanced monitoring
SMA-2 | Overdue 61–90 days     | Standard; most at-risk
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NOTE: SMA is NOT NPA. Income still on accrual for SMA.
CRILC Reporting: SMA-1 and SMA-2 accounts with exposure ≥₹5 Crore
must be reported to CRILC every fortnight.
```

### 2.2 Non-Performing Asset (NPA) — Definition

**A loan asset becomes NPA when it CEASES TO GENERATE INCOME for the bank.**

```
TERM LOANS:
→ NPA when interest AND/OR principal overdue for MORE THAN 90 DAYS
→ Day 91 from due date = NPA

CASH CREDIT / OVERDRAFT — "OUT OF ORDER" CRITERIA:
An account is "Out of Order" and becomes NPA when:
  CONDITION A: Outstanding balance continuously exceeds
               sanctioned limit OR Drawing Power for >90 days
  OR
  CONDITION B: No credit in the account for continuous 90 days
  OR
  CONDITION C: Credits are not sufficient to cover the interest
               debited during the last 90 days
→ Even ONE of these conditions = NPA

BILLS PURCHASED / DISCOUNTED:
→ NPA when the bill is not paid by the drawee (remains overdue)
   for MORE THAN 90 DAYS

AGRICULTURAL LOANS:
→ Short Duration Crops (one growing season, e.g. paddy, wheat):
  NPA if interest/principal not paid within TWO crop seasons
  from the due date of repayment
→ Long Duration Crops (plantation crops, sugarcane, etc.):
  NPA if interest/principal not paid within ONE crop season
  from due date
→ Allied Activities (dairy, poultry, fisheries, animal husbandry):
  Normal 90-day rule applies

EXPORT CREDIT:
→ For PCFC (Rupee packing credit): normal 90-day rule
→ For Export bills: 90 days from due date

LEASE RECEIVABLES:
→ NPA if the amount of lease rental and principal
  outstanding for 90+ days

NPI (Non-Performing Investments):
→ Any scheduled interest or principal payment on
  debt securities overdue >90 days
```

### 2.3 Cross-Default Rule (Critical!)

```
CROSS-DEFAULT / BORROWER-LEVEL NPA RULE:
If ANY facility of a borrower becomes NPA:
→ ALL OTHER facilities of the SAME BORROWER
  at the SAME BANK must also be classified NPA

This includes:
→ All branches of the same bank
→ All loan types (CC, TL, BG, LC, etc.)
→ All related entities if borrower is a company group
  (as per bank's credit policy on related parties)

AUDITOR CHECK:
[ ] For each NPA account: verify borrower's ALL accounts NPA?
[ ] Check linked accounts (PAN-based lookup recommended)
[ ] Guarantors: if guarantee invoked, guarantor's accounts NPA?

EXCEPTION: OD accounts created for specific purposes (e.g.
interest conversion) are exempt if separately tracked.
```

### 2.4 NPA Sub-Classification

```
CLASSIFICATION MATRIX:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CATEGORY          | AGE OF NPA          | SECURED % | UNSECURED %
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sub-Standard      | ≤12 months NPA      |   15%     |    25%
Doubtful-1 (D1)   | >12 to ≤24 months   |   25%     |   100%
Doubtful-2 (D2)   | >24 to ≤36 months   |   40%     |   100%
Doubtful-3 (D3)   | >36 months NPA      |  100%     |   100%
Loss              | Identified loss     |  100%     |   100%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AGE COMPUTATION:
→ "Date of NPA" = the date the account first became NPA
→ Sub-standard: 0 to 12 months from Date of NPA
→ D1: 13 to 24 months from Date of NPA
→ D2: 25 to 36 months from Date of NPA
→ D3: >36 months from Date of NPA

AUDITOR MUST VERIFY:
[ ] Date of NPA as per CBS vs auditor's determination
[ ] If auditor's date differs → reclassification → MOC entry
[ ] Age determines correct sub-class and provision rate
```

### 2.5 Loss Asset

```
LOSS ASSET — DEFINITION:
An account where:
→ Loss has been identified by the bank, internal auditors,
  external auditors, RBI inspection, or
→ Loss is so apparent that continued classification is meaningless

WHEN TO CLASSIFY AS LOSS:
→ Any D3 account where recovery is nil/negligible
→ Fraud accounts (even if <36 months old)
→ RBI/internal auditor has identified as loss

IMPORTANT: Loss ≠ Written Off
→ Loss assets can remain in books (not yet written off)
→ Must have 100% provision regardless
→ Written off = removed from balance sheet; provision released
```

### 2.6 NPA Upgradation

```
UPGRADATION CRITERIA — VERY STRICT:
An NPA can be UPGRADED to Standard ONLY when:
→ ALL overdue PRINCIPAL is FULLY paid
→ ALL overdue INTEREST is FULLY paid
→ Both conditions must be met simultaneously
→ Partial payment does NOT qualify for upgradation

UPGRADATION TIMING:
→ After full repayment of overdues:
  The account is upgraded to Standard
→ It does NOT automatically go through SMA stages
→ But the bank may monitor it as "upgraded" for 1 year

TECHNICALLY WRITTEN OFF ACCOUNTS:
→ Can only be upgraded after COMPLETE RECOVERY
→ Must be brought back to books first, then upgraded
→ Recovery from written-off accounts → credited to P&L
```

---

## PART 3: PROVISIONING REQUIREMENTS

### 3.1 Standard Asset Provisions

```
STANDARD ASSET PROVISIONING:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Asset Type                                    | Rate
Direct Agriculture & SME loans                | 0.25%
All other Standard assets                     | 0.40%
Commercial Real Estate (CRE)                  | 1.00%
CRE — Residential Housing Projects            | 0.75%
Standard Restructured Loans (monitoring)      | 5.00%
Teaser Rate Home Loans (during teaser period) | 2.00%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NOTE: Standard asset provisions = General/Floating Provisions
These are shown as a CREDIT in the balance sheet (liability)
NOT netted against advances (unlike NPA provisions)
```

### 3.2 NPA Provisioning — Core Rules

```
PROVISION RATES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  | SECURED          | UNSECURED
Sub-Standard      | 15%              | 25%
Doubtful-1 (D1)   | 25%              | 100%
Doubtful-2 (D2)   | 40%              | 100%
Doubtful-3 (D3)   | 100%             | 100%
Loss              | 100%             | 100%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECURED vs UNSECURED SPLIT:
Step 1: Identify "realisable value" of security
        (most recent valuation, not original purchase price)
Step 2: Secured = MIN(Outstanding Balance, Realisable Value of Security)
Step 3: Unsecured = Outstanding Balance − Secured Portion
Step 4: Apply respective rates to each portion
Step 5: Total Required Provision = Provision on Secured + Provision on Unsecured

WHAT COUNTS AS SECURITY (for "Secured" classification)?
✅ Tangible assets: land, building, plant, machinery, vehicles
✅ Charge on stocks and book debts (subject to DP limits)
✅ Gold (valued at current market rate)
✅ FD (bank's own deposit — lien marked)
✅ NSC/KVP/LIC (assigned to bank)
❌ Personal guarantee (unsecured)
❌ Corporate guarantee (unsecured unless guaranteed by assets)
❌ Charge on intangible assets (patents, goodwill)
❌ Second charge on fully encumbered assets

VALUATION DISCOUNTING:
→ Property valuation: use only if obtained by empanelled valuer
  within LAST 3 YEARS. If older, treat as NIL for security.
→ Valuation must be "forced sale value" not "market value"
→ Plant & machinery: valuation/depreciated book value (conservative)
```

### 3.3 Comprehensive Provision Calculation — Step by Step

```
EXAMPLE CALCULATION:

Account: ABC Engineering Pvt Ltd
Classification: Doubtful-2 (NPA since March 2022 — 3 years)
Outstanding Balance: ₹120 Lakhs
Security: Factory land + building, valued at ₹80 Lakhs (2023 valuation)
         Stocks charged: ₹20 Lakhs (stock statement — 6 months old!)

STEP 1: Determine eligible security
  Land + Building: ₹80L (valuation < 3 years → eligible)
  Stocks: 6 months old stock statement. If bank's policy requires
          monthly statements for CC/OD, this is STALE.
          Conservative approach: Treat stocks as NIL for security.

STEP 2: Calculate secured/unsecured:
  Eligible Security: ₹80 Lakhs
  Outstanding: ₹120 Lakhs
  Secured Portion: MIN(120, 80) = ₹80 Lakhs
  Unsecured Portion: 120 − 80 = ₹40 Lakhs

STEP 3: Apply D2 rates:
  Provision on Secured: 80 × 40% = ₹32 Lakhs
  Provision on Unsecured: 40 × 100% = ₹40 Lakhs
  Total Required Provision: ₹72 Lakhs

STEP 4: Compare with existing provision:
  Existing Provision held: ₹50 Lakhs (per CBS)
  SHORTFALL: ₹72L − ₹50L = ₹22 Lakhs → MOC ENTRY
```

### 3.4 Special Provisioning Situations

#### A. IBC/NCLT Accounts

```
RBI Circular DBR.No.BP.BC.101/21.04.048/2017-18 (as updated):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STAGE                         | MINIMUM PROVISION
CIRP Admitted (1st list)      | 50% immediately
                              | (sub-standard: 50%; ≥50% anyway)
CIRP Admitted (2nd list)      | 100% immediately
Resolution Plan Approved      | As per haircut in plan
Liquidation Ordered           | 100% immediately

ADDITIONAL: For accounts where 180 days CIRP period expired
without resolution plan:
→ If banks have not made 50% provision yet → make immediately
→ Additional 20% every 6 months thereafter

AUDITOR CHECK:
[ ] List all NCLT/IBC accounts
[ ] Verify admission dates and CIRP timelines
[ ] Cross-check provisions against RBI requirements
[ ] If resolution plan approved: verify plan terms + provision
[ ] If liquidation: 100% provision mandatory
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

#### B. Restructured/Resolution Framework Accounts

```
RESTRUCTURED ACCOUNTS — PROVISIONING:
Standard Restructured (during monitoring period):  5%
NPA Restructured (slipped after restructuring):     Normal NPA provision
FITL (Funded Interest Term Loan):                  Treated as NPA for
                                                    interest accrual

RBI RESOLUTION FRAMEWORK (June 2019 — KV Kamath Committee):
→ Accounts restructured under this: Monitor for 2 years
→ Monitoring period provision: 10% (higher than standard 5%)
→ If account meets all parameters → upgrade to Standard + release 5%

COVID-19 RESOLUTION FRAMEWORK:
→ Accounts restructured under COVID 2.0 (May 2021 onward)
→ Monitoring period ended typically by 2024
→ Auditor must check if these accounts are still monitoring, have
  slipped to NPA, or been successfully upgraded
```

#### C. Government Guaranteed Accounts

```
CENTRAL GOVERNMENT GUARANTEE:
→ If guarantee is valid and invoked within stipulated time:
  Provision = Only on UNSECURED portion (guarantee covers principal)
→ Guarantee invoked but Government has NOT paid within 30 days:
  Treat as UNSECURED = 100% provision on entire outstanding

STATE GOVERNMENT GUARANTEE:
→ Same treatment as Central Govt guarantee
→ If state has history of non-honouring guarantees:
  Treat as unsecured (conservative approach per RBI guidelines)

CREDIT GUARANTEE SCHEMES (CGTMSE, CGFMU, NCGTC):
→ Only the UNCOVERED portion is treated as unsecured
→ Covered portion: provision at standard secured rates
→ Example: CGTMSE covers 75% of ₹100L loan = ₹75L covered
  Secured: ₹75L × 15% (Sub-std) = ₹11.25L
  Unsecured: ₹25L × 25% = ₹6.25L
  Total: ₹17.5L (vs ₹25L if fully unsecured)
```

#### D. SARFAESI / DRT Accounts

```
IMPACT ON PROVISIONING:
→ SARFAESI action does NOT reduce provision requirement
→ Provision based on outstanding balance, not expected recovery
→ Exception: where physical possession of asset obtained AND
  asset sold OR valuation obtained recently
  → Use realised/realisable value to determine secured portion

60-DAY NOTICE STATUS:
[ ] 60-day notice issued: ___/___/___
[ ] Asset taken possession under Section 13(4)?
[ ] DM/CMM order obtained?
[ ] Asset sold at auction? Sale price: ₹___L
[ ] Recovery progress to date: ₹___L
→ Any recovery: credit to provision account (not P&L directly)
  unless provision fully extinguished
```

#### E. Written-Off Accounts (Technical and Full)

```
TECHNICAL WRITE-OFF:
→ Account removed from Balance Sheet (fully provided and written off)
→ Recovery proceedings STILL ONGOING (SARFAESI, DRT, IBC etc.)
→ These are "Off-Balance Sheet" accounts
→ Auditor should request a list of technical write-offs
→ Ensure all are 100% provided BEFORE write-off
→ Any recovery from technical write-offs → credit to P&L (income)

FULL WRITE-OFF:
→ All recovery proceedings abandoned or settled
→ Removed from records entirely
→ Requires Board approval for write-off
→ Proper documentation in loan file

AUDITOR CHECK:
[ ] Write-off register obtained?
[ ] Board approval for each write-off >₹1 Crore?
[ ] Recovery proceedings status documented?
[ ] SARFAESI/DRT records maintained post-write-off?
[ ] Tax benefit claimed on write-off (Section 36(1)(vii) — for tax audit)
```

---

## PART 4: PROVISION COVERAGE RATIO (PCR)

```
PCR FORMULA:
  PCR = (Total Provisions held / Gross NPA) × 100

COMPONENTS:
  Total Provisions = NPA Provisions + Technical Write-Off provisions
  Gross NPA = All NPA outstanding (before provisions)

RBI MINIMUM REQUIREMENT: PCR ≥ 70%
  (70% including technical write-off provisions)

INTERPRETATION:
  PCR > 70%: Adequate coverage
  PCR = 50-70%: Warning level — report in LFAR
  PCR < 50%: Critical deficiency — likely qualification

EXAMPLE:
  Gross NPA: ₹500 Crore
  NPA Provisions held: ₹280 Crore
  Technical Write-offs: ₹120 Crore
  PCR = (280 + 120) / 500 × 100 = 80% ✅

RUN: scripts/11_provision_coverage_ratio.py
```

---

## PART 5: NPA MANAGEMENT — AUDIT PROCEDURES

### 5.1 NPA Sampling Strategy

```
MANDATORY (100% COVERAGE):
→ All NPA accounts
→ All SMA-2 accounts (potential hidden NPA)
→ All accounts with exposure >₹1 Crore
→ All accounts with recent restructuring (last 2 years)
→ Top 20 performing accounts (test for hidden NPA)

RISK-BASED SAMPLING:
→ CC/OD accounts where balance is close to DP (within 10%)
→ Accounts where credits are regular but only to cover interest
  (no reduction in principal) — potential evergreening
→ Accounts in stressed sectors (real estate, infra, gems/jewellery)
→ Accounts where stock statements have gaps

ANALYTICAL PROCEDURES:
→ Year-over-year NPA movement analysis
→ Sector-wise NPA concentration
→ Account-wise NPA movement (additions/reductions/upgrades)
→ Interest suspense account movement
→ Comparison of branch NPA with system-wide NPA
```

### 5.2 Red Flags for Hidden NPA

```
EVERGREENING INDICATORS (Most Dangerous):
❌ Loans disbursed just before due date of another loan
   (round-tripping: fresh loan repays old loan)
❌ Multiple accounts of same borrower: one repays another
❌ Current account credited at month-end to zero SMA
   then debited back next day
❌ Credits in CC account from unknown/unrelated sources
❌ Inter-company funds transferred to clear CC before due date
❌ Restructuring without genuine financial improvement
❌ Asset classification upgrade without full payment of overdues
❌ DP artificially inflated using unaudited/inflated stock statements
❌ LC/BG devolvements shown as "loans" instead of NPA
❌ Interest charged and immediately reversed (net zero — gaming)

AUDITOR PROCEDURE:
1. Obtain CBS data extract: all debits and credits for last 6 months
2. Look for unusual patterns (large round-number credits near month-end)
3. Trace credits — verify source (genuine business receipts?)
4. For CC/OD: verify stock statements vs actual operations
5. Verify turnover vs projected sales in loan appraisal
```

### 5.3 Drawing Power (DP) Calculation

**Run:** `scripts/02_drawing_power_calculator.py`

```
FORMULA:
DP = (Value of Stock + Value of Debtors - Creditors) × (1 - Margin)
OR equivalently:
DP = (Stock × (1-margin_s)) + (Debtors × (1-margin_d)) - Creditors

COMMON MARGIN RATES:
Stock (raw material):      20-25%
Stock (WIP):               50% (conservative)
Stock (finished goods):    20-25%
Book Debts (<90 days):     25-40%
Book Debts (>90 days):     Not eligible
Export debtors:            10-25% (per bank/sanction terms)

EXAMPLE (detailed):
Sanctioned CC limit: ₹100 Lakhs
Stock statement (30 days old):
  Raw material: ₹40L
  WIP: ₹10L
  Finished goods: ₹30L
Debtors < 90 days: ₹25L
Debtors > 90 days: ₹8L (NOT ELIGIBLE)
Creditors: ₹15L
Margin rates: Stock 25%, Debtors 40%

DP Calculation:
  Raw material eligible: 40 × 0.75 = ₹30.0L
  WIP eligible: 10 × 0.50 = ₹5.0L (if per bank's policy)
  Finished goods eligible: 30 × 0.75 = ₹22.5L
  Debtors <90d eligible: 25 × 0.60 = ₹15.0L
  Less Creditors: (₹15.0L)
  DP = 30 + 5 + 22.5 + 15 - 15 = ₹57.5 Lakhs

Sanctioned Limit: ₹100L; DP: ₹57.5L
Permissible Drawing Power = MIN(100, 57.5) = ₹57.5 Lakhs

If outstanding balance = ₹70L:
  EXCESS over DP = ₹70L - ₹57.5L = ₹12.5L
  If this excess persists >90 days continuously → NPA!

STOCK STATEMENT STALENESS:
→ If latest stock statement >30 days old:
  DP = Previous DP
  OR as per bank policy (some banks: DP = nil if no statement)
→ LFAR reporting required for missing statements
```

---

## PART 6: LFAR AND MOC FOR NPA

### 6.1 LFAR NPA Reporting Template

```
LFAR SECTION I-5 — NPA (Standard Reporting Format):

(a) TOTAL NPA POSITION AS AT 31 MARCH 20XX:

Classification  | No. of A/cs | Outstanding (₹L) | Provision Held (₹L)
Sub-Standard    |             |                  |
Doubtful-1      |             |                  |
Doubtful-2      |             |                  |
Doubtful-3      |             |                  |
Loss            |             |                  |
TOTAL           |             |                  |

(b) AUDITOR'S CLASSIFICATION DISAGREEMENT:
[List all accounts where auditor disagrees with bank]

A/c No. | Name | Outstanding | Bank Class | Auditor Class | Reason
--------|------|-------------|------------|---------------|-------
        |      |             |            |               |
TOTAL ADDITIONAL PROVISION REQUIRED: ₹ _______ Lakhs

(c) PROVISION SHORTFALL SUMMARY:
Bank's Provision (per books):        ₹ _______ Lakhs
Required Provision (per IRACP):      ₹ _______ Lakhs
Shortfall:                           ₹ _______ Lakhs
Provision Coverage Ratio (PCR):      ______ %
(RBI minimum requirement: 70%)

(d) LARGE NPA ACCOUNTS (>₹1 Crore each) — account-wise comments
[Separate annexure with case-by-case analysis]
```

### 6.2 MOC for NPA Issues

```
MOC ENTRY FORMAT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HEAD: ADVANCES — NPA Provisioning
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sl | A/c No | Name | O/s (₹L) | Bank Class | Auditor | Req.Prov | Held | Short
   |        |      |           |            | Class   | (₹L)     | (₹L) | (₹L)

BOOKING ENTRY (if bank agrees):
  Dr. Profit & Loss A/c (NPA Provision) — ₹XX
  Cr. Provision for NPA A/c — ₹XX

INTEREST REVERSAL ENTRY:
  Dr. Interest Suspense A/c — ₹XX
  Cr. Interest Income A/c (P&L) — ₹XX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## PART 7: RESTRUCTURING AND RESOLUTION FRAMEWORK

### 7.1 Types of Restructuring

```
TYPES:
1. OTS (One Time Settlement): full/partial settlement
2. Compromise Settlement: below outstanding, write-off balance
3. RBI Resolution Framework (June 2019 circular)
   → For stressed accounts >₹100 Crore (ICA required)
4. COVID-19 Resolution Framework (May 2021)
5. MSME Restructuring Framework
6. IBC/NCLT (Insolvency & Bankruptcy Code 2016)
7. SDR (Strategic Debt Restructuring — discontinued)
8. S4A (Scheme for Sustainable Structuring — discontinued)
```

### 7.2 Resolution Framework Audit

```
FOR EACH RESTRUCTURED ACCOUNT:
[ ] Board/appropriate authority approval for restructuring?
[ ] Independent TEV (Techno Economic Viability) study?
[ ] Was RBI prior approval required? If yes, obtained?
[ ] Monitoring period running? (Typically 1-2 years)
[ ] Is provision at 5% (standard restructured)?
[ ] Performance during monitoring: covenants met?
[ ] Any accounts that slipped during monitoring → NPA
[ ] Accounts that completed monitoring → upgrade to Standard?
[ ] FITL created: provisioned and disclosed properly?

KEY DATES TO CHECK:
→ Date of restructuring: ___________
→ Monitoring period end date: ___________
→ Any payment default during monitoring? → NPA
→ Performance parameters agreed: ___________
→ Actual performance: ___________
```

---

## PART 8: KEY RBI CIRCULARS FOR NPA/IRACP

```
PRIMARY CIRCULARS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. RBI Master Circular — Prudential Norms on IRAC
   (Updated annually — latest version for FY 2024-25)
   [Latest circular: DBR.No.BP.BC.2/21.04.048/2015-16 as updated]

2. RBI Circular on Resolution Framework (June 7, 2019)
   RBI/2018-19/203 DBR.No.BP.BC.45/21.04.048/2018-19

3. RBI Resolution Framework 2.0 (COVID) — May 5, 2021
   RBI/2021-22/31 DOR.STR.REC.11/21.04.111/2021-22

4. RBI Circular on IBC Provisioning
   DBR.No.BP.BC.101/21.04.048/2017-18 (June 12, 2017)

5. RBI Master Direction on Stress Asset Resolution 2019
   (Updated 2021)

6. SARFAESI Act 2002 + RBI Securitisation Master Directions 2021

7. RBI Circular on KV Kamath Committee Recommendations
   RBI/2020-21/17 DOR.No.BP.BC/4/21.04.048/2020-21
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
