from utils import sha256_file, sha256_string, b64_encode, b64_decode

FILE_PATH = "sample_data/test.txt"

def main():
    print("=== Python Crypto Basics ===\n")

    # 1. File hashing
    print("[1] File Hashing")
    file_hash = sha256_file(FILE_PATH)
    print(f"SHA-256({FILE_PATH}): {file_hash}\n")

    # 2. String hashing
    print("[2] String Hashing")
    s = "Cybernaut"
    print(f"Input: {s}")
    print("SHA-256:", sha256_string(s), "\n")

    # 3. Base64 encoding
    print("[3] Base64 Encoding")
    encoded = b64_encode(s)
    print("Encoded:", encoded)
    print("Decoded:", b64_decode(encoded), "\n")

    # 4. Integrity check example
    print("[4] Integrity Check Example")
    original_hash = file_hash
    new_hash = sha256_file(FILE_PATH)

    if original_hash == new_hash:
        print("[OK] File integrity verified.")
    else:
        print("[ALERT] File has changed!")

if __name__ == "__main__":
    main()
