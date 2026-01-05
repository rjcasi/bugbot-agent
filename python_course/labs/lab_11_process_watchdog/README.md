# Lab 11 — Process Watchdog (Suspicious Process Detector)

## Goal
Build a Python script that monitors running processes and alerts when suspicious names or resource spikes appear.

## Skills
- psutil process inspection
- CPU/memory monitoring
- pattern matching
- defensive automation

## Tasks
1. List all running processes.
2. Detect suspicious names (configurable list).
3. Detect CPU or memory spikes.
4. Print alerts in real time.

## Stretch
- Export alerts to JSON.
- Add a log file.
- Add a CLI for custom suspicious patterns.

## Integration
This lab can later power:
- a "Process Watchdog" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from process patterns
