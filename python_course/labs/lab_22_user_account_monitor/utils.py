import json

SUSPICIOUS_PATTERNS = [
    "test",
    "tmp",
    "backup",
    "guest",
    "admin2",
    "root2",
]

def read_users():
    """Return a dict of username -> {uid, gid, home, shell}."""
    users = {}

    try:
        with open("/etc/passwd", "r") as f:
            for line in f:
                parts = line.strip().split(":")
                if len(parts) < 7:
                    continue

                username, _, uid, gid, _, home, shell = parts
                users[username] = {
                    "uid": int(uid),
                    "gid": int(gid),
                    "home": home,
                    "shell": shell,
                }
    except Exception:
        return {}

    return users

def is_suspicious(username):
    """Return True if username matches suspicious patterns."""
    username_lower = username.lower()
    return any(p in username_lower for p in SUSPICIOUS_PATTERNS)

def save_baseline(data, path="user_baseline.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_baseline(path="user_baseline.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def detect_drift(old, new):
    """Return new users, deleted users, and suspicious users."""
    new_users = [u for u in new if u not in old]
    deleted_users = [u for u in old if u not in new]
    suspicious = [u for u in new if is_suspicious(u)]

    return new_users, deleted_users, suspicious
