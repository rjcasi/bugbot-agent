from utils import connect_rpc, get_balance, wei_to_eth

# Public RPC (read-only, safe)
RPC_URL = "https://rpc.ankr.com/eth"  # free, rate-limited, safe

def main():
    print("=== Python Blockchain Reader (Read-Only) ===\n")

    address = input("Enter Ethereum address (default: Vitalik's): ").strip()
    if not address:
        address = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"  # public, safe

    print(f"\nConnecting to RPC: {RPC_URL}")
    w3 = connect_rpc(RPC_URL)

    print(f"Reading balance for: {address}")
    balance_wei = get_balance(w3, address)
    balance_eth = wei_to_eth(balance_wei)

    print("\n=== Balance ===")
    print(f"Wei:  {balance_wei}")
    print(f"ETH:  {balance_eth:.6f}")

if __name__ == "__main__":
    main()
