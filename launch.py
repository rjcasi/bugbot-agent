import os

PANELS = {
    "1": "spaces/cyber_arena_app/app.py",
    "2": "spaces/heatmap_app/app.py",
    "3": "spaces/raster_app/app.py",
    "4": "spaces/fuzz_generator_app/app.py",
    "5": "spaces/token_visualizer_app/app.py",
    "6": "spaces/model_card_app/app.py",
    "7": "spaces/raster_app/projector_app/app.py",
    "8": "spaces/robotics_arena_app.py/app.py",
}

print("\n=== BugBot-Agent Cockpit ===")
print("1. Cyber Arena")
print("2. Heatmap Panel")
print("3. Raster Panel")
print("4. Fuzz Generator")
print("5. Token Visualizer")
print("6. Model Card Dashboard")
print("7. Embedding Projector")
print("8. Robotics Arena (scaffold)\n")

choice = input("Select a panel: ").strip()

if choice in PANELS:
    os.system(f"python {PANELS[choice]}")
else:
    print("Invalid choice.")
