from argparse import ArgumentParser
from os.path import splitext

import pandas as pd


def get_targets(filetarget):
    with open(filetarget, 'r') as target:
        targetseries = pd.read_table(target, delimiter='/n', squeeze=True, header=None, engine='python')
        # Every fourth row of data is the revelant one
        return targetseries[::4]


def arguments():
    parser = ArgumentParser(description="""
    Takes first argument and uses second argument to filter it.
    """)

    parser.add_argument('file', help='Exact rows from.')

    parser.add_argument('targets', nargs="+",help='Filter keywords.')

    return parser.parse_args()


def main():
    args = arguments()

    filedata = pd.read_csv(args.file, delimiter='\t', header=None)

    for target in args.targets:
        targetlist = get_targets(target)
        # Chop off the first letter of targetlist
        targetlist = [target[1:] for target in targetlist]

        # Returns rows that has targetlist in thrid column
        filtered = filedata[filedata[3].isin(targetlist)]
        # Output as file_target.bed 
        output_name = "{}_{}.bed".format(splitext(args.file)[0], splitext(target)[0])
        filtered.to_csv(output_name, sep="\t", index=None, header=None)


if __name__ == "__main__":
    main()
