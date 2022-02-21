"""Read data from a file."""
import os

JSON = 'json'
YAML = 'yaml'


def read_file(file_path):
    """Read file content.

    Args:
        file_path: path to file

    Returns:
        file content, file type
    """
    file_types = {
        '.json': JSON,
        '.yml': YAML,
        '.yaml': YAML,
    }

    _, extension = os.path.splitext(file_path)
    file_type = file_types.get(extension.lower(), None)

    with open(file_path) as data_file:
        file_content = data_file.read()

    return file_content, file_type
