from gendiff.gendiff import generate_diff
from tests.fixtures.fixtures import *


def test_generate_plain_json_plain_format_diff(plain_file_plain_format_diff):
    """Test plain json files differences."""
    assert plain_file_plain_format_diff == generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json',
        format_name='plain',
    )


def test_generate_nested_json_stylish_format_diff(nested_file_stylish_format_diff):
    """Test nested json file differences."""
    assert nested_file_stylish_format_diff == generate_diff(
        'tests/fixtures/file3.json',
        'tests/fixtures/file4.json',
    )


def test_generate_plain_yaml_stylish_format_diff(plain_file_stylish_format_diff):
    """Test plain yaml files differences."""
    assert plain_file_stylish_format_diff == generate_diff(
        'tests/fixtures/file1.yml',
        'tests/fixtures/file2.yaml',
    )


def test_generate_nested_yaml_stylish_format_diff(nested_file_stylish_format_diff):
    """Test nested yaml files differences."""
    assert nested_file_stylish_format_diff == generate_diff(
        'tests/fixtures/file3.yml',
        'tests/fixtures/file4.yml',
    )
