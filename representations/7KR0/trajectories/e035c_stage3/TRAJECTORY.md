# E035 trajectory (frozen flags, harness evaluator) — paired rows at k ≡ 2 (mod 3)


## Replicate 1

| loop | T select | C1 select | C2 select | ΔT−C1 (σ) | ΔT−C2 (σ) | T report | C1 report | T full | C1 full | Δgap T−C1 (σ) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 0.10139 | 0.10323 | 0.10214 | — | — | 0.10750 | 0.10823 | 0.10443 | 0.10571 | — |

Per-arm trajectories (select / full / R-work; MA3 = 3-point moving average of full, the paper's reading):

| loop | T | T MA3 | C1 | C1 MA3 | C2 | C2 MA3 |
|---|---|---|---|---|---|---|
| 0 | 0.10121 / 0.10451 / 0.09644 | — | — | — | — | — |
| 1 | 0.10136 / 0.10469 / 0.09634 | — | 0.10313 / 0.10556 / 0.09628 | — | 0.10209 / 0.10480 / 0.09564 | — |
| 2 | 0.10139 / 0.10443 / 0.09618 | 0.10454 | 0.10323 / 0.10571 / 0.09626 | — | 0.10214 / 0.10482 / 0.09540 | — |
| 4 | — | — | 0.10320 / 0.10570 / 0.09627 | — | 0.10214 / 0.10482 / 0.09540 | — |
| 5 | — | — | 0.10310 / 0.10548 / 0.09598 | — | 0.10231 / 0.10492 / 0.09536 | — |

endpoints (paper's rule: last loop before three consecutive rises in select; 'provisional' = rule not yet triggered, latest loop shown): C1: loop 5 select 0.10310 full 0.10548 (provisional), C2: loop 5 select 0.10231 full 0.10492 (provisional), T: loop 2 select 0.10139 full 0.10443 (provisional)

## Replicate 2 (start B0_r2)

| loop | T select | C1 select | C2 select | ΔT−C1 (σ) | ΔT−C2 (σ) | T report | C1 report | T full | C1 full | Δgap T−C1 (σ) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 0.10051 | 0.10147 | — | — | — | 0.10739 | 0.10674 | 0.10393 | 0.10409 | — |

Per-arm trajectories (select / full / R-work; MA3 = 3-point moving average of full, the paper's reading):

| loop | T | T MA3 | C1 | C1 MA3 | C2 | C2 MA3 |
|---|---|---|---|---|---|---|
| 0 | 0.10022 / 0.10409 / 0.09535 | — | — | — | — | — |
| 1 | 0.10039 / 0.10397 / 0.09509 | — | 0.10148 / 0.10407 / 0.09524 | — | — | — |
| 2 | 0.10051 / 0.10393 / 0.09502 | 0.10399 | 0.10147 / 0.10409 / 0.09491 | — | — | — |
| 4 | — | — | 0.10149 / 0.10408 / 0.09491 | — | — | — |
| 5 | — | — | 0.10152 / 0.10409 / 0.09483 | — | — | — |

endpoints (paper's rule: last loop before three consecutive rises in select; 'provisional' = rule not yet triggered, latest loop shown): C1: loop 5 select 0.10152 full 0.10409 (provisional), T: loop 2 select 0.10051 full 0.10393 (provisional)

## Replicate 3 (start B0_r3)

| loop | T select | C1 select | C2 select | ΔT−C1 (σ) | ΔT−C2 (σ) | T report | C1 report | T full | C1 full | Δgap T−C1 (σ) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 0.09989 | 0.10105 | — | — | — | 0.10726 | 0.10710 | 0.10356 | 0.10406 | — |

Per-arm trajectories (select / full / R-work; MA3 = 3-point moving average of full, the paper's reading):

| loop | T | T MA3 | C1 | C1 MA3 | C2 | C2 MA3 |
|---|---|---|---|---|---|---|
| 0 | 0.09982 / 0.10377 / 0.09488 | — | — | — | — | — |
| 1 | 0.10016 / 0.10371 / 0.09465 | — | 0.10104 / 0.10413 / 0.09491 | — | — | — |
| 2 | 0.09989 / 0.10356 / 0.09458 | 0.10368 | 0.10105 / 0.10406 / 0.09485 | — | — | — |
| 4 | — | — | 0.10105 / 0.10405 / 0.09485 | — | — | — |
| 5 | — | — | 0.10117 / 0.10411 / 0.09473 | — | — | — |

endpoints (paper's rule: last loop before three consecutive rises in select; 'provisional' = rule not yet triggered, latest loop shown): C1: loop 5 select 0.10117 full 0.10411 (provisional), T: loop 2 select 0.09989 full 0.10356 (provisional)

## Mean ΔT−C1 and ΔT−C2 on full R-free over replicates, at equal loop count

| loop | mean ΔT−C1 full | n | mean ΔT−C2 full | n |
|---|---|---|---|---|
| 2 | -0.00065 | 3 | -0.00039 | 1 |
