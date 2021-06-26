#!/usr/bin/env python
"""Difference Calculator main script."""

import argparse

from gendiff.gendiff import generate_diff


def get_args():
    """Get command line arguments.

    Returns:
        command line args
    """
    parser = argparse.ArgumentParser(
        description='Compares two text files and shows a difference.',
        usage='%(prog)s [options] <filepath1> <filepath2>',  # noqa:WPS323
    )

    parser.add_argument('first_file', help=argparse.SUPPRESS)
    parser.add_argument('second_file', help=argparse.SUPPRESS)
    parser.add_argument(
        '-f',
        '--format',
        dest='format_name',
        metavar='',
        choices=['json', 'plain', 'stylish'],
        default='stylish',
        help='output format [json | plain | stylish] (default: stylish)',
    )

    return parser.parse_args()


def main():
    """Calculate file difference."""
    args = get_args()

    file_path1 = args.first_file
    file_path2 = args.second_file
    format_name = args.format_name

    diff = generate_diff(file_path1, file_path2, format_name=format_name)

    print(diff)


if __name__ == '__main__':
    main()
