import os


def engine():
    pass


def run():
    REPO_ROOT_DIR = os.environ['GITHUB_WORKSPACE']
    WORKSPACE_DIR = os.path.abspath(os.path.join(REPO_ROOT_DIR, '..', 'lineosaurus-workspace'))
    
    SHOW_CREDIT = os.environ['SHOW_CREDIT']

    print(repr(REPO_ROOT_DIR))
    print(repr(WORKSPACE_DIR))
    print(repr(SHOW_CREDIT))

    print(repr(os.listdir(WORKSPACE_DIR)))
    for i, f in enumerate(os.listdir(WORKSPACE_DIR), 1):
        print(i, f)