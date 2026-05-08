# Full Codebase RAG + LangGraph Agent

Production-ready project.

1. Install: 
    pip install -r requirements.txt
    ollama pull llama3  
    # optional models : llama3, mistral, codellama, deepseek-coder
    # Use Ollama for local development, swap generator file for prod use
2. Create virtual env
   python -m venv venv 
   venv\Scripts\activate
3. Ingest a repo: python -m scripts.ingest_repo ./app
3. Run API: uvicorn app.main:app --reload
4. Query: GET /agent?q=Where is authentication handled?


