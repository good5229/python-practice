import itertools
import sys

n, k = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()
for s in itertools.combinations(num_list, k):
    for j in s:
        print(j, end=' ')
    print('')
