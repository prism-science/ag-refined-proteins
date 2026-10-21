# 9ARN: every step of run Tba97f6 (the gate's facts lines)

R-free and R-work are the gate's numbers after the step (the candidate's median seed; for a refused step, the refused candidate). σ is the margin against the parent as written in the facts line; the verdict is against the control.

| step | parent | worker | change | R-free | σ | R-work | gap | clash | waters | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| S0000 | - | preprocessing | deposited model, anonymised, scored on the run's working data | 0.2944 |  | 0.2542 | 0.0402 | 1.6 | - | INIT |
| S0001 | S0000 | preprocessing | phenix.refine 10 cycles, sites + ADP + water occupancies, ordered solvent, nqh_flips off, 3 seeds; the median seed | 0.2970 |  | 0.2346 | 0.0624 | 3.2 | - | INIT |
| S0002 | S0000 | refinement | water ADPs anisotropic | 0.2955 |  | 0.2470 | 0.0485 | 3.2 | - | ACCEPT |
| S0003 | S0000 | solvent | waters at 4.0 sigma, mode single | 0.3018 |  | 0.2354 | 0.0664 | 4.0 | - | REFUSE |
| S0004 | S0000 | solvent | waters at 3.0 sigma, mode single | 0.3072 |  | 0.2347 | 0.0726 | 4.0 | - | REFUSE |
| S0005 | S0000 | solvent | waters at 2.5 sigma, mode single | 0.3188 |  | 0.2349 | 0.0839 | 4.0 | - | REFUSE |
| S0006 | S0000 | refinement | water ADPs anisotropic | 0.2955 |  | 0.2470 | 0.0485 | 3.2 | - | ACCEPT |
| S0007 | S0000 | refinement | restraint weights wc 0.3 wu 0.25 against 0.5 1 | 0.3070 |  | 0.2275 | 0.0795 | 4.0 | - | REFUSE |
| S0008 | S0000 | refinement | 20 macro-cycles against 10 | 0.3103 |  | 0.2388 | 0.0716 | 2.4 | - | REFUSE |
| S0009 | S0000 | refinement | altloc occupancies refined | 0.3100 |  | 0.2350 | 0.0750 | 2.4 | - | REFUSE |
| S0010 | S0000 | solvent | waters at 2.5 sigma, mode single | 0.3188 |  | 0.2349 | 0.0839 | 4.0 | - | REFUSE |
| S0011 | S0000 | rotamer-finder | no rotamer fit raised the residue CC by 0.02 | 0.2944 |  | 0.2542 | 0.0402 | 1.6 | - | REFUSE |
| S0012 | S0000 | solvent | the model in force is not a C-copy ensemble | 0.2944 |  | 0.2542 | 0.0402 | 1.6 | - | REFUSE |
| S0013 | S0000 | rotamer-finder | the model in force is not a C-copy ensemble | 0.2944 |  | 0.2542 | 0.0402 | 1.6 | - | REFUSE |
| S0014 | S0000 | refinement | 20 macro-cycles against 10 | 0.3103 |  | 0.2388 | 0.0716 | 2.4 | - | REFUSE |
| S0015 | S0000 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.3039 |  | 0.2326 | 0.0714 | 4.0 | - | REFUSE |
| S0016 | S0000 | refinement | riding hydrogens added (phenix.ready_set, else mmtbx.reduce2); the control has none | 0.3025 |  | 0.2290 | 0.0736 | 3.2 | - | REFUSE |
| S0017 | S0000 | refinement | protein ADPs isotropic (anisotropic before) | 0.3185 |  | 0.2657 | 0.0528 | 3.2 | - | REFUSE |
| S0018 | S0000 | refinement | TLS, 1 group (one for each protein chain) | 0.3069 |  | 0.2603 | 0.0466 | 4.0 | - | REFUSE |
| S0019 | S0000 | refinement | restraint weights wc 0.3 wu 0.25 against 0.5 1 | 0.3070 |  | 0.2275 | 0.0795 | 4.0 | - | REFUSE |
| S0020 | S0000 | refinement | one protein chain: no NCS | 0.2944 |  | 0.2542 | 0.0402 | 1.6 | - | REFUSE |
| S0021 | S0000 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.3039 |  | 0.2326 | 0.0714 | 4.0 | - | REFUSE |
| S0022 | S0000 | rotamer-finder | 2 copies from shake, riding H, 20 macro-cycles | 0.3174 |  | 0.2321 | 0.0854 | 13.8 | - | BUILD |
| S0023 | S0000 | solvent | waters at 4.0 sigma, mode single | 0.3018 |  | 0.2354 | 0.0664 | 4.0 | - | REFUSE |
| S0024 | S0000 | solvent | waters at 3.0 sigma, mode single | 0.3072 |  | 0.2347 | 0.0726 | 4.0 | - | REFUSE |
| S0025 | S0000 | solvent | waters at 2.5 sigma, mode single | 0.3188 |  | 0.2349 | 0.0839 | 4.0 | - | REFUSE |
| S0026 | S0000 | refinement | water ADPs anisotropic | 0.2955 |  | 0.2470 | 0.0485 | 3.2 | - | ACCEPT |
| S0027 | S0000 | refinement | altloc occupancies refined | 0.3100 |  | 0.2350 | 0.0750 | 2.4 | - | REFUSE |
| S0028 | S0000 | refinement | 20 macro-cycles against 10 | 0.3103 |  | 0.2388 | 0.0716 | 2.4 | - | REFUSE |
| S0029 | S0000 | refinement | TLS, 2 groups (the deposited groups), protein ADPs isotropic | 0.3099 |  | 0.2588 | 0.0511 | 4.8 | - | REFUSE |
| S0030 | S0000 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.3039 |  | 0.2326 | 0.0714 | 4.0 | - | REFUSE |
| S0031 | S0000 | refinement | riding hydrogens added (phenix.ready_set, else mmtbx.reduce2); the control has none | 0.3025 |  | 0.2290 | 0.0736 | 3.2 | - | REFUSE |
| S0032 | S0000 | refinement | restraint weights wc 1 wu 1 against 0.5 1 | 0.3032 |  | 0.2357 | 0.0675 | 2.4 | - | REFUSE |
| S0033 | S0000 | refinement | restraint weights wc 0.3 wu 0.25 against 0.5 1 | 0.3070 |  | 0.2275 | 0.0795 | 4.0 | - | REFUSE |
| S0034 | S0000 | refinement | water ADPs anisotropic | 0.2955 |  | 0.2470 | 0.0485 | 3.2 | - | ACCEPT |
| S0035 | S0000 | refinement | 20 macro-cycles against 10 | 0.3103 |  | 0.2388 | 0.0716 | 2.4 | - | REFUSE |
| S0036 | S0000 | solvent | waters below 1.0 sigma in the work-only 2mFo-DFc map removed | 0.3014 |  | 0.2347 | 0.0667 | 4.0 | - | ACCEPT |
| S0037 | S0000 | solvent | no water in an own-conformer clash | 0.2944 |  | 0.2542 | 0.0402 | 1.6 | - | REFUSE |
| S0038 | S0000 | refinement | TLS, 2 groups (phenix.find_tls_groups) | 0.3098 |  | 0.2572 | 0.0527 | 2.4 | - | REFUSE |
| S0039 | S0000 | refinement | restraint weights wc 0.5 wu 0.5 against 0.5 1 | 0.3059 |  | 0.2307 | 0.0752 | 2.4 | - | REFUSE |
| S0040 | S0000 | refinement | restraint weights wc 0.5 wu 2 against 0.5 1 | 0.3027 |  | 0.2391 | 0.0636 | 1.6 | - | REFUSE |
| S0041 | S0000 | refinement | restraint weights wc 0.4 wu 1 against 0.5 1 | 0.3073 |  | 0.2328 | 0.0745 | 3.2 | - | REFUSE |
| S0042 | S0000 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.3039 |  | 0.2326 | 0.0714 | 4.0 | - | REFUSE |
| S0043 | S0000 | refinement | 20 macro-cycles against 10 | 0.3103 |  | 0.2388 | 0.0716 | 2.4 | - | REFUSE |
| S0044 | S0000 | rotamer-finder | 2 copies from qfit, riding H, 20 macro-cycles | 0.3084 |  | 0.2280 | 0.0804 | 8.1 | - | BUILD |
| S0045 | S0000 | rotamer-finder | Coot zone refinement A 0-2 | 0.3049 |  | 0.2388 | 0.0661 | 1.6 | - | REFUSE |
| S0046 | S0000 | rotamer-finder | Coot zone refinement A 30-32 | 0.3054 |  | 0.2391 | 0.0663 | 1.6 | - | REFUSE |
| S0047 | S0000 | rotamer-finder | Coot zone refinement A 21-23 | 0.3032 |  | 0.2379 | 0.0654 | 1.6 | - | REFUSE |
| S0048 | S0000 | refinement | 20 macro-cycles against 10 | 0.3103 |  | 0.2388 | 0.0716 | 2.4 | - | REFUSE |
| S0049 | S0000 | refinement | restraint weights wc 2 wu 2 against 0.5 1 | 0.2992 |  | 0.2423 | 0.0569 | 1.6 | - | ACCEPT |
| S0050 | S0000 | refinement | restraint weights wc 3 wu 3 against 2 2 | 0.3006 |  | 0.2457 | 0.0549 | 1.6 | - | REFUSE |
| S0051 | S0000 | refinement | restraint weights wc 5 wu 5 against 2 2 | 0.3022 |  | 0.2549 | 0.0473 | 0.8 | - | REFUSE |
| S0052 | S0000 | refinement | restraint weights wc 0.5 wu 3 against 2 2 | 0.3019 |  | 0.2404 | 0.0615 | 2.4 | - | REFUSE |
| S0053 | S0000 | refinement | restraint weights wc 0.5 wu 5 against 2 2 | 0.3012 |  | 0.2469 | 0.0543 | 2.4 | - | REFUSE |
| S0054 | S0000 | refinement | 1 group B factor for each residue (strategy group_adp) against individual ADPs | 0.2987 |  | 0.2592 | 0.0395 | 1.6 | - | REFUSE |
| S0055 | S0000 | refinement | 2 group B factors (main chain, side chain) for each residue (strategy group_adp) against individual ADPs | 0.3033 |  | 0.2621 | 0.0412 | 1.6 | - | REFUSE |
| S0056 | S0000 | refinement | secondary-structure restraints and Ramachandran restraints against none (the low-resolution restraints) | 0.2934 |  | 0.2388 | 0.0546 | 2.4 | - | ACCEPT |
| S0057 | S0056 | refinement | 20 macro-cycles against 10 | 0.2987 |  | 0.2442 | 0.0545 | 2.4 | - | REFUSE |
| S0058 | S0056 | refinement | rotamer restraints (side-chain torsions restrained to the nearest rotamer, refinement.main.rotamer_restraints) against none | 0.2985 |  | 0.2529 | 0.0456 | 0.8 | - | REFUSE |
| S0059 | S0056 | solvent | waters below 1.0 sigma in the work-only 2mFo-DFc map removed | 0.2994 |  | 0.2436 | 0.0559 | 2.4 | - | REFUSE |
| S0060 | S0056 | refinement | water ADPs anisotropic | 0.2873 |  | 0.2346 | 0.0527 | 2.4 | - | ACCEPT |
| S0061 | S0060 | refinement | water ADPs anisotropic | 0.2864 |  | 0.2345 | 0.0519 | 2.4 | - | REFUSE |
| S0062 | S0060 | refinement | TLS, 2 groups (phenix.find_tls_groups) | 0.2769 |  | 0.2389 | 0.0380 | 1.6 | - | ACCEPT |
| S0063 | S0062 | refinement | bulk-solvent mask radii optimised (refinement.main.optimize_mask) against the fixed defaults | 0.2813 |  | 0.2397 | 0.0416 | 1.6 | - | REFUSE |
| S0064 | S0062 | refinement | simulated annealing (Cartesian) in the candidate's refinement against the recipe without it | 0.3116 |  | 0.2596 | 0.0520 | 0.8 | - | REFUSE |
| S0065 | S0062 | refinement | protein ADPs isotropic (anisotropic before) | 0.2994 |  | 0.2534 | 0.0459 | 1.6 | - | REFUSE |
| S0066 | S0062 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2813 |  | 0.2397 | 0.0416 | 1.6 | - | REFUSE |
| S0067 | S0062 | refinement | restraint weights wc 1 wu 1 against 2 2 | 0.2797 |  | 0.2369 | 0.0428 | 0.8 | - | REFUSE |
| S0068 | S0062 | solvent | waters at 4.0 sigma, mode single | 0.2827 |  | 0.2393 | 0.0434 | 1.6 | - | REFUSE |
| S0069 | S0062 | refinement | TLS, 2 groups (the deposited groups), protein ADPs isotropic against the standing 2 group(s) | 0.2994 |  | 0.2534 | 0.0459 | 1.6 | - | REFUSE |
| S0070 | S0062 | refinement | 20 macro-cycles against 10 | 0.2861 |  | 0.2451 | 0.0410 | 1.6 | - | REFUSE |
| S0071 | S0062 | solvent | SO4 at the mFo-DFc peaks of 4.0 sigma and above that no atom explains, next to a nitrogen (occupancy 1, a tetrahedron the refinement turns) | 0.2859 |  | 0.2455 | 0.0403 | 1.6 | - | REFUSE |
| S0072 | S0062 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.2813 |  | 0.2397 | 0.0416 | 1.6 | - | REFUSE |
| S0073 | S0062 | solvent | waters at 4.0 sigma, mode single | 0.2827 |  | 0.2393 | 0.0434 | 1.6 | - | REFUSE |
| S0074 | S0062 | refinement | 20 macro-cycles against 10 | 0.2861 |  | 0.2451 | 0.0410 | 1.6 | - | REFUSE |
