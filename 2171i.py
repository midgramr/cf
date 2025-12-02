import sys
import math
from collections.abc import Sequence

input = lambda: sys.stdin.readline().rstrip()
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

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

def solve_quad(a: float, b: float, c: float) -> list[float]:
    template = '(-b {} math.sqrt(b**2 - 4*a*c)) / (2*a)'
    try:
        x1 = eval(template.format('+'))
        x2 = eval(template.format('-'))
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

    convex_hull: Sequence[Point]
    if len(points) == 1:
        return math.pi * r**2 / 2
    elif len(points) == 2:
        convex_hull = points
    else:
        convex_hull = graham_scan(points)

    ans = 0
    for i, (p1x, p1y) in enumerate(convex_hull):
        (p2x, p2y) = convex_hull[i - 1 if i > 0 else -1]

        # NOTE: Need to know whether my circular segment
        # contains all the points

        l: float
        if p2x == p1x:
            # Edge case: vertical line
            x = p1x
            ysqrt = math.sqrt(r**2 - x**2)
            y1, y2 = -ysqrt, ysqrt
            l = y2 - y1

        else:
            # Compute secant line from p1, p2
            m = (p2y - p1y) / (p2x - p1x)
            b = p1y - m * p1x

            # Compute chord endpoints & length
            x1, x2 = solve_quad(m**2 + 1, 2 * m * b, b**2 - r**2)
            y1, y2 = m * x1 + b, m * x2 + b
            l = norm((x2 - x1, y2 - y1))

        # Solve for theta (circular segment angle)
        theta = 2 * math.asin(l / (2 * r))

        # Finally, solve for area of circular segment
        area = r**2 / 2 * (theta - math.sin(theta))

        ans = max(ans, area)

    return ans

def main():
    T = 1
    for _ in range(T):
        ans = solve()
        print(f'{ans:.7f}')
main()
