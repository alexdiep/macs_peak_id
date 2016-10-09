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
    """
    Takes a Path() to a target.fa file and processes it into a Dataframe.
    Also calculates the percent of N in the sequence and appends to table.
    Returns a Dataframe()
    """
    targets_id, targets_n_perc = [], []
    for t in SeqIO.parse(targets_file, "fasta"):
        targets_id.append(t.id)
        targets_n_perc.append(n_perc(t))

    return pd.DataFrame({'peak_id': targets_id, 'n_perc': targets_n_perc})

def get_targets_path(peaks_path, targets_path):
    """
    Returns a dict of target paths with peak name as the key.
    """
    peak_names = [p.stem[:-6] for p in peaks_path]
    targets_dict = {}
    for t_path in targets_path:
        for peak_name in peak_names:
            # Check if peak_name is a substring of parent folder of target.fa
            if peak_name in t_path.parts[-2]:
                targets_dict[peak_name] = t_path
                peak_names.remove(peak_name)

    return targets_dict

def main():
    args = arguments()
    
    output_folder = Path(args.output)
    # Check if output folder exists already and buries expection if it does
    try:
        output_folder.mkdir()
    except FileExistsError:
        pass

    # Check if peaks folder contains bed files
    try:
        next(Path(args.peaks).glob('*.bed'))
    except StopIteration:
        raise FileNotFoundError('Peaks folder contains no .bed files.')

    # Check if target folder contains target.fa in subdirs
    try:
        next(Path(args.targets).glob("**/target.fa"))
    except StopIteration:
        raise FileNotFoundError('Targets folder contains no target.fa files.')
    
    targets_dict = get_targets_path(Path(args.peaks).glob('*.bed'),
                                    Path(args.targets).glob("**/target.fa"))
    

    for peaks_path in Path(args.peaks).glob('*.bed'):
        # Get file name and drop "_peaks"
        peaks_name = peaks_path.stem[:-6]

        with peaks_path.open() as peaks_file:
            peaks = pd.read_table(peaks_file, header=None)
            # Label the third column of the bed file as peak_id
            # Make it easier to filter and combine files
            peaks.rename(columns={peaks.columns[3]:'peak_id'}, inplace=True)

            with targets_dict[peaks_name].open() as targets_file:
                # Contains the target file that is associated with the gene
                targets_df = make_targets_df(targets_file)
                # Creates three new target dataframes based on the percent of N
                targets_df_70N = targets_df[targets_df['n_perc'] < 70]
                targets_df_25N = targets_df[targets_df['n_perc'] < 25]
                targets_df_0N = targets_df[targets_df['n_perc'] == 0]

                              # Find the lines of peak names that exist in both bed and target files
                peaks_dict = {'nonrep': pd.merge(peaks, targets_df, on=['peak_id']),
                              # Continue to match peak ids but with the percent of N
                              'nonrep_25N': pd.merge(peaks, targets_df_25N, on=['peak_id']),
                              'nonrep_0N': pd.merge(peaks, targets_df_0N, on=['peak_id']),
                              'nonrep_70N': pd.merge(peaks, targets_df_70N, on=['peak_id']),
                              # Find the lines that wasn't found in target files based from the percent of N
                              'rep_0N': peaks[~peaks['peak_id'].isin(targets_df_0N['peak_id'])],
                              'rep_25N': peaks[~peaks['peak_id'].isin(targets_df_25N['peak_id'])],
                              'rep_70N': peaks[~peaks['peak_id'].isin(targets_df_70N['peak_id'])]}

                for peaks_key, peaks_value in peaks_dict.items():
                    # Doesn't write empty files to output
                    if not peaks_value.empty:
                        # Output format is "gene_name.(non)rep_(0,25,75)N.bed"
                        # The label for the analysis is from the peaks_dict
                        with (output_folder / '{}.{}.bed'.format(peaks_name, peaks_key)).open('w') as o:
                            peaks_value.to_csv(o, sep="\t", index=None, header=None)


if __name__ == "__main__":
    main()
