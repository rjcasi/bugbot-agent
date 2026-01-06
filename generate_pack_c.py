import os

BASE = "python_course/labs"

LABS = {
    "lab_44_jwt_auth": {
        "files": {
            "README.md": "# Lab 44 – JWT Authentication\n\nLearn how JWT tokens work and how to secure API endpoints.",
            "main.py": "from utils import run_lab\n\nif __name__ == '__main__':\n    run_lab()",
            "utils.py": "import jwt, datetime\n\nSECRET = 'mysecret'\n\ndef run_lab():\n    print('Generating JWT token...')\n    token = jwt.encode({'user':'test','exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=5)}, SECRET, algorithm='HS256')\n    print('Token:', token)\n    print('Decoding token...')\n    decoded = jwt.decode(token, SECRET, algorithms=['HS256'])\n    print('Decoded:', decoded)",
        }
    },

    "lab_45_rate_limiting": {
        "files": {
            "README.md": "# Lab 45 – Rate Limiting\n\nSimulates rate limiting logic for API protection.",
            "main.py": "from utils import simulate\n\nif __name__ == '__main__':\n    simulate()",
            "utils.py": "import time\n\nMAX_REQ = 5\nWINDOW = 10\n\nrequests_log = []\n\ndef simulate():\n    print('Simulating rate limiting...')\n    for i in range(10):\n        now = time.time()\n        requests_log.append(now)\n        requests_log[:] = [t for t in requests_log if now - t < WINDOW]\n        if len(requests_log) > MAX_REQ:\n            print(f'Request {i}: BLOCKED (rate limit exceeded)')\n        else:\n            print(f'Request {i}: ALLOWED')\n        time.sleep(1)",
        }
    },

    "lab_46_sql_injection_sim": {
        "files": {
            "README.md": "# Lab 46 – SQL Injection Simulation (Safe)\n\nDemonstrates why parameterized queries matter.",
            "main.py": "from utils import run_demo\n\nif __name__ == '__main__':\n    run_demo()",
            "utils.py": "def run_demo():\n    print('Simulating SQL injection (safe)...')\n    user_input = \"' OR '1'='1\"  # classic payload\n    insecure_query = f\"SELECT * FROM users WHERE name = '{user_input}'\"\n    print('Insecure query:', insecure_query)\n    print('Secure version uses parameterized queries instead.')",
        }
    },

    "lab_47_xss_sim": {
        "files": {
            "README.md": "# Lab 47 – XSS Simulation (Safe)\n\nShows how unescaped input can break a page.",
            "main.py": "from utils import simulate\n\nif __name__ == '__main__':\n    simulate()",
            "utils.py": "def simulate():\n    print('Simulating XSS (safe)...')\n    user_input = '<script>alert(1)</script>'\n    print('Unsafe render:', user_input)\n    safe = user_input.replace('<','&lt;').replace('>','&gt;')\n    print('Safe render:', safe)",
        }
    },

    "lab_48_csrf_sim": {
        "files": {
            "README.md": "# Lab 48 – CSRF Simulation (Safe)\n\nExplains how CSRF tokens protect forms.",
            "main.py": "from utils import run_lab\n\nif __name__ == '__main__':\n    run_lab()",
            "utils.py": "import secrets\n\ndef run_lab():\n    print('Generating CSRF token...')\n    token = secrets.token_hex(16)\n    print('Token:', token)\n    print('Validating token...')\n    print('If token matches, request is allowed.')",
        }
    },

    "lab_49_api_hardening": {
        "files": {
            "README.md": "# Lab 49 – API Hardening\n\nLearn safe defaults for building secure APIs.",
            "main.py": "from utils import show_rules\n\nif __name__ == '__main__':\n    show_rules()",
            "utils.py": "def show_rules():\n    print('API Hardening Rules:')\n    print('- Validate all input')\n    print('- Sanitize output')\n    print('- Use HTTPS')\n    print('- Use JWT or OAuth2')\n    print('- Implement rate limiting')\n    print('- Log suspicious activity')",
        }
    },

    "lab_50_input_validation": {
        "files": {
            "README.md": "# Lab 50 – Input Validation\n\nShows how to validate and sanitize user input.",
            "main.py": "from utils import validate\n\nif __name__ == '__main__':\n    validate()",
            "utils.py": "def validate():\n    tests = ['hello', '<script>', '123', 'DROP TABLE']\n    for t in tests:\n        safe = t.replace('<','').replace('>','').replace('DROP','')\n        print(f'Input: {t} -> Sanitized: {safe}')",
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

print("Lab Pack C created successfully!")
