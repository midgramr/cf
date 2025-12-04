#!/usr/bin/env pypy3

import sys

read = lambda f: f.readline().rstrip()
readint = lambda f: int(read(f))
readints = lambda f: list(map(int, read(f).split()))
pf = lambda s: print(s, flush=True)
err = lambda s: print(s, file=sys.stderr, flush=True)

def parse_test(path: str) -> list[tuple]:
    tests = []
    with open(path) as f:
        t = readint(f)
        for _ in range(t):
            n = readint(f)
            p = readints(f)
            l, r = readints(f)
            # NOTE: Could construct fenwick tree here, but too lazy
            a = p[:]
            a[l - 1 : r] = [v + 1 for v in a[l - 1 : r]]
            tests.append((n, p, a, l, r))
    return tests

input = lambda: sys.stdin.readline().rstrip()

def main():
    tests = parse_test('input/2.in')
    t = len(tests)
    pf(t)
    err(f't = {t}')
    for i, (n, p, a, l, r) in enumerate(tests):
        pf(n)
        err(f'Testcase {i + 1}: n = {n}, p = {p}, l = {l}, r = {r}')
        # Testcase must be answered within 40 queries
        solved = False
        for _ in range(40):
            q, x, y = input().split()
            x, y = int(x), int(y)
            if q == '!':
                if x == l and y == r:
                    err(f'Correctly answered testcase {i + 1}.')
                    solved = True
                    break
                else:
                    err(f'Incorrect answer for testcase {i + 1}')
                    exit(1)
            elif q == '1':
                pf(sum(p[x - 1 : y]))
            else:
                pf(sum(a[x - 1 : y]))
        if not solved:
            err(f'Testcase {i + 1} not solved within 40 queries.')
            exit(1)
main()
