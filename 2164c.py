import sys
from heapq import heappop, heappush, heapify

input = lambda: sys.stdin.readline().rstrip()
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

def solve():
    _, a, b, c = (LII() for _ in range(4))
    heapify(a)
    monsters = list(sorted(zip(b, c)))
    swords_left, monsters_left, res = [], [], 0
    j = 0

    while a:
        x = heappop(a)
        add_to_left_heap = True
        while j < len(monsters) and x >= monsters[j][0]:
            bi, ci = monsters[j]
            j += 1
            if ci > 0:
                # If we can keep our sword or get a better one, just kill the monster
                res += 1
                if ci > x:
                    # We found a better sword, add back onto our swords heap
                    heappush(a, ci)
                    add_to_left_heap = False
                    break
            else:
                # If we lose our sword by killing the monster, save it for later
                heappush(monsters_left, -bi)
        if add_to_left_heap:
            # Sword has one use left; push onto max-heap
            heappush(swords_left, -x)

    while monsters_left and swords_left:
        monster = -monsters_left[0]
        x = -swords_left[0]
        if x >= monster:
            heappop(swords_left)
            heappop(monsters_left)
            res += 1
        else:
            heappop(monsters_left)

    return res

def main():
    T = II()
    for _ in range(T):
        ans = solve()
        print(ans)
main()
