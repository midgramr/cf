from functools import cache
import sys

input = lambda: sys.stdin.readline().rstrip()
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

def sieve(n: int) -> tuple[list[int], set[int]]:
    """Get list of all primes <= n"""
    is_prime = [True] * (n + 1)

    for i in range(2, n + 1):
        if not is_prime[i]:
            continue
        for j in range(i**2, n + 1, i):
            is_prime[j] = False

    primes, prime_set = [], set()
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            prime_set.add(i)

    return primes, prime_set

N = 2 * int(1e5)
primes, prime_set = sieve(N)

@cache
def prime_fact(n: int) -> set[int]:
    if n in prime_set:
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

def solve():
    _, A, _, = II(), LII(), LII()
    prime_facts = set()

    for a in A:
        facts = prime_fact(a)
        for fact in facts:
            # Check whether two numbers
            # already share factors
            if fact in prime_facts:
                return 0
        prime_facts |= facts

    # Consecutive integers don't share common factors
    for a in A:
        facts = prime_fact(a + 1)
        for fact in facts:
            if fact in prime_facts:
                return 1

    return 2

def main():
    T = II()
    for _ in range(T):
        ans = solve()
        print(ans)
main()
