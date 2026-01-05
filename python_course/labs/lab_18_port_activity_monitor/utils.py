import psutil
import json

def get_listening_ports():
    """Return a set of (port, pid) for listening sockets."""
    ports = set()

    for conn in psutil.net_connections(kind="inet"):
        if conn.status == psutil.CONN_LISTEN:
            port = conn.laddr.port
            pid = conn.pid
            ports.add((port, pid))

    return ports

def save_baseline(data, path="port_baseline.json"):
    serializable = [{"port": p, "pid": pid} for p, pid in data]
    with open(path, "w") as f:
        json.dump(serializable, f, indent=4)

def load_baseline(path="port_baseline.json"):
    try:
        with open(path, "r") as f:
            raw = json.load(f)
            return {(item["port"], item["pid"]) for item in raw}
    except FileNotFoundError:
        return None

def detect_drift(old, new):
    """Return lists of new ports and missing ports."""
    new_ports = new - old
    missing_ports = old - new
    return new_ports, missing_ports
