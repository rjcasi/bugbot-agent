import os

BASE = "python_course/labs"

LABS = {
    "lab_59_hashing_basics": {
        "files": {
            "README.md": "# Lab 59 – Hashing Basics\n\nLearn SHA-256 hashing and why it matters.",
            "main.py": "from utils import run_lab\n\nif __name__ == '__main__':\n    run_lab()",
            "utils.py": "import hashlib\n\ndef run_lab():\n    print('Hashing \"hello\" with SHA-256...')\n    h = hashlib.sha256(b'hello').hexdigest()\n    print('Hash:', h)",
        }
    },

    "lab_60_salted_hashing": {
        "files": {
            "README.md": "# Lab 60 – Salted Hashing\n\nLearn how salts protect passwords.",
            "main.py": "from utils import run_lab\n\nif __name__ == '__main__':\n    run_lab()",
            "utils.py": "import hashlib, os\n\ndef run_lab():\n    salt = os.urandom(16)\n    password = b'mypassword'\n    print('Salt:', salt.hex())\n    h = hashlib.sha256(salt + password).hexdigest()\n    print('Salted hash:', h)",
        }
    },

    "lab_61_password_storage": {
        "files": {
            "README.md": "# Lab 61 – Password Storage\n\nLearn safe password hashing using PBKDF2.",
            "main.py": "from utils import store_password\n\nif __name__ == '__main__':\n    store_password()",
            "utils.py": "import hashlib, os\n\ndef store_password():\n    password = b'mypassword'\n    salt = os.urandom(16)\n    print('Salt:', salt.hex())\n    dk = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)\n    print('Derived key:', dk.hex())",
        }
    },

    "lab_62_message_signing": {
        "files": {
            "README.md": "# Lab 62 – Message Signing\n\nLearn how digital signatures work (safe, local).",
            "main.py": "from utils import sign_message\n\nif __name__ == '__main__':\n    sign_message()",
            "utils.py": "from cryptography.hazmat.primitives.asymmetric import rsa, padding\nfrom cryptography.hazmat.primitives import hashes\n\ndef sign_message():\n    print('Generating RSA key pair...')\n    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)\n    public_key = key.public_key()\n\n    message = b'hello world'\n    print('Signing message...')\n    signature = key.sign(message, padding.PKCS1v15(), hashes.SHA256())\n    print('Signature:', signature.hex())\n\n    print('Verifying signature...')\n    public_key.verify(signature, message, padding.PKCS1v15(), hashes.SHA256())\n    print('Signature verified!')",
        }
    },

    "lab_63_signature_verification": {
        "files": {
            "README.md": "# Lab 63 – Signature Verification\n\nVerify digital signatures safely.",
            "main.py": "from utils import verify_demo\n\nif __name__ == '__main__':\n    verify_demo()",
            "utils.py": "from cryptography.hazmat.primitives.asymmetric import rsa, padding\nfrom cryptography.hazmat.primitives import hashes\n\ndef verify_demo():\n    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)\n    public_key = key.public_key()\n    msg = b'test'\n    sig = key.sign(msg, padding.PKCS1v15(), hashes.SHA256())\n    print('Verifying...')\n    public_key.verify(sig, msg, padding.PKCS1v15(), hashes.SHA256())\n    print('Verified!')",
        }
    },

    "lab_64_local_blockchain": {
        "files": {
            "README.md": "# Lab 64 – Local Blockchain Simulation\n\nSimulate a blockchain locally (no real networks).",
            "main.py": "from utils import simulate_chain\n\nif __name__ == '__main__':\n    simulate_chain()",
            "utils.py": "import hashlib, json\n\ndef simulate_chain():\n    print('Simulating blockchain...')\n    block = {'index': 1, 'data': 'hello'}\n    block_str = json.dumps(block).encode()\n    h = hashlib.sha256(block_str).hexdigest()\n    print('Block hash:', h)",
        }
    },

    "lab_65_wallet_generation": {
        "files": {
            "README.md": "# Lab 65 – Wallet Generation (Safe)\n\nGenerate a local keypair (not connected to any chain).",
            "main.py": "from utils import generate_wallet\n\nif __name__ == '__main__':\n    generate_wallet()",
            "utils.py": "from cryptography.hazmat.primitives.asymmetric import ec\n\ndef generate_wallet():\n    print('Generating EC keypair...')\n    key = ec.generate_private_key(ec.SECP256K1())\n    public = key.public_key()\n    print('Private key generated (not exported).')\n    print('Public key:', public.public_numbers())",
        }
    },

    "lab_66_smart_contract_safety": {
        "files": {
            "README.md": "# Lab 66 – Smart Contract Safety\n\nLearn common smart contract vulnerabilities (theory only).",
            "main.py": "from utils import show_vulns\n\nif __name__ == '__main__':\n    show_vulns()",
            "utils.py": "def show_vulns():\n    print('Common Smart Contract Vulnerabilities:')\n    print('- Reentrancy')\n    print('- Integer overflow/underflow')\n    print('- Unchecked external calls')\n    print('- Missing access control')",
        }
    }
}

# --- CREATE EVERYTHING ---
for lab, data in LABS.items():
    lab_path = os.path.join(BASE, lab)
    os.makedirs(lab_path, exist_ok=True)

    for filename, content in data["files"].items():
        with open(os.path.join(lab_path, filename), "w") as f:
            f.write(content)

print("Lab Pack E created successfully!")
