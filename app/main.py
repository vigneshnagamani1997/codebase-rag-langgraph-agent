from fastapi import FastAPI
from app.rag.retriever import retrieve
from app.rag.generator import generate_answer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/query")
def query(q: str):
    docs, meta = retrieve(q)
    answer = generate_answer(q, docs)

    return {
        "answer": answer,
        "sources": meta
    }