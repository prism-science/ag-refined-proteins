# 3TC7: every step of run T431c8e_nqh (the gate's facts lines)

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
| S0066 | S0061 | refinement | restraint weights wc 0.2 wu 0.25 against 0.3 0.25 | 0.1493 |  | 0.0810 | 0.0684 | 10.3 | - | REFUSE |
| S0067 | S0061 | refinement | restraint weights wc 0.3 wu 0.1 against 0.3 0.25 | 0.1494 |  | 0.0826 | 0.0667 | 7.7 | - | REFUSE |
| S0068 | S0061 | refinement | restraint weights wc 0.5 wu 0.5 against 0.3 0.25 | 0.1497 |  | 0.0849 | 0.0648 | 5.5 | - | REFUSE |
| S0069 | S0061 | refinement | restraint weights wc 0.2 wu 0.1 against 0.3 0.25 | 0.1493 |  | 0.0810 | 0.0684 | 10.3 | - | REFUSE |
| S0070 | S0061 | refinement | bulk-solvent mask radii optimised (refinement.main.optimize_mask) against the fixed defaults | 0.1495 |  | 0.0821 | 0.0673 | 8.3 | - | REFUSE |
| S0071 | S0061 | refinement | the groups are the standing groups | 0.1475 |  | 0.0806 | 0.0668 | 6.8 | - | REFUSE |
| S0072 | S0061 | solvent | waters at 3.5 sigma, mode single | 0.1500 |  | 0.0825 | 0.0675 | 7.8 | - | REFUSE |
| S0073 | S0061 | solvent | waters at 3.5 sigma, mode single | 0.1500 |  | 0.0825 | 0.0675 | 7.8 | - | REFUSE |
| S0074 | S0061 | solvent | waters at 3.0 sigma, mode single | 0.1528 |  | 0.0823 | 0.0705 | 8.1 | - | REFUSE |
| S0075 | S0061 | solvent | waters at 3.0 sigma, mode single | 0.1528 |  | 0.0823 | 0.0705 | 8.1 | - | REFUSE |
| S0076 | S0061 | solvent | waters at 2.5 sigma, mode single | 0.1546 |  | 0.0810 | 0.0736 | 7.3 | - | REFUSE |
| S0077 | S0061 | solvent | waters at 2.0 sigma, mode single | 0.1570 |  | 0.0796 | 0.0773 | 7.5 | - | REFUSE |
| S0078 | S0061 | refinement | altloc occupancies refined | 0.1493 |  | 0.0825 | 0.0668 | 7.7 | - | REFUSE |
| S0079 | S0061 | rotamer-finder | no rotamer fit raised the residue CC by 0 | 0.1475 |  | 0.0806 | 0.0668 | 6.8 | - | REFUSE |
| S0080 | S0061 | solvent | waters in own-copy clashes moved to a copy they clear; nothing deleted | 0.1493 |  | 0.0826 | 0.0667 | 7.2 | - | REFUSE |
| S0081 | S0061 | rotamer-finder | copies under difference peaks: the weakest copy takes the peak copy's rotamer | 0.1501 |  | 0.0826 | 0.0675 | 7.8 | - | REFUSE |
| S0082 | S0061 | rotamer-finder | waters in protein density deleted (own-copy clashes and other-copy density with occupancy above 1.5/C); Coot rotamer fit and real-space refinement of each copy of the residues next to them | 0.1550 |  | 0.0900 | 0.0650 | 8.0 | - | REFUSE |
| S0083 | S0061 | rotamer-finder | waters in protein density deleted (own-copy clashes and other-copy density with occupancy above 1.5/C) | 0.1562 |  | 0.0911 | 0.0651 | 7.2 | - | REFUSE |
| S0084 | S0061 | rotamer-finder | Coot rotamer fit and real-space refinement of each copy of the residues with an atom beyond +-3.5 sigma in the work-only mFo-DFc map | 0.1493 |  | 0.0825 | 0.0668 | 9.0 | - | REFUSE |
| S0085 | S0061 | refinement | restraint weights wc 1 wu 1 against 0.3 0.25 | 0.1505 |  | 0.0884 | 0.0621 | 3.0 | - | REFUSE |
| S0086 | S0061 | rotamer-finder | Coot rotamer fit and real-space refinement of each copy of the residues with an atom beyond +-3.5 sigma in the work-only mFo-DFc map; the counted waters that a moved side chain overlaps deleted | 0.1498 |  | 0.0847 | 0.0652 | 7.4 | - | ACCEPT |
| S0087 | S0086 | rotamer-finder | waters in protein density deleted (own-copy clashes and other-copy density with occupancy above 1.5/C); Coot rotamer fit and real-space refinement of each copy of the residues next to them | 0.1611 |  | 0.0962 | 0.0649 | 10.1 | - | REFUSE |
| S0088 | S0086 | rotamer-finder | Coot rotamer fit and real-space refinement of each copy of the residues with an atom beyond +-3.5 sigma in the work-only mFo-DFc map; the counted waters that a moved side chain overlaps deleted | 0.1521 |  | 0.0881 | 0.0640 | 8.2 | - | REFUSE |
| S0089 | S0086 | solvent | waters in own-copy clashes moved to a copy they clear; nothing deleted | 0.1516 |  | 0.0856 | 0.0660 | 7.7 | - | REFUSE |
| S0090 | S0086 | solvent | waters at 3.0 sigma, mode single | 0.1526 |  | 0.0845 | 0.0681 | 8.2 | - | REFUSE |
| S0091 | S0086 | refinement | water ADPs anisotropic (individual, next to the group B factors of the protein) | 0.1572 |  | 0.0761 | 0.0811 | 8.2 | - | REFUSE |
| S0092 | S0086 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.1515 |  | 0.0855 | 0.0661 | 8.6 | - | REFUSE |
| S0093 | S0086 | rotamer-finder | waters in protein density deleted (own-copy clashes and other-copy density with occupancy above 1.5/C); Coot rotamer fit and real-space refinement of each copy of the residues next to them | 0.1614 |  | 0.0963 | 0.0651 | 10.0 | - | REFUSE |
| S0094 | S0086 | rotamer-finder | Coot rotamer fit and real-space refinement of each copy of the residues with an atom beyond +-3.5 sigma in the work-only mFo-DFc map; the counted waters that a moved side chain overlaps deleted | 0.1519 |  | 0.0881 | 0.0639 | 8.3 | - | REFUSE |
| S0095 | S0086 | solvent | no peak at 6.0 sigma on a lettered water or in open solvent | 0.1498 |  | 0.0847 | 0.0652 | 7.4 | - | REFUSE |
| S0096 | S0086 | rotamer-finder | Coot rotamer fit and real-space refinement of each copy of the residues with an atom beyond +-3.5 sigma in the work-only mFo-DFc map; the counted waters that a moved side chain overlaps deleted | 0.1518 |  | 0.0875 | 0.0643 | 8.5 | - | REFUSE |
| S0097 | S0086 | rotamer-finder | no protein atom whose copy B-factors differ by more than 3 times | 0.1498 |  | 0.0847 | 0.0652 | 7.4 | - | REFUSE |
| S0098 | S0086 | solvent | waters at 3.0 sigma, mode single, none within 2.6 A of a protein atom of any copy | 0.1526 |  | 0.0854 | 0.0672 | 8.4 | - | REFUSE |
| S0099 | S0086 | solvent | waters at 2.5 sigma, mode single, none within 2.6 A of a protein atom of any copy | 0.1529 |  | 0.0845 | 0.0684 | 7.9 | - | REFUSE |
| S0100 | S0086 | refinement | water ADPs anisotropic (individual, next to the group B factors of the protein) | 0.1572 |  | 0.0761 | 0.0811 | 8.2 | - | REFUSE |
| S0101 | S0086 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.1515 |  | 0.0855 | 0.0661 | 8.6 | - | REFUSE |
| S0102 | S0086 | solvent | no peak at 6.0 sigma on a lettered water or in open solvent | 0.1498 |  | 0.0847 | 0.0652 | 7.4 | - | REFUSE |
| S0103 | S0086 | rotamer-finder | no protein atom whose copy B-factors differ by more than 3 times | 0.1498 |  | 0.0847 | 0.0652 | 7.4 | - | REFUSE |
| S0104 | S0086 | refinement | methionine as selenomethionine in copies A and B of 6 (MET -> MSE, SD -> SE): a selenium fraction of 1/3 for the partial incorporation; the three tallest peaks of the work-only mFo-DFc map (12.0, 11.9, 10.3 sigma) are on the SD atoms; an anomalous group for Se (f' -8 and f'' 4 held: merged F-obs; data at 0.97915 A) against the sulfur model | 0.1498 |  | 0.0873 | 0.0625 | 8.7 | - | ACCEPT |
| S0105 | S0104 | refinement | selenium kept in copy A of Met73, Met109 and Met237 (a fraction of 1/6); copy B of the five methionines and copy A of Met154 and Met200 back to sulfur. At S0104 every SE atom lies in negative mFo-DFc density (-7.7 to -10.5 sigma), and the SD atoms of Met154 and Met200 near 0; the anomalous group (f' -8, f'' 4, held) stays for the SE atoms left | 0.1512 |  | 0.0854 | 0.0658 | 9.2 | - | REFUSE |
| S0106 | S0104 | refinement | selenium kept in copy A of Met73, Met109 and Met237 (a fraction of 1/6); copy B of the five methionines and copy A of Met154 and Met200 back to sulfur. At S0104 every SE atom lies in negative mFo-DFc density (-7.7 to -10.5 sigma), and the SD atoms of Met154 and Met200 near 0; a repair of the deepest point (the fork's check, set before its first step); the same change was refused as an improving step on T431c8e_oct28 (S0105, R-free -1.94 sigma) | 0.1512 |  | 0.0854 | 0.0658 | 9.2 | - | ACCEPT |
| S0107 | S0106 | solvent | no peak at 6.0 sigma on a lettered water or in open solvent | 0.1512 |  | 0.0854 | 0.0658 | 9.2 | - | REFUSE |
| S0108 | S0106 | rotamer-finder | Coot rotamer fit and real-space refinement of each copy of the residues with an atom beyond +-3.5 sigma in the work-only mFo-DFc map; the counted waters that a moved side chain overlaps deleted | 0.1504 |  | 0.0864 | 0.0640 | 9.0 | - | ACCEPT |
| S0109 | S0108 | rotamer-finder | no protein atom whose copy B-factors differ by more than 3 times | 0.1504 |  | 0.0864 | 0.0640 | 9.0 | - | REFUSE |
| S0110 | S0108 | solvent | waters at 3.0 sigma, mode single, none within 2.6 A of a protein atom of any copy | 0.1529 |  | 0.0887 | 0.0642 | 9.1 | - | REFUSE |
| S0111 | S0108 | solvent | waters at 2.5 sigma, mode single, none within 2.6 A of a protein atom of any copy | 0.1547 |  | 0.0877 | 0.0670 | 9.0 | - | REFUSE |
| S0112 | S0108 | refinement | water ADPs anisotropic (individual, next to the group B factors of the protein) | 0.1515 |  | 0.0722 | 0.0792 | 8.4 | - | REFUSE |
| S0113 | S0108 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.1524 |  | 0.0883 | 0.0640 | 9.2 | - | REFUSE |
| S0114 | S0108 | solvent | no peak at 6.0 sigma on a lettered water or in open solvent | 0.1504 |  | 0.0864 | 0.0640 | 9.0 | - | REFUSE |
| S0115 | S0108 | rotamer-finder | no protein atom whose copy B-factors differ by more than 3 times | 0.1504 |  | 0.0864 | 0.0640 | 9.0 | - | REFUSE |
| S0116 | S0108 | refinement | nonbonded restraint weight 300 against the default 100 (the clash term alone; wc and wu unchanged) | 0.1521 |  | 0.0896 | 0.0625 | 3.5 | - | ACCEPT |
| S0117 | S0116 | solvent | nothing to change: lettered waters of one site in every conformer (within 0.5 A of their centroid) merged into one shared water at occupancy 1 | 0.1521 |  | 0.0896 | 0.0625 | 3.5 | - | REFUSE |
| S0118 | S0116 | solvent | nothing to change: lettered waters of one site in every conformer (within 1 A of their centroid) merged into one shared water at occupancy 1 | 0.1521 |  | 0.0896 | 0.0625 | 3.5 | - | REFUSE |
| S0119 | S0116 | rotamer-finder | residues whose conformers lie within 0.5 A RMSD of each other collapsed to one conformer (no letter, occupancy 1) | 0.1582 |  | 0.0952 | 0.0630 | 5.0 | - | REFUSE |
| S0120 | S0116 | rotamer-finder | residues whose conformers lie within 0.75 A RMSD of each other collapsed to one conformer (no letter, occupancy 1) | 0.1742 |  | 0.1200 | 0.0542 | 7.7 | - | REFUSE |
| S0121 | S0116 | rotamer-finder | nothing to change: conformers with side-chain B above 2 x the site median: B to the median, occupancy x (median/B)^1.5, the residue's occupancies renormalised to 1 | 0.1521 |  | 0.0896 | 0.0625 | 3.5 | - | REFUSE |
| S0122 | S0116 | connectivity | connectivity relabel, 10 min effort, Untangler low_compute_clash_resolution | 0.1550 |  | 0.0912 | 0.0639 | 3.5 | - | REFUSE |
| S0123 | S0116 | refinement | nonbonded restraint weight 1000 against 300 (the clash term alone; wc and wu unchanged) | 0.1553 |  | 0.0930 | 0.0623 | 0.8 | - | ACCEPT |
| S0124 | S0123 | rotamer-finder | Coot rotamer fit and real-space refinement of each conformer of the residues in the most repeated MolProbity clash contacts (A13,A17,A114,A142,A172,A160,A217,A221), on the omit maps; a repair on the clashscore | 0.1579 |  | 0.0952 | 0.0627 | 0.7 | - | REFUSE |
