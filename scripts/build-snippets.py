#!/usr/bin/env python3
"""Generate Macaulay2 / GAP / Magma presentation snippets for every family from
the display relations in data/families/*.yaml, into data/snippets.json (keyed by
the family's data key). Hugo renders these in tabs. Run before hugo."""
import glob, json, os, re

GREEK = {"α": "alpha", "β": "beta", "γ": "gamma", "λ": "lambda", "σ": "sigma",
         "ω": "omega", "Ω": "Omega", "ζ": "zeta", "δ": "delta", "μ": "mu", "π": "pi"}


def norm_ids(s):
    for g, a in GREEK.items():
        s = s.replace(g, a)
    s = s.replace("_{", "").replace("}", "").replace("_", "")  # q_{13}->q13, x_4->x4
    s = re.sub(r"(?<![A-Za-z0-9])i(?![A-Za-z0-9])", "ii", s)    # imaginary unit
    return s


def split_terms(s):
    """Split on top-level ' + ' / ' - ' (operators surrounded by spaces)."""
    res, depth, start, sign = [], 0, 0, "+"
    for i, c in enumerate(s):
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
        elif depth == 0 and c in "+-" and i > 0 and s[i - 1] == " " \
                and i + 1 < len(s) and s[i + 1] == " ":
            res.append((sign, s[start:i - 1].strip()))
            sign, start = c, i + 1
    res.append((sign, s[start:].strip()))
    return res


def join_factors(term):
    facs, i, n = [], 0, len(term)
    while i < n:
        if term[i] == " ":
            i += 1
            continue
        if term[i] == "(":
            depth, j = 0, i
            while j < n:
                if term[j] == "(":
                    depth += 1
                elif term[j] == ")":
                    depth -= 1
                    if depth == 0:
                        j += 1
                        break
                j += 1
            grp = "(" + mul(term[i + 1:j - 1]) + ")"
            if j < n and term[j] == "^":
                grp += "^"
                j += 1
                while j < n and term[j].isdigit():
                    grp += term[j]
                    j += 1
            facs.append(grp)
            i = j
        else:
            j = i
            while j < n and term[j] not in " (":
                j += 1
            facs.append(term[i:j])
            i = j
    return "*".join(facs)


def mul(s):
    out = ""
    for k, (sign, term) in enumerate(split_terms(s)):
        t = join_factors(term)
        if k == 0:
            out = t if sign == "+" else "-" + t
        else:
            out += " " + sign + " " + t
    return out


def relations(path):
    rels, on = [], False
    for ln in open(path):
        if re.match(r"^relations:", ln):
            on = True
            continue
        if on:
            m = re.match(r'^\s*-\s*"(.*)"\s*$', ln)
            if m:
                rels.append(m.group(1))
            elif ln.strip() and not ln.startswith(" "):
                break
    return [mul(norm_ids(r)) for r in rels]


def params(rels):
    ids = set()
    for r in rels:
        ids |= set(re.findall(r"[A-Za-z][A-Za-z0-9]*", r))
    return sorted(ids - {"x1", "x2", "x3", "x4"})


def m2(rels, ps):
    K = "frac(QQ[%s])" % ", ".join(ps) if ps else "QQ"
    body = ",\n  ".join(rels)
    return ('needsPackage "AssociativeAlgebras"\n'
            f"K = {K};\n"
            "A = K<|x1,x2,x3,x4|>;\n"
            f"I = ideal {{\n  {body}\n}};\n"
            "B = A/I;")


def gap(rels, ps):
    body = ",\n  ".join(rels)
    if ps:
        decl = ('PolyRing := FunctionField(Rationals, [%s]);;\n'
                % ", ".join('"%s"' % p for p in ps))
        decl += "indets := IndeterminatesOfFunctionField(PolyRing);;\n"
        decl += "".join(f"{p} := indets[{i + 1}];;\n" for i, p in enumerate(ps))
    else:
        decl = "PolyRing := Rationals;;\n"
    return (decl
            + 'kQ := FreeKAlgebra(PolyRing, 4, "x");;\n'
            + "x1 := kQ.x1;; x2 := kQ.x2;; x3 := kQ.x3;; x4 := kQ.x4;;\n"
            + f"rels := [\n  {body}\n];;\n"
            + "A := kQ / rels;;")


def magma(rels, ps):
    body = ",\n  ".join(rels)
    if ps:
        K = "K<%s> := RationalFunctionField(Rationals(), %d);" % (", ".join(ps), len(ps))
    else:
        K = "K := Rationals();"
    return (f"// untested (Magma not available here)\n{K}\n"
            "F<x1,x2,x3,x4> := FreeAlgebra(K, 4);\n"
            f"rels := [\n  {body}\n];\n"
            "A := quo< F | rels >;")


snippets = {}
for f in glob.glob("data/families/*.yaml"):
    key = os.path.basename(f)[:-5]
    rels = relations(f)
    ps = params(rels)
    snippets[key] = {"m2": m2(rels, ps), "gap": gap(rels, ps), "magma": magma(rels, ps)}

os.makedirs("data", exist_ok=True)
json.dump(snippets, open("data/snippets.json", "w"), indent=1, ensure_ascii=False)
print(f"wrote data/snippets.json with {len(snippets)} families")
