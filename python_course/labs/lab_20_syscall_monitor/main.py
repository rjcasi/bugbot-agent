from utils import (
    capture_process_behavior,
    save_baseline,
    load_baseline,
    detect_drift
)

def main():
    print("=== System Call Behavior Monitor (Lab 20) ===\n")

    baseline = load_baseline()
    current = capture_process_behavior()

    if baseline is None:
        print("[+] No baseline found. Creating one now...")
        save_baseline(current)
        print("[+] Baseline saved to syscall_baseline.json")
        return

    print("[+] Baseline found. Checking for drift...\n")

    drifts = detect_drift(baseline, current)

    if not drifts:
        print("[✓] No drift detected. Process behavior stable.")
        return

    print("[!] Drift detected:")
    for d in drifts:
        print(" -", d)

if __name__ == "__main__":
    main()
