#!/usr/bin/env python
"""Difference Calculator main script."""

import argparse

from gendiff.gendiff import generate_diff


def main():  # noqa: WPS210
    """Calculate file difference."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        default='stylish',
        help='set format of output',
    )
    args = parser.parse_args()

    file_path1 = args.first_file
    file_path2 = args.second_file
    format_name = args.format

    diff = generate_diff(file_path1, file_path2, format_name=format_name)

    print(diff)


if __name__ == '__main__':
    main()
