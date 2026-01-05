from utils import (
    capture_syscalls,
    save_baseline,
    load_baseline,
    detect_drift
)

def main():
    print("=== System Call Drift Detector (Lab 35) ===\n")

    pid = input("Enter PID to monitor: ").strip()

    if not pid.isdigit():
        print("[!] Invalid PID.")
        return

    pid = int(pid)

    baseline = load_baseline()
    current = capture_syscalls(pid)

    if current is None:
        print("[!] Failed to attach to process or capture syscalls.")
        return

    if baseline is None:
        print("[+] No baseline found. Creating one now...")
        save_baseline(current)
        print("[+] Baseline saved to syscall_baseline.json")
        return

    print("[+] Baseline found. Checking for drift...\n")

    new_calls, missing_calls, freq_drift, suspicious = detect_drift(baseline, current)

    if not new_calls and not missing_calls and not freq_drift and not suspicious:
        print("[✓] No drift detected. Syscall behavior stable.")
        return

    if new_calls:
        print("[!] New syscalls detected:")
        for c in new_calls:
            print(f" - {c}")

    if missing_calls:
        print("\n[!] Missing syscalls:")
        for c in missing_calls:
            print(f" - {c}")

    if freq_drift:
        print("\n[!] Syscall frequency drift detected:")
        for c, old, new in freq_drift:
            print(f" - {c}: {old} → {new}")

    if suspicious:
        print("\n[!] Suspicious syscalls detected:")
        for c in suspicious:
            print(f" - {c}")

if __name__ == "__main__":
    main()
