from utils import (
    read_firewall_rules,
    save_baseline,
    load_baseline,
    detect_drift
)

def main():
    print("=== Firewall Rule Drift Detector (Lab 24) ===\n")

    baseline = load_baseline()
    current = read_firewall_rules()

    if baseline is None:
        print("[+] No baseline found. Creating one now...")
        save_baseline(current)
        print("[+] Baseline saved to firewall_baseline.json")
        return

    print("[+] Baseline found. Checking for drift...\n")

    new_rules, deleted_rules, suspicious = detect_drift(baseline, current)

    if not new_rules and not deleted_rules and not suspicious:
        print("[✓] No drift detected. Firewall rules stable.")
        return

    if new_rules:
        print("[!] New firewall rules detected:")
        for r in new_rules:
            print(f" - {r}")

    if deleted_rules:
        print("\n[!] Deleted firewall rules:")
        for r in deleted_rules:
            print(f" - {r}")

    if suspicious:
        print("\n[!] Suspicious firewall rules detected:")
        for r in suspicious:
            print(f" - {r}")

if __name__ == "__main__":
    main()
