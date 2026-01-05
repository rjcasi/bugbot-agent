from utils import (
    read_crontab,
    save_baseline,
    load_baseline,
    detect_drift
)

def main():
    print("=== Cron Job Drift Detector (Lab 23) ===\n")

    baseline = load_baseline()
    current = read_crontab()

    if baseline is None:
        print("[+] No baseline found. Creating one now...")
        save_baseline(current)
        print("[+] Baseline saved to cron_baseline.json")
        return

    print("[+] Baseline found. Checking for drift...\n")

    new_jobs, deleted_jobs, modified_jobs, suspicious = detect_drift(baseline, current)

    if not new_jobs and not deleted_jobs and not modified_jobs and not suspicious:
        print("[✓] No drift detected. Cron jobs stable.")
        return

    if new_jobs:
        print("[!] New cron jobs detected:")
        for j in new_jobs:
            print(f" - {j}")

    if deleted_jobs:
        print("\n[!] Deleted cron jobs:")
        for j in deleted_jobs:
            print(f" - {j}")

    if modified_jobs:
        print("\n[!] Modified cron jobs:")
        for old, new in modified_jobs:
            print(f" - OLD: {old}")
            print(f"   NEW: {new}")

    if suspicious:
        print("\n[!] Suspicious cron entries detected:")
        for j in suspicious:
            print(f" - {j}")

if __name__ == "__main__":
    main()
