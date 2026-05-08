from app.db.chroma import collection

def retrieve(query, k=5):
    results = collection.query(
        query_texts=[query],
        n_results=k
    )

    return results["documents"][0], results["metadatas"][0]