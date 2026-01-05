import json

def read_entropy():
    """Return the current system entropy value."""
    try:
        with open("/proc/sys/kernel/random/entropy_avail", "r") as f:
            return int(f.read().strip())
    except Exception:
        return None

def save_baseline(data, path="entropy_baseline.json"):
    with open(path, "w") as f:
        json.dump({"entropy": data}, f, indent=4)

def load_baseline(path="entropy_baseline.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)["entropy"]
    except FileNotFoundError:
        return None

def detect_drift(old, new, drop_threshold=0.5, spike_threshold=1.5):
    """Return drift messages for entropy changes."""
    drifts = []

    if new < old * drop_threshold:
        drifts.append(f"Entropy drop detected: {old} → {new}")

    if new > old * spike_threshold:
        drifts.append(f"Entropy spike detected: {old} → {new}")

    return drifts
