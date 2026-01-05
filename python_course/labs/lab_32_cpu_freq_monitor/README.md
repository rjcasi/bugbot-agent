# Lab 32 — CPU Frequency Drift Detector (Thermal Throttle & Clock Manipulation Monitor)

## Goal
Build a Python script that monitors CPU frequency, stores a baseline, and detects drift over time.

## Skills
- psutil CPU frequency inspection
- baseline capture
- drift detection
- thermal throttle detection
- defensive automation

## Tasks
1. Read current CPU frequency.
2. Save baseline to JSON.
3. Compare current frequency to baseline.
4. Detect:
   - frequency drops (thermal throttle)
   - frequency spikes (overclock or malicious manipulation)
   - instability patterns
5. Print alerts.

## Stretch
- Add per‑core frequency tracking.
- Add rolling averages.
- Add timestamped drift logs.

## Integration
This lab can later power:
- a "CPU Health" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from hardware drift patterns
