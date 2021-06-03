"""Generate_diff module."""

from collections import namedtuple

import yaml

ADDED = '+'
UNCHANGED = ' '
REMOVED = '-'

INDENT = '  '


def generate_diff(file_path1, file_path2):
    """Return file difference.

    Args:
        file_path1: path to first file
        file_path2: path to second file

    Returns:
        multi-line string with differences
    """
    # as json is a valid yaml format, no need to process json separately
    with open(file_path1) as f1:
        data1 = yaml.safe_load(f1)
    with open(file_path2) as f2:
        data2 = yaml.safe_load(f2)

    data_diff = get_data_diff(data1, data2)

    return convert_diff_to_string(data_diff)


def get_data_diff(data1, data2):
    """
    Return a data difference.

    Args:
        data1: first data
        data2: second data

    Returns:
        list of differences
    """
    diff = []
    DiffItem = namedtuple('Item', 'key, prefix, value')

    added_keys = data2.keys() - data1.keys()
    removed_keys = data1.keys() - data2.keys()

    for key in sorted(data1.keys() | data2.keys()):
        if key in removed_keys:
            diff.append(DiffItem(key, REMOVED, data1[key]))
        elif key in added_keys:
            diff.append(DiffItem(key, ADDED, data2[key]))
        # if key is not in removed_keys and added_keys then key is unchanged
        # but value may be different
        elif data1[key] == data2[key]:
            diff.append(DiffItem(key, UNCHANGED, data1[key]))
        else:
            diff.append(DiffItem(key, REMOVED, data1[key]))
            diff.append(DiffItem(key, ADDED, data2[key]))

    return diff


def convert_diff_to_string(diff):
    """
    Convert list of differences to string.

    Args:
        diff: list of differences

    Returns:
        multi-line string with differences
    """
    first_line = '{'
    lines = map(get_formatted_line, diff)
    last_line = '}'

    return '\n'.join((first_line, *lines, last_line))


def get_formatted_line(diff_item):
    """
    Return formatted line for list of differences item.

    Args:
        diff_item: single item from diff list

    Returns:
          formatted line
    """
    return '{indent}{prefix} {key}: {value}'.format(
        indent=INDENT,
        prefix=diff_item.prefix,
        key=diff_item.key,
        value=diff_item.value,
    )
