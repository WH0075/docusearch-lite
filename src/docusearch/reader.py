from pathlib import Path
from src.docusearch.cleaner import clean_text

def read_text_file(file_path: Path) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def load_documents(data_dir: str) -> list[dict]:
    documents = []
    base_dir = Path(data_dir)

    if not base_dir.exists():
        raise FileNotFoundError(f"Data directory not found: {data_dir}")

    for path in base_dir.rglob("*"):
        if path.suffix.lower() not in [".txt", ".md"]:
            continue
        
        text = read_text_file(path)
        text = clean_text(text)
        documents.append({
            "file_path": str(path),
            "file_name": path.name,
            "text": text,
        })
    
    if not documents:
        raise ValueError(f"No readable documents found in: {data_dir}")

    return documents
