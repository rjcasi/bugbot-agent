import subprocess
import json
import statistics

def ping_host(host, count=5):
    """Ping a host and return list of latencies (ms)."""
    latencies = []

    for _ in range(count):
        try:
            result = subprocess.run(
                ["ping", "-c", "1", host],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            if result.returncode != 0:
                latencies.append(None)
                continue

            for line in result.stdout.split("\n"):
                if "time=" in line:
                    ms = float(line.split("time=")[1].split(" ")[0])
                    latencies.append(ms)
        except Exception:
            latencies.append(None)

    return latencies

def compute_stats(latencies):
    """Return avg latency and packet loss."""
    valid = [x for x in latencies if x is not None]
    loss = (len(latencies) - len(valid)) / len(latencies)

    avg = statistics.mean(valid) if valid else None

    return avg, loss

def save_baseline(data, path="latency_baseline.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_baseline(path="latency_baseline.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def detect_drift(baseline, current, threshold=1.5):
    """Return list of drift messages."""
    drifts = []

    if baseline["avg_latency"] and current["avg_latency"]:
        if current["avg_latency"] > baseline["avg_latency"] * threshold:
            drifts.append(
                f"Latency drift: baseline={baseline['avg_latency']:.2f}ms, current={current['avg_latency']:.2f}ms"
            )

    if current["packet_loss"] > baseline["packet_loss"] * threshold:
        drifts.append(
            f"Packet loss drift: baseline={baseline['packet_loss']:.2%}, current={current['packet_loss']:.2%}"
        )

    return drifts
