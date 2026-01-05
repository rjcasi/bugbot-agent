import subproces
import json

SUSPICIOUS_KEYWORDS = [
    "0.0.0.0",      # default route changes
    "tun",          # VPN tunnels
    "wg",           # WireGuard
    "ppp",          # dial-up / PPPoE
    "docker",       # container routing
    "podman",
]

def read_routes():
    """Return a list of routing table entries as dicts."""
    try:
        result = subprocess.run(
            ["ip", "route"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            return []

        routes = []
        for line in result.stdout.split("\n"):
            if not line.strip():
                continue

            parts = line.split()
            entry = {
                "raw": line.strip(),
                "dst": parts[0],
                "via": parts[2] if "via" in parts else None,
                "dev": parts[parts.index("dev") + 1] if "dev" in parts else None,
            }
            routes.append(entry)

        return routes

    except Exception:
        return []

def is_suspicious(route):
    raw = route["raw"].lower()
    return any(k in raw for k in SUSPICIOUS_KEYWORDS)

def save_baseline(data, path="route_baseline.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_baseline(path="route_baseline.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def detect_drift(old, new):
    old_raw = {r["raw"] for r in old}
    new_raw = {r["raw"] for r in new}

    new_routes = [r for r in new if r["raw"] not in old_raw]
    missing_routes = [r for r in old if r["raw"] not in new_raw]

    modified = []
    old_by_dst = {r["dst"]: r for r in old}
    for r in new:
        if r["dst"] in old_by_dst and r["raw"] != old_by_dst[r["dst"]]["raw"]:
            modified.append((old_by_dst[r["dst"]], r))

    suspicious = [r for r in new if is_suspicious(r)]

    return new_routes, missing_routes, modified, suspicious
