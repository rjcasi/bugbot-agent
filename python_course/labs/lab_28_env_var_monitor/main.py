from utils import (
    read_env,
    save_baseline,
    load_baseline,
    detect_drift
)

def main():
    print("=== Environment Variable Drift Detector (Lab 28) ===\n")

    baseline = load_baseline()
    current = read_env()

    if baseline is None:
        print("[+] No baseline found. Creating one now...")
        save_baseline(current)
        print("[+] Baseline saved to env_baseline.json")
        return

    print("[+] Baseline found. Checking for drift...\n")

    new_vars, deleted_vars, modified_vars, suspicious = detect_drift(baseline, current)

    if not new_vars and not deleted_vars and not modified_vars and not suspicious:
        print("[✓] No drift detected. Environment stable.")
        return

    if new_vars:
        print("[!] New environment variables detected:")
        for k in new_vars:
            print(f" - {k}")

    if deleted_vars:
        print("\n[!] Deleted environment variables:")
        for k in deleted_vars:
            print(f" - {k}")

    if modified_vars:
        print("\n[!] Modified environment variables:")
        for k, old, new in modified_vars:
            print(f" - {k}: '{old}' → '{new}'")

    if suspicious:
        print("\n[!] Suspicious environment variables detected:")
        for k in suspicious:
            print(f" - {k}")

if __name__ == "__main__":
    main()
