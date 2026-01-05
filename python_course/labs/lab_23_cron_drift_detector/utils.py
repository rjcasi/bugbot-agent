import subprocess
import json

SUSPICIOUS_KEYWORDS = [
    "curl",
    "wget",
    "nc",
    "bash -i",
    "python -c",
    "reverse",
    "crypto",
    "miner",
]

def read_crontab():
    """Return a list of cron job lines."""
    try:
        result = subprocess.run(
            ["crontab", "-l"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            return []
        lines = [
            line.strip()
            for line in result.stdout.split("\n")
            if line.strip() and not line.startswith("#")
        ]
        return lines
    except Exception:
        return []

def is_suspicious(entry):
    """Return True if a cron entry contains suspicious keywords."""
    entry_lower = entry.lower()
    return any(k in entry_lower for k in SUSPICIOUS_KEYWORDS)

def save_baseline(data, path="cron_baseline.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_baseline(path="cron_baseline.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def detect_drift(old, new):
    """Return new jobs, deleted jobs, modified jobs, suspicious jobs."""
    new_jobs = [j for j in new if j not in old]
    deleted_jobs = [j for j in old if j not in new]

    # Modified jobs = same schedule but different command
    modified = []
    for old_job in old:
        old_parts = old_job.split()
        for new_job in new:
            new_parts = new_job.split()
            if len(old_parts) > 5 and len(new_parts) > 5:
                if old_parts[:5] == new_parts[:5] and old_job != new_job:
                    modified.append((old_job, new_job))

    suspicious = [j for j in new if is_suspicious(j)]

    return new_jobs, deleted_jobs, modified, suspicious
