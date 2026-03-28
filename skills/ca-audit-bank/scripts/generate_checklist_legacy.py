#!/usr/bin/env python3
"""
Bank Audit Checklist Generator
Generates a customised audit checklist based on branch type and audit scope.
Usage: python3 generate_checklist.py
"""

import json
from datetime import date

def get_branch_type():
    print("\n=== BANK AUDIT CHECKLIST GENERATOR ===")
    print("Based on ICAI Guidance Note on Audit of Banks (2025 Edition)\n")
    
    print("Select Branch Type:")
    print("1. General Banking Branch")
    print("2. Large/Very Large Advance Branch (>₹25 Crore exposure)")
    print("3. Forex Branch")
    print("4. Service Branch / Clearing House")
    print("5. Digital Banking Unit (DBU)")
    print("6. Agricultural / Rural Branch")
    
    choice = input("\nEnter choice (1-6): ").strip()
    
    types = {
        "1": "General Banking Branch",
        "2": "Large/Very Large Advance Branch",
        "3": "Forex Branch", 
        "4": "Service Branch",
        "5": "Digital Banking Unit",
        "6": "Agricultural/Rural Branch"
    }
    return types.get(choice, "General Banking Branch"), choice


def get_audit_parameters():
    print("\n--- Branch Details ---")
    bank_name = input("Bank Name: ").strip() or "[Bank Name]"
    branch_name = input("Branch Name: ").strip() or "[Branch Name]"
    fy = input("Financial Year (e.g., 2024-25): ").strip() or "2024-25"
    total_advances = input("Approximate Total Advances (₹ Crores): ").strip() or "N/A"
    total_deposits = input("Approximate Total Deposits (₹ Crores): ").strip() or "N/A"
    
    return {
        "bank_name": bank_name,
        "branch_name": branch_name,
        "fy": fy,
        "total_advances": total_advances,
        "total_deposits": total_deposits,
        "date": date.today().strftime("%d/%m/%Y")
    }


