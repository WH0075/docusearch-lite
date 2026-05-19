import pytest

from src.docusearch.config import load_config


def test_missing_config_file(tmp_path):
    missing_config = tmp_path / "missing.yaml"

    with pytest.raises(FileNotFoundError):
        load_config(str(missing_config))


def test_empty_config_file(tmp_path):
    empty_config = tmp_path / "empty.yaml"
    empty_config.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        load_config(str(empty_config))


def test_load_config_success(tmp_path):
    config_file = tmp_path / "config.yaml"
    config_file.write_text(
        "data_dir: data/raw\n"
        "index_dir: data/index\n"
        "chunk_size: 300\n"
        "top_k: 5\n"
        "log_file: logs/app.log\n",
        encoding="utf-8"
    )

    config = load_config(str(config_file))

    assert config["data_dir"] == "data/raw"
    assert config["chunk_size"] == 300
