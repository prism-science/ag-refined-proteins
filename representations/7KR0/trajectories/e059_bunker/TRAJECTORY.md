# 7KR0 - six-copy water treatment trajectory (sixcopy_waters 1.5.2 (2026-10-11): work-only decision maps (D582); sleep third absent from phenix input (D584); sparse-first schedule (D586); bunker set held outside every working file (D587); step memo (a step already judged on the same base is not re-run))

Rewritten 2026-10-11T08:54:36Z. Evaluator: cctbx fmodel on the frozen data and inherited flags (flags.mtz sha256 717a4b44f207), R-free on the full free set and on the select / report halves (sleep withheld: 2904). Gap = R-free(full) - R-work. Clashscore: phenix.clashscore keep_hydrogens=True. Rotamers: phenix.rotalyze. The six-copy model is a representation (PROTOCOL 18.1), never a deliverable. Bunker (D587): 3400 work reflections in vault/, absent from every working file.

## Baseline (single model, standing recipe, 5 macro-cycles, N = 3)

| model | R-work | full | select | report | gap | clashscore | rotamers % |
|---|---|---|---|---|---|---|---|
| deposited, our flags | 0.11020 | 0.11826 | 0.12129 | 0.11537 | 0.0081 | | |
| re-refined mean | 0.10613 | 0.11602 | 0.11809 | 0.11404 | 0.0099 | 4.77 | 1.33 |
| re-refined sigma | | 0.00014 | 0.00019 | 0.00024 | 0.00008 | | |

## Build

| model | R-work | full | select | report | gap | water atoms | ANISOU | clashscore | rotamers % |
|---|---|---|---|---|---|---|---|---|---|
| deposited (our flags) | 0.11020 | 0.11826 | 0.12129 | 0.11537 | 0.0081 | 316 | 2310 |  |  |
| six copies unrefined | 0.17315 | 0.17620 | 0.18200 | 0.17064 | 0.0030 | 1896 | 9588 | 225.57 | 5.79 |
| S0 six copies, 20 mc | 0.09699 | 0.10955 | 0.11154 | 0.10763 | 0.0126 | 1896 | 9588 | 3.83 | 2.01 |

## Steps (every seed of both arms; weights = (wc, wu); floor sigma {"r_free_select": 0.000979, "r_free_report": 0.001081, "r_free_full": 0.001022, "n": 6, "provisional": true})

