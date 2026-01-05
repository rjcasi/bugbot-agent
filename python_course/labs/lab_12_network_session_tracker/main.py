import time
from utils import (
    get_connections,
    detect_suspicious_ips,
    detect_failed_attempts,
    detect_high_volume
)

INTERVAL = 3  # seconds

def main():
    print("=== Network Session Tracker (Lab 12) ===\n")

    while True:
        time.sleep(INTERVAL)

        conns = get_connections()

        # Suspicious IPs
        sus = detect_suspicious_ips(conns)
        for laddr, raddr, status, pid in sus:
            print(f"[!] Suspicious IP: {raddr} (PID {pid}) Status={status}")

        # Failed attempts
        fails = detect_failed_attempts(conns)
        for laddr, raddr, status, pid in fails:
            print(f"[!] Failed connection: {raddr} Status={status} PID={pid}")

        # High-volume ports
        hv = detect_high_volume(conns)
        for port in hv:
            print(f"[!] High-volume port: {port} (many connections)")

if __name__ == "__main__":
    main()
