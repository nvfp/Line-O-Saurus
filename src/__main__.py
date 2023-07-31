import argparse

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