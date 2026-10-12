# 7KR0 - six-copy water treatment trajectory (sixcopy_waters 1.8 (2026-10-11): single-copy picks - one labelled water per peak (E063); work-only decision maps (D582); sleep third absent from phenix input (D584); sparse-first schedule (D586); bunker set held outside every working file (D587); half-map peak agreement and water-site occupancy cap (E062); step memo (a step already judged on the same base is not re-run); floor sigma from ten r0 refinements (D594))

Rewritten 2026-10-12T07:59:04Z. Evaluator: cctbx fmodel on the frozen data and inherited flags (flags.mtz sha256 5f47d255934d), R-free on the full free set and on the select / report halves (sleep withheld: 2904). Gap = R-free(full) - R-work. Clashscore: phenix.clashscore keep_hydrogens=True. Rotamers: phenix.rotalyze. The six-copy model is a representation (PROTOCOL 18.1), never a deliverable. Bunker (D587): 3400 work reflections in vault/, absent from every working file.

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

## Steps (every seed of both arms; weights = (wc, wu); floor sigma {"r_free_select": 0.00085, "r_free_report": 0.000866, "r_free_full": 0.000848, "n": 10, "provisional": false})

| step | arm | seed | R-work | full | select | report | gap | water atoms | ANISOU | clashscore | rotamers % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| r0_weights | cand | 1 | 0.09215 | 0.10783 | 0.11021 | 0.10556 | 0.0157 | 1020 | 8712 |  |  |
| r0_weights | cand | 2 | 0.09366 | 0.10904 | 0.11170 | 0.10650 | 0.0154 | 1020 | 8712 |  |  |
| r0_weights | cand | 3 | 0.09318 | 0.10864 | 0.11125 | 0.10614 | 0.0155 | 1020 | 8712 |  |  |
| r0_weights | cand | 4 | 0.09318 | 0.10861 | 0.11094 | 0.10638 | 0.0154 | 1020 | 8712 | 3.96 | 1.54 |
| r0_weights | cand | 5 | 0.09266 | 0.10835 | 0.11077 | 0.10603 | 0.0157 | 1020 | 8712 |  |  |
| r0_weights | ctrl | 1 | 0.09354 | 0.10719 | 0.10955 | 0.10493 | 0.0136 | 1020 | 8712 |  |  |
| r0_weights | ctrl | 2 | 0.09605 | 0.10949 | 0.11160 | 0.10746 | 0.0134 | 1020 | 8712 |  |  |
| r0_weights | ctrl | 3 | 0.09347 | 0.10726 | 0.10966 | 0.10496 | 0.0138 | 1020 | 8712 |  |  |
| r0_weights | ctrl | 4 | 0.09562 | 0.10907 | 0.11149 | 0.10675 | 0.0134 | 1020 | 8712 | 4.02 | 1.54 |
| r0_weights | ctrl | 5 | 0.09555 | 0.10915 | 0.11155 | 0.10685 | 0.0136 | 1020 | 8712 |  |  |
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
| r2_pick | cand | 1 | 0.06773 | 0.08514 | 0.08764 | 0.08274 | 0.0174 | 1341 | 8798 |  |  |
| r2_pick | cand | 2 | 0.06771 | 0.08490 | 0.08736 | 0.08254 | 0.0172 | 1341 | 8798 |  |  |
| r2_pick | cand | 3 | 0.06775 | 0.08485 | 0.08753 | 0.08228 | 0.0171 | 1341 | 8798 | 4.61 | 1.18 |
| r2_pick | ctrl | 1 | 0.07341 | 0.08920 | 0.09131 | 0.08718 | 0.0158 | 1106 | 8798 | 4.15 | 1.30 |
| r2_pick | ctrl | 2 | 0.07335 | 0.08915 | 0.09128 | 0.08711 | 0.0158 | 1106 | 8798 |  |  |
| r2_pick | ctrl | 3 | 0.07355 | 0.08926 | 0.09135 | 0.08726 | 0.0157 | 1106 | 8798 |  |  |
| r2_aniso_water | cand | 1 | 0.06448 | 0.08329 | 0.08494 | 0.08170 | 0.0188 | 1281 | 8973 |  |  |
| r2_aniso_water | cand | 2 | 0.06448 | 0.08317 | 0.08493 | 0.08148 | 0.0187 | 1281 | 8973 | 5.00 | 1.30 |
| r2_aniso_water | cand | 3 | 0.06455 | 0.08318 | 0.08487 | 0.08156 | 0.0186 | 1281 | 8973 |  |  |
| r2_aniso_water | ctrl | 1 | 0.06604 | 0.08434 | 0.08653 | 0.08225 | 0.0183 | 1281 | 8738 | 5.00 | 1.30 |
| r2_aniso_water | ctrl | 2 | 0.06598 | 0.08424 | 0.08648 | 0.08209 | 0.0183 | 1281 | 8738 |  |  |
| r2_aniso_water | ctrl | 3 | 0.06598 | 0.08422 | 0.08658 | 0.08196 | 0.0182 | 1281 | 8738 |  |  |
| r3_pick | cand | 1 | 0.06292 | 0.08480 | 0.08745 | 0.08227 | 0.0219 | 1604 | 8738 | 5.38 | 1.30 |
| r3_pick | cand | 2 | 0.06312 | 0.08490 | 0.08760 | 0.08231 | 0.0218 | 1604 | 8738 |  |  |
| r3_pick | cand | 3 | 0.06302 | 0.08486 | 0.08742 | 0.08242 | 0.0218 | 1604 | 8738 |  |  |
| r3_pick | ctrl | 1 | 0.06604 | 0.08434 | 0.08653 | 0.08225 | 0.0183 | 1281 | 8738 | 5.00 | 1.30 |
| r3_pick | ctrl | 2 | 0.06598 | 0.08424 | 0.08648 | 0.08209 | 0.0183 | 1281 | 8738 |  |  |
| r3_pick | ctrl | 3 | 0.06598 | 0.08422 | 0.08658 | 0.08196 | 0.0182 | 1281 | 8738 |  |  |
| r3_aniso_water | cand | 1 | 0.06448 | 0.08329 | 0.08494 | 0.08170 | 0.0188 | 1281 | 8973 |  |  |
| r3_aniso_water | cand | 2 | 0.06448 | 0.08317 | 0.08493 | 0.08148 | 0.0187 | 1281 | 8973 | 5.00 | 1.30 |
| r3_aniso_water | cand | 3 | 0.06455 | 0.08318 | 0.08487 | 0.08156 | 0.0186 | 1281 | 8973 |  |  |
| r3_aniso_water | ctrl | 1 | 0.06604 | 0.08434 | 0.08653 | 0.08225 | 0.0183 | 1281 | 8738 | 5.00 | 1.30 |
| r3_aniso_water | ctrl | 2 | 0.06598 | 0.08424 | 0.08648 | 0.08209 | 0.0183 | 1281 | 8738 |  |  |
| r3_aniso_water | ctrl | 3 | 0.06598 | 0.08422 | 0.08658 | 0.08196 | 0.0182 | 1281 | 8738 |  |  |
| r4_pick | cand | 1 | 0.06361 | 0.08403 | 0.08559 | 0.08254 | 0.0204 | 1438 | 8738 | 5.25 | 1.30 |
| r4_pick | cand | 2 | 0.06377 | 0.08404 | 0.08565 | 0.08249 | 0.0203 | 1438 | 8738 |  |  |
| r4_pick | cand | 3 | 0.06378 | 0.08393 | 0.08554 | 0.08238 | 0.0202 | 1438 | 8738 |  |  |
| r4_pick | ctrl | 1 | 0.06604 | 0.08434 | 0.08653 | 0.08225 | 0.0183 | 1281 | 8738 | 5.00 | 1.30 |
| r4_pick | ctrl | 2 | 0.06598 | 0.08424 | 0.08648 | 0.08209 | 0.0183 | 1281 | 8738 |  |  |
| r4_pick | ctrl | 3 | 0.06598 | 0.08422 | 0.08658 | 0.08196 | 0.0182 | 1281 | 8738 |  |  |
| r4_aniso_water | cand | 1 | 0.06448 | 0.08329 | 0.08494 | 0.08170 | 0.0188 | 1281 | 8973 |  |  |
| r4_aniso_water | cand | 2 | 0.06448 | 0.08317 | 0.08493 | 0.08148 | 0.0187 | 1281 | 8973 | 5.00 | 1.30 |
| r4_aniso_water | cand | 3 | 0.06455 | 0.08318 | 0.08487 | 0.08156 | 0.0186 | 1281 | 8973 |  |  |
| r4_aniso_water | ctrl | 1 | 0.06604 | 0.08434 | 0.08653 | 0.08225 | 0.0183 | 1281 | 8738 | 5.00 | 1.30 |
| r4_aniso_water | ctrl | 2 | 0.06598 | 0.08424 | 0.08648 | 0.08209 | 0.0183 | 1281 | 8738 |  |  |
| r4_aniso_water | ctrl | 3 | 0.06598 | 0.08422 | 0.08658 | 0.08196 | 0.0182 | 1281 | 8738 |  |  |
| r5_pick | cand | 1 | 0.06561 | 0.08505 | 0.08670 | 0.08347 | 0.0194 | 1307 | 8738 | 4.87 | 1.30 |
| r5_pick | cand | 2 | 0.06523 | 0.08477 | 0.08640 | 0.08321 | 0.0195 | 1307 | 8738 |  |  |
| r5_pick | cand | 3 | 0.06552 | 0.08512 | 0.08693 | 0.08339 | 0.0196 | 1307 | 8738 |  |  |
| r5_pick | ctrl | 1 | 0.06604 | 0.08434 | 0.08653 | 0.08225 | 0.0183 | 1281 | 8738 | 5.00 | 1.30 |
| r5_pick | ctrl | 2 | 0.06598 | 0.08424 | 0.08648 | 0.08209 | 0.0183 | 1281 | 8738 |  |  |
| r5_pick | ctrl | 3 | 0.06598 | 0.08422 | 0.08658 | 0.08196 | 0.0182 | 1281 | 8738 |  |  |
| r5_aniso_water | cand | 1 | 0.06448 | 0.08329 | 0.08494 | 0.08170 | 0.0188 | 1281 | 8973 |  |  |
| r5_aniso_water | cand | 2 | 0.06448 | 0.08317 | 0.08493 | 0.08148 | 0.0187 | 1281 | 8973 | 5.00 | 1.30 |
| r5_aniso_water | cand | 3 | 0.06455 | 0.08318 | 0.08487 | 0.08156 | 0.0186 | 1281 | 8973 |  |  |
| r5_aniso_water | ctrl | 1 | 0.06604 | 0.08434 | 0.08653 | 0.08225 | 0.0183 | 1281 | 8738 | 5.00 | 1.30 |
| r5_aniso_water | ctrl | 2 | 0.06598 | 0.08424 | 0.08648 | 0.08209 | 0.0183 | 1281 | 8738 |  |  |
| r5_aniso_water | ctrl | 3 | 0.06598 | 0.08422 | 0.08658 | 0.08196 | 0.0182 | 1281 | 8738 |  |  |

