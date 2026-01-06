import hashlib, os

def store_password():
    password = b'mypassword'
    salt = os.urandom(16)
    print('Salt:', salt.hex())
    dk = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
    print('Derived key:', dk.hex())