#!/usr/bin/env python3
"""
MOC (MEMORANDUM OF CHANGES) TEMPLATE GENERATOR
Bank Audit | ICAI Guidance Note on Audit of Banks (2025 Edition)
Generates formatted MOC with all standard entries
"""

from datetime import date


def get_float(prompt: str, default: float = 0.0) -> float:
    try:
        val = input(f"  {prompt} [{default}]: ").strip()
        return float(val) if val else default
    except:
        return default


def generate_moc():
    SEP = "═" * 80
    THIN = "─" * 80

    print(f"\n{SEP}")
    print("  MEMORANDUM OF CHANGES (MOC) GENERATOR")
    print("  Bank Branch Audit | ICAI GN 2025")
    print(SEP)

    # Header info
    bank_name = input("\n  Bank Name: ").strip() or "ABC Bank"
    branch_name = input("  Branch Name: ").strip() or "Main Branch"
    branch_code = input("  Branch Code/IFSC: ").strip() or "ABCD0001234"
    fy = input("  Financial Year (e.g. 2024-25): ").strip() or "2024-25"
    audit_firm = input("  CA Firm Name: ").strip() or "M/s XYZ & Associates"
    audit_date = input("  MOC Date (DD/MM/YYYY): ").strip() or date.today().strftime("%d/%m/%Y")

    moc_entries = []

    print(f"\n{'─'*60}")
    print("  ENTER MOC ENTRIES")
    print("  Common categories: NPA Provision, Income Reversal,")
    print("  Standard Asset Provision, Investment Depreciation,")
    print("  Suspense Write-off, Fixed Asset Depreciation")
    print(f"{'─'*60}")

    # NPA provisions
    print("\n  [1] NPA PROVISION SHORTFALLS:")
    print("  (Enter each NPA account with provision shortfall)")

    npa_entries = []
    while True:
        add = input("  Add NPA provision entry? (y/n): ").strip().lower()
        if add != 'y':
            break
        acc_no = input("  A/c No.: ").strip()
        borrower = input("  Borrower Name: ").strip()
        classification = input("  Classification (SS/D1/D2/D3/Loss): ").strip().upper()
        outstanding = get_float("  Outstanding (₹ Lakhs)")
        provision_required = get_float("  Provision Required (₹ Lakhs)")
        provision_held = get_float("  Provision Held (₹ Lakhs)")
        shortfall = max(0, provision_required - provision_held)
        bank_agrees = input("  Does bank agree? (y/n): ").strip().lower() == 'y'

        npa_entries.append({
            "acc_no": acc_no, "borrower": borrower, "classification": classification,
            "outstanding": outstanding, "required": provision_required,
            "held": provision_held, "shortfall": shortfall, "agreed": bank_agrees
        })
        print(f"  ✓ Added: {borrower} | Shortfall: ₹{shortfall:.2f}L | {'Bank agrees' if bank_agrees else '⚠ Bank disagrees'}")

    total_npa_shortfall = sum(e["shortfall"] for e in npa_entries)
    total_npa_agreed = sum(e["shortfall"] for e in npa_entries if e["agreed"])
    total_npa_disagreed = sum(e["shortfall"] for e in npa_entries if not e["agreed"])
    moc_entries.append(("NPA Provision Shortfall", total_npa_shortfall, total_npa_agreed, total_npa_disagreed))

    # Income reversal
    print("\n  [2] INCOME REVERSAL (Unrealised interest on NPA accounts):")
    income_reversal_total = get_float("  Total interest to be reversed (₹ Lakhs)")
    income_agreed = get_float("  Of which bank agrees (₹ Lakhs)", income_reversal_total)
    income_disagreed = max(0, income_reversal_total - income_agreed)
    moc_entries.append(("Interest Income Reversal (NPA)", income_reversal_total, income_agreed, income_disagreed))

    # Standard asset provision
    print("\n  [3] STANDARD ASSET PROVISION SHORTFALL:")
    std_shortfall = get_float("  Standard asset provision shortfall (₹ Lakhs)")
    std_agreed = get_float("  Of which bank agrees (₹ Lakhs)", std_shortfall)
    std_disagreed = max(0, std_shortfall - std_agreed)
    moc_entries.append(("Standard Asset Provision Shortfall", std_shortfall, std_agreed, std_disagreed))

    # Investment depreciation
    print("\n  [4] INVESTMENT DEPRECIATION (AFS/HFT MTM shortfall):")
    inv_dep = get_float("  Additional investment depreciation required (₹ Lakhs)")
    inv_dep_agreed = get_float("  Of which bank agrees (₹ Lakhs)", inv_dep)
    inv_dep_disagreed = max(0, inv_dep - inv_dep_agreed)
    moc_entries.append(("Investment Depreciation (MTM)", inv_dep, inv_dep_agreed, inv_dep_disagreed))

    # Other entries
    print("\n  [5] OTHER MOC ENTRIES (enter 0 if not applicable):")
    suspense_writeoff = get_float("  Unrecoverable suspense write-off (₹ Lakhs)")
    fraud_provision = get_float("  Fraud provision not made (₹ Lakhs)")
    depreciation_fixed = get_float("  Fixed asset depreciation under/over (₹ Lakhs)")
    other_items = get_float("  Any other adjustments (₹ Lakhs)")

    moc_entries.append(("Suspense Write-offs", suspense_writeoff, suspense_writeoff, 0))
    moc_entries.append(("Fraud Provision", fraud_provision, fraud_provision, 0))
    moc_entries.append(("Fixed Asset Depreciation Adjustment", depreciation_fixed, depreciation_fixed, 0))
    moc_entries.append(("Other Adjustments", other_items, other_items, 0))

    # Calculate totals
    total_all = sum(e[1] for e in moc_entries)
    total_agreed = sum(e[2] for e in moc_entries)
    total_disagreed = sum(e[3] for e in moc_entries)

    # ── OUTPUT MOC DOCUMENT ──
    print(f"\n{SEP}")
    print("  MEMORANDUM OF CHANGES (MOC)")
    print(SEP)
    print(f"""
  TO,
  The Manager / Branch Head
  {branch_name} ({branch_code})
  {bank_name}

  FROM: {audit_firm}
  DATE: {audit_date}

  SUBJECT: Memorandum of Changes — Branch Audit FY {fy}

  Dear Sir/Madam,

  During the course of statutory audit of {branch_name}, {bank_name} for the
  financial year ended 31 March {fy[-2:]}, we have identified the following
  items requiring adjustments in the financial statements of the branch.

  We request you to give effect to the following changes/incorporate these
  adjustments in the financial statements and seek confirmation/comments
  where you are unable to agree.
""")

    print(f"  MOC SUMMARY TABLE:")
    print(f"  {'─'*76}")
    print(f"  {'Sl':>3}  {'Head of Account':<38} {'Amount(₹L)':>10}  {'Agreed':>9}  {'Disagreed':>9}")
    print(f"  {'─'*76}")

    for sl, (head, amount, agreed, disagreed) in enumerate(moc_entries, 1):
        if amount > 0:
            print(f"  {sl:>3}  {head:<38} {amount:>10.2f}  {agreed:>9.2f}  {disagreed:>9.2f}")

    print(f"  {'─'*76}")
    print(f"  {'':>3}  {'TOTAL':<38} {total_all:>10.2f}  {total_agreed:>9.2f}  {total_disagreed:>9.2f}")
    print(f"  {'─'*76}")

    # NPA account-wise
    if npa_entries:
        print(f"\n  ANNEXURE A — NPA PROVISION SHORTFALL (Account-wise):")
        print(f"  {'─'*76}")
        print(f"  {'A/c No.':<14} {'Borrower':<22} {'Class':<6} {'O/s':>8} {'Req':>8} {'Held':>8} {'Short':>8} {'Agreed'}")
        print(f"  {'─'*76}")
        for e in npa_entries:
            print(f"  {e['acc_no']:<14} {e['borrower'][:20]:<22} {e['classification']:<6} "
                  f"{e['outstanding']:>8.2f} {e['required']:>8.2f} {e['held']:>8.2f} "
                  f"{e['shortfall']:>8.2f} {'Yes' if e['agreed'] else 'NO ⚠'}")
        print(f"  {'─'*76}")
        print(f"  Total NPA Provision Shortfall: ₹{total_npa_shortfall:.2f} Lakhs")
        print(f"  Agreed: ₹{total_npa_agreed:.2f}L | Disagreed: ₹{total_npa_disagreed:.2f}L")

    # Impact analysis
    print(f"""
  IMPACT ON FINANCIAL STATEMENTS:
  ─────────────────────────────────────────────────────────
  Total Adjustments Required (Debit to P&L):  ₹{total_all:>10.2f} Lakhs
  Adjustments agreed by Bank:                 ₹{total_agreed:>10.2f} Lakhs
  Adjustments NOT agreed by Bank:             ₹{total_disagreed:>10.2f} Lakhs

  If agreed items are incorporated:
  → Net Profit/Loss will reduce by:           ₹{total_agreed:>10.2f} Lakhs
  → Net Worth will reduce by:                 ₹{total_agreed:>10.2f} Lakhs

  If disagreed items are NOT incorporated:
  → Audit report will be QUALIFIED/EOM*
  * Subject to materiality assessment

  MATERIALITY NOTE:
  → Disagreed amount ₹{total_disagreed:.2f}L compared to materiality threshold
  → Refer materiality working paper for threshold assessment
""")

    print(f"""
  AUDITOR'S NOTE:
  We request you to:
  1. Give effect to all agreed adjustments before finalisation
  2. Provide written explanation for any items not agreed
  3. Forward this MOC along with branch figures to the
     Statutory Central Auditor (SCA)
  4. Retain signed copy in branch audit records

  For {audit_firm}

  Sd/-
  Partner
  ICAI Membership No.: ___________

  ─────────────────────────────────────────────────
  BANK'S ACKNOWLEDGEMENT:
  Received and noted on: ___________
  Branch Head Signature: ___________
  Adjustments incorporated in books: Yes / No / Partial
  Comments: ___________________________________________
""")

    print(f"  {'='*76}")
    print("  MOC GENERATED SUCCESSFULLY")
    print(f"  Forward to SCA with branch figures and LFAR")
    if total_disagreed > 0:
        print(f"  ⚠  Disagreed items: ₹{total_disagreed:.2f}L — assess qualification need")
    print(f"  {'='*76}")


if __name__ == "__main__":
    generate_moc()
