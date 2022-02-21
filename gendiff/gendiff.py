"""Generate_diff module."""

from gendiff.data_parser import parse_data
from gendiff.data_reader import read_file
from gendiff.formatters.format import STYLISH, format_diff
from gendiff.get_diff import get_diff


def generate_diff(file_path1, file_path2, format_name=STYLISH):
    """Return file difference.

    Args:
        file_path1: path to first file
        file_path2: path to second file
        format_name: output format selector

    Returns:
        multi-line string with differences
    """
    try:
        content1, type1 = read_file(file_path1)
        content2, type2 = read_file(file_path2)

        data1 = parse_data(content1, type1)
        data2 = parse_data(content2, type2)

        diff = get_diff(data1, data2)
    except (FileNotFoundError, ValueError) as error:
        print(error)
        exit(1)

    return format_diff(diff, format_name)
