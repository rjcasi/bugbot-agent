def run_demo():
    print('Simulating SQL injection (safe)...')
    user_input = "' OR '1'='1"  # classic payload
    insecure_query = f"SELECT * FROM users WHERE name = '{user_input}'"
    print('Insecure query:', insecure_query)
    print('Secure version uses parameterized queries instead.')