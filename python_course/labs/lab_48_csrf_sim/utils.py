import secrets

def run_lab():
    print('Generating CSRF token...')
    token = secrets.token_hex(16)
    print('Token:', token)
    print('Validating token...')
    print('If token matches, request is allowed.')