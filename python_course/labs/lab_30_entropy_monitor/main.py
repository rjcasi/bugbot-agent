from utils import (
    read_entropy,
    save_baseline,
    load_baseline,
    detect_drift
)

def main():
    print("=== System Entropy Drift Detector (Lab 30) ===\n")

    baseline = load_baseline()
    current = read_entropy()

    if current is None:
        print("[!] Could not read system entropy.")
        return

    if baseline is None:
        print("[+] No baseline found. Creating one now...")
        save_baseline(current)
        print("[+] Baseline saved to entropy_baseline.json")
        return

    print("[+] Baseline found. Checking for drift...\n")

    drifts = detect_drift(baseline, current)

    if not drifts:
        print("[✓] No drift detected. Entropy stable.")
        return

    print("[!] Drift detected:")
    for d in drifts:
        print(" -", d)

if __name__ == "__main__":
    main()
