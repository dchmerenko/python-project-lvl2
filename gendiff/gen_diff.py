"""Generate_diff module."""

import yaml
from gendiff.formatters.plain import get_plain_format_output
from gendiff.formatters.stylish import get_stylish_format_output
from gendiff.lib import ADDED, NESTED, REMOVED, UNCHANGED, UPDATED, DiffItem


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """Return file difference.

    Args:
        file_path1: path to first file
        file_path2: path to second file
        format_name: output format selector

    Returns:
        multi-line string with differences
    """
    # as json is a valid yaml format, no need to process json exclusively
    with open(file_path1) as f1:
        data1 = yaml.safe_load(f1)
    with open(file_path2) as f2:
        data2 = yaml.safe_load(f2)

    diff = get_diff(data1, data2)

    if format_name == 'plain':
        return get_plain_format_output(diff)
    return get_stylish_format_output(diff)


def get_diff(data1, data2):
    """Return a data difference.

    Args:
        data1: first data
        data2: second data

    Returns:
        list of differences
    """
    diff = []

    added_keys = data2.keys() - data1.keys()
    removed_keys = data1.keys() - data2.keys()

    for key in sorted(data1.keys() | data2.keys()):
        value1, value2 = data1.get(key), data2.get(key)

        if key in removed_keys:
            status, value = REMOVED, value1
        elif key in added_keys:
            status, value = ADDED, value2
        elif value1 == value2:
            status, value = UNCHANGED, value1
        elif is_nested(value1, value2):
            status, value = NESTED, get_diff(value1, value2)
        else:
            status, value = UPDATED, (value1, value2)

        diff.append(DiffItem(key, status, value))

    return diff


def is_nested(value1, value2):
    """Check if both values are dict type.

    Args:
        value1: first value
        value2: second value

    Returns:
        True if both values are dict type else False
    """
    return isinstance(value1, dict) and isinstance(value2, dict)
