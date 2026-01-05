# Lab 17 — Network Latency & Packet Loss Monitor (ICMP Drift Detector)

## Goal
Build a Python script that measures network latency and packet loss, stores a baseline, and detects drift.

## Skills
- ICMP ping
- latency measurement
- packet loss detection
- rolling averages
- anomaly detection
- defensive automation

## Tasks
1. Ping a target host multiple times.
2. Compute average latency and packet loss.
3. Save baseline to JSON.
4. Compare current values to baseline.
5. Print drift alerts.

## Stretch
- Add jitter measurement.
- Add multi‑host monitoring.
- Add timestamped anomaly logs.

## Integration
This lab can later power:
- a "Network Health" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from network drift patterns
