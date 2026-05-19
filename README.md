# DocuSearch-Lite

## 1. Project Introduction

DocuSearch-Lite is a simple local document search system for learning Python engineering.

It supports loading local `.txt` and `.md` documents, cleaning text, splitting documents into chunks, building a JSON index, keyword-based search, CLI commands, FastAPI service, and unit tests.

This project is designed as a small engineering practice project before moving to RAG and Agent systems.

## 2. Features

- Load local `.txt` and `.md` documents
- Clean text by removing extra spaces and excessive newlines
- Split documents into overlapping chunks
- Build a structured JSON index
- Search documents by keyword
- Provide CLI commands
- Provide FastAPI service
- Provide unit tests with pytest
- Use YAML configuration
- Use logging for runtime information

## 3. Project Structure

```text
docusearch-lite/
├── README.md
├── requirements.txt
├── .gitignore
├── pytest.ini
├── configs/
│   └── config.yaml
├── data/
│   ├── raw/
│   ├── processed/
│   └── index/
├── src/
│   └── docusearch/
│       ├── __init__.py
│       ├── cli.py
│       ├── config.py
│       ├── logger.py
│       ├── reader.py
│       ├── cleaner.py
│       ├── chunker.py
│       ├── indexer.py
│       ├── searcher.py
│       └── api.py
└── tests/
    ├── test_cleaner.py
    ├── test_chunker.py
    ├── test_reader.py
    ├── test_searcher.py
    ├── test_config.py
    └── test_indexer.py
```

## 4. Core Modules

### `config.py`

Loads project configuration from `configs/config.yaml`.

### `logger.py`

Creates a logger and writes runtime logs to `logs/app.log`.

### `reader.py`

Loads `.txt` and `.md` files from the local data directory.

### `cleaner.py`

Cleans text by normalizing newlines, removing extra spaces, and stripping leading/trailing whitespace.

### `chunker.py`

Splits long documents into fixed-size chunks with overlap.

### `indexer.py`

Builds a JSON index from local documents. Each chunk record contains:

```json
{
  "doc_id": 0,
  "chunk_id": 0,
  "file_name": "sample.txt",
  "file_path": "data/raw/sample.txt",
  "text": "chunk text"
}
```

### `searcher.py`

Loads the JSON index and performs simple keyword-based top-k search.

### `cli.py`

Provides command-line commands:

- `ingest`
- `search`
- `stats`

### `api.py`

Provides FastAPI endpoints:

- `GET /health`
- `POST /search`
- `GET /stats`

## 5. Installation

Clone the project and enter the project directory:

```bash
cd docusearch-lite
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 6. Configuration

The default configuration file is:

```text
configs/config.yaml
```

Example:

```yaml
data_dir: data/raw
index_dir: data/index
chunk_size: 300
top_k: 5
log_file: logs/app.log
```

## 7. Prepare Sample Documents

Put `.txt` or `.md` files into:

```text
data/raw/
```

Example:

```bash
echo "Large language models are powerful." > data/raw/sample1.txt
printf "# Agent\nAI agents can use tools.\n" > data/raw/sample2.md
```

## 8. CLI Usage

### Build index

```bash
python -m src.docusearch.cli ingest
```

Example output:

```text
Built index with 2 chunks.
```

### Search documents

```bash
python -m src.docusearch.cli search "agent" --top-k 3
```

Example output:

```text
[1] score=2 file=sample2.md
# Agent
AI agents can use tools.
```

### Show index statistics

```bash
python -m src.docusearch.cli stats
```

Example output:

```text
Total chunks: 2
```

## 9. API Usage

Start the FastAPI service:

```bash
uvicorn src.docusearch.api:app --reload
```

Open the interactive API documentation in your browser:

```text
http://127.0.0.1:8000/docs
```

Available endpoints:

### Health check

```text
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

### Search

```text
POST /search
```

Request body:

```json
{
  "query": "agent",
  "top_k": 3
}
```

Response:

```json
{
  "query": "agent",
  "results": [
    {
      "doc_id": 0,
      "chunk_id": 0,
      "file_name": "sample2.md",
      "file_path": "data/raw/sample2.md",
      "text": "# Agent\nAI agents can use tools.",
      "score": 2
    }
  ]
}
```

### Stats

```text
GET /stats
```

Response:

```json
{
  "total_chunks": 2
}
```

## 10. Tests

Run all tests:

```bash
pytest
```

Example output:

```text
20 passed
```

The test suite covers:

- Text cleaning
- Text chunking
- Reader behavior
- Search behavior
- Missing files
- Invalid query
- Invalid top_k
- Configuration loading
- Index building

## 11. Git Ignore Policy

The following files or directories should not be committed:

```text
.venv/
__pycache__/
*.pyc
logs/
data/
```

`data/` and `logs/` are runtime artifacts. The source code, configuration template, and tests should be committed.

## 12. Current Limitations

- Search is based on simple keyword matching
- No embedding-based semantic retrieval yet
- No PDF parser yet
- No RAG generation yet
- No evaluation metrics yet

## 13. Future Work

- Add embedding-based retrieval
- Add PDF parser
- Add RAG generation
- Add search evaluation metrics
- Add better API error responses
- Add more unit tests for API and CLI
- Add support for larger document collections

## 14. Learning Goals

This project is built to practice:

- Linux and WSL development workflow
- Python project structure
- Virtual environment and dependency management
- YAML configuration
- Logging
- File reading and text preprocessing
- Chunking for RAG preparation
- JSON index building
- Keyword search
- CLI development with argparse
- FastAPI service development
- Unit testing with pytest
- Git and GitHub workflow