from utils import capture_baseline, save_baseline, load_baseline, detect_drift

def main():
    print("=== System Baseline & Drift Detector (Lab 13) ===\n")

    baseline = load_baseline()

    if baseline is None:
        print("[+] No baseline found. Creating one now...")
        data = capture_baseline()
        save_baseline(data)
        print("[+] Baseline saved to baseline.json")
        return

    print("[+] Baseline found. Checking for drift...\n")

    current = capture_baseline()
    drifts = detect_drift(baseline, current)

    if not drifts:
        print("[✓] No drift detected. System is stable.")
    else:
        print("[!] Drift detected:")
        for d in drifts:
            print(" -", d)

if __name__ == "__main__":
    main()
