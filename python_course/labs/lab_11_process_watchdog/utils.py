import psutil
import time

SUSPICIOUS = [
    "nc", "netcat", "ncat",
    "hydra", "john",
    "sqlmap",
    "meterpreter", "msfconsole",
    "powershell.exe", "cmd.exe"
]

def get_processes():
    """Return a list of (pid, name, cpu, mem)."""
    procs = []
    for p in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
        try:
            info = p.info
            procs.append((
                info["pid"],
                info["name"],
                info["cpu_percent"],
                info["memory_percent"]
            ))
        except psutil.NoSuchProcess:
            pass
    return procs

def detect_suspicious(procs):
    """Return list of suspicious processes."""
    hits = []
    for pid, name, cpu, mem in procs:
        if name and name.lower() in SUSPICIOUS:
            hits.append((pid, name, cpu, mem))
    return hits

def detect_spikes(procs, cpu_thresh=50, mem_thresh=20):
    """Return processes exceeding CPU/memory thresholds."""
    spikes = []
    for pid, name, cpu, mem in procs:
        if cpu > cpu_thresh or mem > mem_thresh:
            spikes.append((pid, name, cpu, mem))
    return spikes
