"""Generate_diff module."""

from collections import namedtuple

import yaml

UNCHANGED = 0
ADDED = 1
REMOVED = 2
UPDATED = 3
NESTED = 4

data_prefix = {
    ADDED: '+',
    REMOVED: '-',
}

INDENT = '    '

DiffItem = namedtuple('DiffItem', 'key, status, value')


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

    data_diff = get_data_diff(data1, data2)

    if format_name == 'plain':
        return get_plain_format_output(data_diff)
    return get_stylish_format_output(data_diff)


def get_data_diff(data1, data2):
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
            status, value = NESTED, get_data_diff(value1, value2)
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


def get_stylish_format_output(data, nest_level=0):
    """Return data in stylish output format.

    Args:
        data: diff data
        nest_level: nesting level

    Returns:
        multi-line string with differences
    """

    def get_line(prefix, key, value):
        """Format line.

        Args:
            prefix: prefix
            key: key
            value: value

        Returns:
            Formatted line
        """
        return '{indent}  {prefix} {key}: {value}'.format(
            indent=indent,
            prefix=prefix,
            key=key,
            value=get_stylish_format_output(value, nest_level + 1),
        )

    result = []
    indent = INDENT * nest_level

    if isinstance(data, list):
        lines = map(
            lambda diff_item: get_stylish_format_output(diff_item, nest_level),
            data,
        )
        line = '\n'.join(('{', *lines, indent + '}'))
    elif isinstance(data, dict):
        lines = map(
            lambda key: get_line(' ', key, data[key]),
            data,
        )
        line = '\n'.join(('{', *lines, indent + '}'))
    elif isinstance(data, DiffItem):
        if data.status == UPDATED:
            removed_line = get_line('-', data.key, data.value[0])
            added_line = get_line('+', data.key, data.value[1])
            line = '\n'.join((removed_line, added_line))
        else:
            prefix = data_prefix.get(data.status, ' ')
            line = get_line(prefix, data.key, data.value)
    else:
        line = str(data)

    result.append(line)

    return '\n'.join(result)


def get_plain_format_output(data, key=''):
    """Return data in plain output format.

    Args:
        data: diff data
        key: data key

    Returns:
        multi-line string with differences
    """
    def str_value(value):
        """Get string representation for value.

        Args:
            value: value

        Returns:
            Value or '[complex value]'
        """
        return '[complex value]' if isinstance(value, dict) else repr(value)

    def get_key(child_key):
        """Get key for nested value.

        Args:
            child_key: child_key

        Returns:
            Key for nested value
        """
        return '{0}.{1}'.format(key, child_key) if key else child_key

    result = []

    for diff_item in data:
        if diff_item.status == UNCHANGED:
            continue
        elif diff_item.status == ADDED:
            line = "Property '{key}' was added with value: {value}".format(
                key=get_key(diff_item.key),
                value=str_value(diff_item.value),
            )
        elif diff_item.status == REMOVED:
            line = "Property '{key}' was removed".format(
                key=get_key(diff_item.key),
            )
        elif diff_item.status == UPDATED:
            line_msg = "Property '{key}' was updated. From {old} to {new}"
            line = line_msg.format(
                key=get_key(diff_item.key),
                old=str_value(diff_item.value[0]),
                new=str_value(diff_item.value[1]),
            )
        elif diff_item.status == NESTED:
            line = get_plain_format_output(
                diff_item.value,
                key=get_key(diff_item.key),
            )
        else:
            line = 'Wrong diff item status'

        result.append(line)

    return '\n'.join(result)
