# Lab 20 — System Call Monitor (Process Behavior Drift Detector)

## Goal
Build a Python script that monitors per‑process behavior using context switches, I/O counts, and thread activity to detect drift from a baseline.

## Skills
- psutil process inspection
- behavioral baselining
- drift detection
- defensive automation

## Tasks
1. Capture per‑process behavior metrics:
   - voluntary context switches
   - involuntary context switches
   - read/write counts
   - thread count
2. Save baseline to JSON.
3. Compare current behavior to baseline.
4. Detect drift and print alerts.

## Stretch
- Add per‑process anomaly scoring.
- Add timestamped drift logs.
- Add CLI flags for baseline vs monitor mode.

## Integration
This lab can later power:
- a "Syscall Behavior" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from behavioral drift patterns
