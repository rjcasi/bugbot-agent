import subprocess
import json

SUSPICIOUS_CAPS = [
    "cap_sys_admin",
    "cap_setuid",
    "cap_setgid",
    "cap_net_admin",
    "cap_dac_override",
]

def read_capabilities():
    """Return a dict of file -> capabilities."""
    caps = {}

    try:
        result = subprocess.run(
            ["getcap", "-r", "/"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            return {}

        for line in result.stdout.split("\n"):
            if "=" in line:
                path, cap = line.split("=", 1)
                caps[path.strip()] = cap.strip()
    except Exception:
        return {}

    return caps

def is_suspicious(cap_string):
    cap_lower = cap_string.lower()
    return any(c in cap_lower for c in SUSPICIOUS_CAPS)

def save_baseline(data, path="capability_baseline.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_baseline(path="capability_baseline.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def detect_drift(old, new):
    new_files = [f for f in new if f not in old]
    deleted_files = [f for f in old if f not in new]

    modified = []
    for f in new:
        if f in old and new[f] != old[f]:
            modified.append((f, old[f], new[f]))

    suspicious = [f for f in new if is_suspicious(new[f])]

    return new_files, deleted_files, modified, suspicious
