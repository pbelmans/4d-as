---
title: "The centre"
summary: "central elements and the centre's Hilbert series"
math: true
---

The **centre** \(\operatorname{Z}(A)\) of a graded algebra is the graded
subalgebra of elements commuting with everything. For a generic noncommutative
\(\mathbb{P}^3\) it is trivial in low degrees (\(\operatorname{Z}(A) = k\)); extra
central elements signal extra geometry. The classic case is a pencil of
**central quadrics**, as for the [Sklyanin](/families/sklyanin/) algebra.

## Families with non-trivial centre

The dimensions \(\dim \operatorname{Z}(A)_n\) through degree 6, with the centre's
Hilbert series \(\operatorname{h}_{\operatorname{Z}(A)}(t) = \sum_n \dim_k \operatorname{Z}(A)_n \, t^n\):

| family | \(Z_1\) | \(Z_2\) | \(Z_3\) | \(Z_4\) | \(Z_5\) | \(Z_6\) | \(\operatorname{h}_{\operatorname{Z}(A)}(t)\) |
|---|---|---|---|---|---|---|---|
| [Sklyanin](/families/sklyanin/), [Sklyanin twist](/families/sklyanin-twist/) | 0 | 2 | 0 | 3 | 0 | 4 | \(1/(1-t^2)^2 = k[\Omega_1, \Omega_2]\) |
| [Clifford](/families/clifford/) | 0 | 4 | 0 | 10 | 0 | 20 | \(1/(1-t^2)^4 = k[x_1^2, \dots, x_4^2]\) |
| [Cassidy–Vancliff 2](/families/cassidy-vancliff-2/) | 0 | 2 | 0 | 5 | 0 | 8 | \(1 + 2t^2 + 5t^4 + 8t^6 + \cdots\) |
| [\(\mathrm{S}_\infty\) twist](/families/s-infinity-twist/) | 0 | 1 | 0 | 2 | 0 | 2 | \(1 + t^2 + 2t^4 + 2t^6 + \cdots\) |
| [central extension of Sklyanin](/families/lebruyn/) | 1 | 1 | 2 | 2 | 2 | 3 | \(1 + t + t^2 + 2t^3 + 2t^4 + 2t^5 + 3t^6 + \cdots\) |

For Sklyanin and Clifford the centre is an honest polynomial ring — a pencil of
central quadrics, respectively the four central squares. The
[Cassidy–Vancliff 1](/families/cassidy-vancliff-1/) and
[Shelton–Tingey](/families/shelton-tingey/) algebras have trivial centre in
degree 2 but acquire central elements first in **degree 4**.
([Cassidy–Vancliff 3](/families/cassidy-vancliff-3/) is regular only at special
parameters, where its centre depends on the chosen point.) Every other family has
trivial centre in low degrees — the sole exception being the
[commutative](/families/commutative/) ring, which is its own centre.

## Every family

The number of independent central quadrics and cubics
(\(\dim \operatorname{Z}(A)_2\), \(\dim \operatorname{Z}(A)_3\)) for every family:

{{< family-table "centre" >}}

## How it was computed

The degree-by-degree dimensions above were computed with Macaulay2 over a
generic point of a finite field \(\mathrm{GF}(p)\) (\(p \equiv 1 \bmod 12\)),
confirmed at two primes to pin down the generic value; an explicit
noncommutative Gröbner basis to degree 8 ensures degree-\(\le 6\) central
elements are not truncated. For the small-parameter families these agree with a
computation over the function field \(\mathbb{Q}(\text{params})\); with many
parameters (Clifford has 24, the central extension 12) a function-field Gröbner
basis does not terminate, which is why the finite-field computation is used.
