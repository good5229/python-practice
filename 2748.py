import datetime
import sys


def pibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return pibonacci(n - 2) + pibonacci(n - 1)


def pibo2(n):
    f = [0 for _ in range(n + 1)]
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


n = int(sys.stdin.readline().strip())
print(datetime.datetime.now())
print(pibonacci(n))
print(datetime.datetime.now())
print(datetime.datetime.now())
print(pibo2(n))
print(datetime.datetime.now())

