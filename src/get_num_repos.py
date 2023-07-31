import json


def get_num_repos(raw):
    return len(json.loads(raw))