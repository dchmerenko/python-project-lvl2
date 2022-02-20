"""Read data from a file."""
import json
import os

import yaml


def read_file(file_path):
    """Read file content.

    Args:
        file_path: path to file

    Returns:
        file content, file type

    Raises:
        ValueError: wrong file type
    """
    file_types = {
        '.json': 'json',
        '.yml': 'yaml',
        '.yaml': 'yaml',
    }

    _, extension = os.path.splitext(file_path)
    file_type = file_types.get(extension.lower(), None)

    if not file_type:
        raise ValueError("Wrong file type: '{0}'. Only '{1}' allowed.".format(
            file_path,
            ', '.join(sorted(set(file_types.values()))),
        ))

    with open(file_path) as data_file:
        file_content = data_file.read()

    return file_content, file_type


def read_data(file_content, file_type):
    """Read data from file.

    Args:
        file_content: file content
        file_type: file type

    Returns:
        parsed file data
    """
    data_parsers = {
        'json': json.loads,
        'yaml': yaml.safe_load,
    }

    return data_parsers[file_type](file_content)
