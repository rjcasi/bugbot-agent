def parse_log_line(line: str):
    """Parse a log line into structured fields."""
    parts = line.strip().split()
    if len(parts) < 5:
        return None

    timestamp = parts[0] + " " + parts[1]
    method = parts[2]
    path = parts[3]
    status = parts[4]
    ip = parts[5] if len(parts) > 5 else "unknown"

    return {
        "timestamp": timestamp,
        "method": method,
        "path": path,
        "status": status,
        "ip": ip
    }
