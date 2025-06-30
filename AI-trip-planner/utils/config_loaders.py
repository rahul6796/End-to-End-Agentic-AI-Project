

import os
import yaml

def load_config(config_path: str = 'config/config.yaml') -> dict:
    """
    this function takes the config file path.
    return the dict of all the configuration inside it.
    """

    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    return config