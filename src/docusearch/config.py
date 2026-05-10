import yaml
from pathlib import Path

def load_config(config_path: str = "configs/config.yaml") -> dict:
    """
    Load project configuration from a YAML file.

    Args:
        config_path: Path to the YAML config file.

    Returns:
        A dictionary containing configuration values.
    
    Raises:
        FileNotFoundError: If the config file does not exist.
        ValueError: If the config file is empty.

    """
    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    with open(path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    if config is None:
        raise ValueError(f"Config file is empty: {config_path}")
    
    return config