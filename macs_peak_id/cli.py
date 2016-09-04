from argparse import ArgumentParser

def arguments():
    parser = ArgumentParser()

    parser.add_argument('file', help='Test description')

    return parser.parse_args()

def main():
    print(arguments())

if __name__ == "__main__":
    main()