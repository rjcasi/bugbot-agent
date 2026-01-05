from collections import Counter
from utils import parse_log_line

LOG_PATH = "sample_data/log.txt"

def load_logs(path: str):
    with open(path, "r") as f:
        return [line.strip() for line in f.readlines()]

def analyze_logs(lines):
    ip_counter = Counter()
    status_counter = Counter()
    parsed = []

    for line in lines:
        entry = parse_log_line(line)
        if not entry:
            continue

        parsed.append(entry)
        ip_counter[entry["ip"]] += 1
        status_counter[entry["status"]] += 1

    return parsed, ip_counter, status_counter

def detect_anomalies(ip_counter, threshold=3):
    """Flag IPs with unusually high activity."""
    return [ip for ip, count in ip_counter.items() if count >= threshold]

def main():
    print("Loading logs...")
    lines = load_logs(LOG_PATH)

    parsed, ip_counter, status_counter = analyze_logs(lines)

    print("\n=== Top IPs ===")
    for ip, count in ip_counter.most_common():
        print(f"{ip}: {count} requests")

    print("\n=== Status Codes ===")
    for status, count in status_counter.items():
        print(f"{status}: {count}")

    anomalies = detect_anomalies(ip_counter)
    print("\n=== Anomalies (IPs with high activity) ===")
    for ip in anomalies:
        print(f"[!] Suspicious activity from {ip}")

if __name__ == "__main__":
    main()
