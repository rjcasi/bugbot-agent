import re

# Suspicious regex patterns
PATTERNS = {
    "bruteforce": re.compile(r"failed login|authentication failure|invalid password", re.IGNORECASE),
    "sql_injection": re.compile(r"(union select|or 1=1|drop table|--)", re.IGNORECASE),
    "path_traversal": re.compile(r"\.\./|\.\.\\", re.IGNORECASE),
}

def scan_log(path):
    """Yield (line_number, line, matches) for suspicious lines."""
    alerts = []

    try:
        with open(path, "r", errors="ignore") as f:
            for i, line in enumerate(f, start=1):
                matches = []
                for name, pattern in PATTERNS.items():
                    if pattern.search(line):
                        matches.append(name)

                if matches:
                    alerts.append((i, line.strip(), matches))

    except FileNotFoundError:
        return None

    return alerts
