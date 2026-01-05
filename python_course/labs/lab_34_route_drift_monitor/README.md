# Lab 34 — Network Route Drift Detector (Routing Table Integrity Monitor)

## Goal
Build a Python script that monitors the system routing table, stores a baseline, and detects drift over time.

## Skills
- parsing `ip route` output
- baseline capture
- drift detection
- suspicious route heuristics

## Tasks
1. Read routing table entries.
2. Save baseline to JSON.
3. Compare current routes to baseline.
4. Detect:
   - new routes
   - missing routes
   - modified routes
   - suspicious gateways or interfaces
5. Print alerts.

## Stretch
- Add per-interface drift detection.
- Add timestamped drift logs.
- Add multi-table support (main, local, custom tables).

## Integration
This lab can later power:
- a "Routing Integrity" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from network drift patterns
