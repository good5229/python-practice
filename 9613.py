import itertools
import math
import sys

n = int(sys.stdin.readline().strip())
ans = []
for i in range(n):
    a, *arr = map(int, sys.stdin.readline().split())
    sum = 0
    for s in itertools.permutations(arr, 2):
        sum += math.gcd(s[0], s[1])
    ans.append(int(sum/2))

print(*ans)
