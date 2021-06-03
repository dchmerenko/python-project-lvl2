import pytest
import subprocess

from test_generate_diff import plain_file_diff


@pytest.fixture
def gendiff_help_message():
    """Return script help message."""
    return open("tests/fixtures/gendiff_help_message").read()


def test_scripts_gendiff_help_message(gendiff_help_message):
    assert gendiff_help_message == subprocess.check_output(
        ["gendiff", "-h"],
        universal_newlines=True,
    )


def test_scripts_plain_json(plain_file_diff):
    assert plain_file_diff == subprocess.check_output(
        ["gendiff", "tests/fixtures/file1.json", "tests/fixtures/file2.json"],
        universal_newlines=True,
    )[:-1]  # delete last '\n'
