"""Plain formatter."""

from gendiff.lib import ADDED, NESTED, REMOVED, UNCHANGED, UPDATED


def get_plain_format_output(diff, parent_key=''):
    """Recursively return data in plain output format.

    Args:
        diff: diff data
        parent_key: parent key

    Returns:
        multi-line string with differences in plain format
    """
    result = []

    for diff_item in diff:
        if diff_item.status == UNCHANGED:
            continue
        elif diff_item.status == ADDED:
            line = "Property '{0}' was added with value: {1}".format(
                combine_key(parent_key, diff_item.key),
                format_value(diff_item.value),
            )
        elif diff_item.status == REMOVED:
            line = "Property '{0}' was removed".format(
                combine_key(parent_key, diff_item.key),
            )
        elif diff_item.status == UPDATED:
            line = "Property '{0}' was updated. From {1} to {2}"
            line = line.format(
                combine_key(parent_key, diff_item.key),
                format_value(diff_item.value[0]),
                format_value(diff_item.value[1]),
            )
        elif diff_item.status == NESTED:
            line = get_plain_format_output(
                diff_item.value,
                combine_key(parent_key, diff_item.key),
            )
        else:
            line = 'Wrong diff item status'

        result.append(line)

    return '\n'.join(result)


def format_value(value):
    """Return string representation for property value.

    Args:
        value: property value

    Returns:
        Plain property value or '[complex value]'
    """
    return '[complex value]' if isinstance(value, dict) else repr(value)


def combine_key(parent_key, child_key):
    """Combine keys for nested property.

    Args:
        parent_key: parent key
        child_key: child key

    Returns:
        combined key
    """
    return '{0}.{1}'.format(parent_key, child_key) if parent_key else child_key