def generate_checklist(branch_type_name, branch_type_code, params):
    
    # Common checklist items for all branches
    common_items = {
        "Pre-Audit Planning": [
            "Obtain and review prior year Statutory Audit Report and LFAR",
            "Obtain compliance status on prior year LFAR adverse remarks",
            "Obtain Concurrent Audit Reports for all 12 months",
            "Obtain Internal Audit / Inspection Reports",
            "Obtain RBI Section 35 Inspection Report (if any)",
            "Issue Engagement Letter (SA 210)",
            "Assess independence (SA 200/220)",
            "Determine audit materiality (typically 0.5-1% of total advances)",
            "Prepare audit program and allocate to team members",
            "Obtain trial balance / CBS closing balances as at 31 March",
        ],
        "Cash & Physical Verification": [
            "Physical cash count on Day 1 (before opening of vault)",
            "Reconcile physical cash with CBS balance",
            "Verify Cash Retention Limit (CRL) compliance",
            "Report excess cash beyond CRL (if any)",
            "Verify ATM cash balance with ATM custodian report",
            "Verify denomination-wise tally",
            "Check dual custody of vault (two-key system)",
            "Currency chest operations (if applicable)",
            "Check mutilated/soiled note records",
            "Verify cash-in-transit insurance",
        ],
        "Balances with RBI / Other Banks": [
            "Obtain balance confirmation from RBI / SBI / other banks",
            "Reconcile confirmation with CBS balance",
            "Report unreconciled items >30 days in LFAR",
            "Verify CRR compliance (currently 4% of NDTL)",
            "Verify SLR compliance (currently 18% of NDTL)",
            "Reconcile inter-branch accounts (IBA)",
        ],
        "Investments": [
            "Obtain investment schedule (HTM/AFS/HFT category-wise)",
            "Verify physical holdings / SGL/CSGL confirmation from RBI",
            "Verify HTM valuation: amortised cost",
            "Verify AFS valuation: LOCOM (lower of cost or market value)",
            "Verify HFT valuation: daily MTM",
            "Check for NPI (Non-Performing Investments)",
            "Verify SLR compliance using investment data",
            "Check inter-category transfer approvals",
        ],
        "Advances — Documentation": [
            "Obtain complete list of advances from CBS",
            "Select sample of loan accounts for verification",
            "Verify sanction letter in each file",
            "Verify DOA (Discretionary Powers) compliance",
            "Check security documents: title deed, mortgage/hypothecation",
            "Verify insurance policies (valid, bank as mortgagee)",
            "Check stock/debtors statements for CC/OD accounts",
            "Verify stock audit reports (if applicable)",
            "Check legal opinion on property title (within 3 years)",
            "Verify property valuation (within 3 years, empanelled valuer)",
            "Check latest audited financials of borrower",
            "Verify credit ratings (CRISIL/ICRA/CARE) where applicable",
        ],
        "Advances — NPA Verification": [
            "Obtain CBS-generated NPA list as at 31 March",
            "Obtain bank's manual NPA classification list",
            "Cross-verify both lists for discrepancies",
            "Verify date of NPA for each account independently",
            "Verify correct sub-classification (Sub-std/D1/D2/D3/Loss)",
            "Compute required provision and compare with held provision",
            "Verify income reversal on accounts newly classified as NPA",
            "Check cross-default rule: all facilities of NPA borrower classified as NPA",
            "Identify 'out-of-order' accounts not classified as NPA",
            "Check Drawing Power (DP) vs outstanding for CC/OD accounts",
            "Verify stagnant accounts with no credits for 90 days",
            "Verify CRILC reporting for accounts >=₹5 crore",
            "Check SARFAESI proceedings for eligible NPA accounts",
            "Verify collateral valuation for doubtful accounts (within 3 years)",
            "Prepare MOC for all classification disagreements",
        ],
        "Deposits & Liabilities": [
            "Reconcile total deposits with CBS",
            "Verify interest rates applied vs rate card",
            "Check EBLR compliance for floating rate deposits",
            "Verify senior citizen differential interest correctly applied",
            "Check TDS deduction on interest >₹40,000 / ₹50,000",
            "Verify Form 15G/15H received and correctly processed",
            "Check TDS deposit within 7 days of deduction",
            "Verify Form 26Q (TDS return) filed quarterly on time",
            "Check dormant/inoperative accounts: KYC refresh done?",
            "Verify DEAF transfer for unclaimed deposits (10+ years)",
            "Check PMJDY accounts: zero balance compliance",
            "Verify FCNR(B)/NRE/NRO accounts: repatriation norms",
        ],
        "Profit & Loss Account": [
            "Verify no interest accrual on NPA accounts",
            "Verify unrealised income reversed on NPA",
            "Verify commission / fee income accounted correctly",
            "Verify interest on deposits: correct rates x balances",
            "Verify staff expense: payroll reconciliation, PF/gratuity",
            "Verify all provisions: NPA, standard assets, depreciation",
            "Verify rent and utilities: supported by agreements and bills",
            "Analytical review: NII vs prior year (significant variances?)",
        ],
        "Off-Balance Sheet / Contingent Liabilities": [
            "Reconcile BG register with CBS",
            "Verify BGs: expiry dates, invocations, provisions",
            "Reconcile LC register with CBS",
            "Verify LC devolvements: classified as advances?",
            "Forward exchange contracts: MTM, limits observed",
            "Disclosure of contingent liabilities in notes to accounts",
        ],
        "Suspense & Reconciliation": [
            "Obtain schedule of all suspense/sundry accounts",
            "Verify all entries >30 days — explained?",
            "Report unreconciled entries in LFAR",
            "Check inter-branch account reconciliation",
            "ATM suspense account reconciliation",
            "Government transaction accounts: reconciled?",
            "Red flag: debit entries to suspense to avoid NPA recognition",
        ],
        "KYC / AML Compliance": [
            "Verify KYC for new accounts opened during FY",
            "Check CDD / EDD records for high-risk customers",
            "Verify PEP accounts: enhanced monitoring in place",
            "CTR filings: cash transactions >₹10 lakhs reported to FIU-IND",
            "STR filings: suspicious transactions reported timely",
            "Non-KYC compliant accounts: operations restricted per RBI",
        ],
        "Reporting & LFAR": [
            "Prepare draft LFAR (Section I to IV)",
            "Prepare MOC with all disagreements",
            "Discuss LFAR and MOC with Branch Manager",
            "Obtain management comments on LFAR",
            "Prepare NPA Certificate",
            "Obtain Management Representation Letter (SA 580)",
            "Prepare Statutory Audit Report (SA 700 format)",
            "Obtain all required certificates per appointment letter",
            "Finalise Audit Report and sign with UDIN",
            "Submit LFAR by June 30",
        ],
    }
    
    # Branch-type specific items
    additional_items = {}
    
    if branch_type_code == "3":  # Forex
        additional_items["Forex Specific Checks"] = [
            "Reconcile NOSTRO accounts: stale items reported",
            "Verify PCFC/EPC interest rates per RBI guidelines",
            "Check export bills: outstanding >6 months regularised or reported",
            "Verify import LC payments within FEMA time limits",
            "Check EEFC/RFC accounts: FEMA compliance",
            "Verify dealing room: stop-loss limits, front/back office segregation",
            "SWIFT controls: dual authorization, confirmation process",
            "Verify FEDAI guidelines compliance",
            "Forward contracts: MTM daily, limits observed",
        ]
    
    if branch_type_code == "2":  # Large Advance
        additional_items["Large Advance Specific Checks"] = [
            "TEV/DPR studies for all project loans",
            "DSRA (Debt Service Reserve Account) maintenance verified",
            "Consortium documentation: NOC from lead bank",
            "Top 10 NPA accounts: detailed analysis in LFAR",
            "IBC/NCLT proceedings: status and provisioning",
            "ICA (Inter-Creditor Agreement) compliance for stressed accounts",
            "Large Exposure Framework (LEF): single/group limits respected",
        ]
    
    if branch_type_code == "6":  # Agriculture
        additional_items["Agricultural Specific Checks"] = [
            "KCC portfolio: annual review/renewal done?",
            "Crop insurance: PMFBY enrolment and claims",
            "Agricultural NPA: seasonal norms applied correctly",
            "SF/MF identification: Udyam / land records verified",
            "PACS linkage: documentation complete",
            "Government waiver schemes: accounting correct",
            "SHG loans: RBI documentation norms met",
        ]
    
    if branch_type_code == "5":  # DBU
        additional_items["Digital Banking Unit Checks"] = [
            "Digital lending: LSP agreements with RBI",
            "KFS (Key Fact Statement) issued for all digital loans",
            "Loan disbursement: directly to borrower account",
            "No automatic credit increase without explicit consent",
            "RBI Digital Lending Guidelines (Sep 2022) compliance",
            "Grievance redressal mechanism: in place and functional",
            "Cyber security: incidents during FY reported?",
        ]
    
    return {**common_items, **additional_items}


