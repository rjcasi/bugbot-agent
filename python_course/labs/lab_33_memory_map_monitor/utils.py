import json
import os

SUSPICIOUS_PATTERNS = [
    "w+x",      # writable + executable
    "xp",       # executable private mapping
]

def read_memory_map(pid):
    """Return a list of memory regions for a process."""
    maps_path = f"/proc/{pid}/maps"

    if not os.path.exists(maps_path):
        return None

    regions = []

    try:
        with open(maps_path, "r") as f:
            for line in f:
                parts = line.strip().split()
                addr, perms = parts[0], parts[1]
                path = parts[-1] if len(parts) > 5 else ""

                regions.append({
                    "addr": addr,
                    "perms": perms,
                    "path": path
                })
    except Exception:
        return None

    return regions

def is_suspicious(region):
    perms = region["perms"].lower()
    return any(p in perms for p in SUSPICIOUS_PATTERNS)

def save_baseline(data, path="memory_map_baseline.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_baseline(path="memory_map_baseline.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def detect_drift(old, new):
    """Return new regions, missing regions, modified perms, suspicious regions."""
    old_set = {(r["addr"], r["perms"], r["path"]) for r in old}
    new_set = {(r["addr"], r["perms"], r["path"]) for r in new}

    new_regions = [r for r in new if (r["addr"], r["perms"], r["path"]) not in old_set]
    missing_regions = [r for r in old if (r["addr"], r["perms"], r["path"]) not in new_set]

    modified = []
    old_by_addr = {r["addr"]: r for r in old}
    for r in new:
        if r["addr"] in old_by_addr and r["perms"] != old_by_addr[r["addr"]]["perms"]:
            modified.append((old_by_addr[r["addr"]], r))

    suspicious = [r for r in new if is_suspicious(r)]

    return new_regions, missing_regions, modified, suspicious
