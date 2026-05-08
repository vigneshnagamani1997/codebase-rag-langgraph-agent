import chromadb
from chromadb.utils import embedding_functions

client = chromadb.Client()

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = client.get_or_create_collection(
    name="codebase",
    embedding_function=embedding_fn
)