# flake8: noqa

import subprocess
from tests.fixtures.fixtures import *


def test_scripts_gendiff_help_message(gendiff_help_message):
    """Test script help screen message."""
    assert gendiff_help_message == subprocess.check_output(
        ["gendiff", "-h"],
        universal_newlines=True,
    )


def test_scripts_plain_json_stylish_format(plain_file_stylish_format_diff):
    """Test script process plain json files differences."""
    assert plain_file_stylish_format_diff == subprocess.check_output(
        ["gendiff", "tests/fixtures/file1.json", "tests/fixtures/file2.json"],
        universal_newlines=True,
    ).rstrip()
