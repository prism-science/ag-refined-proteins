# 7R2H: every step of run Ta4f3f9 (the gate's facts lines)

R-free and R-work are the gate's numbers after the step (the candidate's median seed; for a refused step, the refused candidate). σ is the margin against the parent as written in the facts line; the verdict is against the control.

| step | parent | worker | change | R-free | σ | R-work | gap | clash | waters | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| S0000 | - | preprocessing | deposited model, anonymised, scored on the run's working data | 0.1551 |  | 0.1445 | 0.0106 | 0.0 | - | INIT |
| S0001 | S0000 | preprocessing | phenix.refine 10 cycles, sites + ADP + water occupancies, ordered solvent, nqh_flips off, 3 seeds; the median seed | 0.1355 |  | 0.1243 | 0.0112 | 4.3 | - | INIT |
| S0002 | S0001 | solvent | PO4 at the mFo-DFc peaks of 5.0 sigma and above that no atom explains, next to a nitrogen (occupancy 1, a tetrahedron the refinement turns) | 0.1397 |  | 0.1277 | 0.0120 | 15.5 | - | REFUSE |
| S0003 | S0001 | refinement | the deposited model has no TLS group | 0.1355 |  | 0.1243 | 0.0112 | 4.3 | - | REFUSE |
| S0004 | S0001 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.1356 |  | 0.1231 | 0.0125 | 3.0 | - | REFUSE |
| S0005 | S0001 | refinement | riding H already present | 0.1355 |  | 0.1243 | 0.0112 | 4.3 | - | REFUSE |
| S0006 | S0001 | refinement | TLS, 1 group (one for each protein chain) | 0.1482 |  | 0.1388 | 0.0094 | 3.0 | - | REFUSE |
| S0007 | S0001 | refinement | restraint weights wc 1 wu 1 against 0.5 1 | 0.1358 |  | 0.1238 | 0.0120 | 1.7 | - | REFUSE |
| S0008 | S0001 | refinement | restraint weights wc 0.3 wu 0.25 against 0.5 1 | 0.1326 |  | 0.1190 | 0.0137 | 3.5 | - | ACCEPT |
| S0009 | S0008 | refinement | restraint weights wc 0.2 wu 0.25 against 0.3 0.25 | 0.1337 |  | 0.1185 | 0.0152 | 3.9 | - | REFUSE |
| S0010 | S0008 | refinement | one protein chain: no NCS | 0.1326 |  | 0.1190 | 0.0137 | 3.5 | - | REFUSE |
| S0011 | S0008 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.1335 |  | 0.1187 | 0.0148 | 3.9 | - | REFUSE |
| S0012 | S0008 | refinement | water ADPs anisotropic | 0.1214 |  | 0.1052 | 0.0161 | 3.9 | - | ACCEPT |
| S0013 | S0012 | refinement | water ADPs anisotropic | 0.1219 |  | 0.1046 | 0.0173 | 3.9 | - | REFUSE |
| S0014 | S0012 | rotamer-finder | 6 copies from shake, riding H, 20 macro-cycles | 0.1114 |  | 0.0876 | 0.0238 | 4.6 | - | BUILD |
| S0015 | S0014 | solvent | waters at 4.0 sigma, mode single | 0.1071 |  | 0.0798 | 0.0273 | 5.7 | - | ACCEPT |
| S0016 | S0015 | solvent | waters at 4.0 sigma, mode single | 0.1027 |  | 0.0756 | 0.0270 | 6.5 | - | ACCEPT |
| S0017 | S0016 | solvent | waters at 4.0 sigma, mode single | 0.1011 |  | 0.0724 | 0.0286 | 6.7 | - | ACCEPT |
| S0018 | S0017 | solvent | waters at 3.0 sigma, mode single | 0.1001 |  | 0.0697 | 0.0304 | 7.8 | - | REFUSE |
| S0019 | S0017 | solvent | waters at 2.5 sigma, mode single | 0.0993 |  | 0.0693 | 0.0300 | 7.8 | - | ACCEPT |
| S0020 | S0019 | solvent | waters at 2.5 sigma, mode single | 0.0991 |  | 0.0672 | 0.0319 | 8.1 | - | REFUSE |
| S0021 | S0019 | refinement | water ADPs anisotropic | 0.0983 |  | 0.0671 | 0.0312 | 8.3 | - | REFUSE |
| S0022 | S0019 | refinement | 20 macro-cycles against 10 | 0.0985 |  | 0.0681 | 0.0305 | 8.3 | - | REFUSE |
| S0023 | S0019 | refinement | altloc occupancies refined | 0.0984 |  | 0.0676 | 0.0308 | 8.1 | - | REFUSE |
| S0024 | S0019 | solvent | waters at 2.5 sigma, mode single | 0.0991 |  | 0.0672 | 0.0319 | 8.1 | - | REFUSE |
| S0025 | S0019 | rotamer-finder | no rotamer fit raised the residue CC by 0.02 | 0.0993 |  | 0.0693 | 0.0300 | 7.8 | - | REFUSE |
