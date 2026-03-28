#!/usr/bin/env python3
"""SMA Classification Tool — Bank Audit | ICAI GN 2025"""

def main():
    print("\n" + "="*60)
    print("  SMA CLASSIFICATION TOOL")
    print("  Bank Audit | RBI IRACP Norms | CRILC Check")
    print("="*60)
    
    accounts = []
    while True:
        acc = input("\n  Account No.: ").strip() or f"A{len(accounts)+1:03d}"
        name = input("  Borrower: ").strip() or "Borrower"
        try:
            days = int(input("  Days Overdue (0=Regular): ").strip() or "0")
        except:
            days = 0
        try:
            exposure = float(input("  Total Exposure (₹ Lakhs): ").strip() or "0")
        except:
            exposure = 0
        
        if days <= 0: cls = "Standard ✅"
        elif days <= 30: cls = "SMA-0 ⚠"
        elif days <= 60: cls = "SMA-1 ⚠"
        elif days <= 90: cls = "SMA-2 ❌"
        else: cls = f"NPA! ({days}d) ❌"
        
        crilc = exposure >= 500 and "SMA-1" in cls or "SMA-2" in cls
        accounts.append({"acc": acc, "name": name, "days": days, "cls": cls,
                         "exposure": exposure, "crilc": crilc})
        print(f"  → {cls} | CRILC: {'⚠ REQUIRED' if crilc else 'Not required'}")
        
        if input("  Add another? (y/n): ").strip().lower() != 'y':
            break
    
    print("\n  SUMMARY:")
    for a in accounts:
        print(f"  {a['acc']} | {a['name'][:20]} | {a['days']}d | {a['cls']}")
        if a['crilc']:
            print(f"         → CRILC REPORTING REQUIRED (Exposure: ₹{a['exposure']:.0f}L)")

if __name__ == "__main__":
    main()
