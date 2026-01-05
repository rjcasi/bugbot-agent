from utils import (
    read_users,
    save_baseline,
    load_baseline,
    detect_drift
)

def main():
    print("=== User Account Drift Detector (Lab 22) ===\n")

    baseline = load_baseline()
    current = read_users()

    if baseline is None:
        print("[+] No baseline found. Creating one now...")
        save_baseline(current)
        print("[+] Baseline saved to user_baseline.json")
        return

    print("[+] Baseline found. Checking for drift...\n")

    new_users, deleted_users, suspicious = detect_drift(baseline, current)

    if not new_users and not deleted_users and not suspicious:
        print("[✓] No drift detected. User accounts stable.")
        return

    if new_users:
        print("[!] New users detected:")
        for u in new_users:
            print(f" - {u}")

    if deleted_users:
        print("\n[!] Deleted users:")
        for u in deleted_users:
            print(f" - {u}")

    if suspicious:
        print("\n[!] Suspicious usernames detected:")
        for u in suspicious:
            print(f" - {u}")

if __name__ == "__main__":
    main()
