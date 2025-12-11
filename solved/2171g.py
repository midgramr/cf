from math import log2
import sys
from typing import Iterable

input = lambda: sys.stdin.readline().rstrip('\n\r ')
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

def extended_euclid(a: int, b: int) -> tuple[int, int, int]:
    """Returns (gcd(a,b), x, y), where gcd(a,b) = ax + by."""
    if a < b:
        d, x, y = extended_euclid(b, a)
        return d, y, x
    if b == 0:
        return a, 1, 0
    dp, xp, yp = extended_euclid(b, a % b)
    return dp, yp, xp - a // b * yp

def modular_inverse(a: int, n: int) -> int:
    return extended_euclid(n, a)[2]

# Idea: precompute factorials
MOD = int(1e6) + 3
fac = [1] * MOD
for i in range(2, MOD):
    fac[i] = (i * fac[i - 1]) % MOD

def factorial(x: int) -> int:
    if x >= MOD:
        return 0
    return fac[x]

def prod(nums: Iterable[int]) -> int:
    res = 1
    for num in nums:
        res = res * (num % MOD) % MOD
    return res

def solve():
    _ = II()
    a, b = LII(), LII()

    x, seqs = 0, 1
    k = int(min(log2(bi // ai) for ai, bi in zip(a, b)))
    for j in reversed(range(k + 1)):
        next_a = [bi // 2**j for bi in b]

        m = sum(aj - ai for aj, ai in zip(next_a, a))
        prod_mi = prod(factorial(aj - ai) for aj, ai in zip(next_a, a))
        seqs = seqs * factorial(m) * modular_inverse(prod_mi, MOD) % MOD

        x += m
        if j > 0:
            # Add 1 to account for each x2 operation
            x += 1
            a = [ai * 2 for ai in next_a]

    return x, int(seqs) % MOD

T = II()
for _ in range(T):
    x, s = solve()
    print(x, s)
