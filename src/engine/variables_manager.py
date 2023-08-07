import os

from mykit.kit.time import TimeFmt


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


def replace_vars(text):
    for var, value in Vars.__dict__.items():
        if var.startswith('__'): continue  # `Vars` magic attributes (Vars internal)
        text = text.replace(var, str(value))
    return text