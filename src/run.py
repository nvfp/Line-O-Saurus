import os
import re
from datetime import datetime

from mykit.kit.text import byteFmt

from src.get_options import get_options


def get_readme(REPO_ROOT_DIR):
    for i, j in enumerate(os.listdir(REPO_ROOT_DIR), 1):
        print(f'DEBUG: {str(i).zfill(2)}: {repr(j)}')
        if re.match(r'^readme\.md$', j, re.IGNORECASE):
            return os.path.join(REPO_ROOT_DIR, j)
    raise FileNotFoundError('README.md not found.')


def engine(WORKSPACE_DIR, OPTIONS):

    total_line, total_size = 0, 0

    def rec(path):
        line, size = 0, 0
        for i in os.listdir(path):
            p = os.path.join(path, i)
            if os.path.isfile(p):
                with open(p, 'r', encoding='utf-8') as f: line += len(f.read().split('\n'))
                size += os.path.getsize(p)
            else:
                _line, _size = rec(p)
                line += _line
                size += _size
        return line, size
    
    for repo in os.listdir(WORKSPACE_DIR):
        repo_path = os.path.join(WORKSPACE_DIR, repo)
        LINE, SIZE = rec(repo_path)
        total_line += LINE
        total_size += SIZE

    return f'{total_line} {byteFmt(total_size)}'
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
.foobar  ▆                                 43%  1k lines
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
        os.environ['SHOW_CREDIT'],
    )

    README = get_readme(REPO_ROOT_DIR)
    TEXT = engine(WORKSPACE_DIR, OPTIONS)

    with open(README, 'w') as f:
        f.write(TEXT)