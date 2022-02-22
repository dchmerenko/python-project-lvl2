"""Parse data module."""

import json

import yaml

JSON = 'json'
YAML = 'yaml'


def parse_data(content, extension):
    """Parse data from content.

    Args:
        content: content
        extension: file extension

    Returns:
        parsed data

    Raises:
        ValueError: wrong file type
    """
    content_types = {
        '.json': JSON,
        '.yml': YAML,
        '.yaml': YAML,
    }

    content_type = content_types.get(extension, None)

    if content_type is None:
        raise ValueError(
            'Error: wrong content type. Only JSON, YAML are allowed.',
        )

    data_parsers = {
        JSON: json.loads,
        YAML: yaml.safe_load,
    }

    return data_parsers[content_type](content)
