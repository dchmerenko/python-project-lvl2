"""Read data from files."""
import os.path
import json
import yaml


def read_data(file_path):
    """Read data from file."""

    file_types = {".json": "json",
                  ".yml": "yaml",
                  ".yaml": "yaml"}

    data_parsers = {"json": json.load,
                    "yaml": yaml.safe_load}

    _, extension = os.path.splitext(file_path)

    file_type = file_types.get(extension.lower(), None)

    if not file_type:
        raise ValueError("Wrong file type: {file_path}")

    with open(file_path) as f:
        data = data_parsers[file_type](f)

    return data
