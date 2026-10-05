# E035 trajectory (frozen flags, harness evaluator)

B0 (six-copy base, 20 mc): select 0.10175 report 0.10734 full 0.10453 work 0.09598
B0_r2 (B0 shaken 0.1 Å + 6 mc, the paper's randomized start): select 0.10076 report 0.10683 full 0.10377
B0_r3 (B0 shaken 0.1 Å + 6 mc, the paper's randomized start): select 0.09992 report 0.10759 full 0.10373

## Replicate 1

| loop | T select | C1 select | C2 select | ΔT−C1 (σ) | ΔT−C2 (σ) | T report | C1 report | T full | C1 full | Δgap T−C1 (σ) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0.11394 | 0.11580 | 0.11380 | — | — | 0.11729 | 0.11775 | 0.11560 | 0.11677 | — |

Per-arm trajectories (select / full / R-work; MA3 = 3-point moving average of full, the paper's reading):

| loop | T | T MA3 | C1 | C1 MA3 | C2 | C2 MA3 |
|---|---|---|---|---|---|---|
| 1 | 0.11394 / 0.11560 / 0.10875 | — | 0.11580 / 0.11677 / 0.10926 | — | 0.11380 / 0.11461 / 0.10628 | — |
| 2 | — | — | — | — | 0.12387 / 0.12392 / 0.11539 | — |

endpoints (paper's rule: last loop before three consecutive rises in select; 'provisional' = rule not yet triggered, latest loop shown): C1: loop 1 select 0.11580 full 0.11677 (provisional), C2: loop 2 select 0.12387 full 0.12392 (provisional), T: loop 1 select 0.11394 full 0.11560 (provisional)

## Replicate 2 (start B0_r2)

| loop | T select | C1 select | C2 select | ΔT−C1 (σ) | ΔT−C2 (σ) | T report | C1 report | T full | C1 full | Δgap T−C1 (σ) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0.11505 | 0.11197 | — | — | — | 0.11900 | 0.11713 | 0.11701 | 0.11454 | — |

Per-arm trajectories (select / full / R-work; MA3 = 3-point moving average of full, the paper's reading):

| loop | T | T MA3 | C1 | C1 MA3 | C2 | C2 MA3 |
|---|---|---|---|---|---|---|
| 1 | 0.11505 / 0.11701 / 0.10751 | — | 0.11197 / 0.11454 / 0.10514 | — | — | — |

endpoints (paper's rule: last loop before three consecutive rises in select; 'provisional' = rule not yet triggered, latest loop shown): C1: loop 1 select 0.11197 full 0.11454 (provisional), T: loop 1 select 0.11505 full 0.11701 (provisional)

## Replicate 3 (start B0_r3)

| loop | T select | C1 select | C2 select | ΔT−C1 (σ) | ΔT−C2 (σ) | T report | C1 report | T full | C1 full | Δgap T−C1 (σ) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0.10636 | 0.10239 | — | — | — | 0.11096 | 0.10692 | 0.10865 | 0.10465 | — |

Per-arm trajectories (select / full / R-work; MA3 = 3-point moving average of full, the paper's reading):

| loop | T | T MA3 | C1 | C1 MA3 | C2 | C2 MA3 |
|---|---|---|---|---|---|---|
| 1 | 0.10636 / 0.10865 / 0.09996 | — | 0.10239 / 0.10465 / 0.09600 | — | — | — |

endpoints (paper's rule: last loop before three consecutive rises in select; 'provisional' = rule not yet triggered, latest loop shown): C1: loop 1 select 0.10239 full 0.10465 (provisional), T: loop 1 select 0.10636 full 0.10865 (provisional)

## Mean ΔT−C1 and ΔT−C2 on full R-free over replicates, at equal loop count

| loop | mean ΔT−C1 full | n | mean ΔT−C2 full | n |
|---|---|---|---|---|
| 1 | 0.00177 | 3 | 0.00099 | 1 |
