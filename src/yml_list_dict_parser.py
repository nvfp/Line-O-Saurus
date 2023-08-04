import json
import re


def parse_list(raw_str):

    """
    When users use:
    foo: "['x', 'y', 'z']"
    """
    if '\n' not in raw_str:
        return json.loads(raw_str)

    """
    When users use:
    foo: |-
      - x
      - y
      - z
    """
    l = []
    for line in raw_str.split('\n'):
        res = re.search(r'^- (?P<val>.+)$', line)
        if res is None: raise AssertionError(f'Failed to parse {repr(raw_str)}.')
        l.append(res.group('val'))
    return l


def parse_dict(raw_str):
    
    """
    When users use:
    foo: "{'x': 'foo', 'y': 'bar'}"
    """
    if '\n' not in raw_str:
        return json.loads(raw_str)

    """
    When users use:
    foo: |-
      - x: foo
      - y: bar
    """
    l = []
    for line in raw_str.split('\n'):
        res = re.search(r'^- (?P<val>.+)$', line)
        if res is None: raise AssertionError(f'Failed to parse {repr(raw_str)}.')
        l.append(res.group('val'))
    return l