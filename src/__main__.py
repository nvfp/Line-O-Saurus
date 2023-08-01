import argparse
import os
import sys

## Make all dirs under the project's root dir importable
sys.path.append(os.environ['GITHUB_ACTION_PATH'])

from src.get_num_repos import get_num_repos
from src.get_clone_urls import get_clone_urls


def main():

    p = argparse.ArgumentParser()
    s = p.add_subparsers(dest='cmd')

    x = s.add_parser('get-num-repos')
    x.add_argument('raw')

    x = s.add_parser('get-clone-urls')
    x.add_argument('raw')

    x = s.add_parser('run')

    args = p.parse_args()
    if args.cmd == 'get-num-repos':
        print(get_num_repos(args.raw))  # Output the result to the shell
    elif args.cmd == 'get-clone-urls':
        print(' '.join(get_clone_urls(args.raw)))  # Output the result to the shell
    elif args.cmd == 'run':
        print(3)


if __name__ == '__main__':
    main()