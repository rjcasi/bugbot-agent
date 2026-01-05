# Lab 14 — File Hash Integrity Monitor (SHA‑256 Drift Detector)

## Goal
Build a Python script that computes SHA‑256 hashes of files, stores a baseline, and detects drift when files change.

## Skills
- SHA‑256 hashing
- directory traversal
- JSON serialization
- drift detection
- defensive automation

## Tasks
1. Walk a directory and hash all files.
2. Save baseline hashes to JSON.
3. Compare current hashes to baseline.
4. Print drift alerts.

## Stretch
- Add timestamped hash history.
- Add ignore patterns.
- Add CLI flags for baseline vs check mode.

## Integration
This lab can later power:
- a "File Integrity" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from file drift patterns
