"""Generate_diff module."""

from gendiff.data_reader import read_data
from gendiff.formatters.format import format_diff
from gendiff.get_diff import get_diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """Return file difference.

    Args:
        file_path1: path to first file
        file_path2: path to second file
        format_name: output format selector

    Returns:
        multi-line string with differences
    """
    data1 = read_data(file_path1)
    data2 = read_data(file_path2)

    diff = get_diff(data1, data2)

    return format_diff(diff, format_name)
