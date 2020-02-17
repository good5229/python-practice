from math import gcd, sqrt


def solve(a, b):
    c = b // a
    i = int(sqrt(c))
    while i > 0:
        if c % i == 0 and gcd(i, c // i) == 1:
            break
        i -= 1
    return i * a, b // i


num1, num2 = map(int, input().split())
print(*solve(num1, num2))

