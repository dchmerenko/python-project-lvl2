"""Plain formatter."""

import json


def get_plain_format_output(diff, parent_key=''):
    """Recursively return data in plain output format.

    Args:
        diff: diff data
        parent_key: parent key

    Returns:
        multi-line string with differences in plain format
    """
    result = []
    keys = diff.keys()

    for key, value in diff.items():
        if is_updated(key, keys):
            updated_value = diff[get_updated_key(key)]
            line = "Property '{0}' was updated. From {1} to {2}"
            line = line.format(
                combine_key(parent_key, key),
                format_value(value),
                format_value(updated_value),
            )
        elif is_removed(key):
            line = "Property '{0}' was removed".format(
                combine_key(parent_key, key),
            )
        elif is_added(key, keys):
            line = "Property '{0}' was added with value: {1}".format(
                combine_key(parent_key, key),
                format_value(value),
            )
        elif isinstance(value, dict):
            line = get_plain_format_output(
                value,
                combine_key(parent_key, key),
            )
        else:
            continue

        result.append(line)

    return '\n'.join(result)


def strip(key):
    """Strip key from prefix.

    Args:
        key: key

    Returns:
        key stripped from prefix
    """
    if key.startswith('- ') or key.startswith('+ '):
        return key[2:]
    return key


def get_updated_key(key):
    """Return key with updated prefix.

    Args:
        key: key

    Returns:
        key with prefix '+ '
    """
    return '+ ' + strip(key)


def format_value(value):
    """Return string representation for property value.

    Args:
        value: property value

    Returns:
        Plain property value or '[complex value]'
    """
    return '[complex value]' if isinstance(value, dict) else json.JSONEncoder().encode(value).replace('\"', '\'')


def combine_key(parent_key, child_key):
    """Combine keys for nested property.

    Args:
        parent_key: parent key
        child_key: child key

    Returns:
        combined key
    """
    child_key = strip(child_key)
    return '{0}.{1}'.format(parent_key, child_key) if parent_key else child_key


def is_updated(key, keys):
    """Check if key value is an updated value.

    Args:
        key: key
        keys: keys

    Returns:
        True if key value is updated value else False
    """
    return key.startswith('- ') and ('+ ' + strip(key) in keys)


def is_removed(key):
    """Check if key is a key for removed value.

    Args:
        key: key

    Returns:
        True if key value is removed value else False
    """
    return key.startswith('- ')


def is_added(key, keys):
    """Check if key is a key for added value.

    Args:
        key: key
        keys: keys

    Returns:
        True if key value is added value else False
    """
    return key.startswith('+ ') and ('- ' + strip(key) not in keys)
