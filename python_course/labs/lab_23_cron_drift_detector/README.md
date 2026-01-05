# Lab 23 — Cron Job Drift Detector (Scheduled Task Integrity Monitor)

## Goal
Build a Python script that reads system cron jobs, stores a baseline, and detects drift over time.

## Skills
- reading crontab
- parsing scheduled tasks
- baseline capture
- drift detection
- defensive automation

## Tasks
1. Read system cron jobs.
2. Save baseline to JSON.
3. Compare current cron entries to baseline.
4. Detect:
   - new cron jobs
   - deleted cron jobs
   - modified cron jobs
   - suspicious commands
5. Print alerts.

## Stretch
- Add per‑user cron monitoring.
- Add timestamped drift logs.
- Add CLI flags for baseline vs check mode.

## Integration
This lab can later power:
- a "Cron Integrity" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from scheduled task drift
