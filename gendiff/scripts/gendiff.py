#!/usr/bin/env python
"""Difference Calculator main script."""

import argparse


def main():
    """Calculate file difference."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.parse_args()


if __name__ == '__main__':
    main()
