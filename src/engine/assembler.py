from src.constants import __version__


CREDIT = f'Counted by [Lineosaurus v{__version__}](https://github.com/nvfp/Line-O-Saurus)'


def assembler(header, custom_title, cards, footer, show_credit, auto_line_break):

    ## header
    text = header

    ## custom-title
    if custom_title != '':
        if auto_line_break: text += '\n\n'
        text += custom_title

    ## card-order
    if cards != '':
        if auto_line_break: text += '\n\n'
        text += cards

    ## footer
    if footer != '':
        if auto_line_break: text += '\n\n'
        text += footer

    ## show-credit
    if show_credit:
        if auto_line_break: text += '\n\n'
        text += CREDIT

    return text