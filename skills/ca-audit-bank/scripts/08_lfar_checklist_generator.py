#!/usr/bin/env python3
"""
LFAR (LONG FORM AUDIT REPORT) CHECKLIST GENERATOR
Bank Branch Audit | RBI Circular DOS.CO.PPG./SEC.01/11.01.005/2020-21
ICAI Guidance Note on Audit of Banks (2025 Edition)

Generates branch-specific LFAR questionnaire with status tracking
"""

from datetime import date


def get_input(prompt: str, options: list = None) -> str:
    if options:
        print(f"  {prompt}")
        for i, opt in enumerate(options, 1):
            print(f"    {i}. {opt}")
        choice = input("  Choice: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        return options[0]
    return input(f"  {prompt}: ").strip()


def generate_lfar_checklist():
    SEP = "═" * 76
    THIN = "─" * 76

    print(f"\n{SEP}")
    print("  LFAR CHECKLIST GENERATOR — BRANCH LEVEL")
    print("  RBI Revised LFAR Format | Effective FY 2020-21 onwards")
    print(SEP)

    # Branch profile
    bank = input("  Bank Name: ").strip() or "ABC Bank"
    branch = input("  Branch Name: ").strip() or "Main Branch"
    fy = input("  FY (e.g. 2024-25): ").strip() or "2024-25"

    branch_type = get_input("Branch Type", [
        "General Banking",
        "Large Advance Branch",
        "Forex Branch",
        "Agricultural Branch",
        "MSME Branch",
        "Recovery Branch"
    ])

    has_forex = "Forex" in branch_type or \
                input("  Does branch handle forex? (y/n): ").strip().lower() == 'y'
    has_large_advances = "Large" in branch_type or \
                          input("  Advances >₹25 Crore? (y/n): ").strip().lower() == 'y'

    print(f"\n  Generating LFAR checklist for {branch}...")

    lfar = []

    # ── SECTION I: ADVANCES ──
    lfar.append(("SECTION I: ADVANCES", "HEADING", "", ""))

    lfar += [
        ("I-1a", "Has branch complied with sanction terms and conditions?",
         "Check all loan files: rate of interest, collateral, end-use", ""),
        ("I-1b", "Is credit monitoring and supervision satisfactory?",
         "Follow-up system for overdue accounts; periodic visits to borrowers", ""),
        ("I-1c", "Are adequate records of loan documents maintained?",
         "Document checklist vs actual documents in each file", ""),
        ("I-2a", "Are security documents (mortgage, hypothecation) properly executed?",
         "Check registration, stamp duty, date of execution", ""),
        ("I-2b", "Insurance policies: valid, bank as mortgagee/lossee?",
         "Check expiry, sum insured vs security value", ""),
        ("I-2c", "Stock/debtor statements: received monthly for CC/OD accounts?",
         "Any gaps in submission (month-wise)", ""),
        ("I-2d", "Stock audit conducted for CC/OD above threshold?",
         "Empanelled stock auditor; findings followed up?", ""),
        ("I-2e", "Legal title search within last 3 years?",
         "Property mortgage accounts", ""),
        ("I-2f", "Property valuation within last 3 years by empanelled valuer?",
         "Forced sale value vs market value; valuer credentials", ""),
        ("I-3a", "Annual credit review conducted for all accounts?",
         "Renewal dates, review schedules in place", ""),
        ("I-3b", "Branch visits to borrower premises conducted and documented?",
         "CC/OD accounts especially — stock inspection reports", ""),
        ("I-4a", "Are all NPA accounts correctly classified as at 31 March?",
         "Verify CBS data vs auditor's independent calculation", ""),
        ("I-4b", "Any accounts where auditor disagrees with bank classification?",
         "Document all classification differences with reasons", ""),
        ("I-4c", "SMA-1 and SMA-2 accounts: is enhanced monitoring in place?",
         "CRILC reporting done for eligible accounts (≥₹5Cr)?", ""),
        ("I-4d", "Is provisioning adequate as per RBI IRACP norms?",
         "Compare account-wise required vs held; compute shortfall", ""),
        ("I-4e", "Provision Coverage Ratio (PCR): at or above 70%?",
         "PCR = Provisions/(Gross NPA) × 100; report if <70%", ""),
        ("I-4f", "Unrealised income reversed for all NPA accounts?",
         "Interest Suspense account balance vs unrealised interest", ""),
        ("I-5a", "SARFAESI proceedings: 60-day notices served timely?",
         "Verify notice dates, possession actions, auctions conducted", ""),
        ("I-5b", "DRT/NCLT proceedings: claims filed, status tracked?",
         "List of accounts in legal proceedings with current status", ""),
        ("I-5c", "OTS/compromise settlements: proper approval obtained?",
         "Board/RBI approval where required; documentation in file", ""),
        ("I-5d", "Technically written-off accounts: list maintained?",
         "Recovery proceedings still active; provisions 100%", ""),
        ("I-5e", "Restructured accounts: monitoring period being tracked?",
         "Slippage to NPA during monitoring; provision adequacy", ""),
        ("I-6a", "Any suspected fraud in advance accounts?",
         "Diversion of funds, inflated stocks, multiple financing", ""),
        ("I-6b", "Are FMR filings done timely for detected frauds?",
         "≥₹1Cr within 3 weeks; ≥₹50Cr flash report 24 hours", ""),
        ("I-6c", "Large Exposure Framework (LEF) complied?",
         "Single borrower: 25% of Tier I; Group: 35% of Tier I", ""),
    ]

    if has_large_advances:
        lfar += [
            ("I-LA1", "TEV studies obtained for project finance accounts?",
             "Independent TEV by reputed agency", ""),
            ("I-LA2", "Escrow/Trust & Retention accounts in place for project loans?",
             "Cash flow channelled through dedicated accounts", ""),
            ("I-LA3", "DSRA (Debt Service Reserve Account) maintained?",
             "Verify balance; sufficient to cover next 2 instalments", ""),
            ("I-LA4", "Consortium meetings attended; minutes obtained?",
             "Lead bank sharing of information; common data room", ""),
            ("I-LA5", "Top 10 NPA accounts: detailed case-wise comments prepared?",
             "Status of recovery, provisioning, legal action", ""),
        ]

    # ── SECTION II: LIABILITIES ──
    lfar.append(("SECTION II: LIABILITIES", "HEADING", "", ""))
    lfar += [
        ("II-1a", "Correct interest rates applied on deposits?",
         "CBS rate master vs Board-approved rate card; exceptions?", ""),
        ("II-1b", "Senior citizen differential rate applied correctly?",
         "0.25-0.50% additional rate on FDs; verify in sample", ""),
        ("II-1c", "Dormant/inoperative accounts: operations properly restricted?",
         "2+ years no transaction → activation procedure followed?", ""),
        ("II-1d", "DEAF: unclaimed deposits ≥10 years transferred to RBI?",
         "DEAF transfer certificate obtained; process documented", ""),
        ("II-1e", "TDS compliance: correctly deducted, deposited, returns filed?",
         "TDS @10% on >₹40,000; Form 15G/H; 26Q quarterly filing", ""),
        ("II-1f", "DICGC premium paid timely?",
         "Premium on insured deposits (₹5L per depositor coverage)", ""),
        ("II-2a", "Inter-bank borrowings: properly authorised and accounted?",
         "Verify board/policy limits; interest accrual correct", ""),
        ("II-2b", "Refinance (NABARD/SIDBI/NHB): end-use verified?",
         "Check that refinanced funds deployed for intended purpose", ""),
    ]

    # ── SECTION III: P&L ──
    lfar.append(("SECTION III: PROFIT & LOSS", "HEADING", "", ""))
    lfar += [
        ("III-1a", "Income from NPA accounts: only cash-basis recognised?",
         "No accrual on NPA; Interest Suspense account balance", ""),
        ("III-1b", "Processing fee income: amortised correctly (Ind AS)?",
         "EIR method; processing fee not recognised fully upfront", ""),
        ("III-1c", "Commission on LC/BG: amortised over tenure?",
         "Not recognised upfront; deferred revenue schedule", ""),
        ("III-2a", "All expenses properly authorised per DOA?",
         "Delegation of Authority matrix; unapproved expenses?", ""),
        ("III-2b", "Provisions adequate — NPA, standard assets, depreciation?",
         "IRACP provision compliance; standard asset provision rates", ""),
        ("III-3a", "Suspense account balances: cleared and reconciled?",
         "Age analysis; old debits (potential losses) and credits", ""),
        ("III-3b", "IBR (Inter-Branch Reconciliation): up-to-date?",
         "Old outstanding items >30 days: list and amounts", ""),
    ]

    # ── SECTION IV: GENERAL ──
    lfar.append(("SECTION IV: GENERAL", "HEADING", "", ""))
    lfar += [
        ("IV-1a", "Books of account maintained as per Banking Regulation Act?",
         "Proper day books, ledgers, registers as required", ""),
        ("IV-1b", "CBS data backed up regularly; no manual entries outside CBS?",
         "Any overrides logged; unauthorised manual transactions?", ""),
        ("IV-2a", "Concurrent audit reports: obtained for all 12 months?",
         "Any months without concurrent audit report?", ""),
        ("IV-2b", "Concurrent audit observations: compliance status?",
         "Pending observations list; remediation timeline", ""),
        ("IV-2c", "Prior year LFAR adverse remarks: compliance obtained?",
         "Compare with last year's LFAR; recurring issues?", ""),
        ("IV-2d", "RBI Section 35 inspection observations: complied?",
         "Last inspection date; outstanding observations", ""),
        ("IV-3a", "KYC/AML compliance: all accounts KYC-compliant?",
         "Periodic re-KYC for high-risk/medium-risk accounts", ""),
        ("IV-3b", "Gold loan LTV (Loan-to-Value) maintained ≤75%?",
         "RBI ceiling: 75%; periodic re-valuation of gold", ""),
        ("IV-3c", "Locker operations: rental income, key register, physical verification?",
         "Unclaimed lockers; surrender process; inventory record", ""),
        ("IV-4a", "Fraud register maintained by branch?",
         "All frauds recorded; FMR filings verified", ""),
        ("IV-4b", "List of frauds detected during FY: complete?",
         "Amount, nature, date, FMR status, recovery initiated", ""),
        ("IV-5a", "CRILC reporting: all eligible accounts reported?",
         "SMA-1, SMA-2 with exposure ≥₹5Cr; fortnightly reporting", ""),
        ("IV-5b", "Wilful defaulters: reported to CRILC and credit bureaus?",
         "Legal process followed for wilful defaulter declaration", ""),
        ("IV-6a", "MIS reports to HO: submitted accurately and on time?",
         "Any discrepancies between branch MIS and CBS data?", ""),
    ]

    if has_forex:
        lfar.append(("SECTION V: FOREX (Additional)", "HEADING", "", ""))
        lfar += [
            ("V-1a", "NOSTRO accounts: fully reconciled, stale items cleared?",
             "Items >30 days unreconciled → LFAR adverse comment", ""),
            ("V-1b", "Export bills outstanding >6 months: regularised or reported?",
             "EDPMS reconciliation; FEMA compliance", ""),
            ("V-1c", "Import LC payments made within 6 months?",
             "Overdue import LCs → regularisation or write-off", ""),
            ("V-2a", "PCFC/EPC: interest at RBI-prescribed rates?",
             "Verify rate applied matches RBI circular rates", ""),
            ("V-2b", "Dealing room: front/back office segregation maintained?",
             "Open position limits; stop-loss compliance; deal tickets", ""),
            ("V-2c", "R-returns filed with RBI within due dates?",
             "Monthly/quarterly R-returns; accuracy of reporting", ""),
            ("V-2d", "FEDAI guidelines compliance for foreign exchange?",
             "Card rates, transaction rates within FEDAI guidelines", ""),
        ]

    # ── PRINT CHECKLIST ──
    print(f"\n{SEP}")
    print(f"  LFAR CHECKLIST — {branch.upper()} | {bank.upper()}")
    print(f"  Financial Year: {fy}")
    print(SEP)

    findings = {"YES": 0, "NO": 0, "NA": 0, "PENDING": 0}
    adverse_items = []

    current_section = ""
    for item in lfar:
        ref, question, guidance, status = item

        if "HEADING" in question:
            print(f"\n  {'─'*72}")
            print(f"  {ref}")
            print(f"  {'─'*72}")
            current_section = ref
            continue

        print(f"\n  [{ref}] {question}")
        print(f"  Guidance: {guidance}")

        resp = input("  Status (Y=Yes/Satisfactory, N=No/Adverse, NA=Not Applicable, P=Pending): ").strip().upper()
        if resp not in ["Y", "N", "NA", "P"]:
            resp = "P"

        status_map = {"Y": "YES ✅", "N": "NO ❌", "NA": "N/A", "P": "PENDING ⏳"}
        print(f"  → Status: {status_map.get(resp, resp)}")

        if resp == "N":
            adverse_note = input("  Adverse Observation (brief note for LFAR): ").strip()
            adverse_items.append((ref, question, adverse_note))
            findings["NO"] += 1
        elif resp == "Y":
            findings["YES"] += 1
        elif resp == "NA":
            findings["NA"] += 1
        else:
            findings["PENDING"] += 1

    # ── LFAR SUMMARY ──
    total_items = sum(findings.values())
    print(f"\n{SEP}")
    print("  LFAR COMPLETION SUMMARY")
    print(SEP)
    print(f"  Total items reviewed:    {total_items}")
    print(f"  Satisfactory (Yes):      {findings['YES']}")
    print(f"  Adverse (No):            {findings['NO']}")
    print(f"  Not Applicable:          {findings['NA']}")
    print(f"  Pending:                 {findings['PENDING']}")

    if adverse_items:
        print(f"\n  ADVERSE OBSERVATIONS FOR LFAR:")
        print(f"  {'─'*72}")
        for i, (ref, q, note) in enumerate(adverse_items, 1):
            print(f"\n  {i}. [{ref}] {q}")
            if note:
                print(f"     Observation: {note}")
            print(f"     Status: ADVERSE — Include in LFAR")

        print(f"\n  These {len(adverse_items)} adverse observations must be:")
        print(f"  1. Included in LFAR with specific account details/amounts")
        print(f"  2. Discussed with Branch Head for management response")
        print(f"  3. Material items: included in MOC/Audit Report as well")

    print(f"\n  LFAR DEADLINE: 30th June {fy[-4:]}")
    print(f"  Forward LFAR to: Bank Management AND Statutory Central Auditor (SCA)")


if __name__ == "__main__":
    generate_lfar_checklist()
