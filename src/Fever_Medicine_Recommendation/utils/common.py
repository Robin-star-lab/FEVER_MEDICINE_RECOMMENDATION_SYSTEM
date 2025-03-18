from box import ConfigBox
import yaml
import os
from pathlib import Path
from ensure import ensure_annotations
from logger import fever_logger
def read_yaml(filepath)->ConfigBox:
    with open(filepath) as yaml_file:
        config_data = yaml.safe_load(yaml_file)
        return  ConfigBox(config_data)
    fever_logger.info(f"Read yaml at: {filepath}")
def create_directories(path_to_directories:list):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        
        fever_logger.info(f"Created directory at path: {path}")


@ensure_annotations
def save_data(filepath:Path):
    with open(filepath, 'w') as data:
        data.write()