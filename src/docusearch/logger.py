import logging
from pathlib import Path

def get_logger(name: str = "docusearch", log_file: str = "logs/app.log") -> logging.Logger:
    """
    Create and return a logger.

    Args:
        name: Logger name.
        log_file: Path to the log file.
    
    Returns:
        A configured logger object.
    """

    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(log_file, encoding="utf-8")

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger