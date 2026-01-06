import os

BASE = "python_course/labs"

LABS = {
    "lab_51_bug_bounty_scope": {
        "files": {
            "README.md": "# Lab 51 – Bug Bounty Scope Reading\n\nLearn how to read program scopes safely.",
            "main.py": "from utils import show_scope\n\nif __name__ == '__main__':\n    show_scope()",
            "utils.py": "def show_scope():\n    print('Bug Bounty Scope Rules:')\n    print('- Test only assets explicitly listed')\n    print('- Never test production without permission')\n    print('- Avoid user data')\n    print('- Follow rate limits')",
        }
    },

    "lab_52_vuln_classification": {
        "files": {
            "README.md": "# Lab 52 – Vulnerability Classification\n\nLearn common vulnerability categories.",
            "main.py": "from utils import classify\n\nif __name__ == '__main__':\n    classify()",
            "utils.py": "def classify():\n    vulns = ['XSS', 'CSRF', 'IDOR', 'SQLi', 'SSRF']\n    for v in vulns:\n        print('Category:', v)",
        }
    },

    "lab_53_safe_poc": {
        "files": {
            "README.md": "# Lab 53 – Safe Proof of Concept\n\nLearn how to write safe PoCs for your own apps.",
            "main.py": "from utils import demo\n\nif __name__ == '__main__':\n    demo()",
            "utils.py": "def demo():\n    print('Safe PoC Example:')\n    print('Send harmless payload to your own test server.')",
        }
    },

    "lab_54_recon_automation": {
        "files": {
            "README.md": "# Lab 54 – Recon Automation\n\nAutomate safe recon tasks.",
            "main.py": "from utils import run_recon\n\nif __name__ == '__main__':\n    run_recon()",
            "utils.py": "import requests\n\ndef run_recon():\n    print('Running recon automation...')\n    r = requests.get('https://example.com')\n    print('Status:', r.status_code)",
        }
    },

    "lab_55_asset_mapping": {
        "files": {
            "README.md": "# Lab 55 – Asset Mapping\n\nLearn how to map assets safely.",
            "main.py": "from utils import map_assets\n\nif __name__ == '__main__':\n    map_assets()",
            "utils.py": "def map_assets():\n    assets = ['api.example.com', 'dev.example.com', 'test.example.com']\n    for a in assets:\n        print('Asset:', a)",
        }
    },

    "lab_56_responsible_disclosure": {
        "files": {
            "README.md": "# Lab 56 – Responsible Disclosure\n\nLearn how to write safe disclosure reports.",
            "main.py": "from utils import template\n\nif __name__ == '__main__':\n    template()",
            "utils.py": "def template():\n    print('Disclosure Template:')\n    print('- Summary')\n    print('- Steps to reproduce')\n    print('- Impact')\n    print('- Suggested fix')",
        }
    },

    "lab_57_bug_report_writer": {
        "files": {
            "README.md": "# Lab 57 – Bug Report Writer\n\nPractice writing structured bug reports.",
            "main.py": "from utils import write_report\n\nif __name__ == '__main__':\n    write_report()",
            "utils.py": "def write_report():\n    print('Bug Report Example:')\n    print('Title: Input validation issue')\n    print('Impact: Low')\n    print('Fix: Add sanitization')",
        }
    },

    "lab_58_safe_attack_sim": {
        "files": {
            "README.md": "# Lab 58 – Safe Attack Simulation\n\nSimulate attacks safely against your own local apps.",
            "main.py": "from utils import simulate\n\nif __name__ == '__main__':\n    simulate()",
            "utils.py": "def simulate():\n    print('Simulating safe attack...')\n    print('Sending harmless payload to local test server.')",
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

print("Lab Pack D created successfully!")
