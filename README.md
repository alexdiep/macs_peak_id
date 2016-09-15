MACS_PEAK_ID
===
Created for genetics lab in UF.

Analysis the output of [HOMER](http://homer.salk.edu/homer/).

Install
---
```sh
$ pip install git+https://github.com/alexdiep/macs_peak_id
$ pip uninstall macs_peak_id
```

Usage
---
```sh
$ macs_peak_id peaks/ unmasked/
```
`peaks/` folder should contain all of the bed files desired for analysing.
`unmasked/` folder should be a HOMER output that contains target.fa.

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

Output would be a `results/` folder. To be programmed.
```
$tree results/
results
...
```