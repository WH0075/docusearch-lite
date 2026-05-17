import argparse

from src.docusearch.config import load_config
from src.docusearch.indexer import build_index
from src.docusearch.searcher import search, load_index


def main():
    parser = argparse.ArgumentParser(description="DocuSearch-Lite CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("ingest")

    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("query")
    search_parser.add_argument("--top_k", type=int, default=5)

    subparsers.add_parser("stats")

    args = parser.parse_args()
    config = load_config()

    index_path = f"{config["index_dir"]}/chunks.json"


    if args.command == "ingest":
        chunks = build_index(
            data_dir=config["data_dir"],
            index_path=index_path,
            chunk_size=config["chunk_size"],
        )
        print(f"Built index with {len(chunks)} chunks.")

    elif args.command == "search":
        results = search(args.query, index_path=index_path, top_k=args.top_k)

        if not results:
            print(f"No results found for query: {args.query}")
            return
        
        for i, item in enumerate(results, start=1):
            print(f"\n[{i}] score={item['score']} file={item['file_name']}")
            print(item["text"][:300])

    elif args.command == "stats":
        chunks = load_index(index_path)
        print(f"Total chunks: {len(chunks)}")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()