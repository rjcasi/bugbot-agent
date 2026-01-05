import os
import json
import stat

CRITICAL_PATHS = [
    "/etc/passwd",
    "/etc/shadow",
    "/etc/ssh/sshd_config",
    "/etc/sudoers",
]

def get_file_info(path):
    """Return permissions, owner, group for a file."""
    try:
        st = os.stat(path)
        return {
            "mode": stat.S_IMODE(st.st_mode),
            "uid": st.st_uid,
            "gid": st.st_gid,
        }
    except FileNotFoundError:
        return None

def capture_baseline():
    data = {}
    for path in CRITICAL_PATHS:
        data[path] = get_file_info(path)
    return data

def save_baseline(data, path="file_perm_baseline.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_baseline(path="file_perm_baseline.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def detect_drift(old, new):
    drifts = []

    for path in old:
        if new[path] is None:
            drifts.append(f"{path} is missing")
            continue

        if old[path] is None:
            drifts.append(f"{path} was created")
            continue

        if old[path]["mode"] != new[path]["mode"]:
            drifts.append(
                f"{path} permissions changed: {oct(old[path]['mode'])} → {oct(new[path]['mode'])}"
            )

        if old[path]["uid"] != new[path]["uid"]:
            drifts.append(
                f"{path} owner changed: {old[path]['uid']} → {new[path]['uid']}"
            )

        if old[path]["gid"] != new[path]["gid"]:
            drifts.append(
                f"{path} group changed: {old[path]['gid']} → {new[path]['gid']}"
            )

    return drifts
