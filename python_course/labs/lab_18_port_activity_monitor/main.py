from utils import get_listening_ports, save_baseline, load_baseline, detect_drift

def main():
    print("=== Port Activity Baseline & Drift Detector (Lab 18) ===\n")

    baseline = load_baseline()
    current = get_listening_ports()

    if baseline is None:
        print("[+] No baseline found. Creating one now...")
        save_baseline(current)
        print("[+] Baseline saved to port_baseline.json")
        return

    print("[+] Baseline found. Checking for drift...\n")

    new_ports, missing_ports = detect_drift(baseline, current)

    if not new_ports and not missing_ports:
        print("[✓] No drift detected. Port activity stable.")
        return

    if new_ports:
        print("[!] New listening ports detected:")
        for port, pid in new_ports:
            print(f" - Port {port} (PID {pid})")

    if missing_ports:
        print("\n[!] Missing ports (previously active):")
        for port, pid in missing_ports:
            print(f" - Port {port} (PID {pid})")

if __name__ == "__main__":
    main()
