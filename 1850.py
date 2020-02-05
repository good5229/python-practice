import math
import sys

a, b = map(int, sys.stdin.readline().split())
gcd = math.gcd(a, b)
print("1" * gcd)
