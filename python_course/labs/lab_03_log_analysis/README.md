# Lab 03 — Log Analysis (Blue Team)

## Goal
Use Python to parse log files and surface useful summaries and anomalies.

## Skills
- file I/O
- string parsing / `split`
- basic counting and aggregation

## Tasks
1. Read a log file (e.g., web server log).
2. Count requests per IP.
3. Find the top talkers and print a summary.

## Stretch
- Detect IPs with unusually high activity.
- Write a summary report to a file.

## Integration
Later, this lab can connect to BugBot / Cybernaut logs and visualize in the cockpit.

# Lab 03 — Log Analysis (Blue Team)

## Goal
Use Python to parse log files and extract meaningful defensive insights.

## Skills
- file reading
- string parsing
- counting and aggregation
- anomaly detection

## Tasks
1. Load a sample log file.
2. Count requests per IP address.
3. Identify the top talkers.
4. Detect unusual activity (e.g., too many requests).

## Stretch
- Export results to JSON.
- Add regex-based parsing.
- Add a simple anomaly threshold.

## Integration
This lab can later feed into:
- a "Log Insights" panel in the Cybernaut cockpit
- the Evolution Organ (agent learns from logs)
- RB-App defensive scenarios