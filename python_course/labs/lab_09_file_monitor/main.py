import time
from utils import scan_folder

FOLDER = "sample_data"
INTERVAL = 2  # seconds

def main():
    print("=== File Monitor (Defense Script) ===")
    print(f"Monitoring folder: {FOLDER}\n")

    previous = scan_folder(FOLDER)

    while True:
        time.sleep(INTERVAL)
        current = scan_folder(FOLDER)

        # Detect added files
        added = set(current.keys()) - set(previous.keys())
        for f in added:
            print(f"[+] Added: {f}")

        # Detect removed files
        removed = set(previous.keys()) - set(current.keys())
        for f in removed:
            print(f"[-] Removed: {f}")

        # Detect modified files
        for f in current:
            if f in previous and current[f] != previous[f]:
                print(f"[!] Modified: {f}")

        previous = current

if __name__ == "__main__":
    main()
