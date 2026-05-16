from config import load_config
from logger import get_logger
from indexer import build_index

def main():
    config = load_config()
    logger = get_logger(log_file=config["log_file"])

    logger.info("DocuSearch-Lite started.")
    logger.info("Config loaded successfully.")
    
    index_path = f'{config["index_dir"]}/chunks.json'

    chunks = build_index(
        data_dir=config["data_dir"],
        index_path=index_path,
        chunk_size=config["chunk_size"],
    )

    logger.info(f"Build index with {len(chunks)} chunks.")
    logger.info(f"Index saved to {index_path}")
    

    print("DocuSearch-Lite is running.")
    print(f"Index built successfully: {index_path}")
    print(f"Total chunks: {len(chunks)}")

    
    

if __name__ == "__main__":
    main()