#!/usr/bin/env python3
"""
BANK AUDIT — REGULATORY COMPLIANCE CALCULATORS
Covers: SLR/CRR, PSL, Capital Adequacy (CRAR/Basel III), Materiality
ICAI Guidance Note on Audit of Banks (2025 Edition)
FY 2024-25
"""

from datetime import date


SEPARATOR = "═" * 72
THIN_SEP = "─" * 72


def get_float(prompt: str, default: float = 0.0) -> float:
    try:
        val = input(f"  {prompt} [{default}]: ").strip()
        return float(val) if val else default
    except ValueError:
        return default


# ══════════════════════════════════════════════════════
# MODULE A: SLR / CRR COMPLIANCE CALCULATOR
# ══════════════════════════════════════════════════════

def slr_crr_calculator():
    print(f"\n{SEPARATOR}")
    print("  SLR / CRR COMPLIANCE CALCULATOR")
    print("  CRR = 4.00% | SLR = 18.00% of NDTL")
    print(f"  As per RBI Act S.42 and Banking Regulation Act S.24")
    print(SEPARATOR)

    print("\n  Enter NDTL (Net Demand and Time Liabilities) data:")
    print("  (Use average NDTL for the reporting fortnight)")

    ndtl = get_float("NDTL — Net Demand and Time Liabilities (₹ Crore)")

    # CRR
    crr_rate = 0.04
    crr_required = ndtl * crr_rate
    crr_maintained = get_float("CRR maintained (Cash with RBI) (₹ Crore)")
    crr_shortfall = max(0, crr_required - crr_maintained)
    crr_excess = max(0, crr_maintained - crr_required)

    # SLR
    slr_rate = 0.18
    slr_required = ndtl * slr_rate
    print("\n  SLR-eligible assets:")
    g_secs = get_float("Government Securities (₹ Crore)")
    sdl = get_float("State Development Loans (₹ Crore)")
    rbi_eligible_bonds = get_float("RBI-approved Eligible Bonds (₹ Crore)")
    cash_with_rbi = get_float("Cash with RBI (above CRR) if SLR-eligible (₹ Crore)", 0)
    total_slr_assets = g_secs + sdl + rbi_eligible_bonds + cash_with_rbi
    slr_shortfall = max(0, slr_required - total_slr_assets)
    slr_excess = max(0, total_slr_assets - slr_required)

    print(f"\n{SEPARATOR}")
    print("  CRR / SLR COMPLIANCE ANALYSIS")
    print(SEPARATOR)
    print(f"\n  NDTL:                          ₹{ndtl:>12.2f} Crore")

    print(f"\n  CRR COMPLIANCE (Rate: {crr_rate*100:.2f}%):")
    print(f"  CRR Required:                  ₹{crr_required:>12.2f} Crore")
    print(f"  CRR Maintained:                ₹{crr_maintained:>12.2f} Crore")
    if crr_shortfall > 0:
        penalty = crr_shortfall * 0.05  # approx penalty (Bank Rate + 3%)
        print(f"  ❌ CRR SHORTFALL:              ₹{crr_shortfall:>12.2f} Crore")
        print(f"     Approximate Penalty:        ₹{penalty:>12.2f} Crore p.a.")
        print(f"     (Penalty = Bank Rate + 3% per annum on shortfall)")
        print(f"     → MUST report in Audit Report / LFAR")
    else:
        print(f"  ✅ CRR Excess:                 ₹{crr_excess:>12.2f} Crore")

    print(f"\n  SLR COMPLIANCE (Rate: {slr_rate*100:.2f}%):")
    print(f"  SLR Required:                  ₹{slr_required:>12.2f} Crore")
    print(f"  G-Secs:                        ₹{g_secs:>12.2f} Crore")
    print(f"  State Dev. Loans (SDL):        ₹{sdl:>12.2f} Crore")
    print(f"  Other Eligible Bonds:          ₹{rbi_eligible_bonds:>12.2f} Crore")
    print(f"  Total SLR Assets:              ₹{total_slr_assets:>12.2f} Crore")
    if slr_shortfall > 0:
        print(f"  ❌ SLR SHORTFALL:              ₹{slr_shortfall:>12.2f} Crore")
        print(f"     → Issue QUALIFIED SLR Certificate")
        print(f"     → Report in Audit Report")
    else:
        print(f"  ✅ SLR Excess:                 ₹{slr_excess:>12.2f} Crore")
        print(f"  ✅ Issue CLEAN SLR Compliance Certificate")

    print(f"\n  SLR / CRR CERTIFICATES:")
    print(f"  → CRR Certificate: {'UNQUALIFIED ✅' if crr_shortfall == 0 else 'QUALIFIED ❌'}")
    print(f"  → SLR Certificate: {'UNQUALIFIED ✅' if slr_shortfall == 0 else 'QUALIFIED ❌'}")


# ══════════════════════════════════════════════════════
# MODULE B: PSL COMPLIANCE CALCULATOR
# ══════════════════════════════════════════════════════

def psl_compliance_calculator():
    print(f"\n{SEPARATOR}")
    print("  PSL (PRIORITY SECTOR LENDING) COMPLIANCE CALCULATOR")
    print("  As per RBI Master Directions on PSL (Updated FY 2024-25)")
    print(SEPARATOR)

    print("\n  ANBC CALCULATION:")
    net_bank_credit = get_float("Net Bank Credit (NBC) from RBI Return (₹ Crore)")
    fcnr_deposits = get_float("Outstanding FCNR(B) and NRNR Deposits (₹ Crore)", 0)
    co_lending_os = get_float("Eligible Co-lending Outstandings (₹ Crore)", 0)
    inter_bank_lending = get_float("Lending to Banks (to be deducted) (₹ Crore)", 0)
    anbc = net_bank_credit + fcnr_deposits + co_lending_os - inter_bank_lending

    # Off-Balance Sheet
    ceobe = get_float("CEOBE (Credit Equivalent of Off-Balance Sheet) (₹ Crore)", 0)
    base = max(anbc, ceobe)

    print(f"\n  ANBC:  ₹{anbc:.2f} Crore")
    print(f"  CEOBE: ₹{ceobe:.2f} Crore")
    print(f"  Base (higher of ANBC/CEOBE): ₹{base:.2f} Crore")

    # PSL targets
    targets = {
        "Total PSL":              0.40,
        "Agriculture (total)":    0.18,
        "Small & Marginal Farmers": 0.10 * 0.18 / 0.18,  # 10% of 18% = 10% of agri
        "Micro Enterprises":      0.075,
        "Weaker Sections":        0.12,
    }
    target_amounts = {k: base * v for k, v in targets.items()}

    print(f"\n  PSL OUTSTANDING (enter actuals):")
    psl_actuals = {}
    for cat in targets:
        psl_actuals[cat] = get_float(f"{cat} (₹ Crore)")

    # PSLC (certificates)
    print(f"\n  PSLC (Priority Sector Lending Certificates) PURCHASED:")
    pslc_agriculture = get_float("PSLC — Agriculture (₹ Crore)", 0)
    pslc_sf_mf = get_float("PSLC — Small/Marginal Farmers (₹ Crore)", 0)
    pslc_micro = get_float("PSLC — Micro Enterprises (₹ Crore)", 0)
    pslc_general = get_float("PSLC — General (₹ Crore)", 0)

    # RIDF contributions (count towards PSL)
    ridf_nabard = get_float("RIDF/NABARD Contribution (₹ Crore)", 0)
    ridf_sidbi = get_float("SIDBI/NHB/MUDRA Contribution (₹ Crore)", 0)

    print(f"\n{SEPARATOR}")
    print("  PSL COMPLIANCE ANALYSIS")
    print(SEPARATOR)
    print(f"\n  Base (ANBC/CEOBE higher):  ₹{base:.2f} Crore")
    print(f"\n  {'Category':<28} {'Target':>8} {'Target(₹Cr)':>12} {'Actual(₹Cr)':>12} {'Shortfall':>12} {'Status'}")
    print(f"  {THIN_SEP}")

    has_shortfall = False
    total_shortfall = 0
    for cat, target_pct in targets.items():
        target_amt = base * target_pct
        actual = psl_actuals[cat]
        # Add PSLCs to relevant categories
        if "Agriculture" in cat:
            actual += pslc_agriculture + ridf_nabard
        if "Small" in cat:
            actual += pslc_sf_mf
        if "Micro" in cat:
            actual += pslc_micro
        if cat == "Total PSL":
            actual += pslc_general + ridf_nabard + ridf_sidbi

        shortfall = max(0, target_amt - actual)
        surplus = max(0, actual - target_amt)
        status = "✅" if shortfall == 0 else "❌"
        if shortfall > 0:
            has_shortfall = True
            total_shortfall += shortfall

        print(f"  {cat:<28} {target_pct*100:>7.1f}% {target_amt:>12.2f} {actual:>12.2f} "
              f"{shortfall:>12.2f} {status}")

    print(f"  {THIN_SEP}")

    if has_shortfall:
        print(f"\n  ⚠  PSL SHORTFALL DETECTED")
        print(f"  → Bank must contribute to RIDF/SIDBI/NHB/MUDRA for shortfall")
        print(f"  → PSL Shortfall Certificate: QUALIFIED ❌")
        print(f"  → Report in LFAR and note in audit report")
        print(f"  → Interest earned on RIDF is lower (disincentive for shortfall)")
    else:
        print(f"\n  ✅ All PSL targets met!")
        print(f"  → PSL Certificate: UNQUALIFIED ✅")

    # PSL Certificate text
    print(f"\n  SUGGESTED PSL CERTIFICATE TEXT:")
    print(f"  ─────────────────────────────────────────────────")
    status_text = "has achieved" if not has_shortfall else "has NOT achieved"
    print(f"  \"We certify that the Branch {status_text} the targets")
    print(f"  prescribed under Priority Sector Lending as per RBI Master")
    print(f"  Directions on Priority Sector Lending for FY {date.today().year-1}-{str(date.today().year)[-2:]}.")
    print(f"  The achieved PSL outstanding (including PSLCs/RIDF)")
    print(f"  is ₹{psl_actuals['Total PSL']:.2f} Crore against target of ₹{base*0.40:.2f} Crore.")
    if has_shortfall:
        print(f"  There is a shortfall in [categories with shortfall].\"")
    else:
        print(f"  All sub-targets including agriculture, weaker sections")
        print(f"  and micro enterprises have been achieved.\"")


