import psutil
import json

SUSPICIOUS_PARENTS = [
    "bash",
    "sh",
    "python",
    "nc",
    "socat",
    "perl",
]

def capture_process_tree():
    """Return a dict of parent_pid -> list of child_pids."""
    tree = {}

    for proc in psutil.process_iter(["pid", "ppid", "name"]):
        try:
            pid = proc.info["pid"]
            ppid = proc.info["ppid"]

            if ppid not in tree:
                tree[ppid] = []
            tree[ppid].append(pid)

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return tree

def get_process_name(pid):
    try:
        return psutil.Process(pid).name()
    except Exception:
        return "unknown"

def save_baseline(data, path="process_tree_baseline.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_baseline(path="process_tree_baseline.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def detect_drift(old, new):
    """Return new relationships, missing relationships, suspicious relationships."""
    new_edges = []
    missing_edges = []
    suspicious = []

    # Detect new and suspicious relationships
    for parent in new:
        for child in new[parent]:
            if parent not in old or child not in old.get(parent, []):
                new_edges.append((parent, child))

                pname = get_process_name(parent)
                if pname.lower() in SUSPICIOUS_PARENTS:
                    suspicious.append((parent, child, pname))

    # Detect missing relationships
    for parent in old:
        for child in old[parent]:
            if parent not in new or child not in new.get(parent, []):
                missing_edges.append((parent, child))

    return new_edges, missing_edges, suspicious
