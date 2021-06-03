import pytest
from gendiff.gendiff import generate_diff


@pytest.fixture
def plain_json_diff():
    with open('tests/fixtures/file1.json_file2.json_diff') as f:
        return f.read()


def test_generate_diff(plain_json_diff):
    diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')

    assert diff == plain_json_diff
