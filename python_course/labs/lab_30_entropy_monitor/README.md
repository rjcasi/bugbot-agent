# Lab 30 — System Entropy Drift Detector (Randomness Health Monitor)

## Goal
Build a Python script that monitors system entropy, stores a baseline, and detects drift over time.

## Skills
- reading /proc/sys/kernel/random/entropy_avail
- baseline capture
- drift detection
- defensive automation

## Tasks
1. Read current entropy.
2. Save baseline to JSON.
3. Compare current entropy to baseline.
4. Detect:
   - entropy drops
   - entropy spikes
   - instability patterns
5. Print alerts.

## Stretch
- Add rolling average entropy tracking.
- Add timestamped drift logs.
- Add CLI flags for baseline vs check mode.

## Integration
This lab can later power:
- an "Entropy Health" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from randomness drift patterns
