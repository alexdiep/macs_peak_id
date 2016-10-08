MACS_PEAK_ID
===
Created for genetics lab in UF.

Analysis the output of [HOMER](http://homer.salk.edu/homer/).

Install
---
```sh
$ sudo pip3 install git+https://github.com/zhoulab/macs_peak_id
$ sudo pip3 uninstall macs_peak_id
```
If you are running the code on HPC or other environments where 
you don't have sudo permissions then you need to install it locally.
```sh
# HPC specific code
$ module load python3
$ module load git
# Install script to ~/.local/bin
$ pip3 install --user git+https://github.com/zhoulab/macs_peak_id
# Add ~/.local/bin to path
$ export PATH=$PATH:~/.local/bin
```
If you don't want to write `export PATH=$PATH:~/.local/bin` every 
time you open the terminal then add `~/.local/bin` to your PATH 
in .bash_profile with `PATH=$PATH:~/.local/bin`.

Usage
---
```sh
$ macs_peak_id peaks/ unmasked/
```
`peaks/` folder should contain all of the bed files desired for analyzing.
`unmasked/` folder should be a HOMER output that contains target.fa, the 
peak name should be in the parent folder.
`--output` folder could be anything if you wanted to redirect the output.

```
$ tree peaks/
dm6_peaks
├── Kc167_P53_NT60A_peaks.bed
├── Kc167_P53_NT60B_peaks.bed
├── Kc167_P53_XR60A_peaks.bed
├── ...
$ tree unmasked/
dm6_unmasked
├── Kc167_P53_NT60Afa
│   ├── homerResults
│   ├── knownResults
│   ├── ...
│   └── target.fa
├── Kc167_P53_NT60Bfa
│   ├── homerResults
│   ├── knownResults
│   ├── ...
│   └── target.fa
├── Kc167_P53_XR60Afa
│   ├── homerResults
│   ├── knownResults
│   ├── ...
│   └── target.fa
├── ....

```

Output would be a `results/` folder.
```
$tree results/
results
├── Kc167_P53_NT60A.0Nnonrep.bed
├── Kc167_P53_NT60A.0Nrep.bed
├── Kc167_P53_NT60A.25Nnonrep.bed
├── Kc167_P53_NT60A.25Nrep.bed
├── Kc167_P53_NT60A.rep.bed
├── Kc167_P53_NT60B.0Nnonrep.bed
├── Kc167_P53_NT60B.0Nrep.bed
├── Kc167_P53_NT60B.25Nnonrep.bed
├── Kc167_P53_NT60B.25Nrep.bed
├── Kc167_P53_NT60B.rep.bed
├── Kc167_P53_XR60A.0Nnonrep.bed
├── Kc167_P53_XR60A.0Nrep.bed
├── Kc167_P53_XR60A.25Nnonrep.bed
├── Kc167_P53_XR60A.25Nrep.bed
├── Kc167_P53_XR60A.rep.bed
├── Kc167_P53_XR60B.0Nnonrep.bed
├── Kc167_P53_XR60B.0Nrep.bed
├── Kc167_P53_XR60B.25Nnonrep.bed
├── Kc167_P53_XR60B.25Nrep.bed
├── Kc167_P53_XR60B.rep.bed
├── R_w1118_P53_NT60A.0Nnonrep.bed
├── R_w1118_P53_NT60A.0Nrep.bed
├── ...
```

Analysis
---
From line 87 to line 98, the analysis is done from there.

Splits the target.fa files into three dataframes by the percentile of N in 
sequences.
```python
targets_df_70N = targets_df[targets_df['n_perc'] < 70]
targets_df_25N = targets_df[targets_df['n_perc'] < 25]
targets_df_0N = targets_df[targets_df['n_perc'] == 0]
```

Filter the peaks with targets, so only the rows with peak id's in both 
peak and targets remain.
```python
peaks_dict = {'nonrep': pd.merge(peaks, targets_df, on=['peak_id']),
              'nonrep_25N': pd.merge(peaks, targets_df_25N, on=['peak_id']),
              'nonrep_0N': pd.merge(peaks, targets_df_0N, on=['peak_id']),
              'nonrep_70N': pd.merge(peaks, targets_df_70N, on=['peak_id']),
              ...
```

Then filter peaks so only rows that aren't in the target files remains.
```python
              ...
              'rep_0N': peaks[~peaks['peak_id'].isin(targets_df_0N['peak_id'])],
              'rep_25N': peaks[~peaks['peak_id'].isin(targets_df_25N['peak_id'])],
              'rep_70N': peaks[~peaks['peak_id'].isin(targets_df_70N['peak_id'])]}
```

Output is formated as the gene name and then the label of the analysis.
```python
# Output format is "gene_name.(non)rep_(0,25,75)N.bed"
with (output_folder/ '{}.{}.bed'.format(peaks_name, peaks_key)).open('w') as o:
            peaks_value.to_csv(o, sep="\t", index=None, header=None)
```