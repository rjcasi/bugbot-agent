from utils import (
    get_ntp_time,
    get_local_time,
    save_baseline,
    load_baseline,
    detect_drift
)

def main():
    print("=== System Time Drift Detector (Lab 31) ===\n")

    baseline = load_baseline()

    local = get_local_time()
    ntp = get_ntp_time()

    if ntp is None:
        print("[!] Failed to query NTP server. Cannot check drift.")
        return

    offset = local - ntp

    if baseline is None:
        print("[+] No baseline found. Creating one now...")
        save_baseline(offset)
        print(f"[+] Baseline saved with offset {offset:.3f}s")
        return

    print("[+] Baseline found. Checking for drift...\n")

    drifts = detect_drift(baseline, offset)

    if not drifts:
        print("[✓] No drift detected. System time stable.")
        return

    print("[!] Drift detected:")
    for d in drifts:
        print(" -", d)

if __name__ == "__main__":
    main()
