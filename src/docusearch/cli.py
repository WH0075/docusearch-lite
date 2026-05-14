from config import load_config
from logger import get_logger
from reader import load_documents
from chunker import chunk_text


def main():
    config = load_config()

    logger = get_logger(log_file=config["log_file"])

    logger.info("DocuSearch-Lite started.")
    logger.info("Config loaded successfully.")
    logger.info(f"Config content: {config}")

    docs = load_documents(config["data_dir"])
    logger.info(f"Loaded {len(docs)} documents.")

    all_chunks = []
    for doc in docs:
        chunks = chunk_text(
            doc["text"],
            chunk_size = config["chunk_size"],
            overlap = 50,
        )
        all_chunks.extend(chunks)
    
    logger.info(f"Create {len(all_chunks)} chunks.")

    print("DocuSearch-Lite is running.")
    print("Config loaded successfully.")
    print(config)

    print("Documents loaded:")
    print(docs)

    print("Chunks created:")
    print(all_chunks)
    

if __name__ == "__main__":
    main()