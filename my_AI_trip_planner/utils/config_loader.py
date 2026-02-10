import yaml
import os
def load_config(config_path: str = "config.yaml") -> dict:
    """
    Docstring for load_config
    This function will load the configuration from the specified YAML file and return it as a dictionary.
    """
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config