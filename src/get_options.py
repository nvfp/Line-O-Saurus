import json
import os
import re

from src.constants import CARDS


## The default values are given for testing purposes
def get_options(
    ONLY_TYPE='',
    IGNORE_TYPE='',
    HEADER='',
    FOOTER='',
    CUSTOM_TITLE='',
    NUM_SHOWN='5',
    SHOW_APPROX='true',
    CARD_TITLES='',
    CARD_ORDER='',
    SHOW_CREDIT='true',
):
    
    REPO_ROOT_DIR = os.environ['GITHUB_WORKSPACE']

    class OPTIONS: ...

    if ONLY_TYPE == '':
        OPTIONS.ONLY_TYPE = None
    else:
        try:
            only_type = json.loads(ONLY_TYPE)
            if (type(only_type) is not list) or (len(only_type) == 0):
                raise AssertionError('Invalid only-type value.')
            for i in only_type:
                if type(i) is not str:
                    raise AssertionError('Invalid only-type value.')
                if not re.match(r'^\.\w+$', i):
                    raise AssertionError('Invalid only-type value.')
            OPTIONS.ONLY_TYPE = only_type
        except json.decoder.JSONDecodeError:
            raise AssertionError('Invalid only-type value.')

    if IGNORE_TYPE == '':
        OPTIONS.IGNORE_TYPE = None
    else:
        try:
            ignore_type = json.loads(IGNORE_TYPE)
            if (type(ignore_type) is not list) or (len(ignore_type) == 0):
                raise AssertionError('Invalid ignore-type value.')
            for i in ignore_type:
                if type(i) is not str:
                    raise AssertionError('Invalid ignore-type value.')
                if not re.match(r'^\.\w+$', i):
                    raise AssertionError('Invalid ignore-type value.')
            OPTIONS.IGNORE_TYPE = ignore_type
        except json.decoder.JSONDecodeError:
            raise AssertionError('Invalid ignore-type value.')
    
    if HEADER == '':
        OPTIONS.HEADER = None
    else:
        header = os.path.join(REPO_ROOT_DIR, HEADER)
        if not os.path.isfile(header):
            raise AssertionError('Invalid header value.')
        OPTIONS.HEADER = header
    
    if FOOTER == '':
        OPTIONS.FOOTER = None
    else:
        footer = os.path.join(REPO_ROOT_DIR, FOOTER)
        if not os.path.isfile(footer):
            raise AssertionError('Invalid footer value.')
        OPTIONS.FOOTER = footer

    OPTIONS.CUSTOM_TITLE = CUSTOM_TITLE

    try:
        num_shown = int(NUM_SHOWN)
        if num_shown < 1:
            raise AssertionError('Invalid num-shown value.')
        OPTIONS.NUM_SHOWN = num_shown
    except ValueError:
        raise AssertionError('Invalid num-shown value.')

    if SHOW_APPROX == 'true':
        OPTIONS.SHOW_APPROX = True
    elif SHOW_APPROX == 'false':
        OPTIONS.SHOW_APPROX = False
    else:
        raise AssertionError('Invalid show-approx value.')

    if CARD_TITLES == '':
        OPTIONS.CARD_TITLES = None
    else:
        try:
            card_titles = json.loads(CARD_TITLES)
            if (type(card_titles) is not dict) or (len(card_titles) == 0):
                raise AssertionError('Invalid card-titles value.')
            for k, v in card_titles.items():
                if (k not in CARDS) or (type(v) is not str):
                    raise AssertionError('Invalid card-titles value.')
            OPTIONS.CARD_TITLES = card_titles
        except json.decoder.JSONDecodeError:
            raise AssertionError('Invalid card-titles value.')

    if CARD_ORDER == '':
        OPTIONS.CARD_ORDER = None
    else:
        try:
            card_order = json.loads(CARD_ORDER)
            if (type(card_order) is not list) or (len(card_order) == 0):
                raise AssertionError('Invalid card-order value.')
            for i in card_order:
                if i not in CARDS:
                    raise AssertionError('Invalid card-order value.')
            if len(card_order) != len(set(card_order)):
                raise AssertionError('Invalid card-order value.')  # Has duplicates
            OPTIONS.CARD_ORDER = card_order
        except json.decoder.JSONDecodeError:
            raise AssertionError('Invalid card-order value.')

    if SHOW_CREDIT == 'true':
        OPTIONS.SHOW_CREDIT = True
    elif SHOW_CREDIT == 'false':
        OPTIONS.SHOW_CREDIT = False
    else:
        raise AssertionError('Invalid show-credit value.')

    return OPTIONS