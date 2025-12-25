import subprocess
import webbrowser
import time

def run_backend():
    return subprocess.Popen(["uvicorn", "launch:app", "--reload"])

def open_cockpit():
    webbrowser.open("http://localhost:8000")

if __name__ == "__main__":
    backend = run_backend()
    time.sleep(1)
    open_cockpit()
    backend.wait()
    