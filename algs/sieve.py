#!/usr/bin/env pypy3

from math import isqrt

def sieve(n: int) -> list[int]:
    """Return list of all primes <= n"""
    is_prime = [True] * (n + 1)
    for i in range(2, isqrt(n) + 1):
        if not is_prime[i]:
            continue
        for j in range(i ** 2, n + 1, i):
            is_prime[j] = False
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
    return primes

n = 2 * int(1e5)
s = sieve(n)
print(len(s))
print(s[:500])
