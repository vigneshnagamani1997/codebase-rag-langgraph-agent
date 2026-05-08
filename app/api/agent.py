from fastapi import APIRouter
from app.agent.langgraph_agent import run_agent

router = APIRouter()

@router.get("/agent")
def agent(q: str):
    return {"answer": run_agent(q)}