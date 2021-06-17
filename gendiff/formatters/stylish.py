"""Stylish formatter."""

from gendiff.lib import INDENT, UPDATED, DiffItem, data_prefix


def get_stylish_format_output(data, nest_level=0):
    """Recursively return data in stylish output format.

    Args:
        data: diff data
        nest_level: nesting level

    Returns:
        multi-line string with differences
    """

    def get_line(prefix, key, value):
        """Get formatted line(s).

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
            lambda dict_key: get_line(' ', dict_key, data[dict_key]),
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
