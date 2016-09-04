# MAC_PEAK_ID
Small Python script for some files
Objective – To write a script to extract lines from one file that matches specific terms
Steps –
1. Every 4th line of targetnoN.fa file has a peak ID
2. Extract lines containing only these MACS_peak_IDs from input file - S_w1118_P53_XR30_peaks.bed
3. Column 4 of S_w1118_P53_XR30_peaks.bed file contains the MACS_peak_ID info
4. Output the entire line if it contains the MACS_peak_ID

Will be useful to supply these 2 files as argument, to be able to run on multiple files
