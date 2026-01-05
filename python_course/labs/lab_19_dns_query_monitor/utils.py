import socket
import time
import json

SUSPICIOUS_TLDS = [
    ".xyz", ".top", ".click", ".info", ".gq", ".tk", ".ml", ".ga"
]

def resolve_domain(domain):
    """Resolve a domain and return (ip, latency_ms)."""
    start = time.time()
    try:
        ip = socket.gethostbyname(domain)
        latency = (time.time() - start) * 1000
        return ip, latency
    except Exception:
        return None, None

def check_tld(domain):
    """Return True if domain ends with a suspicious TLD."""
    for tld in SUSPICIOUS_TLDS:
        if domain.endswith(tld):
            return True
    return False

def save_baseline(data, path="dns_baseline.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_baseline(path="dns_baseline.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def detect_drift(old, new, latency_threshold=1.5):
    """Return lists of new domains, missing domains, and latency drift."""
    new_domains = [d for d in new if d not in old]
    missing_domains = [d for d in old if d not in new]

    latency_drift = []
    for domain in new:
        if domain in old:
            old_lat = old[domain]["latency"]
            new_lat = new[domain]["latency"]
            if old_lat and new_lat and new_lat > old_lat * latency_threshold:
                latency_drift.append((domain, old_lat, new_lat))

    return new_domains, missing_domains, latency_drift
