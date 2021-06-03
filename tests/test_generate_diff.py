import pytest
from gendiff.gendiff import generate_diff


@pytest.fixture
def plain_json_diff():
    """Return plain json files diff example."""
    return open('tests/fixtures/file1.json_file2.json_diff').read()


def test_generate_diff(plain_json_diff):
    """Test plain json files differences."""
    assert plain_json_diff == generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json',
    )
