from argparse import ArgumentParser
from pathlib import Path

import pandas as pd

from Bio import SeqIO

def arguments():
    parser = ArgumentParser(description="""
    Takes in a folder of bed files and filters it with matching target.fa files.
    """)

    parser.add_argument('peaks', help='Folder to exact .bed files.')

    parser.add_argument('targets', help='Folder to exact target.fa files')

    return parser.parse_args()

def n_perc(record):
    """
    Returns percent of 'N' of a record
    """
    n_count = record.seq.count('N')
    return 100 * n_count / len(record)

def main():
    args = arguments()

    

    # Dict for target.fa
    # Index is gene Name 
    # f.parts[-2] is parent dir of target.fa. [:-2] gets rid of "*fa" chars at end
    targets_dict = {f.parts[-2][:-2]: f for f in Path(args.targets).glob("**/target.fa")}

    for peaks_path in Path(args.peaks).glob("*.bed"):
        # Get file name drop "_peaks"
        peaks_name = peaks_path.stem[:-6]

        with peaks_path.open() as peaks_file:
            peaks = pd.read_table(peaks_file, header=None)

            with targets_dict[peaks_name].open() as targets_file:
                targets = list(SeqIO.parse(targets_file, "fasta"))
                
                targets_ids = [t.id for t in targets]
                peaks_filtered = peaks[peaks[3].isin(targets_ids)]

                targets_n_perc = pd.DataFrame({'id':targets_ids,
                                               'n_perc': [n_perc(t) for t in targets]})


if __name__ == "__main__":
    main()
