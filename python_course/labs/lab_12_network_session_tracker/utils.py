import psutil
import time

SUSPICIOUS_IPS = [
    "185.220.",   # Tor exit nodes (example prefix)
    "45.155.",    # VPN ranges (example prefix)
    "23.129.",    # Known scanning ranges (example prefix)
]

def get_connections():
    """Return a list of (laddr, raddr, status, pid)."""
    conns = []
    for c in psutil.net_connections(kind="inet"):
        try:
            laddr = f"{c.laddr.ip}:{c.laddr.port}" if c.laddr else None
            raddr = f"{c.raddr.ip}:{c.raddr.port}" if c.raddr else None
            conns.append((laddr, raddr, c.status, c.pid))
        except Exception:
            pass
    return conns

def detect_suspicious_ips(conns):
    hits = []
    for laddr, raddr, status, pid in conns:
        if raddr:
            for prefix in SUSPICIOUS_IPS:
                if raddr.startswith(prefix):
                    hits.append((laddr, raddr, status, pid))
    return hits

def detect_failed_attempts(conns):
    """Detect repeated SYN_SENT or TIME_WAIT states."""
    return [
        (laddr, raddr, status, pid)
        for laddr, raddr, status, pid in conns
        if status in ("SYN_SENT", "TIME_WAIT")
    ]

def detect_high_volume(conns, threshold=20):
    """Detect local ports with many connections."""
    counts = {}
    for laddr, raddr, status, pid in conns:
        if laddr:
            port = laddr.split(":")[-1]
            counts[port] = counts.get(port, 0) + 1

    return [port for port, count in counts.items() if count > threshold]
