MACS_PEAK_ID
===
Created for genetics lab in UF.
Takes in BED and FASTQ files to filter out BED files.

Install
---
```sh
$ pip install git+https://github.com/alexdiep/macs_peak_id
$ pip uninstall macs_peak_id
```

Usage
---
```sh
$ macs_peak_id input.bed target1.fa target2.fa... 
```
```
$ ls .
input_target1_non-repeats.bed
input_target2_non-repeats.bed
input_target1_repeats.bed
input_target2_repeats.bed
```
`input_target1_non-repeats.bed` contains rows matched with file `target1.fa`. `mac_peaks_id` also 
produces a counterpart, `input_target1_repeats.bed`, containing unmatched rows. Same naming 
scheme for `target2.fa`.

