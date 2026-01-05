from utils import (
    resolve_domain,
    check_tld,
    save_baseline,
    load_baseline,
    detect_drift
)

DOMAINS = [
    "google.com",
    "microsoft.com",
    "github.com",
    "cloudflare.com",
    "example.xyz",   # suspicious TLD example
]

def main():
    print("=== DNS Query Monitor (Lab 19) ===\n")

    baseline = load_baseline()

    print("[+] Resolving domains...\n")
    results = {}

    for domain in DOMAINS:
        ip, latency = resolve_domain(domain)
        results[domain] = {
            "ip": ip,
            "latency": latency,
            "suspicious_tld": check_tld(domain)
        }

    if baseline is None:
        print("[+] No baseline found. Creating one now...")
        save_baseline(results)
        print("[+] Baseline saved to dns_baseline.json")
        return

    print("[+] Baseline found. Checking for drift...\n")

    new_domains, missing_domains, latency_drift = detect_drift(baseline, results)

    if not new_domains and not missing_domains and not latency_drift:
        print("[✓] No drift detected. DNS activity stable.")
        return

    if new_domains:
        print("[!] New domains detected:")
        for d in new_domains:
            print(f" - {d}")

    if missing_domains:
        print("\n[!] Missing domains (previously monitored):")
        for d in missing_domains:
            print(f" - {d}")

    if latency_drift:
        print("\n[!] Latency drift detected:")
        for domain, old_lat, new_lat in latency_drift:
            print(f" - {domain}: {old_lat:.2f}ms → {new_lat:.2f}ms")

    print("\n[+] Suspicious TLDs:")
    for domain, data in results.items():
        if data["suspicious_tld"]:
            print(f" - {domain}")

if __name__ == "__main__":
    main()
