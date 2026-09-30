# `data/` — the families of 4-dimensional AS-regular algebras

Each YAML file describes one family of quadratic (Koszul) Artin–Schelter
regular algebras of global dimension 4 — i.e. a "noncommutative `P^3`".

## Conventions

- **Generators** are written `x_1, x_2, x_3, x_4` (four generators), never
  `x, y, z, w`. In the untwisted central extension `x_4` is central; in its Zhang twist,
  the distinguished generator is `x_3`, which is normal and anticommutes
  with the other generators.
- **Relations** are quadratic expressions understood to be equal to `0`.
  Monomials are written in the order they appear, e.g. `x_3 x_1 - h x_1 x_3`
  means `x_3 x_1 - h·x_1 x_3 = 0`.
- The families and their invariants are from **arXiv:2511.08390**.

## Schema

```yaml
name: "Sklyanin"            # display name
kind: "named"              # "double-Ore" (A–Z) or "named"
generators: ["x_1", "x_2", "x_3", "x_4"]
quadratic: true
num_parameters: 2          # number of scalar parameters
hh0: [1, 2, 9]             # graded HH^*_0 in degrees 1, 2, 3 (arXiv:2511.08390)
hh_qgr: [1, 0, 2, 7]       # directly computed HH^*(qgr A) in degrees 0–3 (optional)
point_scheme_dim: 1        # dimension of the point scheme
point_scheme: "..."        # succinct description of the point scheme
year: 1982                 # year of first definition (the introducing work)
slug: "sklyanin"           # URL slug under /families/ (ore-a, ore-b, … for A–Z)
sortkey: "1982 sklyanin"   # "<year> <slug>"; drives the default table order
ks_rank: 2                 # rank of the Kodaira–Spencer map
ks_inj: true               # is it injective?
ks_surj: true              # is it surjective?
centre_z1: 0               # dim Z_1(A) (central linear forms)
centre_z2: 2               # dim Z_2(A) (central quadrics)
centre_z3: 0               # dim Z_3(A) (central cubics)
centre_z4: 3               # dim Z_4(A) (central quartics)
centre_z5: 0               # dim Z_5(A)
centre_z6: 4               # dim Z_6(A)
centre_z7: 0               # dim Z_7(A)
centre_z8: 5               # dim Z_8(A)
centre_z9: 0               # dim Z_9(A)
centre_z10: 6              # dim Z_10(A)
centre_parameters: '$\alpha = \beta$' # optional branch label for the centre table
normal_1: -1               # proj. dim of the normal locus in degree 1 (-1 = none)
normal_2: 1                # proj. dim of the normal locus in degree 2
calabi_yau: true           # is A Calabi-Yau? (Nakayama automorphism nu = id)
nakayama: "\\mathrm{id}"   # the Nakayama automorphism nu on A_1, as LaTeX
nakayama_type: "identity"  # identity | scalar | diagonal | monomial | unipotent | general
nakayama_constant: true    # is nu constant over the parameter space? (omit if no params)
homological_det: 1         # det nu (the homological determinant): 1, -1, or "i"
nakayama_field: "qq"       # provenance: qq | gf-params | gf | gf-sample
parameters:                # symbols + constraints
  - symbol: "β, γ"
    description: "..."
introduced:                # where the family was first constructed
  reference: "..."         # citation key (MRxxxxxxx or arXiv id)
  note: "..."
construction: >            # the idea behind the construction
  ...
relations:                 # each expression = 0
  - "..."
code_derive:               # parameters fixed by a constraint, in code form (optional)
  - "alpha = -(beta + gamma)/(1 + beta*gamma)"
references:                # further literature (citation keys)
  - "..."
notes: "..."               # other remarks, e.g. a parameter constraint (optional)
```

Computed invariants (`hh0`, `hh_qgr`, `point_scheme_dim`, `centre_z*`,
`normal_*`, the `ks_*` fields) come from arXiv:2511.08390 and from the
reproduction scripts in `code/`.
The centre dimensions through degree 10 were checked for all 54 families with
recorded data using `scripts/compute-centre.py` at parameter samples over
the five prime fields of orders `60013`, `90001`, `120049`, `150001`,
and `180001`, with identical results and agreement with the
previous degree 2–4 entries. These are sampled dimensions, not proofs of
genericity. Run `npm run snippets`, then `python3 scripts/compute-centre.py`;
the generated Macaulay2 scripts, logs and results are saved under
`code/centre-table-results/`. The script respects the prescribed roots of
unity, computes a Gröbner basis through degree 11, and checks the algebra's
Hilbert function through degree 11 before computing central elements.
For `s-d-i` it replaces the first Sklyanin relation; the variants `s-d-i:0`
through `s-d-i:5` check all six choices, which gave the same dimensions.
The Generalized Clifford 1 entries use `alpha=beta=i`, labelled by
`centre_parameters`; the `generalized-clifford-1:opposite` variant checks
`alpha=i,beta=-i`, which instead gives `[0,0,0,3,0,0,0,13,0,0]` in degrees 1–10.
Generalized Clifford 2 uses `alpha2=1`; its `:zero` variant checks `alpha2=0`.
Both normalizations satisfy the regularity condition and give the same dimensions
in the five-prime checks.
Generalized Clifford 3 and the S-d-i twist still have no recorded centre data.

The Nakayama fields (`calabi_yau`, `nakayama`,
`nakayama_type`, `nakayama_constant`, `homological_det`, `nakayama_field`) come
from `code/nakayama.m2`, and the point schemes of the seven families they were
missing for from `code/point_scheme_extra.m2`. Fields that are absent (e.g. an
un-computed `point_scheme_dim`) render as `?`.
