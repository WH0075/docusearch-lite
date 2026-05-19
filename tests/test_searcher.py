import json
import pytest

from src.docusearch.searcher import load_index, simple_score, search


def test_load_index_success(tmp_path):
    index_path = tmp_path / "chunks.json"
    data = [
        {
            "doc_id": 0,
            "chunk_id": 0,
            "file_name": "sample.txt",
            "file_path": "sample.txt",
            "text": "AI agents can use tools."
        }
    ]
    index_path.write_text(json.dumps(data), encoding="utf-8")
    
    chunks = load_index(str(index_path))

    assert len(chunks) == 1
    assert chunks[0]["file_name"] == "sample.txt"


def test_missing_index_file(tmp_path):
    missing_path = tmp_path / "missing.json"

    with pytest.raises(FileNotFoundError):
        load_index(str(missing_path))


def test_simple_score_counts_terms():
    score = simple_score("agent tools", "Agent agents can use tools.")

    assert score >= 2


def test_search_returns_matching_results(tmp_path):
    index_path = tmp_path / "chunks.json"
    data = [
        {
            "doc_id": 0,
            "chunk_id": 0,
            "file_name": "agent.md",
            "file_path": "agent.md",
            "text": "AI agents can use tools."
        },
        {
            "doc_id": 1,
            "chunks_id": 0,
            "file_name": "other.md",
            "file_path": "other.md",
            "text": "This document is about cooking."
        }
    ]
    index_path.write_text(json.dumps(data), encoding="utf-8")

    results = search("agent", str(index_path), top_k=5)

    assert len(results) == 1
    assert results[0]["file_name"] == "agent.md"
    assert results[0]["score"] > 0


def test_empty_query(tmp_path):
    index_path = tmp_path / "chunks.json"
    index_path.write_text("[]", encoding="utf-8")

    with pytest.raises(ValueError):
        search("", str(index_path))


def test_blank_query(tmp_path):
    index_path = tmp_path / "chunks.json"
    index_path.write_text("[]", encoding="utf-8")

    with pytest.raises(ValueError):
        search("  ", str(index_path))


def test_invaild_top_k(tmp_path):
    index_path = tmp_path / "chunks.json"
    index_path.write_text("[]", encoding="utf-8")

    with pytest.raises(ValueError):
        search("agent", str(index_path), top_k=0)