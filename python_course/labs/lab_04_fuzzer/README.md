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
