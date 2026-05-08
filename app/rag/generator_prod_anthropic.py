import os
from anthropic import Anthropic

client = Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

def generate_answer(query, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a senior engineer assistant.

Answer the question using ONLY the context below.

Context:
{context}

Question:
{query}
"""

    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text