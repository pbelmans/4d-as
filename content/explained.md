---
title: "Explained"
math: true
---

Background notions, explained.

## Artin–Schelter regular algebras

Let \(k\) be a field and let
\(A = \bigoplus_{i \geq 0} A_i\) be a connected graded \(k\)-algebra,
that is, \(A_0 = k\) and \(A\) is finitely generated in degree \(1\).
Write \(k = A/A_{\geq 1}\) for the trivial module.

The algebra \(A\) is **Artin–Schelter regular** (or *AS-regular*) of
dimension \(d\) if:

1. \(A\) has finite global dimension \(d\);
2. \(A\) has finite Gelfand–Kirillov dimension, i.e. polynomial growth;
3. \(A\) is **Gorenstein**: there is an integer \(\ell\) such that
   \[
   \operatorname{Ext}^i_A(k, A) \cong
   \begin{cases} k(\ell) & i = d, \\ 0 & i \neq d. \end{cases}
   \]

For \(d = 1\) and \(d = 2\) these algebras are completely understood,
and the \(d = 3\) case was classified by Artin, Schelter, Tate, and
Van den Bergh. The classification in dimension \(d = 4\) is the subject
of this website.
