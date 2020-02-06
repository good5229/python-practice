import sys

i = sys.stdin.readline().strip()
sum = 1
for _ in sorted(map(int, sys.stdin.readline().split())):
    print(sum)
    if _ > sum: break
    sum += _
print(sum)
