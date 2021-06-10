import pytest
from gendiff.gendiff import generate_diff


@pytest.fixture
def plain_file_diff():
    """Return plain files diff example."""
    return open('tests/fixtures/file1_file2_diff').read()


@pytest.fixture
def nested_file_diff():
    """Return nested files diff example."""
    return open('tests/fixtures/file3_file4_diff').read()


def test_generate_diff_json(plain_file_diff):
    """Test plain json files differences."""
    assert plain_file_diff == generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json',
    )


def test_generate_diff_nested_json(nested_file_diff):
    """Test nested json file differences."""
    assert nested_file_diff == generate_diff(
        'tests/fixtures/file3.json',
        'tests/fixtures/file4.json',
    )


def test_generate_diff_yaml(plain_file_diff):
    """Test plain yaml files differences."""
    assert plain_file_diff == generate_diff(
        'tests/fixtures/file1.yml',
        'tests/fixtures/file2.yaml',
    )


def test_generate_diff_nested_yaml(nested_file_diff):
    """Test nested yaml files differences."""
    assert nested_file_diff == generate_diff(
        'tests/fixtures/file3.yml',
        'tests/fixtures/file4.yml',
    )
