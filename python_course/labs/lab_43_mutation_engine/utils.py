import random, string

def mutate(value):
    ops=[
        lambda v: v + random.choice(string.ascii_letters),
        lambda v: v[::-1],
        lambda v: v.upper(),
        lambda v: v * 2,
        lambda v: '',
        lambda v: 'A' * random.randint(1, 500),
    ]
    return random.choice(ops)(value)