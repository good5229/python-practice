from math import gcd, sqrt


def solve(a, b):
    c = b // a
    i = int(sqrt(c))
    while i > 0:
        if c % i == 0 and gcd(i, c // i) == 1:
            break
        i -= 1
    return i * a, b // i


a, b = map(int, input().split())
print(*solve(a, b))
