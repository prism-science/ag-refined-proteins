# 7KR0 - six-copy water treatment trajectory (sixcopy_waters 1.0 (E049, 2026-10-09))

Rewritten 2026-10-10T08:47:27Z. Evaluator: cctbx fmodel on the frozen data and inherited flags (flags.mtz sha256 31939295cafa), R-free on the full free set and on the select / report halves (sleep withheld: 0). Gap = R-free(full) - R-work. Clashscore: phenix.clashscore keep_hydrogens=True. Rotamers: phenix.rotalyze. The six-copy model is a representation (PROTOCOL 18.1), never a deliverable.

## Baseline (single model, standing recipe, 5 macro-cycles, N = 3)

| model | R-work | full | select | report | gap | clashscore | rotamers % |
|---|---|---|---|---|---|---|---|
| deposited, our flags | 0.11030 | 0.11752 | 0.11592 | 0.11914 | 0.0072 | | |
| re-refined mean | 0.10816 | 0.11633 | 0.11459 | 0.11809 | 0.0082 | 4.77 | 1.33 |
| re-refined sigma | | 0.00014 | 0.00027 | 0.00003 | 0.00020 | | |

## Build

| model | R-work | full | select | report | gap | water atoms | ANISOU | clashscore | rotamers % |
|---|---|---|---|---|---|---|---|---|---|
| deposited (our flags) | 0.11030 | 0.11752 | 0.11592 | 0.11914 | 0.0072 | 316 | 2310 |  |  |
| six copies unrefined | 0.17328 | 0.17608 | 0.17375 | 0.17843 | 0.0028 | 1896 | 9588 | 225.57 | 5.79 |
| S0 six copies, 20 mc | 0.09726 | 0.10798 | 0.10586 | 0.11013 | 0.0107 | 1896 | 9588 | 4.41 | 2.01 |

## Steps (every seed of both arms; weights = (wc, wu); floor sigma {"r_free_select": 6e-05, "r_free_report": 0.000174, "r_free_full": 7.2e-05, "n": 6, "provisional": true})