| step | arm | seed | R-work | full | select | report | gap | water atoms | ANISOU | clashscore | rotamers % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| r0_weights | cand | 1 | 0.09215 | 0.10783 | 0.11021 | 0.10556 | 0.0157 | 1020 | 8712 |  |  |
| r0_weights | cand | 2 | 0.09366 | 0.10904 | 0.11170 | 0.10650 | 0.0154 | 1020 | 8712 |  |  |
| r0_weights | cand | 3 | 0.09318 | 0.10864 | 0.11125 | 0.10614 | 0.0155 | 1020 | 8712 | 3.96 | 1.42 |
| r0_weights | ctrl | 1 | 0.09354 | 0.10719 | 0.10955 | 0.10493 | 0.0136 | 1020 | 8712 |  |  |
| r0_weights | ctrl | 2 | 0.09605 | 0.10949 | 0.11160 | 0.10746 | 0.0134 | 1020 | 8712 |  |  |
| r0_weights | ctrl | 3 | 0.09347 | 0.10726 | 0.10966 | 0.10496 | 0.0138 | 1020 | 8712 | 4.02 | 1.54 |
| r1_pick | cand | 1 | 0.07966 | 0.09490 | 0.09678 | 0.09311 | 0.0152 | 1555 | 8712 | 3.70 | 1.54 |
| r1_pick | cand | 2 | 0.07953 | 0.09496 | 0.09689 | 0.09311 | 0.0154 | 1555 | 8712 |  |  |
| r1_pick | cand | 3 | 0.07953 | 0.09465 | 0.09665 | 0.09274 | 0.0151 | 1555 | 8712 |  |  |
| r1_pick | ctrl | 1 | 0.09354 | 0.10719 | 0.10955 | 0.10493 | 0.0136 | 1020 | 8712 |  |  |
| r1_pick | ctrl | 2 | 0.09605 | 0.10949 | 0.11160 | 0.10746 | 0.0134 | 1020 | 8712 |  |  |
| r1_pick | ctrl | 3 | 0.09347 | 0.10726 | 0.10966 | 0.10496 | 0.0138 | 1020 | 8712 | 4.02 | 1.54 |
| r1_aniso_water | cand | 1 | 0.07471 | 0.09004 | 0.09191 | 0.08825 | 0.0153 | 1157 | 8849 | 4.02 | 1.18 |
| r1_aniso_water | cand | 2 | 0.07470 | 0.09006 | 0.09185 | 0.08834 | 0.0154 | 1157 | 8849 |  |  |
| r1_aniso_water | cand | 3 | 0.07490 | 0.09015 | 0.09196 | 0.08841 | 0.0152 | 1157 | 8849 |  |  |
| r1_aniso_water | ctrl | 1 | 0.07735 | 0.09330 | 0.09569 | 0.09102 | 0.0160 | 1157 | 8595 |  |  |
| r1_aniso_water | ctrl | 2 | 0.07726 | 0.09323 | 0.09575 | 0.09082 | 0.0160 | 1157 | 8595 | 4.02 | 1.18 |
| r1_aniso_water | ctrl | 3 | 0.07724 | 0.09324 | 0.09580 | 0.09079 | 0.0160 | 1157 | 8595 |  |  |
| r2_pick | cand | 1 | 0.06749 | 0.08635 | 0.08809 | 0.08469 | 0.0189 | 1860 | 8798 |  |  |
| r2_pick | cand | 2 | 0.06767 | 0.08638 | 0.08829 | 0.08455 | 0.0187 | 1860 | 8798 |  |  |
| r2_pick | cand | 3 | 0.06769 | 0.08634 | 0.08823 | 0.08453 | 0.0186 | 1860 | 8798 | 4.87 | 1.30 |
| r2_pick | ctrl | 1 | 0.07341 | 0.08920 | 0.09131 | 0.08718 | 0.0158 | 1106 | 8798 | 4.15 | 1.30 |
| r2_pick | ctrl | 2 | 0.07335 | 0.08915 | 0.09128 | 0.08711 | 0.0158 | 1106 | 8798 |  |  |
| r2_pick | ctrl | 3 | 0.07355 | 0.08926 | 0.09135 | 0.08726 | 0.0157 | 1106 | 8798 |  |  |
| r3_pick | cand | 1 | 0.07026 | 0.08715 | 0.08973 | 0.08469 | 0.0169 | 1465 | 8798 |  |  |
| r3_pick | cand | 2 | 0.07010 | 0.08725 | 0.08991 | 0.08470 | 0.0172 | 1465 | 8798 |  |  |
| r3_pick | cand | 3 | 0.07023 | 0.08706 | 0.08976 | 0.08448 | 0.0168 | 1465 | 8798 | 4.35 | 1.30 |
| r3_pick | ctrl | 1 | 0.07341 | 0.08920 | 0.09131 | 0.08718 | 0.0158 | 1106 | 8798 | 4.15 | 1.30 |
| r3_pick | ctrl | 2 | 0.07335 | 0.08915 | 0.09128 | 0.08711 | 0.0158 | 1106 | 8798 |  |  |
| r3_pick | ctrl | 3 | 0.07355 | 0.08926 | 0.09135 | 0.08726 | 0.0157 | 1106 | 8798 |  |  |
| r4_pick | cand | 1 | 0.07026 | 0.08715 | 0.08973 | 0.08469 | 0.0169 | 1465 | 8798 |  |  |
| r4_pick | cand | 2 | 0.07010 | 0.08725 | 0.08991 | 0.08470 | 0.0172 | 1465 | 8798 |  |  |
| r4_pick | cand | 3 | 0.07023 | 0.08706 | 0.08976 | 0.08448 | 0.0168 | 1465 | 8798 | 4.35 | 1.30 |
| r4_pick | ctrl | 1 | 0.07341 | 0.08920 | 0.09131 | 0.08718 | 0.0158 | 1106 | 8798 | 4.15 | 1.30 |
| r4_pick | ctrl | 2 | 0.07335 | 0.08915 | 0.09128 | 0.08711 | 0.0158 | 1106 | 8798 |  |  |
| r4_pick | ctrl | 3 | 0.07355 | 0.08926 | 0.09135 | 0.08726 | 0.0157 | 1106 | 8798 |  |  |

## Decisions

