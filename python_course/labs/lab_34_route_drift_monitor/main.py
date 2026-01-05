from utils import (
    read_routes,
    save_baseline,
    load_baseline,
    detect_drift
)

def main():
    print("=== Network Route Drift Detector (Lab 34) ===\n")

    baseline = load_baseline()
    current = read_routes()

    if baseline is None:
        print("[+] No baseline found. Creating one now...")
        save_baseline(current)
        print("[+] Baseline saved to route_baseline.json")
        return

    print("[+] Baseline found. Checking for drift...\n")

    new_routes, missing_routes, modified, suspicious = detect_drift(baseline, current)

    if not new_routes and not missing_routes and not modified and not suspicious:
        print("[✓] No drift detected. Routing table stable.")
        return

    if new_routes:
        print("[!] New routes detected:")
        for r in new_routes:
            print(f" - {r['raw']}")

    if missing_routes:
        print("\n[!] Missing routes:")
        for r in missing_routes:
            print(f" - {r['raw']}")

    if modified:
        print("\n[!] Modified routes:")
        for old, new in modified:
            print(f" - OLD: {old['raw']}")
            print(f"   NEW: {new['raw']}")

    if suspicious:
        print("\n[!] Suspicious routes detected:")
        for r in suspicious:
            print(f" - {r['raw']}")

if __name__ == "__main__":
    main()
