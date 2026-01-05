import json
import subprocess

# Kernel parameters to monitor
PARAMS = [
    "kernel.pid_max",
    "kernel.threads-max",
    "vm.swappiness",
    "fs.file-max",
    "net.ipv4.ip_forward",
    "net.ipv4.tcp_syncookies",
]

def read_sysctl(param):
    """Return the value of a sysctl parameter."""
    try:
        result = subprocess.run(
            ["sysctl", "-n", param],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            return None
        return result.stdout.strip()
    except Exception:
        return None

def capture_baseline():
    """Return a dict of param -> value."""
    data = {}
    for p in PARAMS:
        data[p] = read_sysctl(p)
    return data

def save_baseline(data, path="kernel_baseline.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_baseline(path="kernel_baseline.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def detect_drift(old, new):
    """Return list of drift messages."""
    drifts = []

    for param in old:
        if old[param] != new[param]:
            drifts.append(f"{param} changed: {old[param]} → {new[param]}")

    return drifts
