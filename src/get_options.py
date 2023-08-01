

## The default values are given for testing purposes
def get_options(
    SHOW_CREDIT,
    ONLY_TYPE,
    IGNORE_TYPE,
    HEADER,
    FOOTER,
    CUSTOM_TITLE,
    NUM_SHOWN,
    SHOW_APPROX,
    CARD_TITLES,
    CARD_ORDER,

    # SHOW_CREDIT='true',
    # ONLY_TYPE='null',
    # IGNORE_TYPE='null',
    # HEADER='null',
    # FOOTER='null',
    # CUSTOM_TITLE='null',
    # NUM_SHOWN='5',
    # SHOW_APPROX='true',
    # CARD_TITLES='null',
    # CARD_ORDER='null',
):
    class OPTIONS: ...

    # if SHOW_CREDIT == 'true':
    #     OPTIONS.SHOW_CREDIT = True
    # elif SHOW_CREDIT == 'false':
    #     OPTIONS.SHOW_CREDIT = False
    # else:
    #     raise AssertionError('Invalid show-credit value.')

    print(f'SHOW_CREDIT: {repr(SHOW_CREDIT)}')
    print(f'ONLY_TYPE: {repr(ONLY_TYPE)}')
    print(f'IGNORE_TYPE: {repr(IGNORE_TYPE)}')
    print(f'HEADER: {repr(HEADER)}')
    print(f'FOOTER: {repr(FOOTER)}')
    print(f'CUSTOM_TITLE: {repr(CUSTOM_TITLE)}')
    print(f'NUM_SHOWN: {repr(NUM_SHOWN)}')
    print(f'SHOW_APPROX: {repr(SHOW_APPROX)}')
    print(f'CARD_TITLES: {repr(CARD_TITLES)}')
    print(f'CARD_ORDER: {repr(CARD_ORDER)}')
    print(f'SHOW_CREDIT: {type(SHOW_CREDIT)}')
    print(f'ONLY_TYPE: {type(ONLY_TYPE)}')
    print(f'IGNORE_TYPE: {type(IGNORE_TYPE)}')
    print(f'HEADER: {type(HEADER)}')
    print(f'FOOTER: {type(FOOTER)}')
    print(f'CUSTOM_TITLE: {type(CUSTOM_TITLE)}')
    print(f'NUM_SHOWN: {type(NUM_SHOWN)}')
    print(f'SHOW_APPROX: {type(SHOW_APPROX)}')
    print(f'CARD_TITLES: {type(CARD_TITLES)}')
    print(f'CARD_ORDER: {type(CARD_ORDER)}')
    
    return OPTIONS