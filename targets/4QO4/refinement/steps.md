# 4QO4: every step of run T40560e (the gate's facts lines)

R-free and R-work are the gate's numbers after the step (the candidate's median seed; for a refused step, the refused candidate). σ is the margin against the parent as written in the facts line; the verdict is against the control.

| step | parent | worker | change | R-free | σ | R-work | gap | clash | waters | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| S0000 | - | preprocessing | deposited model, anonymised, scored on the run's working data | 0.3133 |  | 0.2631 | 0.0502 | 16.0 | - | INIT |
| S0001 | S0000 | preprocessing | phenix.refine 10 cycles, sites + ADP + water occupancies, ordered solvent, nqh_flips off, 3 seeds; the median seed | 0.3097 |  | 0.2443 | 0.0654 | 2.6 | - | INIT |
| S0002 | S0001 | refinement | water ADPs anisotropic | 0.3173 |  | 0.2378 | 0.0795 | 2.6 | - | REFUSE |
| S0003 | S0001 | solvent | waters at 4.0 sigma, mode single | 0.3126 |  | 0.2385 | 0.0741 | 3.2 | - | REFUSE |
| S0004 | S0001 | refinement | water ADPs anisotropic | 0.3173 |  | 0.2378 | 0.0795 | 2.6 | - | REFUSE |
| S0005 | S0001 | solvent | waters at 4.0 sigma, mode single | 0.3126 |  | 0.2385 | 0.0741 | 3.2 | - | REFUSE |
| S0006 | S0001 | solvent | waters at 3.0 sigma, mode single | 0.3259 |  | 0.2395 | 0.0864 | 4.5 | - | REFUSE |
| S0007 | S0001 | solvent | waters at 2.5 sigma, mode single | 0.3413 |  | 0.2369 | 0.1043 | 3.9 | - | REFUSE |
| S0008 | S0001 | refinement | water ADPs anisotropic | 0.3173 |  | 0.2378 | 0.0795 | 2.6 | - | REFUSE |
| S0009 | S0001 | refinement | restraint weights wc 0.3 wu 0.25 against 0.5 1 | 0.3025 |  | 0.2348 | 0.0677 | 3.9 | - | ACCEPT |
| S0010 | S0009 | refinement | 20 macro-cycles against 10 | 0.3014 |  | 0.2353 | 0.0662 | 3.2 | - | REFUSE |
| S0011 | S0009 | refinement | altloc occupancies refined | 0.3010 |  | 0.2346 | 0.0663 | 3.2 | - | REFUSE |
| S0012 | S0009 | solvent | waters at 2.5 sigma, mode single | 0.3233 |  | 0.2273 | 0.0960 | 2.6 | - | REFUSE |
| S0013 | S0009 | rotamer-finder | no rotamer fit raised the residue CC by 0.02 | 0.3025 |  | 0.2348 | 0.0677 | 3.9 | - | REFUSE |
| S0014 | S0009 | solvent | the model in force is not a C-copy ensemble | 0.3025 |  | 0.2348 | 0.0677 | 3.9 | - | REFUSE |
| S0015 | S0009 | rotamer-finder | the model in force is not a C-copy ensemble | 0.3025 |  | 0.2348 | 0.0677 | 3.9 | - | REFUSE |
| S0016 | S0009 | refinement | 20 macro-cycles against 10 | 0.3014 |  | 0.2353 | 0.0662 | 3.2 | - | REFUSE |
| S0017 | S0009 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.3016 |  | 0.2342 | 0.0674 | 3.2 | - | ACCEPT |
| S0018 | S0017 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.3008 |  | 0.2347 | 0.0661 | 2.6 | - | REFUSE |
| S0019 | S0017 | refinement | riding hydrogens added (phenix.ready_set, else mmtbx.reduce2); the control has none | 0.3104 |  | 0.2282 | 0.0823 | 5.8 | - | REFUSE |
| S0020 | S0017 | refinement | no anisotropic protein atom in the model in force | 0.3016 |  | 0.2342 | 0.0674 | 3.2 | - | REFUSE |
| S0021 | S0017 | refinement | TLS, 1 group (one for each protein chain) | 0.3000 |  | 0.2255 | 0.0745 | 3.9 | - | REFUSE |
| S0022 | S0017 | refinement | restraint weights wc 0.2 wu 0.25 against 0.3 0.25 | 0.3022 |  | 0.2323 | 0.0699 | 4.5 | - | REFUSE |
| S0023 | S0017 | refinement | one protein chain: no NCS | 0.3016 |  | 0.2342 | 0.0674 | 3.2 | - | REFUSE |
| S0024 | S0017 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.3008 |  | 0.2347 | 0.0661 | 2.6 | - | REFUSE |
| S0025 | S0017 | refinement | 20 macro-cycles against 10 | 0.3045 |  | 0.2357 | 0.0688 | 2.6 | - | REFUSE |
| S0026 | S0017 | refinement | restraint weights wc 1 wu 1 against 0.3 0.25 | 0.3187 |  | 0.2446 | 0.0742 | 3.9 | - | REFUSE |
| S0027 | S0017 | solvent | waters below 1.0 sigma in the work-only 2mFo-DFc map removed | 0.3057 |  | 0.2372 | 0.0686 | 3.2 | - | REFUSE |
| S0028 | S0017 | solvent | water clash cleanup | 0.3011 |  | 0.2354 | 0.0657 | 1.9 | - | REFUSE |
| S0029 | S0017 | refinement | TLS, 9 groups (phenix.find_tls_groups) | 0.3094 |  | 0.2248 | 0.0847 | 5.1 | - | REFUSE |
| S0030 | S0017 | refinement | restraint weights wc 0.5 wu 0.5 against 0.3 0.25 | 0.3071 |  | 0.2387 | 0.0684 | 3.9 | - | REFUSE |
| S0031 | S0017 | refinement | restraint weights wc 0.5 wu 2 against 0.3 0.25 | 0.3186 |  | 0.2469 | 0.0717 | 3.9 | - | REFUSE |
| S0032 | S0017 | refinement | restraint weights wc 0.4 wu 1 against 0.3 0.25 | 0.3145 |  | 0.2427 | 0.0718 | 1.9 | - | REFUSE |
| S0033 | S0017 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.3008 |  | 0.2347 | 0.0661 | 2.6 | - | REFUSE |
| S0034 | S0017 | refinement | 20 macro-cycles against 10 | 0.3045 |  | 0.2357 | 0.0688 | 2.6 | - | REFUSE |
| S0035 | S0017 | rotamer-finder | 2 copies from qfit, riding H, 20 macro-cycles | 0.3136 |  | 0.1985 | 0.1151 | 24.7 | - | BUILD |
| S0036 | S0017 | rotamer-finder | Coot zone refinement A 43-45 | 0.3021 |  | 0.2346 | 0.0675 | 3.2 | - | REFUSE |
| S0037 | S0017 | rotamer-finder | Coot zone refinement A 104-106 | 0.3017 |  | 0.2343 | 0.0674 | 3.2 | - | REFUSE |
| S0038 | S0017 | rotamer-finder | Coot zone refinement A 77-79 | 0.3015 |  | 0.2342 | 0.0673 | 3.2 | - | REFUSE |
| S0039 | S0017 | refinement | 20 macro-cycles against 10 | 0.3045 |  | 0.2357 | 0.0688 | 2.6 | - | REFUSE |
| S0040 | S0017 | refinement | bulk-solvent mask radii optimised (refinement.main.optimize_mask) against the fixed defaults | 0.3027 |  | 0.2347 | 0.0679 | 2.6 | - | REFUSE |
| S0041 | S0017 | refinement | restraint weights wc 1 wu 1 against 0.3 0.25 | 0.3187 |  | 0.2446 | 0.0742 | 3.9 | - | REFUSE |
| S0042 | S0017 | refinement | altloc occupancies refined | 0.3038 |  | 0.2351 | 0.0687 | 2.6 | - | REFUSE |
| S0043 | S0017 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.3008 |  | 0.2347 | 0.0661 | 2.6 | - | REFUSE |
| S0044 | S0017 | refinement | 20 macro-cycles against 10 | 0.3045 |  | 0.2357 | 0.0688 | 2.6 | - | REFUSE |
| S0045 | S0017 | rotamer-finder | no rotamer fit raised the residue CC by 0.02 | 0.3016 |  | 0.2342 | 0.0674 | 3.2 | - | REFUSE |
| S0046 | S0017 | refinement | 20 macro-cycles against 10 | 0.3045 |  | 0.2357 | 0.0688 | 2.6 | - | REFUSE |
| S0047 | S0017 | refinement | simulated annealing (Cartesian) in the candidate's refinement against the recipe without it | 0.3042 |  | 0.2361 | 0.0681 | 1.9 | - | REFUSE |
| S0048 | S0017 | refinement | simulated annealing (torsion-angle) in the candidate's refinement against the recipe without it | 0.3071 |  | 0.2359 | 0.0712 | 1.9 | - | REFUSE |
| S0049 | S0017 | refinement | 20 macro-cycles against 10 | 0.3045 |  | 0.2357 | 0.0688 | 2.6 | - | REFUSE |
| S0050 | S0017 | solvent | SO4 at the mFo-DFc peaks of 5.0 sigma and above that no atom explains, next to a nitrogen (occupancy 1, a tetrahedron the refinement turns) | 0.2877 |  | 0.2261 | 0.0616 | 4.4 | - | ACCEPT |
| S0051 | S0050 | solvent | SO4 at the mFo-DFc peaks of 5.0 sigma and above that no atom explains, next to a nitrogen (occupancy 1, a tetrahedron the refinement turns) | 0.2829 |  | 0.2255 | 0.0574 | 5.7 | - | REFUSE |
| S0052 | S0050 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2837 |  | 0.2255 | 0.0582 | 5.7 | - | ACCEPT |
| S0053 | S0052 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2823 |  | 0.2241 | 0.0581 | 5.1 | - | REFUSE |
| S0054 | S0052 | solvent | waters at 4.0 sigma, mode single | 0.2849 |  | 0.2242 | 0.0607 | 4.4 | - | REFUSE |
| S0055 | S0052 | refinement | 20 macro-cycles against 10 | 0.2830 |  | 0.2252 | 0.0578 | 4.4 | - | REFUSE |
| S0056 | S0052 | rotamer-finder | residues 69 to 72 of chain A built by phenix.fit_loops into the work-only 2mFo-DFc map and inserted (the deposited model has none) | 0.2708 |  | 0.2216 | 0.0491 | 7.3 | - | REFUSE |
| S0057 | S0052 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2823 |  | 0.2241 | 0.0581 | 5.1 | - | REFUSE |
| S0058 | S0052 | solvent | waters at 4.0 sigma, mode single | 0.2849 |  | 0.2242 | 0.0607 | 4.4 | - | REFUSE |
| S0059 | S0052 | refinement | 20 macro-cycles against 10 | 0.2830 |  | 0.2252 | 0.0578 | 4.4 | - | REFUSE |
| S0060 | S0052 | rotamer-finder | residues 69 to 72 of chain A built by phenix.fit_loops into the work-only 2mFo-DFc map, their rotamers fitted by Coot and inserted (the deposited model has none) | 0.2773 |  | 0.2244 | 0.0529 | 6.7 | - | REFUSE |
| S0061 | S0052 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2823 |  | 0.2241 | 0.0581 | 5.1 | - | REFUSE |
| S0062 | S0052 | solvent | waters at 4.0 sigma, mode single | 0.2849 |  | 0.2242 | 0.0607 | 4.4 | - | REFUSE |
| S0063 | S0052 | refinement | 20 macro-cycles against 10 | 0.2830 |  | 0.2252 | 0.0578 | 4.4 | - | REFUSE |
| S0064 | S0052 | rotamer-finder | residues 69 to 72 of chain A built by phenix.fit_loops into the work-only 2mFo-DFc map, their rotamers fitted by Coot and inserted (the deposited model has none); a side chain with a correlation under 0.3 cut to CB | 0.2747 |  | 0.2229 | 0.0518 | 7.3 | - | ACCEPT |
| S0065 | S0064 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2741 |  | 0.2217 | 0.0524 | 8.0 | - | REFUSE |
| S0066 | S0064 | solvent | waters at 4.0 sigma, mode single | 0.2749 |  | 0.2225 | 0.0524 | 8.6 | - | REFUSE |
| S0067 | S0064 | refinement | 20 macro-cycles against 10 | 0.2743 |  | 0.2222 | 0.0520 | 7.3 | - | REFUSE |
| S0068 | S0064 | refinement | the occupancy of each ligand, ion and buffer molecule refined as one group (waters as before) against the recipe (held at their values) | 0.2789 |  | 0.2203 | 0.0586 | 7.3 | - | REFUSE |
| S0069 | S0064 | rotamer-finder | 2 copies from qfit, riding H, 20 macro-cycles | 0.2893 |  | 0.1884 | 0.1009 | 20.6 | - | BUILD |
| S0070 | S0064 | rotamer-finder | Coot zone refinement A 42-46 | 0.2745 |  | 0.2237 | 0.0508 | 6.7 | - | REFUSE |
| S0071 | S0064 | rotamer-finder | Coot zone refinement A 77-80 | 0.2739 |  | 0.2223 | 0.0516 | 7.3 | - | REFUSE |
| S0072 | S0064 | rotamer-finder | Coot zone refinement A 108-110 | 0.2746 |  | 0.2241 | 0.0505 | 7.3 | - | REFUSE |
| S0073 | S0064 | rotamer-finder | Coot zone refinement A 54-56 | 0.2742 |  | 0.2242 | 0.0500 | 7.3 | - | REFUSE |
| S0074 | S0064 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2741 |  | 0.2217 | 0.0524 | 8.0 | - | REFUSE |
| S0075 | S0064 | refinement | reference-model torsion restraints to reference_model.pdb (phenix reference_model, sigma 1.0, limit 15; the sequences aligned by phenix) against none | 0.2976 |  | 0.2319 | 0.0657 | 9.2 | - | REFUSE |
| S0076 | S0064 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2741 |  | 0.2217 | 0.0524 | 8.0 | - | REFUSE |
| S0077 | S0064 | refinement | 20 macro-cycles against 10 | 0.2743 |  | 0.2222 | 0.0520 | 7.3 | - | REFUSE |
| S0078 | S0064 | refinement | reference-model torsion restraints to reference_model.pdb (phenix reference_model, sigma 3, limit 15, outliers kept, main chain only; the sequences aligned by phenix) against none | 0.2747 |  | 0.2220 | 0.0527 | 6.7 | - | REFUSE |
| S0079 | S0064 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2741 |  | 0.2217 | 0.0524 | 8.0 | - | REFUSE |
