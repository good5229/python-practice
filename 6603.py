import itertools
import sys

num = 1
while num != 0:
    num = list(map(int, sys.stdin.readline().split()))
    if num[0] == 0:
        break
    for s in itertools.combinations(num[1:], 6):
        print(' '.join(map(str,s)))
    print('')
