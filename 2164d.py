#!/usr/bin/env pypy3

import sys

input = lambda: sys.stdin.readline().rstrip()
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

def solve():
    n, K = LII()
    s, t = input(), input()

    if s[0] != t[0]:
        return -1

    j = n - 1
    shift = [0] * n
    for i in reversed(range(1, n)):
        j = min(i, j)
        while j >= 0 and t[i] != s[j]:
            j -= 1
        if j < 0 or i - j > K:
            return -1
        shift[i] = i - j

    k = max(shift)
    print(k)

    # `s` is immutable so create a char array for modifications
    cur = [c for c in s]
    for _ in range(k):
        j = n - 1
        for i in reversed(range(1, n)):
            if shift[i] == 0:
                continue
            j = min(j, i)
            while j > i - shift[i]:
                cur[j] = cur[j - 1]
                j -= 1
            shift[i] -= 1
        print(''.join(cur))

    return None

def main():
    T = II()
    for _ in range(T):
        ans = solve()
        if ans:
            print(ans)
main()
