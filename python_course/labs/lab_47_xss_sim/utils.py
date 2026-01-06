def simulate():
    print('Simulating XSS (safe)...')
    user_input = '<script>alert(1)</script>'
    print('Unsafe render:', user_input)
    safe = user_input.replace('<','&lt;').replace('>','&gt;')
    print('Safe render:', safe)