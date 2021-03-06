import math
import sys

m, n = map(int, sys.stdin.readline().split())


def isPrime(num):
    if num == 1:
        return False
    n = int(math.sqrt(num))
    for k in range(2, n + 1):
        if num % k == 0:
            return False
    return True


for k in range(m, n + 1):
    if isPrime(k):
        print(k)

        