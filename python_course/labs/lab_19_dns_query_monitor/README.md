# Lab 19 — Suspicious DNS Query Monitor (Domain Reputation Drift Detector)

## Goal
Build a Python script that resolves domains, measures DNS latency, and detects suspicious or newly‑seen domains using a baseline.

## Skills
- DNS resolution
- latency measurement
- domain reputation heuristics
- baseline capture
- drift detection
- defensive automation

## Tasks
1. Resolve a list of domains.
2. Measure DNS latency.
3. Save baseline results to JSON.
4. Detect:
   - new domains
   - missing domains
   - latency drift
   - suspicious TLDs
5. Print alerts.

## Stretch
- Add WHOIS lookup.
- Add passive DNS history.
- Add timestamped drift logs.

## Integration
This lab can later power:
- a "DNS Health" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from DNS drift patterns
