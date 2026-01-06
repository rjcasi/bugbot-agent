from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def verify_demo():
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = key.public_key()
    msg = b'test'
    sig = key.sign(msg, padding.PKCS1v15(), hashes.SHA256())
    print('Verifying...')
    public_key.verify(sig, msg, padding.PKCS1v15(), hashes.SHA256())
    print('Verified!')