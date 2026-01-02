from functools import cmp_to_key
import sys

input = lambda: sys.stdin.readline().rstrip('\r\n ')
ii = lambda: int(input())
lii = lambda: list(map(int, input().split()))

def solve(group: list[int], primes: list[int], prime_idx: dict[int, int]):
    n = ii()

    def cmp(x: int, y: int):
        if group[x] < group[y]:
            return -1
        elif group[x] > group[y]:
            return 1
        else:
            # Create product of current and next prime
            p1 = group[x]
            k = prime_idx[p1] + 1
            if k < len(primes):
                p2 = primes[k]
                if x == p1 * p2:
                    return 1
                if y == p1 * p2:
                    return -1
            return -1 if x < y else 1

    a = list(i for i in range(1, n + 1))
    a.sort(key=cmp_to_key(cmp))

    out = []
    i, j = 0, len(a) - 1
    while i < j:
        if i == j - 1:
            out.extend([a[i], a[j]])
            break
        out.extend([a[j], a[i], a[i + 1]])
        i, j = i + 2, j - 1

    return ' '.join(map(str, out))

def main():
    N = 2 * int(1e5)

    # Sieve to get nums grouped by smallest prime factor
    group = [0] * (N + 1)
    group[1] = N
    prime_idx = {}
    primes = []
    for i in range(2, N + 1):
        if group[i]:
            continue
        prime_idx[i] = len(primes)
        primes.append(i)
        group[i] = i
        for j in range(i * i, N + 1, i):
            if group[j]:
                continue
            group[j] = i

    T = ii()

    out = []
    for _ in range(T):
        out.append(solve(group, primes, prime_idx))
    print('\n'.join(out))

main()
