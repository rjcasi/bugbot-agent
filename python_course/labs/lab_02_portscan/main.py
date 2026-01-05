import socket

def scan_port(host: str, port: int) -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((host, port))
        s.close()
        return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

def main():
    host = input("Enter host to scan (e.g. 127.0.0.1): ").strip() or "127.0.0.1"
    print(f"Scanning {host}...")

    open_ports = []
    for port in range(20, 1025):
        if scan_port(host, port):
            print(f"[+] Port {port} open")
            open_ports.append(port)

    print("\nScan complete.")
    print("Open ports:", open_ports)

if __name__ == "__main__":
    main()
