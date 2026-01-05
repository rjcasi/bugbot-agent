from utils import (
    read_cpu_freq,
    save_baseline,
    load_baseline,
    detect_drift
)

def main():
    print("=== CPU Frequency Drift Detector (Lab 32) ===\n")

    baseline = load_baseline()
    current = read_cpu_freq()

    if current is None:
        print("[!] Could not read CPU frequency.")
        return

    if baseline is None:
        print("[+] No baseline found. Creating one now...")
        save_baseline(current)
        print(f"[+] Baseline saved with frequency {current:.1f} MHz")
        return

    print("[+] Baseline found. Checking for drift...\n")

    drifts = detect_drift(baseline, current)

    if not drifts:
        print("[✓] No drift detected. CPU frequency stable.")
        return

    print("[!] Drift detected:")
    for d in drifts:
        print(" -", d)

if __name__ == "__main__":
    main()
