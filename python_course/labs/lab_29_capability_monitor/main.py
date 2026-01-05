from utils import (
    read_capabilities,
    save_baseline,
    load_baseline,
    detect_drift
)

def main():
    print("=== Linux Capability Drift Detector (Lab 29) ===\n")

    baseline = load_baseline()
    current = read_capabilities()

    if baseline is None:
        print("[+] No baseline found. Creating one now...")
        save_baseline(current)
        print("[+] Baseline saved to capability_baseline.json")
        return

    print("[+] Baseline found. Checking for drift...\n")

    new_files, deleted_files, modified, suspicious = detect_drift(baseline, current)

    if not new_files and not deleted_files and not modified and not suspicious:
        print("[✓] No drift detected. Capabilities stable.")
        return

    if new_files:
        print("[!] New privileged files detected:")
        for f in new_files:
            print(f" - {f} = {current[f]}")

    if deleted_files:
        print("\n[!] Privileged files removed:")
        for f in deleted_files:
            print(f" - {f}")

    if modified:
        print("\n[!] Modified capabilities:")
        for f, old, new in modified:
            print(f" - {f}: '{old}' → '{new}'")

    if suspicious:
        print("\n[!] Suspicious capabilities detected:")
        for f in suspicious:
            print(f" - {f} = {current[f]}")

if __name__ == "__main__":
    main()