# ══════════════════════════════════════════════════════
# MODULE C: CAPITAL ADEQUACY (CRAR / BASEL III)
# ══════════════════════════════════════════════════════

def capital_adequacy_crar():
    print(f"\n{SEPARATOR}")
    print("  CAPITAL ADEQUACY RATIO (CRAR) — BASEL III CALCULATOR")
    print("  As per RBI Master Circular on Basel III Capital Regulations")
    print(f"  Minimum: CET1 8.0% | Tier1 9.5% | Total CRAR 11.5%")
    print(SEPARATOR)

    print("\n  REGULATORY CAPITAL (₹ Crore):")
    print("  CET1 (Common Equity Tier 1):")
    paid_up_equity = get_float("  Paid-up Equity Capital")
    share_premium = get_float("  Share Premium Account")
    retained_earnings = get_float("  Retained Earnings/Statutory Reserves")
    other_comprehensive = get_float("  Eligible OCI components")
    cet1_deductions = get_float("  Deductions from CET1 (Intangibles, DTA, etc.)")
    cet1 = paid_up_equity + share_premium + retained_earnings + other_comprehensive - cet1_deductions

    print("\n  AT1 (Additional Tier 1 Instruments):")
    at1_instruments = get_float("  AT1 Bonds/Instruments outstanding")
    at1_deductions = get_float("  Deductions from AT1", 0)
    at1 = max(0, at1_instruments - at1_deductions)

    tier1_capital = cet1 + at1

    print("\n  Tier 2 Capital:")
    tier2_instruments = get_float("  Tier 2 Instruments (Sub-debt bonds)")
    tier2_provisions = get_float("  Eligible Provisions (Gen. Provisions, Floating)")
    tier2_deductions = get_float("  Deductions from Tier 2", 0)
    tier2 = tier2_instruments + tier2_provisions - tier2_deductions
    # Tier 2 cannot exceed Tier 1
    tier2 = min(tier2, tier1_capital)

    total_capital = tier1_capital + tier2

    print("\n  RISK WEIGHTED ASSETS (₹ Crore):")
    print("  Credit Risk RWA:")
    rwa_standard = get_float("  Standard Assets RWA (at applicable risk weights)")
    rwa_npa = get_float("  NPA RWA (sub-standard/doubtful)")
    rwa_offbalance = get_float("  Off-Balance Sheet RWA (BG, LC, derivatives)")
    rwa_credit = rwa_standard + rwa_npa + rwa_offbalance

    print("\n  Market Risk RWA:")
    rwa_market = get_float("  Market Risk Capital Charge (×12.5 for RWA)")

    print("\n  Operational Risk RWA:")
    rwa_operational = get_float("  Operational Risk Capital Charge (×12.5 for RWA)")

    total_rwa = rwa_credit + rwa_market + rwa_operational

    # Ratios
    cet1_ratio = (cet1 / total_rwa * 100) if total_rwa > 0 else 0
    tier1_ratio = (tier1_capital / total_rwa * 100) if total_rwa > 0 else 0
    total_crar = (total_capital / total_rwa * 100) if total_rwa > 0 else 0

    # Minimums (incl Capital Conservation Buffer of 2.5%)
    MIN_CET1 = 8.0   # 5.5% + 2.5% CCB
    MIN_TIER1 = 9.5  # 7.0% + 2.5% CCB
    MIN_CRAR = 11.5  # 9.0% + 2.5% CCB

    print(f"\n{SEPARATOR}")
    print("  CAPITAL ADEQUACY ANALYSIS (BASEL III)")
    print(SEPARATOR)
    print(f"\n  CAPITAL STRUCTURE:")
    print(f"  CET1 Capital:         ₹{cet1:>12.2f} Crore")
    print(f"  AT1 Capital:          ₹{at1:>12.2f} Crore")
    print(f"  Tier 1 Capital:       ₹{tier1_capital:>12.2f} Crore")
    print(f"  Tier 2 Capital:       ₹{tier2:>12.2f} Crore")
    print(f"  Total Capital:        ₹{total_capital:>12.2f} Crore")
    print(f"\n  RISK WEIGHTED ASSETS:")
    print(f"  Credit Risk:          ₹{rwa_credit:>12.2f} Crore")
    print(f"  Market Risk:          ₹{rwa_market:>12.2f} Crore")
    print(f"  Operational Risk:     ₹{rwa_operational:>12.2f} Crore")
    print(f"  Total RWA:            ₹{total_rwa:>12.2f} Crore")

    print(f"\n  CAPITAL RATIOS:")
    print(f"  {'Ratio':<20} {'Actual':>8} {'Minimum':>9} {'Status'}")
    print(f"  {THIN_SEP[:45]}")
    print(f"  {'CET1 Ratio':<20} {cet1_ratio:>7.2f}% {MIN_CET1:>8.1f}%  "
          f"{'✅' if cet1_ratio >= MIN_CET1 else '❌ BREACH!'}")
    print(f"  {'Tier 1 Ratio':<20} {tier1_ratio:>7.2f}% {MIN_TIER1:>8.1f}%  "
          f"{'✅' if tier1_ratio >= MIN_TIER1 else '❌ BREACH!'}")
    print(f"  {'Total CRAR':<20} {total_crar:>7.2f}% {MIN_CRAR:>8.1f}%  "
          f"{'✅' if total_crar >= MIN_CRAR else '❌ BREACH!'}")

    # Leverage Ratio
    total_exposure = get_float("\n  Total On + Off Balance Sheet Exposure (for Leverage Ratio) (₹ Crore)")
    leverage_ratio = (tier1_capital / total_exposure * 100) if total_exposure > 0 else 0
    print(f"  {'Leverage Ratio':<20} {leverage_ratio:>7.2f}% {'4.0':>8}%  "
          f"{'✅' if leverage_ratio >= 4.0 else '❌ BREACH!'}")

    # D-SIB surcharge
    is_dsib = input("\n  Is this a D-SIB (SBI/HDFC Bank/ICICI Bank)? (y/n): ").strip().lower() == 'y'
    if is_dsib:
        dsib_surcharge = get_float("D-SIB CET1 surcharge (%)")
        effective_min_cet1 = MIN_CET1 + dsib_surcharge
        print(f"  D-SIB CET1 minimum: {effective_min_cet1:.1f}% ({MIN_CET1}% + {dsib_surcharge}% surcharge)")
        if cet1_ratio < effective_min_cet1:
            print(f"  ❌ CET1 BELOW D-SIB REQUIREMENT of {effective_min_cet1:.1f}%!")

    # Capital Buffer status
    cet1_buffer = cet1_ratio - 5.5  # Above minimum (excluding CCB)
    print(f"\n  CAPITAL CONSERVATION BUFFER (CCB):")
    print(f"  CCB Required: 2.5%")
    if cet1_ratio >= MIN_CET1:
        print(f"  ✅ Full CCB maintained")
        print(f"  → Bank can pay full dividends and bonuses")
    elif cet1_ratio >= 7.5:  # 5.5 + 2.0 buffer
        print(f"  ⚠  Partial CCB — dividend/bonus payout restrictions apply")
    else:
        print(f"  ❌ CCB breached — significant dividend/bonus restrictions")

    print(f"\n  CAPITAL ADEQUACY CERTIFICATE:")
    if total_crar >= MIN_CRAR and tier1_ratio >= MIN_TIER1 and cet1_ratio >= MIN_CET1:
        print(f"  → Issue UNQUALIFIED Capital Adequacy Certificate ✅")
    else:
        print(f"  → Issue QUALIFIED Capital Adequacy Certificate ❌")
        print(f"  → Report capital breach in main Audit Report")


