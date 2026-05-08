def precision_at_k(relevant, retrieved):
    return len(set(relevant) & set(retrieved)) / len(retrieved)

def recall_at_k(relevant, retrieved):
    return len(set(relevant) & set(retrieved)) / len(relevant)

def mrr(relevant, retrieved):
    for i, doc in enumerate(retrieved):
        if doc in relevant:
            return 1 / (i + 1)
    return 0