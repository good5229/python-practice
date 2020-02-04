import math
import sys

a, b = map(int, sys.stdin.readline().split())
print(math.gcd(a, b)) ##최대공약수
print(int(a * b / math.gcd(a, b))) ##최소공배수
