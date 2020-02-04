import sys

n, k = map(int, sys.stdin.readline().split())


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if k < 0:
    print("0")
elif k > n:
    print("0")
else:
    ans = factorial(n) / (factorial(k) * factorial(n - k))
    print(int(ans))
