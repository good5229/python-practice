import math
import sys

n = int(sys.stdin.readline().strip())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    gcd = math.gcd(a, b)
    lcm = int(a * b / math.gcd(a, b))
    print(lcm)
