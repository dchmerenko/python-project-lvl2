"""Read data from a file."""
import json
import os

import yaml


def read_data(file_path):
    """Read data from file.

    Args:
        file_path: path to file

    Returns:
        parsed file data

    Raises:
        ValueError: wrong file type
    """
    file_types = {
        '.json': 'json',
        '.yml': 'yaml',
        '.yaml': 'yaml',
    }

    data_parsers = {
        'json': json.loads,
        'yaml': yaml.safe_load,
    }

    _, extension = os.path.splitext(file_path)

    file_type = file_types.get(extension.lower(), None)

    if not file_type:
        raise ValueError('Wrong file type: {file_path}')

    file_content = read_file(file_path)

    return data_parsers[file_type](file_content)


def read_file(file_path):
    """Read file content.

    Args:
        file_path: path to file

    Returns:
        file content
    """
    with open(file_path) as data_file:
        file_content = data_file.read()

    return file_content
