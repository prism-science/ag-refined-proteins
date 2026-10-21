# 1LZ8: every step of run Tee73c5 (the gate's facts lines)

R-free and R-work are the gate's numbers after the step (the candidate's median seed; for a refused step, the refused candidate). σ is the margin against the parent as written in the facts line; the verdict is against the control.

| step | parent | worker | change | R-free | σ | R-work | gap | clash | waters | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| S0000 | - | preprocessing | deposited model, anonymised, scored on the run's working data | 0.2826 |  | 0.2024 | 0.0802 | 5.1 | - | INIT |
| S0001 | S0000 | preprocessing | phenix.refine 10 cycles, sites + ADP + water occupancies, ordered solvent, nqh_flips off, 3 seeds; the median seed | 0.2712 |  | 0.2048 | 0.0664 | 4.1 | - | INIT |
| S0002 | S0001 | refinement | water ADPs anisotropic | 0.2727 |  | 0.1919 | 0.0808 | 4.6 | - | REFUSE |
| S0003 | S0001 | refinement | water ADPs anisotropic | 0.2727 |  | 0.1919 | 0.0808 | 4.6 | - | REFUSE |
| S0004 | S0001 | solvent | waters at 4.0 sigma, mode single | 0.2675 |  | 0.2012 | 0.0663 | 3.6 | - | REFUSE |
| S0005 | S0001 | solvent | waters at 3.0 sigma, mode single | 0.2698 |  | 0.2000 | 0.0699 | 3.6 | - | REFUSE |
| S0006 | S0001 | solvent | waters at 2.5 sigma, mode single | 0.2774 |  | 0.1985 | 0.0789 | 3.6 | - | REFUSE |
| S0007 | S0001 | refinement | water ADPs anisotropic | 0.2727 |  | 0.1919 | 0.0808 | 4.6 | - | REFUSE |
| S0008 | S0001 | refinement | restraint weights wc 0.3 wu 0.25 against 0.5 1 | 0.2638 |  | 0.1950 | 0.0688 | 4.1 | - | REFUSE |
| S0009 | S0001 | refinement | 20 macro-cycles against 10 | 0.2660 |  | 0.2027 | 0.0634 | 4.1 | - | REFUSE |
| S0010 | S0001 | refinement | altloc occupancies refined | 0.2657 |  | 0.2022 | 0.0635 | 4.1 | - | REFUSE |
| S0011 | S0001 | solvent | waters at 2.5 sigma, mode single | 0.2774 |  | 0.1985 | 0.0789 | 3.6 | - | REFUSE |
| S0012 | S0001 | rotamer-finder | no rotamer fit raised the residue CC by 0.02 | 0.2712 |  | 0.2048 | 0.0664 | 4.1 | - | REFUSE |
| S0013 | S0001 | solvent | the model in force is not a C-copy ensemble | 0.2712 |  | 0.2048 | 0.0664 | 4.1 | - | REFUSE |
| S0014 | S0001 | rotamer-finder | the model in force is not a C-copy ensemble | 0.2712 |  | 0.2048 | 0.0664 | 4.1 | - | REFUSE |
| S0015 | S0001 | refinement | 20 macro-cycles against 10 | 0.2660 |  | 0.2027 | 0.0634 | 4.1 | - | REFUSE |
| S0016 | S0001 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2657 |  | 0.2027 | 0.0630 | 4.1 | - | ACCEPT |
| S0017 | S0016 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2652 |  | 0.2022 | 0.0630 | 4.1 | - | REFUSE |
| S0018 | S0016 | refinement | riding hydrogens added (phenix.ready_set, else mmtbx.reduce2); the control has none | 0.2628 |  | 0.1894 | 0.0735 | 5.1 | - | REFUSE |
| S0019 | S0016 | refinement | no anisotropic protein atom in the model in force | 0.2657 |  | 0.2027 | 0.0630 | 4.1 | - | REFUSE |
| S0020 | S0016 | refinement | TLS, 1 group (one for each protein chain) | 0.2599 |  | 0.2039 | 0.0561 | 4.1 | - | ACCEPT |
| S0021 | S0020 | refinement | restraint weights wc 0.3 wu 0.25 against 0.5 1 | 0.2563 |  | 0.1971 | 0.0592 | 5.1 | - | REFUSE |
| S0022 | S0020 | refinement | one protein chain: no NCS | 0.2599 |  | 0.2039 | 0.0561 | 4.1 | - | REFUSE |
| S0023 | S0020 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2599 |  | 0.2051 | 0.0548 | 3.6 | - | REFUSE |
| S0024 | S0020 | refinement | 20 macro-cycles against 10 | 0.2597 |  | 0.2070 | 0.0527 | 4.1 | - | REFUSE |
| S0025 | S0020 | refinement | restraint weights wc 1 wu 1 against 0.5 1 | 0.2600 |  | 0.2055 | 0.0545 | 4.1 | - | REFUSE |
| S0026 | S0020 | solvent | waters below 1.0 sigma in the work-only 2mFo-DFc map removed | 0.2631 |  | 0.2058 | 0.0574 | 2.0 | - | REFUSE |
| S0027 | S0020 | solvent | water clash cleanup | 0.2580 |  | 0.2030 | 0.0551 | 2.6 | - | REFUSE |
| S0028 | S0020 | refinement | TLS, 6 groups (phenix.find_tls_groups) against the standing 1 group(s) | 0.2565 |  | 0.2014 | 0.0551 | 4.1 | - | REFUSE |
| S0029 | S0020 | refinement | restraint weights wc 0.5 wu 0.5 against 0.5 1 | 0.2580 |  | 0.2003 | 0.0577 | 4.6 | - | REFUSE |
| S0030 | S0020 | refinement | restraint weights wc 0.5 wu 2 against 0.5 1 | 0.2591 |  | 0.2058 | 0.0533 | 4.1 | - | REFUSE |
| S0031 | S0020 | refinement | restraint weights wc 0.4 wu 1 against 0.5 1 | 0.2578 |  | 0.2017 | 0.0561 | 4.1 | - | REFUSE |
| S0032 | S0020 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2579 |  | 0.2026 | 0.0554 | 4.6 | - | ACCEPT |
| S0033 | S0032 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2582 |  | 0.2034 | 0.0548 | 4.1 | - | ACCEPT |
| S0034 | S0032 | refinement | 20 macro-cycles against 10 | 0.2588 |  | 0.2043 | 0.0545 | 4.1 | - | REFUSE |
| S0035 | S0032 | rotamer-finder | 2 copies from qfit, riding H, 20 macro-cycles | 0.2482 |  | 0.1618 | 0.0864 | 4.8 | - | BUILD |
| S0036 | S0035 | solvent | waters at 4.0 sigma, mode single | 0.2494 |  | 0.1585 | 0.0909 | 4.8 | - | REFUSE |
| S0037 | S0035 | solvent | waters at 3.0 sigma, mode single | 0.2504 |  | 0.1535 | 0.0969 | 4.1 | - | REFUSE |
| S0038 | S0035 | solvent | waters at 2.5 sigma, mode single | 0.2598 |  | 0.1506 | 0.1092 | 5.6 | - | REFUSE |
| S0039 | S0035 | refinement | water ADPs anisotropic | 0.2528 |  | 0.1533 | 0.0995 | 3.3 | - | REFUSE |
| S0040 | S0035 | refinement | 20 macro-cycles against 10 | 0.2492 |  | 0.1606 | 0.0886 | 4.6 | - | REFUSE |
| S0041 | S0035 | refinement | altloc occupancies refined | 0.2476 |  | 0.1608 | 0.0868 | 3.6 | - | REFUSE |
| S0042 | S0035 | solvent | no clashing water clears another copy | 0.2482 |  | 0.1618 | 0.0864 | 4.8 | - | REFUSE |
| S0043 | S0035 | rotamer-finder | copies under difference peaks: the weakest copy takes the peak copy's rotamer | 0.2510 |  | 0.1606 | 0.0904 | 4.1 | - | REFUSE |
| S0044 | S0035 | refinement | 20 macro-cycles against 10 | 0.2492 |  | 0.1606 | 0.0886 | 4.6 | - | REFUSE |
| S0045 | S0035 | refinement | 20 macro-cycles against 10 | 0.2492 |  | 0.1606 | 0.0886 | 4.6 | - | REFUSE |
| S0046 | S0032 | rotamer-finder | 3 copies from qfit, riding H, 20 macro-cycles | 0.2492 |  | 0.1548 | 0.0944 | 6.0 | - | BUILD |
| S0047 | S0035 | refinement | bulk-solvent mask radii optimised (refinement.main.optimize_mask) against the fixed defaults | 0.2453 |  | 0.1597 | 0.0856 | 4.6 | - | REFUSE |
| S0048 | S0035 | refinement | restraint weights wc 1 wu 1 against 0.5 1 | 0.2450 |  | 0.1633 | 0.0816 | 2.8 | - | REFUSE |
| S0049 | S0035 | refinement | restraint weights wc 0.3 wu 0.25 against 0.5 1 | 0.2548 |  | 0.1565 | 0.0983 | 6.1 | - | REFUSE |
| S0050 | S0035 | refinement | altloc occupancies refined | 0.2476 |  | 0.1608 | 0.0868 | 3.6 | - | REFUSE |
| S0051 | S0035 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2492 |  | 0.1604 | 0.0888 | 4.1 | - | REFUSE |
| S0052 | S0035 | refinement | 20 macro-cycles against 10 | 0.2492 |  | 0.1606 | 0.0886 | 4.6 | - | REFUSE |
| S0053 | S0035 | refinement | restraint weights wc 1 wu 1 against 0.5 1 | 0.2450 |  | 0.1633 | 0.0816 | 2.8 | - | ACCEPT |
| S0054 | S0053 | refinement | restraint weights wc 2 wu 2 against 1 1 | 0.2451 |  | 0.1673 | 0.0777 | 1.0 | - | ACCEPT |
| S0055 | S0053 | solvent | waters at 4.0 sigma, mode single | 0.2449 |  | 0.1646 | 0.0803 | 1.0 | - | REFUSE |
| S0056 | S0053 | solvent | waters at 3.0 sigma, mode single | 0.2463 |  | 0.1597 | 0.0866 | 1.0 | - | REFUSE |
| S0057 | S0053 | solvent | waters at 2.5 sigma, mode single | 0.2525 |  | 0.1571 | 0.0954 | 1.0 | - | REFUSE |
| S0058 | S0053 | refinement | water ADPs anisotropic | 0.2503 |  | 0.1613 | 0.0890 | 1.5 | - | REFUSE |
| S0059 | S0053 | refinement | altloc occupancies refined | 0.2461 |  | 0.1673 | 0.0788 | 1.0 | - | REFUSE |
| S0060 | S0053 | refinement | bulk-solvent mask radii optimised (refinement.main.optimize_mask) against the fixed defaults | 0.2440 |  | 0.1667 | 0.0773 | 0.8 | - | ACCEPT |
| S0061 | S0060 | refinement | 20 macro-cycles against 10 | 0.2428 |  | 0.1676 | 0.0752 | 1.3 | - | REFUSE |
| S0062 | S0060 | refinement | simulated annealing (Cartesian) in the candidate's refinement against the recipe without it | 0.2710 |  | 0.1807 | 0.0903 | 1.8 | - | REFUSE |
| S0063 | S0060 | refinement | simulated annealing (torsion-angle) in the candidate's refinement against the recipe without it | 0.2557 |  | 0.1721 | 0.0836 | 5.9 | - | REFUSE |
| S0064 | S0060 | refinement | 20 macro-cycles against 10 | 0.2428 |  | 0.1676 | 0.0752 | 1.3 | - | REFUSE |
| S0065 | S0060 | refinement | secondary-structure restraints and Ramachandran restraints against none (the low-resolution restraints) | 0.2425 |  | 0.1683 | 0.0742 | 1.3 | - | REFUSE |
| S0066 | S0060 | refinement | 1 group B factor for each residue (strategy group_adp) against individual ADPs | 0.2449 |  | 0.1742 | 0.0708 | 1.0 | - | REFUSE |
| S0067 | S0060 | refinement | 2 group B factors (main chain, side chain) for each residue (strategy group_adp) against individual ADPs | 0.2428 |  | 0.1728 | 0.0700 | 1.3 | - | REFUSE |
| S0068 | S0060 | refinement | TLS, 6 groups (phenix.find_tls_groups) against the standing 1 group(s) | 0.2424 |  | 0.1660 | 0.0763 | 1.3 | - | REFUSE |
| S0069 | S0060 | refinement | restraint weights wc 3 wu 3 against 2 2 | 0.2436 |  | 0.1706 | 0.0730 | 0.5 | - | REFUSE |
| S0070 | S0060 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2427 |  | 0.1671 | 0.0756 | 1.0 | - | ACCEPT |
| S0071 | S0070 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2427 |  | 0.1674 | 0.0754 | 1.0 | - | REFUSE |
| S0072 | S0070 | refinement | 20 macro-cycles against 10 | 0.2450 |  | 0.1679 | 0.0771 | 1.3 | - | REFUSE |
| S0073 | S0070 | solvent | CL at the mFo-DFc peaks of 4.0 sigma and above that no atom explains, next to a nitrogen (occupancy 1) | 0.2408 |  | 0.1662 | 0.0746 | 1.3 | - | ACCEPT |
| S0074 | S0073 | solvent | no peak at 4.0 sigma clear of the model with a nitrogen within 4.5 A | 0.2408 |  | 0.1662 | 0.0746 | 1.3 | - | REFUSE |
| S0075 | S0073 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2434 |  | 0.1665 | 0.0770 | 1.5 | - | REFUSE |
| S0076 | S0073 | solvent | waters at 4.0 sigma, mode single | 0.2422 |  | 0.1656 | 0.0766 | 1.8 | - | REFUSE |
| S0077 | S0073 | refinement | 20 macro-cycles against 10 | 0.2453 |  | 0.1679 | 0.0774 | 1.3 | - | REFUSE |
| S0078 | S0073 | refinement | the occupancy of each ligand, ion and buffer molecule refined as one group (waters as before) against the recipe (held at their values) | 0.2431 |  | 0.1666 | 0.0765 | 1.5 | - | REFUSE |
| S0079 | S0073 | rotamer-finder | 3 copies from shake, riding H, 20 macro-cycles | 0.2563 |  | 0.1620 | 0.0943 | 2.5 | - | BUILD |
| S0080 | S0073 | refinement | reference-model torsion restraints to reference_model.pdb (phenix reference_model, sigma 1.0, limit 15; the sequences aligned by phenix) against none | 0.2434 |  | 0.1665 | 0.0770 | 1.5 | - | REFUSE |
| S0081 | S0073 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2434 |  | 0.1665 | 0.0770 | 1.5 | - | REFUSE |
| S0082 | S0073 | refinement | 20 macro-cycles against 10 | 0.2453 |  | 0.1679 | 0.0774 | 1.3 | - | REFUSE |
