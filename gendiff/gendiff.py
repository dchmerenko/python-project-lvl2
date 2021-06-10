"""Generate_diff module."""

from collections import namedtuple

import yaml

ADDED = '+'
UNCHANGED = ' '
REMOVED = '-'

INDENT = '    '

DiffItem = namedtuple('DiffItem', 'key, prefix, value')


def generate_diff(file_path1, file_path2):
    """Return file difference.

    Args:
        file_path1: path to first file
        file_path2: path to second file

    Returns:
        multi-line string with differences
    """
    # as json is a valid yaml format, no need to process json exclusively
    with open(file_path1) as f1:
        data1 = yaml.safe_load(f1)
    with open(file_path2) as f2:
        data2 = yaml.safe_load(f2)

    data_diff = get_data_diff(data1, data2)

    return make_string(data_diff)


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
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            nested_data = get_data_diff(data1[key], data2[key])
            diff.append(DiffItem(key, UNCHANGED, nested_data))
        else:
            diff.append(DiffItem(key, REMOVED, data1[key]))
            diff.append(DiffItem(key, ADDED, data2[key]))

    return diff


def make_string(child, nest_level=0):
    """
    Convert item to string.

    Args:
        child: item
        nest_level: nesting level

    Returns:
        multi-line string with differences
    """
    result = []
    indent = INDENT * nest_level
    if isinstance(child, list):
        lines = map(
            lambda list_element: make_string(list_element, nest_level),
            child,
        )
        result.extend(('{', *lines, indent + '}'))
    elif isinstance(child, DiffItem):
        line = '{0}  {1} {2}: {3}'.format(
            indent,
            child.prefix,
            child.key,
            make_string(child.value, nest_level + 1),
        )
        result.append(line)
    elif isinstance(child, dict):
        lines = (
            '{0}    {1}: {2}'.format(
                indent,
                key,
                make_string(child_value, nest_level + 1),
            ) for key, child_value in child.items()
        )
        result.extend(('{', *lines, indent + '}'))
    else:
        result.append(str(child))

    return '\n'.join(result)
