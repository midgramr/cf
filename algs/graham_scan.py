#!/usr/bin/env pypy3

import math
from collections.abc import Sequence

Point = tuple[float, float]

def cross(a: Point, b: Point) -> float:
    (ax, ay), (bx, by) = a, b
    return ax * by - ay * bx

def dot(a: Point, b: Point) -> float:
    (ax, ay), (bx, by) = a, b
    return ax * bx + ay * by

def norm(a: Point) -> float:
    return math.hypot(*a)

def graham_scan(points: Sequence[Point]) -> Sequence[Point]:
    # Find p0
    p0 = points[0]
    for x, y in points:
        if y < p0[1] or (y == p0[1] and x < p0[0]):
            p0 = (x, y)

    # Sort points by angle w.r.t. p0
    def key(a: Point):
        x = (a[0] - p0[0], a[1] - p0[1])
        unit = (1, 0)
        dist = norm(x)
        # Compute -cos(theta) to get monotonically increasing value in [0, pi)
        angle = -dot(unit, x) / dist if dist > 0 else -1
        return (angle, dist)

    candidates = sorted(points, key=key)

    # Remove colinear points w.r.t p0
    points = [candidates[0]]
    n = len(candidates)
    for i in range(1, n):
        a = candidates[i]
        angle, _ = key(a)
        if i < n - 1:
            angle2, _ = key(candidates[i + 1])
            if angle == angle2:
                continue
        points.append(a)

    if len(points) < 3:
        return []

    stk = points[:3]
    for i in range(3, len(points)):
        p = points[i]
        while len(stk) > 2:
            prev1, prev2 = stk[-1], stk[-2]
            # Check whether (prev2 - prev1) and p - prev1 makes a left turn
            a = (prev1[0] - prev2[0], prev1[1] - prev2[1])
            b = (p[0] - prev1[0], p[1] - prev1[1])
            if cross(a, b) > 0:
                break
            stk.pop()
        stk.append(p)

    return stk

# points = [(3.0, -3.0), (-3.0, -3.0), (-3.0, 3.0), (3.0, 3.0)]
# points = [(9.0, -4.0), (2.0, -2.0), (8.0, 3.0), (0.0, 4.0), (-6.0, 10.0), (6.0, 6.0), (3.0, 5.0)]
points = [
    (15, 15),
    (-4, -1),
    (0, -1),
    (2, -9),
    (0, 2),
    (8, 1),
    (3, -3),
    (-9, 3),
    (8, 6),
    (9, 7),
    (-9, -1),
    (2, 6),
    (-2, 7),
    (-10, -8),
    (4, 0),
    (-5, -8),
]
print(graham_scan(points))
