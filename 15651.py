import itertools
import sys

n, m = map(int, sys.stdin.readline().split())
num_list = []
for i in range(1, n + 1):
    num_list.append(i)

for s in itertools.product(num_list, repeat=m):
    for k in range(len(s)):
        print(s[k], end=' ')
    print('')
