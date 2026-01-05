import psutil
import json

def capture_process_behavior():
    """Return a dict of pid -> behavior metrics."""
    data = {}

    for proc in psutil.process_iter(["pid", "name"]):
        try:
            ctx = proc.num_ctx_switches()
            io = proc.io_counters()
            threads = proc.num_threads()

            data[proc.pid] = {
                "name": proc.info["name"],
                "voluntary_ctx": ctx.voluntary,
                "involuntary_ctx": ctx.involuntary,
                "read_count": io.read_count,
                "write_count": io.write_count,
                "threads": threads,
            }
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return data

def save_baseline(data, path="syscall_baseline.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_baseline(path="syscall_baseline.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def detect_drift(old, new, threshold=2.0):
    """Return list of drift messages."""
    drifts = []

    for pid in new:
        if pid not in old:
            drifts.append(f"New process detected: PID {pid} ({new[pid]['name']})")
            continue

        for key in ["voluntary_ctx", "involuntary_ctx", "read_count", "write_count", "threads"]:
            old_val = old[pid][key]
            new_val = new[pid][key]

            if old_val == 0:
                continue

            if new_val > old_val * threshold:
                drifts.append(
                    f"PID {pid} ({new[pid]['name']}): {key} drift {old_val} → {new_val}"
                )

    for pid in old:
        if pid not in new:
            drifts.append(f"Missing process: PID {pid} ({old[pid]['name']})")

    return drifts
