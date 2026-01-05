import psutil
import json

def read_cpu_freq():
    """Return current CPU frequency in MHz."""
    try:
        freq = psutil.cpu_freq()
        return freq.current if freq else None
    except Exception:
        return None

def save_baseline(freq, path="cpu_freq_baseline.json"):
    with open(path, "w") as f:
        json.dump({"freq": freq}, f, indent=4)

def load_baseline(path="cpu_freq_baseline.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)["freq"]
    except FileNotFoundError:
        return None

def detect_drift(old, new, drop_threshold=0.7, spike_threshold=1.3):
    """Return drift messages for CPU frequency changes."""
    drifts = []

    if new < old * drop_threshold:
        drifts.append(f"CPU frequency drop detected: {old:.1f} MHz → {new:.1f} MHz")

    if new > old * spike_threshold:
        drifts.append(f"CPU frequency spike detected: {old:.1f} MHz → {new:.1f} MHz")

    return drifts
