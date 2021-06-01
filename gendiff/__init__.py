"""Python-project-lvl2 project module."""

import json


def generate_diff(file_path1, file_path2):

    diff = {}

    ADDED = '+ '
    UNCHANGED = '  '
    REMOVED = '- '

    json1 = json.load(open(file_path1))
    json2 = json.load(open(file_path2))

    added_keys = json2.keys() - json1.keys()
    unchanged_keys = json1.keys() & json2.keys()
    removed_keys = json1.keys() - json2.keys()

    for key in sorted(json1.keys() | json2.keys()):
        if key in unchanged_keys:
            if json1[key] == json2[key]:
                diff[UNCHANGED + key] = json1[key]
            else:
                diff[REMOVED + key] = json1[key]
                diff[ADDED + key] = json2[key]
        elif key in removed_keys:
            diff[REMOVED + key] = json1[key]
        elif key in added_keys:
            diff[ADDED + key] = json2[key]

    return diff
