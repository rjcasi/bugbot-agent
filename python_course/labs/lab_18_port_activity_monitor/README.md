# Lab 18 — Port Activity Baseline & Drift Detector (Socket Behavior Monitor)

## Goal
Build a Python script that captures a baseline of active listening ports and detects drift over time.

## Skills
- psutil socket inspection
- baseline capture
- drift detection
- defensive automation

## Tasks
1. List all listening ports.
2. Save baseline to JSON.
3. Compare current ports to baseline.
4. Detect:
   - new ports
   - missing ports
   - unexpected services
5. Print drift alerts.

## Stretch
- Add per‑process port mapping.
- Add timestamped drift logs.
- Add CLI flags for baseline vs check mode.

## Integration
This lab can later power:
- a "Port Activity" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from port drift patterns
