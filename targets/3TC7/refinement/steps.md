# 3TC7: every step of run T431c8e_gap (the gate's facts lines)

R-free and R-work are the gate's numbers after the step (the candidate's median seed; for a refused step, the refused candidate). σ is the margin against the parent as written in the facts line; the verdict is against the control.

| step | parent | worker | change | R-free | σ | R-work | gap | clash | waters | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| S0000 | - | preprocessing | deposited model, anonymised, scored on the run's working data | 0.1918 |  | 0.1536 | 0.0382 | 2.9 | - | INIT |
| S0001 | S0000 | preprocessing | phenix.refine 10 cycles, sites + ADP + water occupancies, ordered solvent, nqh_flips off, 3 seeds; the median seed | 0.1856 |  | 0.1412 | 0.0443 | 1.7 | - | INIT |
| S0002 | S0001 | refinement | the deposited model has no TLS group | 0.1856 |  | 0.1412 | 0.0443 | 1.7 | - | REFUSE |
| S0003 | S0001 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.1842 |  | 0.1387 | 0.0455 | 1.9 | - | ACCEPT |
| S0004 | S0003 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.1849 |  | 0.1387 | 0.0462 | 1.7 | - | REFUSE |
| S0005 | S0003 | refinement | riding hydrogens added (phenix.ready_set, else mmtbx.reduce2); the control has none | 0.1743 |  | 0.1282 | 0.0461 | 2.7 | - | ACCEPT |
| S0006 | S0005 | refinement | protein ADPs isotropic (anisotropic before) | 0.1759 |  | 0.1429 | 0.0331 | 2.4 | - | REFUSE |
| S0007 | S0005 | refinement | TLS, 1 group (one for each protein chain) | 0.1765 |  | 0.1451 | 0.0314 | 3.2 | - | REFUSE |
| S0008 | S0005 | refinement | restraint weights wc 1 wu 1 against 0.5 1 | 0.1744 |  | 0.1300 | 0.0444 | 2.2 | - | REFUSE |
| S0009 | S0005 | refinement | restraint weights wc 0.3 wu 0.25 against 0.5 1 | 0.1782 |  | 0.1203 | 0.0579 | 2.9 | - | REFUSE |
| S0010 | S0005 | refinement | one protein chain: no NCS | 0.1743 |  | 0.1282 | 0.0461 | 2.7 | - | REFUSE |
| S0011 | S0005 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.1746 |  | 0.1284 | 0.0462 | 2.9 | - | REFUSE |
| S0012 | S0005 | refinement | water ADPs anisotropic | 0.1708 |  | 0.1215 | 0.0494 | 2.4 | - | REFUSE |
| S0013 | S0005 | rotamer-finder | 2 copies from shake, riding H, 20 macro-cycles | 0.1734 |  | 0.1113 | 0.0622 | 4.4 | - | BUILD |
| S0014 | S0013 | solvent | waters at 4.0 sigma, mode single | 0.1696 |  | 0.1051 | 0.0646 | 4.2 | - | REFUSE |
| S0015 | S0013 | refinement | restraint weights wc 1 wu 1 against 0.5 1 | 0.1719 |  | 0.1119 | 0.0600 | 4.0 | - | REFUSE |
| S0016 | S0013 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.1706 |  | 0.1084 | 0.0622 | 4.8 | - | ACCEPT |
| S0017 | S0013 | solvent | waters at 3.0 sigma, mode single | 0.1701 |  | 0.1016 | 0.0684 | 4.0 | - | REFUSE |
| S0018 | S0016 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.1697 |  | 0.1081 | 0.0616 | 4.9 | - | ACCEPT |
| S0019 | S0016 | solvent | waters at 3.0 sigma, mode single | 0.1688 |  | 0.1004 | 0.0683 | 4.9 | - | REFUSE |
| S0020 | S0018 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.1688 |  | 0.1078 | 0.0609 | 4.5 | - | ACCEPT |
| S0021 | S0018 | solvent | waters at 3.0 sigma, mode single | 0.1675 |  | 0.0997 | 0.0678 | 4.5 | - | REFUSE |
| S0022 | S0020 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.1696 |  | 0.1068 | 0.0628 | 4.7 | - | REFUSE |
| S0023 | S0020 | solvent | waters at 2.5 sigma, mode single | 0.1627 |  | 0.0964 | 0.0663 | 4.3 | - | REFUSE |
| S0024 | S0020 | refinement | water ADPs anisotropic | 0.1659 |  | 0.0992 | 0.0667 | 4.4 | - | REFUSE |
| S0025 | S0020 | refinement | 20 macro-cycles against 10 | 0.1702 |  | 0.1071 | 0.0631 | 4.5 | - | REFUSE |
| S0026 | S0020 | refinement | altloc occupancies refined | 0.1696 |  | 0.1072 | 0.0623 | 4.7 | - | REFUSE |
| S0027 | S0020 | solvent | waters at 2.5 sigma, mode single | 0.1627 |  | 0.0964 | 0.0663 | 4.3 | - | REFUSE |
| S0028 | S0020 | rotamer-finder | no rotamer fit raised the residue CC by 0.02 | 0.1688 |  | 0.1078 | 0.0609 | 4.5 | - | REFUSE |
| S0029 | S0020 | solvent | no clashing water clears another copy | 0.1688 |  | 0.1078 | 0.0609 | 4.5 | - | REFUSE |
| S0030 | S0020 | rotamer-finder | copies under difference peaks: the weakest copy takes the peak copy's rotamer | 0.1702 |  | 0.1071 | 0.0631 | 4.4 | - | REFUSE |
| S0031 | S0020 | refinement | 20 macro-cycles against 10 | 0.1702 |  | 0.1071 | 0.0631 | 4.5 | - | REFUSE |
| S0032 | S0020 | rotamer-finder | 6 copies from shake, riding H, 20 macro-cycles | 0.1657 |  | 0.0897 | 0.0760 | 7.0 | - | BUILD |
| S0033 | S0032 | refinement | restraint weights wc 1 wu 1 against 0.5 1 | 0.1623 |  | 0.0879 | 0.0745 | 3.3 | - | ACCEPT |
| S0034 | S0033 | refinement | restraint weights wc 2 wu 2 against 1 1 | 0.1629 |  | 0.0914 | 0.0716 | 1.6 | - | REFUSE |
| S0035 | S0033 | solvent | PO4 at the mFo-DFc peaks of 5.0 sigma and above that no atom explains, next to a nitrogen (occupancy 1, a tetrahedron the refinement turns) | 0.1643 |  | 0.0857 | 0.0785 | 2.6 | - | REFUSE |
| S0036 | S0033 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.1612 |  | 0.0850 | 0.0762 | 2.8 | - | REFUSE |
| S0037 | S0033 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.1612 |  | 0.0850 | 0.0762 | 2.8 | - | ACCEPT |
| S0038 | S0033 | refinement | methionine as selenomethionine (MET -> MSE, SD -> SE) with an anomalous group for Se (f' -8, f'' 4, both refined; data at 0.97915 A) against the sulfur model | 0.1652 |  | 0.0971 | 0.0681 | 2.9 | - | REFUSE |
| S0039 | S0033 | refinement | protein ADPs isotropic (anisotropic before) | 0.1540 |  | 0.0928 | 0.0612 | 3.3 | - | ACCEPT |
| S0040 | S0033 | solvent | waters at 4.0 sigma, mode single | 0.1580 |  | 0.0834 | 0.0746 | 2.2 | - | ACCEPT |
| S0041 | S0037 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.1631 |  | 0.0832 | 0.0799 | 2.5 | - | REFUSE |
| S0042 | S0037 | refinement | methionine as selenomethionine (MET -> MSE, SD -> SE) with an anomalous group for Se (f' -8, f'' 4, both refined; data at 0.97915 A) against the sulfur model | 0.1661 |  | 0.0960 | 0.0701 | 2.7 | - | REFUSE |
| S0043 | S0039 | solvent | waters at 4.0 sigma, mode single | 0.1528 |  | 0.0884 | 0.0644 | 2.7 | - | ACCEPT |
| S0044 | S0039 | refinement | 1 group B factor for each residue (strategy group_adp) against individual ADPs | 0.1547 |  | 0.0910 | 0.0636 | 3.0 | - | ACCEPT |
| S0045 | S0039 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.1563 |  | 0.0937 | 0.0626 | 3.5 | - | REFUSE |
| S0046 | S0043 | solvent | waters at 4.0 sigma, mode single | 0.1512 |  | 0.0865 | 0.0647 | 2.6 | - | ACCEPT |
| S0047 | S0043 | refinement | TLS, 1 group (one for each protein chain) | 0.1514 |  | 0.0869 | 0.0645 | 2.6 | - | ACCEPT |
| S0048 | S0046 | solvent | waters at 4.0 sigma, mode single | 0.1500 |  | 0.0850 | 0.0650 | 2.5 | - | REFUSE |
| S0049 | S0046 | refinement | 20 macro-cycles against 10 | 0.1506 |  | 0.0852 | 0.0654 | 2.5 | - | REFUSE |
| S0050 | S0046 | solvent | waters at 3.0 sigma, mode single | 0.1480 |  | 0.0833 | 0.0647 | 2.8 | - | ACCEPT |
| S0051 | S0050 | solvent | waters at 3.0 sigma, mode single | 0.1515 |  | 0.0854 | 0.0661 | 2.6 | - | REFUSE |
| S0052 | S0050 | solvent | waters at 2.5 sigma, mode single | 0.1531 |  | 0.0848 | 0.0682 | 2.8 | - | REFUSE |
| S0053 | S0050 | solvent | waters at 2.0 sigma, mode single | 0.1552 |  | 0.0834 | 0.0718 | 2.7 | - | REFUSE |
| S0054 | S0050 | refinement | the standing recipe refines group ADPs (group1): no individual ADP selection | 0.1480 |  | 0.0833 | 0.0647 | 2.8 | - | REFUSE |
| S0055 | S0050 | refinement | 20 macro-cycles against 10 | 0.1489 |  | 0.0857 | 0.0633 | 2.6 | - | REFUSE |
| S0056 | S0050 | refinement | altloc occupancies refined | 0.1485 |  | 0.0853 | 0.0633 | 2.7 | - | REFUSE |
| S0057 | S0050 | solvent | waters at 2.5 sigma, mode single | 0.1531 |  | 0.0848 | 0.0682 | 2.8 | - | REFUSE |
| S0058 | S0050 | rotamer-finder | no rotamer fit raised the residue CC by 0.02 | 0.1480 |  | 0.0833 | 0.0647 | 2.8 | - | REFUSE |
| S0059 | S0050 | solvent | waters in own-copy clashes moved to a copy they clear; nothing deleted | 0.1488 |  | 0.0854 | 0.0634 | 2.8 | - | REFUSE |
| S0060 | S0050 | rotamer-finder | copies under difference peaks: the weakest copy takes the peak copy's rotamer | 0.1487 |  | 0.0860 | 0.0627 | 3.0 | - | REFUSE |
| S0061 | S0050 | refinement | restraint weights wc 0.3 wu 0.25 against 1 1 | 0.1475 |  | 0.0806 | 0.0668 | 6.8 | - | ACCEPT |
| S0062 | S0061 | refinement | 20 macro-cycles against 10 | 0.1500 |  | 0.0831 | 0.0669 | 8.1 | - | REFUSE |
| S0063 | S0061 | refinement | water ADPs anisotropic (individual, next to the group B factors of the protein) | 0.1501 |  | 0.0712 | 0.0789 | 7.7 | - | REFUSE |
| S0064 | S0061 | solvent | waters at 4.0 sigma, mode single | 0.1495 |  | 0.0828 | 0.0666 | 7.9 | - | REFUSE |
| S0065 | S0061 | refinement | 20 macro-cycles against 10 | 0.1500 |  | 0.0831 | 0.0669 | 8.1 | - | REFUSE |
