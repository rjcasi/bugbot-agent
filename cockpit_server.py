from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

app = FastAPI()

# Mount cockpit folder for HTML panels
app.mount("/cockpit", StaticFiles(directory="cockpit"), name="cockpit")

# -----------------------------
#   ROOT PANEL (index.html)
# -----------------------------
@app.get("/")
def root():
    return FileResponse("cockpit/index.html")


# -----------------------------
#   EXISTING PANELS
# -----------------------------
@app.get("/robotics")
def robotics():
    return FileResponse("cockpit/robotic_arena.html")


# -----------------------------
#   NEW ORGANS (4 panels)
# -----------------------------
@app.get("/causal_set")
def causal_set():
    return FileResponse("cockpit/causal_set.html")


@app.get("/embeddings")
def embeddings():
    return FileResponse("cockpit/embeddings.html")


@app.get("/fourier_surface")
def fourier_surface():
    return FileResponse("cockpit/fourier_surface.html")


@app.get("/robotics_panel")
def robotics_panel():
    return FileResponse("cockpit/robotics_panel.html")


# -----------------------------
#   PHYSICS ARENA (Unified Organ)
# -----------------------------
@app.get("/physics_arena")
def physics_arena():
    return FileResponse("cockpit/physics_arena.html")


# -----------------------------
#   SERVER LAUNCHER
# -----------------------------
if __name__ == "__main__":
    uvicorn.run("cockpit_server:app", host="127.0.0.1", port=8000, reload=True)