import json

SUSPICIOUS_KEYWORDS = [
    "rootkit",
    "hide",
    "stealth",
    "backdoor",
    "mal",
    "ghost",
]

def read_modules():
    """Return a dict of module -> size."""
    modules = {}

    try:
        with open("/proc/modules", "r") as f:
            for line in f:
                parts = line.split()
                if len(parts) >= 2:
                    name = parts[0]
                    size = int(parts[1])
                    modules[name] = size
    except Exception:
        return {}

    return modules

def is_suspicious(module_name):
    """Return True if module name contains suspicious patterns."""
    name_lower = module_name.lower()
    return any(k in name_lower for k in SUSPICIOUS_KEYWORDS)

def save_baseline(data, path="module_baseline.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_baseline(path="module_baseline.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def detect_drift(old, new, size_threshold=2.0):
    """Return new modules, missing modules, size drift, suspicious modules."""
    new_modules = [m for m in new if m not in old]
    missing_modules = [m for m in old if m not in new]

    size_drift = []
    for m in new:
        if m in old:
            old_size = old[m]
            new_size = new[m]
            if old_size > 0 and new_size > old_size * size_threshold:
                size_drift.append((m, old_size, new_size))

    suspicious = [m for m in new if is_suspicious(m)]

    return new_modules, missing_modules, size_drift, suspicious
