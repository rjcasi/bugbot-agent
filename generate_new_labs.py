import os

BASE = "python_course/labs"

LABS = {
    "lab_36_recon_expanded": {
        "files": {
            "README.md": "# Lab 36 – Recon Expanded\n\nThis lab teaches advanced recon techniques.",
            "main.py": "from utils import run_lab\n\nif __name__ == '__main__':\n    run_lab()",
            "utils.py": "import requests\nfrom bs4 import BeautifulSoup\n\ndef run_lab():\n    print('Running Recon Expanded Lab...')\n    url = 'https://example.com'\n    r = requests.get(url)\n    soup = BeautifulSoup(r.text, 'html.parser')\n    for link in soup.find_all('a'):\n        print('Found link:', link.get('href'))",
        },
        "folders": ["sample_data"]
    },

    "lab_37_api_fuzzer": {
        "files": {
            "README.md": "# Lab 37 – API Fuzzer\n\nSafe API fuzzing against your own local API.",
            "main.py": "from utils import fuzz\n\nif __name__ == '__main__':\n    fuzz()",
            "utils.py": "import requests\n\ndef fuzz():\n    url = 'http://localhost:5000/api/test'\n    payloads = [None, '', 123, [], {}, {'key': 'A' * 1000}]\n    for p in payloads:\n        try:\n            r = requests.post(url, json=p)\n            print(f'Payload: {p} -> {r.status_code}')\n        except Exception as e:\n            print('Error:', e)",
        }
    },

    "lab_38_form_fuzzer": {
        "files": {
            "README.md": "# Lab 38 – Form Fuzzer\n\nTests form validation on your own login endpoint.",
            "main.py": "from utils import fuzz_form\n\nif __name__ == '__main__':\n    fuzz_form()",
            "utils.py": "import requests\n\ndef fuzz_form():\n    url = 'http://localhost:5000/login'\n    usernames = ['admin', 'test', '', 'A'*500]\n    passwords = ['password', '', 'B'*500]\n    for u in usernames:\n        for p in passwords:\n            r = requests.post(url, data={'username': u, 'password': p})\n            print(f'{u}:{p} -> {r.status_code}')",
        }
    },

    "lab_39_header_fuzzer": {
        "files": {
            "README.md": "# Lab 39 – Header Fuzzer\n\nMutates HTTP headers to test robustness.",
            "main.py": "import requests, random, string\n\ndef randstr(n=20):\n    return ''.join(random.choice(string.ascii_letters) for _ in range(n))\n\nif __name__ == '__main__':\n    url = 'http://localhost:5000'\n    for _ in range(10):\n        headers = {randstr(): randstr(), 'User-Agent': randstr()}\n        r = requests.get(url, headers=headers)\n        print('Status:', r.status_code)",
        }
    },

    "lab_40_query_fuzzer": {
        "files": {
            "README.md": "# Lab 40 – Query Fuzzer\n\nTests query parameter handling.",
            "main.py": "import requests\n\nif __name__ == '__main__':\n    url = 'http://localhost:5000/search'\n    params = [{'q': ''}, {'q': 'A'*1000}, {'q': '<script>'}]\n    for p in params:\n        r = requests.get(url, params=p)\n        print(f'{p} -> {r.status_code}')",
        }
    },

    "lab_41_file_fuzzer": {
        "files": {
            "README.md": "# Lab 41 – File Upload Fuzzer\n\nTests file upload validation.",
            "main.py": "import requests, io\n\nif __name__ == '__main__':\n    url = 'http://localhost:5000/upload'\n    files = [\n        ('file', ('empty.txt', io.BytesIO(b''))),\n        ('file', ('big.txt', io.BytesIO(b'A'*100000))),\n        ('file', ('binary.bin', io.BytesIO(b'\\x00\\xFF\\x00\\xFF'))),\n    ]\n    for f in files:\n        r = requests.post(url, files=[f])\n        print(f'{f[1][0]} -> {r.status_code}')",
        },
        "folders": ["sample_data"]
    },

    "lab_42_tcp_fuzzer": {
        "files": {
            "README.md": "# Lab 42 – TCP Protocol Fuzzer\n\nFuzzes your own local TCP service.",
            "main.py": "import socket, time\n\nHOST='127.0.0.1'\nPORT=9000\npayloads=[b'', b'A'*10, b'A'*1000, b'\\x00\\xFF\\x00\\xFF']\n\nif __name__ == '__main__':\n    for p in payloads:\n        s = socket.socket()\n        s.connect((HOST, PORT))\n        s.sendall(p)\n        time.sleep(0.2)\n        s.close()\n        print('Sent:', p)",
        }
    },

    "lab_43_mutation_engine": {
        "files": {
            "README.md": "# Lab 43 – Mutation Engine\n\nCore mutation logic for fuzzing.",
            "main.py": "from utils import mutate\n\nif __name__ == '__main__':\n    for _ in range(10):\n        print(mutate('test'))",
            "utils.py": "import random, string\n\ndef mutate(value):\n    ops=[\n        lambda v: v + random.choice(string.ascii_letters),\n        lambda v: v[::-1],\n        lambda v: v.upper(),\n        lambda v: v * 2,\n        lambda v: '',\n        lambda v: 'A' * random.randint(1, 500),\n    ]\n    return random.choice(ops)(value)",
        }
    }
}

# --- CREATE EVERYTHING ---
for lab, data in LABS.items():
    lab_path = os.path.join(BASE, lab)
    os.makedirs(lab_path, exist_ok=True)

    # Create subfolders
    for folder in data.get("folders", []):
        os.makedirs(os.path.join(lab_path, folder), exist_ok=True)

    # Create files
    for filename, content in data["files"].items():
        with open(os.path.join(lab_path, filename), "w") as f:
            f.write(content)

print("All labs created successfully!")
