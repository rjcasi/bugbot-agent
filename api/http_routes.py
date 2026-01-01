from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from src.cyber_arena.recon_engine import run_recon
from src.cyber_arena.fuzz_engine import generate_fuzz_payloads

router = APIRouter()

# =========================
#   CORE COCKPIT PANELS
# =========================

@router.get("/cyber_arena", response_class=HTMLResponse)
def cyber_arena():
    return open("cockpit/panels/cyber_arena.html").read()

@router.get("/heatmap", response_class=HTMLResponse)
def heatmap():
    return open("cockpit/panels/heatmap.html").read()

@router.get("/raster", response_class=HTMLResponse)
def raster():
    return open("cockpit/panels/raster.html").read()

@router.get("/embedding_projector", response_class=HTMLResponse)
def embedding_projector():
    return open("cockpit/panels/embedding_projector.html").read()

@router.get("/token_visualizer", response_class=HTMLResponse)
def token_visualizer():
    return open("cockpit/panels/token_visualizer.html").read()

@router.get("/model_card", response_class=HTMLResponse)
def model_card():
    return open("cockpit/panels/model_card.html").read()

@router.get("/robotics", response_class=HTMLResponse)
def robotics():
    return open("cockpit/panels/robotics.html").read()

@router.get("/causal_set", response_class=HTMLResponse)
def causal_set():
    return open("cockpit/panels/causal_set.html").read()

@router.get("/embeddings", response_class=HTMLResponse)
def embeddings():
    return open("cockpit/panels/embeddings.html").read()

@router.get("/fourier_surface", response_class=HTMLResponse)
def fourier_surface():
    return open("cockpit/panels/fourier_surface.html").read()

@router.get("/robotics_panel", response_class=HTMLResponse)
def robotics_panel():
    return open("cockpit/panels/robotics_panel.html").read()

@router.get("/physics_arena", response_class=HTMLResponse)
def physics_arena():
    return open("cockpit/panels/physics_arena.html").read()

# =========================
#   NEW CYBERNAUT ORGANS
# =========================

@router.get("/recon", response_class=HTMLResponse)
def recon_panel():
    return open("cockpit/panels/recon_panel.html").read()

@router.get("/fuzz", response_class=HTMLResponse)
def fuzz_panel():
    return open("cockpit/panels/fuzz_panel.html").read()

# =========================
#   API ENDPOINTS
# =========================

@router.get("/recon_data")
def recon_data():
    return {"results": run_recon()}

@router.get("/fuzz_data")
def fuzz_data():
    return {"payloads": generate_fuzz_payloads()}
