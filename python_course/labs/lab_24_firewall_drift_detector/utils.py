import subprocess
import json

SUSPICIOUS_KEYWORDS = [
    "ACCEPT all -- 0.0.0.0/0",
    "ACCEPT     all",
    "ALLOW IN Anywhere",
    "ALLOW OUT Anywhere",
    "DROP all -- 0.0.0.0/0",
]

def read_iptables():
    """Return list of iptables rules as strings."""
    try:
        result = subprocess.run(
            ["iptables", "-S"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            return []
        return [line.strip() for line in result.stdout.split("\n") if line.strip()]
    except Exception:
        return []

def read_ufw():
    """Return list of ufw rules as strings."""
    try:
        result = subprocess.run(
            ["ufw", "status"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            return []
        lines = result.stdout.split("\n")
        return [line.strip() for line in lines if line.strip() and "Status:" not in line]
    except Exception:
        return []

def read_firewall_rules():
    """Return combined firewall rules."""
    rules = read_iptables()
    if not rules:
        rules = read_ufw()
    return rules

def is_suspicious(rule):
    """Return True if rule contains suspicious patterns."""
    rule_lower = rule.lower()
    return any(k.lower() in rule_lower for k in SUSPICIOUS_KEYWORDS)

def save_baseline(data, path="firewall_baseline.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_baseline(path="firewall_baseline.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def detect_drift(old, new):
    """Return new rules, deleted rules, and suspicious rules."""
    new_rules = [r for r in new if r not in old]
    deleted_rules = [r for r in old if r not in new]
    suspicious = [r for r in new if is_suspicious(r)]
    return new_rules, deleted_rules, suspicious
