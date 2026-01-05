import hashlib
import base64

def sha256_file(path: str) -> str:
    """Compute SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def sha256_string(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()

def b64_encode(s: str) -> str:
    return base64.b64encode(s.encode()).decode()

def b64_decode(s: str) -> str:
    return base64.b64decode(s.encode()).decode()
