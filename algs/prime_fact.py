#!/usr/bin/env pypy3
from sieve import sieve

N = 2 * int(1e5)
primes = sieve(N)

def prime_fact(n: int) -> set[int]:
    if n in primes:
        return {n}
    factors = set()
    m = n
    for prime in primes:
        # In the worst case when n is semiprime,
        # this will stop before sqrt(n)
        if prime > m:
            break
        if m % prime == 0:
            factors.add(prime)
            while m % prime == 0:
                m //= prime
    if m > 1:
        factors.add(m)
    return factors

if __name__ == '__main__':
    n = int(input("n = "))
    factors = prime_fact(n)
    print(factors)
