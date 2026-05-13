from pathlib import Path
from cleaner import clean_text

def read_text_file(file_path: Path) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def load_documents(data_dir: str) -> list[dict]:
    documents = []
    base_dir = Path(data_dir)

    print("Scanning directory:", base_dir)

    for path in base_dir.rglob("*"):
        print("Found path:", path, "suffix:", path.suffix)

        if path.suffix.lower() not in [".txt", ".md"]:
            continue
        
        text = read_text_file(path)
        text = clean_text(text)
        documents.append({
            "file_path": str(path),
            "file_name": path.name,
            "text": text,
        })
    
    return documents
