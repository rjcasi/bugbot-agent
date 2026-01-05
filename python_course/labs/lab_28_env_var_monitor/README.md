# Lab 28 — Environment Variable Drift Detector (Process Env Integrity Monitor)

## Goal
Build a Python script that monitors environment variables, stores a baseline, and detects drift over time.

## Skills
- os.environ inspection
- baseline capture
- drift detection
- suspicious variable heuristics
- defensive automation

## Tasks
1. Read environment variables.
2. Save baseline to JSON.
3. Compare current variables to baseline.
4. Detect:
   - new variables
   - deleted variables
   - modified variables
   - suspicious variables
5. Print alerts.

## Stretch
- Add regex‑based secret detection.
- Add timestamped drift logs.
- Add CLI flags for baseline vs check mode.

## Integration
This lab can later power:
- an "Environment Integrity" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from runtime drift patterns
