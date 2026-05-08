import json
from app.rag.retriever import retrieve

def precision_at_k(retrieved, relevant):
    return len(set(retrieved) & set(relevant)) / len(retrieved)

def recall_at_k(retrieved, relevant):
    return len(set(retrieved) & set(relevant)) / len(relevant)

def run_eval():
    with open("app/evals/dataset.json") as f:
        data = json.load(f)

    precisions = []
    recalls = []

    for item in data:
        query = item["query"]
        relevant_docs = item["relevant_docs"]

        docs, _ = retrieve(query)
        retrieved_ids = docs  # simplify

        precisions.append(precision_at_k(retrieved_ids, relevant_docs))
        recalls.append(recall_at_k(retrieved_ids, relevant_docs))

    print("Avg Precision:", sum(precisions)/len(precisions))
    print("Avg Recall:", sum(recalls)/len(recalls))