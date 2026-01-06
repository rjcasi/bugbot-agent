import os

BASE = "python_course/labs"

LABS = {
    # ---------------- RED TEAM ----------------
    "lab_75_red_recon_chain": {
        "files": {
            "README.md": "# Lab 75 – Red Team Recon Chain\n\nChain recon steps safely against your own local targets.",
            "main.py": "from utils import run_chain\n\nif __name__ == '__main__':\n    run_chain()",
            "utils.py": "import requests\n\ndef run_chain():\n    print('Running recon chain...')\n    urls = ['http://localhost:5000', 'http://localhost:5000/api']\n    for u in urls:\n        try:\n            r = requests.get(u)\n            print(f'{u} -> {r.status_code}')\n        except:\n            print(f'{u} unreachable')",
        }
    },

    "lab_76_red_fuzz_chain": {
        "files": {
            "README.md": "# Lab 76 – Red Team Fuzz Chain\n\nChain fuzzing steps safely.",
            "main.py": "from utils import fuzz_chain\n\nif __name__ == '__main__':\n    fuzz_chain()",
            "utils.py": "import requests\n\ndef fuzz_chain():\n    print('Running fuzz chain...')\n    payloads = [None, '', {'key':'A'*500}]\n    for p in payloads:\n        try:\n            r = requests.post('http://localhost:5000/api/test', json=p)\n            print(f'Payload {p} -> {r.status_code}')\n        except:\n            print('Error sending payload')",
        }
    },

    "lab_77_red_attack_surface_map": {
        "files": {
            "README.md": "# Lab 77 – Attack Surface Mapping (Safe)\n\nMap your own local attack surface.",
            "main.py": "from utils import map_surface\n\nif __name__ == '__main__':\n    map_surface()",
            "utils.py": "def map_surface():\n    print('Mapping attack surface...')\n    endpoints = ['/','/login','/api/test','/upload']\n    for e in endpoints:\n        print('Found endpoint:', e)",
        }
    },

    "lab_78_red_safe_exploit_sim": {
        "files": {
            "README.md": "# Lab 78 – Safe Exploit Simulation\n\nSimulate harmless exploit logic.",
            "main.py": "from utils import simulate\n\nif __name__ == '__main__':\n    simulate()",
            "utils.py": "def simulate():\n    print('Simulating exploit (safe)...')\n    print('Sending harmless payload to local test server.')",
        }
    },

    # ---------------- BLUE TEAM ----------------
    "lab_79_blue_log_defense": {
        "files": {
            "README.md": "# Lab 79 – Blue Team Log Defense\n\nAnalyze logs for suspicious patterns.",
            "main.py": "from utils import analyze\n\nif __name__ == '__main__':\n    analyze()",
            "utils.py": "def analyze():\n    logs = ['OK','OK','FAILED LOGIN','OK']\n    for l in logs:\n        if 'FAILED' in l:\n            print('Alert:', l)\n        else:\n            print('Normal:', l)",
        }
    },

    "lab_80_blue_anomaly_detector": {
        "files": {
            "README.md": "# Lab 80 – Blue Team Anomaly Detector\n\nDetect anomalies in simple datasets.",
            "main.py": "from utils import detect\n\nif __name__ == '__main__':\n    detect()",
            "utils.py": "def detect():\n    values = [10, 12, 11, 50, 13]\n    avg = sum(values)/len(values)\n    for v in values:\n        if abs(v - avg) > 20:\n            print('Anomaly:', v)\n        else:\n            print('Normal:', v)",
        }
    },

    "lab_81_blue_firewall_sim": {
        "files": {
            "README.md": "# Lab 81 – Firewall Simulation\n\nSimulate allow/deny rules.",
            "main.py": "from utils import simulate\n\nif __name__ == '__main__':\n    simulate()",
            "utils.py": "def simulate():\n    rules = {'/admin': 'DENY', '/': 'ALLOW'}\n    for path, rule in rules.items():\n        print(f'{path}: {rule}')",
        }
    },

    "lab_82_blue_incident_response": {
        "files": {
            "README.md": "# Lab 82 – Incident Response Simulation\n\nSimulate a safe IR workflow.",
            "main.py": "from utils import respond\n\nif __name__ == '__main__':\n    respond()",
            "utils.py": "def respond():\n    print('Incident detected: abnormal login attempts')\n    print('Step 1: Contain')\n    print('Step 2: Eradicate')\n    print('Step 3: Recover')",
        }
    },

    # ---------------- GREY TEAM ----------------
    "lab_83_grey_recon_bot": {
        "files": {
            "README.md": "# Lab 83 – Grey Team Recon Bot\n\nAutomate recon tasks safely.",
            "main.py": "from utils import run_bot\n\nif __name__ == '__main__':\n    run_bot()",
            "utils.py": "import requests\n\ndef run_bot():\n    print('Running recon bot...')\n    try:\n        r = requests.get('http://localhost:5000')\n        print('Status:', r.status_code)\n    except:\n        print('Target unreachable')",
        }
    },

    "lab_84_grey_fuzz_bot": {
        "files": {
            "README.md": "# Lab 84 – Grey Team Fuzz Bot\n\nAutomate safe fuzzing tasks.",
            "main.py": "from utils import run_bot\n\nif __name__ == '__main__':\n    run_bot()",
            "utils.py": "import requests\n\ndef run_bot():\n    print('Running fuzz bot...')\n    payloads = ['', None]\n    for p in payloads:\n        try:\n            r = requests.post('http://localhost:5000/api/test', json=p)\n            print('Payload sent ->', r.status_code)\n        except:\n            print('Error sending payload')",
        }
    },

    "lab_85_grey_drift_bot": {
        "files": {
            "README.md": "# Lab 85 – Grey Team Drift Bot\n\nMonitor drift automatically.",
            "main.py": "from utils import monitor\n\nif __name__ == '__main__':\n    monitor()",
            "utils.py": "import time, os\n\ndef monitor():\n    print('Monitoring entropy drift...')\n    for _ in range(5):\n        print('Entropy:', os.urandom(4).hex())\n        time.sleep(1)",
        }
    },

    "lab_86_grey_pipeline": {
        "files": {
            "README.md": "# Lab 86 – Grey Team Automation Pipeline\n\nChain recon + fuzz + drift safely.",
            "main.py": "from utils import pipeline\n\nif __name__ == '__main__':\n    pipeline()",
            "utils.py": "import requests, os\n\ndef pipeline():\n    print('Running automation pipeline...')\n    try:\n        r = requests.get('http://localhost:5000')\n        print('Recon:', r.status_code)\n    except:\n        print('Recon failed')\n    print('Entropy:', os.urandom(4).hex())",
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

print("Lab Pack G created successfully!")
