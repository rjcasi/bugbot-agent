from web3 import Web3

def connect_rpc(rpc_url: str):
    """Connect to a blockchain RPC endpoint."""
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    if not w3.is_connected():
        raise ConnectionError("Could not connect to RPC endpoint.")
    return w3

def get_balance(w3, address: str):
    """Return balance in Wei."""
    return w3.eth.get_balance(address)

def wei_to_eth(wei: int) -> float:
    return wei / 10**18
