# Lab 27 — File Permission Drift Detector (Critical Path Integrity Monitor)

## Goal
Build a Python script that monitors file permissions on critical paths, stores a baseline, and detects drift.

## Skills
- os.stat permission inspection
- baseline capture
- drift detection
- defensive automation

## Tasks
1. Read permissions for critical files.
2. Save baseline to JSON.
3. Compare current permissions to baseline.
4. Detect:
   - permission changes
   - ownership changes
   - missing files
5. Print alerts.

## Stretch
- Add recursive directory scanning.
- Add timestamped drift logs.
- Add CLI flags for baseline vs check mode.

## Integration
This lab can later power:
- a "File Integrity" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from filesystem drift
