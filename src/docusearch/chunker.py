def chunk_text(text: str, chunk_size: int = 300, overlap: int = 50) -> list[str]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")
    
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)
        
        start += chunk_size - overlap
    
    return chunks