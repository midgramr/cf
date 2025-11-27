#!/usr/bin/env pypy3

import sys

input = lambda: sys.stdin.readline().rstrip()
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))
pf = lambda x: print(x, flush=True)

def query(l: int, r: int) -> int:
    pf(f'1 {l} {r}')
    p = II()
    pf(f'2 {l} {r}')
    a = II()
    return a - p

def solve():
    n = II()
    M = query(1, n)
    l, r = 1, n
    while l < r:
        m = (l + r) // 2
        q = query(l, m)
        if q == 0:
            l = m + 1
        elif q == M:
            r = m
        else:
            L = m - q + 1
            R = m + M - q
            return L, R
    # Edge case: L == R
    return l, l

def main():
    T = II()
    for _ in range(T):
        l, r = solve()
        pf(f'! {l} {r}')
main()
