import sys


def f(n):
    if n <= 1:
        return 1
    else:
        return n * f(n - 1)


n = int(sys.stdin.readline().strip())
print(f(n))
