import hashlib
import os
import json

def sha256_file(path):
    """Return SHA-256 hash of a file."""
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                h.update(chunk)
        return h.hexdigest()
    except FileNotFoundError:
        return None

def hash_directory(root):
    """Return {filepath: sha256} for all files under root."""
    hashes = {}
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            full = os.path.join(dirpath, name)
            digest = sha256_file(full)
            if digest:
                hashes[full] = digest
    return hashes

def save_baseline(data, path="hash_baseline.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_baseline(path="hash_baseline.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def detect_drift(old, new):
    """Return list of drift messages."""
    drifts = []

    # Modified or deleted files
    for path in old:
        if path not in new:
            drifts.append(f"Deleted: {path}")
        elif old[path] != new[path]:
            drifts.append(f"Modified: {path}")

    # New files
    for path in new:
        if path not in old:
            drifts.append(f"New file: {path}")

    return drifts
