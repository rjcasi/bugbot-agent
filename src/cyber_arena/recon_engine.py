# src/cyber_arena/recon_engine.py

import random

SIMULATED_HOSTS = [
    {"ip": "10.0.0.2", "ports": [22, 80, 443]},
    {"ip": "10.0.0.3", "ports": [21, 8080]},
    {"ip": "10.0.0.4", "ports": [3306]},
]

def run_recon():
    """Return a simulated network scan result."""
    results = []
    for host in SIMULATED_HOSTS:
        open_ports = []
        for port in host["ports"]:
            if random.random() > 0.2:  # 80% chance port appears open
                open_ports.append(port)
        results.append({
            "ip": host["ip"],
            "open_ports": open_ports
        })
    return results