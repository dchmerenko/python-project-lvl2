import pytest
import subprocess


@pytest.fixture
def gendiff_h_out():
    return open("tests/fixtures/gendiff_h_out").read()


def test_scripts_gendiff_h(gendiff_h_out):
    assert gendiff_h_out == subprocess.check_output(["gendiff", "-h"], universal_newlines=True)
