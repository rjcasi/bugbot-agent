# telemetry/emitter.py
import time
import json

def emit(event_type, pattern, data=None):
    payload = {
        "timestamp": time.time(),
        "event": event_type,
        "pattern": pattern,
        "data": data or {}
    }
    print(json.dumps(payload), flush=True)