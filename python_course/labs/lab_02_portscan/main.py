import socket
import time

def scan_port(host: str, port: int) -> bool:
    """Return True if port is open, False otherwise."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((host, port))
        s.close()
        return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

def main():
    host = input("Enter host to scan (default 127.0.0.1): ").strip() or "127.0.0.1"
    print(f"\nScanning {host}...\n")

    start = time.time()
    open_ports = []

    for port in range(20, 1025):
        if scan_port(host, port):
            print(f"[+] Port {port} open")
            open_ports.append(port)

    duration = time.time() - start

    print("\n=== Scan Complete ===")
    print("Open ports:", open_ports)
    print(f"Time taken: {duration:.2f} seconds")

if __name__ == "__main__":
    main()
