from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def sign_message():
    print('Generating RSA key pair...')
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = key.public_key()

    message = b'hello world'
    print('Signing message...')
    signature = key.sign(message, padding.PKCS1v15(), hashes.SHA256())
    print('Signature:', signature.hex())

    print('Verifying signature...')
    public_key.verify(signature, message, padding.PKCS1v15(), hashes.SHA256())
    print('Signature verified!')