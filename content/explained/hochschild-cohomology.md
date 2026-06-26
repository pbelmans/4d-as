---
title: "Hochschild cohomology"
summary: "the deformation theory of the algebra and of qgr"
math: true
---

The **Hochschild cohomology** \(\mathrm{HH}^\bullet(A)\) of an algebra \(A\) is
the cohomology of the complex \(\operatorname{Hom}_{A^e}(P_\bullet, A)\), where
\(P_\bullet\) is the bar (or, for a Koszul algebra, the Koszul) resolution of
\(A\) as an \(A\)-bimodule. It governs the deformation theory of \(A\):
\(\mathrm{HH}^0(A)\) is the centre, \(\mathrm{HH}^1(A)\) the outer derivations,
and \(\mathrm{HH}^2(A)\) the infinitesimal deformations.

## The graded refinement \(\mathrm{HH}^\bullet_0\)

For a connected graded algebra the Hochschild cohomology is itself graded, and
the part of internal degree \(0\), written \(\mathrm{HH}^\bullet_0(A)\), is the
piece relevant to **graded** deformations — those that keep the grading and the
number of generators and relations. The dimensions
\(\dim \mathrm{HH}^i_0(A)\) for \(i = 0, 1, 2, 3\) are the invariants tabulated
on this site (with \(\mathrm{HH}^0_0 = 1\) always). In particular
\(\mathrm{HH}^2_0(A)\) is the space of first-order graded deformations, and is
identified with the tangent space to the moduli stack at \([A]\) — this is what
the [Kodaira–Spencer map](/explained/kodaira-spencer-map/) measures.

## Hochschild cohomology of qgr

The category \(\operatorname{qgr} A\) of finitely generated graded modules
modulo finite-dimensional ones is the **noncommutative projective scheme**
attached to \(A\) — the noncommutative \(\mathbb{P}^3\) itself, as opposed to its
homogeneous coordinate ring. Its Hochschild cohomology
\(\mathrm{HH}^\bullet(\operatorname{qgr} A)\) is the deformation theory of the
*variety* rather than the *ring*; it always satisfies
\(\mathrm{HH}^0 = k\) and has Euler characteristic \(-4\). It is generally
different from \(\mathrm{HH}^\bullet_0(A)\): the naive alternating-sum relation
between the two holds for \(\mathbb{P}^3\) and the Sklyanin algebra but fails in
general, so it must be computed directly.
