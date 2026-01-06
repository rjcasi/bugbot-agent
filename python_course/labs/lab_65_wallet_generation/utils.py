from cryptography.hazmat.primitives.asymmetric import ec

def generate_wallet():
    print('Generating EC keypair...')
    key = ec.generate_private_key(ec.SECP256K1())
    public = key.public_key()
    print('Private key generated (not exported).')
    print('Public key:', public.public_numbers())