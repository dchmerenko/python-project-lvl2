from gendiff.gendiff import generate_diff


def test_generate_diff():
    diff = generate_diff('tests/file1.json', 'tests/file2.json')
    result = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
    assert result == diff
