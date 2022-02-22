"""Read data from a file."""

import os


def read_file(file_path):
    """Read file content.

    Args:
        file_path: path to file

    Returns:
        file content, file extension
    """
    _, extension = os.path.splitext(file_path)
    extension = extension.lower()

    with open(file_path) as data_file:
        content = data_file.read()

    return content, extension
