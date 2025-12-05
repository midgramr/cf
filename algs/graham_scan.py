#!/usr/bin/env pypy3

from math import hypot
from collections.abc import Sequence
from functools import cmp_to_key

Point = tuple[float, float]

def graham_scan(points: Sequence[Point]) -> Sequence[Point]:
    # Find bottom left point
    p0 = points[0]
    for x, y in points:
        if y < p0[1] or (y == p0[1] and x < p0[0]):
            p0 = (x, y)

    def cross(a: Point, b: Point) -> float:
        (ax, ay), (bx, by) = a, b
        return ax * by - ay * bx

    def cmp_dist(a: Point, b: Point) -> int:
        dist1, dist2 = hypot(*a), hypot(*b)
        if dist1 > dist2:
            return 1
        elif dist1 < dist2:
            return -1
        else:
            return 0

    # Sort points by polar angle with p0
    def cmp(a: Point, b: Point) -> int:
        if a == p0:
            return -1
        if b == p0:
            return 1
        p1 = (a[0] - p0[0], a[1] - p0[1])
        p2 = (b[0] - p0[0], b[1] - p0[1])
        prod = cross(p1, p2)
        if prod > 0:
            return -1
        elif prod < 0:
            return 1
        else:
            return cmp_dist(a, b)

    points = sorted(points, key=cmp_to_key(cmp))

    if len(points) < 3:
        return points

    stk = points[:2]
    for i in range(2, len(points)):
        p3 = points[i]
        while len(stk) > 1:
            p2, p1 = stk[-1], stk[-2]
            # Check whether last 3 points make a left turn
            a = (p2[0] - p1[0], p2[1] - p1[1])
            b = (p3[0] - p2[0], p3[1] - p2[1])
            if cross(a, b) > 0:
                break
            stk.pop()
        stk.append(p3)

    return stk

# points = [(3.0, -3.0), (-3.0, -3.0), (-3.0, 3.0), (3.0, 3.0)]
points = [(9.0, -4.0), (2.0, -2.0), (8.0, 3.0), (0.0, 4.0), (-6.0, 10.0), (6.0, 6.0), (3.0, 5.0)]
# points = [
#     (15, 15),
#     (-4, -1),
#     (0, -1),
#     (2, -9),
#     (0, 2),
#     (8, 1),
#     (3, -3),
#     (-9, 3),
#     (8, 6),
#     (9, 7),
#     (-9, -1),
#     (2, 6),
#     (-2, 7),
#     (-10, -8),
#     (4, 0),
#     (-5, -8),
# ]
# points = [(0, 0), (1, 1), (2, 2), (10, 10), (-1, 1)]
print(graham_scan(points))
