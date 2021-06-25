"""Stylish formatter."""

import json

from gendiff.lib import INDENT


def get_stylish_format_output(data, nest_level=0):
    """Recursively return data in stylish output format.

    Args:
        data: diff data
        nest_level: nesting level

    Returns:
        multi-line string with differences
    """
    result = []
    indent = str(INDENT * nest_level)

    if isinstance(data, dict):
        lines = map(
            lambda key: get_line(indent, key, data[key], nest_level),
            data.keys(),
        )
        line = '\n'.join(('{', *lines, indent + '}'))
    else:
        line = json.JSONEncoder().encode(data)
    result.append(line)

    return '\n'.join(result)


def get_line(indent, key, value, nest_level):
    """Get formatted line(s).

    Args:
        nest_level: nest_level
        indent: indent
        key: key
        value: value

    Returns:
        Formatted line
    """
    prefix = '' if key.startswith('+ ') or key.startswith('- ') else '  '
    return '{indent}  {prefix}{key}: {value}'.format(
        indent=indent,
        prefix=prefix,
        key=key,
        value=get_stylish_format_output(value, nest_level + 1),
    )
