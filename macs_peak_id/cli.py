from argparse import ArgumentParser
import pathlib

import pandas as pd

import Bio

def arguments():
    parser = ArgumentParser(description="""
    Takes in a folder of bed files and filters it with matching target.fa files.
    """)

    parser.add_argument('peaks', help='Folder to exact .bed files.')

    parser.add_argument('targets', help='Folder to exact target.fa files')

    return parser.parse_args()


def main():
    args = arguments()

    peaks_path = pathlib.Path(args.peaks)
    bed_files = list(peaks_path.glob("*.bed"))

    bed_file = bed_files[0]

    targets_path = pathlib.Path(args.targets)
    targets_files = list(targets_path.glob("**/target.fa"))

    targets_file = targets_files[0]


if __name__ == "__main__":
    main()
