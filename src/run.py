import os
import re


def get_readme(REPO_ROOT_DIR):
    for i, j in enumerate(os.listdir(REPO_ROOT_DIR), 1):
        print(f'DEBUG: {str(i).zfill(2)}: {repr(j)}')
        if re.match(r'^readme\.md$', j, re.IGNORECASE):
            return os.path.join(REPO_ROOT_DIR, j)
    raise FileNotFoundError('README.md not found.')


def engine():
    pass


def run():

    REPO_ROOT_DIR = os.environ['GITHUB_WORKSPACE']
    WORKSPACE_DIR = os.path.abspath(os.path.join(REPO_ROOT_DIR, '..', 'lineosaurus-workspace'))

    SHOW_CREDIT = os.environ['SHOW_CREDIT']
    ONLY_TYPE = os.environ['ONLY_TYPE']
    IGNORE_TYPE = os.environ['IGNORE_TYPE']
    HEADER = os.environ['HEADER']
    FOOTER = os.environ['FOOTER']
    CUSTOM_TITLE = os.environ['CUSTOM_TITLE']
    NUM_SHOWN = os.environ['NUM_SHOWN']
    SHOW_APPROX = os.environ['SHOW_APPROX']
    CARD_TITLES = os.environ['CARD_TITLES']
    CARD_ORDER = os.environ['CARD_ORDER']

    README = get_readme(REPO_ROOT_DIR)
    with open(README, 'w') as f:
        f.write('foo')