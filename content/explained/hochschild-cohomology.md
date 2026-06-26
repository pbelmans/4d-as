---
title: "Hochschild cohomology of the algebra"
summary: "deformations of the graded algebra"
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
on this site (with \(\mathrm{HH}^0_0 = 1\) always).

In particular \(\mathrm{HH}^2_0(A)\) is the space of first-order graded
deformations, and is identified with the tangent space to the moduli stack at
\([A]\) — this is what the
[Kodaira–Spencer map](/explained/kodaira-spencer-map/) measures.

This is the deformation theory of the *ring* \(A\). The deformation theory of
the associated *variety* is captured instead by the
[Hochschild cohomology of qgr](/explained/hochschild-cohomology-of-qgr/).

## Overview

\(\dim \mathrm{HH}^i_0(A)\) for \(i = 1, 2, 3\), for every family
(\(\mathrm{HH}^0_0 = 1\) always), as computed in {{< arxiv "2511.08390" >}}:

{{< family-table "hh0" >}}
