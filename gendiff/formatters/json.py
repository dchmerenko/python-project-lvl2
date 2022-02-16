"""Json formatter."""

import json


def get_json_format_output(diff):
    """Return data in json output format.

    Args:
        diff: diff data

    Returns:
        data in json output format
    """
    return json.dumps(diff, indent=4)
