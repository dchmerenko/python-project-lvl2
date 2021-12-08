#!/usr/bin/env python
"""File difference calculator main script."""

from gendiff.args_parser import get_args
from gendiff.gendiff import generate_diff


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
