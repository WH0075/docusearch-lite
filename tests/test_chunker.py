import pytest
from src.docusearch.chunker import chunk_text


def test_chunk_text_basic():
    text = "a" * 100
    chunks = chunk_text(text, chunk_size=30, overlap=10)
    assert len(chunks) > 1

def test_chunk_text_invalid_chunk_size():
    with pytest.raises(ValueError):
        chunk_text("hello", chunk_size=0)

def test_chunk_text_invalid_overlap():
    with pytest.raises(ValueError):
        chunk_text("hello", chunk_size=10, overlap=10)
