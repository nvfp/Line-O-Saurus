import json
import os
import re

from src.constants import CARDS
from src.yml_list_dict_parser import parse_dict, parse_list


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
    PREFER_EXTENSION='true',
    SHOW_CREDIT='true',
):
    
    REPO_ROOT_DIR = os.environ['GITHUB_WORKSPACE']

    class OPTIONS: ...

    ## only-type
    if ONLY_TYPE == '':  # If `null` in YAML
        OPTIONS.ONLY_TYPE = None
    else:
        try:
            only_type = parse_list(ONLY_TYPE)
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

    ## ignore-type
    if IGNORE_TYPE == '':
        OPTIONS.IGNORE_TYPE = None
    else:
        try:
            ignore_type = parse_list(IGNORE_TYPE)
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
    
    ## header
    if HEADER == '':
        OPTIONS.HEADER = ''
    else:
        header = os.path.join(REPO_ROOT_DIR, HEADER)
        if not os.path.isfile(header):
            raise AssertionError('Invalid header value.')
        with open(header, 'r') as f:
            OPTIONS.HEADER = f.read()
    
    ## footer
    if FOOTER == '':
        OPTIONS.FOOTER = ''
    else:
        footer = os.path.join(REPO_ROOT_DIR, FOOTER)
        if not os.path.isfile(footer):
            raise AssertionError('Invalid footer value.')
        with open(footer, 'r') as f:
            OPTIONS.FOOTER = f.read()

    ## custom-title
    if CUSTOM_TITLE == '':
        ## This default is mirroring the one in the README
        OPTIONS.CUSTOM_TITLE = "(_DATE_) _LINE_ lines of code stretch through _OWNER_'s repositories."
    else:
        OPTIONS.CUSTOM_TITLE = CUSTOM_TITLE

    ## num-shown
    try:
        num_shown = int(NUM_SHOWN)
        if num_shown < 1:
            raise AssertionError('Invalid num-shown value.')
        OPTIONS.NUM_SHOWN = num_shown
    except ValueError:
        raise AssertionError('Invalid num-shown value.')

    ## show-approx
    if SHOW_APPROX == 'true':
        OPTIONS.SHOW_APPROX = True
    elif SHOW_APPROX == 'false':
        OPTIONS.SHOW_APPROX = False
    else:
        raise AssertionError('Invalid show-approx value.')

    ## card-titles
    if CARD_TITLES == '':
        ## This default is mirroring the one in the README
        OPTIONS.CARD_TITLES = {
            'line': "Lines of code",
            'type': "Languages",
            'star': "Stargazers",
            'stat': "_OWNER_'s statistics",
        }
    else:
        try:
            card_titles = parse_dict(CARD_TITLES)
            if (type(card_titles) is not dict) or (len(card_titles) == 0):
                raise AssertionError('Invalid card-titles value.')
            for k, v in card_titles.items():
                if (k not in CARDS) or (type(v) is not str):
                    raise AssertionError('Invalid card-titles value.')
            OPTIONS.CARD_TITLES = card_titles
        except json.decoder.JSONDecodeError:
            raise AssertionError('Invalid card-titles value.')

    ## card-order
    if CARD_ORDER == '':
        ## This default is mirroring the one in the README
        OPTIONS.CARD_ORDER = ['line', 'type', 'star', 'stat']
    else:
        try:
            card_order = parse_list(CARD_ORDER)
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

    ## show-credit
    if PREFER_EXTENSION == 'true':
        OPTIONS.PREFER_EXTENSION = True
    elif PREFER_EXTENSION == 'false':
        OPTIONS.PREFER_EXTENSION = False
    else:
        raise AssertionError('Invalid prefer-extension value.')

    ## show-credit
    if SHOW_CREDIT == 'true':
        OPTIONS.SHOW_CREDIT = True
    elif SHOW_CREDIT == 'false':
        OPTIONS.SHOW_CREDIT = False
    else:
        raise AssertionError('Invalid show-credit value.')

    return OPTIONS