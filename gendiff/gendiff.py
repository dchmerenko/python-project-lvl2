"""Generate_diff module."""

import json

ADDED = '+ '
UNCHANGED = '  '
REMOVED = '- '

INDENT = '  '
ROW_TEMPLATE = '{0}: {1}'


def generate_diff(file_path1, file_path2):
    """Return file difference.

    Args:
        file_path1: path to first file
        file_path2: path to second file

    Returns:
        multi-string with differences
    """
    diff = []

    with open(file_path1) as f1:
        json1 = json.load(f1)
    with open(file_path2) as f2:
        json2 = json.load(f2)

    added_keys = json2.keys() - json1.keys()
    removed_keys = json1.keys() - json2.keys()

    for key in sorted(json1.keys() | json2.keys()):
        if key in removed_keys:
            diff.append(ROW_TEMPLATE.format(REMOVED + key, json1[key]))
        elif key in added_keys:
            diff.append(ROW_TEMPLATE.format(ADDED + key, json2[key]))
        else:
            if json1[key] == json2[key]:
                diff.append(ROW_TEMPLATE.format(UNCHANGED + key, json1[key]))
            else:
                diff.append(ROW_TEMPLATE.format(REMOVED + key, json1[key]))
                diff.append(ROW_TEMPLATE.format(ADDED + key, json2[key]))

    rows = '\n{0}'.format(INDENT).join(diff)

    return ''.join(('{\n', INDENT, rows, '\n}'))
