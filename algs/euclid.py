#!/usr/bin/env pypy3

def euclid(a: int, b: int) -> int:
    if a < b:
        return euclid(b, a)
    if b == 0:
        return a
    return euclid(b, a % b)

def extended_euclid(a: int, b: int) -> tuple[int, int, int]:
    """Returns (gcd(a,b), x, y), where gcd(a,b) = ax + by."""
    if a < b:
        d, x, y = extended_euclid(b, a)
        return d, y, x
    if b == 0:
        return a, 1, 0
    dp, xp, yp = extended_euclid(b, a % b)
    return dp, yp, xp - a // b * yp

print(extended_euclid(2, 9))
