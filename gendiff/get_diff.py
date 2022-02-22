"""Return a data difference."""

ADDED = 'added'
MODIFIED = 'modified'
NESTED = 'nested'
REMOVED = 'removed'
UNCHANGED = 'unchanged'


def get_diff(old_data, new_data):
    """Return a data difference.

    Args:
        old_data: old data
        new_data: new data

    Returns:
        list of differences

    Raises:
        ValueError: wrong data
    """
    diff = []

    if not is_dict(old_data, new_data):
        raise ValueError(
            "Error: wrong data. "
            "Compared data should have 'key: value' structure.",
        )

    for key in sorted(old_data.keys() | new_data.keys()):
        old_value, new_value = old_data.get(key), new_data.get(key)
        if key not in old_data:
            record_type, record_value = ADDED, new_value
        elif key not in new_data:
            record_type, record_value = REMOVED, old_value
        elif old_value == new_value:
            record_type, record_value = UNCHANGED, old_value
        elif is_dict(old_value, new_value):
            record_type, record_value = NESTED, get_diff(old_value, new_value)
        else:
            record_type, record_value = MODIFIED, [old_value, new_value]

        diff.append({'key': key, 'type': record_type, 'value': record_value})

    return diff


def is_dict(value1, value2):
    """Check if both values are dict type.

    Args:
        value1: first value
        value2: second value

    Returns:
        True if both values are dict type else False
    """
    return isinstance(value1, dict) and isinstance(value2, dict)
