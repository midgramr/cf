from math import floor, log2
import sys

input = lambda: sys.stdin.readline().rstrip('\n\r ')
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

def solve():
    _ = II()
    a, b = LII(), LII()
    MOD = int(1e6) + 3

    # breakpoint()
    ans = 0
    k = floor(min(log2(bi / ai) for ai, bi in zip(a, b)))
    for j in reversed(range(1, k + 1)):
        next_a = [floor(bi / 2**j) for bi in b]
        ans += sum(aj - ai for aj, ai in zip(next_a, a)) + 1
        a = [ai * 2 for ai in next_a]
    ans += sum(bi - ai for ai, bi in zip(a, b))

    # TODO: compute number of ways

    return ans

def main():
    T = II()
    for _ in range(T):
        ans = solve()
        print(ans)
main()
