from utils import entropy, score, rating

def main():
    print("=== Password Strength Auditor ===\n")

    pwd = input("Enter a password to evaluate: ").strip()

    s = score(pwd)
    e = entropy(pwd)
    r = rating(s)

    print("\n=== Results ===")
    print(f"Score:   {s}/100")
    print(f"Entropy: {e:.2f} bits")
    print(f"Rating:  {r}")

    print("\n=== Suggestions ===")
    if len(pwd) < 12:
        print("- Increase length to 12+ characters.")
    if pwd.lower() == pwd or pwd.upper() == pwd:
        print("- Add both uppercase and lowercase letters.")
    if not any(c.isdigit() for c in pwd):
        print("- Add at least one number.")
    if pwd.isalnum():
        print("- Add at least one symbol.")
    if s >= 80:
        print("- Excellent password.")

if __name__ == "__main__":
    main()
