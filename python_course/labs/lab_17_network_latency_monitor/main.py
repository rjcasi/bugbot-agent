from utils import ping_host, compute_stats, save_baseline, load_baseline, detect_drift

TARGET = "8.8.8.8"  # Google DNS

def main():
    print("=== Network Latency & Packet Loss Monitor (Lab 17) ===\n")

    baseline = load_baseline()

    print(f"[+] Pinging {TARGET}...\n")
    latencies = ping_host(TARGET)
    avg, loss = compute_stats(latencies)

    current = {
        "avg_latency": avg,
        "packet_loss": loss
    }

    if baseline is None:
        print("[+] No baseline found. Creating one now...")
        save_baseline(current)
        print("[+] Baseline saved to latency_baseline.json")
        return

    print("[+] Baseline found. Checking for drift...\n")

    drifts = detect_drift(baseline, current)

    if not drifts:
        print("[✓] No drift detected. Network stable.")
    else:
        print("[!] Drift detected:")
        for d in drifts:
            print(" -", d)

if __name__ == "__main__":
    main()
