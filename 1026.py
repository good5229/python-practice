import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

A = sorted(a, reverse=True)
B = sorted(b)
ans = 0
for i in range(n):
    ans += A[i] * B[i]
print(ans)
