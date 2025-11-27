#!/usr/bin/env python3

import sys

input = lambda: sys.stdin.readline().rstrip()
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))
pf = lambda x: print(x, flush=True)

def query(l: int, r: int) -> tuple[int, int]:
    pf(f'1 {l} {r}')
    p = II()
    pf(f'2 {l} {r}')
    a = II()
    return p, a

def solve():
    n = II()

    # Starting point for the search for the right boundary
    # Update this whenever we find a new rightmost mismatch interval
    next_l = 2

    l, r = 1, n
    while l < r:
        m = (l + r) // 2
        p, a = query(l, m)
        if p != a:
            # left boundary is in [l, m]
            r = m
        else:
            # left boundary is in (m, r]
            l = m + 1
            next_l = max(next_l, l + 1)
    left_bound = l

    # Edge case: the right boundary extends to the last element
    p, a = query(n, n)
    if p != a:
        return left_bound, n

    # Now I'm searching for the first non-different value
    l, r = next_l, n
    while l < r:
        m = (l + r) // 2
        p, a = query(m, r)
        if p == a:
            r = m
        else:
            # if p[m, r] != a[m, r], >= 1 elements on the left don't match
            # thus, we can at least throw out m
            l = m + 1
    right_bound = l - 1

    return left_bound, right_bound

def main():
    T = II()
    for _ in range(T):
        l, r = solve()
        pf(f'! {l} {r}')
main()
