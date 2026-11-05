# 7KR0: every step of run Tff1b3f_x (the gate's facts lines)

R-free and R-work are the gate's numbers after the step (the candidate's median seed; for a refused step, the refused candidate). σ is the margin against the parent as written in the facts line; the verdict is against the control.

| step | parent | worker | change | R-free | σ | R-work | gap | clash | waters | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| S0004 | S0001 | refinement | water ADPs anisotropic | 0.1050 |  | 0.0955 | 0.0095 | 6.3 | - | RETRY_CONNECTIVITY |
| S0005 | S0001 | refinement | 20 macro-cycles against 10 | 0.1093 |  | 0.0990 | 0.0103 | 4.8 | - | REFUSE |
| S0006 | S0001 | refinement | water ADPs anisotropic (the arms of S0004, re-judged under the clash cap of 15; operator 2026-10-15) | 0.1050 |  | 0.0955 | 0.0095 | 6.3 | - | ACCEPT |
| S0007 | S0006 | rotamer-finder | 6 copies from shake, riding H, 20 macro-cycles | 0.0931 |  | 0.0801 | 0.0130 | 5.5 | - | BUILD |
| S0008 | S0007 | solvent | waters at 4.0 sigma, mode single | 0.0876 |  | 0.0717 | 0.0159 | 5.0 | - | ACCEPT |
| S0009 | S0008 | connectivity | connectivity: failed (exit 1; PulpSolverError: PuLP: cannot execute cplex / log tail: ome/dev/runs/hr/Tff1b3f/pending/ens_relabel_10/prepare/untangler/Untangler/LinearOptimizer/Solver_sites_formulation.py", line 2814, in r) | 0.0876 |  | 0.0717 | 0.0159 | 5.0 | - | REFUSE |
| S0010 | S0008 | solvent | waters at 3.0 sigma, mode single | 0.0841 |  | 0.0657 | 0.0183 | 4.7 | - | ACCEPT |
| S0011 | S0010 | refinement | water ADPs anisotropic | 0.0809 |  | 0.0622 | 0.0186 | 4.7 | - | ACCEPT |
| S0012 | S0011 | refinement | restraint weights wc 0.3 wu 0.25 against 0.5 1 | 0.0783 |  | 0.0576 | 0.0207 | 5.9 | - | ACCEPT |
| S0013 | S0012 | connectivity | connectivity: failed (wall timeout;  / log tail:   19747313345.11    38.14%     9784   5236    184    147488   947.8s
         0       0         0   0.00%   12237498365.33  19747313345.11    38.03%     9909   5327    184  ) | 0.0783 |  | 0.0576 | 0.0207 | 5.9 | - | REFUSE |
| S0014 | S0012 | solvent | waters at 3.0 sigma, mode single | 0.0772 |  | 0.0555 | 0.0217 | 6.8 | - | ACCEPT |
| S0015 | S0014 | solvent | waters at 2.5 sigma, mode single | 0.0776 |  | 0.0539 | 0.0237 | 6.7 | - | REFUSE |
| S0016 | S0014 | refinement | 20 macro-cycles against 10 | 0.0761 |  | 0.0544 | 0.0217 | 6.4 | - | ACCEPT |
| S0017 | S0016 | refinement | copies merged into conformers (rmsd 0.3 A, floor 0.1, max 4); occupancies refined | 0.0890 |  | 0.0736 | 0.0154 | 24.8 | - | BUILD |
| S0018 | S0016 | solvent | waters at 2.0 sigma, mode single | 0.0767 |  | 0.0522 | 0.0245 | 7.6 | - | REFUSE |
| S0019 | S0016 | refinement | water ADPs anisotropic | 0.0756 |  | 0.0534 | 0.0223 | 6.6 | - | ACCEPT |
| S0020 | S0017 | solvent | water clash cleanup | 0.0997 |  | 0.0835 | 0.0162 | 8.5 | - | REFUSE |
| S0021 | S0017 | solvent | water hygiene | 0.0895 |  | 0.0733 | 0.0162 | 23.7 | - | REFUSE |
| S0022 | S0017 | refinement | 20 macro-cycles against 10 | 0.0894 |  | 0.0736 | 0.0158 | 23.3 | - | REFUSE |
| S0023 | S0019 | refinement | 20 macro-cycles against 10 | 0.0746 |  | 0.0528 | 0.0218 | 7.1 | - | ACCEPT |
| S0024 | S0023 | refinement | altloc occupancies refined | 0.0743 |  | 0.0517 | 0.0226 | 7.4 | - | REFUSE |
| S0025 | S0023 | solvent | waters at 2.5 sigma, mode single | 0.0740 |  | 0.0513 | 0.0227 | 8.0 | - | ACCEPT |
| S0026 | S0025 | refinement | water ADPs anisotropic | 0.0738 |  | 0.0505 | 0.0233 | 8.1 | - | REFUSE |
| S0027 | S0025 | refinement | 40 macro-cycles against 10 | 0.0739 |  | 0.0511 | 0.0229 | 7.8 | - | REFUSE |
| S0028 | S0025 | connectivity | connectivity relabel, 10 min effort | 0.0744 |  | 0.0509 | 0.0235 | 12.8 | - | REFUSE |
| S0029 | S0025 | refinement | water ADPs anisotropic | 0.0738 |  | 0.0505 | 0.0233 | 8.1 | - | REFUSE |
| S0030 | S0025 | solvent | waters at 2.5 sigma, mode single | 0.0736 |  | 0.0500 | 0.0236 | 7.9 | - | ACCEPT |
| S0031 | S0030 | connectivity | connectivity relabel, 10 min effort | 0.0736 |  | 0.0493 | 0.0243 | 9.0 | - | REFUSE |
| S0032 | S0030 | refinement | hydrogen positions and ADPs refined individually (riding before) | 0.0746 |  | 0.0474 | 0.0271 | 7.5 | - | REFUSE |
| S0033 | S0030 | refinement | altloc occupancies refined | 0.0733 |  | 0.0488 | 0.0244 | 8.4 | - | ACCEPT |
| S0034 | S0033 | refinement | restraint weights wc 0.3 wu 0.1 against 0.3 0.25 | 0.0738 |  | 0.0477 | 0.0261 | 8.2 | - | REFUSE |
| S0035 | S0033 | refinement | restraint weights wc 0.2 wu 0.25 against 0.3 0.25 | 0.0736 |  | 0.0482 | 0.0254 | 9.1 | - | REFUSE |
| S0036 | S0033 | refinement | restraint weights wc 0.2 wu 0.1 against 0.3 0.25 | 0.0737 |  | 0.0473 | 0.0264 | 8.9 | - | REFUSE |
| S0037 | S0033 | refinement | 20 macro-cycles against 10 | 0.0736 |  | 0.0489 | 0.0247 | 8.5 | - | REFUSE |
| S0038 | S0033 | refinement | water ADPs anisotropic | 0.0735 |  | 0.0483 | 0.0253 | 8.7 | - | REFUSE |
| S0039 | S0033 | solvent | waters at 2.5 sigma, mode single | 0.0729 |  | 0.0480 | 0.0249 | 8.6 | - | ACCEPT |
| S0040 | S0039 | solvent | single-copy waters above their share expanded to copies, occupancy kept | 0.0731 |  | 0.0476 | 0.0255 | 12.3 | - | REFUSE |
| S0041 | S0039 | solvent | waters at 2.5 sigma, mode copies | 0.0738 |  | 0.0477 | 0.0260 | 9.2 | - | REFUSE |
| S0042 | S0039 | solvent | waters at 2.5 sigma, mode single | 0.0726 |  | 0.0472 | 0.0254 | 9.0 | - | ACCEPT |
| S0043 | S0042 | solvent | waters at 2.5 sigma, mode single | 0.0726 |  | 0.0465 | 0.0262 | 9.6 | - | REFUSE |
| S0044 | S0042 | solvent | waters at 2.0 sigma, mode single | 0.0728 |  | 0.0462 | 0.0266 | 10.3 | - | REFUSE |
| S0045 | S0042 | refinement | water occupancies reset to the copy share and held; occupancy refinement off | 0.0916 |  | 0.0700 | 0.0216 | 9.6 | - | REFUSE |
| S0046 | S0042 | refinement | restraint weights wc 0.3 wu 0.5 against 0.3 0.25 | 0.0727 |  | 0.0477 | 0.0250 | 9.2 | - | REFUSE |
| S0047 | S0042 | refinement | restraint weights wc 0.3 wu 1 against 0.3 0.25 | 0.0731 |  | 0.0488 | 0.0243 | 9.1 | - | REFUSE |
| S0048 | S0042 | refinement | 20 macro-cycles against 10 | 0.0727 |  | 0.0471 | 0.0256 | 9.0 | - | REFUSE |
| S0049 | S0042 | rotamer-finder | no rotamer fit raised the residue CC by 0.02 | 0.0726 |  | 0.0472 | 0.0254 | 9.0 | - | REFUSE |
| S0050 | S0042 | solvent | every water expanded to ceil(occupancy x C) copies, occupancy kept, refined with each at or below 1/C | 0.0906 |  | 0.0708 | 0.0198 | 9.2 | - | REFUSE |
| S0051 | S0042 | rotamer-finder | copies under difference peaks: the weakest copy takes the peak copy's rotamer | 0.0725 |  | 0.0473 | 0.0252 | 8.9 | - | REFUSE |
| S0052 | S0042 | rotamer-finder | copies under difference peaks: the weakest copy takes the peak copy's rotamer | 0.0725 |  | 0.0470 | 0.0255 | 8.8 | - | REFUSE |
| S0053 | S0042 | solvent | waters in own-copy clashes moved to a copy they clear; nothing deleted | 0.0726 |  | 0.0467 | 0.0259 | 7.7 | - | ACCEPT |
| S0054 | S0053 | solvent | waters in own-copy clashes moved to a copy they clear; nothing deleted | 0.0728 |  | 0.0465 | 0.0263 | 8.0 | - | REFUSE |
| S0055 | S0053 | solvent | waters below 0.5 sigma in the work-only 2mFo-DFc map removed | 0.0783 |  | 0.0600 | 0.0183 | 7.2 | - | REFUSE |
| S0056 | S0053 | solvent | waters below 1.0 sigma in the work-only 2mFo-DFc map removed | 0.0843 |  | 0.0694 | 0.0149 | 6.1 | - | REFUSE |
| S0057 | S0053 | solvent | water clash cleanup | 0.0740 |  | 0.0484 | 0.0256 | 5.4 | - | REFUSE |
| S0058 | S0053 | refinement | bulk-solvent mask radii optimised (refinement.main.optimize_mask) against the fixed defaults | 0.0728 |  | 0.0465 | 0.0263 | 8.1 | - | REFUSE |
| S0059 | S0053 | solvent | waters at 2.0 sigma, mode single, 3 hydrogen-bond partners required | 0.0733 |  | 0.0463 | 0.0269 | 8.5 | - | REFUSE |
| S0060 | S0053 | refinement | 20 macro-cycles against 10 | 0.0729 |  | 0.0469 | 0.0260 | 7.9 | - | REFUSE |
| S0061 | S0053 | rotamer-finder | copies under difference peaks: the weakest copy takes the peak copy's rotamer | 0.0738 |  | 0.0477 | 0.0261 | 8.3 | - | REFUSE |
| S0062 | S0053 | rotamer-finder | no rotamer fit raised the residue CC by 0.02 | 0.0726 |  | 0.0467 | 0.0259 | 7.7 | - | REFUSE |
| S0063 | S0053 | refinement | 20 macro-cycles against 10 | 0.0729 |  | 0.0469 | 0.0260 | 7.9 | - | REFUSE |
| S0064 | S0030 | refinement | inter-cell nonbond clashes excluded (custom_scripts/disable_intercell_nonbonds.py, overlap 0.4 A and more across a unit-cell translation) against none | 0.0738 |  | 0.0491 | 0.0248 | 8.6 | - | REFUSE |
| S0065 | S0030 | connectivity | the candidate of S0031 judged again, unchanged, inter-cell nonbond exclusions in both arms (custom_scripts/disable_intercell_nonbonds.py) | 0.0734 |  | 0.0492 | 0.0242 | 8.8 | - | REFUSE |
| S0066 | S0053 | refinement | hydrogen positions and ADPs refined individually (riding before) | 0.0731 |  | 0.0448 | 0.0283 | 6.7 | - | REFUSE |
| S0067 | S0053 | refinement | restraint weights wc 0.2 wu 0.25 against 0.3 0.25 | 0.0727 |  | 0.0461 | 0.0266 | 8.3 | - | REFUSE |
| S0068 | S0053 | refinement | restraint weights wc 0.3 wu 0.1 against 0.3 0.25 | 0.0727 |  | 0.0456 | 0.0272 | 7.8 | - | REFUSE |
| S0069 | S0053 | refinement | restraint weights wc 0.5 wu 0.5 against 0.3 0.25 | 0.0731 |  | 0.0480 | 0.0251 | 7.4 | - | REFUSE |
| S0070 | S0053 | solvent | waters at 3.5 sigma, mode single | 0.0727 |  | 0.0464 | 0.0263 | 8.0 | - | REFUSE |
| S0071 | S0053 | refinement | restraint weights wc 0.2 wu 0.1 against 0.3 0.25 | 0.0727 |  | 0.0452 | 0.0275 | 8.2 | - | REFUSE |
| S0072 | S0053 | solvent | waters at 3.0 sigma, mode single | 0.0726 |  | 0.0465 | 0.0262 | 8.0 | - | REFUSE |
| S0073 | S0053 | refinement | protein ADPs isotropic (anisotropic before) | 0.0768 |  | 0.0561 | 0.0207 | 9.0 | - | REFUSE |
| S0074 | S0053 | solvent | waters at 2.5 sigma, mode single | 0.0729 |  | 0.0463 | 0.0266 | 8.6 | - | REFUSE |
| S0075 | S0053 | refinement | TLS, 1 group (one for each protein chain) | 0.0818 |  | 0.0593 | 0.0225 | 8.1 | - | REFUSE |
| S0076 | S0053 | refinement | water ADPs anisotropic | 0.0730 |  | 0.0460 | 0.0270 | 8.0 | - | REFUSE |
| S0077 | S0053 | refinement | water ADPs anisotropic | 0.0730 |  | 0.0460 | 0.0270 | 8.0 | - | REFUSE |
| S0078 | S0053 | refinement | altloc occupancies refined | 0.0726 |  | 0.0464 | 0.0262 | 8.1 | - | REFUSE |
| S0079 | S0053 | rotamer-finder | no rotamer fit raised the residue CC by 0 | 0.0726 |  | 0.0467 | 0.0259 | 7.7 | - | REFUSE |
| S0080 | S0053 | refinement | altloc occupancies refined | 0.0726 |  | 0.0464 | 0.0262 | 8.1 | - | REFUSE |
| S0081 | S0053 | rotamer-finder | no rotamer fit raised the residue CC by 0 | 0.0726 |  | 0.0467 | 0.0259 | 7.7 | - | REFUSE |
| S0082 | S0007 | solvent | every water at its copy share (lettered 1/6, shared 1) and held; occupancy refinement off, 10 macro-cycles | 0.0932 |  | 0.0750 | 0.0182 | 10.4 | - | BUILD |
| S0083 | S0082 | solvent | waters at 4.0 sigma, mode single | 0.0864 |  | 0.0668 | 0.0196 | 10.6 | - | REFUSE |
| S0084 | S0082 | solvent | waters at 4.0 sigma, mode single | 0.0864 |  | 0.0668 | 0.0196 | 10.6 | - | ACCEPT |
| S0085 | S0084 | solvent | waters at 4.0 sigma, mode single | 0.0843 |  | 0.0628 | 0.0215 | 10.8 | - | ACCEPT |
| S0086 | S0085 | solvent | waters at 4.0 sigma, mode single | 0.0829 |  | 0.0606 | 0.0223 | 11.3 | - | REFUSE |
| S0087 | S0085 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.0832 |  | 0.0608 | 0.0224 | 11.0 | - | REFUSE |
| S0088 | S0085 | solvent | waters at 3.0 sigma, mode single | 0.0816 |  | 0.0596 | 0.0219 | 11.2 | - | ACCEPT |
| S0089 | S0088 | solvent | waters at 3.0 sigma, mode single | 0.0810 |  | 0.0576 | 0.0234 | 12.3 | - | REFUSE |
| S0090 | S0088 | refinement | water ADPs anisotropic | 0.0762 |  | 0.0534 | 0.0228 | 11.7 | - | ACCEPT |
| S0091 | S0090 | refinement | water ADPs anisotropic | 0.0758 |  | 0.0524 | 0.0233 | 12.1 | - | ACCEPT |
| S0092 | S0091 | refinement | water ADPs anisotropic | 0.0755 |  | 0.0520 | 0.0235 | 12.1 | - | ACCEPT |
| S0093 | S0092 | solvent | waters in own-copy clashes moved to a copy they clear; nothing deleted | 0.0764 |  | 0.0526 | 0.0238 | 11.9 | - | REFUSE |
| S0094 | S0092 | solvent | waters at 2.5 sigma, mode single | 0.0737 |  | 0.0494 | 0.0244 | 11.7 | - | ACCEPT |
| S0095 | S0094 | solvent | waters at 2.5 sigma, mode single | 0.0736 |  | 0.0483 | 0.0253 | 12.1 | - | REFUSE |
| S0096 | S0094 | solvent | waters at 2.0 sigma, mode single | 0.0741 |  | 0.0477 | 0.0264 | 12.0 | - | REFUSE |
| S0097 | S0094 | rotamer-finder | copies under difference peaks: the weakest copy takes the peak copy's rotamer | 0.0735 |  | 0.0485 | 0.0250 | 12.9 | - | REFUSE |
| S0098 | S0094 | refinement | 20 macro-cycles against 10 | 0.0729 |  | 0.0488 | 0.0242 | 11.5 | - | ACCEPT |
| S0099 | S0098 | solvent | the strongest mFo-DFc peaks (6.0 sigma and up): a lettered water under a peak made a water of every copy; a peak in open solvent a new water of every copy | 0.0730 |  | 0.0479 | 0.0251 | 12.6 | - | REFUSE |
| S0100 | S0098 | connectivity | connectivity relabel, 10 min effort | 0.0732 |  | 0.0484 | 0.0249 | 14.6 | - | REFUSE |
| S0101 | S0098 | solvent | waters in the range of motion deleted (within 2.2 A of a protein atom of any copy) | 0.0866 |  | 0.0627 | 0.0238 | 11.6 | - | REFUSE |
| S0102 | S0098 | rotamer-finder | Coot rotamer fit and real-space refinement of each copy of the residues with an atom beyond +-3.5 sigma in the work-only mFo-DFc map; the counted waters that a moved side chain overlaps deleted | 0.0753 |  | 0.0505 | 0.0248 | 11.7 | - | REFUSE |
| S0103 | S0098 | rotamer-finder | B-factors of the copies reset to the copy median where they differ by more than 3 times | 0.0730 |  | 0.0482 | 0.0249 | 11.7 | - | ACCEPT |
| S0104 | S0103 | solvent | waters at 3.0 sigma, mode single, none within 2.6 A of a protein atom of any copy | 0.0729 |  | 0.0474 | 0.0255 | 12.8 | - | REFUSE |
| S0105 | S0103 | solvent | waters at 2.5 sigma, mode single, none within 2.6 A of a protein atom of any copy | 0.0723 |  | 0.0475 | 0.0249 | 12.6 | - | ACCEPT |
| S0106 | S0105 | refinement | water ADPs anisotropic | 0.0731 |  | 0.0479 | 0.0253 | 12.7 | - | REFUSE |
| S0107 | S0105 | refinement | restraint weights wc 1 wu 1 against 0.3 0.25 | 0.0733 |  | 0.0508 | 0.0225 | 9.5 | - | REFUSE |
| S0108 | S0105 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.0725 |  | 0.0469 | 0.0255 | 13.3 | - | REFUSE |
| S0109 | S0105 | solvent | the strongest mFo-DFc peaks (6.0 sigma and up): a lettered water under a peak made a water of every copy; a peak in open solvent a new water of every copy | 0.0724 |  | 0.0472 | 0.0252 | 13.4 | - | REFUSE |
| S0110 | S0105 | connectivity | connectivity relabel, 10 min effort | 0.0725 |  | 0.0478 | 0.0247 | 15.2 | - | REFUSE |
| S0111 | S0105 | connectivity | connectivity: failed (exit 1; ImportError: cannot import name 'WIP_Solver' from 'LinearOptimizer' (/home/dev/runs/hr/Tff1b3f_oct28/pending/untangle_lcr/prepare/untangler/Untangler/LinearOptimizer/__init__.py) / log tail: .) | 0.0723 |  | 0.0475 | 0.0249 | 12.6 | - | REFUSE |
| S0112 | S0105 | rotamer-finder | B-factors of the copies reset to the copy median where they differ by more than 3 times | 0.0725 |  | 0.0472 | 0.0253 | 12.7 | - | ACCEPT |
| S0113 | S0105 | connectivity | connectivity relabel, 10 min effort, Untangler low_compute_clash_resolution | 0.0730 |  | 0.0476 | 0.0254 | 13.9 | - | REFUSE |
| S0114 | S0112 | refinement | Asn/Gln/His flips by reduce in the candidate's refinement (nqh_flips, off in the recipe) against the recipe without them | 0.0724 |  | 0.0466 | 0.0259 | 13.5 | - | REFUSE |
| S0115 | S0112 | refinement | nonbonded restraint weight 300 against the default 100 (the clash term alone; wc and wu unchanged) | 0.0735 |  | 0.0487 | 0.0248 | 2.5 | - | REFUSE |
| S0116 | S0112 | solvent | lettered waters of one site in every conformer (within 0.5 A of their centroid) merged into one shared water at occupancy 1 | 0.0738 |  | 0.0487 | 0.0251 | 13.2 | - | REFUSE |
| S0117 | S0112 | solvent | lettered waters of one site in every conformer (within 1 A of their centroid) merged into one shared water at occupancy 1 | 0.0800 |  | 0.0567 | 0.0233 | 12.3 | - | REFUSE |
| S0118 | S0112 | rotamer-finder | residues whose conformers lie within 0.5 A RMSD of each other collapsed to one conformer (no letter, occupancy 1) | 0.0738 |  | 0.0516 | 0.0222 | 17.5 | - | REFUSE |
| S0119 | S0112 | rotamer-finder | residues whose conformers lie within 0.75 A RMSD of each other collapsed to one conformer (no letter, occupancy 1) | 0.0765 |  | 0.0552 | 0.0213 | 21.6 | - | REFUSE |
| S0120 | S0112 | rotamer-finder | conformers with side-chain B above 2 x the site median: B to the median, occupancy x (median/B)^1.5, the residue's occupancies renormalised to 1 | 0.0723 |  | 0.0466 | 0.0257 | 13.6 | - | ACCEPT |
| S0121 | S0120 | connectivity | connectivity relabel, 10 min effort, Untangler low_compute_clash_resolution | 0.0727 |  | 0.0468 | 0.0258 | 14.7 | - | REFUSE |
| S0122 | S0120 | refinement | nonbonded restraint weight 1000 against the default 100 (the clash term alone; wc and wu unchanged) | 0.0744 |  | 0.0506 | 0.0238 | 1.1 | - | REFUSE |
| S0123 | S0120 | rotamer-finder | Coot rotamer fit and real-space refinement of each conformer of the residues in the most repeated MolProbity clash contacts (A37,A50,A45,A65,A20,A155,A113,A139,A92,A94,A2), on the omit maps; a repair on the clashscore | 0.0722 |  | 0.0465 | 0.0258 | 14.1 | - | REFUSE |
| S0124 | S0120 | refinement | nonbonded restraint weight 300 against the default 100 (the clash term alone; wc and wu unchanged) | 0.0734 |  | 0.0487 | 0.0247 | 2.6 | - | REFUSE |
| S0125 | S0120 | connectivity | connectivity relabel, 30 min effort, Untangler low_compute_clash_resolution | 0.0727 |  | 0.0468 | 0.0258 | 14.7 | - | REFUSE |
| S0126 | S0120 | refinement | hydrogen positions and ADPs refined individually (riding before) | 0.0745 |  | 0.0488 | 0.0257 | 14.1 | - | REFUSE |
| S0127 | S0120 | refinement | nonbonded restraint weight 150 against the default 100 (the clash term alone; wc and wu unchanged) | 0.0729 |  | 0.0476 | 0.0253 | 4.9 | - | REFUSE |
| S0128 | S0124 | refinement | nonbonded restraint weight 200 against the default 100 (the clash term alone; wc and wu unchanged) | 0.0731 |  | 0.0479 | 0.0252 | 2.5 | - | REFUSE |
| S0129 | S0124 | rotamer-finder | conformers with side-chain B above 2 x the site median: B to the median, occupancy x (median/B)^1.5, the residue's occupancies renormalised to 1 | 0.0725 |  | 0.0466 | 0.0259 | 7.3 | - | ACCEPT |
| S0130 | S0124 | connectivity | connectivity relabel, 30 min effort, Untangler low_compute_clash_resolution | 0.0723 |  | 0.0471 | 0.0251 | 9.7 | - | REFUSE |
| S0131 | S0129 | refinement | nonbonded restraint weight 200 against the default 100 (the clash term alone; wc and wu unchanged) | 0.0736 |  | 0.0489 | 0.0247 | 4.1 | - | REFUSE |
| S0132 | S0129 | connectivity | connectivity relabel, 30 min effort, Untangler low_compute_clash_resolution | 0.0729 |  | 0.0465 | 0.0264 | 10.8 | - | REFUSE |
| S0133 | S0130 | refinement | nonbonded restraint weight 200 against the default 100 (the clash term alone; wc and wu unchanged) | 0.0736 |  | 0.0488 | 0.0248 | 3.9 | - | REFUSE |
| S0134 | S0130 | rotamer-finder | conformers with side-chain B above 2 x the site median: B to the median, occupancy x (median/B)^1.5, the residue's occupancies renormalised to 1 | 0.0723 |  | 0.0465 | 0.0257 | 11.3 | - | ACCEPT |
| S0135 | S0128 | rotamer-finder | conformers with side-chain B above 2 x the site median: B to the median, occupancy x (median/B)^1.5, the residue's occupancies renormalised to 1 | 0.0726 |  | 0.0464 | 0.0261 | 6.4 | - | ACCEPT |
| S0136 | S0135 | rotamer-finder | conformers with side-chain B above 2 x the site median: B to the median, occupancy x (median/B)^1.5, the residue's occupancies renormalised to 1 | 0.0725 |  | 0.0459 | 0.0266 | 8.2 | - | REFUSE |
| S0137 | S0135 | rotamer-finder | conformers with side-chain B above 1.5 x the site median: B to the median, occupancy x (median/B)^1.5, the residue's occupancies renormalised to 1 | 0.0746 |  | 0.0493 | 0.0253 | 8.2 | - | REFUSE |
| S0138 | S0135 | refinement | nonbonded restraint weight 150 against the default 100 (the clash term alone; wc and wu unchanged) | 0.0732 |  | 0.0469 | 0.0263 | 2.9 | - | REFUSE |
| S0139 | S0135 | refinement | nonbonded restraint weight 200 against the default 100 (the clash term alone; wc and wu unchanged) | 0.0733 |  | 0.0472 | 0.0261 | 2.7 | - | REFUSE |
| S0140 | S0135 | refinement | nonbonded restraint weight 120 against the default 100 (the clash term alone; wc and wu unchanged) | 0.0731 |  | 0.0468 | 0.0262 | 3.5 | - | REFUSE |
| S0141 | S0135 | refinement | nonbonded restraint weight 110 against the default 100 (the clash term alone; wc and wu unchanged) | 0.0730 |  | 0.0468 | 0.0263 | 3.7 | - | REFUSE |
| S0142 | S0135 | refinement | nonbonded restraint weight 130 against the default 100 (the clash term alone; wc and wu unchanged) | 0.0731 |  | 0.0468 | 0.0263 | 3.1 | - | REFUSE |
| S0143 | S0135 | refinement | nonbonded restraint weight 60 against phenix's default (16 at d_min <= 1.2 A, else 100: phenix/refinement/fsr/preprocess.py) (the clash term alone; wc and wu unchanged) | 0.0728 |  | 0.0464 | 0.0265 | 5.2 | - | ACCEPT |
| S0144 | S0135 | refinement | nonbonded restraint weight 40 against phenix's default (16 at d_min <= 1.2 A, else 100: phenix/refinement/fsr/preprocess.py) (the clash term alone; wc and wu unchanged) | 0.0728 |  | 0.0461 | 0.0266 | 5.8 | - | ACCEPT |
| S0145 | S0135 | refinement | nonbonded restraint weight 25 against phenix's default (16 at d_min <= 1.2 A, else 100: phenix/refinement/fsr/preprocess.py) (the clash term alone; wc and wu unchanged) | 0.0725 |  | 0.0461 | 0.0264 | 7.1 | - | ACCEPT |
| S0146 | S0120 | refinement | nonbonded restraint weight 30 against phenix's default (16 at d_min <= 1.2 A, else 100: phenix/refinement/fsr/preprocess.py) (the clash term alone; wc and wu unchanged) | 0.0725 |  | 0.0465 | 0.0260 | 11.1 | - | ACCEPT |
| S0147 | S0144 | refinement | nonbonded restraint weight 50 against 40 (the clash term alone; wc and wu unchanged) | 0.0728 |  | 0.0460 | 0.0268 | 5.6 | - | REFUSE |
| S0148 | S0144 | rotamer-finder | conformers with side-chain B above 2 x the site median: B to the median, occupancy x (median/B)^1.5, the residue's occupancies renormalised to 1 | 0.0727 |  | 0.0460 | 0.0267 | 6.0 | - | ACCEPT |
| S0149 | S0145 | rotamer-finder | conformers with side-chain B above 2 x the site median: B to the median, occupancy x (median/B)^1.5, the residue's occupancies renormalised to 1 | 0.0727 |  | 0.0458 | 0.0268 | 6.8 | - | ACCEPT |
| S0150 | S0144 | connectivity | connectivity relabel, 30 min effort, Untangler low_compute_clash_resolution | 0.0731 |  | 0.0466 | 0.0266 | 7.9 | - | REFUSE |
