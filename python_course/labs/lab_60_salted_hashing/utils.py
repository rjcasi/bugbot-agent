import hashlib, os

def run_lab():
    salt = os.urandom(16)
    password = b'mypassword'
    print('Salt:', salt.hex())
    h = hashlib.sha256(salt + password).hexdigest()
    print('Salted hash:', h)