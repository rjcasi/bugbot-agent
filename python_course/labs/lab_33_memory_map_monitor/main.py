from utils import (
    read_memory_map,
    save_baseline,
    load_baseline,
    detect_drift
)

def main():
    print("=== Memory Map Drift Detector (Lab 33) ===\n")

    pid = input("Enter PID to inspect: ").strip()

    if not pid.isdigit():
        print("[!] Invalid PID.")
        return

    pid = int(pid)

    baseline = load_baseline()
    current = read_memory_map(pid)

    if current is None:
        print(f"[!] Could not read memory map for PID {pid}.")
        return

    if baseline is None:
        print("[+] No baseline found. Creating one now...")
        save_baseline(current)
        print("[+] Baseline saved to memory_map_baseline.json")
        return

    print("[+] Baseline found. Checking for drift...\n")

    new_regions, missing_regions, modified, suspicious = detect_drift(baseline, current)

    if not new_regions and not missing_regions and not modified and not suspicious:
        print("[✓] No drift detected. Memory map stable.")
        return

    if new_regions:
        print("[!] New memory regions:")
        for r in new_regions:
            print(f" - {r['addr']} {r['perms']} {r['path']}")

    if missing_regions:
        print("\n[!] Missing memory regions:")
        for r in missing_regions:
            print(f" - {r['addr']} {r['perms']} {r['path']}")

    if modified:
        print("\n[!] Modified permissions:")
        for old, new in modified:
            print(f" - {old['addr']}: {old['perms']} → {new['perms']}")

    if suspicious:
        print("\n[!] Suspicious memory regions detected:")
        for r in suspicious:
            print(f" - {r['addr']} {r['perms']} {r['path']}")

if __name__ == "__main__":
    main()
