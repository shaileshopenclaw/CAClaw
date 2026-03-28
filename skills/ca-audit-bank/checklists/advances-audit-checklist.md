# ADVANCES AUDIT COMPLETE CHECKLIST
## Bank Branch Audit | ICAI GN 2025 | RBI IRACP Norms

---

## MASTER LOAN FILE CHECKLIST (Per Account)

```
LOAN FILE COMPLETENESS — MUST-HAVE DOCUMENTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DOCUMENT                              | Required | Present | Remarks
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SANCTION & PROCESSING:
[ ] Loan Application (signed by borrower)
[ ] Sanction Letter (signed by competent authority)
[ ] Borrower's acceptance of sanction terms
[ ] CMA (Credit Monitoring Arrangement) / Financial Analysis
[ ] Project Report (for term loans/project finance)
[ ] Income proof (ITR, salary slips, P&L)
[ ] Latest 2-3 years audited financial statements
[ ] GST Returns (last 12 months, if applicable)
[ ] Bank statements of main operating account (12 months)
[ ] Credit appraisal note / credit proposal
[ ] DOA (Delegation of Authority) compliance: sanctioned by right authority?

KYC / AML:
[ ] Aadhaar (OVD — Officially Valid Document)
[ ] PAN Card (mandatory for loans above ₹50,000)
[ ] Latest ITR (last 2 years)
[ ] Photograph (proprietor/partners/directors)
[ ] Board Resolution (company borrowers)
[ ] Certificate of Incorporation (company)
[ ] MOA / AOA (company)
[ ] Partnership Deed (partnership firms)
[ ] CIBIL / credit bureau report (at sanction AND at last renewal)
[ ] CRILC check (≥₹5 Crore) — status at other banks verified

SECURITY DOCUMENTS:
[ ] Registered Mortgage Deed (for immovable property)
[ ] Hypothecation Agreement (for movable assets — stocks, equipment)
[ ] Pledge Agreement (for shares, FDs, gold)
[ ] Personal Guarantee (guarantor's signature + KYC)
[ ] Corporate Guarantee (company resolution, financials of guarantor)
[ ] DPN (Demand Promissory Note) — for term loans
[ ] Letter of Continuity (for CC/OD — extending security to future advances)
[ ] Board Resolution for execution of security documents

PROPERTY / COLLATERAL:
[ ] Title Deed / Sale Deed / Gift Deed (original)
[ ] Search Report / Title Investigation Report (by empanelled advocate)
    → Must be < 3 years old; covers at least 30 years title history
[ ] Encumbrance Certificate (EC) — shows no prior charges
[ ] Property Valuation Report by empanelled valuer
    → Must be < 3 years old; shows both market value + forced sale value
[ ] Latest property tax receipt (municipal taxes paid)
[ ] Khata / 7/12 extract / Patta (land records)
[ ] Approved building plan (for constructed property)
[ ] Occupancy/Completion Certificate (OC/CC)

INSURANCE:
[ ] Comprehensive insurance on charged assets (stock, equipment, property)
[ ] Insurance amount ≥ value of asset (not just loan amount)
[ ] Bank named as: "Mortgagee" or "Loss Payee" (not just endorsee)
[ ] Policy validity: current (not expired!)
[ ] Type: fire + allied perils for property; all-risk for equipment
[ ] Renewal tracking: reminder system in branch?

ONGOING MONITORING (CC/OD ACCOUNTS):
[ ] Monthly stock/debtor statement: all 12 months present?
[ ] Drawing Power register: updated monthly
[ ] Account conduct: regular credits (turnover-based analysis)
[ ] Stock audit report (CC/OD > bank-specified threshold):
    Conducted by empanelled stock auditor; recommendations followed?
[ ] Annual review / renewal: done within due date?
[ ] Credit monitoring visit report: quarterly (for large accounts)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## WORKING CAPITAL LOAN AUDIT CHECKLIST

```
CASH CREDIT / OVERDRAFT — DETAILED PROCEDURES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ ] Verify sanctioned CC limit (per sanction letter)
[ ] Compute Drawing Power (DP) for latest stock statement
    → Use scripts/02_drawing_power_calculator.py for calculation
    → Formula: (Eligible Stock + Eligible Debtors - Creditors)
