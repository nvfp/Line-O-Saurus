from src.engine.get_line_card import get_line_card
from src.engine.get_type_card import get_type_card
from src.engine.get_size_card import get_size_card
from src.engine.get_stat_card import get_stat_card
from src.engine.get_char_card import get_char_card
from src.engine.get_star_card import get_star_card
from src.engine.get_cmit_card import get_cmit_card
from src.engine.get_file_card import get_file_card
from src.engine.variables_manager import Vars, replace_vars


def card_factory(WORKSPACE_DIR, OPTIONS):

    cards = []

    for card in OPTIONS.CARD_ORDER:

        if card == 'line': cards.append(get_line_card(
            WORKSPACE_DIR, OPTIONS.ONLY_TYPE, OPTIONS.IGNORE_TYPE,
            OPTIONS.NUM_SHOWN, OPTIONS.SHOW_APPROX, OPTIONS.CARD_TITLES['line']
        ))

        if card == 'type': cards.append(get_type_card(
            WORKSPACE_DIR, OPTIONS.ONLY_TYPE, OPTIONS.IGNORE_TYPE,
            OPTIONS.NUM_SHOWN, OPTIONS.SHOW_APPROX, OPTIONS.PREFER_EXTENSION, OPTIONS.CARD_TITLES['type']
        ))

        if card == 'size': cards.append(get_size_card(
            WORKSPACE_DIR, OPTIONS.ONLY_TYPE, OPTIONS.IGNORE_TYPE,
            OPTIONS.NUM_SHOWN, OPTIONS.CARD_TITLES['size']
        ))

        if card == 'stat': cards.append(get_stat_card(
            WORKSPACE_DIR, OPTIONS.ONLY_TYPE, OPTIONS.IGNORE_TYPE,
            OPTIONS.CARD_TITLES['stat']
        ))

        if card == 'char': cards.append(get_char_card(
            WORKSPACE_DIR, OPTIONS.ONLY_TYPE, OPTIONS.IGNORE_TYPE,
            OPTIONS.NUM_SHOWN, OPTIONS.SHOW_APPROX, OPTIONS.PREFER_EXTENSION, OPTIONS.CARD_TITLES['char']
        ))

        if card == 'star': cards.append(get_star_card(
            OPTIONS.NUM_SHOWN, OPTIONS.SHOW_APPROX, OPTIONS.CARD_TITLES['star']
        ))

        if card == 'cmit': cards.append(get_cmit_card(
            WORKSPACE_DIR, OPTIONS.NUM_SHOWN, OPTIONS.SHOW_APPROX, OPTIONS.CARD_TITLES['cmit']
        ))

        if card == 'file': cards.append(get_file_card(
            WORKSPACE_DIR, OPTIONS.ONLY_TYPE, OPTIONS.IGNORE_TYPE,
            OPTIONS.NUM_SHOWN, OPTIONS.SHOW_APPROX, OPTIONS.CARD_TITLES['file']
        ))

    return '\n\n'.join(cards)


def assembler(header, custom_title, cards, footer, show_credit):

    if header == '':
        text = header
    else:
        text = header + '\n\n'

    ## Apparently, at the moment, the custom title cannot be an empty string.
    text += custom_title + '\n\n'

    text += cards

    if footer != '':
        text += '\n\n' + footer

    if show_credit:
        text += '\n\nCounted by [Lineosaurus](https://github.com/nvfp/Line-O-Saurus)'

    return text


def engine(WORKSPACE_DIR, OPTIONS):

    header = replace_vars(OPTIONS.HEADER)
    custom_title = replace_vars(OPTIONS.CUSTOM_TITLE)
    card_titles = {k: replace_vars(v) for k, v in OPTIONS.CARD_TITLES.items()}
    footer = replace_vars(OPTIONS.FOOTER)

    cards = card_factory(WORKSPACE_DIR, OPTIONS)

    return assembler(header, custom_title, cards, footer, OPTIONS.SHOW_CREDIT)