import pytest


@pytest.fixture
def gendiff_help_message():
    """Return script help message."""
    return open("tests/fixtures/gendiff_help_message").read()


@pytest.fixture
def plain_file_plain_format_diff():
    """Return plain files diff example."""
    return open('tests/fixtures/file1_file2_plain_diff').read()


@pytest.fixture
def plain_file_stylish_format_diff():
    """Return plain files diff example."""
    return open('tests/fixtures/file1_file2_stylish_diff').read()


@pytest.fixture
def nested_file_plain_format_diff():
    """Return nested files diff example."""
    return open('tests/fixtures/file3_file4_plain_diff').read()


@pytest.fixture
def nested_file_stylish_format_diff():
    """Return nested files diff example."""
    return open('tests/fixtures/file3_file4_stylish_diff').read()


@pytest.fixture
def nested_file_json_format_diff():
    """Return nested files diff example."""
    return open('tests/fixtures/file3_file4_json_diff').read()


@pytest.fixture
def plain_file_json_format_diff():
    """Return nested files diff example."""
    return open('tests/fixtures/file1_file2_json_diff').read()
