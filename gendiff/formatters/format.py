"""Format difference module."""

from gendiff.formatters.json import get_json_format_output
from gendiff.formatters.plain import get_plain_format_output
from gendiff.formatters.stylish import get_stylish_format_output


def format_diff(diff, format_name):
    """Format difference.

    Args:
        diff: list of differences
        format_name: format name

    Returns:
        multi-line string with differences
    """
    formatter = {
        'json': get_json_format_output,
        'plain': get_plain_format_output,
        'stylish': get_stylish_format_output,
    }

    format_output = formatter.get(format_name, get_stylish_format_output)

    return format_output(diff)
