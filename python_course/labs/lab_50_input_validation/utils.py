def validate():
    tests = ['hello', '<script>', '123', 'DROP TABLE']
    for t in tests:
        safe = t.replace('<','').replace('>','').replace('DROP','')
        print(f'Input: {t} -> Sanitized: {safe}')