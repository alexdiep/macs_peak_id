from argparse import ArgumentParser
import pathlib

def arguments():
    parser = ArgumentParser(description="""
    Takes in a folder of bed files and filters it with matching target.fa files.
    """)

    parser.add_argument('peaks', help='Folder to exact .bed files.')

    parser.add_argument('targets', help='Folder to exact target.fa files')

    return parser.parse_args()


def main():
    args = arguments()

    print([x for x in pathlib.Path(args.peaks).iterdir()])

    print([x for x in pathlib.Path(args.targets).iterdir()])

if __name__ == "__main__":
    main()
