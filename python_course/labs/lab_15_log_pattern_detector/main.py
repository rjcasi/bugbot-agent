from utils import scan_log

LOG_PATH = "sample.log"  # You can change this

def main():
    print("=== Suspicious Log Pattern Detector (Lab 15) ===\n")

    alerts = scan_log(LOG_PATH)

    if alerts is None:
        print(f"[!] Log file not found: {LOG_PATH}")
        return

    if not alerts:
        print("[✓] No suspicious patterns detected.")
        return

    print("[!] Suspicious activity detected:\n")
    for line_num, text, matches in alerts:
        print(f"Line {line_num}: {text}")
        print(f"  → Matches: {', '.join(matches)}\n")

if __name__ == "__main__":
    main()
