# 3QUE: every step of run T9884ae (the gate's facts lines)

R-free and R-work are the gate's numbers after the step (the candidate's median seed; for a refused step, the refused candidate). σ is the margin against the parent as written in the facts line; the verdict is against the control.

| step | parent | worker | change | R-free | σ | R-work | gap | clash | waters | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| S0000 | - | preprocessing | deposited model, anonymised, scored on the run's working data | 0.2901 |  | 0.2231 | 0.0670 | 10.6 | - | INIT |
| S0001 | S0000 | preprocessing | phenix.refine 10 cycles, sites + ADP + water occupancies, ordered solvent, nqh_flips off, 3 seeds; the median seed | 0.2853 |  | 0.1895 | 0.0958 | 10.4 | - | INIT |
| S0002 | S0001 | refinement | the deposited model has no TLS group | 0.2853 |  | 0.1895 | 0.0958 | 10.4 | - | REFUSE |
| S0003 | S0001 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2840 |  | 0.1810 | 0.1030 | 9.7 | - | REFUSE |
| S0004 | S0001 | refinement | riding hydrogens added (phenix.ready_set, else mmtbx.reduce2); the control has none | 0.3003 |  | 0.1781 | 0.1222 | 9.5 | - | REFUSE |
| S0005 | S0001 | refinement | no anisotropic protein atom in the model in force | 0.2853 |  | 0.1895 | 0.0958 | 10.4 | - | REFUSE |
| S0006 | S0001 | refinement | TLS, 1 group (one for each protein chain) | 0.2815 |  | 0.1850 | 0.0966 | 9.2 | - | REFUSE |
| S0007 | S0001 | refinement | restraint weights wc 1 wu 1 against 0.5 1 | 0.2843 |  | 0.1893 | 0.0950 | 6.9 | - | REFUSE |
| S0008 | S0001 | refinement | restraint weights wc 0.3 wu 0.25 against 0.5 1 | 0.3002 |  | 0.1704 | 0.1298 | 13.9 | - | REFUSE |
| S0009 | S0001 | refinement | one protein chain: no NCS | 0.2853 |  | 0.1895 | 0.0958 | 10.4 | - | REFUSE |
| S0010 | S0001 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2840 |  | 0.1810 | 0.1030 | 9.7 | - | REFUSE |
| S0011 | S0001 | refinement | water ADPs anisotropic | 0.2890 |  | 0.1844 | 0.1045 | 7.9 | - | REFUSE |
| S0012 | S0001 | solvent | waters at 4.0 sigma, mode single | 0.2936 |  | 0.1794 | 0.1142 | 8.8 | - | REFUSE |
| S0013 | S0001 | solvent | waters at 3.0 sigma, mode single | 0.3025 |  | 0.1830 | 0.1195 | 11.1 | - | REFUSE |
| S0014 | S0001 | solvent | waters at 2.5 sigma, mode single | 0.3150 |  | 0.1801 | 0.1349 | 12.5 | - | REFUSE |
| S0015 | S0001 | refinement | water ADPs anisotropic | 0.2890 |  | 0.1844 | 0.1045 | 7.9 | - | REFUSE |
| S0016 | S0001 | refinement | 20 macro-cycles against 10 | 0.2843 |  | 0.1809 | 0.1034 | 8.6 | - | REFUSE |
| S0017 | S0001 | refinement | altloc occupancies refined | 0.2872 |  | 0.1810 | 0.1063 | 9.2 | - | REFUSE |
| S0018 | S0001 | solvent | waters at 2.5 sigma, mode single | 0.3150 |  | 0.1801 | 0.1349 | 12.5 | - | REFUSE |
| S0019 | S0001 | rotamer-finder | Coot auto-fit rotamers on the residues under the strongest difference peaks | 0.2856 |  | 0.1809 | 0.1047 | 9.7 | - | REFUSE |
| S0020 | S0001 | solvent | the model in force is not a C-copy ensemble | 0.2853 |  | 0.1895 | 0.0958 | 10.4 | - | REFUSE |
| S0021 | S0001 | rotamer-finder | the model in force is not a C-copy ensemble | 0.2853 |  | 0.1895 | 0.0958 | 10.4 | - | REFUSE |
| S0022 | S0001 | refinement | 20 macro-cycles against 10 | 0.2843 |  | 0.1809 | 0.1034 | 8.6 | - | REFUSE |
| S0023 | S0001 | solvent | waters below 1.0 sigma in the work-only 2mFo-DFc map removed | 0.2926 |  | 0.1877 | 0.1049 | 10.4 | - | REFUSE |
| S0024 | S0001 | solvent | water clash cleanup | 0.2938 |  | 0.1872 | 0.1067 | 9.2 | - | REFUSE |
| S0025 | S0001 | refinement | TLS, 3 groups (phenix.find_tls_groups) | 0.2769 |  | 0.1802 | 0.0967 | 8.6 | - | REFUSE |
| S0026 | S0001 | refinement | restraint weights wc 0.5 wu 0.5 against 0.5 1 | 0.2856 |  | 0.1764 | 0.1092 | 8.8 | - | REFUSE |
| S0027 | S0001 | refinement | TLS, 3 groups (phenix.find_tls_groups) | 0.2769 |  | 0.1802 | 0.0967 | 8.6 | - | ACCEPT |
| S0028 | S0001 | refinement | restraint weights wc 0.5 wu 2 against 0.5 1 | 0.2910 |  | 0.1890 | 0.1021 | 8.5 | - | REFUSE |
| S0029 | S0027 | refinement | TLS, 4 groups (phenix.find_tls_groups) against the standing 3 group(s) | 0.2802 |  | 0.1817 | 0.0985 | 7.9 | - | REFUSE |
| S0030 | S0027 | refinement | restraint weights wc 0.4 wu 1 against 0.5 1 | 0.2830 |  | 0.1824 | 0.1006 | 9.5 | - | REFUSE |
| S0031 | S0027 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2775 |  | 0.1817 | 0.0959 | 7.6 | - | REFUSE |
| S0032 | S0027 | rotamer-finder | 2 copies from qfit, riding H, 20 macro-cycles | 0.3237 |  | 0.1757 | 0.1480 | 21.9 | - | BUILD |
| S0033 | S0027 | refinement | 20 macro-cycles against 10 | 0.2782 |  | 0.1821 | 0.0961 | 7.9 | - | REFUSE |
| S0034 | S0027 | refinement | restraint weights wc 2 wu 2 against 0.5 1 | 0.2721 |  | 0.1970 | 0.0751 | 5.5 | - | ACCEPT |
| S0035 | S0034 | refinement | restraint weights wc 3 wu 3 against 2 2 | 0.2730 |  | 0.2031 | 0.0699 | 4.2 | - | REFUSE |
| S0036 | S0034 | refinement | restraint weights wc 0.5 wu 2 against 2 2 | 0.2823 |  | 0.1864 | 0.0959 | 7.6 | - | REFUSE |
| S0037 | S0034 | refinement | secondary-structure restraints and Ramachandran restraints against none (the low-resolution restraints) | 0.2700 |  | 0.1973 | 0.0728 | 4.9 | - | REFUSE |
| S0038 | S0034 | refinement | 1 group B factor for each residue (strategy group_adp) against individual ADPs | 0.2839 |  | 0.2062 | 0.0778 | 5.3 | - | REFUSE |
| S0039 | S0034 | refinement | 2 group B factors (main chain, side chain) for each residue (strategy group_adp) against individual ADPs | 0.2835 |  | 0.2056 | 0.0779 | 5.1 | - | REFUSE |
| S0040 | S0034 | refinement | rotamer restraints (side-chain torsions restrained to the nearest rotamer, refinement.main.rotamer_restraints) against none | 0.2801 |  | 0.2111 | 0.0690 | 8.8 | - | REFUSE |
| S0041 | S0034 | rotamer-finder | Coot auto-fit rotamers on the rotamer outliers (phenix.rotalyze) | 0.2705 |  | 0.1958 | 0.0748 | 4.9 | - | ACCEPT |
| S0042 | S0041 | rotamer-finder | Coot auto-fit rotamers on the rotamer outliers (phenix.rotalyze) | 0.2696 |  | 0.1956 | 0.0739 | 4.0 | - | REFUSE |
| S0043 | S0041 | refinement | TLS, 4 groups (phenix.find_tls_groups) against the standing 3 group(s) | 0.2717 |  | 0.1957 | 0.0760 | 4.9 | - | REFUSE |
| S0044 | S0041 | refinement | restraint weights wc 1 wu 1 against 2 2 | 0.2725 |  | 0.1869 | 0.0856 | 6.3 | - | REFUSE |
| S0045 | S0041 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2705 |  | 0.1967 | 0.0738 | 4.8 | - | REFUSE |
| S0046 | S0041 | refinement | 20 macro-cycles against 10 | 0.2699 |  | 0.1953 | 0.0747 | 4.6 | - | REFUSE |
| S0047 | S0041 | refinement | simulated annealing (Cartesian) in the candidate's refinement against the recipe without it | 0.2880 |  | 0.2021 | 0.0859 | 4.8 | - | REFUSE |
| S0048 | S0041 | refinement | simulated annealing (torsion-angle) in the candidate's refinement against the recipe without it | 0.2732 |  | 0.1945 | 0.0787 | 8.5 | - | REFUSE |
| S0049 | S0041 | refinement | 20 macro-cycles against 10 | 0.2699 |  | 0.1953 | 0.0747 | 4.6 | - | REFUSE |
| S0050 | S0041 | refinement | bulk-solvent mask radii optimised (refinement.main.optimize_mask) against the fixed defaults | 0.2710 |  | 0.1971 | 0.0739 | 4.6 | - | REFUSE |
| S0051 | S0041 | refinement | riding hydrogens added (phenix.ready_set, else mmtbx.reduce2); the control has none | 0.2760 |  | 0.1855 | 0.0905 | 1.9 | - | REFUSE |
| S0052 | S0041 | refinement | secondary-structure restraints and Ramachandran restraints against none (the low-resolution restraints) | 0.2685 |  | 0.1963 | 0.0723 | 4.8 | - | ACCEPT |
| S0053 | S0052 | rotamer-finder | Coot auto-fit rotamers on the rotamer outliers (phenix.rotalyze) | 0.2700 |  | 0.1968 | 0.0733 | 5.3 | - | REFUSE |
| S0054 | S0052 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2706 |  | 0.1958 | 0.0748 | 5.5 | - | REFUSE |
| S0055 | S0052 | refinement | 20 macro-cycles against 10 | 0.2712 |  | 0.1953 | 0.0759 | 5.1 | - | REFUSE |
| S0056 | S0052 | refinement | the occupancy of each ligand, ion and buffer molecule refined as one group (waters as before) against the recipe (held at their values) | 0.2722 |  | 0.1971 | 0.0751 | 5.3 | - | REFUSE |
| S0057 | S0052 | refinement | reference-model torsion restraints to reference_model.pdb (phenix reference_model, sigma 1.0, limit 15; the sequences aligned by phenix) against none | 0.2642 |  | 0.2124 | 0.0518 | 6.3 | - | ACCEPT |
| S0058 | S0057 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2650 |  | 0.2147 | 0.0503 | 5.5 | - | REFUSE |
| S0059 | S0057 | rotamer-finder | Coot auto-fit rotamers on the rotamer outliers (phenix.rotalyze) | 0.2654 |  | 0.2150 | 0.0505 | 6.5 | - | REFUSE |
| S0060 | S0057 | refinement | 20 macro-cycles against 10 | 0.2641 |  | 0.2167 | 0.0474 | 5.8 | - | REFUSE |
| S0061 | S0057 | solvent | waters at 4.0 sigma, mode single | 0.2698 |  | 0.2142 | 0.0556 | 6.2 | - | REFUSE |
| S0062 | S0057 | solvent | waters at 3.0 sigma, mode single | 0.2725 |  | 0.2088 | 0.0637 | 6.9 | - | REFUSE |
| S0063 | S0057 | refinement | riding hydrogens added (phenix.ready_set, else mmtbx.reduce2); the control has none | 0.2698 |  | 0.2060 | 0.0637 | 3.4 | - | REFUSE |
| S0064 | S0057 | refinement | bulk-solvent mask radii optimised (refinement.main.optimize_mask) against the fixed defaults | 0.2650 |  | 0.2147 | 0.0503 | 5.5 | - | REFUSE |
| S0065 | S0057 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2650 |  | 0.2147 | 0.0503 | 5.5 | - | REFUSE |
| S0066 | S0057 | refinement | 20 macro-cycles against 10 | 0.2641 |  | 0.2167 | 0.0474 | 5.8 | - | REFUSE |
| S0067 | S0057 | refinement | restraint weights wc 1 wu 1 against 2 2 | 0.2632 |  | 0.1997 | 0.0635 | 6.0 | - | REFUSE |
| S0068 | S0057 | refinement | restraint weights wc 3 wu 3 against 2 2 | 0.2670 |  | 0.2245 | 0.0425 | 6.9 | - | REFUSE |
| S0069 | S0057 | refinement | restraint weights wc 2 wu 4 against 2 2 | 0.2683 |  | 0.2194 | 0.0489 | 5.5 | - | REFUSE |
| S0070 | S0057 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2650 |  | 0.2147 | 0.0503 | 5.5 | - | REFUSE |
