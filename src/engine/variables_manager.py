import datetime
import os


class Vars:

    _DATE_ = datetime.datetime.now().strftime('%b %#d, %Y')
    _OWNER_ = os.environ['GITHUB_ACTOR']
    _LINES_ = None
    _LINE_ = None


def replace_vars(text):
    for var, value in Vars.__dict__.items():
        if var.startswith('__'): continue  # `Vars` magic attributes (Vars internal)
        text = text.replace(var, value)
    return text