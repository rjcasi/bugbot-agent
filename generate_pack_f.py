import os

BASE = "python_course/labs"

LABS = {
    "lab_67_api_drift_monitor": {
        "files": {
            "README.md": "# Lab 67 – API Drift Monitor\n\nDetect changes in API responses over time.",
            "main.py": "from utils import monitor\n\nif __name__ == '__main__':\n    monitor()",
            "utils.py": "import requests, time\n\ndef monitor():\n    url = 'http://localhost:5000/api/test'\n    print('Monitoring API drift...')\n    baseline = None\n    for _ in range(5):\n        r = requests.get(url)\n        if baseline is None:\n            baseline = r.text\n            print('Baseline set.')\n        elif r.text != baseline:\n            print('DRIFT DETECTED!')\n        else:\n            print('No drift.')\n        time.sleep(1)",
        }
    },

    "lab_68_network_latency_drift": {
        "files": {
            "README.md": "# Lab 68 – Network Latency Drift\n\nTrack latency changes over time.",
            "main.py": "from utils import track\n\nif __name__ == '__main__':\n    track()",
            "utils.py": "import time, socket\n\ndef track():\n    host = '127.0.0.1'\n    port = 80\n    print('Tracking latency drift...')\n    for _ in range(5):\n        start = time.time()\n        try:\n            s = socket.socket()\n            s.settimeout(1)\n            s.connect((host, port))\n            s.close()\n            latency = (time.time() - start) * 1000\n            print(f'Latency: {latency:.2f} ms')\n        except:\n            print('Connection failed.')\n        time.sleep(1)",
        }
    },

    "lab_69_system_resource_drift": {
        "files": {
            "README.md": "# Lab 69 – System Resource Drift\n\nMonitor CPU and memory drift (safe).",
            "main.py": "from utils import monitor\n\nif __name__ == '__main__':\n    monitor()",
            "utils.py": "import psutil, time\n\ndef monitor():\n    print('Monitoring CPU/memory drift...')\n    for _ in range(5):\n        cpu = psutil.cpu_percent()\n        mem = psutil.virtual_memory().percent\n        print(f'CPU: {cpu}%, MEM: {mem}%')\n        time.sleep(1)",
        }
    },

    "lab_70_entropy_drift": {
        "files": {
            "README.md": "# Lab 70 – Entropy Drift\n\nSimulate entropy changes over time.",
            "main.py": "from utils import simulate\n\nif __name__ == '__main__':\n    simulate()",
            "utils.py": "import os, time\n\ndef simulate():\n    print('Simulating entropy drift...')\n    for _ in range(5):\n        entropy = os.urandom(8).hex()\n        print('Entropy sample:', entropy)\n        time.sleep(1)",
        }
    },

    "lab_71_route_drift_monitor": {
        "files": {
            "README.md": "# Lab 71 – Route Drift Monitor\n\nSimulate route table drift (safe).",
            "main.py": "from utils import simulate\n\nif __name__ == '__main__':\n    simulate()",
            "utils.py": "def simulate():\n    print('Simulating route drift...')\n    routes = [\n        '192.168.1.0/24 via 192.168.1.1',\n        '192.168.1.0/24 via 192.168.1.254'\n    ]\n    print('Baseline:', routes[0])\n    print('Drifted:', routes[1])",
        }
    },

    "lab_72_process_drift_monitor": {
        "files": {
            "README.md": "# Lab 72 – Process Drift Monitor\n\nDetect changes in running processes.",
            "main.py": "from utils import monitor\n\nif __name__ == '__main__':\n    monitor()",
            "utils.py": "import psutil, time\n\ndef monitor():\n    print('Monitoring process drift...')\n    baseline = {p.pid for p in psutil.process_iter()}\n    time.sleep(2)\n    current = {p.pid for p in psutil.process_iter()}\n    drift = current.symmetric_difference(baseline)\n    print('Process drift:', drift)",
        }
    },

    "lab_73_syscall_drift_sim": {
        "files": {
            "README.md": "# Lab 73 – Syscall Drift Simulation\n\nSimulate syscall pattern drift (safe).",
            "main.py": "from utils import simulate\n\nif __name__ == '__main__':\n    simulate()",
            "utils.py": "def simulate():\n    print('Simulating syscall drift...')\n    baseline = ['open', 'read', 'write']\n    drifted = ['open', 'read', 'write', 'socket']\n    print('Baseline:', baseline)\n    print('Drifted:', drifted)",
        }
    },

    "lab_74_kernel_param_drift": {
        "files": {
            "README.md": "# Lab 74 – Kernel Parameter Drift\n\nSimulate kernel parameter changes (safe).",
            "main.py": "from utils import simulate\n\nif __name__ == '__main__':\n    simulate()",
            "utils.py": "def simulate():\n    print('Simulating kernel parameter drift...')\n    baseline = {'vm.swappiness': 60}\n    drifted = {'vm.swappiness': 10}\n    print('Baseline:', baseline)\n    print('Drifted:', drifted)",
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

print("Lab Pack F created successfully!")
