from utils import (
    capture_process_tree,
    save_baseline,
    load_baseline,
    detect_drift,
    get_process_name
)

def main():
    print("=== Process Tree Drift Detector (Lab 25) ===\n")

    baseline = load_baseline()
    current = capture_process_tree()

    if baseline is None:
        print("[+] No baseline found. Creating one now...")
        save_baseline(current)
        print("[+] Baseline saved to process_tree_baseline.json")
        return

    print("[+] Baseline found. Checking for drift...\n")

    new_edges, missing_edges, suspicious = detect_drift(baseline, current)

    if not new_edges and not missing_edges and not suspicious:
        print("[✓] No drift detected. Process tree stable.")
        return

    if new_edges:
        print("[!] New parent/child relationships:")
        for parent, child in new_edges:
            print(f" - {get_process_name(parent)} ({parent}) → {get_process_name(child)} ({child})")

    if missing_edges:
        print("\n[!] Missing parent/child relationships:")
        for parent, child in missing_edges:
            print(f" - {get_process_name(parent)} ({parent}) → {get_process_name(child)} ({child})")

    if suspicious:
        print("\n[!] Suspicious parent/child relationships:")
        for parent, child, pname in suspicious:
            print(f" - {pname} ({parent}) → {get_process_name(child)} ({child})")

if __name__ == "__main__":
    main()
