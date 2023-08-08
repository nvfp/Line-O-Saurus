import os

from mykit.kit.time import TimeFmt

from src.constants import __version__


class Vars:

    _DATE_ = TimeFmt.date()
    _OWNER_ = os.environ['GITHUB_ACTOR']

    ## Total lines of code across all repositories, regardless only-type and ignore-type.
    _LINES_ = ''
    _LINESROUND_ = ''
    _LINESAPPROX_ = ''

    ## Total lines of code across all repositories, following only-type and ignore-type.
    _LINE_ = ''
    _LINEROUND_ = ''
    _LINEAPPROX_ = ''

    _VER_ = __version__


def replace_vars(text):
    for var, value in Vars.__dict__.items():
        if var.startswith('__'): continue  # `Vars` magic attributes (Vars internal)
        text = text.replace(var, str(value))
    return text