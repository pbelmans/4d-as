"""Check centre dimensions against the site's presentations at five finite fields.

Run npm run snippets first, then python3 scripts/compute-centre.py [family ...].
The two unresolved families are excluded. For S_{d,i}, i=1 is used, as in
code/nakayama.m2; pass s-d-i:0 through s-d-i:5 to check all relation choices.
Generalized Clifford 1 uses alpha=beta=i; append :opposite for alpha=i,beta=-i.
Generalized Clifford 2 uses alpha2=1; append :zero for alpha2=0.
Outputs are evidence from specialisations, not proofs of genericity.
"""
import argparse
import concurrent.futures
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SNIPPETS = json.loads((ROOT / 'data/snippets.json').read_text())
PRIMES = (60013, 90001, 120049, 150001, 180001)


def script(name, prime, degree):
    key, _, variant = name.partition(':')
    source = SNIPPETS[key]['m2']
    match = re.search(r'QQ\[([^\]]*)\]', source)
    params = [s.strip() for s in match[1].split(',')] if match else []
    root4 = next(i for i in range(2, prime) if (i*i+1) % prime == 0)
    root3 = next(i for i in range(2, prime) if (i*i+i+1) % prime == 0)
    fixed = {'ii': 'imI'}
    if key in ('B', 'E', 'F'):
        fixed['p'] = 'imI'
    if key == 'C':
        fixed['p'] = f'{root3}_kk'
    if key in ('I', 'J'):
        fixed['q'] = 'imI'
    if key == 'generalized-clifford-1':
        fixed.update(alpha='imI', beta='-imI' if variant == 'opposite' else 'imI')
    if key == 'generalized-clifford-2':
        fixed['alpha2'] = '0_kk' if variant == 'zero' else '1_kk'
    lines = [
        'needsPackage "AssociativeAlgebras"',
        f'kk = ZZ/{prime};',
        f'imI = {root4}_kk;',
        f'setRandomSeed {prime+12345};',
        'sampleScalar = () -> (v := random kk; while v == 0 or v == 1 or v == -1 do v = random kk; v);',
    ]
    lines += [f'{p} = {fixed.get(p, "sampleScalar()")};' for p in params if p != 'ii']
    if key == 'generalized-clifford-2':
        lines.append('if (alpha1^2 + alpha2^2*beta1)*(beta1^2 + beta2^2*alpha1) == 0 then error "nonregular parameter sample";')
    for line in source.split('A =')[0].splitlines():
        if '=' in line and not line.startswith('K ='):
            lines.append(line)
    lines.append('A = kk<|x1,x2,x3,x4|>;')
    body = re.search(r'I = ideal \{(.*?)\};', source, re.S)[1]
    rels = [line.strip().rstrip(',') for line in body.strip().splitlines()]
    if key in ('s-d-i', 's-d-i-twist'):
        del rels[int(variant or 0)]
    body = ',\n'.join(rels)
    lines.append('I = ideal {\n' + re.sub(r'\bii\b', 'imI', body) + '\n};')
    lines += [
        f'NCGB(I, {degree+1});',
        'B = A/I;',
        f'hd = for n from 1 to {degree+1} list numcols ncBasis(n,B);',
        '<< "HILBERT " << toString hd << endl << flush;',
        f'if hd != apply(toList(1..{degree+1}), n -> binomial(n+3,3)) then exit 2;',
        '<< "CENTRE" << flush;',
        f'for n from 1 to {degree} do << " " << numcols centralElements(B,n) << flush;',
        '<< endl;',
        'exit 0',
    ]
    return '\n'.join(lines) + '\n'


def run(job):
    name, prime, degree, timeout, out = job
    path = out / f'{name.replace(":", "-")}-{prime}.m2'
    path.write_text(script(name, prime, degree))
    with path.with_suffix('.log').open('w') as log:
        try:
            result = subprocess.run(['M2', '--script', str(path)], stdout=log, stderr=subprocess.STDOUT, timeout=timeout, cwd=ROOT)
            success = result.returncode == 0
        except subprocess.TimeoutExpired:
            log.write('\nTIMEOUT\n')
            success = False
    match = re.search(r'CENTRE((?: \d+){%d})' % degree, path.with_suffix('.log').read_text())
    dims = [int(n) for n in match[1].split()] if match and success else None
    return name, prime, dims


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--degree', type=int, default=10)
    parser.add_argument('--timeout', type=int, default=600, help='seconds per family and prime')
    parser.add_argument('--primes', nargs='+', type=int, default=PRIMES)
    parser.add_argument('families', nargs='*')
    args = parser.parse_args()
    if args.degree < 1:
        parser.error('--degree must be positive')
    names = args.families or sorted(set(SNIPPETS) - {'generalized-clifford-3', 's-d-i-twist'})
    out = ROOT / f'code/centre-table-results/degree-{args.degree}'
    out.mkdir(parents=True, exist_ok=True)
    results = {}
    results_path = out / ('results-' + '-'.join(map(str, args.primes)) + '.json')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        jobs = [(name, prime, args.degree, args.timeout, out) for name in names for prime in args.primes]
        for future in concurrent.futures.as_completed([pool.submit(run, job) for job in jobs]):
            name, prime, dims = future.result()
            results.setdefault(name, {})[prime] = dims
            print(name, prime, dims, flush=True)
            results_path.write_text(json.dumps(results, indent=2) + '\n')
    failed = [name for name, rows in results.items() if None in rows.values() or len({tuple(d) for d in rows.values()}) != 1]
    print('DISAGREEMENTS OR FAILURES:', failed)
    sys.exit(bool(failed))
