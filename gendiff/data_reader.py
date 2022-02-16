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
        'json': json.load,
        'yaml': yaml.safe_load,
    }

    _, extension = os.path.splitext(file_path)

    file_type = file_types.get(extension.lower(), None)

    if not file_type:
        raise ValueError('Wrong file type: {file_path}')

    with open(file_path) as parsed_file:
        parsed_data = data_parsers[file_type](parsed_file)

    return parsed_data
