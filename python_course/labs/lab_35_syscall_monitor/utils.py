import subprocess
import json
import time
from collections import Counter

SUSPICIOUS_SYSCALLS = [
    "ptrace",
    "execve",
    "mprotect",
    "clone",
    "fork",
    "vfork",
    "openat",
    "unlink",
]

def capture_syscalls(pid, duration=3):
    """Attach strace to a PID and capture syscalls for N seconds."""
    try:
        proc = subprocess.Popen(
            ["strace", "-p", str(pid), "-e", "trace=all"],
            stderr=subprocess.PIPE,
            stdout=subprocess.DEVNULL,
            text=True
        )
    except Exception:
        return None

    time.sleep(duration)

    proc.terminate()

    syscalls = []
    try:
        for line in proc.stderr:
            if "(" in line:
                call = line.split("(")[0].strip()
                syscalls.append(call)
    except Exception:
        pass

    return Counter(syscalls)

def save_baseline(data, path="syscall_baseline.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_baseline(path="syscall_baseline.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def detect_drift(old, new, freq_threshold=2.0):
    new_calls = [c for c in new if c not in old]
    missing_calls = [c for c in old if c not in new]

    freq_drift = []
    for c in new:
        if c in old and new[c] > old[c] * freq_threshold:
            freq_drift.append((c, old[c], new[c]))

    suspicious = [c for c in new if c in SUSPICIOUS_SYSCALLS]

    return new_calls, missing_calls, freq_drift, suspicious
