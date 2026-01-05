# Lab 22 — User Account Drift Detector (New/Deleted/Suspicious Users)

## Goal
Build a Python script that enumerates system users, stores a baseline, and detects drift over time.

## Skills
- reading /etc/passwd
- identity monitoring
- baseline capture
- drift detection
- defensive automation

## Tasks
1. Read system user accounts.
2. Save baseline to JSON.
3. Compare current users to baseline.
4. Detect:
   - new users
   - deleted users
   - suspicious usernames
5. Print alerts.

## Stretch
- Add UID/GID drift detection.
- Add shell or home directory drift.
- Add timestamped drift logs.

## Integration
This lab can later power:
- a "User Accounts" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from identity drift patterns
