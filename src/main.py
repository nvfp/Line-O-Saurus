import os


def main():
    SHOW_CREDIT = os.environ['SHOW_CREDIT']
    GH_WORKSPACE = os.environ['GITHUB_WORKSPACE']
    
    print(GH_WORKSPACE)


if __name__ == '__main__':
    main()