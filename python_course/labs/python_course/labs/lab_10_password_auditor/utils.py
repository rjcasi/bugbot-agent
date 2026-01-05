import math
import re

def entropy(password: str) -> float:
    """Estimate password entropy based on character set size."""
    charset = 0
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[^a-zA-Z0-9]", password):
        charset += 32  # rough estimate for symbols

    if charset == 0:
        return 0.0

    return len(password) * math.log2(charset)

def score(password: str) -> int:
    """Return a score from 0–100."""
    s = 0

    # Length
    if len(password) >= 8:
        s += 20
    if len(password) >= 12:
        s += 20

    # Character variety
    if re.search(r"[a-z]", password):
        s += 10
    if re.search(r"[A-Z]", password):
        s += 10
    if re.search(r"[0-9]", password):
        s += 10
    if re.search(r"[^a-zA-Z0-9]", password):
        s += 10

    # Penalties
    if re.fullmatch(r"[a-zA-Z]+", password):
        s -= 10
    if re.fullmatch(r"[0-9]+", password):
        s -= 20

    return max(0, min(100, s))

def rating(score: int) -> str:
    if score < 30:
        return "Weak"
    if score < 60:
        return "Moderate"
    if score < 80:
        return "Strong"
    return "Very Strong"
