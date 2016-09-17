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

    parser.add_argument('-o', '--output', default='results', help='Folder to output to')

    return parser.parse_args()

def n_perc(record):
    """
    Returns percent of 'N' of a record
    """
    n_count = record.seq.count('N')
    return 100 * n_count / len(record)

def make_targets_df(targets_file):
    targets_id, targets_n_perc = [], []
    for t in SeqIO.parse(targets_file, "fasta"):
        targets_id.append(t.id)
        targets_n_perc.append(n_perc(t))

    return pd.DataFrame({'peak_id': targets_id, 'n_perc': targets_n_perc})

def main():
    args = arguments()

    output_folder = Path(args.output)
    try:
        output_folder.mkdir()
    except OSError:
        pass

    # Dict for target.fa
    # Index is gene Name 
    # f.parts[-2] is parent dir of target.fa. [:-2] gets rid of "*fa" chars at end
    targets_dict = {f.parts[-2][:-2]: f for f in Path(args.targets).glob("**/target.fa")}

    for peaks_path in Path(args.peaks).glob("*.bed"):
        # Get file name drop "_peaks"
        peaks_name = peaks_path.stem[:-6]

        with peaks_path.open() as peaks_file:
            peaks = pd.read_table(peaks_file, header=None)
            peaks.rename(columns={peaks.columns[3]:'peak_id'}, inplace=True)

            with targets_dict[peaks_name].open() as targets_file:
                targets_df = make_targets_df(targets_file)

                peaks_filtered = peaks[peaks['peak_id'].isin(targets_df['peak_id'])]
                peaks_filtered = pd.merge(peaks_filtered, targets_df, on=['peak_id'])

                with (output_folder / (peaks_name+'.rep.bed')).open('w') as o:
                    peaks_filtered.to_csv(o, sep="\t", index=None, header=None)

                

if __name__ == "__main__":
    main()
