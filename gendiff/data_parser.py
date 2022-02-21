"""Parse data module."""

import json

import yaml
from gendiff.data_reader import JSON, YAML


def parse_data(file_content, file_type):
    """Read data from file.

    Args:
        file_content: file content
        file_type: file type

    Returns:
        parsed file data

    Raises:
        ValueError: wrong file type
    """
    if not file_type:
        raise ValueError(
            'Error: wrong file type. Only JSON, YAML files are allowed.',
        )

    data_parsers = {
        JSON: json.loads,
        YAML: yaml.safe_load,
    }

    return data_parsers[file_type](file_content)
