import random
import string
import time

def generate_random_fuzz_string(length=32):
    """Generate a random fuzz string of ASCII characters."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))


def generate_and_record_fuzz(num_patterns=10, length=32, record_list=None):
    """
    Generate fuzz patterns and optionally record them into a shared list.
    Returns a list of fuzz strings.
    """

    patterns = []

    for _ in range(num_patterns):
        fuzz = generate_random_fuzz_string(length)
        patterns.append({
            "timestamp": time.time(),
            "pattern": fuzz
        })

        if record_list is not None:
            record_list.append(fuzz)

    return patterns
