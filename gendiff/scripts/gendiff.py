#!/usr/bin/env python
"""Difference Calculator main script."""

import argparse, pprint

from gendiff import generate_diff


def main():
    """Calculate file difference."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        # choices=['plain', 'json'],
                        default='plain',
                        help='set format of output')
    args = parser.parse_args()

    print('first file:', args.first_file)
    print('second file:', args.second_file)
    print('format:', args.format)

    file_path1 = args.first_file
    file_path2 = args.second_file
    format_ = args.format

    diff = generate_diff(file_path1, file_path2)
    pprint.pprint(diff)


if __name__ == '__main__':
    main()
