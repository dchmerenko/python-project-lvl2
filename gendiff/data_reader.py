"""Read data from files."""
import os.path
import json
import yaml


def read_data(file_path):
    """Read data from file."""

    file_types = {".json": "json",
                  ".yml": "yaml",
                  ".yaml": "yaml"}

    _, extension = os.path.splitext(file_path)

    file_type = file_types.get(extension.lower(), None)

    with open(file_path) as f:
        file_data = f.read()

    return parse_data(file_data, file_type)


def parse_data(file_data, file_type):
    """Load file data to dictionary."""

    data_parsers = {"json": json.load,
                    "yaml": yaml.safe_load}
    if file_type:
        return data_parser[file_type](file_data)
    else:
        raise ValueError("Wrong file type")
