"""Plain formatter."""

import json

from gendiff.gendiff import ADDED, MODIFIED, NESTED, REMOVED


def get_plain_format_output(diff, parent_key=''):
    """Recursively return data in plain output format.

    Args:
        diff: diff data
        parent_key: parent key

    Returns:
        multi-line string with differences in plain format
    """
    lines = []

    records = {
        record['key']: (record['type'], record['value']) for record in diff
    }

    for key, (record_type, record_value) in records.items():
        if record_type == ADDED:
            line = "Property '{0}' was added with value: {1}".format(
                combine_key(parent_key, key),
                format_value(record_value),
            )
        elif record_type == MODIFIED:
            line = "Property '{0}' was updated. From {1} to {2}".format(
                combine_key(parent_key, key),
                format_value(record_value[0]),
                format_value(record_value[1]),
            )
        elif record_type == NESTED:
            line = get_plain_format_output(
                record_value,
                combine_key(parent_key, key),
            )
        elif record_type == REMOVED:
            line = "Property '{0}' was removed".format(
                combine_key(parent_key, key),
            )
        else:
            continue

        if line:
            lines.append(line)

    return '\n'.join(lines)


def format_value(record_value):
    """Return string representation for property value.

    Args:
        record_value: property value

    Returns:
        Plain property value or '[complex value]'
    """
    if isinstance(record_value, dict):
        return '[complex value]'
    return json.JSONEncoder().encode(record_value).replace('"', "'")


def combine_key(parent_key, child_key):
    """Combine keys for nested property.

    Args:
        parent_key: parent key
        child_key: child key

    Returns:
        combined key
    """
    return '{0}.{1}'.format(parent_key, child_key) if parent_key else child_key
