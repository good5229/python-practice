import sys

n = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().split()))
if len(num) == 1:
    print(max(num) ** 2)
else:
    print(max(num) * min(num))
