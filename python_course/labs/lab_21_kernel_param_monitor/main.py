from utils import (
    capture_baseline,
    save_baseline,
    load_baseline,
    detect_drift
)

def main():
    print("=== Kernel Parameter Drift Detector (Lab 21) ===\n")

    baseline = load_baseline()
    current = capture_baseline()

    if baseline is None:
        print("[+] No baseline found. Creating one now...")
        save_baseline(current)
        print("[+] Baseline saved to kernel_baseline.json")
        return

    print("[+] Baseline found. Checking for drift...\n")

    drifts = detect_drift(baseline, current)

    if not drifts:
        print("[✓] No drift detected. Kernel parameters stable.")
        return

    print("[!] Drift detected:")
    for d in drifts:
        print(" -", d)

if __name__ == "__main__":
    main()
