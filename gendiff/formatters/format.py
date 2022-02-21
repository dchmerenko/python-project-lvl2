"""Format difference module."""

from gendiff.formatters.json import get_json_format_output
from gendiff.formatters.plain import get_plain_format_output
from gendiff.formatters.stylish import get_stylish_format_output

JSON = 'json'
PLAIN = 'plain'
STYLISH = 'stylish'


def format_diff(diff, format_name):
    """Format difference.

    Args:
        diff: list of differences
        format_name: format name

    Returns:
        multi-line string with differences

    Raises:
        ValueError: wrong output format
    """
    formatter = {
        JSON: get_json_format_output,
        PLAIN: get_plain_format_output,
        STYLISH: get_stylish_format_output,
    }

    if format_name is None:
        format_name = STYLISH

    format_output = formatter.get(format_name, None)

    if not format_output:
        raise ValueError('Error: wrong output format.')

    return format_output(diff)
