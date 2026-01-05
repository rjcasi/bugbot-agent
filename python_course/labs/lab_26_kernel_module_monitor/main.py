from utils import (
    read_modules,
    save_baseline,
    load_baseline,
    detect_drift
)

def main():
    print("=== Kernel Module Drift Detector (Lab 26) ===\n")

    baseline = load_baseline()
    current = read_modules()

    if baseline is None:
        print("[+] No baseline found. Creating one now...")
        save_baseline(current)
        print("[+] Baseline saved to module_baseline.json")
        return

    print("[+] Baseline found. Checking for drift...\n")

    new_mods, missing_mods, size_drift, suspicious = detect_drift(baseline, current)

    if not new_mods and not missing_mods and not size_drift and not suspicious:
        print("[✓] No drift detected. Kernel modules stable.")
        return

    if new_mods:
        print("[!] New kernel modules detected:")
        for m in new_mods:
            print(f" - {m}")

    if missing_mods:
        print("\n[!] Missing kernel modules:")
        for m in missing_mods:
            print(f" - {m}")

    if size_drift:
        print("\n[!] Kernel module size drift detected:")
        for m, old, new in size_drift:
            print(f" - {m}: {old} → {new}")

    if suspicious:
        print("\n[!] Suspicious kernel modules detected:")
        for m in suspicious:
            print(f" - {m}")

if __name__ == "__main__":
    main()
