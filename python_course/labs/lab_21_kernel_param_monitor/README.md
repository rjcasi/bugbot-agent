# Lab 21 — Kernel Parameter Drift Detector (sysctl Baseline Monitor)

## Goal
Build a Python script that reads kernel parameters, stores a baseline, and detects drift over time.

## Skills
- reading /proc/sys
- sysctl inspection
- baseline capture
- drift detection
- defensive automation

## Tasks
1. Read a set of kernel parameters.
2. Save baseline to JSON.
3. Compare current values to baseline.
4. Detect drift and print alerts.

## Stretch
- Add full sysctl dump.
- Add timestamped drift logs.
- Add CLI flags for baseline vs check mode.

## Integration
This lab can later power:
- a "Kernel Health" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from kernel drift patterns
