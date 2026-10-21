# 8C5N: every step of run T5f59f1 (the gate's facts lines)

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
