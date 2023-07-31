import os


def main():
    SHOW_CREDIT = os.environ['SHOW_CREDIT']
    print(SHOW_CREDIT)
    print(type(SHOW_CREDIT))
    print(repr(SHOW_CREDIT))


if __name__ == '__main__':
    main()