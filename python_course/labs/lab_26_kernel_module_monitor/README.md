# Lab 26 — Kernel Module Drift Detector (Loaded Modules Baseline Monitor)

## Goal
Build a Python script that reads loaded kernel modules, stores a baseline, and detects drift over time.

## Skills
- reading /proc/modules
- kernel module inspection
- baseline capture
- drift detection
- defensive automation

## Tasks
1. Read loaded kernel modules.
2. Save baseline to JSON.
3. Compare current modules to baseline.
4. Detect:
   - new modules
   - missing modules
   - suspicious modules
5. Print alerts.

## Stretch
- Add module size drift detection.
- Add timestamped drift logs.
- Add CLI flags for baseline vs check mode.

## Integration
This lab can later power:
- a "Kernel Modules" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from kernel drift patterns
