#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════╗
║           COMPREHENSIVE BANK AUDIT CALCULATOR SUITE                      ║
║           NPA Provision Calculator | ICAI GN 2025 | RBI IRACP Norms     ║
║           Version 3.0 | FY 2024-25                                       ║
╚══════════════════════════════════════════════════════════════════════════╝

Features:
  1. NPA Provision Calculator (account-wise + portfolio)
  2. Drawing Power Calculator (CC/OD accounts)
  3. SMA Classification Tool
  4. PCR (Provision Coverage Ratio) Calculator
  5. MOC Summary Generator
  6. LFAR NPA Section Auto-fill
  7. IBC/NCLT Provision Calculator
  8. Export to text report

Usage: python3 01_npa_provision_calculator.py
"""

import json
from datetime import date, datetime, timedelta
from typing import Optional

# ══════════════════════════════════════════════════════
# CONSTANTS — RBI IRACP NORMS FY 2024-25
# ══════════════════════════════════════════════════════

PROVISION_RATES = {
    "Sub-Standard":   {"secured": 0.15, "unsecured": 0.25},
    "Doubtful-1":     {"secured": 0.25, "unsecured": 1.00},
    "Doubtful-2":     {"secured": 0.40, "unsecured": 1.00},
    "Doubtful-3":     {"secured": 1.00, "unsecured": 1.00},
    "Loss":           {"secured": 1.00, "unsecured": 1.00},
}

STANDARD_ASSET_RATES = {
    "Agriculture/SME":                0.0025,
    "Other Standard":                 0.0040,
    "CRE (Commercial Real Estate)":   0.0100,
    "CRE Residential":                0.0075,
    "Restructured Standard":          0.0500,
    "Teaser Home Loans":              0.0200,
}

IBC_PROVISION_RATES = {
    "CIRP Admitted (List 1 — <180d)":  0.50,
    "CIRP Admitted (List 2 — >180d)":  1.00,
    "Resolution Plan Approved":        "Haircut %",
    "Liquidation Ordered":             1.00,
}

SEPARATOR = "═" * 72
THIN_SEP = "─" * 72


# ══════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ══════════════════════════════════════════════════════

def print_banner():
    print(f"\n{SEPARATOR}")
    print("  BANK AUDIT — NPA PROVISION & CLASSIFICATION CALCULATOR")
    print("  ICAI Guidance Note on Audit of Banks (2025 Edition)")
    print("  RBI IRACP Norms | FY 2024-25")
    print(SEPARATOR)

def get_float(prompt: str, default: float = 0.0) -> float:
    """Safe float input with default."""
    try:
        val = input(f"  {prompt} [{default}]: ").strip()
        return float(val) if val else default
    except ValueError:
        print("  ⚠  Invalid input. Using default.")
        return default

def get_date(prompt: str) -> Optional[date]:
    """Get date input in DD/MM/YYYY format."""
    val = input(f"  {prompt} (DD/MM/YYYY, or Enter to skip): ").strip()
    if not val:
        return None
    try:
        return datetime.strptime(val, "%d/%m/%Y").date()
    except ValueError:
        print("  ⚠  Invalid date format. Skipping.")
        return None

def classify_npa_by_date(npa_date: date, as_of_date: date = None) -> str:
    """Auto-classify NPA based on date of NPA."""
    if as_of_date is None:
        as_of_date = date.today()
    months_as_npa = (as_of_date - npa_date).days / 30.44
    if months_as_npa <= 12:
        return "Sub-Standard"
    elif months_as_npa <= 24:
        return "Doubtful-1"
    elif months_as_npa <= 36:
        return "Doubtful-2"
    else:
        return "Doubtful-3"

def classify_sma(days_overdue: int) -> str:
    """Classify SMA based on days overdue."""
    if days_overdue <= 0:
        return "Standard (Regular)"
    elif days_overdue <= 30:
        return "SMA-0"
    elif days_overdue <= 60:
        return "SMA-1"
    elif days_overdue <= 90:
        return "SMA-2"
    else:
        return "NPA (>90 days)"

def calculate_provision(outstanding: float, security_value: float, 
                         classification: str) -> dict:
    """Calculate NPA provision as per RBI IRACP norms."""
    rates = PROVISION_RATES[classification]
    secured_portion = min(outstanding, security_value)
    unsecured_portion = outstanding - secured_portion
    
    prov_secured = secured_portion * rates["secured"]
    prov_unsecured = unsecured_portion * rates["unsecured"]
    total_required = prov_secured + prov_unsecured
    
    return {
        "outstanding": outstanding,
        "security_value": security_value,
        "secured_portion": secured_portion,
        "unsecured_portion": unsecured_portion,
        "secured_rate": rates["secured"],
        "unsecured_rate": rates["unsecured"],
        "prov_secured": prov_secured,
        "prov_unsecured": prov_unsecured,
        "total_required": total_required,
    }


# ══════════════════════════════════════════════════════
# MODULE 1: NPA PROVISION CALCULATOR
# ══════════════════════════════════════════════════════

def npa_provision_calculator():
    print(f"\n{'━'*72}")
    print("  MODULE 1: NPA PROVISION CALCULATOR")
    print("  Per RBI IRACP Norms — Account-by-Account Analysis")
    print(f"{'━'*72}")
    
    audit_date = date(date.today().year, 3, 31)
    print(f"\n  Audit Date: 31 March {audit_date.year}")
    
    accounts = []
    
    while True:
        print(f"\n  {'─'*60}")
        print(f"  ACCOUNT {len(accounts) + 1}")
        print(f"  {'─'*60}")
        
        account_no = input("  Account Number: ").strip() or f"ACC-{len(accounts)+1:03d}"
        name = input("  Borrower Name: ").strip() or "Unknown Borrower"
        account_type = input("  Account Type (CC/TL/OD/Bills/Agri): ").strip().upper() or "TL"
        
        # NPA Classification
        print("\n  NPA Classification Method:")
        print("  1. Enter classification manually")
        print("  2. Auto-classify by Date of NPA")
        classify_method = input("  Choice [1/2]: ").strip()
        
        if classify_method == "2":
            npa_date = get_date("Date of NPA")
            if npa_date:
                auto_class = classify_npa_by_date(npa_date, audit_date)
                days_npa = (audit_date - npa_date).days
                print(f"\n  ✅ Auto-classified: {auto_class}")
                print(f"     (NPA for {days_npa} days / {days_npa/30.44:.1f} months)")
                classification = auto_class
            else:
                classification = "Sub-Standard"
        else:
            print("\n  Classification:")
            classes = list(PROVISION_RATES.keys())
            for i, c in enumerate(classes, 1):
                print(f"  {i}. {c}")
            choice = input("  Select [1-5]: ").strip()
            classification = classes[int(choice)-1] if choice.isdigit() and 1 <= int(choice) <= 5 else "Sub-Standard"
        
        # Financial data
        print()
        outstanding = get_float("Outstanding Balance (₹ Lakhs)")
        security_value = get_float("Realisable Value of Security (₹ Lakhs, 0 if unsecured)")
        existing_provision = get_float("Existing Provision Held by Bank (₹ Lakhs)")
        unrealised_interest = get_float("Unrealised Interest NOT yet reversed (₹ Lakhs)", 0)
        
        # Additional info for LFAR
        is_ibc = input("  Is this account under IBC/NCLT? (y/n): ").strip().lower() == 'y'
        ibc_stage = ""
        if is_ibc:
            ibc_stages = list(IBC_PROVISION_RATES.keys())
            print("\n  IBC Stage:")
            for i, s in enumerate(ibc_stages, 1):
                print(f"  {i}. {s}")
            stage_choice = input("  Select: ").strip()
            if stage_choice.isdigit() and 1 <= int(stage_choice) <= len(ibc_stages):
                ibc_stage = ibc_stages[int(stage_choice)-1]
        
        # Calculate provision
        calc = calculate_provision(outstanding, security_value, classification)
        total_required = calc["total_required"]
        
        # IBC additional check
        ibc_provision = 0
        if is_ibc and ibc_stage in IBC_PROVISION_RATES:
            rate = IBC_PROVISION_RATES[ibc_stage]
            if isinstance(rate, float):
                ibc_provision = outstanding * rate
                total_required = max(total_required, ibc_provision)
        
        shortfall = max(0, total_required - existing_provision)
        excess = max(0, existing_provision - total_required)
        
        # Display result
        print(f"\n  {'─'*60}")
        print(f"  PROVISION ANALYSIS: {name} ({account_no})")
        print(f"  {'─'*60}")
        print(f"  Classification:          {classification}")
        print(f"  Outstanding Balance:     ₹{outstanding:>10.2f} Lakhs")
        print(f"  Security Value:          ₹{security_value:>10.2f} Lakhs")
        print(f"  Secured Portion:         ₹{calc['secured_portion']:>10.2f} Lakhs  @ {calc['secured_rate']*100:.0f}%")
        print(f"  Unsecured Portion:       ₹{calc['unsecured_portion']:>10.2f} Lakhs  @ {calc['unsecured_rate']*100:.0f}%")
        print(f"  Provision on Secured:    ₹{calc['prov_secured']:>10.2f} Lakhs")
        print(f"  Provision on Unsecured:  ₹{calc['prov_unsecured']:>10.2f} Lakhs")
        if is_ibc and ibc_provision > 0:
            print(f"  IBC Minimum Provision:   ₹{ibc_provision:>10.2f} Lakhs")
        print(f"  {'─'*42}")
        print(f"  TOTAL REQUIRED:          ₹{total_required:>10.2f} Lakhs")
        print(f"  EXISTING (Bank):         ₹{existing_provision:>10.2f} Lakhs")
        
        if shortfall > 0:
            print(f"  ⚠  SHORTFALL:            ₹{shortfall:>10.2f} Lakhs  ← MOC ENTRY")
            if unrealised_interest > 0:
                print(f"  ⚠  INTEREST REVERSAL:   ₹{unrealised_interest:>10.2f} Lakhs  ← MOC ENTRY")
        elif excess > 0:
            print(f"  ✅ Excess Provision:     ₹{excess:>10.2f} Lakhs")
        else:
            print(f"  ✅ Provision ADEQUATE")
        
        account_data = {
            "account_no": account_no,
            "name": name,
            "account_type": account_type,
            "classification": classification,
            "outstanding": outstanding,
            "security_value": security_value,
            "secured_portion": calc["secured_portion"],
            "unsecured_portion": calc["unsecured_portion"],
            "prov_secured": calc["prov_secured"],
            "prov_unsecured": calc["prov_unsecured"],
            "total_required": total_required,
            "existing_provision": existing_provision,
            "unrealised_interest": unrealised_interest,
            "shortfall": shortfall,
            "excess": excess,
            "is_ibc": is_ibc,
            "ibc_stage": ibc_stage,
        }
        accounts.append(account_data)
        
        more = input("\n  Add another account? (y/n): ").strip().lower()
        if more != 'y':
            break
    
    # ── PORTFOLIO SUMMARY ──
    if not accounts:
        print("  No accounts entered.")
        return accounts
    
    print(f"\n{SEPARATOR}")
    print("  NPA PORTFOLIO SUMMARY — PROVISION ANALYSIS")
    print(f"  As at 31 March {audit_date.year}")
    print(SEPARATOR)
    
    # Classification-wise summary
    class_summary = {}
    for acc in accounts:
        cls = acc["classification"]
        if cls not in class_summary:
            class_summary[cls] = {"count": 0, "outstanding": 0, "required": 0, "held": 0, "shortfall": 0}
        class_summary[cls]["count"] += 1
        class_summary[cls]["outstanding"] += acc["outstanding"]
        class_summary[cls]["required"] += acc["total_required"]
        class_summary[cls]["held"] += acc["existing_provision"]
        class_summary[cls]["shortfall"] += acc["shortfall"]
    
    print(f"\n  {'Classification':<16} {'Accounts':>8} {'O/s (₹L)':>12} {'Req.(₹L)':>12} {'Held(₹L)':>12} {'Shortfall':>12}")
    print(f"  {THIN_SEP}")
    
    total_os = total_req = total_held = total_short = 0
    for cls, data in class_summary.items():
        print(f"  {cls:<16} {data['count']:>8} {data['outstanding']:>12.2f} "
              f"{data['required']:>12.2f} {data['held']:>12.2f} {data['shortfall']:>12.2f}")
        total_os += data['outstanding']
        total_req += data['required']
        total_held += data['held']
        total_short += data['shortfall']
    
    print(f"  {THIN_SEP}")
    total_count = len(accounts)
    print(f"  {'TOTAL':<16} {total_count:>8} {total_os:>12.2f} "
          f"{total_req:>12.2f} {total_held:>12.2f} {total_short:>12.2f}")
    
    # PCR
    pcr = (total_held / total_os * 100) if total_os > 0 else 0
    provision_ratio = (total_held / total_req * 100) if total_req > 0 else 0
    
    print(f"\n  KEY METRICS:")
    print(f"  Gross NPA Outstanding:              ₹{total_os:>10.2f} Lakhs")
    print(f"  Total Provision Required:           ₹{total_req:>10.2f} Lakhs")
    print(f"  Total Provision Held:               ₹{total_held:>10.2f} Lakhs")
    print(f"  TOTAL PROVISION SHORTFALL (MOC):    ₹{total_short:>10.2f} Lakhs")
    print(f"  Provision Coverage Ratio (PCR):     {pcr:>10.1f}%  {'✅' if pcr >= 70 else '⚠  BELOW 70% RBI MIN'}")
    
    # Total interest reversal
    total_interest_reversal = sum(a["unrealised_interest"] for a in accounts)
    if total_interest_reversal > 0:
        print(f"  Total Interest Reversal Required:   ₹{total_interest_reversal:>10.2f} Lakhs")
    
    # MOC Summary
    print(f"\n  MOC ENTRIES REQUIRED:")
    moc_items = [a for a in accounts if a["shortfall"] > 0 or a["unrealised_interest"] > 0]
    if moc_items:
        print(f"\n  {'A/c No.':<14} {'Name':<22} {'Class':<14} {'Prov Short':>12} {'Int.Rev':>10}")
        print(f"  {THIN_SEP}")
        for acc in moc_items:
            print(f"  {acc['account_no']:<14} {acc['name'][:20]:<22} {acc['classification']:<14} "
                  f"{acc['shortfall']:>12.2f} {acc['unrealised_interest']:>10.2f}")
        print(f"  {THIN_SEP}")
        total_moc = sum(a["shortfall"] for a in moc_items)
        total_int_rev = sum(a["unrealised_interest"] for a in moc_items)
        print(f"  {'TOTAL MOC IMPACT':<52} {total_moc:>12.2f} {total_int_rev:>10.2f}")
        print(f"\n  TOTAL P&L IMPACT (Debit): ₹{total_moc + total_int_rev:.2f} Lakhs")
    else:
        print("  ✅ No MOC entries required — provisions are adequate")
    
    # LFAR note
    print(f"\n  LFAR NOTE:")
    print(f"  Use these figures to fill LFAR Section I-5 (NPA) for the branch.")
    print(f"  PCR of {pcr:.1f}% {'meets' if pcr >= 70 else 'DOES NOT MEET'} RBI minimum of 70%.")
    
    return accounts


# ══════════════════════════════════════════════════════
# MODULE 2: DRAWING POWER CALCULATOR
# ══════════════════════════════════════════════════════

def drawing_power_calculator():
    print(f"\n{'━'*72}")
    print("  MODULE 2: DRAWING POWER (DP) CALCULATOR")
    print("  For Cash Credit / Overdraft Accounts")
    print(f"{'━'*72}")
    
    print("\n  Enter details for CC/OD account:")
    account_no = input("  Account Number: ").strip() or "CC-001"
    name = input("  Borrower Name: ").strip() or "Borrower"
    sanctioned_limit = get_float("Sanctioned CC/OD Limit (₹ Lakhs)")
    
    # Stock Statement
    print(f"\n  STOCK STATEMENT:")
    stock_date_raw = input("  Stock Statement Date (DD/MM/YYYY): ").strip()
    try:
        stock_date = datetime.strptime(stock_date_raw, "%d/%m/%Y").date()
        days_old = (date.today() - stock_date).days
        if days_old > 90:
            print(f"  ❌ CRITICAL: Stock statement is {days_old} days old (>90 days)")
            print(f"     Consider treating DP as NIL per conservative approach")
        elif days_old > 30:
            print(f"  ⚠  WARNING: Stock statement is {days_old} days old (>30 days)")
            print(f"     Previous DP should be used per RBI guidelines")
        else:
            print(f"  ✅ Stock statement is {days_old} days old (within 30 days)")
    except:
        days_old = 999
        print("  ⚠  Invalid date — treating as stale statement")
    
    # Stock details
    print(f"\n  STOCK COMPONENTS (as per stock statement):")
    raw_material = get_float("Raw Material (₹ Lakhs)")
    wip = get_float("Work in Progress / WIP (₹ Lakhs)")
    finished_goods = get_float("Finished Goods (₹ Lakhs)")
    other_stock = get_float("Other Stock (Packing material etc.) (₹ Lakhs)")
    
    print(f"\n  MARGIN RATES (per sanction terms / bank policy):")
    margin_rm = get_float("Margin on Raw Material (%)", 25) / 100
    margin_wip = get_float("Margin on WIP (%)", 50) / 100
    margin_fg = get_float("Margin on Finished Goods (%)", 25) / 100
    margin_other = get_float("Margin on Other Stock (%)", 25) / 100
    
    print(f"\n  BOOK DEBTS:")
    debtors_lt90 = get_float("Debtors < 90 days (₹ Lakhs)")
    debtors_90_180 = get_float("Debtors 90-180 days (₹ Lakhs)")
    debtors_gt180 = get_float("Debtors > 180 days (₹ Lakhs)")
    margin_debtors = get_float("Margin on Eligible Debtors (%)", 40) / 100
    eligible_debtors_limit = get_float("Maximum eligible debtors (if capped in sanction, else 0)")
    
    print(f"\n  CREDITORS:")
    creditors = get_float("Outstanding Creditors (₹ Lakhs)")
    
    print(f"\n  CURRENT ACCOUNT:")
    current_outstanding = get_float("Current Outstanding Balance in CC Account (₹ Lakhs)")
    
    # CALCULATION
    # Eligible items per standard sanction terms
    eligible_rm = raw_material * (1 - margin_rm)
    eligible_wip = wip * (1 - margin_wip)
    eligible_fg = finished_goods * (1 - margin_fg)
    eligible_other = other_stock * (1 - margin_other)
    
    # Debtors: only <90 days eligible (per standard RBI norms)
    eligible_debtors_raw = debtors_lt90 * (1 - margin_debtors)
    if eligible_debtors_limit > 0:
        eligible_debtors = min(eligible_debtors_raw, eligible_debtors_limit * (1 - margin_debtors))
    else:
        eligible_debtors = eligible_debtors_raw
    
    ineligible_debtors = (debtors_90_180 + debtors_gt180)
    
    # DP Calculation
    dp_before_limit = eligible_rm + eligible_wip + eligible_fg + eligible_other + eligible_debtors - creditors
    drawing_power = min(max(dp_before_limit, 0), sanctioned_limit)
    
    # Analysis
    excess_outstanding = max(0, current_outstanding - drawing_power)
    excess_over_limit = max(0, current_outstanding - sanctioned_limit)
    
    print(f"\n{SEPARATOR}")
    print(f"  DRAWING POWER CALCULATION — {name} ({account_no})")
    print(SEPARATOR)
    print(f"\n  STOCK ANALYSIS:")
    print(f"  Raw Material:       ₹{raw_material:>8.2f}L  × (1-{margin_rm*100:.0f}%) = ₹{eligible_rm:>8.2f}L eligible")
    print(f"  WIP:                ₹{wip:>8.2f}L  × (1-{margin_wip*100:.0f}%) = ₹{eligible_wip:>8.2f}L eligible")
    print(f"  Finished Goods:     ₹{finished_goods:>8.2f}L  × (1-{margin_fg*100:.0f}%) = ₹{eligible_fg:>8.2f}L eligible")
    print(f"  Other Stock:        ₹{other_stock:>8.2f}L  × (1-{margin_other*100:.0f}%) = ₹{eligible_other:>8.2f}L eligible")
    total_stock = raw_material + wip + finished_goods + other_stock
    total_eligible_stock = eligible_rm + eligible_wip + eligible_fg + eligible_other
    print(f"  Total Stock:        ₹{total_stock:>8.2f}L  ─►  Eligible: ₹{total_eligible_stock:.2f}L")
    
    print(f"\n  DEBTORS ANALYSIS:")
    print(f"  < 90 days (eligible):  ₹{debtors_lt90:>8.2f}L  × (1-{margin_debtors*100:.0f}%) = ₹{eligible_debtors:>8.2f}L")
    print(f"  90-180 days (inelig.): ₹{debtors_90_180:>8.2f}L  (NOT ELIGIBLE — >90 days)")
    print(f"  > 180 days (inelig.):  ₹{debtors_gt180:>8.2f}L  (NOT ELIGIBLE — Doubtful)")
    
    print(f"\n  DP COMPUTATION:")
    print(f"  + Eligible Stock:       ₹{total_eligible_stock:>10.2f} Lakhs")
    print(f"  + Eligible Debtors:     ₹{eligible_debtors:>10.2f} Lakhs")
    print(f"  - Creditors:            ₹{creditors:>10.2f} Lakhs")
    print(f"  {THIN_SEP[:42]}")
    print(f"  = DP before limit:      ₹{dp_before_limit:>10.2f} Lakhs")
    print(f"  Sanctioned Limit:       ₹{sanctioned_limit:>10.2f} Lakhs")
    print(f"  {'─'*42}")
    print(f"  DRAWING POWER (DP):     ₹{drawing_power:>10.2f} Lakhs")
    
    print(f"\n  ACCOUNT STATUS:")
    print(f"  Current Outstanding:    ₹{current_outstanding:>10.2f} Lakhs")
    print(f"  Drawing Power:          ₹{drawing_power:>10.2f} Lakhs")
    
    if excess_over_limit > 0:
        print(f"  ❌ Excess over Limit:  ₹{excess_over_limit:>10.2f} Lakhs  ← IRREGULAR")
    elif excess_outstanding > 0:
        print(f"  ⚠  Excess over DP:    ₹{excess_outstanding:>10.2f} Lakhs")
        print(f"     If excess > 90 days continuously → NPA!")
    else:
        print(f"  ✅ Outstanding is within Drawing Power")
    
    utilisation = (current_outstanding / drawing_power * 100) if drawing_power > 0 else 999
    print(f"  DP Utilisation:         {utilisation:>10.1f}%")
    
    if days_old > 30:
        print(f"\n  ⚠  IMPORTANT: Stock statement is {days_old} days old.")
        print(f"     DP calculation above is for reference only.")
        print(f"     Actual applicable DP should use previous valid statement.")
    
    print(f"\n  INELIGIBLE ASSETS (Note for LFAR):")
    print(f"  Old Debtors (90-180 days): ₹{debtors_90_180:.2f}L")
    print(f"  Very Old Debtors (>180d):  ₹{debtors_gt180:.2f}L")
    print(f"  WIP at conservative rate:  (check sanction — some banks exclude WIP)")
    
    print(f"\n  LFAR NOTE (if applicable):")
    if excess_outstanding > 0:
        print(f"  \"Account No. {account_no} ({name}): Outstanding ₹{current_outstanding:.2f}L exceeds")
        print(f"  Drawing Power ₹{drawing_power:.2f}L by ₹{excess_outstanding:.2f}L.")
        print(f"  Check if excess persists >90 days — may require NPA classification.\"")


# ══════════════════════════════════════════════════════
# MODULE 3: SMA CLASSIFICATION TOOL
# ══════════════════════════════════════════════════════

def sma_classification_tool():
    print(f"\n{'━'*72}")
    print("  MODULE 3: SMA CLASSIFICATION & CRILC REPORTING TOOL")
    print(f"{'━'*72}")
    
    print("\n  Enter account details:")
    accounts = []
    
    while True:
        print(f"\n  Account {len(accounts)+1}:")
        acc_no = input("  Account Number: ").strip() or f"A{len(accounts)+1:03d}"
        name = input("  Borrower Name: ").strip() or "Borrower"
        outstanding = get_float("Outstanding (₹ Lakhs)")
        exposure = get_float("Total Exposure to Borrower (₹ Lakhs, for CRILC check)")
        days_overdue = int(get_float("Days Overdue (0 if regular)"))
        
        sma_class = classify_sma(days_overdue)
        crilc_required = exposure >= 500  # ₹5 Crore = ₹500 Lakhs
        
        accounts.append({
            "acc_no": acc_no,
            "name": name,
            "outstanding": outstanding,
            "exposure": exposure,
            "days_overdue": days_overdue,
            "sma_class": sma_class,
            "crilc_required": crilc_required,
        })
        
        print(f"\n  Classification: {sma_class}")
        if crilc_required and sma_class in ["SMA-1", "SMA-2"]:
            print(f"  ⚠  CRILC REPORTING REQUIRED (exposure ≥₹5 Crore, {sma_class})")
        
        more = input("\n  Add another? (y/n): ").strip().lower()
        if more != 'y':
            break
    
    print(f"\n{SEPARATOR}")
    print("  SMA SUMMARY")
    print(SEPARATOR)
    print(f"\n  {'A/c No.':<12} {'Name':<22} {'O/s (₹L)':>10} {'Days':>6} {'Class':<12} {'CRILC'}")
    print(f"  {THIN_SEP}")
    
    for acc in accounts:
        crilc_flag = "⚠ YES" if acc["crilc_required"] and acc["sma_class"] in ["SMA-1", "SMA-2"] else ""
        print(f"  {acc['acc_no']:<12} {acc['name'][:20]:<22} {acc['outstanding']:>10.2f} "
              f"{acc['days_overdue']:>6} {acc['sma_class']:<12} {crilc_flag}")
    
    crilc_accounts = [a for a in accounts if a["crilc_required"] and 
                      a["sma_class"] in ["SMA-1", "SMA-2"]]
    if crilc_accounts:
        print(f"\n  ⚠  {len(crilc_accounts)} account(s) require CRILC reporting (exposure ≥₹5Cr):")
        for acc in crilc_accounts:
            print(f"     → {acc['acc_no']} | {acc['name']} | {acc['sma_class']} | Exposure: ₹{acc['exposure']:.2f}L")
    
    return accounts


# ══════════════════════════════════════════════════════
# MODULE 4: PROVISION COVERAGE RATIO (PCR) CALCULATOR
# ══════════════════════════════════════════════════════

def pcr_calculator():
    print(f"\n{'━'*72}")
    print("  MODULE 4: PROVISION COVERAGE RATIO (PCR) CALCULATOR")
    print("  RBI Minimum: 70% | Ideal: 80%+")
    print(f"{'━'*72}")
    
    print("\n  Enter NPA data:")
    gross_npa = get_float("Gross NPA Outstanding (₹ Crore)")
    npa_provisions = get_float("NPA Provisions held in books (₹ Crore)")
    technical_writeoffs = get_float("Technical Write-off amount (₹ Crore, for PCR-II)")
    floating_provisions = get_float("Floating/Countercyclical Provisions (₹ Crore)")
    
    # PCR-I: without technical write-offs
    pcr_1 = (npa_provisions / gross_npa * 100) if gross_npa > 0 else 0
    # PCR-II: including technical write-offs (RBI's preferred measure)
    pcr_2 = ((npa_provisions + technical_writeoffs) / gross_npa * 100) if gross_npa > 0 else 0
    # PCR-III: including floating provisions
    pcr_3 = ((npa_provisions + technical_writeoffs + floating_provisions) / gross_npa * 100) if gross_npa > 0 else 0
    
    net_npa = gross_npa - npa_provisions
    net_npa_ratio_total = (net_npa / gross_npa * 100) if gross_npa > 0 else 0
    
    print(f"\n{SEPARATOR}")
    print("  PROVISION COVERAGE RATIO ANALYSIS")
    print(SEPARATOR)
    print(f"\n  Gross NPA:                          ₹{gross_npa:>10.2f} Crore")
    print(f"  NPA Provisions (books):             ₹{npa_provisions:>10.2f} Crore")
    print(f"  Technical Write-offs:               ₹{technical_writeoffs:>10.2f} Crore")
    print(f"  Net NPA:                            ₹{net_npa:>10.2f} Crore")
    
    print(f"\n  PCR-I   (provisions only):          {pcr_1:>10.1f}%  {'✅' if pcr_1 >= 70 else '❌ Below 70%'}")
    print(f"  PCR-II  (incl. tech write-offs):    {pcr_2:>10.1f}%  {'✅' if pcr_2 >= 70 else '❌ Below 70%'}")
    print(f"  PCR-III (incl. floating prov.):     {pcr_3:>10.1f}%")
    
    print(f"\n  RBI Minimum Requirement: 70% (PCR-II basis)")
    if pcr_2 < 70:
        shortfall_amount = (0.70 * gross_npa) - (npa_provisions + technical_writeoffs)
        print(f"  ❌ SHORTFALL TO REACH 70%: ₹{shortfall_amount:.2f} Crore")
        print(f"     Report in LFAR and Management Letter")
    else:
        print(f"  ✅ PCR meets RBI minimum of 70%")


# ══════════════════════════════════════════════════════
# MODULE 5: STANDARD ASSET PROVISION CALCULATOR
# ══════════════════════════════════════════════════════

def standard_asset_provision_calculator():
    print(f"\n{'━'*72}")
    print("  MODULE 5: STANDARD ASSET PROVISION CALCULATOR")
    print(f"{'━'*72}")
    
    print("\n  Enter portfolio data for standard asset provision check:")
    
    categories = list(STANDARD_ASSET_RATES.keys())
    totals = {}
    
    for cat in categories:
        rate = STANDARD_ASSET_RATES[cat]
        outstanding = get_float(f"{cat} — Outstanding (₹ Crore)", 0)
        if outstanding > 0:
            required = outstanding * rate
            totals[cat] = {"outstanding": outstanding, "rate": rate, "required": required}
    
    if not totals:
        print("  No data entered.")
        return
    
    print(f"\n{SEPARATOR}")
    print("  STANDARD ASSET PROVISION SUMMARY")
    print(SEPARATOR)
    print(f"\n  {'Category':<35} {'O/s (₹Cr)':>12} {'Rate':>6} {'Req.(₹Cr)':>12}")
    print(f"  {THIN_SEP}")
    
    total_os = total_req = 0
    for cat, data in totals.items():
        print(f"  {cat:<35} {data['outstanding']:>12.2f} {data['rate']*100:>5.2f}% {data['required']:>12.2f}")
        total_os += data['outstanding']
        total_req += data['required']
    
    print(f"  {THIN_SEP}")
    print(f"  {'TOTAL':<35} {total_os:>12.2f} {'':>6} {total_req:>12.2f}")
    
    held = get_float("\n  Standard Asset Provisions currently held by bank (₹ Crore)")
    shortfall = max(0, total_req - held)
    excess = max(0, held - total_req)
    
    print(f"\n  Required:  ₹{total_req:.2f} Crore")
    print(f"  Held:      ₹{held:.2f} Crore")
    if shortfall > 0:
        print(f"  ⚠  SHORTFALL: ₹{shortfall:.2f} Crore → MOC entry required")
    elif excess > 0:
        print(f"  ✅ Excess: ₹{excess:.2f} Crore (excess can remain; do not reverse without RBI approval)")
    else:
        print(f"  ✅ Standard asset provisions are adequate")


# ══════════════════════════════════════════════════════
# MAIN MENU
# ══════════════════════════════════════════════════════

def main():
    print_banner()
    
    while True:
        print(f"\n{SEPARATOR}")
        print("  MAIN MENU")
        print(SEPARATOR)
        print("  1. NPA Provision Calculator (Account-wise)")
        print("  2. Drawing Power Calculator (CC/OD)")
        print("  3. SMA Classification Tool")
        print("  4. Provision Coverage Ratio (PCR)")
        print("  5. Standard Asset Provision Calculator")
        print("  6. Run All (Full Audit Calculation Suite)")
        print("  0. Exit")
        print(SEPARATOR)
        
        choice = input("  Select module [0-6]: ").strip()
        
        if choice == "1":
            npa_provision_calculator()
        elif choice == "2":
            drawing_power_calculator()
        elif choice == "3":
            sma_classification_tool()
        elif choice == "4":
            pcr_calculator()
        elif choice == "5":
            standard_asset_provision_calculator()
        elif choice == "6":
            print("\n  Running full suite...")
            npa_provision_calculator()
            drawing_power_calculator()
            pcr_calculator()
        elif choice == "0":
            print("\n  ✅ Bank Audit Calculator — Session ended.")
            print("  Refer outputs to LFAR Section I-5 and MOC.")
            break
        else:
            print("  Invalid choice. Please select 0-6.")

if __name__ == "__main__":
    main()
