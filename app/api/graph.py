
from fastapi import APIRouter
from app.utils.graph_builder import build_graph

router = APIRouter()

@router.get("/graph")
def graph():
    return build_graph("./")
