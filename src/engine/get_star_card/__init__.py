import os

from mykit.kit.text import num_approx
from mykit.kit.utils import sort_dict_by_val, get_first_n_dict_items
from pyggc.ghcli.simple import pack_stargazers, total_stargazers

from src.constants import PB_LEN
from src.engine.card_maker import card_maker


# foo-bar-baz  124,211 stargazers  33%  ⭐️🌟⭐️🌟⭐️🌟⭐️🌟⭐️🌟⭐️
# foo-bar         5124 stargazers  11%  ⭐️🌟⭐️🌟⭐️🌟⭐️
# foo              221 stargazers   8%  ⭐️🌟⭐️🌟
# foo-bar-baz       21 stargazers   3%  ⭐️


def get_entries(SHOW_APPROX, total, pack_cut):
    
    entries = []
    
    for repo, star in pack_cut.items():
        
        if SHOW_APPROX:
            nstar = num_approx(star)
        else:
            nstar = f'{star:,}'

        bars = ''
        for b in range(round(PB_LEN*star/total)):
            if (b%2) == 0:
                bars += '⭐️'
            else:
                bars += '🌟'

        entries.append([
            repo,
            f'{nstar} stargazers',
            f'{round(100*star/total)}%',
            bars
        ])

    return entries


## A unit test will be created for this function
def writer(NUM_SHOWN, SHOW_APPROX, card_title, total, pack):
    
    pack_sorted = sort_dict_by_val(pack, reverse=True)
    pack_cut = get_first_n_dict_items(pack_sorted, NUM_SHOWN)

    entries = get_entries()

    align = [-1, 1, 1, -1]
    card = card_maker(card_title, entries, align)


def get_star_card(NUM_SHOWN, SHOW_APPROX, card_title):

    OWNER = os.environ['GITHUB_ACTOR']

    total = total_stargazers(OWNER)
    pack = pack_stargazers(OWNER)

    card = writer(NUM_SHOWN, SHOW_APPROX, card_title, total, pack)

    return card