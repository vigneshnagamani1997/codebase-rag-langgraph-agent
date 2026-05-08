import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.rag.ingestion import ingest_repo
from app.db.chroma import collection
from app.rag.retriever import retrieve

if __name__ == "__main__":
    repo_path = sys.argv[1]
    ingest_repo(repo_path)
    print("Ingestion complete.")
    print(f"Ingesting file: {repo_path}")
    print("Total docs:", collection.count())
    docs, meta = retrieve("what does ingestion do?")
    print(docs)