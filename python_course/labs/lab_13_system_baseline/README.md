# Lab 13 — System Baseline & Drift Detector (Config Integrity Monitor)

## Goal
Build a Python script that captures a baseline of key system values and detects drift over time.

## Skills
- JSON serialization
- system inspection
- drift detection
- defensive automation

## Tasks
1. Capture a baseline of:
   - OS info
   - CPU count
   - total RAM
   - disk usage
   - installed Python packages
2. Save baseline to JSON.
3. Compare current state to baseline.
4. Print drift alerts.

## Stretch
- Add hashing of config files.
- Add timestamped baseline history.
- Add CLI flags for baseline vs check mode.

## Integration
This lab can later power:
- a "System Drift" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from system changes
