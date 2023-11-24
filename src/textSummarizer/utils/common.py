import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations    # using decorator for datatype errors handling
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read yaml file and return a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the YAML file.
    Raises:
        ValueError: If the YAML file is empty.
        e: If the file is empty.
    Return:
        ConfigBox: A ConfigBox instance.
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'YAML file: {path_to_yaml} loaded successfully')
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError('YAML file is empty')
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create a list of directories.

    Args:
        path_to_directories (list): List of paths of directories.
        verbose (bool, optional): Ignore if multiple directories are to be created. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'Created directory at: {path}')


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get size in kilobytes.

    Args:
        path (Path): Path of the file.
    Returns:
        str: Size of the file in kilobytes.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f'~{size_in_kb}KB'