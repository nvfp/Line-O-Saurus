import os
import re
from datetime import datetime

from mykit.kit.text import byteFmt
from mykit.kit.pLog import pL

from src.constants import NON_TEXT_TYPE, NON_TEXT_FILENAME
from get_options.get_options import get_options


def get_readme(REPO_ROOT_DIR):
    for i, j in enumerate(os.listdir(REPO_ROOT_DIR), 1):
        pL.debug(f'Searching for README attempt#{str(i).zfill(2)}: {repr(j)}')
        if re.match(r'^readme\.md$', j, re.IGNORECASE):
            return os.path.join(REPO_ROOT_DIR, j)
    raise FileNotFoundError('README.md not found.')


def engine(WORKSPACE_DIR, OPTIONS):

    total_pub_repos, total_line, total_size = 0, 0, 0
    pool = {}

    def rec(path):
        line, size = 0, 0
        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            if os.path.isfile(file_path):
                file_ext = os.path.splitext(file_path)[1]
                if (file_name in NON_TEXT_FILENAME) or (file_ext in NON_TEXT_TYPE):
                    pass
                else:
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f: line += len(f.read().split('\n'))
                    except Exception as err:
                        pL.error(f'path: {repr(file_path)}  err: {err}')
                size += os.path.getsize(file_path)
            else:
                _line, _size = rec(file_path)
                line += _line
                size += _size
        return line, size
    
    for repo in os.listdir(WORKSPACE_DIR):
        total_pub_repos += 1
        repo_path = os.path.join(WORKSPACE_DIR, repo)
        LINE, SIZE = rec(repo_path)
        total_line += LINE
        total_size += SIZE
        pool[repo] = {
            'line': LINE,
            'line': LINE,
        }

    return f'{total_line} {byteFmt(total_size)}  {total_pub_repos}'
    text = f"""
# {datetime.now().strftime('%b %d, %Y')}, 300,000 lines across foo bar repositories

## Lines of code

```shell
abcd-12312  ▆▆▆▆▆▆▆▆▆▆▆               50%  132,412 lines
ad-312      ▆▆▆▆▆▆                        132,412 lines
ab          ▆                                 132,412 lines
abcd-12312  ▆                                 132,412 lines
abcd-12312  ▆                                 132,412 lines
```

### Top languages

```css
.py      ▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆  90%  13k lines
.ts      ▆▆▆▆▆▆                        43%  43k lines
.tx      ▆                                 43%  22k lines
.foobar  ▆                                 43%   1k lines
.scsc    ▆                                 43%  433 lines
```

### sizes

```css
.py      ▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆  90%  13k lines
.ts      ▆▆▆▆▆▆                        43%  43k lines
.tx      ▆                                 43%  22k lines
.foobar  ▆                                 43%   1k lines
.scsc    ▆                                 43%  433 lines
```

### commits

```css
.py      ▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆  90%  13k lines
.ts      ▆▆▆▆▆▆                        43%  43k lines
.tx      ▆                                 43%  22k lines
.foobar  ▆                                 43%   1k lines
.scsc    ▆                                 43%  433 lines
```

### Statistics

```markdown
number of repo     132
lines of code      213,231
number of files    231
number of stars    32
number of commits  141,241
total size  141,241
top language  141,241
```

Counted by [Line-O-Saurus](https://github.com/nvfp/Line-O-Saurus)🦕
"""
    return text


def run():

    REPO_ROOT_DIR = os.environ['GITHUB_WORKSPACE']
    WORKSPACE_DIR = os.path.abspath(os.path.join(REPO_ROOT_DIR, '..', 'lineosaurus-workspace'))

    ## Debugging purposes
    pL.debug(f'ONLY_TYPE . . . : {repr(os.environ["ONLY_TYPE"])}.')
    pL.debug(f'IGNORE_TYPE . . : {repr(os.environ["IGNORE_TYPE"])}.')
    pL.debug(f'HEADER  . . . . : {repr(os.environ["HEADER"])}.')
    pL.debug(f'FOOTER  . . . . : {repr(os.environ["FOOTER"])}.')
    pL.debug(f'CUSTOM_TITLE    : {repr(os.environ["CUSTOM_TITLE"])}.')
    pL.debug(f'NUM_SHOWN . . . : {repr(os.environ["NUM_SHOWN"])}.')
    pL.debug(f'SHOW_APPROX . . : {repr(os.environ["SHOW_APPROX"])}.')
    pL.debug(f'CARD_TITLES . . : {repr(os.environ["CARD_TITLES"])}.')
    pL.debug(f'CARD_ORDER  . . : {repr(os.environ["CARD_ORDER"])}.')
    pL.debug(f'PREFER_EXTENSION: {repr(os.environ["PREFER_EXTENSION"])}.')
    pL.debug(f'SHOW_CREDIT . . : {repr(os.environ["SHOW_CREDIT"])}.')

    OPTIONS = get_options(
        os.environ['ONLY_TYPE'],
        os.environ['IGNORE_TYPE'],
        os.environ['HEADER'],
        os.environ['FOOTER'],
        os.environ['CUSTOM_TITLE'],
        os.environ['NUM_SHOWN'],
        os.environ['SHOW_APPROX'],
        os.environ['CARD_TITLES'],
        os.environ['CARD_ORDER'],
        os.environ['PREFER_EXTENSION'],
        os.environ['SHOW_CREDIT'],
    )

    ## Debugging purposes
    pL.debug(f'OPTIONS.ONLY_TYPE . . . : {repr(OPTIONS.ONLY_TYPE)}.')
    pL.debug(f'OPTIONS.IGNORE_TYPE . . : {repr(OPTIONS.IGNORE_TYPE)}.')
    pL.debug(f'OPTIONS.HEADER  . . . . : {repr(OPTIONS.HEADER)}.')
    pL.debug(f'OPTIONS.FOOTER  . . . . : {repr(OPTIONS.FOOTER)}.')
    pL.debug(f'OPTIONS.CUSTOM_TITLE    : {repr(OPTIONS.CUSTOM_TITLE)}.')
    pL.debug(f'OPTIONS.NUM_SHOWN . . . : {repr(OPTIONS.NUM_SHOWN)}.')
    pL.debug(f'OPTIONS.SHOW_APPROX . . : {repr(OPTIONS.SHOW_APPROX)}.')
    pL.debug(f'OPTIONS.CARD_TITLES . . : {repr(OPTIONS.CARD_TITLES)}.')
    pL.debug(f'OPTIONS.CARD_ORDER  . . : {repr(OPTIONS.CARD_ORDER)}.')
    pL.debug(f'OPTIONS.PREFER_EXTENSION: {repr(OPTIONS.PREFER_EXTENSION)}.')
    pL.debug(f'OPTIONS.SHOW_CREDIT . . : {repr(OPTIONS.SHOW_CREDIT)}.')

    README = get_readme(REPO_ROOT_DIR)
    # TEXT = engine(WORKSPACE_DIR, OPTIONS)
    TEXT = OPTIONS.CUSTOM_TITLE

    with open(README, 'w') as f:
        f.write(TEXT)