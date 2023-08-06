import os
import re

from mykit.kit.pLog import pL

from src.get_options.get_options import get_options
from src.engine.engine import engine


def get_readme(REPO_ROOT_DIR):
    for i, j in enumerate(os.listdir(REPO_ROOT_DIR), 1):
        pL.debug(f'Searching for README attempt#{str(i).zfill(2)}: {repr(j)}')
        if re.match(r'^readme\.md$', j, re.IGNORECASE):
            return os.path.join(REPO_ROOT_DIR, j)
    raise FileNotFoundError('README.md not found.')


def run():

    REPO_ROOT_DIR = os.environ['GITHUB_WORKSPACE']
    WORKSPACE_DIR = os.path.abspath(os.path.join(REPO_ROOT_DIR, '..', 'lineosaurus-workspace'))

    ## Debugging purposes
    pL.debug(f'REPO_ROOT_DIR: {repr(REPO_ROOT_DIR)}.')
    pL.debug(f'OWNER: {repr(os.environ["GITHUB_ACTOR"])}.')

    ## Debugging purposes
    pL.debug(f'ONLY_TYPE . . . : {repr(os.environ["ONLY_TYPE"])}.')
    pL.debug(f'IGNORE_TYPE . . : {repr(os.environ["IGNORE_TYPE"])}.')
    pL.debug(f'HEADER  . . . . : {repr(os.environ["HEADER"])}.')
    pL.debug(f'FOOTER  . . . . : {repr(os.environ["FOOTER"])}.')
    pL.debug(f'CUSTOM_TITLE    : {repr(os.environ["CUSTOM_TITLE"])}.')
    pL.debug(f'NUM_SHOWN . . . : {repr(os.environ["NUM_SHOWN"])}.')
    pL.debug(f'SHOW_APPROX . . : {repr(os.environ["SHOW_APPROX"])}.')
    pL.debug(f'CARD_TITLES . . : {repr(os.environ["CARD_TITLES"])}.')
    pL.debug(f'CARD_ORDER  . . : {repr(os.environ["CARD_ORDER"])}.')
    pL.debug(f'PREFER_EXTENSION: {repr(os.environ["PREFER_EXTENSION"])}.')
    pL.debug(f'SHOW_CREDIT . . : {repr(os.environ["SHOW_CREDIT"])}.')

    OPTIONS = get_options(
        os.environ['ONLY_TYPE'],
        os.environ['IGNORE_TYPE'],
        os.environ['HEADER'],
        os.environ['FOOTER'],
        os.environ['CUSTOM_TITLE'],
        os.environ['NUM_SHOWN'],
        os.environ['SHOW_APPROX'],
        os.environ['CARD_TITLES'],
        os.environ['CARD_ORDER'],
        os.environ['PREFER_EXTENSION'],
        os.environ['SHOW_CREDIT'],
    )

    ## Debugging purposes
    pL.debug(f'OPTIONS.ONLY_TYPE . . . : {repr(OPTIONS.ONLY_TYPE)}.')
    pL.debug(f'OPTIONS.IGNORE_TYPE . . : {repr(OPTIONS.IGNORE_TYPE)}.')
    pL.debug(f'OPTIONS.HEADER  . . . . : {repr(OPTIONS.HEADER)}.')
    pL.debug(f'OPTIONS.FOOTER  . . . . : {repr(OPTIONS.FOOTER)}.')
    pL.debug(f'OPTIONS.CUSTOM_TITLE    : {repr(OPTIONS.CUSTOM_TITLE)}.')
    pL.debug(f'OPTIONS.NUM_SHOWN . . . : {repr(OPTIONS.NUM_SHOWN)}.')
    pL.debug(f'OPTIONS.SHOW_APPROX . . : {repr(OPTIONS.SHOW_APPROX)}.')
    pL.debug(f'OPTIONS.CARD_TITLES . . : {repr(OPTIONS.CARD_TITLES)}.')
    pL.debug(f'OPTIONS.CARD_ORDER  . . : {repr(OPTIONS.CARD_ORDER)}.')
    pL.debug(f'OPTIONS.PREFER_EXTENSION: {repr(OPTIONS.PREFER_EXTENSION)}.')
    pL.debug(f'OPTIONS.SHOW_CREDIT . . : {repr(OPTIONS.SHOW_CREDIT)}.')

    README = get_readme(REPO_ROOT_DIR)
    TEXT = engine(WORKSPACE_DIR, OPTIONS)

    with open(README, 'w') as f:
        f.write(TEXT)