| step | arm | seed | R-work | full | select | report | gap | water atoms | ANISOU | clashscore | rotamers % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| r0_weights | cand | 1 | 0.09400 | 0.10879 | 0.10755 | 0.11004 | 0.0148 | 1076 | 8768 |  |  |
| r0_weights | cand | 2 | 0.09394 | 0.10875 | 0.10741 | 0.11011 | 0.0148 | 1076 | 8768 |  |  |
| r0_weights | cand | 3 | 0.09406 | 0.10885 | 0.10746 | 0.11025 | 0.0148 | 1076 | 8768 | 4.02 | 1.42 |
| r0_weights | ctrl | 1 | 0.09701 | 0.10935 | 0.10779 | 0.11094 | 0.0123 | 1076 | 8768 |  |  |
| r0_weights | ctrl | 2 | 0.09699 | 0.10930 | 0.10784 | 0.11078 | 0.0123 | 1076 | 8768 | 3.70 | 1.54 |
| r0_weights | ctrl | 3 | 0.09701 | 0.10918 | 0.10788 | 0.11050 | 0.0122 | 1076 | 8768 |  |  |
| r1_pick | cand | 1 | 0.07563 | 0.08943 | 0.08943 | 0.08944 | 0.0138 | 1980 | 8768 |  |  |
| r1_pick | cand | 2 | 0.07574 | 0.08946 | 0.08953 | 0.08939 | 0.0137 | 1980 | 8768 | 4.22 | 1.54 |
| r1_pick | cand | 3 | 0.07609 | 0.09003 | 0.09008 | 0.08998 | 0.0139 | 1980 | 8768 |  |  |
| r1_pick | ctrl | 1 | 0.09701 | 0.10935 | 0.10779 | 0.11094 | 0.0123 | 1076 | 8768 |  |  |
| r1_pick | ctrl | 2 | 0.09699 | 0.10930 | 0.10784 | 0.11078 | 0.0123 | 1076 | 8768 | 3.70 | 1.54 |
| r1_pick | ctrl | 3 | 0.09701 | 0.10918 | 0.10788 | 0.11050 | 0.0122 | 1076 | 8768 |  |  |
| r1_aniso_water | cand | 1 | 0.07066 | 0.08580 | 0.08575 | 0.08584 | 0.0151 | 1401 | 9093 |  |  |
| r1_aniso_water | cand | 2 | 0.07033 | 0.08571 | 0.08562 | 0.08581 | 0.0154 | 1401 | 9093 | 4.67 | 1.30 |
| r1_aniso_water | cand | 3 | 0.07059 | 0.08566 | 0.08535 | 0.08598 | 0.0151 | 1401 | 9093 |  |  |
| r1_aniso_water | ctrl | 1 | 0.07340 | 0.08869 | 0.08914 | 0.08823 | 0.0153 | 1401 | 8623 |  |  |
| r1_aniso_water | ctrl | 2 | 0.07368 | 0.08878 | 0.08927 | 0.08829 | 0.0151 | 1401 | 8623 |  |  |
| r1_aniso_water | ctrl | 3 | 0.07336 | 0.08865 | 0.08914 | 0.08815 | 0.0153 | 1401 | 8623 | 4.74 | 1.18 |
| r2_pick | cand | 1 | 0.06359 | 0.07980 | 0.07769 | 0.08193 | 0.0162 | 2256 | 8970 |  |  |
| r2_pick | cand | 2 | 0.06340 | 0.07968 | 0.07749 | 0.08190 | 0.0163 | 2256 | 8970 |  |  |
| r2_pick | cand | 3 | 0.06344 | 0.07969 | 0.07766 | 0.08175 | 0.0163 | 2256 | 8970 | 5.58 | 1.30 |
| r2_pick | ctrl | 1 | 0.06893 | 0.08513 | 0.08536 | 0.08489 | 0.0162 | 1278 | 8970 |  |  |
| r2_pick | ctrl | 2 | 0.06873 | 0.08510 | 0.08533 | 0.08488 | 0.0164 | 1278 | 8970 | 4.61 | 1.30 |
| r2_pick | ctrl | 3 | 0.06890 | 0.08505 | 0.08518 | 0.08492 | 0.0162 | 1278 | 8970 |  |  |
| r2_pick_cleanup | cand | 1 | 0.06258 | 0.07971 | 0.07784 | 0.08160 | 0.0171 | 1887 | 8902 | 4.28 | 1.30 |
| r2_pick_cleanup | cand | 2 | 0.06259 | 0.07979 | 0.07772 | 0.08189 | 0.0172 | 1886 | 8905 |  |  |
| r2_pick_cleanup | cand | 3 | 0.06271 | 0.07984 | 0.07792 | 0.08177 | 0.0171 | 1886 | 8907 |  |  |
| r2_pick_cleanup | ctrl | 1 | 0.06770 | 0.08442 | 0.08503 | 0.08379 | 0.0167 | 1230 | 8922 |  |  |
| r2_pick_cleanup | ctrl | 2 | 0.06769 | 0.08459 | 0.08529 | 0.08388 | 0.0169 | 1233 | 8925 |  |  |
| r2_pick_cleanup | ctrl | 3 | 0.06764 | 0.08465 | 0.08528 | 0.08400 | 0.0170 | 1230 | 8922 | 5.06 | 1.30 |
| r2_aniso_water | cand | 1 | 0.06060 | 0.07898 | 0.07674 | 0.08125 | 0.0184 | 1797 | 9489 | 4.48 | 1.30 |
| r2_aniso_water | cand | 2 | 0.06049 | 0.07903 | 0.07682 | 0.08126 | 0.0185 | 1797 | 9489 |  |  |
| r2_aniso_water | cand | 3 | 0.06062 | 0.07895 | 0.07662 | 0.08130 | 0.0183 | 1797 | 9489 |  |  |
| r2_aniso_water | ctrl | 1 | 0.06183 | 0.07987 | 0.07763 | 0.08214 | 0.0180 | 1797 | 8872 | 4.41 | 1.30 |
| r2_aniso_water | ctrl | 2 | 0.06175 | 0.07993 | 0.07779 | 0.08209 | 0.0182 | 1797 | 8872 |  |  |
| r2_aniso_water | ctrl | 3 | 0.06145 | 0.07965 | 0.07741 | 0.08191 | 0.0182 | 1797 | 8872 |  |  |
| r3_pick | cand | 1 | 0.05833 | 0.07556 | 0.07297 | 0.07818 | 0.0172 | 2198 | 9384 | 5.19 | 1.30 |
| r3_pick | cand | 2 | 0.05821 | 0.07551 | 0.07301 | 0.07803 | 0.0173 | 2198 | 9384 |  |  |
| r3_pick | cand | 3 | 0.05828 | 0.07538 | 0.07282 | 0.07797 | 0.0171 | 2198 | 9384 |  |  |
| r3_pick | ctrl | 1 | 0.05969 | 0.07897 | 0.07668 | 0.08129 | 0.0193 | 1692 | 9384 |  |  |
| r3_pick | ctrl | 2 | 0.05974 | 0.07915 | 0.07687 | 0.08147 | 0.0194 | 1692 | 9384 | 4.54 | 1.30 |
| r3_pick | ctrl | 3 | 0.05981 | 0.07918 | 0.07689 | 0.08150 | 0.0194 | 1692 | 9384 |  |  |
| r3_pick_cleanup | cand | 1 | 0.05761 | 0.07572 | 0.07316 | 0.07831 | 0.0181 | 2017 | 9333 |  |  |
| r3_pick_cleanup | cand | 2 | 0.05760 | 0.07572 | 0.07326 | 0.07821 | 0.0181 | 2011 | 9338 | 4.61 | 1.18 |
| r3_pick_cleanup | cand | 3 | 0.05775 | 0.07581 | 0.07336 | 0.07830 | 0.0181 | 2001 | 9331 |  |  |
| r3_pick_cleanup | ctrl | 1 | 0.05900 | 0.07928 | 0.07681 | 0.08178 | 0.0203 | 1652 | 9344 |  |  |
| r3_pick_cleanup | ctrl | 2 | 0.05928 | 0.07946 | 0.07690 | 0.08205 | 0.0202 | 1645 | 9337 | 4.67 | 1.18 |
| r3_pick_cleanup | ctrl | 3 | 0.05919 | 0.07939 | 0.07691 | 0.08190 | 0.0202 | 1654 | 9346 |  |  |
| r3_aniso_water | cand | 1 | 0.05676 | 0.07586 | 0.07364 | 0.07811 | 0.0191 | 1947 | 9639 | 4.41 | 1.18 |
| r3_aniso_water | cand | 2 | 0.05673 | 0.07578 | 0.07359 | 0.07801 | 0.0191 | 1947 | 9639 |  |  |
| r3_aniso_water | cand | 3 | 0.05667 | 0.07591 | 0.07370 | 0.07814 | 0.0192 | 1947 | 9639 |  |  |
| r3_aniso_water | ctrl | 1 | 0.05682 | 0.07597 | 0.07369 | 0.07827 | 0.0191 | 1947 | 9309 | 4.35 | 1.18 |
| r3_aniso_water | ctrl | 2 | 0.05707 | 0.07608 | 0.07380 | 0.07838 | 0.0190 | 1947 | 9309 |  |  |
| r3_aniso_water | ctrl | 3 | 0.05704 | 0.07594 | 0.07367 | 0.07825 | 0.0189 | 1947 | 9309 |  |  |
| r4_pick | cand | 1 | 0.05663 | 0.07499 | 0.07300 | 0.07701 | 0.0184 | 2203 | 9309 |  |  |
| r4_pick | cand | 2 | 0.05660 | 0.07498 | 0.07297 | 0.07702 | 0.0184 | 2203 | 9309 | 4.87 | 1.18 |
| r4_pick | cand | 3 | 0.05658 | 0.07499 | 0.07296 | 0.07705 | 0.0184 | 2203 | 9309 |  |  |
| r4_pick | ctrl | 1 | 0.05682 | 0.07597 | 0.07369 | 0.07827 | 0.0191 | 1947 | 9309 | 4.35 | 1.18 |
| r4_pick | ctrl | 2 | 0.05707 | 0.07608 | 0.07380 | 0.07838 | 0.0190 | 1947 | 9309 |  |  |
| r4_pick | ctrl | 3 | 0.05704 | 0.07594 | 0.07367 | 0.07825 | 0.0189 | 1947 | 9309 |  |  |
| r4_aniso_water | cand | 1 | 0.05582 | 0.07525 | 0.07324 | 0.07729 | 0.0194 | 2112 | 9804 | 5.00 | 1.18 |
| r4_aniso_water | cand | 2 | 0.05566 | 0.07511 | 0.07313 | 0.07710 | 0.0194 | 2112 | 9804 |  |  |
| r4_aniso_water | cand | 3 | 0.05595 | 0.07527 | 0.07327 | 0.07728 | 0.0193 | 2112 | 9804 |  |  |
| r4_aniso_water | ctrl | 1 | 0.05616 | 0.07549 | 0.07339 | 0.07761 | 0.0193 | 2112 | 9287 |  |  |
| r4_aniso_water | ctrl | 2 | 0.05612 | 0.07537 | 0.07325 | 0.07752 | 0.0193 | 2112 | 9287 | 5.06 | 1.18 |
| r4_aniso_water | ctrl | 3 | 0.05600 | 0.07536 | 0.07323 | 0.07751 | 0.0194 | 2112 | 9287 |  |  |
| r5_pick | cand | 1 | 0.05586 | 0.07448 | 0.07291 | 0.07607 | 0.0186 | 2287 | 9287 |  |  |
| r5_pick | cand | 2 | 0.05569 | 0.07453 | 0.07300 | 0.07608 | 0.0188 | 2287 | 9287 |  |  |
| r5_pick | cand | 3 | 0.05585 | 0.07455 | 0.07299 | 0.07612 | 0.0187 | 2287 | 9287 | 5.06 | 1.18 |
| r5_pick | ctrl | 1 | 0.05616 | 0.07549 | 0.07339 | 0.07761 | 0.0193 | 2112 | 9287 |  |  |
| r5_pick | ctrl | 2 | 0.05612 | 0.07537 | 0.07325 | 0.07752 | 0.0193 | 2112 | 9287 | 5.06 | 1.18 |
| r5_pick | ctrl | 3 | 0.05600 | 0.07536 | 0.07323 | 0.07751 | 0.0194 | 2112 | 9287 |  |  |
| r5_aniso_water | cand | 1 | 0.05515 | 0.07456 | 0.07320 | 0.07593 | 0.0194 | 2197 | 9889 |  |  |
| r5_aniso_water | cand | 2 | 0.05513 | 0.07444 | 0.07308 | 0.07582 | 0.0193 | 2197 | 9889 |  |  |
| r5_aniso_water | cand | 3 | 0.05504 | 0.07447 | 0.07318 | 0.07578 | 0.0194 | 2197 | 9889 | 5.25 | 1.18 |
| r5_aniso_water | ctrl | 1 | 0.05546 | 0.07466 | 0.07310 | 0.07625 | 0.0192 | 2197 | 9262 | 5.25 | 1.18 |
| r5_aniso_water | ctrl | 2 | 0.05541 | 0.07480 | 0.07331 | 0.07630 | 0.0194 | 2197 | 9262 |  |  |
| r5_aniso_water | ctrl | 3 | 0.05523 | 0.07469 | 0.07308 | 0.07633 | 0.0195 | 2197 | 9262 |  |  |
| r5_cleanup | cand | 1 | 0.05567 | 0.07494 | 0.07355 | 0.07634 | 0.0193 | 2184 | 9254 | 4.41 | 1.18 |
| r5_cleanup | cand | 2 | 0.05557 | 0.07489 | 0.07352 | 0.07627 | 0.0193 | 2184 | 9254 |  |  |
| r5_cleanup | cand | 3 | 0.05575 | 0.07492 | 0.07365 | 0.07620 | 0.0192 | 2184 | 9254 |  |  |
| r5_cleanup | ctrl | 1 | 0.05546 | 0.07466 | 0.07310 | 0.07625 | 0.0192 | 2197 | 9262 | 5.25 | 1.18 |
| r5_cleanup | ctrl | 2 | 0.05541 | 0.07480 | 0.07331 | 0.07630 | 0.0194 | 2197 | 9262 |  |  |
| r5_cleanup | ctrl | 3 | 0.05523 | 0.07469 | 0.07308 | 0.07633 | 0.0195 | 2197 | 9262 |  |  |
| r6_pick | cand | 1 | 0.05538 | 0.07430 | 0.07277 | 0.07585 | 0.0189 | 2318 | 9262 |  |  |
| r6_pick | cand | 2 | 0.05534 | 0.07425 | 0.07275 | 0.07577 | 0.0189 | 2318 | 9262 | 5.38 | 1.18 |
| r6_pick | cand | 3 | 0.05539 | 0.07425 | 0.07271 | 0.07582 | 0.0189 | 2318 | 9262 |  |  |
| r6_pick | ctrl | 1 | 0.05546 | 0.07466 | 0.07310 | 0.07625 | 0.0192 | 2197 | 9262 | 5.25 | 1.18 |
| r6_pick | ctrl | 2 | 0.05541 | 0.07480 | 0.07331 | 0.07630 | 0.0194 | 2197 | 9262 |  |  |
| r6_pick | ctrl | 3 | 0.05523 | 0.07469 | 0.07308 | 0.07633 | 0.0195 | 2197 | 9262 |  |  |
| r6_pick_cleanup | cand | 1 | 0.05547 | 0.07463 | 0.07324 | 0.07603 | 0.0192 | 2229 | 9236 | 4.67 | 1.42 |
| r6_pick_cleanup | cand | 2 | 0.05545 | 0.07454 | 0.07325 | 0.07583 | 0.0191 | 2232 | 9233 |  |  |
| r6_pick_cleanup | cand | 3 | 0.05540 | 0.07442 | 0.07302 | 0.07583 | 0.0190 | 2232 | 9233 |  |  |
| r6_pick_cleanup | ctrl | 1 | 0.05528 | 0.07479 | 0.07321 | 0.07638 | 0.0195 | 2160 | 9248 |  |  |
| r6_pick_cleanup | ctrl | 2 | 0.05506 | 0.07481 | 0.07318 | 0.07646 | 0.0198 | 2156 | 9246 | 5.38 | 1.18 |
| r6_pick_cleanup | ctrl | 3 | 0.05518 | 0.07480 | 0.07311 | 0.07651 | 0.0196 | 2158 | 9247 |  |  |
| r6_aniso_water | cand | 1 | 0.05515 | 0.07456 | 0.07320 | 0.07593 | 0.0194 | 2197 | 9889 |  |  |
| r6_aniso_water | cand | 2 | 0.05513 | 0.07444 | 0.07308 | 0.07582 | 0.0193 | 2197 | 9889 |  |  |
| r6_aniso_water | cand | 3 | 0.05504 | 0.07447 | 0.07318 | 0.07578 | 0.0194 | 2197 | 9889 | 5.25 | 1.18 |
| r6_aniso_water | ctrl | 1 | 0.05546 | 0.07466 | 0.07310 | 0.07625 | 0.0192 | 2197 | 9262 | 5.25 | 1.18 |
| r6_aniso_water | ctrl | 2 | 0.05541 | 0.07480 | 0.07331 | 0.07630 | 0.0194 | 2197 | 9262 |  |  |
| r6_aniso_water | ctrl | 3 | 0.05523 | 0.07469 | 0.07308 | 0.07633 | 0.0195 | 2197 | 9262 |  |  |

