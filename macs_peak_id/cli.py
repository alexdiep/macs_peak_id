from argparse import ArgumentParser

def main():
    parser = ArgumentParser()

    parser.add_argument('file', help='Test description')

    args = parser.parse_args()

    print(args.file)

if __name__ == "__main__":
    main()