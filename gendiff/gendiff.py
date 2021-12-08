"""Generate_diff module."""

from gendiff.data_reader import read_data
from gendiff.formatters.json_formatter import get_json_format_output
from gendiff.formatters.plain import get_plain_format_output
from gendiff.formatters.stylish import get_stylish_format_output

ADDED = '+'
MODIFIED = '%'
NESTED = '>'
REMOVED = '-'
UNCHANGED = '='


def generate_diff(file_path1, file_path2, format_name):
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

    formatter = {
        'json': get_json_format_output,
        'plain': get_plain_format_output,
        'stylish': get_stylish_format_output,
    }

    format_diff = formatter.get(format_name, get_stylish_format_output)

    return format_diff(diff)


def get_diff(data1, data2):
    """Return a data difference.

    Args:
        data1: first data
        data2: second data

    Returns:
        list of differences

    diff = [
        {
            "key": key,
            "type": 'added',
            "value": data2[key],
        },
        ...
    ]
    """
    diff = []

    added_keys = data2.keys() - data1.keys()
    removed_keys = data1.keys() - data2.keys()

    for key in sorted(data1.keys() | data2.keys()):
        record = {'key': key}
        value1, value2 = data1.get(key), data2.get(key)

        if key in removed_keys:
            record['type'], record['value'] = REMOVED, value1
        elif key in added_keys:
            record['type'], record['value'] = ADDED, value2
        elif value1 == value2:
            record['type'], record['value'] = UNCHANGED, value1
        elif is_nested(value1, value2):
            record['type'], record['value'] = NESTED, get_diff(value1, value2)
        else:
            record['type'], record['value'] = MODIFIED, (value1, value2)

        diff.append(record)

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
