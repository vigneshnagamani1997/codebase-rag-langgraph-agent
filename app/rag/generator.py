import requests

def generate_answer(query, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = f"""
Answer the question using ONLY the context.

Context:
{context}

Question:
{query}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]