# Lab 06 — Crypto Basics (Hashing & Encoding)

## Goal
Understand hashing and encoding for integrity and safe handling of data.

## Skills
- `hashlib` (SHA-256)
- `base64`
- comparing hashes

## Tasks
1. Read a file and compute its SHA-256 hash.
2. Base64-encode a string.
3. Compare two hashes and detect changes.

## Stretch
- Build a simple "integrity check" script for a folder.

## Integration
Can feed into a "File Integrity" widget in your cockpit.
# Lab 06 — Crypto Basics (Hashing & Encoding)

## Goal
Learn how to hash and encode data using Python to verify integrity and safely handle sensitive information.

## Skills
- SHA-256 hashing
- Base64 encoding/decoding
- file integrity checks
- comparing hashes

## Tasks
1. Read a file and compute its SHA-256 hash.
2. Base64-encode a string.
3. Compare two hashes to detect changes.
4. Build a simple integrity checker.

## Stretch
- Monitor a folder and detect when files change.
- Export results to JSON.
- Add a CLI interface.

## Integration
This lab can later power:
- a "File Integrity" tile in the Cybernaut cockpit
- defensive monitoring in the Cybernaut agent
- RB-App defensive scenarios
