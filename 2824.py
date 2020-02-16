import math
import sys

n = int(sys.stdin.readline().strip())
arr_A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
arr_B = list(map(int, sys.stdin.readline().split()))
A = B = 1
for num_a in arr_A:
    A *= num_a
for num_b in arr_B:
    B *= num_b

gcd = math.gcd(A, B)
print(str(gcd)[-9:])
