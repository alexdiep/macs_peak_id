from argparse import ArgumentParser
import os

def filter(file):
    with open(file, 'r') as target:
         target_series = pd.read_table(target, delimiter='/n', squeeze=True, header=None)
         # Every fourth row of data is the revelant one
         return target_series[::4]



def arguments():
    parser = ArgumentParser()

    parser.add_argument('file', help='Test description')

    parser.add_argument('filter', help='Test description')

    return parser.parse_args()

def main():
    args = arguments()
    
    filterlist = filter(args.filter)


if __name__ == "__main__":
    main()