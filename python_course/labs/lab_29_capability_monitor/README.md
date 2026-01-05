# Lab 29 — System Capability Drift Detector (Linux Capabilities Monitor)

## Goal
Build a Python script that inspects Linux file capabilities, stores a baseline, and detects drift over time.

## Skills
- getcap inspection
- privilege monitoring
- baseline capture
- drift detection
- defensive automation

## Tasks
1. Read file capabilities using `getcap -r /`.
2. Save baseline to JSON.
3. Compare current capabilities to baseline.
4. Detect:
   - new privileged binaries
   - removed privileged binaries
   - modified capabilities
   - suspicious capabilities
5. Print alerts.

## Stretch
- Add per‑capability severity scoring.
- Add timestamped drift logs.
- Add CLI flags for baseline vs check mode.

## Integration
This lab can later power:
- a "Capabilities Integrity" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from privilege drift patterns
