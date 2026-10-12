# 7KR0 - six-copy water treatment trajectory (sixcopy_waters 1.5.2 (2026-10-11): work-only decision maps (D582); sleep third absent from phenix input (D584); sparse-first schedule (D586); bunker set held outside every working file (D587); step memo (a step already judged on the same base is not re-run))

Rewritten 2026-10-11T07:37:32Z. Evaluator: cctbx fmodel on the frozen data and inherited flags (flags.mtz sha256 8c34618c120d), R-free on the full free set and on the select / report halves (sleep withheld: 2904). Gap = R-free(full) - R-work. Clashscore: phenix.clashscore keep_hydrogens=True. Rotamers: phenix.rotalyze. The six-copy model is a representation (PROTOCOL 18.1), never a deliverable. Bunker (D587): none.

## Baseline (single model, standing recipe, 5 macro-cycles, N = 3)

| model | R-work | full | select | report | gap | clashscore | rotamers % |
|---|---|---|---|---|---|---|---|
| deposited, our flags | 0.11031 | 0.11835 | 0.12153 | 0.11531 | 0.0080 | | |
| re-refined mean | 0.10621 | 0.11619 | 0.11834 | 0.11413 | 0.0100 | 5.27 | 1.33 |
| re-refined sigma | | 0.00004 | 0.00013 | 0.00009 | 0.00004 | | |

## Build

| model | R-work | full | select | report | gap | water atoms | ANISOU | clashscore | rotamers % |
|---|---|---|---|---|---|---|---|---|---|
| deposited (our flags) | 0.11031 | 0.11835 | 0.12153 | 0.11531 | 0.0080 | 316 | 2310 |  |  |
| six copies unrefined | 0.17321 | 0.17613 | 0.18197 | 0.17055 | 0.0029 | 1896 | 9588 | 225.57 | 5.79 |
| S0 six copies, 20 mc | 0.09725 | 0.10921 | 0.11075 | 0.10773 | 0.0120 | 1896 | 9588 | 4.15 | 2.01 |

## Steps (every seed of both arms; weights = (wc, wu); floor sigma {"r_free_select": 0.000262, "r_free_report": 0.000296, "r_free_full": 0.000276, "n": 6, "provisional": true})

