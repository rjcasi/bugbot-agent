# api/http_routes.py

from fastapi import APIRouter
from core.patterns.registry import pattern_registry
from core.patterns.serializer import serialize_pattern_tree, pattern_tree_to_json

router = APIRouter()

@router.get("/patterns")
def get_patterns():
    xml = serialize_pattern_tree(pattern_registry)
    json_data = pattern_tree_to_json(xml)
    return json_data