# Lab 04 — Input Fuzzer (Safe Testing)

## Goal
Generate random inputs to test how a function behaves under unexpected conditions.

## Skills
- random data generation
- try/except around risky calls
- logging failures

## Tasks
1. Write a function that expects clean input (e.g., integer math).
2. Write a fuzzer that passes random values (strings, ints, None, etc.).
3. Log which inputs cause errors.

## Stretch
- Categorize errors by type.
- Add a summary of error patterns.

## Integration
Later, this can fuzz parts of your agent or RB-App logic in a controlled way.
# Lab 04 — Input Fuzzer (Safe Testing)

## Goal
Use Python to generate random, unexpected inputs to test how a function behaves under stress.

## Skills
- random data generation
- try/except handling
- logging failures
- analyzing error patterns

## Tasks
1. Write a function that expects clean input (e.g., integer math).
2. Write a fuzzer that passes random values (strings, ints, None, lists, etc.).
3. Log which inputs cause errors.
4. Summarize error types.

## Stretch
- Add categories of inputs (numeric, text, edge cases).
- Add a JSON summary report.
- Add a "mutation" mode that slightly alters valid inputs.

## Integration
This lab can later:
- fuzz parts of your Cybernaut agent
- fuzz RB-App endpoints safely
- feed error patterns into the Evolution Organ