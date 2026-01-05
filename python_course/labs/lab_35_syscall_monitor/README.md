# Lab 35 — System Call Drift Detector (strace-based Behavior Monitor)

## Goal
Build a Python script that attaches to a process using `strace`, captures system calls, stores a baseline, and detects drift.

## Skills
- using strace
- syscall frequency analysis
- baseline capture
- drift detection
- suspicious syscall heuristics

## Tasks
1. Attach to a PID using strace.
2. Capture system calls for a short window.
3. Save baseline to JSON.
4. Compare current syscall frequencies to baseline.
5. Detect:
   - new syscalls
   - missing syscalls
   - frequency drift
   - suspicious syscalls
6. Print alerts.

## Stretch
- Add syscall sequence analysis.
- Add per-thread syscall tracking.
- Add timestamped drift logs.

## Integration
This lab can later power:
- a "Syscall Behavior" tile in the Cybernaut cockpit
- RB‑App defensive automation
- Evolution Organ learning from behavioral drift patterns
