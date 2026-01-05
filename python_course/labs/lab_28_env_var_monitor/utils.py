import os
import json

SUSPICIOUS_KEYS = [
    "secret",
    "token",
    "password",
    "key",
    "aws",
    "gcp",
    "azure",
    "ssh",
]

def read_env():
    """Return a dict of environment variables."""
    return dict(os.environ)

def is_suspicious(key, value):
    key_lower = key.lower()
    value_lower = str(value).lower()
    return any(k in key_lower or k in value_lower for k in SUSPICIOUS_KEYS)

def save_baseline(data, path="env_baseline.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_baseline(path="env_baseline.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def detect_drift(old, new):
    new_vars = [k for k in new if k not in old]
    deleted_vars = [k for k in old if k not in new]

    modified_vars = []
    for k in new:
        if k in old and new[k] != old[k]:
            modified_vars.append((k, old[k], new[k]))

    suspicious = [k for k in new if is_suspicious(k, new[k])]

    return new_vars, deleted_vars, modified_vars, suspicious
