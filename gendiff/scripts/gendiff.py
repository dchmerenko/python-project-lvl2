#!/usr/bin/env python
"""Difference Calculator main script."""

import argparse

from gendiff.gendiff import generate_diff


def get_args():
    """Get command line arguments.

    Returns:
        command line args
    """
    parser = argparse.ArgumentParser(description='Generate diff')

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    return parser.parse_args()


def main():
    """Print formatted file difference."""
    args = get_args()

    diff = generate_diff(
        args.first_file,
        args.second_file,
        args.format,
    )

    print(diff)


if __name__ == '__main__':
    main()
