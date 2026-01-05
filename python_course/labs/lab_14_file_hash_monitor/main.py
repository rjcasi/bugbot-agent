from utils import hash_directory, save_baseline, load_baseline, detect_drift

TARGET_DIR = "."  # monitor current directory

def main():
    print("=== File Hash Integrity Monitor (Lab 14) ===\n")

    baseline = load_baseline()

    if baseline is None:
        print("[+] No baseline found. Creating one now...")
        data = hash_directory(TARGET_DIR)
        save_baseline(data)
        print("[+] Baseline saved to hash_baseline.json")
        return

    print("[+] Baseline found. Checking for drift...\n")

    current = hash_directory(TARGET_DIR)
    drifts = detect_drift(baseline, current)

    if not drifts:
        print("[✓] No drift detected. Files are stable.")
    else:
        print("[!] Drift detected:")
        for d in drifts:
            print(" -", d)

if __name__ == "__main__":
    main()
