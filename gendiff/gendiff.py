"""Generate_diff module."""

import json
from collections import namedtuple

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
    with open(file_path1) as f1:
        json1 = json.load(f1)
    with open(file_path2) as f2:
        json2 = json.load(f2)

    json_diff = get_json_diff(json1, json2)

    return convert_diff_to_string(json_diff)


def get_json_diff(json1, json2):
    """
    Return a json difference.

    Args:
        json1: first json
        json2: second json

    Returns:
        list of differences
    """
    diff = []
    # WPS110 Found wrong variable name: Item - Item it's a class name
    Item = namedtuple('Item', 'key, prefix, value')  # noqa: WPS110

    added_keys = json2.keys() - json1.keys()
    removed_keys = json1.keys() - json2.keys()

    for key in sorted(json1.keys() | json2.keys()):
        if key in removed_keys:
            diff.append(Item(key, REMOVED, json1[key]))
        elif key in added_keys:
            diff.append(Item(key, ADDED, json2[key]))
        else:
            if json1[key] == json2[key]:
                diff.append(Item(key, UNCHANGED, json1[key]))
            else:
                diff.append(Item(key, REMOVED, json1[key]))
                diff.append(Item(key, ADDED, json2[key]))

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
