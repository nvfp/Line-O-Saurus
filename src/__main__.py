import argparse
import os
import sys

## Make all dirs under the project's root dir importable
print(repr(os.environ['GITHUB_ACTION_PATH']))
print(os.listdir(os.environ['GITHUB_ACTION_PATH']))
sys.path.append(os.environ['GITHUB_ACTION_PATH'])

from .get_num_repos import get_num_repos


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
        get_num_repos(args.raw)
    elif args.cmd == 'get-clone-urls':
        print(repr(args.raw))
    elif args.cmd == 'run':
        print(3)


if __name__ == '__main__':
    main()