# 8C5N: every step of run T5f59f1_oct28 (the gate's facts lines)

R-free and R-work are the gate's numbers after the step (the candidate's median seed; for a refused step, the refused candidate). σ is the margin against the parent as written in the facts line; the verdict is against the control.

| step | parent | worker | change | R-free | σ | R-work | gap | clash | waters | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| S0000 | - | preprocessing | deposited model, anonymised, scored on the run's working data | 0.1571 |  | 0.1480 | 0.0092 | 7.0 | - | INIT |
| S0001 | S0000 | preprocessing | phenix.refine 10 cycles, sites + ADP + water occupancies, ordered solvent, nqh_flips off, 3 seeds; the median seed | 0.1294 |  | 0.1247 | 0.0046 | 4.8 | - | INIT |
| S0002 | S0001 | solvent | CL at the mFo-DFc peaks of 5.0 sigma and above that no atom explains, next to a nitrogen (occupancy 1) | 0.1346 |  | 0.1287 | 0.0059 | 4.0 | - | REFUSE |
| S0003 | S0001 | refinement | the deposited model has no TLS group | 0.1294 |  | 0.1247 | 0.0046 | 4.8 | - | REFUSE |
| S0004 | S0001 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.1306 |  | 0.1247 | 0.0059 | 3.1 | - | REFUSE |
| S0005 | S0001 | refinement | riding hydrogens added (phenix.ready_set, else mmtbx.reduce2); the control has none | 0.1275 |  | 0.1204 | 0.0071 | 3.6 | - | REFUSE |
| S0006 | S0001 | refinement | TLS, 1 group (one for each protein chain) | 0.1465 |  | 0.1408 | 0.0058 | 3.1 | - | REFUSE |
| S0007 | S0001 | refinement | restraint weights wc 1 wu 1 against 0.5 1 | 0.1310 |  | 0.1253 | 0.0058 | 3.5 | - | REFUSE |
| S0008 | S0001 | refinement | restraint weights wc 0.3 wu 0.25 against 0.5 1 | 0.1261 |  | 0.1193 | 0.0068 | 2.2 | - | ACCEPT |
| S0009 | S0008 | refinement | restraint weights wc 0.2 wu 0.25 against 0.3 0.25 | 0.1269 |  | 0.1191 | 0.0078 | 4.0 | - | REFUSE |
| S0010 | S0008 | refinement | one protein chain: no NCS | 0.1261 |  | 0.1193 | 0.0068 | 2.2 | - | REFUSE |
| S0011 | S0008 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.1270 |  | 0.1193 | 0.0077 | 4.0 | - | REFUSE |
| S0012 | S0008 | refinement | water ADPs anisotropic | 0.1197 |  | 0.1122 | 0.0075 | 4.8 | - | ACCEPT |
| S0013 | S0012 | refinement | water ADPs anisotropic | 0.1197 |  | 0.1114 | 0.0083 | 6.2 | - | REFUSE |
| S0014 | S0012 | rotamer-finder | 6 copies from shake, riding H, 20 macro-cycles | 0.1025 |  | 0.0880 | 0.0145 | 6.0 | - | BUILD |
| S0015 | S0014 | solvent | waters at 4.0 sigma, mode single | 0.0977 |  | 0.0801 | 0.0176 | 6.7 | - | ACCEPT |
| S0016 | S0015 | solvent | waters at 4.0 sigma, mode single | 0.0960 |  | 0.0760 | 0.0200 | 7.6 | - | ACCEPT |
| S0017 | S0016 | solvent | waters at 4.0 sigma, mode single | 0.0959 |  | 0.0742 | 0.0216 | 8.5 | - | REFUSE |
| S0018 | S0016 | solvent | waters at 3.0 sigma, mode single | 0.0938 |  | 0.0725 | 0.0212 | 8.5 | - | ACCEPT |
| S0019 | S0018 | solvent | waters at 3.0 sigma, mode single | 0.0931 |  | 0.0703 | 0.0228 | 9.7 | - | REFUSE |
| S0020 | S0018 | solvent | waters at 2.5 sigma, mode single | 0.0924 |  | 0.0696 | 0.0228 | 9.2 | - | REFUSE |
| S0021 | S0018 | refinement | water ADPs anisotropic | 0.0916 |  | 0.0692 | 0.0224 | 9.4 | - | ACCEPT |
| S0022 | S0021 | refinement | water ADPs anisotropic | 0.0915 |  | 0.0681 | 0.0233 | 10.2 | - | REFUSE |
| S0023 | S0021 | refinement | 20 macro-cycles against 10 | 0.0912 |  | 0.0684 | 0.0228 | 11.3 | - | REFUSE |
| S0024 | S0021 | refinement | altloc occupancies refined | 0.0911 |  | 0.0675 | 0.0236 | 10.4 | - | REFUSE |
| S0025 | S0021 | solvent | waters at 2.5 sigma, mode single | 0.0906 |  | 0.0665 | 0.0241 | 9.7 | - | REFUSE |
| S0026 | S0021 | rotamer-finder | no rotamer fit raised the residue CC by 0.02 | 0.0916 |  | 0.0692 | 0.0224 | 9.4 | - | REFUSE |
| S0027 | S0021 | solvent | waters in own-copy clashes moved to a copy they clear; nothing deleted | 0.0908 |  | 0.0675 | 0.0233 | 8.8 | - | ACCEPT |
| S0028 | S0027 | rotamer-finder | copies under difference peaks: the weakest copy takes the peak copy's rotamer | 0.0908 |  | 0.0668 | 0.0240 | 10.0 | - | REFUSE |
| S0029 | S0027 | refinement | 20 macro-cycles against 10 | 0.0909 |  | 0.0675 | 0.0234 | 10.8 | - | REFUSE |
| S0030 | S0014 | solvent | every water at its copy share (lettered 1/6, shared 1) and held; occupancy refinement off, 10 macro-cycles | 0.1022 |  | 0.0824 | 0.0198 | 9.7 | - | BUILD |
| S0031 | S0030 | solvent | waters at 4.0 sigma, mode single | 0.0965 |  | 0.0749 | 0.0215 | 11.3 | - | ACCEPT |
| S0032 | S0031 | solvent | waters at 4.0 sigma, mode single | 0.0945 |  | 0.0719 | 0.0226 | 13.1 | - | REFUSE |
| S0033 | S0031 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.0945 |  | 0.0721 | 0.0224 | 13.3 | - | ACCEPT |
| S0034 | S0031 | solvent | waters at 3.0 sigma, mode single | 0.0924 |  | 0.0704 | 0.0221 | 12.4 | - | ACCEPT |
| S0035 | S0034 | solvent | waters at 3.0 sigma, mode single | 0.0914 |  | 0.0679 | 0.0235 | 13.2 | - | REFUSE |
| S0036 | S0034 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.0915 |  | 0.0684 | 0.0231 | 13.2 | - | ACCEPT |
| S0037 | S0034 | refinement | water ADPs anisotropic | 0.0891 |  | 0.0672 | 0.0219 | 12.3 | - | ACCEPT |
| S0038 | S0037 | refinement | water ADPs anisotropic | 0.0889 |  | 0.0663 | 0.0226 | 12.9 | - | REFUSE |
| S0039 | S0037 | solvent | waters in own-copy clashes moved to a copy they clear; nothing deleted | 0.0879 |  | 0.0647 | 0.0232 | 13.1 | - | REFUSE |
| S0040 | S0037 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.0879 |  | 0.0648 | 0.0231 | 13.1 | - | ACCEPT |
| S0041 | S0037 | solvent | waters at 2.5 sigma, mode single | 0.0881 |  | 0.0642 | 0.0239 | 13.1 | - | REFUSE |
| S0042 | S0040 | solvent | waters at 2.5 sigma, mode single | 0.0880 |  | 0.0633 | 0.0247 | 14.0 | - | REFUSE |
| S0043 | S0040 | solvent | waters at 2.0 sigma, mode single | 0.0887 |  | 0.0631 | 0.0256 | 13.7 | - | REFUSE |
| S0044 | S0040 | rotamer-finder | copies under difference peaks: the weakest copy takes the peak copy's rotamer | 0.0877 |  | 0.0639 | 0.0238 | 14.2 | - | REFUSE |
| S0045 | S0040 | refinement | 20 macro-cycles against 10 | 0.0877 |  | 0.0644 | 0.0233 | 14.6 | - | REFUSE |
| S0046 | S0040 | rotamer-finder | waters in protein density deleted (own-copy clashes and other-copy density with occupancy above 1.5/C); Coot rotamer fit and real-space refinement of each copy of the residues next to them | 0.0871 |  | 0.0642 | 0.0230 | 14.4 | - | ACCEPT |
| S0047 | S0046 | rotamer-finder | Coot rotamer fit and real-space refinement of each copy of the residues with an atom beyond +-3.5 sigma in the work-only mFo-DFc map; the counted waters that a moved side chain overlaps deleted | 0.0890 |  | 0.0649 | 0.0241 | 13.8 | - | REFUSE |
| S0048 | S0046 | refinement | restraint weights wc 1 wu 1 against 0.3 0.25 | 0.0895 |  | 0.0696 | 0.0199 | 12.7 | - | REFUSE |
| S0049 | S0046 | rotamer-finder | B-factors of the copies reset to the copy median where they differ by more than 3 times | 0.0871 |  | 0.0637 | 0.0234 | 15.0 | - | ACCEPT |
| S0050 | S0049 | rotamer-finder | waters in protein density deleted (own-copy clashes and other-copy density with occupancy above 1.5/C); Coot rotamer fit and real-space refinement of each copy of the residues next to them | 0.0874 |  | 0.0634 | 0.0241 | 14.2 | - | ACCEPT |
| S0051 | S0050 | solvent | the strongest mFo-DFc peaks (6.0 sigma and up): a lettered water under a peak made a water of every copy; a peak in open solvent a new water of every copy | 0.0876 |  | 0.0631 | 0.0245 | 14.8 | - | REFUSE |
| S0052 | S0050 | connectivity | connectivity relabel, 10 min effort | 0.0876 |  | 0.0634 | 0.0242 | 13.5 | - | REFUSE |
| S0053 | S0050 | solvent | waters in the range of motion deleted (within 2.2 A of a protein atom of any copy) | 0.0921 |  | 0.0693 | 0.0228 | 15.5 | - | REFUSE |
| S0054 | S0050 | rotamer-finder | Coot rotamer fit and real-space refinement of each copy of the residues with an atom beyond +-3.5 sigma in the work-only mFo-DFc map; the counted waters that a moved side chain overlaps deleted | 0.0893 |  | 0.0638 | 0.0255 | 14.5 | - | REFUSE |
| S0055 | S0050 | rotamer-finder | B-factors of the copies reset to the copy median where they differ by more than 3 times | 0.0876 |  | 0.0629 | 0.0247 | 14.6 | - | ACCEPT |
| S0056 | S0055 | solvent | waters at 3.0 sigma, mode single, none within 2.6 A of a protein atom of any copy | 0.0878 |  | 0.0624 | 0.0254 | 14.9 | - | REFUSE |
| S0057 | S0055 | connectivity | connectivity: failed (exit 1; ImportError: cannot import name 'WIP_Solver' from 'LinearOptimizer' (/home/dev/runs/hr/T5f59f1_oct28/pending/untangle_lcr/prepare/untangler/Untangler/LinearOptimizer/__init__.py) / log tail: .) | 0.0876 |  | 0.0629 | 0.0247 | 14.6 | - | REFUSE |
| S0058 | S0055 | solvent | waters at 2.5 sigma, mode single, none within 2.6 A of a protein atom of any copy | 0.0879 |  | 0.0622 | 0.0257 | 15.2 | - | REFUSE |
| S0059 | S0055 | connectivity | connectivity relabel, 10 min effort, Untangler low_compute_clash_resolution | 0.0873 |  | 0.0625 | 0.0248 | 15.2 | - | REFUSE |
| S0060 | S0055 | refinement | water ADPs anisotropic | 0.0879 |  | 0.0631 | 0.0249 | 15.0 | - | REFUSE |
| S0061 | S0055 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.0877 |  | 0.0625 | 0.0252 | 15.1 | - | REFUSE |
| S0062 | S0055 | solvent | no peak at 6.0 sigma on a lettered water or in open solvent | 0.0876 |  | 0.0629 | 0.0247 | 14.6 | - | REFUSE |
| S0063 | S0055 | connectivity | connectivity relabel, 10 min effort, Untangler low_compute_clash_resolution | 0.0873 |  | 0.0625 | 0.0248 | 15.2 | - | REFUSE |
| S0064 | S0055 | rotamer-finder | B-factors of the copies reset to the copy median where they differ by more than 3 times | 0.0875 |  | 0.0625 | 0.0250 | 14.9 | - | REFUSE |
| S0065 | S0055 | rotamer-finder | conformer B-factors above the site median reset to the median where the conformer's 2mFo-DFc density is at least 0.5 of the site's (no ratio threshold); conformers in weak density keep their B | 0.0875 |  | 0.0627 | 0.0248 | 14.8 | - | ACCEPT |
