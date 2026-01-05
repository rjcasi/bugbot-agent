# Lab 09 — File Monitor (Defense Script)

## Goal
Build a Python script that monitors a folder for file changes using hashing and timestamps.

## Skills
- directory scanning
- SHA-256 hashing
- detecting file changes
- defensive automation

## Tasks
1. Scan a folder and record file hashes.
2. Re-scan periodically.
3. Detect added, removed, or modified files.
4. Print alerts in real time.

## Stretch
- Export alerts to JSON.
- Add a log file.
- Add a CLI for choosing the folder.

## Integration
This lab can later power:
- a "File Integrity" tile in the Cybernaut cockpit
- defensive monitoring for RB-App
- Evolution Organ learning from file-change patterns
