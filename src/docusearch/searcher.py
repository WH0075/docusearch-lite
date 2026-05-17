import json
from pathlib import Path


def load_index(index_path: str) -> list[dict]:
    path = Path(index_path)
    if not path:
        raise FileNotFoundError(f"Index file not found: {index_path}")
    
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def simple_score(query: str, text: str) -> int:
    query_terms = query.lower().split()
    text_lower = text.lower()
    return sum(text_lower.count(term) for term in query_terms)


def search(query: str, index_path: str, top_k: int = 5) -> list[dict]:
    chunks = load_index(index_path)
    results = []

    for chunk in chunks:
        score = simple_score(query, chunk["text"])
        if score > 0:
            item = chunk.copy()
            item["score"] = score
            results.append(item)
        
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top_k]