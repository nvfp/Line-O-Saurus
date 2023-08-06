import os

from mykit.kit.text import num_approx
from mykit.kit.utils import sort_dict_by_val, get_first_n_dict_items
from pyggc.ghcli.simple import pack_stargazers, total_stargazers

from src.constants import PB_LEN
from src.engine.card_maker import card_maker


# foo-bar-baz  124,211 lines  33%  ▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆
# foo-bar         5124 lines  11%  ▆▆▆▆▆▆▆▆▆▆▆▆▆
# foo              221 lines   8%  ▆▆▆▆▆▆▆▆
# foo-bar-baz       21 lines   3%  ▆▆


LANG = 'txt'


def get_line_card(ONLY_TYPE, IGNORE_TYPE, NUM_SHOWN, SHOW_APPROX, card_title):
    card = writer(NUM_SHOWN, SHOW_APPROX, card_title, total, pack)
    return card