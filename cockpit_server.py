from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

from src.bugbot_agent.agent import Agent
from src.bugbot_agent.organ_hub import OrganHub
from src.bugbot_agent.organs.red_blue_cockpit.routes import router as rbapp_router, init_cockpit

app = FastAPI()

# -----------------------------
#   TEMPLATES + STATIC
# -----------------------------
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# -----------------------------
#   NEW COCKPIT UI (root)
# -----------------------------
@app.get("/")
def cockpit(request: Request):
    return templates.TemplateResponse("cockpit.html", {"request": request})

# -----------------------------
#   AGENT + ORGAN HUB
# -----------------------------
agent = Agent()
organ_hub = OrganHub(agent)
init_cockpit(agent)

# -----------------------------
#   RB-APP ORGAN ROUTES
# -----------------------------
app.include_router(rbapp_router, prefix="/rbapp")

# -----------------------------
#   OLD STATIC PANELS (optional)
# -----------------------------
app.mount("/cockpit", StaticFiles(directory="cockpit"), name="cockpit")

@app.get("/robotics")
def robotics():
    return FileResponse("cockpit/robotic_arena.html")

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

@app.get("/physics_arena")
def physics_arena():
    return FileResponse("cockpit/physics_arena.html")

# -----------------------------
#   SERVER LAUNCHER
# -----------------------------
if __name__ == "__main__":
    uvicorn.run("cockpit_server:app", host="127.0.0.1", port=8000, reload=True)