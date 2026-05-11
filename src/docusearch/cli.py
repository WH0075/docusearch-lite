from config import load_config
from logger import get_logger
from reader import load_documents



def main():
    config = load_config()

    logger = get_logger(log_file=config["log_file"])

    logger.info("DocuSearch-Lite started.")
    logger.info("Config loaded successfully.")
    logger.info(f"Config content: {config}")

    docs = load_documents(config["data_dir"])
    logger.info(f"Loaded {len(docs)} documents.")

    print("DocuSearch-Lite is running.")
    print("Config loaded successfully.")
    print(config)

    print("Documents loaded:")
    print(docs)

if __name__ == "__main__":
    main()