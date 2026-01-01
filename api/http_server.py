from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from api.http_routes import router as http_router
from api.websocket_routes import router as ws_router

app = FastAPI()

# Include routes
app.include_router(http_router)
app.include_router(ws_router)

# Serve cockpit static files
app.mount("/cockpit", StaticFiles(directory="cockpit", html=True), name="cockpit")

@app.get("/", response_class=HTMLResponse)
def root():
    with open("cockpit/index.html", "r") as f:
        return f.read()
