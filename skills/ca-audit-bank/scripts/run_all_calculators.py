#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════╗
║     BANK AUDIT MASTER CALCULATOR SUITE — RUN ALL                        ║
║     ICAI Guidance Note on Audit of Banks (2025 Edition)                 ║
║     Complete Calculation Suite for Bank Branch Audit                    ║
╚══════════════════════════════════════════════════════════════════════════╝

Modules Available:
  1. NPA Provision Calculator (account-wise + portfolio)
  2. Drawing Power Calculator (CC/OD accounts)
  3. SMA Classification Tool
  4. PCR (Provision Coverage Ratio) Calculator
  5. Standard Asset Provision Calculator
  6. SLR/CRR Compliance Calculator
  7. PSL (Priority Sector) Compliance Calculator
  8. Capital Adequacy / CRAR (Basel III)
  9. Materiality Calculator
  10. LFAR Checklist Generator
  11. MOC Template Generator

Run individually from scripts/ directory or use this menu.
"""

import subprocess
import sys
import os

SEPARATOR = "═" * 72

MODULES = {
    "1": ("NPA Provision Calculator", "01_npa_provision_calculator.py", "Module 1 — NPA Provision"),
    "2": ("Drawing Power Calculator (CC/OD)", "01_npa_provision_calculator.py", "Module 2 — Drawing Power"),
    "3": ("SMA Classification Tool", "01_npa_provision_calculator.py", "Module 3 — SMA"),
    "4": ("PCR — Provision Coverage Ratio", "01_npa_provision_calculator.py", "Module 4 — PCR"),
    "5": ("Standard Asset Provision", "01_npa_provision_calculator.py", "Module 5 — Std Asset Prov"),
    "6": ("SLR / CRR Compliance", "03_regulatory_compliance_calculators.py", "Module A — SLR/CRR"),
    "7": ("PSL Compliance Calculator", "03_regulatory_compliance_calculators.py", "Module B — PSL"),
    "8": ("Capital Adequacy / CRAR (Basel III)", "03_regulatory_compliance_calculators.py", "Module C — CRAR"),
    "9": ("Materiality Calculator", "03_regulatory_compliance_calculators.py", "Module D — Materiality"),
    "10": ("LFAR Checklist Generator", "08_lfar_checklist_generator.py", "LFAR Checklist"),
    "11": ("MOC Template Generator", "09_moc_template_generator.py", "MOC Template"),
}


def print_banner():
    print(f"\n{SEPARATOR}")
    print("  🏦 BANK AUDIT MASTER CALCULATOR SUITE")
    print("  ICAI Guidance Note on Audit of Banks (2025 Edition)")
    print("  Complete Calculation Suite | FY 2024-25")
    print(SEPARATOR)


def print_audit_reference_card():
    """Print quick reference card for bank auditors."""
    print(f"\n{SEPARATOR}")
    print("  BANK AUDIT QUICK REFERENCE CARD")
    print(SEPARATOR)
    print("""
  KEY RATIOS (FY 2024-25):
  ┌─────────────────────────────────────────────────────────────────┐
  │  CRR:          4.00% of NDTL                                    │
  │  SLR:         18.00% of NDTL                                    │
  │  CET1 + CCB:   8.00% min (= 5.5% + 2.5% CCB)                  │
  │  Tier1 + CCB:  9.50% min                                        │
  │  Total CRAR:  11.50% min (= 9.0% + 2.5% CCB)                   │
  │  PCR:         ≥ 70%                                             │
  │  Gold LTV:    ≤ 75%                                             │
  └─────────────────────────────────────────────────────────────────┘

  NPA CLASSIFICATION:
  ┌─────────────────────────────────────────────────────────────────┐
  │  Term Loans:     Overdue > 90 days                              │
  │  CC/OD:          Balance > DP/Limit for > 90 days              │
  │  Agri (Short):   2 crop seasons overdue                        │
  │  Agri (Long):    1 crop season overdue                         │
  │  SMA-0:          1–30 days  (Standard)                         │
  │  SMA-1:          31–60 days (Standard; CRILC if ≥₹5Cr)        │
  │  SMA-2:          61–90 days (Standard; CRILC if ≥₹5Cr)        │
  └─────────────────────────────────────────────────────────────────┘

  PROVISION RATES:
  ┌─────────────────┬─────────────┬──────────────┐
  │  Classification │  Secured %  │  Unsecured % │
  ├─────────────────┼─────────────┼──────────────┤
  │  Sub-Standard   │     15%     │      25%     │
  │  Doubtful-1     │     25%     │     100%     │
  │  Doubtful-2     │     40%     │     100%     │
  │  Doubtful-3     │    100%     │     100%     │
  │  Loss           │    100%     │     100%     │
  └─────────────────┴─────────────┴──────────────┘

  FRAUD REPORTING:
  ┌─────────────────────────────────────────────────────────────────┐
  │  ≥₹50 Crore:  Flash report within 24 HOURS                     │
  │  ≥₹1 Crore:   FMR within 3 WEEKS of detection                  │
  │  ≥₹5 Crore:   CBI referral (if staff involvement)              │
  └─────────────────────────────────────────────────────────────────┘

  KEY DEADLINES:
  ┌─────────────────────────────────────────────────────────────────┐
  │  Branch Audit Report:   ~April 30                               │
  │  MOC to SCA:            ~April 30                               │
  │  Certificates:          ~May 15                                 │
  │  SCA Audit Report:      ~May 30                                 │
  │  LFAR:                  June 30                                 │
  └─────────────────────────────────────────────────────────────────┘
""")


def main():
    print_banner()
    print_audit_reference_card()

    # Get script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    while True:
        print(f"\n{SEPARATOR}")
        print("  MAIN MENU — SELECT CALCULATOR")
        print(SEPARATOR)
        for key, (name, _, _) in MODULES.items():
            print(f"  {key:>2}. {name}")
        print(f"\n  Q  . Quick Reference Card (print again)")
        print(f"  0  . Exit")
        print(SEPARATOR)

        choice = input("  Select [0-11/Q]: ").strip().upper()

        if choice == "0":
            print("\n  ✅ Bank Audit Calculator Suite — Exited.")
            print("  Files to submit: Audit Report, MOC, LFAR, Certificates")
            print("  LFAR Deadline: June 30 | Audit Report: ~April 30")
            break
        elif choice == "Q":
            print_audit_reference_card()
        elif choice in MODULES:
            name, script_file, module_hint = MODULES[choice]
            script_path = os.path.join(script_dir, script_file)

            if os.path.exists(script_path):
                print(f"\n  Launching: {name}...")
                print(f"  Hint: When prompted for module selection, choose: {module_hint}")
                print(f"  {'─'*60}")
                try:
                    subprocess.run([sys.executable, script_path])
                except KeyboardInterrupt:
                    print("\n  [Returned to main menu]")
            else:
                print(f"  ⚠  Script not found: {script_file}")
                print(f"     Please ensure all scripts are in the scripts/ directory")
        else:
            print("  ⚠  Invalid choice. Please select 0–11 or Q.")


if __name__ == "__main__":
    main()
