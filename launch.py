import subprocess
import webbrowser
import time
import platform
import os
import sys
from fastapi import FastAPI

# -------------------------------
# FASTAPI BACKEND APP
# -------------------------------

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "status": "BugBot-Agent cockpit is alive",
        "message": "Select a panel from the terminal menu.",
        "panels": [
            "Cyber Arena", "Heatmap Panel", "Raster Panel", "Fuzz Generator",
            "Token Visualizer", "Model Card Dashboard", "Embedding Projector",
            "Robotics Arena (old)", "Causal Set Panel", "Embedding Space Panel",
            "Fourier Surface Panel", "Robotics Panel (new)", "Physics Arena"
        ]
    }

# Optional router imports
try:
    from api.websocket_routes import router as ws_router
    from api.http_routes import router as http_router

    app.include_router(ws_router)
    app.include_router(http_router)
except Exception as e:
    print("\n[WARNING] Could not import routers yet. Backend may still start.")
    print("Error:", e)


# -------------------------------
# COCKPIT PANEL LAUNCHER
# -------------------------------

BASE_URL = "http://127.0.0.1:8000"

def open_panel(route: str):
    """Open a cockpit panel in the default web browser."""
    url = f"{BASE_URL}/{route}"
    print(f"\nOpening panel: {url}\n")
    time.sleep(0.3)

    if platform.system() == "Linux":
        print("WSL detected. Open the URL manually in your Windows browser.")
    else:
        webbrowser.open(url)


def open_cockpit_home():
    """Open the cockpit home page."""
    print("\nOpening cockpit home...\n")
    if platform.system() == "Linux":
        print("WSL detected. Open http://127.0.0.1:8000 manually.")
    else:
        webbrowser.open(BASE_URL)


# -------------------------------
# TERMINAL COCKPIT MENU
# -------------------------------

def cockpit_menu():
    """Terminal-based cockpit menu."""
    while True:
        print("\n=== BUGBOT-AGENT COCKPIT ===")
        print("1. Cyber Arena")
        print("2. Heatmap Panel")
        print("3. Raster Panel")
        print("4. Fuzz Generator")
        print("5. Token Visualizer")
        print("6. Model Card Dashboard")
        print("7. Embedding Projector")
        print("8. Robotics Arena (old)")
        print("9. Exit")

        print("\n--- NEW ORGANS ---")
        print("14. Causal Set Panel")
        print("15. Embedding Space Panel")
        print("16. Fourier Surface Panel")
        print("17. Robotics Panel (new)")
        print("18. Physics Arena (Unified Organ)")

        choice = input("\nSelect a panel: ").strip()

        # Existing cockpit panels
        if choice == "1":
            open_panel("cyber_arena")
        elif choice == "2":
            open_panel("heatmap")
        elif choice == "3":
            open_panel("raster")
        elif choice == "4":
            open_panel("fuzz_generator")
        elif choice == "5":
            open_panel("token_visualizer")
        elif choice == "6":
            open_panel("model_card")
        elif choice == "7":
            open_panel("embedding_projector")
        elif choice == "8":
            open_panel("robotics")

        # New organs
        elif choice == "14":
            open_panel("causal_set")
        elif choice == "15":
            open_panel("embeddings")
        elif choice == "16":
            open_panel("fourier_surface")
        elif choice == "17":
            open_panel("robotics_panel")
        elif choice == "18":
            open_panel("physics_arena")

        elif choice == "9":
            print("\nExiting cockpit.\n")
            break

        else:
            print("\nInvalid choice. Try again.\n")


# -------------------------------
# BACKEND LAUNCHER
# -------------------------------

def run_backend():
    """Start the FastAPI backend using Uvicorn."""
    return subprocess.Popen(["uvicorn", "launch:app", "--reload"])


# -------------------------------
# MAIN ENTRYPOINT
# -------------------------------

if __name__ == "__main__":

    # Prevent Uvicorn reload from re-running the launcher
    if os.environ.get("RUN_MAIN") == "true":
        cockpit_menu()
        sys.exit()

    print("\n=== BUGBOT-AGENT IGNITION SEQUENCE ===")
    print("[OrganHub] Pattern Tree routing initialized.")
    print("[CyberBridge] Online.")
    print("[RoboticsMap] Awaiting telemetry.")
    print("[PhysicsArena] Unified organ activated.")
    print("[WSL Check] Browser auto-launch disabled on Linux.\n")

    backend = run_backend()
    time.sleep(1)
    open_cockpit_home()
    cockpit_menu()
    backend.wait()