#!/usr/bin/env pypy3

from random import randrange, sample
from bisect import bisect_right
import subprocess
import pdb

MAX = int(10)

t = 1000
for i in range(t):
    x = randrange(1, MAX)
    n, k = randrange(1, x + 1), randrange(1, x + 1)
    a = sample(range(x + 1), n)
    a.sort()

    with open('input.txt', 'w') as f:
        print(1, file=f)
        print(n, k, x, file=f)
        print(' '.join(map(str, a)), file=f)

    out = subprocess.run(
            './build/e < input.txt', shell=True, text=True, capture_output=True)
    out2 = subprocess.run(
            './build/e2 < input.txt', shell=True, text=True, capture_output=True)

    def verify(ans: list[int]) -> list[int]:
        # binary search two closest elements
        res = []
        for p in ans:
            right = bisect_right(a, p)
            left = right - 1
            d = MAX
            if p >= a[left]:
                d = p - a[left]
            if right < len(a):
                d = min(d, a[right] - p)
            res.append(d)
        return list(sorted(res))

    # Each test case has multiple potential solutions
    try:
        ans1 = verify(list(map(int, out.stdout.split())))
        ans2 = verify(list(map(int, out2.stdout.split())))
    except:
        pdb.post_mortem()
    else:
        if (ans1 != ans2):
            print(f'Mismatch on iteration {i}')
            exit(1)

