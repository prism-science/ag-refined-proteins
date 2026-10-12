# 7KR0 - six-copy water treatment trajectory (sixcopy_waters 1.7 (2026-10-11): work-only decision maps (D582); sleep third absent from phenix input (D584); sparse-first schedule (D586); bunker set held outside every working file (D587); half-map peak agreement and water-site occupancy cap (E062); step memo (a step already judged on the same base is not re-run); floor sigma from ten r0 refinements (D594))

Rewritten 2026-10-12T05:42:30Z. Evaluator: cctbx fmodel on the frozen data and inherited flags (flags.mtz sha256 5f47d255934d), R-free on the full free set and on the select / report halves (sleep withheld: 2904). Gap = R-free(full) - R-work. Clashscore: phenix.clashscore keep_hydrogens=True. Rotamers: phenix.rotalyze. The six-copy model is a representation (PROTOCOL 18.1), never a deliverable. Bunker (D587): 3400 work reflections in vault/, absent from every working file.

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
| r1_pick | cand | 1 | 0.07757 | 0.09365 | 0.09660 | 0.09083 | 0.0161 | 1799 | 8712 |  |  |
| r1_pick | cand | 2 | 0.07788 | 0.09418 | 0.09751 | 0.09099 | 0.0163 | 1799 | 8712 | 4.09 | 1.54 |
| r1_pick | cand | 3 | 0.07807 | 0.09434 | 0.09751 | 0.09131 | 0.0163 | 1799 | 8712 |  |  |
| r1_pick | ctrl | 1 | 0.09607 | 0.10949 | 0.11200 | 0.10709 | 0.0134 | 1020 | 8712 |  |  |
| r1_pick | ctrl | 2 | 0.09605 | 0.10934 | 0.11174 | 0.10704 | 0.0133 | 1020 | 8712 | 3.83 | 1.54 |
| r1_pick | ctrl | 3 | 0.09561 | 0.10907 | 0.11137 | 0.10687 | 0.0135 | 1020 | 8712 |  |  |
| r2_pick | cand | 1 | 0.08000 | 0.09391 | 0.09684 | 0.09110 | 0.0139 | 1525 | 8712 |  |  |
| r2_pick | cand | 2 | 0.07984 | 0.09393 | 0.09694 | 0.09104 | 0.0141 | 1525 | 8712 | 3.96 | 1.54 |
| r2_pick | cand | 3 | 0.08019 | 0.09419 | 0.09729 | 0.09122 | 0.0140 | 1525 | 8712 |  |  |
| r2_pick | ctrl | 1 | 0.09607 | 0.10949 | 0.11200 | 0.10709 | 0.0134 | 1020 | 8712 |  |  |
| r2_pick | ctrl | 2 | 0.09605 | 0.10934 | 0.11174 | 0.10704 | 0.0133 | 1020 | 8712 | 3.83 | 1.54 |
| r2_pick | ctrl | 3 | 0.09561 | 0.10907 | 0.11137 | 0.10687 | 0.0135 | 1020 | 8712 |  |  |
| r2_aniso_water | cand | 1 | 0.07565 | 0.09036 | 0.09290 | 0.08794 | 0.0147 | 1139 | 8831 |  |  |
| r2_aniso_water | cand | 2 | 0.07542 | 0.09049 | 0.09323 | 0.08786 | 0.0151 | 1139 | 8831 |  |  |
| r2_aniso_water | cand | 3 | 0.07539 | 0.09052 | 0.09317 | 0.08799 | 0.0151 | 1139 | 8831 | 4.48 | 1.18 |
| r2_aniso_water | ctrl | 1 | 0.07818 | 0.09383 | 0.09656 | 0.09122 | 0.0156 | 1139 | 8601 |  |  |
| r2_aniso_water | ctrl | 2 | 0.07802 | 0.09397 | 0.09656 | 0.09149 | 0.0160 | 1139 | 8601 | 4.41 | 1.18 |
| r2_aniso_water | ctrl | 3 | 0.07818 | 0.09378 | 0.09633 | 0.09134 | 0.0156 | 1139 | 8601 |  |  |
| r3_pick | cand | 1 | 0.06901 | 0.08577 | 0.08858 | 0.08308 | 0.0168 | 1712 | 8779 |  |  |
| r3_pick | cand | 2 | 0.06901 | 0.08597 | 0.08870 | 0.08335 | 0.0170 | 1712 | 8779 |  |  |
| r3_pick | cand | 3 | 0.06905 | 0.08585 | 0.08861 | 0.08321 | 0.0168 | 1712 | 8779 | 4.87 | 1.30 |
| r3_pick | ctrl | 1 | 0.07376 | 0.08906 | 0.09140 | 0.08683 | 0.0153 | 1087 | 8779 | 4.48 | 1.30 |
| r3_pick | ctrl | 2 | 0.07361 | 0.08890 | 0.09127 | 0.08663 | 0.0153 | 1087 | 8779 |  |  |
| r3_pick | ctrl | 3 | 0.07629 | 0.09134 | 0.09394 | 0.08886 | 0.0151 | 1087 | 8779 |  |  |
| r3_aniso_water | cand | 1 | 0.06678 | 0.08434 | 0.08621 | 0.08254 | 0.0176 | 1430 | 9122 |  |  |
| r3_aniso_water | cand | 2 | 0.06685 | 0.08440 | 0.08636 | 0.08253 | 0.0176 | 1430 | 9122 | 5.00 | 1.30 |
| r3_aniso_water | cand | 3 | 0.06687 | 0.08452 | 0.08652 | 0.08260 | 0.0176 | 1430 | 9122 |  |  |
| r3_aniso_water | ctrl | 1 | 0.06764 | 0.08503 | 0.08741 | 0.08274 | 0.0174 | 1430 | 8745 |  |  |
| r3_aniso_water | ctrl | 2 | 0.06764 | 0.08509 | 0.08741 | 0.08286 | 0.0175 | 1430 | 8745 | 5.19 | 1.42 |
| r3_aniso_water | ctrl | 3 | 0.06779 | 0.08495 | 0.08721 | 0.08279 | 0.0172 | 1430 | 8745 |  |  |
| r4_pick | cand | 1 | 0.06512 | 0.08292 | 0.08434 | 0.08155 | 0.0178 | 1926 | 8745 |  |  |
| r4_pick | cand | 2 | 0.06494 | 0.08291 | 0.08427 | 0.08160 | 0.0180 | 1926 | 8745 | 5.71 | 1.42 |
| r4_pick | cand | 3 | 0.06501 | 0.08273 | 0.08426 | 0.08127 | 0.0177 | 1926 | 8745 |  |  |
| r4_pick | ctrl | 1 | 0.06764 | 0.08503 | 0.08741 | 0.08274 | 0.0174 | 1430 | 8745 |  |  |
| r4_pick | ctrl | 2 | 0.06764 | 0.08509 | 0.08741 | 0.08286 | 0.0175 | 1430 | 8745 | 5.19 | 1.42 |
| r4_pick | ctrl | 3 | 0.06779 | 0.08495 | 0.08721 | 0.08279 | 0.0172 | 1430 | 8745 |  |  |
| r4_pick_cleanup | cand | 1 | 0.06488 | 0.08348 | 0.08553 | 0.08151 | 0.0186 | 1665 | 8711 |  |  |
| r4_pick_cleanup | cand | 2 | 0.06458 | 0.08329 | 0.08532 | 0.08135 | 0.0187 | 1649 | 8709 |  |  |
| r4_pick_cleanup | cand | 3 | 0.06491 | 0.08347 | 0.08551 | 0.08152 | 0.0186 | 1657 | 8707 | 3.96 | 1.42 |
| r4_pick_cleanup | ctrl | 1 | 0.06666 | 0.08429 | 0.08671 | 0.08196 | 0.0176 | 1376 | 8729 |  |  |
| r4_pick_cleanup | ctrl | 2 | 0.06672 | 0.08415 | 0.08651 | 0.08188 | 0.0174 | 1377 | 8732 | 5.19 | 1.54 |
| r4_pick_cleanup | ctrl | 3 | 0.06667 | 0.08420 | 0.08649 | 0.08201 | 0.0175 | 1379 | 8729 |  |  |
| r4_aniso_water | cand | 1 | 0.06678 | 0.08434 | 0.08621 | 0.08254 | 0.0176 | 1430 | 9122 |  |  |
| r4_aniso_water | cand | 2 | 0.06685 | 0.08440 | 0.08636 | 0.08253 | 0.0176 | 1430 | 9122 | 5.00 | 1.30 |
| r4_aniso_water | cand | 3 | 0.06687 | 0.08452 | 0.08652 | 0.08260 | 0.0176 | 1430 | 9122 |  |  |
| r4_aniso_water | ctrl | 1 | 0.06764 | 0.08503 | 0.08741 | 0.08274 | 0.0174 | 1430 | 8745 |  |  |
| r4_aniso_water | ctrl | 2 | 0.06764 | 0.08509 | 0.08741 | 0.08286 | 0.0175 | 1430 | 8745 | 5.19 | 1.42 |
| r4_aniso_water | ctrl | 3 | 0.06779 | 0.08495 | 0.08721 | 0.08279 | 0.0172 | 1430 | 8745 |  |  |
| r5_pick | cand | 1 | 0.06512 | 0.08292 | 0.08434 | 0.08155 | 0.0178 | 1926 | 8745 |  |  |
| r5_pick | cand | 2 | 0.06494 | 0.08291 | 0.08427 | 0.08160 | 0.0180 | 1926 | 8745 | 5.71 | 1.42 |
| r5_pick | cand | 3 | 0.06501 | 0.08273 | 0.08426 | 0.08127 | 0.0177 | 1926 | 8745 |  |  |
| r5_pick | ctrl | 1 | 0.06764 | 0.08503 | 0.08741 | 0.08274 | 0.0174 | 1430 | 8745 |  |  |
| r5_pick | ctrl | 2 | 0.06764 | 0.08509 | 0.08741 | 0.08286 | 0.0175 | 1430 | 8745 | 5.19 | 1.42 |
| r5_pick | ctrl | 3 | 0.06779 | 0.08495 | 0.08721 | 0.08279 | 0.0172 | 1430 | 8745 |  |  |
| r5_pick_cleanup | cand | 1 | 0.06488 | 0.08348 | 0.08553 | 0.08151 | 0.0186 | 1665 | 8711 |  |  |
| r5_pick_cleanup | cand | 2 | 0.06458 | 0.08329 | 0.08532 | 0.08135 | 0.0187 | 1649 | 8709 |  |  |
| r5_pick_cleanup | cand | 3 | 0.06491 | 0.08347 | 0.08551 | 0.08152 | 0.0186 | 1657 | 8707 | 3.96 | 1.42 |
| r5_pick_cleanup | ctrl | 1 | 0.06666 | 0.08429 | 0.08671 | 0.08196 | 0.0176 | 1376 | 8729 |  |  |
| r5_pick_cleanup | ctrl | 2 | 0.06672 | 0.08415 | 0.08651 | 0.08188 | 0.0174 | 1377 | 8732 | 5.19 | 1.54 |
| r5_pick_cleanup | ctrl | 3 | 0.06667 | 0.08420 | 0.08649 | 0.08201 | 0.0175 | 1379 | 8729 |  |  |
| r5_aniso_water | cand | 1 | 0.06678 | 0.08434 | 0.08621 | 0.08254 | 0.0176 | 1430 | 9122 |  |  |
| r5_aniso_water | cand | 2 | 0.06685 | 0.08440 | 0.08636 | 0.08253 | 0.0176 | 1430 | 9122 | 5.00 | 1.30 |
| r5_aniso_water | cand | 3 | 0.06687 | 0.08452 | 0.08652 | 0.08260 | 0.0176 | 1430 | 9122 |  |  |
| r5_aniso_water | ctrl | 1 | 0.06764 | 0.08503 | 0.08741 | 0.08274 | 0.0174 | 1430 | 8745 |  |  |
| r5_aniso_water | ctrl | 2 | 0.06764 | 0.08509 | 0.08741 | 0.08286 | 0.0175 | 1430 | 8745 | 5.19 | 1.42 |
| r5_aniso_water | ctrl | 3 | 0.06779 | 0.08495 | 0.08721 | 0.08279 | 0.0172 | 1430 | 8745 |  |  |
| r6_pick | cand | 1 | 0.06512 | 0.08292 | 0.08434 | 0.08155 | 0.0178 | 1926 | 8745 |  |  |
| r6_pick | cand | 2 | 0.06494 | 0.08291 | 0.08427 | 0.08160 | 0.0180 | 1926 | 8745 | 5.71 | 1.42 |
| r6_pick | cand | 3 | 0.06501 | 0.08273 | 0.08426 | 0.08127 | 0.0177 | 1926 | 8745 |  |  |
| r6_pick | ctrl | 1 | 0.06764 | 0.08503 | 0.08741 | 0.08274 | 0.0174 | 1430 | 8745 |  |  |
| r6_pick | ctrl | 2 | 0.06764 | 0.08509 | 0.08741 | 0.08286 | 0.0175 | 1430 | 8745 | 5.19 | 1.42 |
| r6_pick | ctrl | 3 | 0.06779 | 0.08495 | 0.08721 | 0.08279 | 0.0172 | 1430 | 8745 |  |  |
| r6_pick_cleanup | cand | 1 | 0.06488 | 0.08348 | 0.08553 | 0.08151 | 0.0186 | 1665 | 8711 |  |  |
| r6_pick_cleanup | cand | 2 | 0.06458 | 0.08329 | 0.08532 | 0.08135 | 0.0187 | 1649 | 8709 |  |  |
| r6_pick_cleanup | cand | 3 | 0.06491 | 0.08347 | 0.08551 | 0.08152 | 0.0186 | 1657 | 8707 | 3.96 | 1.42 |
| r6_pick_cleanup | ctrl | 1 | 0.06666 | 0.08429 | 0.08671 | 0.08196 | 0.0176 | 1376 | 8729 |  |  |
| r6_pick_cleanup | ctrl | 2 | 0.06672 | 0.08415 | 0.08651 | 0.08188 | 0.0174 | 1377 | 8732 | 5.19 | 1.54 |
| r6_pick_cleanup | ctrl | 3 | 0.06667 | 0.08420 | 0.08649 | 0.08201 | 0.0175 | 1379 | 8729 |  |  |
| r6_aniso_water | cand | 1 | 0.06678 | 0.08434 | 0.08621 | 0.08254 | 0.0176 | 1430 | 9122 |  |  |
| r6_aniso_water | cand | 2 | 0.06685 | 0.08440 | 0.08636 | 0.08253 | 0.0176 | 1430 | 9122 | 5.00 | 1.30 |
| r6_aniso_water | cand | 3 | 0.06687 | 0.08452 | 0.08652 | 0.08260 | 0.0176 | 1430 | 9122 |  |  |
| r6_aniso_water | ctrl | 1 | 0.06764 | 0.08503 | 0.08741 | 0.08274 | 0.0174 | 1430 | 8745 |  |  |
| r6_aniso_water | ctrl | 2 | 0.06764 | 0.08509 | 0.08741 | 0.08286 | 0.0175 | 1430 | 8745 | 5.19 | 1.42 |
| r6_aniso_water | ctrl | 3 | 0.06779 | 0.08495 | 0.08721 | 0.08279 | 0.0172 | 1430 | 8745 |  |  |

