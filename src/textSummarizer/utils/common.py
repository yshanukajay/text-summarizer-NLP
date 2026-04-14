import os
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        """
        Reads a yaml file and returns a ConfigBox object.

        Args:
            path_to_yaml (Path): Path to the yaml file.

        Returns:
            ConfigBox: A ConfigBox object containing the yaml data.
        """
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)

        if not isinstance(content, dict):
            raise BoxValueError("YAML file must contain a dictionary.")

        return ConfigBox(content)
    
    except BoxValueError as e:
        logger.error(f"Error in YAML content: {e}")
        raise

@ensure_annotations
def create_directories(path_to_directories: list[Path], verbose=True) -> None:
    try:
        """
        Creates directories from a list of paths.

        Args:
            path_to_directories (list[Path]): List of paths to create directories.
            verbose (bool, optional): If True, logs the creation of directories. Defaults to True.
        """
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directory created at: {path}")

    except Exception as e:
        logger.error(f"Error creating directories: {e}")
        raise