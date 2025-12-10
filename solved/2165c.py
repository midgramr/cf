import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

def solve():
    (n, q), A = LII(), LII()
    A.sort(reverse=True)

    for _ in range(q):
        c = II()
        heap = []
        ans = 0
        # Realistically, this should never iterate through all of A
        # if n >> log2(c), since we can pop at most log(c) bits from c
        i = 0
        while i < n or heap:
            if c == 0:
                break

            cur: int
            if i < n:
                if heap and -heap[0] > A[i]:
                    cur = -heappop(heap)
                else:
                    cur = A[i]
                    i += 1
            else:
                cur = -heappop(heap)

            j = c.bit_length() - 1
            if cur < 1 << j:
                ans += (1 << j) - cur
                c ^= 1 << j
            elif cur < 1 << (j + 1):
                c ^= 1 << j
                heappush(heap, -(cur ^ (1 << j)))
            else:
                # We found a single number that can satisfy all remaining
                # bits in c
                c = 0
                break
        ans += c
        print(ans)

def main():
    T = II()
    for _ in range(T):
        solve()
main()
