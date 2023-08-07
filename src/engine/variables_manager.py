import datetime
import os


class Vars:

    _DATE_ = datetime.datetime.now().strftime('%b %-d, %Y')
    _OWNER_ = os.environ['GITHUB_ACTOR']

    ## Total lines of code across the owner's repositories, regardless of only-type and ignore-type.
    _LINES_ = ''
    _LINES_ROUND_ = ''
    _LINES_APPROX_ = ''

    _LINE_ = ''


def replace_vars(text):
    for var, value in Vars.__dict__.items():
        if var.startswith('__'): continue  # `Vars` magic attributes (Vars internal)
        text = text.replace(var, value)
    return text