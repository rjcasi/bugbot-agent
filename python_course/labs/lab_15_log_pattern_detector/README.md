# Lab 15 — Suspicious Log Pattern Detector (Regex‑Driven Threat Scanner)

## Goal
Build a Python script that scans log files for suspicious patterns using regular expressions.

## Skills
- regex pattern matching
- log parsing
- threat detection
- defensive automation

## Tasks
1. Read a log file line by line.
2. Detect suspicious patterns:
   - brute-force attempts
   - SQL injection attempts
   - path traversal attempts
3. Print alerts with line numbers.

## Stretch
- Add JSON export of alerts.
- Add a CLI for custom regex patterns.
- Add a live tail mode.

## Integration
This lab can later power:
- a "Log Scanner" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from threat patterns
