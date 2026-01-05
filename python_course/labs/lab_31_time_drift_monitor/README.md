# Lab 31 — System Time Drift Detector (Clock Skew & NTP Integrity Monitor)

## Goal
Build a Python script that compares local system time to NTP time, stores a baseline, and detects drift.

## Skills
- reading system time
- querying NTP servers
- baseline capture
- drift detection
- defensive automation

## Tasks
1. Read local system time.
2. Query an NTP server.
3. Compute time difference.
4. Save baseline to JSON.
5. Detect:
   - time drift
   - NTP failures
   - suspicious skew
6. Print alerts.

## Stretch
- Add multiple NTP servers.
- Add rolling drift averages.
- Add timestamped drift logs.

## Integration
This lab can later power:
- a "Time Integrity" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from temporal drift patterns