[ ] If latest stock statement >30 days old: flag in LFAR
    → DP should revert to previous valid DP per bank policy
[ ] Compare: Outstanding Balance vs DP vs Sanctioned Limit
    → If Balance > DP for >90 days: NPA!
    → If Balance > Sanctioned Limit: irregular; report immediately
[ ] Review debits and credits for last 6 months:
    → Are credits genuine business receipts or circular entries?
    → Is monthly turnover consistent with stated business size?
    → Are debits going to known suppliers/expenses or unknown parties?
[ ] Interest application: correct rate applied? EBLR/MCLR reset done?
[ ] Penal charges: any applied? Under new RBI norms (Apr 2024)?
[ ] CC account dormant (no turnover): separately flag for NPA analysis
[ ] Excess: any transactions above CC limit? Sanctioned or unauthorized?
[ ] Concurrent audit: any CC-specific findings unresolved?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## TERM LOAN AUDIT CHECKLIST

```
TERM LOAN AUDIT PROCEDURES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ ] Disbursement schedule: as per sanction terms?
    → Stage-wise disbursement verified?
    → Physical progress verified before each disbursal?
[ ] Repayment schedule: per sanction letter
    → Compare actual repayments with schedule
    → Overdue EMI/installments: number of days, amount
[ ] Moratorium: as per terms? Not extended without approval?
[ ] Interest on TL: accrued monthly, correctly applied
    → EBLR/MCLR reset: done on due dates? New rate applied correctly?
[ ] Post-disbursement verification:
    → End-use of funds: verified (invoices, utilisation certificate)?
    → For project loans: completion certificate received?
    → For equipment loans: asset in place? Insurance done?
[ ] NPA date: when EMI first became overdue (calculate 91st day)
[ ] DSRA (Debt Service Reserve Account): maintained if stipulated?
    → Balance: covers next 2 quarters of debt service?
[ ] Escrow mechanism: in place for large project loans?
    → All project receivables routed through escrow?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## AGRICULTURAL LOAN AUDIT CHECKLIST

```
AGRICULTURAL / KCC LOAN PROCEDURES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ ] Land records: 7/12 extract or Patta — area, ownership correct
[ ] Scale of Finance (SoF): used correct SoF set by DLTC/SLTC?
[ ] KCC limit calculation:
    Crop cultivation expense × Number of crops + Post-harvest + Maintenance
    + Allied activity (if applicable) = Total KCC limit
[ ] Crop type identified: Short Duration or Long Duration?
    → Determines NPA timeline (2 seasons vs 1 season)
[ ] Seasonal due date: correctly set in CBS for repayment?
[ ] Interest subvention: claimed correctly from NABARD/Govt?
    → 7% effective rate to farmer; 1.5% bank gets from govt
    → 3% prompt repayment incentive disbursed to farmers?
[ ] Natural calamity: any RBI/NABARD relief circular applicable?
    → Rescheduling without NPA classification — documented?
[ ] Joint Liability Groups (JLG): all members' signatures on loan?
[ ] Kisan Credit Card (physical card): issued to farmer?
[ ] PM-KISAN: ₹6,000 benefit being credited to KCC account?
[ ] Kisan Vikas Patra (KVP) or NSC: accepted as collateral? Valid?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## NPA VERIFICATION PROCEDURE — FIELD STEPS

