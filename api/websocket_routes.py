# api/websocket_routes.py

from fastapi import APIRouter, WebSocket
import asyncio

from core.patterns.serializer import serialize_pattern_tree, pattern_tree_to_json
from core.patterns.registry import pattern_registry

router = APIRouter()

@router.websocket("/patterns")
async def pattern_tree_stream(ws: WebSocket):
    await ws.accept()

    while True:
        xml = serialize_pattern_tree(pattern_registry)
        json_data = pattern_tree_to_json(xml)
        await ws.send_text(json_data)
        await asyncio.sleep(1.0)