# ══════════════════════════════════════════════════════
# MODULE D: MATERIALITY CALCULATOR
# ══════════════════════════════════════════════════════

def materiality_calculator():
    print(f"\n{SEPARATOR}")
    print("  MATERIALITY CALCULATOR FOR BANK AUDIT")
    print("  As per SA 320 (Materiality in Planning and Performing an Audit)")
    print(SEPARATOR)

    print("\n  Enter financial data:")
    total_advances = get_float("Total Advances (₹ Crore)")
    total_deposits = get_float("Total Deposits (₹ Crore)")
    total_assets = get_float("Total Assets (₹ Crore)")
    nii = get_float("Net Interest Income (NII) (₹ Crore)")
    pre_tax_profit = get_float("Pre-Tax Profit / (Loss) (₹ Crore)")
    gross_npa = get_float("Gross NPA (₹ Crore)")

    # Multiple materiality benchmarks
    mat_advances_05 = total_advances * 0.005
    mat_advances_1 = total_advances * 0.01
    mat_nii_2 = nii * 0.02
    mat_nii_5 = nii * 0.05
    mat_assets = total_assets * 0.005
    mat_profit = abs(pre_tax_profit) * 0.05 if pre_tax_profit != 0 else 0

    print(f"\n{SEPARATOR}")
    print("  MATERIALITY ANALYSIS")
    print(SEPARATOR)
    print(f"\n  BENCHMARK CALCULATIONS:")
    print(f"  0.5% of Total Advances:         ₹{mat_advances_05:>10.2f} Crore")
    print(f"  1.0% of Total Advances:         ₹{mat_advances_1:>10.2f} Crore")
    print(f"  2.0% of Net Interest Income:    ₹{mat_nii_2:>10.2f} Crore")
    print(f"  5.0% of Net Interest Income:    ₹{mat_nii_5:>10.2f} Crore")
    print(f"  0.5% of Total Assets:           ₹{mat_assets:>10.2f} Crore")
    print(f"  5.0% of Pre-Tax Profit:         ₹{mat_profit:>10.2f} Crore")

    # Recommended materiality
    # For banks with large NPA: use advances-based
    npa_ratio = (gross_npa / total_advances * 100) if total_advances > 0 else 0

    if npa_ratio > 5:
        # High NPA bank — use conservative (lower) materiality
        recommended = mat_advances_05
        basis = "0.5% of Advances (conservative — High NPA bank)"
    elif pre_tax_profit < 0:
        # Loss-making bank — use assets or NII
        recommended = min(mat_assets, mat_nii_2) if nii > 0 else mat_assets
        basis = "Lower of 0.5% Assets or 2% NII (loss-making bank)"
    else:
        # Normal bank — use 0.75% of advances
        recommended = total_advances * 0.0075
        basis = "0.75% of Total Advances (typical)"

    performance_mat = recommended * 0.75
    trivial_threshold = recommended * 0.05

    print(f"\n  GROSS NPA RATIO: {npa_ratio:.1f}%")
    print(f"\n  RECOMMENDED MATERIALITY:")
    print(f"  Basis: {basis}")
    print(f"  Overall Materiality (OM):       ₹{recommended:>10.2f} Crore")
    print(f"  Performance Materiality (PM):   ₹{performance_mat:>10.2f} Crore  (75% of OM)")
    print(f"  Trivial / Inconsequential:      ₹{trivial_threshold:>10.2f} Crore  (5% of OM)")

    print(f"\n  IMPLICATIONS:")
    print(f"  → NPA differences >₹{recommended:.2f} Cr require qualification (if disagreed)")
    print(f"  → MOC items >₹{performance_mat:.2f} Cr require escalation to SCA")
    print(f"  → Items <₹{trivial_threshold:.2f} Cr can be ignored (clearly inconsequential)")
    print(f"  → Individual NPA account differences up to PM to be reported in LFAR")
    print(f"  → Aggregate MOC: if total >OM and disagreed → LIKELY QUALIFICATION")

    print(f"\n  IN RUPEES LAKHS:")
    print(f"  Overall Materiality:            ₹{recommended*100:>10.0f} Lakhs")
    print(f"  Performance Materiality:        ₹{performance_mat*100:>10.0f} Lakhs")
    print(f"  Trivial Threshold:              ₹{trivial_threshold*100:>10.0f} Lakhs")


# ══════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════

def main():
    print(f"\n{SEPARATOR}")
    print("  BANK AUDIT — REGULATORY COMPLIANCE CALCULATORS")
    print("  ICAI GN 2025 | RBI Norms | FY 2024-25")
    print(SEPARATOR)

    while True:
        print(f"\n  MENU:")
        print("  A. SLR / CRR Compliance Calculator")
        print("  B. PSL (Priority Sector Lending) Compliance")
        print("  C. Capital Adequacy / CRAR (Basel III)")
        print("  D. Materiality Calculator")
        print("  0. Exit")

        choice = input("\n  Select [A/B/C/D/0]: ").strip().upper()
        if choice == "A":
            slr_crr_calculator()
        elif choice == "B":
            psl_compliance_calculator()
        elif choice == "C":
            capital_adequacy_crar()
        elif choice == "D":
            materiality_calculator()
        elif choice == "0":
            break
        else:
            print("  Invalid choice.")

if __name__ == "__main__":
    main()