## Decisions

- **r0_weights** (weights, weights cand [0.3, 0.25] / ctrl [0.5, 1.0], 10 mc): **not adopted** - gap widens +0.00252 > 0.002. dselect -0.00036 (sigma 0.00006), dreport -0.00060, dfull -0.00048, dgap +0.00252; cand mean full 0.10880 / ctrl 0.10928; clashscore 4.02 / 3.70; rotamers 1.42 / 1.54
- **r1_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **ADOPTED** - all criteria met. dselect -0.01816 (sigma 0.00025), dreport -0.02113, dfull -0.01964, dgap +0.00155; cand mean full 0.08964 / ctrl 0.10928; clashscore 4.22 / 3.70; rotamers 1.54 / 1.54. {"sigma": 3.0, "n_peaks": 296, "n_sites": 224, "n_copies": 904}. Adopted model `/home/dev/runs/7KR0/experiments/e049_portable/steps/r1_pick/cand_s2.pdb`
- **r1_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **ADOPTED** - all criteria met. dselect -0.00361 (sigma 0.00015), dreport -0.00235, dfull -0.00298, dgap -0.00003; cand mean full 0.08572 / ctrl 0.08871; clashscore 4.67 / 4.74; rotamers 1.30 / 1.18. {"n_water_iso": 470}. Adopted model `/home/dev/runs/7KR0/experiments/e049_portable/steps/r1_aniso_water/cand_s2.pdb`
- **r2_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - clashscore 5.58 > 5 and above control 4.61. dselect -0.00768 (sigma 0.00010), dreport -0.00304, dfull -0.00537, dgap +0.00001; cand mean full 0.07973 / ctrl 0.08509; clashscore 5.58 / 4.61; rotamers 1.30 / 1.30. {"sigma": 2.5, "n_peaks": 526, "n_sites": 291, "n_copies": 978}
- **r2_pick_cleanup** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **ADOPTED** - all criteria met. dselect -0.00738 (sigma 0.00013), dreport -0.00214, dfull -0.00477, dgap +0.00028; cand mean full 0.07978 / ctrl 0.08455; clashscore 4.28 / 5.06; rotamers 1.30 / 1.30. Adopted model `/home/dev/runs/7KR0/experiments/e049_portable/steps/r2_pick_cleanup/cand_s1.pdb`
- **r2_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **ADOPTED** - all criteria met. dselect -0.00088 (sigma 0.00015), dreport -0.00078, dfull -0.00083, dgap +0.00028; cand mean full 0.07899 / ctrl 0.07982; clashscore 4.48 / 4.41; rotamers 1.30 / 1.30. {"n_water_iso": 617}. Adopted model `/home/dev/runs/7KR0/experiments/e049_portable/steps/r2_aniso_water/cand_s1.pdb`
- **r3_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - clashscore 5.19 > 5 and above control 4.54. dselect -0.00388 (sigma 0.00011), dreport -0.00336, dfull -0.00362, dgap -0.00215; cand mean full 0.07548 / ctrl 0.07910; clashscore 5.19 / 4.54; rotamers 1.30 / 1.30. {"sigma": 2.5, "n_peaks": 411, "n_sites": 169, "n_copies": 506}
- **r3_pick_cleanup** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **ADOPTED** - all criteria met. dselect -0.00362 (sigma 0.00008), dreport -0.00364, dfull -0.00363, dgap -0.00212; cand mean full 0.07575 / ctrl 0.07938; clashscore 4.61 / 4.67; rotamers 1.18 / 1.18. Adopted model `/home/dev/runs/7KR0/experiments/e049_portable/steps/r3_pick_cleanup/cand_s2.pdb`
- **r3_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select -0.00008 not <= -2 sigma (0.00006). dselect -0.00008 (sigma 0.00006), dreport -0.00021, dfull -0.00014, dgap +0.00011; cand mean full 0.07585 / ctrl 0.07600; clashscore 4.41 / 4.35; rotamers 1.18 / 1.18. {"n_water_iso": 330}
- **r4_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **ADOPTED** - all criteria met. dselect -0.00074 (sigma 0.00006), dreport -0.00128, dfull -0.00101, dgap -0.00063; cand mean full 0.07499 / ctrl 0.07600; clashscore 4.87 / 4.35; rotamers 1.18 / 1.18. {"sigma": 2.5, "n_peaks": 334, "n_sites": 99, "n_copies": 256}. Adopted model `/home/dev/runs/7KR0/experiments/e049_portable/steps/r4_pick/cand_s2.pdb`
- **r4_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select -0.00008 not <= -2 sigma (0.00008). dselect -0.00008 (sigma 0.00008), dreport -0.00032, dfull -0.00020, dgap +0.00008; cand mean full 0.07521 / ctrl 0.07541; clashscore 5.00 / 5.06; rotamers 1.18 / 1.18. {"n_water_iso": 517}
- **r5_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **ADOPTED** - all criteria met. dselect -0.00033 (sigma 0.00007), dreport -0.00146, dfull -0.00089, dgap -0.00060; cand mean full 0.07452 / ctrl 0.07541; clashscore 5.06 / 5.06; rotamers 1.18 / 1.18. {"sigma": 2.5, "n_peaks": 306, "n_sites": 71, "n_copies": 175}. Adopted model `/home/dev/runs/7KR0/experiments/e049_portable/steps/r5_pick/cand_s3.pdb`
- **r5_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select -0.00001 not <= -2 sigma (0.00010). dselect -0.00001 (sigma 0.00010), dreport -0.00045, dfull -0.00023, dgap +0.00003; cand mean full 0.07449 / ctrl 0.07472; clashscore 5.25 / 5.25; rotamers 1.18 / 1.18. {"n_water_iso": 627}
- **r5_cleanup** (cleanup, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select worse by +0.00041 > 2 sigma (0.00010). dselect +0.00041 (sigma 0.00010), dreport -0.00002, dfull +0.00020, dgap -0.00010; cand mean full 0.07492 / ctrl 0.07472; clashscore 4.41 / 5.25; rotamers 1.18 / 1.18. {"n_water_removed": 13, "clashscore_base": 5.06}
- **r6_pick** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - clashscore 5.38 > 5 and above control 5.25. dselect -0.00042 (sigma 0.00010), dreport -0.00048, dfull -0.00045, dgap -0.00045; cand mean full 0.07427 / ctrl 0.07472; clashscore 5.38 / 5.25; rotamers 1.18 / 1.18. {"sigma": 2.5, "n_peaks": 270, "n_sites": 42, "n_copies": 121}
- **r6_pick_cleanup** (pick, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select +0.00000 not <= -2 sigma (0.00010). dselect +0.00000 (sigma 0.00010), dreport -0.00055, dfull -0.00027, dgap -0.00054; cand mean full 0.07453 / ctrl 0.07480; clashscore 4.67 / 5.38; rotamers 1.42 / 1.18
- **r6_aniso_water** (aniso_water, weights cand [0.5, 1.0] / ctrl [0.5, 1.0], 10 mc): **not adopted** - select -0.00001 not <= -2 sigma (0.00010). dselect -0.00001 (sigma 0.00010), dreport -0.00045, dfull -0.00023, dgap +0.00003; cand mean full 0.07449 / ctrl 0.07472; clashscore 5.25 / 5.25; rotamers 1.18 / 1.18. {"n_water_iso": 627}

## Rounds

| round | adopted | model in force | full | clashscore | rotamers % | ended |
|---|---|---|---|---|---|---|
| 1 | True | `/home/dev/runs/7KR0/experiments/e049_portable/steps/r1_aniso_water/cand_s2.pdb` | 0.08571 | 4.67 | 1.30 | 2026-10-09T09:40:35Z |
| 2 | True | `/home/dev/runs/7KR0/experiments/e049_portable/steps/r2_aniso_water/cand_s1.pdb` | 0.07898 | 4.48 | 1.30 | 2026-10-09T14:36:13Z |
| 3 | True | `/home/dev/runs/7KR0/experiments/e049_portable/steps/r3_pick_cleanup/cand_s2.pdb` | 0.07572 | 4.61 | 1.18 | 2026-10-09T19:28:33Z |
| 4 | True | `/home/dev/runs/7KR0/experiments/e049_portable/steps/r4_pick/cand_s2.pdb` | 0.07498 | 4.87 | 1.18 | 2026-10-09T22:47:24Z |
| 5 | True | `/home/dev/runs/7KR0/experiments/e049_portable/steps/r5_pick/cand_s3.pdb` | 0.07455 | 5.06 | 1.18 | 2026-10-10T03:45:28Z |