## Decisions

- **r0_weights** (weights, weights cand [0.3, 0.25] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select +0.00020 not <= -2 sigma (0.00085). dselect +0.00020 (sigma 0.00085), dreport -0.00007, dfull +0.00007, dgap +0.00194; cand mean full 0.10850 / ctrl 0.10843; clashscore 3.96 / 4.02; rotamers 1.54 / 1.54
- **r1_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - gap widens +0.00283 > 0.002. dselect -0.01449 (sigma 0.00085), dreport -0.01595, dfull -0.01524, dgap +0.00283; cand mean full 0.09406 / ctrl 0.10930; clashscore 4.09 / 3.83; rotamers 1.54 / 1.54. {"sigma": 3.0, "n_peaks": 243, "n_sites": 199, "n_copies": 779}
- **r1_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - every water already anisotropic. {"n_water_iso": 0}
- **r2_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **ADOPTED** - all criteria met. dselect -0.01468 (sigma 0.00085), dreport -0.01588, dfull -0.01529, dgap +0.00061; cand mean full 0.09401 / ctrl 0.10930; clashscore 3.96 / 3.83; rotamers 1.54 / 1.54. {"sigma": 4.0, "n_peaks": 140, "n_sites": 126, "n_copies": 505}. Adopted model `/home/dev/runs/7KR0/experiments/e062_halfmap/steps/r2_pick/cand_s2.pdb`
- **r2_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **ADOPTED** - all criteria met. dselect -0.00338 (sigma 0.00085), dreport -0.00342, dfull -0.00340, dgap -0.00076; cand mean full 0.09046 / ctrl 0.09386; clashscore 4.48 / 4.41; rotamers 1.18 / 1.18. {"n_water_iso": 230}. Adopted model `/home/dev/runs/7KR0/experiments/e062_halfmap/steps/r2_aniso_water/cand_s3.pdb`
- **r3_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **ADOPTED** - all criteria met. dselect -0.00357 (sigma 0.00106), dreport -0.00423, dfull -0.00391, dgap +0.00162; cand mean full 0.08586 / ctrl 0.08977; clashscore 4.87 / 4.48; rotamers 1.30 / 1.30. {"sigma": 3.0, "n_peaks": 238, "n_sites": 185, "n_copies": 625}. Adopted model `/home/dev/runs/7KR0/experiments/e062_halfmap/steps/r3_pick/cand_s3.pdb`
- **r3_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select -0.00098 not <= -2 sigma (0.00085). dselect -0.00098 (sigma 0.00085), dreport -0.00024, dfull -0.00060, dgap +0.00025; cand mean full 0.08442 / ctrl 0.08502; clashscore 5.00 / 5.19; rotamers 1.30 / 1.42. {"n_water_iso": 377}
- **r4_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - clashscore 5.71 > 5 and above control 5.19. dselect -0.00305 (sigma 0.00085), dreport -0.00132, dfull -0.00217, dgap +0.00050; cand mean full 0.08285 / ctrl 0.08502; clashscore 5.71 / 5.19; rotamers 1.42 / 1.42. {"sigma": 2.5, "n_peaks": 278, "n_sites": 165, "n_copies": 496}
- **r4_pick_cleanup** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select -0.00112 not <= -2 sigma (0.00085). dselect -0.00112 (sigma 0.00085), dreport -0.00049, dfull -0.00080, dgap +0.00109; cand mean full 0.08341 / ctrl 0.08421; clashscore 3.96 / 5.19; rotamers 1.42 / 1.54. {"sigma": 2.5}
- **r4_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select -0.00098 not <= -2 sigma (0.00085). dselect -0.00098 (sigma 0.00085), dreport -0.00024, dfull -0.00060, dgap +0.00025; cand mean full 0.08442 / ctrl 0.08502; clashscore 5.00 / 5.19; rotamers 1.30 / 1.42. {"n_water_iso": 377}
- **r5_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - clashscore 5.71 > 5 and above control 5.19. dselect -0.00305 (sigma 0.00085), dreport -0.00132, dfull -0.00217, dgap +0.00050; cand mean full 0.08285 / ctrl 0.08502; clashscore 5.71 / 5.19; rotamers 1.42 / 1.42. {"sigma": 2.5, "n_peaks": 278, "n_sites": 165, "n_copies": 496}
- **r5_pick_cleanup** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select -0.00112 not <= -2 sigma (0.00085). dselect -0.00112 (sigma 0.00085), dreport -0.00049, dfull -0.00080, dgap +0.00109; cand mean full 0.08341 / ctrl 0.08421; clashscore 3.96 / 5.19; rotamers 1.42 / 1.54. {"sigma": 2.5}
- **r5_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select -0.00098 not <= -2 sigma (0.00085). dselect -0.00098 (sigma 0.00085), dreport -0.00024, dfull -0.00060, dgap +0.00025; cand mean full 0.08442 / ctrl 0.08502; clashscore 5.00 / 5.19; rotamers 1.30 / 1.42. {"n_water_iso": 377}
- **r6_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - clashscore 5.71 > 5 and above control 5.19. dselect -0.00305 (sigma 0.00085), dreport -0.00132, dfull -0.00217, dgap +0.00050; cand mean full 0.08285 / ctrl 0.08502; clashscore 5.71 / 5.19; rotamers 1.42 / 1.42. {"sigma": 2.5, "n_peaks": 278, "n_sites": 165, "n_copies": 496}
- **r6_pick_cleanup** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select -0.00112 not <= -2 sigma (0.00085). dselect -0.00112 (sigma 0.00085), dreport -0.00049, dfull -0.00080, dgap +0.00109; cand mean full 0.08341 / ctrl 0.08421; clashscore 3.96 / 5.19; rotamers 1.42 / 1.54. {"sigma": 2.5}
- **r6_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select -0.00098 not <= -2 sigma (0.00085). dselect -0.00098 (sigma 0.00085), dreport -0.00024, dfull -0.00060, dgap +0.00025; cand mean full 0.08442 / ctrl 0.08502; clashscore 5.00 / 5.19; rotamers 1.30 / 1.42. {"n_water_iso": 377}

## Rounds

| round | adopted | model in force | full | clashscore | rotamers % | ended |
|---|---|---|---|---|---|---|
| 1 | False | `/home/dev/runs/7KR0/experiments/e062_halfmap/build/S0.pdb` | 0.10955 | 3.83 | 2.01 | 2026-10-11T19:37:07Z |
| 2 | True | `/home/dev/runs/7KR0/experiments/e062_halfmap/steps/r2_aniso_water/cand_s3.pdb` | 0.09052 | 4.48 | 1.18 | 2026-10-11T22:53:59Z |
| 3 | True | `/home/dev/runs/7KR0/experiments/e062_halfmap/steps/r3_pick/cand_s3.pdb` | 0.08585 | 4.87 | 1.30 | 2026-10-12T02:14:15Z |
| 4 | False | `/home/dev/runs/7KR0/experiments/e062_halfmap/steps/r3_pick/cand_s3.pdb` | 0.08585 | 4.87 | 1.30 | 2026-10-12T05:31:37Z |
| 5 | False | `/home/dev/runs/7KR0/experiments/e062_halfmap/steps/r3_pick/cand_s3.pdb` | 0.08585 | 4.87 | 1.30 | 2026-10-12T05:36:19Z |
| 6 | False | `/home/dev/runs/7KR0/experiments/e062_halfmap/steps/r3_pick/cand_s3.pdb` | 0.08585 | 4.87 | 1.30 | 2026-10-12T05:41:03Z |

**Stopped** 2026-10-12T05:41:03Z: 3 consecutive rounds without an adopted step. Final model `/home/dev/runs/7KR0/experiments/e062_halfmap/steps/r3_pick/cand_s3.pdb`.

## Final (independent scorer: fmodel on all reflections, no outlier rejection, manual R)

| model | R-work | R-free | select | report | clashscore | rotamers % | atoms |
|---|---|---|---|---|---|---|---|
| final | 0.06905 | 0.08585 | 0.08822 | 0.08297 | 4.87 | 1.30 | 17126 |
| S0 | 0.09699 | 0.10955 | 0.11153 | 0.10763 | 3.83 | 2.01 | 17310 |
| baseline_median | 0.10621 | 0.11614 | 0.11807 | 0.11431 | 4.77 | 1.33 | 4300 |
| deposited | 0.11020 | 0.11826 | 0.12135 | 0.11531 |  |  | 4300 |

## Sleep-third consultations (PROTOCOL 3.8)

- 2026-10-12T05:42:24Z root: R-free sleep 0.08373 (E062 registered endpoint: the run stopped 2026-10-12T05:41:03Z at its round-3 model (copies mode with the site-occupancy cap and the half-map thinning; independent 0.08585 on the judging thirds) after the 2.5sigma composite pick+cleanup was refused at z -1.3 and the memo chain closed rounds 5 and 6; one logged read of the sleep third and the vault; no other line works from this file)
