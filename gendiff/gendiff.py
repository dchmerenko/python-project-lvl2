"""Generate_diff module."""

# flake8: noqa

from collections import namedtuple

import yaml

ADDED = '+'
UNCHANGED = ' '
REMOVED = '-'

INDENT = '    '

DiffItem = namedtuple('DiffItem', 'key, prefix, value')


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """Return file difference.

    Args:
        file_path1: path to first file
        file_path2: path to second file
        format_name: output format selector

    Returns:
        multi-line string with differences
    """
    # as json is a valid yaml format, no need to process json exclusively
    with open(file_path1) as f1:
        data1 = yaml.safe_load(f1)
    with open(file_path2) as f2:
        data2 = yaml.safe_load(f2)

    data_diff = get_data_diff(data1, data2)

    if format_name == 'plain':
        return get_plain_format_output(data_diff)
    return get_stylish_format_output(data_diff)


def get_data_diff(data1, data2):
    """
    Return a data difference.

    Args:
        data1: first data
        data2: second data

    Returns:
        list of differences
    """
    diff = []

    added_keys = data2.keys() - data1.keys()
    removed_keys = data1.keys() - data2.keys()

    for key in sorted(data1.keys() | data2.keys()):
        if key in removed_keys:
            diff.append(DiffItem(key, REMOVED, data1[key]))
        elif key in added_keys:
            diff.append(DiffItem(key, ADDED, data2[key]))
        # if key is not in removed_keys and added_keys then key is unchanged
        # but value may be different
        elif data1[key] == data2[key]:
            diff.append(DiffItem(key, UNCHANGED, data1[key]))
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            nested_data = get_data_diff(data1[key], data2[key])
            diff.append(DiffItem(key, UNCHANGED, nested_data))
        else:
            diff.append(DiffItem(key, REMOVED, data1[key]))
            diff.append(DiffItem(key, ADDED, data2[key]))

    return diff


def get_stylish_format_output(data, nest_level=0):
    """
    Return data in stylish output format.

    Args:
        data: diff data
        nest_level: nesting level

    Returns:
        multi-line string with differences
    """
    result = []
    indent = INDENT * nest_level
    if isinstance(data, list):
        lines = map(
            lambda child: get_stylish_format_output(child, nest_level),
            data,
        )
        result.extend(('{', *lines, indent + '}'))
    elif isinstance(data, DiffItem):
        line = '{0}  {1} {2}: {3}'.format(
            indent,
            data.prefix,
            data.key,
            get_stylish_format_output(data.value, nest_level + 1),
        )
        result.append(line)
    elif isinstance(data, dict):
        lines = (
            '{0}    {1}: {2}'.format(
                indent,
                key,
                get_stylish_format_output(child_value, nest_level + 1),
            ) for key, child_value in data.items()
        )
        result.extend(('{', *lines, indent + '}'))
    else:
        result.append(str(data))

    return '\n'.join(result)


def get_plain_format_output(data, nest_level=0):
    """
    Return data in plain output format.

    Args:
        data: diff data
        nest_level: nesting level

    Returns:
        multi-line string with differences
    """
    return '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From 'little' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''

# [
#     DiffItem(key='common', prefix=' ', value=[
#         DiffItem(key='follow', prefix='+', value=False),
#         DiffItem(key='setting1', prefix=' ', value='Value 1'),
#         DiffItem(key='setting2', prefix='-', value=200),
#         DiffItem(key='setting3', prefix='-', value=True),
#         DiffItem(key='setting3', prefix='+', value=None),
#         DiffItem(key='setting4', prefix='+', value='blah blah'),
#         DiffItem(key='setting5', prefix='+', value={'key5': 'value5'}),
#         DiffItem(key='setting6', prefix=' ', value=[
#             DiffItem(key='doge', prefix=' ', value=[
#                 DiffItem(key='wow', prefix='-', value='little'),
#                 DiffItem(key='wow', prefix='+', value='so much')
#             ]),
#             DiffItem(key='key', prefix=' ', value='value'),
#             DiffItem(key='ops', prefix='+', value='vops')
#         ])
#     ]),
#     DiffItem(key='group1', prefix=' ', value=[
#         DiffItem(key='baz', prefix='-', value='bas'),
#         DiffItem(key='baz', prefix='+', value='bars'),
#         DiffItem(key='foo', prefix=' ', value='bar'),
#         DiffItem(key='nest', prefix='-', value={'key': 'value'}),
#         DiffItem(key='nest', prefix='+', value='str')
#     ]),
#     DiffItem(key='group2', prefix='-', value={'abc': 12345, 'deep': {'id': 45}}),
#     DiffItem(key='group3', prefix='+', value={'deep': {'id': {'number': 45}}, 'fee': 100500}),
# ]

