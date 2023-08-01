import os


def run():
    REPO_ROOT_DIR = os.environ['GITHUB_WORKSPACE']
    WORKSPACE_DIR = os.path.abspath(os.path.join(REPO_ROOT_DIR, '..', 'lineosaurus-workspace'))
    
    SHOW_CREDIT = os.environ['SHOW_CREDIT']

    print(repr(REPO_ROOT_DIR))
    print(repr(WORKSPACE_DIR))
    print(repr(SHOW_CREDIT))