```
STEP-BY-STEP NPA AUDIT PROCEDURE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1 — DATA EXTRACTION FROM CBS:
  [ ] Get full advances data dump as at 31 March (all accounts)
  [ ] Get NPA list from CBS (accounts tagged NPA)
  [ ] Get SMA list (SMA-0, SMA-1, SMA-2) as at 31 March
  [ ] Get provision register (account-wise provision held)
  [ ] Get Interest Suspense account balance
  [ ] Get write-off register (technical + full write-off)

STEP 2 — MANDATORY FULL REVIEW:
  [ ] ALL accounts tagged as NPA in CBS
  [ ] ALL accounts with outstanding >₹1 Crore
  [ ] ALL SMA-2 accounts (most at risk)
  [ ] ALL restructured accounts in monitoring period

STEP 3 — RISK-BASED SAMPLING (Standard accounts):
  [ ] CC/OD accounts where outstanding >90% of DP
  [ ] Accounts in stressed sectors (real estate, infra, gems)
  [ ] Accounts with irregular credits (large year-end credits)
  [ ] Accounts where renewal is overdue by >6 months

STEP 4 — FOR EACH NPA ACCOUNT:
  [ ] Verify Date of NPA per CBS → compute age → confirm sub-classification
  [ ] Cross-default: verify ALL accounts of same borrower are NPA
  [ ] Calculate required provision using scripts/01_npa_provision_calculator.py
  [ ] Compare required vs held → identify shortfall → MOC entry
  [ ] Verify interest reversed / in suspense (no P&L accrual)
  [ ] Check LFAR para I-5: all required comments prepared

STEP 5 — FOR CC/OD ACCOUNTS:
  [ ] Latest stock/debtor statement date → stale if >30 days?
  [ ] Compute DP → compare with outstanding → any excess?
  [ ] If excess >90 days: should be NPA — reclassify in MOC
  [ ] Review account movement: genuine business or circular?

STEP 6 — INCOME REVERSAL VERIFICATION:
  [ ] For newly NPA accounts: interest accrued from NPA date reversed?
  [ ] Interest Suspense account: balance matches unrealised interest?
  [ ] Any income accrual on NPA accounts: flag in MOC

STEP 7 — LARGE NPA ACCOUNTS (>₹1 Crore each):
  [ ] Prepare account-wise analysis for LFAR (Section I-5)
  [ ] For each: outstanding, NPA date, classification, provision, recovery status
  [ ] SARFAESI/DRT/IBC status: documented
  [ ] Provision adequacy: case-by-case assessment
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## EVERGREENING DETECTION PROCEDURE

```
ANALYTICAL PROCEDURES TO DETECT EVERGREENING:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEST 1: CREDIT PATTERN ANALYSIS
  For all CC/OD accounts:
  [ ] Extract last 12 months credit transactions
  [ ] Are credits concentrated near month-end (last 3 working days)?
  [ ] Are credits always just enough to bring balance below DP?
  [ ] Compare credit amounts vs debit amounts → net reduction in balance?
  → If credits only come month-end and immediately followed by debits: suspicious

TEST 2: SOURCE OF CREDITS
  For accounts with suspicious credit pattern:
  [ ] Trace top 5 credit transactions: source account
  [ ] Is source: known supplier/customer or unrelated entity?
  [ ] Related party? Group company? → Round-tripping risk
  [ ] Same amount going out and coming back: classic evergreening

TEST 3: TURNOVER ANALYSIS
  [ ] Total annual credits in CC account vs stated turnover in latest financials
  [ ] Ratio: CC Credits / Stated Revenue should be ~40-60% (varies by industry)
  → If CC credits >> stated revenue: unexplained funds → investigate

TEST 4: LOAN DISBURSEMENT TIMING
  [ ] Any fresh term loan disbursed within 7 days of due date of another loan?
  [ ] Disbursement going to related party account?
  → Request CBS transaction trace: disbursement → intermediate account → repayment

TEST 5: INTEREST-ONLY CREDITS
  [ ] Are some accounts receiving EXACTLY the amount of interest debited?
  → Interest evergreening: paying interest but not principal
  → Not technically NPA but not genuine recovery either → LFAR item
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## ADVANCES SAMPLE SIZE GUIDANCE

```
SAMPLE SELECTION — RISK-BASED APPROACH:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CATEGORY                         | COVERAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
All NPA accounts                 | 100% (no sampling — ALL reviewed)
All SMA-2 accounts               | 100%
All accounts >₹1 Crore           | 100%
Restructured accounts            | 100%
Accounts >₹50L to ₹1Cr          | 50% (risk-based selection)
Accounts >₹10L to ₹50L          | 20-30%
Accounts <₹10L (standard)        | 5-10% (statistical sample)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NOTE: Adjust based on assessed risk. Higher inherent risk = larger sample.
For high-risk branches (GNPA >10%): increase all samples by 50%.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
