import json

from src.docusearch.indexer import build_index


def test_build_index_creates_json_file(tmp_path):
    data_dir = tmp_path / "raw"
    index_dir = tmp_path / "index"
    index_path = index_dir / "chunks.json"

    data_dir.mkdir()
    sample_file = data_dir / "sample.txt"
    sample_file.write_text("Large language models are powerful.", encoding="utf-8")

    chunks = build_index(
        data_dir=str(data_dir),
        index_path=str(index_path),
        chunk_size=300,
    )

    assert len(chunks) == 1
    assert index_path.exists()

    loaded = json.loads(index_path.read_text(encoding="utf-8"))
    assert len(loaded) == 1
    assert loaded[0]["file_name"] == "sample.txt"
    assert "text" in loaded[0]