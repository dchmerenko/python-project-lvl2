"""Stylish formatter."""

import json

from gendiff.lib import ADDED, MODIFIED, NESTED, REMOVED

INDENT = '    '


def get_stylish_format_output(diff, level=0):
    """Recursively return data in stylish output format.

    Args:
        diff: diff data
        level: nesting level

    Returns:
        multi-line string with differences
    """
    lines = []

    for record in diff:
        new_lines = get_lines(
            record['type'],
            record['key'],
            record['value'],
            level + 1,
        )
        lines.extend(new_lines)

    return '\n'.join((
        '{',
        *lines,
        INDENT * level + '}',
    ))


def get_lines(record_type, record_key, record_value, level):
    """Return formatted lines with proper indent.

    Args:
        record_type: diff record type
        record_key: diff record key
        record_value: diff record value
        level: indent level

    Returns:
        formatted lines with proper indent.
    """
    indent = INDENT * level
    prefix = {ADDED: '+', REMOVED: '-'}.get(record_type, ' ')

    if record_type == MODIFIED:
        old_value, new_value = record_value
        old_line = get_lines(REMOVED, record_key, old_value, level)
        new_line = get_lines(ADDED, record_key, new_value, level)
        return [*old_line, *new_line]
    elif record_type == NESTED:
        record_value = get_stylish_format_output(record_value, level)
    elif isinstance(record_value, dict):
        dict_lines = json.dumps(record_value, indent=INDENT).replace('"', '')
        record_value = '\n{indent}'.format(indent=indent).join(
            map(lambda line: line.rstrip(','), dict_lines.split('\n')),
        )
    else:
        record_value = json.JSONEncoder().encode(record_value).strip('"')

    return ['{indent}{prefix} {key}: {value}'.format(
        indent=indent[:-2],
        prefix=prefix,
        key=record_key,
        value=record_value,
    )]
