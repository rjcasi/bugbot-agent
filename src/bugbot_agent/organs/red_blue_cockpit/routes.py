# src/bugbot_agent/organs/red_blue_cockpit/routes.py

from fastapi import APIRouter
from pydantic import BaseModel
from .controller import RedBlueCockpit

router = APIRouter()
cockpit = None

# Request models
class FuzzRequest(BaseModel):
    target: str

class EventRequest(BaseModel):
    event: dict


def init_cockpit(agent):
    global cockpit
    cockpit = RedBlueCockpit(agent)
    print("[RB-APP ORGAN] Red/Blue Cockpit initialized.")


@router.post("/rb/fuzz")
def fuzz_route(req: FuzzRequest):
    result = cockpit.run_fuzz(req.target)
    return {"result": result}


@router.post("/rb/defend")
def defend_route(req: EventRequest):
    result = cockpit.auto_defend(req.event)
    return {"result": result}


@router.post("/rb/explain")
def explain_route(req: EventRequest):
    result = cockpit.explain(req.event)
    return {"result": result}

@router.get("/ping")
def ping():
    return {"status": "RB-App organ online"}

@router.post("/action")
def action(payload: dict):
    action = payload.get("action", "none")
    return {"received": action, "status": "ok"}
