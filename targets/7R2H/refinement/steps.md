# 7R2H: every step of run Ta4f3f9_oct28 (the gate's facts lines)

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
| S0026 | S0019 | solvent | waters in own-copy clashes moved to a copy they clear; nothing deleted | 0.0986 |  | 0.0677 | 0.0309 | 7.1 | - | REFUSE |
| S0027 | S0019 | rotamer-finder | copies under difference peaks: the weakest copy takes the peak copy's rotamer | 0.0987 |  | 0.0679 | 0.0308 | 8.4 | - | REFUSE |
| S0028 | S0019 | refinement | 20 macro-cycles against 10 | 0.0985 |  | 0.0681 | 0.0305 | 8.3 | - | REFUSE |
| S0029 | S0019 | refinement | restraint weights wc 1 wu 1 against 0.3 0.25 | 0.1001 |  | 0.0736 | 0.0265 | 6.5 | - | REFUSE |
| S0030 | S0019 | refinement | protein ADPs isotropic (anisotropic before) | 0.0980 |  | 0.0743 | 0.0237 | 8.0 | - | ACCEPT |
| S0031 | S0030 | refinement | 1 group B factor for each residue (strategy group_adp) against individual ADPs | 0.0969 |  | 0.0734 | 0.0235 | 8.8 | - | REFUSE |
| S0032 | S0030 | refinement | TLS, 1 group (one for each protein chain) | 0.0965 |  | 0.0707 | 0.0257 | 9.1 | - | ACCEPT |
| S0033 | S0032 | solvent | waters at 4.0 sigma, mode single | 0.0966 |  | 0.0701 | 0.0265 | 9.2 | - | REFUSE |
| S0034 | S0032 | solvent | waters at 3.0 sigma, mode single | 0.0964 |  | 0.0697 | 0.0268 | 9.7 | - | REFUSE |
| S0035 | S0032 | solvent | waters at 2.5 sigma, mode single | 0.0962 |  | 0.0691 | 0.0271 | 9.7 | - | ACCEPT |
| S0036 | S0035 | solvent | waters at 2.5 sigma, mode single | 0.0977 |  | 0.0696 | 0.0282 | 9.8 | - | REFUSE |
| S0037 | S0035 | solvent | waters at 2.0 sigma, mode single | 0.0970 |  | 0.0676 | 0.0294 | 9.6 | - | ACCEPT |
| S0038 | S0035 | refinement | water ADPs anisotropic | 0.0970 |  | 0.0699 | 0.0272 | 8.6 | - | REFUSE |
| S0039 | S0035 | refinement | 20 macro-cycles against 10 | 0.0975 |  | 0.0704 | 0.0271 | 9.9 | - | REFUSE |
| S0040 | S0035 | refinement | altloc occupancies refined | 0.0975 |  | 0.0700 | 0.0275 | 9.3 | - | REFUSE |
| S0041 | S0035 | solvent | waters at 2.5 sigma, mode single | 0.0977 |  | 0.0696 | 0.0282 | 9.8 | - | REFUSE |
| S0042 | S0035 | rotamer-finder | no rotamer fit raised the residue CC by 0.02 | 0.0962 |  | 0.0691 | 0.0271 | 9.7 | - | REFUSE |
| S0043 | S0035 | solvent | waters in own-copy clashes moved to a copy they clear; nothing deleted | 0.0976 |  | 0.0700 | 0.0276 | 8.2 | - | ACCEPT |
| S0044 | S0035 | rotamer-finder | copies under difference peaks: the weakest copy takes the peak copy's rotamer | 0.0973 |  | 0.0691 | 0.0282 | 10.0 | - | REFUSE |
| S0045 | S0035 | refinement | 20 macro-cycles against 10 | 0.0975 |  | 0.0704 | 0.0271 | 9.9 | - | REFUSE |
| S0046 | S0035 | rotamer-finder | 8 copies from 6 (the first 2 duplicated), waters kept, 20 macro-cycles | 0.0976 |  | 0.0703 | 0.0274 | 9.6 | - | BUILD |
| S0047 | S0046 | solvent | waters at 4.0 sigma, mode single | 0.0977 |  | 0.0691 | 0.0286 | 9.9 | - | REFUSE |
| S0048 | S0046 | solvent | waters at 3.0 sigma, mode single | 0.0981 |  | 0.0691 | 0.0289 | 10.1 | - | REFUSE |
| S0049 | S0046 | solvent | waters at 2.5 sigma, mode single | 0.0979 |  | 0.0685 | 0.0294 | 10.0 | - | REFUSE |
| S0050 | S0046 | solvent | waters at 2.0 sigma, mode single | 0.0991 |  | 0.0681 | 0.0310 | 9.9 | - | REFUSE |
| S0051 | S0046 | refinement | water ADPs anisotropic | 0.0954 |  | 0.0686 | 0.0268 | 10.0 | - | ACCEPT |
| S0052 | S0051 | refinement | water ADPs anisotropic | 0.0966 |  | 0.0699 | 0.0268 | 10.9 | - | REFUSE |
| S0053 | S0051 | refinement | 20 macro-cycles against 10 | 0.0959 |  | 0.0671 | 0.0288 | 11.4 | - | REFUSE |
| S0054 | S0051 | refinement | altloc occupancies refined | 0.0974 |  | 0.0682 | 0.0292 | 10.9 | - | REFUSE |
| S0055 | S0051 | solvent | waters in own-copy clashes moved to a copy they clear; nothing deleted | 0.0956 |  | 0.0670 | 0.0286 | 9.8 | - | ACCEPT |
| S0056 | S0051 | rotamer-finder | copies under difference peaks: the weakest copy takes the peak copy's rotamer | 0.0953 |  | 0.0671 | 0.0282 | 10.8 | - | REFUSE |
| S0057 | S0051 | solvent | waters at 3.0 sigma, mode single | 0.0949 |  | 0.0658 | 0.0292 | 11.0 | - | REFUSE |
| S0058 | S0051 | solvent | waters at 2.5 sigma, mode single | 0.0959 |  | 0.0666 | 0.0292 | 11.1 | - | REFUSE |
| S0059 | S0051 | refinement | 20 macro-cycles against 10 | 0.0959 |  | 0.0671 | 0.0288 | 11.4 | - | REFUSE |
| S0060 | S0051 | solvent | no peak at 6.0 sigma on a lettered water or in open solvent | 0.0954 |  | 0.0686 | 0.0268 | 10.0 | - | REFUSE |
| S0061 | S0051 | rotamer-finder | Coot rotamer fit and real-space refinement of each copy of the residues with an atom beyond +-3.5 sigma in the work-only mFo-DFc map; the counted waters that a moved side chain overlaps deleted | 0.0981 |  | 0.0713 | 0.0269 | 10.6 | - | REFUSE |
| S0062 | S0051 | rotamer-finder | B-factors of the copies reset to the copy median where they differ by more than 3 times | 0.0950 |  | 0.0661 | 0.0289 | 10.7 | - | ACCEPT |
| S0063 | S0051 | solvent | phosphate (the crystals grew in 0.1 M K2HPO4) with P at the tallest mFo-DFc peak of the model (23.5 sigma; 1.2 to 1.8 A from OE2 of six copies of Glu23, each OE2 in negative density; no rotation of Glu23 reaches the peak; Lys25 NZ, Asn3 ND2 and Ser81 N within 4.5 A); occupancy 1, a tetrahedron the refinement turns; the copies' atoms move in the refinement | 0.0990 |  | 0.0733 | 0.0257 | 13.9 | - | REFUSE |
| S0064 | S0051 | rotamer-finder | Coot refit of each copy (omit maps) of Glu23, Ile156 and Ser81, the residues under the three tallest mFo-DFc peaks (23.3, 11.9, 10.9 sigma); the counted waters a moved side chain overlaps deleted | 0.0948 |  | 0.0666 | 0.0281 | 10.8 | - | REFUSE |
| S0065 | S0051 | solvent | a water at the tallest mFo-DFc peak of the model (23.5 sigma; 1.2 to 1.8 A from OE2 of six copies of Glu23, each OE2 in negative density; no rotation of Glu23 reaches the peak; Lys25 NZ, Asn3 ND2 and Ser81 N within 4.5 A); occupancy 1; the alternative to K and PO4 at the same site | 0.0953 |  | 0.0668 | 0.0285 | 10.8 | - | REFUSE |
| S0066 | S0051 | solvent | K (the crystals grew in 0.1 M K2HPO4) at the tallest mFo-DFc peak of the model (23.5 sigma; 1.2 to 1.8 A from OE2 of six copies of Glu23, each OE2 in negative density; no rotation of Glu23 reaches the peak; Lys25 NZ, Asn3 ND2 and Ser81 N within 4.5 A); occupancy 1; the copies' atoms move in the refinement | 0.0960 |  | 0.0678 | 0.0282 | 10.4 | - | REFUSE |
| S0067 | S0062 | solvent | waters at 3.0 sigma, mode single, none within 2.6 A of a protein atom of any copy | 0.0967 |  | 0.0668 | 0.0299 | 11.9 | - | REFUSE |
| S0068 | S0051 | rotamer-finder | Coot refit of each copy (omit maps) of Lys25, then Glu23: the tallest mFo-DFc peak (23.5 sigma) lies 0.2 to 1.0 A from where NZ of Lys25 would be in the rotamer chi -100, -20, 150, 180 of each copy; no Glu23 oxygen reaches it (1.2 A at best), and the copies' Glu23 OE2 atoms sit 1.2 to 1.8 A from it in negative density; a water, K or PO4 at the peak was refused (S0063, S0065, S0066) | 0.0949 |  | 0.0660 | 0.0289 | 10.9 | - | REFUSE |
| S0069 | S0062 | solvent | waters at 2.5 sigma, mode single, none within 2.6 A of a protein atom of any copy | 0.0972 |  | 0.0668 | 0.0304 | 11.6 | - | REFUSE |
| S0070 | S0062 | rotamer-finder | Coot refit of each copy (omit maps) of Ser81, Ile117, Leu5 and Arg151: at each a difference peak of 6.9 to 10.9 sigma lies 1.1 to 1.9 A from the same atom of 4 to 7 copies, those atoms in negative density (-1.6 to -4.8 sigma on average; scripts/review/pulled_sites.py): a rotamer that no copy has | 0.0957 |  | 0.0671 | 0.0285 | 11.4 | - | REFUSE |
| S0071 | S0062 | refinement | water ADPs anisotropic | 0.0953 |  | 0.0675 | 0.0279 | 11.5 | - | ACCEPT |
| S0072 | S0071 | refinement | 10 macro-cycles against none (a zero-cycle control): convergence of the model in force | 0.0951 |  | 0.0652 | 0.0299 | 12.1 | - | REFUSE |
| S0073 | S0071 | solvent | no peak at 6.0 sigma on a lettered water or in open solvent | 0.0953 |  | 0.0675 | 0.0279 | 11.5 | - | REFUSE |
| S0074 | S0071 | rotamer-finder | B-factors of the copies reset to the copy median where they differ by more than 3 times | 0.0952 |  | 0.0652 | 0.0300 | 11.9 | - | REFUSE |
| S0075 | S0071 | rotamer-finder | conformer B-factors above the site median reset to the median where the conformer's 2mFo-DFc density is at least 0.5 of the site's (no ratio threshold); conformers in weak density keep their B | 0.0946 |  | 0.0650 | 0.0296 | 12.1 | - | REFUSE |
| S0076 | S0071 | rotamer-finder | conformer B-factors above the site median reset to the median where the conformer density is at least 0.5 of the site median (no ratio threshold); the same change as S0075, judged as an improving step (S0075 was refused as a repair with R-free -2.7 sigma against the control: no count fell 10 %) | 0.0946 |  | 0.0650 | 0.0296 | 12.1 | - | ACCEPT |
