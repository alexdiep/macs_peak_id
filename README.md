MACS_PEAK_ID
===
Created for genetics lab in UF.

Install
---
```sh
$ pip install git+https://github.com/alexdiep/macs_peak_id
$ pip uninstall macs_peak_id
```

Usage
---
Script is imcomplete. Usage below does not apply for the time being.
```sh
$ macs_peak_id peaks.bed target1.fa target2.fa... 
```
```
$ ls .
peaks_target1.bed peaks_target2.bed peaks_targetnoN1.bed peaks_targetnoN2.bed
```
`peaks_target1.bed` contains rows matched with file `target1.fa`. `mac_peaks_id` also 
produces a counterpart, `peaks_target1_noN.bed`, containing nonmatched rows. Same naming 
scheme for `target2.fa`.

Issues
---
The script was created for the data in the folder. Tweaking is needed to apply for other 
datasets. Also, might be really slow.
