from fastapi import FastAPI
from pydantic import BaseModel

from src.docusearch.config import load_config
from src.docusearch.searcher import search, load_index

app = FastAPI(title="Docusearch-Lite API")


class SearchRequest(BaseModel):
    query: str
    top_k: int = 5


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/search")
def search_api(request: SearchRequest):
    config = load_config()
    index_path = f"{config['index_dir']}/chunks.json"
    results = search(request.query, index_path=index_path, top_k=request.top_k)
    return {"query": request.query, "results": results}


@app.get("/stats")
def stats():
    config = load_config()
    index_path = f"{config['index_dir']}/chunks.json"
    chunks = load_index(index_path)
    return {"total_chunks": len(chunks)}