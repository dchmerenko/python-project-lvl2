"""Project library."""

from collections import namedtuple

UNCHANGED = 0
ADDED = 1
REMOVED = 2
UPDATED = 3
NESTED = 4

data_prefix = {
    ADDED: '+',
    REMOVED: '-',
}

INDENT = '    '

DiffItem = namedtuple('DiffItem', 'key, status, value')
