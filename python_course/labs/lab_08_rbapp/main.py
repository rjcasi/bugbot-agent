from utils import call_ping, call_action

DEFAULT_URL = "http://127.0.0.1:8000/rbapp"

def main():
    print("=== RB-App Red/Blue Automation Lab ===\n")

    base_url = input(f"Enter RB-App base URL (default: {DEFAULT_URL}): ").strip()
    if not base_url:
        base_url = DEFAULT_URL

    # 1. Ping the organ
    print("\n[1] Pinging RB-App...")
    try:
        ping = call_ping(base_url)
        print("Ping response:", ping)
    except Exception as e:
        print("Ping failed:", e)
        return

    # 2. Action loop
    while True:
        print("\nAvailable actions:")
        print(" 1. red_probe")
        print(" 2. blue_defend")
        print(" 3. status_check")
        print(" 4. exit")

        choice = input("Choose an action: ").strip()

        if choice == "4":
            print("Exiting.")
            break

        action_map = {
            "1": "red_probe",
            "2": "blue_defend",
            "3": "status_check"
        }

        action = action_map.get(choice)
        if not action:
            print("Invalid choice.")
            continue

        print(f"\n[+] Sending action: {action}")
        try:
            result = call_action(base_url, action)
            print("Response:", result)
        except Exception as e:
            print("Action failed:", e)

if __name__ == "__main__":
    main()