| step | arm | seed | R-work | full | select | report | gap | water atoms | ANISOU | clashscore | rotamers % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| r0_weights | cand | 1 | 0.09220 | 0.10749 | 0.11002 | 0.10507 | 0.0153 | 1054 | 8746 |  |  |
| r0_weights | cand | 2 | 0.09318 | 0.10817 | 0.11069 | 0.10575 | 0.0150 | 1054 | 8746 |  |  |
| r0_weights | cand | 3 | 0.09317 | 0.10815 | 0.11058 | 0.10582 | 0.0150 | 1054 | 8746 | 3.83 | 1.42 |
| r0_weights | ctrl | 1 | 0.09379 | 0.10716 | 0.10963 | 0.10480 | 0.0134 | 1054 | 8746 |  |  |
| r0_weights | ctrl | 2 | 0.09368 | 0.10725 | 0.10977 | 0.10484 | 0.0136 | 1054 | 8746 |  |  |
| r0_weights | ctrl | 3 | 0.09373 | 0.10720 | 0.10964 | 0.10486 | 0.0135 | 1054 | 8746 | 3.57 | 1.54 |
| r1_pick | cand | 1 | 0.07991 | 0.09443 | 0.09738 | 0.09161 | 0.0145 | 1571 | 8746 |  |  |
| r1_pick | cand | 2 | 0.07979 | 0.09404 | 0.09762 | 0.09061 | 0.0142 | 1571 | 8746 | 3.89 | 1.54 |
| r1_pick | cand | 3 | 0.08005 | 0.09464 | 0.09844 | 0.09101 | 0.0146 | 1571 | 8746 |  |  |
| r1_pick | ctrl | 1 | 0.09379 | 0.10716 | 0.10963 | 0.10480 | 0.0134 | 1054 | 8746 |  |  |
| r1_pick | ctrl | 2 | 0.09368 | 0.10725 | 0.10977 | 0.10484 | 0.0136 | 1054 | 8746 |  |  |
| r1_pick | ctrl | 3 | 0.09373 | 0.10720 | 0.10964 | 0.10486 | 0.0135 | 1054 | 8746 | 3.57 | 1.54 |
| r1_aniso_water | cand | 1 | 0.07498 | 0.08986 | 0.09325 | 0.08662 | 0.0149 | 1153 | 8845 |  |  |
| r1_aniso_water | cand | 2 | 0.07508 | 0.08994 | 0.09326 | 0.08677 | 0.0149 | 1153 | 8845 | 4.28 | 1.42 |
| r1_aniso_water | cand | 3 | 0.07489 | 0.08985 | 0.09327 | 0.08658 | 0.0150 | 1153 | 8845 |  |  |
| r1_aniso_water | ctrl | 1 | 0.07738 | 0.09287 | 0.09670 | 0.08919 | 0.0155 | 1153 | 8594 | 4.35 | 1.42 |
| r1_aniso_water | ctrl | 2 | 0.07722 | 0.09293 | 0.09689 | 0.08913 | 0.0157 | 1153 | 8594 |  |  |
| r1_aniso_water | ctrl | 3 | 0.07745 | 0.09280 | 0.09643 | 0.08933 | 0.0153 | 1153 | 8594 |  |  |
| r2_pick | cand | 1 | 0.06811 | 0.08639 | 0.09017 | 0.08277 | 0.0183 | 1851 | 8783 |  |  |
| r2_pick | cand | 2 | 0.06811 | 0.08636 | 0.09013 | 0.08274 | 0.0182 | 1851 | 8783 | 5.25 | 1.54 |
| r2_pick | cand | 3 | 0.06799 | 0.08641 | 0.09004 | 0.08293 | 0.0184 | 1851 | 8783 |  |  |
| r2_pick | ctrl | 1 | 0.07352 | 0.08942 | 0.09318 | 0.08581 | 0.0159 | 1091 | 8783 |  |  |
| r2_pick | ctrl | 2 | 0.07335 | 0.08928 | 0.09308 | 0.08563 | 0.0159 | 1091 | 8783 | 4.61 | 1.42 |
| r2_pick | ctrl | 3 | 0.07326 | 0.08927 | 0.09305 | 0.08564 | 0.0160 | 1091 | 8783 |  |  |
| r3_pick | cand | 1 | 0.07053 | 0.08757 | 0.09156 | 0.08376 | 0.0170 | 1463 | 8783 |  |  |
| r3_pick | cand | 2 | 0.07035 | 0.08764 | 0.09180 | 0.08366 | 0.0173 | 1463 | 8783 |  |  |
| r3_pick | cand | 3 | 0.07053 | 0.08766 | 0.09174 | 0.08376 | 0.0171 | 1463 | 8783 | 4.67 | 1.42 |
| r3_pick | ctrl | 1 | 0.07352 | 0.08942 | 0.09318 | 0.08581 | 0.0159 | 1091 | 8783 |  |  |
| r3_pick | ctrl | 2 | 0.07335 | 0.08928 | 0.09308 | 0.08563 | 0.0159 | 1091 | 8783 | 4.61 | 1.42 |
| r3_pick | ctrl | 3 | 0.07326 | 0.08927 | 0.09305 | 0.08564 | 0.0160 | 1091 | 8783 |  |  |
| r3_aniso_water | cand | 1 | 0.06860 | 0.08637 | 0.08951 | 0.08336 | 0.0178 | 1310 | 9002 |  |  |
| r3_aniso_water | cand | 2 | 0.06860 | 0.08666 | 0.08986 | 0.08359 | 0.0181 | 1310 | 9002 |  |  |
| r3_aniso_water | cand | 3 | 0.06871 | 0.08659 | 0.08985 | 0.08347 | 0.0179 | 1310 | 9002 | 4.61 | 1.42 |
| r3_aniso_water | ctrl | 1 | 0.06935 | 0.08710 | 0.09107 | 0.08329 | 0.0178 | 1310 | 8754 | 4.74 | 1.42 |
| r3_aniso_water | ctrl | 2 | 0.06944 | 0.08720 | 0.09118 | 0.08340 | 0.0178 | 1310 | 8754 |  |  |
| r3_aniso_water | ctrl | 3 | 0.06942 | 0.08714 | 0.09100 | 0.08344 | 0.0177 | 1310 | 8754 |  |  |
| r4_pick | cand | 1 | 0.06600 | 0.08579 | 0.09044 | 0.08133 | 0.0198 | 1894 | 8754 | 5.06 | 1.42 |
| r4_pick | cand | 2 | 0.06607 | 0.08612 | 0.09086 | 0.08158 | 0.0200 | 1894 | 8754 |  |  |
| r4_pick | cand | 3 | 0.06592 | 0.08578 | 0.09040 | 0.08135 | 0.0199 | 1894 | 8754 |  |  |
| r4_pick | ctrl | 1 | 0.06935 | 0.08710 | 0.09107 | 0.08329 | 0.0178 | 1310 | 8754 | 4.74 | 1.42 |
| r4_pick | ctrl | 2 | 0.06944 | 0.08720 | 0.09118 | 0.08340 | 0.0178 | 1310 | 8754 |  |  |
| r4_pick | ctrl | 3 | 0.06942 | 0.08714 | 0.09100 | 0.08344 | 0.0177 | 1310 | 8754 |  |  |
| r4_aniso_water | cand | 1 | 0.06860 | 0.08637 | 0.08951 | 0.08336 | 0.0178 | 1310 | 9002 |  |  |
| r4_aniso_water | cand | 2 | 0.06860 | 0.08666 | 0.08986 | 0.08359 | 0.0181 | 1310 | 9002 |  |  |
| r4_aniso_water | cand | 3 | 0.06871 | 0.08659 | 0.08985 | 0.08347 | 0.0179 | 1310 | 9002 | 4.61 | 1.42 |
| r4_aniso_water | ctrl | 1 | 0.06935 | 0.08710 | 0.09107 | 0.08329 | 0.0178 | 1310 | 8754 | 4.74 | 1.42 |
| r4_aniso_water | ctrl | 2 | 0.06944 | 0.08720 | 0.09118 | 0.08340 | 0.0178 | 1310 | 8754 |  |  |
| r4_aniso_water | ctrl | 3 | 0.06942 | 0.08714 | 0.09100 | 0.08344 | 0.0177 | 1310 | 8754 |  |  |
| r5_pick | cand | 1 | 0.06813 | 0.08696 | 0.09104 | 0.08305 | 0.0188 | 1452 | 8754 |  |  |
| r5_pick | cand | 2 | 0.06825 | 0.08682 | 0.09071 | 0.08310 | 0.0186 | 1452 | 8754 |  |  |
| r5_pick | cand | 3 | 0.06813 | 0.08688 | 0.09078 | 0.08315 | 0.0187 | 1452 | 8754 | 4.61 | 1.42 |
| r5_pick | ctrl | 1 | 0.06935 | 0.08710 | 0.09107 | 0.08329 | 0.0178 | 1310 | 8754 | 4.74 | 1.42 |
| r5_pick | ctrl | 2 | 0.06944 | 0.08720 | 0.09118 | 0.08340 | 0.0178 | 1310 | 8754 |  |  |
| r5_pick | ctrl | 3 | 0.06942 | 0.08714 | 0.09100 | 0.08344 | 0.0177 | 1310 | 8754 |  |  |
| r5_aniso_water | cand | 1 | 0.06860 | 0.08637 | 0.08951 | 0.08336 | 0.0178 | 1310 | 9002 |  |  |
| r5_aniso_water | cand | 2 | 0.06860 | 0.08666 | 0.08986 | 0.08359 | 0.0181 | 1310 | 9002 |  |  |
| r5_aniso_water | cand | 3 | 0.06871 | 0.08659 | 0.08985 | 0.08347 | 0.0179 | 1310 | 9002 | 4.61 | 1.42 |
| r5_aniso_water | ctrl | 1 | 0.06935 | 0.08710 | 0.09107 | 0.08329 | 0.0178 | 1310 | 8754 | 4.74 | 1.42 |
| r5_aniso_water | ctrl | 2 | 0.06944 | 0.08720 | 0.09118 | 0.08340 | 0.0178 | 1310 | 8754 |  |  |
| r5_aniso_water | ctrl | 3 | 0.06942 | 0.08714 | 0.09100 | 0.08344 | 0.0177 | 1310 | 8754 |  |  |
| r6_pick | cand | 1 | 0.06813 | 0.08696 | 0.09104 | 0.08305 | 0.0188 | 1452 | 8754 |  |  |
| r6_pick | cand | 2 | 0.06825 | 0.08682 | 0.09071 | 0.08310 | 0.0186 | 1452 | 8754 |  |  |
| r6_pick | cand | 3 | 0.06813 | 0.08688 | 0.09078 | 0.08315 | 0.0187 | 1452 | 8754 | 4.61 | 1.42 |
| r6_pick | ctrl | 1 | 0.06935 | 0.08710 | 0.09107 | 0.08329 | 0.0178 | 1310 | 8754 | 4.74 | 1.42 |
| r6_pick | ctrl | 2 | 0.06944 | 0.08720 | 0.09118 | 0.08340 | 0.0178 | 1310 | 8754 |  |  |
| r6_pick | ctrl | 3 | 0.06942 | 0.08714 | 0.09100 | 0.08344 | 0.0177 | 1310 | 8754 |  |  |
| r6_aniso_water | cand | 1 | 0.06860 | 0.08637 | 0.08951 | 0.08336 | 0.0178 | 1310 | 9002 |  |  |
| r6_aniso_water | cand | 2 | 0.06860 | 0.08666 | 0.08986 | 0.08359 | 0.0181 | 1310 | 9002 |  |  |
| r6_aniso_water | cand | 3 | 0.06871 | 0.08659 | 0.08985 | 0.08347 | 0.0179 | 1310 | 9002 | 4.61 | 1.42 |
| r6_aniso_water | ctrl | 1 | 0.06935 | 0.08710 | 0.09107 | 0.08329 | 0.0178 | 1310 | 8754 | 4.74 | 1.42 |
| r6_aniso_water | ctrl | 2 | 0.06944 | 0.08720 | 0.09118 | 0.08340 | 0.0178 | 1310 | 8754 |  |  |
| r6_aniso_water | ctrl | 3 | 0.06942 | 0.08714 | 0.09100 | 0.08344 | 0.0177 | 1310 | 8754 |  |  |

