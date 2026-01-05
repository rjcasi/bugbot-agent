import random
import string

def random_string(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def random_input():
    """Generate a random input of various types."""
    options = [
        random.randint(-1000, 1000),
        random.random(),
        None,
        random_string(),
        [],
        {},
        [random.randint(0, 10) for _ in range(3)],
    ]
    return random.choice(options)
