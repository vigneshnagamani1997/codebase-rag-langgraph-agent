from fastapi import APIRouter
router = APIRouter()

@router.get('/agent')
def agent(q:str): return {'answer': q}