## Decisions

- **r0_weights** (weights, weights cand [0.3, 0.25] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select +0.00075 not <= -2 sigma (0.00026); report +0.00072 does not agree in sign. dselect +0.00075 (sigma 0.00026), dreport +0.00072, dfull +0.00073, dgap +0.00161; cand mean full 0.10794 / ctrl 0.10720; clashscore 3.83 / 3.57; rotamers 1.42 / 1.54
- **r1_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **ADOPTED** - all criteria met. dselect -0.01187 (sigma 0.00040), dreport -0.01375, dfull -0.01283, dgap +0.00098; cand mean full 0.09437 / ctrl 0.10720; clashscore 3.89 / 3.57; rotamers 1.54 / 1.54. {"sigma": 4.0, "n_peaks": 138, "n_sites": 120, "n_copies": 517}. Adopted model `/home/dev/runs/7KR0/experiments/e051b_workonly/steps/r1_pick/cand_s2.pdb`
- **r1_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **ADOPTED** - all criteria met. dselect -0.00341 (sigma 0.00026), dreport -0.00256, dfull -0.00298, dgap -0.00061; cand mean full 0.08989 / ctrl 0.09287; clashscore 4.28 / 4.35; rotamers 1.42 / 1.42. {"n_water_iso": 251}. Adopted model `/home/dev/runs/7KR0/experiments/e051b_workonly/steps/r1_aniso_water/cand_s2.pdb`
- **r2_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - clashscore 5.25 > 5 and above control 4.61; rotamer outliers 1.54% > 1.5% and above control 1.42%; gap widens +0.00237 > 0.002. dselect -0.00299 (sigma 0.00026), dreport -0.00288, dfull -0.00293, dgap +0.00237; cand mean full 0.08639 / ctrl 0.08932; clashscore 5.25 / 4.61; rotamers 1.54 / 1.42. {"sigma": 3.0, "n_peaks": 320, "n_sites": 209, "n_copies": 760}
- **r2_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - every water already anisotropic. {"n_water_iso": 0}
- **r3_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **ADOPTED** - all criteria met. dselect -0.00141 (sigma 0.00026), dreport -0.00197, dfull -0.00169, dgap +0.00121; cand mean full 0.08763 / ctrl 0.08932; clashscore 4.67 / 4.61; rotamers 1.42 / 1.42. {"sigma": 4.0, "n_peaks": 116, "n_sites": 90, "n_copies": 372}. Adopted model `/home/dev/runs/7KR0/experiments/e051b_workonly/steps/r3_pick/cand_s3.pdb`
- **r3_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - report +0.00010 does not agree in sign. dselect -0.00135 (sigma 0.00026), dreport +0.00010, dfull -0.00061, dgap +0.00016; cand mean full 0.08654 / ctrl 0.08715; clashscore 4.61 / 4.74; rotamers 1.42 / 1.42. {"n_water_iso": 248}
- **r4_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select -0.00052 not <= -2 sigma (0.00026); clashscore 5.06 > 5 and above control 4.74; gap widens +0.00216 > 0.002. dselect -0.00052 (sigma 0.00026), dreport -0.00195, dfull -0.00125, dgap +0.00216; cand mean full 0.08590 / ctrl 0.08715; clashscore 5.06 / 4.74; rotamers 1.42 / 1.42. {"sigma": 3.0, "n_peaks": 297, "n_sites": 175, "n_copies": 584}
- **r4_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - report +0.00010 does not agree in sign. dselect -0.00135 (sigma 0.00026), dreport +0.00010, dfull -0.00061, dgap +0.00016; cand mean full 0.08654 / ctrl 0.08715; clashscore 4.61 / 4.74; rotamers 1.42 / 1.42. {"n_water_iso": 248}
- **r5_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select -0.00024 not <= -2 sigma (0.00026). dselect -0.00024 (sigma 0.00026), dreport -0.00028, dfull -0.00026, dgap +0.00097; cand mean full 0.08689 / ctrl 0.08715; clashscore 4.61 / 4.74; rotamers 1.42 / 1.42. {"sigma": 4.0, "n_peaks": 69, "n_sites": 42, "n_copies": 142}
- **r5_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - report +0.00010 does not agree in sign. dselect -0.00135 (sigma 0.00026), dreport +0.00010, dfull -0.00061, dgap +0.00016; cand mean full 0.08654 / ctrl 0.08715; clashscore 4.61 / 4.74; rotamers 1.42 / 1.42. {"n_water_iso": 248}
- **r6_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select -0.00024 not <= -2 sigma (0.00026). dselect -0.00024 (sigma 0.00026), dreport -0.00028, dfull -0.00026, dgap +0.00097; cand mean full 0.08689 / ctrl 0.08715; clashscore 4.61 / 4.74; rotamers 1.42 / 1.42. {"sigma": 4.0, "n_peaks": 69, "n_sites": 42, "n_copies": 142}
- **r6_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - report +0.00010 does not agree in sign. dselect -0.00135 (sigma 0.00026), dreport +0.00010, dfull -0.00061, dgap +0.00016; cand mean full 0.08654 / ctrl 0.08715; clashscore 4.61 / 4.74; rotamers 1.42 / 1.42. {"n_water_iso": 248}

## Rounds

| round | adopted | model in force | full | clashscore | rotamers % | ended |
|---|---|---|---|---|---|---|
| 1 | True | `/home/dev/runs/7KR0/experiments/e051b_workonly/steps/r1_aniso_water/cand_s2.pdb` | 0.08994 | 4.28 | 1.42 | 2026-10-10T23:16:38Z |
| 2 | False | `/home/dev/runs/7KR0/experiments/e051b_workonly/steps/r1_aniso_water/cand_s2.pdb` | 0.08994 | 4.28 | 1.42 | 2026-10-11T00:51:51Z |
| 3 | True | `/home/dev/runs/7KR0/experiments/e051b_workonly/steps/r3_pick/cand_s3.pdb` | 0.08766 | 4.67 | 1.42 | 2026-10-11T04:08:44Z |
| 4 | False | `/home/dev/runs/7KR0/experiments/e051b_workonly/steps/r3_pick/cand_s3.pdb` | 0.08766 | 4.67 | 1.42 | 2026-10-11T05:52:02Z |
| 5 | False | `/home/dev/runs/7KR0/experiments/e051b_workonly/steps/r3_pick/cand_s3.pdb` | 0.08766 | 4.67 | 1.42 | 2026-10-11T07:31:36Z |
| 6 | False | `/home/dev/runs/7KR0/experiments/e051b_workonly/steps/r3_pick/cand_s3.pdb` | 0.08766 | 4.67 | 1.42 | 2026-10-11T07:36:17Z |

**Stopped** 2026-10-11T07:36:17Z: 3 consecutive rounds without an adopted step. Final model `/home/dev/runs/7KR0/experiments/e051b_workonly/steps/r3_pick/cand_s3.pdb`.

## Final (independent scorer: fmodel on all reflections, no outlier rejection, manual R)

| model | R-work | R-free | select | report | clashscore | rotamers % | atoms |
|---|---|---|---|---|---|---|---|
| final | 0.07053 | 0.08766 | 0.09130 | 0.08348 | 4.67 | 1.42 | 16877 |
| S0 | 0.09725 | 0.10921 | 0.11074 | 0.10773 | 4.15 | 2.01 | 17310 |
| baseline_median | 0.10617 | 0.11615 | 0.11831 | 0.11409 | 5.27 | 1.33 | 4300 |
| deposited | 0.11031 | 0.11835 | 0.12158 | 0.11528 |  |  | 4300 |

## Sleep-third consultations (PROTOCOL 3.8)

- 2026-10-11T07:37:32Z root: R-free sleep 0.08502 (E051b final (D583 b, D586): the clean 7KR0 six-copy ensemble under the work-only-map script with the sparse-first schedule, stopped 2026-10-11 after three rounds without an adoption (round-3 model); the one logged sleep-third consultation (PROTOCOL 3.8))