## Decisions

- **r0_weights** (weights, weights cand [0.3, 0.25] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select +0.00020 not <= -2 sigma (0.00085). dselect +0.00020 (sigma 0.00085), dreport -0.00007, dfull +0.00007, dgap +0.00194; cand mean full 0.10850 / ctrl 0.10843; clashscore 3.96 / 4.02; rotamers 1.54 / 1.54
- **r1_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **ADOPTED** - all criteria met. dselect -0.01350 (sigma 0.00085), dreport -0.01280, dfull -0.01314, dgap +0.00164; cand mean full 0.09484 / ctrl 0.10798; clashscore 3.70 / 4.02; rotamers 1.54 / 1.54. {"sigma": 4.0, "n_peaks": 139, "n_sites": 121, "n_copies": 535}. Adopted model `/home/dev/runs/7KR0/experiments/e063_single/steps/r1_pick/cand_s1.pdb`
- **r1_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **ADOPTED** - all criteria met. dselect -0.00384 (sigma 0.00085), dreport -0.00255, dfull -0.00318, dgap -0.00066; cand mean full 0.09008 / ctrl 0.09326; clashscore 4.02 / 4.02; rotamers 1.18 / 1.18. {"n_water_iso": 254}. Adopted model `/home/dev/runs/7KR0/experiments/e063_single/steps/r1_aniso_water/cand_s1.pdb`
- **r2_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **ADOPTED** - all criteria met. dselect -0.00380 (sigma 0.00085), dreport -0.00466, dfull -0.00424, dgap +0.00147; cand mean full 0.08496 / ctrl 0.08920; clashscore 4.61 / 4.15; rotamers 1.18 / 1.30. {"sigma": 3.0, "n_peaks": 316, "n_sites": 235, "n_copies": 235}. Adopted model `/home/dev/runs/7KR0/experiments/e063_single/steps/r2_pick/cand_s3.pdb`
- **r2_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select -0.00162 not <= -2 sigma (0.00085). dselect -0.00162 (sigma 0.00085), dreport -0.00052, dfull -0.00106, dgap +0.00045; cand mean full 0.08321 / ctrl 0.08427; clashscore 5.00 / 5.00; rotamers 1.30 / 1.30. {"n_water_iso": 235}
- **r3_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select +0.00096 not <= -2 sigma (0.00085); report +0.00024 does not agree in sign; clashscore 5.38 > 5 and above control 5.00; gap widens +0.00357 > 0.002. dselect +0.00096 (sigma 0.00085), dreport +0.00024, dfull +0.00059, dgap +0.00357; cand mean full 0.08486 / ctrl 0.08427; clashscore 5.38 / 5.00; rotamers 1.30 / 1.30. {"sigma": 2.5, "n_peaks": 578, "n_sites": 323, "n_copies": 323}
- **r3_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select -0.00162 not <= -2 sigma (0.00085). dselect -0.00162 (sigma 0.00085), dreport -0.00052, dfull -0.00106, dgap +0.00045; cand mean full 0.08321 / ctrl 0.08427; clashscore 5.00 / 5.00; rotamers 1.30 / 1.30. {"n_water_iso": 235}
- **r4_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select -0.00094 not <= -2 sigma (0.00085); report +0.00037 does not agree in sign; clashscore 5.25 > 5 and above control 5.00; gap widens +0.00201 > 0.002. dselect -0.00094 (sigma 0.00085), dreport +0.00037, dfull -0.00027, dgap +0.00201; cand mean full 0.08400 / ctrl 0.08427; clashscore 5.25 / 5.00; rotamers 1.30 / 1.30. {"sigma": 3.0, "n_peaks": 265, "n_sites": 157, "n_copies": 157}
- **r4_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select -0.00162 not <= -2 sigma (0.00085). dselect -0.00162 (sigma 0.00085), dreport -0.00052, dfull -0.00106, dgap +0.00045; cand mean full 0.08321 / ctrl 0.08427; clashscore 5.00 / 5.00; rotamers 1.30 / 1.30. {"n_water_iso": 235}
- **r5_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select +0.00015 not <= -2 sigma (0.00085); report +0.00126 does not agree in sign. dselect +0.00015 (sigma 0.00085), dreport +0.00126, dfull +0.00071, dgap +0.00126; cand mean full 0.08498 / ctrl 0.08427; clashscore 4.87 / 5.00; rotamers 1.30 / 1.30. {"sigma": 4.0, "n_peaks": 49, "n_sites": 26, "n_copies": 26}
- **r5_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select -0.00162 not <= -2 sigma (0.00085). dselect -0.00162 (sigma 0.00085), dreport -0.00052, dfull -0.00106, dgap +0.00045; cand mean full 0.08321 / ctrl 0.08427; clashscore 5.00 / 5.00; rotamers 1.30 / 1.30. {"n_water_iso": 235}

## Rounds

| round | adopted | model in force | full | clashscore | rotamers % | ended |
|---|---|---|---|---|---|---|
| 1 | True | `/home/dev/runs/7KR0/experiments/e063_single/steps/r1_aniso_water/cand_s1.pdb` | 0.09004 | 4.02 | 1.18 | 2026-10-11T20:53:07Z |
| 2 | True | `/home/dev/runs/7KR0/experiments/e063_single/steps/r2_pick/cand_s3.pdb` | 0.08485 | 4.61 | 1.18 | 2026-10-12T00:08:53Z |
| 3 | False | `/home/dev/runs/7KR0/experiments/e063_single/steps/r2_pick/cand_s3.pdb` | 0.08485 | 4.61 | 1.18 | 2026-10-12T01:48:36Z |
| 4 | False | `/home/dev/runs/7KR0/experiments/e063_single/steps/r2_pick/cand_s3.pdb` | 0.08485 | 4.61 | 1.18 | 2026-10-12T03:28:49Z |
| 5 | False | `/home/dev/runs/7KR0/experiments/e063_single/steps/r2_pick/cand_s3.pdb` | 0.08485 | 4.61 | 1.18 | 2026-10-12T05:06:58Z |

**Stopped** 2026-10-12T05:06:58Z: 3 consecutive rounds without an adopted step. Final model `/home/dev/runs/7KR0/experiments/e063_single/steps/r2_pick/cand_s3.pdb`.

## Final (independent scorer: fmodel on all reflections, no outlier rejection, manual R)

| model | R-work | R-free | select | report | clashscore | rotamers % | atoms |
|---|---|---|---|---|---|---|---|
| final | 0.06775 | 0.08485 | 0.08744 | 0.08203 | 4.61 | 1.18 | 16755 |
| S0 | 0.09699 | 0.10955 | 0.11153 | 0.10763 | 3.83 | 2.01 | 17310 |
| baseline_median | 0.10621 | 0.11614 | 0.11807 | 0.11431 | 4.77 | 1.33 | 4300 |
| deposited | 0.11020 | 0.11826 | 0.12135 | 0.11531 |  |  | 4300 |

## Sleep-third consultations (PROTOCOL 3.8)

- 2026-10-12T07:58:59Z root: R-free sleep 0.08563 (E063 registered endpoint: the run stopped 2026-10-12T05:06:58Z at its round-2 model (one labelled water per peak; independent 0.08485 on the judging thirds, select 0.08744 / report 0.08203); one logged read of the sleep third and the vault. Taken after E063, E064 and E067 stopped at this file and after E066, the last line that started from it, adopted its own step at 07:56:02Z, so no running line can end at this file; file sha256 e2bb296b4ca9a6ee, not previously read (E059/E059b 45b42ffd, E062 e5341bf8). D605: a scorer run at 07:22Z on the harness split-v2 files mixed 1942 of this file's 2904 sleep reflections into a printed R-free; that number is not used.)
