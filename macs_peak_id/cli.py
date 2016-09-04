from argparse import ArgumentParser

import pandas as pd


def get_targets(filetarget):
    with open(filetarget, 'r') as target:
        targetseries = pd.read_table(target, delimiter='/n', squeeze=True, header=None, engine='python')
        # Every fourth row of data is the revelant one
        return targetseries[::4]


def arguments():
    parser = ArgumentParser(description="""
    Made for biolab. Takes first argument and uses second arugment to filter it.
    Has data cleaning stuff for the specific data set it came with.
    """)

    parser.add_argument('file', help='Main file to exact rows from. Tested with thrid column.')

    parser.add_argument('target', help='Filter keywords for exaction. All words has first letter chopped off.')

    return parser.parse_args()


def main():
    args = arguments()

    targetlist = get_targets(args.target)
    # Chop off the first letter of targetlist
    targetlist = [target[1:] for target in targetlist]
    targetlist = pd.Series(targetlist)

    filedata = pd.read_csv(args.file, delimiter='\t', header=None)

    # Returns rows that has targetlist in thrid column
    print(filedata[filedata[3].isin(targetlist)])


if __name__ == "__main__":
    main()
