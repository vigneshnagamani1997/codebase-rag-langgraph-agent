import os
from app.rag.chunking import chunk_python_file
from app.db.chroma import collection

def ingest_repo(repo_path):
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                chunks = chunk_python_file(path)

                for i, chunk in enumerate(chunks):
                    collection.add(
                        documents=[chunk["code"]],
                        metadatas=[{
                            "file": path,
                            "name": chunk["name"],
                            "type": chunk["type"]
                        }],
                        ids=[f"{path}-{i}"]
                    )