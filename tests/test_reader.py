import pytest

from src.docusearch.reader import load_documents


def test_load_documents_from_txt(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("hello    world", encoding="utf-8")

    documents = load_documents(str(tmp_path))

    assert len(documents) == 1
    assert documents[0]["file_name"] == "sample.txt"
    assert documents[0]["text"] == "hello world"


def test_load_documents_from_md(tmp_path):
    file_path = tmp_path / "sample.md"
    file_path.write_text("# Agent\nAI agents can use tools.", encoding="utf-8")

    documents = load_documents(str(tmp_path))

    assert len(documents) == 1
    assert documents[0]["file_name"] == "sample.md"
    assert "AI agents" in documents[0]["text"]


def test_data_dir_not_found(tmp_path):
    missing_dir = tmp_path / "missing"

    with pytest.raises(FileNotFoundError):
        load_documents(str(missing_dir))


def test_no_readable_documents(tmp_path):
    file_path = tmp_path / "image.png"
    file_path.write_text("not a readable document", encoding="utf-8")

    with pytest.raises(ValueError):
        load_documents(str(tmp_path))