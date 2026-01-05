# Lab 25 — Process Tree Drift Detector (Parent/Child Relationship Monitor)

## Goal
Build a Python script that maps process parent/child relationships, stores a baseline, and detects drift over time.

## Skills
- psutil process inspection
- process tree mapping
- baseline capture
- drift detection
- defensive automation

## Tasks
1. Enumerate all processes.
2. Map parent → child relationships.
3. Save baseline to JSON.
4. Compare current tree to baseline.
5. Detect:
   - new parent/child relationships
   - missing relationships
   - suspicious parent/child pairs
6. Print alerts.

## Stretch
- Add per‑process anomaly scoring.
- Add timestamped drift logs.
- Add CLI flags for baseline vs check mode.

## Integration
This lab can later power:
- a "Process Tree" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from structural drift patterns
