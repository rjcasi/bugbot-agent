import os
import hashlib

def sha256_file(path: str) -> str:
    """Compute SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def scan_folder(folder: str):
    """Return a dict: {filename: hash} for all files in a folder."""
    state = {}
    for root, _, files in os.walk(folder):
        for f in files:
            full = os.path.join(root, f)
            state[full] = sha256_file(full)
    return state