- **r0_weights** (weights, weights cand [0.3, 0.25] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select +0.00078 not <= -2 sigma (0.00098); report +0.00028 does not agree in sign. dselect +0.00078 (sigma 0.00098), dreport +0.00028, dfull +0.00053, dgap +0.00188; cand mean full 0.10850 / ctrl 0.10798; clashscore 3.96 / 4.02; rotamers 1.42 / 1.54
- **r1_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **ADOPTED** - all criteria met. dselect -0.01350 (sigma 0.00098), dreport -0.01280, dfull -0.01314, dgap +0.00164; cand mean full 0.09484 / ctrl 0.10798; clashscore 3.70 / 4.02; rotamers 1.54 / 1.54. {"sigma": 4.0, "n_peaks": 139, "n_sites": 121, "n_copies": 535}. Adopted model `/home/dev/runs/7KR0/experiments/e059_bunker/steps/r1_pick/cand_s1.pdb`
- **r1_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **ADOPTED** - all criteria met. dselect -0.00384 (sigma 0.00098), dreport -0.00255, dfull -0.00318, dgap -0.00066; cand mean full 0.09008 / ctrl 0.09326; clashscore 4.02 / 4.02; rotamers 1.18 / 1.18. {"n_water_iso": 254}. Adopted model `/home/dev/runs/7KR0/experiments/e059_bunker/steps/r1_aniso_water/cand_s1.pdb`
- **r2_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - gap widens +0.00298 > 0.002. dselect -0.00311 (sigma 0.00098), dreport -0.00259, dfull -0.00285, dgap +0.00298; cand mean full 0.08636 / ctrl 0.08920; clashscore 4.87 / 4.15; rotamers 1.30 / 1.30. {"sigma": 3.0, "n_peaks": 316, "n_sites": 208, "n_copies": 754}
- **r2_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - every water already anisotropic. {"n_water_iso": 0}
- **r3_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select -0.00151 not <= -2 sigma (0.00098). dselect -0.00151 (sigma 0.00098), dreport -0.00256, dfull -0.00205, dgap +0.00120; cand mean full 0.08716 / ctrl 0.08920; clashscore 4.35 / 4.15; rotamers 1.30 / 1.30. {"sigma": 4.0, "n_peaks": 115, "n_sites": 89, "n_copies": 359}
- **r3_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - every water already anisotropic. {"n_water_iso": 0}
- **r4_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select -0.00151 not <= -2 sigma (0.00098). dselect -0.00151 (sigma 0.00098), dreport -0.00256, dfull -0.00205, dgap +0.00120; cand mean full 0.08716 / ctrl 0.08920; clashscore 4.35 / 4.15; rotamers 1.30 / 1.30. {"sigma": 4.0, "n_peaks": 115, "n_sites": 89, "n_copies": 359}
- **r4_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - every water already anisotropic. {"n_water_iso": 0}

## Rounds

| round | adopted | model in force | full | clashscore | rotamers % | ended |
|---|---|---|---|---|---|---|
| 1 | True | `/home/dev/runs/7KR0/experiments/e059_bunker/steps/r1_aniso_water/cand_s1.pdb` | 0.09004 | 4.02 | 1.18 | 2026-10-11T05:35:05Z |
| 2 | False | `/home/dev/runs/7KR0/experiments/e059_bunker/steps/r1_aniso_water/cand_s1.pdb` | 0.09004 | 4.02 | 1.18 | 2026-10-11T07:14:33Z |
| 3 | False | `/home/dev/runs/7KR0/experiments/e059_bunker/steps/r1_aniso_water/cand_s1.pdb` | 0.09004 | 4.02 | 1.18 | 2026-10-11T08:50:09Z |
| 4 | False | `/home/dev/runs/7KR0/experiments/e059_bunker/steps/r1_aniso_water/cand_s1.pdb` | 0.09004 | 4.02 | 1.18 | 2026-10-11T08:53:14Z |

**Stopped** 2026-10-11T08:53:14Z: 3 consecutive rounds without an adopted step. Final model `/home/dev/runs/7KR0/experiments/e059_bunker/steps/r1_aniso_water/cand_s1.pdb`.

## Final (independent scorer: fmodel on all reflections, no outlier rejection, manual R)

| model | R-work | R-free | select | report | clashscore | rotamers % | atoms |
|---|---|---|---|---|---|---|---|
| final | 0.07471 | 0.09004 | 0.09161 | 0.08794 | 4.02 | 1.18 | 16571 |
| S0 | 0.09699 | 0.10955 | 0.11153 | 0.10763 | 3.83 | 2.01 | 17310 |
| baseline_median | 0.10621 | 0.11614 | 0.11807 | 0.11431 | 4.77 | 1.33 | 4300 |
| deposited | 0.11020 | 0.11826 | 0.12135 | 0.11531 |  |  | 4300 |

## Sleep-third consultations (PROTOCOL 3.8)

- 2026-10-11T08:54:30Z root: R-free sleep 0.08862 (E059 final (D587): the clean 7KR0 six-copy ensemble on the bunkered working data (2 % of the work reflections in the vault), stopped 2026-10-11T08:53Z after three rounds without an adoption (round-1 model); the one logged sleep-third consultation and the one vault read (PROTOCOL 3.8, proposed 3.10))
