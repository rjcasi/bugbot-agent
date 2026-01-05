# Lab 24 — Firewall Rule Drift Detector (iptables / ufw Baseline Monitor)

## Goal
Build a Python script that reads firewall rules (iptables or ufw), stores a baseline, and detects drift over time.

## Skills
- iptables inspection
- ufw inspection
- baseline capture
- drift detection
- defensive automation

## Tasks
1. Read firewall rules.
2. Save baseline to JSON.
3. Compare current rules to baseline.
4. Detect:
   - new rules
   - deleted rules
   - modified rules
   - suspicious rules
5. Print alerts.

## Stretch
- Add per‑chain drift detection.
- Add timestamped drift logs.
- Add CLI flags for baseline vs check mode.

## Integration
This lab can later power:
- a "Firewall Integrity" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from firewall drift patterns
