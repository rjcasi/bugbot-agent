import platform
import psutil
import json
import pkg_resources

def capture_baseline():
    """Return a dictionary of baseline system info."""
    return {
        "os": platform.platform(),
        "cpu_count": psutil.cpu_count(),
        "total_ram_gb": round(psutil.virtual_memory().total / (1024**3), 2),
        "disk_total_gb": round(psutil.disk_usage("/").total / (1024**3), 2),
        "disk_used_gb": round(psutil.disk_usage("/").used / (1024**3), 2),
        "packages": sorted([str(p) for p in pkg_resources.working_set])
    }

def save_baseline(data, path="baseline.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_baseline(path="baseline.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def detect_drift(old, new):
    """Return a list of drift messages."""
    drifts = []

    for key in old:
        if old[key] != new[key]:
            drifts.append(f"{key} changed: {old[key]} → {new[key]}")

    return drifts