def print_checklist(branch_type_name, params, checklist):
    output = []
    output.append("=" * 70)
    output.append("BANK AUDIT CHECKLIST")
    output.append("=" * 70)
    output.append(f"Bank: {params['bank_name']}")
    output.append(f"Branch: {params['branch_name']}")
    output.append(f"Branch Type: {branch_type_name}")
    output.append(f"Financial Year: {params['fy']}")
    output.append(f"Total Advances: ₹{params['total_advances']} Crores")
    output.append(f"Total Deposits: ₹{params['total_deposits']} Crores")
    output.append(f"Generated on: {params['date']}")
    output.append(f"Framework: ICAI Guidance Note on Audit of Banks (2025 Edition)")
    output.append("=" * 70)
    output.append("")
    
    total_items = 0
    for section, items in checklist.items():
        output.append(f"\n{'─' * 60}")
        output.append(f"  {section.upper()}")
        output.append(f"{'─' * 60}")
        for i, item in enumerate(items, 1):
            output.append(f"  [ ] {i:2d}. {item}")
            total_items += 1
    
    output.append("\n" + "=" * 70)
    output.append(f"TOTAL CHECKLIST ITEMS: {total_items}")
    output.append("=" * 70)
    output.append("\nKEY DEADLINES:")
    output.append("→ Audit Report Submission: Typically April 30")
    output.append("→ LFAR Submission: June 30")
    output.append("→ All Certificates: As per appointment letter")
    output.append("\nGenerated using Bank Audit Skill | ICAI GN 2025 | CA Use Only")
    
    return "\n".join(output)


def save_checklist(output, params):
    filename = f"bank_audit_checklist_{params['branch_name'].replace(' ', '_')}_{params['fy']}.txt"
    filename = filename.replace("/", "-")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(output)
    
    print(f"\n✅ Checklist saved to: {filename}")
    return filename


def main():
    branch_type_name, branch_type_code = get_branch_type()
    params = get_audit_parameters()
    checklist = generate_checklist(branch_type_name, branch_type_code, params)
    output = print_checklist(branch_type_name, params, checklist)
    
    print("\n" + output)
    
    save = input("\n\nSave checklist to file? (y/n): ").strip().lower()
    if save == 'y':
        filename = save_checklist(output, params)
        print(f"File saved. You can print or share: {filename}")
    
    print("\n✅ Bank Audit Checklist generated successfully.")
    print("Refer to SKILL.md references/ folder for detailed guidance on each area.")


if __name__ == "__main__":
    main()
