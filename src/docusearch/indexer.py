import json
from pathlib import Path

from src.docusearch.reader import load_documents
from src.docusearch.cleaner import clean_text
from src.docusearch.chunker import chunk_text


def build_index(data_dir: str, index_path: str, chunk_size: int = 300) -> list[dict]:
    documents = load_documents(data_dir)
    chunks = []

    for doc_id, doc in enumerate(documents):
        text = clean_text(doc["text"])
        doc_chunks = chunk_text(text, chunk_size=chunk_size)

        for chunk_id, chunk in enumerate(doc_chunks):
            chunks.append({
                "doc_id": doc_id,
                "chunk_id": chunk_id,
                "file_name": doc["file_name"],
                "file_path": doc["file_path"],
                "text": chunk,
            })
    
    Path(index_path).parent.mkdir(parents=True, exist_ok=True)

    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

    return chunks