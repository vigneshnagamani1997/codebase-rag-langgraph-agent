from app.rag.retriever import retrieve

def search_code(query):
    docs, meta = retrieve(query, k=5)
    return "\n\n".join(docs)