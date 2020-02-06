import math
import sys


def f(n):
    if n == 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
prime_list = []
d = [i for i in range(n, m + 1) if f(i)]
if len(d) == 0:
    print(-1)
else:
    print(sum(d))
    print(min(d))
