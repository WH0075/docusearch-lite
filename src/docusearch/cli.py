from config import load_config
from logger import get_logger


def main():
    config = load_config()

    logger = get_logger(log_file=config["log_file"])

    logger.info("DocuSearch-Lite started.")
    logger.info("Config loaded successfully.")
    logger.info(f"Config content: {config}")

    print("DocuSearch-Lite is running.")
    print("Config loaded successfully.")
    print(config)

if __name__ == "__main__":
    main()