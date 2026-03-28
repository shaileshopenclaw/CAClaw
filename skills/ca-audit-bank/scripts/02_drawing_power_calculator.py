#!/usr/bin/env python3
"""
Drawing Power Calculator — Bank Audit
For CC/OD accounts | ICAI GN 2025 | RBI IRACP Norms
"""

def get_float(prompt, default=0.0):
    try:
        val = input(f"  {prompt} [{default}]: ").strip()
        return float(val) if val else default
    except:
        return default

def main():
    print("\n" + "="*70)
    print("  DRAWING POWER CALCULATOR — CC/OD ACCOUNTS")
    print("  Bank Audit | ICAI GN 2025 | RBI IRACP Norms")
    print("="*70)

    accounts = []
    while True:
        print(f"\n  Account {len(accounts)+1}:")
        acc_no = input("  Account No.: ").strip() or "CC-001"
        name = input("  Borrower: ").strip() or "Borrower"
        limit = get_float("Sanctioned CC Limit (₹L)")
        outstanding = get_float("Current Outstanding (₹L)")
        stock = get_float("Total Stock (₹L)")
        margin_stock = get_float("Margin on Stock (%)", 25) / 100
        debtors_lt90 = get_float("Debtors < 90 days (₹L)")
        margin_debtors = get_float("Margin on Debtors (%)", 40) / 100
        creditors = get_float("Creditors (₹L)")
        
        eligible_stock = stock * (1 - margin_stock)
        eligible_debtors = debtors_lt90 * (1 - margin_debtors)
        dp = max(0, min(eligible_stock + eligible_debtors - creditors, limit))
        excess = max(0, outstanding - dp)
        excess_over_limit = max(0, outstanding - limit)
        
        print(f"\n  Results for {name}:")
        print(f"  Eligible Stock: ₹{eligible_stock:.2f}L | Eligible Debtors: ₹{eligible_debtors:.2f}L")
        print(f"  Less Creditors: ₹{creditors:.2f}L")
        print(f"  DRAWING POWER: ₹{dp:.2f}L (Limit: ₹{limit:.2f}L)")
        print(f"  Outstanding: ₹{outstanding:.2f}L")
        if excess_over_limit > 0:
            print(f"  ❌ Excess over LIMIT: ₹{excess_over_limit:.2f}L → IRREGULAR")
        elif excess > 0:
            print(f"  ⚠  Excess over DP: ₹{excess:.2f}L → NPA if >90 days!")
        else:
            print(f"  ✅ Within Drawing Power")
        
        accounts.append({"acc_no": acc_no, "name": name, "limit": limit,
                         "outstanding": outstanding, "dp": dp, "excess": excess})
        
        if input("\n  Another account? (y/n): ").strip().lower() != 'y':
            break
    
    print("\n" + "="*70 + "\n  SUMMARY\n" + "="*70)
    print(f"  {'A/c':<12} {'Borrower':<20} {'Limit':>8} {'O/s':>8} {'DP':>8} {'Excess':>8}")
    print("  " + "-"*66)
    for a in accounts:
        print(f"  {a['acc_no']:<12} {a['name'][:18]:<20} {a['limit']:>8.2f} "
              f"{a['outstanding']:>8.2f} {a['dp']:>8.2f} {a['excess']:>8.2f}")
    
    high_risk = [a for a in accounts if a['excess'] > 0]
    if high_risk:
        print(f"\n  ⚠  {len(high_risk)} account(s) exceed Drawing Power — check NPA eligibility!")
    print()

if __name__ == "__main__":
    main()
