import os
import re

from src.get_options import get_options


def get_readme(REPO_ROOT_DIR):
    for i, j in enumerate(os.listdir(REPO_ROOT_DIR), 1):
        print(f'DEBUG: {str(i).zfill(2)}: {repr(j)}')
        if re.match(r'^readme\.md$', j, re.IGNORECASE):
            return os.path.join(REPO_ROOT_DIR, j)
    raise FileNotFoundError('README.md not found.')


def engine():
    import time
    return time.time()


def run():

    REPO_ROOT_DIR = os.environ['GITHUB_WORKSPACE']
    WORKSPACE_DIR = os.path.abspath(os.path.join(REPO_ROOT_DIR, '..', 'lineosaurus-workspace'))

    OPTIONS = get_options(
        os.environ['SHOW_CREDIT'],
        os.environ['ONLY_TYPE'],
        os.environ['IGNORE_TYPE'],
        os.environ['HEADER'],
        os.environ['FOOTER'],
        os.environ['CUSTOM_TITLE'],
        os.environ['NUM_SHOWN'],
        os.environ['SHOW_APPROX'],
        os.environ['CARD_TITLES'],
        os.environ['CARD_ORDER'],
    )

    README = get_readme(REPO_ROOT_DIR)
    TEXT = engine()

    with open(README, 'w') as f:
        f.write(TEXT)