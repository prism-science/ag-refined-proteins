# 7KR0: every step of run Tff1b3f (the gate's facts lines)

R-free and R-work are the gate's numbers after the step (the candidate's median seed; for a refused step, the refused candidate). σ is the margin against the parent as written in the facts line; the verdict is against the control.

| step | parent | worker | change | R-free | σ | R-work | gap | clash | waters | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| S0000 | - | preprocessing | deposited model, anonymised, scored on the run's working data | 0.1175 |  | 0.1103 | 0.0071 | 4.3 | 316 | INIT |
| S0001 | S0000 | preprocessing | phenix.refine 10 cycles, sites + ADP + water occupancies, ordered solvent, nqh_flips off, 3 seeds; the median seed | 0.1094 | -50.5 | 0.1005 | +0.0018 | 5.3 | 407 | INIT |
| S0002 | S0001 | solvent | waters at 3.0 sigma, mode single | 0.1102 | +3.4 | 0.0972 | +0.0040 | 5.3 | 456 | REFUSE |
| S0003 | S0001 | solvent | waters at 4.0 sigma, mode single | 0.1096 | +0.9 | 0.0977 | +0.0030 | 5.0 | 428 | REFUSE |
| S0004 | S0001 | refinement | water ADPs anisotropic | 0.1049 | -27.9 | 0.0954 | +0.0006 | 6.3 | 407 | RETRY_CONNECTIVITY |
| S0005 | S0001 | refinement | 20 macro-cycles against 10 | 0.1093 | -0.9 | 0.0990 | +0.0014 | 4.8 | 407 | REFUSE |
| S0006 | S0001 | refinement | water ADPs anisotropic (the arms of S0004, re-judged under the clash cap of 15; operator 2026-10-15) | 0.1049 | -27.9 | 0.0954 | +0.0006 | 6.3 | 407 | ACCEPT |
| S0007 | S0006 | rotamer-finder | 6 copies from shake, riding H, 20 macro-cycles | 0.0930 |  | 0.0801 | +0.0035 | 5.5 | 2442 | BUILD |
| S0008 | S0007 | solvent | waters at 4.0 sigma, mode single | 0.0875 | -34.6 | 0.0716 | +0.0029 | 5.0 | 1438 | ACCEPT |
| S0009 | S0008 | connectivity | connectivity: failed (exit 1; PulpSolverError: PuLP: cannot execute cplex / log tail: ome/dev/runs/hr/Tff1b3f/pending/ens_relabel_10/prepare/untangler/Untangler/LinearOptimizer/Solver_sites_formulation.py", line 2814, in r) | 0.0875 |  | 0.0716 | +0.0000 | 5.0 | 1438 | REFUSE |
| S0010 | S0008 | solvent | waters at 3.0 sigma, mode single | 0.0840 | -21.6 | 0.0657 | +0.0025 | 4.7 | 1498 | ACCEPT |
| S0011 | S0010 | refinement | water ADPs anisotropic | 0.0808 | -20.2 | 0.0622 | +0.0003 | 4.7 | 1498 | ACCEPT |
| S0011 | | | 7KR0 pipeline: split, picks, relabel, aniso water, merge | | | | | | | prev bca8c84 |
| S0012 | S0011 | refinement | restraint weights wc 0.3 wu 0.25 against 0.5 1 | 0.0783 | -16.0 | 0.0576 | +0.0021 | 5.9 | 1498 | ACCEPT |
| S0013 | S0012 | connectivity | connectivity: failed (wall timeout; / log tail: 19747313345.11 38.14% 9784 5236 184 147488 947.8s 0 0 0 0.00% 12237498365.33 19747313345.11 38.03% 9909 5327 184 ) | 0.0783 |  | 0.0576 | +0.0000 | 5.9 | 1498 | REFUSE |
| S0014 | S0012 | solvent | waters at 3.0 sigma, mode single | 0.0772 | -6.6 | 0.0555 | +0.0010 | 6.8 | 1512 | ACCEPT |
| S0015 | S0014 | solvent | waters at 2.5 sigma, mode single | 0.0775 | +2.0 | 0.0539 | +0.0019 | 6.7 | 1667 | REFUSE |
| S0016 | S0014 | refinement | 20 macro-cycles against 10 | 0.0761 | -7.0 | 0.0544 | -0.0000 | 6.4 | 1512 | ACCEPT |
| S0017 | S0016 | refinement | copies merged into conformers (rmsd 0.3 A, floor 0.1, max 4); occupancies refined | 0.0890 |  | 0.0735 | -0.0063 | 24.8 | 1043 | BUILD |
| S0018 | S0016 | solvent | waters at 2.0 sigma, mode single | 0.0767 | +3.6 | 0.0521 | +0.0028 | 7.6 | 1824 | REFUSE |
| S0019 | S0016 | refinement | water ADPs anisotropic | 0.0756 | -3.1 | 0.0533 | +0.0006 | 6.6 | 1512 | ACCEPT |
| S0020 | S0017 | solvent | water clash cleanup | 0.0997 | +67.2 | 0.0835 | +0.0008 | 8.5 | 975 | REFUSE |
| S0021 | S0017 | solvent | water hygiene | 0.0894 | +2.9 | 0.0733 | +0.0008 | 23.7 | 1011 | REFUSE |
| S0022 | S0017 | refinement | 20 macro-cycles against 10 | 0.0894 | +2.7 | 0.0736 | +0.0004 | 23.3 | 1043 | REFUSE |
| S0023 | S0019 | refinement | 20 macro-cycles against 10 | 0.0745 | -6.6 | 0.0527 | -0.0005 | 7.1 | 1512 | ACCEPT |
| S0024 | S0023 | refinement | altloc occupancies refined | 0.0742 | -1.8 | 0.0517 | +0.0008 | 7.4 | 1512 | REFUSE |
| S0025 | S0023 | solvent | waters at 2.5 sigma, mode single | 0.0740 | -3.3 | 0.0513 | +0.0009 | 8.0 | 1658 | ACCEPT |
| S0026 | S0025 | refinement | water ADPs anisotropic | 0.0738 | -1.5 | 0.0505 | +0.0006 | 8.1 | 1658 | REFUSE |
| S0027 | S0025 | refinement | 40 macro-cycles against 10 | 0.0739 | -0.7 | 0.0510 | +0.0001 | 7.8 | 1658 | REFUSE |
| S0028 | S0025 | connectivity | connectivity relabel, 10 min effort | 0.0743 | +2.0 | 0.0508 | +0.0008 | 12.8 | 1658 | REFUSE |
| S0029 | S0025 | refinement | water ADPs anisotropic | 0.0738 | -1.5 | 0.0505 | +0.0006 | 8.1 | 1658 | REFUSE |
| S0030 | S0025 | solvent | waters at 2.5 sigma, mode single | 0.0735 | -2.9 | 0.0499 | +0.0008 | 7.9 | 1781 | ACCEPT |
| S0031 | S0030 | connectivity | connectivity relabel, 10 min effort | 0.0735 | +0.0 | 0.0492 | +0.0007 | 9.0 | 1781 | REFUSE |
| S0032 | S0030 | refinement | hydrogen positions and ADPs refined individually (riding before) | 0.0745 | +3.4 | 0.0474 | +0.0035 | 7.5 | 1781 | REFUSE |
| S0033 | S0030 | refinement | altloc occupancies refined | 0.0732 | -1.8 | 0.0488 | +0.0009 | 8.4 | 1781 | ACCEPT |
| S0034 | S0033 | refinement | restraint weights wc 0.3 wu 0.1 against 0.3 0.25 | 0.0737 | +3.0 | 0.0476 | +0.0016 | 8.2 | 1781 | REFUSE |
| S0035 | S0033 | refinement | restraint weights wc 0.2 wu 0.25 against 0.3 0.25 | 0.0735 | +1.9 | 0.0481 | +0.0010 | 9.1 | 1781 | REFUSE |
| S0036 | S0033 | refinement | restraint weights wc 0.2 wu 0.1 against 0.3 0.25 | 0.0737 | +2.7 | 0.0473 | +0.0019 | 8.9 | 1781 | REFUSE |
| S0037 | S0033 | refinement | 20 macro-cycles against 10 | 0.0736 | +2.1 | 0.0489 | +0.0002 | 8.5 | 1781 | REFUSE |
| S0038 | S0033 | refinement | water ADPs anisotropic | 0.0735 | +1.7 | 0.0482 | +0.0008 | 8.7 | 1781 | REFUSE |
| S0039 | S0033 | solvent | waters at 2.5 sigma, mode single | 0.0729 | -2.3 | 0.0479 | +0.0005 | 8.6 | 1877 | ACCEPT |
| S0040 | S0039 | solvent | single-copy waters above their share expanded to copies, occupancy kept | 0.0730 | +1.1 | 0.0475 | +0.0006 | 12.3 | 2960 | REFUSE |
| S0041 | S0039 | solvent | waters at 2.5 sigma, mode copies | 0.0737 | +5.3 | 0.0477 | +0.0011 | 9.2 | 2109 | REFUSE |
| S0042 | S0039 | solvent | waters at 2.5 sigma, mode single | 0.0726 | -1.9 | 0.0471 | +0.0005 | 9.0 | 1958 | ACCEPT |
| S0043 | S0042 | solvent | waters at 2.5 sigma, mode single | 0.0726 | +0.1 | 0.0464 | +0.0007 | 9.6 | 2018 | REFUSE |
| S0044 | S0042 | solvent | waters at 2.0 sigma, mode single | 0.0727 | +1.1 | 0.0461 | +0.0012 | 10.3 | 2204 | REFUSE |
| S0045 | S0042 | refinement | water occupancies reset to the copy share and held; occupancy refinement off | 0.0915 | +118.5 | 0.0700 | -0.0039 | 9.6 | 1958 | REFUSE |
| S0046 | S0042 | refinement | restraint weights wc 0.3 wu 0.5 against 0.3 0.25 | 0.0726 | +0.4 | 0.0476 | -0.0004 | 9.2 | 1958 | REFUSE |
| S0047 | S0042 | refinement | restraint weights wc 0.3 wu 1 against 0.3 0.25 | 0.0730 | +3.0 | 0.0488 | -0.0011 | 9.1 | 1958 | REFUSE |
| S0048 | S0042 | refinement | 20 macro-cycles against 10 | 0.0726 | +0.5 | 0.0470 | +0.0002 | 9.0 | 1958 | REFUSE |
| S0049 | S0042 | rotamer-finder | no rotamer fit raised the residue CC by 0.02 | 0.0726 |  | 0.0471 | +0.0000 | 9.0 | 1958 | REFUSE |
| S0050 | S0042 | solvent | every water expanded to ceil(occupancy x C) copies, occupancy kept, refined with each at or below 1/C | 0.0905 | +59.7 | 0.0708 | -0.0057 | 9.2 | 3726 | REFUSE |
| S0051 | S0042 | rotamer-finder | copies under difference peaks: the weakest copy takes the peak copy's rotamer | 0.0725 | -0.6 | 0.0472 | -0.0002 | 8.9 | 1956 | REFUSE |
| S0052 | S0042 | rotamer-finder | copies under difference peaks: the weakest copy takes the peak copy's rotamer | 0.0725 | -0.6 | 0.0469 | +0.0001 | 8.8 | 1956 | REFUSE |
| S0053 | S0042 | solvent | waters in own-copy clashes moved to a copy they clear; nothing deleted | 0.0725 | -0.3 | 0.0466 | +0.0005 | 7.7 | 1958 | ACCEPT |
| S0054 | S0053 | solvent | waters in own-copy clashes moved to a copy they clear; nothing deleted | 0.0727 | +1.3 | 0.0465 | +0.0004 | 8.0 | 1958 | REFUSE |
