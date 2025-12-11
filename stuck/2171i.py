import sys
import math
from math import asin, hypot, sqrt, sin
from collections.abc import Sequence
from functools import cmp_to_key

input = lambda: sys.stdin.readline().rstrip('\n\r ')
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

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

def solve_quad(a: float, b: float, c: float) -> list[float]:
    try:
        x1 = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)
        x2 = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
    except ValueError:
        # If roots are complex, don't return them
        return []
    return [x1, x2] if x1 != x2 else [x1]

def solve():
    n, r = LII()
    points = []
    for _ in range(n):
        x, y = LII()
        points.append((x, y))

    semicircle_area = math.pi * r**2 / 2
    convex_hull = graham_scan(points)
    m = len(convex_hull)

    if m < 3:
        return semicircle_area

    ans = 0
    for i, (p2x, p2y) in enumerate(convex_hull):
        p1x, p1y = convex_hull[i - 1 if i > 0 else -1]
        p3x, p3y = convex_hull[i + 1 if i < m - 1 else 0]

        # Find length of secant line
        l: float
        if p2x == p1x:
            # Edge case: vertical line
            x = p1x

            # Check whether secant line divides all points
            # into the circular segment
            if (p3x >= x) == (x >= 0):
                return semicircle_area

            ysqrt = sqrt(r**2 - x**2)
            y1, y2 = -ysqrt, ysqrt
            l = y2 - y1
        else:
            # Compute secant line from p1, p2
            m = (p2y - p1y) / (p2x - p1x)
            b = p1y - m * p1x

            if (p3y >= m * p3x + b) == (b >= 0):
                return semicircle_area

            # Compute chord endpoints & length
            x1, x2 = solve_quad(m**2 + 1, 2 * m * b, b**2 - r**2)
            y1, y2 = m * x1 + b, m * x2 + b
            l = hypot(x2 - x1, y2 - y1)

        # Solve for theta (circular segment angle)
        theta = 2 * asin(l / (2 * r))

        # Solve for area of circular segment
        segment_area = r**2 / 2 * (theta - sin(theta))

        ans = max(ans, segment_area)

    return ans

def main():
    T = 1
    for _ in range(T):
        ans = solve()
        print(f'{ans:.7f}')
main()
