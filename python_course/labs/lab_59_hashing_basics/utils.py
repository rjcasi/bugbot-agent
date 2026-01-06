import hashlib

def run_lab():
    print('Hashing "hello" with SHA-256...')
    h = hashlib.sha256(b'hello').hexdigest()
    print('Hash:', h)