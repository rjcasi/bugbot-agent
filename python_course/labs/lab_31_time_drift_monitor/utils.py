import json
import time
import socket
import struct

NTP_SERVER = "pool.ntp.org"
NTP_PORT = 123
NTP_DELTA = 2208988800  # seconds between 1900 and 1970

def get_ntp_time(server=NTP_SERVER):
    """Return NTP time in seconds since epoch or None on failure."""
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.settimeout(2)

        msg = b'\x1b' + 47 * b'\0'
        client.sendto(msg, (server, NTP_PORT))
        data, _ = client.recvfrom(48)

        if data:
            t = struct.unpack("!12I", data)[10]
            return t - NTP_DELTA
    except Exception:
        return None

def get_local_time():
    return time.time()

def save_baseline(offset, path="time_baseline.json"):
    with open(path, "w") as f:
        json.dump({"offset": offset}, f, indent=4)

def load_baseline(path="time_baseline.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)["offset"]
    except FileNotFoundError:
        return None

def detect_drift(old_offset, new_offset, threshold=2.0):
    """Return drift messages if offset changes significantly."""
    drifts = []

    if abs(new_offset - old_offset) > threshold:
        drifts.append(
            f"Time drift detected: offset changed {old_offset:.3f}s → {new_offset:.3f}s"
        )

    return driftsimport json
import time
import socket
import struct

NTP_SERVER = "pool.ntp.org"
NTP_PORT = 123
NTP_DELTA = 2208988800  # seconds between 1900 and 1970

def get_ntp_time(server=NTP_SERVER):
    """Return NTP time in seconds since epoch or None on failure."""
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.settimeout(2)

        msg = b'\x1b' + 47 * b'\0'
        client.sendto(msg, (server, NTP_PORT))
        data, _ = client.recvfrom(48)

        if data:
            t = struct.unpack("!12I", data)[10]
            return t - NTP_DELTA
    except Exception:
        return None

def get_local_time():
    return time.time()

def save_baseline(offset, path="time_baseline.json"):
    with open(path, "w") as f:
        json.dump({"offset": offset}, f, indent=4)

def load_baseline(path="time_baseline.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)["offset"]
    except FileNotFoundError:
        return None

def detect_drift(old_offset, new_offset, threshold=2.0):
    """Return drift messages if offset changes significantly."""
    drifts = []

    if abs(new_offset - old_offset) > threshold:
        drifts.append(
            f"Time drift detected: offset changed {old_offset:.3f}s → {new_offset:.3f}s"
        )

    return drifts
