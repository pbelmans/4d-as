---
title: "The centre"
summary: "central elements and the centre's Hilbert series"
math: true
---

The **centre** \(Z(A)\) of a graded algebra is the graded subalgebra of elements
commuting with everything. For a generic noncommutative \(\mathbb{P}^3\) it is
trivial in low degrees (\(Z = k\)); extra central elements signal extra
geometry. The classic case is a pencil of **central quadrics**, as for the
Sklyanin algebra.

## Hilbert series of the centre

Writing \(H_Z(t) = \sum_n (\dim_k Z_n)\, t^n\), the following were computed over
the generic point — i.e. with the rational function field \(\mathbb{Q}(\text{params})\)
as base field — for the families with small parameter sets:

| family | \(H_Z(t)\) |
|---|---|
| generic double Ore | \(1\) (trivial centre) |
| Sklyanin, Sklyanin twist | \(1/(1-t^2)^2\), \(\;Z = k[\Omega_1, \Omega_2]\) |
| \(S_\infty\) twist | \(1/(1-t^2)\) |
| Clifford | \(1/(1-t^2)^4\), \(\;Z = k[x_1^2, x_2^2, x_3^2, x_4^2]\) |
| Le Bruyn central extension | no closed form (a central degree-1 variable and higher central elements) |

## Status of the computation

This is **not yet done for every family**. The dimensions
\(\dim Z_1, Z_2, Z_3\) were computed genuinely over \(\mathbb{Q}(\text{params})\)
for the small-parameter families above; for the others the values are obtained
over a finite field \(\mathrm{GF}(p)\) at a generic point, which gives the
generic dimension with high probability. Computing over
\(\mathbb{Q}(\text{params})\) for the families with many parameters (Clifford
has 24, the Le Bruyn extension 12) is infeasible — a Gröbner basis over a
function field falls back to a slow algorithm and does not terminate.
