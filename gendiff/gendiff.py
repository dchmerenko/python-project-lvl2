"""Generate_diff module."""

from gendiff.data_reader import read_data
from gendiff.formatters.format import format_diff
from gendiff.lib import ADDED, MODIFIED, NESTED, REMOVED, UNCHANGED


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """Return file difference.

    Args:
        file_path1: path to first file
        file_path2: path to second file
        format_name: output format selector

    Returns:
        multi-line string with differences
    """
    data1 = read_data(file_path1)
    data2 = read_data(file_path2)

    diff = get_diff(data1, data2)

    return format_diff(diff, format_name)


def get_diff(old_data, new_data):
    """Return a data difference.

    Args:
        old_data: old data
        new_data: new data

    Returns:
        list of differences
    """
    diff = []

    for key in sorted(old_data.keys() | new_data.keys()):
        old_value, new_value = old_data.get(key), new_data.get(key)
        if key not in old_data:
            record_type, record_value = ADDED, new_value
        elif key not in new_data:
            record_type, record_value = REMOVED, old_value
        elif old_value == new_value:
            record_type, record_value = UNCHANGED, old_value
        elif is_nested(old_value, new_value):
            record_type, record_value = NESTED, get_diff(old_value, new_value)
        else:
            record_type, record_value = MODIFIED, [old_value, new_value]

        diff.append({'key': key, 'type': record_type, 'value': record_value})

    return diff


def is_nested(old_value, new_value):
    """Check if both values are dict type.

    Args:
        old_value: old value
        new_value: new value

    Returns:
        True if both values are dict type else False
    """
    return isinstance(old_value, dict) and isinstance(new_value, dict)
