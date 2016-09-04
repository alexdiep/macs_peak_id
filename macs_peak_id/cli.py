from argparse import ArgumentParser

import os

import pandas as pd

def get_targets(file):
    with open(file, 'r') as target:
         targetseries = pd.read_table(target, delimiter='/n', squeeze=True, header=None, engine='python')
         # Every fourth row of data is the revelant one
         return targetseries[::4]


def arguments():
    parser = ArgumentParser()

    parser.add_argument('file', help='Test description')

    parser.add_argument('target', help='Test description')

    return parser.parse_args()


def main():
    args = arguments()
    
    targetlist = get_targets(args.target)
    targetlist = [target[1:] for target in targetlist]
    targetlist = pd.Series(targetlis)

    filedata = pd.read_csv(args.file, delimiter='\t', header=None)

    matched = filedata[3][targetlist].index

    print(filedata[filedata[3].isin(targetlist)])


if __name__ == "__main__":
    main()