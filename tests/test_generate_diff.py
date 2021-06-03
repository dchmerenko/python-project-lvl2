import pytest
from gendiff.gendiff import generate_diff


@pytest.fixture
def plain_file_diff():
    """Return plain files diff example."""
    return open('tests/fixtures/file1_file2_diff').read()


def test_generate_diff_json(plain_file_diff):
    """Test plain json files differences."""
    assert plain_file_diff == generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json',
    )


def test_generate_diff_yaml(plain_file_diff):
    """Test plain yaml files differences."""
    assert plain_file_diff == generate_diff(
        'tests/fixtures/file1.yml',
        'tests/fixtures/file2.yaml',
    )
