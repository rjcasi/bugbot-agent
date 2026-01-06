import hashlib, json

def simulate_chain():
    print('Simulating blockchain...')
    block = {'index': 1, 'data': 'hello'}
    block_str = json.dumps(block).encode()
    h = hashlib.sha256(block_str).hexdigest()
    print('Block hash:', h)