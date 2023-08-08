import os
import re

from mykit.kit.time import TimeFmt

from src.constants import __version__


class Vars:

    _DATE_ = TimeFmt.date()
    _OWNER_ = os.environ['GITHUB_ACTOR']

    ## Total lines of code across the owner's repositories, regardless of only-type and ignore-type.
    _LINES_ = ''
    _LINES_ROUND_ = ''
    _LINES_APPROX_ = ''

    _LINE_ = ''
    _LINE_ROUND_ = ''
    _LINE_APPROX_ = ''

    _VER_ = __version__


def replace_vars(text):
    for var, value in Vars.__dict__.items():
        if var.startswith('__'): continue  # `Vars` magic attributes (Vars internal)
        text = re.sub(r'\b' + var + r'\b', str(value), text)
    return text