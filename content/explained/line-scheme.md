---
title: "Line scheme"
summary: "the scheme parametrising line modules"
math: true
---

A **line module** over a connected graded algebra \(A\) is a cyclic graded
module \(M = \bigoplus_{i \geq 0} M_i\) with Hilbert series
\(\operatorname{h}_M(t) = (1-t)^{-2}\), i.e. \(\dim_k M_i = i + 1\) — the
module-theoretic analogue of a line \(\mathbb{P}^1 \subset \mathbb{P}^3\), one
dimension up from a [point module](/explained/point-scheme/).

The line modules of \(A\) are parametrised by a projective scheme, the
**line scheme** of \(A\). A line of \(\mathbb{P}^3 = \mathbb{P}(A_1^*)\) is a
point of the Grassmannian \(\operatorname{Gr}(2,4)\), which sits via its
Plücker embedding as the **Klein quadric** in \(\mathbb{P}^5\); the line scheme
is the closed subscheme of \(\operatorname{Gr}(2,4)\) cut out by the conditions
for a line to carry a line module.
[Shelton–Vancliff](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/S0024610702003186)
proved this functor is representable and, for a quadratic Auslander-regular
algebra of global dimension 4, gave the explicit determinantal equations used
here (the construction implemented as `lineSchemeFourDim` in the Macaulay2
package [`AssociativeAlgebras`](https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/AssociativeAlgebras/html/_line__Scheme__Four__Dim.html)).

For the commutative polynomial ring every line of \(\mathbb{P}^3\) is a line
module, so the line scheme is all of \(\operatorname{Gr}(2,4)\) — the Klein
quadric itself, of dimension \(4\). For a **generic** quadratic
\(\mathbb{P}^3\) it is instead a **curve of degree \(20\)**, and Shelton–Vancliff
show that once the line scheme is one-dimensional it already determines the
defining relations of the algebra. So a line scheme of higher dimension is the
mark of a genuinely special algebra:

- the [Sklyanin](/families/sklyanin/) algebra (and its degenerate cousin
  [\(\mathrm{S}_\infty\)](/families/s-infinity/), which shares its point scheme)
  has a **two-dimensional** line scheme: the surface of *secant lines* to the
  quartic elliptic curve \(E\) that is its point scheme — an elliptic ruled
  surface of degree \(8\). Its line modules are exactly the lines of
  \(\mathbb{P}^3\) meeting \(E\) with multiplicity \(\geq 2\)
  ([Shelton–Vancliff](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/S0024610702003186);
  see also [Smith](https://sites.math.washington.edu/~smith/Research/Skly-survey.pdf));
- [Vancliff](/families/vancliff/)'s algebra, whose point scheme is a quadric
  *surface*, has a **three-dimensional** line scheme;
- many double-Ore families have a line scheme that is a plane (a pencil of
  lines through a point, or the lines in a plane) together with a curve.

## Overview

The line scheme of every family on this site, computed at a generic point of
its parameter space (over \(\mathbb{Q}(\text{params})\) where feasible, otherwise
over \(\mathrm{GF}(p)\) at generic parameters for two primes \(p \equiv 1
\bmod 12\); the dimension and degree agree across both). The dimension is the
key invariant: \(1\) is generic, higher is special.

{{< family-table "line-scheme" >}}
