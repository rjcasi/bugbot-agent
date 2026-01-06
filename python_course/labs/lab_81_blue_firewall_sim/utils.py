def simulate():
    rules = {'/admin': 'DENY', '/': 'ALLOW'}
    for path, rule in rules.items():
        print(f'{path}: {rule}')