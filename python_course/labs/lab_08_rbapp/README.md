# Lab 08 — RB-App Red/Blue Automation

## Goal
Use Python to talk to your RB-App FastAPI organ and automate red/blue actions.

## Skills
- `requests` with JSON
- calling `/rbapp/ping` and other endpoints
- interpreting responses

## Tasks
1. Call `/rbapp/ping` and print the JSON.
2. Add one more RB-App endpoint (e.g. `/rbapp/action`).
3. Build a simple CLI that triggers actions and shows the response.

## Stretch
- Add a basic "scenario" loop that runs multiple actions.

## Integration
This lab *directly* talks to your BugBot Agent cockpit and RB-App organ.
# Lab 08 — RB-App Red/Blue Automation

## Goal
Use Python to communicate with the RB-App FastAPI organ and automate red/blue actions.

## Skills
- HTTP requests with JSON
- interacting with FastAPI endpoints
- parsing JSON responses
- building automation loops

## Tasks
1. Call `/rbapp/ping` and print the JSON response.
2. Add a second endpoint (e.g., `/rbapp/action`) to trigger a safe simulated action.
3. Build a CLI that lets the user choose actions.
4. Display results in a clean format.

## Stretch
- Add a scenario loop (multiple actions in sequence).
- Add timing and logging.
- Add a JSON output mode.

## Integration
This lab directly interacts with:
- the RB-App organ
- the Cybernaut cockpit
- the Evolution Organ (agent learns from actions)
