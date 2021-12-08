"""Script argument parser."""

import argparse


def get_args():
    """Get command line arguments.

    Returns:
        command line args
    """
    parser = argparse.ArgumentParser(description='Generate diff')

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output',
    )

    return parser.parse_args()
